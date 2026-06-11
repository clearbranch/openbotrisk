"""Generate a synthetic browser-fingerprint visit log.

The generator creates two phenomena that make browser identification hard:

- **drift**, where one browser's fingerprint changes over time;
- **clones**, where distinct stock devices present identical fingerprints.

The output is deterministic for the default seed and is written to
``experiments/fingerprint-identification/generated/fp_visits.csv``.

Example:
    ```bash
    python src/openbotrisk/experiments/fingerprint_identification/generate_fingerprints.py
    ```
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[3]
DATA_DIR = REPO_ROOT / "experiments" / "fingerprint-identification" / "generated"

SEED = 7
T0 = pd.Timestamp("2026-01-01")
DAYS = 120
N_DESKTOP = 150
N_MOBILE = 150

GPU_VARIANTS = {
    "desktop": ["nvidia_a", "nvidia_b", "amd_a", "intel_a", "intel_b", "apple_m"],
    "mobile": ["soc_std"],
}
DRIFT_PER_DAY = {
    "version_bump": 0.035,
    "os_update": 0.004,
    "font_change": 0.006,
    "screen_change": 0.003,
    "timezone_trip": 0.002,
}
COOKIE_CLEAR = 0.03
PRIVATE_MODE = 0.10
FINGERPRINT_ATTRS = [
    "os",
    "os_version",
    "browser_family",
    "browser_version",
    "screen",
    "timezone",
    "language",
    "fonts",
    "canvas",
]


def _desktop_templates() -> list[dict[str, Any]]:
    """Return desktop browser templates for the synthetic population."""

    return [
        {
            "os": "Windows",
            "os_version": 11,
            "browser_family": family,
            "device_type": "desktop",
            "screen": screen,
            "timezone": "Europe/London",
            "language": "en-GB",
        }
        for family in ["Chrome", "Firefox", "Edge"]
        for screen in ["1920x1080", "2560x1440"]
    ] + [
        {
            "os": "macOS",
            "os_version": 15,
            "browser_family": family,
            "device_type": "desktop",
            "screen": screen,
            "timezone": "Europe/London",
            "language": "en-GB",
        }
        for family in ["Chrome", "Safari", "Firefox"]
        for screen in ["2560x1600", "3024x1964"]
    ] + [
        {
            "os": "Linux",
            "os_version": 24,
            "browser_family": "Firefox",
            "device_type": "desktop",
            "screen": "1920x1080",
            "timezone": "Europe/London",
            "language": "en-GB",
        },
        {
            "os": "Linux",
            "os_version": 24,
            "browser_family": "Chrome",
            "device_type": "desktop",
            "screen": "3440x1440",
            "timezone": "Europe/London",
            "language": "en-GB",
        },
        {
            "os": "Windows",
            "os_version": 10,
            "browser_family": "Chrome",
            "device_type": "desktop",
            "screen": "1366x768",
            "timezone": "Europe/London",
            "language": "en-GB",
        },
    ]


def _mobile_templates() -> list[dict[str, Any]]:
    """Return stock mobile browser templates for the synthetic population."""

    return [
        {
            "os": "iOS",
            "os_version": 19,
            "browser_family": "Safari",
            "device_type": "mobile",
            "screen": "390x844",
            "timezone": "Europe/London",
            "language": "en-GB",
        },
        {
            "os": "iOS",
            "os_version": 19,
            "browser_family": "Safari",
            "device_type": "mobile",
            "screen": "430x932",
            "timezone": "Europe/London",
            "language": "en-GB",
        },
        {
            "os": "Android",
            "os_version": 16,
            "browser_family": "Chrome",
            "device_type": "mobile",
            "screen": "412x915",
            "timezone": "Europe/London",
            "language": "en-GB",
        },
        {
            "os": "Android",
            "os_version": 15,
            "browser_family": "Chrome",
            "device_type": "mobile",
            "screen": "384x854",
            "timezone": "Europe/London",
            "language": "en-GB",
        },
    ]


def _canvas_hash(browser: dict[str, Any]) -> str:
    """Return a deterministic canvas/WebGL-like hash for a browser state."""

    return (
        f"cv_{browser['os']}{browser['os_version']}_"
        f"{browser['browser_family']}{browser['browser_version']}_"
        f"{browser['gpu']}_{browser['screen']}"
    )


def _make_browser_population(rng: np.random.Generator) -> list[dict[str, Any]]:
    """Create desktop and mobile browser records.

    Args:
        rng: NumPy random generator.

    Returns:
        Browser-state dictionaries. The dictionaries are intentionally mutable
        because drift updates them over simulated time.
    """

    desktops = _desktop_templates()
    mobiles = _mobile_templates()
    browsers: list[dict[str, Any]] = []
    browser_id = 0

    for _ in range(N_DESKTOP):
        browser_id += 1
        template = dict(desktops[int(rng.integers(0, len(desktops)))])
        template.update(
            browser_id=f"b{browser_id:04d}",
            browser_version=int(rng.integers(120, 126)),
            gpu=rng.choice(GPU_VARIANTS["desktop"]),
            fonts=f"fontset_{rng.integers(0, 10**6):06d}",
            cookie=f"ck_{browser_id:04d}_0",
            cookie_gen=0,
        )
        browsers.append(template)

    for _ in range(N_MOBILE):
        browser_id += 1
        template = dict(mobiles[int(rng.integers(0, len(mobiles)))])
        template.update(
            browser_id=f"b{browser_id:04d}",
            browser_version=int(rng.integers(123, 125)),
            gpu="soc_std",
            fonts="fontset_mobile_std",
            cookie=f"ck_{browser_id:04d}_0",
            cookie_gen=0,
        )
        browsers.append(template)
    return browsers


def _apply_drift(
    rng: np.random.Generator,
    browser: dict[str, Any],
    gap_days: float,
) -> None:
    """Mutate one browser state to simulate drift since the last visit.

    Args:
        rng: NumPy random generator.
        browser: Mutable browser-state dictionary.
        gap_days: Simulated days since the previous visit.

    Returns:
        ``None``. The browser dictionary is modified in place.
    """

    is_mobile = browser["device_type"] == "mobile"
    for _ in range(int(gap_days) + 1):
        if rng.random() < DRIFT_PER_DAY["version_bump"]:
            browser["browser_version"] += 1
        if rng.random() < DRIFT_PER_DAY["os_update"]:
            browser["os_version"] += 1
        if not is_mobile and rng.random() < DRIFT_PER_DAY["font_change"]:
            browser["fonts"] = f"fontset_{rng.integers(0, 10**6):06d}"
        if not is_mobile and rng.random() < DRIFT_PER_DAY["screen_change"]:
            browser["screen"] = rng.choice(["1920x1080", "2560x1440", "3840x2160"])
        if rng.random() < DRIFT_PER_DAY["timezone_trip"]:
            browser["timezone"] = rng.choice(
                ["Europe/London", "Europe/Paris", "America/New_York"]
            )


def _visit_record(
    rng: np.random.Generator,
    browser: dict[str, Any],
    visit_day: float,
) -> dict[str, Any]:
    """Build one visit record for the current browser state."""

    if rng.random() < COOKIE_CLEAR:
        browser["cookie_gen"] += 1
        browser["cookie"] = f"ck_{browser['browser_id'][1:]}_{browser['cookie_gen']}"

    return {
        "ts": T0 + pd.Timedelta(days=visit_day),
        "true_browser": browser["browser_id"],
        "cookie": None if rng.random() < PRIVATE_MODE else browser["cookie"],
        "os": browser["os"],
        "os_version": browser["os_version"],
        "browser_family": browser["browser_family"],
        "browser_version": browser["browser_version"],
        "device_type": browser["device_type"],
        "screen": browser["screen"],
        "timezone": browser["timezone"],
        "language": browser["language"],
        "fonts": browser["fonts"],
        "canvas": _canvas_hash(browser),
    }


def generate_fingerprint_visits(seed: int = SEED) -> pd.DataFrame:
    """Generate the synthetic browser-fingerprint visit table.

    Args:
        seed: Random seed. The default reproduces the methodology figure.

    Returns:
        A visit-level DataFrame containing browser attributes, intermittent
        cookies, and a hidden ``true_browser`` label for evaluation.

    Example:
        ```python
        visits = generate_fingerprint_visits()
        assert visits.true_browser.nunique() == 300
        ```
    """

    rng = np.random.default_rng(seed)
    visits: list[dict[str, Any]] = []

    for browser in _make_browser_population(rng):
        visit_day = float(rng.uniform(0, 6))
        while visit_day < DAYS:
            gap = float(rng.exponential(4) + 0.5)
            _apply_drift(rng, browser, gap)
            visits.append(_visit_record(rng, browser, visit_day))
            visit_day += gap

    df = pd.DataFrame(visits).sort_values("ts").reset_index(drop=True)
    df.insert(0, "visit_id", [f"v{i:06d}" for i in range(len(df))])
    return df


def _print_summary(visits: pd.DataFrame) -> None:
    """Print a compact summary of the generated population."""

    print(f"{len(visits)} visits from {visits.true_browser.nunique()} browsers")
    print(
        visits.groupby(
            visits.true_browser.map(lambda browser: "mobile" if browser > "b0150" else "desktop")
        )
        .size()
        .rename("visits")
        .to_string()
    )

    first = visits.drop_duplicates("true_browser")
    for device_type in ["desktop", "mobile"]:
        sub = first[first.device_type == device_type]
        distinct = sub[FINGERPRINT_ATTRS].astype(str).agg("|".join, axis=1).nunique()
        print(
            f"{device_type}: {len(sub)} browsers, "
            f"{distinct} distinct first fingerprints"
        )


def main() -> None:
    """Generate the visit CSV used by the fingerprint-method comparison."""

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    visits = generate_fingerprint_visits()
    visits.to_csv(DATA_DIR / "fp_visits.csv", index=False)
    _print_summary(visits)


if __name__ == "__main__":
    main()
