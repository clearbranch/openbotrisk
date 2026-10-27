import hashlib
from ipaddress import ip_address

import numpy as np
import pandas as pd
import pytest

from openbotrisk.ip_enrichment import (
    ASdbTable,
    IntervalSet,
    IPinfoTable,
    ListedIPs,
    PeeringDBTable,
    ProviderTable,
    RouteTable,
    artifact_provenance,
    asn_agreement,
    enrich,
    flag_asn_list,
    flag_intervals,
    flag_listed,
    flag_providers,
    ip_frame,
    matching_manifest_record,
    normalise,
    normalise_asn,
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


def test_manifest_evidence_requires_name_and_hash_and_uses_newest_match():
    records = [
        {"name": "source.csv", "sha256": "right", "retrieved_at": "first"},
        {"name": "source.csv", "sha256": "wrong", "retrieved_at": "wrong bytes"},
        {"name": "other.csv", "sha256": "right", "retrieved_at": "wrong name"},
        {"name": "source.csv", "sha256": "right", "retrieved_at": "newest"},
    ]
    match = matching_manifest_record(records, "source.csv", "right")
    assert match is not None
    assert match["retrieved_at"] == "newest"
    assert matching_manifest_record(records, "source.csv", "missing") is None


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


@pytest.mark.parametrize(
    ("raw", "expected"),
    [("AS13335", 13335), ("as 13335", 13335), (13335, 13335), (13335.0, 13335)],
)
def test_asn_normalisation(raw, expected):
    assert normalise_asn(raw) == expected


@pytest.mark.parametrize("raw", [None, pd.NA, np.nan, 0, "AS0", "AS12.5", "not-an-asn"])
def test_invalid_or_unavailable_asn_is_none(raw):
    assert normalise_asn(raw) is None


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


def test_provider_details_retain_overlaps_relationships_and_remove_exact_duplicates():
    records = pd.DataFrame(
        {
            "cidr": ["10.0.0.0/8", "10.1.0.0/16", "10.1.0.0/16", "2001:db8::/32"],
            "provider": ["broad", "specific", "specific", "v6-provider"],
            "service": ["compute", "relay", "relay", "edge"],
            "region": ["global", "eu-west", "eu-west", "global"],
            "last_updated": ["2026-01-01", "2026-01-02", "2026-01-02", "2026-01-03"],
        }
    )
    providers = ProviderTable(records)
    details = providers.lookup(frame("10.1.0.0", "10.1.255.255", "10.2.0.1", "2001:db8::1"))

    assert len(details.iloc[0]) == 2
    assert details.iloc[0][0] == {
        "cidr": "10.1.0.0/16",
        "provider": "specific",
        "service": "relay",
        "region": "eu-west",
        "source_updated_at": "2026-01-02",
    }
    assert details.iloc[0] == details.iloc[1]
    assert [match["provider"] for match in details.iloc[2]] == ["broad"]
    assert [match["provider"] for match in details.iloc[3]] == ["v6-provider"]
    assert providers.provider_names(details).iloc[0] == ("broad", "specific")


def test_provider_details_are_na_for_unsupported_or_invalid_inputs():
    providers = ProviderTable(
        pd.DataFrame(
            {
                "cidr": ["10.0.0.0/8"],
                "provider": ["v4"],
                "service": [""],
                "region": [""],
                "last_updated": ["2026-01-01"],
            }
        )
    )
    result = providers.lookup(frame("11.0.0.1", "2001:db8::1", "junk"))
    assert result.iloc[0] == ()
    assert result.iloc[1:].isna().all()


def test_peeringdb_missing_types_and_multi_category_semantics():
    table = PeeringDBTable(
        [
            {
                "asn": "AS64500",
                "name": "Campus and enterprise network",
                "info_types": ["Educational/Research", "Enterprise"],
                "website": "https://example.test",
                "info_scope": "Regional",
                "updated": "2026-01-01T00:00:00Z",
                "status": "ok",
            },
            {"asn": 64501, "name": "Unclassified", "info_types": [], "status": "ok"},
            {"asn": 64502, "name": "Types unavailable", "info_types": None, "status": "ok"},
            {"asn": 64503, "name": "Deleted", "info_types": ["Enterprise"], "status": "deleted"},
        ]
    )
    result = table.lookup(pd.Series(pd.array([64500, 64501, 64502, 64503], dtype="Int64")))

    assert result.loc[0, "peeringdb_info_types"] == ("Educational/Research", "Enterprise")
    assert result.loc[0, "education_network_reported"] == True  # noqa: E712
    assert result.loc[0, "enterprise_network_reported"] == True  # noqa: E712
    assert result.loc[0, "cable_dsl_isp_network_reported"] == False  # noqa: E712
    assert result.loc[1, "peeringdb_info_types"] == ()
    assert result.loc[1, list(PeeringDBTable.TYPE_FLAGS)].eq(False).all()
    assert result.loc[2, list(PeeringDBTable.TYPE_FLAGS)].isna().all()
    assert result.loc[3].isna().all()
    assert table.record_presence(pd.Series([64500, 64501, 64503, pd.NA])).tolist() == [
        True,
        True,
        False,
        pd.NA,
    ]


def make_ipinfo():
    return IPinfoTable(
        pd.DataFrame(
            {
                "network": ["1.0.0.0/24", "1.0.3.0/24", "2001:db8::/126"],
                "country": ["Australia", "United Kingdom", "Documentation"],
                "continent": ["Oceania", "Europe", "Documentation"],
                "asn": ["AS13335", 64501, "AS64502"],
                "as_name": ["Cloudflare", "Example", "Example v6"],
                "as_domain": ["cloudflare.com", "example.test", "v6.example.test"],
            }
        )
    )


def test_ipinfo_cidr_boundaries_gaps_and_ipv6():
    result = make_ipinfo().lookup(
        frame("1.0.0.0", "1.0.0.255", "1.0.1.0", "2001:db8::", "2001:db8::3", "2001:db8::4")
    )
    assert result["ipinfo_asn"].tolist()[:2] == [13335, 13335]
    assert pd.isna(result.loc[2, "ipinfo_asn"])
    assert result.loc[3, "ipinfo_asn"] == 64502
    assert result.loc[4, "ipinfo_asn"] == 64502
    assert pd.isna(result.loc[5, "ipinfo_asn"])


def test_asn_agreement_only_exists_when_both_sources_have_an_asn():
    left = pd.Series(pd.array(["AS13335", 64500, pd.NA, 64502], dtype="object"))
    right = pd.Series(pd.array([13335, "AS64501", 64500, pd.NA], dtype="object"))
    result = asn_agreement(left, right)
    assert result.tolist()[:2] == [True, False]
    assert result.iloc[2:].isna().all()


def test_asdb_preserves_multiple_category_pairs_and_normalises_asn():
    table = ASdbTable(
        pd.DataFrame(
            {
                "ASN": ["AS64500"],
                "Category 1 - Layer 1": ["Education"],
                "Category 1 - Layer 2": ["University"],
                "Category 2 - Layer 1": ["Technology"],
                "Category 2 - Layer 2": ["ISP"],
                "Category 3 - Layer 1": ["Education"],
                "Category 3 - Layer 2": ["University"],
            }
        )
    )
    result = table.lookup(pd.Series(pd.array([64500, 64501], dtype="Int64")))
    assert result.loc[0, "asdb_category_pairs"] == (
        {"layer1": "Education", "layer2": "University"},
        {"layer1": "Technology", "layer2": "ISP"},
    )
    assert result.loc[0, "asdb_layer1_categories"] == ("Education", "Technology")
    assert pd.isna(result.loc[1, "asdb_category_pairs"])
    assert table.record_presence(pd.Series([64500, 64501, pd.NA])).tolist() == [
        True,
        False,
        pd.NA,
    ]


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


def test_route_ipv6_boundaries_and_high_64_bits():
    first_start = int(ip_address("2001:db8:1::"))
    first_end = int(ip_address("2001:db8:1::ffff"))
    second_start = int(ip_address("3001:db8:1::"))
    second_end = int(ip_address("3001:db8:1::ffff"))
    route = RouteTable(
        [first_start, second_start],
        [first_end, second_end],
        [64510, 64511],
        ["GB", "US"],
        ["FIRST-V6", "SECOND-V6"],
        version=[6, 6],
    )

    result = route.lookup(
        frame(
            str(ip_address(first_start - 1)),
            str(ip_address(first_start)),
            str(ip_address(first_end)),
            str(ip_address(first_end + 1)),
            "3001:db8:1::1234",
        )
    )

    assert result["route_asn"].isna().tolist() == [True, False, False, True, False]
    assert result.loc[[1, 2, 4], "route_asn"].tolist() == [64510, 64510, 64511]
    assert result.loc[1, "asn_name"] == "FIRST-V6"
    assert result.loc[4, "asn_country"] == "US"


def test_route_keeps_ipv4_and_ipv6_numeric_spaces_separate_and_maps_v4_mapped_ipv6():
    route = RouteTable(
        [1, 1],
        [1, 1],
        [64500, 64501],
        ["v4", "v6"],
        ["IPV4", "IPV6"],
        version=[4, 6],
    )

    result = route.lookup(frame("0.0.0.1", "::1", "::ffff:0.0.0.1"))

    assert result["route_asn"].tolist() == [64500, 64501, 64500]
    assert result["asn_name"].tolist() == ["IPV4", "IPV6", "IPV4"]


def test_route_tsv_retains_both_families_and_treats_asn_zero_as_unknown(tmp_path):
    path = tmp_path / "combined.tsv"
    path.write_text(
        "1.0.0.0\t1.0.0.255\t13335\tAU\tV4-AS\n"
        "2001:db8::\t2001:db8::ff\t64502\tGB\tV6-AS\n"
        "2001:db8:1::\t2001:db8:1::ff\t0\tNone\tNot routed\n"
    )

    route = RouteTable.from_tsv(path)
    result = route.lookup(frame("1.0.0.7", "2001:db8::7", "2001:db8:1::7", "2001:db8:2::1"))

    assert route.version.tolist() == [4, 6, 6]
    assert result["route_asn"].isna().tolist() == [False, False, True, True]
    assert result.loc[:1, "route_asn"].tolist() == [13335, 64502]


def test_ipv6_route_enables_asn_downstream_joins_but_not_ipv4_only_lists():
    route = RouteTable(
        [int(ip_address("2001:db8::"))],
        [int(ip_address("2001:db8::3"))],
        [64502],
        ["GB"],
        ["V6-EXAMPLE"],
        version=[6],
    )
    peeringdb = PeeringDBTable(
        [
            {
                "asn": 64502,
                "name": "IPv6 example network",
                "info_types": ["Educational/Research", "Cable/DSL/ISP"],
            }
        ]
    )
    asdb = ASdbTable(
        pd.DataFrame(
            {
                "ASN": ["AS64502"],
                "Category 1 - Layer 1": ["Education"],
                "Category 1 - Layer 2": ["Research"],
            }
        )
    )
    v4_only = IntervalSet.from_cidr_text("10.0.0.0/8")

    result = enrich(
        ["2001:db8::1", "2001:db8:2::1"],
        route=route,
        ipinfo=make_ipinfo(),
        peeringdb=peeringdb,
        asdb=asdb,
        bad_asns={64502},
        vpn=v4_only,
        datacentre=v4_only,
    )

    assert result.loc[0, "route_asn"] == 64502
    assert result.loc[0, "asn_name"] == "V6-EXAMPLE"
    assert result.loc[0, "asn_country"] == "GB"
    assert result.loc[0, "route_ipinfo_asn_agree"] == True  # noqa: E712
    assert result.loc[0, "hosting_asn_listed"] == True  # noqa: E712
    assert result.loc[0, "education_network_reported"] == True  # noqa: E712
    assert result.loc[0, "cable_dsl_isp_network_reported"] == True  # noqa: E712
    assert result.loc[0, "asdb_layer1_categories"] == ("Education",)
    assert result.loc[:, ["vpn_listed", "datacentre_listed"]].isna().all().all()
    assert result.loc[1, ["route_asn", "hosting_asn_listed", "peeringdb_name"]].isna().all()


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


def test_enrich_preserves_duplicate_input_index_with_optional_metadata_sources():
    ips = pd.Series(["1.0.0.7", "2001:db8::1"], index=pd.Index([7, 7], name="event"))
    route = RouteTable(
        [int(ip_address("1.0.0.0")), int(ip_address("2001:db8::"))],
        [int(ip_address("1.0.0.255")), int(ip_address("2001:db8::3"))],
        [13335, 64502],
        ["AU", "GB"],
        ["CLOUDFLARENET", "V6-EXAMPLE"],
        version=[4, 6],
    )
    cloud = ProviderTable(
        pd.DataFrame(
            {
                "cidr": ["1.0.0.0/24", "2001:db8::/126"],
                "provider": ["v4-provider", "v6-provider"],
                "service": [None, None],
                "region": [None, None],
                "last_updated": [None, None],
            }
        )
    )
    peeringdb = PeeringDBTable(
        [
            {"asn": 13335, "name": "IPv4 network", "info_types": ["Content"]},
            {"asn": 64502, "name": "IPv6 network", "info_types": ["Educational/Research"]},
        ]
    )
    asdb = ASdbTable(
        pd.DataFrame(
            {
                "ASN": ["AS13335", "AS64502"],
                "Category 1 - Layer 1": ["Technology", "Education"],
                "Category 1 - Layer 2": ["Hosting", "Research"],
            }
        )
    )
    v4_only = IntervalSet.from_cidr_text("1.0.0.0/24")

    result = enrich(
        ips,
        route=route,
        cloud=cloud,
        peeringdb=peeringdb,
        ipinfo=make_ipinfo(),
        asdb=asdb,
        tor=ListedIPs(ips),
        vpn=v4_only,
        datacentre=v4_only,
        bad_asns={13335, 64502},
    )

    assert len(result) == len(ips)
    pd.testing.assert_index_equal(result.index, ips.index, exact=True)
    assert result["ip_input"].tolist() == ips.tolist()
    assert result["route_asn"].tolist() == [13335, 64502]
    assert result["cloud_matches"].tolist() == [("v4-provider",), ("v6-provider",)]
    assert result["peeringdb_name"].tolist() == ["IPv4 network", "IPv6 network"]
    assert result["ipinfo_asn"].tolist() == [13335, 64502]
    assert result["asdb_layer1_categories"].tolist() == [("Technology",), ("Education",)]
    assert result["tor_exit_listed"].tolist() == [True, True]
    assert result["hosting_asn_listed"].tolist() == [True, True]
    assert result["vpn_listed"].iloc[0] == True  # noqa: E712
    assert pd.isna(result["vpn_listed"].iloc[1])
    assert result["datacentre_listed"].iloc[0] == True  # noqa: E712
    assert pd.isna(result["datacentre_listed"].iloc[1])


def test_enrich_reports_route_ipinfo_agreement_and_disagreement():
    result = enrich(["1.0.0.7", "1.0.3.7", "1.0.2.7"], route=make_route(), ipinfo=make_ipinfo())

    assert result["route_ipinfo_asn_agree"].iloc[0] == True  # noqa: E712
    assert result["route_ipinfo_asn_agree"].iloc[1] == False  # noqa: E712
    assert pd.isna(result["route_ipinfo_asn_agree"].iloc[2])
    assert result.loc[1, "route_asn"] == 64500
    assert result.loc[1, "ipinfo_asn"] == 64501


def test_enrich_accepts_legacy_provider_sets_for_backward_compatibility():
    records = pd.DataFrame(
        {"cidr": ["10.0.0.0/8"], "ip_version": ["IPv4"], "provider": ["legacy"]}
    )
    result = enrich(["10.1.2.3", "11.0.0.1"], cloud=provider_sets(records))

    assert result["cloud_matches"].tolist() == [("legacy",), ()]
    assert result["cloud_match_details"].isna().all()
