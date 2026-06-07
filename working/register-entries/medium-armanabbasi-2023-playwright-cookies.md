# Medium / armanabbasi (2023) - How to Get and Use Cookies in Playwright

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF export of Medium article; previous extraction draft reviewed.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.

## Bibliographic

- **Citation**: armanabbasi. (2023). *How to Get and Use Cookies in Playwright: A Step-by-Step Guide for Beginners*. Medium. Published 13 November 2023.
- **Source URL or path**: `https://medium.com/@armanabbasi/how-to-get-and-use-cookies-in-playwright-a-step-by-step-guide-for-beginners-d09bb345ff1`; uploaded PDF `How to Get and Use Cookies in Playwright_ A Step-by-Step Guide for Beginners _ by armanabbasi _ Medium.pdf`.
- **Date accessed / captured**: uploaded 2026-06-06.
- **Category**: foundations
- **Evidence basis**: tutorial / capability-doc
- **Operational proximity**: capability — shows a basic browser-automation capability for handling cookies/session state; not observed abuse, not evasion evidence, and not detection evidence.
- **Tags**: cookies, session-state, browser-automation, playwright, chromium, browser-context, authentication-state, SSO, Cypress, testing, foundations

## What it claims

- Playwright is a framework for web testing and automation.
- Playwright can save authentication state from a browser context and reuse it in tests.
- Cookies can be captured from a Playwright browser context after login.
- Captured cookies can be returned and used outside the immediate test flow.
- Cookie capture can help in practical testing scenarios involving SSO pages or when moving state between tools such as Playwright and Cypress.

## What evidence it provides

- A short beginner tutorial.
- A small Playwright/Chromium example showing:
  - importing Playwright test utilities and Chromium;
  - launching a browser;
  - creating a new browser context;
  - navigating to a base URL;
  - placeholder login steps;
  - calling `context.cookies()` after login;
  - returning the captured cookie data.
- Explanatory prose for:
  - `test`;
  - `chromium.launch`;
  - `browser.newContext`;
  - `context.cookies`;
  - try/catch error handling.
- A GitHub repository link associated with the article.

## Signals or techniques mentioned

- cookies as browser/session state;
- Playwright browser contexts;
- independent browser sessions similar to incognito contexts;
- Chromium browser automation;
- headed browser launch;
- login-flow automation placeholder;
- cookie extraction through a browser automation framework;
- SSO testing context;
- cross-framework state movement, specifically Playwright to Cypress.

## Threat types covered

Not threat-specific.

Indirectly relevant to:

- credentialed automation;
- automated authenticated sessions;
- cookie/session continuity;
- testing flows that reuse authenticated state.

But the source itself does **not** discuss:

- scraping;
- credential stuffing;
- account takeover;
- bot detection;
- cookie theft;
- cookie replay abuse;
- bypassing authentication;
- bypassing anti-bot controls.

## What is strong

- Useful beginner-level example showing that browser automation frameworks can access cookie/session state.
- Helps bridge abstract cookie/session concepts and practical browser automation.
- Useful for a foundation page explaining that automation is not limited to stateless HTTP requests; it can operate through a browser context with cookies.
- Useful as a low-level example for why cookies and sessions matter in automation workflows.

## What is weak or limited

- Low-substance source compared with official Playwright documentation.
- Medium tutorial, not primary documentation, academic evidence, vendor telemetry, or legal evidence.
- The login flow is only a placeholder; it does not demonstrate a full SSO or production authentication workflow.
- It does not discuss important web-security details such as `HttpOnly`, `Secure`, `SameSite`, token refresh, session expiry, device binding, risk scoring, MFA, or session revocation.
- It does not address whether copied cookies remain valid across browsers, devices, IPs, fingerprints, or protected environments.
- It does not test whether Playwright automation is detectable.
- There is a minor code-quality issue in the article: the catch block refers to closing `chrome`, while the browser variable is named `browser`.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates one basic building block of browser automation: preserving session state by reading cookies from an automated browser context.

- **What does it fail to represent?**  
  It does not represent malicious bot use, anti-bot evasion, real-world attacker behaviour, production session replay, or detection trade-offs. It does not show that cookie reuse is sufficient against modern defences.

- **What additional evidence would be needed to go further?**  
  Official Playwright documentation on cookies/storage state; MDN/RFC material on cookies and session attributes; web-security guidance on session management; bot-management sources explaining how cookies interact with browser/device fingerprints, IP reputation, TLS/HTTP fingerprints, behaviour, and account-risk models.

## What it cannot show

- It cannot show that captured cookies can impersonate users in protected production systems.
- It cannot show that cookie reuse bypasses bot detection.
- It cannot show how modern defences bind sessions to browser, device, IP, TLS, behaviour, or risk signals.
- It cannot show attacker prevalence or abuse impact.
- It cannot support claims about credential stuffing, scraping, ticket bots, or account takeover without other evidence.
- It cannot replace official Playwright documentation.

## Project impact

Use this as a **minor foundations / automation-techniques entry**.

Best uses:

- explain that Playwright can read cookies from a browser context;
- show that authenticated browser automation can preserve state;
- support a simple “scripts vs browser automation” explanation;
- bridge cookies/sessions foundations to browser automation.

Do not use it as:

- abuse evidence;
- bypass evidence;
- detection evidence;
- proof of attacker capability beyond a narrow automation API capability;
- a source for session-security best practice.

## Relationship to stronger sources

- Pair with **MDN cookies** for cookie concepts and attributes.
- Pair with **official Playwright docs** for canonical automation/storage-state behaviour.
- Pair with **PortSwigger authentication/session material** for security implications.
- Pair with **OWASP OAT** only at a high level if mapping authenticated automation to broader threat categories.
- Pair with **vendor/academic bot-detection sources** when discussing how sessions are linked with other signals.

## Dual-use containment

This source includes a simple cookie-capture automation example. In project use, keep it at the concept level: automation frameworks can access and preserve session state. Do not turn it into a recipe for cookie replay, session takeover, or bypassing login/anti-bot controls.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `medium-armanabbasi-2023-playwright-cookies` |
| Title | *How to Get and Use Cookies in Playwright: A Step-by-Step Guide for Beginners* |
| Organisation / authors | armanabbasi / Medium |
| Year | 2023 |
| Category | foundations |
| Evidence basis | tutorial / capability-doc |
| Operational proximity | capability |
| Signals / techniques | cookies; Playwright browser contexts; Chromium automation; `context.cookies`; authenticated state |
| Threat types | none directly; indirectly relevant to credentialed automation/session continuity |
| Project use | Minor foundation example for cookies/session state in browser automation |
| Main caution | Beginner tutorial only; not abuse, bypass, detection, or security-best-practice evidence |
| Entry file | `medium-armanabbasi-2023-playwright-cookies.md` |
