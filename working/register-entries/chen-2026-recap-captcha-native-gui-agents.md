# Chen et al. (2026) - ReCAP: CAPTCHA-capable native GUI agents

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded arXiv PDF `2603.23559v1.pdf`.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.

## Bibliographic

- **Citation**: Chen, Y., Zhai, H., Wang, C., Yang, R., Zhang, L., Wang, G., & Zhang, H. (2026). *CAPTCHA Solving for Native GUI Agents: Automated Reasoning-Action Data Generation and Self-Corrective Training*. arXiv:2603.23559v1. Posted March 2026.
- **Source URL or path**: uploaded PDF `2603.23559v1.pdf`.
- **Publication status**: arXiv preprint. Treat as not peer-reviewed unless later publication is confirmed.
- **Category**: academic
- **Evidence basis**: empirical-measurement / method demonstration / preprint
- **Operational proximity**: measured-but-bounded — demonstrates CAPTCHA-solving capability in trained GUI agents on synthetic and real-world CAPTCHA benchmarks, but does not measure live abuse or operational deployment.
- **Tags**: CAPTCHA, CAPTCHA-defeat, GUI-agents, VLMs, ReCAP, Qwen3-VL, vision-language-models, interactive-CAPTCHA, OCR, slider-CAPTCHA, image-grid, self-correction, chain-of-thought, automation, AI-agents, OAT-009

## What it claims

- General GUI agents have become capable at web, desktop, and mobile interaction, but CAPTCHA solving remains a difficult subtask.
- Modern CAPTCHAs increasingly require visual reasoning, interactive control, spatial localisation, continuous control, and recovery from mistakes, not just static OCR.
- The authors introduce **ReCAP**, a CAPTCHA-capable native GUI agent designed to solve modern interactive CAPTCHA challenges while preserving general GUI-agent performance.
- They build a dynamic CAPTCHA system covering seven representative challenge types:
  - Text;
  - Compact Text;
  - Icon Match;
  - Icon Selection;
  - Paged;
  - Slider;
  - Image Grid.
- They generate large-scale solution trajectories with reasoning traces and self-correction traces from failed attempts.
- ReCAP-32B improves synthetic/dynamic CAPTCHA solving from roughly 30% for baseline GUI agents to about 80%.
- ReCAP models also transfer to a benchmark of 26 real-world CAPTCHA variants, though results are mixed and still far from universal success.

## What evidence it provides

This is a **method demonstration and benchmark paper**.

It provides:

- a dynamic CAPTCHA generation environment;
- a taxonomy of CAPTCHA-solving primitives:
  - OCR;
  - continuous control / dragging;
  - spatial localisation / clicking;
  - visual semantic comprehension;
- a data-generation pipeline for reasoning-action traces;
- a self-correction training pipeline using failed trajectories;
- training details for ReCAP-8B and ReCAP-32B;
- synthetic held-out CAPTCHA benchmark results;
- real-world CAPTCHA benchmark results across 26 variants;
- ablations showing the contribution of reasoning and self-correction data.

## Main quantitative details

### Training data

| Component | Reported value |
|---|---:|
| Solution trajectories | ~150,000 |
| Self-correction trajectories | ~10,000 |
| General GUI grounding/interaction trajectories from Aguvis | ~50,000 |
| Interaction trajectories from AgentNet | ~23,000 |
| Total training scale | ~230,000 samples |
| Base models | Qwen3-VL-8B-Thinking and Qwen3-VL-32B-Thinking |
| Training epochs | 1 |

### Dynamic CAPTCHA benchmark

The paper evaluates models on 1,000 held-out CAPTCHA instances from its dynamic generation system.

| Model / framework | Overall success rate |
|---|---:|
| UI-TARS-1.5-7B | 33.60% |
| Qwen3-VL-Thinking-8B | 28.70% |
| Qwen3-VL-Thinking-32B | 29.70% |
| OpenAI CUA | 31.80% |
| Halligan framework | 25.14% |
| ReCAP-8B | 71.90% |
| ReCAP-32B | 81.00% |

ReCAP-32B performs especially strongly on interaction-heavy synthetic tasks such as Icon Match, Slider, and Image Grid.

### Real-world CAPTCHA benchmark

The paper also evaluates transfer to 26 real-world CAPTCHA variants, including reCAPTCHA v2, hCaptcha, Geetest, Arkose/FunCaptcha, Amazon WAF, Yandex, Tencent, and others.

The results are mixed:

- ReCAP-32B is often best or second-best on interaction-heavy challenges.
- Halligan remains stronger on several text-heavy or pattern-recognition CAPTCHA types.
- Some real-world variants remain very difficult for all methods.
- Transfer is meaningful but not universal.

## Important visual evidence in the PDF

- **Figure 2 on page 3** groups the dynamic CAPTCHA suite into four interaction primitives: OCR, dragging/continuous control, clicking/spatial localisation, and visual semantic comprehension.
- **Figure 3 on page 4** shows two data-generation pipelines:
  - reasoning solution trace generation;
  - self-correction trace generation.
- **Table 1 on page 6** reports the synthetic dynamic CAPTCHA benchmark where ReCAP-32B reaches 81.00% overall success.
- **The real-world benchmark table later in the paper** reports 26 CAPTCHA variants and shows that ReCAP transfers beyond the synthetic generator, but unevenly.

## Signals or techniques mentioned

- CAPTCHA solving;
- GUI agents;
- native vision-language model agents;
- raw screenshot perception;
- low-level GUI actions;
- OCR under noise and text stylisation;
- precise clicking;
- continuous dragging;
- slider challenges;
- image-grid challenges;
- visual semantic comprehension;
- reasoning-action traces;
- chain-of-thought reasoning;
- self-correction traces;
- rejection sampling from failed attempts;
- stochastic rendering;
- dynamic CAPTCHA generation;
- real-world CAPTCHA transfer benchmark;
- Qwen3-VL;
- OpenAI CUA;
- UI-TARS;
- Halligan;
- Oedipus.

## Threat types covered

Directly relevant to:

- OAT-009 CAPTCHA Defeat.

Indirectly relevant to:

- OAT-011 Scraping, when CAPTCHA challenges block automated data collection;
- OAT-008 Credential Stuffing, where CAPTCHA challenges are used as login-abuse friction;
- OAT-019 Account Creation, where CAPTCHA is used during registration;
- OAT-005 Scalping / OAT-013 Sniping / OAT-021 Denial of Inventory, where CAPTCHA protects high-demand transactional flows;
- agentic automation workflows that encounter CAPTCHA gates during general GUI/web use.

## What is strong

- Strong current academic source for CAPTCHA-capable GUI agents.
- Much stronger than vendor tutorials for showing actual model training and benchmarked capability.
- Useful because it connects CAPTCHA solving to general GUI-agent development, not only specialised solver services.
- Good evidence that CAPTCHA is becoming a benchmark problem for native GUI agents.
- Useful for showing the direction of travel: the distinction between “general AI agent” and “specialist CAPTCHA solver” may narrow over time.
- Good source for the simple-to-complex story:
  - static text CAPTCHA;
  - visual-semantic CAPTCHA;
  - interactive CAPTCHA;
  - trained GUI agent with reasoning/action/self-correction.

## What is weak or limited

- Preprint, not confirmed peer-reviewed.
- Much of the training/evaluation relies on the authors’ dynamic CAPTCHA generator, which may not represent production anti-bot systems.
- Reported 80% synthetic success does not mean 80% success against real protected websites.
- Real-world CAPTCHA results are mixed and variant-dependent.
- CAPTCHA solving is evaluated as task success, not as complete anti-bot evasion.
- The paper does not model IP reputation, TLS/HTTP fingerprints, cookie/session reputation, browser integrity, device binding, behavioural telemetry, or account-level risk.
- It does not measure live abuse, actor behaviour, or real-world deployment.
- It does not evaluate defensive countermeasures against such agents.
- Chain-of-thought style training raises reproducibility and disclosure questions; do not reproduce reasoning traces or operational prompts in the public register.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  Automated CAPTCHA completion by increasingly capable GUI agents. It approximates the visual/interactive task-solving layer of CAPTCHA defeat.

- **What does it fail to represent?**  
  It does not represent a full attack pipeline. Real anti-bot systems often combine CAPTCHA with IP reputation, browser fingerprints, token integrity, behavioural scoring, account history, risk scoring, and server-side controls. Passing a CAPTCHA challenge is not the same as bypassing an entire bot-management system.

- **What additional evidence would be needed to go further?**  
  Independent replication; peer review; evaluation against live provider systems under authorised test conditions; comparison with commercial solver services; measurement of latency/cost; and integration with wider browser/proxy/session detection layers.

## What it cannot show

- It cannot show that ReCAP works reliably on real protected production sites.
- It cannot show full bot-detection bypass.
- It cannot show live abuse prevalence.
- It cannot show whether CAPTCHA remains effective as part of layered defence.
- It cannot show commercial solver-market scale.
- It cannot show legal or ethical acceptability.
- It cannot replace vendor telemetry or defensive product evidence.

## Project impact

Use this as the **academic/current-trend anchor for CAPTCHA Defeat by GUI agents**.

Best uses:

- explain why OAT-009 CAPTCHA Defeat is changing as GUI agents improve;
- show that CAPTCHA solving can be trained as a general GUI-agent skill;
- connect AI-agent capability to browser automation and anti-bot challenge systems;
- support a “CAPTCHA is a friction layer, not a complete defence” framing;
- contrast model-based GUI-agent solving with commercial token-solving APIs.

Do not use it as:

- operational bypass evidence;
- proof that CAPTCHA is dead;
- proof of real-world abuse;
- proof of complete anti-bot evasion;
- a source for implementation details or solver instructions.

## Relationship to other register entries

- **OWASP Automated Threat Handbook**: use OAT-009 CAPTCHA Defeat as the threat-category label.
- **Cloudflare Turnstile**: defensive challenge-system source; ReCAP is a solver-capability source.
- **Commercial CAPTCHA-solving API ecosystem entry**: market/capability source for solver services; ReCAP is academic model-based capability.
- **OpenClaw / AI-agent entries**: ReCAP supports the broader point that agents can acquire more interaction capabilities over time.
- **Laperdrix / Berke / Martínez Llamas**: use for fingerprinting/privacy/detection layers beyond CAPTCHA puzzles.
- **NIST / ASVS / PortSwigger**: use for authentication/session controls when CAPTCHA is part of login or registration protection.

## Dual-use containment

High dual-use. The paper describes automated CAPTCHA solving and releases code/model/data. In the register, keep discussion at capability, benchmark, and defensive-framing level. Avoid reproducing prompts, code, solver workflows, or operational instructions for solving CAPTCHA on third-party sites.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `chen-2026-recap-captcha-native-gui-agents` |
| Title | *CAPTCHA Solving for Native GUI Agents: Automated Reasoning-Action Data Generation and Self-Corrective Training* |
| Authors | Yuxi Chen; Haoyu Zhai; Chenkai Wang; Rui Yang; Lingming Zhang; Gang Wang; Huan Zhang |
| Year | 2026 |
| Category | academic |
| Evidence basis | empirical-measurement / method demonstration / preprint |
| Operational proximity | measured-but-bounded |
| Signals / techniques | GUI agents; OCR; dragging; clicking; visual-semantic comprehension; reasoning-action traces; self-correction; dynamic CAPTCHA generation |
| Threat types | OAT-009 CAPTCHA Defeat; indirectly scraping, account creation, credential stuffing, scalping/sniping where CAPTCHA is a friction layer |
| Project use | Academic anchor for CAPTCHA-capable GUI agents and changing CAPTCHA-defeat capability |
| Main caution | Synthetic/dynamic benchmark and preprint; not proof of live anti-bot bypass or real-world abuse |
| Entry file | `chen-2026-recap-captcha-native-gui-agents.md` |
