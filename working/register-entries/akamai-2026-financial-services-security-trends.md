# AI-Empowered Botnets and API Visibility Gaps: Attack Trends in Financial Services — Akamai Security 2026

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: full text, uploaded PDF
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Akamai Security. (2026). *AI-Empowered Botnets and API Visibility Gaps: Attack Trends in Financial Services*. State of the Internet/Security, V12 Issue 02. Akamai. Public URL not stated in the uploaded PDF; footer gives `Akamai.com/security`.
- **Source URL or path**: `SRC-040-akamai-2026-financial-services-security-trends.pdf`
- **Date accessed**: 2026-06-06
- **Category**: vendor
- **Evidence basis**: empirical-operational — the report is primarily based on Akamai's internal operational telemetry from protected web application, API, and DDoS traffic. Some API-risk claims are survey-based and some AI/bot claims rely on private threat-intelligence data; those are noted separately below.
- **Operational proximity**: observed — the strongest bot/API claims are based on Akamai-observed production traffic and security alerts against real protected websites, applications, APIs, and customer traffic. This remains vendor-measured rather than independently measured, and several claims in the source are lower-proximity vendor interpretation or survey claims.
- **Tags**: vendor, vendor-telemetry, financial-services, api-abuse, api-security, behavioural, botnets, scraping, ai-agent, headless-browser, user-risk, web-attacks, DDoS-out-of-scope

## What it claims

- Financial services web attacks grew by 11% globally from 2024 to 2025, and financial services ranked second after commerce for total web attacks over January 2024 to December 2025.
- The source reports 110 billion web attacks against financial services over the two-year period, including 20 billion web attacks on API endpoints.
- Banking was the dominant financial-services vertical for web attacks in 2025, accounting for 60% of financial-services web attacks and 83% of web attacks against financial-services API endpoints.
- The source frames financial-services APIs as a narrower but deeper attack surface than commerce or games: fewer API endpoint attacks than those sectors, but more complex business logic involving KYC/AML providers, interbank clearing, fintech providers, and credit-worthiness validators.
- The report claims a shift from conventional signature-detectable attacks toward behaviour-based API threats, including BOLA, BOPLA, shadow/zombie APIs, misconfiguration, broken access control, and AI-connected API data exposure.
- The report states that, in Akamai's 2026 API Security Impact Study, 96% of global financial-services respondents reported at least one API security incident in the previous 12 months.
- The report states that a soon-to-be-published Akamai survey found data leaks and AI-related API attacks were each reported by 39% of financial-services respondents as common API security incident types, followed by insufficient access-control exploitation at 35%.
- The report states that respondents attributed API security incidents mainly to misconfigurations (65%), lack of dedicated API security tools (48%), and vulnerabilities in AI-related APIs (39%).
- Advanced bot activity is reported to have surged by 147% in late 2025; in one case, 96% of site traffic was identified as scraping bots.
- The report claims attackers continue to use low-and-slow bot tactics, including dropping request rates below one request per second to evade threshold-based detection.
- The report claims attackers are using AI and advanced headless browsers to make bot traffic blend more closely with legitimate browser behaviour, including what it calls transparent browser impersonation.
- The report argues mitigation should move beyond basic signature blocking toward behavioural heuristics and user-risk telemetry within transactional flows.
- The source reports an average of 2.5 billion daily AI bot requests across Akamai's network, with AI-related traffic nearly doubling in the second half of 2025.
- The report claims AI agents can navigate complex applications, perform contextual analysis, and sometimes make decisions, marking a shift from automation to autonomy.
- The source cites private threat-intelligence data in which an abused search bot targeted 570,000 unique URLs in a single window, and a large-scale AI training crawler targeted transactional API endpoints across nearly 7,000 hostnames and 37,000 unique paths in less than seven days.
- The report concludes that AI amplifies existing risks around DNS, DDoS, APIs, scraping, and data exposure, rather than replacing older security risks.

## What evidence it provides

- The web-attack and Layer 7 DDoS data is based on application-layer alerts seen through Akamai's WAF. Web application attack alerts are triggered when Akamai detects a malicious payload in a request to a protected website, application, or API. Layer 7 DDoS alerts are triggered when Akamai detects volumetric anomalies in requests to protected properties.
- The methodology states that Layer 7 DDoS alerts may be triggered by benign or malicious requests, and that alerts do not indicate attack success. This is important because alert volume is not the same thing as successful abuse, compromise, or business impact.
- The report states that its telemetry comes from an internal Akamai tool analysing security events detected on Akamai Cloud, described as approximately 340,000 servers in more than 4,000 locations on nearly 1,300 networks in more than 130 countries, with security data measured in petabytes per month.
- The report notes that the analysed WAF/Layer 7 DDoS data does not consider custom configurations of protected properties, even though Akamai products allow substantial customer customisation.
- The 96% API-incident claim and incident-cause percentages come from Akamai's 2026 API Security Impact Study and a soon-to-be-published API Security Risks in Financial Services survey, not from fully reproduced survey methods in this PDF. Treat these as survey claims reported by Akamai, not independently inspectable evidence from this document alone.
- The advanced bot activity, 96% scraping-bot case, 2.5 billion daily AI bot requests, 570,000-URL abused-search-bot case, and AI crawler hitting nearly 7,000 hostnames / 37,000 paths are presented as Akamai telemetry or private threat-intelligence observations. The PDF does not provide raw data, labelling criteria, denominator definitions, confidence intervals, or validation against independent ground truth.
- The claims about AI-powered evasion, headless browsers, and transparent browser impersonation are partly telemetry-backed and partly interpretive. The report does not provide a technical detection study showing how Akamai classifies AI-driven botnets or headless-browser traffic.
- DDoS figures and named botnet takedown material are supported by Akamai operational reporting and law-enforcement/industry collaboration claims, but most of the network-layer DDoS and IoT botnet material sits outside this project's main scope.

## Signals or techniques mentioned

- WAF malicious-payload alerts for protected websites, applications, and APIs.
- Layer 7 DDoS volumetric anomaly alerts on request counts.
- API endpoint attack tracking split from web application attack tracking.
- Behaviour-based API threat framing, including BOLA and BOPLA.
- Unmanaged API exposure, including shadow APIs and zombie APIs.
- Misconfiguration and broken access control.
- AI-related API vulnerabilities and AI-connected data exposure.
- Low-and-slow bot tactics, including sub-one-request-per-second request rates.
- Advanced headless browsers.
- AI-driven botnets and claimed browser-behaviour mimicry.
- Transparent browser impersonation.
- Behavioural heuristics.
- User-risk telemetry in transactional flows.
- AI bot request classification.
- AI crawler / AI training crawler traffic against transactional API endpoints.
- HTTP/2 protocol-edge exploitation is mentioned in a DDoS context; useful only as a side note because much of that material is outside this project's web bot/abuse focus.

## What threat type it covers

- Web application attacks against financial-services sites and APIs.
- API abuse and API visibility gaps, including authorisation failures, exposed sensitive data, misconfiguration, and AI-related API risk.
- Scraping and AI crawler activity against transactional APIs and large URL surfaces.
- Bot evasion and bot traffic blending, especially via AI-assisted behaviour mimicry and advanced headless browsers.
- Account takeover and fraud are mentioned as potential downstream concerns, but not analysed in detail.
- Layer 7 DDoS overlaps partially with the project's web-facing abuse scope, but most DDoS, IoT botnet, geopolitical, and named-actor material is out of scope for this project.

## Framing distance

This is a useful observed-use vendor telemetry source, but it approximates the real bot/abuse problem through Akamai's customer base, Akamai's edge visibility, Akamai product alert definitions, and Akamai's classification pipeline. That is stronger than a pure vendor capability claim because it reports observed production traffic, but weaker than independent measurement because the source does not expose raw data, labels, sampling rules, false-positive rates, false-negative rates, or customer-selection effects.

For the project, the most valuable framing is not "Akamai proves AI bots are widespread". The safer framing is: a major edge/security vendor reports seeing increased AI-labelled bot traffic, scraping/crawler activity against APIs, and evasion patterns involving low-rate traffic, headless browsers, and behavioural mimicry in financial-services traffic. This supports the claim that commercial telemetry sees bot/API behaviour that public datasets struggle to reproduce, while also showing why those claims are hard to verify externally.

The source is finance-sector-specific and heavily weighted toward Akamai-protected properties. It does not represent smaller sites, sites using other vendors, unprotected sites, or the public web as a whole. Its API-incident survey claims represent respondent self-report, not traffic measurement. Its bot and AI-agent claims need corroboration from other vendors, independent measurement studies, victim postmortems, or controlled experiments before being used as broad field claims.

## What it cannot show

- It cannot show market-wide prevalence of AI bot abuse across the web.
- It cannot independently validate whether traffic labelled as AI bot, scraping bot, advanced bot, or malicious crawler is correctly classified.
- It cannot show detection efficacy, because the report is not an evaluation of Akamai controls and does not provide false-positive or false-negative rates.
- It cannot show attack success, because the methodology explicitly says alerts do not indicate whether an attack succeeded.
- It cannot separate product visibility from threat prevalence: a trend may reflect actual attacker change, Akamai customer mix, customer configuration, detection-rule changes, or changes in labelling.
- It cannot support detailed claims about attacker identity or named campaigns within this project, because named-actor attribution is out of scope.
- It cannot support the project's public-data methodology directly, because the underlying telemetry is private and not reproducible.
- It cannot show that AI caused the observed trends; the report often uses AI as an explanatory frame, but the evidence presented is correlational or observational.
- It cannot show that financial-services patterns generalise to booking systems, ecommerce, public services, or other project examples without additional evidence.

## Project impact

- Worth extracting, but cite carefully as vendor telemetry rather than neutral measurement.
- Useful for the project's observed-use lane: it gives concrete vendor-reported production observations about bot activity, API abuse, scraping bots, AI bot request volume, and crawler/API targeting.
- Useful for the "what public data cannot replicate" argument: the source's most valuable evidence depends on private edge/WAF telemetry and customer traffic that cannot be reproduced from public datasets.
- Supports a technical-territory page on API visibility gaps: shadow/zombie APIs, sensitive-data exposure, BOLA/BOPLA, misconfiguration, broken access control, and AI-connected APIs.
- Supports a browser-native / AI-agent discussion, but only as vendor-reported observation. Pair with independent sources on Playwright/Puppeteer/headless browsers, browser agents, crawler behaviour, and controlled experiments before making stronger claims.
- Supports a detection-signals section with behavioural heuristics, user-risk telemetry, request-rate patterns, WAF alerts, and API endpoint visibility.
- Should not be used for vendor comparison or evaluation. The project should not characterise Akamai's product quality from this source.
- Most of the named actor, geopolitical, IoT botnet, ransomware, MITRE, compliance, and network-layer DDoS material should be ignored or recorded only as out-of-scope context.
- This is not a foundations source. It assumes the reader already understands WAFs, APIs, DDoS, botnets, and web attacks.
