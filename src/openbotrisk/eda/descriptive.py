"""Reusable descriptive statistics for the EDA notebooks."""
from __future__ import annotations

from typing import Iterable

import pandas as pd


def missingness_table(df: pd.DataFrame) -> pd.DataFrame:
    """Return per-column null counts and rates, sorted by rate desc."""
    n = len(df)
    null_counts = df.isna().sum()
    out = pd.DataFrame({
        "column": null_counts.index,
        "null_count": null_counts.values,
        "null_rate": (null_counts.values / n) if n else 0,
        "dtype": [str(df[c].dtype) for c in null_counts.index],
    })
    return out.sort_values("null_rate", ascending=False).reset_index(drop=True)


def cardinality_table(df: pd.DataFrame, cols: Iterable[str]) -> pd.DataFrame:
    """Unique value counts for the given columns."""
    n = len(df)
    rows = []
    for c in cols:
        if c not in df.columns:
            continue
        nunique = df[c].nunique(dropna=True)
        null_count = int(df[c].isna().sum())
        rows.append({
            "column": c,
            "n_unique": int(nunique),
            "unique_rate": (nunique / n) if n else 0,
            "null_count": null_count,
            "null_rate": (null_count / n) if n else 0,
        })
    return pd.DataFrame(rows)


def label_balance(df: pd.DataFrame, label_col: str) -> pd.DataFrame:
    """Class counts and rates for a label column."""
    counts = df[label_col].value_counts(dropna=False)
    n = counts.sum()
    return pd.DataFrame({
        "value": counts.index,
        "count": counts.values,
        "rate": counts.values / n if n else 0,
    })


def temporal_summary(df: pd.DataFrame, time_col: str) -> dict:
    """Min/max and crude granularity check on a time column."""
    s = pd.to_datetime(df[time_col], errors="coerce")
    s = s.dropna()
    if s.empty:
        return {"column": time_col, "min": None, "max": None, "n": 0}
    return {
        "column": time_col,
        "min": str(s.min()),
        "max": str(s.max()),
        "span": str(s.max() - s.min()),
        "n": int(len(s)),
        "n_unique": int(s.nunique()),
    }
