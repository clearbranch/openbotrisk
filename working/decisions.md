# Decision log

Append-only. Each entry records a choice and its rationale. Revisions are new entries, not edits to old ones.

## Format

```
## YYYY-MM-DD — Decision title

**Decision:** What was decided.

**Rationale:** Why this choice was made over the alternatives. Include constraints, references to REPO.md or PROJECT.md where relevant.
```

---

## 2026-05-23 — Single-repo structure

**Decision:** One repo (`openbotrisk/openbotrisk`) holds site content, code, notebooks, and working documents together.

**Rationale:** Splitting site and code into two repos introduces cross-repo coordination overhead with no benefit at this stage. The model follows `open-road-risk`. Structure can be revisited if the repo becomes unwieldy.

---

## 2026-05-23 — Split licence

**Decision:** MIT for code (`src/`, `notebooks/`, `tests/`); CC BY 4.0 for written content (`site/`, project documents).

**Rationale:** The project exists to be read and used. CC BY 4.0 allows anyone to reuse, adapt, and republish the writing with attribution, matching the demystification intent. MIT is standard permissive for code. See `LICENSE` for the full text of both.

---

## 2026-05-23 — Tooling choices

**Decision:** Python 3.11, conda + `environment.yml`, ruff (line-length 100), pre-commit, Quarto, GitHub Pages from `gh-pages` branch.

**Rationale:** Follows ORR convention. Quarto fits a writing-led project where the site is the deliverable. GitHub Pages is free and the standard Quarto deployment target. ruff at line-length 100 matches ORR convention; no strict docstring/naming rules because the codebase is exploratory.
