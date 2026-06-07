# Bhardwaj et al. (2026) - Beyond BeautifulSoup: benchmarking LLM-powered web scraping for everyday users

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded arXiv PDF `2601.06301v1.pdf`.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.
- **Source handling decision**: keep as a standalone entry. This is directly relevant to the project because it measures how LLM-assisted scripting and end-to-end agents lower the skill barrier for scraping, including authentication, anti-bot, and CAPTCHA contexts.

## Bibliographic

- **Citation**: Bhardwaj, A., Diwan, N., & Wang, G. (2026). *Beyond BeautifulSoup: Benchmarking LLM-Powered Web Scraping for Everyday Users*. arXiv:2601.06301v1. Posted 9 January 2026.
- **Source URL or path**: uploaded PDF `2601.06301v1.pdf`.
- **Publication status**: arXiv preprint. Treat as not peer-reviewed unless later venue publication is confirmed.
- **Category**: academic
- **Evidence basis**: empirical-benchmark / method comparison / preprint
- **Operational proximity**: measured-but-bounded — evaluates off-the-shelf LLM-assisted scraping workflows across 35 websites and five complexity tiers, but under constrained benchmark conditions and not as live abuse telemetry.
- **Tags**: LLM-scraping, web-scraping, LLM-agents, agentic-browsing, novice-users, scraping-democratization, BeautifulSoup, Scrapy, Claude, Simular.ai, authentication, MFA, CAPTCHA, anti-bot, browser-automation, OAT-011, OAT-009, capability-amplification

## What it claims

- LLMs and consumer-facing agents have lowered the skill barrier for web scraping.
- Historically, effective scraping required technical knowledge of HTML parsing, request handling, session management, authentication, and anti-bot circumvention.
- LLM-assisted scripting lets users generate scraping scripts while manually executing and debugging them.
- End-to-end LLM agents can navigate websites, fill forms, handle dynamic content, and extract data with less manual coding.
- For static websites, traditional scraping tools assisted by LLMs are still faster and often more efficient.
- For dynamic, authentication-heavy, or protected sites, end-to-end agents can succeed where basic BeautifulSoup/Scrapy workflows fail.
- CAPTCHA remains difficult: agent success on CAPTCHA benchmark sites is low compared with other categories.
- The authors frame this as a democratization problem: even low-skill users can attempt workflows that previously required specialist scraping knowledge.

## What evidence it provides

This is an **empirical benchmark of low-skill/off-the-shelf scraping workflows**.

It provides:

- a benchmark across 35 websites;
- five website difficulty tiers:
  - simple HTML;
  - complex HTML;
  - simple authentication;
  - complex authentication;
  - CAPTCHA;
- two workflow families:
  - LLM-assisted scripting (LAS), where the LLM generates code but the user executes/debugs;
  - end-to-end LLM agent (ELA), where the agent navigates and extracts through integrated tools;
- four evaluated tools/approaches:
  - BeautifulSoup with LLM-assisted scripting;
  - Scrapy with LLM-assisted scripting;
  - Claude as a tool-enabled agent;
  - Simular.ai as a visual/browser agent;
- metrics:
  - extraction success rate;
  - execution time;
  - manual effort required;
  - failure/error categories.

It does **not** provide:

- production abuse telemetry;
- evidence of malicious scraping campaigns;
- independent anti-bot bypass evaluation;
- evidence that agents defeat real-world protected sites reliably;
- legal or terms-of-service analysis;
- current commercial bot-management effectiveness evidence;
- a complete taxonomy of agentic abuse.

## Key quantitative details

### Extraction success rate

| Category | BeautifulSoup | Scrapy | Claude | Simular.ai |
|---|---:|---:|---:|---:|
| Simple HTML | 0.93 | 0.82 | 1.00 | 1.00 |
| Complex HTML | 0.80 | 0.20 | 0.57 | 1.00 |
| Simple Authentication | Not supported | Not supported | 0.20 | 0.63 |
| Complex Authentication | Not supported | Not supported | 0.12 | 0.70 |
| CAPTCHA | Not supported | Not supported | 0.05 | 0.10 |

### Main interpretation

- Traditional LLM-assisted scripting performs well and quickly for static/simple content.
- End-to-end agents are slower but more capable on dynamic, authentication, and protected workflows.
- CAPTCHA performance remains low, even for agents.
- Simular.ai performs best overall in this benchmark, especially on complex HTML and authentication categories.
- Claude performs well on simple HTML but much worse on authentication and CAPTCHA categories.

## Important visual/source evidence

- **Figure 1 / page 2** shows the benchmark design: LLM-assisted scripting has a prompt-to-code-to-execution loop with manual refinement, while end-to-end agents receive a goal prompt and act through production agent tooling.
- **Table 1 / page 5** classifies sites across five tiers by technical complexity and authentication/protection requirements.
- **Table 2 / page 5** reports extraction success rates by tool and category.
- **Table 3 / page 6** reports manual effort, showing traditional tools become unsupported for auth/CAPTCHA categories while agents remain usable but higher effort.
- **Figure 2 / page 6** reports execution time, showing the trade-off: traditional tools are much faster on simple/static sites, while agents are slower but handle more complex flows.
- **Appendix / page 9** includes benchmark prompts. These should not be reproduced in the register or public review because they are operationally useful.

## Signals or techniques mentioned

- LLM-assisted scraping;
- end-to-end LLM agents;
- natural-language task prompting;
- code generation;
- BeautifulSoup;
- Scrapy;
- Claude;
- Simular.ai;
- browser automation;
- visual page interpretation;
- dynamic JavaScript content;
- authentication workflows;
- email/MFA workflow handling;
- session/cookie handling;
- CAPTCHA challenge attempts;
- rate limiting;
- Cloudflare;
- anti-bot checks;
- structured extraction to CSV;
- retries and error checking;
- manual prompt refinement;
- novice-user capability;
- scraping democratization.

## Threat types covered

Directly relevant:

- web scraping capability;
- agentic web automation;
- low-skill capability amplification.

OAT mapping:

- **OAT-011 Scraping** — primary mapping. The paper is explicitly about web data extraction.
- **OAT-009 CAPTCHA Defeat** — partial mapping. CAPTCHA is included as a benchmark tier, but success rates are low.
- **OAT-019 Account Creation / account workflows** — indirect relevance where agents handle login/account flows, but the paper does not focus on registration abuse.
- **OAT-008 Credential Stuffing** — indirect only; authentication workflows are evaluated, but credential stuffing is not.
- **OAT-006 Expediting** — indirect, where agents automate multi-step human workflows.
- **OAT-005 Scalping / OAT-013 Sniping / OAT-021 Denial of Inventory** — indirect only; the evaluated capability could apply to scarce-resource workflows but the paper does not test them.

## What is strong

- Strong current source for the **LLM/agentic scraping capability** strand.
- Useful because it measures novice/off-the-shelf use rather than expert-optimised performance.
- Good complement to scraper/vendor sources:
  - vendor sources show commercial capability and market framing;
  - this source measures what low-skill users can do with general LLM tools.
- Useful evidence for the claim that LLM agents shift the scraping threat model from “skilled developer” to “prompt-and-refine user”.
- Provides clear comparative results across static, dynamic, authentication, and CAPTCHA tiers.
- Useful for balancing claims:
  - agents are not universally better;
  - traditional scripts remain faster on static pages;
  - CAPTCHA remains hard;
  - authentication/dynamic flows are where agents add most value.
- Good bridge to OpenClaw/agentic traffic sources and CAPTCHA/solver sources.

## What is weak or limited

- arXiv preprint, not confirmed peer-reviewed.
- Benchmark is small: 35 sites, one hardware environment, specific tool versions, and three trials per site.
- Some site choices involve real commercial platforms; the paper’s benchmark design may not generalise to all protected sites.
- CAPTCHA tests use demo/test environments to ensure reproducibility, not live production challenge systems.
- “Not supported” for BeautifulSoup/Scrapy means not reasonably completed with the basic prompts/workflows used, not impossible for an expert.
- The benchmark measures accessibility and success, not legality, ethics, stealth, scale, or defender outcomes.
- It does not measure modern anti-bot platform detection precision/recall.
- It does not test advanced adversaries using proxies, CAPTCHA solvers, browser-fingerprint alignment, residential IPs, or custom browser automation.
- It includes operational prompts and workflow detail, which should not be reproduced in the project.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  Low-skill users using LLMs and agents to perform web scraping and multi-step website interaction, including authentication and challenge-protected contexts.

- **What does it fail to represent?**  
  It does not represent sustained malicious campaigns, industrial scraping, proxy-enabled abuse, commercial solver integration, stealth, account farms, or adversarial adaptation against a named anti-bot vendor.

- **What additional evidence would be needed to go further?**  
  Larger independent benchmarks; production anti-bot telemetry; studies of agentic traffic at scale; controlled tests with proxies and browser-fingerprint alignment; legal/ethical analysis; and incident reports involving LLM/agentic scraping.

## What it cannot show

- It cannot show scraping-abuse prevalence.
- It cannot show that LLM agents bypass production anti-bot systems reliably.
- It cannot show legality or terms-of-service compliance.
- It cannot show stealth or evasion effectiveness.
- It cannot show large-scale automation economics.
- It cannot show defender false positives or false negatives.
- It cannot replace vendor telemetry or real incident evidence.

## Project impact

Use this as a **core agentic-scraping benchmark entry**.

Best uses:

- support the claim that LLMs and agents lower the skill barrier for scraping;
- distinguish LLM-assisted scripting from end-to-end LLM agents;
- show where agents help most: dynamic content, authentication, and complex workflows;
- show limits: slower execution and poor CAPTCHA success;
- link agentic scraping to the broader bot/automation threat surface;
- support the “democratization of capability” part of the review.

Do not use it as:

- a how-to guide;
- proof of real-world malicious scraping;
- proof of production anti-bot bypass;
- legal guidance;
- evidence of full OAT coverage beyond scraping/CAPTCHA-adjacent contexts.

## Relationship to other register entries

- **OpenClaw / HUMAN and Bitsight agentic sources**: OpenClaw provides exposed-agent/observed-traffic case evidence; this paper provides benchmarked scraping capability for ordinary LLM/agent workflows.
- **Commercial CAPTCHA-solving API ecosystem**: commercial solvers handle CAPTCHA as a service; this paper shows general LLM agents still struggle with CAPTCHA benchmark sites.
- **ReCAP CAPTCHA-capable GUI agents**: ReCAP is specialised CAPTCHA-capable training; this paper evaluates general off-the-shelf agents and shows low CAPTCHA success.
- **ScrapingBee / Bright Data / proxy entries**: those are commercial infrastructure/capability sources; this paper is an academic benchmark of general LLM workflows.
- **Tschacher bot-detection architecture**: provides detection-stack context for why agents interacting through browsers complicate signal collection.
- **ASVS / NIST / API Security**: use for controls and authentication/session governance around protected workflows.
- **OWASP OAT / Handbook**: use OAT-011 Scraping and OAT-009 CAPTCHA Defeat for threat category mapping.

## Dual-use containment

High dual-use. The paper includes operational workflows, site tiers, prompts, and code references. In the register, keep only benchmark findings, capability framing, and defensive implications. Avoid reproducing prompts, target lists, code snippets, login workflows, CAPTCHA instructions, or tool-specific scraping procedures.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `bhardwaj-2026-beyond-beautifulsoup-llm-powered-web-scraping` |
| Title | *Beyond BeautifulSoup: Benchmarking LLM-Powered Web Scraping for Everyday Users* |
| Authors | Arth Bhardwaj; Nirav Diwan; Gang Wang |
| Year | 2026 |
| Category | academic |
| Evidence basis | empirical-benchmark / method comparison / preprint |
| Operational proximity | measured-but-bounded |
| Signals / techniques | LLM-assisted scripting; end-to-end LLM agents; BeautifulSoup; Scrapy; Claude; Simular.ai; authentication; MFA; CAPTCHA; anti-bot checks |
| Threat types | OAT-011 Scraping; partial OAT-009 CAPTCHA Defeat; indirect relevance to account/workflow automation |
| Project use | Core benchmark for LLM/agentic scraping and low-skill capability amplification |
| Main caution | Preprint and bounded benchmark; not live abuse telemetry, legal guidance, or production anti-bot bypass evidence |
| Entry file | `bhardwaj-2026-beyond-beautifulsoup-llm-powered-web-scraping.md` |
