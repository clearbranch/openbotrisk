"""Shared-identifier graph clustering for the synthetic account dataset.

The method links accounts that reuse identifiers such as card, phone, device,
email, or IP address. It is intentionally small and readable; for production
scale the same logic would usually move to graph databases, distributed jobs,
or igraph/Leiden-style tooling.

Example:
    Run after generating synthetic data:

    ```bash
    python src/openbotrisk/experiments/identifier_synchrony/generate_data.py
    python src/openbotrisk/experiments/identifier_synchrony/method1_identifier_graph.py
    ```
"""

from __future__ import annotations

# ruff: noqa: E402,I001

import os
from collections.abc import Mapping
from pathlib import Path
from typing import Any

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from matplotlib.axes import Axes


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[3]
DATA_DIR = REPO_ROOT / "experiments" / "identifier-synchrony" / "generated"
IMAGE_DIR = REPO_ROOT / "site" / "methodology" / "images"

ID_TYPES: dict[str, float] = {
    "card": 3.0,
    "email": 2.5,
    "phone": 2.5,
    "device_id": 2.0,
    "ip": 1.0,
}
DEGREE_CAP = 40
MIN_EDGE_W = 0.8
BIG_COMPONENT = 80
K_SHRINK = 10

PALETTE = {
    "legit": "#b8b8b8",
    "travel_agent": "#2a9d2a",
    "ring_lazy": "#d62728",
    "ring_careful": "#9467bd",
    "ring_mid": "#ff7f0e",
}


def _build_bipartite_graph(
    users: pd.DataFrame,
    id_types: Mapping[str, float] = ID_TYPES,
) -> nx.Graph:
    """Build an account-to-identifier bipartite graph.

    Args:
        users: User table containing ``user_id`` and identifier columns.
        id_types: Identifier columns to include and their base edge weights.

    Returns:
        A ``networkx.Graph`` with account nodes and identifier nodes.
    """

    graph = nx.Graph()
    for row in users.itertuples(index=False):
        user_id = row.user_id
        graph.add_node(user_id, bipartite="user")
        for col in id_types:
            ident = f"{col}::{getattr(row, col)}"
            graph.add_node(ident, bipartite="ident", id_type=col)
            graph.add_edge(user_id, ident)
    return graph


def _prune_promiscuous_identifiers(
    graph: nx.Graph,
    degree_cap: int = DEGREE_CAP,
) -> pd.Series:
    """Remove high-degree identifier nodes from a bipartite graph.

    Args:
        graph: Bipartite account-identifier graph. The graph is modified in
            place.
        degree_cap: Maximum allowed number of users per identifier.

    Returns:
        A ``Series`` of pruned identifier-node degrees, indexed by node name.
    """

    ident_nodes = [
        node
        for node, data in graph.nodes(data=True)
        if data.get("bipartite") == "ident"
    ]
    degrees = pd.Series({node: graph.degree(node) for node in ident_nodes})
    pruned = degrees[degrees > degree_cap]
    graph.remove_nodes_from(pruned.index)
    return pruned


def _identifier_degrees(graph: nx.Graph) -> pd.Series:
    """Return degrees for identifier nodes in a bipartite graph."""

    ident_nodes = [
        node
        for node, data in graph.nodes(data=True)
        if data.get("bipartite") == "ident"
    ]
    return pd.Series({node: graph.degree(node) for node in ident_nodes})


def _project_to_user_graph(
    bipartite: nx.Graph,
    users: pd.DataFrame,
    id_types: Mapping[str, float] = ID_TYPES,
    min_edge_w: float = MIN_EDGE_W,
) -> tuple[nx.Graph, int]:
    """Project a bipartite graph into a weighted user-user graph.

    Args:
        bipartite: Account-identifier graph after pruning.
        users: User table whose ``user_id`` values become graph nodes.
        id_types: Base weight per identifier type.
        min_edge_w: Minimum projected edge weight to keep.

    Returns:
        ``(graph, weak_edge_count)``. ``graph`` is the weighted user graph;
        ``weak_edge_count`` is the number of projected edges pruned.
    """

    graph = nx.Graph()
    graph.add_nodes_from(users.user_id)
    for ident in [node for node in bipartite if isinstance(node, str) and "::" in node]:
        members = list(bipartite.neighbors(ident))
        k = len(members)
        if k < 2:
            continue
        id_type = ident.split("::", maxsplit=1)[0]
        weight = id_types[id_type] / np.log2(1 + k)
        for i, u in enumerate(members):
            for v in members[i + 1 :]:
                if graph.has_edge(u, v):
                    graph[u][v]["weight"] += weight
                else:
                    graph.add_edge(u, v, weight=weight)

    weak_edges = [
        (u, v)
        for u, v, weight in graph.edges(data="weight")
        if weight < min_edge_w
    ]
    graph.remove_edges_from(weak_edges)
    return graph, len(weak_edges)


def _cluster_user_graph(graph: nx.Graph, big_component: int = BIG_COMPONENT) -> dict[str, int]:
    """Assign cluster IDs from connected components and Louvain communities.

    Args:
        graph: Weighted user-user graph.
        big_component: Components larger than this are split with Louvain.

    Returns:
        Mapping from user ID to integer cluster ID. Singletons are omitted.
    """

    clusters: dict[str, int] = {}
    cid = 0
    for component in nx.connected_components(graph):
        if len(component) <= 1:
            continue
        if len(component) > big_component:
            subgraph = graph.subgraph(component)
            communities = nx.community.louvain_communities(
                subgraph, weight="weight", seed=1
            )
            for community in communities:
                cid += 1
                for user_id in community:
                    clusters[user_id] = cid
        else:
            cid += 1
            for user_id in component:
                clusters[user_id] = cid
    return clusters


def _burstiness(ts: pd.Series) -> float:
    """Calculate median inter-registration gap in hours.

    Args:
        ts: Registration timestamps for one cluster.

    Returns:
        Median gap in hours, or ``nan`` for clusters with fewer than three
        timestamps.
    """

    if len(ts) < 3:
        return float("nan")
    gaps = np.diff(np.sort(ts.values)).astype("timedelta64[s]").astype(float)
    return float(np.median(gaps) / 3600)


def score_clusters(users: pd.DataFrame, k_shrink: int = K_SHRINK) -> pd.DataFrame:
    """Score Method 1 clusters by shrunk CAPTCHA rate and burstiness.

    Args:
        users: User table containing ``cluster_m1`` and ``captcha_hit``.
        k_shrink: Pseudo-observations toward the global CAPTCHA base rate.

    Returns:
        Cluster score table sorted by ``captcha_shrunk`` descending.
    """

    base_rate = users.captcha_hit.mean()
    rows: list[dict[str, Any]] = []
    for cluster_id, group in users.dropna(subset=["cluster_m1"]).groupby("cluster_m1"):
        n = len(group)
        shrunk = (group.captcha_hit.sum() + k_shrink * base_rate) / (n + k_shrink)
        rows.append(
            {
                "cluster": int(cluster_id),
                "size": n,
                "captcha_raw": group.captcha_hit.mean(),
                "captcha_shrunk": shrunk,
                "med_reg_gap_h": _burstiness(group.reg_ts),
                "top_asn": group.asn.mode()[0],
                "majority_truth": group.group.mode()[0],
            }
        )
    return pd.DataFrame(rows).sort_values("captcha_shrunk", ascending=False)


def run_identifier_graph(
    users: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, nx.Graph, pd.Series, int]:
    """Run Method 1 and attach ``cluster_m1`` to the user table.

    Args:
        users: Synthetic user table from ``generate_data.py``.

    Returns:
        ``(users_with_clusters, scores, user_graph, original_degrees,
        weak_edge_count)``.
    """

    bipartite = _build_bipartite_graph(users)
    original_degrees = _identifier_degrees(bipartite)
    pruned = _prune_promiscuous_identifiers(bipartite)
    print("Pruned promiscuous identifiers:")
    print(pruned.to_string() if len(pruned) else "  (none)")

    user_graph, weak_count = _project_to_user_graph(bipartite, users)
    print(
        f"\nProjected graph: {user_graph.number_of_nodes()} users, "
        f"{user_graph.number_of_edges()} edges ({weak_count} weak edges pruned)"
    )

    clusters = _cluster_user_graph(user_graph)
    users = users.copy()
    users["cluster_m1"] = users.user_id.map(clusters).astype("Int64")
    print(
        f"{users.cluster_m1.notna().sum()} users in {len(set(clusters.values()))} "
        f"clusters; {users.cluster_m1.isna().sum()} singletons"
    )

    scores = score_clusters(users)
    return users, scores, user_graph, original_degrees, weak_count


def _plot_degree_distribution(ax: Axes, degrees: pd.Series) -> None:
    """Plot identifier degree distribution."""

    ax.hist(degrees.values, bins=np.logspace(0, 2.5, 30), color="#4878a8")
    ax.axvline(DEGREE_CAP, color="crimson", ls="--", label=f"degree cap = {DEGREE_CAP}")
    ax.set(
        xscale="log",
        yscale="log",
        xlabel="users per identifier",
        ylabel="identifier count",
        title="Identifier degree distribution\n(prune the right tail)",
    )
    ax.legend()


def _plot_user_projection(ax: Axes, users: pd.DataFrame, graph: nx.Graph) -> None:
    """Plot clustered user-user projection colored by ground truth."""

    clustered = users.dropna(subset=["cluster_m1"])
    subgraph = graph.subgraph(clustered.user_id)
    pos = nx.spring_layout(subgraph, seed=2, k=0.3)
    colors = clustered.set_index("user_id").group.map(PALETTE)
    nx.draw_networkx_nodes(
        subgraph,
        pos,
        node_size=18,
        ax=ax,
        node_color=[colors[node] for node in subgraph.nodes],
    )
    nx.draw_networkx_edges(subgraph, pos, alpha=0.15, ax=ax)
    for group, color in PALETTE.items():
        ax.scatter([], [], color=color, label=group, s=30)
    ax.legend(fontsize=8)
    ax.set_axis_off()
    ax.set_title(
        "User-user projection, coloured by ground truth\n"
        "(ring_careful absent: nothing to link)"
    )


def _plot_cluster_scores(ax: Axes, users: pd.DataFrame, scores: pd.DataFrame) -> None:
    """Plot cluster size against shrunk CAPTCHA rate."""

    base_rate = users.captcha_hit.mean()
    s5 = scores[scores["size"] >= 3]
    truth_col = s5.majority_truth.map(PALETTE)
    ax.scatter(s5["size"], s5.captcha_shrunk, c=truth_col, s=50)
    ax.axhline(base_rate, color="grey", ls=":", label=f"base rate {base_rate:.02f}")
    ax.set(
        xscale="log",
        xlabel="cluster size",
        ylabel="shrunk captcha rate",
        title="Cluster scoring: size vs shrunk captcha rate\n"
        "(travel agent sits at base rate)",
    )
    ax.legend()


def plot_identifier_graph_results(
    users: pd.DataFrame,
    scores: pd.DataFrame,
    graph: nx.Graph,
    degrees: pd.Series,
    output_path: Path,
) -> None:
    """Write the Method 1 figure.

    Args:
        users: User table with Method 1 clusters attached.
        scores: Cluster score table.
        graph: Weighted user-user graph.
        degrees: Identifier degree distribution before pruning.
        output_path: PNG file path to write.

    Returns:
        ``None``. Writes a PNG figure.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    _plot_degree_distribution(axes[0], degrees)
    _plot_user_projection(axes[1], users, graph)
    _plot_cluster_scores(axes[2], users, scores)
    fig.tight_layout()
    fig.savefig(output_path, dpi=140)
    plt.close(fig)


def main() -> None:
    """Run Method 1, write ``users_m1.csv``, and update the Methodology figure."""

    users = pd.read_csv(DATA_DIR / "users.csv", parse_dates=["reg_ts"])
    users, scores, graph, degrees, _weak_count = run_identifier_graph(users)

    print("\nTop clusters by shrunk captcha rate (size >= 5):")
    print(
        scores[scores["size"] >= 5]
        .head(10)
        .to_string(index=False, float_format=lambda x: f"{x:.3f}")
    )

    print("\nDetection by ground-truth group (share of members in any cluster of size>=5):")
    big = set(scores[scores["size"] >= 5].cluster)
    users["in_big_cluster"] = users.cluster_m1.isin(big)
    print(
        users.groupby("group").in_big_cluster.mean().to_string(
            float_format=lambda x: f"{x:.2f}"
        )
    )

    plot_identifier_graph_results(
        users,
        scores,
        graph,
        degrees,
        IMAGE_DIR / "method1_identifier_graph.png",
    )
    print("\nSaved method1_identifier_graph.png")
    users.to_csv(DATA_DIR / "users_m1.csv", index=False)


if __name__ == "__main__":
    main()
