# Balancing Security and Privacy: Web Bot Detection, Privacy Challenges, and Regulatory Compliance under the GDPR and AI Act — Martínez Llamas et al. 2025

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: full text from uploaded PDF
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Martínez Llamas, J., Vranckaert, K., Preuveneers, D., & Joosen, W. (2025). *Balancing Security and Privacy: Web Bot Detection, Privacy Challenges, and Regulatory Compliance under the GDPR and AI Act* [version 1; peer review: 2 approved]. *Open Research Europe*, 5:76. https://doi.org/10.12688/openreseurope.19347.1
- **Source URL or path**: https://doi.org/10.12688/openreseurope.19347.1; local uploaded PDF: `SRC-047-martinez-llamas-2025-web-bot-detection-privacy-gdpr-ai-act.pdf`
- **Date accessed**: 2026-06-06
- **Category**: academic
- **Evidence basis**: methods-taxonomy
- **Operational proximity**: capability — the source is a peer-reviewed review / taxonomy paper describing detection methods, evasion methods, privacy risks, GDPR / AI Act implications, and PETs. It does not itself measure live bot abuse or production traffic, but it supports that these detection and evasion capability classes exist in the literature.
- **Tags**: academic, methods-taxonomy, taxonomy, privacy, gdpr, ai-act, compliance, pets, data-minimisation, differential-privacy, homomorphic-encryption, secure-multiparty-computation, fingerprinting, browser-fingerprinting, device-fingerprinting, tls-fingerprinting, behavioural-biometrics, mouse-dynamics, keystroke-dynamics, network-traffic, http-headers, ip-addresses, user-agent, proxies, residential-proxies, ip-rotation, headless-browser, selenium, puppeteer, playwright, adversarial-fingerprints, behavioural-mimicry, captcha, machine-learning, automated-decision-making, dpia, human-oversight

## What it claims

- The paper argues that web bots have a dual role: they support benign automation such as indexing and customer support, but also enable malicious activities such as credential stuffing, scraping, scalping, and DDoS.
- It claims that bot detection is an arms race: as detection improves, malicious bots adapt using more human-like behaviour, proxy infrastructure, fingerprint manipulation, and AI-enabled techniques.
- It proposes a data-driven taxonomy of web bot detection methods, organised by the data source used for detection rather than by the modelling method alone.
- It classifies key detection data sources into network traffic data, fingerprints, and behavioural biometrics.
- It states that network-traffic detection relies on signals such as IP addresses, HTTP headers, request frequency, geolocation, proxy / VPN / data-centre IP indicators, user-agent strings, referers, cookies, timestamps, and robots.txt behaviour.
- It states that traffic-derived detection methods may be rule-based, statistical, or ML-based, including models over request patterns, session features, access logs, and more complex deep-learning or reinforcement-learning approaches.
- It claims that fingerprinting can support one-shot or early detection by combining browser, device, or TLS attributes, but that these same attributes create tracking and privacy risks.
- It identifies example fingerprint attributes including user-agent, timestamp, timezone, IP, plug-ins, canvas, screen resolution, viewport, GPU, fonts, language, cookie support, JavaScript support, touch-screen support, and WebDriver.
- It claims that behavioural biometrics such as mouse movements, scrolling, clicks, and keystrokes can help distinguish humans from bots because human interactions are more variable and less mechanically efficient.
- It also claims that behavioural data raises privacy risks because it can function as a de facto identifier, enabling tracking, profiling, or inference about users.
- It describes bad bots by sophistication level: simple bots such as scripts or cURL-like automation, moderate bots that disguise themselves as browsers and use headless browsing, and advanced bots that emulate human behaviours such as mouse movements and browsing patterns.
- It identifies evasion strategies including headless browsers, adversarial fingerprints, network proxies, residential proxies, IP rotation, rate-limit avoidance, throttling avoidance, session regeneration, behavioural mimicry, and machine-learning-enabled adaptation.
- It states that headless browsers and automation frameworks such as Selenium, Puppeteer, and Playwright are widely used for legitimate automation but are also exploited for bot development and evasion.
- It claims that bots can manipulate default automation signals, such as `HeadlessChrome` user-agent markers or WebDriver / Chromium automation indicators, to make browser fingerprints appear closer to human-controlled browsers.
- It states that residential proxies can make IP-based detection harder because traffic is routed through genuine residential devices or ISP-assigned residential IPs; it also notes ethical concerns where residential proxy traffic is routed through users' devices without transparent consent.
- It claims that advanced bots can distribute requests across proxy pools, introduce random delays, create new sessions with distinct cookies / headers / user-agent strings, and dynamically adjust their behaviour in response to server warnings or temporary blocks.
- It states that AI and ML can be used defensively for bot detection and adversarially by bots to learn from detection responses, adapt strategies, and improve CAPTCHA bypass.
- It argues that web bot detection can involve personal data because detection systems monitor information that can identify, single out, or infer attributes about users.
- It claims that IP addresses and device identifiers may constitute personal data under GDPR depending on the controller's ability to identify or single out users.
- It argues that the usual legal basis for cybersecurity-related bot detection under GDPR may often be legitimate interest, provided the processing is necessary and proportionate and does not override user rights.
- It states that behavioural patterns such as mouse and keystroke patterns may be biometric data, but their use to distinguish bots from humans may be permissible for network-security purposes if they are not used to identify a particular individual and if necessity is shown.
- It argues that automated bot-detection responses can raise GDPR Article 22 issues where they amount to solely automated decisions with legal or similarly significant effects, especially where false positives block access to important accounts or services.
- It states that human oversight or human overruling may be required where automated decisions have significant effects.
- It states that Data Protection Impact Assessments may be required for higher-risk bot-detection processing, especially systematic profiling, large-scale sensitive-data processing, data matching, vulnerable subjects, or innovative technologies.
- It argues that the EU AI Act may apply to some bot-detection systems, including some rule-based systems because the Act's AI-system definition is broader than machine learning alone.
- It claims most AI Act banned practices are only indirectly relevant to bot detection if the system is used for social scoring, criminal-risk assessment, sensitive biometric categorisation, or function creep beyond security.
- It argues that AI-based bot detection generally will not require high-risk AI certification unless it involves biometric identification / singling-out or is deployed as a safety component in critical infrastructure.
- It states that high-risk AI systems, where applicable, require risk management, data governance, documentation, logging, transparency, human oversight, accuracy, robustness, cybersecurity, and quality-management controls.
- It claims that bot disclosure rules under the AI Act are relevant to some AI systems that interact directly with people or generate synthetic content, but web bot detection itself is usually a specific-purpose model rather than a general-purpose AI model.
- It argues that Privacy Enhancing Technologies can reduce privacy risk in bot detection, but cannot by themselves ensure legal compliance.
- It discusses data minimisation, IP truncation, IP hashing, salting, differential privacy, homomorphic encryption, and secure multi-party computation as possible privacy-aware techniques.
- It claims that data minimisation is difficult in bot detection because defenders may justify broader data collection as necessary in an adversarial arms race.
- It claims that IP hashing has limitations because the finite IPv4 space makes precomputed reversal attacks possible unless additional protections such as salting are used.
- It claims that differential privacy can reduce re-identification risk but may reduce bot-detection accuracy by masking rare or anomalous patterns.
- It claims that homomorphic encryption and secure multi-party computation protect data during computation but introduce operational, computational, latency, coordination, and expertise burdens.
- It concludes that PETs must be combined with organisational measures such as documentation, transparent processes, clear policies, audits, and human oversight to satisfy GDPR and AI Act expectations.
- It concludes that PETs may also make evasion detection harder because anonymised or encrypted data can reduce the signals available for detecting malicious bots.

## What evidence it provides

- The source is a review / taxonomy paper rather than an empirical measurement study. It synthesises existing academic literature, law, regulatory frameworks, and privacy-enhancing-technology concepts.
- The evidence for the detection taxonomy comes from cited literature on access logs, Markov models, Bayesian models, ML classifiers, deep-learning models, reinforcement-learning detection, browser/device/TLS fingerprinting, mouse dynamics, and keystroke dynamics.
- The evidence for evasion classes comes from cited literature and state-of-practice descriptions of headless browsing, adversarial fingerprinting, proxies / residential proxies, IP rotation, rate-limit avoidance, behavioural mimicry, ML adaptation, and CAPTCHA bypass.
- The evidence for legal analysis comes from GDPR articles and recitals, CJEU case law such as Nowak, Breyer, OT, and SCHUFA, the ePrivacy Directive, DORA, NIS2, the EU AI Act, the Cyber Resilience Act, EDPB / Article 29 Working Party guidance, and AI Act provisions on high-risk systems and human oversight.
- The evidence for PETs comes from general privacy-engineering literature on data minimisation, differential privacy, homomorphic encryption, and secure multi-party computation, applied conceptually to bot-detection scenarios.
- The source does not report a dataset, experiment, production deployment, benchmark, accuracy score, false-positive rate, or live abuse observation.
- The source includes peer review information and is published in Open Research Europe with two approved reviews.
- The paper states that no data are associated with the article.

## Signals or techniques mentioned

- IP addresses.
- IP geolocation.
- ISP details.
- Residential vs data-centre IP distinction.
- Proxy / VPN detection.
- IP blacklists and reputation lists.
- Request frequency / rate signals.
- HTTP headers.
- User-Agent header.
- Accept-Language header.
- Referer header.
- Cookies.
- Content type.
- Timestamps.
- URL referers.
- Request forwarding status.
- robots.txt access and compliance.
- Web access logs.
- Session features.
- Number of pages visited.
- Number of HTTP requests.
- Volume of data retrieved.
- Session duration.
- Time spent on page.
- Login or purchase actions.
- Rule-based heuristics.
- Statistical baselines.
- Discrete-time Markov chains.
- Hidden Markov models.
- Bayesian probabilistic modelling.
- Random Forests.
- Support Vector Machines.
- k-Nearest Neighbours.
- Deep learning.
- Reinforcement learning.
- Browser fingerprints.
- Device fingerprints.
- TLS fingerprints.
- User-agent strings.
- Operating system / platform.
- Screen resolution.
- Colour depth.
- Fonts.
- Time zone.
- Language preferences.
- WebGL.
- Canvas.
- JavaScript features / JavaScript support.
- GPU details.
- CPU details.
- Battery status.
- Sensor data.
- TLS cipher suites.
- TLS version.
- TLS extensions and extension ordering.
- WebDriver indicator.
- Mouse movements.
- Scrolling behaviour.
- Clicks.
- Keystroke dynamics.
- CNNs over mouse-movement images.
- LSTM models over temporal behaviour.
- CAPTCHA.
- Headless browsers.
- Selenium.
- Puppeteer.
- Playwright.
- Adversarial fingerprints.
- User-agent customisation.
- Browser automation flags.
- Data-centre proxies.
- Residential IP proxies.
- IP rotation.
- Request scheduling.
- Random delays.
- Session regeneration.
- Cookie/header/user-agent variation.
- Server-response monitoring.
- Behavioural mimicry.
- Synthetic mouse and keyboard events.
- Machine-learning-enabled bot adaptation.
- AI-powered CAPTCHA bypass.
- Data minimisation.
- IP truncation.
- IP hashing.
- Salting.
- Differential privacy.
- Homomorphic encryption.
- Secure multi-party computation.
- DPIA.
- Automated decision-making.
- Human oversight.
- High-risk AI-system compliance.

## Threat types covered

- Credential stuffing.
- Web scraping.
- Scalping.
- Spamming.
- DDoS.
- Malicious automation.
- Bot evasion.
- CAPTCHA bypass.
- Automated account / session abuse at a general level.
- The source is broad and method-focused; it does not deeply analyse one specific abuse flow such as ticket scalping, booking-slot sniping, payment abuse, or fake account creation.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** It approximates the technical and governance terrain of web bot detection: what data defenders collect, how detection families are organised, how bots evade those methods, and how GDPR / AI Act obligations shape the design of detection systems. It is valuable as a bridge between technical bot-management literature and privacy / regulatory constraints.
- **What does it fail to represent?** It does not represent production telemetry, attacker use at scale, observed abuse against real sites, vendor effectiveness, current agentic-browser traffic, or a benchmarked detection model. It also abstracts across many bot contexts, so it does not show how methods differ in booking, ticketing, financial services, retail, advertising, or API abuse flows.
- **What additional evidence would be needed to go further?** Empirical studies or vendor/victim telemetry showing how these detection and evasion techniques appear in production; comparative measurements of false positives and false negatives under privacy-preserving transformations; case studies of GDPR / AI Act governance for deployed bot-detection systems; and experiments testing the effect of PETs on detection performance in adversarial settings.

## What it cannot show

- It cannot show whether a particular detection method works well in production.
- It cannot show real-world prevalence of any bot class or evasion tactic.
- It cannot show how often residential proxies, headless browsers, behavioural mimicry, or ML-enabled evasion are used in live attacks.
- It cannot show vendor product efficacy or validate vendor claims.
- It cannot show that PETs preserve enough signal for operational bot detection; it discusses likely trade-offs but does not benchmark them.
- It cannot show how regulators will enforce the AI Act or GDPR against specific bot-detection deployments.
- It cannot show current AI-agent traffic patterns or browser-native automation trends beyond general AI / automation implications.
- It cannot settle legal advice for a particular organisation; the legal discussion is a scholarly analysis and would need jurisdiction-specific counsel before operational use.
- It cannot show how much data is actually necessary for a given bot-detection system because necessity is context-specific and adversarially unstable.

## Project impact

- High-value source for the project's foundations / technical-territory pages because it provides a clear data-source taxonomy: network traffic, fingerprints, and behavioural biometrics.
- Useful anchor for explaining why bot detection creates privacy risk: the same signals that help distinguish bots can also identify, track, or profile users.
- Strong source for the regulatory-compliance strand: GDPR legal bases, legitimate interest, Article 22 automated decisions, DPIAs, biometric-data cautions, AI Act risk tiers, and high-risk AI-system obligations.
- Useful bridge between the technical evidence review and the governance page: it supports the idea that bot mitigation cannot be framed as purely technical where it relies on extensive user monitoring and automated access decisions.
- Good companion to vendor telemetry sources: vendor reports show observed bot activity and claimed controls; this paper gives an academic map of the data categories and compliance constraints behind those controls.
- Supports a project framing that “more signal” is not always straightforwardly better: stronger detection can increase privacy exposure and compliance burden.
- Useful for PET discussion, but with the caveat that PETs may reduce detection power and require organisational controls rather than being a magic compliance layer.
- Should be cited as a review / taxonomy source, not as direct observed-use evidence.
- Good source for a future page or box on “the detection/privacy trade-off” and “why bot detection data can be personal data”.

## Possible register row

| Field | Value |
|---|---|
| Register id | `martinez-llamas-2025-web-bot-detection-privacy-gdpr-ai-act` |
| Title | *Balancing Security and Privacy: Web Bot Detection, Privacy Challenges, and Regulatory Compliance under the GDPR and AI Act* |
| Category | academic |
| Evidence basis | methods-taxonomy |
| Operational proximity | capability |
| Tags | web-bot-detection; privacy; GDPR; AI Act; PETs; fingerprinting; behavioural-biometrics; network-traffic; evasion; proxies; headless-browser; human-oversight |
| Project use | Academic taxonomy and compliance anchor for detection signals, evasion classes, privacy risks, and GDPR / AI Act implications |
| Main caution | Review paper; no production telemetry, no empirical measurement of abuse, no validation of detection effectiveness |
