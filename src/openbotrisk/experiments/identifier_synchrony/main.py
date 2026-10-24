"""Run the full identifier/synchrony experiment pipeline end to end.

The stages must run in dependency order because they chain through CSVs in
``DATA_DIR``: ``generate_data`` writes ``users.csv``/``events.csv``; Method 1
writes ``users_m1.csv``; Method 2 reads it and writes ``users_final.csv``; the
bucket and parameter sweeps read the generated data. This orchestrator runs
them in order, finishing with the Method 1 and Method 2 sensitivity sweeps.

It is also the single place to tune the pipeline: edit the control-panel
constants below. Each stage script still runs standalone with its own
module-level defaults, so these values intentionally mirror those defaults.

Example:
    ```bash
    python src/openbotrisk/experiments/identifier_synchrony/main.py
    ```
"""

from __future__ import annotations

# ruff: noqa: I001

import pandas as pd

from openbotrisk.config import IMAGE_DIR

try:
    from . import (
        concept_figures,
        generate_data,
        method1_ablation,
        method1_identifier_graph,
        method1_param_sweep,
        method2_bucket_sweep,
        method2_param_sweep,
        method2_synchrony,
    )
except ImportError:  # pragma: no cover - supports direct script execution
    import concept_figures
    import generate_data
    import method1_ablation
    import method1_identifier_graph
    import method1_param_sweep
    import method2_bucket_sweep
    import method2_param_sweep
    import method2_synchrony


# --- Control panel: edit these to tune the pipeline -----------------------

# Stage 0 - synthetic data generation
SEED = 42
START = pd.Timestamp("2026-01-01")
HORIZON_DAYS = 120

# Stage 1 - identifier graph (Method 1)
ID_TYPES = {
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

# Stage 2 - behavioural synchrony (Method 2)
BUCKET = pd.Timedelta(hours=1)
JACCARD_MIN = 0.25
MIN_SHARED = 5
TOKEN_USER_CAP = 80

# Stage 3 - bucket-width sweep
BUCKET_GRID = [0.5, 1, 2, 4, 8, 16]

# Stage 4 - Method 1 parameter sweeps
DEGREE_CAP_GRID = [10, 20, 40, 80, 160, 320]
MIN_EDGE_W_GRID = [0.2, 0.4, 0.8, 1.6, 3.2]

# Stage 5 - Method 2 Jaccard sweep
JACCARD_GRID = [0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5]


def main() -> None:
    """Run every pipeline stage in dependency order, ending with the sweeps."""

    print("=== Stage 0: generate synthetic data ===")
    generate_data.main(seed=SEED, start=START, horizon_days=HORIZON_DAYS)

    print("\n=== Stage 1: identifier graph (Method 1) ===")
    method1_identifier_graph.main(
        id_types=ID_TYPES,
        degree_cap=DEGREE_CAP,
        min_edge_w=MIN_EDGE_W,
        big_component=BIG_COMPONENT,
        k_shrink=K_SHRINK,
    )

    print("\n=== Stage 2: behavioural synchrony (Method 2) ===")
    method2_synchrony.main(
        bucket=BUCKET,
        jaccard_min=JACCARD_MIN,
        min_shared=MIN_SHARED,
        token_user_cap=TOKEN_USER_CAP,
    )

    print("\n=== Stage 3: bucket-width sweep ===")
    method2_bucket_sweep.main(
        bucket_grid=BUCKET_GRID,
        jaccard_min=JACCARD_MIN,
        min_shared=MIN_SHARED,
        token_user_cap=TOKEN_USER_CAP,
    )

    print("\n=== Stage 4: Method 1 parameter sweeps ===")
    method1_param_sweep.main(
        degree_cap_grid=DEGREE_CAP_GRID,
        min_edge_w_grid=MIN_EDGE_W_GRID,
    )

    print("\n=== Stage 5: Method 2 Jaccard sweep ===")
    method2_param_sweep.main(grid=JACCARD_GRID)

    print("\n=== Stage 6: concept illustrations (independent of the data) ===")
    concept_figures.main(out_dir=IMAGE_DIR)

    print("\n=== Stage 7: Method 1 recovery ablation ===")
    method1_ablation.main()

    print("\nPipeline complete.")


if __name__ == "__main__":
    main()
