# Repo structure and immediate todos

*Operational working document. Companion to `PROJECT.md` (which sets scope) — this document handles the practical question of how the work is organised in the repo.*

---

## Intention

This repository holds everything for `openbotrisk`: the public site, the code that supports its writing and methodology investigations, and the working documents that record the project's decisions and reading.

It is structured for a long-horizon information project with a single primary author initially and possible contributors later. Optimised for: clarity of structure, ease of returning to after a break, contribution-readiness without contribution-driven scaffolding upfront.

One repo, not two. The site, the code, and the working documents live together. The model is `open-road-risk`'s, with adjustments for the demystification framing.

---

## Directory structure

```
openbotrisk/
├── README.md                 # Repo-level orientation (what is this, how to navigate)
├── PROJECT.md                # Scope document (the guiding statement of intent)
├── REPO.md                   # This file — operational structure and todos
├── LICENSE                   # MIT for code, CC BY 4.0 for written content (split noted in file)
├── .gitignore                # Standard Python + Quarto + macOS/Linux ignores
├── .pre-commit-config.yaml   # ruff, detect-secrets, large-file checks
├── pyproject.toml            # Python project config (ruff, dependencies, build)
├── environment.yml           # Conda environment specification
│
├── _quarto.yml               # Site configuration
├── index.qmd                 # Site landing page
│
├── site/                     # All site content (Quarto markdown)
│   ├── orientation/          # What this is, how to read, scope
|   ├── foundations/          # Basics 
│   ├── background/           # Threat model, landscape, vendor evidence
│   ├── techniques/           # Technique families: detection, fingerprinting, etc.
│   ├── methodology/          # Methodology investigations (writeups)
│   ├── boundaries/           # What can and cannot be replicated from public data
│   ├── reading/              # Literature register and primary sources
│   └── open-questions/       # Gaps, disagreements, unresolved issues
│
├── src/                      # Code supporting the methodology investigations
│   └── openbotrisk/          # Importable package (analysis, plotting, utilities)
│
├── notebooks/                # Exploratory work, not yet site-ready
│
├── data/                     # Local data references (gitignored except docs)
│   └── README.md             # What datasets, where they live, how to obtain
│
├── working/                  # Internal working documents (committed but not on site)
│   ├── decisions.md          # Decision log: choices made and why
│   ├── reading-register.md   # Tracked reading with status and notes
│   └── dataset-assessment.md # Comparative dataset assessment (when started)
│
├── tests/                    # Tests for src/ code
│
└── .github/
    └── workflows/            # CI: ruff, pytest, Quarto build check
```

### Why this structure

- **`site/` separate from `src/`** — the written artefact is the deliverable; code supports it. Keeping them separate makes both easier to navigate.
- **`working/` for internal-but-public documents** — committed to the repo, visible to anyone reading the GitHub view, but not built into the site. Decisions log and reading register live here.
- **`data/` mostly gitignored** — datasets are large, often licence-restricted, often updating. The directory's README documents what data is expected and where to get it.
- **`notebooks/` for exploration** — accepts that not all work goes straight to site-ready. Cleaned-up findings move into `site/` writeups; the notebook itself remains in `notebooks/` for reproducibility.
- **`src/openbotrisk/`** — importable Python package, not a flat scripts directory. Forces some structural discipline from the start.

---

## Tooling

Concrete commitments. Versions pinned in dependency files as work begins; this section names the choices.

| Concern | Choice | Reason |
|---|---|---|
| Language | Python 3.11+ | ORR convention; broad library support |
| Environment | conda + `environment.yml` | ORR convention; reproducibility for non-pip dependencies (Quarto, geo libraries if needed) |
| Linting / formatting | ruff | ORR convention; fast, single tool |
| Pre-commit | pre-commit framework | ruff, detect-secrets, large-file checks |
| Site framework | Quarto | ORR convention; matches the writing-led project shape |
| Site hosting | GitHub Pages from `gh-pages` branch | Free; standard Quarto deployment |
| Domain | `https://clearbranch.github.io/openbotrisk/` pointed at GitHub Pages | Stable URL, simple setup |
| CI | GitHub Actions | Run ruff, pytest, and Quarto build on PRs |
| Branch protection | Required on `main` | PR-based workflow; no direct commits |
| Issue tracking | GitHub Issues | Sufficient for solo-with-possible-contributors |
| Decision recording | `working/decisions.md` | Lightweight log, not formal ADRs |

Tooling decisions explicitly deferred (decide when relevant, not now):
- Graph library (NetworkX vs igraph vs PyTorch Geometric) — defer to methodology phase
- Large-data tooling (DuckDB vs Polars vs Spark) — defer until datasets are committed
- Static analysis beyond ruff (mypy?) — defer
- Documentation tooling for the `src/` package — defer until package is non-trivial

---

## Licensing

Split licence appropriate for a code-and-writing project:

- **Code** (everything in `src/`, `notebooks/`, `tests/`): MIT
- **Written content** (everything in `site/`, the README, project documents): CC BY 4.0
- The `LICENSE` file at the root documents both and which applies where

The CC BY 4.0 choice means anyone can reuse, adapt, and republish the writing with attribution. This matches the demystification intent — the work exists to be used by others, including future builders.

---

## Immediate todos

### Setup (do once, then stop)

- [ ] Create GitHub org `openbotrisk` (confirm namespace available)
- [ ] Create repo `openbotrisk/openbotrisk`
- [ ] Initialise with this file, `PROJECT.md`, `README.md`, `LICENSE`
- [ ] Set branch protection on `main` (require PRs)
- [ ] Set up `.pre-commit-config.yaml` with ruff, detect-secrets, large-file checks
- [ ] Set up `pyproject.toml` and `environment.yml` (minimal initial dependencies)
- [ ] Set up GitHub Actions for ruff and pre-commit on PRs
- [ ] Register `https://clearbranch.github.io/openbotrisk/` domain
- [ ] Set up `_quarto.yml` with site skeleton
- [ ] Configure GitHub Pages deployment from a `gh-pages` branch
- [ ] Verify site builds locally and deploys to `https://clearbranch.github.io/openbotrisk/`
- [ ] Add minimal `index.qmd` (placeholder, points to PROJECT.md content reformatted)

### Phase 0 — Orientation (the actual work that follows setup)

Reading and orientation, before any methodology investigation begins. The output of this phase is the early `site/` content and a populated `working/reading-register.md`.

- [ ] Read OWASP Automated Threat Handbook end-to-end; summarise into `site/background/`
- [ ] Identify and read 10-15 vendor public technical documents (whitepapers, technical blog posts, conference talks): Netacea, Cloudflare Bot Management, DataDome, HUMAN, Kasada, Arkose, others
- [ ] Identify and read 5-10 academic publications on bot detection and adjacent areas; literature register page in `site/reading/`
- [ ] Identify and read independent technical writing on this category: Troy Hunt, blog posts from anti-fraud teams that have published, conference talks (BSides, OWASP, RSA)
- [ ] Identify and read public threat intelligence reports on bot operations: industry reports, F5 Labs, Imperva Bad Bot Report, etc.
- [ ] Sanity check: does the project's intended map of the territory duplicate existing maps? Document conclusion in `working/decisions.md`
- [ ] Draft the orientation page: who this is for, how to read, scope and non-scope (the PROJECT.md content adapted for an external reader)
- [ ] Draft the first version of the background/landscape page: threat model, actors, economics, why bot pressure exists

### After Phase 0 (deferred decisions)

To be decided when Phase 0 reading is far enough along to inform the choice:

- [ ] Phase 1 first chunk: what specific 2-3 month piece launches the substantive work
- [ ] Methodology component scope: which public datasets, which layers, which methodology questions
- [ ] First methodology investigation: design document before code

---

## Operating discipline

A few practical habits, recorded so they don't drift:

**Per-piece definition of done.** A piece of writing is "done" when: it has a clear thesis, supporting evidence is cited, the writing reads through cleanly for the intended audience, and limitations are stated explicitly. Pieces that don't meet this stay in `notebooks/` or as drafts; only done work appears in `site/`.

**Decisions get logged.** Any choice that someone (including future-you) might reasonably question goes in `working/decisions.md` with a short rationale. Examples: tooling choices, dataset choices, scope decisions, names of things. The log is append-only; revisions are new entries, not edits to old ones.

**Reading gets registered.** Anything substantive that informs the writing goes in `working/reading-register.md`: full reference, status (queued / read / extracted), brief notes on relevance. The register is the project's bibliographic memory.

**No private branches for long.** Work either ships to `main` via PR within a few days, or it gets explicitly noted in `working/decisions.md` as long-running. Dead branches are pruned.

**Writing lags experiments, but not by much.** Definition of done for any methodology experiment includes a writeup. An experiment that runs but isn't written up does not count as progress.

---

## What this document is not

- Not a roadmap. PROJECT.md sets scope; the order of work emerges as Phase 0 reveals what matters.
- Not a contribution guide. Premature.
- Not exhaustive. Things missing here are decisions deferred, not decisions skipped.

Edit when the structure or todos genuinely need to change. Don't iterate on this document for its own sake.
