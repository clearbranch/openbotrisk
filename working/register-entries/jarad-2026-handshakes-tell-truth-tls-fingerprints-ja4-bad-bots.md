# When Handshakes Tell the Truth: Detecting Web Bad Bots via TLS Fingerprints — Jarad & Bıçakcı 2026

## Bibliographic

- **Citation**: Jarad, G., & Bıçakcı, K. (2026). When Handshakes Tell the Truth: Detecting Web Bad Bots via TLS Fingerprints. arXiv:2602.09606v1.
- **Source URL or path**: 2602.09606v1.pdf
- **Date accessed**: 2026-06-01
- **Category**: academic / threat-surface
- **Tags**: TLS-fingerprinting, JA4, JA4DB, bot-detection, bad-bots, protocol-fingerprinting, XGBoost, CatBoost, TLS-ClientHello, machine-learning, header-spoofing, full-stack-emulation, public-data-limits

## What it claims

- TLS fingerprinting can help distinguish malicious bots from benign/human traffic by using low-level handshake metadata rather than JavaScript or behavioural telemetry.
- JA4 fingerprints capture TLS ClientHello properties such as protocol, TLS version, SNI, cipher count, extension count, ALPN, and hashes of cipher/extension information.
- TLS fingerprints are more resistant to superficial evasion such as IP rotation or User-Agent spoofing because those tactics do not necessarily change the underlying TLS stack.
- Gradient-boosted models can classify bad-bot versus benign traffic using JA4-derived features with very high reported performance.
- CatBoost slightly outperforms XGBoost in the reported experiment.
- JA4 is useful for client-application identification and opportunistic bot mitigation, but it is not a standalone authentication or attribution mechanism.
- The approach is weak against full-stack browser automation that uses a real browser network stack, and against specialised tools that spoof browser-like TLS handshakes.

## What evidence it provides

The paper evaluates two gradient-boosted classifiers on JA4 fingerprint data from JA4DB.

The dataset is described as a community-maintained JA4 fingerprint repository built from:
- controlled/lab submissions of known clients
- passive observation of labelled fingerprints in real traffic

After cleaning and labelling, the paper reports:
- 227,404 records total
- 50,212 bad-bot records
- 148,610 benign records
- 32,007 good-bot records excluded from model training

Labelling rules:
- traffic with known crawler identifiers such as Googlebot, Bingbot, or LinkedInBot is treated as “good bot” and excluded
- remaining entries are labelled “bad bot” if the application field includes the term “bot”
- otherwise records are labelled benign

Features are extracted from JA4 strings and metadata, including:
- protocol
- TLS version
- SNI flag
- cipher count
- extension count
- ALPN code
- JA4_B cipher-suite hash
- JA4_C extension/signature hash
- application
- OS
- device
- verified flag
- observation count

Models:
- XGBoost with 500 trees, max depth 8, learning rate 0.05, subsample 0.8, colsample 0.8
- CatBoost with 500 iterations, depth 8, learning rate 0.05
- 80/20 train/test split
- no synthetic oversampling

Reported XGBoost results:
- true negatives: 28,699
- true positives: 9,840
- false positives: 338
- false negatives: 203
- bot precision: 0.9668
- bot recall: 0.9798
- bot F1: 0.9732
- accuracy: 0.9862
- AUC: 0.998

Reported CatBoost results:
- true negatives: 28,701
- true positives: 9,842
- false positives: 336
- false negatives: 201
- bot precision: 0.9670
- bot recall: 0.9800
- bot F1: 0.9734
- accuracy: 0.9863

The strongest technical evidence is that JA4-derived features can separate labelled client categories in this dataset. The weaker part is whether the labels and dataset composition represent real production “bad bot” detection against adaptive adversaries.

## Signals or techniques mentioned

- TLS fingerprinting
- TLS ClientHello
- JA4 fingerprints
- JA4DB
- JA4_a
- JA4_b
- JA4_c
- JA3
- JA3S
- JA4+
- JA4H_ab
- cipher-suite list
- cipher count
- extension count
- extension ordering
- ALPN
- TLS version
- SNI presence
- HTTP header ordering
- Accept-Language absence
- User-Agent / TLS mismatch
- protocol-level fingerprinting
- XGBoost
- CatBoost
- gradient-boosted trees
- confusion matrix
- precision
- recall
- F1
- ROC / AUC
- feature importance
- IP rotation
- User-Agent spoofing
- full-stack browser automation
- specialised TLS spoofing

## Threat types covered

The paper is not organised around OWASP Automated Threat categories.

Directly covered:
- malicious web bot traffic as represented in JA4DB labels
- automated scripts and scrapers using non-browser TLS stacks
- header spoofing / User-Agent spoofing
- IP rotation and proxy-based origin changes
- non-standard TLS libraries and configurations

Relevant project/OAT mappings:
- scraping and automated access where bots use non-browser HTTP/TLS stacks
- credential stuffing, account creation, carding, scalping, and ATO only insofar as those attacks use detectable non-browser TLS stacks
- weak direct evidence for business-logic abuse because the paper classifies fingerprints rather than modelling specific abuse workflows

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates protocol-level bot detection where automated clients use TLS stacks that differ from real browsers. It is useful for the project because it adds a signal family not covered by mouse biometrics, web logs, or JavaScript fingerprinting: passive TLS handshake metadata.

- **What does it fail to represent?**  
  The labelling is a major limitation. Labelling “bad bot” based on whether an application field includes “bot” risks circularity or dataset artefacts. The dataset is a JA4 fingerprint repository, not a full production bot-management dataset with observed abuse outcomes. It does not show detection against adaptive adversaries who know JA4 is being used. It explicitly says full-stack browser automation with real Chrome, Playwright, Puppeteer, or Selenium can share the same TLS stack as legitimate users, making JA4 weak or ineffective in those cases. It also recognises specialised TLS spoofing as a limitation. It does not evaluate abuse flows, JavaScript behaviour, accounts, proxies, browser fingerprints, or commercial anti-bot stacks.

- **What additional evidence would be needed to go further?**  
  Production web traffic with independently verified bot/human labels; adversarial tests using Playwright/Puppeteer/Selenium real browsers; tests with curl-impersonate, uTLS, anti-detect browsers, cloud browsers, mobile proxies, and residential proxies; evaluation across specific abuse flows; temporal validation to test model drift; comparison with server logs, JS fingerprints, and behavioural signals; analysis of whether top features are robust or simply encode dataset labelling conventions.

## What it cannot show

- It cannot show that JA4 alone is sufficient for bot detection.
- It cannot show robust detection against full-stack browser automation.
- It cannot show robust detection against advanced TLS fingerprint spoofing.
- It cannot show that high AUC transfers to production bot-management systems.
- It cannot show detection of specific abuse types such as credential stuffing, carding, scalping, fake account creation, or ATO.
- It cannot establish prevalence or business impact.
- It cannot rule out dataset leakage or labelling artefacts, given the dependence on JA4DB metadata and application labels.
- It cannot replace FP-Inconsistent-style evidence based on purchased evasive traffic and live anti-bot services.

## Project impact

- Useful source for a protocol-layer / TLS-fingerprinting section.
- Adds a distinct signal family to the project taxonomy:
  - web logs
  - behavioural biometrics
  - JavaScript/browser fingerprints
  - TLS/protocol fingerprints
  - anti-bot service outcomes
- Good source for explaining where TLS fingerprints help: cheap passive signal, resistant to User-Agent spoofing and IP rotation, useful for identifying non-browser stacks.
- Also good for explaining where TLS fingerprints fail: real-browser automation and deliberate TLS mimicry.
- Should be cited cautiously. The headline metrics are impressive, but the evidence is not as strong as it looks unless the labelling and train/test separation are independently validated.
- Best used as a “promising but bounded protocol signal” source, not as a claim that JA4 solves modern bot detection.
