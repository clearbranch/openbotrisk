# Machine Learning Based Detection and Evasion Techniques for Advanced Web Bots — Iliou 2022

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: Claude (chat interface)
- **Model name + version, if known**: Claude Opus 4.8
- **Source access**: full text (183-page PDF). Load-bearing figures verified directly against the results chapters: web-log ROC (D1/D2 AUC), the GAN evasion recall table, and the dataset-construction passages. Not every claim re-derived from the PDF; qualitative claims carried from the v1 extraction were spot-checked, not exhaustively re-read.
- **Prompt version**: source-extraction-prompt v3 (2026-06)
- **Re-extraction note**: v2 re-run of `iliou-2022-thesis-advanced-web-bots.md` (SRC-011). Adds the v3 metadata block, `Evidence basis`, `Operational proximity`, and the scarce-resource section that the v1 file predated; sharpens the advanced-bot detection figure (D2 AUC = 0.64) which v1 left qualitative. Does not contradict v1 on any verified point.

## Bibliographic

- **Citation**: Iliou, C. (2022). *Machine Learning Based Detection and Evasion Techniques for Advanced Web Bots*. PhD dissertation, Bournemouth University, Faculty of Science & Technology, Department of Computing and Informatics. February 2022.
- **Source URL or path**: local archived PDF `ILIOU__Christos_Ph_D__2022.pdf`. No DOI or stable repository URL recorded in the document; the expected repository is Bournemouth University Research Online (BURO) but the stable URL is **not verified** — flag for the author to confirm before the citation is published.
- **Date accessed**: 2026-05-31 (v1); re-verified 2026-06-06 (v2)
- **Category**: academic
- **Evidence basis**: empirical-academic — a controlled study combining a literature review with original detection and evasion experiments (web-log classifiers, CNN mouse-trajectory detection, RL and GAN evasion).
- **Operational proximity**: `capability` — rigorous controlled/academic work, but it does not measure observed abuse against a real commercial target. The web-log data is from one low-traffic academic server (MKLab) with weak/proxy labels (user-agent parsing + GreyNoise); the advanced-bot, RL, and GAN experiments use researcher-generated bots on constructed servers. Per the v3 rule, a rigorous controlled experiment is `capability`, not `observed`/`measured`, unless it measures real-target activity.
- **Tags**: advanced-bots, behavioural, mouse-dynamics, web-logs, evasion, machine-learning, cnn, reinforcement-learning, gan, taxonomy, methods, adversarial-evaluation

## What it claims

- Web bots vary by sophistication, from simple scripts through browser-automation bots to advanced bots with browser-like fingerprints and humanlike behaviour.
- Advanced web bots are harder to detect because they combine browser-like fingerprints with humanlike browsing behaviour, mouse movements, keystrokes, CAPTCHA-solving, proxies, and other evasion techniques.
- Behaviour-based detection is harder to evade than signature/indicator-based detection, because changing behaviour requires more effort than changing a single indicator.
- Existing behaviour-based detection methods can perform well in aggregate but perform poorly when evaluated specifically against advanced web bots.
- Web-log detection and mouse-trajectory detection capture complementary parts of behaviour; combining them improves detection of advanced bots.
- Mouse trajectories can be represented as images and classified with convolutional neural networks.
- Advanced web bots can use reinforcement learning to adapt browsing behaviour against detection feedback and find behaviours that evade web-log detectors.
- Advanced web bots can use GANs to generate humanlike mouse/touchscreen trajectories that reduce the effectiveness of CNN-based trajectory detectors.
- Web bot detection should be treated as an adaptive detection/evasion problem, not a static binary classification task; detection frameworks need continual updating because bots adapt over time.

## What evidence it provides

The thesis provides both a literature review and original empirical experiments.

**Web-log detection.** Uses HTTP logs from MKLab's public web server over one year (20/3/2016–20/3/2017). Sessions are defined by IP + user-agent (+ PHP session ID) with a 30-minute idle timeout, and only sessions with more than k=30 requests are retained. Labels are assigned by user-agent parsing and GreyNoise checks, producing human, simple-bot, and advanced-bot groups. Two sub-datasets isolate the comparison: **D1** (humans + simple bots) and **D2** (humans + advanced bots). An ensemble of SVM, Random Forest, AdaBoost, and MLP classifiers is used, with features from request frequency, content types, response codes, HTTP errors, access patterns, session length, browsing speed, and hyperlink-following, and feature selection via PCA, chi-square, SFS, SFFS.
  - **Verified load-bearing result:** the framework detects simple bots (D1) at **AUC = 1.00** but advanced bots (D2) at only **AUC = 0.64**, and the thesis states that at a low false-positive rate the framework detects very few advanced bots. This is the thesis's own quantification of "high aggregate performance hides weak advanced-bot detection." (NB: 0.64 is the *thesis* figure; the ~0.68-at-low-FPR figure belongs to the 2019 ARES paper, SRC-012 — do not conflate.)

**Combined web-log + mouse-movement framework.** Uses a controlled web server of Wikipedia-derived pages. Phase 1: 50 human, 50 moderate-bot, 50 advanced-bot sessions (D3 = humans vs moderate; D4 = humans vs advanced). Phase 2: an expanded 110-page server (11 Wikipedia topics) with 28 additional users creating two sessions each (D5 = humans vs advanced; D6 = humans vs moderate+advanced mix), evaluated with user-independent 7-fold cross-validation repeated five times to account for training randomness. Mouse movements are collected via embedded JavaScript as `(x, y, t)` sequences, converted to 2-D images/matrices, and classified with CNNs; web-log and mouse-movement detector scores are then fused. The thesis reports fused detection outperforms either signal family alone, with very high accuracy/AUC (>0.999) in its tested setups.

**Reinforcement-learning evasion.** Models scraping bots on the 110-page server using deep Q-learning (DQN, epsilon-greedy, experience replay, reward shaped around evading detection while exploring pages). Heuristic bots show near-zero evasion; RL bots increasingly find evasive behaviours as training increases. Retraining the detector on RL-bot behaviour reduces evasion initially, but further bot training again finds evasive behaviours — i.e. an adaptive arms race rather than a stable equilibrium.

**GAN evasion.** Considers scraping bots (mouse trajectories) and mobile bots (touchscreen trajectories), using a controlled Web dataset and the HuMIdb mobile dataset, with human trajectories split by user so detector and evasive bots train on different users. The detector scores well against same-setup GAN trajectories but recall drops against trajectories from evasive bots trained on different human data. **Verified figure:** average bot recall is **0.452 (Web mouse-trajectory)** vs **0.937 (HuMIdb)**, i.e. much stronger evasion in the web mouse-trajectory setting.

## Signals or techniques mentioned

- Bot sophistication levels: simple scripts, browsing-automation bots, moderate bots, advanced bots
- Browser-like fingerprints and fingerprint evasion; Selenium, Puppeteer, Puppeteer stealth plugin; JavaScript/browser properties used to detect automation (incl. Selenium artefacts)
- User-agent strings and parsing; IP-based annotation and GreyNoise API checks
- HTTP logs and web-session extraction; session identifiers (IP + user-agent + PHP session ID); 30-minute session timeout; k=30 request threshold
- Web-log features: request frequency, content type, response codes, HTTP errors, access patterns, session length, browsing speed, hyperlink-following
- Feature analysis/selection: PCA, chi-square, SFS, SFFS
- Classifiers: SVM/SVC, Random Forest, AdaBoost, MLP, voting / ensemble probability averaging
- Evaluation metrics: accuracy, balanced accuracy, precision, recall, F-score, ROC/AUC, FPR working points
- Mouse-movement collection via embedded JavaScript; `(x, y, t)` sequences; trajectories represented as images / 2-D matrices; CNN trajectory classification; fusion of web-log and mouse-movement scores
- Reinforcement learning for evasion: Q-learning, DQN, epsilon-greedy, experience replay, reward shaping; Python Gym, keras-rl2, TensorFlow, Keras
- GANs/DCGANs for synthetic humanlike mouse/touchscreen trajectories; generator/discriminator adversarial training; LeakyReLU, convolutional and transposed-convolutional layers
- CAPTCHA and CAPTCHA-solving; proxies, IP changes, browser-automation software, regular browsers, malware-controlled browsers
- Replay attacks (acknowledged limitation)

## Threat types covered

The thesis covers a broad set of bot/automated-abuse categories, including: content/web scraping (price, inventory, content); scalping and limited-stock purchasing; denial of inventory / cart holding; credential cracking, password guessing/spraying, credential stuffing, account takeover; fake account creation (spam, propaganda, reviews, surveys, SEO); validation of stolen card data, gift cards, coupons, vouchers; web scanning and footprinting; HTTP-level DoS/DDoS; ad fraud and click/display manipulation; expediting/sniping/rapid-action abuse; skewing decision-making metrics.

In OWASP OAT terms it aligns most with scraping, credential stuffing, account takeover, carding/payment-flow abuse, scalping, denial of inventory, account creation, and ad/click fraud. The thesis is **not** organised around OWASP OAT labels, so the mapping is project-side alignment, not the author's taxonomy.

## Scarce-resource abuse fields

**Not applicable — source does not concern scarce-resource abuse.** The thesis lists scalping, denial of inventory, and expediting/sniping among bot threat categories in its taxonomy, but it does not study scarce-resource abuse as a subject; its empirical work is scraping/advanced-bot detection and mouse-trajectory/web-log methods plus RL/GAN evasion. Do not project scarce-resource fields onto this row.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**
  One of the strongest academic anchors for the project's advanced-bot territory. It approximates the arms race between behaviour-based detectors and bots that try to look human at both the web-log and mouse-movement levels — specifically: once bots run through browser automation with humanlike timing, navigation, and mouse movement, how much does behaviour-based detection still buy, and how far can evasion pressure reduce reported performance?

- **What does it fail to represent?**
  The empirical setting is mostly academic and controlled. The web-log data is from a single low-traffic public lab server; the mouse-trajectory experiments use constructed servers with Wikipedia-derived pages and researcher-generated moderate/advanced bots, with modest human sample sizes. Bot behaviours are generated by the researcher, not by adversaries operating for economic gain. The detector has no commercial cross-customer telemetry, production-scale device intelligence, reputation graphs, residential-proxy signals, payment/account history, or multi-site entity resolution. The work predates the current wave of cloud-browser infrastructure, AI browser agents, and some modern anti-detect tooling. Strong on behavioural/ML evasion; weaker on infrastructure-level bot operations.

- **What additional evidence would be needed to go further?**
  Production data from real bot-management deployments; evaluation against current Playwright/Puppeteer/Selenium stealth stacks, anti-detect browsers, cloud browsers, browser extensions, residential proxies, and AI agents; independent replication of the datasets/methods; longitudinal evaluation of detector/bot adaptation over time; comparison with commercial telemetry features; and study of how these behavioural signals combine with graph/entity-resolution and infrastructure signals.

## What it cannot show

- Cannot show the reported detection performance generalises to production bot-management systems.
- Cannot show mouse trajectories alone are sufficient for operational detection — the thesis itself favours combining signal families.
- Cannot show the generated advanced bots match the full diversity, incentives, and engineering quality of real adversarial bots.
- Cannot show how modern browser-native automation, cloud-browser services, browser extensions, AI browser agents, or current anti-detect stacks behave — those are outside the thesis period and setup.
- Cannot validate vendor-scale claims — it lacks cross-customer telemetry and commercial operational data.
- Cannot prove RL or GAN evasion are common in the wild; it shows they are technically plausible and can reduce detector performance in the tested settings.
- Cannot resolve legal, economic, or actor-attribution questions — outside both the thesis and this project's scope.
- Cannot eliminate the replay-attack issue for mouse-movement detection; the thesis flags this as a limitation.
- Cannot make the OAT taxonomy unnecessary; it complements OWASP by adding academic detection/evasion evidence rather than replacing the threat-category vocabulary.

## Project impact

- Main academic anchor for the openbotrisk treatment of advanced web bot detection.
- Supplies the sophistication taxonomy (simple scripts → browsing automation → moderate → advanced with browser-like fingerprints + humanlike behaviour) used on the Background/adversary page.
- Supports treating bot detection as an adaptive detection/evasion problem, not a static classifier benchmark.
- Provides the verified, citable figure for "high aggregate performance hides weak advanced-bot detection": web-log AUC 1.00 (simple, D1) vs **0.64 (advanced, D2)**, very few advanced bots caught at low FPR. This sharpens the SRC-011/SRC-012 split — the thesis figure is 0.64; the ~0.68-at-low-FPR figure is the 2019 ARES paper. Pages citing the advanced-bot weakness should attribute the right number to the right source.
- Supports the technical-territory section organised by signal families (web logs, browser/fingerprint indicators, mouse/behavioural biometrics, fused detection).
- Provides methodological examples for the public-data-limits argument: useful experiments, still far from commercial telemetry and production adversarial traffic.
- Provides concrete adversarial-evaluation examples (RL, GAN) for the methodology investigations and controlled-experiment planning — including the 0.452 vs 0.937 recall contrast as evidence that GAN evasion bites hardest where human data is most varied.
- Should be cited alongside OWASP, not instead of it: OWASP supplies the abuse taxonomy; Iliou supplies academic detection/evasion framing and methods evidence.
- Not comprehensive coverage of the current threat surface — strong on behavioural ML detection/evasion, must be supplemented with current vendor, threat-surface, browser-automation, cloud-browser, and AI-agent sources.
