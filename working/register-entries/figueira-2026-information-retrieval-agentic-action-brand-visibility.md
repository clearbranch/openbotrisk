# Figueira (2026) - From Information Retrieval to Agentic Action: brand visibility in AI-mediated markets

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded preprint PDF `preprints202605.1208.v1.pdf`; updated project files `EVIDENCE-REVIEW(5).md` and `evidence-register(8).qmd` were available for scope context.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.
- **Source handling decision**: create a low-priority/adjacent entry. This is not bot-detection or abuse evidence. It is useful only for the AI-mediated markets / agentic action context: why content access, retrieval, attribution, and tool-execution surfaces matter commercially.

## Bibliographic

- **Citation**: Figueira, M. G. (2026). *From Information Retrieval to Agentic Action: A Framework for Brand Visibility in AI-Mediated Markets*. Preprints.org. Posted 18 May 2026. DOI: `10.20944/preprints202605.1208.v1`.
- **Source URL or path**: uploaded PDF `preprints202605.1208.v1.pdf`.
- **Publication status**: concept paper; not peer-reviewed.
- **Licence**: Creative Commons Attribution 4.0 International.
- **Category**: threat-surface / AI-mediated market context
- **Evidence basis**: conceptual framework / marketing strategy theory / preprint
- **Operational proximity**: n/a / low — not observed abuse, not scraper telemetry, not bot-detection evidence, and not a technical measurement study.
- **Tags**: AI-mediated-markets, agentic-AI, AEO, GEO, AgO, answer-engine-optimization, generative-engine-optimization, agentic-optimization, brand-erasure, AI-search, RAG, tool-use, consumer-AI-delegation, attribution, robots.txt, AI-visibility, marketing-strategy

## What it claims

- Digital visibility is shifting from search-result pages to AI-generated answers, and then from answers to agent-executed actions.
- The paper proposes three linked optimisation layers:
  - Answer Engine Optimization (AEO): visibility in extracted factual answers;
  - Generative Engine Optimization (GEO): visibility/citation in synthesized AI answers;
  - Agentic Optimization (AgO): selection and successful execution by AI agents.
- The author argues that brands should treat the AI assistant not merely as a channel, but as a delegated decision-making intermediary.
- The focal strategic risk is **brand erasure**: an AI system satisfies the user’s need without surfacing, citing, or transacting with the brand whose content/product/service contributed to the outcome.
- The paper proposes that brands need a “dual audience” strategy: humans still matter, but machines increasingly mediate whether humans encounter the brand at all.
- It proposes new measurement concepts such as share-of-citation, embedding proximity, definitional anchoring, agent execution rate, brand entity grounding, and hallucination rate.
- It discusses robots.txt and crawler policy as strategic choices with trade-offs between control, corpus presence, attribution leverage, and visibility.

## What evidence it provides

This is a **conceptual/positioning paper**, not an empirical study.

It provides:

- a marketing-strategy framework for AI-mediated visibility;
- a useful vocabulary for AI search and agentic selection:
  - AEO;
  - GEO;
  - AgO;
  - brand erasure;
  - dual-audience design;
  - machine experience as a layer;
  - agent execution rate;
- a table summarising the optimisation stack across extraction, synthesis, and execution;
- a table mapping click-era KPIs to AI-mediated KPIs;
- a discussion of robots.txt and attribution/gatekeeping trade-offs;
- a conceptual link between content structure, machine-readable affordances, APIs/manifests, and agentic action.

It does **not** provide:

- bot-detection evidence;
- web-scraping measurements;
- observed AI-crawler traffic;
- anti-bot bypass evidence;
- scraping or abuse prevalence;
- controlled experiments;
- production telemetry;
- legal analysis sufficient for compliance claims;
- technical details on agent infrastructure, browser automation, or crawler identification.

## Important visual/source evidence

- **Page 1** clearly labels the document as a “Concept Paper” and “Not peer-reviewed version”; this caveat should travel with any use of the source.
- **Table 1 / page 6** summarises the optimisation stack:
  - AEO targets closed-domain extraction and is measured by fact-extraction accuracy;
  - GEO targets open-domain synthesis and is measured by share-of-citation;
  - AgO targets task execution and is measured by agent execution rate.
- **Table 2 / page 8** maps click-economy KPIs to AI-mediated KPIs, such as click-through rate to share-of-citation, page rank to embedding proximity, conversion rate to agent execution rate, and bounce rate to hallucination rate.
- **Section 6.2 / page 9** discusses hallucination, takedown, and limits of robots.txt, with the important caveat that robots.txt is a signal respected by well-behaved crawlers rather than a hard technical control.

## Signals or techniques mentioned

- AI-generated answers;
- AI Overviews;
- RAG;
- web search;
- tool-augmented language models;
- computer-use APIs;
- agents executing actions;
- manifests;
- machine-readable schemas;
- product/pricing/inventory data;
- idempotent endpoints;
- authentication flows;
- API latency;
- structured data;
- knowledge graphs;
- entity grounding;
- embedding proximity;
- share-of-citation;
- definitional anchoring;
- brand erasure;
- hallucination rate;
- robots.txt;
- training crawlers;
- inference-time retrieval crawlers;
- search-index crawlers;
- AI visibility audits.

## Threat types covered

No OWASP Automated Threat category is directly covered.

Indirect relevance:

- **OAT-011 Scraping** — weak contextual relevance because AI search/retrieval relies on web content collection and robots.txt/crawler choices.
- **Agentic transaction/action risks** — contextual relevance where agents select platforms, call APIs, or complete tasks.
- **OAT-006 Expediting / OAT-020 Account Aggregation** — possible conceptual relevance where agents execute tasks through services, but this source does not discuss abuse.
- **AI crawler/content access governance** — contextual relevance, not an OAT category.

This source should not be used as evidence for credential stuffing, scalping, sniping, CAPTCHA defeat, proxy abuse, or bot-detection methods.

## What is strong

- Useful framing source for why AI-mediated retrieval and agentic action matter commercially.
- Helpful bridge between AI scraping/retrieval papers and the wider commercial incentives around visibility.
- Gives language for the shift from:
  - search page;
  - AI answer;
  - agentic action.
- Useful for explaining why content owners may simultaneously want:
  - AI systems to see/cite them;
  - control over scraping;
  - protection against misattribution or hallucination.
- The AEO/GEO/AgO stack is a clean organising device, even if it is not evidence.
- Pairs well with Seiden et al.:
  - Seiden measures AI scraper/content retrieval opacity;
  - Figueira explains why content owners/brands care about attribution and AI-mediated visibility.
- Pairs weakly with Bhardwaj et al.:
  - Bhardwaj shows LLM agents can perform website workflows;
  - Figueira explains the market consequence if agents become action intermediaries.

## What is weak or limited

- Not peer-reviewed.
- Conceptual and strategy-oriented.
- Not a security paper.
- Not empirical.
- Not bot-specific.
- Makes broad claims about marketing and AI-mediated markets that should not become load-bearing without stronger sources.
- Some “new KPI” proposals are useful but not validated.
- It cites practitioner/company announcements and trade-relevant material; do not treat those as rigorous evidence through this source.
- The paper’s “brand erasure” framing is commercially useful but should not be confused with abuse, harm, or legal infringement.
- It should not expand the evidence review into general marketing/SEO/AEO/GEO unless that is a deliberate scope decision.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates the commercial environment in which AI crawlers, answer engines, and agentic systems become economically important intermediaries. It helps explain why content access, attribution, and agent-executable surfaces matter.

- **What does it fail to represent?**  
  It does not represent abuse, adversarial automation, scraping measurements, detection systems, or technical controls. It is a business/marketing framework.

- **What additional evidence would be needed to go further?**  
  Empirical AI search/crawler studies; publisher telemetry; legal/regulatory sources; agentic transaction benchmarks; provider transparency reports; and measured studies of AI-answer citation/attribution.

## What it cannot show

- It cannot show AI scraping prevalence.
- It cannot show which crawlers feed which AI systems.
- It cannot show bot or scraper detection performance.
- It cannot show that robots.txt is obeyed or ignored in practice.
- It cannot show actual brand-erasure rates.
- It cannot validate AEO/GEO/AgO as established disciplines.
- It cannot establish legal rights to citation or attribution.
- It cannot support claims about automated abuse directly.

## Project impact

Use this as a **low-priority AI-mediated market context source**.

Best uses:

- add a short contextual note explaining why AI scraping/retrieval is commercially contested;
- frame why site owners may not simply want to block all AI crawlers — visibility, attribution, and control are in tension;
- explain the move from information retrieval to agentic action as a market-context background point;
- support a small “why this matters beyond security” paragraph, if the review needs one.

Do not use it as:

- core evidence;
- bot evidence;
- observed-use evidence;
- technical authority;
- legal authority;
- a reason to broaden the project into SEO/marketing strategy.

## Relationship to other register entries

- **Seiden et al. 2026 canary tokens**: stronger measured source for AI scraper/content-retrieval opacity. Figueira gives only market-context vocabulary.
- **Bhardwaj et al. 2026 LLM-powered scraping**: stronger measured source for novice/agentic scraping capability. Figueira gives commercial consequences of agentic action.
- **Cloudflare / HUMAN / DataDome AI-bot and bot-management sources**: stronger operational sources for detection/control.
- **OpenClaw / agentic traffic sources**: stronger security/threat-surface sources for agentic systems.
- **MDN/RFC/robots.txt foundations**: stronger foundations for crawler/access-control mechanics.
- **Evidence Review scope guide**: this source sits at the edge of scope. Keep it narrow as context, not as a new marketing/SEO lane.

## Dual-use containment

Low dual-use. The main risk is scope creep and overclaiming, not operational harm. Avoid turning the review into AEO/GEO/SEO advice, and avoid presenting speculative market-strategy propositions as established evidence.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `figueira-2026-information-retrieval-agentic-action-brand-visibility` |
| Title | *From Information Retrieval to Agentic Action: A Framework for Brand Visibility in AI-Mediated Markets* |
| Author | Marcos Guimaraes Figueira |
| Year | 2026 |
| Category | threat-surface / AI-mediated market context |
| Evidence basis | conceptual framework / marketing strategy theory / preprint |
| Operational proximity | n/a / low |
| Signals / techniques | AEO; GEO; AgO; AI Overviews; RAG; tool-augmented agents; manifests; structured data; agent execution rate; robots.txt; attribution |
| Threat types | none directly; weak context for OAT-011 Scraping and AI crawler/content-access governance |
| Scarce-resource abuse | Not applicable |
| Project use | Low-priority context for why AI retrieval and agentic action matter commercially and why crawler access/attribution is contested |
| Main caution | Concept paper, not peer-reviewed, not empirical, not security/bot evidence |
| Entry file | `figueira-2026-information-retrieval-agentic-action-brand-visibility.md` |
