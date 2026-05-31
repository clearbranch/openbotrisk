# A Large-scale Empirical Analysis of Browser Fingerprints Properties for Web Authentication — Andriamilanto et al. 2021

## Bibliographic

- **Citation**: Andriamilanto, N., Allard, T., Le Guelvouit, G., & Garel, A. (2021). A Large-scale Empirical Analysis of Browser Fingerprints Properties for Web Authentication. *ACM Transactions on the Web*. https://doi.org/10.1145/3478026
- **Source URL or path**: 2006.09511v2.pdf
- **Date accessed**: 2026-06-01
- **Category**: academic / foundations
- **Tags**: browser-fingerprinting, authentication, web-authentication, multi-factor-authentication, fingerprint-stability, fingerprint-distinctiveness, canvas, audio-fingerprint, WebGL, dynamic-attributes, privacy, public-data-limits

## What it claims

- Browser fingerprints can be useful as an additional web-authentication factor because they are distinctive, frictionless to collect, and require no extra user action.
- Browser fingerprints should not be treated as perfect identifiers; their usefulness depends on distinctiveness, stability, collection time, size, and verification accuracy.
- A wide fingerprint surface with many attributes can produce much higher distinctiveness than studies using a small number of attributes.
- Browser fingerprints evolve over time, but many attributes remain stable enough to support a simple verification mechanism.
- Mobile browser fingerprints are less distinctive than desktop browser fingerprints in the authors’ dataset.
- Browser fingerprinting has privacy risks, even when used for authentication rather than tracking.
- Browser-fingerprint authentication mechanisms need to consider replay, mimicry, account recovery, fingerprint evolution, and browser population bias.

## What evidence it provides

The paper provides a large-scale empirical analysis of browser fingerprints as a possible web-authentication factor.

The dataset was collected over six months, from December 2016 to June 2017, through fingerprinting scripts placed on two general-audience French web pages controlled by an industrial partner. The final working dataset contains:

- 4,145,408 fingerprints
- 1,989,365 browsers
- 216 original attributes
- 46 extracted attributes
- 262 total attributes
- 6 months of collection

The collected attributes include:

- 200 JavaScript properties
- 16 HTTP header fields
- five HTML5 canvas attributes
- three audio fingerprinting methods
- one WebGL canvas

The paper evaluates browser fingerprints using properties inspired by biometric authentication:

- distinctiveness
- stability
- collection time
- size
- loss of efficacy across device types
- accuracy of a simple verification mechanism

Key reported findings include:

- Overall unicity rate of 81.8% on the complete dataset.
- Stable time-partitioned unicity rate of more than 81.3%.
- 94.7% of fingerprints are shared by eight browsers or fewer.
- Desktop fingerprints are much more distinctive than mobile fingerprints, with time-partitioned unicity around 84% for desktop and 42% for mobile.
- On average, more than 91% of attributes remain identical between two observations, even when separated by nearly six months.
- Half of fingerprints are collected in under 2.92 seconds, and 95% in under 10.42 seconds.
- The simple illustrative verification mechanism achieves an equal error rate of 0.61%.

The evidence is strong for the properties of browser fingerprints in a large browser population. It is not direct evidence about bot detection or bot evasion.

## Signals or techniques mentioned

- Browser fingerprinting
- Web authentication
- Multi-factor authentication
- User-Agent
- HTTP headers
- JavaScript properties
- navigator object
- Canvas fingerprinting
- HTML5 canvas
- Audio fingerprinting
- WebGL canvas
- Dynamic fingerprinting attributes
- Cookies / UID
- Hashed IP address
- Attribute stability
- Attribute distinctiveness
- Unicity rate
- Anonymity sets
- Fingerprint similarity
- Equal error rate
- Collection time
- Fingerprint size
- Desktop vs mobile fingerprint differences
- Replay attack discussion
- Fingerprint evolution
- Browser population bias
- Authentication verification mechanism

## Threat types covered

The paper is not organised around OWASP Automated Threat categories and is not a bot-abuse paper.

Directly covered:

- browser fingerprinting as an additional authentication factor
- web-authentication strengthening
- password weakness and phishing as motivation for additional factors
- privacy/security trade-offs in browser fingerprinting

Relevant project/OAT mappings:

- cross-cutting relevance to bot detection and anti-fraud where browser fingerprints are used to assess whether a session is expected or anomalous
- indirect relevance to credential stuffing and account takeover because fingerprints may be used as an additional login risk signal
- indirect relevance to fake account creation, scraping, scalping, and carding where browser fingerprints may be part of bot detection or risk scoring
- not direct evidence for any specific automated threat category

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates the defender-side question: “Are browser fingerprints stable and distinctive enough to be useful as a risk or authentication signal?” This is relevant to bot management because anti-bot systems often use browser/device fingerprints, and account-security systems may use fingerprints to detect unusual login sessions.

- **What does it fail to represent?**  
  It does not study bots, automation frameworks, evasion tools, commercial anti-bot services, malicious traffic, or adversarially altered fingerprints. The dataset is from general web visitors, mainly French-speaking users, not bot operators. It does not measure whether fingerprints distinguish bots from humans. It does not evaluate Playwright, Puppeteer, Selenium, anti-detect browsers, cloud browsers, residential proxies, or AI browser agents. It also predates some modern browser privacy changes and current fingerprinting/evasion tooling.

- **What additional evidence would be needed to go further?**  
  Evaluation against real bot traffic; testing under fingerprint spoofing and anti-detect browsers; integration with login-risk or bot-detection outcomes; current replication with modern browser versions; comparison with privacy-preserving browsers; analysis under residential proxy and cloud browser use; evidence from commercial bot-management or account-security systems.

## What it cannot show

- It cannot show that browser fingerprints detect bots reliably.
- It cannot show that fingerprint-based bot detection is robust to spoofing.
- It cannot show that fingerprints are sufficient for account takeover detection or credential-stuffing defence.
- It cannot show current distinctiveness or stability without replication, because browsers and privacy protections have changed since 2016–2017.
- It cannot show whether anti-detect browsers can construct realistic fingerprints.
- It cannot resolve the privacy trade-off around fingerprinting.
- It cannot replace FP-Inconsistent or similar studies that directly examine evasive bot traffic.

## Project impact

- Strong foundations source for the browser-fingerprinting section.
- Useful companion to Iqbal et al. 2021 FP-Inspector:
  - Iqbal et al. explains detection of fingerprinting scripts.
  - Andriamilanto et al. explains the authentication usefulness and measurable properties of fingerprints.
  - FP-Inconsistent then explains how evasive bot traffic alters fingerprints and creates inconsistencies.
- Supports a nuanced claim: browser fingerprints can be useful signals, but they are probabilistic and population-dependent rather than perfect identifiers.
- Useful for a section on why fingerprinting is attractive to defenders: passive/frictionless collection, high distinctiveness, and some stability.
- Also useful for a privacy limitations section: the same properties that make fingerprints useful for authentication can make them risky for tracking.
- Should be cited as authentication/fingerprint-property evidence, not as direct bot-detection evidence.
