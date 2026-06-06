# MDN - HTTP caching

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF capture of an MDN Web Docs page.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: MDN Web Docs. 2026. *HTTP caching*. Mozilla Developer Network. Accessed via uploaded PDF capture, 2026-06-06.
- **Source URL or path**: Uploaded file: `/mnt/data/HTTP caching - HTTP _ MDN.pdf`
- **Date accessed**: 2026-06-06
- **Category**: foundations
- **Evidence basis**: reference-doc
- **Operational proximity**: foundational - neutral technical reference material. It explains normal web mechanisms rather than documenting abuse, prevalence, or defensive performance.
- **Tags**: foundations, http-caching, cache-control, private-cache, shared-cache, proxy-cache, cdn, etag, last-modified, vary, cookies, personalized-content, crawler-behaviour

## What it claims

- HTTP caches store responses associated with requests and reuse them for later requests, improving response speed and reducing origin-server work.
- Private caches are tied to a specific client, while shared caches sit between clients and servers and may be shared among users.
- Personalized content should be marked private when it is intended only for a private cache; cookies alone do not automatically make a response private.
- Cache-Control, ETag, Last-Modified, If-None-Match, and related headers manage validation, freshness, reuse, and revalidation.
- Managed caches such as reverse proxies, CDNs, and service workers may have their own controls and dashboards.

## What evidence it provides

- This is a foundation source for caching, not direct bot evidence. It explains a part of the web stack that affects what scrapers fetch, what servers see, and how repeated requests may or may not hit origin servers.
- It is useful for the project because cache behaviour affects both measurement and defence: high request volumes may be absorbed by caches, stale content can mislead scrapers, and personalised responses must avoid shared-cache leakage.
- It also supports foundation explanations of ETag/Last-Modified crawler behaviour and why conditional requests can reduce load compared with naive repeated full fetches.

## Signals or techniques mentioned

- Cache-Control
- private
- no-cache
- no-store
- max-age
- ETag
- Last-Modified
- If-None-Match
- 304 Not Modified
- Age
- Vary
- shared cache
- private cache
- proxy cache
- CDN
- service worker cache

## Threat types covered

- High-volume scraping load
- Cache-aware crawling
- Personalized content leakage via shared cache
- Conditional-request patterns
- CDN/reverse-proxy defence layer

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** It does not approximate a live abuse incident. It explains the protocol or browser mechanism that later bot, scraping, abuse, and defence sources rely on.
- **What does it fail to represent?** It does not show malicious use, prevalence, success rates, attack tooling, defender efficacy, or real-world incident impact.
- **What additional evidence would be needed to go further?** To support threat claims, pair this foundation source with vendor telemetry, academic measurement, legal/enforcement records, or observed incident reports.

## What it cannot show

- It cannot show real-world abuse prevalence.
- It cannot show that any specific bot, scraper, or attacker used the mechanism maliciously.
- It cannot validate any anti-bot vendor claims.
- It cannot prove that a detection method is effective.
- It cannot determine whether a given scraping workflow is lawful or policy-compliant.

## Project impact

Use this as a background source for why not every scrape request is equal. Caches can reduce server load, change what is observed at origin, and create privacy/security risks when personalised content is cached incorrectly.

## Possible register row

| Field | Value |
|---|---|
| Register id | `mdn-2026-http-caching` |
| Title | *HTTP caching* |
| Category | foundations |
| Evidence basis | reference-doc |
| Operational proximity | foundational |
| Tags | foundations; http-caching; cache-control; private-cache; shared-cache; proxy-cache; cdn; etag; last-modified; vary |
| Project use | Foundation reference for the relevant HTTP/browser mechanism |
| Main caution | Foundation/reference only; do not use as observed abuse or effectiveness evidence |
