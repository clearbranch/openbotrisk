# FP-Inconsistent: Measurement and Analysis of Fingerprint Inconsistencies in Evasive Bot Traffic — Venugopalan et al. 2025

## Bibliographic

- **Citation**: Venugopalan, H., Munir, S., Ahmed, S., Wang, T., King, S. T., & Shafiq, Z. (2025). FP-Inconsistent: Measurement and Analysis of Fingerprint Inconsistencies in Evasive Bot Traffic. arXiv:2406.07647v3.
- **Source URL or path**: 2406.07647v3.pdf
- **Date accessed**: 2026-05-31
- **Category**: academic / threat-surface
- **Tags**: browser-fingerprinting, evasive-bots, fingerprint-inconsistency, anti-bot-services, DataDome, BotD, FingerprintJS, honey-site, impression-fraud, bot-services, measurement, spatial-inconsistency, temporal-inconsistency, public-data-limits

## What it claims

- Evasive bots alter browser fingerprint attributes to avoid detection by anti-bot services.
- These altered fingerprints often contain inconsistencies that real devices are unlikely or unable to produce.
- Commercial anti-bot services do not reliably detect all evasive bot traffic in the authors’ honey-site experiment.
- A data-driven inconsistency-detection method can reduce the amount of bot traffic that evades existing anti-bot services.
- Fingerprint inconsistency can be spatial, where attributes within one request conflict with each other, or temporal, where attributes change implausibly across requests from the same device.
- Bots can evade not merely by avoiding block-listed IPs or ASNs, but by manipulating fingerprint attributes such as plugins, touch support, hardware concurrency, screen resolution, and platform.
- Bot detection and user tracking overlap but are not identical: detecting implausible or inconsistent configurations does not necessarily require uniquely identifying every user.
- FP-Inconsistent is proposed as a semi-automatic, data-driven way to generate inconsistency rules for bot detection.
- The approach may create false positives for some privacy-enhancing technologies, especially Tor, and this requires mitigation.

## What evidence it provides

The paper provides a large-scale measurement study using a honey-site architecture and traffic purchased from bot services.

The authors deployed multiple versions of a honey site under one parent domain. Each version used a unique random string in the URL. They purchased traffic from different bot services and gave each service a different URL string, allowing requests to be attributed to a specific bot service while filtering out unrelated traffic.

The honey site integrated two anti-bot services:
- DataDome
- BotD from the FingerprintJS ecosystem

The site also collected browser fingerprint attributes using FingerprintJS.

The dataset contains:
- 507,080 requests
- 20 bot services
- 3 months of data collection, from September to November 2023

Reported detection/evasion evidence:
- DataDome detected 55.44% of bot-service requests.
- BotD detected 47.07% of bot-service requests.
- The paper reports average evasion rates of 52.93% against DataDome and 44.56% against BotD.
- Evasion varied heavily by bot service; some services evaded one or both anti-bot systems at high rates.

The authors analysed fingerprint attributes associated with evasion:
- For BotD, the presence of PDF plugins was strongly associated with evasion.
- For DataDome, lower hardwareConcurrency values helped evasion.
- For services evading both DataDome and BotD, touchSupport was important for BotD evasion while hardwareConcurrency remained relevant for DataDome.

The paper identifies examples of inconsistencies:
- User-Agent claims of iPhone combined with impossible screen resolutions.
- Mismatches between timezone-derived location and IP geolocation.
- The same first-party cookie appearing with different navigator.platform values over time.
- A device presenting changing values for attributes that should not change for the same device.

The proposed FP-Inconsistent method turns these observations into rules:
- spatial inconsistency rules from incompatible attribute pairs inside one request
- temporal inconsistency rules from implausible changes across requests linked by cookies or IP addresses

Reported improvement:
- Combined FP-Inconsistent rules increased DataDome detection from 55.44% to 76.88%.
- Combined FP-Inconsistent rules increased BotD detection from 47.07% to 70.86%.
- The rules reduced evasion by 48.11% for DataDome and 44.95% for BotD.
- The method achieved a true negative rate of 96.84% on 2,206 real-user requests from university students.
- The paper reports that Safari, uBlock Origin, and AdBlockPlus were not detected as bots; Tor was detected as bot traffic due to IP/timezone inconsistency; Brave triggered some temporal inconsistency concerns when fingerprint protection was combined with retained cookies.

The evidence is unusually relevant to current bot-management practice because it evaluates real purchased bot-service traffic against deployed anti-bot products, rather than only synthetic research bots.

## Signals or techniques mentioned

- Browser fingerprint attributes
- User-Agent
- navigator.plugins
- PDF plugins / Chrome PDF Viewer
- navigator.userAgent
- navigator.platform
- navigator.languages / browser language
- touchSupport
- maximum touch points
- hardwareConcurrency / CPU cores
- deviceMemory
- screenResolution
- screenFrame
- forcedColors
- contrast
- canvas fingerprinting
- WebGL-related APIs
- audio fingerprinting
- timezone
- IP geolocation
- ASN and public ASN block lists
- MaxMind minFraud
- MaxMind GeoLite2
- cookies as temporal device identifiers
- FingerprintJS
- DataDome
- BotD
- OpenWPM script/API observation
- SHAP explainability
- XGBoost / random forest classifiers
- spatial inconsistency rules
- temporal inconsistency rules
- filter-list style deployment
- honey-site URL isolation
- bot-service purchased traffic
- privacy-enhancing browsers and extensions:
  - Brave
  - Tor
  - Safari
  - uBlock Origin
  - AdBlockPlus

## Threat types covered

The paper’s explicit threat model is impression fraud rather than account takeover, credential stuffing, carding, scraping, or scalping.

It focuses on publishers buying traffic from bot services that advertise “realistic” or “undetectable” visits. These bots aim to create page views or engagement that can generate advertising revenue while evading anti-bot services.

Relevant project/OAT mappings:
- best mapped to advertising / impression fraud and bot-traffic monetisation
- relevant to the broader browser-fingerprint evasion layer used across many OAT categories
- indirectly relevant to scraping, credential stuffing, scalping, carding, account creation, and account takeover because those threat types may also rely on altered browser fingerprints
- not direct evidence for those other abuse flows unless the project explicitly separates “fingerprint evasion mechanism” from “abuse objective”

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  This is one of the closest sources to modern operational bot pressure. It uses real purchased traffic from bot services, deployed anti-bot services, a honey-site design to establish traffic provenance, and real browser fingerprint attributes. It is especially useful for the project’s modern threat-surface section because it connects evasive bot services, commercial anti-bot detection, and concrete fingerprint inconsistency signals.

- **What does it fail to represent?**  
  The abuse objective is impression fraud. The honey site does not require account login, checkout, booking, payment, credential testing, inventory acquisition, scraping of valuable content, or API interaction. Purchased bot-service traffic may differ from bespoke bot operators targeting high-value workflows. The anti-bot services are black boxes and only two services are tested. The real-user validation set is relatively small and university-based. The approach uses FingerprintJS attributes and may improve with other attributes, but that also raises privacy issues. Temporal inconsistency detection partly depends on cookies or stable identifiers, which bots can delete or avoid. The paper does not directly evaluate Playwright, Puppeteer, Selenium, anti-detect browsers, cloud browsers, residential proxy networks, or AI browser agents as labelled tooling classes, even if some purchased traffic may use similar infrastructure.

- **What additional evidence would be needed to go further?**  
  Evaluation against transactional abuse flows; replication across more anti-bot services; larger and more diverse real-user validation; testing against named automation stacks and anti-detect browsers; evaluation under cookie deletion and privacy controls; integration with TLS fingerprints, behavioural signals, and server-side request patterns; analysis of residential proxy and mobile proxy effects; longitudinal study of bot adaptation after inconsistency rules are deployed.

## What it cannot show

- It cannot show that FP-Inconsistent fully solves evasive bot detection.
- It cannot show that all commercial anti-bot services perform similarly; only DataDome and BotD are tested.
- It cannot show results for credential stuffing, carding, scalping, scraping, account creation, or ATO workflows.
- It cannot show that the bot services represent the most sophisticated operators.
- It cannot show that the inconsistency rules will remain effective once bot operators adapt to them.
- It cannot avoid all privacy trade-offs: increasing fingerprint attributes or persistent identifiers can improve detection but may threaten privacy.
- It cannot guarantee low false positives for all privacy-enhancing tools; Tor is a clear problem case in the paper.
- It cannot replace user-impact evaluation because the real-user traffic sample is limited.

## Project impact

- Very strong source for the project’s modern browser-fingerprint / anti-bot-service section.
- Stronger operational relevance than the controlled Iliou and Acien studies because it uses purchased bot-service traffic and real anti-bot services.
- Useful bridge between academic work and vendor claims: it independently evaluates DataDome and BotD rather than relying on vendor marketing.
- Supports the project’s taxonomy distinction between:
  - behavioural biometrics / web-log detection
  - browser fingerprinting
  - evasion tooling
  - commercial anti-bot services
  - threat-surface measurement
- Important source for the claim that IP block lists are insufficient against evasive bots.
- Provides concrete, testable signals that could inform a prototype or methodology page: impossible device configurations, IP/timezone mismatch, User-Agent/screen mismatch, cookie/platform changes.
- Supports a nuanced privacy section: bot detection and tracking overlap, but are not identical; stronger detection can still create privacy risks.
- Should be treated as a major modern anchor, but with the scope caveat that the evaluated threat model is impression fraud, not all OWASP automated threats.
