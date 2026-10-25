import numpy as np
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from openbotrisk.experiments.identifier_synchrony.generate_data import (
    HORIZON_DAYS,
    T0,
    _rand_ts_organic,
    authored_network_fixture,
    generate_synthetic_data,
)


@pytest.fixture(scope="module")
def generated():
    return generate_synthetic_data()


def test_generation_is_reproducible_for_a_fixed_seed(generated):
    users, events = generated
    repeated_users, repeated_events = generate_synthetic_data()
    assert_frame_equal(users, repeated_users)
    assert_frame_equal(events, repeated_events)


@pytest.mark.parametrize("hard", [False, True])
def test_all_events_respect_registration_and_observation_boundaries(hard):
    users, events = generate_synthetic_data(hard=hard)
    joined = events.merge(
        users[["user_id", "group", "reg_ts"]],
        on="user_id",
        validate="many_to_one",
    )
    observation_end = T0 + pd.Timedelta(days=HORIZON_DAYS)

    assert (joined["ts"] >= joined["reg_ts"]).all()
    assert (joined["ts"] < observation_end).all()
    assert set(joined["group"]) >= {
        "legit",
        "travel_agent",
        "ring_lazy",
        "ring_careful",
        "ring_mid",
    }


def test_organic_sampler_preserves_daytime_weighting():
    timestamps = _rand_ts_organic(np.random.default_rng(123), 20_000)
    repeated = _rand_ts_organic(np.random.default_rng(123), 20_000)
    hour = np.asarray(timestamps.hour) + np.asarray(timestamps.minute) / 60
    daytime_share = ((hour >= 8) & (hour < 22)).mean()

    assert timestamps.equals(repeated)
    assert 0.82 < daytime_share < 0.86


def test_incompatible_custom_horizon_is_rejected():
    with pytest.raises(ValueError, match="incompatible with the fixed campaign schedule"):
        generate_synthetic_data(horizon_days=70)


def test_authored_network_fixture_is_separate_from_ground_truth(generated):
    users, _ = generated
    fixture = authored_network_fixture()

    assert "group" not in fixture.columns
    assert fixture["fixture_source"].eq("authored synthetic scenario").all()
    assert fixture["ip"].str.startswith("ip_").all()

    joined = users.merge(fixture, on="ip", how="inner", validate="many_to_one")
    benign_shared = joined[joined["ip"].isin(["ip_cgnat_000601", "ip_office_000602"])]
    suspicious_unflagged = joined[joined["ip"].isin(["ip_res_000607", "ip_res_000657"])]

    assert len(benign_shared) > 25
    assert set(benign_shared["group"]) <= {"legit", "travel_agent"}
    assert set(suspicious_unflagged["group"]) == {"ring_careful", "ring_mid"}
    assert not suspicious_unflagged["datacentre_listed"].any()
    assert not suspicious_unflagged["tor_exit_listed"].any()
