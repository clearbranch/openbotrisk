"""Public IP enrichment helpers.

Every source remains a separate feature. Boolean results are nullable: ``True``
means matched, ``False`` means checked and not matched, and ``NA`` means the
source could not be applied. IPv6 is deliberately out of scope for interval
lookups and therefore returns ``NA``, not ``False``.
"""

from __future__ import annotations

import hashlib
import json
import urllib.request
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from ipaddress import collapse_addresses, ip_address, ip_network
from pathlib import Path

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class Snapshot:
    """Provenance for one downloaded source artifact."""

    name: str
    url: str
    path: Path
    sha256: str
    retrieved_at: str | None
    file_mtime: str | None
    source_updated_at: str | None


def artifact_provenance(
    name: str,
    url: str,
    path: str | Path,
    *,
    retrieved_at: str | None = None,
    source_updated_at: str | None = None,
) -> Snapshot:
    """Describe local bytes without treating their mtime as a retrieval time."""
    path = Path(path)
    with path.open("rb") as artifact:
        sha256 = hashlib.file_digest(artifact, "sha256").hexdigest()
    file_mtime = datetime.fromtimestamp(path.stat().st_mtime, UTC).isoformat(timespec="seconds")
    return Snapshot(
        name=name,
        url=url,
        path=path,
        sha256=sha256,
        retrieved_at=retrieved_at,
        file_mtime=file_mtime,
        source_updated_at=source_updated_at,
    )


def snapshot(
    name: str,
    url: str,
    raw_dir: str | Path,
    timeout: int = 120,
    *,
    source_updated_at: str | None = None,
) -> Snapshot:
    """Download an artifact unchanged and append its provenance to a manifest."""
    raw_dir = Path(raw_dir)
    raw_dir.mkdir(parents=True, exist_ok=True)
    data = urllib.request.urlopen(url, timeout=timeout).read()
    path = raw_dir / name
    path.write_bytes(data)
    snap = artifact_provenance(
        name,
        url,
        path,
        retrieved_at=datetime.now(UTC).isoformat(timespec="seconds"),
        source_updated_at=source_updated_at,
    )
    record = {**asdict(snap), "path": str(path)}
    with (raw_dir / "manifest.jsonl").open("a") as manifest:
        manifest.write(json.dumps(record) + "\n")
    return snap


def normalise(ip: object) -> tuple[str | None, int | None, int | None]:
    """Strictly parse an address into canonical text, version, and IPv4 integer."""
    if ip is None or (not isinstance(ip, str) and pd.isna(ip)):
        return (None, None, None)
    try:
        addr = ip_address(str(ip).strip())
    except ValueError:
        return (None, None, None)
    if addr.version == 6 and addr.ipv4_mapped is not None:
        addr = addr.ipv4_mapped
    return (str(addr), addr.version, int(addr) if addr.version == 4 else None)


def ip_frame(ips: object) -> pd.DataFrame:
    """Return one normalized row per input value, retaining order and index."""
    series = pd.Series(ips, dtype="object")
    cache = {value: normalise(value) for value in series.dropna().unique()}
    rows = [
        cache.get(value, (None, None, None)) if isinstance(value, str) else normalise(value)
        for value in series
    ]
    text, version, v4 = zip(*rows, strict=True) if rows else ((), (), ())
    return pd.DataFrame(
        {
            "ip_input": series.to_numpy(dtype=object),
            "ip_normalized": pd.array(text, dtype="string"),
            "ip_version": pd.array(version, dtype="Int8"),
            "v4": pd.array(v4, dtype="UInt32"),
        },
        index=series.index,
    )


def _na_bool(index: pd.Index) -> pd.Series:
    return pd.Series(pd.NA, index=index, dtype="boolean")


class IntervalSet:
    """Sorted, non-overlapping IPv4 intervals built from CIDR networks."""

    def __init__(self, networks: object):
        nets = sorted(collapse_addresses(network for network in networks if network.version == 4))
        self.start = np.array([int(network.network_address) for network in nets], dtype=np.uint64)
        self.end = np.array([int(network.broadcast_address) for network in nets], dtype=np.uint64)
        if len(nets) > 1:
            assert (self.start[1:] > self.end[:-1]).all(), "intervals overlap after collapse"

    @classmethod
    def from_cidr_text(cls, text: str) -> IntervalSet:
        """Build an interval set from a newline-delimited CIDR list."""
        networks = [
            ip_network(line.strip(), strict=False)
            for line in text.splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]
        return cls(networks)

    @classmethod
    def from_file(cls, path: str | Path) -> IntervalSet:
        """Build an interval set from a UTF-8 CIDR-list file."""
        return cls.from_cidr_text(Path(path).read_text())

    def __len__(self) -> int:
        return len(self.start)

    @property
    def addresses(self) -> int:
        """Return the number of distinct addresses represented by the set."""
        return int((self.end - self.start + 1).sum())

    def contains(self, u32: np.ndarray) -> np.ndarray:
        """Return membership for an array of unsigned IPv4 integers."""
        u32 = np.asarray(u32, dtype=np.uint64)
        out = np.zeros(len(u32), dtype=bool)
        if len(self.start) == 0:
            return out
        positions = np.searchsorted(self.start, u32, side="right") - 1
        checkable = positions >= 0
        out[checkable] = u32[checkable] <= self.end[positions[checkable]]
        return out

    def overlap_addresses(self, other: IntervalSet) -> int:
        """Count addresses present in both sets with a two-pointer sweep."""
        left = right = total = 0
        while left < len(self.start) and right < len(other.start):
            lower = max(int(self.start[left]), int(other.start[right]))
            upper = min(int(self.end[left]), int(other.end[right]))
            if lower <= upper:
                total += upper - lower + 1
            if self.end[left] < other.end[right]:
                left += 1
            else:
                right += 1
        return total


def flag_intervals(frame: pd.DataFrame, intervals: IntervalSet | None) -> pd.Series:
    """Flag IPv4 interval matches; return NA for inapplicable or absent data."""
    out = _na_bool(frame.index)
    if intervals is None:
        return out
    mask = (frame["ip_version"] == 4).fillna(False).to_numpy(dtype=bool)
    if mask.any():
        out[mask] = intervals.contains(frame.loc[mask, "v4"].to_numpy(dtype=np.uint64))
    return out


class ListedIPs:
    """Exact-address list whose represented IP versions determine applicability."""

    def __init__(self, addresses: object):
        parsed = [normalise(address) for address in addresses]
        self.addresses = {text for text, _, _ in parsed if text is not None}
        self.versions = {version for _, version, _ in parsed if version is not None}

    @classmethod
    def from_file(cls, path: str | Path) -> ListedIPs:
        """Build an exact-address list from a newline-delimited file."""
        lines = [line.strip() for line in Path(path).read_text().splitlines()]
        return cls(line for line in lines if line and not line.startswith("#"))

    def __len__(self) -> int:
        return len(self.addresses)


def flag_listed(frame: pd.DataFrame, listed: ListedIPs | None) -> pd.Series:
    """Flag exact matches only for IP versions represented by the source."""
    out = _na_bool(frame.index)
    if listed is None:
        return out
    mask = frame["ip_version"].isin(list(listed.versions)).fillna(False).to_numpy(dtype=bool)
    if mask.any():
        out[mask] = frame.loc[mask, "ip_normalized"].isin(listed.addresses).to_numpy(dtype=bool)
    return out


def provider_sets(records: pd.DataFrame, group: str = "provider") -> dict[str, IntervalSet]:
    """Build provider-level IPv4 interval sets from ``all_providers.json`` rows."""
    v4 = records[records["ip_version"] == "IPv4"]
    return {
        name: IntervalSet(ip_network(cidr, strict=False) for cidr in rows["cidr"])
        for name, rows in v4.groupby(group)
    }


def flag_providers(frame: pd.DataFrame, sets: dict[str, IntervalSet] | None) -> pd.Series:
    """Return every matching provider, or NA when the lookup is inapplicable."""
    out = pd.Series([pd.NA] * len(frame), index=frame.index, dtype="object")
    if sets is None:
        return out
    mask = (frame["ip_version"] == 4).fillna(False).to_numpy(dtype=bool)
    if not mask.any():
        return out
    values = frame.loc[mask, "v4"].to_numpy(dtype=np.uint64)
    unique, inverse = np.unique(values, return_inverse=True)
    names = list(sets)
    hits = (
        np.column_stack([sets[name].contains(unique) for name in names])
        if names
        else np.zeros((len(unique), 0), dtype=bool)
    )
    tuples = [tuple(np.array(names)[row]) for row in hits]
    out.loc[mask] = pd.Series(
        [tuples[position] for position in inverse], index=frame.index[mask], dtype="object"
    )
    return out


class RouteTable:
    """IPv4 ranges mapped to origin ASNs; ASN 0 and unmatched inputs yield NA."""

    def __init__(
        self,
        start: object,
        end: object,
        asn: object,
        country: object,
        description: object,
    ):
        order = np.argsort(start)
        self.start = np.asarray(start, dtype=np.uint64)[order]
        self.end = np.asarray(end, dtype=np.uint64)[order]
        self.asn = np.asarray(asn, dtype=np.int64)[order]
        self.country = np.asarray(country, dtype=object)[order]
        self.description = np.asarray(description, dtype=object)[order]
        if len(self.start) > 1:
            assert (self.start[1:] > self.end[:-1]).all(), "route ranges overlap"

    @classmethod
    def from_tsv(cls, path: str | Path) -> RouteTable:
        """Load a five-column IPtoASN-style TSV, optionally compressed."""
        frame = pd.read_csv(
            path,
            sep="\t",
            header=None,
            dtype=str,
            compression="infer",
            names=["start", "end", "asn", "country", "description"],
            keep_default_na=False,
        )
        frame = frame[~frame["start"].str.contains(":", regex=False)]
        return cls(
            frame["start"].map(lambda value: int(ip_address(value))).to_numpy(),
            frame["end"].map(lambda value: int(ip_address(value))).to_numpy(),
            frame["asn"].astype("int64").to_numpy(),
            frame["country"].to_numpy(),
            frame["description"].to_numpy(),
        )

    def lookup(self, frame: pd.DataFrame) -> pd.DataFrame:
        """Look up origin metadata for each normalized input row."""
        length = len(frame)
        asn = pd.array([pd.NA] * length, dtype="Int64")
        name = pd.array([pd.NA] * length, dtype="string")
        country = pd.array([pd.NA] * length, dtype="string")
        mask = (frame["ip_version"] == 4).fillna(False).to_numpy(dtype=bool)
        if mask.any() and len(self.start):
            values = frame.loc[mask, "v4"].to_numpy(dtype=np.uint64)
            positions = np.searchsorted(self.start, values, side="right") - 1
            matched = positions >= 0
            matched[matched] = (values[matched] <= self.end[positions[matched]]) & (
                self.asn[positions[matched]] != 0
            )
            indices = np.flatnonzero(mask)[matched]
            asn[indices] = self.asn[positions[matched]]
            name[indices] = self.description[positions[matched]]
            country[indices] = self.country[positions[matched]]
        return pd.DataFrame(
            {"route_asn": asn, "asn_name": name, "asn_country": country},
            index=frame.index,
        )


def flag_asn_list(route_asn: pd.Series, asns: set[int] | None) -> pd.Series:
    """Flag known ASNs; unknown origins and absent source data yield NA."""
    out = _na_bool(route_asn.index)
    if asns is None:
        return out
    known = route_asn.notna().to_numpy(dtype=bool)
    if known.any():
        out[known] = route_asn[known].astype("int64").isin(list(asns)).to_numpy(dtype=bool)
    return out


def enrich(
    ips: object,
    *,
    route: RouteTable | None = None,
    cloud: dict[str, IntervalSet] | None = None,
    tor: ListedIPs | None = None,
    vpn: IntervalSet | None = None,
    datacentre: IntervalSet | None = None,
    bad_asns: set[int] | None = None,
) -> pd.DataFrame:
    """Return the stable enrichment columns, using NA for every absent source."""
    frame = ip_frame(ips)
    out = frame[["ip_input", "ip_normalized", "ip_version"]].copy()
    if route is not None:
        out = out.join(route.lookup(frame))
    else:
        for column, dtype in (
            ("route_asn", "Int64"),
            ("asn_name", "string"),
            ("asn_country", "string"),
        ):
            out[column] = pd.array([pd.NA] * len(out), dtype=dtype)
    out["cloud_matches"] = flag_providers(frame, cloud)
    out["tor_exit_listed"] = flag_listed(frame, tor)
    out["vpn_listed"] = flag_intervals(frame, vpn)
    out["datacentre_listed"] = flag_intervals(frame, datacentre)
    out["hosting_asn_listed"] = flag_asn_list(out["route_asn"], bad_asns)
    return out
