# Kolhar & Sridevi (2025/2026) - AI/ML for cybersecurity and cyber-risk management

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF chapters:
  - `Secure-and-Ethically-Aligned-AI-Solutions-for-Cybersecurity-and-Threat-Detection.pdf`
  - `Future-Trends-and-Innovation-in-Machine-Intelligence-for-Cyber-Risk-Management.pdf`
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.
- **Source handling decision**: combine as one low-priority AI/ML cybersecurity background entry. Use *Secure and Ethically Aligned AI Solutions* as the main source; treat *Future Trends and Innovation in Machine Intelligence for Cyber Risk Management* as a supporting overlapping chapter.

## Bibliographic

### Main source

- **Citation**: Kolhar, A., & Sridevi. (2026). *Secure and Ethically Aligned AI Solutions for Cybersecurity and Threat Detection*. Chapter 11. IGI Global Scientific Publishing. DOI: `10.4018/979-8-3373-6038-6.ch011`.
- **Source URL or path**: uploaded PDF `Secure-and-Ethically-Aligned-AI-Solutions-for-Cybersecurity-and-Threat-Detection.pdf`.

### Supporting related source

- **Citation**: Kolhar, A., & Sridevi. (2025). *Future Trends and Innovation in Machine Intelligence for Cyber Risk Management*. Chapter 18. IGI Global. DOI: `10.4018/979-8-3693-7540-2.ch018`.
- **Source URL or path**: uploaded PDF `Future-Trends-and-Innovation-in-Machine-Intelligence-for-Cyber-Risk-Management.pdf`.

## Category and treatment

- **Category**: book chapter / AI-cybersecurity background
- **Evidence basis**: review / conceptual framework / governance overview
- **Operational proximity**: low — useful for explaining ML/AI detection concepts, SOC workflow, and governance concerns, but not specific to bot abuse and not empirical evidence.
- **Tags**: AI-cybersecurity, machine-learning, threat-detection, anomaly-detection, UEBA, SOC, supervised-learning, unsupervised-learning, deep-learning, malware-analysis, phishing-detection, XAI, adversarial-ML, data-poisoning, evasion, fairness, transparency, accountability, human-in-the-loop, GDPR, AI-Act, PETs, cyber-risk-management

## What the sources claim

- AI and ML are increasingly important in cybersecurity because they can analyse large volumes of logs, network traffic, endpoint activity, user behaviour, and threat-intelligence data.
- Supervised learning is useful for known threat detection, but depends on labelled data and struggles with novel threats outside its training distribution.
- Unsupervised learning can identify anomalies and possible zero-day or insider-threat activity, but may generate false positives.
- User and Entity Behaviour Analytics can build behavioural baselines for users, hosts, and applications, then flag deviations such as unusual access times, locations, or file access patterns.
- Deep learning can support malware analysis through CNNs over binary-as-image representations and RNN/LSTM models over sequences of API/system calls.
- AI-enabled cybersecurity needs governance: fairness, transparency, explainability, robustness, accountability, human oversight, privacy protection, and regulatory alignment.
- AI in cybersecurity is dual-use: defenders use ML for detection and response, while attackers can use AI to craft phishing, find vulnerabilities, automate evasion, or scale attacks.
- The future-trends chapter frames AI/ML as part of cyber-risk management through predictive analytics, automated incident response, adaptive mitigation, AI-driven threat intelligence, and AI-powered deception.

## What evidence it provides

This is a **secondary conceptual/review source**, not an empirical bot-detection or threat-measurement paper.

It provides:

- a useful high-level taxonomy of ML roles in cybersecurity:
  - supervised learning for known threats;
  - unsupervised learning for anomalies;
  - UEBA for user/entity behaviour;
  - feature engineering using cloud telemetry, endpoint data, API calls, and network logs;
  - CNNs for static malware analysis;
  - RNN/LSTM for behavioural malware analysis;
  - NLP for phishing and social engineering;
- a SOC workflow example:
  - unsupervised alert generation;
  - analyst triage and UEBA context;
  - supervised ML enrichment;
  - human decision and response;
  - feedback loop for retraining;
- ethical/governance concepts:
  - fairness and bias mitigation;
  - transparency and explainability;
  - robustness and reliability;
  - accountability and human oversight;
  - PETs such as homomorphic encryption and differential privacy;
  - GDPR and EU AI Act framing;
- future trends:
  - AI-driven threat intelligence;
  - AI-assisted deception/honeypots;
  - adaptive threat mitigation;
  - predictive analytics;
  - long-term security strategy and workforce challenges.

It does **not** provide:

- original experiments;
- production telemetry;
- a bot-detection dataset;
- performance benchmarks for web-bot detection;
- direct evidence of scraper, credential-stuffing, proxy, CAPTCHA, or AI-agent abuse;
- rigorous legal analysis comparable to a law/regulation source;
- authoritative control requirements comparable to NIST/ASVS.

## Important visual/source evidence

- In *Secure and Ethically Aligned AI Solutions*, **Figure 1 on page 6** shows a simplified ML-enhanced SOC workflow: alert from unsupervised model, analyst triage/UEBA context, IOC enrichment, supervised scan, human decision, incident response, and feedback-loop retraining.
- The same chapter’s ML section distinguishes supervised learning, unsupervised anomaly detection, UEBA, and feature engineering from cloud telemetry, endpoint data, API calls, and network logs.
- Later sections cover privacy-enhancing technologies and governance/regulatory framing, including GDPR, the EU AI Act, human oversight, and explainability.
- The *Future Trends* chapter is useful mostly for reinforcing the same broad points: AI/ML supports anomaly detection, pattern recognition, behavioural analysis, predictive analytics, adaptive mitigation, and automated incident response.

## Signals or techniques mentioned

- supervised learning;
- unsupervised learning;
- anomaly detection;
- pattern recognition;
- behavioural analysis;
- UEBA;
- feature engineering;
- cloud telemetry;
- endpoint process lineage;
- API calls;
- network logs;
- packet size/frequency;
- malware binary-to-image conversion;
- CNNs;
- RNNs;
- LSTMs;
- API/system call sequences;
- NLP for phishing;
- threat intelligence;
- SIEM feedback loops;
- human-in-the-loop review;
- adversarial training;
- evasion attacks;
- data poisoning;
- model robustness;
- XAI;
- homomorphic encryption;
- differential privacy;
- GDPR;
- EU AI Act;
- continuous compliance;
- bias monitoring.

## Threat types covered

Directly discussed at high level:

- malware;
- phishing;
- network intrusion;
- insider threats;
- zero-day detection;
- account/credential misuse signals through UEBA;
- AI-driven cyber threats;
- adversarial attacks against AI systems.

Indirect relevance to openbotrisk:

- bot detection as a form of anomaly/behavioural detection;
- credential stuffing and account abuse where UEBA/risk scoring is used;
- scraper/API abuse where traffic or API behaviour deviates from baselines;
- AI-agent risk where human oversight, governance, explainability, and logging are needed.

OAT mapping is weak but possible:

- **OAT-008 Credential Stuffing** — indirect, via account and behavioural anomaly detection.
- **OAT-011 Scraping** — indirect, via traffic/API anomaly detection.
- **OAT-019 Account Creation** — indirect, via behavioural/risk detection.
- **OAT-016 Skewing** — indirect, if behavioural anomaly models detect synthetic activity.
- **OAT-015 Denial of Service** — indirect, via traffic anomaly detection.

## What is strong

- Useful for adding the **ML/cybersecurity detection angle** to the review.
- Gives a clear, readable way to explain supervised vs unsupervised vs UEBA detection.
- Useful for a section that says bot detection belongs within a broader family of ML-based cybersecurity detection.
- Useful for explaining why ML detection is not a magic black box: feature quality, false positives, human triage, feedback loops, explainability, and governance matter.
- The SOC workflow example is useful for reader comprehension.
- Good support for an ML review subsection on:
  - signals;
  - models;
  - analyst workflow;
  - feedback loops;
  - governance.

## What is weak or limited

- Broad and generic.
- Secondary book chapters, not primary empirical papers.
- Some claims are sweeping and should not be made load-bearing without stronger sources.
- Not specific to web bots, scraper detection, CAPTCHA, proxies, TLS fingerprints, browser fingerprints, or AI agents.
- Does not provide reproducible methods or benchmark datasets.
- Governance/legal discussion is useful background but should be secondary to stronger sources such as Martínez Llamas et al., NIST, OWASP, GDPR/AI Act primary/regulator guidance.
- The two chapters overlap substantially, so they should not both be separate register rows unless the review becomes specifically about AI cybersecurity.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  The ML-based detection layer around cyber threats: models that detect anomalies, risky behaviour, malware, phishing, and suspicious user/entity activity.

- **What does it fail to represent?**  
  It does not represent web-bot detection specifically. It does not measure bot traffic, attacker adaptation, CAPTCHA defeat, proxy use, browser automation, or anti-bot platform performance.

- **What additional evidence would be needed to go further?**  
  Academic bot-detection papers; vendor telemetry; protocol/browser-fingerprinting sources; behavioural-biometrics studies; adversarial ML papers for bot detection; SOC case studies; and stronger governance/privacy sources.

## What it cannot show

- It cannot show that ML detects web bots effectively.
- It cannot show bot prevalence.
- It cannot show detection precision/recall in production.
- It cannot show current attacker capability.
- It cannot show whether AI-based detection is legally compliant.
- It cannot replace the Martínez Llamas bot-detection/privacy review.
- It cannot replace empirical JA4/browser-fingerprint/proxy/CAPTCHA papers.

## Project impact

Use this as a **low-priority but useful ML/cybersecurity background entry**.

Best uses:

- add a short review section on ML in cybersecurity;
- explain supervised learning, unsupervised anomaly detection, UEBA, and human-in-the-loop SOC workflow;
- connect bot detection to broader cyber detection patterns;
- add governance language around explainability, bias, model robustness, and oversight;
- support the point that ML needs good features and feedback loops, not just a model.

Do not use it as:

- web-bot-specific evidence;
- observed abuse evidence;
- primary legal/governance evidence;
- detection-performance evidence;
- a main source for bot detection methods.

## Relationship to other register entries

- **Martínez Llamas et al. 2025 bot-detection/privacy review** remains the stronger bot-specific ML/detection/governance source.
- **Jarad & Bıçakcı JA4/TLS** is stronger for a specific ML/protocol-fingerprint detection method.
- **Laperdrix / Berke** are stronger for browser-fingerprinting foundations.
- **Cloudflare/HUMAN/DataDome** sources are stronger for operational bot-management framing.
- **NIST / ASVS / OWASP** are stronger for control requirements.
- **API Security Testing entry** connects ML detection to API abuse, scraping, credential stuffing, and business logic.

## Suggested addition to the literature/review narrative

A useful section would be:

> **Machine learning in cyber detection**  
> Bot detection is one branch of a broader ML-cybersecurity problem. Supervised models help when known labels exist; unsupervised models and UEBA help identify deviations from normal behaviour; and SOC workflows still need human triage, feedback loops, and governance. The useful question is not “can ML detect bots?” but “what signals are available, what labels are trustworthy, how does the model fail, and how are decisions reviewed?”

This would strengthen the review by situating bot detection inside normal cyber-detection practice, while avoiding overclaiming.

## Dual-use containment

Low dual-use. The chapters are conceptual and defensive. The main risk is overclaiming and generic padding. Use them to improve explanatory structure, not as hard evidence.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `kolhar-sridevi-2025-2026-ai-ml-cybersecurity-governance-background` |
| Title | *AI/ML for cybersecurity and cyber-risk management* |
| Authors | Amrutha Kolhar; Sridevi |
| Year | 2025–2026 |
| Category | book chapter / AI-cybersecurity background |
| Evidence basis | review / conceptual framework / governance overview |
| Operational proximity | low |
| Signals / techniques | supervised learning; unsupervised anomaly detection; UEBA; feature engineering; CNNs; RNN/LSTM; NLP phishing; XAI; adversarial robustness; human-in-the-loop; GDPR; AI Act |
| Threat types | general malware, phishing, intrusion, insider threat; indirect relevance to bot/account/API abuse detection |
| Project use | Background source for ML-in-cybersecurity section and governance/oversight framing |
| Main caution | Broad secondary source; not web-bot-specific, observed-abuse, or detection-performance evidence |
| Entry file | `kolhar-sridevi-2025-2026-ai-ml-cybersecurity-governance-background.md` |
