# Towards a framework for detecting advanced Web bots — Iliou et al. 2019

## Bibliographic

- **Citation**: Iliou, C., Kostoulas, T., Tsikrika, T., Katos, V., Vrochidis, S., & Kompatsiaris, Y. (2019). Towards a framework for detecting advanced Web bots. In *Proceedings of the 14th International Conference on Availability, Reliability and Security (ARES 2019)*, Canterbury, United Kingdom. ACM. https://doi.org/10.1145/3339252.3339267
- **Source URL or path**: SRC-012-iliou-2019-ares-detecting-advanced-web-bots.pdf
- **Date accessed**: 2026-05-31
- **Category**: academic
- **Tags**: advanced-bots, web-logs, supervised-learning, behavioural, false-positive-rate, feature-selection, honeypot, greynoise, user-agent, evasion, public-data-limits

## What it claims

- Web bot detection is a multifaceted problem: simple bots and advanced bots should not be treated as a single homogeneous class.
- Existing machine-learning approaches to web bot detection can perform very well on simple or conspicuous bots, but this can hide weak performance against advanced bots.
- Advanced web bots can try to evade detection by presenting browser-like fingerprints and, in some cases, humanlike browsing behaviour.
- Web-log features alone can detect simple bots effectively, especially in a false-positive-intolerant setting.
- Detecting advanced bots from HTTP web logs is substantially harder than detecting simple bots.
- Evaluation should separate simple bots from advanced bots, otherwise overall metrics can be misleading.
- Low false-positive requirements matter in realistic web-server settings because misclassifying humans damages user experience.
- Features useful for detecting simple bots differ from features useful for detecting advanced bots.
- The paper’s proposed annotation method combines user-agent classification with honeypot-derived IP evidence to better identify advanced bots than user-agent lists alone.

## What evidence it provides

The paper evaluates a modular supervised machine-learning framework on one year of real HTTP log data from MKLab’s public web server, covering 20 March 2016 to 20 March 2017.

The framework parses HTTP server logs, extracts visitor sessions, computes session-level features, automatically annotates sessions, performs feature analysis/selection, then trains classifiers. Sessions are extracted using an IP plus user-agent pair, with a 30-minute inactivity threshold and a minimum session length of 30 HTTP requests.

The paper splits sessions into:
- simple bot sessions
- advanced bot sessions
- human sessions

The annotation process uses:
- useragentstring.com to classify user-agent strings as browser, crawler, library, link checker, or unknown
- GreyNoise to identify IPs showing malicious or opportunistic activity
- manual annotation for unknown user agents

The dataset includes 26,012 sessions in the simple-bot comparison dataset and 24,211 sessions in the advanced-bot comparison dataset. It uses a time-based train/test split: training data from 20 March 2016 to 4 December 2016, and testing data from 4 December 2016 to 20 March 2017.

The paper tests SVM, Random Forest, AdaBoost, MLP, and a voting classifier. It uses PCA, chi-square ranking, and Sequential Feature Selection to analyse and choose features. It evaluates AUC, balanced accuracy, precision, recall, and F-score, including a false-positive-intolerant working point with FPR = 0.01.

Reported evidence includes:
- simple bots are detected with AUC = 1.00 using the voting classifier
- advanced bots are much harder, with AUC around 0.68 for the voting classifier
- at FPR = 0.01, the voting classifier detects only 18 of 123 advanced bots while misclassifying 417 of 6,195 humans
- in the same low-FPR setting, advanced-bot balanced accuracy is around 55%
- simple-bot detection in the low-FPR setting achieves high precision and recall, while advanced-bot detection does not

The evidence is stronger than a purely controlled synthetic study because it uses real public-server logs, but the ground truth still depends on automatic annotation proxies rather than confirmed bot operator labels.

## Signals or techniques mentioned

- HTTP web-log signals:
  - total requests
  - total session bytes
  - HTTP GET, POST, and HEAD request counts
  - percentage of HTTP 3xx and 4xx responses
  - image, PDF, CSS, and JavaScript request proportions
  - HTML-to-image ratio
  - unsigned referrers
  - search-engine referrer indicator
  - unknown referrer indicator
  - URL depth standard deviation
  - maximum and average requests per page
  - consecutive sequential HTTP request features
  - session time
  - browsing speed
  - standard deviation of inter-request times
- Session construction:
  - IP plus user-agent pair
  - 30-minute inactivity timeout
  - minimum request threshold
- Annotation signals:
  - user-agent type
  - browser-like user-agent
  - GreyNoise / honeypot-observed malicious activity
- Methods:
  - Support Vector Machine
  - Random Forest
  - AdaBoost
  - Multi-layer Perceptron
  - voting classifier / probability averaging
  - PCA
  - chi-square feature ranking
  - Sequential Feature Selection
  - ROC / AUC
  - false-positive-rate working points
  - balanced accuracy
- Threat / evasion concepts:
  - browser-like fingerprint
  - humanlike behaviour
  - user-agent spoofing
  - IP randomisation
  - avoiding robots.txt
  - advanced bots as a separate detection target

## Threat types covered

The paper is not organised around OWASP OAT categories, but it discusses malicious web bots used for:

- content scraping
- vulnerability scanning
- account takeover
- distributed denial of service
- marketing fraud
- carding
- spam

The experimental focus is not a specific business-logic abuse type. It is mainly about detecting simple versus advanced web bots in HTTP web logs. In the project’s vocabulary, it is most relevant to advanced scraping/content-harvesting bots and general automated web abuse rather than credential stuffing, carding, scalping, or fake account creation specifically.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates the practical problem of detecting automated sessions in real HTTP web-server logs when some bots are obvious and others try to look browser-like. Its main value is methodological: it shows that high aggregate bot-detection performance can mask weak detection of advanced/evasive bots, especially when false positives must be kept low.

- **What does it fail to represent?**  
  The dataset is from a public web server, not a transactional site with login, checkout, booking, stock, payment, loyalty, or account flows. The advanced-bot labels are inferred from user-agent and GreyNoise/honeypot evidence, not confirmed by operator intent or ground-truth instrumentation. The method does not use client-side behaviour, JavaScript fingerprinting, mouse dynamics, TLS fingerprints, residential proxy detection, graph/entity resolution, or cross-domain telemetry. It predates modern browser-native automation, cloud browser services, anti-detect browsers at current maturity, AI browser agents, and large-scale residential proxy commercialisation.

- **What additional evidence would be needed to go further?**  
  Production-labelled data from transactional web applications; validation against known bot campaigns or controlled bot runs; comparison with client-side behavioural and fingerprinting signals; tests against modern Playwright/Puppeteer/Selenium stealth tooling; analysis under residential proxy rotation; precision/recall trade-offs under realistic business costs; repeat evaluation on multiple sites and sectors.

## What it cannot show

- It cannot show that HTTP web logs alone are sufficient for advanced bot management.
- It cannot show production performance against modern stealth automation.
- It cannot prove that GreyNoise/honeypot-labelled sessions are all malicious web bots targeting the site.
- It cannot distinguish all human users from NAT/shared-IP bot activity with certainty because sessions are based on IP plus user-agent rather than stronger identity.
- It cannot evaluate mobile-app or API-specific bot abuse.
- It cannot address mouse dynamics, keystroke behaviour, browser fingerprinting, TLS fingerprinting, or graph/entity approaches.
- It cannot establish prevalence or business impact of advanced bots.
- It cannot support vendor-like claims about operational mitigation, only detection performance under the paper’s setup.

## Project impact

- Provides the cleanest source for the claim that simple-bot detection results can hide poor advanced-bot detection.
- Supports the project’s “framing distance” theme: reported ML performance depends heavily on the bot sophistication included in the dataset.
- Useful anchor for the Technical territory section on web-log-based bot detection.
- Useful contrast with the later Iliou et al. 2021 paper, which responds to this limitation by adding mouse behavioural biometrics.
- Supports an argument page on why bot-detection evaluation must define the threat model before presenting metrics.
- Gives concrete web-log feature families that can be used in the methodology investigations section.
- Should be cited cautiously because its advanced-bot labels are proxy labels, not fully verified ground truth.
- Reinforces the project’s public-data-limits position: real web logs are useful, but without richer telemetry and stronger labels, advanced bot evaluation remains uncertain.
