# FBI/CISA et al. (2025) - Scattered Spider advisory: identity abuse, helpdesk social engineering, and legitimate-tool use

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**:
  - canonical uploaded PDF `SRC-095-aa23-320a-scattered-spider-508c.pdf` dated 29 July 2025;
  - older uploaded PDF `SRC-095-aa23-320a-scattered-spider-0.pdf` dated 16 November 2023, used only as historical/source-family context.
- **Source handling decision**: use the 2025 updated advisory as canonical. Fold the 2023 advisory into this entry only if comparing evolution.

## Bibliographic

- **Citation**: FBI, CISA, RCMP, ASD’s ACSC, AFP, CCCS, and NCSC-UK. (2025). *Scattered Spider*. Joint Cybersecurity Advisory AA23-320A, updated 29 July 2025.
- **Source URL or path**: uploaded PDF `SRC-095-aa23-320a-scattered-spider-508c.pdf`.
- **Category**: official government advisory / actor TTPs
- **Evidence basis**: government advisory / investigation-derived TTPs / MITRE ATT&CK mapping
- **Operational proximity**: observed-investigative — strong non-vendor evidence for identity/social-engineering/legitimate-tool abuse, but actor-specific and not bot-specific.
- **Tags**: Scattered-Spider, UNC3944, Octo-Tempest, Muddled-Libra, helpdesk-social-engineering, SIM-swap, MFA-fatigue, OTP, RMM-tools, remote-access-tools, valid-accounts, SSO, cloud-discovery, ransomware, DragonForce, BlackCat, account-takeover, identity-abuse

## What it claims

- Scattered Spider is a cybercriminal group targeting large companies and contracted IT helpdesks.
- The group uses social engineering, SMS/voice phishing, push bombing/MFA fatigue, and SIM swapping to obtain credentials, install remote access tools, or bypass MFA.
- The group impersonates IT/helpdesk staff and, in updated TTPs, can pose as employees to convince helpdesk personnel to provide sensitive information or reset access.
- After access, actors use legitimate remote monitoring/management and tunneling tools.
- The group abuses valid accounts, MFA token changes, federated identity, SSO, cloud dashboards, and discovery of SharePoint, vCenter, backups, and credential documentation.
- The 2025 update notes data theft for extortion and ransomware use, including DragonForce alongside prior TTPs.

## What evidence it provides

This is an official joint advisory. It provides:

- government-backed summary of recent activity and TTPs;
- MITRE ATT&CK mappings;
- lists of legitimate tools repurposed for criminal activity;
- identity and MFA abuse patterns;
- social-engineering and helpdesk compromise patterns;
- discovery and cloud-service dashboard abuse;
- mitigation recommendations:
  - offline backups;
  - phishing-resistant MFA;
  - application controls;
  - credential and access hardening;
  - monitoring of remote access tooling and identity events.

It does **not** provide:

- bot-specific telemetry;
- automated web abuse evidence;
- marketplace pricing;
- exact victim logs;
- neutral prevalence measurements;
- full campaign reconstruction for all incidents.

## Important evidence

- The 2025 advisory is co-authored by several government agencies and says TTPs were obtained through FBI investigations as recently as June 2025.
- It highlights social engineering, push bombing, SIM swap, credential theft, and use of commercial remote access tools.
- It maps Scattered Spider activity to MITRE ATT&CK, including phishing, trusted relationships, valid accounts, user execution, persistence via accounts/MFA modifications, domain trust/federated identity changes, and cloud instance use.
- The older 2023 advisory gives similar core TTPs and useful detail on Scattered Spider adding federated identity providers, registering MFA tokens, searching SharePoint and credential stores, and using AWS Systems Manager Inventory.

## Signals or techniques mentioned

- helpdesk impersonation;
- employee impersonation;
- SMS phishing / smishing;
- voice phishing / vishing;
- OTP theft;
- MFA fatigue / push bombing;
- SIM swapping;
- valid domain accounts;
- trusted relationships with IT helpdesks;
- commercial remote access/RMM tools;
- ScreenConnect;
- Splashtop;
- TeamViewer;
- Tailscale;
- Tactical.RMM;
- Ngrok;
- Pulseway;
- MFA token modification;
- forged web credentials;
- federated identity provider abuse;
- SSO tenant abuse;
- cloud instance creation;
- AWS Systems Manager Inventory;
- SharePoint discovery;
- VMware vCenter discovery;
- infrastructure backups;
- code repositories;
- ransomware and extortion.

## Threat types covered

Directly relevant:

- account takeover;
- identity abuse;
- helpdesk social engineering;
- MFA bypass;
- ransomware/extortion;
- legitimate-tool abuse;
- cloud discovery.

OAT mapping:

- **OAT-008 Credential Stuffing / Account Takeover** — strong relevance to ATO, though not credential-stuffing at scale.
- **OAT-019 Account Creation** — indirect, through account creation/persistence and identity-provider manipulation.
- **OAT-020 Account Aggregation** — indirect, where valid access enables data aggregation across SaaS/cloud assets.
- **OAT-006 Expediting** — weak; legitimate tools accelerate operations, but not a web-automation case.
- Not a scraping, CAPTCHA, scalping, or proxy-market source.

## What is strong

- Strong non-vendor balance source.
- Shows that adversarial infrastructure is not only purchased services; it can also be legitimate enterprise tools and helpdesk processes repurposed through social engineering.
- Directly supports “legitimate-tool abuse” and “identity is infrastructure” themes.
- Strong complement to Kasada’s account-market/verification-bypass framing.
- Useful control emphasis: phishing-resistant MFA, application controls, remote-tool governance, backups, and identity monitoring.

## What is weak or limited

- Actor-specific.
- Not bot-specific.
- TTPs are summarised for public advisory use, not full case evidence.
- Some TTPs come from public reporting/trusted third parties in addition to investigations.
- It can pull the review toward general ransomware/social engineering if not kept focused.

## Framing distance

- **What real-world bot/abuse problem does this approximate?**  
  Account and identity compromise through social engineering and legitimate tool abuse, which can underlie automated abuse or SaaS/cloud compromise.

- **What does it fail to represent?**  
  It does not represent web bots, scraper infrastructure, or CAPTCHA/proxy cost stacks.

## Project impact

Use this as the **official government actor/TTP balance source** for the SaaSification section.

Best uses:

- show that adversarial infrastructure includes helpdesks, identity providers, RMM tools, valid accounts, and SSO;
- support the “verification is not the same as security” point;
- connect account-market sources to real-world identity compromise;
- add non-vendor weight to identity/MFA sections.

Do not use it as:

- bot telemetry;
- scraping/scalping evidence;
- broad prevalence measurement.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `cisa-fbi-2025-scattered-spider-identity-helpdesk-legitimate-tools` |
| Title | *Scattered Spider Joint Cybersecurity Advisory* |
| Organisations | FBI, CISA, RCMP, ASD ACSC, AFP, CCCS, NCSC-UK |
| Year | 2025 |
| Category | official government advisory / actor TTPs |
| Evidence basis | government advisory / investigation-derived TTPs / MITRE ATT&CK mapping |
| Operational proximity | observed-investigative |
| Signals / techniques | helpdesk impersonation; SIM swap; MFA fatigue; OTP theft; RMM tools; valid accounts; SSO/federated identity; cloud discovery |
| Threat types | ATO/identity abuse; legitimate-tool abuse; ransomware/extortion; indirect OAT-008/OAT-019 relevance |
| Project use | Non-vendor source for identity abuse and legitimate-tool infrastructure |
| Main caution | Actor-specific and not bot-specific |
| Entry file | `cisa-fbi-2025-scattered-spider-identity-helpdesk-legitimate-tools.md` |
