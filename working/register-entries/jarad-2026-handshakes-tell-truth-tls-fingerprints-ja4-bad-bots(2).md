# Jarad & Bıçakcı (2026) - When Handshakes Tell the Truth: Detecting Web Bad Bots via TLS Fingerprints

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded arXiv PDF `2602.09606v1(1).pdf`; previous extraction draft `jarad-2026-handshakes-tell-truth-tls-fingerprints-ja4-bad-bots(1).md` reviewed.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.

## Bibliographic

- **Citation**: Jarad, G., & Bıçakcı, K. (2026). *When Handshakes Tell the Truth: Detecting Web Bad Bots via TLS Fingerprints*. arXiv:2602.09606v1. Posted 10 February 2026.
- **Source URL or path**: uploaded PDF `2602.09606v1(1).pdf`; arXiv identifier `2602.09606v1`.
- **Publication status**: arXiv preprint. Treat as not peer-reviewed unless later venue acceptance is confirmed.
- **Date accessed / captured**: uploaded 2026-06-06.
- **Category**: academic
- **Evidence basis**: empirical-measurement / method demonstration / preprint
- **Operational proximity**: measured-but-bounded — evaluates ML classifiers on JA4DB-derived labelled TLS fingerprint records, but labels and features are not equivalent to independently verified production abuse.
- **Tags**: TLS-fingerprinting, JA4, JA4DB, bot-detection, bad-bots, protocol-fingerprinting, TLS-ClientHello, JA3, JA4H, XGBoost, CatBoost, machine-learning, header-spoofing, IP-rotation, full-stack-emulation, Playwright, Puppeteer, Selenium, TLS-spoofing, label-leakage, public-data-limits

## What it claims

- TLS fingerprinting can help distinguish malicious bots from benign/human traffic by using low-level TLS handshake metadata rather than JavaScript, CAPTCHA, or behavioural telemetry.
- JA4 fingerprints capture repeatable TLS ClientHello properties such as protocol, TLS version, SNI presence, cipher count, extension count, ALPN, and hashes of cipher and extension/signature information.
- TLS fingerprints are more resistant to superficial evasion such as User-Agent spoofing and IP rotation because those tactics do not necessarily change the underlying TLS stack.
- Gradient-boosted models can classify bad-bot versus benign traffic using JA4-derived features with very high reported performance.
- CatBoost slightly outperforms XGBoost in the reported experiment.
- JA4 is useful for client-application identification and opportunistic bot mitigation, but it is not a standalone authentication or attribution mechanism.
- The method is weak against full-stack browser automation using real browser network stacks and against specialised tools that deliberately mimic browser TLS handshakes.

## What evidence it provides

The paper evaluates two gradient-boosted classifiers on JA4 fingerprint data from JA4DB.

The dataset is described as a community-maintained repository built from controlled submissions of known clients and passive observation of labelled fingerprints in real traffic.

After cleaning and labelling, the paper reports:

| Dataset component | Reported value |
|---|---:|
| Total records after analysis | 227,404 |
| Bad-bot records | 50,212 |
| Benign records | 148,610 |
| Good-bot records excluded | 32,007 |
| Train/test split | 80/20 |
| Test-set size in confusion matrices | 39,080 |

Labelling rule reported by the paper:

- records with known crawler identifiers such as Googlebot, Bingbot, or LinkedInBot are treated as “good bots” and excluded;
- remaining records are labelled “bad bot” if the `application` field contains the term `bot`;
- otherwise records are labelled benign.

Features extracted include protocol, TLS version, SNI flag, cipher count, extension count, ALPN code, JA4_B cipher-suite hash, JA4_C extension/signature hash, application, OS, device, verified flag, and observation count.

Models:

- XGBoost classifier with 500 boosting trees, max depth 8, learning rate 0.05, subsample 0.8, colsample 0.8, fixed seed, no synthetic oversampling.
- CatBoost classifier with 500 iterations, depth 8, learning rate 0.05, fixed seed, categorical features supplied directly.

Reported model performance:

| Model | TN | FP | FN | TP | Bot precision | Bot recall | Bot F1 | Accuracy | AUC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| XGBoost | 28,699 | 338 | 203 | 9,840 | 0.9668 | 0.9798 | 0.9732 | 0.9862 | 0.998 |
| CatBoost | 28,701 | 336 | 201 | 9,842 | 0.9670 | 0.9800 | 0.9734 | 0.9863 | not separately reported in table; described as similar/slightly better |

The strongest evidence is that JA4DB-derived fingerprint records can be separated into the paper’s labelled categories with high internal test-set performance. The weaker and more important issue is whether those labels and features measure real bad-bot detection rather than dataset metadata separation.

## Important methodological caution

This entry should carry a stronger caution than the previous draft.

The paper’s labelling and feature design create a serious risk of **label leakage / circularity**:

- the paper labels traffic as “bad bot” if the `application` field includes the term `bot`;
- the paper also includes `application` as a model feature;
- other metadata features such as OS, device, verified flag, and observation count may encode dataset curation rather than purely TLS-handshake behaviour.

That means the headline metrics may partly reflect the model learning dataset labels or JA4DB metadata conventions, not learning a generally transferable TLS-based distinction between human users and malicious bots.

The paper’s own threat-model section is useful and honest about boundaries: JA4 has high value against simple non-browser stacks and header/IP spoofing, but low or no value against full-stack browser automation using a real browser network stack, and only medium value against specialised TLS spoofing.

## Signals or techniques mentioned

- TLS fingerprinting;
- TLS ClientHello;
- TLS ServerHello;
- JA4 fingerprints;
- JA4DB;
- JA3;
- JA3S;
- JA4+;
- JA4H_ab;
- protocol;
- TLS version;
- SNI presence;
- cipher-suite list;
- cipher count;
- extension set/order;
- extension count;
- ALPN;
- JA4_B cipher hash;
- JA4_C extension/signature hash;
- HTTP header ordering;
- Accept-Language absence as a possible non-human signal;
- User-Agent / TLS mismatch;
- IP rotation;
- User-Agent spoofing;
- proxy/VPN use;
- full-stack browser automation;
- advanced TLS spoofing;
- XGBoost;
- CatBoost;
- feature importance;
- AUC, precision, recall, F1, confusion matrices.

## Threat types covered

The paper is not organised around OWASP Automated Threat categories.

Directly covered:

- malicious web bot traffic as represented by JA4DB labels;
- automated scripts and scrapers using non-browser TLS stacks;
- header spoofing / User-Agent spoofing;
- IP rotation and proxy-origin changes;
- non-standard TLS libraries and configurations.

Indirect OAT mappings:

- OAT-011 Scraping, when scraper clients use detectable non-browser TLS stacks;
- OAT-008 Credential Stuffing, only if those login attempts use detectable non-browser TLS stacks;
- OAT-019 Account Creation, only if automation uses detectable non-browser TLS stacks;
- OAT-001 Carding / OAT-010 Card Cracking, only if the automation uses detectable non-browser TLS stacks;
- OAT-005 Scalping / OAT-013 Sniping, only if the automation does not use a real browser-like TLS stack.

Weak direct evidence for business-logic abuse, because the paper classifies fingerprints rather than measuring abuse workflows or outcomes.

## What is strong

- Useful source for the protocol-layer detection strand.
- Good explanation of why TLS handshake metadata can add a signal family that is different from cookies, User-Agent strings, JavaScript fingerprints, behavioural biometrics, and web logs.
- Good for explaining why User-Agent spoofing and IP rotation are incomplete evasion tactics if the underlying TLS stack remains inconsistent.
- Good for explicitly showing limits: real-browser automation and deliberate TLS mimicry weaken JA4-only approaches.
- The reported confusion matrices and metrics are concrete and easy to map into the evidence register.
- The threat-model table is useful for a reader-facing explanation of when JA4 helps and when it fails.

## What is weak or limited

- arXiv preprint, not confirmed peer-reviewed.
- High risk of label leakage because `application` appears to be both part of the labelling rule and a model feature.
- Bad-bot labels depend on JA4DB metadata rather than independently verified abuse outcomes.
- The dataset is a fingerprint repository, not a production web-application abuse dataset.
- The paper excludes good bots rather than modelling the full operational task of separating humans, benign crawlers, malicious bots, and ambiguous automation.
- No temporal holdout is reported, so model drift is not tested.
- No adversarial evaluation is performed.
- No tests against Playwright/Puppeteer/Selenium-driven real browsers are performed, even though the paper says this is a key limitation.
- No tests against curl-impersonate, uTLS-style TLS mimicry, anti-detect browsers, residential proxy infrastructure, or cloud browser services are reported.
- No comparison with JavaScript/browser fingerprints, behavioural signals, server-side logs, account outcomes, or vendor bot scores.
- It does not establish that JA4 works against current high-end bot operators.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  Protocol-layer detection of automated clients whose TLS stacks differ from mainstream human-operated browsers. It is most relevant to simple scripts, scraper clients, malware-like clients, unusual libraries, and superficial spoofing where User-Agent or IP changes do not alter the TLS ClientHello.

- **What does it fail to represent?**  
  The hard modern case: browser-native automation and adversaries who align TLS, HTTP headers, browser fingerprint, cookies, session behaviour, and human-like interaction. It also does not represent real business-logic abuse outcomes or production bot-management decisioning.

- **What additional evidence would be needed to go further?**  
  Production traffic with independently verified labels; temporal validation; adversarial tests against Playwright, Puppeteer, Selenium, anti-detect browsers, curl-impersonate/uTLS, cloud browsers, and residential proxies; evaluation across specific abuse workflows; and ablation tests that remove `application` and other metadata features to test how much signal comes from JA4 itself.

## What it cannot show

- It cannot show that JA4 alone is sufficient for bot detection.
- It cannot show robust detection against real-browser automation.
- It cannot show robust detection against advanced TLS spoofing.
- It cannot show that the high AUC transfers to production bot-management systems.
- It cannot show detection of specific abuse types such as credential stuffing, carding, scalping, account creation, ticket bots, appointment-slot abuse, or ATO.
- It cannot establish prevalence or business impact.
- It cannot rule out dataset leakage or label artefacts.
- It cannot replace in-the-wild anti-bot evaluation or production telemetry.

## Project impact

Use this as a **promising-but-bounded protocol-signal source**.

Best uses:

- add TLS/JA4 to the detection-signal taxonomy;
- explain why IP and User-Agent are not enough;
- explain why lower-layer coherence matters;
- provide a concrete example of ML over protocol fingerprints;
- show that protocol fingerprints help mainly when clients use non-browser stacks;
- explain why browser-native automation changes the problem.

Do not use it as:

- proof that JA4 solves bad-bot detection;
- proof that TLS fingerprints detect Playwright/Puppeteer/Selenium automation;
- proof of real-world abuse prevalence;
- strong evidence for any specific OAT category;
- validated vendor-grade detection performance.

## Relationship to other register entries

- Pair with **MDN HTTP/User-Agent/cookies** for foundations.
- Pair with **Laperdrix / Berke browser fingerprinting** for browser/device fingerprinting.
- Pair with **Cloudflare Detection IDs** for coherence checks such as claimed browser versus low-level request characteristics.
- Pair with **ScrapingBee / bypass-guide entries** for the attacker-side recognition that multiple layers must align.
- Pair with **Martínez Llamas et al.** for detection/privacy trade-offs and taxonomy.
- Pair with **FP-Inconsistent / evasive bot traffic** if added, because that is closer to purchased/operational evasive traffic than this JA4DB classification paper.

## Dual-use containment

This source is moderate dual-use. It describes signal families and limitations, including where JA4 fails. In project use, keep it at the level of defensive signal taxonomy and methodological limits. Avoid turning the limitations into a checklist for bypassing TLS fingerprint detection.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `jarad-2026-handshakes-tell-truth-tls-fingerprints-ja4-bad-bots` |
| Title | *When Handshakes Tell the Truth: Detecting Web Bad Bots via TLS Fingerprints* |
| Authors | Ghalia Jarad; Kemal Bıçakcı |
| Year | 2026 |
| Category | academic |
| Evidence basis | empirical-measurement / method demonstration / preprint |
| Operational proximity | measured-but-bounded |
| Signals / techniques | TLS ClientHello; JA4; JA4DB; cipher count; extension count; ALPN; SNI; JA4_B; JA4_C; User-Agent/TLS mismatch; XGBoost; CatBoost |
| Threat types | generic bad bots; indirectly OAT-011 and other OATs only when abuse uses non-browser TLS stacks |
| Project use | Protocol-layer detection source; useful for explaining where TLS fingerprints help and where browser-native automation defeats them |
| Main caution | High headline metrics are weakened by possible label leakage and JA4DB metadata dependence; not production abuse or adversarial-evasion evidence |
| Entry file | `jarad-2026-handshakes-tell-truth-tls-fingerprints-ja4-bad-bots.md` |
