"""
Four browser-identification methods on the synthetic visit log, in
increasing order of inference about what commercial vendors do.

  A. STATELESS EXACT HASH            [documented -- the open-source pattern]
     ID = hash(all attributes). Any drift = new ID; any clone = same ID.

  B. CONSTRAINT-CHAIN LINKING        [reconstruction -- FP-STALKER rule variant]
     Maintain chains of visits. A new visit joins an existing chain if hard
     constraints hold (same OS/browser family/device type; version never
     decreases) and at most MAX_DIFFS soft attributes differ. Tie-break:
     fewest diffs, then recency.

  C. SUPERVISED PAIRWISE MATCHING    [reconstruction -- FP-STALKER ML variant]
     A classifier estimates P(same browser | visit, chain) from
     per-attribute agreement + version/time gaps, trained on pairs
     labelled by cookie co-occurrence (mirroring how vendors obtain
     ground truth). Threshold sweep traces the split/merge trade-off.

  D. ANCHORED HYBRID                 [inference from vendor documentation]
     Cookie bound to a chain wins (deterministic anchor); otherwise fall
     back to C; new cookies get bound to the resulting chain.

Engineering notes (also true of real systems):
  - Candidate chains are BLOCKED by hard key and capped to the most
    recently active; production matchers do the same (blocking) or the
    pairwise step is intractable.
  - All candidate scoring is one batched classifier call per visit.

Evaluation per method:
  false-split : share of returning visits NOT given the same ID as that
                browser's previous visit. (1 - this) is exactly the
                "accuracy" number vendors publish.
  false-merge : share of visits whose ID also contains a different true
                browser. The error that poisons downstream clustering;
                not published by vendors.
"""

import hashlib
from collections import defaultdict

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("fp_visits.csv", parse_dates=["ts"])
ATTRS = ["os", "os_version", "browser_family", "browser_version",
         "device_type", "screen", "timezone", "language", "fonts", "canvas"]
SOFT = ["screen", "timezone", "language", "fonts", "canvas", "os_version"]
MAX_DIFFS = 2
CAND_CAP = 100          # blocking: consider only the most recent chains per key

# ---- vectorized encodings -----------------------------------------------------
soft_codes = np.stack([pd.factorize(df[a])[0] for a in SOFT], axis=1)
versions = df.browser_version.to_numpy()
ts_days = ((df.ts - df.ts.min()).dt.total_seconds() / 86400).to_numpy()
hard_key = list(zip(df.os, df.browser_family, df.device_type))
true_browser = df.true_browser.to_numpy()
cookies = df.cookie.to_numpy(dtype=object)
N = len(df)


# ---- evaluation ----------------------------------------------------------------
def evaluate(ids, name, breakdown=False):
    d = pd.DataFrame(dict(true_browser=true_browser, id=ids,
                          dt=df.device_type))
    prev = d.groupby("true_browser")["id"].shift()
    ret = prev.notna()
    split = (d.id[ret].to_numpy() != prev[ret].to_numpy()).mean()
    impure = {i for i, g in d.groupby("id") if g.true_browser.nunique() > 1}
    merge = d.id.isin(impure).mean()
    print(f"{name:38s} false-split {split:.3f}   false-merge {merge:.3f}   "
          f"ids {d.id.nunique()}")
    if breakdown:
        per_dt = {}
        for dt in ["desktop", "mobile"]:
            sub = d[d.dt == dt]
            imp = {i for i, g in sub.groupby("id") if g.true_browser.nunique() > 1}
            pv = sub.groupby("true_browser")["id"].shift()
            rt = pv.notna()
            sp = (sub.id[rt].to_numpy() != pv[rt].to_numpy()).mean()
            mg = sub.id.isin(imp).mean()
            per_dt[dt] = (sp, mg)
            print(f"     {dt:8s}: false-split {sp:.3f}   false-merge {mg:.3f}")
        return split, merge, per_dt
    return split, merge


results = {}

# ============================================================== A. exact hash
ids_a = [hashlib.md5("|".join(str(df.iloc[i][a]) for a in ATTRS).encode())
         .hexdigest()[:12] for i in range(N)]
results["A exact hash"] = evaluate(ids_a, "A  stateless exact hash", breakdown=True)


# ====================================== shared sequential linker (B, C, D) =====
def link(scorer, accept, use_cookie_anchor=False, cookie_veto=False):
    """Chains stored as parallel arrays for vectorized scoring.

    cookie_veto: if this visit carries a cookie and a candidate chain's
    most recent visit carried a DIFFERENT cookie, reject that candidate --
    two live cookies imply two devices. This is how a deterministic layer
    resists false MERGES, not just false splits. Cookie-less (private
    mode) visits get no protection, in either direction.
    """
    ch_codes, ch_ver, ch_ts, ch_id, ch_cookie = [], [], [], [], []
    index = defaultdict(list)
    cookie_to_chain = {}
    out = []
    for i in range(N):
        ci_found = None
        has_cookie = isinstance(cookies[i], str)
        if use_cookie_anchor and has_cookie and cookies[i] in cookie_to_chain:
            ci_found = cookie_to_chain[cookies[i]]
        else:
            cand = [ci for ci in index[hard_key[i]][-CAND_CAP:]
                    if versions[i] >= ch_ver[ci]]
            if cookie_veto and has_cookie:
                cand = [ci for ci in cand
                        if ch_cookie[ci] is None or ch_cookie[ci] == cookies[i]]
            if cand:
                C = np.array(cand)
                eq = (soft_codes[i] == np.stack([ch_codes[ci] for ci in cand]))
                vgap = np.minimum(versions[i] - np.array([ch_ver[ci] for ci in cand]), 5) / 5
                tgap = np.minimum(ts_days[i] - np.array([ch_ts[ci] for ci in cand]), 60) / 60
                scores = scorer(eq.astype(float), vgap, tgap)
                best = int(np.argmax(scores))
                if accept(scores[best]):
                    ci_found = int(C[best])
        if ci_found is None:
            ci_found = len(ch_id)
            ch_id.append(f"c{ci_found:05d}")
            ch_codes.append(None); ch_ver.append(None); ch_ts.append(None)
            ch_cookie.append(None)
            index[hard_key[i]].append(ci_found)
        if use_cookie_anchor and has_cookie:
            cookie_to_chain[cookies[i]] = ci_found
        ch_codes[ci_found] = soft_codes[i]
        ch_ver[ci_found] = versions[i]
        ch_ts[ci_found] = ts_days[i]
        if has_cookie:
            ch_cookie[ci_found] = cookies[i]
        out.append(ch_id[ci_found])
    return out


# ================================================= B. constraint-chain linking
def rule_scorer(eq, vgap, tgap):
    diffs = (1 - eq).sum(axis=1)
    s = -diffs - 1e-3 * tgap          # fewest diffs; recency breaks ties
    s[diffs > MAX_DIFFS] = -np.inf
    return s

results["B constraint chains"] = evaluate(
    link(rule_scorer, lambda s: s > -np.inf), "B  constraint-chain linking",
    breakdown=True)

# ============================================ C. supervised pairwise matching
# Training pairs from the first 30 days, labelled by cookie co-occurrence.
train_mask = ts_days < 30
tr_idx = np.where(train_mask & pd.notna(cookies))[0]
rng = np.random.default_rng(3)


def feats(i, j):
    eq = (soft_codes[i] == soft_codes[j]).astype(float)
    vg = min(abs(versions[i] - versions[j]), 5) / 5
    tg = min(abs(ts_days[i] - ts_days[j]), 60) / 60
    return np.concatenate([eq, [vg, tg]])


by_cookie = defaultdict(list)
by_hard = defaultdict(list)
for i in tr_idx:
    by_cookie[cookies[i]].append(i)
    by_hard[hard_key[i]].append(i)

X, y = [], []
for c, idxs in by_cookie.items():
    if len(idxs) < 2:
        continue
    for _ in range(min(4, len(idxs))):
        i, j = rng.choice(idxs, 2, replace=False)
        X.append(feats(i, j)); y.append(1)
for k, idxs in by_hard.items():
    if len(idxs) < 2:
        continue
    for _ in range(min(400, len(idxs) * 3)):
        i, j = rng.choice(idxs, 2, replace=False)
        if cookies[i] != cookies[j]:
            X.append(feats(i, j)); y.append(0)
X, y = np.array(X), np.array(y)
clf = LogisticRegression(max_iter=2000).fit(X, y)
print(f"     C training pairs: {y.sum()} pos / {len(y)-y.sum()} neg "
      f"(cookie labels -- clone pairs are mislabelled negatives)")
print("     C learned weights:",
      {n: round(w, 2) for n, w in zip(SOFT + ["vgap", "tgap"], clf.coef_[0])})


def ml_scorer(eq, vgap, tgap):
    F = np.column_stack([eq, vgap, tgap])
    return clf.predict_proba(F)[:, 1]


TH = 0.5
results["C supervised matching"] = evaluate(
    link(ml_scorer, lambda s: s >= TH), "C  supervised pairwise matching",
    breakdown=True)

sweep = []
for th in [0.2, 0.4, 0.6, 0.8, 0.95]:
    s, m = evaluate(link(ml_scorer, lambda x, th=th: x >= th),
                    f"     C @ threshold {th:.2f}")
    sweep.append((th, s, m))
sweep = pd.DataFrame(sweep, columns=["threshold", "false_split", "false_merge"])

# ===================================================== D. anchored hybrid
results["D anchor only"] = evaluate(
    link(ml_scorer, lambda s: s >= TH, use_cookie_anchor=True),
    "D  anchored hybrid (recover only)", breakdown=True)

results["D anchor + veto"] = evaluate(
    link(ml_scorer, lambda s: s >= TH, use_cookie_anchor=True, cookie_veto=True),
    "D' anchored hybrid + cookie veto", breakdown=True)

# ------------------------------------------------------------------- plot
fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.5), sharey=True)
marks = dict(zip(results, ["s", "^", "o", "D", "*"]))
cols = dict(zip(results, ["#d62728", "#ff7f0e", "#9467bd", "#2a9d2a", "#1f77b4"]))
for ax, dt in zip(axes, ["desktop", "mobile"]):
    for name, (_, _, per_dt) in results.items():
        sp, mg = per_dt[dt]
        ax.scatter(mg, sp, marker=marks[name], color=cols[name],
                   s=140, label=name, zorder=3)
    ax.set(xlabel="false-merge rate (distinct browsers fused)",
           title=f"{dt} " + ("(high-entropy, drifting)" if dt == "desktop"
                             else "(cloned stock devices)"),
           xlim=(-0.05, 1.05))
    ax.grid(alpha=0.25)
axes[0].set_ylabel("false-split rate (returning browser missed = 1$-$'accuracy')")
axes[0].legend(fontsize=9)
fig.suptitle("Identification methods, split vs merge errors -- "
             "vendors publish only the y-axis", y=1.02)
plt.tight_layout()
plt.savefig("fp_methods_tradeoff.png", dpi=140, bbox_inches="tight")
print("\nSaved fp_methods_tradeoff.png")
