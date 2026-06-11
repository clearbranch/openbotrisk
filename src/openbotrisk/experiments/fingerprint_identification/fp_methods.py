"""Compare browser-identification methods on the synthetic visit log.

The methods are ordered by how much inference they make about commercial
visitor-ID systems:

- stateless exact fingerprint hashing;
- constraint-chain linking;
- supervised pairwise matching;
- anchored hybrids that combine matching with intermittent cookies.

Evaluation reports two errors: false splits, where one returning browser is
fragmented into multiple IDs, and false merges, where distinct browsers are
fused under one ID.

Example:
    ```bash
    python src/openbotrisk/experiments/fingerprint_identification/generate_fingerprints.py
    python src/openbotrisk/experiments/fingerprint_identification/fp_methods.py
    ```
"""

from __future__ import annotations

# ruff: noqa: E402,I001

import hashlib
import os
from collections import defaultdict
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import TypeAlias

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.axes import Axes
from sklearn.linear_model import LogisticRegression


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[3]
DATA_DIR = REPO_ROOT / "experiments" / "fingerprint-identification" / "generated"
IMAGE_DIR = REPO_ROOT / "site" / "methodology" / "images"

ATTRS = [
    "os",
    "os_version",
    "browser_family",
    "browser_version",
    "device_type",
    "screen",
    "timezone",
    "language",
    "fonts",
    "canvas",
]
SOFT = ["screen", "timezone", "language", "fonts", "canvas", "os_version"]
MAX_DIFFS = 2
CAND_CAP = 100
TRAIN_DAYS = 30
THRESHOLD = 0.5
SWEEP_THRESHOLDS = [0.2, 0.4, 0.6, 0.8, 0.95]

Scorer: TypeAlias = Callable[[np.ndarray, np.ndarray, np.ndarray], np.ndarray]
Acceptor: TypeAlias = Callable[[float], bool]


@dataclass(frozen=True)
class EncodedVisits:
    """Vectorized visit features used by sequential matchers."""

    visits: pd.DataFrame
    soft_codes: np.ndarray
    versions: np.ndarray
    ts_days: np.ndarray
    hard_key: list[tuple[str, str, str]]
    true_browser: np.ndarray
    cookies: np.ndarray


@dataclass(frozen=True)
class EvaluationResult:
    """Split/merge metrics for one identification method."""

    false_split: float
    false_merge: float
    by_device: dict[str, tuple[float, float]]
    n_ids: int


def encode_visits(visits: pd.DataFrame) -> EncodedVisits:
    """Prepare vectorized arrays for the matching methods.

    Args:
        visits: Visit table from ``generate_fingerprints.py``.

    Returns:
        Encoded arrays for soft attributes, version gaps, time gaps, hard
        blocking keys, true labels, and cookies.
    """

    soft_codes = np.stack([pd.factorize(visits[attr])[0] for attr in SOFT], axis=1)
    ts_days = ((visits.ts - visits.ts.min()).dt.total_seconds() / 86400).to_numpy()
    hard_key = list(
        zip(visits.os, visits.browser_family, visits.device_type, strict=True)
    )
    return EncodedVisits(
        visits=visits,
        soft_codes=soft_codes,
        versions=visits.browser_version.to_numpy(),
        ts_days=ts_days,
        hard_key=hard_key,
        true_browser=visits.true_browser.to_numpy(),
        cookies=visits.cookie.to_numpy(dtype=object),
    )


def evaluate_identifiers(
    encoded: EncodedVisits,
    ids: Sequence[str],
    name: str,
    *,
    breakdown: bool = False,
) -> EvaluationResult:
    """Measure false-split and false-merge rates for assigned IDs.

    Args:
        encoded: Encoded visit features and true labels.
        ids: Assigned ID for each visit, in visit-table order.
        name: Display name used in console output.
        breakdown: Print desktop/mobile metrics when ``True``.

    Returns:
        ``EvaluationResult`` containing overall and per-device-type errors.
    """

    d = pd.DataFrame(
        {
            "true_browser": encoded.true_browser,
            "id": ids,
            "device_type": encoded.visits.device_type,
        }
    )
    false_split = _false_split_rate(d)
    false_merge = _false_merge_rate(d)
    by_device: dict[str, tuple[float, float]] = {}

    print(
        f"{name:38s} false-split {false_split:.3f}   "
        f"false-merge {false_merge:.3f}   ids {d.id.nunique()}"
    )
    for device_type in ["desktop", "mobile"]:
        subset = d[d.device_type == device_type]
        split = _false_split_rate(subset)
        merge = _false_merge_rate(subset)
        by_device[device_type] = (split, merge)
        if breakdown:
            print(
                f"     {device_type:8s}: false-split {split:.3f}   "
                f"false-merge {merge:.3f}"
            )
    return EvaluationResult(false_split, false_merge, by_device, d.id.nunique())


def _false_split_rate(assignments: pd.DataFrame) -> float:
    """Return share of returning visits assigned a different ID."""

    previous = assignments.groupby("true_browser")["id"].shift()
    returning = previous.notna()
    if not returning.any():
        return 0.0
    return float(
        (assignments.id[returning].to_numpy() != previous[returning].to_numpy()).mean()
    )


def _false_merge_rate(assignments: pd.DataFrame) -> float:
    """Return share of visits whose assigned ID contains another browser."""

    impure_ids = {
        assigned_id
        for assigned_id, group in assignments.groupby("id")
        if group.true_browser.nunique() > 1
    }
    return float(assignments.id.isin(impure_ids).mean())


def exact_hash_ids(visits: pd.DataFrame) -> list[str]:
    """Assign IDs by hashing all fingerprint attributes exactly.

    Args:
        visits: Visit table.

    Returns:
        One 12-character hash ID per visit.
    """

    return [
        hashlib.md5("|".join(str(row[attr]) for attr in ATTRS).encode()).hexdigest()[
            :12
        ]
        for _idx, row in visits.iterrows()
    ]


def link_visits(
    encoded: EncodedVisits,
    scorer: Scorer,
    accept: Acceptor,
    *,
    use_cookie_anchor: bool = False,
    cookie_veto: bool = False,
) -> list[str]:
    """Sequentially link visits into chains.

    Args:
        encoded: Encoded visit features.
        scorer: Function that scores candidate chains for a visit.
        accept: Predicate deciding whether the best score is high enough.
        use_cookie_anchor: If ``True``, a known cookie-to-chain binding wins
            before fuzzy matching.
        cookie_veto: If ``True``, reject candidates with a different live
            cookie. This resists false merges when deterministic state exists.

    Returns:
        Chain ID assigned to each visit.
    """

    chain_codes: list[np.ndarray | None] = []
    chain_version: list[int | None] = []
    chain_ts: list[float | None] = []
    chain_id: list[str] = []
    chain_cookie: list[str | None] = []
    index: defaultdict[tuple[str, str, str], list[int]] = defaultdict(list)
    cookie_to_chain: dict[str, int] = {}
    out: list[str] = []

    for idx in range(len(encoded.visits)):
        chain_idx = _find_chain(
            encoded,
            idx,
            scorer,
            accept,
            chain_codes,
            chain_version,
            chain_ts,
            chain_cookie,
            index,
            cookie_to_chain,
            use_cookie_anchor=use_cookie_anchor,
            cookie_veto=cookie_veto,
        )

        if chain_idx is None:
            chain_idx = len(chain_id)
            chain_id.append(f"c{chain_idx:05d}")
            chain_codes.append(None)
            chain_version.append(None)
            chain_ts.append(None)
            chain_cookie.append(None)
            index[encoded.hard_key[idx]].append(chain_idx)

        cookie = encoded.cookies[idx]
        has_cookie = isinstance(cookie, str)
        if use_cookie_anchor and has_cookie:
            cookie_to_chain[cookie] = chain_idx
        chain_codes[chain_idx] = encoded.soft_codes[idx]
        chain_version[chain_idx] = int(encoded.versions[idx])
        chain_ts[chain_idx] = float(encoded.ts_days[idx])
        if has_cookie:
            chain_cookie[chain_idx] = cookie
        out.append(chain_id[chain_idx])
    return out


def _find_chain(
    encoded: EncodedVisits,
    idx: int,
    scorer: Scorer,
    accept: Acceptor,
    chain_codes: list[np.ndarray | None],
    chain_version: list[int | None],
    chain_ts: list[float | None],
    chain_cookie: list[str | None],
    index: defaultdict[tuple[str, str, str], list[int]],
    cookie_to_chain: dict[str, int],
    *,
    use_cookie_anchor: bool,
    cookie_veto: bool,
) -> int | None:
    """Find the best existing chain for one visit, if any."""

    cookie = encoded.cookies[idx]
    has_cookie = isinstance(cookie, str)
    if use_cookie_anchor and has_cookie and cookie in cookie_to_chain:
        return cookie_to_chain[cookie]

    candidates = [
        chain_idx
        for chain_idx in index[encoded.hard_key[idx]][-CAND_CAP:]
        if chain_version[chain_idx] is not None
        and encoded.versions[idx] >= chain_version[chain_idx]
    ]
    if cookie_veto and has_cookie:
        candidates = [
            chain_idx
            for chain_idx in candidates
            if chain_cookie[chain_idx] is None or chain_cookie[chain_idx] == cookie
        ]
    if not candidates:
        return None

    candidate_array = np.array(candidates)
    candidate_codes = np.stack([chain_codes[chain_idx] for chain_idx in candidates])
    eq = encoded.soft_codes[idx] == candidate_codes
    version_gap = np.minimum(
        encoded.versions[idx] - np.array([chain_version[ci] for ci in candidates]), 5
    ) / 5
    time_gap = np.minimum(
        encoded.ts_days[idx] - np.array([chain_ts[ci] for ci in candidates]), 60
    ) / 60
    scores = scorer(eq.astype(float), version_gap, time_gap)
    best = int(np.argmax(scores))
    if accept(float(scores[best])):
        return int(candidate_array[best])
    return None


def rule_scorer(eq: np.ndarray, _version_gap: np.ndarray, time_gap: np.ndarray) -> np.ndarray:
    """Score candidates with the constraint-chain rule.

    Args:
        eq: Per-soft-attribute equality matrix.
        _version_gap: Unused version-gap vector. Version monotonicity is already
            enforced as a hard constraint before scoring.
        time_gap: Gap from candidate chain to visit, scaled to ``[0, 1]``.

    Returns:
        Score per candidate; ``-inf`` means reject.
    """

    diffs = (1 - eq).sum(axis=1)
    scores = -diffs - 1e-3 * time_gap
    scores[diffs > MAX_DIFFS] = -np.inf
    return scores


def pair_features(encoded: EncodedVisits, visit_a: int, visit_b: int) -> np.ndarray:
    """Build one pairwise feature row for supervised matching."""

    eq = (encoded.soft_codes[visit_a] == encoded.soft_codes[visit_b]).astype(float)
    version_gap = min(abs(encoded.versions[visit_a] - encoded.versions[visit_b]), 5) / 5
    time_gap = min(abs(encoded.ts_days[visit_a] - encoded.ts_days[visit_b]), 60) / 60
    return np.concatenate([eq, [version_gap, time_gap]])


def train_pairwise_classifier(
    encoded: EncodedVisits,
    *,
    seed: int = 3,
    train_days: int = TRAIN_DAYS,
) -> LogisticRegression:
    """Train a cookie-labelled pairwise matcher.

    Args:
        encoded: Encoded visit features.
        seed: Random seed for pair sampling.
        train_days: Use cookie-labelled visits before this day as training data.

    Returns:
        Fitted ``LogisticRegression`` classifier.
    """

    rng = np.random.default_rng(seed)
    train_idx = np.where((encoded.ts_days < train_days) & pd.notna(encoded.cookies))[0]

    by_cookie: defaultdict[str, list[int]] = defaultdict(list)
    by_hard: defaultdict[tuple[str, str, str], list[int]] = defaultdict(list)
    for idx in train_idx:
        by_cookie[encoded.cookies[idx]].append(idx)
        by_hard[encoded.hard_key[idx]].append(idx)

    x_rows: list[np.ndarray] = []
    y_rows: list[int] = []
    for indices in by_cookie.values():
        if len(indices) < 2:
            continue
        for _ in range(min(4, len(indices))):
            visit_a, visit_b = rng.choice(indices, 2, replace=False)
            x_rows.append(pair_features(encoded, int(visit_a), int(visit_b)))
            y_rows.append(1)

    for indices in by_hard.values():
        if len(indices) < 2:
            continue
        for _ in range(min(400, len(indices) * 3)):
            visit_a, visit_b = rng.choice(indices, 2, replace=False)
            if encoded.cookies[visit_a] != encoded.cookies[visit_b]:
                x_rows.append(pair_features(encoded, int(visit_a), int(visit_b)))
                y_rows.append(0)

    x = np.array(x_rows)
    y = np.array(y_rows)
    classifier = LogisticRegression(max_iter=2000).fit(x, y)
    print(
        f"     C training pairs: {y.sum()} pos / {len(y) - y.sum()} neg "
        f"(cookie labels -- clone pairs are mislabelled negatives)"
    )
    weights = {
        name: round(float(weight), 2)
        for name, weight in zip(
            SOFT + ["vgap", "tgap"], classifier.coef_[0], strict=True
        )
    }
    print("     C learned weights:", weights)
    return classifier


def make_ml_scorer(classifier: LogisticRegression) -> Scorer:
    """Return a scorer that applies a fitted pairwise classifier."""

    def _ml_scorer(eq: np.ndarray, version_gap: np.ndarray, time_gap: np.ndarray) -> np.ndarray:
        features = np.column_stack([eq, version_gap, time_gap])
        return classifier.predict_proba(features)[:, 1]

    return _ml_scorer


def run_identification_methods(
    visits: pd.DataFrame,
) -> tuple[dict[str, EvaluationResult], pd.DataFrame]:
    """Run Methods A-D and print their metrics.

    Args:
        visits: Visit table from ``generate_fingerprints.py``.

    Returns:
        ``(results, threshold_sweep)``. ``results`` maps method names to
        metrics; ``threshold_sweep`` traces Method C across match thresholds.
    """

    encoded = encode_visits(visits)
    results: dict[str, EvaluationResult] = {}

    results["A exact hash"] = evaluate_identifiers(
        encoded,
        exact_hash_ids(visits),
        "A  stateless exact hash",
        breakdown=True,
    )

    results["B constraint chains"] = evaluate_identifiers(
        encoded,
        link_visits(encoded, rule_scorer, lambda score: score > -np.inf),
        "B  constraint-chain linking",
        breakdown=True,
    )

    classifier = train_pairwise_classifier(encoded)
    ml_scorer = make_ml_scorer(classifier)
    results["C supervised matching"] = evaluate_identifiers(
        encoded,
        link_visits(encoded, ml_scorer, lambda score: score >= THRESHOLD),
        "C  supervised pairwise matching",
        breakdown=True,
    )

    sweep = []
    for threshold in SWEEP_THRESHOLDS:
        result = evaluate_identifiers(
            encoded,
            link_visits(encoded, ml_scorer, lambda score, th=threshold: score >= th),
            f"     C @ threshold {threshold:.2f}",
        )
        sweep.append((threshold, result.false_split, result.false_merge))

    results["D anchor only"] = evaluate_identifiers(
        encoded,
        link_visits(
            encoded,
            ml_scorer,
            lambda score: score >= THRESHOLD,
            use_cookie_anchor=True,
        ),
        "D  anchored hybrid (recover only)",
        breakdown=True,
    )

    results["D anchor + veto"] = evaluate_identifiers(
        encoded,
        link_visits(
            encoded,
            ml_scorer,
            lambda score: score >= THRESHOLD,
            use_cookie_anchor=True,
            cookie_veto=True,
        ),
        "D' anchored hybrid + cookie veto",
        breakdown=True,
    )

    sweep_df = pd.DataFrame(
        sweep, columns=["threshold", "false_split", "false_merge"]
    )
    return results, sweep_df


def _plot_tradeoff_panel(
    ax: Axes,
    results: dict[str, EvaluationResult],
    device_type: str,
) -> None:
    """Plot split/merge points for one device type."""

    markers = dict(zip(results, ["s", "^", "o", "D", "*"], strict=True))
    colors = dict(
        zip(results, ["#d62728", "#ff7f0e", "#9467bd", "#2a9d2a", "#1f77b4"], strict=True)
    )
    for name, result in results.items():
        split, merge = result.by_device[device_type]
        ax.scatter(
            merge,
            split,
            marker=markers[name],
            color=colors[name],
            s=140,
            label=name,
            zorder=3,
        )
    subtitle = (
        "(high-entropy, drifting)"
        if device_type == "desktop"
        else "(cloned stock devices)"
    )
    ax.set(
        xlabel="false-merge rate (distinct browsers fused)",
        title=f"{device_type} {subtitle}",
        xlim=(-0.05, 1.05),
    )
    ax.grid(alpha=0.25)


def plot_method_tradeoff(
    results: dict[str, EvaluationResult],
    output_path: Path,
) -> None:
    """Write the split/merge trade-off figure.

    Args:
        results: Metrics from ``run_identification_methods``.
        output_path: PNG path to write.

    Returns:
        ``None``. The figure is written to disk.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.5), sharey=True)
    for ax, device_type in zip(axes, ["desktop", "mobile"], strict=True):
        _plot_tradeoff_panel(ax, results, device_type)
    axes[0].set_ylabel("false-split rate (returning browser missed = 1$-$'accuracy')")
    axes[0].legend(fontsize=9)
    fig.suptitle(
        "Identification methods, split vs merge errors -- vendors publish only the y-axis",
        y=1.02,
    )
    plt.tight_layout()
    plt.savefig(output_path, dpi=140, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    """Run the fingerprint-identification comparison and write the figure."""

    visits = pd.read_csv(DATA_DIR / "fp_visits.csv", parse_dates=["ts"])
    results, _sweep = run_identification_methods(visits)
    plot_method_tradeoff(results, IMAGE_DIR / "fp_methods_tradeoff.png")
    print("\nSaved fp_methods_tradeoff.png")


if __name__ == "__main__":
    main()
