# PortSwigger Web Security Academy - OAuth 2.0 authentication vulnerabilities

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF export of PortSwigger Web Security Academy page.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: PortSwigger Web Security Academy. 2026. *OAuth 2.0 authentication vulnerabilities*. PortSwigger.
- **Source URL or path**: `OAuth 2.0 authentication vulnerabilities _ Web Security Academy.pdf`; likely WSA topic page `https://portswigger.net/web-security/oauth`
- **Date accessed / captured**: uploaded 2026-06-06
- **Category**: vendor / educational-reference
- **Evidence basis**: methods-taxonomy
- **Operational proximity**: capability - educational material describing vulnerability classes in OAuth implementations, not observed abuse prevalence.
- **Tags**: oauth, oauth2, third-party-authentication, social-login, implicit-flow, redirect-uri, csrf, access-token, authorization-code, scope-validation, openid-connect, account-takeover

## What it claims

- OAuth is a commonly used authorization framework that is also widely used for third-party authentication/social login.
- OAuth authentication can be prone to implementation mistakes because the specification is flexible and many configuration settings are optional.
- Vulnerabilities can arise in the client application’s OAuth implementation or in the OAuth service configuration.
- Vulnerability classes include improper implementation of the implicit grant type, flawed CSRF protection, leaking authorization codes/access tokens, flawed scope validation, and unverified user registration.
- The `state` parameter should ideally contain an unguessable value and function as CSRF protection for the client application.
- Redirect URI validation is a major security control; flawed validation can enable code/token leakage.
- Access-token theft can allow not only login to the victim’s account but also API calls to the OAuth resource server.

## What evidence it provides

- This is strong foundation material for third-party authentication risk.
- It shows why “login with X” should be treated as part of the authentication attack surface, not as an automatically safe outsourcing of identity.
- It is useful for the project where account takeover and automated abuse intersect: OAuth flows create web/API interactions that can be probed, misconfigured, or abused.

## Signals or techniques mentioned

- OAuth grant types
- authorization endpoint
- `client_id`
- `redirect_uri`
- `response_type`
- authorization code
- access token
- implicit grant
- CSRF / missing or weak `state`
- redirect URI validation
- `.well-known/oauth-authorization-server`
- `.well-known/openid-configuration`
- scope validation
- unverified user registration
- OpenID Connect

## Threat types covered

- OAuth authentication bypass
- account hijacking through OAuth misconfiguration
- token leakage
- authorization-code leakage
- forced OAuth profile linking
- scope upgrade
- third-party authentication abuse
- API access using stolen tokens

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** Abuse of third-party login and OAuth-based authentication flows, including account takeover and token/API misuse.
- **What does it fail to represent?** It does not quantify prevalence, show bot automation at scale, or provide real-world incident counts.
- **What additional evidence would be needed to go further?** Real OAuth incident reports, bug bounty disclosures, standards guidance, OAuth/OIDC security BCPs, or telemetry on automated OAuth probing.

## What it cannot show

- It cannot prove OAuth is generally unsafe.
- It cannot show how often these flaws occur in production.
- It cannot quantify attacker automation around OAuth flows.
- It cannot replace the OAuth/OIDC specifications or best-current-practice documents.

## Project impact

Use this as the OAuth/third-party-authentication foundation entry. It broadens the login-abuse section beyond simple username/password forms and supports a “authentication is a system of flows” framing.

## Possible register row

| Field | Value |
|---|---|
| Register id | `portswigger-2026-oauth-2-authentication-vulnerabilities` |
| Title | *OAuth 2.0 authentication vulnerabilities* |
| Category | vendor / educational-reference |
| Evidence basis | methods-taxonomy |
| Operational proximity | capability |
| Tags | oauth; oauth2; third-party-authentication; social-login; implicit-flow; redirect-uri; csrf; access-token; authorization-code; scope-validation; openid-connect; account-takeover |
| Project use | Foundation for third-party authentication/OAuth abuse pathways |
| Main caution | Educational vulnerability taxonomy; not observed abuse prevalence or standard-setting guidance |
