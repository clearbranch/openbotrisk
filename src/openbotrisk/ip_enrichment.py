"""Public IP enrichment helpers.

Every source remains a separate feature. Boolean results are nullable: ``True``
means matched, ``False`` means checked and not matched, and ``NA`` means the
source could not be applied. IPinfo and detailed provider indexes support IPv4
and IPv6; the community interval lists and route table are explicitly IPv4-only.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import socket
import urllib.request
from bisect import bisect_right
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


def matching_manifest_record(
    records: list[dict[str, object]], name: str, sha256: str
) -> dict[str, object] | None:
    """Return the newest manifest evidence for the exact named artifact bytes."""
    return next(
        (
            record
            for record in reversed(records)
            if record.get("name") == name and record.get("sha256") == sha256
        ),
        None,
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


def normalise_asn(value: object) -> int | None:
    """Return an integer ASN from values such as ``AS13335`` or ``13335``."""
    if value is None or value is pd.NA or isinstance(value, bool):
        return None
    if isinstance(value, (int, np.integer)):
        return int(value) if int(value) > 0 else None
    if isinstance(value, (float, np.floating)):
        if math.isnan(float(value)) or not float(value).is_integer():
            return None
        return int(value) if int(value) > 0 else None
    match = re.fullmatch(r"(?:AS)?\s*(\d+)", str(value).strip(), flags=re.IGNORECASE)
    if match is None:
        return None
    asn = int(match.group(1))
    return asn if asn > 0 else None


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


def _na_object(index: pd.Index) -> pd.Series:
    return pd.Series([pd.NA] * len(index), index=index, dtype="object")


def _clean_text(value: object) -> str | None:
    if value is None or value is pd.NA:
        return None
    if isinstance(value, float) and math.isnan(value):
        return None
    text = str(value).strip()
    return text or None


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


class ProviderTable:
    """Prefix index retaining every rezmoss provider record and its attributes."""

    DETAIL_COLUMNS = ("cidr", "provider", "service", "region", "source_updated_at")

    def __init__(self, records: pd.DataFrame):
        columns = ("cidr", "provider", "service", "region", "last_updated")
        missing = set(columns).difference(records.columns)
        if missing:
            raise ValueError(f"Provider records are missing columns: {sorted(missing)}")

        indexes: dict[int, dict[int, dict[int, dict[tuple[object, ...], dict[str, object]]]]] = {
            4: {},
            6: {},
        }
        for row in records.loc[:, columns].itertuples(index=False, name=None):
            values = dict(zip(columns, row, strict=True))
            network = ip_network(str(values["cidr"]), strict=False)
            detail: dict[str, object] = {
                "cidr": str(network),
                "provider": _clean_text(values["provider"]),
                "service": _clean_text(values["service"]),
                "region": _clean_text(values["region"]),
                "source_updated_at": _clean_text(values["last_updated"]),
            }
            key = tuple(detail[column] for column in self.DETAIL_COLUMNS)
            prefix_index = indexes[network.version].setdefault(network.prefixlen, {})
            matches = prefix_index.setdefault(int(network.network_address), {})
            matches[key] = detail

        self._indexes: dict[int, dict[int, dict[int, tuple[dict[str, object], ...]]]] = {
            version: {
                prefixlen: {
                    start: tuple(rows[key] for key in sorted(rows, key=self._detail_sort_key))
                    for start, rows in networks.items()
                }
                for prefixlen, networks in by_prefix.items()
            }
            for version, by_prefix in indexes.items()
        }
        self.versions = {version for version, index in self._indexes.items() if index}
        self._prefix_lengths = {
            version: sorted(index, reverse=True) for version, index in self._indexes.items()
        }

    @classmethod
    def from_json(cls, path: str | Path) -> ProviderTable:
        """Load the normalized rezmoss ``all_providers.json`` artifact."""
        return cls(pd.read_json(path, convert_dates=False))

    @staticmethod
    def _detail_sort_key(key: tuple[object, ...]) -> tuple[str, ...]:
        return tuple("" if value is None else str(value) for value in key)

    @staticmethod
    def _match_sort_key(match: dict[str, object]) -> tuple[object, ...]:
        prefixlen = ip_network(str(match["cidr"]), strict=False).prefixlen
        return (
            -prefixlen,
            str(match["provider"] or ""),
            str(match["service"] or ""),
            str(match["region"] or ""),
            str(match["cidr"]),
            str(match["source_updated_at"] or ""),
        )

    def _lookup_one(self, text: str) -> tuple[dict[str, object], ...]:
        address = ip_address(text)
        bits = address.max_prefixlen
        address_int = int(address)
        found: dict[tuple[object, ...], dict[str, object]] = {}
        for prefixlen in self._prefix_lengths[address.version]:
            host_bits = bits - prefixlen
            start = (address_int >> host_bits) << host_bits if host_bits else address_int
            for detail in self._indexes[address.version][prefixlen].get(start, ()):
                key = tuple(detail[column] for column in self.DETAIL_COLUMNS)
                found[key] = detail
        return tuple(sorted(found.values(), key=self._match_sort_key))

    def lookup(self, frame: pd.DataFrame) -> pd.Series:
        """Return structured matching rows; unsupported address families remain NA."""
        out = _na_object(frame.index)
        mask = frame["ip_version"].isin(self.versions).fillna(False).to_numpy(dtype=bool)
        if not mask.any():
            return out
        texts = frame.loc[mask, "ip_normalized"].astype(str)
        cache = {text: self._lookup_one(text) for text in texts.unique()}
        out.loc[mask] = pd.Series(
            [cache[text] for text in texts], index=frame.index[mask], dtype="object"
        )
        return out

    def provider_names(self, details: pd.Series) -> pd.Series:
        """Derive the backwards-compatible provider tuple from detailed matches."""
        out = _na_object(details.index)
        known = details.notna()
        out.loc[known] = pd.Series(
            [
                tuple(
                    sorted(
                        {
                            str(match["provider"])
                            for match in matches
                            if match["provider"] is not None
                        }
                    )
                )
                for matches in details.loc[known]
            ],
            index=details.index[known],
            dtype="object",
        )
        return out


class PeeringDBTable:
    """Active PeeringDB network records keyed by normalized ASN."""

    FIELDS = (
        "peeringdb_name",
        "peeringdb_info_types",
        "peeringdb_website",
        "peeringdb_info_scope",
        "peeringdb_updated",
    )
    TYPE_FLAGS = {
        "education_network_reported": "Educational/Research",
        "enterprise_network_reported": "Enterprise",
        "cable_dsl_isp_network_reported": "Cable/DSL/ISP",
    }

    def __init__(self, records: object):
        by_asn: dict[int, dict[str, object]] = {}
        for raw in records:
            if raw.get("status", "ok") != "ok":
                continue
            asn = normalise_asn(raw.get("asn"))
            if asn is None:
                continue
            if asn in by_asn:
                raise ValueError(f"Multiple active PeeringDB records for AS{asn}")
            raw_types = raw.get("info_types")
            if raw_types is None:
                info_types = None
            else:
                if isinstance(raw_types, str):
                    raw_types = [raw_types]
                info_types = tuple(dict.fromkeys(filter(None, map(_clean_text, raw_types))))
            by_asn[asn] = {
                "peeringdb_name": _clean_text(raw.get("name")),
                "peeringdb_info_types": info_types,
                "peeringdb_website": _clean_text(raw.get("website")),
                "peeringdb_info_scope": _clean_text(raw.get("info_scope")),
                "peeringdb_updated": _clean_text(raw.get("updated")),
            }
        self._records = by_asn

    @classmethod
    def from_json(cls, path: str | Path) -> PeeringDBTable:
        """Load a PeeringDB API envelope and retain active network rows."""
        payload = json.loads(Path(path).read_text())
        if not isinstance(payload, dict) or not isinstance(payload.get("data"), list):
            raise ValueError("Expected a PeeringDB API response with a data list")
        return cls(payload["data"])

    def __len__(self) -> int:
        return len(self._records)

    def record_presence(self, asns: pd.Series) -> pd.Series:
        """Report whether a valid ASN has a source record; invalid ASNs remain unknown."""
        result = _na_bool(asns.index)
        for index, value in asns.items():
            asn = normalise_asn(value)
            if asn is not None:
                result.at[index] = asn in self._records
        return result

    def lookup(self, asns: pd.Series) -> pd.DataFrame:
        """Return source-specific metadata; absent ASN records remain unknown."""
        result = pd.DataFrame(index=asns.index)
        for field in self.FIELDS:
            dtype = "object" if field == "peeringdb_info_types" else "string"
            result[field] = pd.Series(pd.NA, index=asns.index, dtype=dtype)
        for flag in self.TYPE_FLAGS:
            result[flag] = _na_bool(asns.index)

        for index, value in asns.items():
            asn = normalise_asn(value)
            record = self._records.get(asn) if asn is not None else None
            if record is None:
                continue
            for field in self.FIELDS:
                result.at[index, field] = record[field]
            info_types = record["peeringdb_info_types"]
            if info_types is not None:
                for flag, category in self.TYPE_FLAGS.items():
                    result.at[index, flag] = category in info_types
        return result


class IPinfoTable:
    """IPinfo Lite IPv4/IPv6 longest-prefix lookup without address expansion."""

    SOURCE_COLUMNS = ("country", "continent", "asn", "as_name", "as_domain")
    OUTPUT_COLUMNS = (
        "ipinfo_country",
        "ipinfo_continent",
        "ipinfo_asn",
        "ipinfo_as_name",
        "ipinfo_as_domain",
    )

    def __init__(self, records: pd.DataFrame):
        required = {"network", *self.SOURCE_COLUMNS}
        missing = required.difference(records.columns)
        if missing:
            raise ValueError(f"IPinfo records are missing columns: {sorted(missing)}")

        metadata = records.loc[:, self.SOURCE_COLUMNS].reset_index(drop=True)
        entries: dict[int, dict[int, list[tuple[int, int]]]] = {4: {}, 6: {}}
        for row_index, cidr in enumerate(records["network"]):
            start, prefixlen, version = self._prefix(str(cidr))
            entries[version].setdefault(prefixlen, []).append((start, row_index))

        self._metadata = metadata
        self._starts: dict[int, dict[int, object]] = {4: {}, 6: {}}
        self._rows: dict[int, dict[int, np.ndarray]] = {4: {}, 6: {}}
        for version, by_prefix in entries.items():
            for prefixlen, rows in by_prefix.items():
                rows.sort(key=lambda item: (item[0], item[1]))
                starts = [row[0] for row in rows]
                if any(left == right for left, right in zip(starts, starts[1:], strict=False)):
                    raise ValueError(f"Duplicate IPinfo IPv{version} /{prefixlen} networks")
                self._starts[version][prefixlen] = (
                    np.asarray(starts, dtype=np.uint64) if version == 4 else starts
                )
                self._rows[version][prefixlen] = np.asarray(
                    [row[1] for row in rows], dtype=np.int64
                )
        self.versions = {version for version, index in self._starts.items() if index}
        self._prefix_lengths = {
            version: sorted(index, reverse=True) for version, index in self._starts.items()
        }

    @classmethod
    def from_parquet(cls, path: str | Path) -> IPinfoTable:
        """Load only the IPinfo Lite fields used by the enrichment output."""
        columns = ["network", *cls.SOURCE_COLUMNS]
        return cls(pd.read_parquet(path, columns=columns))

    @staticmethod
    def _prefix(cidr: str) -> tuple[int, int, int]:
        if "/" in cidr:
            address_text, prefix_text = cidr.rsplit("/", 1)
        else:
            address_text = cidr
            prefix_text = "128" if ":" in address_text else "32"
        family = socket.AF_INET6 if ":" in address_text else socket.AF_INET
        version = 6 if family == socket.AF_INET6 else 4
        bits = 128 if version == 6 else 32
        prefixlen = int(prefix_text)
        if not 0 <= prefixlen <= bits:
            raise ValueError(f"Invalid IPv{version} prefix length in {cidr}")
        address_int = int.from_bytes(socket.inet_pton(family, address_text), "big")
        host_bits = bits - prefixlen
        start = (address_int >> host_bits) << host_bits if host_bits else address_int
        return start, prefixlen, version

    def __len__(self) -> int:
        return len(self._metadata)

    def _row_for_address(self, text: str) -> int | None:
        address = ip_address(text)
        version = address.version
        if version not in self.versions:
            return None
        value = int(address)
        bits = address.max_prefixlen
        for prefixlen in self._prefix_lengths[version]:
            host_bits = bits - prefixlen
            start = (value >> host_bits) << host_bits if host_bits else value
            starts = self._starts[version][prefixlen]
            if version == 4:
                position = int(np.searchsorted(starts, start, side="left"))
            else:
                position = bisect_right(starts, start) - 1
            if position >= 0 and position < len(starts) and int(starts[position]) == start:
                return int(self._rows[version][prefixlen][position])
        return None

    def lookup(self, frame: pd.DataFrame) -> pd.DataFrame:
        """Look up IPinfo fields without converting country into ASN geography."""
        result = pd.DataFrame(index=frame.index)
        for column in self.OUTPUT_COLUMNS:
            dtype = "Int64" if column == "ipinfo_asn" else "string"
            result[column] = pd.Series(pd.NA, index=frame.index, dtype=dtype)

        mask = frame["ip_version"].isin(self.versions).fillna(False).to_numpy(dtype=bool)
        if not mask.any():
            return result
        texts = frame.loc[mask, "ip_normalized"].astype(str)
        cache = {text: self._row_for_address(text) for text in texts.unique()}
        for index, text in texts.items():
            row_index = cache[text]
            if row_index is None:
                continue
            source = self._metadata.iloc[row_index]
            result.at[index, "ipinfo_country"] = _clean_text(source["country"])
            result.at[index, "ipinfo_continent"] = _clean_text(source["continent"])
            result.at[index, "ipinfo_asn"] = normalise_asn(source["asn"])
            result.at[index, "ipinfo_as_name"] = _clean_text(source["as_name"])
            result.at[index, "ipinfo_as_domain"] = _clean_text(source["as_domain"])
        return result


class ASdbTable:
    """Stanford ASdb multi-label industry categories keyed by normalized ASN."""

    OUTPUT_COLUMNS = (
        "asdb_category_pairs",
        "asdb_layer1_categories",
        "asdb_layer2_categories",
    )

    def __init__(self, records: pd.DataFrame):
        if "ASN" not in records.columns:
            raise ValueError("ASdb records require an ASN column")
        numbered: dict[int, dict[int, str]] = {}
        for column in records.columns:
            match = re.fullmatch(r"Category (\d+) - Layer ([12])", column)
            if match:
                numbered.setdefault(int(match.group(1)), {})[int(match.group(2))] = column
        pairs = [numbered[number] for number in sorted(numbered) if 1 in numbered[number]]
        if not pairs:
            raise ValueError("ASdb records contain no numbered category columns")

        columns = ["ASN", *(column for pair in pairs for column in pair.values())]
        positions = {column: index for index, column in enumerate(columns)}
        by_asn: dict[int, tuple[dict[str, str | None], ...]] = {}
        for row in records.loc[:, columns].itertuples(index=False, name=None):
            asn = normalise_asn(row[positions["ASN"]])
            if asn is None:
                continue
            found: dict[tuple[str | None, str | None], dict[str, str | None]] = {}
            for pair in pairs:
                layer1 = _clean_text(row[positions[pair[1]]])
                layer2 = _clean_text(row[positions[pair[2]]]) if 2 in pair else None
                if layer1 is None and layer2 is None:
                    continue
                key = (layer1, layer2)
                found[key] = {"layer1": layer1, "layer2": layer2}
            by_asn[asn] = tuple(found.values())
        self._records = by_asn

    @classmethod
    def from_csv(cls, path: str | Path) -> ASdbTable:
        """Load the wide categorized-AS CSV without assuming a category count."""
        return cls(pd.read_csv(path, dtype=str))

    def __len__(self) -> int:
        return len(self._records)

    def record_presence(self, asns: pd.Series) -> pd.Series:
        """Report whether a valid ASN has a source record; invalid ASNs remain unknown."""
        result = _na_bool(asns.index)
        for index, value in asns.items():
            asn = normalise_asn(value)
            if asn is not None:
                result.at[index] = asn in self._records
        return result

    def lookup(self, asns: pd.Series) -> pd.DataFrame:
        """Return all supplied category pairs; no category reconciliation is applied."""
        result = pd.DataFrame(index=asns.index)
        for column in self.OUTPUT_COLUMNS:
            result[column] = _na_object(asns.index)
        for index, value in asns.items():
            asn = normalise_asn(value)
            pairs = self._records.get(asn) if asn is not None else None
            if pairs is None:
                continue
            layer1 = tuple(dict.fromkeys(pair["layer1"] for pair in pairs if pair["layer1"]))
            layer2 = tuple(dict.fromkeys(pair["layer2"] for pair in pairs if pair["layer2"]))
            result.at[index, "asdb_category_pairs"] = pairs
            result.at[index, "asdb_layer1_categories"] = layer1
            result.at[index, "asdb_layer2_categories"] = layer2
        return result


def asn_agreement(left: pd.Series, right: pd.Series) -> pd.Series:
    """Compare normalized ASNs only where both sources supplied a value."""
    out = _na_bool(left.index)
    left_values = left.map(normalise_asn)
    right_values = right.map(normalise_asn)
    known = left_values.notna() & right_values.notna()
    out.loc[known] = (
        left_values.loc[known].astype("int64").to_numpy()
        == right_values.loc[known].astype("int64").to_numpy()
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
    cloud: dict[str, IntervalSet] | ProviderTable | None = None,
    peeringdb: PeeringDBTable | None = None,
    ipinfo: IPinfoTable | None = None,
    asdb: ASdbTable | None = None,
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

    if isinstance(cloud, ProviderTable):
        details = cloud.lookup(frame)
        out["cloud_matches"] = cloud.provider_names(details)
        out["cloud_match_details"] = details
    else:
        out["cloud_matches"] = flag_providers(frame, cloud)
        out["cloud_match_details"] = _na_object(out.index)

    if ipinfo is not None:
        out = out.join(ipinfo.lookup(frame))
    else:
        for column in IPinfoTable.OUTPUT_COLUMNS:
            dtype = "Int64" if column == "ipinfo_asn" else "string"
            out[column] = pd.Series(pd.NA, index=out.index, dtype=dtype)
    out["route_ipinfo_asn_agree"] = asn_agreement(out["route_asn"], out["ipinfo_asn"])

    if peeringdb is not None:
        out = out.join(peeringdb.lookup(out["route_asn"]))
    else:
        for column in PeeringDBTable.FIELDS:
            dtype = "object" if column == "peeringdb_info_types" else "string"
            out[column] = pd.Series(pd.NA, index=out.index, dtype=dtype)
        for column in PeeringDBTable.TYPE_FLAGS:
            out[column] = _na_bool(out.index)

    if asdb is not None:
        out = out.join(asdb.lookup(out["route_asn"]))
    else:
        for column in ASdbTable.OUTPUT_COLUMNS:
            out[column] = _na_object(out.index)

    out["tor_exit_listed"] = flag_listed(frame, tor)
    out["vpn_listed"] = flag_intervals(frame, vpn)
    out["datacentre_listed"] = flag_intervals(frame, datacentre)
    out["hosting_asn_listed"] = flag_asn_list(out["route_asn"], bad_asns)
    return out
