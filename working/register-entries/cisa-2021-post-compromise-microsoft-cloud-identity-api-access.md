# CISA (2021) - Detecting post-compromise threat activity in Microsoft cloud environments

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF `SRC-094-cisa-2021-post-compromise-microsoft-cloud-identity-api-access.pdf`.
- **Source handling decision**: keep as a smaller supporting entry. It is official and relevant to cloud identity compromise, but archived/older and SolarWinds/SVR-linked, so it should not be treated as current trend evidence.

## Bibliographic

- **Citation**: CISA. (2021). *Detecting Post-Compromise Threat Activity in Microsoft Cloud Environments*. Cybersecurity Advisory AA21-008A, last revised 15 April 2021.
- **Source URL or path**: uploaded PDF `SRC-094-cisa-2021-post-compromise-microsoft-cloud-identity-api-access.pdf`.
- **Category**: official guidance / cloud identity post-compromise
- **Evidence basis**: government advisory / detection guidance / incident-linked TTPs
- **Operational proximity**: observed-guidance — relevant to real post-compromise cloud activity, but historical and archived.
- **Tags**: CISA, Microsoft-cloud, Azure-AD, M365, O365, SolarWinds, SVR, federated-identity, forged-tokens, Golden-SAML, OAuth, API-access, service-principals, Sparrow, cloud-persistence, post-compromise-detection

## What it claims

- CISA observed an APT actor using compromised applications in Microsoft 365/Azure environments.
- The activity involved:
  - compromising or bypassing federated identity solutions;
  - using forged authentication tokens to move laterally into Microsoft cloud environments;
  - using privileged cloud access to establish difficult-to-detect API-based persistence.
- Initial access may come from SolarWinds Orion compromise, password guessing/spraying, or inappropriately secured administrative/service credentials.
- Sophisticated actors can use credentials from one part of an organisation to cross trust boundaries, evade detection, and access cloud resources.

## What evidence it provides

This is an official detection advisory. It provides:

- high-level TTPs for Microsoft cloud post-compromise activity;
- relevance to Azure AD, O365, M365, and ADFS;
- MITRE ATT&CK mapping;
- discussion of forged OAuth/SAML-style tokens;
- detection and hunting guidance;
- reference to CISA’s Sparrow tool and other analysis/detection resources.

It does **not** provide:

- current 2026 telemetry;
- bot-specific evidence;
- SaaS pricing evidence;
- public raw incident data;
- general prevalence statistics;
- broad cloud threat landscape coverage.

## Important evidence

- The advisory says CISA saw compromised applications in Microsoft 365/Azure and additional credentials/API access to cloud resources.
- It names three key components: federated identity compromise/bypass, forged authentication tokens, and privileged cloud access for API-based persistence.
- It notes that this level of compromise is challenging to remediate and needs multi-disciplinary recovery.
- The document is marked archived, so do not use it as current policy or current trend guidance.

## Signals or techniques mentioned

- Microsoft 365;
- Azure AD / Entra ID predecessor naming;
- O365/M365;
- ADFS certificate-signing capability;
- forged authentication tokens;
- OAuth;
- SAML/Golden SAML-style attacks;
- API-based access;
- compromised applications;
- service principals;
- password guessing;
- password spraying;
- unsecured administrative/service credentials;
- lateral movement across trust boundaries;
- MFA bypass/manipulation;
- Sparrow;
- Azure Sentinel / Microsoft cloud logs.

## Threat types covered

Directly relevant:

- cloud identity compromise;
- cloud post-compromise persistence;
- valid credential/service-principal abuse;
- forged token abuse;
- API-based access.

Indirect OAT relevance:

- **OAT-008 Account Takeover** — relevant at enterprise identity/cloud level.
- **OAT-020 Account Aggregation** — conceptually relevant where cloud access aggregates data across services.
- **OAT-018 Footprinting** — possible in cloud discovery, but not core.
- Not scraping/scalping/CAPTCHA/proxy evidence.

## What is strong

- Official government source.
- Good non-vendor support for the idea that cloud/SaaS compromise is often identity/API/token based.
- Useful control framing around detecting cloud post-compromise activity.
- Good historical anchor for the move from on-prem compromise into cloud identity and API persistence.

## What is weak or limited

- Archived content.
- Last revised in 2021.
- SolarWinds/SVR-specific context.
- Microsoft-cloud-specific.
- Not current trend evidence.
- Not bot-specific.
- Some tool and product names have changed.

## Project impact

Use this as a **smaller official cloud identity supporting entry**.

Best uses:

- support the cloud/SaaS abuse section with non-vendor official guidance;
- show that API access, service principals, tokens, and federated identity are long-standing cloud compromise issues;
- balance Recorded Future’s 2026 cloud report with CISA official material.

Do not use it as:

- current prevalence evidence;
- current Microsoft-product guidance without checking current docs;
- bot/automated-threat evidence.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `cisa-2021-post-compromise-microsoft-cloud-identity-api-access` |
| Title | *Detecting Post-Compromise Threat Activity in Microsoft Cloud Environments* |
| Organisation | CISA |
| Year | 2021 |
| Category | official guidance / cloud identity post-compromise |
| Evidence basis | government advisory / detection guidance / incident-linked TTPs |
| Operational proximity | observed-guidance |
| Signals / techniques | federated identity; forged tokens; OAuth/SAML; Azure AD; M365; API access; service principals; Sparrow |
| Threat types | cloud identity compromise; API-based persistence; indirect OAT-008/OAT-020 relevance |
| Project use | Smaller official source for cloud identity/API post-compromise behaviour |
| Main caution | Archived and older; not current trend or bot-specific evidence |
| Entry file | `cisa-2021-post-compromise-microsoft-cloud-identity-api-access.md` |
