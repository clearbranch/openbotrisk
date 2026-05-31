# Cloudflare Bot Management documentation — Cloudflare 2026

## Bibliographic

- **Citation**: Cloudflare. (2026). Cloudflare bot solutions / Bot Management documentation. Cloudflare Docs.
- **Source URL or path**:
  - https://developers.cloudflare.com/bots/
  - https://developers.cloudflare.com/bots/llms.txt
  - https://developers.cloudflare.com/bots/reference/bot-management-variables/
- **Date accessed**: 2026-06-01
- **Category**: vendor / technical documentation
- **Tags**: Cloudflare, bot-management, vendor-docs, bot-score, verified-bots, signed-agents, bot-detection-engines, bot-analytics, JA3, JA4, detection-ids, javascript-detections, waf-custom-rules, account-abuse-protection, AI-crawlers, public-data-limits

## What it claims

- Cloudflare provides bot-specific products for detecting and mitigating automated traffic.
- Its bot solutions are positioned against bad bots that scrape content, stuff credentials, hoard inventory, inflate server costs, and abuse websites or APIs.
- Cloudflare separates simpler plan-level products, such as Bot Fight Mode and Super Bot Fight Mode, from Enterprise Bot Management.
- Bot Management for Enterprise provides more granular controls than the simpler products, including per-request bot scores, custom rules, per-endpoint handling, and detailed analytics.
- Bot Management exposes several decision variables to Ruleset Engine/WAF custom rules and Workers.
- Cloudflare assigns a bot score from 1 to 99, where lower values indicate stronger likelihood that a request is automated.
- Cloudflare distinguishes bad bots from allowed/verified bots, such as search engines and monitoring services.
- Cloudflare supports several signal families and controls, including bot scores, detection IDs, JA3/JA4 fingerprints, JavaScript detections, sequence rules, bot analytics, verified bots, signed agents, and bot-management variables.
- The documentation presents product mechanics and configuration options, not independent evidence of detection effectiveness.

## What evidence it provides

The source is vendor documentation rather than an empirical study.

The docs index shows the scope of Cloudflare’s bot documentation. It includes pages for:

- Bot solutions overview
- Plans
- Bot Analytics
- Account Abuse Protection
- AI Labyrinth
- Block AI Bots
- Custom rules
- Detection IDs
- account takeover detections
- scraping detections
- residential proxy and other additional detections
- JA3/JA4 fingerprint
- Signals Intelligence for JA4
- JavaScript detections
- robots.txt setting
- Sequence rules
- Static resource protection
- Bot detection engines
- Bot scores
- Bot tags
- Signed agents
- Verified bots
- Bot Feedback Loop
- Bot Management variables
- IP validation
- Web Bot Auth
- Machine Learning models
- Bot Detection Alerts
- troubleshooting false positives

The overview page frames the product family as follows:

- Bot Fight Mode: a simple toggle/challenge product for detected bot traffic.
- Super Bot Fight Mode: configurable challenge/block behaviour for known bot patterns, static resources, and analytics.
- Bot Management for Enterprise: granular per-request scores, custom rules, per-endpoint handling, and detailed analytics, especially for ecommerce, banking, and security use cases.

The Bot Management variables page provides the strongest technical detail for this register entry. It shows that Cloudflare exposes Bot Management fields inside WAF/custom-rule logic and Workers. Relevant fields include:

- `cf.bot_management.score`
- `cf.bot_management.verified_bot`
- `cf.bot_management.static_resource`
- `cf.bot_management.ja3_hash`
- `cf.bot_management.ja4`
- `cf.bot_management.detection_ids`
- `cf.bot_management.signed_agent`
- `cf.verified_bot_category`

It also exposes Workers variables such as:

- `request.cf.botManagement.score`
- `request.cf.botManagement.verifiedBot`
- `request.cf.botManagement.staticResource`
- `request.cf.botManagement.ja3Hash`
- `request.cf.botManagement.ja4`
- `request.cf.botManagement.jsDetection.passed`
- `request.cf.botManagement.detectionIds`
- `request.cf.botManagement.signedAgent`
- `request.cf.verifiedBotCategory`

The variables page also states that JA3/JA4 fingerprints help profile SSL/TLS clients across destination IPs, ports, and X.509 certificates, and that detection IDs correlate to heuristic detections made on a request. It describes verified bots as allowed bots identified through reverse DNS validation, ASN blocks, public lists, and internal data or machine learning where other methods are unavailable.

## Signals or techniques mentioned

- Per-request bot score
- Verified bot flag
- Verified bot categories
- Signed agents
- Web Bot Auth
- IP validation
- Reverse DNS validation for verified bots
- ASN block checks
- Public bot lists
- Internal data and machine learning for bot verification
- Static-resource detection
- JA3 hash
- JA4 fingerprint
- JavaScript detections
- Detection IDs
- Heuristic detections
- Bot tags
- Bot analytics
- WAF custom rules
- Ruleset Engine fields
- Workers request fields
- Sequence rules
- Bot Detection Alerts
- Machine Learning model update controls
- Bot Feedback Loop
- Account Abuse Protection
- Account takeover detections
- Scraping detections
- Residential proxy detections
- AI crawler blocking
- robots.txt management
- AI Labyrinth honeypot-style crawler trap

## Threat types covered

The documentation is broad product documentation rather than a single threat study.

Directly named or implied threat types include:

- scraping
- credential stuffing
- inventory hoarding
- server-cost inflation
- account abuse
- account takeover
- AI crawler/content scraping
- automated traffic against websites and APIs
- unwanted automated access to static resources
- residential proxy traffic and other automated signals

Relevant OWASP Automated Threat mappings:

- OAT-008 Credential Stuffing
- OAT-011 Scraping
- OAT-019 Account Creation or related account abuse, depending on endpoint
- OAT-020 Denial of Inventory / inventory hoarding
- account-takeover and login-abuse families
- AI crawler/content harvesting as a modern scraper/crawler variant

The docs are useful for mapping vendor concepts to threat categories, but not for estimating prevalence or proving mitigation performance.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates the defender/operator view of bot management at a major edge provider. It is useful for understanding how a large vendor exposes bot risk to customers: scores, rule fields, verified-bot identity, JA3/JA4 fingerprints, JavaScript detection status, detection IDs, analytics, and custom-rule responses.

- **What does it fail to represent?**  
  It does not provide independent validation of Cloudflare’s detection performance. It does not provide raw traffic data, model details, feature weights, ground-truth labelling methods, false-positive rates, false-negative rates, sector-level calibration, or adversarial evaluation against modern evasion stacks. It is a product/control surface description, not an audit.

- **What additional evidence would be needed to go further?**  
  Independent evaluation of Cloudflare Bot Management against labelled traffic; comparison against other anti-bot services; adversarial tests with Playwright, Puppeteer, Selenium, anti-detect browsers, cloud browsers, residential proxies, mobile proxies, TLS spoofing, and AI browser agents; customer-side false-positive studies; abuse-flow-specific studies for login, checkout, scraping, inventory, and account creation; transparent methodology for bot-score calibration.

## What it cannot show

- It cannot show that Cloudflare Bot Management detects bots accurately.
- It cannot show false-positive or false-negative rates.
- It cannot show robustness against modern evasive automation.
- It cannot show that bot scores are calibrated consistently across sectors or endpoints.
- It cannot show which exact features or models drive a given bot score.
- It cannot establish bot prevalence or business impact.
- It cannot replace academic/independent sources such as Iliou et al., FP-Inconsistent, FP-Inspector, or JA4/TLS fingerprinting studies.
- It cannot prove that verified-bot identification is complete or error-free.

## Project impact

- Strong vendor-baseline source for the Open Bot Risk evidence register.
- Useful for defining the “industry control surface” of bot management:
  - score
  - verified bot status
  - detection IDs
  - JavaScript detection result
  - JA3/JA4 fingerprints
  - WAF/custom-rule actions
  - analytics and feedback loops
- Helps connect academic signal families to real product fields:
  - JA4/TLS fingerprinting links to `cf.bot_management.ja4`
  - JavaScript/browser signals link to JavaScript detections
  - heuristic detections link to detection IDs
  - allowed crawler identity links to verified bots and signed agents
- Useful contrast against Netacea:
  - Netacea stresses server-side/no-client-JS and intent analysis in its marketing material.
  - Cloudflare docs expose a broader edge/WAF variable model, including JA3/JA4, JavaScript detections, verified bots, and custom rules.
- Important for modern crawler/agent scope because Cloudflare docs now include signed agents, Web Bot Auth, AI crawler blocking, AI Labyrinth, and robots.txt management.
- Should be cited as vendor documentation for product capabilities and terminology, not as evidence that the product works as claimed.
