"""
Sensitivity of Method 2 to the time-bucket width.

First run with BUCKET=1h fragmented ring_careful (jitter ~30 min) and
missed ring_mid entirely (jitter ~1h, participation 0.7). That is not a
bug; it is the method's central tuning problem: the bucket must be wide
enough to span the ring's internal jitter, but every widening admits
more coincidental co-occurrence from legitimate users. Sweep it and
look at both curves.
"""

# ruff: noqa: I001

from collections import defaultdict
from itertools import combinations
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import networkx as nx
import pandas as pd
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[3]
DATA_DIR = REPO_ROOT / "experiments" / "identifier-synchrony" / "generated"
IMAGE_DIR = REPO_ROOT / "site" / "methodology" / "images"
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

events = pd.read_csv(DATA_DIR / "events.csv", parse_dates=["ts"])
users = pd.read_csv(DATA_DIR / "users.csv", parse_dates=["reg_ts"])
truth = users.set_index("user_id").group
t0 = events.ts.min()

JACCARD_MIN = 0.25
MIN_SHARED = 5
TOKEN_USER_CAP = 80


def run(bucket_hours):
    bucket = pd.Timedelta(hours=bucket_hours)
    user_tokens = defaultdict(set)
    for r in events.itertuples():
        off = (r.ts - t0) / bucket
        for b in (int(off), int(off + 0.5) + 10**6):
            user_tokens[r.user_id].add((r.action, r.target, b))

    token_users = defaultdict(list)
    for u, toks in user_tokens.items():
        for t in toks:
            token_users[t].append(u)

    pair_shared = defaultdict(int)
    for _t, us in token_users.items():
        if 2 <= len(us) <= TOKEN_USER_CAP:
            for u, v in combinations(sorted(us), 2):
                pair_shared[(u, v)] += 1

    G = nx.Graph()
    for (u, v), s in pair_shared.items():
        if s < MIN_SHARED:
            continue
        jac = s / (len(user_tokens[u]) + len(user_tokens[v]) - s)
        if jac >= JACCARD_MIN:
            G.add_edge(u, v)

    detected = set()
    for comp in nx.connected_components(G):
        if len(comp) >= 3:
            detected |= comp
    det = pd.Series({u: u in detected for u in users.user_id})
    det.index.name = "user_id"
    return det.groupby(truth).mean()


grid = [0.5, 1, 2, 4, 8, 16]
res = pd.DataFrame({b: run(b) for b in grid}).T
res.index.name = "bucket_h"
print(res.to_string(float_format=lambda x: f"{x:.2f}"))

fig, ax = plt.subplots(figsize=(8, 5))
palette = {"legit": "#b8b8b8", "travel_agent": "#2a9d2a",
           "ring_lazy": "#d62728", "ring_careful": "#9467bd", "ring_mid": "#ff7f0e"}
for g in res.columns:
    ax.plot(res.index, res[g], "o-", color=palette[g], label=g)
ax.set(xscale="log", xlabel="time-bucket width (hours)",
       ylabel="share of group detected",
       title="Method 2 sensitivity to bucket width\n"
             "wider buckets catch looser rings -- and eventually legit users")
ax.legend()
plt.tight_layout()
plt.savefig(IMAGE_DIR / "method2_bucket_sweep.png", dpi=140)
print("Saved method2_bucket_sweep.png")
