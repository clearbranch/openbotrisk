# Cloudflare - Turnstile

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: live official Cloudflare developer documentation.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Cloudflare. 2026. *Overview - Cloudflare Turnstile docs*. Cloudflare Developers. Accessed 2026-06-06.
- **Source URL or path**: `https://developers.cloudflare.com/turnstile/`
- **Date accessed**: 2026-06-06
- **Category**: vendor
- **Evidence basis**: capability-doc
- **Operational proximity**: capability - challenge/CAPTCHA-alternative documentation.
- **Tags**: cloudflare, turnstile, captcha-alternative, browser-signals, proof-of-work, proof-of-space, web-apis, browser-quirks, human-behaviour, pre-clearance

## What it claims

- Turnstile adapts challenge outcomes to the individual visitor or browser.
- Cloudflare runs small non-interactive JavaScript challenges to gather signals about the visitor or browser environment.
- The challenges can include proof-of-work, proof-of-space, probing for web APIs, and other checks for browser quirks and human behaviour.
- Turnstile offers managed, non-interactive, and invisible widget types.
- Turnstile Analytics can assess issued challenges and challenge solve rate.
- Pre-clearance can issue a cookie for single-page application challenge integration.

## What evidence it provides

- Useful for explaining modern CAPTCHA replacement: the interaction is not necessarily a visual puzzle; the system may evaluate browser and environment signals first.
- Supports the project’s point that bot defence may rely on client-side execution, browser capability checks, and risk-adaptive challenge difficulty.
- Defensive capability source, not a measurement source.

## Signals or techniques mentioned

- non-interactive JavaScript challenges
- proof-of-work
- proof-of-space
- Web API probing
- browser quirks
- human behaviour checks
- managed widget
- invisible widget
- pre-clearance cookie
- challenge solve rate

## Threat types covered

- automated scripts
- bot traffic submitted through forms or protected flows
- non-human browser environments
- challenge replay/token misuse, when combined with token validation material

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** Web forms, sign-up flows, login flows, and other application interactions where a site wants to distinguish likely humans from automation.
- **What does it fail to represent?** It does not show bypass rates, usability impact, challenge failure rates by user group, or independent accessibility/privacy assessment.
- **What additional evidence would be needed to go further?** Independent evaluations, Cloudflare telemetry, accessibility testing, privacy addendum review, or implementation case studies.

## What it cannot show

- It cannot prove Turnstile stops advanced bots.
- It cannot show the impact on legitimate users.
- It cannot show real-world abuse prevalence.
- It cannot establish that a Turnstile deployment is legally sufficient.

## Project impact

Use this as the entry for challenge systems and CAPTCHA alternatives. It helps explain the move from “solve a puzzle” to “evaluate browser/environment/human-like signals with adaptive friction.”

## Possible register row

| Field | Value |
|---|---|
| Register id | `cloudflare-2026-turnstile` |
| Title | *Overview - Cloudflare Turnstile docs* |
| Category | vendor |
| Evidence basis | capability-doc |
| Operational proximity | capability |
| Tags | cloudflare; turnstile; captcha-alternative; browser-signals; proof-of-work; proof-of-space; web-apis; browser-quirks; human-behaviour; pre-clearance |
| Project use | Challenge-system / CAPTCHA-alternative foundation |
| Main caution | Product documentation; not proof of challenge effectiveness or usability impact |
