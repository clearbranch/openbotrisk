# Evidence Review Scope Guide

*Working document. Scopes the evidence review component (Component 8.1 of PROJECT.md). Companion to GOVERNANCE.md, which defines editorial discipline and AI usage. Edits welcome; treat changes as deliberate scope decisions, not silent drift.*

---

## 1. Purpose

This document defines what the project's evidence review covers, how it's organised, and how reading gets done. It exists so the work doesn't drift into unbounded reading or duplicate effort, and so the agent prompts that follow have a clear scope to operate within.

The term "evidence review" rather than "literature review" reflects that the project reads across source types — academic papers, vendor public material, technical documentation, threat surface writing, standards references — and treats them as evidence about the field rather than as canonical authority. Academic literature is one category among four, not the whole.

The evidence review is not preparation for the project. It is part of the project. Its output forms a substantial part of the site — the Foundations section, the Background and landscape section, and most of what's cited throughout. Time spent reading is time spent producing the artefact.

The goal is not academic completeness. The goal is to ground the project's writing in what's actually known and published, so that claims made on the site can be traced to sources and so that readers can follow the project's reasoning back to primary material.

---

## 2. Categories

The evidence review covers four categories. They have different source types, different reading methods, and different output forms. They are organised explicitly rather than merged into a single review because the differences matter.

### 2.1 Foundations

The basic concepts the project's other sections assume readers may need: how the internet identifies users and sessions, what an IP address is and isn't, how browser fingerprinting works at a basic level, what HTTP headers carry, what TLS adds, how cookies and authentication interact, what kinds of detection models exist at a high level.

Source types: technical documentation (MDN, RFCs at appropriate level, OWASP), web security tutorials and academies (PortSwigger Web Security Academy is a strong candidate), accessible introductory material on web protocols and security.

Output: the Foundations section of the site, written so a reader who needs this material in one place can find it without prerequisites beyond general technical literacy.

### 2.2 Vendor and industry evidence

Public material from companies operating in the bot and abuse prevention space and adjacent. Treated as evidence about what the field does and claims to do, not as targets of evaluation.

Source types: vendor technical blogs, white papers, conference talks, public patent filings where relevant, case studies, product technical documentation, threat reports vendors publish.

Specific vendors whose material is in scope (non-exhaustive, starting point):

- Bot management: Cloudflare, HUMAN, DataDome, Kasada, Arkose Labs, Netacea, PerimeterX
- WAF and broader application security: F5, Imperva, Akamai
- Cloud browser infrastructure: Browserbase, Browserless, Hyperbrowser, Bright Data
- Anti-fraud and related: Sift, Forter, Riskified (where bot-relevant)
- AI agent infrastructure: Anthropic (Claude in Chrome safety material), OpenAI agent material

Output: the Background and landscape section of the site, the Technical territory section where vendor descriptions illuminate techniques, citations throughout where claims about the field are made.

### 2.3 Academic and research literature

Peer-reviewed and pre-print academic work on bot detection, web abuse, behavioural biometrics, browser fingerprinting, and adjacent areas.

Source types: journal articles (Digital Threats, Computers & Security, IEEE Security & Privacy, ACM TWEB and similar), conference papers (USENIX Security, NDSS, CCS, IMC, WWW, RAID), theses where directly relevant, technical reports from academic groups.

Explicit anchors:

- Iliou 2022 thesis and the Iliou et al. 2021 Digital Threats paper — the academic anchor for advanced web bot detection
- OWASP Automated Threats to Web Applications — the field's nearest thing to a canonical taxonomy
- Recent surveys on bot detection techniques (especially those that classify by data source: network, fingerprinting, behavioural)
- Recent surveys on browser fingerprinting
- TLS fingerprinting / JA3 / JA4 work where relevant to bot detection

Output: the Technical territory section, the Methodology investigations section's framing, the reading register page.

### 2.4 Threat surface and territory

Material that describes how the threat surface looks in practice without being either basic foundations or academic theory. Includes how attacker tooling works, how automation infrastructure evolves, how the threat model is shifting (particularly around browser-native automation and AI agents).

Source types: OWASP automated threat handbook (sits across foundations and this category), scraper-side and evasion-side public material (treated as evidence of what attackers know defenders look for, with awareness of bias), GitHub repositories cataloguing detection signals, technical writing from independent security researchers, conference talks from non-vendor practitioners.

Specific items worth mentioning as starting points:

- OWASP Automated Threats to Web Applications (OAT taxonomy)
- ScrapFly and similar scraper-tooling technical writing
- niespodd/browser-fingerprinting GitHub catalogue
- Browser automation library documentation (Playwright, Puppeteer, Selenium) — particularly their stealth/anti-detection sections
- Anthropic, OpenAI safety material on browser agents

Output: the Browser-native automation parts of the Technical territory section, citations throughout.

### 2.5 Observed-use evidence (cross-cutting lane)

A distinction the first four categories blur: *capability evidence* ("this tool or technique exists") is weaker than *use evidence* ("it is observed against real sites"). The register tracks this with the `operational proximity` field (register appendix), **not** as a fifth category — observed-use material is not a single source silo, it is drawn from across the others:

- **Vendor telemetry** stays in §2.2 but is read for what it *observes in production* (proximity `observed`, vendor-measured), kept distinct from vendor *capability claims* (`capability` / `claimed`).
- **Measurement studies** stay in §2.3 but are the highest-value use evidence (proximity `measured`, independent) — bot, credential-stuffing, and ad-fraud measurement in the wild.
- **Victim-side engineering postmortems** and **enforcement / legal records** are the genuinely new source types this lane admits. They sit under §2.4 threat-surface, with the cautions in §3.

The lane is first-class because the project must not let "a mature bypass and automation tooling market exists" stand in for "these tools are used against real sites at scale." The first is well-supported by public sources; the second is mostly held in vendor and platform telemetry and, for prevalence specifically, is largely unenterable from outside. That boundary is itself a finding to state plainly, not an obstacle to work around.

### Standards and protocols as a cross-cutting tag

Standards and protocol references (RFCs, W3C specifications, TLS/JA3/JA4 reference material) are not a separate category but recur across categories. Sources are tagged `standards` in the reading register when they belong to this class. Used for canonical reference rather than treated as evidence to be analysed.

---

## 3. Scope boundaries

### What's in scope

- Methods, techniques, signals, infrastructure
- How automation works technically
- What defenders detect and how
- What's known about the limits of public-data research
- How the threat surface is shifting (browser-native automation, AI agents)
- Observed-use evidence: vendor production telemetry, independent measurement studies, victim engineering postmortems, and enforcement / legal records — read for technique and operational proximity (the `operational proximity` axis)

### What's out of scope

- Specific named threat actors and groups
- The criminal economics of abuse (who makes money, how money flows)
- Specific high-profile incidents or campaigns
- Vendor comparison or evaluation (vendors are sources, not subjects)
- Broader cyber security: malware, network intrusion, vulnerability research, EDR, IR
- IoT botnets and network-level DDoS
- Cryptography and protocol design beyond what's needed for foundations
- Legal and regulatory aspects of bot management (mentioned briefly if at all)

The methods-not-actors framing is sharp. A technique described abstractly is in; a campaign described with named actors is out. A vendor explaining how they detect credential stuffing is in; a threat intel report attributing a campaign to a named group is out.

**Legal and enforcement records: technique, not attribution.** Court filings, indictments, and enforcement actions are admitted *only* for the technique and operational proximity they evidence (e.g. "automated account creation with proxy rotation was used against a booking flow"). The named actor, the campaign, the victim's identity where sensitive, and the prosecutorial narrative are all out of scope. A legal record that cannot be used without retelling the campaign is not used. This admits the observed-use lane (§2.5) while keeping the methods-not-actors line intact.

**Dual-use sources: evidence, not recipe.** Bypass, anti-detect, and evasion sources — and the operational detail inside some legal and victim records — describe how controls are circumvented. The project cites them as evidence of the adversary's capability and mental model, and records *that* a technique exists and its operational proximity. It does **not** reproduce step-by-step bypass procedures or working evasion code, and it does **not** synthesise scattered details from several sources into a more complete how-to than any single source provides (the aggregation hazard — the real risk for a demystification site that reads widely across attacker-side material). Where a source's value cannot be captured without reproducing an operational recipe, summarise the claim and proximity and link out. Editorial enforcement of this lives in `GOVERNANCE.md`.

### Sources to read carefully or skip

- Verizon DBIR and similar incident-focused reports: skip in general (actor-focused), extract the rare technique-focused sections
- Vendor case studies that name attacks or attackers: skip the attribution, extract the technique
- Marketing material with no technical substance: skip
- Material primarily about compliance, governance, or risk management framing: skip
- Books on general web security or general cyber: skip unless specifically on web abuse/bot topics

---

## 4. Reading method per category

Different categories warrant different approaches.

### Foundations

Read efficiently. The material is largely settled and well-documented. The output is a clear synthesis in the project's voice, not an analytical contribution. Agent-assisted drafting works well here; the editorial review focuses on accuracy and pedagogical clarity.

### Vendor material

Read with explicit awareness of bias. Vendors describe what they do in marketing-flavoured language; extract technical content, distinguish claim from substantiation, note when claims are unverifiable from outside. The valuable output is structured extraction of what's claimed and what evidence supports it.

Vendor material is unlimited. The reading rule: extract a set of representative claims per vendor and stop. The goal is not to catalogue every blog post; it's to understand what the field claims to do.

### Academic literature

Read with structured extraction, similar to the pattern used for past research projects. For each paper: what it claims, what data it uses, what method it applies, what it finds, what its limitations are, what it doesn't address. Build a register entry per paper.

Academic literature is bounded but large. The reading rule: start with surveys and the anchor papers (Iliou, OWASP), follow citation chains forward and backward, stop when the citation network closes (you keep seeing the same papers cited by new ones).

### Threat surface material

Read with awareness of source provenance. Scraper-side material describes what attackers think defenders look for; vendor-side describes what defenders claim to do; independent researchers and academics provide the third corner. All three matter; none is neutral.

The reading rule: cover the major vendors of scraper tooling and the major detection writeups, but don't over-invest in either side.

### Observed-use and legal / enforcement material

Read for proximity first: what did the source actually *observe or measure* against a real target, versus assert? Separate vendor telemetry (`observed`, vendor-measured) from vendor capability claims (`capability` / `claimed`). For legal, enforcement, and victim postmortems, extract the technique and operational proximity and strip attribution per §3. Maintain prevalence humility throughout — even good observed-use evidence rarely supports market-wide prevalence claims, and the honest position is usually "observed in these settings," not "common across the web." Apply the dual-use no-recipe discipline (§3) on what gets reproduced.

---

## 5. Extraction fields per source

Every source read produces a register entry. The required fields:

| Field | What goes in it |
|---|---|
| Citation | Full reference; for vendor material, the URL and date accessed |
| Category | Foundations / vendor / academic / threat-surface |
| Tags | Including `standards` where relevant, plus topic tags |
| What it claims | The substantive claim(s) the source makes, in extracted form |
| What evidence it provides | What the source offers to support its claims |
| Operational proximity | How close the source sits to *observed abuse against a real target*: `capability` / `claimed` / `observed` / `measured` / `n/a`. Orthogonal to evidence basis (which records source type and rigour) — recorded separately so a lab result and a vendor blog are not flattened onto one axis. Defined in the register appendix |
| What signals or techniques it mentions | Specific signals (TLS fingerprint, click cadence, etc.) and methods (XGBoost, autoencoder, etc.) |
| What threat type it covers | Which OAT categories or similar |
| Scarce-resource abuse fields | Conditional fields for appointment, ticketing, reservation, product-drop, queueing, cancellation-monitoring, booking-flow, inventory-hoarding, and limited-inventory abuse. Defined in the register appendix. The scarce-resource-specific `evidence_of_use` field does not replace `operational proximity`; it classifies use evidence inside this narrower abuse pattern while `operational proximity` remains the broader corpus-level capability-to-use axis |
| Framing distance | What real-world bot/abuse problem this source approximates; what it fails to represent; what additional evidence would be needed to go further |
| What it cannot show | The limits of the source — what readers should not conclude from it alone |
| Project impact | How this source affects the project's writing or taxonomy |

The framing distance field is critical and recurring. It prevents the failure mode where public datasets, vendor blogs, academic papers, and commercial telemetry get treated as roughly equivalent evidence about the field. Each source approximates the real problem in different ways and fails to represent it in different ways. Naming this explicitly per source keeps the project's analytical position visible.

---

## 6. Output forms

The evidence review produces several distinct artefacts:

| Artefact | What it is | Where it lives |
|---|---|---|
| Reading register | One entry per source read, with the extraction fields above | `working/reading-register.md`, also published on the site |
| Foundations section | Pedagogical content covering the basics | `site/foundations/` |
| Background and landscape section | Threat model, actors-as-evidence, vendor landscape | `site/background/` |
| Technical territory section | What techniques exist, organised by family | `site/techniques/` |
| Decision notes | What the reading surfaced that affects project direction | `working/decisions.md` |
| Citations throughout | Every factual claim that could be checked is sourced | Inline on site pages |

The reading register is the bibliographic memory. Every source read produces an entry, whether or not it ends up cited in published content. Sources read and rejected are recorded with a brief note on why — saves future re-reading.

---

## 7. What "enough" looks like

Hard numbers are not committed upfront. Instead, three check-in triggers:

**First-batch review.** After approximately the first 10 sources in each category, review whether the scope is working: are the right things being included, is the framing surviving contact with the actual material, is anything important missing? Adjust the scope guide if needed.

**Citation network closure.** A category's reading is approximately complete when new sources mostly cite material already in the register. Continued reading produces diminishing returns. This is the natural endpoint for academic literature; vendor and threat-surface material has weaker closure properties.

**Site coverage check.** Each substantive section of the site has a "what this section claims" outline. Reading is enough for that section when the outline can be supported by cited sources. Sections that can't be supported get adjusted, not papered over.

These triggers are checks, not deadlines. The discipline is that they actually get applied — first-batch review actually happens, citation closure is actually noticed, site coverage is actually verified.

---

## 8. Agent automation

Agent automation is used heavily across all four categories. The working method is:

1. Author defines scope (this document) and prompt for a specific reading task
2. Agent does structured extraction from sources, produces draft register entries and (where relevant) draft site content
3. Author reviews per the editorial discipline defined in GOVERNANCE.md
4. Reviewed content goes into the reading register and, after further editorial work, onto the site

This is not blind delegation. The author remains responsible for what gets published; the agent reduces the labour cost of extraction and first-pass drafting. The detailed governance of how agent output is reviewed is in GOVERNANCE.md.

---

## 9. Anchors

Two anchors structure the reading:

**OWASP Automated Threats to Web Applications** acts as the spine for the threat taxonomy. The project builds on OWASP's framing rather than replacing it. Where the project says something that contradicts or extends OWASP, the disagreement is explicit. Every substantive page on the site passes the test: what does this clarify that a reader would not get by reading the relevant OWASP entry, a single vendor blog, or one academic paper alone?

**Iliou (2022 thesis, 2021 paper) and associated work** acts as the academic anchor for web bot detection specifically. It provides the simple / moderate / advanced bot sophistication taxonomy, the web logs + behavioural biometrics combined approach, and the evasion-aware framing that informs how the project thinks about adversarial pressure.

These anchors do not exhaust the literature. Other surveys, papers, and sources are read alongside. The anchors are reference points that subsequent reading is positioned against, not the totality of what gets read.

---

## 10. Open questions

Items left deliberately open at this stage:

- Whether to do a separate methodology-focused review for the methodology investigations component, or to fold relevant methodology papers into the general review
- How much of the fraud-analytics adjacent literature (graph-based fraud detection, social network analysis for fraud) to include given the methods-not-actors constraint
- Whether the controlled experiments component (PROJECT.md Section 8.3) needs its own targeted reading on browser automation and TLS fingerprinting
- How to handle non-English sources where relevant (probably out of scope but worth flagging)

These resolve as the reading progresses, not before.
