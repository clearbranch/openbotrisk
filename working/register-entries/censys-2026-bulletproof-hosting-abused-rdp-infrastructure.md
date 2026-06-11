# Censys (2026) - Bulletproof hosting and abused RDP infrastructure

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF `SRC-096-censys-2026-bulletproof-hosting-abused-rdp-infrastructure.pdf`.
- **Source handling decision**: keep as a standalone full entry. It is a useful infrastructure-measurement source for adversarial infrastructure and bulletproof hosting, and it helps balance generic vendor threat reports with internet-scale measurement style evidence.

## Bibliographic

- **Citation**: Censys. (2026). *Hiding in Plain Sight: Tracking Bulletproof Hosting and Abused RDP Infrastructure*. Blog/report capture, 3 February 2026.
- **Source URL or path**: uploaded PDF `SRC-096-censys-2026-bulletproof-hosting-abused-rdp-infrastructure.pdf`.
- **Category**: infrastructure measurement / threat infrastructure
- **Evidence basis**: internet-scale scanning analysis / technical measurement / threat detection
- **Operational proximity**: measured infrastructure — relevant to adversarial infrastructure, but not bot-specific and not proof of intent for any individual host.
- **Tags**: bulletproof-hosting, BPH, RDP, abused-infrastructure, Windows-hostnames, VM-templates, ASNs, VPS, takedown-evasion, ransomware-infrastructure, persistence, hosting-abuse, threat-infrastructure, Censys

## What it claims

- Bulletproof hosting is infrastructure that knowingly or persistently enables malicious activity and evades abuse complaints or takedown requests.
- The defining feature is not a specific service type but repeated tolerance of abuse and infrastructure that persists longer than it should.
- Modern BPH is harder to identify because operators move away from monolithic providers and use reseller ecosystems, short-lived prefixes, and infrastructure churn.
- No single signal proves bulletproof hosting. It must be inferred from long-term behavioural and technical patterns.
- RDP is a useful technical artifact because exposed Windows hosts often leak deployment fingerprints such as hostnames and certificate patterns.
- Reused Windows VM templates and repeated hostnames can expose attacker provisioning lineage across otherwise distributed infrastructure.

## What evidence it provides

This is a technical measurement source. It provides:

- a conceptual distinction between BPH, ordinary VPS providers, residential ISPs, and compromised infrastructure;
- a signal taxonomy for inferring BPH:
  - infrastructure signals;
  - operational behaviour;
  - persistence and evasion;
- discussion of RDP as a durable artifact;
- examples of reused Windows hostnames and VM templates;
- discussion of clustering infrastructure across ASNs, providers, and deployment patterns;
- practical caveats around attribution uncertainty.

It does **not** provide:

- bot-specific abuse data;
- account takeover or CAPTCHA evidence;
- pricing data;
- proof of criminal intent for each host;
- full raw dataset;
- neutral prevalence estimates for all BPH.

## Important visual/source evidence

- Page 1 executive summary: BPH enables long-running malicious activity and can be tracked through internet-scale artifact analysis.
- Page 2: distinguishes what is **not** BPH and explains that intent is hard to observe directly.
- Page 3: table of indicator types: infrastructure, operational behaviour, persistence/evasion.
- Page 4: visual example of reused Windows VM templates at scale.
- Page 4 onward: Windows hostname patterns as a way to reveal broader ransomware or malicious infrastructure.
- Later sections discuss persistence and how malicious behaviour can continue across infrastructure.

## Signals or techniques mentioned

- bulletproof hosting;
- abuse-tolerant hosting;
- RDP exposure;
- Windows hostnames;
- RDP certificates;
- VM template reuse;
- ASN/provider clustering;
- routed prefixes;
- IP churn;
- reseller ecosystems;
- migration between ASNs;
- persistence over months/years;
- ransomware infrastructure;
- sinkhole/honeypot/crawling signals;
- takedown evasion.

## Threat types covered

Directly relevant:

- adversarial infrastructure;
- ransomware and malicious hosting;
- abuse-tolerant infrastructure;
- infrastructure persistence and evasion.

Indirect OAT relevance:

- OAT-011 Scraping, OAT-008 Credential Stuffing, OAT-005 Scalping, OAT-009 CAPTCHA Defeat, and OAT-019 Account Creation may rely on infrastructure layers, but this source does not measure those threats directly.
- Use as infrastructure context, not automated-threat taxonomy evidence.

## What is strong

- Strong source for the infrastructure layer behind “SaaSification” and cost-stack claims.
- Useful because it focuses on observable artifacts rather than only market claims.
- Good balance against vendor pricing pages and broad threat-intel reports.
- Helps explain why attribution is hard: BPH can resemble legitimate VPS, residential ISP abuse, or compromised infrastructure from a scanning perspective.
- Good source for the claim that infrastructure detection is often probabilistic and multi-signal, not binary.

## What is weak or limited

- Censys is a commercial vendor, though the analysis is measurement-oriented.
- The source is not bot-specific.
- It does not provide complete raw data or reproducible pipelines in the PDF.
- Individual infrastructure attribution remains uncertain.
- It does not show costs, marketplaces, or customer demand.
- It should not be over-generalised to all proxy or cloud infrastructure.

## Framing distance

- **What real-world bot/abuse problem does this approximate?**  
  The persistent hosting and remote-access layer that can support cybercrime and automated abuse operations.

- **What does it fail to represent?**  
  It does not show a specific bot campaign or how infrastructure is purchased or used in one named automated-abuse flow.

## Project impact

Use this as a **core infrastructure-measurement entry**.

Best uses:

- add depth to the adversarial-infrastructure section;
- support the idea that infrastructure can be abuse-tolerant, persistent, and measurable;
- connect BPH/RDP artifacts to broader cybercrime infrastructure;
- balance pricing and vendor-intel sources with technical measurement.

Do not use it as:

- bot-abuse prevalence evidence;
- provider recommendation/blacklist;
- proof that a given provider is criminal;
- direct OAT evidence.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `censys-2026-bulletproof-hosting-abused-rdp-infrastructure` |
| Title | *Hiding in Plain Sight: Tracking Bulletproof Hosting and Abused RDP Infrastructure* |
| Organisation | Censys |
| Year | 2026 |
| Category | infrastructure measurement / threat infrastructure |
| Evidence basis | internet-scale scanning analysis / technical measurement |
| Operational proximity | measured infrastructure |
| Signals / techniques | RDP; Windows hostnames; certificates; VM templates; ASNs; prefix churn; BPH inference; persistence |
| Threat types | threat infrastructure; indirect relevance to automated-abuse infrastructure |
| Project use | Infrastructure-measurement balance source for SaaSification/adversarial infrastructure |
| Main caution | Not bot-specific; attribution remains probabilistic |
| Entry file | `censys-2026-bulletproof-hosting-abused-rdp-infrastructure.md` |
