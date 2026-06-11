# 2026 Thales Bad Bot Report — Bad Bots in the Agentic Age

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: full text
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Thales / Imperva. (2026). *2026 Thales Bad Bot Report: Bad Bots in the Agentic Age*. Thales Cybersecurity Products / Imperva. April 2026. URL verified: https://cpl.thalesgroup.com/bad-bot-report redirects to https://www.imperva.com/resources/resource-library/reports/2026-bad-bot-report/
- **Source URL or path**: `SRC-039-thales-2026-bad-bot-report.pdf`; public landing page: https://cpl.thalesgroup.com/bad-bot-report
- **Date accessed**: 2026-06-06
- **Category**: vendor
- **Evidence basis**: empirical-operational — vendor report based on Thales / Imperva bot mitigation telemetry, blocked requests, Threat Research observations, Security Analyst Services observations, and two anonymised mitigation case studies. Vendor product recommendations and product capability statements inside the report are vendor claims rather than independent evidence.
- **Operational proximity**: observed — the report describes activity observed and mitigated in production customer environments, but the observation is vendor-measured and the underlying dataset, sampling frame, classifier definitions, false-positive rates, and customer mix are not independently auditable from the report.
- **Tags**: vendor, telemetry, observed-use, bot-management, ai-agent, ai-crawler, ai-fetcher, api-abuse, account-takeover, credential-stuffing, business-logic-abuse, scraping, scalping, denial-of-inventory, sms-pumping, browser-impersonation, fingerprinting, behavioural, session-consistency, residential-proxy, mobile-proxy, captcha, headless-browser, browser-automation, puppeteer, selenium, playwright, financial-services, retail, travel

## What it claims

- The report says its 13th annual edition analyses full-year 2025 bot activity using data and insights from Thales Threat Research and Security Analyst Services teams, who investigate and mitigate bot attacks across industries.
- It claims AI-driven automation is becoming embedded in internet traffic rather than remaining an emerging or exceptional category.
- It claims AI agents are emerging as a third category of automated traffic alongside traditional good bots and bad bots, because they access websites, retrieve data, and perform tasks on behalf of users through browsers, search platforms, enterprise tools, applications, and APIs.
- It claims the distinction between legitimate and malicious automation is becoming blurred because both operate through similar channels, workflows, and infrastructure.
- It claims current visibility into AI-driven traffic is limited to detectable or declared AI clients, leaving a larger unverified portion of AI-driven automation outside the report's observable base.
- It claims bots accounted for 53% of observed web traffic in 2025: 40% bad bots, 13% benign automation, and 47% human traffic.
- It claims Thales blocked 17.2 trillion bot requests in 2025.
- It claims AI-enabled bot attacks increased 12.5x year over year, with average daily blocked AI-driven bot attacks rising from 2 million to 25 million in 2025. The source footnotes that AI bot coverage expanded in 2025.
- It claims 21% of all mitigated attacks aligned with OWASP automated threat categories, while 68% aligned with OWASP WAF/API and 11% with DDoS.
- It claims the most common attack types in its data were general automation (29%), API violation (24%), business logic abuse (21%), path traversal/LFI (9%), data leakage (5%), RCE/RFI (4%), XSS (4%), SQLi, protocol manipulation, and other.
- It claims advanced and moderate bot attacks together accounted for 58% of bot attacks in 2025, with advanced attacks at 44% and moderate attacks at 14%.
- It claims simple bot attacks remained common at 42% of all attacks, and that the volume of simple bot attacks increased by more than 230% compared with 2024.
- It claims AI is not creating entirely new attack categories but is accelerating and refining existing forms of automation, including reconnaissance, data gathering, CAPTCHA solving, interaction timing, fingerprint evasion, and persistence.
- It claims detectable AI traffic in 2025 was composed mainly of AI crawlers (85%) and AI fetchers (15%).
- It claims more than 10% of AI fetcher sessions and nearly 9% of AI crawler sessions triggered bad-bot detection rules; it also says 11.9% of AI crawler traffic and 7% of AI fetcher traffic were blocked by customer-defined rules.
- It claims organisations are beginning to define policy for AI agents, including customer-defined blocking of AI crawlers and different treatment of public content versus authentication, transactional, and data-rich endpoints.
- It claims verified AI bots using cryptographically signed headers are emerging as a way for organisations to authenticate, measure, govern, rate-limit, or potentially monetise AI-driven access.
- It claims APIs are a primary target: 27% of bot attacks were directed at API endpoints in 2025.
- It claims Security Analyst Services teams observed API-first malicious campaigns where bots bypassed user interfaces and interacted directly with backend services using well-formed, often authenticated requests.
- It claims API abuse is difficult because requests may be valid, authentication may succeed, and workflows may be followed correctly; the harmful element is scale, persistence, and intent rather than malformed traffic.
- It claims the most common threats targeting APIs in its traffic were data leakage (26%), business logic abuse (13%), and RCE/RFI (13%).
- It claims account takeover remained a persistent damaging form of automated abuse in 2025, with bots exploiting credential reuse and API-driven identity workflows despite widespread use of MFA.
- It claims account takeover attacks increased by 70% when comparing July 2024 with July 2025, while also saying the May-July 2025 surge could be attributed to increased use of AI tools and agents.
- It claims, based on analyst and threat-research observations, that prevalent 2025 evasion tactics included AI-assisted adaptation, CAPTCHA solving at scale, privacy tools, adaptive polymorphic behaviour, fingerprint and identity evasion, API-first execution, residential/mobile proxy masking, headless/browser-automation frameworks, bots-as-a-service platforms, and multi-threaded persistent attack models.
- It claims bad bots frequently impersonate legitimate web or mobile browsers. In 2025, 41% of bad bot traffic declared itself as Chrome and 17% as Android Browser.
- It claims Financial Services was the top targeted industry by bot attack volume, accounting for 24% of all bot attacks, and the top target for account takeover, accounting for 46% of account takeover incidents.
- It claims Retail and Travel were the leading targets for business logic abuse, with Retail at 24% and Travel at 17% of business-logic attacks.
- It claims travel and airline APIs were targeted by high-frequency queries to search, pricing, availability, fare, seat, and route APIs; it describes fetch-style automation, look-to-book inflation, demand-signal distortion, seat spinning, and denial-of-inventory.
- It claims retail organisations experienced high-frequency API polling of availability, pricing, and promotions, plus inventory denial tactics where bots add items to carts without completing purchases.
- It describes an anonymised financial-services mitigation case where automated login traffic targeted authentication APIs before bot protection controls were configured, and where later mitigation used account takeover protection, custom rules, and advanced bot protection.
- It describes an anonymised insurance mitigation case where bots repeatedly triggered SMS OTP requests through authentication APIs, generating about $300,000 in SMS charges over a 20-day period.
- It recommends treating bot mitigation as governance of automation rather than only blocking attacks, with controls over AI agents, APIs, identity systems, business logic, behavioural analysis, session consistency, persistent automation, surface-wide visibility, and human analyst oversight.

## What evidence it provides

- The source's main empirical basis is vendor operational telemetry and analyst observation. It states that the report combines full-year 2025 bot activity with insights from Thales Threat Research and Security Analyst Services teams.
- It reports large-scale quantitative telemetry, including 17.2 trillion blocked bot requests in 2025, traffic composition percentages, attack-type distributions, AI-bot distributions, industry/country breakdowns, API attack breakdowns, account takeover trends, and browser impersonation percentages.
- It provides time-series or year-on-year comparisons for bot traffic shares, simple bot volume, bad-bot share, AI-enabled bot attacks, browser impersonation, and account takeover attacks.
- It provides selected distributions from detectable AI traffic, including the AI crawler/fetcher split and the share triggering bad-bot, customer-defined, DDoS, SQLi, XSS/IRA, and backdoor/RFI rules.
- It provides source/client distribution examples for AI crawler and AI fetcher traffic over a seven-day sample view, but the sample period, sites, population, and inclusion criteria are not stated.
- It provides two anonymised operational case studies: one financial-services account-takeover mitigation and one insurance SMS-pumping mitigation. These are useful observed-use examples but vendor-selected and not independently verifiable.
- It supports the API-first abuse claim through its own bot mitigation activity and Security Analyst Services observations. It does not publish raw request data, classifier logic, or validation metrics.
- It supports evasion-tactic claims with analyst and Threat Research observations. It does not quantify the prevalence of every tactic listed, nor does it provide enough detail for independent replication.
- It references OWASP automated threats, OWASP API Top Ten-style categories, OWASP LLM Top 10, and the Postman 2025 State of the API Report. The report does not provide full bibliographic references for these inside the extracted PDF; treat them as mentioned supporting references, not independently extracted evidence in this entry.
- The evidence is strongest where the report reports direct Thales/Imperva-observed telemetry and weakest where it moves into product recommendations, future predictions, or causal claims about AI enabling observed changes.

## Signals or techniques mentioned

- Traffic-level categories: bad bot, good bot, human, detectable AI traffic, undeclared/unverified AI traffic.
- AI automation categories: AI agents, AI crawlers, AI fetchers, declared/detectable AI clients, self-hosted or modified LLM-driven automation.
- Attack measurements: blocked bot requests, mitigated attacks, OWASP automated-threat alignment, WAF/API alignment, DDoS alignment, country/industry shares, attack sophistication classes.
- API signals and contexts: API endpoint targeting, backend service interaction, well-formed authenticated requests, authentication APIs, search APIs, booking APIs, pricing APIs, payment APIs, availability APIs, OTP-generation APIs, data-rich endpoints.
- Business-logic contexts: login workflows, search features, booking paths, checkout processes, loyalty systems, promotion abuse, inventory hoarding, cart holds without purchase, look-to-book inflation, seat spinning, denial-of-inventory.
- Identity/session signals: credential reuse, MFA context, token reuse, cookie reuse, session ID reuse, authentication workflows, login traffic spikes, deviations from expected login patterns.
- Browser and client signals: declared browser/user-agent family, Chrome impersonation, Android Browser impersonation, valid browser environments, valid fingerprints, browser/device fingerprinting, headers, device attributes, execution patterns, session consistency.
- Behavioural signals: request timing, interaction timing, request sequencing, propagation patterns, timing inconsistencies, behavioural drift, persistence, scale, historical patterns across workflows, downstream operational impact.
- Infrastructure and evasion: residential proxy networks, mobile proxy networks, iCloud Private Relay/privacy tooling, CAPTCHA solving, human CAPTCHA farms, headless browser automation, Puppeteer, Selenium, Playwright, bots-as-a-service platforms, multi-threading, fallback attack models.
- Defensive controls named: customer-defined rules, rate limiting, bot detection models, Advanced Bot Protection, Account Takeover Protection, behavioural monitoring, API discovery, strong authentication/authorization, adaptive challenge mechanisms, computational/proof-of-work techniques.
- Standards/protocol-adjacent mechanism: cryptographically signed headers for verified AI bots. The report does not specify the standard, implementation, or verification scheme.

## Threat types covered

The source does not map every claim to specific OWASP Automated Threat IDs. It covers the following project-relevant threat types and adjacent categories:

- Account takeover and credential stuffing
- Automated login abuse
- API abuse and API-first bot execution
- Business logic abuse
- Scraping and AI-driven crawling/fetching
- Scalping and inventory hoarding
- Denial-of-inventory / seat spinning
- SMS pumping through OTP workflows
- Carding/payment-flow abuse only indirectly through checkout/payment references, not as a central focus
- Data leakage through APIs
- General automation, brute force, vulnerability scanning, and automated probing
- Browser impersonation and automation evasion
- CAPTCHA bypass/solving as an evasion class
- DDoS appears as a category in the report, but DDoS itself is mostly peripheral to the project's web-flow bot-management scope unless tied to application/API-layer automation.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** It approximates the production-facing view of a large bot-management/application-security vendor: what automated traffic its systems classify and block, what its analysts see during mitigations, and how bot pressure appears across applications, APIs, industries, and authentication workflows in protected customer environments. It is particularly useful for the observed-use lane because it moves beyond capability claims into vendor-observed activity, including API-first abuse, ATO, SMS pumping, AI crawler/fetcher traffic, browser impersonation, and persistent adaptive automation.
- **What does it fail to represent?** It does not represent independent measurement of the wider internet. Its population is Thales/Imperva-visible traffic, affected by customer mix, protected-site selection, detection coverage, product deployment, rule configuration, and reporting choices. The report does not disclose the underlying sampling frame, number of customers/sites, classifier definitions, validation metrics, false-positive/false-negative rates, or how changes in coverage affect year-on-year comparisons. It also mixes empirical telemetry, analyst interpretation, product recommendation, and marketing framing in one document.
- **What additional evidence would be needed to go further?** Independent measurement studies, victim-side postmortems, reproducible datasets, clearer methodology on detection/classification, cross-vendor telemetry comparison, external validation of AI-bot labels, and evidence on attack success rates rather than blocked/mitigated request volumes. For the AI-agent claims, additional evidence would be needed on undeclared agents, signed-agent adoption, policy enforcement, and how often agent-like traffic causes measurable harm versus operational load.

## What it cannot show

- It cannot show internet-wide prevalence of bad bots, AI bots, API attacks, or account takeover; the percentages are vendor-measured within Thales/Imperva-visible traffic.
- It cannot show that all blocked requests were malicious or that all unblocked automation was benign; classification quality is not externally validated in the report.
- It cannot show attack success rates. Blocked requests and mitigated attacks are not the same as successful fraud, data extraction, account compromise, or operational harm.
- It cannot cleanly prove that AI caused the reported increases. The report often frames AI as an accelerator and includes a footnote that AI bot coverage expanded in 2025.
- It cannot show the full scale of AI-driven automation because it explicitly says its AI traffic analysis covers detectable or declared AI clients and that a larger unverified portion remains outside observation.
- It cannot show that its customer base is representative of all web-facing organisations, all sectors, or all geographies.
- It cannot show comparative vendor efficacy. Product-specific statements about Imperva Advanced Bot Protection and Account Takeover Protection are vendor claims, not independent benchmark results.
- It cannot show detailed mechanisms for evasion or mitigation without operational gaps; this entry deliberately records technique classes rather than procedures.
- It cannot replace foundations or standards sources for signed headers, browser fingerprinting, APIs, OWASP categories, or LLM security; those need separate canonical sources.

## Project impact

- Strong candidate for the observed-use lane: it provides vendor-measured production evidence rather than only capability evidence, but must always be caveated as vendor telemetry.
- Useful source for the Background / landscape page on the normalisation of automation and the emerging third category of AI agents between traditional good bots and bad bots.
- Useful source for the Technical territory page on API-first abuse, especially the point that harmful bot traffic can be well-formed, authenticated, and workflow-following rather than obviously malformed.
- Useful source for the browser-native automation / AI-agent shift: it explicitly connects AI agents, APIs, fetcher/crawler behaviour, intent ambiguity, and the movement from bot blocking toward automation governance.
- Useful support for a section on observed evasion classes: browser impersonation, fingerprint manipulation, proxy masking, CAPTCHA solving, headless automation frameworks, and persistence/adaptation. Use only as technique-level evidence, not as a recipe.
- Useful source for sector examples: Financial Services for ATO/API identity workflows; Retail and Travel for business logic abuse, inventory denial, and high-frequency API polling.
- The two anonymised case studies can be cited as observed examples of authentication/API abuse without naming targets or actors. Keep them high-level and avoid operational sequence detail.
- The source should not be used to make independent prevalence claims about the whole web, claims about vendor superiority, or precise causal claims about AI. Its main value is as a dated, vendor-measured snapshot of what one large application-security vendor says it observed in 2025.
- Some sections are lower priority or partially out-of-scope for openbotrisk: compliance penalties, broad DDoS framing, generic product recommendations, and LLM application-security material not tied to bot/abuse flows.
