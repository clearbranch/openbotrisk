"""
Method 2: behavioural-synchrony clustering (SynchroTrap-style,
Cao et al. CCS 2014 -- simplified).

Idea: identifiers are cheap to randomise; coordination is not. Two
accounts that repeatedly do the same thing to the same target at the
same time are linked even if they share zero identifiers.

Pipeline:
  1. Discretise each event into (action, target, time_bucket). Buckets
     are OVERLAPPING (stride = bucket/2) so a pair acting 1 minute apart
     across a bucket boundary still co-occurs -- the classic off-by-one
     trap with fixed windows.
  2. Per-user set of these tokens.
  3. Pairwise Jaccard similarity between users -- computed only for pairs
     that co-occur in at least one token (inverted index), never all
     n^2 pairs. Tokens touched by too many users are dropped first
     (a flash-sale item everyone views is not coordination).
  4. Similarity graph: edge if Jaccard >= threshold AND >= min shared
     tokens. Connected components = synchrony clusters.

Scaling note: at real scale exact pairwise Jaccard is replaced by
MinHash/LSH; the inverted-index trick here is the small-data version of
the same idea. SynchroTrap itself ran as a series of daily MapReduce
jobs aggregated over weeks.
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
users = pd.read_csv(DATA_DIR / "users_m1.csv", parse_dates=["reg_ts"])  # carries Method 1 result

BUCKET = pd.Timedelta(hours=1)      # match to attack tempo you care about
JACCARD_MIN = 0.25
MIN_SHARED = 5                      # >= this many shared tokens for an edge
TOKEN_USER_CAP = 80                 # drop tokens touched by more users (trend/noise)

# ---- 1+2. tokenise events into overlapping windows ---------------------------
t0 = events.ts.min()


def buckets(ts):
    """Two overlapping window ids per event (stride = BUCKET/2)."""
    off = (ts - t0) / BUCKET
    return (int(off), int(off + 0.5) + 10**6)  # offset grid shifted by half


user_tokens = defaultdict(set)
for r in events.itertuples():
    for b in buckets(r.ts):
        user_tokens[r.user_id].add((r.action, r.target, b))

# ---- 3. inverted index: token -> users, then pair counting -------------------
token_users = defaultdict(list)
for u, toks in user_tokens.items():
    for t in toks:
        token_users[t].append(u)

pair_shared = defaultdict(int)
dropped_tokens = 0
for _t, us in token_users.items():
    if len(us) < 2:
        continue
    if len(us) > TOKEN_USER_CAP:    # popular item in a popular hour: not signal
        dropped_tokens += 1
        continue
    for u, v in combinations(sorted(us), 2):
        pair_shared[(u, v)] += 1
print(f"{len(token_users)} tokens, {dropped_tokens} dropped as too popular, "
      f"{len(pair_shared)} candidate pairs")

# ---- 4. similarity graph ------------------------------------------------------
G = nx.Graph()
G.add_nodes_from(users.user_id)
for (u, v), shared in pair_shared.items():
    if shared < MIN_SHARED:
        continue
    jac = shared / (len(user_tokens[u]) + len(user_tokens[v]) - shared)
    if jac >= JACCARD_MIN:
        G.add_edge(u, v, weight=jac)

clusters = {}
cid = 0
for comp in nx.connected_components(G):
    if len(comp) < 3:               # require 3+ accounts to call it a group
        continue
    cid += 1
    for u in comp:
        clusters[u] = cid
users["cluster_m2"] = users.user_id.map(clusters).astype("Int64")
print(f"\nMethod 2: {users.cluster_m2.notna().sum()} users in {cid} synchrony clusters")

# ---- evaluate ------------------------------------------------------------------
print("\nDetection by ground-truth group (Method 2):")
users["m2_detected"] = users.cluster_m2.notna()
print(users.groupby("group").m2_detected.mean().to_string(float_format=lambda x: f"{x:.2f}"))

print("\nCluster composition (Method 2):")
for c, grp in users.dropna(subset=["cluster_m2"]).groupby("cluster_m2"):
    print(f"  cluster {int(c)}: n={len(grp)}, truth={dict(grp.group.value_counts())}")

# ---- combined view: which method sees which ring -------------------------------
print("\nMethod 1 vs Method 2 coverage:")
users["m1_detected"] = users.cluster_m1.notna() & users.cluster_m1.map(
    users.cluster_m1.value_counts()).ge(5)
cov = users.groupby("group")[["m1_detected", "m2_detected"]].mean()
print(cov.to_string(float_format=lambda x: f"{x:.2f}"))

# ---- plots ----------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

ax = axes[0]
# timeline of events for a sample of users, showing lockstep waves
palette = {"legit": "#b8b8b8", "travel_agent": "#2a9d2a",
           "ring_lazy": "#d62728", "ring_careful": "#9467bd", "ring_mid": "#ff7f0e"}
sample = pd.concat([
    users[users.group == g].sample(min(12, (users.group == g).sum()), random_state=0)
    for g in palette
])
ev = events[events.user_id.isin(sample.user_id)].merge(
    users[["user_id", "group"]], on="user_id")
ymap = {u: i for i, u in enumerate(sample.user_id)}
ax.scatter(ev.ts, ev.user_id.map(ymap), s=4,
           c=ev.group.map(palette), alpha=0.7)
ax.set(yticks=[], xlabel="time", title="Event raster (12 users/group)\n"
       "vertical stripes = lockstep waves")
for g, c in palette.items():
    ax.scatter([], [], color=c, label=g, s=20)
ax.legend(fontsize=8, loc="upper left")

ax = axes[1]
cov.plot.bar(ax=ax, color=["#4878a8", "#c44e52"])
ax.set(ylabel="share of group detected", ylim=(0, 1.05),
       title="Coverage by method:\nidentifier graph vs behavioural synchrony")
ax.legend(["Method 1 (identifiers)", "Method 2 (synchrony)"], fontsize=9)
ax.tick_params(axis="x", rotation=20)

plt.tight_layout()
plt.savefig(IMAGE_DIR / "method2_synchrony.png", dpi=140)
print("\nSaved method2_synchrony.png")
users.to_csv(DATA_DIR / "users_final.csv", index=False)
