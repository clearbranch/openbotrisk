# DataDome technical blogs and reports: Bot Protect, AI Detection Engine, and Global Bot Security Report — DataDome 2025–2026

## Bibliographic

- **Citation**: DataDome. (2025–2026). DataDome Bot Protect, AI Detection Engine, and 2025 Global Bot Security Report. DataDome.
- **Source URL or path**:
  - https://datadome.co/products/bot-protection/
  - https://datadome.co/ai-detection-engine/
  - https://datadome.co/resources/bot-security-report/
- **Date accessed**: 2026-06-01
- **Category**: vendor / technical marketing and report
- **Tags**: DataDome, bot-management, AI-detection, bot-protection, intent-based-detection, bot-security-report, AI-agents, LLM-crawlers, web-scraping, account-takeover, credential-stuffing, scalping, carding, L7-DDoS, browser-fingerprinting, behavioural-analysis, vendor-claims, public-data-limits

## What it claims

- DataDome positions itself as a cyberfraud and bot-management platform for websites, mobile apps, APIs, and AI/agentic traffic.
- DataDome’s public framing has shifted from generic bot blocking toward “intent-based” traffic control for humans, bots, and AI agents.
- Bot Protect claims to analyze every request rather than sampled traffic, using client-side and server-side signals to assess risk across the user journey.
- DataDome claims its detection engine uses many AI/ML models, collective threat intelligence, signature-based detection, behavioural analysis, time-series modelling, proxy intelligence, and intent recognition.
- DataDome claims to distinguish human users, trusted AI agents/good automation, and malicious bots.
- DataDome claims edge-based low-latency detection and response.
- The 2025 Global Bot Security Report claims that nearly 17,000 websites across 22 industries were tested for exposure to unwanted bots, agentic AI, and LLM crawlers.
- The report page claims only 2.8% of tested websites were fully protected in 2025, down from 8.4% in 2024.
- The report page claims over 61% of tested domains failed every bot test, including basic scripted bots.
- The report page claims LLM crawler traffic grew strongly in 2025, with AI crawlers making up 10.1% of verified bot traffic in August 2025.
- These sources are vendor claims and vendor measurements; they are useful for product framing and threat-surface context, not independent proof of detection performance.

## What evidence it provides

The evidence comes from DataDome’s own public product pages and report pages.

### Bot Protect

DataDome Bot Protect is presented as a real-time bot mitigation product for websites, apps, APIs, and MCP servers. The page names use cases including:

- content and LLM scraping
- account takeover prevention
- credential stuffing
- brute-force attacks
- scalping and inventory hoarding
- carding and payment fraud
- Layer 7 DDoS
- good bot management and agentic commerce

The product page claims that Bot Protect:

- analyzes every request, including page visits, logins, and cart requests
- evaluates hundreds of client-side and server-side signals
- processes over 5 trillion signals daily
- uses 1000+ out-of-the-box and customer-specific models
- uses collective threat intelligence
- distinguishes between human users, trusted AI agents, and malicious bots
- has automated mitigation aligned with business flow
- runs at the edge across 35+ global points of presence
- operates in under 2 milliseconds
- maintains a claimed false-positive rate below 0.01%

These are useful for understanding DataDome’s public product model, but they should be treated as non-independent vendor claims unless backed by independent evidence.

### AI Detection Engine

DataDome’s AI Detection Engine page claims:

- real-time AI detection at the edge
- intent-based detection, not just human/bot classification
- processing of 5 trillion signals daily
- thousands of AI models across customers and industries
- in-house models built by DataDome threat researchers
- supervised and unsupervised learning
- signature-based detection
- behavioural analysis and time-series modelling
- AI-powered intent recognition
- continuous adaptation and threat intelligence
- customer/use-case tailored models
- use of CatBoost, genetic algorithms, fuzzy logic, statistical modelling, data mining, and contrast-set mining

The page frames the detection stack as multi-layered and adaptive. The main value for the evidence register is the taxonomy of vendor signal families:

- signatures/fingerprints
- traffic patterns
- behavioural anomalies
- time-series behaviour
- proxy intelligence
- intent modelling
- customer-specific models
- collective intelligence

### 2025 Global Bot Security Report

The public report page says DataDome tested nearly 17,000 websites across 22 industries against unwanted bots, agentic AI, and LLM crawlers.

The report page claims:

- only 2.8% of tested websites were fully protected in 2025
- this was down from 8.4% in 2024
- more than 61% of tested domains failed every bot test
- LLM crawlers were 10.1% of verified bot traffic in August 2025
- this represented a 3.9x increase from January 2025
- industry protection varied, with travel/hospitality higher than many sectors and technology/software, media/publishing, ticketing/entertainment, and financial services showing low full-protection rates in the public preview

The report page also lists common bot attacks as scraping, account takeover, payment fraud, DDoS attacks, and AI fraud.

This is useful as vendor measurement evidence of exposure and sector framing. It is weaker than an academic study because the page does not provide full methodology, sampling details, detection thresholds, ground truth, raw results, or independent validation in the public preview.

## Signals or techniques mentioned

- Client-side signals
- Server-side signals
- Request-level analysis
- Continuous risk assessment
- User-journey analysis
- Behavioural analysis
- Time-series modelling
- Signature-based detection
- Fingerprints
- Traffic patterns
- Behavioural anomalies
- Proxy intelligence
- Intent recognition
- AI-powered intent modelling
- Supervised learning
- Unsupervised learning
- CatBoost
- Genetic algorithms
- Fuzzy logic
- Statistical modelling
- Data mining
- Contrast-set mining
- Collective threat intelligence
- Customer-specific models
- Out-of-the-box models
- Edge decisioning
- Automated mitigation
- False-positive reduction
- Trusted agent / Agent Trust framing
- LLM crawler detection
- AI crawler trends
- Vulnerability scanning / external bot-exposure testing

## Threat types covered

Directly covered:

- Web scraping
- LLM scraping
- AI crawler access
- Account takeover
- Credential stuffing
- Brute-force login attacks
- Fake account creation
- Account farming
- Carding
- Payment fraud
- Scalping
- Inventory hoarding
- Layer 7 DDoS
- Click fraud / ad fraud
- Influence fraud
- Agentic commerce abuse
- AI-operated accounts
- Unwanted AI agents

Relevant OWASP Automated Threat mappings:

- OAT-008 Credential Stuffing
- OAT-011 Scraping
- OAT-019 Account Creation / account abuse
- OAT-020 Denial of Inventory / scalping
- OAT-001 Account Aggregation or account abuse where relevant
- OAT-014 Vulnerability Scanning where automated reconnaissance is involved
- payment/carding abuse and ATO categories adjacent to OWASP automated threats

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates the commercial bot-management framing used by a major vendor: bot attacks are not just “bot vs human”, but intent, endpoint, user journey, account state, traffic pattern, agent identity, and business outcome. This is valuable for the project because it connects technical signals to concrete abuse categories such as ATO, scraping, scalping, carding, and AI-crawler access.

- **What does it fail to represent?**  
  It does not provide independent detection performance. The headline claims about detection accuracy, false positives, signal volume, number of models, latency, and site vulnerability are vendor-reported. The public report page does not expose enough methodology to verify sampling, test design, bot profiles, thresholding, false-positive handling, or industry representativeness. It does not show how DataDome performs against purchased evasive bot traffic except indirectly through the separate FP-Inconsistent academic paper, where DataDome is one of the tested services.

- **What additional evidence would be needed to go further?**  
  Independent reproduction of the Global Bot Security Report tests; publication of test bot profiles and scoring criteria; raw or aggregated results by attack class; customer-side false-positive studies; adversarial evaluation with Playwright, Puppeteer, Selenium, anti-detect browsers, residential proxies, TLS spoofing, mobile automation, cloud browsers, AI agents, and LLM crawlers; comparison with Cloudflare, Akamai, Imperva, HUMAN, and open-source baselines; endpoint-specific tests for login, checkout, account creation, APIs, and scraping.

## What it cannot show

- It cannot independently prove DataDome’s detection accuracy.
- It cannot verify the claimed false-positive rate.
- It cannot prove that DataDome blocks modern evasive bots at production scale.
- It cannot show how models are trained, validated, or calibrated.
- It cannot prove that “intent” is reliably inferred rather than inferred from correlated signals.
- It cannot establish global bot prevalence without independent sampling and methodology.
- It cannot show whether tested websites were representative of the wider web.
- It cannot replace academic evidence such as FP-Inconsistent, Iliou et al., Acien et al., FP-Inspector, or TLS/JA4 studies.

## Project impact

- Strong vendor-framing source.
- Useful for the project’s “industry framing” and “commercial control plane” sections.
- Good contrast with Cloudflare:
  - Cloudflare docs expose rule fields, bot scores, JA3/JA4, Detection IDs, JavaScript detections, and Web Bot Auth.
  - DataDome stresses intent-based decisioning, collective intelligence, many models, behavioural/time-series modelling, proxy intelligence, and agent trust.
- Useful for modernising the taxonomy beyond simple HTTP scripts and browser automation:
  - AI agents
  - LLM crawlers
  - trusted vs untrusted automation
  - agentic commerce
  - intent-aware bot management
- Should be cited as vendor evidence and product framing, not as independent proof.
- Best paired with FP-Inconsistent because that paper provides external empirical evidence involving DataDome, while DataDome’s own pages explain the vendor’s public claims and terminology.
