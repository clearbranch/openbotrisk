import hashlib
from ipaddress import ip_address

import numpy as np
import pandas as pd
import pytest

from openbotrisk.ip_enrichment import (
    IntervalSet,
    ListedIPs,
    RouteTable,
    artifact_provenance,
    enrich,
    flag_asn_list,
    flag_intervals,
    flag_listed,
    flag_providers,
    ip_frame,
    normalise,
    provider_sets,
)


def frame(*ips):
    return ip_frame(list(ips))


def test_local_artifact_does_not_invent_a_retrieval_time(tmp_path):
    path = tmp_path / "local.tsv.gz"
    path.write_bytes(b"local source bytes")

    provenance = artifact_provenance("local.tsv.gz", "https://example.test/local.tsv.gz", path)

    assert provenance.retrieved_at is None
    assert provenance.file_mtime is not None
    assert provenance.source_updated_at is None
    expected_sha256 = hashlib.sha256(b"local source bytes").hexdigest()
    assert provenance.sha256 == expected_sha256


@pytest.mark.parametrize(
    "raw",
    ["not an ip", "1.2.3.4:443", "1.2.3.0/24", "", "  ", "01.2.3.4", None, np.nan, pd.NA],
)
def test_unparseable_is_none(raw):
    assert normalise(raw) == (None, None, None)


def test_ipv4_mapped_is_normalised_to_ipv4():
    expected = 34 * 2**24 + 82 * 2**16 + 1 * 2**8 + 5
    assert normalise("::ffff:34.82.1.5") == ("34.82.1.5", 4, expected)


def test_ipv6_has_no_v4_integer():
    assert normalise("2001:db8::1") == ("2001:db8::1", 6, None)


def test_whitespace_is_stripped():
    assert normalise(" 8.8.8.8 ")[0] == "8.8.8.8"


def test_interval_boundaries():
    intervals = IntervalSet.from_cidr_text("10.0.0.0/24\n")
    inputs = frame("9.255.255.255", "10.0.0.0", "10.0.0.255", "10.0.1.0")
    assert flag_intervals(inputs, intervals).tolist() == [False, True, True, False]


def test_single_address_network():
    intervals = IntervalSet.from_cidr_text("1.2.3.4/32")
    result = flag_intervals(frame("1.2.3.3", "1.2.3.4", "1.2.3.5"), intervals)
    assert result.tolist() == [False, True, False]


def test_overlap_and_duplicates_are_collapsed():
    intervals = IntervalSet.from_cidr_text("10.0.0.0/16\n10.0.5.0/24\n10.0.5.0/24\n")
    assert len(intervals) == 1
    assert intervals.addresses == 65536


def test_comments_blank_lines_and_ipv6_lines_skipped():
    intervals = IntervalSet.from_cidr_text("# header\n\n10.0.0.0/8\n2001:db8::/32\n")
    assert len(intervals) == 1


def test_empty_set_matches_nothing():
    assert flag_intervals(frame("1.1.1.1"), IntervalSet([])).tolist() == [False]


def test_ipv6_invalid_and_null_are_na_not_false():
    intervals = IntervalSet.from_cidr_text("10.0.0.0/8")
    result = flag_intervals(frame("2001:db8::1", "junk", None), intervals)
    assert result.isna().all()


def test_source_not_loaded_is_na():
    assert flag_intervals(frame("10.0.0.1"), None).isna().all()


def test_mapped_ipv6_is_checked_as_ipv4():
    intervals = IntervalSet.from_cidr_text("34.82.0.0/16")
    assert flag_intervals(frame("::ffff:34.82.1.5"), intervals).tolist() == [True]


def test_private_and_reserved_space_is_just_unlisted():
    intervals = IntervalSet.from_cidr_text("52.0.0.0/8")
    result = flag_intervals(frame("10.0.0.1", "127.0.0.1", "192.168.1.1"), intervals)
    assert result.tolist() == [False, False, False]


def test_overlap_addresses():
    left = IntervalSet.from_cidr_text("10.0.0.0/24\n10.0.2.0/24")
    right = IntervalSet.from_cidr_text("10.0.0.128/25\n10.0.1.0/24\n10.0.2.0/23")
    assert left.overlap_addresses(right) == 128 + 256
    assert left.overlap_addresses(IntervalSet([])) == 0


def test_listed_ips_ipv4_only_list_gives_na_for_ipv6():
    listed = ListedIPs(["1.2.3.4", "5.6.7.8"])
    result = flag_listed(frame("1.2.3.4", "1.2.3.5", "2001:db8::1"), listed)
    assert result.iloc[0]
    assert not result.iloc[1]
    assert pd.isna(result.iloc[2])


def test_listed_ips_with_ipv6_entries_checks_ipv6():
    listed = ListedIPs(["1.2.3.4", "2001:db8::1"])
    result = flag_listed(frame("2001:db8::1", "2001:db8::2"), listed)
    assert result.tolist() == [True, False]


def test_overlapping_providers_return_all_matches():
    records = pd.DataFrame(
        {
            "cidr": ["10.0.0.0/8", "10.1.0.0/16", "2001:db8::/32"],
            "ip_version": ["IPv4", "IPv4", "IPv6"],
            "provider": ["a", "b", "a"],
        }
    )
    result = flag_providers(
        frame("10.1.2.3", "10.9.9.9", "11.0.0.1", "2001:db8::1"),
        provider_sets(records),
    )
    assert result.iloc[0] == ("a", "b")
    assert result.iloc[1] == ("a",)
    assert result.iloc[2] == ()
    assert pd.isna(result.iloc[3])


def test_repeated_addresses_get_identical_results():
    records = pd.DataFrame({"cidr": ["10.0.0.0/8"], "ip_version": ["IPv4"], "provider": ["a"]})
    result = flag_providers(frame("10.0.0.1", "11.0.0.1", "10.0.0.1"), provider_sets(records))
    assert list(result) == [("a",), (), ("a",)]


def make_route():
    return RouteTable(
        start=[int(ip_address("1.0.0.0")), int(ip_address("1.0.1.0")), int(ip_address("1.0.3.0"))],
        end=[
            int(ip_address("1.0.0.255")),
            int(ip_address("1.0.1.255")),
            int(ip_address("1.0.3.255")),
        ],
        asn=[13335, 0, 64500],
        country=["AU", "None", "GB"],
        description=["CLOUDFLARENET", "Not routed", "EXAMPLE-AS"],
    )


def test_route_lookup_gap_asn0_and_v6():
    result = make_route().lookup(
        frame("1.0.0.7", "1.0.1.7", "1.0.2.7", "1.0.3.255", "0.0.0.1", "2001:db8::1")
    )
    assert result["route_asn"].tolist()[0] == 13335
    assert result["route_asn"].isna().tolist() == [False, True, True, False, True, True]
    assert result["asn_name"].iloc[3] == "EXAMPLE-AS"


def test_route_overlap_is_rejected():
    with pytest.raises(AssertionError):
        RouteTable([0, 5], [10, 20], [1, 2], ["x", "y"], ["a", "b"])


def test_asn_list_na_for_unknown_asn():
    asn = pd.Series(pd.array([13335, pd.NA, 64500], dtype="Int64"))
    result = flag_asn_list(asn, {64500})
    assert not result.iloc[0]
    assert result.iloc[2]
    assert pd.isna(result.iloc[1])


def test_enrich_always_has_every_column_and_missing_sources_are_na():
    result = enrich(["8.8.8.8", "junk"])
    for column in [
        "route_asn",
        "cloud_matches",
        "tor_exit_listed",
        "vpn_listed",
        "datacentre_listed",
        "hosting_asn_listed",
    ]:
        assert column in result
        assert result[column].isna().all()


def test_enrich_distinguishes_checked_negative_from_unavailable():
    vpn = IntervalSet.from_cidr_text("10.0.0.0/8")
    result = enrich(["11.0.0.1", "2001:db8::1", "junk"], vpn=vpn, tor=None)

    assert result["vpn_listed"].iloc[0] == False  # noqa: E712
    assert result["vpn_listed"].iloc[1:].isna().all()
    assert result["tor_exit_listed"].isna().all()
