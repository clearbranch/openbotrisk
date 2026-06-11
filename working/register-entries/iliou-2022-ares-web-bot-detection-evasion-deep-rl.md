# Web Bot Detection Evasion Using Deep Reinforcement Learning — Iliou et al. 2022

## Bibliographic

- **Citation**: Iliou, C., Kostoulas, T., Tsikrika, T., Katos, V., Vrochidis, S., & Kompatsiaris, I. (2022). Web Bot Detection Evasion Using Deep Reinforcement Learning. In *Proceedings of the 17th International Conference on Availability, Reliability and Security (ARES 2022)*, Vienna, Austria. ACM, Article 15, 1–10. https://doi.org/10.1145/3538969.3538994
- **Source URL or path**: SRC-014-iliou-2022-ares-web-bot-detection-evasion-deep-rl.pdf
- **Date accessed**: 2026-05-31
- **Category**: academic
- **Tags**: advanced-bots, evasion, reinforcement-learning, deep-reinforcement-learning, DQN, web-logs, behavioural, adversarial-evaluation, scraping, adaptive-adversary, public-data-limits

## What it claims

- Behaviour-based web bot detectors that use web-log features can be evaded by bots using reinforcement learning.
- Web bots can learn browsing behaviours that avoid detection while still visiting pages on a target web server.
- A realistic bot-detection/evasion setting should model both sides as adaptive: bots update their behaviour to evade detection, while the detector retrains on new bot behaviours.
- Heuristic evasive bots are generally detected more easily than reinforcement-learning bots in the paper’s experimental setup.
- Retraining the detector on RL-generated behaviours improves detection of those behaviours, but bots can retrain again and find new evasive behaviours.
- The detection/evasion problem is dynamic rather than static; fixed evaluation against a single bot population is insufficient.
- Using more RL training requests can improve bot evasiveness, but this comes with operational cost because many bots/fingerprints may be needed during training.
- Additional detection mechanisms are needed for bots that use recent machine-learning advances to evade behaviour-based detection.

## What evidence it provides

The paper proposes and evaluates a reinforcement-learning environment for web bot detection evasion.

The environment consists of a web server plus a web bot detection framework. The detector groups web logs into sessions, extracts web-log features, and classifies sessions using an ensemble of SVM, Random Forest, AdaBoost, and MLP classifiers. Detection is performed per request, using separate models for each number of requests considered.

The RL mapping is explicit:
- agent: web bot
- environment: web server and detection framework
- actions: visiting web pages
- state: pages already visited
- reward: value depending on page visited and whether the bot is detected

The RL bot actions include:
- simple download: download only the main page content
- full download: download the page and additional resources such as images, CSS, and JavaScript
- waiting between requests to simulate reading time

The state vector encodes visits to web pages, with different states for simple and full downloads. The reward structure gives positive reward for visiting new pages and new states without detection, zero reward for detection, and a high reward for successfully evading detection after visiting the required number of pages.

The agent uses Deep Q-Networks (DQN), implemented with Gym, keras-rl2, and Keras. The DQN has an input size based on the number of page states and an output size based on the possible actions. Hyperparameters are selected heuristically, including epsilon-greedy exploration probability 0.2 and discount factor 0.9.

The evaluation uses the dataset from Iliou et al. 2021, based on a web server with 110 Wikipedia-derived pages and 112 sessions: 56 human sessions from 28 users and 56 bot sessions. The detector is trained on approximately 70% of the data and tested on the rest.

The evaluation has two phases:
- **Phase 1**: RL bots attempt to evade a pre-trained detector that has not seen RL-generated bot behaviours.
- **Phase 2**: The detector is retrained on RL-generated behaviours, then tested against both previously trained RL bots and newly retrained RL bots.

The paper reports that heuristic bots are mostly detected:
- simple download: 0.7% evasion
- full download: 0.0%
- random: 0.0%
- heuristic #1: 0.1%
- heuristic #2: 0.0%

RL bots achieve higher evasion in Phase 1, with reported evasion rates including:
- RL bot @30k: 38.5%
- RL bot @100k: 39.3%
- RL bot @300k: 44.2%
- RL bot @500k: 38.0%

After detector retraining, the previously trained RL bot @300k falls to 3.4% evasion, but retrained RL bots can again increase evasion:
- RL bot @300k: 18.0%
- RL bot @2m: 56.5%

The paper interprets this as evidence that RL bots can adapt after defenders retrain, although at high training cost.

## Signals or techniques mentioned

- Web-log/session features:
  - total requests
  - total session bytes
  - HTTP GET, POST, HEAD counts
  - percentage of HTTP 3xx and 4xx responses
  - percentage of image, CSS, and JavaScript requests
  - HTML-to-image ratio
  - URL depth standard deviation
  - maximum and average requests per page
  - consecutive sequential HTTP request features
  - session time
  - browsing speed
  - standard deviation of inter-request times
- Detection methods:
  - SVM
  - Random Forest
  - AdaBoost
  - Multi-layer Perceptron
  - ensemble / class-probability averaging
  - per-request detection
  - grid search with 2-fold cross-validation
- Evasion methods:
  - reinforcement learning
  - Deep Q-Network
  - Q-learning
  - epsilon-greedy exploration
  - experience replay
  - reward shaping
  - simple download vs full download
  - simulated waiting / reading time
  - retraining against updated detector
- Infrastructure / tools:
  - Gym
  - keras-rl2
  - Keras
  - PHP session ID
  - Wikipedia-derived controlled web server
  - Puppeteer stealth mentioned as background
  - configurable browser fingerprints mentioned as background

## Threat types covered

The paper is not organised by OWASP OAT category.

The experimental threat model is scraping/content harvesting: web bots repeatedly visit a web server to harvest its content while trying to avoid behaviour-based detection.

Relevant project/OAT mappings:
- closest to OWASP OAT-011 Scraping
- related to scalping only at the conceptual level, because scalping is discussed as a malicious bot use case but not experimentally modelled
- related to credential stuffing, carding, account creation, and vulnerability scanning only as background examples of malicious automation, not as evaluated behaviours

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  The paper approximates adaptive web scraping bots that learn which browsing sequences and timing patterns allow them to avoid web-log-based detection. It is especially useful for thinking about detection/evasion as a feedback loop: defenders train detectors, bots adapt, defenders retrain, bots adapt again.

- **What does it fail to represent?**  
  The setting is controlled and narrow. The target site contains Wikipedia-derived pages, not real transactional workflows such as login, booking, checkout, account creation, gift-card redemption, or payment. The RL agent’s action space is simplified to page choice, download mode, and waiting time. The bot’s goal is content traversal/evasion, not completing an economically meaningful abuse flow. The detector uses web-log features only; it does not include browser fingerprints, TLS fingerprints, JavaScript instrumentation, mouse behaviour, keystrokes, device signals, graph/entity resolution, cross-site telemetry, or commercial threat intelligence. The paper assumes bots can change fingerprints after detection, but does not implement or cost a realistic fingerprint/proxy supply chain. It also does not include current browser-native automation stacks, cloud browsers, residential proxies, anti-detect browsers, extensions, or AI browser agents.

- **What additional evidence would be needed to go further?**  
  Tests against real browser automation tools integrated with RL decision-making; production-style transactional flows; detectors using multiple signal families; evaluation under residential proxy/fingerprint constraints; cost modelling for bot training and fingerprint supply; comparison with non-RL adaptive strategies; evaluation against modern bot-management defences; experiments where both defender and attacker update repeatedly over longer time horizons.

## What it cannot show

- It cannot show that real bot operators currently use this exact RL approach.
- It cannot show that RL bots can evade commercial bot-management systems in production.
- It cannot show that web-log evasion alone is sufficient when defenders use fingerprints, behavioural biometrics, TLS signals, graph signals, or cross-customer telemetry.
- It cannot show operational feasibility without accounting for infrastructure, fingerprints, IP reputation, proxy costs, and detection-triggered blocking.
- It cannot generalise directly to credential stuffing, carding, scalping, fake account creation, or API abuse because the experiment models web-page traversal/scraping.
- It cannot show that longer RL training is always better; the paper itself notes training costs and detector update cycles may make very long training impractical.
- It cannot replace production telemetry because the dataset and environment are controlled and small.

## Project impact

- Provides a focused academic anchor for the project’s adaptive-adversary framing.
- Supports the claim that bot management is not simply a static classifier problem; it is a repeated detection/evasion game.
- Complements the Iliou 2021 GAN paper: GANs target mouse/touch behavioural evasion, while this paper targets web-log behavioural evasion.
- Useful for the Technical territory section on behavioural detection limits and evasion.
- Useful for Methodology investigations if the project later tests simple adaptive agents against public-data detectors.
- Supports a “public data cannot fully represent production adversarial pressure” argument: the paper shows adaptation matters, but also exposes how much simplification is needed in academic experiments.
- Should be cited carefully as a proof-of-concept mechanism, not as evidence of observed production RL bot campaigns.
