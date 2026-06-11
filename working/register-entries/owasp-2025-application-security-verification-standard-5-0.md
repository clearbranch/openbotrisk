# OWASP Application Security Verification Standard 5.0.0

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF `SRC-093-owasp-2025-application-security-verification-standard-5-0.pdf`; current evidence register reviewed for project context.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.

## Bibliographic

- **Citation**: OWASP Foundation. (2025). *Application Security Verification Standard*. Version 5.0.0. May 2025.
- **Source URL or path**: uploaded PDF `SRC-093-owasp-2025-application-security-verification-standard-5-0.pdf`; canonical project source should be checked against OWASP ASVS project/repository before final publication.
- **Date accessed / captured**: uploaded 2026-06-07.
- **Licence**: Creative Commons Attribution-ShareAlike 4.0 International.
- **Category**: foundations
- **Evidence basis**: standards-reference / control-requirements / defensive-guidance
- **Operational proximity**: control — a normative verification standard for application security controls; not observed abuse, not telemetry, and not control-effectiveness evidence.
- **Tags**: OWASP, ASVS, application-security, verification-standard, anti-automation, business-logic-security, rate-limiting, session-management, session-abuse, authentication, authorization, API-security, HTTP-message-validation, logging, secure-design, standards

## What it claims

- ASVS defines application security requirements for web applications and services.
- Version 5.0.0 is a major revision intended to align more closely with the terms Application, Security, Verification, and Standard.
- Requirements are framed around security goals rather than mandating specific implementations.
- ASVS 5.0.0 introduces stronger emphasis on documented security decisions.
- ASVS retains three levels:
  - Level 1: initial / first layer of defence;
  - Level 2: comprehensive standard security practice;
  - Level 3: advanced / high assurance.
- ASVS 5.0.0 contains approximately 350 requirements across 17 chapters.
- ASVS is intended for secure design, development, testing, procurement, training, and verification.
- ASVS is explicitly not a substitute for detailed implementation guidance or a testing guide; it points to OWASP Cheat Sheets and the Web Security Testing Guide for those roles.

## What evidence it provides

This is a **requirements/control standard**, not a measurement source.

It provides:

- a structured set of web-application security requirements;
- levels for selecting control depth;
- control objectives and requirement identifiers;
- requirements relevant to anti-automation, business logic, authentication, session management, authorization, API/message validation, logging, and data protection;
- a way to translate general bot/abuse concerns into verifiable application requirements.

It does **not** provide:

- empirical evidence of bot abuse;
- prevalence estimates;
- attack-volume statistics;
- production telemetry;
- detection accuracy or false-positive/false-negative rates;
- evidence that any specific anti-automation control works against modern adversaries;
- vendor/product comparison;
- bot-management architecture.

## Sections most relevant to openbotrisk

### V2 Validation and Business Logic

This is the most directly relevant section for automated misuse of valid functionality.

Relevant requirements include:

- business-logic locking for limited resources such as theatre seats or delivery slots, preventing double booking or manipulation of allocation logic;
- anti-automation controls to protect against excessive function calls that could cause data exfiltration, garbage-data creation, quota exhaustion, rate-limit breaches, denial of service, or costly resource overuse;
- realistic human timing for business logic flows to prevent excessively rapid transaction submissions.

**Project use:** strong support for the idea that automated abuse is not only a perimeter/vendor issue. Some controls need to be built into the application’s own business logic.

### V6 Authentication

Relevant to credential stuffing, credential cracking, account takeover, and automated login abuse.

Useful ASVS contribution:

- authentication requirements give the application-security baseline;
- ASVS provides a control framework that can be paired with PortSwigger and OWASP OAT credential-stuffing material;
- it is more normative than PortSwigger tutorials but less threat-specific than the OWASP Automated Threat Handbook.

### V7 Session Management

Relevant to cookie/session reuse, session hijacking, authenticated automation, and account-abuse flows.

Useful requirements include:

- backend verification of session tokens;
- dynamic generation of session tokens;
- generation of a new token on authentication/re-authentication;
- inactivity and absolute session timeouts based on risk analysis and documented security decisions;
- termination of sessions on logout/expiration, account disablement/deletion, and authentication-factor changes;
- user ability to view and terminate active sessions;
- further authentication before highly sensitive transactions or operations.

**Project use:** useful counterpart to sources showing browser automation can preserve cookies/session state. ASVS describes what a defensive application should require from sessions and sensitive operations.

### V8 Authorization

Relevant to account aggregation, API misuse, intermediaries, delegated access, and agentic/automated use acting on behalf of a user.

Useful requirements include:

- trusted-service-layer authorization rather than client-side JavaScript controls;
- contextual/adaptive controls based on attributes such as time of day, location, IP address, or device;
- access decisions based on the originating subject’s permissions rather than an intermediary/service acting on their behalf.

**Project use:** useful for the “automation acting through a real account is still constrained by authorization design” point.

### V4 API and Web Service / HTTP Message Structure Validation

Relevant to API abuse, request manipulation, and HTTP-level robustness.

Useful requirements include:

- validating HTTP message structure;
- preventing request smuggling, response splitting, header injection, and denial of service through overly long HTTP messages;
- ensuring load balancers, firewalls, and application servers interpret message boundaries correctly.

**Project use:** useful as defensive baseline, but not directly a bot-detection source.

### V16 Security Logging and Error Handling

Relevant to monitoring and evidence generation.

The register should treat ASVS logging requirements as a bridge between control design and later operational detection. However, ASVS does not provide a bot-specific logging schema or detection model.

### V14 Data Protection

Relevant to scraping, bulk extraction, and sensitive-data protection.

ASVS notes that abnormal bulk extraction/modification/excessive use depends on threat model and business risk, with detection handled under logging and limits handled under validation/business logic.

**Project use:** useful for explaining why “scraping risk” cannot be solved by one generic rule; the application must decide what data matters and what abnormal use means.

## Signals or techniques mentioned

- anti-automation controls;
- realistic human timing;
- rate limits and excessive-call prevention;
- business-logic locking;
- limited-resource protection;
- authentication controls;
- MFA / additional verification;
- session token verification;
- session timeout;
- session termination;
- active-session review/termination;
- re-authentication before sensitive operations;
- contextual/adaptive security controls using time, location, IP address, or device;
- trusted-service-layer authorization;
- HTTP method restriction;
- HTTP message structure validation;
- request smuggling prevention;
- header injection prevention;
- security logging;
- data classification and protection levels.

## Threat types covered

ASVS is not organised around OWASP Automated Threat categories, but it is relevant to several:

- OAT-008 Credential Stuffing — through authentication, rate limiting, session, and logging controls.
- OAT-007 Credential Cracking — through authentication protections and brute-force-aware testing.
- OAT-019 Account Creation — through anti-automation, validation, and authentication controls.
- OAT-011 Scraping — through data protection, anti-automation, API controls, and logging.
- OAT-005 Scalping / OAT-013 Sniping — through limited-resource locking, transaction timing, and business-logic controls.
- OAT-021 Denial of Inventory — through business-logic locking and limited-resource protections.
- OAT-006 Expediting — through realistic human timing and anti-automation controls.
- OAT-015 Denial of Service — through excessive-call prevention and HTTP/message robustness.
- OAT-020 Account Aggregation — indirectly through session, authorization, and intermediary/delegation controls.

## What is strong

- Strong standards/reference source.
- Useful defensive counterpart to OWASP Automated Threat Handbook.
- Particularly useful for showing what must be built into an application rather than outsourced to a bot-management product.
- Strong for business-logic abuse:
  - limited resources;
  - transaction integrity;
  - realistic timing;
  - excessive function calls.
- Strong for session/account controls:
  - session invalidation;
  - active-session visibility;
  - re-authentication for sensitive changes;
  - session timeout and termination.
- Strong for explaining that bot defence overlaps with ordinary application security: authentication, authorization, session management, rate limiting, business logic, and logging.
- Useful for procurement/governance because ASVS gives named, verifiable requirements.

## What is weak or limited

- It is not a bot-detection paper.
- It is not threat telemetry.
- It does not measure whether controls work.
- It does not provide modern bot-management signals such as TLS fingerprints, browser fingerprints, behavioural biometrics, device reputation, risk scores, or ML models.
- It does not explain how attackers evade controls.
- It is not specific to browser-native automation, cloud browsers, residential proxies, anti-detect browsers, or AI agents.
- Its anti-automation section is short and high-level.
- It is a security requirements standard; it should not be stretched into a threat taxonomy or observed-use source.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  The secure-application control layer needed to make automated abuse harder: business logic, authentication, session, authorization, API, logging, and data-protection requirements.

- **What does it fail to represent?**  
  The adversarial detection layer. It does not represent production bot-management systems, modern evasion, attacker tooling, or prevalence. It also does not show whether any control remains effective against adaptive automation.

- **What additional evidence would be needed to go further?**  
  OWASP Automated Threat Handbook for threat categories; PortSwigger for vulnerability mechanics; Cloudflare/HUMAN/DataDome for vendor-side detection and operational framing; academic bot-detection studies for method evaluation; scraper-side sources for public evasion knowledge; legal/victim records for observed-use evidence.

## What it cannot show

- It cannot show that a specific automated threat is common.
- It cannot show that rate limiting or anti-automation controls stop modern bots.
- It cannot show how to detect browser-native automation.
- It cannot show how to distinguish humans from bots in production.
- It cannot show false-positive/user-friction trade-offs.
- It cannot show whether a WAF or bot-management vendor works.
- It cannot establish legal compliance by itself.
- It cannot replace OWASP OAT as the automated-threat taxonomy.

## Project impact

Use this as a **defensive-control foundation source**.

Best uses:

- explain that anti-automation is partly an application-design problem;
- support pages on business-logic abuse, limited-resource protection, and slot/inventory problems;
- provide defensive counterweight to scraper-side capability and bypass sources;
- bridge OWASP OAT categories to concrete application-security requirements;
- support the claim that bot defence spans application logic, sessions, auth, API, logging, and perimeter controls;
- provide a standards-backed basis for “what should be built in” before discussing vendor products.

Do not use it as:

- observed-use evidence;
- evidence that a bot threat is prevalent;
- proof of detection effectiveness;
- a modern bot-detection taxonomy;
- evidence about AI-agent or browser-native automation trends.

## Relationship to other register entries

- **OWASP Automated Threats project page**: ASVS is control requirements; OAT is taxonomy.
- **OWASP Automated Threat Handbook v1.3**: ASVS is broader application-security requirements; Handbook is automation-threat definitions and countermeasure classes.
- **PortSwigger authentication entries**: PortSwigger explains attack/vulnerability mechanics; ASVS gives verifiable requirements.
- **MDN foundations**: MDN explains HTTP/cookies/CORS/headers; ASVS states secure use requirements.
- **Cloudflare/HUMAN/DataDome**: vendors describe detection products and operational signals; ASVS describes application controls, not product performance.
- **Martínez Llamas et al.**: privacy/governance and detection taxonomy; ASVS gives technical requirements but not legal analysis.

## Dual-use containment

Low dual-use. ASVS is defensive and standards-oriented. The main risk is over-claiming: do not imply that following ASVS alone solves bot abuse or replaces modern bot-management/detection work.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `owasp-2025-application-security-verification-standard-5-0` |
| Title | *Application Security Verification Standard*, Version 5.0.0 |
| Organisation / authors | OWASP Foundation |
| Year | 2025 |
| Category | foundations |
| Evidence basis | standards-reference / control-requirements / defensive-guidance |
| Operational proximity | control |
| Signals / techniques | anti-automation; business logic; rate limiting; session management; authentication; authorization; HTTP validation; logging |
| Threat types | indirectly relevant to credential stuffing, scraping, scalping, sniping, account creation, denial of inventory, expediting, DoS |
| Project use | Defensive-control foundation connecting automated-abuse taxonomy to application-security requirements |
| Main caution | Not observed abuse, prevalence, detection-performance, or modern bot-management evidence |
| Entry file | `owasp-2025-application-security-verification-standard-5-0.md` |
