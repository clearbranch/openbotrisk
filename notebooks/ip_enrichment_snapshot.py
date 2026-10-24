"""Download and profile the mutable IP-enrichment lists used in temp_ips.ipynb."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from dataclasses import asdict, dataclass
from ipaddress import IPv4Network, ip_address, ip_network
from pathlib import Path
from urllib import request

SOURCES = {
    "x4_vpn": ("https://raw.githubusercontent.com/X4BNet/lists_vpn/main/output/vpn/ipv4.txt"),
    "x4_datacenter": (
        "https://raw.githubusercontent.com/X4BNet/lists_vpn/main/output/datacenter/ipv4.txt"
    ),
    "rezmoss_merged_v4": (
        "https://raw.githubusercontent.com/rezmoss/cloud-provider-ip-addresses/"
        "main/all_providers/all_providers_merged_v4.txt"
    ),
    "rezmoss_all_providers": (
        "https://raw.githubusercontent.com/rezmoss/cloud-provider-ip-addresses/"
        "main/all_providers/all_providers.json"
    ),
    "bad_asn_list": (
        "https://raw.githubusercontent.com/brianhama/bad-asn-list/master/bad-asn-list.csv"
    ),
    "tor_bulk_exit_list": "https://check.torproject.org/torbulkexitlist",
}


@dataclass(frozen=True)
class Artifact:
    name: str
    url: str
    path: str
    bytes: int
    sha256: str


def fetch_sources(output_dir: Path) -> list[Artifact]:
    """Save exact response bytes and return a reproducibility manifest."""
    output_dir.mkdir(parents=True, exist_ok=True)
    artifacts = []
    for name, url in SOURCES.items():
        suffix = {
            "rezmoss_all_providers": ".json",
            "bad_asn_list": ".csv",
        }.get(name, ".txt")
        path = output_dir / f"{name}{suffix}"
        with request.urlopen(url, timeout=300) as response:
            data = response.read()
        path.write_bytes(data)
        artifacts.append(
            Artifact(
                name=name,
                url=url,
                path=str(path),
                bytes=len(data),
                sha256=hashlib.sha256(data).hexdigest(),
            )
        )
    return artifacts


def load_ipv4_networks(path: Path) -> list[IPv4Network]:
    """Load a non-overlapping IPv4 CIDR list in address order."""
    networks = sorted(
        (ip_network(line, strict=False) for line in path.read_text().splitlines() if line),
        key=lambda network: int(network.network_address),
    )
    if any(network.version != 4 for network in networks):
        raise ValueError(f"Expected IPv4-only input: {path}")
    if any(left.overlaps(right) for left, right in zip(networks, networks[1:], strict=False)):
        raise ValueError(f"Expected a non-overlapping CIDR list: {path}")
    return networks


def intersection_size(left: list[IPv4Network], right: list[IPv4Network]) -> int:
    """Count addresses in the exact intersection of two disjoint interval lists."""
    i = j = total = 0
    while i < len(left) and j < len(right):
        start = max(int(left[i].network_address), int(right[j].network_address))
        end = min(int(left[i].broadcast_address), int(right[j].broadcast_address))
        if start <= end:
            total += end - start + 1
        if int(left[i].broadcast_address) < int(right[j].broadcast_address):
            i += 1
        else:
            j += 1
    return total


def expanded_text_size(networks: list[IPv4Network]) -> int:
    """Calculate bytes for one dotted IPv4 address plus newline per address."""
    digit_lengths = [len(str(value)) for value in range(256)]
    cycle_sum = sum(digit_lengths)

    def digit_prefix(stop: int, block_size: int) -> int:
        cycle_size = 256 * block_size
        cycles, remainder = divmod(stop, cycle_size)
        total = cycles * block_size * cycle_sum
        values, tail = divmod(remainder, block_size)
        total += block_size * sum(digit_lengths[:values])
        if values < 256:
            total += tail * digit_lengths[values]
        return total

    total = 0
    for network in networks:
        start = int(network.network_address)
        stop = int(network.broadcast_address) + 1
        addresses = stop - start
        digit_bytes = sum(
            digit_prefix(stop, block_size) - digit_prefix(start, block_size)
            for block_size in (256**3, 256**2, 256, 1)
        )
        total += digit_bytes + addresses * 4  # three dots and one newline
    return total


def containment_counts(needles: list[IPv4Network], haystack: list[IPv4Network]) -> tuple[int, int]:
    """Count needle starts, then whole needle networks, contained in haystack."""
    index = starts_inside = fully_inside = 0
    for needle in needles:
        while index < len(haystack) and haystack[index].broadcast_address < needle.network_address:
            index += 1
        if index < len(haystack) and needle.network_address in haystack[index]:
            starts_inside += 1
            if needle.subnet_of(haystack[index]):
                fully_inside += 1
    return starts_inside, fully_inside


def profile_snapshot(output_dir: Path) -> dict:
    """Compute coverage, overlap, provider-row, and bad-ASN diagnostics."""
    paths = {
        "x4_vpn": output_dir / "x4_vpn.txt",
        "x4_datacenter": output_dir / "x4_datacenter.txt",
        "rezmoss_merged_v4": output_dir / "rezmoss_merged_v4.txt",
    }
    networks = {name: load_ipv4_networks(path) for name, path in paths.items()}

    coverage = []
    for name, values in networks.items():
        addresses = sum(network.num_addresses for network in values)
        coverage.append(
            {
                "list": name,
                "networks": len(values),
                "addresses": addresses,
                "pct_of_ipv4": addresses / 2**32 * 100,
            }
        )

    datacenter = networks["x4_datacenter"]
    vpn = networks["x4_vpn"]
    merged = networks["rezmoss_merged_v4"]
    merged_overlap = intersection_size(merged, datacenter)
    vpn_overlap = intersection_size(vpn, datacenter)
    starts_inside, fully_inside = containment_counts(vpn, datacenter)

    providers = json.loads((output_dir / "rezmoss_all_providers.json").read_text())
    ipv4_rows = sum(row["ip_version"] == "IPv4" for row in providers)
    ipv6_rows = sum(row["ip_version"] == "IPv6" for row in providers)

    with (output_dir / "bad_asn_list.csv").open(newline="") as source:
        asn_rows = [int(row["ASN"]) for row in csv.DictReader(source)]
    unique_asns = set(asn_rows)

    tor_addresses = {
        str(ip_address(line.strip()))
        for line in (output_dir / "tor_bulk_exit_list.txt").read_text().splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }

    return {
        "coverage": coverage,
        "overlap": {
            "rezmoss_addresses_in_x4_datacenter": merged_overlap,
            "rezmoss_pct_in_x4_datacenter": merged_overlap
            / sum(network.num_addresses for network in merged)
            * 100,
            "vpn_addresses_in_x4_datacenter": vpn_overlap,
            "vpn_pct_in_x4_datacenter": vpn_overlap
            / sum(network.num_addresses for network in vpn)
            * 100,
            "vpn_network_starts_in_x4_datacenter": starts_inside,
            "vpn_networks_fully_in_x4_datacenter": fully_inside,
        },
        "x4_datacenter_expanded_text_bytes": expanded_text_size(datacenter),
        "rezmoss_rows": {
            "total": len(providers),
            "ipv4": ipv4_rows,
            "ipv6": ipv6_rows,
            "ipv6_pct": ipv6_rows / len(providers) * 100,
        },
        "bad_asn": {
            "rows": len(asn_rows),
            "unique_asns": len(unique_asns),
            "rows_16_bit": sum(asn <= 65_535 for asn in asn_rows),
            "unique_16_bit": sum(asn <= 65_535 for asn in unique_asns),
            "maximum_asn": max(asn_rows),
        },
        "tor_bulk_exit_list": {
            "distinct_addresses": len(tor_addresses),
        },
    }


def run_snapshot(output_dir: Path) -> tuple[list[dict], dict]:
    manifest = [asdict(artifact) for artifact in fetch_sources(output_dir)]
    return manifest, profile_snapshot(output_dir)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()
    manifest, profile = run_snapshot(args.output_dir)
    print(json.dumps({"manifest": manifest, "profile": profile}, indent=2))


if __name__ == "__main__":
    main()
