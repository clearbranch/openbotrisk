# Dataset reference pages — scaffold

Four `.qmd` dataset-reference pages, scaffolded from the `notebooks/eda/*.ipynb`
EDA notebooks. **Status: scaffold — framing written, computed numbers left as
marked placeholders.** Tomorrow's job is mechanical: run each notebook against
the real data and paste figures into the marked slots.

## What these are

The EDA notebooks already emit descriptive markdown reports (via
`openbotrisk.eda.report.write_report` → `working/eda/<name>.md`). Those reports
are mechanical: schema, label balance, identifiers, missingness, quirks. They're
provenance, not analysis. These pages wrap that provenance in the site's
house-style framing so each dataset gets a **reader-facing reference page** that
states, up front, *what real bot/abuse problem the dataset approximates and what
it cannot show* — the framing-distance discipline the evidence register mandates
but the bare reports omit.

They are **dataset-reference pages, not investigations.** They describe a
resource; they do not run a method against it. That distinction is a guess on my
part (see "Open decisions" below) — they could be promoted to fuller
investigations if you'd rather.

## The placeholder convention

Every value the notebook *computes* from data appears as:

```
{{ FILL: short description of the number — from <notebook cell> }}
```

These are the only things that need filling. Everything in prose — schema
descriptions, identifier roles, quirks, the framing — is **authored** (lifted
from the notebook's own hardcoded strings or written here) and is correct as-is.

**Do not fabricate placeholder values.** A blank `{{ FILL }}` is safe; a
plausible-looking wrong number is not. The whole point of marking them is so a
reader (or you, tomorrow) can see at a glance what's real vs pending.

## Filling them tomorrow

Two routes:

1. **Run the notebook, copy from the emitted report.** Each notebook still
   writes `working/eda/<name>.md`; the `{{ FILL }}` slots map 1:1 onto sections
   of that report. Fastest path.
2. **Render the qmd with live code.** If you'd rather these execute inline
   (so they stay reproducible on re-render), the code cells from the notebook
   can be embedded — but that needs the data present and `openbotrisk.eda`
   importable at render time, which couples the site build to the datasets.
   Probably not what you want for a public site; route 1 keeps the page static
   and the heavy data out of the render path.

## Where they go

The README's navigation table suggests two candidate homes:

- `site/reading/` — "Literature register and primary sources." Datasets-as-
  sources fits here; these become the data-provenance companions to the
  literature register.
- `site/boundaries/` — "What can and cannot be replicated from public data."
  The framing-distance / what-it-cannot-show emphasis fits *especially* well
  here; that section's whole remit is the public-data limitation these pages
  document per-dataset.

My lean: **`site/boundaries/`**, because the load-bearing content of each page
is the gap between the dataset and the real problem, which is exactly that
section's subject. But `site/reading/` is defensible if you'd rather keep all
source-provenance in one place. Flagged for you.

## Open decisions (for tomorrow)

- [ ] **Reference pages vs investigations.** Built as the former. Promote any to
      the latter if you want a method run against the data (e.g. the identifier
      graph on IEEE-CIS, synchrony on TalkingData — both already flagged in the
      live-site TODO §9).
- [ ] **Section home:** `site/boundaries/` (my lean) or `site/reading/`.
- [ ] **`ctu-13`:** the scope keep/cut from TODO §9 is unresolved. The page is
      scaffolded but carries a prominent scope-warning callout. **Do not publish
      it without resolving the keep/cut** — it's network-layer netflow, which
      your scope excludes. Left in the batch so the decision is concrete, not so
      it ships by default.
- [x] **Index page:** `site/public_datasets/index.qmd` lists the datasets with
      one-line framing each.
- [ ] Confirm the `openbotrisk.eda` loader paths and `data/` subdir names match
      what the pages state in their Reproduction sections (I copied them from the
      notebooks, but couldn't verify against the repo).

## Files

| File | Dataset | On-remit? |
|---|---|---|
| `web-robot-sessions.qmd` | Figshare 3477932 web-robot detection | **strongest** — labelled web sessions |
| `ieee-cis-fraud.qmd` | Kaggle IEEE-CIS fraud detection | strong — identifier-graph companion |
| `talkingdata-adtracking.qmd` | Kaggle TalkingData click-fraud | partial — synchrony companion, conversion-label |
| `ctu-13.qmd` | CTU-13 botnet netflow | **scope-risk** — resolve keep/cut first |
| `index.qmd` | section index | — |
