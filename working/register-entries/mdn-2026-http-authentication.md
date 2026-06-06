# MDN - HTTP authentication

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF capture of an MDN Web Docs page.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: MDN Web Docs. 2026. *HTTP authentication*. Mozilla Developer Network. Accessed via uploaded PDF capture, 2026-06-06.
- **Source URL or path**: Uploaded file: `/mnt/data/HTTP authentication - HTTP _ MDN.pdf`
- **Date accessed**: 2026-06-06
- **Category**: foundations
- **Evidence basis**: reference-doc
- **Operational proximity**: foundational - neutral technical reference material. It explains normal web mechanisms rather than documenting abuse, prevalence, or defensive performance.
- **Tags**: foundations, http-authentication, authorization, www-authenticate, proxy-authentication, 401, 403, 407, basic-auth, bearer-token, credentials, account-protection

## What it claims

- HTTP provides a general framework for access control and authentication, where servers can challenge clients and clients can provide credentials.
- A server can respond with 401 Unauthorized and a WWW-Authenticate header; a client can retry with an Authorization request header.
- Proxy authentication uses the same challenge/response concept with 407 Proxy Authentication Required, Proxy-Authenticate, and Proxy-Authorization.
- A server can return 403 Forbidden when credentials are valid but inadequate, and may return 404 Not Found to hide a resource from unauthorised users.
- Basic authentication sends credentials encoded, not encrypted, so it is insecure without HTTPS/TLS and should not protect sensitive or valuable information without additional safeguards.

## What evidence it provides

- This is a neutral foundation source for explaining access control at the HTTP layer, independent of modern web-app login forms.
- It supports the project by clarifying the difference between authentication, proxy authentication, forbidden access, and hidden resources.
- It is useful when reading bot/scraping sources that discuss credentials, proxy credentials, bearer tokens, logins, and authentication headers.

## Signals or techniques mentioned

- 401 Unauthorized
- WWW-Authenticate
- Authorization
- 407 Proxy Authentication Required
- Proxy-Authenticate
- Proxy-Authorization
- 403 Forbidden
- 404 Not Found as concealment
- Basic authentication
- Bearer tokens
- Digest authentication

## Threat types covered

- Credential-bearing automated requests
- Proxy-authenticated scraping infrastructure
- Account access automation
- Authentication failure/lockout behaviour
- Access-control boundary testing

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

Use this as the foundation source for HTTP-level authentication concepts. It helps avoid conflating cookies, login sessions, Authorization headers, proxy credentials, and application-level account takeover.

## Possible register row

| Field | Value |
|---|---|
| Register id | `mdn-2026-http-authentication` |
| Title | *HTTP authentication* |
| Category | foundations |
| Evidence basis | reference-doc |
| Operational proximity | foundational |
| Tags | foundations; http-authentication; authorization; www-authenticate; proxy-authentication; 401; 403; 407; basic-auth; bearer-token |
| Project use | Foundation reference for the relevant HTTP/browser mechanism |
| Main caution | Foundation/reference only; do not use as observed abuse or effectiveness evidence |
