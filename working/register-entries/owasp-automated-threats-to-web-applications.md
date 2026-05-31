# OWASP Automated Threats to Web Applications

## Bibliographic

- **Citation**: OWASP Foundation. (n.d.). *OWASP Automated Threats to Web Applications*. OWASP. Accessed 2026-05-31. https://owasp.org/www-project-automated-threats-to-web-applications/
- **Source URL or path**: https://owasp.org/www-project-automated-threats-to-web-applications/
- **Date accessed**: 2026-05-31
- **Category**: foundations
- **Tags**: taxonomy, threat-surface, oat, abuse-of-functionality, automated-threats, credential-stuffing, scraping, scalping, account-takeover

## What it claims

- Automated threats to web applications are a distinct problem area: unwanted software-driven use of web application functionality that diverges from accepted behaviour and produces undesirable effects.
- Many regular automated-abuse problems are not well covered by the OWASP Top Ten or other conventional web application issue lists, which has led to weak visibility and inconsistent naming.
- The project’s purpose is to provide a vendor-neutral, technology-agnostic ontology and common language for developers, architects, operators, business owners, security engineers, purchasers, and suppliers/vendors.
- The project focuses mainly on abuse of inherent valid functionality and related design or business-logic flaws, rather than implementation bugs or single-issue vulnerabilities.
- Automated misuse is often misreported as application-layer denial of service, even when denial of service is a side-effect rather than the main attacker objective.
- The OWASP Automated Threat Handbook defines a set of named automated threat events, including carding, credential stuffing, scraping, scalping, denial of inventory, spamming, vulnerability scanning, token cracking, and related categories.
- The ontology can be used for security requirements, sector intelligence sharing, CERT data exchange, penetration-test reporting, service procurement, and vendor capability description.

## What evidence it provides

- The project page says the taxonomy was produced from a review of reports, academic and other papers, news stories, and vulnerability taxonomies/listings.
- The page provides a bibliography of academic, open-source, commercial, and news sources used in the project’s research.
- The use-case section provides fictitious scenarios showing how the taxonomy could be used in requirements, intelligence sharing, CERT exchange, pentest reporting, procurement, and vendor positioning.
- The page provides definitions and a glossary drawing on external taxonomies and standards-like references, including The Open Group risk taxonomy, NISTIR 7298, OSI/TCP-IP model references, and W3C web definitions.
- It does not provide new empirical measurements, datasets, detection accuracy results, production telemetry, prevalence estimates, or controlled experiments.

## Signals or techniques mentioned

- Threat-event classification using OAT identifiers.
- Abuse-of-functionality framing rather than vulnerability-only framing.
- Automated account creation.
- CAPTCHA defeat.
- Carding and card cracking.
- Credential cracking and credential stuffing.
- Denial of inventory.
- Expediting repetitive actions.
- Fingerprinting and footprinting.
- Scalping, scraping, sniping, skewing, spamming, token cracking, vulnerability scanning.
- Use of threat identifiers for requirements, intelligence sharing, monitoring dashboards, penetration-test reporting, procurement, and vendor service descriptions.
- No detailed detection signals are described on the project page itself: no TLS fingerprinting, browser fingerprint fields, mouse dynamics, header-order features, proxy indicators, model classes, or operational detection architecture.

## Threat types covered

- OAT-001 Carding
- OAT-002 Token Cracking
- OAT-003 Cost-Inflation Fraud
- OAT-004 Fingerprinting
- OAT-005 Scalping
- OAT-006 Expediting
- OAT-007 Credential Cracking
- OAT-008 Credential Stuffing
- OAT-009 CAPTCHA Defeat
- OAT-010 Card Cracking
- OAT-011 Scraping
- OAT-012 Cashing Out
- OAT-013 Sniping
- OAT-014 Vulnerability Scanning
- OAT-015 Denial of Service
- OAT-016 Skewing
- OAT-017 Spamming
- OAT-018 Footprinting
- OAT-019 Account Creation
- OAT-020 Account Aggregation
- OAT-021 Denial of Inventory

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** It approximates the classification problem faced by web application owners, security teams, vendors, and buyers when they need to name and separate different forms of automated misuse. For openbotrisk, it also approximates the baseline vocabulary problem: how to organise a broad territory without inventing a private taxonomy too early. It is useful for distinguishing business-logic abuse such as credential stuffing, scraping, scalping, account creation, and denial of inventory from generic vulnerability exploitation or generic “bot traffic”.
- **What does it fail to represent?** It is not a detection study and does not represent production bot-management practice directly. It does not show how to separate bots from humans, how well controls work, which signals are reliable, or how attacks evolve under adversarial pressure. The taxonomy is also dated relative to newer operational territory such as cloud browser services, anti-detect browsers, residential proxy markets, browser automation frameworks, mobile-app automation, and AI browser agents. It is intentionally vendor-neutral, which is useful for vocabulary but means it omits proprietary telemetry and implementation detail.
- **What additional evidence would be needed to go further?** The project would need current vendor documentation and threat reports, academic detection studies, production case studies, telemetry-backed prevalence estimates, examples from browser automation and anti-detect ecosystems, and evidence on how modern bot operators adapt to controls.

## What it cannot show

- It cannot show that the OAT taxonomy is complete for current automated-abuse practice.
- It cannot show which automated threat types are most prevalent or damaging today.
- It cannot show whether any specific detection method works.
- It cannot show whether named controls or mitigations remain effective against modern stealth automation, cloud browsers, residential proxies, or AI-assisted browser agents.
- It cannot show operational trade-offs such as false positives, user friction, latency, cost, maintainability, or evasion resistance.
- It should not be cited as empirical evidence that a particular category is common, only as a vocabulary and classification source unless supported by additional evidence.

## Project impact

- Acts as one of the project’s anchor sources: the baseline OAT vocabulary that later sources are mapped against.
- Provides the spine for the project’s threat taxonomy and abuse-category vocabulary, especially for credential stuffing, scraping, scalping, denial of inventory, account creation, CAPTCHA defeat, and related categories.
- Supports using “automated abuse of valid functionality” as a core framing, rather than treating all bot problems as vulnerability exploitation or denial of service.
- Useful as an organising reference for the evidence register, especially the “Threat types covered” field.
- The project should not reproduce OWASP at lower quality; each synthesis page needs to clarify what it adds beyond the relevant OAT category, a single vendor blog, or one academic paper.
- Best used as the register’s threat-type spine, not as evidence for prevalence, detection effectiveness, or modern tooling coverage.
- Should be caveated heavily in any synthesis: it is a taxonomy/ontology source, not a source of current detection evidence, operational performance claims, or modern tooling coverage.
- The full OWASP Automated Threat Handbook should be considered a separate follow-up source if the project needs the detailed definitions, symptoms, mitigations, and controls rather than the project-page summary.
