# MDN - User-Agent header

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF capture of an MDN Web Docs page.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: MDN Web Docs. 2026. *User-Agent header*. Mozilla Developer Network. Accessed via uploaded PDF capture, 2026-06-06.
- **Source URL or path**: Uploaded file: `/mnt/data/User-Agent header - HTTP _ MDN.pdf`
- **Date accessed**: 2026-06-06
- **Category**: foundations
- **Evidence basis**: reference-doc
- **Operational proximity**: foundational - neutral technical reference material. It explains normal web mechanisms rather than documenting abuse, prevalence, or defensive performance.
- **Tags**: foundations, user-agent, http-header, browser-identification, crawler-identification, fingerprinting, user-agent-reduction, client-hints, bot-detection

## What it claims

- The User-Agent request header is a characteristic string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user-agent.
- Browser User-Agent strings commonly include browser-family compatibility tokens, platform/system information, engine details, and browser version information.
- The information exposed in User-Agent headers has historically raised privacy concerns because it can help identify a particular user-agent and be used for fingerprinting.
- Supporting browsers now reduce some User-Agent information and expose more detailed information through User-Agent Client Hints when requested by servers.
- MDN examples include browser strings as well as bot/tool strings such as Googlebot, YandexAccessibilityBot, curl, and PostmanRuntime.

## What evidence it provides

- This source is strong for the basic definition of User-Agent and why it matters in the project. It explains that User-Agent is both a normal compatibility mechanism and a fingerprinting/privacy surface.
- It helps explain a key bot-detection issue without relying on vendor claims: automated tools often identify themselves differently from browsers, while malicious or grey-market automation may try to imitate browser User-Agent strings.
- The User-Agent reduction section is useful for the privacy/governance strand: browsers are deliberately reducing passive fingerprinting surface, while server-side systems can request more detailed Client Hints where justified.

## Signals or techniques mentioned

- User-Agent string
- browser family tokens
- platform/system information
- browser version
- crawler/tool user-agents
- User-Agent reduction
- Navigator.userAgent
- Navigator.appVersion
- Navigator.platform
- Accept-CH
- Sec-CH-UA client hints

## Threat types covered

- Crawler identification
- Header spoofing
- Browser impersonation
- Fingerprinting and passive tracking
- Bot detection based on default/generic user-agents

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

Use this as the foundation entry for the “what is a User-Agent?” section. It connects simple browser identification, crawler self-identification, scraper defaults, browser spoofing, and privacy-motivated User-Agent reduction.

## Possible register row

| Field | Value |
|---|---|
| Register id | `mdn-2026-user-agent-header` |
| Title | *User-Agent header* |
| Category | foundations |
| Evidence basis | reference-doc |
| Operational proximity | foundational |
| Tags | foundations; user-agent; http-header; browser-identification; crawler-identification; fingerprinting; user-agent-reduction; client-hints; bot-detection |
| Project use | Foundation reference for the relevant HTTP/browser mechanism |
| Main caution | Foundation/reference only; do not use as observed abuse or effectiveness evidence |
