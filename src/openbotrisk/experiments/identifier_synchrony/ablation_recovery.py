"""Method 1 ablation on a CLUSTERING-QUALITY metric (not CAPTCHA risk).

Per true ring we report, over found clusters of >= S members:
  coverage = share of the ring's accounts that land in clusters whose majority
             is that ring (union across fragments -> partial recovery credited);
  pieces   = how many such clusters (1 = clean, >1 = fragmented, 0 = missed);
  purity   = of those clusters' members, the share actually from that ring
             (a merge or benign contamination shows up as purity < 1).

Spurious structure is tracked symmetrically: any cluster whose majority is a
benign group (legit), and any account swept into a cluster of another group.
travel_agent forming one clean cluster is a *correct* recovery of a real benign
group, not spurious -- whether to flag it is a separate (detection) question.
"""

from __future__ import annotations

from collections import Counter, defaultdict

import generate_data as gd
import method1_identifier_graph as m1
import networkx as nx

S = 3
RINGS = ["ring_lazy", "ring_careful", "ring_mid"]
CONFIDENT = {"card": 3.0, "email": 2.5, "phone": 2.5}


def components(graph: nx.Graph) -> dict[str, int]:
    out: dict[str, int] = {}
    for cid, comp in enumerate(nx.connected_components(graph)):
        for n in comp:
            out[n] = cid
    return out


def project(users, id_types, min_edge_w, degree_cap=None):
    bip = m1._build_bipartite_graph(users, id_types)
    if degree_cap is not None:
        m1._prune_promiscuous_identifiers(bip, degree_cap)
    g, _ = m1._project_to_user_graph(bip, users, id_types, min_edge_w)
    return g


def evaluate(users, clusters, s=S):
    grp = users.set_index("user_id").group.to_dict()
    members: dict[int, list[str]] = defaultdict(list)
    for u, c in clusters.items():
        members[c].append(u)
    info = {}
    for c, us in members.items():
        if len(us) < s:
            continue
        comp = Counter(grp[u] for u in us)
        maj, majn = comp.most_common(1)[0]
        info[c] = dict(size=len(us), comp=comp, maj=maj, purity=majn / len(us))

    rows = {}
    for g in RINGS + ["travel_agent"]:
        gc = [c for c, i in info.items() if i["maj"] == g]
        gusers = set(users.loc[users.group == g, "user_id"])
        covered, tot, fromg = set(), 0, 0
        for c in gc:
            cs = set(members[c])
            covered |= cs & gusers
            tot += len(cs)
            fromg += sum(1 for u in cs if grp[u] == g)
        rows[g] = dict(
            cov=len(covered) / len(gusers) if gusers else 0.0,
            pieces=len(gc),
            pur=(fromg / tot) if tot else float("nan"),
        )
    legit_clustered = sum(
        1 for c, i in info.items() for u in members[c]
        if grp[u] == "legit"
    )
    spurious = [c for c, i in info.items() if i["maj"] == "legit"]
    mixed = [c for c, i in info.items() if i["purity"] < 0.8]
    return rows, info, legit_clustered, spurious, mixed


def fmt(r):
    return f"{r['cov']:.2f}/{r['pieces']}/{r['pur']:.2f}"


def line(name, rows, legit_clustered, spurious, mixed):
    cells = " | ".join(fmt(rows[g]) for g in RINGS)
    return (f"{name:<34} {cells:<46} "
            f"legit_in={legit_clustered:<4} spur={len(spurious):<3} "
            f"mixed={len(mixed)}")


def main() -> None:
    users, _ = gd.generate_synthetic_data()

    print("cells are coverage/pieces/purity   (want cov high, purity high)")
    print(f"{'rung':<34} {'ring_lazy':<15}{'ring_careful':<16}{'ring_mid':<15} "
          "spurious structure")
    print("-" * 104)

    configs = [
        ("0. raw projection (all ids)",
         dict(id_types=m1.ID_TYPES, min_edge_w=0.0)),
        ("1. confident ids only",
         dict(id_types=CONFIDENT, min_edge_w=0.0)),
        ("2. all ids + prune (cap 40)",
         dict(id_types=m1.ID_TYPES, min_edge_w=0.0, degree_cap=40)),
        ("3. + weight floor 0.8 (method)",
         dict(id_types=m1.ID_TYPES, min_edge_w=0.8, degree_cap=40)),
    ]
    for name, kw in configs:
        clusters = components(project(users, **kw))
        rows, _info, legit_clustered, spurious, mixed = evaluate(users, clusters)
        print(line(name, rows, legit_clustered, spurious, mixed))

    # --- looser-signal test: a shared "session/fuzzy id" common to detection
    # vendors, shared more broadly. Distribute the careful ring across 5 fuzzy
    # buckets, and contaminate each bucket with a few legit accounts. ---
    u2 = users.copy()
    u2["fuzzy_id"] = ["fz_u_" + uid for uid in u2.user_id]  # default: unique
    rng = gd.np.random.default_rng(7)
    careful = u2.index[u2.group == "ring_careful"].tolist()
    legit_idx = u2.index[u2.group == "legit"].tolist()
    for b in range(5):
        members = careful[b * 10:(b + 1) * 10]
        bystanders = list(rng.choice(legit_idx, 4, replace=False))
        for i in members + bystanders:
            u2.loc[i, "fuzzy_id"] = f"fz_shared_{b:02d}"

    fuzzy_types = {**m1.ID_TYPES, "fuzzy_id": 2.5}
    print("\nlooser-signal test (add a vendor-style shared session id; the 5"
          " careful buckets each hold 10 careful + 4 legit):")
    for name, floor, use_fuzzy in [
        ("  no fuzzy id, floor 0.4", 0.4, False),
        ("  + fuzzy id, floor 0.4", 0.4, True),
        ("  + fuzzy id, floor 0.8", 0.8, True),
    ]:
        ids = fuzzy_types if use_fuzzy else m1.ID_TYPES
        clusters = components(project(u2, ids, min_edge_w=floor, degree_cap=40))
        rows, _info, legit_clustered, spurious, mixed = evaluate(u2, clusters)
        print(line(name, rows, legit_clustered, spurious, mixed))


if __name__ == "__main__":
    main()
