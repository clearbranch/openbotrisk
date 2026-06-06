# MDN - Cross-Origin Resource Sharing (CORS)

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF capture of an MDN Web Docs page.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: MDN Web Docs. 2026. *Cross-Origin Resource Sharing (CORS)*. Mozilla Developer Network. Accessed via uploaded PDF capture, 2026-06-06.
- **Source URL or path**: Uploaded file: `/mnt/data/Cross-Origin Resource Sharing (CORS) - HTTP _ MDN.pdf`
- **Date accessed**: 2026-06-06
- **Category**: foundations
- **Evidence basis**: reference-doc
- **Operational proximity**: foundational - neutral technical reference material. It explains normal web mechanisms rather than documenting abuse, prevalence, or defensive performance.
- **Tags**: foundations, cors, same-origin-policy, fetch, xmlhttprequest, origin-header, preflight, access-control-allow-origin, credentials, cookies, browser-security, web-apis

## What it claims

- CORS is an HTTP-header based mechanism that lets a server indicate which origins other than its own may load/read resources in a browser context.
- Browsers restrict cross-origin HTTP requests initiated from scripts such as fetch() and XMLHttpRequest unless the response includes appropriate CORS headers.
- For some non-simple requests, browsers send a preflight OPTIONS request that indicates the intended method and headers before sending the actual request.
- CORS can govern whether credentials such as cookies and HTTP authentication are sent with cross-origin requests and whether the response is exposed to web content.
- CORS failures are intentionally opaque to JavaScript for security reasons; details are available in browser developer consoles rather than application code.

## What evidence it provides

- This is a foundation source for browser-side web security boundaries. It is not bot evidence, and it should not be misread as a general server-to-server access-control system.
- It is useful because many beginners misunderstand CORS as stopping all scraping. MDN makes clear it is about browser-enforced cross-origin access from scripts, not whether a server can be requested by non-browser clients.
- It also supports explanations of Origin headers, preflight requests, credentialed cross-origin requests, and why browsers behave differently from simple HTTP clients.

## Signals or techniques mentioned

- Origin
- Access-Control-Allow-Origin
- Access-Control-Allow-Credentials
- Access-Control-Allow-Headers
- Access-Control-Allow-Methods
- Access-Control-Max-Age
- Access-Control-Request-Method
- Access-Control-Request-Headers
- OPTIONS preflight
- fetch
- XMLHttpRequest
- credentials include

## Threat types covered

- Browser-side cross-origin data access
- Credentialed cross-origin requests
- Misconfigured CORS exposure
- Distinguishing browser restrictions from scraper/server-side access
- CSRF-adjacent reasoning

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

Use this as the foundation source for CORS. It is valuable mainly to prevent a common error: treating CORS as a general anti-scraping defence rather than a browser-enforced cross-origin sharing mechanism.

## Possible register row

| Field | Value |
|---|---|
| Register id | `mdn-2026-cors` |
| Title | *Cross-Origin Resource Sharing (CORS)* |
| Category | foundations |
| Evidence basis | reference-doc |
| Operational proximity | foundational |
| Tags | foundations; cors; same-origin-policy; fetch; xmlhttprequest; origin-header; preflight; access-control-allow-origin; credentials; cookies |
| Project use | Foundation reference for the relevant HTTP/browser mechanism |
| Main caution | Foundation/reference only; do not use as observed abuse or effectiveness evidence |
