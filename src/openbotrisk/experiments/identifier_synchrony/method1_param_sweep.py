"""Sensitivity sweep for the Method 1 tuning knobs.

Method 1 has two main levers: the degree cap that prunes promiscuous
identifiers before projection, and the minimum projected edge weight that keeps
a user-user link. This script reruns the identifier-graph pipeline across a grid
of each knob (holding the other at its default) and plots detection share by
ground-truth group, mirroring ``method2_bucket_sweep.py``.

Example:
    ```bash
    python src/openbotrisk/experiments/identifier_synchrony/generate_data.py
    python src/openbotrisk/experiments/identifier_synchrony/method1_param_sweep.py
    ```
"""

from __future__ import annotations

# ruff: noqa: E402,I001

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes

try:
    from .method1_identifier_graph import (
        DEGREE_CAP,
        MIN_EDGE_W,
        PALETTE,
        run_identifier_graph,
    )
except ImportError:  # pragma: no cover - supports direct script execution
    from method1_identifier_graph import (
        DEGREE_CAP,
        MIN_EDGE_W,
        PALETTE,
        run_identifier_graph,
    )


from openbotrisk.config import EXPERIMENTS_DIR, IMAGE_DIR

GENERATED_DIR = EXPERIMENTS_DIR / "identifier-synchrony" / "generated"

DEGREE_CAP_GRID = [10, 20, 40, 80, 160, 320]
MIN_EDGE_W_GRID = [0.2, 0.4, 0.8, 1.6, 3.2]

# Detection share at default settings (degree_cap=40, min_edge_w=0.8), used to
# guard against accidental behaviour drift. ``travel_agent`` is fully clustered
# at the size>=5 threshold; a separate scoring step (not clustering) clears it.
DEFAULT_DETECTION = {
    "legit": 0.0,
    "ring_careful": 0.0,
    "ring_lazy": 1.0,
    "ring_mid": 0.0,
    "travel_agent": 1.0,
}


def _detection_share(users: pd.DataFrame, scores: pd.DataFrame, min_size: int = 5) -> pd.Series:
    """Return detection share by ground-truth group for one pipeline run.

    Uses the same rule as ``method1_identifier_graph.main``: a member counts as
    detected when its ``cluster_m1`` falls in a cluster of size >= ``min_size``.

    Args:
        users: User table with ``cluster_m1`` and ``group`` columns.
        scores: Cluster score table with ``cluster`` and ``size`` columns.
        min_size: Minimum cluster size that counts as a detection.

    Returns:
        Detection share indexed by ground-truth group.
    """

    big = set(scores[scores["size"] >= min_size].cluster)
    detected = users.cluster_m1.isin(big)
    return detected.groupby(users.group).mean()


def run_param(
    users: pd.DataFrame,
    *,
    degree_cap: int = DEGREE_CAP,
    min_edge_w: float = MIN_EDGE_W,
) -> pd.Series:
    """Run Method 1 once and return detection share by ground-truth group.

    Args:
        users: User table from ``generate_data.py``.
        degree_cap: Maximum users per identifier before pruning.
        min_edge_w: Minimum projected user-user edge weight to keep.

    Returns:
        Detection share indexed by ground-truth group.
    """

    clustered, scores, _graph, _degrees, _weak = run_identifier_graph(
        users, degree_cap=degree_cap, min_edge_w=min_edge_w, verbose=False
    )
    return _detection_share(clustered, scores)


def run_degree_cap_sweep(users: pd.DataFrame, grid: list[int] = DEGREE_CAP_GRID) -> pd.DataFrame:
    """Sweep the degree cap, holding ``min_edge_w`` at its default."""

    results = pd.DataFrame({cap: run_param(users, degree_cap=cap) for cap in grid}).T
    results.index.name = "degree_cap"
    return results


def run_min_edge_w_sweep(users: pd.DataFrame, grid: list[float] = MIN_EDGE_W_GRID) -> pd.DataFrame:
    """Sweep the minimum edge weight, holding ``degree_cap`` at its default."""

    results = pd.DataFrame({w: run_param(users, min_edge_w=w) for w in grid}).T
    results.index.name = "min_edge_w"
    return results


def _plot_param_sweep(ax: Axes, results: pd.DataFrame, xlabel: str, title: str) -> None:
    """Plot one knob's detection curves by group."""

    for group in results.columns:
        ax.plot(results.index, results[group], "o-", color=PALETTE[group], label=group)
    ax.set(
        xscale="log",
        xlabel=xlabel,
        ylabel="share of group detected",
        ylim=(-0.05, 1.05),
        title=title,
    )
    ax.legend(fontsize=8)


def plot_param_sweeps(
    degree_cap_results: pd.DataFrame,
    min_edge_w_results: pd.DataFrame,
    output_path: Path,
) -> None:
    """Write the two-panel Method 1 parameter-sweep figure.

    Args:
        degree_cap_results: Output of ``run_degree_cap_sweep``.
        min_edge_w_results: Output of ``run_min_edge_w_sweep``.
        output_path: PNG path to write.

    Returns:
        ``None``. The figure is written to disk.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    _plot_param_sweep(
        axes[0],
        degree_cap_results,
        "degree cap (users per identifier)",
        "Method 1 sensitivity to the degree cap\n"
        "tighter caps prune real links; looser caps admit noise",
    )
    _plot_param_sweep(
        axes[1],
        min_edge_w_results,
        "minimum projected edge weight",
        "Method 1 sensitivity to the edge-weight floor\n"
        "higher floors drop weak coincidental links",
    )
    fig.tight_layout()
    fig.savefig(output_path, dpi=140)
    plt.close(fig)


def _check_default(results: pd.DataFrame) -> pd.Series:
    """Print and verify the default-parameter detection shares.

    Args:
        results: A sweep result whose index includes ``DEGREE_CAP``.

    Returns:
        The default-parameter detection share by group.

    Raises:
        AssertionError: If any group's share drifts from the documented
            baseline by more than 0.005.
    """

    share = results.loc[DEGREE_CAP]
    expected = pd.Series(DEFAULT_DETECTION).reindex(share.index)
    print(f"\nDefault-parameter check (degree_cap={DEGREE_CAP}, min_edge_w={MIN_EDGE_W}):")
    print(share.to_string(float_format=lambda x: f"{x:.2f}"))
    drift = {
        g: (round(float(share[g]), 2), float(expected[g]))
        for g in expected.index
        if abs(float(share[g]) - float(expected[g])) > 0.005
    }
    if drift:
        raise AssertionError(f"Method 1 default detection drifted from baseline: {drift}")
    print("OK: Method 1 default detection matches the documented baseline.")
    return share


def main(
    *,
    degree_cap_grid: list[int] = DEGREE_CAP_GRID,
    min_edge_w_grid: list[float] = MIN_EDGE_W_GRID,
) -> None:
    """Run both Method 1 parameter sweeps and write their outputs."""

    users = pd.read_csv(GENERATED_DIR / "users.csv", parse_dates=["reg_ts"])
    degree_cap_results = run_degree_cap_sweep(users, degree_cap_grid)
    min_edge_w_results = run_min_edge_w_sweep(users, min_edge_w_grid)

    degree_cap_results.to_csv(GENERATED_DIR / "method1_degree_cap_sweep.csv")
    min_edge_w_results.to_csv(GENERATED_DIR / "method1_min_edge_w_sweep.csv")

    print("Degree-cap sweep:")
    print(degree_cap_results.to_string(float_format=lambda x: f"{x:.2f}"))
    print("\nMin-edge-weight sweep:")
    print(min_edge_w_results.to_string(float_format=lambda x: f"{x:.2f}"))

    _check_default(degree_cap_results)

    plot_param_sweeps(
        degree_cap_results, min_edge_w_results, IMAGE_DIR / "method1_param_sweep.png"
    )
    print("\nSaved method1_param_sweep.png")


if __name__ == "__main__":
    main()
