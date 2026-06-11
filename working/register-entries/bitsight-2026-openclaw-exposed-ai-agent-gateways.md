# Bitsight (2026) - OpenClaw: exposed AI-agent gateways and enterprise risk

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF capture `SRC-086-bitsight-2026-openclaw-exposed-ai-agent-gateways.pdf`.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.
- **Relationship to existing OpenClaw source**: keep separate from the existing HUMAN Security OpenClaw entry. HUMAN focuses on OpenClaw-associated traffic and abuse patterns; this Bitsight source focuses on internet exposure, configuration risk, integrations/blast radius, and exposed-agent attack surface.

## Bibliographic

- **Citation**: Cruz, J. / Bitsight. (2026). *OpenClaw (ex-Moltbot (ex-Clawdbot)): The AI Butler With Its Claws On The Keys To Your Kingdom*. Bitsight Research Blog. Published 9 February 2026.
- **Source URL or path**: uploaded PDF `SRC-086-bitsight-2026-openclaw-exposed-ai-agent-gateways.pdf`.
- **Date accessed / captured**: uploaded 2026-06-07.
- **Category**: vendor / threat-research
- **Evidence basis**: empirical-exposure measurement / attack-surface analysis / threat-intelligence
- **Operational proximity**: observed-exposure — reports internet-wide scanning of exposed OpenClaw/Clawdbot/Moltbot instances and security analysis of the tool’s deployment patterns. It is stronger for exposure than for confirmed abuse.
- **Tags**: Bitsight, OpenClaw, Clawdbot, Moltbot, AI-agents, agentic-AI, exposed-services, internet-scanning, autonomous-agents, browser-automation, integrations, blast-radius, prompt-injection, remote-code-execution, credential-exposure, cloud-deployment, misconfiguration, default-port, WebSocket-API, reverse-proxy, weak-token, supply-chain-impersonation

## What it claims

- OpenClaw, formerly Moltbot and before that Clawdbot, is a fast-growing open-source/self-hosted AI-agent platform.
- It functions as a persistent AI assistant reachable through chat apps and integrations.
- Its risk comes from being granted broad access to local systems and third-party services, then being exposed to the public internet by users seeking convenience.
- Bitsight observed more than 30,000 distinct OpenClaw and related-variant instances exposed online during the January 27 to February 8, 2026 analysis period.
- OpenClaw’s growth was rapid, with GitHub-star and internet-exposure growth both rising sharply in early 2026.
- Exposed instances appeared not only in hosting/cloud infrastructure but also in sensitive sectors such as healthcare, finance, government, and insurance.
- The main risk is not that OpenClaw is inherently malicious. The risk is that a powerful agent with integrations, system access, and weak deployment boundaries can become a highly privileged exposed service.
- The article warns that each integration expands the blast radius: email, GitHub, smart home, local files, shell access, browsers, and other connected services.
- It also discusses prompt injection, remote code execution through the assistant’s system access, credential/key exposure, and supply-chain impersonation during rapid rebranding.

## What evidence it provides

This is a **vendor threat-research and exposure-measurement source**.

It provides:

- a description of OpenClaw’s user promise and integration model;
- screenshots of the OpenClaw gateway/control-panel installation path;
- screenshots of warning messages shown during installation;
- explanation of gateway bind modes and exposure patterns;
- description of common ways users worked around local-only access restrictions;
- observations from Bitsight’s Groma internet-scanning infrastructure;
- a targeted scan of the default OpenClaw-related gateway port across January 27 to February 8, 2026;
- geographic and sector distribution charts;
- examples of how compromise of an exposed agent can affect integrated services;
- discussion of ecosystem side-effects such as bot-only social networks and rebranding-related impersonation.

### Key quantitative details

| Measure | Reported value |
|---|---:|
| Initial baseline window | January 1 to January 27, 2026 |
| Targeted daily-scan window | January 27 to February 8, 2026 |
| Default gateway port scanned | 18789/tcp |
| Cumulative exposed instances by January 27 baseline | almost 1,000 since beginning of year |
| Distinct exposed instances in daily snapshots | more than 30,000 |
| Cumulative chart endpoint | 31,674 by February 8 |
| Largest daily growth noted | +177% between January 27 and January 28 |
| Named variants tracked | Clawdbot, Moltbot, OpenClaw |

### Important visual evidence in the PDF

- **Page 4** shows the OpenClaw Gateway control panel after installation, which helps explain why the product becomes a privileged control plane rather than just a chat interface.
- **Page 6** shows the project’s own warning screen during installation, including warnings that the bot can read files, run actions/tools, access files in allowed directories, and should not be used on hosts with secrets or untrusted labour. This is useful because the risk is partly acknowledged by the tool itself.
- **Page 10** shows the weak-token example where a one-character token is accepted, supporting the concern that authentication can exist formally while still being weak in practice.
- **Page 11** shows daily exposed-instance counts from targeted scans, with counts rising rapidly across January 27 to February 8.
- **Page 13** shows cumulative exposed instances, reaching more than 30,000 over the scan period.
- **Page 14** shows the geographic distribution and a top-10 country table for exposed instances.
- **Page 15** shows sector distribution, with Technology dominating but sensitive sectors also present.
- **Pages 16–17** show screenshots from Bitsight’s own test instance demonstrating that a connected agent can run commands and search for configuration/API secrets. The article explicitly says these screenshots are from their own instance and not from unauthorized access to exposed systems.
- **Page 20** discusses rebranding-related impersonation and typosquatting, including malicious domains and a cloned repository reported by Malwarebytes.

## Signals or techniques mentioned

- exposed AI-agent gateways;
- self-hosted agent control plane;
- chat-app integrations;
- LLM-provider integration;
- WhatsApp, Telegram, Discord, Slack, Teams;
- GitHub, Trello, Notion, Gmail, browser, social, smart-home integrations;
- persistent assistant with delegated user privileges;
- public HTTP interface exposure;
- gateway bind mode;
- local-only / loopback mode;
- LAN/public binding;
- Tailscale/VPN access;
- reverse proxy exposure;
- insecure-auth configuration;
- token/password authentication;
- weak token/password complexity;
- WebSocket API;
- authentication-bypass attempts;
- protocol-downgrade attempts;
- prompt-injection attempts;
- raw command execution attempts;
- remote code execution through agent capabilities;
- credential/API-key discovery;
- internet-wide scanning;
- default-port scanning;
- project rebranding and typosquatting;
- cloned repositories;
- supply-chain impersonation.

## Threat types covered

Directly covered:

- exposed AI-agent gateway risk;
- misconfigured self-hosted control planes;
- prompt injection against integrated agents;
- remote command execution through an agent’s delegated capabilities;
- credential/API-key exposure;
- source-code/repository risk through GitHub integrations;
- corporate mailbox compromise through email integrations;
- smart-home or local-device control;
- supply-chain impersonation around fast-moving open-source projects;
- shadow IT / unsanctioned deployment of AI agents in corporate or sensitive-sector environments.

OAT mapping:

- OAT-018 Footprinting — exposed gateway discovery and reconnaissance.
- OAT-014 Vulnerability Scanning — probing exposed gateways/API methods.
- OAT-015 Denial of Service — possible but not central in this source.
- OAT-011 Scraping — indirect, if agents browse or automate data collection; not the main focus.
- OAT-016 Skewing — possible through agentic synthetic engagement, but better supported by the separate HUMAN OpenClaw entry.
- OAT-020 Account Aggregation — conceptually relevant where an agent aggregates access across user accounts/services.
- OAT-006 Expediting — indirect, if agents speed up normal workflows using integrations.
- Credential/session compromise risks are present, but this source is more about exposed-agent control planes than classic credential stuffing.

## What is strong

- Strong current source for exposed AI-agent attack surface.
- Stronger than generic “AI agents might be risky” commentary because it includes scanning windows, instance counts, geographic/sector charts, and concrete deployment/configuration patterns.
- Useful complement to HUMAN’s OpenClaw source:
  - Bitsight = exposed instances, internet scanning, deployment/configuration risk, blast radius;
  - HUMAN = observed traffic/abuse patterns associated with OpenClaw gateways.
- Useful for explaining why agentic tools are not just “bots that make requests”. They can inherit human/user privileges across many integrated services.
- Useful for the shadow-IT and governance strand: personal tools can connect to corporate mailboxes, code repositories, files, and internal workflows.
- Useful for explaining why “agent safety” is not only model-output safety; it is also network exposure, authentication, integrations, secrets, and operational boundaries.

## What is weak or limited

- Vendor threat-research blog, not peer-reviewed academic work.
- Underlying scan methodology is described at a high level but not reproducible from the article alone.
- Exposed instance counts do not prove compromise or abuse.
- It focuses on one high-profile tool and may not generalise cleanly to all agentic systems.
- The article includes illustrative local demonstrations from Bitsight’s own instance; these show capability/risk, not exploitation of third-party systems.
- It does not provide success rates for attacks against exposed instances.
- It does not provide detailed validation of false positives in exposed-instance detection.
- Sector attribution depends on Bitsight’s own Graph of Internet Assets/entity mapping, which is not independently auditable from the article.
- Some claims rely on external sources such as Malwarebytes and creator/project posts, which should be verified separately if used as load-bearing claims.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  The attack surface created when browser-capable or system-capable AI agents are deployed as exposed services with broad integrations and inherited user privileges.

- **What does it fail to represent?**  
  It does not prove that exposed OpenClaw instances were widely exploited. It does not measure the downstream abuse traffic generated by agents in the way HUMAN’s source attempts to. It does not show prevalence across all AI-agent frameworks.

- **What additional evidence would be needed to go further?**  
  Independent scanning, reproducible detection signatures, vulnerability advisories, incident reports, honeypot data, vendor telemetry, endpoint/security logs from affected organisations, and follow-up sources on MCP/agent frameworks beyond OpenClaw.

## What it cannot show

- It cannot show all exposed OpenClaw instances were malicious or compromised.
- It cannot show all OpenClaw deployments were unsafe.
- It cannot show internet-wide prevalence of exposed AI-agent systems beyond this named tool and its variants.
- It cannot show successful exploitation rates.
- It cannot show whether Bitsight’s sector attribution is correct in each case.
- It cannot show bot-detection performance.
- It cannot show that OpenClaw itself is malware.
- It cannot replace the existing HUMAN OpenClaw observed-traffic source.

## Project impact

Use this as a **high-value exposed-agent attack-surface source**.

Best uses:

- add an “exposed AI-agent control planes” strand to the agentic-traffic section;
- explain the difference between agent capability, exposed deployment, and observed abuse;
- show how a user-facing agent becomes a privileged system when connected to email, GitHub, browser, files, and shell access;
- support the governance point that agentic tools expand trust boundaries;
- connect agentic automation to application-security concepts: authentication, exposure, secrets, least privilege, network boundaries, and monitoring;
- pair with HUMAN OpenClaw for a stronger two-source treatment:
  - Bitsight for exposure and blast radius;
  - HUMAN for observed request/abuse patterns.

Do not use it as:

- proof that OpenClaw is malicious;
- proof that all exposed agents are exploited;
- proof of agentic abuse prevalence across the whole web;
- evidence that a particular detection product works;
- a procedural guide to exposing or attacking instances.

## Relationship to other register entries

- **HUMAN OpenClaw in the wild**: existing OpenClaw source; keep as separate. It is closer to observed abuse/traffic patterns. Bitsight is closer to exposure measurement and attack-surface governance.
- **HUMAN Agentic Visibility / State of Agentic Traffic**: broader agentic-traffic framing; Bitsight gives a concrete named-tool exposure case.
- **Cloudflare Block AI Bots**: AI crawler/content-access governance; Bitsight is agent-control-plane exposure, not crawler blocking.
- **OWASP OAT / Handbook**: OpenClaw is not a neat OAT category. It is infrastructure/control-plane capability that can support multiple automated threat events.
- **ASVS / NIST**: use these for controls around authentication, session management, secrets, least privilege, logging, and reauthentication.
- **PortSwigger authentication/session sources**: useful for interpreting weak auth/token and exposed management-interface risk.
- **Chromium / Playwright / browser-automation foundations**: helpful background where agents drive browsers or act through browser-like environments.

## Dual-use containment

Moderate dual-use. The source discusses exposure patterns, weak authentication, and possible attack paths. In project use, keep it at the level of risk classification, architecture, and governance. Avoid turning it into an operational checklist for finding or attacking exposed OpenClaw instances.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `bitsight-2026-openclaw-exposed-ai-agent-gateways` |
| Title | *OpenClaw (ex-Moltbot (ex-Clawdbot)): The AI Butler With Its Claws On The Keys To Your Kingdom* |
| Organisation / authors | Bitsight / João Cruz |
| Year | 2026 |
| Category | vendor / threat-research |
| Evidence basis | empirical-exposure measurement / attack-surface analysis / threat-intelligence |
| Operational proximity | observed-exposure |
| Signals / techniques | exposed AI-agent gateway; internet scanning; default gateway port; weak token; integrations; WebSocket API; prompt injection; RCE; credential exposure; rebranding impersonation |
| Threat types | exposed agent control planes; prompt injection; credential/API-key exposure; remote command execution through delegated agent access; supply-chain impersonation; shadow-IT risk |
| Project use | Exposed-agent attack-surface source; pair with HUMAN OpenClaw observed-traffic source |
| Main caution | Exposure does not equal compromise or abuse; vendor scanning methodology and attribution are not independently reproducible from the article |
| Entry file | `bitsight-2026-openclaw-exposed-ai-agent-gateways.md` |
