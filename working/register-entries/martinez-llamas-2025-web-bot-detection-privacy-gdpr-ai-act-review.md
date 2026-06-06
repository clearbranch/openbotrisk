# Martínez Llamas et al. (2025) - Web bot detection, privacy, GDPR and AI Act

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Martínez Llamas, J., Vranckaert, K., Preuveneers, D., & Joosen, W. (2025). *Balancing Security and Privacy: Web Bot Detection, Privacy Challenges, and Regulatory Compliance under the GDPR and AI Act*. Open Research Europe, 5:76. https://doi.org/10.12688/openreseurope.19347.1
- **Publication status**: review article; version 1; peer review approved by two reviewers.
- **First published**: 24 March 2025.
- **Latest published**: 24 March 2025.
- **Document last updated in PDF**: 20 March 2026.
- **Source URL or path**: `53bd845a-4be2-4f15-9f8a-48606e96e78b_19347_-_davy_preuveneers(1).pdf`
- **Category**: academic
- **Evidence basis**: review / methods-taxonomy / legal-regulatory analysis
- **Operational proximity**: capability - conceptual and literature-based analysis of bot detection, evasion, privacy, and regulatory compliance; not observed abuse measurement.
- **Tags**: web-bots, bot-detection, privacy, GDPR, AI-Act, ePrivacy, PETs, fingerprinting, behavioural-biometrics, network-traffic, machine-learning, evasion, headless-browsers, proxies, IP-rotation, DPIA, automated-decision-making

## What it claims

- Web bots are dual-use: they support benign automation such as indexing and automation, but also support malicious activity such as credential stuffing, scraping, scalping, DDoS, and spam.
- Distinguishing humans, good bots, and bad bots is technically difficult because modern automated traffic can mimic browsers, rotate infrastructure, and imitate behavioural signals.
- Detection should be understood by data source, not only by algorithm family. The paper organises detection around network traffic data, fingerprints, and behavioural biometrics.
- More aggressive detection generally means more data collection, creating a tension between security and privacy.
- Bot detection data may be personal data under GDPR, especially where IP addresses, device identifiers, browser fingerprints, or behavioural data can single out users.
- AI-powered bot detection and automated responses may interact with GDPR automated decision-making rules and, in some contexts, the AI Act.
- Privacy Enhancing Technologies (PETs) can reduce privacy risks but do not by themselves guarantee legal compliance, auditability, transparency, fairness, or human oversight.

## What evidence it provides

- A review taxonomy of bot-detection methods:
  - network/request data, including IP addresses, HTTP headers, cookies, request timing, referers, and session features;
  - browser/device/TLS fingerprints, including User-Agent, screen/viewport, fonts, GPU, JavaScript support, cookie support, WebDriver signals, TLS handshake characteristics;
  - behavioural biometrics, including mouse movement, scrolling, clicking, and keystroke timing.
- A review taxonomy of evasion methods:
  - headless browser automation;
  - adversarial fingerprints and browser-identity manipulation;
  - proxies and IP rotation;
  - rate-limit and throttling avoidance;
  - behavioural mimicry;
  - machine-learning/adaptive bots.
- A legal analysis mapping detection practices to GDPR concepts:
  - personal data;
  - legal basis;
  - legitimate interest;
  - data minimisation;
  - purpose limitation;
  - Article 22 automated decision-making;
  - DPIA requirements;
  - biometric data concerns.
- An AI Act analysis:
  - many banned-practice provisions are only indirectly relevant to bot detection;
  - high-risk classification may become relevant where bot detection involves biometric identification or deployment in critical infrastructure.
- A PETs discussion:
  - data minimisation;
  - anonymisation/pseudonymisation;
  - differential privacy;
  - homomorphic encryption;
  - secure multi-party computation;
  - organisational controls and audits.

## Signals or techniques mentioned

- IP address
- geolocation
- ISP / residential vs data-centre IP distinction
- proxy and VPN detection
- HTTP headers
- User-Agent
- Accept-Language
- Referer
- cookies
- session duration
- request rate and arrival patterns
- web access logs
- browser fingerprinting
- device fingerprinting
- TLS fingerprinting
- JavaScript support
- WebDriver signal
- canvas / fonts / GPU / screen / viewport
- mouse movement
- scrolling
- click patterns
- keystroke dynamics
- CAPTCHA
- machine learning
- deep learning
- reinforcement learning
- anomaly detection

## Threat types covered

- credential stuffing
- scraping
- scalping
- spam
- DDoS
- account takeover
- malicious crawling
- automated abuse of web workflows
- good/bad bot distinction
- AI-assisted or adaptive bot evasion

## What is strong

- Strongest academic source so far for the **detection/privacy trade-off**.
- Strong for explaining why bot detection is not just a technical issue but also a governance issue.
- Strong for the “simple to complex” detection structure:
  - IP/rate signals;
  - HTTP headers;
  - browser/device fingerprints;
  - behavioural signals;
  - ML/adaptive systems;
  - legal/privacy controls.
- Good bridge between MDN foundations, PortSwigger authentication abuse, Cloudflare/HUMAN vendor claims, and scraper-side bypass material.
- Good for explaining why defensive vendors collect many signals: each extra layer can improve discrimination, but also increases personal-data and tracking risk.

## What is weak or limited

- This is a review and conceptual/legal analysis, not an empirical study.
- It does not test detection systems, build a tool, collect traffic, or report measured performance.
- It does not provide bot prevalence estimates from primary data.
- It does not validate whether PETs preserve detection performance in operational systems.
- Some regulatory claims should be treated as legal analysis, not legal advice.
- Peer reviewers noted that ePrivacy is mentioned but could be developed further, especially around device fingerprinting and cookie/device access consent.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** The technical and regulatory structure of modern bot detection systems used to separate humans, benign bots, and malicious bots.
- **What does it fail to represent?** Operational detection performance, real attack volume, vendor efficacy, abuse economics, or attacker success rates.
- **What additional evidence would be needed to go further?** Empirical datasets, independent detection benchmarks, vendor telemetry with denominators, legal/regulatory primary guidance, and real deployment case studies.

## What it cannot show

- It cannot prove any detection method works in production.
- It cannot rank vendors or tools.
- It cannot quantify how common bot attacks are.
- It cannot show whether a particular implementation is GDPR or AI Act compliant.
- It cannot prove PETs solve the privacy problem.
- It cannot replace legal advice or regulator guidance.

## Project impact

Use this as a **core review paper** for the academic/methods/governance layer. It should probably be one of the anchor sources for:

- bot detection methods taxonomy;
- privacy risk of detection signals;
- GDPR framing;
- AI Act framing;
- PETs and their limits;
- why “more detection signal” can mean “more personal data”.

This source should not be used as observed-use evidence. Its value is conceptual structure and synthesis.

## Best placement in the evidence register

- Primary section: **Academic and research literature**
- Secondary section: **Detection/privacy/governance**
- Cross-links:
  - MDN HTTP headers / cookies / User-Agent foundations;
  - Cloudflare bot detection engines and Detection IDs;
  - ScrapingBee bypass guides;
  - PortSwigger authentication abuse;
  - survey/data-quality bot papers, where behavioural/attention checks overlap.

## Possible register row

| Field | Value |
|---|---|
| Register id | `martinez-llamas-2025-web-bot-detection-privacy-gdpr-ai-act` |
| Title | *Balancing Security and Privacy: Web Bot Detection, Privacy Challenges, and Regulatory Compliance under the GDPR and AI Act* |
| Category | academic |
| Evidence basis | review / methods-taxonomy / legal-regulatory analysis |
| Operational proximity | capability |
| Tags | web-bots; bot-detection; privacy; GDPR; AI-Act; ePrivacy; PETs; fingerprinting; behavioural-biometrics; network-traffic; machine-learning; evasion; proxies; IP-rotation; DPIA; automated-decision-making |
| Project use | Anchor source for bot-detection taxonomy and detection/privacy trade-off |
| Main caution | Review and legal analysis; not observed abuse evidence or detection performance validation |
