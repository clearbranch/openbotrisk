# OWASP Automated Threat Handbook: Web Applications v1.3

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF `automated-threat-handbook-EN-1v30(1).pdf`; uploaded prior extraction draft `owasp-automated-threat-handbook-v1v3.md`; current governance and evidence-review files available in conversation.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.
- **Relationship to OWASP project-page entry**: separate source. The project page is the high-level taxonomy landing page; this handbook is the fuller definitions/countermeasures/source text.

## Bibliographic

- **Citation**: Watson, C., & Zaw, T. (2026). *OWASP Automated Threat Handbook: Web Applications*. Version 1.3. OWASP Foundation. Published 17 March 2026. ISBN 978-1-291-76891-6.
- **Source URL or path**: uploaded PDF `automated-threat-handbook-EN-1v30(1).pdf`; canonical project page: `https://owasp.org/www-project-automated-threats-to-web-applications/`; source/PDF materials in OWASP project repository.
- **Date accessed**: 2026-06-06
- **Licence**: Creative Commons Attribution-ShareAlike 3.0.
- **Category**: foundations
- **Evidence basis**: taxonomy / ontology / countermeasure-reference
- **Operational proximity**: foundational — detailed vocabulary, definitions, symptoms, and countermeasure classes; not empirical prevalence or detection-performance evidence.
- **Tags**: OWASP, automated-threats, OAT, automated-threat-handbook, taxonomy, ontology, countermeasures, abuse-of-functionality, business-logic-abuse, credential-stuffing, scraping, scalping, sniping, denial-of-inventory, account-creation, captcha-defeat, carding, card-cracking, token-cracking, cost-inflation-fraud, application-security

## What it claims

- The handbook provides actionable information to help defend against automated threats to web applications.
- Its core framework is **21 unique, unordered OWASP Automated Threats (OATs)**.
- The framework describes abuse of **valid web application functionality**, not primarily exploitation of individual implementation bugs.
- The ontology is intended to answer the operational defender question: **“what is happening right now?”**
- The project provides a vendor-neutral, technology-agnostic vocabulary for developers, architects, operators, business owners, security engineers, purchasers, and vendors.
- The OAT categories are based on attacker intent rather than outcome. The same observed method can map to different OATs depending on purpose.
- Version 1.3 renames OAT-003 from **Ad Fraud** to **Cost-Inflation Fraud**, broadening it beyond advertising to messaging services, metered APIs, and AI/RAG-mediated traffic where the underlying pattern is falsified billable interactions.
- The handbook adds, updates, and cross-references threat definitions with CAPEC v3.9, CWE v4.18, WASC Threat Classification, and OWASP attack categories.
- It also provides 14 vendor-agnostic countermeasure classes mapped to builder/defender roles and prevent/detect/recover purposes.

## What evidence it provides

The handbook is best treated as a **consensus/expert-derived taxonomy and reference**, not as a measurement paper.

It provides:

- detailed definitions of all 21 OAT categories;
- sector, party, and data-impact framing for each threat event;
- possible symptoms for each threat event;
- suggested threat-specific countermeasures;
- 14 general countermeasure classes;
- cross-references to CAPEC, CWE, WASC, and OWASP attack-category pages;
- use-case scenarios for requirements, threat sharing, CERT exchange, penetration testing, procurement, and vendor-service characterisation;
- methodological provenance: the original work began in January 2015, used 150+ identified sources, extracted 600+ data points, clustered and de-duplicated those into the original OAT set, and then updated the ontology in later versions.

It does **not** provide:

- prevalence/base-rate data;
- production telemetry;
- attack-volume statistics;
- detection-model performance;
- false-positive/false-negative rates;
- controlled experiments;
- benchmark datasets;
- evidence that any listed countermeasure is effective in current adversarial conditions.

## OAT threat events covered

| OAT id | Name | Defining characteristic |
|---|---|---|
| OAT-001 | Carding | Multiple payment authorisation attempts to verify bulk stolen payment-card data. |
| OAT-002 | Token Cracking | Mass enumeration of coupon numbers, voucher codes, discount tokens, or similar values. |
| OAT-003 | Cost-Inflation Fraud | Mass use of functionality to illegitimately profit from chargeable supporting services. |
| OAT-004 | Fingerprinting | Elicit information about supporting software/framework types and versions. |
| OAT-005 | Scalping | Obtain limited-availability or preferred goods/services by unfair methods. |
| OAT-006 | Expediting | Perform actions to hasten normally slow, tedious, or time-consuming actions. |
| OAT-007 | Credential Cracking | Identify valid login credentials by trying username/password values. |
| OAT-008 | Credential Stuffing | Mass login attempts used to verify stolen username/password pairs. |
| OAT-009 | CAPTCHA Defeat | Solve anti-automation tests. |
| OAT-010 | Card Cracking | Identify missing start/expiry dates and security codes for stolen payment-card data. |
| OAT-011 | Scraping | Collect application content or other data for use elsewhere. |
| OAT-012 | Cashing Out | Buy goods or obtain cash using validated stolen payment-card or account data. |
| OAT-013 | Sniping | Last-minute bid or offer for goods or services. |
| OAT-014 | Vulnerability Scanning | Crawl and fuzz an application to identify weaknesses and possible vulnerabilities. |
| OAT-015 | Denial of Service | Target resources or accounts to reduce application availability. |
| OAT-016 | Skewing | Repeated clicks, page requests, or submissions intended to alter a metric. |
| OAT-017 | Spamming | Add malicious or questionable information to public/private content or messages. |
| OAT-018 | Footprinting | Probe and explore an application to identify constituents and properties. |
| OAT-019 | Account Creation | Create multiple accounts for later misuse. |
| OAT-020 | Account Aggregation | Intermediary collects multiple accounts together and interacts on their behalf. |
| OAT-021 | Denial of Inventory | Deplete goods/services stock without completing purchase or transaction commitment. |

## Countermeasure classes

The handbook’s countermeasures are vendor-agnostic classes rather than product recommendations.

| Class | Main idea |
|---|---|
| Value | Reduce the value of assets/functionality that can be abused. |
| Requirements | Identify automated threats during risk assessment and define design/deployment requirements. |
| Testing | Create abuse and misuse test cases simulating automated attacks. |
| Capacity | Build capacity so permitted and unwanted automation does not degrade normal use. |
| Obfuscation | Make automated mapping harder through dynamic URLs, fields, tokens, headers, or reduced information leakage. |
| Fingerprinting | Use user-agent, HTTP request format/header ordering, header anomalies, or device fingerprint content to judge whether traffic is likely human. |
| Reputation | Use identity, IP/range/geolocation/VPN, behaviour, resource-access, and third-party reputation signals. |
| Authentication | Require authentication, re-authentication, stronger identity checks, behavioural biometrics, puzzles/CAPTCHAs, out-of-band verification, or stronger authentication. |
| Rate | Set usage limits and thresholds per user, group, IP, range, device, fingerprint, event, or transaction. |
| Monitoring | Monitor anomalies, errors, sequencing, usage patterns, and user-generated content. |
| Instrumentation | Build observability and automated response into the application itself. |
| Contract | Use terms, contracts, and acceptable-use rules to prohibit unwanted automation. |
| Response | Define incident response actions for detected automated threats. |
| Sharing | Participate in threat-intelligence sharing. |

## Signals or techniques mentioned

The handbook sits mainly at **symptom/countermeasure-class level**, not detailed detection-engine level.

Useful signals and technique families include:

- User-Agent string;
- HTTP request format;
- HTTP header ordering;
- HTTP protocol/header anomalies;
- device/browser fingerprint content;
- IP address/range/geolocation/VPN-related reputation;
- user identity/session/fingerprint reputation;
- previous site and entry point;
- time of day;
- request rate;
- new-session generation rate;
- navigation paths through the application;
- static vs dynamic resource access;
- access to hidden/invisible links;
- `robots.txt` and paths excluded in `robots.txt`;
- honeytrap resources;
- cache-defined resources;
- JavaScript-generated links not accessed;
- repeated access patterns;
- failed-login rates;
- account-lock rates;
- basket abandonment;
- reduced use of payment steps;
- chargebacks;
- GET/POST/HEAD ratios;
- 404/503 clustering;
- faster-than-average multi-step progression;
- suspicious user-generated-content patterns.

Important absences:

- no named ML model families;
- no detailed TLS fingerprinting such as JA3/JA4;
- no HTTP/2 fingerprinting detail;
- no mouse-trajectory/click-cadence details;
- no current cloud-browser, anti-detect-browser, or residential-proxy ecosystem analysis;
- no AI-agent/browser-agent detection method.

## What is strong

- Strongest canonical source for the OAT vocabulary.
- Strongest source for the “abuse of valid functionality” framing.
- More useful than the OWASP project page when detailed definitions, symptoms, and countermeasure classes are needed.
- Good reference for mapping other sources into consistent threat categories.
- Useful for explaining that automated-abuse categories are intent-based and may not be cleanly separable from raw traffic logs.
- Useful for practical stakeholder communication: engineering, security, procurement, threat sharing, and vendor comparison.
- Its 2026 update is useful because OAT-003 now explicitly recognises metered API and AI/RAG-driven cost-inflation patterns.

## What is weak or limited

- It is not empirical evidence.
- It does not quantify how common any OAT is.
- It does not rank the OATs by harm, likelihood, business impact, or current prevalence.
- It does not evaluate countermeasure effectiveness.
- It does not give operational detection thresholds or detection model designs.
- It is mostly one abstraction level above the modern detection details found in Cloudflare/HUMAN/DataDome-style sources and academic bot-detection papers.
- Its AI references in v1.3 are taxonomic acknowledgements, not a measured account of AI-agent traffic.
- Because the categories are intent-based, the same observed behaviour may need additional context before it can be assigned confidently to one OAT.
- Sector targeting in the handbook is partly judgement-based and the handbook itself seeks better prevalence and sector-specific evidence.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  The defender’s naming and classification layer for automated web-application abuse. It is about how to describe what kind of automated misuse is happening, and what broad classes of controls might be considered.

- **What does it fail to represent?**  
  It does not represent current production detection practice, live adversarial adaptation, telemetry-backed prevalence, or modern attacker tooling. It does not show how to separate humans from bots with measured accuracy.

- **What additional evidence would be needed to go further?**  
  Current vendor telemetry, academic detection studies, legal/enforcement records, scraper-side capability sources, cloud-browser/anti-detect/proxy ecosystem sources, controlled detection evaluations, and real case studies.

## What it cannot show

- It cannot show that any OAT category is currently common.
- It cannot show that the OAT taxonomy is complete for 2026 automation practice.
- It cannot show which threats cause the most loss.
- It cannot show which controls work best.
- It cannot show detection precision/recall.
- It cannot show false-positive or user-friction trade-offs.
- It cannot show whether a particular deployment is privacy-compliant or legally sufficient.
- It cannot prove that AI agents are materially changing abuse patterns; it only recognises AI/RAG-driven traffic as relevant to the taxonomy.

## Project impact

Use this as the **canonical taxonomy backbone** for openbotrisk.

Best uses:

- define and map OAT categories;
- separate automated abuse of valid functionality from conventional vulnerability exploitation;
- support the project’s “methods before actors” framing;
- provide common language for credential stuffing, scraping, scalping, sniping, account creation, CAPTCHA defeat, denial of inventory, cost-inflation fraud, and related categories;
- structure pages that compare old automated-threat vocabulary with current browser automation, managed scraping APIs, residential proxies, anti-detect browsers, AI crawlers, and browser agents;
- provide a countermeasure-class scaffold for explaining defensive options without endorsing any vendor.

Do not use it as:

- prevalence evidence;
- evidence of observed abuse;
- evidence of current attacker capability;
- proof that a control works;
- proof that OWASP categories fully cover AI-agent/browser-agent abuse;
- a detection-architecture reference.

## Relationship to other register entries

- **OWASP project-page entry**: shorter landing-page taxonomy source. Use for high-level vocabulary.
- **This handbook entry**: detailed definitions, symptoms, countermeasure classes, scope rules, and roadmap.
- **Vendor telemetry sources**: use for observed operational trends and prevalence, but caveat as vendor-measured.
- **Academic detection papers/reviews**: use for detection-method taxonomy, model types, privacy trade-offs, and measured studies.
- **Scraper-side capability sources**: use for public capability and evasion knowledge, with dual-use containment.
- **Berke/Laperdrix browser-fingerprinting sources**: use for fingerprinting foundations and privacy risk of browser/device signals.

## Dual-use containment

This source is low-to-moderate dual-use. It provides category names, symptoms, and broad countermeasure classes, not working bypass instructions. The main risk is aggregation: combining OWASP symptoms/countermeasures with scraper-side evasion material could create a more operational playbook than any single source.

Use it at the level of:

- definitions;
- classification;
- countermeasure families;
- framing limits;
- source mapping.

Avoid using it to assemble step-by-step detection evasion or attack workflows.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `owasp-automated-threat-handbook-v1-3` |
| Title | *OWASP Automated Threat Handbook: Web Applications*, Version 1.3 |
| Organisation / authors | Colin Watson and Tin Zaw / OWASP Foundation |
| Year | 2026 |
| Category | foundations |
| Evidence basis | taxonomy / ontology / countermeasure-reference |
| Operational proximity | foundational |
| Signals / techniques | OAT categories; symptoms; countermeasure classes; fingerprinting/reputation/rate/monitoring/instrumentation signals |
| Threat types | all 21 OWASP Automated Threat categories |
| Project use | Canonical detailed OAT taxonomy and countermeasure-class reference |
| Main caution | Not prevalence, observed-use, detection-performance, or current tooling evidence |
| Entry file | `owasp-automated-threat-handbook-v1-3.md` |
