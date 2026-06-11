# Fingerprinting the Fingerprinters: Learning to Detect Browser Fingerprinting Behaviors — Iqbal et al. 2021

## Bibliographic

- **Citation**: Iqbal, U., Englehardt, S., & Shafiq, Z. (2021). Fingerprinting the Fingerprinters: Learning to Detect Browser Fingerprinting Behaviors. *2021 IEEE Symposium on Security and Privacy (SP)*, 1143–1161. https://doi.org/10.1109/SP40001.2021.00017
- **Source URL or path**: SRC-016-iqbal-2021-fingerprinting-the-fingerprinters-fp-inspector.pdf
- **Date accessed**: 2026-05-31
- **Category**: academic / foundations
- **Tags**: browser-fingerprinting, FP-Inspector, JavaScript, static-analysis, dynamic-analysis, OpenWPM, tracking, anti-fraud, bot-detection, APIs, countermeasures, web-measurement, privacy, public-data-limits

## What it claims

- Browser fingerprinting is an opaque, stateless tracking technique that can be used for both anti-fraud/bot-detection and cross-site tracking.
- Existing fingerprinting countermeasures face a trade-off: broad API restriction can break websites, while blocklists and hand-coded heuristics miss evolving or first-party fingerprinting scripts.
- FP-Inspector can detect browser fingerprinting scripts using a machine-learning approach that combines static JavaScript analysis and dynamic execution traces.
- Static analysis helps identify dormant fingerprinting code that may not execute during a crawl.
- Dynamic analysis helps identify obfuscated or minified fingerprinting code that static analysis may miss.
- FP-Inspector detects more fingerprinting scripts than prior manually designed heuristics.
- Targeted countermeasures based on detecting fingerprinting scripts can reduce website breakage compared with blanket API restriction.
- Browser fingerprinting was found on a substantial share of popular websites in the authors’ top-100K crawl.
- Fingerprinting scripts are served by both anti-ad-fraud vendors and potential cross-site trackers.
- Fingerprinting scripts use a wider set of JavaScript APIs than earlier heuristics captured, including APIs not previously well documented as fingerprinting vectors.

## What evidence it provides

The paper proposes FP-Inspector, a machine-learning system for detecting browser fingerprinting scripts.

FP-Inspector has two main components:
- a detection component that extracts syntactic and semantic features from JavaScript
- a mitigation component that applies restrictions or blocking policies to detected fingerprinting scripts

The detection method combines:
- **Static analysis**: JavaScript source files are unpacked, represented as Abstract Syntax Trees, and converted into parent-child syntactic features.
- **Dynamic analysis**: JavaScript execution traces are collected using an extended OpenWPM browser instrumentation setup, recording API accesses, method/property names, arguments, return values, and stack traces.

The system trains separate decision-tree classifiers for static and dynamic representations and combines their results. A script is treated as fingerprinting if either model detects it.

The training/evaluation crawl includes 17,629 websites and 153,354 distinct executing scripts. Ground truth is initially derived from modified heuristics based on prior work, then iteratively improved by manually reviewing disagreements between classifier output and heuristic labels.

Reported classification performance:
- Static model: 99.8% accuracy, 85.5% recall, 92.7% precision
- Dynamic model: 99.9% accuracy, 96.7% recall, 99.1% precision
- Combined model: 99.9% accuracy, 93.8% recall, 93.1% precision
- Combined FP-Inspector detects 26% more scripts than the heuristic baseline

The paper evaluates countermeasure breakage using a browser extension implementing:
- blanket API restriction
- targeted API restriction
- request blocking
- hybrid request blocking/API restriction

Reported breakage on a challenging set of websites:
- blanket API restriction: 68.03% total breakage
- targeted API restriction: 30.32% total breakage
- request blocking: 50.00% total breakage
- hybrid: 46.72% total breakage

The paper then uses FP-Inspector to measure fingerprinting on Alexa top-100K websites. It reports:
- fingerprinting on 30.60% of top-1K sites
- 24.45% of top 1K–10K sites
- 10.18% of top-100K sites overall
- 2,349 domains serving fingerprinting scripts on the top-100K sites

The paper also reports that fingerprinting is especially common on news sites and that major detected vendors include anti-ad-fraud and tracking-related domains.

## Signals or techniques mentioned

- Browser fingerprinting
- Stateless tracking
- JavaScript API access
- HTTP headers
- Canvas fingerprinting
- Canvas font fingerprinting
- WebRTC
- AudioContext / Audio API
- WebGL
- performance.now
- navigator.platform
- navigator.userAgent
- navigator and screen APIs
- Plugin and MimeType objects
- fonts
- extensions
- Battery Status API
- mobile sensors
- DOM interaction APIs
- OpenWPM browser instrumentation
- script execution traces
- JavaScript source files
- inline scripts
- external scripts
- eval / Function unpacking
- Abstract Syntax Trees
- parent-child AST feature pairs
- static code analysis
- dynamic analysis
- information gain feature selection
- decision-tree classifiers
- request blocking
- blanket API restriction
- targeted API restriction
- hybrid mitigation
- website breakage analysis
- Alexa top-100K crawl

## Threat types covered

The paper is not primarily a bot-detection paper. It is a browser-fingerprinting detection and privacy measurement paper.

Directly covered:
- browser fingerprinting for stateless tracking
- browser fingerprinting for anti-fraud and bot detection
- JavaScript-based fingerprinting script detection
- anti-fingerprinting countermeasures and their website-breakage trade-offs

Relevant project/OAT mappings:
- cross-cutting infrastructure relevant to many automated threats
- relevant to bot detection because browser fingerprinting is one of the main signal families used to distinguish automated browsers from real users
- relevant to anti-fraud/impression-fraud territory because some detected vendors are anti-ad-fraud services
- indirect relevance to scraping, credential stuffing, scalping, carding, and account creation where fingerprinting is used as a control or evasion target

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates the detection and mitigation of fingerprinting scripts used by websites and third parties. For Open Bot Risk, its value is foundational: it explains what browser fingerprinting is, why it matters, which APIs are involved, and why detection/mitigation creates a trade-off between privacy, security, and site breakage.

- **What does it fail to represent?**  
  It does not evaluate bot traffic, bot operators, browser automation tools, commercial anti-bot effectiveness, or evasion by bots. It detects fingerprinting scripts, not automated users. It does not test Playwright, Puppeteer, Selenium, anti-detect browsers, residential proxies, cloud browsers, or AI browser agents. It does not measure whether fingerprinting improves bot detection accuracy or which fingerprinting attributes are most effective against bots. The crawl is from 2019-era Alexa rankings and may not represent current web deployment patterns without replication.

- **What additional evidence would be needed to go further?**  
  Current crawl replication; linkage to bot-detection outcomes; evaluation of fingerprinting signals against real or purchased bot traffic; comparison with commercial anti-bot services; measurement of modern APIs and privacy-preserving browser changes; analysis of how automation frameworks alter or expose fingerprinting surfaces; false-positive and accessibility analysis for bot-detection use cases rather than privacy countermeasures.

## What it cannot show

- It cannot show that browser fingerprinting reliably detects bots.
- It cannot show which fingerprinting attributes are most useful for bot management.
- It cannot show that anti-bot vendors’ fingerprinting works as claimed.
- It cannot show how bot operators evade fingerprinting systems.
- It cannot show current prevalence without updating the crawl.
- It cannot resolve the privacy/security trade-off; it shows targeted mitigation can reduce breakage, but fingerprinting remains privacy-sensitive.
- It cannot replace sources like FP-Inconsistent, which directly measure evasive bot traffic against anti-bot services.

## Project impact

- Strong foundations source for the browser fingerprinting section.
- Useful background source before FP-Inconsistent: FP-Inspector explains fingerprinting scripts and APIs; FP-Inconsistent then studies evasive bot fingerprints and commercial anti-bot outcomes.
- Supports a clear project distinction between:
  - detecting fingerprinting scripts
  - using fingerprints to detect bots
  - bots evading fingerprint-based detection
- Useful for explaining why browser fingerprinting is controversial: it supports bot detection and anti-fraud, but also enables opaque cross-site tracking.
- Provides concrete API examples for the technical taxonomy.
- Provides evidence for the site-breakage trade-off when restricting fingerprinting APIs.
- Should not be overused as direct bot-evidence; cite it as fingerprinting foundations and web-measurement evidence.
