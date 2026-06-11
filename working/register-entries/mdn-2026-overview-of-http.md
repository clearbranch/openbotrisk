# MDN - Overview of HTTP

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF capture of an MDN Web Docs page.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: MDN Web Docs. 2026. *Overview of HTTP*. Mozilla Developer Network. Accessed via uploaded PDF capture, 2026-06-06.
- **Source URL or path**: Uploaded file: `/mnt/data/SRC-065-mdn-2026-overview-of-http.pdf`
- **Date accessed**: 2026-06-06
- **Category**: foundations
- **Evidence basis**: reference-doc
- **Operational proximity**: foundational - neutral technical reference material. It explains normal web mechanisms rather than documenting abuse, prevalence, or defensive performance.
- **Tags**: foundations, http, client-server, requests, responses, user-agent, proxies, cookies, sessions, authentication, web-basics

## What it claims

- HTTP is the application-layer protocol used to fetch resources such as HTML documents, images, scripts, videos, and other web assets.
- HTTP is a client-server protocol in which requests are initiated by a user-agent, usually a browser, but also potentially robots, developer tools, or other programs.
- Web pages are assembled through an initial HTML request followed by additional requests for CSS, scripts, images, media, and later resources fetched by scripts.
- HTTP sits above lower transport/network layers such as TCP, TLS, UDP, and IP, so HTTP analysis concerns the application messages rather than the full network path.
- Proxies can sit between clients and servers and perform functions such as caching, filtering, load balancing, authentication, and logging.
- HTTP itself is stateless, but cookies can link requests together into sessions.

## What evidence it provides

- This is a foundation source rather than threat evidence. It gives a clear explanation of how browsers and other user-agents fetch web resources and how individual requests/responses compose a complete web page.
- It supports the project’s basic explanatory layer: what a request is, why a browser makes many requests for one page, what a user-agent is, why proxies matter, and how cookies create state on top of stateless HTTP.
- It is useful for explaining why automated clients can be compared with browsers: both are user-agents that initiate HTTP requests, but they may differ in request patterns, headers, script execution, resource loading, cookies, and timing.

## Signals or techniques mentioned

- HTTP requests and responses
- user-agent concept
- browser resource fetching
- client-server model
- proxies and tunnelling
- HTTP cookies and sessions
- HTTP authentication
- application-layer framing

## Threat types covered

- Foundation for web scraping and crawling
- Foundation for bot detection based on request patterns
- Foundation for session-based abuse and account automation

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

Use this as a plain-language foundation source for the website: before explaining bot detection, readers need to understand that browsers, crawlers, and scripts all act as user-agents making HTTP requests; the differences lie in behaviour, headers, state, resources loaded, and surrounding browser environment.

## Possible register row

| Field | Value |
|---|---|
| Register id | `mdn-2026-overview-of-http` |
| Title | *Overview of HTTP* |
| Category | foundations |
| Evidence basis | reference-doc |
| Operational proximity | foundational |
| Tags | foundations; http; client-server; requests; responses; user-agent; proxies; cookies; sessions; authentication |
| Project use | Foundation reference for the relevant HTTP/browser mechanism |
| Main caution | Foundation/reference only; do not use as observed abuse or effectiveness evidence |
