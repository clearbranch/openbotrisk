# PortSwigger Web Security Academy - How to secure your authentication mechanisms

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF export of PortSwigger Web Security Academy page.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: PortSwigger Web Security Academy. 2026. *How to secure your authentication mechanisms*. PortSwigger.
- **Source URL or path**: `How to secure your authentication mechanisms _ Web Security Academy.pdf`; likely WSA topic page `https://portswigger.net/web-security/authentication/securing`
- **Date accessed / captured**: uploaded 2026-06-06
- **Category**: vendor / defensive-guidance
- **Evidence basis**: control-guidance
- **Operational proximity**: control - defensive implementation guidance, not observed abuse or measured efficacy.
- **Tags**: authentication-security, password-policy, zxcvbn, username-enumeration, rate-limiting, brute-force-protection, captcha, mfa, 2fa, password-reset

## What it claims

- Strong authentication can fail if valid login credentials are disclosed, including through unencrypted connections or username/email disclosure in public profiles or HTTP responses.
- Websites should not rely on users to behave securely; secure behaviour should be enforced where possible.
- Password strength checking can be more effective than simplistic composition rules because users often adapt predictable passwords to pass traditional policies.
- Username enumeration should be prevented by using identical generic messages, identical HTTP status codes, and response times that are as indistinguishable as possible.
- Brute-force protection should disrupt automated login attempts; PortSwigger recommends strict IP-based rate limiting and CAPTCHA after limits, while noting this does not eliminate the threat.
- Verification and validation logic, including supplementary flows such as password reset/change, should be checked carefully.
- MFA is stronger when implemented with a dedicated app or device; email codes are not true multi-factor authentication and SMS 2FA has reliability issues such as SIM swapping.

## What evidence it provides

- This is a useful defensive-control checklist for the authentication-abuse strand.
- It supports the idea that bot/login-abuse defence is not only about a WAF: application logic, error handling, password policy, rate limiting, and recovery flows all matter.
- It also provides caveats: rate limits and CAPTCHA increase friction but do not remove the threat.

## Signals or techniques mentioned

- HTTPS enforcement
- username/email leakage
- password strength checking
- zxcvbn
- generic error messages
- identical status codes
- response-time equalisation
- IP-based user rate limiting
- CAPTCHA after login limits
- verification logic
- password reset/change flows
- MFA/2FA
- SMS 2FA limitations
- app/device-based 2FA

## Threat types covered

- credential disclosure
- username enumeration
- brute-force login
- authentication bypass
- password-reset abuse
- MFA bypass or weak MFA implementation
- credential stuffing, by implication through brute-force/login protection

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** Defensive hardening against automated login abuse and authentication bypass.
- **What does it fail to represent?** It does not provide empirical evidence that these controls stop specific attacks or quantify residual risk.
- **What additional evidence would be needed to go further?** NIST/OWASP primary guidance, production telemetry, usability/security studies on MFA, or evaluations of rate-limiting and CAPTCHA controls.

## What it cannot show

- It cannot prove a given password policy is optimal.
- It cannot quantify CAPTCHA or rate-limit effectiveness.
- It cannot show how attackers currently bypass MFA at scale.
- It cannot replace formal standards such as OWASP ASVS or NIST authentication guidance.

## Project impact

Use as the defensive counterpart to the password-login vulnerability entry. It is useful for a “what closes down the easy routes?” section: generic errors, rate limits, robust verification logic, protected reset/change flows, and proper MFA.

## Possible register row

| Field | Value |
|---|---|
| Register id | `portswigger-2026-secure-authentication-mechanisms` |
| Title | *How to secure your authentication mechanisms* |
| Category | vendor / defensive-guidance |
| Evidence basis | control-guidance |
| Operational proximity | control |
| Tags | authentication-security; password-policy; zxcvbn; username-enumeration; rate-limiting; brute-force-protection; captcha; mfa; 2fa; password-reset |
| Project use | Defensive controls for login/authentication abuse |
| Main caution | Practical guidance, not independent control-effectiveness evidence |
