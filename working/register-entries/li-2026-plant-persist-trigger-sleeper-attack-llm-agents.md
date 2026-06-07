# Li et al. (2026) - Sleeper Attack on Large Language Model Agents

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF `Plant_Persist_Trigger_Sleeper_Attack_on_Large_Lang.pdf`.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, scarce-resource relevance, and dual-use containment.
- **Source handling decision**: keep as a standalone full entry. This is one of the stronger future-agentic-risk sources because it moves beyond single-interaction prompt injection into persistent state poisoning across session context, memory, and reusable skills.

## Bibliographic

- **Citation**: Li, Y., Li, M., Ma, Z., Zhu, F., Liu, D., Wang, W., & Feng, F. (2026). *Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents*. arXiv:2605.28201v1. Posted 27 May 2026.
- **Source URL or path**: uploaded PDF `Plant_Persist_Trigger_Sleeper_Attack_on_Large_Lang.pdf`.
- **Publication status**: arXiv preprint. Treat as not peer-reviewed unless later venue publication is confirmed.
- **Category**: academic / agent-safety / persistent prompt-injection
- **Evidence basis**: benchmark / empirical evaluation / threat-model formalisation / preprint
- **Operational proximity**: measured-but-bounded — evaluates sleeper attacks in a simulated agent/tool environment across multiple models, attack strategies, and state targets. Not observed real-world abuse, but directly relevant to future stateful agent risks.
- **Tags**: Sleeper-Attack, LLM-agents, prompt-injection, indirect-prompt-injection, persistent-state, agent-memory, session-context, reusable-skills, skill-poisoning, memory-poisoning, cross-interaction-attack, latent-instruction-planting, proactive-information-elicitation, persistent-information-corruption, MCP, tool-use, agentic-risk

## What it claims

- Existing agent prompt-injection studies mostly focus on **single-interaction attacks**, where the agent sees malicious external content and acts unsafely in the same user request.
- LLM agents can also be vulnerable to **cross-interaction attacks**, where adversarial content is planted into agent state, remains dormant, and is later triggered by a benign request.
- The paper formalises this as **Sleeper Attack**.
- Sleeper Attack can target three kinds of agent state:
  - session context;
  - memory;
  - reusable skills.
- It defines three attack strategies:
  - Latent Instruction Planting (LIP);
  - Proactive Information Elicitation (PIE);
  - Persistent Information Corruption (PIC).
- The benchmark includes 1,896 instances across six real-world harmful-outcome domains.
- The authors find large gaps between direct single-interaction attacks and delayed sleeper attacks, meaning models that appear safer in direct settings can remain vulnerable once adversarial content persists into state.

## What evidence it provides

This is a **benchmark and threat-model paper**.

It provides:

- a formal definition of Sleeper Attack;
- a distinction between planting stage and trigger stage;
- a taxonomy of attack strategies and agent-state targets;
- a benchmark of 1,896 evaluation instances;
- six harm domains:
  - economic harm;
  - account/system compromise;
  - physical-world harm;
  - personal data leakage;
  - financial data leakage;
  - leakage of other sensitive information;
- evaluation of seven strong open-source and closed-source LLMs;
- controlled comparison between direct single-interaction attacks and sleeper attacks across session, memory, and skill surfaces;
- rule-based attack-success evaluation rather than relying only on closed-source LLM judges.

It does **not** provide:

- observed real-world exploitation;
- production agent telemetry;
- web-bot or scraper evidence;
- anti-bot detection evidence;
- browser/CAPTCHA/proxy evidence;
- legal or compliance analysis;
- proof that deployed commercial agents are affected in exactly the same way.

## Key quantitative details

| Measure | Reported value |
|---|---:|
| Benchmark instances | 1,896 |
| Attack strategies | 3: LIP, PIE, PIC |
| Agent state targets | 3: session, memory, reusable skills |
| Evaluation surfaces | direct, session, memory, skill |
| Evaluated models | 7 |
| LIP direct ASR to strongest state ASR | 11.1% → 39.9% |
| PIE direct ASR to strongest state ASR | 0.6% → 41.6% |
| PIC mean ASR overall | 47.8% |
| Gemini-3-Flash broad vulnerability example | exceeds 50% ASR across LIP, PIE, and PIC in the paper’s summary |
| PIC lower-bound summary | all evaluated agents reach over 27% ASR under PIC |

These figures should be treated as benchmark results under the authors’ simulated framework, not as real-world prevalence.

## Important visual/source evidence

- **Figure 1 / page 2** contrasts direct single-interaction attacks with Sleeper Attack. The important visual point is the two-stage pattern: adversarial content is first planted into state, then later activated by a benign request.
- **Table 1 / page 5** gives benchmark statistics by attack strategy and harm domain, showing how the 1,896 instances are distributed.
- **Table 2 / page 6** reports LIP results across models and surfaces, showing cases where direct attack success is low but session/memory/skill attack success is much higher.
- The problem formulation in **Section 3.1** is useful because it explicitly models state update and later unsafe behaviour as separate interactions.

## Signals or techniques mentioned

- cross-interaction prompt injection;
- external adversarial observations;
- tool-returned data;
- webpages;
- MCP context;
- agent state;
- session context;
- memory;
- reusable skills;
- low-level and high-level skills;
- memory retrieval and update;
- skill retrieval and update;
- latent instruction planting;
- proactive information elicitation;
- persistent information corruption;
- benign trigger query;
- planting query;
- delayed trigger;
- state update;
- rule-based attack success evaluation;
- ordered trace matching;
- argument-value matching;
- simulated tool environment;
- ToolEmu;
- OpenAI Agents SDK.

## Threat types covered

Directly covered:

- persistent prompt injection;
- agent memory poisoning;
- agent skill poisoning;
- external-content attacks on LLM agents;
- delayed unsafe tool/action execution;
- privacy/data leakage through later triggered actions;
- stored information corruption.

Indirect relevance to openbotrisk:

- future stateful agents used for web automation, browser operation, task execution, or account workflows;
- prompt injection in pages, emails, documents, tool outputs, and MCP context;
- attacker-controlled content influencing later agent actions after the original content is no longer visible.

OWASP Automated Threat mapping is indirect:

- **OAT-011 Scraping** — possible where stateful agents are used for information retrieval or web data extraction, but not directly benchmarked as scraping.
- **OAT-019 Account Creation / account workflows** — possible where agents manage accounts or credentials, but not the core focus.
- **OAT-006 Expediting** — broad relevance where agents automate multi-step workflows.
- **OAT-008 Credential Stuffing / ATO context** — indirect through credential/account/system compromise risks, but not credential stuffing evidence.
- **OAT-009 CAPTCHA Defeat** — not directly covered.
- **OAT-005 Scalping / OAT-013 Sniping / OAT-021 Denial of Inventory** — future relevance only if stateful agents automate scarce-resource workflows; not measured here.

## Scarce-resource abuse fields

Not directly applicable.

However, this source is relevant as a **future capability and control-plane risk**. A future booking/ticketing/product-drop agent with memory or reusable skills could be influenced by external content encountered earlier, then mis-handle later scarce-resource tasks. That is an implication, not a measured finding.

## What is strong

- Strong future-agentic-risk source.
- Important because it goes beyond “prompt injection in the current page/email/document” and introduces **persistence across interactions**.
- Directly relevant to long-running agents, memory-enabled agents, skill libraries, MCP-like contexts, and reusable tool guidance.
- Useful companion to OS-HARM:
  - OS-HARM tests computer-use agent safety in GUI environments;
  - Sleeper Attack tests persistent state poisoning across interactions.
- Useful companion to AgentLeak:
  - Sleeper Attack focuses on adversarial state persistence and delayed triggers;
  - AgentLeak focuses on privacy leakage through internal coordination channels.
- Strong for the review’s “future threat surface” section because it shows why agent memory and skills are not just convenience features; they are security boundaries.

## What is weak or limited

- arXiv preprint, not confirmed peer-reviewed.
- Simulated benchmark, not real-world incident evidence.
- Uses generated tasks and simulated tools; ecological validity depends on how well the benchmark approximates deployed agents.
- Model names and capabilities are temporally unstable and may not map to deployed products.
- The attack setup is intentionally adversarial and may overstate ordinary-user risk.
- It does not measure current production mitigations in commercial agent products.
- It does not cover browser fingerprinting, proxies, CAPTCHA, or classic bot-management controls.
- Some details are highly dual-use and should not be reproduced in a public register beyond taxonomy and headline findings.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates stateful agent compromise: malicious external content gets retained in memory/session/skills and later changes agent behaviour during apparently benign tasks.

- **What does it fail to represent?**  
  It does not represent observed abuse in production systems, economic abuse campaigns, or anti-bot evasion. It is a benchmarked threat model.

- **What additional evidence would be needed to go further?**  
  Production incident reports, authorised red-team tests of commercial agents, MCP/security advisories, memory/skill access-control studies, framework-level mitigations, and telemetry from deployed enterprise agents.

## What it cannot show

- It cannot show real-world prevalence.
- It cannot show that a named deployed product is vulnerable in production.
- It cannot show bot-detection performance.
- It cannot show scraping/scalping/credential-stuffing activity.
- It cannot show legal or compliance outcomes.
- It cannot establish that all memory-enabled agents are unsafe.
- It cannot replace OS-HARM, AgentLeak, or OpenClaw sources; it complements them.

## Project impact

Use this as a **core future-agentic-risk entry**.

Best uses:

- add a “persistent state and delayed trigger” subsection;
- show why agent memory, session history, and reusable skills are security-relevant;
- explain that prompt injection can become persistent rather than one-off;
- connect web/email/document/tool content to later agent actions;
- frame agent safety as requiring state hygiene, trust boundaries, memory/skill inspection, provenance, and access controls.

Do not use it as:

- observed abuse evidence;
- proof of production vulnerabilities;
- bot-detection evidence;
- a procedural attack guide;
- evidence of classic web-bot activity.

## Relationship to other register entries

- **OS-HARM**: both are agent-safety benchmarks. OS-HARM is GUI/computer-use safety; Sleeper Attack is persistent state poisoning.
- **AgentLeak**: both address internal agent architecture risks. Sleeper Attack focuses on planted state; AgentLeak focuses on privacy leakage through internal channels.
- **OpenClaw / Bitsight and HUMAN**: OpenClaw gives exposed/observed agent infrastructure; Sleeper Attack provides a benchmarked state-persistence threat model.
- **Bhardwaj et al. LLM scraping**: Bhardwaj shows agent-assisted scraping capability; Sleeper Attack shows how agents may be compromised across interactions.
- **Seiden AI web scrapers**: Seiden is crawler/retrieval measurement; Sleeper Attack is stateful agent safety.
- **Tschacher bot-detection architecture**: Tschacher is passive bot detection; Sleeper Attack is an agent control-plane and state-integrity issue.

## Dual-use containment

High dual-use. The paper defines attack strategies, state targets, and evaluation mechanisms. In project writing, keep the content to taxonomy, benchmark scale, headline results, and defensive implications. Avoid reproducing concrete payloads, trigger instructions, harmful goals, templates, or operational examples.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `li-2026-plant-persist-trigger-sleeper-attack-llm-agents` |
| Title | *Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents* |
| Authors | Yongxiang Li; Moxin Li; Zhixin Ma; Fengbin Zhu; Dongrui Liu; Wenjie Wang; Fuli Feng |
| Year | 2026 |
| Category | academic / agent-safety / persistent prompt-injection |
| Evidence basis | benchmark / empirical evaluation / threat-model formalisation / preprint |
| Operational proximity | measured-but-bounded |
| Signals / techniques | sleeper attack; session context; memory; reusable skills; latent instruction planting; proactive information elicitation; persistent information corruption; delayed trigger |
| Threat types | persistent prompt injection; memory/skill poisoning; delayed unsafe actions; privacy/data leakage; indirect future relevance to web automation and account workflows |
| Scarce-resource abuse | Not directly applicable; future capability/control-plane relevance only |
| Project use | Core future-agentic-risk source for persistent state poisoning and delayed-trigger agent attacks |
| Main caution | Controlled benchmark/preprint; not observed abuse, production vulnerability proof, or classic bot-detection evidence |
| Entry file | `li-2026-plant-persist-trigger-sleeper-attack-llm-agents.md` |
