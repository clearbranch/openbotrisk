# Evidence Targets

Working list of sources to read or extract next. This is planning material, not the evidence register. Rows here are candidates until they are extracted into `working/register-entries/` and projected into the public register.

## Broad Evidence Gaps

| Priority | Target source | Why | Evidence role | Link or search expression |
|---|---|---|---|---|
| P0 | Imperva Bad Bot Report, latest annual edition | Already queued; gives prevalence/trend framing from a major WAF/bot-management incumbent. | Vendor telemetry / observed-use claim | <https://www.imperva.com/resources/resource-library/reports/imperva-bad-bot-report/> |
| P0 | Akamai State of the Internet reports on bots, scraping, credential stuffing, commerce abuse | Adds missing edge/WAF incumbent view and production-side telemetry claims. | Vendor telemetry / observed-use claim | `site:akamai.com "State of the Internet" bot credential stuffing scraping abuse` |
| P0 | F5 / Shape Security credential-stuffing or automation reports | Strong fit for login abuse, ATO, credential stuffing, and bot-driven transactional abuse. | Vendor telemetry / observed-use claim | `site:f5.com/labs Shape Security credential stuffing bots automation report` |
| P0 | HUMAN / Satori threat reports | Useful where they document ad fraud, botnets, automation infrastructure, or takedown-style operational findings. | Threat-intel / operational evidence | <https://www.humansecurity.com/learn/blog/tag/satori-threat-intelligence/> |
| P0 | Cloudflare Radar / bot traffic material | Production-side visibility at large scale; useful counterweight to scraper-side material. | Vendor telemetry / observed-use claim | <https://radar.cloudflare.com/traffic/bots> |
| P0 | Academic measurement studies of web bots “in the wild” | Best route to independent evidence that automated activity is observed against real services. | Independent measured-use evidence | `"web bot" "measurement study" "in the wild" website traffic` |
| P0 | Academic measurement studies of credential stuffing | Directly supports one of the project’s in-scope abuse types. | Independent measured-use evidence | `"credential stuffing" measurement study web login attacks` |
| P0 | Platform/victim engineering posts about scraping or bot pressure | Stronger than tool docs because they come from organisations defending real sites. | Victim-side observed-use evidence | `site:engineering.* scraping bots abuse rate limiting "credential stuffing"` |
| P1 | GitHub / npm / PyPI abuse or account-automation posts | Developer platforms often publish concrete abuse-mitigation writeups. | Victim-side observed-use evidence | `site:github.blog abuse bots rate limiting scraping fake accounts` |
| P1 | Wikimedia / Wikipedia anti-scraping or bot traffic material | Useful non-commercial platform view; can support scraping/load pressure claims. | Victim-side observed-use evidence | `site:wikimedia.org scraping bots traffic abuse rate limiting` |
| P1 | Reddit, Stack Overflow, or large community-platform anti-scraping posts | Adds platform-side evidence for scraping/fake-account pressure. | Victim-side observed-use evidence | `site:redditinc.com engineering scraping bots abuse`; `site:stackoverflow.blog scraping bots abuse` |
| P1 | Legal/enforcement records on ticket bots and scalping | Concrete evidence of automation used against limited-inventory websites; keep technique-focused, not actor-focused. | Legal-record / observed-use evidence | `"ticket bots" lawsuit automated purchasing website` |
| P1 | Legal records on scraping disputes | Useful for showing automation used against websites, but avoid drifting into legal analysis. | Legal-record / observed-use evidence | `"scraping" complaint automated access website bots` |
| P1 | Legal/enforcement records on fake accounts or credential stuffing | Helps support fake-account/ATO scope without relying only on vendors. | Legal-record / observed-use evidence | `"credential stuffing" indictment automated login website` |
| P1 | Current bot-detection survey classified by signal/data source | Needed for academic backbone and citation-network closure. | Academic survey / literature map | `"web bot detection" survey fingerprinting behavioural network traffic` |
| P1 | Browser-fingerprinting survey: Laperdrix et al. | Missing academic anchor for fingerprinting literature. | Academic survey / foundations for fingerprinting | `Laperdrix Bielova Baudry Avoine Browser Fingerprinting A Survey ACM TWEB` |
| P1 | niespodd/browser-fingerprinting catalogue | Already named in the scope guide; useful catalogue of signals and evasion surface. | Threat-surface catalogue | <https://github.com/niespodd/browser-fingerprinting> |
| P1 | Anthropic computer-use / browser-agent safety material | Adds primary agent-builder source; current agent evidence is too defender-vendor-heavy. | Agent-builder primary source | `site:anthropic.com computer use browser safety Claude` |
| P1 | OpenAI computer-use / Operator / agent safety material | Same reason as Anthropic; important for browser-native automation shift. | Agent-builder primary source | `site:openai.com Operator computer use agent safety browser` |
| P1 | Google reCAPTCHA Enterprise / Cloud Armor bot-management docs | Challenge/risk-score platform view; useful for foundations and vendor landscape. | Capability-doc / vendor architecture | `site:cloud.google.com reCAPTCHA Enterprise bot fraud risk score` |
| P2 | MDN HTTP headers, cookies, client hints, Fetch | Foundations gap; supports clear explanation of what signals browsers expose. | Foundations | <https://developer.mozilla.org/en-US/docs/Web/HTTP> |
| P2 | RFC 9110 / 9112 / 9113 / 9114 | Canonical HTTP semantics and protocol references. | Standards | <https://www.rfc-editor.org/rfc/rfc9110> |
| P2 | RFC 6265 cookies | Canonical cookie/session reference. | Standards | <https://www.rfc-editor.org/rfc/rfc6265> |
| P2 | RFC 8446 TLS 1.3 | Needed for TLS-fingerprinting foundations. | Standards | <https://www.rfc-editor.org/rfc/rfc8446> |
| P2 | W3C WebDriver specification | Canonical reference for browser automation control. | Standards / automation foundations | <https://www.w3.org/TR/webdriver2/> |
| P2 | PortSwigger Web Security Academy sessions/authentication/rate-limiting material | Strong pedagogical foundation source, not an analytical anchor. | Foundations | <https://portswigger.net/web-security> |
| P2 | OWASP API Security Top 10 | Helps API abuse and business-logic abuse foundations. | Foundations / taxonomy | <https://owasp.org/API-Security/> |
| P2 | Anti-detect browser docs: GoLogin, Multilogin, Kameleo, AdsPower, Octo Browser | Shows supply-side browser-profile/fingerprint market; do not treat as abuse prevalence. | Market/capability evidence | `anti detect browser fingerprint profile proxy docs GoLogin Multilogin Kameleo` |
| P2 | Camoufox, Nodriver, SeleniumBase UC Mode | More concrete stealth/evasion tooling entries. | Tooling capability / evasion surface | `Camoufox GitHub browser fingerprint`; `Nodriver GitHub undetected browser`; `SeleniumBase UC Mode docs` |
| P2 | curl_cffi / tls-client / browserforge | Adds non-browser TLS/HTTP impersonation tooling beyond Rnet. | Tooling capability / protocol impersonation | `curl_cffi JA3 browser impersonation`; `tls-client browser fingerprint`; `browserforge fingerprint generator` |

## Scarce-Resource Abuse Targets

| Priority | Source | Evidence level | Scarce resource | Likely register category | Why it matters |
|---|---|---|---|---|---|
| P0 | DVSA: “How we’re dealing with bots and the reselling of driving tests” | observed-use | appointment | threat-surface / victim-side | Very strong fit. DVSA explicitly says bots secure slots faster than customers, hold appointments, and resell them. It also discusses CAPTCHA, advanced bot protection, and false-positive friction without giving operational detail. |
| P0 | DVSA: “What we are doing to tackle companies selling driving tests for profit” | observed-use | appointment | threat-surface / victim-side | Strong follow-up. DVSA says Advanced Bot Protection was introduced for all booking services and “successfully reduced bot traffic”; also gives concrete platform changes and registration suspensions. |
| P0 | FTC first BOTS Act cases, 2021 | legal-record | ticket | legal-record / threat-surface | Clean legal evidence. FTC alleges automated software bought tens of thousands of tickets, followed by resale; gives penalties and statutory framing. |
| P0 | FTC BOTS Act compliance refresher, 2025 | legal-record | ticket | legal-record / foundations-adjacent | Useful concise source because it lists the abuse pattern: automated ticket search/reservation, IP concealment, fake accounts, and cards to evade limits. |
| P0 | Ticketmaster v. RMG Technologies preliminary injunction | legal-record | ticket | legal-record / victim-side | Older but very concrete. Court record describes automated devices, CAPTCHA bypass allegations, high-volume requests, and purchase of large ticket quantities. |
| P0 | NY Attorney General, “Obstructed View” ticket report | legal-record / observed-use | ticket | legal-record / threat-surface | Strong ticket-bot background source. Useful for the public-policy/legal history of ticket bots, but read for technique and evidence only, not campaign narrative. |
| P0 | DataDome Galileo: DDR5 RAM scalping surge | vendor-measured | product | vendor / observed-use | Strong recent vendor telemetry. Claims bots hit DDR5 product pages 6x more than legitimate traffic, with 10M+ scraping requests and stock-checking behaviour every 6.5 seconds. |
| P1 | Queue-it/Akamai Hype Event Protection case material | vendor-measured | ticket / product | vendor / queueing architecture | Useful queue/limited-inventory evidence. Reports bot purchases and suspected denial-of-inventory ticket bots reserving tickets while pushing users to secondary markets. |
| P1 | Resy: restaurant reservation fraud | observed-use / vendor-measured | reservation | platform-side / vendor | Good reservation-specific evidence. Resy says bot/broker reservations have higher no-show and late-cancellation rates, and a restaurant noticed fewer bot-made reservations after mitigation. |
| P1 | EU Council Visa Working Party document via Statewatch | regulatory-record | appointment | legal/regulatory / threat-surface | Useful for visa appointment abuse. It records third-party companies booking all appointments and reselling them at high prices, but does not by itself prove bot automation. |
| P1 | Türkiye Trade Ministry investigation reporting | legal/regulatory-reporting | appointment | legal-record candidate | Claims seven companies are under review for bot-based capture and resale of Schengen visa appointment slots. Good candidate, but find the original ministry statement before treating as strong evidence. |
| P2 | Visa Catcher / Visard appointment services | market-evidence | appointment | threat-surface / market | Shows a live service ecosystem for monitoring and auto-booking visa appointments. Do not treat as abuse proof by itself. |
| P2 | OpenTable / Resy automation examples | capability-only | reservation | threat-surface / tooling | Shows reservation-sniping capability exists: monitoring availability and booking faster than manual users. Weak evidence for hostile abuse unless paired with Resy/platform evidence. |
| P2 | Imperva retail scalping API case | vendor-measured / observed-use | product | vendor / threat-surface | Relevant to product inventory abuse: bots exploited an exposed API and targeted inventory. Useful, but vendor case study, so treat cautiously. |

## Suggested First Read Batch

Read these first, in this order:

| Order | Source | Coverage gained |
|---:|---|---|
| 1 | DVSA: “How we’re dealing with bots and reselling of driving tests” | Strong appointment-slot abuse case. |
| 2 | FTC first BOTS Act cases | Legal ticketing anchor. |
| 3 | Ticketmaster v. RMG Technologies | Concrete court record for automated ticket purchasing and CAPTCHA-bypass allegations. |
| 4 | NY AG “Obstructed View” report | Ticket-bot background and public-policy/legal history. |
| 5 | DataDome DDR5 RAM scalping report | Product-drop telemetry case. |
| 6 | Resy reservation fraud post | Restaurant reservation abuse case. |
| 7 | Queue-it/Akamai Hype Event Protection | Queueing / denial-of-inventory case. |
| 8 | EU Council / Statewatch visa appointment abuse document | Visa appointment regulatory case. |
