# NIST SP 800-63B-4 - Digital Identity Guidelines: Authentication and Authenticator Management

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF `SRC-073-nist-2025-sp-800-63b-4-authentication-authenticator-management.pdf`.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.

## Bibliographic

- **Citation**: Temoshok, D., Fenton, J. L., Choong, Y.-Y., Lefkovitz, N., Regenscheid, A., Galluzzo, R., & Richer, J. P. (2025). *Digital Identity Guidelines: Authentication and Authenticator Management*. NIST Special Publication 800-63B-4. National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-63B-4
- **Publication date**: July 2025.
- **Publication status**: Final NIST Special Publication; approved 2025-05-30.
- **Source URL or path**: uploaded PDF `SRC-073-nist-2025-sp-800-63b-4-authentication-authenticator-management.pdf`; DOI `10.6028/NIST.SP.800-63B-4`.
- **Category**: foundations
- **Evidence basis**: standards-reference / authentication-guidance / control-requirements
- **Operational proximity**: control — normative guidance for authentication, authenticator management, reauthentication, and session management. It is not bot-abuse telemetry, not detection-performance evidence, and not a vendor product source.
- **Tags**: NIST, SP800-63B, authentication, authenticator-management, AAL, MFA, phishing-resistance, passwords, credential-stuffing, rate-limiting, throttling, session-management, browser-cookies, session-secrets, account-recovery, fraud-indicators, privacy-risk, biometrics, risk-based-authentication

## What it claims

- SP 800-63B-4 provides requirements for remote user authentication at Authentication Assurance Levels (AALs) 1, 2, and 3.
- Authentication is based on proving possession/control of authenticators bound to a subscriber account.
- AAL1 provides basic confidence; AAL2 requires two distinct authentication factors; AAL3 requires phishing-resistant cryptographic authentication with non-exportable keys.
- AAL2 verifiers must offer at least one phishing-resistant authentication option; AAL3 requires phishing resistance.
- Passwords are not phishing-resistant.
- Browser cookies are not authenticators; they are only short-term secrets for session maintenance.
- Rate limiting/throttling is required for online guessing protection where applicable.
- Risk/fraud indicators such as IP address, geolocation, timing/request patterns, and browser metadata may be used, but they do not change the AAL or substitute for an authentication factor.
- Use of fraud indicators and session monitoring creates privacy obligations and should be assessed for efficacy and possible negative impacts on users.

## What evidence it provides

This is a **control and standards source**, not empirical threat evidence.

It provides:

- normative requirements for authentication and verifier behaviour;
- password requirements, including blocklists and online throttling;
- authenticator lifecycle guidance: binding, recovery, invalidation, loss/theft/compromise;
- phishing-resistance definitions and recognised mechanisms;
- session-management requirements for cookies, access tokens, reauthentication, and monitoring;
- security considerations for authenticator threats and session attacks;
- privacy and customer-experience considerations for authentication systems.

It does **not** provide:

- observed bot-abuse prevalence;
- credential-stuffing volumes;
- detection-model performance;
- false-positive or false-negative rates for fraud indicators;
- vendor/tool evaluation;
- modern browser-automation evasion evidence;
- evidence that a specific control stops a specific automated-abuse campaign.

## Details most relevant to openbotrisk

### Authentication assurance levels

NIST defines three AALs:

| AAL | Relevant meaning |
|---|---|
| AAL1 | Basic confidence; single-factor or multi-factor authentication permitted. MFA is recommended but not required. |
| AAL2 | High confidence; two distinct factors required. Verifiers must offer at least one phishing-resistant authentication option. |
| AAL3 | Very high confidence; public-key cryptographic authentication, phishing resistance, authentication intent, replay resistance, and non-exportable keys required. |

Project use: helps distinguish **authentication strength** from **bot detection**. A strong login process can reduce account takeover risk, but it does not by itself classify traffic as human or bot.

### Passwords and credential stuffing

Useful requirements:

- single-factor passwords must be at least 15 characters;
- passwords used only as part of MFA must be at least 8 characters;
- password composition rules must not be imposed;
- periodic password changes must not be required unless compromise is suspected;
- passwords must be checked against a blocklist of common, expected, or compromised values;
- password managers and paste/autofill should be allowed;
- verifiers must implement rate limiting for failed authentication attempts;
- passwords must be salted and hashed with a suitable password hashing scheme.

Project use: strong standards anchor for credential-cracking and credential-stuffing defensive baseline. Pair with PortSwigger for attack mechanics and OWASP OAT for threat category naming.

### Rate limiting / throttling

NIST requires controls against online guessing attacks where required by authenticator type. Unless otherwise specified, failed attempts using a specific authenticator on a single subscriber account must be limited to no more than 100 before disabling that authenticator.

Additional techniques may include:

- bot detection and mitigation challenge before authentication;
- increasing wait times after failed attempts;
- risk-based/adaptive authentication using IP address, geolocation, timing of request patterns, or browser metadata.

Project use: strong source for login throttling and adaptive authentication as defensive controls. It should not be used as evidence that these controls defeat modern bots, especially distributed credential-stuffing.

### Phishing resistance

NIST defines phishing resistance as a protocol property that prevents disclosure of authentication secrets or valid authenticator outputs to an impostor verifier without relying on user vigilance.

Important points:

- manual-entry OTP and out-of-band codes are not phishing-resistant;
- phishing resistance requires cryptographic authentication;
- recognised methods include channel binding and verifier name binding;
- AAL2 must offer a phishing-resistant option;
- AAL3 requires phishing-resistant authentication.

Project use: useful for account-takeover and session-risk pages. It helps separate **phishing resistance** from generic MFA.

### Session management

Relevant session points:

- browser cookies do not count as physical authenticators, except as short-term secrets for session maintenance;
- session secrets maintain continuity of authenticated sessions;
- authenticated sessions require reauthentication timeouts depending on AAL;
- session monitoring may use signals such as IP address, geolocation, request timing, and browser characteristics;
- session attacks such as hijacking and CSRF can have security impacts similar to authentication compromise;
- session secrets should be protected from access by mobile code where possible.

Project use: important counterpart to browser-automation/cookie sources. It prevents the project from overstating “cookie capture” as equivalent to authentication: NIST treats cookies as session-maintenance secrets, not authenticators.

### Privacy and fraud indicators

NIST requires privacy risk assessment around records retention and optional session monitoring. It also says fraud indicators should be assessed for efficacy and potential negative impacts on user populations.

Project use: good standards source for the governance/privacy side of bot and fraud detection. It supports the argument that risk signals are not free: they require efficacy assessment and privacy review.

## Signals or techniques mentioned

- authentication assurance levels;
- passwords;
- password blocklists;
- failed-attempt rate limiting / throttling;
- bot detection and mitigation challenge before authentication;
- increasing wait periods after failures;
- risk-based/adaptive authentication;
- IP address;
- geolocation;
- timing of request patterns;
- browser metadata;
- phishing-resistant authentication;
- channel binding;
- verifier name binding;
- replay resistance;
- authentication intent;
- authenticator binding;
- authenticator recovery;
- account recovery;
- session secrets;
- browser cookies;
- access tokens;
- reauthentication;
- session monitoring;
- biometric characteristics including keystroke patterns, typing speed, mouse movements, gait, and device handling.

## Threat types covered

NIST is not an automated-threat taxonomy, but it supports several openbotrisk areas:

- credential stuffing;
- credential cracking;
- account takeover;
- phishing-mediated account compromise;
- session hijacking;
- session replay / cookie/session abuse;
- brute-force attacks against passwords and OTPs;
- account recovery abuse;
- MFA fatigue / push-style abuse, by implication and through stronger authentication guidance;
- fraud-risk signalling in authentication.

OAT mappings:

- OAT-008 Credential Stuffing — strong defensive relevance.
- OAT-007 Credential Cracking — strong defensive relevance.
- OAT-019 Account Creation — indirect relevance through authentication and fraud indicators.
- OAT-020 Account Aggregation — indirect relevance where accounts are accessed by intermediaries or delegated flows.
- OAT-011 Scraping — only indirectly, where authenticated sessions are used for automated data access.
- OAT-006 Expediting / OAT-005 Scalping / OAT-013 Sniping — indirect relevance if access is account/session gated.

## What is strong

- Authoritative standards source for authentication and session management.
- Stronger than vendor blogs for password policy, MFA, phishing resistance, session cookies, and reauthentication.
- Very useful corrective to simplistic claims:
  - MFA does not automatically mean phishing-resistant;
  - cookies are not authenticators;
  - fraud/risk indicators are not authentication factors;
  - IP/geolocation/browser metadata may support risk decisions but require efficacy and privacy assessment.
- Useful bridge between PortSwigger vulnerability mechanics and ASVS application requirements.
- Useful for explaining why account-abuse defences are layered: password policy, blocklists, throttling, MFA, phishing resistance, session controls, recovery controls, and monitoring.

## What is weak or limited

- Not a bot-detection source.
- Not an observed-abuse source.
- Not specific to scraping, scalping, sniping, or AI agents.
- Does not evaluate bot-management systems.
- Does not describe modern anti-detect browsers, residential proxy markets, cloud browser services, or browser automation frameworks.
- Does not provide detection thresholds for fraud indicators.
- Does not prove rate limiting is sufficient against distributed attacks.
- U.S. federal context is central; applicability outside that context should be treated as authoritative guidance, not mandatory law.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  Account and session protection against online guessing, credential theft, phishing, session hijacking, and risky authentication/session behaviour.

- **What does it fail to represent?**  
  It does not represent the operational bot-detection layer: browser fingerprints, TLS fingerprints, behavioural biometrics, vendor bot scores, scraping infrastructure, anti-detect tooling, or abuse prevalence.

- **What additional evidence would be needed to go further?**  
  OWASP OAT for automated-threat categories; PortSwigger for web-authentication vulnerability mechanics; ASVS for application-security verification requirements; Cloudflare/HUMAN/DataDome for operational bot-management framing; academic bot-detection/privacy papers for detection signals; and legal/enforcement/vendor telemetry sources for observed abuse.

## What it cannot show

- It cannot show that credential stuffing is common.
- It cannot show that rate limiting defeats credential stuffing.
- It cannot show that a given fraud indicator is accurate or fair.
- It cannot show that bot-detection challenges work.
- It cannot show browser automation detectability.
- It cannot show commercial bot-management efficacy.
- It cannot classify bot traffic by itself.
- It cannot replace OWASP OAT or bot-detection literature.

## Project impact

Use this as a **core authentication/session-control foundation source**.

Best uses:

- credential stuffing and account takeover defensive baseline;
- password policy and password-blocklist guidance;
- rate limiting and throttling baseline;
- phishing-resistant authentication explanation;
- session/cookie distinction;
- privacy/governance of fraud indicators;
- bridge from PortSwigger attack mechanics to ASVS verification requirements.

Do not use it as:

- threat prevalence evidence;
- bot-detection performance evidence;
- evidence of current attacker tooling;
- proof that controls close down modern automation;
- a scraping or AI-agent source.

## Relationship to other register entries

- **ASVS 5.0.0**: ASVS converts NIST-style authentication/session guidance into broader web-application verification requirements.
- **PortSwigger authentication entries**: PortSwigger explains attack mechanics; NIST provides standards-level control requirements.
- **OWASP OAT / Handbook**: OAT names automated threat events; NIST is focused on authentication and session assurance.
- **MDN cookies**: MDN explains cookie mechanics; NIST explains that cookies are session secrets, not authenticators.
- **Medium Playwright cookies**: Playwright source shows automation can read cookies; NIST gives the defensive/session-management frame.
- **Martínez Llamas et al.**: privacy/governance of detection signals; NIST gives specific authentication privacy-risk requirements.
- **Cloudflare/HUMAN/DataDome**: vendor sources describe bot-management signals; NIST describes authentication/session controls.

## Dual-use containment

Low dual-use. This is defensive standards guidance. The main risk is overclaiming: do not use NIST authentication controls as evidence that bot abuse has been solved, or as evidence of observed automated abuse.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `nist-2025-sp-800-63b-4-authentication-authenticator-management` |
| Title | *Digital Identity Guidelines: Authentication and Authenticator Management* |
| Organisation / authors | NIST / Temoshok et al. |
| Year | 2025 |
| Category | foundations |
| Evidence basis | standards-reference / authentication-guidance / control-requirements |
| Operational proximity | control |
| Signals / techniques | passwords; blocklists; throttling; bot challenges; adaptive authentication; IP; geolocation; request timing; browser metadata; phishing resistance; session cookies; session monitoring |
| Threat types | credential stuffing; credential cracking; account takeover; phishing; session hijacking; session abuse |
| Project use | Core authentication/session-control source for account-abuse and credential-stuffing sections |
| Main caution | Not bot-abuse telemetry, not bot-detection performance evidence, and not a current automation-tooling source |
| Entry file | `nist-2025-sp-800-63b-4-authentication-authenticator-management.md` |
