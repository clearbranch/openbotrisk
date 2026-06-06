# PortSwigger Web Security Academy - Vulnerabilities in password-based login

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF export of PortSwigger Web Security Academy page.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: PortSwigger Web Security Academy. 2026. *Vulnerabilities in password-based login*. PortSwigger.
- **Source URL or path**: `Vulnerabilities in password-based login _ Web Security Academy.pdf`; likely WSA topic page `https://portswigger.net/web-security/authentication/password-based`
- **Date accessed / captured**: uploaded 2026-06-06
- **Category**: vendor / educational-reference
- **Evidence basis**: methods-taxonomy
- **Operational proximity**: capability - describes attack classes and defensive failure modes, not measured prevalence.
- **Tags**: password-login, brute-force, username-enumeration, credential-stuffing, account-locking, rate-limiting, http-basic-auth, account-takeover

## What it claims

- Password-based login treats knowledge of the secret password as proof of identity, making the site vulnerable if credentials are guessed or obtained.
- Brute-force attacks use trial and error, often automated with username/password wordlists, and can be made more efficient using predictable username formats and human password patterns.
- Username enumeration can occur through different status codes, different error messages, or response-time differences.
- Brute-force protection often relies on account locking or IP-based blocking, but both can fail if implemented with flawed logic.
- Account locking does not adequately prevent attacks that try common passwords across many accounts, and it does not stop credential stuffing using breached username/password pairs.
- HTTP Basic Authentication is described as generally weak: credentials are repeatedly sent in the Authorization header and it often lacks brute-force protection and CSRF protection.

## What evidence it provides

- This is a strong foundation source for the login-abuse track.
- It directly explains why simple defences such as IP blocks and account locks are not complete answers.
- It connects well to scraper/bot infrastructure sources: rotating IPs, apparent-IP manipulation, and automation become relevant because rate limits and IP blocks are common defences.
- It gives a clean conceptual bridge from credential dumps to credential stuffing.

## Signals or techniques mentioned

- username enumeration
- status-code differences
- error-message differences
- response-timing differences
- brute-force wordlists
- predictable usernames
- predictable password patterns
- account locking
- IP-based blocking
- rate limiting
- CAPTCHA after limits
- credential stuffing
- HTTP Basic Authentication
- Authorization header

## Threat types covered

- brute-force login
- credential stuffing
- username enumeration
- account takeover
- basic-auth brute force
- session-related weaknesses / CSRF exposure in basic-auth contexts

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** Automated login abuse, especially brute-force and credential-stuffing attempts against password-based authentication.
- **What does it fail to represent?** It does not measure attack frequency, current tooling, target sectors, or real-world success rates.
- **What additional evidence would be needed to go further?** Vendor login-attack telemetry, breach credential reuse studies, legal cases, or honeypot/experiment studies.

## What it cannot show

- It cannot quantify credential-stuffing prevalence.
- It cannot prove any particular defence is sufficient.
- It cannot show effectiveness of CAPTCHA, rate limiting, or IP blocking in the wild.
- It cannot prove specific attacker business models.

## Project impact

Use this as a core foundation source for credential stuffing and login abuse. It is especially useful when explaining why IP reputation, rate limiting, account locking, and CAPTCHA are partial controls rather than final solutions.

## Possible register row

| Field | Value |
|---|---|
| Register id | `portswigger-2026-password-based-login-vulnerabilities` |
| Title | *Vulnerabilities in password-based login* |
| Category | vendor / educational-reference |
| Evidence basis | methods-taxonomy |
| Operational proximity | capability |
| Tags | password-login; brute-force; username-enumeration; credential-stuffing; account-locking; rate-limiting; http-basic-auth; account-takeover |
| Project use | Foundation for credential stuffing and login-abuse mechanics |
| Main caution | Educational attack/defence taxonomy; not real-world prevalence evidence |
