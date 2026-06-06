# Cloudflare - Block AI Bots

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: live official Cloudflare developer documentation.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Cloudflare. 2026. *Block AI Bots - Cloudflare bot solutions docs*. Cloudflare Developers. Accessed 2026-06-06.
- **Source URL or path**: `https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/`
- **Date accessed**: 2026-06-06
- **Category**: vendor
- **Evidence basis**: capability-doc
- **Operational proximity**: capability - vendor defensive control for AI crawler traffic.
- **Tags**: cloudflare, ai-bots, ai-crawlers, verified-bots, unverified-bots, ai-crawl-control, crawler-governance, content-access-control

## What it claims

- Cloudflare offers a Block AI bots setting in the application security dashboard.
- Activating the setting blocks verified bots classified as AI crawlers, as well as a number of unverified bots that behave similarly.
- Site owners can block AI bots on all pages, block only on hostnames with ads, or leave blocking off.
- For blocking individual AI crawlers rather than all crawlers, Cloudflare directs users to AI Crawl Control.

## What evidence it provides

- Useful current-trend evidence that AI crawler traffic is being treated as a distinct management category in mainstream web-security products.
- Supports a content-governance strand: not all bot traffic is treated as classic security abuse; some is managed as crawler/content-access policy.
- It is not evidence of malicious AI-agent use or crawler prevalence.

## Signals or techniques mentioned

- verified AI crawler classification
- unverified bots that behave similarly
- hostname-level blocking
- ad-hostname-specific blocking
- AI Crawl Control
- individual AI crawler controls

## Threat types covered

- AI crawler access
- unverified AI-like crawling
- content access without publisher consent
- crawler governance rather than classic fraud/ATO abuse

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** Site-owner control over AI crawler and AI-like crawler access.
- **What does it fail to represent?** It does not show how bots are classified, how often they appear, whether blocking succeeds, or whether the traffic is harmful.
- **What additional evidence would be needed to go further?** Cloudflare Radar AI crawler data, publisher case studies, independent crawler measurements, or legal/policy sources on content scraping and AI training.

## What it cannot show

- It cannot prove AI crawlers are malicious.
- It cannot quantify AI crawler traffic.
- It cannot show effectiveness or false positives.
- It cannot settle legal questions around crawling, training, indexing, or content access.

## Project impact

Use this as the Cloudflare entry for the AI-crawler/current-trend layer. It is a good complement to HUMAN agentic-traffic sources and scraper-side sources, but frame it as defensive product categorisation and governance rather than observed abuse.

## Possible register row

| Field | Value |
|---|---|
| Register id | `cloudflare-2026-block-ai-bots` |
| Title | *Block AI Bots - Cloudflare bot solutions docs* |
| Category | vendor |
| Evidence basis | capability-doc |
| Operational proximity | capability |
| Tags | cloudflare; ai-bots; ai-crawlers; verified-bots; unverified-bots; ai-crawl-control; crawler-governance; content-access-control |
| Project use | Current-trend source for AI crawler management in defensive products |
| Main caution | Product-control documentation; not abuse prevalence or effectiveness evidence |
