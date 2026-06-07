# OWASP Automated Threats to Web Applications

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: official OWASP project page checked live; prior local register entry and current governance file reviewed.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.

## Bibliographic

- **Citation**: OWASP Foundation. (n.d.). *OWASP Automated Threats to Web Applications*. OWASP. Accessed 2026-06-06. https://owasp.org/www-project-automated-threats-to-web-applications/
- **Source URL or path**: `https://owasp.org/www-project-automated-threats-to-web-applications/`
- **Date accessed**: 2026-06-06
- **Organisation**: OWASP Foundation
- **Category**: foundations
- **Evidence basis**: taxonomy / ontology / reference classification
- **Operational proximity**: foundational — vocabulary and classification source, not observed-use evidence and not detection-performance evidence.
- **Tags**: OWASP, automated-threats, OAT, taxonomy, ontology, abuse-of-functionality, business-logic-abuse, credential-stuffing, scraping, scalping, sniping, denial-of-inventory, account-creation, captcha-defeat, carding, card-cracking, token-cracking, application-security

## What it claims

- Automated threats to web applications are threat events carried out using automated actions.
- The project focuses on unwanted automated use of web application functionality, especially misuse of inherent valid functionality and related design/business-logic flaws.
- The project explicitly excludes tool-based exploitation of single-issue vulnerabilities from its main scope.
- OWASP argues that many common automated-abuse problems are not well covered by the OWASP Top Ten or other conventional issue lists, which creates poor visibility and inconsistent naming.
- The project’s purpose is to provide a vendor-neutral, technology-agnostic ontology and common language for developers, architects, operators, business owners, security engineers, purchasers, and suppliers/vendors.
- The project also identifies symptoms, mitigations, and controls in the broader problem area, with the fuller definitions located in the OWASP Automated Threat Handbook.
- The project page positions the OAT terms as useful for security requirements, threat intelligence sharing, CERT exchange, penetration-test reporting, procurement, and vendor capability description.

## What evidence it provides

- A vendor-neutral classification framework for automated misuse of web applications.
- A named OAT identifier set covering common automated threat events.
- Summary descriptions for each OAT event on the project page.
- Use-case scenarios showing how the taxonomy can support:
  - application security requirements;
  - sector intelligence sharing;
  - CERT-to-CERT threat-data exchange;
  - penetration-test reporting;
  - procurement / service acquisition;
  - vendor service characterisation.
- A bibliography of academic, open-source, commercial, and news sources used in the OWASP research process.
- Cross-comparison against older taxonomies and lists such as CAPEC, WASC Threat Classification, and the OWASP WASC Web Hacking Incidents Database.

## What it does not provide

- No original empirical measurement.
- No production telemetry.
- No prevalence estimates.
- No current attack-volume numbers.
- No detection accuracy, false-positive, or false-negative metrics.
- No modern operational detail on current anti-detect browsers, cloud browser services, residential proxy markets, AI browser agents, or LLM-driven browser automation.
- No working detection architecture.
- No evidence that any particular mitigation remains effective against current automation.

## OAT threat events covered

| OAT id | Name | Project-page summary |
|---|---|---|
| OAT-020 | Account Aggregation | Intermediary application collects and interacts with multiple accounts on their behalf. |
| OAT-019 | Account Creation | Create multiple accounts for later misuse. |
| OAT-003 | Cost-Inflation Fraud | Mass use of functionality to profit from chargeable supporting services. |
| OAT-009 | CAPTCHA Defeat | Solve anti-automation tests. |
| OAT-010 | Card Cracking | Identify missing start/expiry dates and security codes for stolen payment card data. |
| OAT-001 | Carding | Multiple payment authorisation attempts to verify bulk stolen payment-card data. |
| OAT-012 | Cashing Out | Buy goods or obtain cash using validated stolen payment-card or account data. |
| OAT-007 | Credential Cracking | Identify valid login credentials by trying username/password values. |
| OAT-008 | Credential Stuffing | Mass login attempts to verify stolen username/password pairs. |
| OAT-021 | Denial of Inventory | Deplete stock or service availability without completing purchase/commitment. |
| OAT-015 | Denial of Service | Target application/database/user-account resources to reduce availability. |
| OAT-006 | Expediting | Perform actions to hasten usually slow, tedious, or time-consuming actions. |
| OAT-004 | Fingerprinting | Elicit information about supporting software/framework types and versions. |
| OAT-018 | Footprinting | Probe/explore an application to identify constituents and properties. |
| OAT-005 | Scalping | Obtain limited-availability or preferred goods/services by unfair methods. |
| OAT-011 | Scraping | Collect application content or other data for use elsewhere. |
| OAT-016 | Skewing | Repeated clicks, page requests, or submissions intended to alter a metric. |
| OAT-013 | Sniping | Last-minute bid or offer for goods or services. |
| OAT-017 | Spamming | Add malicious or questionable information to public/private content or messages. |
| OAT-002 | Token Cracking | Mass enumeration of coupon numbers, voucher codes, discount tokens, etc. |
| OAT-014 | Vulnerability Scanning | Crawl and fuzz an application to identify weaknesses and possible vulnerabilities. |

## Signals or techniques mentioned

The project page is mostly a taxonomy source, so it does not give a technical detection-signal list in the way Cloudflare, HUMAN, DataDome, or academic bot-detection papers do. The relevant signals/technique families are category-level:

- automated account creation;
- credential stuffing;
- credential cracking;
- carding and card cracking;
- token cracking;
- scraping;
- scalping;
- sniping;
- expediting repetitive actions;
- CAPTCHA defeat;
- denial of inventory;
- skewing metrics;
- spamming;
- vulnerability scanning;
- footprinting and fingerprinting;
- automated abuse of valid application functionality;
- use of OAT identifiers in requirements, threat sharing, monitoring, procurement, and reporting.

## Threat types covered

- All 21 OWASP Automated Threat event categories.
- Particularly relevant to openbotrisk:
  - OAT-008 Credential Stuffing;
  - OAT-011 Scraping;
  - OAT-005 Scalping;
  - OAT-013 Sniping;
  - OAT-021 Denial of Inventory;
  - OAT-019 Account Creation;
  - OAT-009 CAPTCHA Defeat;
  - OAT-004 Fingerprinting;
  - OAT-018 Footprinting;
  - OAT-016 Skewing;
  - OAT-006 Expediting.

## What is strong

- Strong anchor source for vocabulary.
- Strong source for the “automated abuse of valid functionality” framing.
- Useful because it is vendor-neutral and not trying to sell a product.
- Useful for avoiding private taxonomy drift: the project can map sources onto OWASP categories before inventing additional project-specific categories.
- Useful for explaining why “bot problem” is not one problem: credential stuffing, scraping, scalping, sniping, inventory denial, metric skewing, and account creation are different events with different motives and controls.
- Useful for procurement and communication framing: it gives shared names that business, security, engineering, and vendor teams can use.

## What is weak or limited

- It is a taxonomy/ontology source, not a measurement source.
- It is dated relative to newer operational territory:
  - browser-native automation frameworks;
  - anti-detect browsers;
  - residential proxy markets;
  - cloud browser services;
  - managed scraping APIs;
  - AI crawlers;
  - agentic browser automation;
  - LLM-assisted workflow automation.
- It does not describe modern detection layers such as TLS fingerprints, HTTP/2 fingerprinting, browser fingerprint coherence checks, behavioural biometrics, bot scores, ML scoring, JavaScript detections, or per-endpoint risk policies.
- The project page gives only summary descriptions; the full OWASP Automated Threat Handbook is needed for fuller symptoms, controls, and mitigations.
- The page can make the field look more settled than it is. OWASP gives names, not proof that the named categories are complete or equally important today.
- Some modern cases cut across OAT categories. For example, appointment-slot abuse may involve expediting, sniping, denial of inventory, account creation, credential/account misuse, and resale-market incentives.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  The classification problem faced by web-application owners, security teams, vendors, and researchers when they need to name different forms of automated misuse. It approximates the vocabulary layer of the field rather than the operational detection layer.

- **What does it fail to represent?**  
  It does not represent production detection practice, live adversarial adaptation, telemetry-backed prevalence, or modern tool ecosystems. It does not show how to distinguish bots from humans, what data to collect, how controls perform, or how attackers adapt to controls.

- **What additional evidence would be needed to go further?**  
  Current vendor documentation and telemetry; academic bot-detection studies; legal/enforcement records; scraper-side capability sources; cloud browser / anti-detect / proxy ecosystem sources; and case studies showing operational abuse against real sites.

## What it cannot show

- It cannot show that any OAT category is common today.
- It cannot show that the taxonomy is complete for current automated-abuse practice.
- It cannot show which automated threats cause the most harm.
- It cannot show which controls work.
- It cannot show modern bypass capability.
- It cannot show false-positive/user-friction trade-offs.
- It cannot show compliance with privacy, consumer-protection, or sector-specific rules.
- It should not be cited as prevalence evidence unless paired with a separate empirical source.

## Project impact

Use this as the **threat-type spine** for openbotrisk.

Best uses:

- map sources to common OAT categories;
- explain the difference between automated misuse and ordinary vulnerability exploitation;
- provide a neutral vocabulary before discussing vendor-specific claims;
- structure pages on credential stuffing, scraping, scalping, sniping, denial of inventory, account creation, and CAPTCHA defeat;
- compare older automated-threat vocabulary with newer automation modes such as browser automation, cloud browsers, anti-detect browsers, and AI agents.

Do not use it as:

- evidence that a threat is common;
- proof of modern attacker capability;
- evidence that a defence works;
- evidence about current AI-agent or cloud-browser trends;
- a substitute for the full OWASP Automated Threat Handbook.

## How this updates the previous entry

The previous local entry already had the core treatment right: OWASP should be used as a taxonomy spine, not prevalence or detection evidence. This update tightens it under the newer prompt structure by adding:

- explicit extraction metadata;
- evidence basis and operational proximity;
- a full OAT table;
- stronger “what it cannot show” limits;
- clearer modern-coverage limitations;
- explicit project-use and non-use guidance;
- a sharper distinction between the project page and the full Handbook.

## Relationship to the full OWASP Automated Threat Handbook

This entry is for the **OWASP project page**. The full Automated Threat Handbook should remain a separate source if the project needs detailed symptoms, controls, and mitigations.

Suggested handling:

- `owasp-automated-threats-to-web-applications` = project-page taxonomy spine.
- `owasp-automated-threat-handbook-v1-3` = full handbook definitions, symptoms, mitigations, and controls.

## Dual-use containment

This source is low dual-use by itself because it provides category names and summaries, not bypass instructions. The main risk is synthesis: combining OWASP categories with scraper-side bypass guides could accidentally create operational playbooks. For this source, keep use at the vocabulary and classification level.

## Possible register row

| Field | Value |
|---|---|
| Register id | `owasp-automated-threats-to-web-applications` |
| Title | *OWASP Automated Threats to Web Applications* |
| Organisation / authors | OWASP Foundation |
| Year | n.d.; accessed 2026-06-06 |
| Category | foundations |
| Evidence basis | taxonomy / ontology / reference classification |
| Operational proximity | foundational |
| Signals / techniques | OAT category set; abuse-of-functionality framing; automated misuse categories |
| Threat types | all 21 OAT categories |
| Project use | Threat-type spine and vendor-neutral vocabulary for automated web-application misuse |
| Main caution | Taxonomy source only; not prevalence, observed abuse, current tooling, or detection-effectiveness evidence |
| Entry file | `owasp-automated-threats-to-web-applications.md` |
