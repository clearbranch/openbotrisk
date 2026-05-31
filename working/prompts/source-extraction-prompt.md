# Agent prompt — source extraction for evidence review

You are extracting evidence from a single source for the `openbotrisk` project. Output is a structured register entry. This is not synthesis or drafting — that is a separate task. Extract what the source says and the metadata the project needs.

The repo already exists with `PROJECT.md`, `EVIDENCE-REVIEW.md`, and `GOVERNANCE.md` committed. Read all three before doing anything. They define scope, the extraction fields, and the editorial discipline. Treat them as authoritative.

---

## INPUTS

The author provides:

- **Source identifier**: URL for web sources, or relative path for locally archived sources
- **Category**: one of `foundations`, `vendor`, `academic`, `threat-surface`
- **Optional notes**: any context about why this source is being read, what to focus on, what to ignore

If any of these are missing or ambiguous, stop and ask.

---

## PROCESS

1. Read `PROJECT.md`, `EVIDENCE-REVIEW.md`, and `GOVERNANCE.md` in the repo
2. Access the source. For URLs, fetch the page. For PDFs, read the document. If access fails, stop and report
3. Identify the source type and key bibliographic metadata
4. Read the source enough to fill the extraction fields below honestly — not skimming, not exhaustive
5. Produce a register entry at `working/register-entries/<slug>.md` following the structure below
6. Do not modify the main reading register (`working/reading-register.md`) — the author merges entries manually after review
7. Report back with the file path of the entry and any flags raised

---

## OUTPUT STRUCTURE

The entry follows this template exactly. Every field is filled. If a field genuinely doesn't apply (rare), say so explicitly with reasoning rather than leaving blank.

```markdown
# <Title of source>

## Bibliographic

- **Citation**: Full reference. For academic: authors, year, title, venue, DOI if available. For vendor: organisation, title, URL, date accessed. For threat-surface: as appropriate to source type.
- **Source URL or path**: Direct link to the source, or relative path if archived
- **Date accessed**: YYYY-MM-DD
- **Category**: One of foundations / vendor / academic / threat-surface
- **Tags**: Topic tags as relevant. Include `standards` if the source is an RFC, W3C spec, or similar canonical reference. Other useful tags: `taxonomy`, `survey`, `methods`, `behavioural`, `fingerprinting`, `infrastructure`, `cloud-browser`, `ai-agent`, `tls`, `entity-resolution`, etc. Use existing tags if they fit; introduce new ones sparingly.

## What it claims

The substantive claim(s) the source makes, in extracted form. Bullet points, one claim per bullet. Use the source's own framing rather than the project's. If the source makes many claims, prioritise the load-bearing ones — claims that bear on the source's argument or that the project might cite.

Do not embed the project's opinion in this section. Just what the source says.

## What evidence it provides

For each significant claim, what the source offers to support it: experiments, datasets, case studies, references to other sources, or none. If a claim has no supporting evidence beyond assertion, say so. If the source is itself reporting empirical results, summarise the empirical basis (sample size, time period, method).

## Signals or techniques mentioned

Specific technical content the source describes. Bullet points. Examples of what goes here:

- Specific signals: TLS fingerprints, JA3/JA4, click cadence, mouse trajectory, navigator.webdriver, header order, etc.
- Specific methods: XGBoost, autoencoders, isolation forest, graph neural networks, sequence models, rule-based heuristics, etc.
- Specific infrastructure: cloud browser services, anti-detect browsers, residential proxy networks, etc.

This field exists so future searches across the register can find which sources cover which technical material.

## Threat types covered

Which OWASP OAT categories (e.g. OAT-001 Carding, OAT-008 Credential Stuffing, OAT-011 Scraping) or similar abuse categories the source addresses. If the source does not map to OAT, describe in the project's vocabulary (credential stuffing, scalping, scraping, account takeover, click fraud, etc.).

## Framing distance

This is the most important analytical field. Three parts:

- **What real-world bot/abuse problem does this source approximate?** What part of the operational territory does the source actually illuminate? Be specific.
- **What does it fail to represent?** What's absent, simplified, or biased about how the source approaches the territory? Common gaps include: missing adversarial pressure, controlled vs production data, single-site vs cross-site, missing commercial telemetry, dated threat model, etc.
- **What additional evidence would be needed to go further?** What would a reader need to actually understand the territory beyond what this source provides?

Be honest. The project's analytical position depends on naming framing distance per source explicitly.

## What it cannot show

The limits of the source — what readers should not conclude from it alone. Examples: "high accuracy on this dataset does not generalise to production traffic," "vendor claims about detection rates are not independently verifiable," "academic threat models pre-date AI browser agents." Distinct from framing distance in that this field names specific over-claims to avoid.

## Project impact

How this source affects the project's writing or taxonomy. Bullet points. Examples:

- "Provides the technical detail for the Foundations page on browser fingerprinting"
- "Vendor claim X is cited as evidence of what the field claims to do, with caveat that it is unverified"
- "Contradicts source Y's framing of credential stuffing detectability; worth surfacing the disagreement"
- "Read but offers nothing new beyond what is already in the register" (legitimate finding — record and move on)

If the source was read and rejected as not useful for the project, this field is where that decision is recorded with the reason.
```

---

## WORKED EXAMPLE

A fictional but representative example showing what a good entry looks like. Use this as the bar.

```markdown
# Detection of Advanced Web Bots via Mouse Movement Analysis — Smith et al. 2023

## Bibliographic

- **Citation**: Smith, J., Jones, A. (2023). Detection of advanced web bots via mouse movement analysis. *Journal of Web Security*, 12(3), 145-167. DOI: 10.1234/jws.2023.12.3.145
- **Source URL or path**: https://doi.org/10.1234/jws.2023.12.3.145
- **Date accessed**: 2026-05-31
- **Category**: academic
- **Tags**: behavioural, methods, advanced-bots, mouse-dynamics

## What it claims

- Mouse trajectory entropy and pause distribution distinguish human users from advanced bot frameworks in a controlled study
- Standard browser automation tools (Selenium, Puppeteer) produce mouse trajectories with significantly lower entropy than human users
- A CNN trained on mouse trajectory images outperforms classical statistical features at distinguishing the two classes
- Detection accuracy drops by 15-20% when bot trajectories are augmented with GAN-generated humanlike movement

## What evidence it provides

Controlled study with 200 human participants and 1000 bot sessions across three automation frameworks. Mouse movements collected via JavaScript probe on a custom test site over six weeks in 2022. Reports classification accuracy, precision, recall, ROC-AUC for several model variants on a held-out test set.

Empirical basis: single-site test environment, recruited human participants paid via Prolific. No production traffic, no real adversarial bots.

## Signals or techniques mentioned

- Mouse trajectory features: entropy, pause distribution, velocity profile, acceleration
- CNN on rasterised trajectory images
- Statistical baselines: SVM with engineered features
- GAN-based trajectory generation as adversarial test
- Standard automation tools: Selenium, Playwright, Puppeteer

## Threat types covered

Advanced web bots in the sense of OWASP OAT-021 (Denial of Inventory) and OAT-005 (Scalping) contexts — bot operators using browser automation to mimic human behaviour for value-extraction purposes. Does not address credential stuffing or scraping specifically.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** Detection of standard browser automation tools (Selenium, Puppeteer, Playwright) being used against a controlled site, where the automation is not specifically engineered to evade detection.
- **What does it fail to represent?** Production traffic with real adversarial pressure. Stealth automation tools (Puppeteer-stealth, undetected-chromedriver). Cloud browser services. Browser extensions and AI agents. Cross-site behavioural signals. The "humans" are paid participants in a controlled task, not representative of production users.
- **What additional evidence would be needed to go further?** Production data with real bot/human mix, evaluation against modern stealth automation, longitudinal data showing how detection survives adversarial adaptation.

## What it cannot show

- That the reported accuracy generalises to production traffic — the controlled setting biases toward easier detection
- That CNN-on-mouse-trajectory is the right approach in operational settings (cost, latency, evasion resistance not assessed)
- That mouse movement alone is sufficient — the paper does not test fusion with other signals
- That the 15-20% adversarial degradation is the worst case — GAN-based augmentation is one specific adversarial strategy, not the strongest possible

## Project impact

- Provides empirical anchor for the Technical territory page on behavioural detection — concrete claim that mouse-based detection is feasible in controlled settings
- Reinforces the project's framing-distance point: "high accuracy in controlled studies does not transfer cleanly to production"
- Cited on the Behavioural detection methods page as one of several sources documenting the mouse-trajectory approach
- The GAN augmentation result is worth surfacing as evidence that adversarial evaluation matters even when omitted from baseline studies
```

---

## STOP AND ASK CASES

In any of these situations, stop and report back rather than proceeding:

- The source identifier doesn't resolve (broken URL, missing file, paywall)
- The source is much longer than expected and would require its own multi-pass treatment (long books, multi-volume technical references)
- The source's category is unclear — it doesn't fit cleanly into foundations / vendor / academic / threat-surface
- A required extraction field genuinely cannot be filled from the source content
- The source claims something that contradicts another entry already in `working/register-entries/` — flag the contradiction rather than silently resolving
- The source appears to be out of scope per `PROJECT.md` Section 3
- The source contains material from a category explicitly out of scope (named threat actors, criminal economics, broader cyber) — flag rather than extract
- Citations or bibliographic metadata are ambiguous (missing author, missing date, multiple plausible references)
- The source's reading method per `EVIDENCE-REVIEW.md` Section 4 seems to require an approach beyond what this prompt covers
- Any other ambiguity that would require the author's judgement rather than the agent's

When stopping, report:

- What was attempted
- What the issue is
- What additional information or decision is needed from the author

Do not invent answers. Do not skip fields. Do not make scope judgements on the author's behalf.

---

## CONSTRAINTS

| Do | Don't |
|---|---|
| Read all three scope documents before starting | Skip context-reading because the task seems clear |
| Use the source's own framing in "What it claims" | Insert project opinion into the claims field |
| Be specific in framing distance | Use generic phrases like "limited generalisability" |
| Use existing tags where possible | Invent new tags casually |
| Flag contradictions with prior entries | Silently resolve disagreements between sources |
| Cite by stable identifier where available (DOI, archived URL) | Cite by transient links that may rot |
| Report runtime and any access issues | Optimise for appearing successful |

---

## DEFINITION OF DONE

The extraction is complete when:

- An entry file exists at `working/register-entries/<slug>.md` with all fields filled
- The slug is descriptive (e.g. `iliou-2022-thesis.md`, `cloudflare-bot-management-2024.md`)
- Every claim in "What it claims" is something the source actually says
- "Framing distance" is specific, not generic
- Bibliographic metadata is complete and accurate
- The author can read the entry and know whether to read the source themselves

Report back with:

- The file path of the entry
- Runtime
- Any "stop and ask" cases that were not actually blocking but worth flagging
- Anything notable about the source that doesn't fit the template fields but the author should know

---

## OPERATING RULES

- Do not modify `PROJECT.md`, `EVIDENCE-REVIEW.md`, `GOVERNANCE.md`, `REPO.md`
- Do not write to `working/reading-register.md` — the author merges entries manually
- Do not commit, do not push, do not interact with any remote
- Do not produce site content, synthesis pages, or anything beyond the register entry
- Do not improvise around missing information — ask
- Stay within scope per `PROJECT.md` Section 3 — flag out-of-scope sources rather than extracting

