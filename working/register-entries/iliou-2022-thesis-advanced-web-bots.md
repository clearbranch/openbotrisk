# Machine Learning Based Detection and Evasion Techniques for Advanced Web Bots — Iliou 2022

## Bibliographic

- **Citation**: Iliou, C. (2022). *Machine Learning Based Detection and Evasion Techniques for Advanced Web Bots*. PhD dissertation, Bournemouth University, Faculty of Science & Technology, Department of Computing and Informatics.
- **Source URL or path**: `ILIOU, Christos_Ph.D._2022(1).pdf` / local archived PDF
- **Date accessed**: 2026-05-31
- **Category**: academic
- **Tags**: advanced-bots, behavioural, mouse-dynamics, web-logs, evasion, machine-learning, cnn, reinforcement-learning, gan, taxonomy, methods, adversarial-evaluation

## What it claims

- Web bots vary by sophistication, from simple scripts through browser-automation bots to advanced bots with browser-like fingerprints and humanlike behaviour.
- Advanced web bots are more difficult to detect because they can combine browser-like fingerprints with humanlike browsing behaviour, mouse movements, keystrokes, CAPTCHA-solving capability, proxies, and other evasion techniques.
- Behaviour-based detection is harder for attackers to evade than simple signature or indicator-based detection because changing behaviour requires more effort than changing a single indicator of compromise.
- Existing behaviour-based web bot detection methods can perform well in aggregate but perform poorly when evaluated specifically against advanced web bots.
- Web-log detection and mouse-trajectory detection capture complementary parts of behaviour; combining them can improve detection of advanced bots.
- Mouse trajectories can be represented as images and classified using convolutional neural networks.
- Advanced web bots can use reinforcement learning to adapt browsing behaviour in response to detection feedback and find behaviours that evade web-log based detectors.
- Advanced web bots can use GANs to generate humanlike mouse or touchscreen trajectories that reduce the effectiveness of CNN-based trajectory detectors.
- Web bot detection should be treated as an adaptive detection/evasion problem rather than a static binary classification task.
- Detection frameworks need continual updating because bots can adapt their fingerprints and behaviour over time.

## What evidence it provides

The thesis provides both literature review and empirical experiments.

For the web-log detection work, it uses HTTP logs from MKLab's public web server over one year, from 20 March 2016 to 20 March 2017. Sessions with more than 30 requests were retained. Sessions were labelled using user-agent parsing and GreyNoise checks, producing human, simple-bot, and advanced-bot groups. Two sub-datasets were built: D1 for humans plus simple bots and D2 for humans plus advanced bots. The thesis reports that the same broad detection approach performs much less well against advanced bots than against simple bots.

For the combined web-log plus mouse-movement framework, the thesis uses a controlled web server containing Wikipedia-derived pages. In the first phase, 50 human sessions, 50 moderate-bot sessions, and 50 advanced-bot sessions were collected. D3 compares humans with moderate bots; D4 compares humans with advanced bots. In the second phase, an expanded 110-page web server was used, with 28 additional users creating two sessions each. D5 compares humans with advanced bots; D6 compares humans with a mix of moderate and advanced bots. The second phase uses user-independent 7-fold cross-validation and repeats experiments five times to account for training randomness.

For the web-log module, the thesis evaluates an ensemble of SVM, Random Forest, AdaBoost, and MLP classifiers. It uses feature extraction from HTTP request behaviour, file types, response codes, and browsing patterns, with feature selection via PCA, chi-square, SFS, and SFFS depending on experiment.

For the mouse-trajectory module, it collects mouse movements via a JavaScript file embedded in pages, stores coordinates and timestamps, converts mouse trajectories to two-dimensional matrices/images, and uses CNNs for classification. The thesis reports that combining web logs and mouse movement scores can detect advanced bots more effectively than either signal family alone.

For the reinforcement-learning evasion experiments, the thesis models scraping bots interacting with a 110-page server. Bots use deep Q-learning / DQN to learn which pages to visit and how long to wait, with reward shaped around evading detection and exploring new pages. Heuristic bots show near-zero evasion in the reported tests, while RL bots increasingly find evasive behaviours as training increases. The thesis also evaluates retraining of the detector on RL-bot behaviours, showing that retraining reduces evasion initially but that further bot training can again find evasive behaviours.

For the GAN evasion experiments, the thesis considers scraping bots using mouse trajectories and mobile bots using touchscreen trajectories. It uses a Web dataset from controlled browsing sessions and the HuMIdb mobile dataset. Human trajectory images are split by user so the detector and the evasive bots train on different user sets. The detector achieves high balanced accuracy when trained and tested against GAN-generated bot trajectories from the same setup, but detection recall drops when evaluated against trajectories generated by evasive bots trained on different human data. The reported average bot recall is 0.452 for the Web mouse-trajectory dataset and 0.937 for HuMIdb, implying much stronger evasion in the web mouse-trajectory setting.

## Signals or techniques mentioned

- Bot sophistication levels: simple scripts, browsing-automation bots, moderate bots, advanced bots
- Browser-like fingerprints and fingerprint evasion
- Selenium, Puppeteer, Puppeteer stealth plugin
- JavaScript/browser properties used to detect automation, including Selenium-related artefacts
- User-agent strings and user-agent parsing
- IP-based annotation and GreyNoise API checks
- HTTP logs and web-session extraction
- Session identifiers, including IP plus user-agent and PHP session ID
- Session timeout of 30 minutes
- Web-log features from request frequency, requested content type, response codes, HTTP errors, access patterns, session length, browsing speed, and hyperlink-following behaviour
- Feature analysis and selection: PCA, chi-square, SFS, SFFS
- Classifiers: SVM/SVC, Random Forest, AdaBoost, MLP, voting / ensemble class probability averaging
- Evaluation metrics: accuracy, balanced accuracy, precision, recall, F-score, ROC/AUC, false positive rate working points
- Mouse movement collection through embedded JavaScript
- Mouse coordinates and timestamps: `(x, y, t)` sequences
- Mouse trajectories represented as images / two-dimensional matrices
- CNNs for mouse-trajectory image classification
- Fusion of web-log and mouse-movement detector scores
- Reinforcement learning for evasion
- Q-learning, DQN, epsilon-greedy exploration, experience replay, reward shaping
- Python Gym, keras-rl2, TensorFlow, Keras
- GANs and DCGANs for generating synthetic humanlike mouse or touchscreen trajectories
- Generator/discriminator adversarial training
- LeakyReLU, convolutional and transposed-convolutional layers
- CAPTCHA and CAPTCHA-solving as part of the wider bot landscape
- Proxies, IP changes, browser automation software, regular browsers, malware-controlled browsers
- Replay attacks as an acknowledged limitation

## Threat types covered

The thesis covers a broad set of bot and automated-abuse categories, including:

- Content scraping / web scraping, including price, inventory, and content extraction
- Scalping and limited-stock purchasing
- Denial of inventory / cart holding
- Credential cracking, password guessing, password spraying, credential stuffing, and account takeover
- Fake account creation for spam, propaganda amplification, reviews, surveys, and SEO manipulation
- Validation of stolen card data, gift cards, coupons, and vouchers
- Web scanning and footprinting
- HTTP-level DoS/DDoS
- Ad fraud and click/display manipulation
- Expediting, sniping, and rapid action abuse
- Skewing decision-making metrics

In OWASP OAT terms, it is most relevant to scraping, credential stuffing, account takeover, carding/payment-flow abuse, scalping, denial of inventory, account creation, and ad/click fraud. The thesis is not organised around OWASP OAT labels, so the mapping should be treated as project-side alignment rather than the author's own taxonomy.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  This is one of the strongest academic anchors for the project's advanced-bot territory. It approximates the arms race between behaviour-based detectors and bots that attempt to look human at both the web-log and mouse-movement levels. It is especially useful for the question: once bots run through browser automation and attempt humanlike timing, page navigation, and mouse movement, how much does behaviour-based detection still buy, and how can evasion pressure reduce reported performance?

- **What does it fail to represent?**  
  The empirical setting is still mostly academic and controlled. The web-log dataset comes from one public lab web server, and the mouse-trajectory experiments use constructed web servers with Wikipedia-derived pages and generated moderate/advanced bots. The human sample sizes are modest compared with production traffic. Bot behaviours are generated by the researcher rather than by real adversaries operating for economic gain. The detector does not have commercial cross-customer telemetry, production-scale device intelligence, reputation graphs, residential-proxy signals, payment/account history, or multi-site entity resolution. The work predates the current wave of cloud browser infrastructure, AI browser agents, and some modern anti-detect tooling. The source is strong on behavioural and ML evasion, but weaker on current infrastructure-level bot operations.

- **What additional evidence would be needed to go further?**  
  Production data from real bot-management deployments; evaluations against current Playwright/Puppeteer/Selenium stealth stacks, anti-detect browsers, cloud browsers, browser extensions, residential proxies, and AI agents; independent replication of the datasets and methods; longitudinal evaluation showing how detector/bot adaptation behaves over time; comparisons with commercial telemetry features; and studies of how these behavioural signals combine with graph/entity-resolution and infrastructure signals.

## What it cannot show

- It cannot show that the reported detection performance would generalise to production bot-management systems.
- It cannot show that mouse trajectories alone are sufficient for operational detection; the thesis itself supports combining signal families.
- It cannot show that the generated advanced bots match the full diversity, incentives, and engineering quality of real adversarial bots.
- It cannot show how modern browser-native automation, cloud browser services, browser extensions, AI browser agents, or current anti-detect stacks behave, because those are outside the thesis period and setup.
- It cannot validate vendor-scale claims, because it lacks cross-customer telemetry and commercial operational data.
- It cannot prove that RL or GAN evasion are common in the wild; it shows that these techniques are technically plausible and can reduce detector performance in the tested settings.
- It cannot resolve legal, economic, or actor-attribution questions; those are outside both the thesis and this project's intended scope.
- It cannot eliminate the replay-attack issue for mouse movement detection; the thesis flags this as a limitation.
- It cannot make the OAT taxonomy unnecessary; it complements OWASP by adding academic detection/evasion evidence rather than replacing the threat-category vocabulary.

## Project impact

- Acts as the main academic anchor for the openbotrisk treatment of advanced web bot detection.
- Provides a useful sophistication taxonomy: simple scripts, browsing automation, moderate bots, and advanced bots with browser-like fingerprints plus humanlike behaviour.
- Supports the project's decision to treat bot detection as an adaptive detection/evasion problem, not a static classifier benchmark.
- Provides concrete empirical support for separating simple-bot performance from advanced-bot performance.
- Supports a technical territory section organised around signal families: web logs, browser/fingerprint indicators, mouse/behavioural biometrics, and fused detection.
- Provides methodological examples for the project's public-data limits argument: the experiments are useful, but still far from commercial telemetry and production adversarial traffic.
- Provides a strong source for the claim that high reported performance can hide weak performance against the harder subclass of advanced bots.
- Provides evidence that combining signals can improve robustness, while also showing that fused detection still faces adaptive evasion.
- Provides concrete examples of adversarial evaluation using RL and GANs, useful for the methodology investigations and controlled-experiment planning.
- Should be cited alongside OWASP rather than instead of OWASP: OWASP supplies the abuse taxonomy; Iliou supplies academic detection/evasion framing and methods evidence.
- The project should avoid treating the thesis as comprehensive coverage of the current threat surface. It is strong on behavioural ML detection and evasion, but should be supplemented with current vendor, threat-surface, browser-automation, cloud-browser, and AI-agent sources.
