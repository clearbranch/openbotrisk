# Background page — status & editorial notes

Internal companion to `index.qmd` (the "Background and landscape" page). Not part of the published page. Holds the scope judgements, source review state, evidence gaps, revision notes, and open questions that were previously narrated inline on the page itself. Keep editorial status here; keep the page as clean prose.

## Scope judgement — economics in/out boundary

The two governing documents do not align perfectly. `PROJECT.md` §5 lists "the economics of bot activity" as part of this section. `EVIDENCE-REVIEW.md` §3 marks "the criminal economics of abuse — who makes money, how money flows" as *out* of scope. The reconciliation taken on the page: the **cost structure of automation** (what it costs an adversary to run bots — tooling, proxies, CAPTCHA-solving) is in scope, because it bears directly on what defences are trying to change. The **revenue structure of abuse** (who profits and how money moves) is out. This is a judgement, not a settled decision — flagged for review.

## Open scope question — privacy / regulatory strand

The register has picked up a privacy/regulatory strand: GDPR/AI Act review (Martínez Llamas et al. 2025), a scraping-legality explainer (ScrapingBee), and the BOTS Act enforcement record (FTC 2021). Whether this belongs on the background page as territory description, or sits outside scope as policy/advocacy, is unresolved — it turns on a PROJECT.md / EVIDENCE-REVIEW.md scope reconciliation not yet done. Currently left off the page.

## Source review state

- **OWASP Automated Threat Handbook v1.3** (SRC-027): entry is `needs review` and was produced without the repo scope docs. Until reviewed, OAT codes on the page are confirmed against OWASP's public project materials rather than treated as settled from the handbook.
- **OAT code verification TODO** — codes not yet verified against the full handbook, named on the page without a number:
  - carding / card-cracking (payment-flow abuse)
  - loyalty, promotion, and stored-value abuse
  - API / business-logic abuse

## Evidence gaps (named in scope, not yet covered)

- **Anti-fraud adjacency** — Sift, Forter, Riskified (where bot-relevant): named in scope, not yet in the register.
- **Agent-builder primary sources** — Anthropic's Claude-in-Chrome safety material, OpenAI's agent material, and equivalents: named in scope, not yet extracted. This is the most important specific gap in the AI-agent section — the page can describe how *defenders* and *independents* see AI agents, but not how the people *building* them describe them.
- **WAF / broader application security** — now partially covered (F5, Imperva/Thales, Akamai); was previously a full gap.

## Revision notes

- **Advanced-bot AUC corrected 0.68 → 0.64.** Verified against Iliou et al. 2019 (ARES) Figure 5 and the Iliou 2022 thesis. Both report the same 0.64 on the same MKLab web-log data, so they corroborate one figure rather than giving two; the low-FPR detail (18/123 advanced bots at FPR=0.01, ~55% balanced accuracy) is from the 2019 paper. The register's SRC-011/SRC-012 rows still need the same correction (inventory + framing ledger still read ~0.68).
- **FP-Inconsistent (SRC-015) downgraded from "single anchor".** The first draft called it the *single* external operational check on a commercial detector. The register now holds several independent / observed-use anchors (FP-Agent, Wardle, Jarad & Bıçakcı), so that claim was corrected on the page.
- **AI-agent "one side only" claim softened.** The first draft said the AI-agent surface was seen "almost entirely through defender-vendor framing… one side only". Softened once an independent measurement (Wang et al. 2026, FP-Agent) and a first-party operator account (Wikimedia 2026) were added — the remaining one-sidedness is specifically the absent agent-builder material.
- **SRC-018 caveat sharpened.** From "weak labels" to the label-leakage / circularity point (the `application` field is both the labelling rule and a model feature), matching the v2 re-extraction.

## Open questions

- Where exactly the in-scope/out-of-scope line on "economics" should sit — the cost-of-automation vs money-flow split is a working judgement.
- Whether the defence-side landscape can be given any neutral structure at all, or whether it is irreducibly vendor-described — and if the latter, whether that opacity is itself a finding worth foregrounding.
- Whether the corpus-wide `operational proximity` finding — capability and market existence are well-evidenced; real-world prevalence and efficacy are not — should be the *headline* claim of the section rather than a caveat threaded through it.
- How much weight the small set of operational/measured anchors (Venugopalan et al. 2025; Wang et al. 2026, FP-Agent; Wardle 2019; Jarad & Bıçakcı 2026) can bear, given each is a single setting, a specific threat model, or a dated/weak-label dataset.
- Whether **scarce-resource abuse** now warrants its own subsection (or page), given it has moved from abstract OAT mapping to observed (DVSA 2023) and legal-record (FTC 2021) evidence with a direct booking-style-worked-example fit.
- Whether the privacy/regulatory strand belongs on this page as territory description or is out of scope as policy.
