# Kasada technical writing: Bot Defense, adversarial retooling, AI Agent Trust, and 2026 benchmark report — Kasada 2025–2026

## Bibliographic

- **Citation**: Kasada. (2025–2026). Kasada Bot Defense, AI Agent Trust Management, Adversarial Techniques, and 2026 Benchmark Report: Bots, Fraud, and AI. Kasada.
- **Source URL or path**:
  - https://www.kasada.io/
  - https://www.kasada.io/bot-defense/
  - https://www.kasada.io/ai-agent-trust-management/
  - https://www.kasada.io/adversarial-techniques/
  - https://www.kasada.io/reports/2026-benchmark-report-bots-fraud-and-ai/
- **Date accessed**: 2026-06-01
- **Category**: vendor / technical marketing and adversarial-threat framing
- **Tags**: Kasada, bot-defense, bot-management, dynamic-defenses, invisible-challenges, client-side-sensors, client-validation, proof-of-execution, obfuscation, virtual-machine, adversarial-retooling, solver-services, CAPTCHA-bypass, residential-proxies, headless-browsers, Puppeteer, stealth-plugin, AI-agent-trust, Web-Bot-Auth, agent-governance, fraud, scraping, ATO, checkout-fraud, fake-account-creation, GenAI-abuse, vendor-claims, public-data-limits

## What it claims

- Kasada positions its platform as protection against automated threats, fraud, and AI agents without CAPTCHAs or visual challenges.
- Its technical framing is adversarial: attackers are not just automating websites, they actively study and bypass bot-management products.
- Kasada argues traditional bot-management approaches are vulnerable to retooling because static defences can be reverse engineered, fooled, or bypassed.
- Kasada claims its approach is dynamic, unpredictable, and expensive for attackers to evade.
- The product page describes an architecture based on invisible client-side challenges, server-side detection, client validation, proof of execution, anomaly detection, data analytics, and threat intelligence.
- Kasada claims “hundreds of sophisticated sensors” collect hidden traces of automation in the client.
- Kasada claims dynamic code paths execute inside a highly obfuscated virtual machine, forcing attackers to run code in real browsers or mobile devices and making client signal data harder to fake.
- Kasada frames attacker methods as an economy of retooling, including solver services, headless browsers/device simulators, residential proxies, and CAPTCHA bypass services.
- Kasada AI Agent Trust frames AI agents as neither automatically good nor automatically bad: businesses should decide whether agents get read-only access, write/transaction access, or no access.
- The 2026 benchmark-report landing page claims bad traffic increasingly blends in, AI lowers the barrier to attack, and many traditional detections miss fraud until damage is done.
- These sources are useful for vendor threat framing and product architecture. They are not independent evidence of detection effectiveness.

## What evidence it provides

The evidence is vendor product material, a vendor adversarial-techniques page, and a public report landing page.

### Kasada Bot Defense

Kasada Bot Defense claims a defence-in-depth architecture with several named elements:

- **Invisible signal collection**: hidden client-side traces of automation, intended to detect bots from the first request without interrupting real users or allowing malicious requests to hit backend systems.
- **Client validation**: checking client-provided data for signs of automation and tampering.
- **Data analytics**: using live product data to investigate real-time bypass attempts.
- **Proof of execution**: dynamic code paths executed in a highly obfuscated virtual machine, intended to force execution in real browsers/mobile devices and secure client signal data.
- **Fast anomaly detection**: analytical models over bot interactions, with claimed session-behaviour anomaly identification in less than 2ms.
- **Threat intelligence**: information extracted from botting communities and attack tools, with new invisible sensors added client-side across the customer base.

The Bot Defense page also claims:

- websites, APIs, and apps are covered
- no CAPTCHAs or visual challenges are served to humans
- Kasada ingests more than 1 trillion data points weekly
- more than 2 billion requests are protected daily
- 35% of requests to Kasada are classified as bad bots
- claimed false-positive rate below 0.01% in a customer quote/context
- attackers retool and Kasada updates client-side defences quickly

These are useful for understanding Kasada’s stated product model, but they are vendor claims.

### Adversarial Techniques page

This is probably the most useful Kasada source for the project’s attacker-side taxonomy. The page argues that financially motivated actors share tools and services that make bots look and act like real users.

It identifies several adversarial techniques:

- **Solver services**: services built to bypass bot-management solutions and produce human-like bypass tokens. Kasada gives example pricing of roughly 80¢–$3.50 per 1,000 solves.
- **Headless browsers and device simulators**: customised automation environments, including Puppeteer with stealth plugins, used to appear as legitimate clients and automate human-like behaviour.
- **Residential proxy networks**: traffic routed through legitimate consumer IPs to defeat IP reputation and rate-limiting approaches. Kasada gives example pricing of roughly $50–$500 per month.
- **CAPTCHA bypasses**: AI/ML, human farms, and reverse-engineering services that extract, solve, and replay CAPTCHA challenges. Kasada gives example pricing around 50¢ per 1,000 CAPTCHAs.

The value here is the concrete adversarial-retooling framing. It supports the idea that modern bot defence must consider attack supply chains, solver marketplaces, residential proxies, headless/stealth browsers, and anti-bot-specific bypass tooling.

### AI Agent Trust Management

Kasada’s AI Agent Trust page claims that AI agents break the old assumption that automation should be blocked by default. It argues that some agents represent real customers and may need controlled access, while unknown or malicious automation should be restricted.

The page describes AI-agent governance patterns:

- verified agents allowed read-only access
- unknown scraping blocked at the edge
- trusted aggregators distinguished from unknown bots
- scoped access for search queries versus booking transactions
- trusted AI agents allowed to complete transactions
- malicious bots blocked automatically
- audit logs and reporting for compliance
- permissions by HTTP method
- endpoint-level permissions planned
- classification by verification strength, from cryptographic Web Bot Auth signatures to weaker signals such as user agents and IP ranges
- separate analysis of crawling bots and agentic bots

This is useful for the project’s modern automation taxonomy because it distinguishes:

- known/verified bots
- AI crawlers
- agentic bots
- trusted aggregators
- unknown scrapers
- transaction-capable agents
- spoofable identity signals

### 2026 Benchmark Report landing page

The report landing page frames the problem as bad traffic that blends in, skews metrics, and causes downstream business decisions to be based on bad signals.

The public page claims:

- bad traffic often mimics real users and runs quietly until damage is done
- AI has made attacks faster and cheaper
- companies hit by bot attacks report losing an average of 45% of revenue
- stolen account sales generated $151M on criminal marketplaces last year
- 219% increase in bad bots
- 79% of AI traffic comes from crawlers and scrapers
- the report contains benchmarks across retail, airlines, digital, hospitality, finance, and streaming

The public landing page does not expose enough methodology to treat these as neutral prevalence estimates. It is useful as vendor trend framing only unless the full report is available and methodologically assessable.

## Signals or techniques mentioned

- Invisible client-side challenges
- Client-side sensors
- Hidden traces of automation
- Server-side detection
- Client validation
- Tamper detection
- Proof of execution
- Dynamic code paths
- Obfuscated virtual machine
- Real browser/mobile device execution
- Fast anomaly detection
- Analytical models
- Live data analytics
- Threat intelligence from botting communities
- Dynamic defence updates
- Obfuscation
- Anti-reverse-engineering
- Solver services
- Human bypass tokens
- Headless browsers
- Device simulators
- Puppeteer
- Puppeteer Extra Stealth plugin
- Human-like automation
- Residential proxy networks
- Consumer IP exit nodes
- CAPTCHA bypass services
- AI/ML CAPTCHA solving
- Human farms
- CAPTCHA reverse engineering
- AI Agent Trust
- Agent verification strength
- Web Bot Auth signatures
- User-agent and IP-range identity signals
- HTTP-method permissions
- Read-only vs write/transaction access
- Agentic bot/crawler distinction
- Edge blocking
- Audit logs
- Report/export of AI bot traffic

## Threat types covered

Directly covered or named in Kasada navigation/product material:

- Account takeover
- API abuse
- Checkout fraud
- Content scraping
- Fake account creation
- GenAI abuse
- Agentic AI abuse
- Scraping and crawling
- Fraudulent booking or inventory queries
- Flight/travel API abuse
- Pricing/inventory scraping
- CAPTCHA bypass
- Solver-service-assisted botting
- Residential-proxy-assisted abuse
- Headless-browser automation
- Checkout and booking transaction abuse
- Bad traffic distorting analytics/metrics

Relevant OWASP Automated Threat mappings:

- OAT-008 Credential Stuffing / ATO-adjacent login abuse
- OAT-011 Scraping
- OAT-019 Account Creation / fake account creation
- OAT-020 Denial of Inventory / inventory hoarding and travel/retail booking abuse
- automated CAPTCHA bypass and solver workflows as cross-cutting evasion
- API automation and business-logic abuse
- AI-agent/crawler abuse as a modern cross-cutting category

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates the adversarial vendor view of bot management: attackers adapt to defences, buy solver services, use headless/stealth browsers, route through residential proxies, bypass CAPTCHAs, and increasingly use AI/agentic automation. This is highly relevant to the project taxonomy because it explains why “basic HTTP scripts versus browser automation” is too simple for the modern threat surface.

- **What does it fail to represent?**  
  It does not provide independent detection performance, raw data, formal evaluation, false-positive/false-negative rates, reproducible experiments, or third-party audit evidence. The architecture descriptions are product claims. The benchmark-report public page gives headline numbers without enough methodology to judge sampling, measurement, labels, thresholds, or representativeness. The adversarial-pricing examples are useful but should be treated as vendor threat-intelligence claims unless corroborated.

- **What additional evidence would be needed to go further?**  
  Independent testing of Kasada against labelled production bot traffic; adversarial tests using Puppeteer, Playwright, Selenium, stealth plugins, anti-detect browsers, real-browser automation, residential/mobile proxies, CAPTCHA solvers, cloud browsers, and AI agents; evidence of attacker retooling before/after Kasada changes; public methodology for benchmark figures; comparison with Cloudflare, DataDome, HUMAN/PerimeterX, Netacea, Akamai, Imperva, and open academic baselines; customer-side false-positive studies.

## What it cannot show

- It cannot prove Kasada’s bot detection accuracy.
- It cannot verify claims about false-positive or false-negative rates.
- It cannot prove that proof-of-execution or obfuscated virtual-machine challenges are robust against all retooling.
- It cannot show how modern Playwright/Puppeteer/Selenium/anti-detect systems perform against Kasada.
- It cannot show that the 2026 benchmark numbers are representative without the full methodology.
- It cannot establish general bot prevalence or revenue loss independently.
- It cannot replace academic sources such as Iliou et al., Acien et al., FP-Inconsistent, FP-Inspector, or TLS/JA4 studies.

## Project impact

- Strong vendor/adversarial-framing source.
- Better than generic product marketing because it gives concrete attacker-side categories:
  - solver services
  - headless browsers/device simulators
  - Puppeteer stealth tooling
  - residential proxies
  - CAPTCHA bypass services
  - AI agents and transaction-capable automation
- Useful for strengthening the project taxonomy:
  - HTTP scripts
  - browser automation
  - stealth plugins / anti-detect browsers
  - residential proxy infrastructure
  - CAPTCHA-solving supply chains
  - dynamic challenge bypass
  - AI agents and verified-agent governance
- Good contrast with other vendors:
  - Cloudflare exposes bot scores, JA3/JA4, Detection IDs, WAF fields, and Web Bot Auth.
  - DataDome stresses intent-based AI detection and collective threat intelligence.
  - HUMAN stresses cyberfraud journey, browser automation, agentic activity, and investigation workflows.
  - Kasada stresses adversarial economics, dynamic client-side defences, proof-of-execution, and raising attacker cost.
- Use as vendor threat-intelligence and product-architecture evidence, not independent proof.
