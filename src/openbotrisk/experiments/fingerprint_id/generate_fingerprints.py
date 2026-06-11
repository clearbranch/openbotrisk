"""
Synthetic browser-fingerprint visit log for comparing identification methods.

Two phenomena drive everything, so the generator must produce both:

  DRIFT  : a single browser's fingerprint changes over time (version bumps,
           font installs, monitor changes, travel). Drift causes FALSE SPLITS
           for exact matching.
  CLONES : distinct devices with identical fingerprints (stock mobiles).
           Clones cause FALSE MERGES for any browser-content-only method.

Population:
  150 desktop browsers : drawn from 15 templates, but per-browser font sets
                         and GPU variants give them high individual entropy.
  150 mobile browsers  : drawn from 4 stock templates; within a template,
                         browser-observable attributes are IDENTICAL.

Each browser visits on a random schedule over 120 days. Between visits its
state drifts. Each visit also carries an intermittent first-party cookie
(cleared ~3%/visit, hidden ~10% of visits by private browsing) -- this is
both the deterministic identification layer and, mirroring real vendor
practice, the ground-truth source for training a pairwise matcher.

Drift rates are guesses of plausible magnitude, not calibrated to any
measured population (FP-STALKER reports measured drift; we do not copy its
numbers). Conclusions should be read as qualitative.
"""

import numpy as np
import pandas as pd

rng = np.random.default_rng(7)
T0 = pd.Timestamp("2026-01-01")
DAYS = 120

# ------------------------------------------------------------------ templates
desktop_templates = [
    dict(os="Windows", os_version=11, browser_family=f, device_type="desktop",
         screen=s, timezone="Europe/London", language="en-GB")
    for f in ["Chrome", "Firefox", "Edge"] for s in ["1920x1080", "2560x1440"]
] + [
    dict(os="macOS", os_version=15, browser_family=f, device_type="desktop",
         screen=s, timezone="Europe/London", language="en-GB")
    for f in ["Chrome", "Safari", "Firefox"] for s in ["2560x1600", "3024x1964"]
] + [
    dict(os="Linux", os_version=24, browser_family="Firefox",
         device_type="desktop", screen="1920x1080",
         timezone="Europe/London", language="en-GB"),
    dict(os="Linux", os_version=24, browser_family="Chrome",
         device_type="desktop", screen="3440x1440",
         timezone="Europe/London", language="en-GB"),
    dict(os="Windows", os_version=10, browser_family="Chrome",
         device_type="desktop", screen="1366x768",
         timezone="Europe/London", language="en-GB"),
]

mobile_templates = [
    dict(os="iOS", os_version=19, browser_family="Safari", device_type="mobile",
         screen="390x844", timezone="Europe/London", language="en-GB"),
    dict(os="iOS", os_version=19, browser_family="Safari", device_type="mobile",
         screen="430x932", timezone="Europe/London", language="en-GB"),
    dict(os="Android", os_version=16, browser_family="Chrome", device_type="mobile",
         screen="412x915", timezone="Europe/London", language="en-GB"),
    dict(os="Android", os_version=15, browser_family="Chrome", device_type="mobile",
         screen="384x854", timezone="Europe/London", language="en-GB"),
]

GPU_VARIANTS = {  # canvas/WebGL hash depends on (template family, gpu, browser major)
    "desktop": ["nvidia_a", "nvidia_b", "amd_a", "intel_a", "intel_b", "apple_m"],
    "mobile": ["soc_std"],          # stock phones: one GPU per template -> clones
}

browsers = []
bid = 0
for _ in range(150):
    bid += 1
    t = dict(rng.choice(desktop_templates))
    t.update(
        browser_id=f"b{bid:04d}",
        browser_version=int(rng.integers(120, 126)),
        gpu=rng.choice(GPU_VARIANTS["desktop"]),
        # desktop font sets: individually distinctive (installed software)
        fonts=f"fontset_{rng.integers(0, 10**6):06d}",
        cookie=f"ck_{bid:04d}_0", cookie_gen=0,
    )
    browsers.append(t)
for _ in range(150):
    bid += 1
    t = dict(mobile_templates[rng.integers(0, len(mobile_templates))])
    t.update(
        browser_id=f"b{bid:04d}",
        browser_version=int(rng.integers(123, 125)),
        gpu="soc_std",
        fonts="fontset_mobile_std",   # identical across all stock phones
        cookie=f"ck_{bid:04d}_0", cookie_gen=0,
    )
    browsers.append(t)


def canvas_hash(b):
    """Deterministic: same hardware+software state -> same canvas hash."""
    return (f"cv_{b['os']}{b['os_version']}_{b['browser_family']}"
            f"{b['browser_version']}_{b['gpu']}_{b['screen']}")


# ------------------------------------------------------------- visit schedule
DRIFT_PER_DAY = dict(version_bump=0.035, os_update=0.004, font_change=0.006,
                     screen_change=0.003, timezone_trip=0.002)
COOKIE_CLEAR = 0.03
PRIVATE_MODE = 0.10

visits = []
for b in browsers:
    is_mobile = b["device_type"] == "mobile"
    t = float(rng.uniform(0, 6))
    while t < DAYS:
        # drift since last visit
        gap = float(rng.exponential(4) + 0.5)
        for _ in range(int(gap) + 1):
            if rng.random() < DRIFT_PER_DAY["version_bump"]:
                b["browser_version"] += 1
            if rng.random() < DRIFT_PER_DAY["os_update"]:
                b["os_version"] += 1
            if not is_mobile and rng.random() < DRIFT_PER_DAY["font_change"]:
                b["fonts"] = f"fontset_{rng.integers(0, 10**6):06d}"
            if not is_mobile and rng.random() < DRIFT_PER_DAY["screen_change"]:
                b["screen"] = rng.choice(["1920x1080", "2560x1440", "3840x2160"])
            if rng.random() < DRIFT_PER_DAY["timezone_trip"]:
                b["timezone"] = rng.choice(
                    ["Europe/London", "Europe/Paris", "America/New_York"])
        if rng.random() < COOKIE_CLEAR:
            b["cookie_gen"] += 1
            b["cookie"] = f"ck_{b['browser_id'][1:]}_{b['cookie_gen']}"
        visits.append(dict(
            ts=T0 + pd.Timedelta(days=t),
            true_browser=b["browser_id"],
            cookie=None if rng.random() < PRIVATE_MODE else b["cookie"],
            os=b["os"], os_version=b["os_version"],
            browser_family=b["browser_family"],
            browser_version=b["browser_version"],
            device_type=b["device_type"], screen=b["screen"],
            timezone=b["timezone"], language=b["language"],
            fonts=b["fonts"], canvas=canvas_hash(b),
        ))
        t += gap

df = pd.DataFrame(visits).sort_values("ts").reset_index(drop=True)
df.insert(0, "visit_id", [f"v{i:06d}" for i in range(len(df))])
df.to_csv("fp_visits.csv", index=False)

print(f"{len(df)} visits from {df.true_browser.nunique()} browsers")
print(df.groupby(df.true_browser.map(lambda x: 'mobile' if x > 'b0150' else 'desktop'))
        .size().rename('visits').to_string())
# how cloned are the mobiles? distinct full-attribute combos at t0 vs population
attrs = ["os", "os_version", "browser_family", "browser_version",
         "screen", "timezone", "language", "fonts", "canvas"]
first = df.drop_duplicates("true_browser")
for dt in ["desktop", "mobile"]:
    sub = first[first.device_type == dt]
    print(f"{dt}: {len(sub)} browsers, "
          f"{sub[attrs].astype(str).agg('|'.join, axis=1).nunique()} distinct first fingerprints")
