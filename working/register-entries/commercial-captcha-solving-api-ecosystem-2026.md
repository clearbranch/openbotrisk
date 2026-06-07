# Commercial CAPTCHA-solving API ecosystem - CapSolver, Medium/CapSolver workflow, and HasData benchmark

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF captures:
  - `What Is a CAPTCHA Solving API_ How It Works and When to Use It.pdf`
  - `Solving modern CAPTCHA for AI Agent and Automation Workflow _ by Matthew Hayes _ Medium.pdf`
  - `We Benchmarked CAPTCHA Solving Services to Find the Best One - DEV Community.pdf`
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.
- **Source handling decision**: combine these into one entry. CapSolver is the main source; the Medium and DEV/HasData articles are supporting sources showing AI-agent framing and benchmark/tutorial culture.

## Bibliographic

### Main source

- **Citation**: Fujimoto, S. / CapSolver. (2026). *What Is a CAPTCHA Solving API? How It Works and When to Use It*. CapSolver Blog. Published 2 April 2026.
- **Source URL or path**: uploaded PDF `What Is a CAPTCHA Solving API_ How It Works and When to Use It.pdf`.

### Supporting sources

- **Citation**: Hayes, M. (2025). *Solving modern CAPTCHA for AI Agent and Automation Workflow*. Medium. Published 20 November 2025.
- **Source URL or path**: uploaded PDF `Solving modern CAPTCHA for AI Agent and Automation Workflow _ by Matthew Hayes _ Medium.pdf`.

- **Citation**: Skakun, V. / HasData. (2026). *We Benchmarked CAPTCHA Solving Services to Find the Best One*. DEV Community. Posted 16 February 2026; edited 18 February 2026.
- **Source URL or path**: uploaded PDF `We Benchmarked CAPTCHA Solving Services to Find the Best One - DEV Community.pdf`.

## Category and treatment

- **Category**: vendor / commercial CAPTCHA-solving ecosystem
- **Evidence basis**: capability-doc / vendor marketing / tutorial ecosystem / vendor-adjacent benchmark
- **Operational proximity**: capability — shows that CAPTCHA-solving APIs are openly marketed and integrated into automation workflows. It is not independent abuse prevalence, not defensive validation, and not proof that services work against target sites in the wild.
- **Tags**: CAPTCHA, CAPTCHA-solving-API, OAT-009, CAPTCHA-defeat, CapSolver, 2Captcha, CapMonster, Anti-Captcha, DeathByCaptcha, SolveCaptcha, Cloudflare-Turnstile, reCAPTCHA, Geetest, AWS-WAF, token-generation, automation, scraping, price-monitoring, SEO, automated-account-management, AI-agents, solver-market

## What the sources claim

### CapSolver source

- A CAPTCHA-solving API lets developers automate resolution of CAPTCHA challenges through programmatic requests.
- It works by sending CAPTCHA data, such as site keys or images, to a provider that returns a token or solution.
- Modern providers may use AI or human workers.
- CAPTCHA-solving APIs are framed as useful for large-scale scraping, price monitoring, automated account management, SEO/SERP workflows, and other automation tasks.
- The source lists challenge types including reCAPTCHA v2/v3, Cloudflare Turnstile, image-to-text CAPTCHA, Geetest, and AWS WAF CAPTCHA.
- CapSolver is presented as a provider handling reCAPTCHA and Cloudflare Turnstile among other challenges.

### Medium / Hayes source

- Modern anti-bot systems are described as behavioural and token-based rather than only puzzle/image-based.
- General AI agents are said to struggle because they lack low-level control over browser inputs, fingerprinting, timing, and network consistency.
- Specialised solvers are framed as token-generation systems that simulate a trusted browser session and return the output token.
- The article explicitly frames this around AI-agent and automation workflows.

### DEV / HasData source

- The article benchmarks five CAPTCHA-solving services:
  - 2Captcha;
  - CapMonster Cloud;
  - Anti-Captcha;
  - DeathByCaptcha;
  - SolveCaptcha.
- It frames latency and success rate as important for automation throughput and cost.
- It includes performance tables, cost calculations, integration complexity, and scripts.
- For this register, treat it only as evidence that benchmark/tutorial material exists and that practitioners compare services by latency, accuracy, cost, and integration complexity.

## What evidence it provides

This combined entry provides evidence of a **commercial CAPTCHA-solving ecosystem**:

- services openly market CAPTCHA solving as an API capability;
- CAPTCHA solving is tied to web scraping, price monitoring, SEO, account management, and automation workflows;
- modern challenge handling is often token-based rather than merely OCR/image solving;
- public tutorials and benchmarks discuss provider choice, latency, success rates, cost, and integration complexity;
- AI-agent automation is being explicitly linked to solver APIs because general agents may struggle with fingerprinting/timing/browser-trust layers.

It does **not** provide:

- independent proof of effectiveness;
- live abuse prevalence;
- controlled measurements against protected target sites;
- legality or terms-of-service compliance;
- defensive detection performance;
- transparent methods for vendor claims;
- a safe or complete view of the market.

## Important visual/source evidence

- **CapSolver page 1** visually frames the product as a “CAPTCHA Solving API” that sits between an automated client/API and human verification.
- **CapSolver page 3** contains a table of supported CAPTCHA types and use cases, including reCAPTCHA, Cloudflare Turnstile, image-to-text, Geetest, and AWS WAF.
- **Medium page 2** contains a table of common AI-agent automation failure modes: non-human fingerprinting, deterministic mouse input, missing token logic, and poor challenge adaptation.
- **Medium page 3** compares general AI agents with specialised solvers, framing specialised solvers as full-browser simulation plus token generation.
- **DEV/HasData page 1** shows a chart comparing CAPTCHA-solving services across CAPTCHA types; later pages include benchmark and tutorial material. The details are operational, so they should be summarised rather than reproduced.

## Signals or techniques mentioned

- CAPTCHA-solving APIs;
- image CAPTCHA solving;
- site key extraction;
- task creation;
- polling for task results;
- returned validation token;
- reCAPTCHA token;
- Turnstile token;
- `cf_clearance` cookie, as mentioned in the Medium source;
- Cloudflare Turnstile;
- reCAPTCHA v2/v3;
- Geetest;
- AWS WAF CAPTCHA;
- image-to-text CAPTCHA;
- token generation;
- browser validation;
- high-trust browser session simulation;
- device/browser fingerprinting;
- mouse cadence / motion patterns;
- timing irregularities;
- proof-of-work;
- network consistency;
- proxy quality and IP reputation;
- latency and success-rate benchmarking;
- cost per thousand / CPM framing.

## Threat types covered

Directly relevant to:

- OAT-009 CAPTCHA Defeat.

Indirectly relevant to:

- OAT-011 Scraping — explicitly through large-scale scraping and price monitoring.
- OAT-019 Account Creation — relevant through automated account management and registration workflows.
- OAT-008 Credential Stuffing — relevant when CAPTCHA is used to protect login flows, though not a main topic.
- OAT-005 Scalping / OAT-013 Sniping / OAT-021 Denial of Inventory — relevant where CAPTCHA protects high-demand transactional flows.
- OAT-016 Skewing — possible where automated activity needs to pass verification, but not directly evidenced here.

## What is strong

- Strong evidence that CAPTCHA solving exists as a commercial API market.
- Useful for the “CAPTCHA Defeat is a service ecosystem, not just a research idea” point.
- CapSolver provides plain-language market framing and challenge-type coverage.
- The Medium source adds the AI-agent angle: modern anti-bot systems require browser trust, timing, fingerprinting, and token handling, not just image recognition.
- The DEV/HasData source adds evidence that practitioners publicly benchmark services on speed, success rate, cost, and integration complexity.
- Good complement to the ReCAP academic source:
  - ReCAP = model/training/benchmark capability;
  - commercial entry = market/API/workflow capability.

## What is weak or limited

- Highly vendor-adjacent and marketing-heavy.
- CapSolver and Medium/CapSolver framing should not be treated as independent evidence.
- The DEV/HasData benchmark is not necessarily independent of commercial interests and is operationally detailed.
- The sources do not prove that solvers work reliably against real protected sites.
- Success-rate, speed, and market-size claims should not be treated as externally verified.
- The sources contain procedural details and code that should not be reproduced in the register.
- The sources do not quantify abuse prevalence.
- They do not prove that solver use is lawful, ethical, or accepted under target-site terms.
- They do not show how defenders detect or mitigate solver use.

## Framing distance

- **What real-world bot/abuse problem do these sources approximate?**  
  The commercial service layer for CAPTCHA Defeat: outsourcing CAPTCHA challenge handling to APIs that return text or validation tokens for automation workflows.

- **What do they fail to represent?**  
  They do not show actual hostile campaigns, observed abuse volume, success against specific protected targets, or full anti-bot bypass. They mostly represent marketed capability and practitioner tutorial/benchmark culture.

- **What additional evidence would be needed to go further?**  
  Independent solver evaluations; defensive telemetry; honeypot data; abuse-case studies; provider transparency reports; legal/enforcement cases; and controlled tests against owned systems with full server-side logging.

## What it cannot show

- It cannot show CAPTCHA-solving abuse prevalence.
- It cannot show that any named solver works against a given production target.
- It cannot show legality or terms compliance.
- It cannot show full bot-management bypass.
- It cannot show defender detection precision/recall.
- It cannot show whether claims about market size, accuracy, or speed are reliable.
- It cannot replace academic or defensive evidence.

## Project impact

Use this as the **commercial CAPTCHA-solving ecosystem entry**.

Best uses:

- explain that CAPTCHA solving can be bought as an API service;
- show the shift from image solving to token-based workflows;
- connect CAPTCHA Defeat to scraping, price monitoring, SEO, account automation, and AI-agent workflows;
- contrast commercial solvers with ReCAP-style trained GUI agents;
- explain why CAPTCHA should be treated as friction rather than a complete anti-automation defence;
- support the OAT-009 CAPTCHA Defeat section.

Do not use it as:

- a how-to guide;
- proof of bypass effectiveness;
- prevalence evidence;
- legal guidance;
- independent benchmark evidence;
- justification to reproduce code or token-injection instructions.

## Relationship to other register entries

- **Chen et al. ReCAP**: academic model-based CAPTCHA-solving capability.
- **Cloudflare Turnstile**: defensive challenge-system source.
- **OWASP Automated Threat Handbook**: OAT-009 CAPTCHA Defeat category.
- **ScrapingBee / Bright Data / proxy entries**: CAPTCHA solvers are often paired with proxies and browser automation in scraping ecosystems.
- **OpenClaw / agentic automation entries**: AI-agent workflows may encounter CAPTCHA barriers and use solver services.
- **Martínez Llamas et al.**: detection/privacy/governance frame for signals such as fingerprints, timing, and behavioural data.
- **NIST / ASVS / PortSwigger**: use when CAPTCHA sits within authentication or account-abuse controls.

## Dual-use containment

High dual-use. These sources include provider names, workflows, benchmark scripts, and code. The register should preserve only capability, market, and governance-level points. Avoid reproducing API calls, payload formats, token-injection steps, benchmark scripts, target demo URLs, or provider-specific instructions.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `commercial-captcha-solving-api-ecosystem-2026` |
| Title | *Commercial CAPTCHA-solving API ecosystem: CapSolver, AI-agent workflows, and solver benchmarks* |
| Organisation / authors | CapSolver / Sora Fujimoto; Matthew Hayes; HasData / Valentina Skakun |
| Year | 2025–2026 |
| Category | vendor / commercial CAPTCHA-solving ecosystem |
| Evidence basis | capability-doc / vendor marketing / tutorial ecosystem / vendor-adjacent benchmark |
| Operational proximity | capability |
| Signals / techniques | CAPTCHA-solving API; token generation; reCAPTCHA; Turnstile; Geetest; AWS WAF; site keys; browser simulation; fingerprinting; timing; proxy quality; latency/success-rate benchmarking |
| Threat types | OAT-009 CAPTCHA Defeat; indirectly scraping, account creation, credential stuffing, scalping/sniping where CAPTCHA is a friction layer |
| Project use | Commercial ecosystem source for CAPTCHA Defeat services and AI-agent/automation integration framing |
| Main caution | High dual-use and vendor-adjacent; not independent abuse prevalence or bypass-effectiveness evidence |
| Entry file | `commercial-captcha-solving-api-ecosystem-2026.md` |
