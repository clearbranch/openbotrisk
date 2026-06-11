# PortSwigger Web Security Academy - Authentication vulnerabilities

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF export of PortSwigger Web Security Academy page.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: PortSwigger Web Security Academy. 2026. *Authentication vulnerabilities*. PortSwigger.
- **Source URL or path**: `SRC-072-portswigger-2026-authentication-vulnerabilities.pdf`; likely WSA topic page `https://portswigger.net/web-security/authentication`
- **Date accessed / captured**: uploaded 2026-06-06
- **Category**: vendor / educational-reference
- **Evidence basis**: vulnerability-taxonomy
- **Operational proximity**: capability - educational material describing classes of weaknesses and lab scenarios, not observed abuse prevalence.
- **Tags**: authentication, broken-authentication, brute-force, authorization, account-takeover, attack-surface, web-security-academy

## What it claims

- Authentication vulnerabilities are usually critical because authentication is directly tied to access control and security.
- They can allow attackers to access sensitive data/functionality and can expose extra attack surface for further exploitation.
- Authentication vulnerabilities commonly arise because mechanisms are weak against brute-force attacks or because implementation logic allows authentication to be bypassed.
- Impact can range from access to a low-privileged account to full application compromise if a high-privileged account is compromised.
- PortSwigger breaks the topic into password-based login, MFA, other authentication mechanisms, and third-party mechanisms such as OAuth.

## What evidence it provides

- This is useful foundation material for explaining why account-takeover and automated login attempts matter.
- It links authentication failure to both initial account compromise and follow-on exploitation.
- It supports the project’s “account abuse” strand, but as a taxonomy/source of concepts rather than empirical measurement.

## Signals or techniques mentioned

- brute-force attacks
- broken authentication
- authentication bypass
- password-based login
- multi-factor authentication weaknesses
- third-party authentication
- OAuth authentication
- account takeover
- privilege impact

## Threat types covered

- account takeover
- brute-force login
- authentication bypass
- post-login attack-surface expansion
- high-privilege account compromise

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** Automated and semi-automated attempts to gain access to accounts through login and authentication weaknesses.
- **What does it fail to represent?** It does not quantify real-world prevalence, attacker volume, success rates, economic harm, or current bot tooling.
- **What additional evidence would be needed to go further?** Credential-stuffing telemetry, legal cases, breach reports, honeypot studies, or vendor/academic measurement of login-abuse traffic.

## What it cannot show

- It cannot prove these attacks are common on a specific site.
- It cannot show automation prevalence.
- It cannot show bot-detection effectiveness.
- It cannot act as legal or regulatory evidence.

## Project impact

Use as a foundation entry for authentication as an attack surface. It helps connect bot automation to concrete outcomes: brute-forcing, credential stuffing, account takeover, and post-login abuse.

## Possible register row

| Field | Value |
|---|---|
| Register id | `portswigger-2026-authentication-vulnerabilities` |
| Title | *Authentication vulnerabilities* |
| Category | vendor / educational-reference |
| Evidence basis | vulnerability-taxonomy |
| Operational proximity | capability |
| Tags | authentication; broken-authentication; brute-force; authorization; account-takeover; attack-surface; web-security-academy |
| Project use | Foundation for authentication/account-takeover attack surface |
| Main caution | Educational taxonomy and labs; not observed abuse prevalence |
