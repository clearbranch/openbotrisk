"""Sensitivity sweep for the Method 2 time-bucket width.

The synchrony method has a central tuning problem: buckets must be wide enough
to span a ring's internal jitter, but every widening admits more coincidental
co-occurrence from legitimate users. This script runs the same clustering logic
across several bucket widths and plots detection share by ground-truth group.

Example:
    ```bash
    python src/openbotrisk/experiments/identifier_synchrony/generate_data.py
    python src/openbotrisk/experiments/identifier_synchrony/method2_bucket_sweep.py
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
    from .method2_synchrony import (
        JACCARD_MIN,
        MIN_SHARED,
        PALETTE,
        TOKEN_USER_CAP,
        _build_similarity_graph,
        _build_user_tokens,
        _cluster_components,
        _count_shared_tokens,
    )
except ImportError:  # pragma: no cover - supports direct script execution
    from method2_synchrony import (
        JACCARD_MIN,
        MIN_SHARED,
        PALETTE,
        TOKEN_USER_CAP,
        _build_similarity_graph,
        _build_user_tokens,
        _cluster_components,
        _count_shared_tokens,
    )


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[3]
DATA_DIR = REPO_ROOT / "experiments" / "identifier-synchrony" / "generated"
IMAGE_DIR = REPO_ROOT / "site" / "methodology" / "images"

BUCKET_GRID = [0.5, 1, 2, 4, 8, 16]


def run_bucket(
    events: pd.DataFrame,
    users: pd.DataFrame,
    bucket_hours: float,
    *,
    jaccard_min: float = JACCARD_MIN,
    min_shared: int = MIN_SHARED,
    token_user_cap: int = TOKEN_USER_CAP,
) -> pd.Series:
    """Run synchrony clustering for one bucket width.

    Args:
        events: Event table from ``generate_data.py``.
        users: User table from ``generate_data.py``.
        bucket_hours: Width of each overlapping time bucket in hours.
        jaccard_min: Minimum Jaccard similarity for an edge.
        min_shared: Minimum shared-token count for an edge.
        token_user_cap: Drop tokens touched by more users than this cap.

    Returns:
        Detection share by ground-truth group for the bucket width.

    Example:
        ```python
        detection = run_bucket(events, users, bucket_hours=2)
        assert 0 <= detection["ring_lazy"] <= 1
        ```
    """

    bucket = pd.Timedelta(hours=bucket_hours)
    user_tokens = _build_user_tokens(events, bucket)
    pair_shared, _token_count, _dropped = _count_shared_tokens(
        user_tokens, token_user_cap
    )
    graph = _build_similarity_graph(
        users.user_id,
        user_tokens,
        pair_shared,
        min_shared=min_shared,
        jaccard_min=jaccard_min,
    )
    detected = set(_cluster_components(graph, min_size=3))
    by_user = pd.Series(
        {user_id: user_id in detected for user_id in users.user_id},
        name="detected",
    )
    by_user.index.name = "user_id"
    truth = users.set_index("user_id").group
    return by_user.groupby(truth).mean()


def run_bucket_sweep(
    events: pd.DataFrame,
    users: pd.DataFrame,
    bucket_grid: list[float] = BUCKET_GRID,
) -> pd.DataFrame:
    """Run Method 2 over a grid of bucket widths.

    Args:
        events: Event table from ``generate_data.py``.
        users: User table from ``generate_data.py``.
        bucket_grid: Bucket widths, in hours.

    Returns:
        DataFrame indexed by bucket width, with one detection column per
        ground-truth group.
    """

    results = pd.DataFrame(
        {bucket: run_bucket(events, users, bucket) for bucket in bucket_grid}
    ).T
    results.index.name = "bucket_h"
    return results


def _plot_bucket_sweep(ax: Axes, results: pd.DataFrame) -> None:
    """Plot bucket-width sensitivity curves."""

    for group in results.columns:
        ax.plot(results.index, results[group], "o-", color=PALETTE[group], label=group)
    ax.set(
        xscale="log",
        xlabel="time-bucket width (hours)",
        ylabel="share of group detected",
        title="Method 2 sensitivity to bucket width\n"
        "wider buckets catch looser rings -- and eventually legit users",
    )
    ax.legend()


def plot_bucket_sweep(results: pd.DataFrame, output_path: Path) -> None:
    """Write the bucket-sensitivity plot.

    Args:
        results: Output from ``run_bucket_sweep``.
        output_path: PNG path to write.

    Returns:
        ``None``. The figure is written to disk.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 5))
    _plot_bucket_sweep(ax, results)
    plt.tight_layout()
    plt.savefig(output_path, dpi=140)
    plt.close(fig)


def main() -> None:
    """Run the bucket-width sweep and write its figure."""

    events = pd.read_csv(DATA_DIR / "events.csv", parse_dates=["ts"])
    users = pd.read_csv(DATA_DIR / "users.csv", parse_dates=["reg_ts"])
    results = run_bucket_sweep(events, users)
    print(results.to_string(float_format=lambda x: f"{x:.2f}"))
    plot_bucket_sweep(results, IMAGE_DIR / "method2_bucket_sweep.png")
    print("Saved method2_bucket_sweep.png")


if __name__ == "__main__":
    main()
