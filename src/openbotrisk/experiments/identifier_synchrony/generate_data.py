"""
Synthetic data for demonstrating two bot-group clustering methods.

Population (ground truth in column `group`):
  legit        : ~1000 independent users. Some share IP/device/card within
                 households (the realistic source of benign identifier edges).
  travel_agent : 25 accounts sharing one card + one IP, organic registration
                 times, normal behaviour. A benign tight cluster -- the
                 false-positive trap for identifier clustering.
  ring_lazy    : 60 bot accounts, heavy identifier reuse (cards, devices,
                 IPs, phone). Easy for Method 1 (identifier graph).
  ring_careful : 50 bot accounts, every identifier unique (residential
                 proxies, fresh fingerprints, virtual cards) BUT acting in
                 lockstep. Invisible to Method 1, target for Method 2
                 (behavioural synchrony).
  ring_mid     : 40 bot accounts, partial device reuse + loose synchrony.
                 Partially visible to both.

Outputs:
  users.csv  : user_id, group, reg_ts, card, email, phone, ip, asn,
               device_id, captcha_hit
  events.csv : user_id, ts, action, target   (for Method 2)

Honesty note: synthetic data demonstrates the *mechanics*, not the
*effectiveness*, of these methods. The rings are detectable by construction.
"""

from pathlib import Path

import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[3]
DATA_DIR = REPO_ROOT / "experiments" / "identifier-synchrony" / "generated"
DATA_DIR.mkdir(exist_ok=True)

T0 = pd.Timestamp("2026-01-01")
HORIZON_DAYS = 120

users = []
events = []
_uid = 0


def new_uid():
    global _uid
    _uid += 1
    return f"u{_uid:05d}"


def rand_ts_organic(n):
    """Registrations spread over the horizon, diurnal-ish."""
    days = rng.uniform(0, HORIZON_DAYS, n)
    hour = rng.normal(15, 5, n) % 24  # daytime-weighted
    return T0 + pd.to_timedelta(days, "D") + pd.to_timedelta(hour, "h")


def ident(prefix, i):
    return f"{prefix}{i:06d}"


# ---------------------------------------------------------------- legit users
# Households: 1-3 users sharing IP, sometimes device/card.
n_households = 600
hh_sizes = rng.choice([1, 1, 1, 1, 2, 2, 3], n_households)
card_i = ip_i = dev_i = email_i = phone_i = 0
legit_uids = []
for hh in range(n_households):
    ip_i += 1
    hh_ip = ident("ip_res_", ip_i)
    hh_asn = rng.choice(["AS_BT", "AS_Sky", "AS_Virgin", "AS_EE_mobile"])
    card_i += 1
    hh_card = ident("card_", card_i)          # sometimes shared in household
    for m in range(hh_sizes[hh]):
        uid = new_uid()
        legit_uids.append(uid)
        email_i += 1
        phone_i += 1
        share_card = m > 0 and rng.random() < 0.4
        if not share_card:
            card_i += 1
        dev_i += 1
        users.append(dict(
            user_id=uid, group="legit",
            reg_ts=rand_ts_organic(1)[0],
            card=hh_card if share_card else ident("card_", card_i),
            email=ident("em_", email_i),
            phone=ident("ph_", phone_i),
            ip=hh_ip, asn=hh_asn,
            device_id=ident("dev_", dev_i),
            captcha_hit=rng.random() < 0.02,   # 2% base rate
        ))

# One promiscuous benign IP: a university CGNAT egress shared by 120 users.
# This is the giant-component trap for Method 1.
ip_i += 1
cgnat_ip = ident("ip_cgnat_", ip_i)
for uid in rng.choice(legit_uids, 120, replace=False):
    for u in users:
        if u["user_id"] == uid:
            u["ip"] = cgnat_ip
            u["asn"] = "AS_UniNet"

# --------------------------------------------------------------- travel agent
card_i += 1
agent_card = ident("card_", card_i)
ip_i += 1
agent_ip = ident("ip_office_", ip_i)
agent_uids = []
for _ in range(25):
    uid = new_uid()
    agent_uids.append(uid)
    email_i += 1
    phone_i += 1
    dev_i += 1
    users.append(dict(
        user_id=uid, group="travel_agent",
        reg_ts=rand_ts_organic(1)[0],          # organic accumulation
        card=agent_card, email=ident("em_", email_i),
        phone=ident("ph_", phone_i),
        ip=agent_ip, asn="AS_BT_business",
        device_id=ident("dev_", dev_i),
        captcha_hit=rng.random() < 0.02,
    ))

# ----------------------------------------------------------------- ring_lazy
# 60 accounts, 5 cards, 8 devices, 4 datacenter IPs, 3 phones. Registered in
# two bursts. High captcha rate. Heavy identifier reuse = Method 1 fodder.
lazy_cards = [ident("card_", card_i + 1 + i) for i in range(5)]
card_i += 5
lazy_devs = [ident("dev_", dev_i + 1 + i) for i in range(8)]
dev_i += 8
lazy_ips = [ident("ip_dc_", ip_i + 1 + i) for i in range(4)]
ip_i += 4
lazy_phones = [ident("ph_", phone_i + 1 + i) for i in range(3)]
phone_i += 3
lazy_uids = []
burst_starts = [T0 + pd.Timedelta(days=20), T0 + pd.Timedelta(days=21)]
for k in range(60):
    uid = new_uid()
    lazy_uids.append(uid)
    email_i += 1
    burst = burst_starts[k % 2]
    users.append(dict(
        user_id=uid, group="ring_lazy",
        reg_ts=burst + pd.Timedelta(seconds=int(rng.uniform(0, 7200))),
        card=rng.choice(lazy_cards), email=ident("em_", email_i),
        phone=rng.choice(lazy_phones),
        ip=rng.choice(lazy_ips), asn="AS_CheapVPS",
        device_id=rng.choice(lazy_devs),
        captcha_hit=rng.random() < 0.45,
    ))

# -------------------------------------------------------------- ring_careful
# 50 accounts. EVERY identifier unique: residential proxies, fresh
# fingerprints, single-use virtual cards. Registered with jittered spacing
# over a week (no obvious burst). Identifier graph sees nothing.
careful_uids = []
for k in range(50):
    uid = new_uid()
    careful_uids.append(uid)
    card_i += 1
    email_i += 1
    phone_i += 1
    ip_i += 1
    dev_i += 1
    users.append(dict(
        user_id=uid, group="ring_careful",
        reg_ts=T0 + pd.Timedelta(days=40) + pd.Timedelta(hours=float(k * 3 + rng.uniform(0, 2))),
        card=ident("card_", card_i), email=ident("em_", email_i),
        phone=ident("ph_", phone_i),
        ip=ident("ip_res_", ip_i),             # residential proxy pool
        asn=rng.choice(["AS_BT", "AS_Sky", "AS_Virgin"]),
        device_id=ident("dev_", dev_i),
        captcha_hit=rng.random() < 0.30,
    ))

# ------------------------------------------------------------------ ring_mid
# 40 accounts, 12 devices reused, unique cards/IPs. Loose synchrony.
mid_devs = [ident("dev_", dev_i + 1 + i) for i in range(12)]
dev_i += 12
mid_uids = []
for _k in range(40):
    uid = new_uid()
    mid_uids.append(uid)
    card_i += 1
    email_i += 1
    phone_i += 1
    ip_i += 1
    users.append(dict(
        user_id=uid, group="ring_mid",
        reg_ts=T0 + pd.Timedelta(days=60) + pd.Timedelta(hours=float(rng.uniform(0, 96))),
        card=ident("card_", card_i), email=ident("em_", email_i),
        phone=ident("ph_", phone_i),
        ip=ident("ip_res_", ip_i), asn="AS_EE_mobile",
        device_id=rng.choice(mid_devs),
        captcha_hit=rng.random() < 0.25,
    ))

users_df = pd.DataFrame(users)

# ============================================================== events table
# Targets: product/listing pages. Legit users browse random targets at
# diurnal times. Rings hit the SAME targets in the SAME time windows
# (campaigns) -- that coordination is what Method 2 detects.

targets = [f"item_{i:04d}" for i in range(500)]
ACTIONS = ["view", "add_to_basket", "checkout"]

def legit_events(uid, n):
    ts = rand_ts_organic(n)
    for t in ts:
        events.append(dict(user_id=uid, ts=t,
                           action=rng.choice(ACTIONS, p=[.8, .15, .05]),
                           target=rng.choice(targets)))

for uid in legit_uids + agent_uids:
    legit_events(uid, int(rng.integers(5, 40)))

def campaign(uids, start, n_waves, wave_gap_h, targets_pool,
             participation=0.9, jitter_s=900):
    """All ring members hit the same targets in tight waves."""
    for w in range(n_waves):
        wave_t = start + pd.Timedelta(hours=w * wave_gap_h)
        wave_targets = rng.choice(targets_pool, 3, replace=False)
        for uid in uids:
            if rng.random() > participation:
                continue
            for tg in wave_targets:
                events.append(dict(
                    user_id=uid,
                    ts=wave_t + pd.Timedelta(seconds=float(rng.uniform(0, jitter_s))),
                    action=rng.choice(ACTIONS, p=[.5, .3, .2]),
                    target=tg))

hot = rng.choice(targets, 30, replace=False)   # contested inventory
campaign(lazy_uids,    T0 + pd.Timedelta(days=22), n_waves=10, wave_gap_h=12,
         targets_pool=hot, jitter_s=300)
campaign(careful_uids, T0 + pd.Timedelta(days=48), n_waves=12, wave_gap_h=8,
         targets_pool=hot, jitter_s=1800)       # looser jitter, still coordinated
campaign(mid_uids,     T0 + pd.Timedelta(days=65), n_waves=6,  wave_gap_h=24,
         targets_pool=hot, jitter_s=3600, participation=0.7)

# Bots also generate some camouflage browsing
for uid in lazy_uids + careful_uids + mid_uids:
    legit_events(uid, int(rng.integers(2, 8)))

events_df = pd.DataFrame(events).sort_values("ts").reset_index(drop=True)

users_df.to_csv(DATA_DIR / "users.csv", index=False)
events_df.to_csv(DATA_DIR / "events.csv", index=False)
print(users_df.group.value_counts())
print(f"{len(events_df)} events")
