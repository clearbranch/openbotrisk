"""Method 1 recovery ablation for easy and hard synthetic data."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import networkx as nx
import pandas as pd

from openbotrisk.config import EXPERIMENTS_DIR

try:
    from . import generate_data
    from . import method1_identifier_graph as m1
    from .recovery_metric import GROUP_ORDER, recovery
except ImportError:  # pragma: no cover - supports direct script execution
    import generate_data
    import method1_identifier_graph as m1
    from recovery_metric import GROUP_ORDER, recovery

GENERATED_DIR = EXPERIMENTS_DIR / "identifier-synchrony" / "generated"

CONFIDENT_ID_TYPES = {"card": 3.0, "email": 2.5, "phone": 2.5}
FUZZY_ID_TYPES = {"fuzzy_id": 2.5}
RECOVERY_SIZE_MIN = 3
DETECTION_SIZE_MIN = 5


def _id_types(users: pd.DataFrame) -> dict[str, float]:
    """Return Method 1 identifiers, including ``fuzzy_id`` only when present."""

    id_types = dict(m1.ID_TYPES)
    if "fuzzy_id" in users.columns:
        id_types.update(FUZZY_ID_TYPES)
    return id_types


def _components(graph: nx.Graph) -> dict[str, int]:
    """Assign component IDs to every graph node."""

    clusters: dict[str, int] = {}
    for cluster_id, component in enumerate(nx.connected_components(graph)):
        for node in component:
            clusters[node] = cluster_id
    return clusters


def _project(
    users: pd.DataFrame,
    id_types: Mapping[str, float],
    min_edge_w: float,
    degree_cap: int | None = None,
) -> nx.Graph:
    """Build a projected user graph for one rung."""

    bipartite = m1._build_bipartite_graph(users, id_types)
    if degree_cap is not None:
        m1._prune_promiscuous_identifiers(bipartite, degree_cap)
    graph, _weak_edges = m1._project_to_user_graph(bipartite, users, id_types, min_edge_w)
    return graph


def _scored_clusters(users: pd.DataFrame, id_types: Mapping[str, float]) -> dict[str, int]:
    """Run full Method 1 and keep clusters that pass the existing size threshold."""

    clustered, scores, _graph, _degrees, _weak = m1.run_identifier_graph(
        users,
        id_types=id_types,
        degree_cap=m1.DEGREE_CAP,
        min_edge_w=m1.MIN_EDGE_W,
        big_component=m1.BIG_COMPONENT,
        k_shrink=m1.K_SHRINK,
        verbose=False,
    )
    scored = set(scores.loc[scores["size"] >= DETECTION_SIZE_MIN, "cluster"])
    cluster_map = clustered.dropna(subset=["cluster_m1"]).set_index("user_id").cluster_m1
    return {
        user_id: int(cluster_id)
        for user_id, cluster_id in cluster_map.items()
        if int(cluster_id) in scored
    }


def _rungs(users: pd.DataFrame) -> list[tuple[str, dict[str, int]]]:
    """Run each Method 1 ablation rung and return cluster mappings."""

    all_ids = _id_types(users)
    graph = _project(users, all_ids, min_edge_w=0.0)
    raw = _components(graph)

    graph = _project(users, CONFIDENT_ID_TYPES, min_edge_w=0.0)
    confident = _components(graph)

    graph = _project(users, all_ids, min_edge_w=0.0, degree_cap=m1.DEGREE_CAP)
    pruned = _components(graph)

    graph = _project(users, all_ids, min_edge_w=m1.MIN_EDGE_W, degree_cap=m1.DEGREE_CAP)
    weighted = _components(graph)
    community = m1._cluster_user_graph(graph, big_component=m1.BIG_COMPONENT)
    scoring = _scored_clusters(users, all_ids)

    return [
        ("0. raw projection (all ids)", raw),
        ("1. confident ids only", confident),
        ("2. all ids + prune (cap 40)", pruned),
        ("3. + weight floor 0.8", weighted),
        ("4. + community", community),
        ("5. + scoring", scoring),
    ]


def _fmt(metric: dict[str, float]) -> str:
    """Format one recovery cell as ``coverage/pieces/purity``."""

    purity = metric["purity"]
    purity_s = "nan" if pd.isna(purity) else f"{purity:.2f}"
    return f"{metric['coverage']:.2f}/{int(metric['pieces'])}/{purity_s}"


def _print_table(label: str, results: list[dict[str, Any]]) -> None:
    """Print the console table in the reference ablation style."""

    groups = [
        group
        for group in GROUP_ORDER
        if any(group in row["per_group"] for row in results)
    ]
    print(f"\nMethod 1 recovery ablation ({label})")
    print("cells are coverage/pieces/purity   (want coverage high, purity high)")
    group_header = "".join(f"{group:<18}" for group in groups)
    print(f"{'rung':<34} {group_header}spurious structure")
    print("-" * (36 + 18 * len(groups) + 34))
    for row in results:
        cells = "".join(
            f"{_fmt(row['per_group'][group]):<18}"
            if group in row["per_group"]
            else f"{'':<18}"
            for group in groups
        )
        spurious = row["spurious"]
        print(
            f"{row['rung_name']:<34} {cells}"
            f"legit_in={spurious['legit_clustered']:<4} "
            f"spur={spurious['n_legit_majority']:<3} mixed={spurious['n_mixed']}"
        )


def _rows(label: str, results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Flatten nested recovery results for CSV output."""

    rows: list[dict[str, Any]] = []
    for rung_index, result in enumerate(results):
        for group, metric in result["per_group"].items():
            rows.append(
                {
                    "dataset": label,
                    "rung_index": rung_index,
                    "rung_name": result["rung_name"],
                    "group": group,
                    "coverage": metric["coverage"],
                    "pieces": int(metric["pieces"]),
                    "purity": metric["purity"],
                    **result["spurious"],
                }
            )
    return rows


def run_ablation(*, hard: bool) -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    """Run the Method 1 ablation on one data mode."""

    users, events = generate_data.generate_synthetic_data(hard=hard)
    if not hard:
        generate_data._assert_default_population(users, events)
        ok, detail = generate_data.check_default_population(users, events)
        print(f"Default determinism check: {'OK' if ok else 'FAILED'} - {detail}")

    results: list[dict[str, Any]] = []
    for rung_name, clusters in _rungs(users):
        per_group, spurious = recovery(users, clusters, size_min=RECOVERY_SIZE_MIN)
        results.append(
            {
                "rung_name": rung_name,
                "per_group": per_group,
                "spurious": spurious,
            }
        )

    label = "hard" if hard else "easy"
    _print_table(label, results)
    return pd.DataFrame(_rows(label, results)), results


def main() -> None:
    """Run easy and hard Method 1 ablations and write CSV outputs."""

    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    easy, _easy_results = run_ablation(hard=False)
    hard, _hard_results = run_ablation(hard=True)
    easy.to_csv(GENERATED_DIR / "method1_ablation_easy.csv", index=False)
    hard.to_csv(GENERATED_DIR / "method1_ablation_hard.csv", index=False)
    print("\nSaved method1_ablation_easy.csv and method1_ablation_hard.csv")


if __name__ == "__main__":
    main()
