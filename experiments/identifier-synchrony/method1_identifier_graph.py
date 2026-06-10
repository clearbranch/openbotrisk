"""
Method 1: shared-identifier graph clustering.

Pipeline:
  1. Bipartite graph: user nodes <-> identifier nodes (card, email, phone,
     ip, device_id). ASN deliberately excluded as an edge -- too coarse;
     kept as a cluster attribute.
  2. Prune promiscuous identifiers (degree > cap). These are CGNAT IPs,
     payment aggregators, default device IDs -- linkage noise.
  3. Project to a weighted user-user graph. Edge weight = sum over shared
     identifiers of  w_type / log2(1 + n_users_on_identifier)
     (inverse-frequency: an identifier shared by 3 users says more than
     one shared by 50).
  4. Connected components; Louvain community detection inside any
     component above a size threshold (the giant-component fix).
  5. Score clusters: empirical-Bayes-shrunk captcha rate + registration
     burstiness (median inter-registration gap).

Packages: networkx + pandas only. For production scale (millions of
users), networkx is the wrong tool -- use igraph/leidenalg or a graph DB;
the *logic* is identical.
"""

import numpy as np
import pandas as pd
import networkx as nx
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]
DATA_DIR = SCRIPT_DIR / "generated"
IMAGE_DIR = REPO_ROOT / "site" / "methodology" / "images"
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

users = pd.read_csv(DATA_DIR / "users.csv", parse_dates=["reg_ts"])

# Identifier types and their base trust as a link (judgment calls -- in a
# real system you'd calibrate these against reviewed cases).
ID_TYPES = {"card": 3.0, "email": 2.5, "phone": 2.5, "device_id": 2.0, "ip": 1.0}
DEGREE_CAP = 40          # identifiers shared by more users than this are pruned
MIN_EDGE_W = 0.8         # prune weak projected edges (e.g. a single busy IP)
BIG_COMPONENT = 80       # run community detection inside components this big

# ---- 1. bipartite graph -----------------------------------------------------
B = nx.Graph()
for _, r in users.iterrows():
    B.add_node(r.user_id, bipartite="user")
    for col in ID_TYPES:
        idn = f"{col}::{r[col]}"             # namespace identifier values
        B.add_node(idn, bipartite="ident", id_type=col)
        B.add_edge(r.user_id, idn)

# ---- 2. prune promiscuous identifiers --------------------------------------
ident_nodes = [n for n, d in B.nodes(data=True) if d.get("bipartite") == "ident"]
degrees = pd.Series({n: B.degree(n) for n in ident_nodes})
pruned = degrees[degrees > DEGREE_CAP]
print("Pruned promiscuous identifiers:")
print(pruned.to_string() if len(pruned) else "  (none)")
B.remove_nodes_from(pruned.index)

# ---- 3. project to user-user graph ------------------------------------------
G = nx.Graph()
G.add_nodes_from(users.user_id)
for idn in [n for n in B if isinstance(n, str) and "::" in n]:
    members = list(B.neighbors(idn))
    k = len(members)
    if k < 2:
        continue
    id_type = idn.split("::")[0]
    w = ID_TYPES[id_type] / np.log2(1 + k)   # inverse-frequency weighting
    for i in range(k):
        for j in range(i + 1, k):            # O(k^2) per identifier -- fine
            u, v = members[i], members[j]    # post-pruning (k <= cap)
            if G.has_edge(u, v):
                G[u][v]["weight"] += w
            else:
                G.add_edge(u, v, weight=w)

weak = [(u, v) for u, v, w in G.edges(data="weight") if w < MIN_EDGE_W]
G.remove_edges_from(weak)
print(f"\nProjected graph: {G.number_of_nodes()} users, {G.number_of_edges()} edges "
      f"({len(weak)} weak edges pruned)")

# ---- 4. components, then Louvain inside big ones -----------------------------
clusters = {}
cid = 0
for comp in nx.connected_components(G):
    if len(comp) <= 1:
        continue                              # singletons: no identifier evidence
    if len(comp) > BIG_COMPONENT:
        sub = G.subgraph(comp)
        for community in nx.community.louvain_communities(sub, weight="weight", seed=1):
            cid += 1
            for u in community:
                clusters[u] = cid
    else:
        cid += 1
        for u in comp:
            clusters[u] = cid

users["cluster_m1"] = users.user_id.map(clusters).astype("Int64")
print(f"{users.cluster_m1.notna().sum()} users in {cid} clusters; "
      f"{users.cluster_m1.isna().sum()} singletons")

# ---- 5. cluster scoring ------------------------------------------------------
BASE_RATE = users.captcha_hit.mean()
K_SHRINK = 10  # pseudo-observations toward base rate; same EB move as ORR ranking


def burstiness(ts):
    """Median inter-registration gap in hours; tiny = burst registration."""
    if len(ts) < 3:
        return np.nan
    gaps = np.diff(np.sort(ts.values)).astype("timedelta64[s]").astype(float)
    return np.median(gaps) / 3600


rows = []
for c, grp in users.dropna(subset=["cluster_m1"]).groupby("cluster_m1"):
    n = len(grp)
    raw = grp.captcha_hit.mean()
    shrunk = (grp.captcha_hit.sum() + K_SHRINK * BASE_RATE) / (n + K_SHRINK)
    rows.append(dict(cluster=int(c), size=n,
                     captcha_raw=raw, captcha_shrunk=shrunk,
                     med_reg_gap_h=burstiness(grp.reg_ts),
                     top_asn=grp.asn.mode()[0],
                     majority_truth=grp.group.mode()[0]))
scores = pd.DataFrame(rows).sort_values("captcha_shrunk", ascending=False)
print("\nTop clusters by shrunk captcha rate (size >= 5):")
print(scores[scores["size"] >= 5].head(10).to_string(index=False,
      float_format=lambda x: f"{x:.3f}"))

# ---- evaluation against ground truth (only possible because synthetic) ------
print("\nDetection by ground-truth group (share of members in any cluster of size>=5):")
big = set(scores[scores["size"] >= 5].cluster)
users["in_big_cluster"] = users.cluster_m1.isin(big)
print(users.groupby("group").in_big_cluster.mean().to_string(float_format=lambda x: f"{x:.2f}"))

# ---- plots -------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

ax = axes[0]
ax.hist(degrees.values, bins=np.logspace(0, 2.5, 30), color="#4878a8")
ax.axvline(DEGREE_CAP, color="crimson", ls="--", label=f"degree cap = {DEGREE_CAP}")
ax.set(xscale="log", yscale="log", xlabel="users per identifier",
       ylabel="identifier count", title="Identifier degree distribution\n(prune the right tail)")
ax.legend()

ax = axes[1]
clustered = users.dropna(subset=["cluster_m1"])
sub = G.subgraph(clustered.user_id)
pos = nx.spring_layout(sub, seed=2, k=0.3)
palette = {"legit": "#b8b8b8", "travel_agent": "#2a9d2a",
           "ring_lazy": "#d62728", "ring_careful": "#9467bd", "ring_mid": "#ff7f0e"}
colors = clustered.set_index("user_id").group.map(palette)
nx.draw_networkx_nodes(sub, pos, node_size=18, ax=ax,
                       node_color=[colors[n] for n in sub.nodes])
nx.draw_networkx_edges(sub, pos, alpha=0.15, ax=ax)
for g, c in palette.items():
    ax.scatter([], [], color=c, label=g, s=30)
ax.legend(fontsize=8); ax.set_axis_off()
ax.set_title("User-user projection, coloured by ground truth\n"
             "(ring_careful absent: nothing to link)")

ax = axes[2]
s5 = scores[scores["size"] >= 3]
truth_col = s5.majority_truth.map(palette)
ax.scatter(s5["size"], s5.captcha_shrunk, c=truth_col, s=50)
ax.axhline(BASE_RATE, color="grey", ls=":", label=f"base rate {BASE_RATE:.02f}")
ax.set(xscale="log", xlabel="cluster size", ylabel="shrunk captcha rate",
       title="Cluster scoring: size vs shrunk captcha rate\n(travel agent sits at base rate)")
ax.legend()

plt.tight_layout()
plt.savefig(IMAGE_DIR / "method1_identifier_graph.png", dpi=140)
print("\nSaved method1_identifier_graph.png")
users.to_csv(DATA_DIR / "users_m1.csv", index=False)
