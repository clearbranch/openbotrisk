# MDN - HTTP headers

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF capture of an MDN Web Docs page.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: MDN Web Docs. 2026. *HTTP headers*. Mozilla Developer Network. Accessed via uploaded PDF capture, 2026-06-06.
- **Source URL or path**: Uploaded file: `/mnt/data/HTTP headers - HTTP _ MDN.pdf`
- **Date accessed**: 2026-06-06
- **Category**: foundations
- **Evidence basis**: reference-doc
- **Operational proximity**: foundational - neutral technical reference material. It explains normal web mechanisms rather than documenting abuse, prevalence, or defensive performance.
- **Tags**: foundations, http-headers, request-headers, response-headers, user-agent, authorization, cookie, cors, cache-control, forwarded, proxy, bot-detection

## What it claims

- HTTP headers let clients and servers pass additional information with requests and responses.
- Headers can be grouped by context: request, response, representation, and payload headers.
- Headers can also be grouped by proxy handling: end-to-end headers should be transmitted to the final recipient, while hop-by-hop headers are meaningful only for a single transport-level connection.
- The header reference includes authentication headers such as WWW-Authenticate and Authorization, cookie headers such as Cookie and Set-Cookie, CORS headers such as Access-Control-Allow-Origin, and proxy-related headers such as Forwarded and Via.
- Headers expose many of the fields that bot-detection systems and scraper tools discuss: User-Agent, Accept-Language, Referer/Origin, Cookie, Authorization, Cache-Control, X-Forwarded-For, and related values.

## What evidence it provides

- This is a foundation/reference source for what headers are and how they are classified. It is not a bot-detection paper, but it provides the vocabulary needed to interpret vendor and academic claims about header-based detection.
- It supports the project’s explanation of why headers matter: headers are not just arbitrary text, they are structured fields in normal HTTP communication and can carry identity, authentication, session, content-negotiation, caching, CORS, and proxy information.
- It also helps distinguish legitimate protocol semantics from bot-detection interpretation. A User-Agent or Accept-Language value is a normal HTTP/browser signal; treating it as suspicious is a detection-layer decision, not something inherent in the header itself.

## Signals or techniques mentioned

- User-Agent
- Accept
- Accept-Language
- Cookie
- Set-Cookie
- Authorization
- WWW-Authenticate
- Cache-Control
- Vary
- Origin
- Access-Control-*
- Forwarded
- Via
- X-Forwarded-For
- Server-Timing

## Threat types covered

- Header-based bot detection
- Header spoofing and mismatch detection
- Session/authentication-bearing requests
- Proxy-aware request analysis

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

Use this as the foundation source for “what are HTTP headers?” and as a neutral vocabulary bridge between basic web mechanics and later sources on header-order checks, HTTP/2 differences, proxy headers, and browser impersonation.

## Possible register row

| Field | Value |
|---|---|
| Register id | `mdn-2026-http-headers` |
| Title | *HTTP headers* |
| Category | foundations |
| Evidence basis | reference-doc |
| Operational proximity | foundational |
| Tags | foundations; http-headers; request-headers; response-headers; user-agent; authorization; cookie; cors; cache-control; forwarded |
| Project use | Foundation reference for the relevant HTTP/browser mechanism |
| Main caution | Foundation/reference only; do not use as observed abuse or effectiveness evidence |
