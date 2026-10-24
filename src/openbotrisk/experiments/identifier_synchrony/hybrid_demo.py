"""Validate the hybrid group + loose-signal design on the recovery metric."""

from __future__ import annotations

from collections import Counter, defaultdict

import generate_data as gd
import method1_identifier_graph as m1
import networkx as nx

users, _ = gd.generate_synthetic_data()
u = users.copy()
rng = gd.np.random.default_rng(11)

# 1) hybrid = new group, sourced from 3 legit accounts (kept otherwise legit).
legit_idx = u.index[u.group == "legit"].tolist()
hybrids = list(rng.choice(legit_idx, 3, replace=False))
u.loc[hybrids, "group"] = "hybrid"

# 2) loose vendor-style session id: careful ring across 5 buckets; each bucket
#    also catches a hybrid (in 3 of them) and a few ordinary legit bystanders.
u["fuzzy_id"] = ["fz_" + x for x in u.user_id]
careful = u.index[u.group == "ring_careful"].tolist()
legit_left = [i for i in legit_idx if i not in hybrids]
for b in range(5):
    mem = careful[b * 10:(b + 1) * 10]
    extra = ([hybrids[b]] if b < 3 else []) + list(
        rng.choice(legit_left, 3, replace=False))
    for i in mem + extra:
        u.loc[i, "fuzzy_id"] = f"fz_shared_{b}"

ids = {**m1.ID_TYPES, "fuzzy_id": 2.5}
bip = m1._build_bipartite_graph(u, ids)
m1._prune_promiscuous_identifiers(bip, 40)
g, _ = m1._project_to_user_graph(bip, u, ids, 0.4)

grp = u.set_index("user_id").group.to_dict()
members: dict[int, list[str]] = defaultdict(list)
for cid, comp in enumerate(nx.connected_components(g)):
    for n in comp:
        members[cid].append(n)

print("clusters that contain any ring_careful account (size >= 3):")
for _c, us in members.items():
    comp = Counter(grp[x] for x in us)
    if comp.get("ring_careful", 0) > 0 and len(us) >= 3:
        pur = comp["ring_careful"] / len(us)
        print(f"  size {len(us):>2}  purity(careful)={pur:.2f}  {dict(comp)}")
