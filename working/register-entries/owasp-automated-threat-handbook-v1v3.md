# OWASP Automated Threat Handbook (Web Applications) v1.3 — Watson & Zaw 2026

> **STATUS: PROVISIONAL DRAFT.** Produced without access to `PROJECT.md`,
> `EVIDENCE-REVIEW.md`, `GOVERNANCE.md`, or the existing `working/register-entries/`.
> Source-derived fields are complete and reliable. Fields marked `[PROVISIONAL]`
> depend on the scope documents / existing register and must be reviewed before merge.
> `Category` is a proposal, not a decision — confirm before merging.

## Bibliographic

- **Citation**: Watson, C. & Zaw, T. (2026). *OWASP Automated Threat Handbook: Web Applications*, Version 1.3. OWASP Foundation. Published 17 March 2026. ISBN 978-1-291-76891-6. Licensed CC BY-SA 3.0. © 2015–2026 OWASP Foundation.
- **Source URL or path**: `/mnt/user-data/uploads/automated-threat-handbook-EN-1v30.pdf` (archived upload). Canonical project page: https://owasp.org/www-project-automated-threats-to-web-applications/ ; InDesign/PDF sources: https://github.com/OWASP/www-project-automated-threats-to-web-applications/tree/master/assets/files/EN
- **Date accessed**: 2026-06-01
- **Category**: `[PROVISIONAL — proposed: foundations]`. Reasoning: this is the canonical, vendor-neutral OAT *ontology/terminology* reference (a de facto industry-standard taxonomy), not an empirical study (`academic`), a product writeup (`vendor`), or a description of the live attacker ecosystem (`threat-surface`). It defines the vocabulary other sources are mapped to. `threat-surface` is a defensible alternative since it enumerates threats; resolve against `PROJECT.md` §3.
- **Tags**: `[PROVISIONAL — must reconcile with existing register tags]` — proposed: `taxonomy`, `standards` (de facto, not an RFC/W3C spec), `ontology`, `countermeasures`, `credential-stuffing`, `scraping`, `scalping`, `ai-agent`, `behavioural`, `fingerprinting`. Introduced sparingly: `ontology` may duplicate `taxonomy` — collapse if the register already has one.

## What it claims

- A core framework of **21 unique, unordered OWASP Automated Threats (OATs)** describes the abuse of *valid* web application functionality, deliberately excluding tool-based exploitation of single-issue implementation vulnerabilities.
- The ontology's purpose is to provide a **vendor-neutral, technology-agnostic common vocabulary** for developers, architects, operators, owners, security engineers, purchasers and vendors — answering the operational question "what is happening right now?".
- Threat events are categorised by the **intent of the attacker**, not by outcome; consequently the same observed method can map to different OATs depending on intent (e.g. a list of email addresses → OAT-007 Credential Cracking if used against authentication, or OAT-011 Scraping if used to enumerate users).
- **Scope** is web-application abuse of inherent functionality / business-logic flaws; explicitly out of scope are implementation bugs, native mobile apps, other layer-7 protocols (FTP/SMTP), network/HTTP/SSL-TLS DoS, host addressing, Man-in-the-Browser, phishing/pharming/trojan distribution, and non-web business fraud (return fraud, etc.).
- **v1.3 change**: OAT-003 was renamed from *Ad Fraud* to **Cost-Inflation Fraud**, generalising beyond advertising clicks to messaging, metered APIs and AI/RAG-driven traffic; the stated underlying pattern is *falsification of billable interactions to extract revenue*.
- Each OAT is cross-referenced to **CAPEC v3.9, CWE v4.18, WASC Threat Classification v2.0, and OWASP attack categories**; most map to CAPEC-210 / WASC-42 (Abuse of Functionality) and WASC-21 (Insufficient Anti-Automation).
- **14 vendor-agnostic countermeasure classes** (Value, Requirements, Testing, Capacity, Obfuscation, Fingerprinting, Reputation, Authentication, Rate, Monitoring, Instrumentation, Contract, Response, Sharing) are mapped across Builder/Defender SDLC stages and Prevent/Detect/Recover types.
- Not all automation is unwanted (e.g. search-engine indexing, monitoring), and some OATs may be conducted by or with owner consent.

## What evidence it provides

The handbook is a **consensus/expert-derived taxonomy, not an empirical measurement study.** Its evidential basis is methodological provenance rather than data:

- Literature review beginning January 2015: 150+ identified sources yielding 600+ data points (threats, attacks, some vulnerabilities), reduced via a large-scale clustering diagram and de-duplication (≈40 clusters → 24 candidate names → 20 in v1.0; OAT-021 added in v1.2 → 21).
- Comparison against OWASP Top 10, OWASP Proactive Controls, WASC WHID, CAPEC, CWE — none of which were judged to give the owner-viewpoint coverage sought.
- Limited peer review over a few months (AppSec EU/USA 2015, online + printed survey, OWASP Project Summit interviews).
- The full bibliography is **not contained in the handbook** (hosted on the project site), so per-claim primary sourcing cannot be assessed from this document alone.
- **No empirical content**: no prevalence/base-rate data, no detection-performance figures, no datasets, no sample sizes. The handbook itself names prevalence data as an open gap it is seeking help on (Roadmap).

## Signals or techniques mentioned

Content sits at the **countermeasure-class / symptom level, not the algorithm level** — useful for "which OATs reference which detection surfaces," not for ML method coverage.

- **Detection signals (Fingerprinting/Reputation classes):** User-Agent string, HTTP request format & header ordering, HTTP header anomalies/inconsistencies, device fingerprint content; IP address/range/geolocation/VPN reputation; behavioural signals (previous site, entry point, time of day, request rate, new-session-generation rate, navigation paths); resource-access patterns (static vs dynamic, hidden/invisible links, robots.txt and excluded paths, honeytrap resources, cache-defined resources, JS-generated links), and resources *not* accessed.
- **Mechanisms/methods:** rate limiting (per session/user/IP/device/fingerprint), URL/field-name/token randomisation (obfuscation), session/page-specific tokens, deny/block lists & third-party reputation/credit services, CAPTCHA, behavioural biometrics, queuing/asset-allocation randomisation, honeypots, real-time instrumentation/observability with automated response, UGC moderation.
- **Per-OAT symptoms** (cross-searchable): failed-login rates, account-lock rates, basket abandonment, reduced average basket price, chargebacks, GET/POST:HEAD request ratios, static:dynamic content ratios, 404/503 error clustering, faster-than-average multi-step progression, hyperlink density in UGC.
- **Absent:** named ML model families (XGBoost, autoencoders, isolation forest, GNNs, sequence models), JA3/JA4 / TLS fingerprints, mouse-trajectory/click-cadence behavioural detail, cloud-browser/anti-detect-browser/residential-proxy infrastructure. The handbook is one abstraction level above these.

## Threat types covered

This document **is** the OAT taxonomy, so it is the canonical source for all 21 categories: OAT-001 Carding, OAT-002 Token Cracking, OAT-003 Cost-Inflation Fraud, OAT-004 Fingerprinting, OAT-005 Scalping, OAT-006 Expediting, OAT-007 Credential Cracking, OAT-008 Credential Stuffing, OAT-009 CAPTCHA Defeat, OAT-010 Card Cracking, OAT-011 Scraping, OAT-012 Cashing Out, OAT-013 Sniping, OAT-014 Vulnerability Scanning, OAT-015 Denial of Service, OAT-016 Skewing, OAT-017 Spamming, OAT-018 Footprinting, OAT-019 Account Creation, OAT-020 Account Aggregation, OAT-021 Denial of Inventory.

## Framing distance `[PROVISIONAL — depends on PROJECT.md scope]`

- **What real-world bot/abuse problem it approximates:** the *defender's naming layer* for unwanted automation against web applications — the abstract intent/category of "what is happening," plus a structured countermeasure vocabulary. It illuminates how to *talk about* and *classify* automated abuse consistently across stakeholders.
- **What it fails to represent:** the *detection* layer (no signal efficacy, no algorithms, no thresholds); empirical prevalence and base rates; adversarial dynamics and the evasion arms race; production telemetry; the fact that intent-based categories are not cleanly separable from observed behaviour (the handbook concedes one method can be several OATs by intent); countermeasure *effectiveness* (everything is "consider…"). The v1.3 AI/RAG/LLM additions are taxonomic acknowledgements, not modelling of AI-browser-agent detection.
- **What additional evidence would be needed:** vendor and academic sources for concrete detection signals and their measured performance; prevalence/telemetry data; adversarial evaluation; AI-agent-specific behavioural evidence.

## What it cannot show `[PROVISIONAL framing — limits themselves are source-grounded]`

- That any OAT is *detectable* in practice, or with what precision/recall — there is no detection-performance content.
- Prevalence or base rates of any OAT — explicitly a stated gap, not an omission to be inferred around.
- That the intent-based categories partition cleanly in production traffic — the document itself states a single behaviour can map to multiple OATs by intent.
- That any listed countermeasure works, or its cost/latency/evasion-resistance — the classes are suggestions, unevaluated.
- That it reflects the current AI-agent threat surface empirically — the 2026 AI/LLM references are definitional, not measured.

## Project impact `[PROVISIONAL — depends entirely on PROJECT.md]`

- Most likely role: the **canonical taxonomy backbone** for `openbotrisk` — the OAT identifiers/definitions that other (vendor/academic/threat-surface) sources are mapped onto.
- Supplies the **intent-based framing** and the stable vocabulary; supplies the countermeasure-class scaffolding.
- **Caveat to carry forward:** cite it as authority for *naming and definitions*, never as evidence of *detectability, prevalence, or countermeasure efficacy* — those must come from other categories. This is the load-bearing distinction for any page that leans on it.
- Cannot be checked against existing entries for contradictions here (register inaccessible); flag a contradiction-check at merge, especially against any vendor source that claims detection rates per OAT.
