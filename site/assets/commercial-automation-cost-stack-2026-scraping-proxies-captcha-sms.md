# Commercial automation cost stack (2026): scraping APIs, proxies, CAPTCHA solving, managed scraping, and SMS verification

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded pricing/report captures:
  - `SRC-102-web-scraping-pricing-2026-9-platforms-compared-from-0-13-1k-use-apify.pdf`
  - `SRC-102-apify-state-of-web-scraping-report-2026.pdf`
  - `SRC-102-managed-web-scraping-vs-diy-how-to-choose-the-right-approach.pdf`
  - `crawlbase_pricing.odt`
  - `SRC-102-pricing-scrapingbee-web-scraping-api.pdf`
  - `SRC-102-pricing-zenrows.pdf`
  - `SRC-102-web-scraper-api-free-trial.pdf`
  - `SRC-102-12-best-and-cheapest-residential-proxies-in-2026-tested-and-ranked.pdf`
  - `SRC-102-proxy-cheap-affordable-services-buy-cheap-proxies.pdf`
  - `SRC-102-ai-captcha-solver-bypass-recaptcha-and-any-captchas-using-best-auto-captcha-solving-service-api.pdf`
  - `SRC-102-5sim-statistics-active-temp-numbers-and-sms-success-rate.pdf`
- **Prompt version**: newer register/source-extraction pattern used in this conversation.
- **Source handling decision**: combine into one cost-of-capability entry. These sources are mostly vendor or vendor-adjacent pricing/market materials. Their value is as cost and availability signals, not abuse prevalence or effectiveness evidence.

## Bibliographic / source set

### Anchor sources

- Apify / UseApify. (2026). *Web Scraping Pricing 2026: 9 Platforms Compared (From $0.13/1K)*. Uploaded PDF capture.
- Apify / The Web Scraping Club. (2026). *State of Web Scraping Report 2026*. Uploaded PDF.
- Ficstar / Raquell Silva. (2026). *Managed Web Scraping vs. DIY: How to Choose the Right Approach*. Uploaded PDF capture.

### Supporting pricing snapshots

- Crawlbase. (2026). Smart AI Proxy pricing capture. Uploaded ODT/image capture.
- ScrapingBee. (2026). *Pricing - ScrapingBee Web Scraping API*. Uploaded PDF capture.
- ZenRows. (2026). *Pricing - ZenRows*. Uploaded PDF capture.
- Bright Data. (2026). *Web Scraper APIs / Free Trial*. Uploaded PDF capture.
- AIMultiple. (2026). *12 Best & Cheapest Residential Proxies in 2026 (Tested & Ranked)*. Uploaded PDF capture.
- Proxy-Cheap. (2026). *Affordable Services / Buy Cheap Proxies*. Uploaded PDF capture.
- CAPTCHA solver pricing page. (2026). *AI captcha solver: Bypass reCAPTCHA and any captchas using best auto captcha solving service API*. Uploaded PDF capture.
- 5SIM. (2026). *5SIM Statistics – Active Temp Numbers & SMS Success Rate*. Uploaded PDF capture.

## Category and treatment

- **Category**: commercial automation ecosystem / cost-of-capability
- **Evidence basis**: vendor pricing pages / vendor-adjacent comparison / industry survey / pricing snapshots
- **Operational proximity**: market availability — shows services, packaging, and price signals for automation inputs; not observed abuse, not effectiveness measurement, and not independent validation.
- **Tags**: scraping-pricing, scraping-APIs, managed-scraping, web-scraper-API, residential-proxies, smart-proxy, CAPTCHA-solving, temp-SMS, account-verification, automation-economics, cost-of-capability, OAT-011, OAT-009, OAT-019, OAT-008

## What the source cluster shows

This cluster supports one main point:

> Automated abuse capability is not only technically possible; the surrounding commercial ecosystem makes key inputs cheap, modular, and easy to buy: scraping APIs, browser rendering, proxy routing, residential/mobile IPs, CAPTCHA solving, managed scraping, and temporary SMS verification.

The sources do **not** prove malicious use. They show availability and cost signals.

## Main capability layers

| Layer | Sources | Project relevance |
|---|---|---|
| Web scraping APIs and platforms | Apify pricing comparison, ScrapingBee, ZenRows, Crawlbase, Bright Data Web Scraper APIs | Shows that data extraction, browser rendering, proxy rotation, domain-specific endpoints, and bulk scraping are packaged as products. |
| Managed scraping / TCO | Ficstar managed-vs-DIY source | Shows why organisations outsource scraping rather than building internal systems. |
| Industry practice | Apify State of Web Scraping Report 2026 | Shows web scraping as an active professional ecosystem, including proxy usage, infrastructure, bot detection, and AI scraping. |
| Residential and ISP/mobile proxies | AIMultiple proxy comparison, Proxy-Cheap pricing | Shows low-cost residential/static/mobile/datacenter proxy access and targeting features. |
| CAPTCHA solving | CAPTCHA solver pricing page | Shows CAPTCHA-solving sold as a service with per-1,000 pricing and high advertised capacity. |
| SMS / temporary numbers | 5SIM statistics | Shows account-enablement inputs such as low-cost temporary numbers, stock counts, and delivery success rates. |

## Key cost and market signals

## Concrete price examples from the captured sources

These are **snapshot prices from the uploaded captures**, not recommendations and not current-price guidance. The sources mix USD and GBP, and I have kept the original currencies rather than converting them. The point is order-of-magnitude availability, not precise comparison.

### Scraping APIs, browser rendering, and scraper platforms

| Component / provider | Captured price signal | Why it matters |
|---|---:|---|
| Apify free tier | `$5` credits/month | Free/low-cost entry point for small scraping jobs and experiments. |
| Apify Starter | `$29/month`, including `$29` credits | Low monthly entry into a full scraper platform. |
| Apify Scale | `$199/month`, including `$199` credits | Regular scraping/orchestration tier. |
| Apify Business | `$999/month`, including `$999` credits | Mid-market/agency tier before custom enterprise pricing. |
| Apify cost-per-page estimate | simple HTML `~$0.0005–$0.002/page`; JavaScript-rendered `~$0.003–$0.01/page`; residential proxies add `~$1.50–$3/GB` | Shows that page-level extraction can be extremely cheap before developer time and failure handling are counted. |
| ScrapingBee trial | `1,000` free API credits | Low-friction evaluation. |
| ScrapingBee Freelance | `$49/month`, `250,000` API credits, `10` concurrency | Entry paid API layer with proxy/rendering support. |
| ScrapingBee Startup | `$99/month`, `1,000,000` credits, `50` concurrency | Small production scraping/API use. |
| ScrapingBee Business | `$249/month`, `3,000,000` credits, `100` concurrency | Production workload tier. |
| ScrapingBee Business+ | `$599/month`, `8,000,000` credits, `200` concurrency | Higher-volume scraping/API use. |
| ScrapingBee cost-per-page estimate | basic HTML `~$0.00008/page` at Business tier; JavaScript `~$0.0004/page`; premium domains `~$0.002–$0.02/page` | Shows the large price spread between easy pages and protected/high-cost targets. |
| Zyte API PAYG | HTTP: simple `$0.13/1,000`, easy `$0.23/1,000`, moderate `$0.44/1,000`, complex `$0.70/1,000`, advanced `$1.27/1,000` | Cheapest simple HTTP entry in the Apify comparison; costs rise with anti-bot difficulty. |
| Zyte browser-rendered PAYG | simple `$1.01/1,000`, easy `$2.01/1,000`, moderate `$4.02/1,000`, complex `$8.04/1,000`, advanced `$16.08/1,000` | Rendering/protected targets materially change the economics. |
| Zyte committed tier example | at `$500/month` commit, simple HTTP can drop to about `$0.06/1,000` | Volume commitments can materially reduce unit costs. |
| Firecrawl Hobby | `$16/month` for `5,000` credits/pages | Low-cost AI/content-ingestion oriented scraping. |
| Firecrawl Growth | about `$333/month` for `500,000` credits/pages | Example of low per-page cost for clean markdown/AI-ready content. |
| Octoparse Standard | `$69/month` billed annually, or about `$89/month` monthly | No-code cloud scraping entry point. |
| Octoparse Professional | `$249/month` billed annually | No-code/team tier. |
| Bright Data Web Scraper APIs | examples in capture: `$1.50`, `$1.30`, `$1.10`, `$1.00`, `$0.98`, `$0.83`, `$0.75` per `1K` records, with monthly commitments shown at `$499`, `$999`, and `$1,999` | Structured scraper APIs turn extraction into per-record pricing rather than raw scraping infrastructure. |
| Self-hosted stack | around `$20/month` VPS in the Apify comparison, but much higher total cost once proxies and developer time are included | Infrastructure may look cheap, but maintenance and anti-bot work dominate. |

### Total cost of ownership examples

The Apify pricing comparison gives a 12-month TCO estimate for a team scraping `500,000` pages/month. It assumes developer time at `$75/hour`.

| Approach | Platform fees/year | Developer time/year | Estimated 12-month TCO |
|---|---:|---:|---:|
| Apify Business (`$999/month`) | `$11,988` | `~120 hours` / `$9,000` | `~$20,988` |
| Apify Scale (`$199/month`) plus overages | `$3,500` | `~120 hours` / `$9,000` | `~$12,500` |
| Bright Data Pro commit (`$999/month`) | `$11,988` | `~200 hours` / `$15,000` | `~$26,988` |
| Octoparse Professional (`$249/month` annual) | `$2,988` | `~60 hours` / `$4,500` | `~$7,488` |
| Firecrawl Growth (`$333/month`) | `$3,996` | `~80 hours` / `$6,000` | `~$9,996` |
| ScraperAPI Business (`$299/month`) | `$3,588` | `~160 hours` / `$12,000` | `~$15,588` |
| Zyte API (`$500/month` commit) | `$6,000` | `~140 hours` / `$10,500` | `~$16,500` |
| Self-hosted | `~$6,000` | `~480 hours` / `$36,000` | `~$42,000` |

Interpretation: the cheapest-looking option on infrastructure can become the most expensive once engineering time, failure handling, proxy management, and anti-bot maintenance are included.

### Residential, ISP, mobile, and datacenter proxy access

| Provider / source | Captured price signal | Why it matters |
|---|---:|---|
| Bright Data residential proxies | PAYG `$4/GB` with promo; list price `$8/GB`; Starter `$499/month` for `141 GB` at `$3.50/GB`; Professional `$999/month` for `332 GB` at `$3.00/GB`; Enterprise `$1,999/month` for `798 GB` at `$2.50/GB` | Large residential proxy networks are sold as bandwidth products. |
| Oxylabs residential proxies | `$30/month` for `5 GB`, about `$6/GB` | Low monthly entry into large residential pool. |
| Decodo residential proxies | `$11.25/month` or PAYG; `$3.75/GB` monthly / `$4.00/GB` PAYG | Smaller self-serve commitments reduce entry friction. |
| SOAX residential proxies | `$90/month` for `25 GB`, about `$3.60/GB` | Proxy access with targeting/session controls. |
| NetNut residential proxies | `$99/month` for `28 GB`, about `$3.53/GB` | Operations-oriented proxy pricing. |
| Infatica residential proxies | `$96/month` or PAYG; `$3.84/GB` monthly / `$4.00/GB` PAYG; `7-day` paid trial at `$4.00` | Mid-range business-oriented proxy access. |
| Nimble residential proxies | `$8/GB` PAYG or `$150/month` for `150` credits, about `$7.50/GB` | More platform/API-style pricing. |
| IPRoyal residential proxies | `$7.00/GB` subscription or `$7.35/GB` PAYG | Accessible self-serve residential proxy pricing. |
| DataImpulse / low-cost comparison source | residential proxies from `$1/GB` | Shows the low end of headline proxy pricing. |
| Proxy-Cheap capture | examples include static residential around `$2.49/month`, datacenter around `$0.70/month`, and residential traffic around `$2.60/GB`; another headline states stability/reliability “as low as `$1.27` per month” | Proxy products are packaged in several ways: per-IP, per-month, per-GB, static, rotating, residential, ISP, and datacenter. |

Interpretation: proxy access is cheap enough to be a commodity input, but headline price says little about consent, cleanliness, reliability, block rate, or legality.

### CAPTCHA-solving prices

The CAPTCHA solver capture is image-based, but the pricing table on pages 2–4 lists prices per `1,000` solved challenges. Examples include:

| CAPTCHA type | Captured price per 1,000 | Captured solve-time signal |
|---|---:|---:|
| reCAPTCHA v2 | `£0.80–£2.45` | `2 sec.` |
| Image CAPTCHA | `£0.45–£0.89` | `3 sec.` |
| Cloudflare Turnstile | `£1.20` | `3 sec.` |
| reCAPTCHA v3 | `£1.20–£2.45` | `3 sec.` |
| reCAPTCHA Enterprise | `£0.80–£2.45` | `3 sec.` |
| Arkose Labs / FunCaptcha | `£1.20–£41` | `22 sec.` |
| Amazon CAPTCHA | `£1.20` | `11 sec.` |
| DataDome CAPTCHA | `£1.20` | `12 sec.` |
| GeeTest CAPTCHA | `£2.45` | `5 sec.` |
| Audio CAPTCHA | `£0.40` | `7 sec.` |
| Normal CAPTCHA | `£0.45–£0.89` | `2 sec.` |
| Slider CAPTCHA | `£0.99` | `8 sec.` |
| KeyCAPTCHA | `£2.45` | `31 sec.` |

Interpretation: CAPTCHA-solving is priced as a routine per-thousand service. That does not prove effectiveness against any specific protected site, but it does show that CAPTCHA defeat is a commercial service layer.

### Temporary SMS / account-enablement prices

The 5SIM capture gives an England / Telegram example over a `3-day` delivery-success window:

| Virtual number stock label | Captured delivery-success rate | Captured price | Captured stock |
|---|---:|---:|---:|
| Virtual34 | `21.01%` | `$1.30` | `129,900` |
| Virtual63 | `17.14%` | `$1.0896` | `972` |
| Virtual53 | `17.01%` | `$1.10` | `137` |
| Virtual51 | `16.76%` | `$1.05` | `10,321` |
| Virtual60 | `16.45%` | `$1.07` | `10,321` |
| Virtual59 | `15.26%` | `$0.80` | `10,317` |
| Virtual58 | `9.52%` | `$1.7103` | `1,733` |

Interpretation: SMS verification is also commercialised at low per-number prices, but the delivery-success rates in the capture are low and service-specific. This is account-enablement cost evidence, not proof of successful account abuse.

### Scraping APIs and platforms

The Apify pricing comparison reports a market of scraping platforms spanning free tiers, entry plans, pay-as-you-go APIs, and enterprise plans. It frames tools such as Apify, Bright Data, Octoparse, Firecrawl, ScraperAPI, ScrapingBee, Zyte, IPRoyal, Oxylabs, and self-hosted infrastructure as alternatives with different cost and operational trade-offs.

Examples from the captured sources:

- Apify comparison describes entry scraping costs ranging from very low pay-as-you-go API rates to monthly platform plans.
- ScrapingBee pricing capture lists monthly plans from $49/month upward with included API credits, concurrency, JavaScript rendering, rotating/premium proxies, geotargeting, screenshots, extraction rules, dedicated scraper APIs, and Google Search API availability.
- ZenRows capture lists a free trial and monthly plans, with protected/basic result quotas, scraping browser or residential proxy allocation, and concurrent request limits.
- Crawlbase Smart AI Proxy capture shows tiers from a free trial to monthly paid plans, with credits, unique proxies, threads, support, and AI/JavaScript/browser features.
- Bright Data Web Scraper APIs capture markets domain-specific structured data endpoints, bulk requests, crawling/discovery endpoints, output in JSON/CSV, and scraper endpoints for domains/categories including LinkedIn, e-commerce, real estate, and social media.

Interpretation: scraping is sold as infrastructure and as productized extraction. The market is no longer just “write a script with requests and BeautifulSoup”; users can buy complete scraping platforms, API wrappers, browser rendering, proxies, prebuilt endpoints, and managed extraction.

### Managed scraping versus DIY

The managed-vs-DIY source claims in-house scraping operations can be much more expensive once engineering, maintenance, proxy management, infrastructure, and legal/operational overhead are considered. The exact dollar figures are vendor-framed and should not be treated as independent cost accounting, but the source is useful for the business-model point: many buyers prefer managed services because keeping scrapers alive is itself operational work.

Interpretation: paid scraping services reduce not just technical friction, but also staffing and maintenance friction.

### Proxy costs

The residential proxy comparison and Proxy-Cheap capture show that proxy access is available at low headline prices, with common advertised features including:

- rotating residential proxies;
- static residential/ISP proxies;
- datacenter IPv4/IPv6 proxies;
- mobile proxies;
- HTTP/SOCKS5 support;
- country/city/ISP targeting;
- bandwidth- or per-IP pricing;
- trials or small starter packages.

The AIMultiple capture includes claimed benchmarking across vendors and a cost comparison table, while Proxy-Cheap markets very low entry prices for static residential/ISP access.

Interpretation: proxy access is a commodity input. Quality, legality, consent, sourcing, and reliability vary sharply, so low price should not be equated with clean or safe supply.

### CAPTCHA solving costs

The CAPTCHA solver capture lists many CAPTCHA types and prices per 1,000 solved challenges, with advertised solve times and spare capacity. The important project point is not the exact provider workflow, but the market signal: CAPTCHA-solving is packaged as a paid API, including modern challenges such as reCAPTCHA, Cloudflare Turnstile, Arkose/FunCaptcha, Amazon Captcha, Geetest, DataDome CAPTCHA, slider/click/math/text/audio/normal CAPTCHAs, and others.

Interpretation: CAPTCHA defeat is a service layer, not only a research problem. Keep this high-level because it is high dual-use.

### Temporary SMS / account-enablement

The 5SIM capture shows temporary virtual numbers for receiving SMS, with country/service filters, stock counts, prices, and short-period delivery success rates. The example capture shows Telegram numbers for England, with prices around roughly $0.80–$1.71 and stock/success-rate fields.

Interpretation: account-enablement is also commercialised. Temporary SMS services can support legitimate testing and privacy uses, but they are also relevant to account creation, verification bypass, and abuse-at-scale economics.

## Relationship to OAT categories

Direct or strong relevance:

- **OAT-011 Scraping** — scraping APIs, managed extraction, browser rendering, domain-specific scraper endpoints.
- **OAT-009 CAPTCHA Defeat** — commercial CAPTCHA-solving pricing and capacity.
- **OAT-019 Account Creation** — temporary SMS numbers and account verification inputs.
- **OAT-008 Credential Stuffing** — proxy/CAPTCHA/account infrastructure can support login-abuse workflows, though these sources do not prove such abuse.
- **OAT-006 Expediting** — automation services accelerate workflows that might otherwise be manual.
- **OAT-005 Scalping / OAT-013 Sniping / OAT-021 Denial of Inventory** — indirect relevance where proxies, CAPTCHA solving, and SMS verification are used in scarce-resource workflows; not directly evidenced by these pricing pages.

## Scarce-resource abuse fields

These sources are indirectly relevant to scarce-resource abuse because they expose the cost stack behind automation:

- proxies can distribute traffic;
- CAPTCHA solvers can reduce friction;
- SMS numbers can support account creation or verification;
- scraping APIs can monitor availability or extract product/slot/ticket data;
- managed services can lower operational burden.

However, none of these sources show a specific ticketing, appointment, product-drop, or slot-sniping campaign. Use them for **cost-of-capability**, not case evidence.

## What is strong

- Strong market-availability source cluster.
- Shows modularisation of the automation stack: scraping APIs, rendering, proxy routing, CAPTCHA solving, temporary SMS, and managed services.
- Useful for explaining why automated abuse can scale even without elite technical skill.
- Useful complement to academic/technical capability sources.
- Good support for a “cost-of-capability” section of the evidence review.

## What is weak or limited

- Mostly vendor or vendor-adjacent material.
- Prices change frequently.
- Headline prices can be misleading because overage pricing, success rates, proxy quality, JavaScript rendering, anti-bot difficulty, and developer time vary heavily.
- Vendor claims about compliance, ethics, success rate, uptime, or benchmarking are not independent evidence.
- The sources do not prove malicious use, abuse prevalence, or effectiveness against protected targets.
- CAPTCHA and SMS sources are high dual-use and should be treated especially carefully.

## Framing distance

- **What real-world bot/abuse problem does this source cluster approximate?**  
  The economics and modular supply chain for automation: how a person or organisation can buy scraping, proxying, CAPTCHA-solving, and verification-enablement inputs rather than building everything.

- **What does it fail to represent?**  
  It does not represent actual abuse, attacker intent, target harm, or defensive success/failure. It also does not validate that the listed services work against any specific target or are legally/ethically acceptable.

- **What additional evidence would be needed to go further?**  
  Abuse incident reports, enforcement cases, platform telemetry, bot-management telemetry, independent provider audits, transparency reports, legal analysis, and controlled benchmarking under authorised conditions.

## What it cannot show

- It cannot show abuse prevalence.
- It cannot show legality or compliance.
- It cannot show whether residential proxies are consent-based.
- It cannot show whether CAPTCHA solving works on a specific site.
- It cannot show whether SMS verification succeeded in abuse workflows.
- It cannot show bot-detection effectiveness.
- It cannot show that lower price equals higher threat.
- It cannot replace case evidence such as Ticketmaster/Prestige or threat-research sources such as Bitsight.

## Project impact

Use this as a **core cost-of-capability / commercial ecosystem entry**.

Best uses:

- support a review section on automation economics;
- explain that automated abuse can be assembled from commodity services;
- connect scraping/proxy/CAPTCHA/SMS components into one stack;
- contextualise why defenders cannot rely only on “this is technically hard” assumptions;
- support the point that market availability is different from observed abuse.

Do not use it as:

- provider recommendation;
- current price guide;
- abuse proof;
- legality/compliance evidence;
- operational how-to material;
- proof that specific services are malicious.

## Relationship to other register entries

- **Bitsight residential proxy + malware ecosystems**: stronger threat-infrastructure evidence. This cost-stack entry gives price/availability context.
- **Bright Data / Infatica proxy entries**: commercial supply-chain sources. This entry aggregates pricing/market signals across more providers.
- **Commercial CAPTCHA-solving API ecosystem**: this entry adds current price/capacity snapshot; the CAPTCHA ecosystem entry remains the more focused OAT-009 source.
- **Bhardwaj LLM scraping / Seiden AI web scrapers**: academic measurement sources for capability/retrieval. This entry adds market-cost context.
- **Ticketmaster / Prestige / scarce-resource cases**: case evidence for actual ticket/scalping abuse; this entry shows the wider commodity inputs that could support similar abuse.
- **OWASP OAT / Handbook**: use for threat-category mapping.

## Dual-use containment

High dual-use. The cluster includes pricing pages for scraping, proxies, CAPTCHA solving, and temporary SMS verification. Public review use should stay at the level of market structure, cost signals, and defensive implications. Avoid reproducing API calls, provider workflows, target examples, bypass instructions, full price matrices, or step-by-step setup instructions.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `commercial-automation-cost-stack-2026-scraping-proxies-captcha-sms` |
| Title | *Commercial automation cost stack: scraping APIs, proxies, CAPTCHA solving, managed scraping, and SMS verification* |
| Organisations / sources | Apify/UseApify; The Web Scraping Club; Ficstar; Crawlbase; ScrapingBee; ZenRows; Bright Data; AIMultiple; Proxy-Cheap; CAPTCHA solver pricing page; 5SIM |
| Year | 2026 |
| Category | commercial automation ecosystem / cost-of-capability |
| Evidence basis | vendor pricing pages / vendor-adjacent comparison / industry survey / pricing snapshots |
| Operational proximity | market availability |
| Signals / techniques | scraping APIs; browser rendering; managed scraping; residential proxies; ISP/mobile proxies; CAPTCHA solving; temporary SMS; API credits; concurrency; geotargeting |
| Threat types | OAT-011 Scraping; OAT-009 CAPTCHA Defeat; OAT-019 Account Creation; indirect OAT-008 Credential Stuffing and scarce-resource automation |
| Scarce-resource abuse | Indirect cost-stack relevance only |
| Project use | Core source cluster for commercial availability and low/modular cost of automation inputs |
| Main caution | Pricing/vendor sources show availability and claimed capability, not abuse prevalence, legality, sourcing quality, or effectiveness |
| Entry file | `commercial-automation-cost-stack-2026-scraping-proxies-captcha-sms.md` |
