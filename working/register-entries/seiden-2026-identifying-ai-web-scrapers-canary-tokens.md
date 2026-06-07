# Seiden et al. (2026) - Identifying AI web scrapers using canary tokens

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded arXiv PDF `2605.13706v1.pdf`; updated project scope files `EVIDENCE-REVIEW(5).md` and `evidence-register(8).qmd` were available for context.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, dual-use containment, and the observed-use lane.
- **Source handling decision**: keep as a standalone academic/measurement entry. This is related to the previous LLM-powered scraping benchmark but stronger on observed AI-scraper infrastructure because it uses deployed canary-token websites and production AI chatbot outputs.

## Bibliographic

- **Citation**: Seiden, S., Ren, T., Zhang, C., Kim, T., Liu, E., & Wenger, E. (2026). *Identifying AI Web Scrapers Using Canary Tokens*. arXiv:2605.13706v1. Posted 13 May 2026.
- **Source URL or path**: uploaded PDF `2605.13706v1.pdf`.
- **Publication status**: arXiv preprint. Treat as not peer-reviewed unless later publication is confirmed.
- **Category**: academic / threat-surface measurement
- **Evidence basis**: empirical-measurement / canary-token honeysite study / preprint
- **Operational proximity**: measured — deploys real websites, observes visiting scraper User-Agents/ASNs, then queries production AI chatbots and matches returned canary tokens to scraper identities. It is not merely capability evidence, although it is still a controlled measurement rather than victim-site telemetry.
- **Tags**: AI-scraping, LLM-scraping, AI-web-scrapers, canary-tokens, honeysites, User-Agent, ASN, robots.txt, search-engine-crawlers, caching, real-time-content-retrieval, RAG, web-search, AI-chatbots, scraper-identification, OAT-011, observed-use, measurement

## What it claims

- Web data feeds AI systems in at least two ways:
  - pretraining/fine-tuning;
  - inference-time retrieval through search, RAG, cached indexes, or live web access.
- Site owners who want to restrict AI-related scraping first need to identify which scrapers feed which AI systems.
- Existing identification methods rely heavily on self-declared User-Agent strings, company disclosures, one-off tests, or crowdsourced reports; these are incomplete and not fully reliable.
- Canary-token websites can be used to infer which scrapers supply data to which AI chatbots.
- Many AI chatbots do not use only clearly declared AI-specific User-Agents; some appear to rely on search-engine crawlers, generic browser User-Agents, or many rotating generic User-Agent strings.
- Search-engine-based retrieval adds opacity: a chatbot may return content originally served to Googlebot, Bingbot, Bravebot, Baiduspider, or similar crawlers rather than content retrieved directly by an AI-branded crawler.
- Taking a site offline or adding `robots.txt` restrictions may not remove already-retrieved content from AI chatbot outputs, partly because search indexes or chatbot-side caches may retain content.
- User-Agent-based blocking is therefore insufficient where AI systems obtain content through third-party search indexes or opaque scraper chains.

## What evidence it provides

This is an empirical measurement paper using controlled websites and production AI chatbots.

It provides:

- 20 purchased `.com` domains with no recent ICANN history;
- one controlled website per domain;
- website templates containing 10 canary-token placeholders each;
- per-scraper canary-token assignment, where a scraper identity is defined as a unique `(User-Agent, ASN)` pair;
- canary tokens generated from large enough token spaces to reduce accidental matches;
- two-month waiting period to allow indexing/scraping before initial chatbot queries;
- 22 production AI chatbots tested;
- three site-accessibility conditions:
  1. fully accessible;
  2. taken offline;
  3. blocked using `robots.txt`;
- repeated chatbot queries after condition changes;
- token extraction and matching to infer which scraper identities fed which AI chatbot outputs.

## Key quantitative details

| Measure | Reported value |
|---|---:|
| Controlled websites | 20 |
| Canary tokens per site template | 10 |
| Production AI chatbots studied | 22 |
| Initial wait before querying | 2 months |
| Experimental stages | online, offline/robots.txt, restored online |
| Unique User-Agent strings across sites | 2,765 |
| Unique ASNs across sites | 549 |
| Unique visitors across sites | 4,042 |
| Average unique visitors per site | 592.2 |
| Minimum unique visitors on a site | 313 |
| Maximum unique visitors on a site | 674 |
| Matching thresholds | at least 2 tokens or at least 1 website interaction, as implemented by the authors |

The paper’s own summary findings include:

- some AI chatbots returned content associated with search-engine scrapers;
- several systems used or appeared connected to generic browser User-Agents;
- cached or indexed content could still appear after sites were taken offline;
- `robots.txt` was often ineffective at removing already-observed website data from AI chatbot responses.

## Important visual/source evidence

- **Figure 1 / page 3** gives the high-level flow for real-time content retrieval: a website is published; an AI chatbot receives a query; content is pulled from cached/indexed data or scraped directly; the response can include webpage data.
- **Figure 2 / page 5** shows the canary-token measurement pipeline: deploy websites with scraper-specific canary tokens, query AI chatbots, then infer which scraper fed the chatbot from tokens in outputs.
- **Figure 3 / page 8** shows the three-stage measurement timeline: online baseline, offline/robots.txt conditions, and restored-online follow-up.
- **Table 1 / page 7** lists the 22 AI chatbots studied.
- **Table 2 / page 8** reports visitor statistics across the controlled websites.
- Later result tables map AI systems to measured User-Agent categories and accessibility conditions. Treat provider-specific mappings carefully because the paper is a preprint and because the project is methods-first rather than vendor-ranking.

## Signals or techniques mentioned

- canary tokens;
- honeysite measurement;
- dynamic content serving;
- per-scraper token assignment;
- User-Agent strings;
- Autonomous System Number / ASN;
- scraper identity as `(User-Agent, ASN)`;
- search-engine crawlers;
- generic browser User-Agents;
- first-party declared agents;
- third-party search agents;
- cached indexed content;
- live retrieval;
- retrieval-augmented generation / RAG;
- query-time web search;
- `robots.txt`;
- Robots Exclusion Protocol;
- taking sites offline;
- token extraction by regex/string matching;
- token collision handling;
- discarding ambiguous token matches;
- User-Agent spoofing risk;
- IP/TLS/browser fingerprinting as possible extensions.

## Threat types covered

Directly relevant:

- AI-related web scraping;
- LLM/AI chatbot content retrieval;
- scraper identification and attribution;
- unwanted content retrieval from websites;
- search-backed scraper opacity;
- robots.txt and User-Agent-based access-control limits.

OAT mapping:

- **OAT-011 Scraping** — primary mapping. The paper is directly about automated scraping and retrieval of web content by AI-related systems.
- **OAT-018 Footprinting** — indirect relevance where crawlers discover/index controlled sites, but the paper is not primarily about reconnaissance.
- **OAT-016 Skewing** — possible conceptual relevance where served content/canaries influence AI outputs, but the paper uses content manipulation as measurement rather than abuse.
- Other OATs such as credential stuffing, scalping, account creation, and CAPTCHA defeat are not directly covered.

## Scarce-resource abuse fields

Not applicable. This source is about content retrieval and AI web scraping, not appointment/ticket/product-drop/booking-flow inventory abuse.

## What is strong

- Strong measured source for AI-related web scraping and live/content-retrieval opacity.
- More operationally grounded than general LLM-agent capability papers because it observes real scraper visits to controlled websites and traces tokens into production chatbot outputs.
- Good source for the project’s observed-use lane: it is not victim telemetry, but it is a controlled in-the-wild measurement.
- Useful corrective to simple “block the AI bot User-Agent” advice.
- Strong support for the point that AI content retrieval may involve:
  - first-party AI crawlers;
  - third-party search-engine crawlers;
  - generic browser User-Agents;
  - cached/indexed content;
  - direct live retrieval.
- Useful for explaining why `robots.txt` and User-Agent strings are weak governance/control mechanisms when the content supply chain goes through search indexes or cached retrieval.
- Pairs well with the previous Bhardwaj et al. LLM-powered scraping benchmark:
  - Bhardwaj = what ordinary users/agents can do;
  - Seiden = how production AI systems appear to source web content.

## What is weak or limited

- arXiv preprint, not confirmed peer-reviewed.
- Controlled measurement sites, not victim production sites.
- Chatbot-scraper matching depends on canary-token elicitation from chatbot outputs; false negatives are possible if the chatbot accessed content but did not emit tokens.
- The scraper identity definition `(User-Agent, ASN)` is pragmatic but imperfect; different systems could share the same tuple, and the authors note richer fingerprinting could be used.
- The study infers exposure/association, not contractual or internal architecture.
- Some provider-specific conclusions may change quickly as AI products and crawler policies evolve.
- Robots.txt results are difficult to interpret because continued output may reflect caching/indexing rather than fresh disregard for robots.txt.
- It does not measure traffic volume, crawler rate, site load, economic harm, or legal compliance.
- It does not evaluate anti-bot products or detection accuracy.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates the problem of identifying which automated scrapers feed AI chatbot web-search/retrieval outputs, and whether simple site-owner controls affect what AI chatbots can report.

- **What does it fail to represent?**  
  It does not represent malicious scraping campaigns, commercial scraping at scale, or protected victim-site abuse. It measures controlled canary-token propagation through production AI systems rather than direct harm or prevalence.

- **What additional evidence would be needed to go further?**  
  Production web-server telemetry from affected publishers, independent replication over time, crawler policy/audit data, provider transparency reports, legal/contractual analysis, and measurement across more site types and stronger access-control conditions.

## What it cannot show

- It cannot show total AI-scraping prevalence.
- It cannot show that a given chatbot intentionally ignored robots.txt.
- It cannot show exact internal retrieval architecture.
- It cannot show whether scraper behaviour is lawful or compliant.
- It cannot show site harm, load impact, or business impact.
- It cannot show anti-bot detection performance.
- It cannot prove that every User-Agent association is stable over time.
- It cannot replace provider transparency reports or publisher-side telemetry.

## Project impact

Use this as a **core AI-web-scraping measurement entry**.

Best uses:

- support the AI-scraping / agentic-content-retrieval section;
- strengthen the observed-use lane with a controlled real-web measurement;
- explain why AI scraping is not only about model pretraining: inference-time retrieval and search-backed content supply matter;
- explain why User-Agent and robots.txt controls are fragile;
- show that content can continue appearing in AI outputs after a site is offline or blocked;
- motivate broader detection/control discussion involving User-Agent, ASN, IP, TLS, browser fingerprints, search indexes, caching, and content-level canaries.

Do not use it as:

- proof of malicious scraping;
- proof of intentional non-compliance by any provider;
- prevalence evidence for all AI scraping;
- a vendor ranking;
- legal guidance;
- a how-to guide for manipulating AI outputs.

## Relationship to other register entries

- **Bhardwaj et al. 2026 Beyond BeautifulSoup**: companion source. Bhardwaj benchmarks low-skill LLM/agent scraping capability; Seiden measures production AI chatbot retrieval infrastructure through canary tokens.
- **Commercial CAPTCHA-solving ecosystem / ReCAP**: CAPTCHA is not central here; this paper is about retrieval/crawler attribution rather than challenge solving.
- **Tschacher bot-detection architecture**: provides broader context for User-Agent, IP/ASN, TLS, and browser-fingerprint limits.
- **Proxy ecosystem entries**: relevant to identity and attribution limits, though this paper focuses on AI/search crawlers rather than residential proxies.
- **MDN/RFC foundations**: use for User-Agent, robots.txt, HTTP, and protocol background.
- **Cloudflare / HUMAN / DataDome AI-bot entries**: vendor sources can describe operational blocking/detection; this paper provides independent measurement of AI scraper/content-retrieval opacity.
- **OpenClaw / agentic traffic entries**: separate agentic-execution risk; Seiden is about content retrieval into AI chatbot responses.
- **OWASP OAT / Handbook**: map primarily to OAT-011 Scraping.

## Dual-use containment

Moderate dual-use. Canary-token methods can support defensive measurement and publisher control, but can also be used to probe or manipulate AI retrieval pipelines. In project use, keep the discussion at the measurement and governance level. Avoid reproducing full prompt templates, token-generation procedures, domain setup details, or provider-specific probing workflows.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `seiden-2026-identifying-ai-web-scrapers-canary-tokens` |
| Title | *Identifying AI Web Scrapers Using Canary Tokens* |
| Authors | Steven Seiden; Triss Ren; Caroline Zhang; Taein Kim; Enze Liu; Emily Wenger |
| Year | 2026 |
| Category | academic / threat-surface measurement |
| Evidence basis | empirical-measurement / canary-token honeysite study / preprint |
| Operational proximity | measured |
| Signals / techniques | canary tokens; honeysites; User-Agent; ASN; robots.txt; offline site test; search-engine crawlers; generic browser agents; cached/indexed retrieval; RAG/live retrieval |
| Threat types | OAT-011 Scraping; AI web scraping; unwanted AI content retrieval |
| Scarce-resource abuse | Not applicable |
| Project use | Core measured source for AI scraper attribution, retrieval opacity, and limits of User-Agent/robots.txt control |
| Main caution | Controlled canary-token measurement; not prevalence, legal compliance, intentional disregard, or production anti-bot effectiveness evidence |
| Entry file | `seiden-2026-identifying-ai-web-scrapers-canary-tokens.md` |
