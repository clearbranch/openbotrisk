"""Sensitivity sweep for the Method 2 Jaccard threshold.

With the time bucket fixed at its default one hour, this script varies the
minimum Jaccard similarity required for a synchrony edge and plots detection
share by ground-truth group. It complements ``method2_bucket_sweep.py``: the
bucket controls how much jitter a ring can have, the Jaccard floor controls how
much of a pair's behaviour must overlap.

Example:
    ```bash
    python src/openbotrisk/experiments/identifier_synchrony/generate_data.py
    python src/openbotrisk/experiments/identifier_synchrony/method2_param_sweep.py
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
    from .method2_bucket_sweep import run_bucket
    from .method2_synchrony import JACCARD_MIN, PALETTE
except ImportError:  # pragma: no cover - supports direct script execution
    from method2_bucket_sweep import run_bucket
    from method2_synchrony import JACCARD_MIN, PALETTE


from openbotrisk.config import EXPERIMENTS_DIR, IMAGE_DIR

GENERATED_DIR = EXPERIMENTS_DIR / "identifier-synchrony" / "generated"

FIXED_BUCKET_H = 1.0
JACCARD_GRID = [0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5]

# Detection share at default settings (jaccard_min=0.25, 1h bucket), used to
# guard against accidental behaviour drift.
DEFAULT_DETECTION = {
    "legit": 0.0,
    "ring_careful": 0.48,
    "ring_lazy": 0.95,
    "ring_mid": 0.0,
    "travel_agent": 0.0,
}


def run_jaccard_sweep(
    events: pd.DataFrame,
    users: pd.DataFrame,
    grid: list[float] = JACCARD_GRID,
) -> pd.DataFrame:
    """Sweep the Jaccard floor with the bucket fixed at one hour.

    Args:
        events: Event table from ``generate_data.py``.
        users: User table from ``generate_data.py``.
        grid: Jaccard thresholds to evaluate.

    Returns:
        DataFrame indexed by Jaccard threshold, one detection column per group.
    """

    results = pd.DataFrame(
        {
            jaccard: run_bucket(events, users, FIXED_BUCKET_H, jaccard_min=jaccard)
            for jaccard in grid
        }
    ).T
    results.index.name = "jaccard_min"
    return results


def _plot_jaccard_sweep(ax: Axes, results: pd.DataFrame) -> None:
    """Plot Jaccard-threshold detection curves by group."""

    for group in results.columns:
        ax.plot(results.index, results[group], "o-", color=PALETTE[group], label=group)
    ax.set(
        xlabel="minimum Jaccard similarity",
        ylabel="share of group detected",
        ylim=(-0.05, 1.05),
        title="Method 2 sensitivity to the Jaccard floor (1h bucket)\n"
        "stricter thresholds shed loose rings before legit noise",
    )
    ax.legend(fontsize=8)


def plot_jaccard_sweep(results: pd.DataFrame, output_path: Path) -> None:
    """Write the Jaccard-sweep figure.

    Args:
        results: Output of ``run_jaccard_sweep``.
        output_path: PNG path to write.

    Returns:
        ``None``. The figure is written to disk.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 5))
    _plot_jaccard_sweep(ax, results)
    fig.tight_layout()
    fig.savefig(output_path, dpi=140)
    plt.close(fig)


def _check_default(results: pd.DataFrame) -> pd.Series:
    """Print and verify the default-parameter detection shares.

    Args:
        results: A sweep result whose index includes ``JACCARD_MIN``.

    Returns:
        The default-parameter detection share by group.

    Raises:
        AssertionError: If any group's share drifts from the documented
            baseline by more than 0.005.
    """

    share = results.loc[JACCARD_MIN]
    expected = pd.Series(DEFAULT_DETECTION).reindex(share.index)
    print(f"\nDefault-parameter check (jaccard_min={JACCARD_MIN}, bucket={FIXED_BUCKET_H}h):")
    print(share.to_string(float_format=lambda x: f"{x:.2f}"))
    drift = {
        g: (round(float(share[g]), 2), float(expected[g]))
        for g in expected.index
        if abs(float(share[g]) - float(expected[g])) > 0.005
    }
    if drift:
        raise AssertionError(f"Method 2 default detection drifted from baseline: {drift}")
    print("OK: Method 2 default detection matches the documented baseline.")
    return share


def main(*, grid: list[float] = JACCARD_GRID) -> None:
    """Run the Jaccard sweep and write its outputs."""

    events = pd.read_csv(GENERATED_DIR / "events.csv", parse_dates=["ts"])
    users = pd.read_csv(GENERATED_DIR / "users.csv", parse_dates=["reg_ts"])
    results = run_jaccard_sweep(events, users, grid)
    results.to_csv(GENERATED_DIR / "method2_jaccard_sweep.csv")

    print("Jaccard sweep:")
    print(results.to_string(float_format=lambda x: f"{x:.2f}"))

    _check_default(results)

    plot_jaccard_sweep(results, IMAGE_DIR / "method2_jaccard_sweep.png")
    print("\nSaved method2_jaccard_sweep.png")


if __name__ == "__main__":
    main()
