"""Clustering-quality recovery metrics for the identifier/synchrony experiment."""

from __future__ import annotations

from collections import Counter, defaultdict
from collections.abc import Mapping
from typing import Any

import pandas as pd

GROUP_ORDER = ["ring_lazy", "ring_careful", "ring_mid", "travel_agent", "hybrid"]


def _cluster_items(clusters: Mapping[str, Any] | pd.Series) -> list[tuple[str, Any]]:
    """Return non-null ``(user_id, cluster_id)`` pairs from a cluster mapping."""

    items = clusters.items() if isinstance(clusters, pd.Series) else clusters.items()
    return [(user_id, cluster_id) for user_id, cluster_id in items if not pd.isna(cluster_id)]


def _evaluation_groups(users: pd.DataFrame) -> list[str]:
    """Return non-legit groups in stable reporting order."""

    present = set(users["group"])
    ordered = [group for group in GROUP_ORDER if group in present]
    extras = sorted(present - set(ordered) - {"legit"})
    return ordered + extras


def recovery(
    users: pd.DataFrame,
    clusters: Mapping[str, Any] | pd.Series,
    size_min: int = 3,
) -> tuple[dict[str, dict[str, float]], dict[str, int]]:
    """Evaluate how cleanly clusters recover ground-truth groups.

    Args:
        users: User table containing ``user_id`` and ``group``.
        clusters: Mapping from user ID to cluster ID. Null cluster IDs are
            treated as singletons and ignored.
        size_min: Minimum cluster size to evaluate.

    Returns:
        ``(per_group, spurious)``. ``per_group[group]`` contains ``coverage``,
        ``pieces``, and ``purity``. ``spurious`` contains counts for legitimate
        accounts swept into evaluated clusters, legitimate-majority clusters,
        and mixed clusters with purity below 0.8.
    """

    group_by_user = users.set_index("user_id").group.to_dict()
    members: dict[Any, list[str]] = defaultdict(list)
    for user_id, cluster_id in _cluster_items(clusters):
        members[cluster_id].append(user_id)

    info: dict[Any, dict[str, Any]] = {}
    for cluster_id, user_ids in members.items():
        if len(user_ids) < size_min:
            continue
        composition = Counter(group_by_user[user_id] for user_id in user_ids)
        majority, majority_n = composition.most_common(1)[0]
        info[cluster_id] = {
            "size": len(user_ids),
            "composition": composition,
            "majority": majority,
            "purity": majority_n / len(user_ids),
        }

    per_group: dict[str, dict[str, float]] = {}
    for group in _evaluation_groups(users):
        group_clusters = [
            cluster_id
            for cluster_id, cluster_info in info.items()
            if cluster_info["majority"] == group
        ]
        group_users = set(users.loc[users.group == group, "user_id"])
        covered: set[str] = set()
        total_members = 0
        true_members = 0
        for cluster_id in group_clusters:
            cluster_users = set(members[cluster_id])
            covered |= cluster_users & group_users
            total_members += len(cluster_users)
            true_members += sum(user_id in group_users for user_id in cluster_users)
        per_group[group] = {
            "coverage": len(covered) / len(group_users) if group_users else 0.0,
            "pieces": float(len(group_clusters)),
            "purity": true_members / total_members if total_members else float("nan"),
        }

    spurious = {
        "legit_clustered": sum(
            1
            for cluster_id in info
            for user_id in members[cluster_id]
            if group_by_user[user_id] == "legit"
        ),
        "n_legit_majority": sum(
            1 for cluster_info in info.values() if cluster_info["majority"] == "legit"
        ),
        "n_mixed": sum(1 for cluster_info in info.values() if cluster_info["purity"] < 0.8),
    }
    return per_group, spurious
