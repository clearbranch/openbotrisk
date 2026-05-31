# HUMAN / PerimeterX material: Sightline Cyberfraud Defense, bot mitigation, AI-agent detection, and OpenClaw — HUMAN Security 2026

## Bibliographic

- **Citation**: HUMAN Security. (2026). HUMAN Sightline Cyberfraud Defense, Bot Detection and Mitigation, AI Agent Detection, OpenClaw analysis, and 2026 State of AI Traffic & Cyberthreat Benchmark Report. HUMAN Security.
- **Source URL or path**:
  - https://www.humansecurity.com/applications/cyberfraud-defense/
  - https://www.humansecurity.com/platform/solutions/bot-detection-mitigation/
  - https://www.humansecurity.com/learn/blog/ai-agent-signals-traffic-detection/
  - https://www.humansecurity.com/learn/blog/openclaw-ai-agent-abuse/
  - https://www.humansecurity.com/learn/blog/ai-traffic-growth-2025-key-findings/
- **Date accessed**: 2026-06-01
- **Category**: vendor / technical marketing and threat-intelligence blog
- **Tags**: HUMAN, PerimeterX, bot-management, bot-mitigation, Sightline, Satori, AgenticTrust, AI-agents, agentic-browsers, OpenClaw, Playwright, Puppeteer, Selenium, browser-automation, scraping, account-takeover, fake-accounts, carding, scalping, transaction-abuse, content-scraping, LLM-scraping, behavioural-analysis, intelligent-fingerprinting, vendor-claims, public-data-limits

## What it claims

- HUMAN positions its current application-security platform around cyberfraud defense across humans, bots, and AI agents.
- The product framing has moved beyond classic “bot vs human” classification toward full-lifecycle fraud management, customer-journey analysis, AI-agent governance, and intent/impact-aware decisioning.
- HUMAN claims Sightline Cyberfraud Defense uses advanced machine learning, behavioural analysis, and intelligent fingerprinting against malicious bots, human-led fraud, and agentic risks.
- HUMAN claims its platform manages good and bad bots, real and fraudulent human traffic, AI agents, LLM scrapers, and known crawlers across web, mobile, and APIs.
- HUMAN’s bot-mitigation page explicitly names account takeover, scraping, fake accounts, carding, and scalping as malicious bot attack categories.
- HUMAN claims autonomous AI agents are detectable using updated versions of existing anti-bot techniques rather than entirely novel methods.
- HUMAN’s AI-agent blog claims agents commonly use familiar automation strategies: automation libraries, simulated mouse movements, sandboxed browser environments, and spoofing/evasion tactics.
- HUMAN claims their research found AI agents relying on Selenium, Playwright, and Puppeteer, with Playwright most common.
- HUMAN’s OpenClaw blog claims autonomous agent gateways can produce routine automation, suspicious abuse, synthetic referral traffic, active reconnaissance, and WordPress directory/file brute forcing.
- HUMAN’s benchmark-report blog claims AI-driven traffic nearly tripled in 2025, autonomous agent traffic grew strongly, and agentic activity has reached checkout/account-management contexts.
- These sources are useful vendor/threat-intelligence material, but they are not independent proof of product effectiveness.

## What evidence it provides

The evidence is a combination of product pages, vendor threat-intelligence blogs, and a public blog summarising a larger benchmark report.

### HUMAN Sightline Cyberfraud Defense

The Sightline page frames the product as protection against fraud by bots, humans, and AI agents across the customer journey. It claims use of:

- advanced machine learning
- behavioural analysis
- intelligent fingerprinting
- multi-method detection
- custom mitigation
- investigation tools
- adaptive learning and feedback
- session correlation across authentication stages
- AI-generated investigation insights
- first-party data feedback into fraud models

The page’s stated use cases include:

- account takeover
- agentic AI
- compromised accounts
- data contamination
- fake accounts
- scraping
- transaction abuse

This is useful for mapping HUMAN’s product concepts, but it is still product marketing.

### Bot Detection and Mitigation

The bot mitigation page says HUMAN detects and mitigates malicious bot attacks including:

- account takeover
- scraping
- fake accounts
- carding
- scalping

It also claims visibility/control over known bots, crawlers, and AI. It frames key capabilities as:

- detecting sophisticated bots
- responding with hard blocks and soft mitigations
- monitoring known bots and AI traffic
- allowing, denying, monetising, suppressing ads, or showing alternate content
- investigating bot attack paths, changing behaviours, attacker actions, and intent

This supports a useful operational taxonomy: bot management is not just blocking, but deciding whether to allow, deny, monetise, challenge, suppress, or alter content depending on traffic category and business impact.

### AI Agent Detection blog

The AI Agent Detection blog is one of the more useful technical pieces. It says HUMAN generated real sessions through AI services, examined behaviour in controlled environments, translated findings into structured detection signals, and correlated them across two data sources.

It argues that AI agents generally reuse known automation techniques, including:

- automation libraries
- simulated mouse movements
- sandboxed browser environments
- long-standing evasion or spoofing tactics

The blog lists key signal categories for differentiating human and AI-generated traffic:

- **Network context**: IP origin, stability, and routing patterns over time
- **Browser authenticity**: consistency between claimed browser version and actual execution behaviour
- **Execution environment**: automation artifacts, injected scripts, helper components, sandboxed/headless/tool-assisted environments
- **Interaction behaviour**: timing, variability, and continuity of user inputs
- **Session evolution**: how signals change as the session progresses

The blog also says automation libraries can simulate mouse movement, clicks, typing, page-element interaction, browser version, OS, screen resolution, and geolocation, but that modern anti-bot tools use detection methods against framework-powered sessions.

This is useful because it aligns well with the project taxonomy: HTTP scripts, browser automation, stealth/anti-detect, cloud/browser environments, and AI agents.

### OpenClaw blog

The OpenClaw blog describes publicly exposed OpenClaw gateways and claims HUMAN observed activity ranging from routine automation to suspicious abuse.

Reported abuse-like patterns include:

- browser automation controlled by OpenClaw
- high-frequency segmented request activity
- synthetic referral traffic using social-media UTM parameters
- repeated article access from small IP sets
- active reconnaissance
- directory/file brute forcing against common WordPress paths
- possible lowering of the barrier to internet fraud

The source is valuable for the “AI agents as operational actors” part of the project. It is less strong as formal evidence because it is a vendor blog with selected examples rather than a full dataset/methodology paper.

### 2026 State of AI Traffic & Cyberthreat Benchmark blog

The benchmark-summary blog claims:

- automated/AI traffic is growing faster than human traffic
- AI-driven traffic grew 187% from January to December 2025
- AI-driven traffic peaked at 3.61x January levels in October 2025
- more than 95% of AI-driven traffic was concentrated in retail/e-commerce, streaming/media, and travel/hospitality
- OpenAI-associated bots made up around 69% of observed AI-driven traffic by volume in their dataset
- autonomous agent traffic grew 7,851% year over year
- 2.3% of agentic activity occurred on checkout pages
- median scraping-attempt traffic is approaching 20% globally
- post-login account-compromise attempts more than quadrupled year over year
- carding volume has increased 250% since 2022

These are potentially useful trend claims, but they are vendor-measured and require full methodology before being treated as neutral prevalence evidence.

## Signals or techniques mentioned

- Machine learning
- Behavioural analysis
- Intelligent fingerprinting
- Multi-method detection
- Layered AI models
- Session correlation across authentication stages
- First-party data feedback
- Contextualized events
- Custom fraud models
- Threat-network investigation
- Pattern analysis
- AI-generated investigation insights
- Hard blocks
- Soft mitigations
- Silent controls
- Investigation triggers
- Known-bot monitoring
- AI-agent governance
- AgenticTrust
- Agentic Visibility
- LLM scraper/crawler control
- Browser automation
- Selenium
- Playwright
- Puppeteer
- Simulated mouse movements
- Sandboxed browser environments
- Headless/tool-assisted environments
- Automation artifacts
- Injected scripts
- Helper components
- Network context
- IP origin
- Routing patterns
- Browser authenticity
- Claimed browser vs execution behaviour consistency
- Interaction timing and variability
- Session evolution
- Referral-signal manipulation
- UTM parameter abuse
- Directory/file brute forcing
- WordPress path reconnaissance
- AI browser agents
- Autonomous checkout/account-management activity

## Threat types covered

Directly covered:

- Account takeover
- Compromised accounts
- Fake accounts
- Scraping
- LLM/content scraping
- Transaction abuse
- Carding
- Scalping
- Bot detection and mitigation
- Known crawler/AI traffic governance
- Agentic commerce abuse
- Data contamination
- Synthetic referral traffic
- Active reconnaissance
- Directory/file brute forcing
- Client-side supply-chain risk, through separate HUMAN product framing
- Ad fraud/click fraud in the wider HUMAN platform

Relevant OWASP Automated Threat mappings:

- OAT-008 Credential Stuffing
- OAT-011 Scraping
- OAT-019 Account Creation / fake account creation
- OAT-020 Denial of Inventory / scalping
- account takeover and post-login abuse categories
- carding/payment abuse
- automated reconnaissance/scanning
- AI-agent traffic as a modern cross-cutting automation category

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates the current commercial bot-management and cyberfraud framing after the PerimeterX/HUMAN transition: full customer journey, bot/human/AI-agent distinction, fraud workflows, AI-agent governance, and business-impact-aware response. It is particularly useful for your taxonomy because it explicitly bridges classic browser automation with newer autonomous AI agents.

- **What does it fail to represent?**  
  It does not provide independent performance evaluation. The product pages do not expose model details, feature weights, raw data, false-positive rates, false-negative rates, ground-truth labels, or adversarial test design. The OpenClaw and AI-agent blogs are useful threat-intelligence examples, but not formal academic studies. The benchmark-summary blog gives strong headline numbers but not enough public methodology in the blog itself to treat them as neutral prevalence estimates.

- **What additional evidence would be needed to go further?**  
  Independent evaluations of HUMAN/PerimeterX against labelled production traffic; customer-side false-positive studies; technical papers with reproducible methodology; controlled adversarial tests using Selenium, Playwright, Puppeteer, anti-detect browsers, cloud browsers, residential/mobile proxies, TLS spoofing, CAPTCHA solving, and AI browser agents; detailed methodology for AI-agent traffic measurement; comparison with Cloudflare, DataDome, Akamai, Imperva, Netacea, and open academic baselines.

## What it cannot show

- It cannot prove HUMAN’s detection accuracy.
- It cannot independently verify claimed product performance or customer outcomes.
- It cannot prove robustness against advanced evasive automation.
- It cannot establish global AI-agent or bot prevalence without full report methodology.
- It cannot show which individual signals are decisive in production.
- It cannot show whether similar results hold outside HUMAN’s customer/network view.
- It cannot distinguish cleanly between user-driven browser automation and autonomous-agent execution in all cases.
- It cannot replace independent empirical studies such as FP-Inconsistent, FP-Inspector, Iliou et al., Acien et al., or JA4/TLS fingerprinting papers.

## Project impact

- Strong source family for modern vendor framing.
- Better than generic vendor brochures because it contains concrete modern concepts:
  - agentic AI
  - agentic browsers
  - full-stack browser automation
  - Playwright/Selenium/Puppeteer reuse
  - browser authenticity
  - session evolution
  - intent/impact-based governance
  - synthetic referral traffic
  - autonomous reconnaissance
- Useful contrast with Cloudflare and DataDome:
  - Cloudflare exposes operational rule fields such as bot score, JA3/JA4, detection IDs, and Web Bot Auth.
  - DataDome stresses intent-based detection, collective intelligence, and model-heavy product framing.
  - HUMAN stresses customer-journey cyberfraud, agentic visibility, behavioural/fingerprint decisioning, and investigation/governance workflows.
- Strong fit for a section on how the taxonomy should evolve:
  - HTTP scripts and scrapers
  - browser automation
  - stealth/anti-detect
  - cloud/browser environments
  - AI agents and agentic browsers
  - trusted vs untrusted automation
  - intent and business impact
- Should be cited as vendor/threat-intelligence evidence, not independent validation.
