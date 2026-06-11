"""Generate synthetic users and events for the identifier/synchrony experiment.

The generated data is intentionally constructed to show where two clustering
methods succeed and fail:

- shared-identifier graph clustering;
- behavioural synchrony clustering.

The output is deterministic for the default seed and is written to
``experiments/identifier-synchrony/generated/``.

Example:
    Run from the repository root:

    ```bash
    python src/openbotrisk/experiments/identifier_synchrony/generate_data.py
    ```
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[3]
DATA_DIR = REPO_ROOT / "experiments" / "identifier-synchrony" / "generated"

SEED = 42
T0 = pd.Timestamp("2026-01-01")
HORIZON_DAYS = 120
ACTIONS = ["view", "add_to_basket", "checkout"]


@dataclass
class _Counters:
    """Mutable ID counters used while building synthetic records."""

    uid: int = 0
    card: int = 0
    ip: int = 0
    device: int = 0
    email: int = 0
    phone: int = 0


def _new_uid(counters: _Counters) -> str:
    """Return the next synthetic user ID.

    Args:
        counters: Mutable counter state.

    Returns:
        A stable user ID such as ``"u00001"``.
    """

    counters.uid += 1
    return f"u{counters.uid:05d}"


def _ident(prefix: str, i: int) -> str:
    """Return a namespaced synthetic identifier value.

    Args:
        prefix: Identifier prefix, such as ``"card_"`` or ``"ip_res_"``.
        i: Numeric identifier counter.

    Returns:
        A zero-padded identifier string.
    """

    return f"{prefix}{i:06d}"


def _rand_ts_organic(
    rng: np.random.Generator,
    n: int,
    *,
    start: pd.Timestamp = T0,
    horizon_days: int = HORIZON_DAYS,
) -> pd.DatetimeIndex:
    """Generate organic-looking timestamps over the experiment horizon.

    Args:
        rng: NumPy random generator.
        n: Number of timestamps to generate.
        start: Start of the synthetic observation window.
        horizon_days: Number of days in the observation window.

    Returns:
        A ``DatetimeIndex`` with daytime-weighted timestamps.
    """

    days = rng.uniform(0, horizon_days, n)
    hour = rng.normal(15, 5, n) % 24
    return start + pd.to_timedelta(days, "D") + pd.to_timedelta(hour, "h")


def _legit_events(
    rng: np.random.Generator,
    events: list[dict[str, Any]],
    uid: str,
    n: int,
    targets: list[str],
) -> None:
    """Append ordinary browsing events for one synthetic user.

    Args:
        rng: NumPy random generator.
        events: Mutable event-record list to append to.
        uid: Synthetic user ID.
        n: Number of events to append.
        targets: Candidate item/listing targets.

    Returns:
        ``None``. The ``events`` list is modified in place.
    """

    for ts in _rand_ts_organic(rng, n):
        events.append(
            {
                "user_id": uid,
                "ts": ts,
                "action": rng.choice(ACTIONS, p=[0.8, 0.15, 0.05]),
                "target": rng.choice(targets),
            }
        )


def _campaign(
    rng: np.random.Generator,
    events: list[dict[str, Any]],
    uids: list[str],
    start: pd.Timestamp,
    n_waves: int,
    wave_gap_h: int,
    targets_pool: np.ndarray,
    *,
    participation: float = 0.9,
    jitter_s: int = 900,
) -> None:
    """Append coordinated campaign events for a ring.

    Args:
        rng: NumPy random generator.
        events: Mutable event-record list to append to.
        uids: Users participating in the campaign.
        start: Timestamp of the first campaign wave.
        n_waves: Number of campaign waves.
        wave_gap_h: Hours between waves.
        targets_pool: Candidate hot targets.
        participation: Per-user probability of joining each wave.
        jitter_s: Maximum within-wave timestamp jitter in seconds.

    Returns:
        ``None``. The ``events`` list is modified in place.
    """

    for w in range(n_waves):
        wave_t = start + pd.Timedelta(hours=w * wave_gap_h)
        wave_targets = rng.choice(targets_pool, 3, replace=False)
        for uid in uids:
            if rng.random() > participation:
                continue
            for target in wave_targets:
                events.append(
                    {
                        "user_id": uid,
                        "ts": wave_t
                        + pd.Timedelta(seconds=float(rng.uniform(0, jitter_s))),
                        "action": rng.choice(ACTIONS, p=[0.5, 0.3, 0.2]),
                        "target": target,
                    }
                )


def generate_synthetic_data(seed: int = SEED) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Generate the synthetic user and event tables.

    Args:
        seed: Random seed. The default reproduces the figures on the
            Methodology page.

    Returns:
        A tuple ``(users_df, events_df)``. ``users_df`` contains synthetic
        accounts and identifiers; ``events_df`` contains timestamped actions.

    Example:
        ```python
        users, events = generate_synthetic_data()
        assert {"user_id", "group"}.issubset(users.columns)
        ```
    """

    rng = np.random.default_rng(seed)
    counters = _Counters()
    users: list[dict[str, Any]] = []
    events: list[dict[str, Any]] = []

    # Legit users: households share IPs and sometimes cards.
    n_households = 600
    hh_sizes = rng.choice([1, 1, 1, 1, 2, 2, 3], n_households)
    legit_uids: list[str] = []
    for hh_size in hh_sizes:
        counters.ip += 1
        hh_ip = _ident("ip_res_", counters.ip)
        hh_asn = rng.choice(["AS_BT", "AS_Sky", "AS_Virgin", "AS_EE_mobile"])
        counters.card += 1
        hh_card = _ident("card_", counters.card)
        for member in range(hh_size):
            uid = _new_uid(counters)
            legit_uids.append(uid)
            counters.email += 1
            counters.phone += 1
            share_card = member > 0 and rng.random() < 0.4
            if not share_card:
                counters.card += 1
            counters.device += 1
            users.append(
                {
                    "user_id": uid,
                    "group": "legit",
                    "reg_ts": _rand_ts_organic(rng, 1)[0],
                    "card": hh_card if share_card else _ident("card_", counters.card),
                    "email": _ident("em_", counters.email),
                    "phone": _ident("ph_", counters.phone),
                    "ip": hh_ip,
                    "asn": hh_asn,
                    "device_id": _ident("dev_", counters.device),
                    "captcha_hit": rng.random() < 0.02,
                }
            )

    # One benign university CGNAT egress, included as a giant-component trap.
    counters.ip += 1
    cgnat_ip = _ident("ip_cgnat_", counters.ip)
    for uid in rng.choice(legit_uids, 120, replace=False):
        for user in users:
            if user["user_id"] == uid:
                user["ip"] = cgnat_ip
                user["asn"] = "AS_UniNet"

    # Travel agent: benign but tightly linked by office IP and card.
    counters.card += 1
    agent_card = _ident("card_", counters.card)
    counters.ip += 1
    agent_ip = _ident("ip_office_", counters.ip)
    agent_uids: list[str] = []
    for _ in range(25):
        uid = _new_uid(counters)
        agent_uids.append(uid)
        counters.email += 1
        counters.phone += 1
        counters.device += 1
        users.append(
            {
                "user_id": uid,
                "group": "travel_agent",
                "reg_ts": _rand_ts_organic(rng, 1)[0],
                "card": agent_card,
                "email": _ident("em_", counters.email),
                "phone": _ident("ph_", counters.phone),
                "ip": agent_ip,
                "asn": "AS_BT_business",
                "device_id": _ident("dev_", counters.device),
                "captcha_hit": rng.random() < 0.02,
            }
        )

    # Lazy ring: heavy identifier reuse.
    lazy_cards = [_ident("card_", counters.card + 1 + i) for i in range(5)]
    counters.card += 5
    lazy_devs = [_ident("dev_", counters.device + 1 + i) for i in range(8)]
    counters.device += 8
    lazy_ips = [_ident("ip_dc_", counters.ip + 1 + i) for i in range(4)]
    counters.ip += 4
    lazy_phones = [_ident("ph_", counters.phone + 1 + i) for i in range(3)]
    counters.phone += 3
    lazy_uids: list[str] = []
    burst_starts = [T0 + pd.Timedelta(days=20), T0 + pd.Timedelta(days=21)]
    for k in range(60):
        uid = _new_uid(counters)
        lazy_uids.append(uid)
        counters.email += 1
        burst = burst_starts[k % 2]
        users.append(
            {
                "user_id": uid,
                "group": "ring_lazy",
                "reg_ts": burst + pd.Timedelta(seconds=int(rng.uniform(0, 7200))),
                "card": rng.choice(lazy_cards),
                "email": _ident("em_", counters.email),
                "phone": rng.choice(lazy_phones),
                "ip": rng.choice(lazy_ips),
                "asn": "AS_CheapVPS",
                "device_id": rng.choice(lazy_devs),
                "captcha_hit": rng.random() < 0.45,
            }
        )

    # Careful ring: every identifier unique, but behaviour coordinated later.
    careful_uids: list[str] = []
    for k in range(50):
        uid = _new_uid(counters)
        careful_uids.append(uid)
        counters.card += 1
        counters.email += 1
        counters.phone += 1
        counters.ip += 1
        counters.device += 1
        users.append(
            {
                "user_id": uid,
                "group": "ring_careful",
                "reg_ts": T0
                + pd.Timedelta(days=40)
                + pd.Timedelta(hours=float(k * 3 + rng.uniform(0, 2))),
                "card": _ident("card_", counters.card),
                "email": _ident("em_", counters.email),
                "phone": _ident("ph_", counters.phone),
                "ip": _ident("ip_res_", counters.ip),
                "asn": rng.choice(["AS_BT", "AS_Sky", "AS_Virgin"]),
                "device_id": _ident("dev_", counters.device),
                "captcha_hit": rng.random() < 0.30,
            }
        )

    # Mid ring: partial device reuse and loose synchrony.
    mid_devs = [_ident("dev_", counters.device + 1 + i) for i in range(12)]
    counters.device += 12
    mid_uids: list[str] = []
    for _ in range(40):
        uid = _new_uid(counters)
        mid_uids.append(uid)
        counters.card += 1
        counters.email += 1
        counters.phone += 1
        counters.ip += 1
        users.append(
            {
                "user_id": uid,
                "group": "ring_mid",
                "reg_ts": T0
                + pd.Timedelta(days=60)
                + pd.Timedelta(hours=float(rng.uniform(0, 96))),
                "card": _ident("card_", counters.card),
                "email": _ident("em_", counters.email),
                "phone": _ident("ph_", counters.phone),
                "ip": _ident("ip_res_", counters.ip),
                "asn": "AS_EE_mobile",
                "device_id": rng.choice(mid_devs),
                "captcha_hit": rng.random() < 0.25,
            }
        )

    targets = [f"item_{i:04d}" for i in range(500)]
    for uid in legit_uids + agent_uids:
        _legit_events(rng, events, uid, int(rng.integers(5, 40)), targets)

    hot = rng.choice(targets, 30, replace=False)
    _campaign(
        rng,
        events,
        lazy_uids,
        T0 + pd.Timedelta(days=22),
        n_waves=10,
        wave_gap_h=12,
        targets_pool=hot,
        jitter_s=300,
    )
    _campaign(
        rng,
        events,
        careful_uids,
        T0 + pd.Timedelta(days=48),
        n_waves=12,
        wave_gap_h=8,
        targets_pool=hot,
        jitter_s=1800,
    )
    _campaign(
        rng,
        events,
        mid_uids,
        T0 + pd.Timedelta(days=65),
        n_waves=6,
        wave_gap_h=24,
        targets_pool=hot,
        jitter_s=3600,
        participation=0.7,
    )

    for uid in lazy_uids + careful_uids + mid_uids:
        _legit_events(rng, events, uid, int(rng.integers(2, 8)), targets)

    users_df = pd.DataFrame(users)
    events_df = pd.DataFrame(events).sort_values("ts").reset_index(drop=True)
    return users_df, events_df


def main() -> None:
    """Write synthetic users/events CSVs for the Methodology page.

    Args:
        None.

    Returns:
        ``None``. Writes ``users.csv`` and ``events.csv`` under ``DATA_DIR``.
    """

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    users_df, events_df = generate_synthetic_data()
    users_df.to_csv(DATA_DIR / "users.csv", index=False)
    events_df.to_csv(DATA_DIR / "events.csv", index=False)
    print(users_df.group.value_counts())
    print(f"{len(events_df)} events")


if __name__ == "__main__":
    main()
