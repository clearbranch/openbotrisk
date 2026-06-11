"""Behavioural-synchrony clustering for the synthetic account dataset.

Identifiers are cheap to randomise; coordination is not. This method links
accounts that repeatedly do the same thing to the same target at nearly the
same time, even when they share no identifiers.

The implementation is a simplified SynchroTrap-style pipeline:

1. turn each event into overlapping ``(action, target, time_bucket)`` tokens;
2. build an inverted index from token to users;
3. count only user pairs that co-occur in at least one token;
4. keep high-Jaccard edges and call connected components synchrony clusters.

Example:
    Run after generating the synthetic data and Method 1 clusters:

    ```bash
    python src/openbotrisk/experiments/identifier_synchrony/generate_data.py
    python src/openbotrisk/experiments/identifier_synchrony/method1_identifier_graph.py
    python src/openbotrisk/experiments/identifier_synchrony/method2_synchrony.py
    ```
"""

from __future__ import annotations

# ruff: noqa: E402,I001

import os
from collections import defaultdict
from collections.abc import Iterable
from itertools import combinations
from pathlib import Path
from typing import TypeAlias

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from matplotlib.axes import Axes


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[3]
DATA_DIR = REPO_ROOT / "experiments" / "identifier-synchrony" / "generated"
IMAGE_DIR = REPO_ROOT / "site" / "methodology" / "images"

BUCKET = pd.Timedelta(hours=1)
JACCARD_MIN = 0.25
MIN_SHARED = 5
TOKEN_USER_CAP = 80

Token: TypeAlias = tuple[str, str, int]
UserTokens: TypeAlias = dict[str, set[Token]]

PALETTE = {
    "legit": "#b8b8b8",
    "travel_agent": "#2a9d2a",
    "ring_lazy": "#d62728",
    "ring_careful": "#9467bd",
    "ring_mid": "#ff7f0e",
}


def _overlapping_buckets(
    ts: pd.Timestamp,
    t0: pd.Timestamp,
    bucket: pd.Timedelta = BUCKET,
) -> tuple[int, int]:
    """Return two overlapping window IDs for one timestamp.

    Args:
        ts: Event timestamp.
        t0: First timestamp in the event log.
        bucket: Width of each time bucket. The second grid is shifted by half
            a bucket so near-boundary events still co-occur.

    Returns:
        Two integer bucket IDs.
    """

    offset = (ts - t0) / bucket
    return int(offset), int(offset + 0.5) + 10**6


def _build_user_tokens(
    events: pd.DataFrame,
    bucket: pd.Timedelta = BUCKET,
) -> UserTokens:
    """Convert events into per-user sets of synchrony tokens.

    Args:
        events: Event table containing ``user_id``, ``ts``, ``action``, and
            ``target``.
        bucket: Width of each time bucket.

    Returns:
        Mapping from user ID to the user's distinct synchrony tokens.
    """

    t0 = events.ts.min()
    user_tokens: defaultdict[str, set[Token]] = defaultdict(set)
    for row in events.itertuples(index=False):
        for bucket_id in _overlapping_buckets(row.ts, t0, bucket):
            user_tokens[row.user_id].add((row.action, row.target, bucket_id))
    return dict(user_tokens)


def _count_shared_tokens(
    user_tokens: UserTokens,
    token_user_cap: int = TOKEN_USER_CAP,
) -> tuple[dict[tuple[str, str], int], int, int]:
    """Count candidate-pair token overlaps with an inverted index.

    Args:
        user_tokens: Per-user synchrony-token sets.
        token_user_cap: Drop tokens touched by more users than this cap; they
            are usually trend or flash-sale noise rather than coordination.

    Returns:
        ``(pair_shared, token_count, dropped_token_count)``.
    """

    token_users: defaultdict[Token, list[str]] = defaultdict(list)
    for user_id, tokens in user_tokens.items():
        for token in tokens:
            token_users[token].append(user_id)

    pair_shared: defaultdict[tuple[str, str], int] = defaultdict(int)
    dropped_tokens = 0
    for users in token_users.values():
        if len(users) < 2:
            continue
        if len(users) > token_user_cap:
            dropped_tokens += 1
            continue
        for user_a, user_b in combinations(sorted(users), 2):
            pair_shared[(user_a, user_b)] += 1
    return dict(pair_shared), len(token_users), dropped_tokens


def _build_similarity_graph(
    users: Iterable[str],
    user_tokens: UserTokens,
    pair_shared: dict[tuple[str, str], int],
    *,
    min_shared: int = MIN_SHARED,
    jaccard_min: float = JACCARD_MIN,
) -> nx.Graph:
    """Build a user graph from shared-token counts.

    Args:
        users: User IDs to include as graph nodes.
        user_tokens: Per-user synchrony-token sets.
        pair_shared: Candidate pair overlap counts.
        min_shared: Minimum shared-token count before considering Jaccard.
        jaccard_min: Minimum Jaccard similarity for an edge.

    Returns:
        A weighted ``networkx.Graph`` where edge weights are Jaccard scores.
    """

    graph = nx.Graph()
    graph.add_nodes_from(users)
    for (user_a, user_b), shared in pair_shared.items():
        if shared < min_shared:
            continue
        denom = len(user_tokens[user_a]) + len(user_tokens[user_b]) - shared
        jaccard = shared / denom
        if jaccard >= jaccard_min:
            graph.add_edge(user_a, user_b, weight=jaccard)
    return graph


def _cluster_components(graph: nx.Graph, min_size: int = 3) -> dict[str, int]:
    """Assign cluster IDs to connected components.

    Args:
        graph: User similarity graph.
        min_size: Minimum component size to call a synchrony cluster.

    Returns:
        Mapping from user ID to integer cluster ID. Small components are
        omitted.
    """

    clusters: dict[str, int] = {}
    cluster_id = 0
    for component in nx.connected_components(graph):
        if len(component) < min_size:
            continue
        cluster_id += 1
        for user_id in component:
            clusters[user_id] = cluster_id
    return clusters


def run_synchrony_clustering(
    users: pd.DataFrame,
    events: pd.DataFrame,
) -> tuple[pd.DataFrame, nx.Graph, pd.DataFrame]:
    """Run Method 2 and attach ``cluster_m2`` to the user table.

    Args:
        users: User table, usually the ``users_m1.csv`` output from Method 1.
        events: Event table from ``generate_data.py``.

    Returns:
        ``(users_with_clusters, graph, coverage)``. ``coverage`` gives the
        Method 1 and Method 2 detection share by ground-truth group.
    """

    user_tokens = _build_user_tokens(events)
    pair_shared, token_count, dropped = _count_shared_tokens(user_tokens)
    print(
        f"{token_count} tokens, {dropped} dropped as too popular, "
        f"{len(pair_shared)} candidate pairs"
    )

    graph = _build_similarity_graph(users.user_id, user_tokens, pair_shared)
    clusters = _cluster_components(graph)

    users = users.copy()
    users["cluster_m2"] = users.user_id.map(clusters).astype("Int64")
    print(
        f"\nMethod 2: {users.cluster_m2.notna().sum()} users in "
        f"{len(set(clusters.values()))} synchrony clusters"
    )

    print("\nDetection by ground-truth group (Method 2):")
    users["m2_detected"] = users.cluster_m2.notna()
    print(
        users.groupby("group").m2_detected.mean().to_string(
            float_format=lambda x: f"{x:.2f}"
        )
    )

    print("\nCluster composition (Method 2):")
    for cluster_id, group in users.dropna(subset=["cluster_m2"]).groupby(
        "cluster_m2"
    ):
        print(
            f"  cluster {int(cluster_id)}: n={len(group)}, "
            f"truth={dict(group.group.value_counts())}"
        )

    print("\nMethod 1 vs Method 2 coverage:")
    users["m1_detected"] = users.cluster_m1.notna() & users.cluster_m1.map(
        users.cluster_m1.value_counts()
    ).ge(5)
    coverage = users.groupby("group")[["m1_detected", "m2_detected"]].mean()
    print(coverage.to_string(float_format=lambda x: f"{x:.2f}"))
    return users, graph, coverage


def _plot_event_raster(ax: Axes, users: pd.DataFrame, events: pd.DataFrame) -> None:
    """Plot a sample event raster to show lockstep waves."""

    sample = pd.concat(
        [
            users[users.group == group].sample(
                min(12, (users.group == group).sum()), random_state=0
            )
            for group in PALETTE
        ]
    )
    sample_events = events[events.user_id.isin(sample.user_id)].merge(
        users[["user_id", "group"]], on="user_id"
    )
    ymap = {user_id: idx for idx, user_id in enumerate(sample.user_id)}
    ax.scatter(
        sample_events.ts,
        sample_events.user_id.map(ymap),
        s=4,
        c=sample_events.group.map(PALETTE),
        alpha=0.7,
    )
    ax.set(
        yticks=[],
        xlabel="time",
        title="Event raster (12 users/group)\nvertical stripes = lockstep waves",
    )
    for group, color in PALETTE.items():
        ax.scatter([], [], color=color, label=group, s=20)
    ax.legend(fontsize=8, loc="upper left")


def plot_synchrony_results(
    users: pd.DataFrame,
    events: pd.DataFrame,
    coverage: pd.DataFrame,
    output_path: Path,
) -> None:
    """Write the Method 2 event-raster and coverage figure.

    Args:
        users: User table with Method 2 detection columns.
        events: Event table.
        coverage: Detection share by ground-truth group.
        output_path: PNG path to write.

    Returns:
        ``None``. The figure is written to disk.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    _plot_event_raster(axes[0], users, events)

    coverage.plot.bar(ax=axes[1], color=["#4878a8", "#c44e52"])
    axes[1].set(
        ylabel="share of group detected",
        ylim=(0, 1.05),
        title="Coverage by method:\nidentifier graph vs behavioural synchrony",
    )
    axes[1].legend(["Method 1 (identifiers)", "Method 2 (synchrony)"], fontsize=9)
    axes[1].tick_params(axis="x", rotation=20)

    plt.tight_layout()
    plt.savefig(output_path, dpi=140)
    plt.close(fig)


def main() -> None:
    """Run the Method 2 experiment and write its outputs."""

    events = pd.read_csv(DATA_DIR / "events.csv", parse_dates=["ts"])
    users = pd.read_csv(DATA_DIR / "users_m1.csv", parse_dates=["reg_ts"])
    users, _graph, coverage = run_synchrony_clustering(users, events)
    plot_synchrony_results(
        users,
        events,
        coverage,
        IMAGE_DIR / "method2_synchrony.png",
    )
    print("\nSaved method2_synchrony.png")
    users.to_csv(DATA_DIR / "users_final.csv", index=False)


if __name__ == "__main__":
    main()
