"""Dataset loaders for the three EDA datasets.

Each function returns a dict of summary metadata + small pandas frames suitable
for downstream descriptive analysis. Large files are summarised via DuckDB /
polars streaming rather than being fully materialised in memory.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Dict, Any, List

import duckdb
import pandas as pd
import polars as pl


# ---------------------------------------------------------------------------
# TalkingData
# ---------------------------------------------------------------------------
def load_talkingdata_meta(data_dir: str | os.PathLike) -> Dict[str, Any]:
    """Summarise the TalkingData train.csv using DuckDB in a single scan."""
    data_dir = Path(data_dir)
    train = data_dir / "train.csv"
    test = data_dir / "test.csv"

    con = duckdb.connect()
    # Default schema inference (first 20480 rows) — fast.
    con.execute(f"CREATE VIEW train AS SELECT * FROM read_csv_auto('{train}', HEADER=TRUE)")

    schema_df = con.execute("DESCRIBE train").fetchdf()
    cols = schema_df["column_name"].tolist()

    # Single full-table scan: count, nulls, cardinality, label balance, time range.
    card_cols = ["app", "device", "os", "channel", "is_attributed", "ip"]
    null_exprs = ", ".join(
        f"SUM(CASE WHEN \"{c}\" IS NULL THEN 1 ELSE 0 END) AS null_{c}" for c in cols
    )
    card_exprs = ", ".join(
        f"COUNT(DISTINCT \"{c}\") AS card_{c}" for c in card_cols
    )
    single_pass = con.execute(f"""
        SELECT
            COUNT(*) AS row_count,
            {null_exprs},
            {card_exprs},
            SUM(CASE WHEN is_attributed = 0 THEN 1 ELSE 0 END) AS label_0,
            SUM(CASE WHEN is_attributed = 1 THEN 1 ELSE 0 END) AS label_1,
            MIN(click_time) AS t_min,
            MAX(click_time) AS t_max
        FROM train
    """).fetchdf()

    row_count = int(single_pass["row_count"].iloc[0])

    null_df = pd.DataFrame({
        "column": cols,
        "null_count": [int(single_pass[f"null_{c}"].iloc[0]) for c in cols],
    })
    null_df["null_rate"] = null_df["null_count"] / row_count

    cardinality = {c: int(single_pass[f"card_{c}"].iloc[0]) for c in card_cols}

    label_balance = pd.DataFrame({
        "is_attributed": [0, 1],
        "n": [int(single_pass["label_0"].iloc[0]), int(single_pass["label_1"].iloc[0])],
    })

    time_stats = single_pass[["t_min", "t_max"]]
    sample = con.execute("SELECT * FROM train LIMIT 5").fetchdf()

    file_sizes = {p.name: p.stat().st_size for p in data_dir.iterdir() if p.is_file()}
    con.close()

    return {
        "schema": schema_df,
        "row_count": row_count,
        "null_table": null_df,
        "cardinality": cardinality,
        "label_balance": label_balance,
        "time_stats": time_stats,
        "sample": sample,
        "test_row_count": None,  # skip test.csv scan for speed
        "file_sizes": file_sizes,
        "data_dir": str(data_dir),
    }


# ---------------------------------------------------------------------------
# IEEE-CIS
# ---------------------------------------------------------------------------
def load_ieee_meta(data_dir: str | os.PathLike) -> Dict[str, Any]:
    """Load IEEE-CIS train_transaction + train_identity with pandas."""
    data_dir = Path(data_dir)
    tx_path = data_dir / "train_transaction.csv"
    id_path = data_dir / "train_identity.csv"

    tx = pd.read_csv(tx_path, low_memory=False)
    idn = pd.read_csv(id_path, low_memory=False)

    file_sizes = {
        p.name: p.stat().st_size
        for p in data_dir.iterdir()
        if p.is_file()
    }

    return {
        "transaction": tx,
        "identity": idn,
        "file_sizes": file_sizes,
        "data_dir": str(data_dir),
    }


# ---------------------------------------------------------------------------
# CTU-13
# ---------------------------------------------------------------------------
def load_ctu13_meta(data_dir: str | os.PathLike) -> Dict[str, Any]:
    """Concatenate all .binetflow files using polars (streamed read)."""
    data_dir = Path(data_dir)
    binetflow_files: List[Path] = sorted(
        data_dir.glob("*/*.binetflow"),
        key=lambda p: int(p.parent.name),
    )

    per_scenario = []
    frames = []
    for p in binetflow_files:
        df = pl.read_csv(p, infer_schema_length=10000, ignore_errors=True)
        df = df.with_columns(pl.lit(p.parent.name).alias("scenario"))
        per_scenario.append({
            "scenario": p.parent.name,
            "file": p.name,
            "rows": df.height,
            "size_bytes": p.stat().st_size,
        })
        frames.append(df)

    full = pl.concat(frames, how="vertical_relaxed")

    file_sizes = {
        f"{p.parent.name}/{p.name}": p.stat().st_size
        for p in binetflow_files
    }

    return {
        "frame": full,
        "per_scenario": pd.DataFrame(per_scenario),
        "file_sizes": file_sizes,
        "data_dir": str(data_dir),
    }


# ---------------------------------------------------------------------------
# Web Robot Sessions (Figshare 3477932)
# ---------------------------------------------------------------------------
def load_web_robot_meta(data_dir: str | os.PathLike, json_sample_n: int = 100) -> Dict[str, Any]:
    """Load simple_features.csv + semantic_features.csv with pandas, and
    stream-parse the first ``json_sample_n`` entries of public_v2.json
    without materialising the full 3 GB file.

    The raw JSON is one outer dict; entries are written one-per-line as
    ``"<id>":{...},`` so a manual line-by-line parse is sufficient.
    """
    data_dir = Path(data_dir)
    simple_path = data_dir / "simple_features.csv"
    semantic_path = data_dir / "semantic_features.csv"
    json_path = data_dir / "public_v2.json"

    simple = pd.read_csv(simple_path, low_memory=False)
    semantic = pd.read_csv(semantic_path, low_memory=False)

    # --- stream-sample public_v2.json -------------------------------------
    samples: List[Dict[str, Any]] = []
    sample_ids: List[str] = []
    with open(json_path, "r", encoding="utf-8") as fh:
        first = fh.readline()  # opening "{"
        while len(samples) < json_sample_n:
            line = fh.readline()
            if not line:
                break
            s = line.strip()
            if not s or s in ("{", "}"):
                continue
            # Strip trailing comma if present
            if s.endswith(","):
                s = s[:-1]
            # Each entry is of the form: "<id>":{...}
            # Find first ':' that separates key from value object
            try:
                # Wrap the entry in braces and parse as one-key dict
                obj = json.loads("{" + s + "}")
            except json.JSONDecodeError:
                continue
            for k, v in obj.items():
                sample_ids.append(k)
                samples.append(v)
                if len(samples) >= json_sample_n:
                    break

    json_schema: Dict[str, str] = {}
    if samples:
        for k, v in samples[0].items():
            json_schema[k] = type(v).__name__

    file_sizes = {p.name: p.stat().st_size for p in data_dir.iterdir() if p.is_file()}

    return {
        "simple": simple,
        "semantic": semantic,
        "json_sample": samples,
        "json_sample_ids": sample_ids,
        "json_schema": json_schema,
        "json_path": str(json_path),
        "file_sizes": file_sizes,
        "data_dir": str(data_dir),
    }
