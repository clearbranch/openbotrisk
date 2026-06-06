# MDN - Using HTTP cookies

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF capture of an MDN Web Docs page.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: MDN Web Docs. 2026. *Using HTTP cookies*. Mozilla Developer Network. Accessed via uploaded PDF capture, 2026-06-06.
- **Source URL or path**: Uploaded file: `/mnt/data/Using HTTP cookies - HTTP _ MDN.pdf`
- **Date accessed**: 2026-06-06
- **Category**: foundations
- **Evidence basis**: reference-doc
- **Operational proximity**: foundational - neutral technical reference material. It explains normal web mechanisms rather than documenting abuse, prevalence, or defensive performance.
- **Tags**: foundations, cookies, sessions, session-management, tracking, personalization, set-cookie, cookie-header, secure, httponly, samesite, session-fixation, account-takeover

## What it claims

- Cookies are small pieces of data sent by a server to a user’s browser; browsers may store, create, modify, and send them back with later requests.
- Cookies allow web applications to remember state because HTTP is stateless by default.
- MDN describes three main uses: session management, personalization, and tracking.
- Servers set cookies with Set-Cookie response headers and browsers send stored cookies back with Cookie request headers for matching domains/paths.
- Cookie security depends on attributes such as Secure, HttpOnly, Domain, Path, and SameSite.
- Session cookies should be regenerated on authentication to help prevent session fixation; MDN also warns that zombie-cookie techniques violate privacy principles and may create legal liability.

## What evidence it provides

- This is the key foundation source for explaining how sites know that multiple requests belong to the same browser/session.
- It supports the project’s account-abuse and automation strands: credential stuffing, account takeover, scraping behind login, queue manipulation, and slot-sniping all commonly depend on session continuity and cookie state.
- It is also useful for the detection side: cookies are normal state-management tools, but bot-management systems may use cookie challenges, session tokens, and cookie continuity to distinguish browser-like sessions from stateless scripts.

## Signals or techniques mentioned

- Set-Cookie
- Cookie
- session ID
- permanent cookies
- session cookies
- Max-Age
- Expires
- Clear-Site-Data
- Secure
- HttpOnly
- Domain
- Path
- SameSite
- Document.cookie
- Cookie Store API

## Threat types covered

- Session hijacking
- Session fixation
- Account takeover
- Credential stuffing sessions
- Scraping behind login
- Tracking and fingerprinting concerns
- Cookie challenge/session-continuity detection

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

Use this as the core foundation source for sessions. It explains the simple but crucial point that cookies are how a stateless protocol is made stateful, which is central to both bot defence and abuse models.

## Possible register row

| Field | Value |
|---|---|
| Register id | `mdn-2026-using-http-cookies` |
| Title | *Using HTTP cookies* |
| Category | foundations |
| Evidence basis | reference-doc |
| Operational proximity | foundational |
| Tags | foundations; cookies; sessions; session-management; tracking; personalization; set-cookie; cookie-header; secure; httponly |
| Project use | Foundation reference for the relevant HTTP/browser mechanism |
| Main caution | Foundation/reference only; do not use as observed abuse or effectiveness evidence |
