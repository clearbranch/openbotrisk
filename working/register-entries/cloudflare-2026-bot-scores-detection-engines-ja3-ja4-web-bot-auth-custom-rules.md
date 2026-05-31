# Cloudflare bot scores, detection engines, JA3/JA4, detection IDs, Web Bot Auth, and custom rules — Cloudflare 2026

## Bibliographic

- **Citation**: Cloudflare. (2026). Cloudflare Bots documentation: Bot scores, JA3/JA4 fingerprint, Detection IDs, Web Bot Auth, and Custom rules. Cloudflare Docs.
- **Source URL or path**:
  - Cloudflare Bots — Bot scores
  - Cloudflare Bots — JA3/JA4 fingerprint
  - Cloudflare Bots — Detection IDs
  - Cloudflare Bots — Web Bot Auth
  - Cloudflare Bots — Custom rules
- **Date accessed**: 2026-06-01
- **Category**: vendor / technical documentation
- **Tags**: Cloudflare, bot-score, bot-detection-engines, machine-learning, heuristics, anomaly-detection, javascript-detections, JA3, JA4, JA4-signals, detection-ids, web-bot-auth, signed-agents, verified-bots, waf-custom-rules, AI-bots, public-data-limits

## What it claims

- Cloudflare Bot Management assigns a bot score from 1 to 99, where low scores indicate likely automation and high scores indicate likely human traffic.
- Scores can be used in WAF custom rules and Workers to block, challenge, allow, skip, log, or route requests differently.
- Cloudflare groups bot scores into operational categories:
  - 0: not computed
  - 1: automated
  - 2–29: likely automated
  - 30–99: likely human
  - verified bot: non-malicious automated traffic
- Bot scores are generated using multiple detection engines, including heuristics, machine learning, anomaly detection, JavaScript detections, and Cloudflare service handling.
- The heuristics engine catches automated traffic through deterministic pattern matching against known malicious fingerprints.
- The machine-learning engine produces most scores from 2 to 99 using request features, session characteristics, and browser signals.
- JavaScript detections identify headless browsers and automation tools through lightweight client-side JavaScript.
- JA3 and JA4 fingerprints identify TLS clients based on how they initiate TLS connections.
- Detection IDs expose static detection rules for predictable bot behaviour with claimed no overlap with human traffic.
- Web Bot Auth uses HTTP message signatures and Ed25519 keys to cryptographically verify declared bot/agent traffic.
- Custom rules allow customers to combine bot-management fields with path, ASN, URI, user-agent, JA3/JA4, detection IDs, and other request fields.

## What evidence it provides

This is vendor documentation, not an independent empirical evaluation.

### Bot scores and detection engines

Cloudflare defines a bot score as a 1–99 score estimating how likely a request came from a bot. A score of 1 means Cloudflare is highly confident the request is automated; a score of 99 means Cloudflare is highly confident the request came from a human.

Cloudflare describes several score sources:

- **Heuristics**: deterministic checks against known malicious fingerprints. High-confidence automated requests receive score 1; some automation under assessment can receive score 29.
- **Machine learning**: supervised ML trained over request features across Cloudflare traffic. The output variable is described as the predicted probability that a client is human, mapped to the 1–99 bot score.
- **Anomaly detection**: unsupervised baseline/outlier detection for a specific site. Cloudflare says this engine is being deprecated and is not onboarding new customers.
- **JavaScript detections**: lightweight client-side JavaScript intended to catch headless browsers and other automation tools.
- **Cloudflare service / not computed**: special cases where Bot Management did not evaluate the request.

The docs also state that the `__cf_bm` cookie is used to smooth bot scores and reduce false positives for real user sessions.

### JA3/JA4 fingerprints

Cloudflare describes JA3 and JA4 as TLS-based identifiers for clients, derived from connection initiation behaviour. JA4 is described as improving on JA3 by sorting ClientHello extensions, reducing fingerprint proliferation for modern browsers and easing grouping.

The JA3/JA4 docs expose JA4 signals such as:

- `h2h3_ratio_1h`
- `heuristic_ratio_1h`
- `reqs_quantile_1h`
- `uas_rank_1h`
- `browser_ratio_1h`
- `paths_rank_1h`
- `reqs_rank_1h`
- `cache_ratio_1h`
- `ips_rank_1h`
- `ips_quantile_1h`

Cloudflare also notes that JA3/JA4 can be missing for non-encrypted HTTP traffic, Worker-routed traffic, internal Cloudflare routing, or requests where Bot Management is skipped.

Use cases listed include blocking/challenging a JA3 fingerprint associated with an attack, skipping/allowing JA3 fingerprints associated with good traffic, and allowing mobile application traffic that produces a stable JA3 fingerprint.

### Detection IDs

Cloudflare defines Detection IDs as static rules for predictable bot behaviour with no overlap with human traffic. Each ID maps to a specific detection method, such as heuristics, verified bot detections, or anomaly detections.

The docs give an example of a detection ID identifying a client that sends headers in an order different from the claimed browser. Detection IDs can be used in:

- Custom rules
- Advanced Rate Limiting
- Transform Rules
- Workers
- Bot Analytics
- Security Analytics
- Logpush HTTP Requests dataset

Cloudflare also notes that one request can trigger multiple Detection IDs, and that detection tags can identify categories such as Go-language bots.

### Web Bot Auth

Cloudflare describes Web Bot Auth as an authentication method using cryptographic signatures in HTTP messages to verify that a request comes from an automated bot. It is used as a verification method for verified bots and signed agents.

The mechanism uses:

- Ed25519 signing keys
- a public key directory hosted at `/.well-known/http-message-signatures-directory`
- JSON Web Key Sets
- HTTP Message Signatures
- `Signature`
- `Signature-Input`
- `Signature-Agent`
- short `expires` values to reduce replay risk

Cloudflare states that nonce validation is not currently backed by a database of seen nonces, and recommends short expiry intervals as replay protection.

### Custom rules

Cloudflare distinguishes built-in bot settings from WAF custom rules. Built-in settings apply across the domain and include features such as:

- Block AI bots
- AI Labyrinth
- Managed robots.txt
- Super Bot Fight Mode categories
- Verified bots
- Static resource protection
- JavaScript detections

Custom rules are needed for:

- path-specific protection
- custom score thresholds
- compound conditions using country, ASN, URI path, JA3/JA4, or user agent
- custom actions such as Log, Interactive Challenge, or Skip
- detection ID targeting
- forwarding bot data to origin via Transform Rules or Snippets

Example patterns include stricter bot handling on `/login`, challenge thresholds below a chosen bot score, and exclusion of particular detection IDs from enforcement.

## Signals or techniques mentioned

- Bot score
- Bot score groups
- Verified bot flag
- Verified bot category
- `__cf_bm` cookie
- Heuristics engine
- Machine-learning engine
- Anomaly detection engine
- JavaScript detections
- Cloudflare service score source
- Request features
- Headers
- Session characteristics
- Browser signals
- Challenge-solving probability as a model target/proxy
- JA3 fingerprint
- JA4 fingerprint
- JA4 signals
- TLS ClientHello behaviour
- JA4 extension sorting
- HTTP/2 and HTTP/3 ratio signals
- heuristic ratio
- request ranks/quantiles
- user-agent ranks
- path ranks
- IP ranks/quantiles
- cache ratio
- Detection IDs
- Detection tags
- Header-order mismatch with claimed browser
- Go-language bot tags
- Logpush `BotDetectionIDs`
- Web Bot Auth
- HTTP Message Signatures
- Ed25519
- JSON Web Key Set
- JWK thumbprint
- `Signature`
- `Signature-Input`
- `Signature-Agent`
- nonce
- expiry window
- WAF custom rules
- Advanced Rate Limiting
- Transform Rules
- Workers
- Bot Analytics
- Security Analytics
- AI Labyrinth
- Block AI Bots
- Managed robots.txt
- Static resource protection

## Threat types covered

The documentation is broad product documentation. Threat types directly or indirectly covered include:

- scraping
- account takeover
- credential stuffing
- login abuse
- automated traffic against sensitive endpoints
- headless-browser automation
- non-compliant AI crawlers
- unwanted AI bot access
- static-resource abuse
- protocol/client fingerprint abuse
- automated clients using misleading User-Agent strings or non-browser header ordering
- declared bot/agent verification through cryptographic identity

Relevant OWASP Automated Threat mappings:

- OAT-008 Credential Stuffing
- OAT-011 Scraping
- OAT-019 Account Creation / account abuse, depending on use case
- OAT-020 Denial of Inventory where endpoint-specific bot controls are used for inventory hoarding
- account-takeover and login-abuse categories
- AI crawler/content-harvesting as a modern scraping/crawler variant

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates the operational control plane that Cloudflare customers use to respond to suspected automation: bot scores, JA3/JA4, JavaScript detections, detection IDs, Web Bot Auth, verified bots, and custom WAF logic. It is particularly useful for understanding how vendor-side bot-detection signals become customer-facing decisions.

- **What does it fail to represent?**  
  It does not provide independent test data, raw traffic labels, false-positive rates, false-negative rates, model features in full, model weights, customer outcomes, or robust adversarial evaluation. The docs describe how Cloudflare says the system works and how customers can act on exposed fields. They do not prove detection quality.

- **What additional evidence would be needed to go further?**  
  Independent evaluation using labelled bot/human traffic; false-positive analysis on real users; adversarial tests with Playwright, Puppeteer, Selenium, anti-detect browsers, TLS spoofing, residential proxies, cloud browsers, mobile automation, and AI browser agents; endpoint-specific evaluation for login, checkout, scraping, account creation, and APIs; comparison with other vendors and public academic detectors.

## What it cannot show

- It cannot show that Cloudflare bot scores are accurate.
- It cannot show calibration of scores across domains, sectors, endpoints, or traffic mixes.
- It cannot show robustness against modern evasion tooling.
- It cannot show that JavaScript detections reliably catch current headless/browser automation.
- It cannot show that JA3/JA4-based rules generalise beyond observed attacks.
- It cannot show that Detection IDs have truly zero human overlap.
- It cannot show that Web Bot Auth adoption is broad enough to solve crawler/agent identity.
- It cannot replace independent evidence such as FP-Inconsistent or academic adversarial studies.

## Project impact

- Strong vendor-control-plane source.
- Useful for explaining how bot detection becomes actionable:
  - scores
  - fields
  - WAF expressions
  - Workers variables
  - custom thresholds
  - endpoint-specific rules
  - detection-ID targeting
- Strong fit with the project’s taxonomy because it joins several signal families:
  - ML score
  - deterministic heuristics
  - JavaScript/client-side detection
  - TLS fingerprints
  - request/sequence analytics
  - verified-bot identity
  - signed-agent identity
- Useful contrast with academic work:
  - Iliou/Acien focus on web logs and behavioural biometrics.
  - Iqbal/Andriamilanto focus on browser fingerprinting.
  - Jarad focuses on JA4/TLS fingerprints.
  - Cloudflare shows how these ideas appear as vendor-exposed operational fields.
- Useful for the modern AI-crawler/agent section because it includes Block AI Bots, AI Labyrinth, managed robots.txt, signed agents, and Web Bot Auth.
- Should be cited carefully as vendor documentation. It supports “Cloudflare exposes/claims/uses X,” not “X works.”
