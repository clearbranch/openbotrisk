# Anderson et al. (2019) - Measuring the Changing Cost of Cybercrime

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF `SRC-097-anderson-2019-measuring-changing-cost-cybercrime.pdf`.
- **Source handling decision**: keep as a standalone full/medium entry. This is the best non-vendor balance source for the cost/economics strand.

## Bibliographic

- **Citation**: Anderson, R., Barton, C., Böhme, R., Clayton, R., Gaňán, C., Grasso, T., Levi, M., Moore, T., & Vasek, M. (2019). *Measuring the Changing Cost of Cybercrime*. WEIS 2019.
- **Source URL or path**: uploaded PDF `SRC-097-anderson-2019-measuring-changing-cost-cybercrime.pdf`.
- **Category**: academic / security economics
- **Evidence basis**: literature synthesis / measurement framework / cost analysis
- **Operational proximity**: framework — not bot-specific and not current telemetry, but highly useful for interpreting cost claims and avoiding vendor-cost overclaiming.
- **Tags**: cybercrime-cost, security-economics, criminal-revenue, direct-loss, indirect-loss, defence-cost, supporting-infrastructure, botnets, pay-per-install, policy, law-enforcement, measurement-bias

## What it claims

- Cybercrime cost should not be treated as a single headline number.
- The authors separate:
  - criminal revenue;
  - direct losses;
  - indirect losses;
  - defence costs;
  - wider social cost.
- Criminal revenue is often much smaller than the total costs imposed on victims and society.
- Supporting infrastructure, such as botnets and pay-per-install services, may generate comparatively small direct criminal revenue but create large indirect and defence costs.
- Vendor and government surveys often have methodological problems or agendas; measurement needs careful decomposition and caveats.
- The authors argue that society often spends too much on some anticipatory defence and too little on catching and prosecuting those who operate or enable criminal infrastructure.

## What evidence it provides

This is a mature academic economics source. It provides:

- a framework for separating cost categories;
- a comparison with the authors’ earlier 2012 cost-of-cybercrime work;
- discussion of changing cybercrime patterns since 2012;
- discussion of cloud migration, mobile, social networks, payment fraud, business email compromise, cryptocurrency crime, ransomware, and botnet infrastructure;
- a policy argument that indirect and defence costs can dominate criminal revenue.

It does **not** provide:

- current 2026 threat telemetry;
- bot-detection evidence;
- SaaS pricing evidence;
- CAPTCHA/proxy/SMS market evidence;
- web-scraping evidence;
- operational details about current adversarial infrastructure.

## Important evidence and figures

- The paper’s framework figure separates cybercrimes, supporting infrastructure, criminal revenue, direct losses, indirect losses, defence costs, and total social cost.
- The authors define direct loss as victim-side loss/damage, indirect loss as wider social/opportunity cost, and defence cost as prevention and mitigation spending.
- They state that total social cost is direct losses plus indirect losses plus defence costs.
- They use a botnet example where roughly $3m criminal revenue from spam-related Viagra promotion imposed costs around a hundred times larger, because spam defence and bandwidth/attention costs are socialised.
- They discuss pay-per-install as supporting infrastructure and note that recruitment may have become easier with vulnerable IoT devices.

## Threat types covered

This paper is not an OWASP OAT source.

Indirect relevance:

- OAT-011 Scraping, OAT-008 Credential Stuffing, OAT-005 Scalping, OAT-009 CAPTCHA Defeat, and OAT-019 Account Creation can all be interpreted through the paper’s cost framework:
  - criminal revenue to the attacker;
  - direct loss to victims/platforms;
  - indirect loss such as trust degradation and false positives;
  - defence costs such as bot management, friction, monitoring, and law enforcement.

## What is strong

- Best source in this batch for balancing vendor-heavy pricing/threat-intel entries.
- Gives a disciplined way to avoid simplistic “cheap tool = huge harm” claims.
- Supports the project’s distinction between:
  - cost to attacker;
  - revenue to criminal;
  - loss to victim;
  - cost to society;
  - cost to defend.
- Good foundation for discussing why takedown/policing of infrastructure can be economically rational even when individual crime revenues look small.

## What is weak or limited

- Published in 2019, so it is not current for AI agents, modern CAPTCHA solving, 2026 proxy markets, or current cloud/SaaS abuse.
- It is broad cybercrime economics, not automated-abuse-specific.
- Some estimates are necessarily approximate and cross-jurisdictional.
- It should be used as a framework and balancing source, not as current market evidence.

## Framing distance

- **What real-world bot/abuse problem does this approximate?**  
  The economics of automated abuse: attackers can rely on supporting infrastructure whose private revenue is smaller than the broad losses and defence costs imposed.

- **What does it fail to represent?**  
  Current 2026 bot infrastructure, AI-agent scraping, modern proxy/CAPTCHA/SMS pricing, and live platform telemetry.

## Project impact

Use this as the **security-economics foundation** for the cost/economics section.

Best uses:

- introduce cost categories before discussing pricing pages;
- clarify that vendor cost figures are not the same as social cost;
- distinguish criminal revenue from victim and defence costs;
- support discussion of infrastructure operators and enforcement.

Do not use it as:

- current price evidence;
- bot-specific telemetry;
- proof of current abuse prevalence.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `anderson-2019-measuring-changing-cost-cybercrime` |
| Title | *Measuring the Changing Cost of Cybercrime* |
| Authors | Ross Anderson et al. |
| Year | 2019 |
| Category | academic / security economics |
| Evidence basis | literature synthesis / measurement framework / cost analysis |
| Operational proximity | framework |
| Signals / techniques | criminal revenue; direct loss; indirect loss; defence cost; supporting infrastructure; botnets; pay-per-install |
| Threat types | broad cybercrime economics; indirect relevance to all automated-abuse categories |
| Project use | Balance source for cost stack and SaaSification claims |
| Main caution | Not current 2026 telemetry and not bot-specific |
| Entry file | `anderson-2019-measuring-changing-cost-cybercrime.md` |
