# El Yagoubi et al. (2026) - AgentLeak: privacy leakage in multi-agent LLM systems

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF `2602.11510v2.pdf`.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, scarce-resource relevance, and dual-use containment.
- **Source handling decision**: keep as a standalone full entry. This is a strong complement to OS-HARM and Sleeper Attack because it focuses on privacy leakage through internal multi-agent channels rather than final outputs alone.

## Bibliographic

- **Citation**: El Yagoubi, F., Badu-Marfo, G., & Al Mallah, R. (2026). *AgentLeak: A Full-Stack Benchmark for Privacy Leakage in Multi-Agent LLM Systems*. arXiv:2602.11510v2. Posted 27 March 2026.
- **Source URL or path**: uploaded PDF `2602.11510v2.pdf`.
- **Publication status**: arXiv preprint. Treat as not peer-reviewed unless later publication is confirmed.
- **Category**: academic / multi-agent privacy benchmark
- **Evidence basis**: benchmark / empirical evaluation / privacy leakage taxonomy / preprint
- **Operational proximity**: measured-but-bounded — evaluates privacy leakage across multi-agent system traces and internal channels, but not production incident telemetry.
- **Tags**: AgentLeak, multi-agent-systems, LLM-agents, privacy-leakage, data-minimization, internal-channels, inter-agent-messages, shared-memory, output-only-audit, agent-privacy, GDPR, HIPAA, Law-25, contextual-integrity, benchmark, governance

## What it claims

- Multi-agent LLM systems create privacy risks that output-only audits cannot measure.
- Sensitive data can leak through:
  - final outputs;
  - inter-agent messages;
  - tool arguments;
  - tool outputs;
  - shared memory;
  - logs;
  - artifacts.
- Inter-agent communication and shared memory are especially important because current frameworks and guardrails often focus on external outputs rather than internal coordination.
- AgentLeak is presented as a full-stack benchmark for privacy leakage across internal and external channels.
- The benchmark spans 1,000 scenarios across healthcare, finance, legal, and corporate domains.
- The paper argues that multi-agent systems can reduce leakage in final outputs while increasing total system exposure once internal channels are counted.
- The key governance point is that **output-only auditing is insufficient** for multi-agent systems.

## What evidence it provides

This is a **benchmark and empirical evaluation source**.

It provides:

- 1,000 privacy scenarios;
- four domains:
  - healthcare;
  - finance;
  - legal;
  - corporate;
- seven leakage channels:
  - C1 final output;
  - C2 inter-agent messages;
  - C3 tool inputs;
  - C4 tool outputs;
  - C5 shared memory;
  - C6 logs/telemetry;
  - C7 artifacts;
- 32 attack classes;
- coordinator-worker topology evaluation;
- a framework-agnostic evaluation harness;
- adapter layer design for LangChain, CrewAI, AutoGPT, MetaGPT, and custom stacks;
- a unified JSONL trace store;
- a three-tier detection pipeline:
  - canary matching;
  - pattern extraction;
  - LLM-as-judge;
- evaluation across five production LLMs:
  - GPT-4o;
  - GPT-4o-mini;
  - Claude 3.5 Sonnet;
  - Mistral Large;
  - Llama 3.3 70B;
- 4,979 validated execution traces.

It does **not** provide:

- observed production breach evidence;
- bot-detection evidence;
- web scraping or anti-bot evidence;
- prompt-injection persistence evidence at the same level as Sleeper Attack;
- legal advice;
- proof that all multi-agent frameworks behave this way under every configuration;
- external validation of all benchmark scenarios.

## Key quantitative details

| Measure | Reported value |
|---|---:|
| Scenarios | 1,000 |
| Domains | 4 |
| Attack classes | 32 |
| Leakage channels | 7 |
| Validated execution traces | 4,979 |
| Models evaluated | 5 |
| Single-agent final-output leakage | 43.2% |
| Multi-agent final-output leakage C1 | 27.2% |
| Total multi-agent exposure across C1/C2/C5 | 68.9% |
| Inter-agent message leakage C2 | 68.8% |
| Shared memory leakage C5 | 46.7% |
| Mean internal channel leakage | 57.8% |
| External output leakage | 27.2% |
| Output-only audits miss | 41.7% of violations, as reported by authors |

These figures should be treated as benchmark results, not as real-world enterprise leakage prevalence.

## Important visual/source evidence

- **Figure 1 / page 5** shows the AgentLeak harness: adapter layer, unified trace store, leakage detection, utility evaluation, and metrics. The figure is useful because it shows the benchmark is framework-agnostic rather than tied to one agent stack.
- The paper’s opening example on **page 1** illustrates the core problem: a final user output can look clean while an internal delegation message carries excessive sensitive data.
- **Table 1 / page 3** summarises the evaluation gap: existing benchmarks and defenses cover output channels but not internal channels.
- **Section III.B / page 3** defines the seven leakage channels and distinguishes internal channels from external ones.
- **Section IV / page 5** describes scenario schema, private vaults, allowed sets, and the data-minimisation framing.

## Signals or techniques mentioned

- multi-agent LLM systems;
- coordinator-worker topology;
- inter-agent messages;
- shared memory;
- tool inputs;
- tool outputs;
- final outputs;
- logs;
- artifacts;
- private vault;
- allowed disclosure set;
- data minimization;
- contextual integrity;
- canary matching;
- pattern extraction;
- LLM-as-judge;
- Presidio;
- PromptGuard;
- LlamaGuard;
- NeMo Guardrails;
- LangChain;
- CrewAI;
- AutoGPT;
- MetaGPT;
- unified trace store;
- JSONL traces;
- channel-specific leakage policy;
- exposure vs leakage distinction;
- internal channel privacy controls.

## Threat types covered

Directly covered:

- privacy leakage in multi-agent systems;
- excessive internal disclosure;
- data minimization failure;
- inter-agent message leakage;
- shared-memory leakage;
- tool/log/artifact leakage.

Indirect relevance to openbotrisk:

- enterprise agent governance;
- internal data exposure from agents that automate workflows;
- account/customer-data handling by agents;
- audit limitations in agentic systems;
- future abuse where agents process sensitive information during web, email, account, or business workflows.

OAT mapping is indirect:

- **OAT-008 Credential Stuffing / ATO context** — indirect where leaked credentials or sensitive data support account abuse, but this is not credential-stuffing evidence.
- **OAT-019 Account Creation / account workflows** — indirect where agents process identity/account data.
- **OAT-020 Account Aggregation** — conceptually relevant where agents aggregate data across systems.
- **OAT-011 Scraping** — not directly covered.
- **OAT-005 Scalping / OAT-013 Sniping / OAT-021 Denial of Inventory** — not directly covered.
- Treat this as privacy/governance evidence, not OAT evidence.

## Scarce-resource abuse fields

Not applicable.

The source is about privacy leakage in multi-agent systems, not scarce inventory or transactional abuse. It may become relevant if future booking/ticketing/scheduling agents pass sensitive data internally, but that is an extrapolation.

## What is strong

- Strong governance and evaluation source for multi-agent systems.
- Clear and useful central point: **final output safety does not imply system privacy**.
- Strong complement to OS-HARM:
  - OS-HARM measures unsafe actions in computer-use agents;
  - AgentLeak measures privacy leakage through internal multi-agent channels.
- Strong complement to Sleeper Attack:
  - Sleeper Attack focuses on adversarial persistence in state;
  - AgentLeak focuses on routine and adversarial leakage through coordination channels.
- Useful for arguing that agent evaluation must include traces, internal communication, memory, logs, and artifacts, not only final answers.
- Practical value for enterprise deployment discussions because it maps leakage channels onto common agent-framework architecture.
- Good support for data-minimization and governance sections.

## What is weak or limited

- arXiv preprint, not confirmed peer-reviewed.
- Benchmark scenarios, not observed enterprise incidents.
- Evaluated framework configurations may not represent all deployments or hardened setups.
- It focuses on coordinator-worker topologies, not all possible multi-agent architectures.
- Leakage detection uses a pipeline that includes LLM-as-judge and automated matching; false positives/negatives remain possible.
- Some regulatory framing is useful but should not be treated as legal advice.
- The claim that internal propagation is leakage depends on a strict data-minimization policy; some systems may define internal trust boundaries differently.
- It is not a bot-abuse or bot-detection source.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates privacy risk in enterprise agent systems where sensitive data is passed between agents, tools, memory, logs, and final outputs during task execution.

- **What does it fail to represent?**  
  It does not show malicious web-bot behaviour, scraper infrastructure, anti-bot evasion, or real incidents. It measures leakage under benchmarked multi-agent workflows.

- **What additional evidence would be needed to go further?**  
  Production agent telemetry, incident reports, enterprise audits, framework-specific privacy controls, independent replication, legal analysis, and studies of hardened multi-agent systems.

## What it cannot show

- It cannot show real-world leakage prevalence.
- It cannot show that all multi-agent systems leak at the reported rates.
- It cannot show bot-detection performance.
- It cannot show scraping, credential stuffing, scalping, or CAPTCHA abuse.
- It cannot establish legal compliance or non-compliance.
- It cannot replace privacy-law sources or security standards.
- It cannot replace OS-HARM or Sleeper Attack; it covers a different failure mode.

## Project impact

Use this as a **core multi-agent privacy/governance entry**.

Best uses:

- add an “internal channels matter” subsection;
- support the claim that output-only audits are insufficient for agents;
- explain seven leakage channels;
- connect agent governance to data minimization and trace-level auditing;
- strengthen the review’s ML/cybersecurity governance section;
- frame future controls around inter-agent message filtering, memory access controls, channel-specific policies, logging controls, and trace audits.

Do not use it as:

- bot evidence;
- observed abuse evidence;
- production incident evidence;
- legal authority;
- proof that all multi-agent frameworks are unsafe;
- evidence about scraper/bot detection.

## Relationship to other register entries

- **OS-HARM**: both are agent-safety benchmarks. OS-HARM is unsafe action in computer-use agents; AgentLeak is privacy leakage in multi-agent systems.
- **Sleeper Attack**: both involve agent state/internal architecture. Sleeper Attack is adversarial delayed trigger; AgentLeak is leakage across internal coordination channels.
- **OpenClaw / Bitsight and HUMAN**: OpenClaw is exposed/observed agent infrastructure; AgentLeak provides benchmarked internal privacy risk.
- **AI/ML cybersecurity governance entry**: AgentLeak gives a concrete benchmark for governance and audit concerns.
- **NIST / ASVS / privacy standards if added**: should be used for formal controls and legal/compliance grounding.
- **Bhardwaj / Seiden AI scraping entries**: separate AI retrieval/scraping lane; AgentLeak is enterprise/multi-agent privacy lane.

## Dual-use containment

Moderate dual-use. The benchmark discusses leakage channels and attack classes. In public project writing, keep focus on privacy controls and audit design. Avoid reproducing detailed adversarial payloads, scenario prompts, or attack recipes.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `el-yagoubi-2026-agentleak-privacy-leakage-multi-agent-llm-systems` |
| Title | *AgentLeak: A Full-Stack Benchmark for Privacy Leakage in Multi-Agent LLM Systems* |
| Authors | Faouzi El Yagoubi; Godwin Badu-Marfo; Ranwa Al Mallah |
| Year | 2026 |
| Category | academic / multi-agent privacy benchmark |
| Evidence basis | benchmark / empirical evaluation / privacy leakage taxonomy / preprint |
| Operational proximity | measured-but-bounded |
| Signals / techniques | inter-agent messages; shared memory; final outputs; tool inputs/outputs; logs; artifacts; private vault; allowed set; canary matching; LLM-as-judge |
| Threat types | multi-agent privacy leakage; internal-channel exposure; data minimization failure; indirect relevance to enterprise agent governance |
| Scarce-resource abuse | Not applicable |
| Project use | Core governance source showing why final-output audits are insufficient for multi-agent systems |
| Main caution | Controlled benchmark/preprint; not real-world prevalence, bot evidence, or legal compliance proof |
| Entry file | `el-yagoubi-2026-agentleak-privacy-leakage-multi-agent-llm-systems.md` |
