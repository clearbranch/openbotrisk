# Reading register

Bibliographic memory for the project. Anything substantive that informs the writing goes here: full reference, status, the extraction entry it maps to, and brief notes on relevance.

**Status codes:** `queued` / `reading` / `read` / `extracted`

**Sections** follow the four evidence-review categories (EVIDENCE-REVIEW.md §2): Foundations, Vendor and industry, Academic and research, Threat surface and territory. Sources read and rejected are recorded separately (§6), as are sources still queued.

**State:** 28 extraction entries exist — 26 in scope, 2 rejected. Duplicate uploads (Cloudflare bot-scores, DataDome) deduplicated to one entry each. `Entry` column gives the extraction filename; adjust the path prefix to wherever the per-source `.md` files live in the repo.

---

## Foundations

*Basic concepts the other sections assume. Pedagogical source material is still largely missing — see Queued.*

| Reference | Status | Entry | Notes |
|---|---|---|---|
| OWASP. *Automated Threats to Web Applications* (project page). | extracted | `owasp-automated-threats-to-web-applications.md` | OAT taxonomy spine for threat-type vocabulary. Project page only; full Handbook is a separate queued source. Taxonomy/ontology, not detection or prevalence evidence. |

---

## Vendor and industry

*Public material from bot/abuse-prevention companies. Treated as evidence of what the field claims, not independent proof.*

| Reference | Status | Entry | Notes |
|---|---|---|---|
| Cloudflare (2026). Bot scores, JA3/JA4, Detection IDs, Web Bot Auth, custom rules — Bots docs. | extracted | `cloudflare-2026-bot-scores-detection-engines-ja3-ja4-web-bot-auth-custom-rules.md` | Operational control-plane: score 1–99, detection engines, JA3/JA4 signals, Detection IDs, Web Bot Auth, WAF rule fields. Supports "Cloudflare exposes/uses X", not "X works". |
| Cloudflare (2026). Bot Management documentation. | extracted | `cloudflare-2026-bot-management-docs.md` | Product family (Bot Fight Mode → Enterprise) and bot-management variables exposed to WAF/Workers. Companion to the above. |
| DataDome (2025–2026). Bot Protect, AI Detection Engine, 2025 Global Bot Security Report. | extracted | `datadome-2025-2026-bot-protect-ai-detection-global-bot-security-report.md` | Intent-based detection framing; signal-family taxonomy. Report exposure figures (2.8% fully protected) are vendor-measured. Pair with FP-Inconsistent for external evidence on DataDome. |
| Netacea. *Bot Management* (product brochure). | extracted | `netacea-bot-management-product-brochure.md` | Server-side / no-client-JS positioning; two vendor-reported case studies. Product-positioning evidence. |
| Netacea. *Technical Showcase: ML in Advanced Bot Management.* | extracted | `netacea-technical-showcase-machine-learning.md` | ML methods taxonomy (supervised/unsupervised, real-time/batch, general/specific); Intent Analytics. No reproducible detail. |
| Netacea (2023). *Death by a Billion Bots.* | extracted | `netacea-2023-death-by-a-billion-bots.md` | 440-executive survey; business-impact framing ($85.6M/company). Survey evidence; origin/geopolitical claims out of scope. |
| Arkose Labs (2023–2026). Bot Manager, ACTIR, Agentic AI Security Report. | extracted | `arkose-2023-2026-bot-manager-actir-agentic-ai-reports.md` | Account-integrity + attacker-cost framing (dynamic challenges); agentic-AI survey reports. Vendor/survey; several reports gated. |
| Kasada (2025–2026). Bot Defense, Adversarial Techniques, AI Agent Trust, 2026 Benchmark. | extracted | `kasada-2025-2026-bot-defense-adversarial-retooling-ai-agent-trust.md` | Adversarial-retooling framing with solver/proxy/CAPTCHA pricing; proof-of-execution; AI-agent governance. Strong attacker-economy angle. |
| HUMAN Security / PerimeterX (2026). Sightline, AI Agent Detection, OpenClaw, 2026 benchmark. | extracted | `human-2026-sightline-bot-mitigation-ai-agent-detection-openclaw.md` | Cyberfraud-journey framing; concrete AI-agent detection signal categories; OpenClaw observations. Vendor/threat-intel. |

---

## Academic and research

*Peer-reviewed and pre-print work. No survey paper yet — see Queued; citation-network closure can't be assessed until one is in.*

| Reference | Status | Entry | Notes |
|---|---|---|---|
| Iliou, C. (2022). *ML-Based Detection and Evasion Techniques for Advanced Web Bots* (PhD thesis, Bournemouth). | extracted | `iliou-2022-thesis-advanced-web-bots.md` | Primary academic anchor. Sophistication taxonomy (simple→advanced); combined web-log + mouse detection; RL and GAN evasion. Controlled/academic setting. |
| Iliou et al. (2019). Towards a framework for detecting advanced Web bots (ARES). | extracted | `iliou-2019-ares-detecting-advanced-web-bots.md` | Cleanest source for "simple-bot results hide weak advanced-bot detection"; advanced-bot AUC ~0.68 at low FPR. Proxy labels. |
| Iliou et al. (2021). Web Bot Detection Evasion Using GANs (CSR). | extracted | `iliou-2021-csr-web-bot-detection-evasion-gans.md` | GAN evasion of CNN mouse/touch detectors; web mouse recall drops to ~0.45. Adversarial framing. |
| Iliou et al. (2022). Web Bot Detection Evasion Using Deep RL (ARES). | extracted | `iliou-2022-ares-web-bot-detection-evasion-deep-rl.md` | RL web-log evasion; detection/evasion as repeated game. PoC mechanism, not observed campaigns. |
| Venugopalan et al. (2025). FP-Inconsistent (arXiv 2406.07647). | extracted | `venugopalan-2025-fp-inconsistent-fingerprint-inconsistencies-evasive-bot-traffic.md` | Strongest operational academic anchor: purchased evasive bot traffic vs DataDome/BotD on a honey site; inconsistency rules. Threat model is impression fraud. |
| Iqbal et al. (2021). FP-Inspector (IEEE S&P). | extracted | `iqbal-2021-fingerprinting-the-fingerprinters-fp-inspector.md` | Detecting fingerprinting scripts (static+dynamic JS). Foundations for the fingerprinting section; not direct bot-detection evidence. |
| Andriamilanto et al. (2021). Browser fingerprints for web authentication (ACM TWEB). | extracted | `andriamilanto-2021-large-scale-browser-fingerprints-web-authentication.md` | Fingerprint distinctiveness/stability at scale. Auth context, not bots; 2016–17 data, needs replication caveat. |
| Jarad & Bıçakcı (2026). Detecting Bad Bots via TLS Fingerprints (arXiv 2602.09606). | extracted | `jarad-2026-handshakes-tell-truth-tls-fingerprints-ja4-bad-bots.md` | JA4/TLS classification (XGBoost/CatBoost, AUC ~0.998). Headline metrics strong but labelling ("bot" in app field) is a real caveat. |
| Acien et al. (2021). BeCAPTCHA-Mouse (arXiv 2005.00890). | extracted | `acien-2021-becaptcha-mouse-synthetic-mouse-trajectories.md` | Mouse-dynamics detection + synthetic (function/GAN) trajectories; public benchmark. Constrained point-and-click task. |
| Akrout et al. (2019). Hacking reCAPTCHA v3 using RL (arXiv 1903.01003). | extracted | `akrout-2019-recaptcha-v3-reinforcement-learning.md` | RL mouse-movement vs reCAPTCHA v3 score. 2019 PoC against one setup; narrow, likely stale. |

---

## Threat surface and territory

*Automation supply-side and attacker-mental-model material. Capability/infrastructure evidence, not proof of malicious use or bypass success.*

| Reference | Status | Entry | Notes |
|---|---|---|---|
| Playwright / Puppeteer / Selenium (2026). Official documentation. | extracted | `playwright-puppeteer-selenium-2026-browser-automation-docs.md` | Baseline automation capability layer; sits beneath the stealth/cloud layers in the taxonomy. Capability, not intent. |
| ultrafunkamsterdam (2021–2024). undetected-chromedriver (GitHub/PyPI). | extracted | `ultrafunkamsterdam-2024-undetected-chromedriver-docs-github.md` | Selenium ChromeDriver evasion layer; explicit IP-reputation caveat from the maintainer. README claims, not independent tests. |
| Berstend (2018–2023). puppeteer-extra-plugin-stealth (GitHub/npm). | extracted | `berstend-2023-puppeteer-extra-plugin-stealth-docs-github.md` | Modular evasion catalogue (webdriver, plugins, codecs, WebGL, etc.) for Puppeteer/Playwright. Passes public bot tests ≠ production. |
| ScrapFly (2025–2026). Anti-scraping bypass, stealth, proxies, fingerprints, Cloudflare bypass. | extracted | `scrapfly-2025-2026-anti-scraping-bypass-stealth-proxies-fingerprints.md` | API-level bypass (`asp`); byte-perfect JA4/HTTP2/QUIC claims; documents the attacker mental model for Cloudflare. Names Nodriver/Camoufox/UC Mode internally. |
| Bright Data (2026). Web Unlocker, Browser API, proxies, agentic web execution. | extracted | `brightdata-2026-web-unlocker-browser-api-proxies-anti-bot-bypass.md` | Managed proxies/fingerprints/CAPTCHA + cloud browsers; compliance/public-data framing, password entry disabled by default. |
| Browserless / Browserbase / Hyperbrowser (2026). Cloud-browser & agent docs. | extracted | `browserless-browserbase-hyperbrowser-2026-cloud-browser-agent-automation-docs.md` | Cloud browsers + AI-agent infra; stealth, proxies, CAPTCHA-solving, persistent sessions as features. Bridges automation to agentic browsers. |

---

## Read and rejected

*Recorded so they aren't re-read (§6). Both are title-collision retrieval artifacts — "Actions Speak Louder than Words" papers pulled in by string match, unrelated to bots.*

| Reference | Status | Entry | Reason rejected |
|---|---|---|---|
| Kwiatek et al. (2018). Loyalty Program Building Blocks (*Economics and Sociology*). | extracted | `kwiatek-2018-actions-speak-louder-loyalty-program-building-blocks.md` | Marketing/consumer-perception study. No bot/abuse content. Out of scope; keep only if a loyalty-abuse adjacency is later added. |
| Healey et al. (2018). Figurative Language & Gesturing in Entrepreneurial Pitches (*AMJ*). | extracted | `healey-2018-actions-speak-louder-than-words-entrepreneurial-pitches.md` | Communication/persuasion study. No bot/abuse content. Out of scope; possible use only for a dissemination/communication note. |

---

## Queued

*Not yet read.*

### Pre-existing

| Reference | Category | Status | Notes |
|---|---|---|---|
| OWASP Automated Threat Handbook (full). | foundations / threat-surface | queued | Detailed definitions, symptoms, mitigations behind the project-page summary. Read end-to-end in Phase 0. |
| Imperva Bad Bot Report (annual). | vendor | queued | Annual prevalence/trend report. |
| F5 Labs reports. | vendor | queued | — |

### Identified gaps (first-batch review — suggestions, prune freely)

| Reference / area | Category | Status | Why flagged |
|---|---|---|---|
| Browser-fingerprinting survey (e.g. Laperdrix et al., ACM TWEB). | academic | queued | §4/§9 say start with surveys; none in register, so closure can't be judged. |
| Bot-detection technique survey (classified by data source: network / fingerprint / behavioural). | academic | queued | Same — the academic backbone for closure testing. |
| Foundations primers: MDN, relevant RFCs, PortSwigger Web Security Academy. | foundations | queued | Foundations site section (§6 output) currently has no pedagogical sources. |
| Anthropic Claude-in-Chrome safety material; OpenAI agent material. | vendor / threat-surface | queued | AI agents currently seen only through defender-vendor framing; no agent-builder primary source. |
| Akamai, Imperva, F5 (WAF/appsec) technical docs. | vendor | queued | WAF angle named in §2.2 but absent. |
| niespodd/browser-fingerprinting GitHub catalogue. | threat-surface | queued | Named in §2.4; only referenced indirectly so far. |
| Anti-detect browsers (Multilogin, GoLogin, Camoufox); Nodriver; SeleniumBase UC Mode. | threat-surface | queued | Currently mentioned inside the ScrapFly entry, not extracted as their own category. |
