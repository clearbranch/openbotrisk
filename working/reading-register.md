# Reading register

Bibliographic memory for the project. Anything substantive that informs the writing goes here: source reference, status, extraction entry, and brief notes on relevance.

**Status codes:** `queued` / `reading` / `read` / `extracted`.

**Sections** follow the four evidence-review categories (`EVIDENCE-REVIEW.md` §2): Foundations, Vendor and industry, Academic and research, Threat surface and territory. Sources read and rejected are recorded separately, as are sources still queued.

**State:** 55 extraction entries exist — 53 in-scope sources (`SRC-001`–`SRC-053`) and 2 rejected sources (`SRC-R01`–`SRC-R02`). This file was rebuilt from `evidence-register-updated-src041-053.qmd` on 2026-06-06. `Entry` gives the extraction filename; adjust the path prefix to wherever the per-source `.md` files live in the repo.

---

## Foundations

*Basic concepts the other sections assume. This section has improved, but still needs clean pedagogical primers for HTTP, cookies, sessions, TLS, browser fingerprints, and IP/network identity.*

| ID | Reference | Status | Entry | Notes |
|---|---|---|---|---|
| SRC-001 | OWASP (n.d.). *Automated Threats to Web Applications (project page)*. | extracted | `owasp-automated-threats-to-web-applications.md` | OAT taxonomy spine for threat-type vocabulary; project page only; full Handbook is now separate row `SRC-027`. Evidence: taxonomy; proximity: n/a (taxonomy). |
| SRC-027 | OWASP / Watson & Zaw (2026). *Automated Threat Handbook: Web Applications v1.3*. | extracted | `owasp-automated-threat-handbook-v1v3.md` | Full OAT Handbook taxonomy and countermeasure-class reference; provisional extraction produced without repo scope docs, so verify before citation Evidence: taxonomy; proximity: n/a (taxonomy). |
| SRC-028 | armanabbasi / Medium (2023). *How to Get and Use Cookies in Playwright*. | extracted | `medium-playwright-cookies-source-extraction.md` | Low-level foundations example showing browser automation can access and preserve cookie/session state Evidence: capability-doc; proximity: capability. |
| SRC-041 | ScrapingBee (2026). *Top 15 Scraper Sites to Enhance Your Data Collection Skills*. | extracted | `scrapingbee-2026-scraper-test-sites(1).md` | Low-priority foundations/context source for how scraping skills are taught and how vendors frame the move from sandbox practice to production scraping Evidence: capability-doc; proximity: capability (training / sandbox). |

---

## Vendor and industry

*Public material from bot/abuse-prevention companies and adjacent vendors. Treated as evidence of what the field claims, exposes, or observes, not independent proof of efficacy.*

| ID | Reference | Status | Entry | Notes |
|---|---|---|---|---|
| SRC-002 | Cloudflare (2026). *Bot scores, JA3/JA4, Detection IDs, Web Bot Auth, custom rules (Bots docs)*. | extracted | `cloudflare-2026-bot-scores-detection-engines-ja3-ja4-web-bot-auth-custom-rules.md` | Supports "Cloudflare exposes/uses X", not "X works" Evidence: capability-doc; proximity: capability. |
| SRC-003 | Cloudflare (2026). *Bot Management documentation*. | extracted | `cloudflare-2026-bot-management-docs.md` | Product-family and exposed-variable companion to SRC-002 Evidence: capability-doc; proximity: capability. |
| SRC-004 | DataDome (2025–2026). *Bot Protect, AI Detection Engine, 2025 Global Bot Security Report*. | extracted | `datadome-2025-2026-bot-protect-ai-detection-global-bot-security-report.md` | Intent-based framing; 2.8% "fully protected" is vendor-measured; pair with SRC-015 for external evidence Evidence: vendor-claim; threat-intel; proximity: observed (vendor-measured). |
| SRC-005 | Netacea (n.d.). *Bot Management (product brochure)*. | extracted | `netacea-bot-management-product-brochure.md` | Product-positioning evidence Evidence: vendor-claim; proximity: claimed. |
| SRC-006 | Netacea (n.d.). *Technical Showcase: ML in Advanced Bot Management*. | extracted | `netacea-technical-showcase-machine-learning.md` | ML-methods taxonomy; no reproducible detail Evidence: methods-taxonomy; proximity: capability. |
| SRC-007 | Netacea (2023). *Death by a Billion Bots*. | extracted | `netacea-2023-death-by-a-billion-bots.md` | Survey evidence; origin/geopolitical claims out of scope Evidence: survey; proximity: claimed (self-report). |
| SRC-008 | Arkose Labs (2023–2026). *Bot Manager, ACTIR, Agentic AI Security Report*. | extracted | `arkose-2023-2026-bot-manager-actir-agentic-ai-reports.md` | Account-integrity + attacker-cost angle; several reports gated Evidence: vendor-claim; survey; proximity: claimed. |
| SRC-009 | Kasada (2025–2026). *Bot Defense, Adversarial Techniques, AI Agent Trust, 2026 Benchmark*. | extracted | `kasada-2025-2026-bot-defense-adversarial-retooling-ai-agent-trust.md` | Strong attacker-economy angle Evidence: vendor-claim; threat-intel; proximity: observed (vendor-measured). |
| SRC-010 | HUMAN Security / PerimeterX (2026). *Sightline, AI Agent Detection, OpenClaw, 2026 benchmark*. | extracted | `human-2026-sightline-bot-mitigation-ai-agent-detection-openclaw.md` | Concrete AI-agent detection signal categories Evidence: vendor-claim; threat-intel; proximity: observed (vendor-measured). |
| SRC-034 | F5 Labs / Vinberg & Overson (2021). *2021 Credential Stuffing Report*. | extracted | `f5-2021-credential-stuffing-report.md` | Primary observed-use anchor for credential stuffing; combines spill-supply evidence with vendor-measured login abuse against large production sites Evidence: threat-intel; empirical-operational; proximity: observed (vendor-measured). |
| SRC-036 | HUMAN Security / Kaiserman & Cirlig (2026). *OpenClaw in the wild: How autonomous agents can drive abuse at scale*. | extracted | `human-2026-openclaw-in-the-wild(1).md` | Observed-use evidence for agentic browser automation abuse, with explicit attribution caveats Evidence: empirical-operational; proximity: observed (vendor-measured). |
| SRC-037 | HUMAN Security / McArtney (2026). *Agentic Visibility: How to See AI Agents in Your Traffic*. | extracted | `human-2026-agentic-visibility-how-to-see-ai-agent-traffic(1).md` | Product/capability framing for agentic visibility, trust classification, and the shift from visibility to control Evidence: capability-doc; proximity: capability. |
| SRC-038 | HUMAN Security / Kaiserman (2026). *State of Agentic Traffic – May 2026*. | extracted | `human-2026-state-agentic-traffic-may(1).md` | Current vendor-telemetry snapshot of agentic traffic patterns and route exposure, not proof of malicious intent Evidence: empirical-operational; proximity: observed (vendor-measured). |
| SRC-039 | Thales / Imperva (2026). *2026 Thales Bad Bot Report: Bad Bots in the Agentic Age*. | extracted | `thales-2026-bad-bot-report(1).md` | Broad vendor-measured snapshot of production bot, API, ATO, inventory, and AI-agent abuse; useful but not independent prevalence evidence Evidence: empirical-operational; threat-intel; proximity: observed (vendor-measured). |
| SRC-040 | Akamai Security (2026). *AI-Empowered Botnets and API Visibility Gaps: Attack Trends in Financial Services*. | extracted | `akamai-2026-financial-services-security-trends(1).md` | Vendor telemetry source for financial-services API/bot abuse and the public-data boundary; alerts are not proof of successful attacks Evidence: empirical-operational; proximity: observed (vendor-measured). |
| SRC-049 | DataDome / Falokun (2026). *How to Restore Fairness in Online Ticketing by Fighting Ticket Bots*. | extracted | `datadome-2026-ticket-bots(1).md` | Vendor taxonomy for ticket bots / slot-sniping and scarce-inventory abuse; useful when paired with FTC legal-record evidence Evidence: methods-taxonomy; proximity: claimed. |
| SRC-051 | StopBadBots / sminozzi (2025). *Comodo ModSecurity WAF Rules Update: The 2026 Solution / SBB-WAF-Rules*. | extracted | `stopbadbots-2025-sbb-waf-rules(1).md` | Defensive-tooling example for the simple WAF/blocklist/behavioural-threshold end of the control stack Evidence: tooling-readme; proximity: capability. |

---

## Academic and research

*Peer-reviewed, preprint, thesis, and technical-report work. Stronger than before, but still needs survey closure and citation-network checking.*

| ID | Reference | Status | Entry | Notes |
|---|---|---|---|---|
| SRC-011 | Iliou, C. (2022). *ML-Based Detection and Evasion Techniques for Advanced Web Bots (PhD thesis, Bournemouth)*. | extracted | `iliou-2022-thesis-advanced-web-bots.md` | Primary academic anchor; controlled/academic setting Evidence: empirical-academic; proximity: capability. |
| SRC-012 | Iliou et al. (2019). *Towards a framework for detecting advanced web bots (ARES)*. | extracted | `iliou-2019-ares-detecting-advanced-web-bots.md` | Cleanest source for "simple-bot results hide weak advanced-bot detection" Evidence: empirical-academic; proximity: capability. |
| SRC-013 | Iliou et al. (2021). *Web Bot Detection Evasion Using GANs (CSR)*. | extracted | `iliou-2021-csr-web-bot-detection-evasion-gans.md` | Adversarial framing Evidence: empirical-academic; proximity: capability. |
| SRC-014 | Iliou et al. (2022). *Web Bot Detection Evasion Using Deep RL (ARES)*. | extracted | `iliou-2022-ares-web-bot-detection-evasion-deep-rl.md` | PoC mechanism, not observed campaigns Evidence: empirical-academic; proximity: capability. |
| SRC-015 | Venugopalan et al. (2025). *FP-Inconsistent (arXiv 2406.07647)*. | extracted | `venugopalan-2025-fp-inconsistent-fingerprint-inconsistencies-evasive-bot-traffic.md` | Strongest operational academic anchor; external evidence on DataDome Evidence: empirical-operational; proximity: measured (honey-site). |
| SRC-016 | Iqbal et al. (2021). *FP-Inspector (IEEE S&P)*. | extracted | `iqbal-2021-fingerprinting-the-fingerprinters-fp-inspector.md` | Foundations for fingerprinting section; not direct bot-detection evidence Evidence: empirical-academic; proximity: n/a (not bot-use). |
| SRC-017 | Andriamilanto et al. (2021). *Browser fingerprints for web authentication (ACM TWEB)*. | extracted | `andriamilanto-2021-large-scale-browser-fingerprints-web-authentication.md` | Auth context not bots; 2016–17 data, needs replication caveat Evidence: empirical-academic; proximity: n/a (not bot-use). |
| SRC-018 | Jarad & Bıçakcı (2026). *Detecting Bad Bots via TLS Fingerprints (arXiv 2602.09606)*. | extracted | `jarad-2026-handshakes-tell-truth-tls-fingerprints-ja4-bad-bots.md` | Strong headline metrics; labelling ("bot" in app field) is a real caveat Evidence: empirical-academic; proximity: measured (weak labels). |
| SRC-019 | Acien et al. (2021). *BeCAPTCHA-Mouse (arXiv 2005.00890)*. | extracted | `acien-2021-becaptcha-mouse-synthetic-mouse-trajectories.md` | Constrained point-and-click task Evidence: empirical-academic; proximity: capability. |
| SRC-020 | Akrout et al. (2019). *Hacking reCAPTCHA v3 using RL (arXiv 1903.01003)*. | extracted | `akrout-2019-recaptcha-v3-reinforcement-learning.md` | 2019 PoC against one setup; narrow, likely stale Evidence: empirical-academic; proximity: capability. |
| SRC-033 | Wang, Shafiq & Vekaria (2026). *FP-Agent: Fingerprinting AI Browsing Agents*. | extracted | `wang-2026-fp-agent-fingerprinting-ai-browsing-agents.md` | Independent measured anchor for AI-agent detectability; external check of Cloudflare free-tier behaviour, not enterprise efficacy Evidence: empirical-academic; empirical-operational; proximity: measured (honey-site). |
| SRC-047 | Martínez Llamas et al. (2025). *Balancing Security and Privacy: Web Bot Detection, Privacy Challenges, and Regulatory Compliance under the GDPR and AI Act*. | extracted | `martinez-llamas-2025-web-bot-detection-privacy-gdpr-ai-act(1).md` | Academic taxonomy and compliance anchor for detection signals, evasion classes, privacy risks, and GDPR / AI Act implications Evidence: methods-taxonomy; proximity: capability. |
| SRC-048 | Wardle (2019). *How long does it take to get owned?*. | extracted | `wardle-2019-how-long-does-it-take-to-get-owned(1).md` | Independent measured-use evidence for leaked credential use and honey-account methodology; small and dated but transparent Evidence: empirical-academic; proximity: measured (honey identities). |

---

## Threat surface and territory

*Automation supply-side, operator-side, legal/enforcement, and attacker-mental-model material. Mostly capability/infrastructure evidence unless proximity says otherwise.*

| ID | Reference | Status | Entry | Notes |
|---|---|---|---|---|
| SRC-021 | project maintainers (2026). *Official documentation (Playwright / Puppeteer / Selenium)*. | extracted | `playwright-puppeteer-selenium-2026-browser-automation-docs.md` | Capability, not intent; sits beneath stealth/cloud layers Evidence: capability-doc; proximity: capability. |
| SRC-022 | ultrafunkamsterdam (2021–2024). *undetected-chromedriver (GitHub/PyPI)*. | extracted | `ultrafunkamsterdam-2024-undetected-chromedriver-docs-github.md` | README claims, not independent tests Evidence: tooling-readme; proximity: capability. |
| SRC-023 | berstend (2018–2023). *puppeteer-extra-plugin-stealth (GitHub/npm)*. | extracted | `berstend-2023-puppeteer-extra-plugin-stealth-docs-github.md` | "Passes public bot tests" ≠ production Evidence: tooling-readme; proximity: claimed. |
| SRC-024 | ScrapFly (2025–2026). *Anti-scraping bypass, stealth, proxies, fingerprints, Cloudflare bypass*. | extracted | `scrapfly-2025-2026-anti-scraping-bypass-stealth-proxies-fingerprints.md` | Documents the attacker mental model for Cloudflare Evidence: capability-doc; vendor-claim; proximity: claimed. |
| SRC-025 | Bright Data (2026). *Web Unlocker, Browser API, proxies, agentic web execution*. | extracted | `brightdata-2026-web-unlocker-browser-api-proxies-anti-bot-bypass.md` | Compliance/public-data framing Evidence: capability-doc; vendor-claim; proximity: claimed. |
| SRC-026 | respective vendors (2026). *Cloud-browser & agent docs (Browserless / Browserbase / Hyperbrowser)*. | extracted | `browserless-browserbase-hyperbrowser-2026-cloud-browser-agent-automation-docs.md` | Bridges automation to agentic browsers Evidence: capability-doc; proximity: capability. |
| SRC-029 | RoundProxies / Marius Bernard (2025). *How to Use Rnet: The Blazing-Fast Python HTTP Client*. | extracted | `roundproxies-rnet-source-extraction.md` | Scraper-side evidence that browser-like TLS/protocol impersonation is treated as a normal evasion capability Evidence: tooling-readme; capability-doc; proximity: capability. |
| SRC-030 | ScrapFly / Hisham (2026). *How to Bypass Cloudflare Turnstile*. | extracted | `scrapfly-cloudflare-turnstile-source-extraction.md` | Turnstile-specific scraper-side account of challenge-response signal families and bypass classes Evidence: tooling-readme; vendor-claim; capability-doc; proximity: claimed. |
| SRC-031 | ScrapFly / Bernardas Alisauskas (2026). *How to Bypass Imperva Incapsula when Web Scraping in 2026*. | extracted | `scrapfly-imperva-incapsula-source-extraction.md` | Imperva-specific scraper-side view of WAF/bot-protection detection surfaces and claimed evasion patterns Evidence: tooling-readme; capability-doc; vendor-claim; proximity: claimed. |
| SRC-032 | Wikimedia Foundation (2026). *Quo vadis, crawlers? Progress and what's next on safeguarding our infrastructure*. | extracted | `wikimedia-2026-quo-vadis-crawlers-infrastructure.md` | First named-operator account in the register; strong operator-side evidence for AI-crawler pressure and residential-proxy evasion, but platform-specific Evidence: empirical-operational; threat-intel; proximity: observed (first-party operator-reported). |
| SRC-035 | DVSA / Ryder (2023). *How we're dealing with bots and the reselling of driving tests*. | extracted | `dvsa-2023-bots-reselling-driving-tests.md` | Concrete public-sector appointment-abuse example for the booking-style worked example and scarce-resource abuse lane Evidence: threat-intel; proximity: observed (platform-side). |
| SRC-042 | ScrapingBee (2026). *Is Web Scraping Legal? Key Insights and Guidelines You Need to Know*. | extracted | `scrapingbee-2026-web-scraping-legal-guidelines(1).md` | Scraper-side governance framing around the boundary between technical capability and permission; verify legal claims against primary/specialist sources before use Evidence: legal-explainer; proximity: n/a (legal context; not use evidence). |
| SRC-043 | ScrapingBee (2026). *Advanced Web Scraping: Hidden Techniques Pro Developers Actually Use*. | extracted | `scrapingbee-2026-advanced-web-scraping-hidden-techniques(1).md` | Public scraper-side engineering-pattern source for robust extraction at scale; high dual-use, so cite technique families only Evidence: bypass-guide; proximity: capability. |
| SRC-044 | ScrapingBee (2026). *Best Price Scraping Tools for 2026: Top Services Compared*. | extracted | `scrapingbee-2026-price-scraping-tools(1).md` | Market-map evidence showing price scraping as packaged commercial service with anti-bot handling as a core buying criterion Evidence: capability-doc; proximity: capability. |
| SRC-045 | ScrapingBee / Krukowski (2026). *How To Bypass PerimeterX Anti-Bot Protection System In 2026*. | extracted | `scrapingbee-2026-perimeterx-human-bypass(1).md` | Public scraper-side evidence that named-defender bypass thinking is framed as multi-layer signal alignment across IP, TLS, HTTP, fingerprint, session, and behaviour Evidence: bypass-guide; proximity: capability. |
| SRC-046 | niespodd (n.d. / ongoing). *Avoiding bot detection: How to scrape the web without getting blocked? / browser-fingerprinting*. | extracted | `niespodd-browser-fingerprinting(1).md` | Public scraper-side/evasion mental model and tooling-ecosystem map; maintainer claims, not independent effectiveness evidence Evidence: tooling-readme; proximity: claimed. |
| SRC-050 | Federal Trade Commission (2021). *FTC Brings First-Ever Cases Under the BOTS Act*. | extracted | `ftc-2021-first-bots-act-cases(1).md` | High-value observed-use / enforcement evidence for ticket-bot abuse and limited-stock automation; cite as FTC allegations/orders unless underlying records are checked Evidence: legal-record; proximity: observed (enforcement record). |
| SRC-052 | Hamachek (n.d. (~2019–2020 unverified)). *bad-asn-list: open-source ASN blocklist for cloud/hosting/colo traffic*. | extracted | `hamachek-bad-asn-list-datacenter-asn-blocklist.md` | Worked example of network-origin / ASN-reputation detection and the datacenter-blocking → residential-proxy arms-race baseline; anecdotal and dated Evidence: tooling-readme; empirical-operational; proximity: observed (first-party anecdotal). |
| SRC-053 | ScrapingBee (2026). *The Best Web Scraping API to Avoid Getting Blocked*. | extracted | `scrapingbee-2026-web-scraping-api(1).md` | Commercial capability source showing scraping-as-a-service packaging of browsers, proxies, extraction, geotargeting, and anti-blocking features Evidence: capability-doc; proximity: capability. |

---

## Read and rejected

*Recorded so they are not re-read. Rejected sources are kept because the negative decision is itself useful project memory.*

| ID | Reference | Status | Entry | Reason rejected |
|---|---|---|---|---|
| SRC-R01 | Kwiatek et al. (2018). *Loyalty Program Building Blocks (*Economics and Sociology*)*. | extracted / rejected | `kwiatek-2018-actions-speak-louder-loyalty-program-building-blocks.md` | Marketing/consumer-perception study. No bot/abuse content. Out of scope; keep only if a loyalty-abuse adjacency is later added. |
| SRC-R02 | Healey et al. (2018). *Figurative Language & Gesturing in Entrepreneurial Pitches (*AMJ*)*. | extracted / rejected | `healey-2018-actions-speak-louder-than-words-entrepreneurial-pitches.md` | Communication/persuasion study. No bot/abuse content. Out of scope; possible use only for a dissemination/communication note. |

---

## Queued

*Not yet read or not yet extracted as a distinct source. This queue has been pruned so it no longer lists sources already represented by `SRC-027`, `SRC-034`, `SRC-039`, or `SRC-046`.*

### Highest-priority gaps

| Reference / area | Category | Status | Why queued |
|---|---|---|---|
| Foundations primers: MDN HTTP overview, HTTP headers, cookies, browser storage, CORS, user-agent strings; Cloudflare Learning Center for DNS/TLS/CDN basics; selected RFCs only where needed; PortSwigger Web Security Academy for sessions/authentication basics | foundations | queued | The Foundations section still needs accessible canonical material rather than relying on scraper/vendor sources. |
| Recent browser-fingerprinting survey, e.g. Laperdrix et al. / Gómez-Boix lineage plus newer survey material | academic | queued | Needed for citation-network closure around browser/device fingerprinting. |
| Recent web-bot-detection technique survey classified by data source: network, fingerprinting, behavioural/session, graph/entity | academic | queued | Needed as the academic backbone for detection-method coverage. |
| Independent in-the-wild bot, credential-stuffing, ad-fraud, fake-account, or scraping measurement studies | academic / threat-surface | queued | Observed-use lane remains thinner than capability/vendor evidence; independent measurement is highest value. |
| Victim/operator engineering postmortems from platforms affected by scraping, credential stuffing, account creation, booking abuse, or crawler pressure | threat-surface | queued | Balances vendor telemetry with first-party target/operator accounts. |
| Primary legal/enforcement records: BOTS Act complaints/orders, UK ticketing/consumer-law material, DVSA booking terms, regulator guidance where legal claims become load-bearing | legal-record / governance | queued | Vendor legal explainers are not enough for legal claims. |

### Useful but second-order

| Reference / area | Category | Status | Why queued |
|---|---|---|---|
| OpenAI agent / Operator documentation and safety material; Anthropic Claude computer-use / browser-use material; Browser Use and Skyvern docs | vendor / threat-surface | queued | Needed to represent agent-builder framing rather than only defender-vendor framing. |
| Akamai, Imperva/Thales, F5 technical docs for bot management, WAF controls, API-security controls, and exposed rule/score/control-plane fields | vendor | queued | Reports exist, but the technical control-plane layer is still incomplete. |
| Anti-detect browsers and stealth tooling as distinct entries: Multilogin, GoLogin, Camoufox, Nodriver, SeleniumBase UC Mode | threat-surface | queued | Currently mostly present through secondary mentions and catalogues, not their own source entries. |
| Browser-extension and userscript automation material: Tampermonkey/userscripts, browser add-ons used for page monitoring or form automation | threat-surface | queued | Important for the “individual tool running inside the browser” / slot-sniping argument. |
| Public datasets for methodology investigations: ad-fraud, clickstream, login/session, credential-stuffing proxies, web-log, fraud graph datasets | methodology / academic | queued | Needed to connect the written review to reproducible public-data investigations and to state framing distance clearly. |
| Additional Cloudflare Radar / AI crawler / bot traffic reports | vendor telemetry | queued | Potential observed vendor-telemetry complement to Thales, HUMAN, F5, Akamai, and Wikimedia. |

### Recently resolved from the old queue

| Old queued item | Resolved by | Note |
|---|---|---|
| OWASP Automated Threat Handbook full source | SRC-027 | Now extracted; still marked needs review because the extraction was provisional. |
| Imperva Bad Bot Report annual | SRC-039 | Covered via 2026 Thales / Imperva Bad Bot Report. |
| F5 Labs reports | SRC-034 | Credential-stuffing report extracted; further F5 technical docs can still be queued separately if needed. |
| niespodd/browser-fingerprinting GitHub catalogue | SRC-046 | Now extracted as its own threat-surface source. |
| Akamai financial-services report | SRC-040 | Vendor telemetry report extracted; technical docs remain queued separately. |
| Ticket-bot / scarce-resource enforcement example | SRC-050 | FTC BOTS Act source added; more primary legal records can still be useful. |

