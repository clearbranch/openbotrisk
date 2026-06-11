# BeCAPTCHA-Mouse: Synthetic Mouse Trajectories and Improved Bot Detection — Acien et al. 2021

## Bibliographic

- **Citation**: Acien, A., Morales, A., Fierrez, J., & Vera-Rodriguez, R. (2021). BeCAPTCHA-Mouse: Synthetic Mouse Trajectories and Improved Bot Detection. arXiv:2005.00890v2.
- **Source URL or path**: SRC-019-acien-2021-becaptcha-mouse-synthetic-mouse-trajectories.pdf
- **Date accessed**: 2026-05-31
- **Category**: academic
- **Tags**: behavioural-biometrics, mouse-dynamics, bot-detection, CAPTCHA, BeCAPTCHA, synthetic-data, GAN, neuromotor, sigma-lognormal, Random-Forest, benchmark, public-data-limits

## What it claims

- Mouse dynamics can help distinguish human users from bots by capturing behavioural and neuromotor features of human-computer interaction.
- BeCAPTCHA-Mouse is proposed as a bot detector based on mouse dynamics, not as a complete replacement for traditional CAPTCHA or other bot-detection systems.
- Synthetic mouse trajectories can improve both training and evaluation of bot detectors.
- Two synthetic mouse-trajectory generation approaches are proposed:
  - a function-based method using heuristic trajectory shapes and velocity profiles
  - a GAN-based method generating human-like trajectories from Gaussian noise
- Neuromotor features based on the Sigma-Lognormal model can distinguish human mouse movements from synthetic bot trajectories.
- Training with both real and synthetic trajectories substantially improves detection compared with training on real trajectories alone.
- Random Forest performs strongly in the reported experiments, especially compared with deeper recurrent models when training data are limited.
- Mouse-based bot detection can complement cognitive CAPTCHA systems by adding behavioural evidence while a user completes normal interaction tasks.
- The BeCAPTCHA-Mouse benchmark provides a public dataset for mouse-based bot-detection research.

## What evidence it provides

The paper provides a benchmark dataset, feature-engineering method, synthetic trajectory generation methods, and experimental evaluations.

The benchmark is based on mouse trajectories from the Shen et al. database. The original data include more than 200,000 mouse trajectories from 58 users, acquired over 30 to 90 days. The paper uses a subset of 35 samples from each of the 58 users, producing more than 5,000 human trajectories. The benchmark contains:
- 5,000 human mouse trajectories
- 5,000 function-based synthetic trajectories
- 5,000 GAN-generated synthetic trajectories

A mouse trajectory is defined as the movement between two consecutive clicks. The task involves clicking eight buttons in sequence, producing trajectories with different directions and lengths.

The proposed neuromotor feature representation uses the Sigma-Lognormal model from the kinematic theory of rapid human movements. It decomposes mouse velocity profiles into primitive lognormal strokes. For each mouse trajectory, the paper extracts parameters from the lognormal decomposition and summarises them into a 37-feature vector.

The paper proposes two synthesis methods:
- **Function-based synthesis**: combines linear, quadratic, and exponential trajectory shapes with constant, logarithmic, and Gaussian velocity profiles.
- **GAN-based synthesis**: uses an LSTM-based GAN generator and discriminator to produce synthetic mouse coordinate sequences from Gaussian noise.

The experiments compare multiple classifiers:
- SVM
- KNN
- Random Forest
- MLP
- LSTM
- GRU
- GAN discriminator

Key reported results include:
- BeCAPTCHA-Mouse detects high-realism bot trajectories with around 93% average accuracy using only one mouse trajectory.
- Combining the proposed neuromotor features with prior global mouse-dynamics features improves accuracy, with reported results up to around 98.7% in the combined scenario.
- Training with real plus synthetic trajectories clearly outperforms training only on real samples.
- Random Forest generally performs best among the tested statistical classifiers, and performs better than LSTM/GRU when training samples are scarce.
- GAN-generated trajectories can look realistic to humans, but classifiers still identify them with high accuracy, suggesting GAN generators may leave detectable artefacts.

The evidence is useful because it includes a public benchmark and directly studies synthetic bot-like mouse trajectories. However, the interaction task is constrained and does not represent full web-browsing or transactional abuse flows.

## Signals or techniques mentioned

- Mouse trajectory x/y coordinates
- Mouse clicks
- Velocity profile
- Direction and length of trajectory
- Initial acceleration
- Final deceleration
- Fine trajectory correction
- Neuromotor decomposition
- Sigma-Lognormal model
- Lognormal stroke parameters:
  - covered distance
  - initialization time
  - log-temporal delay
  - impulse response time
  - starting angle
  - ending angle
- Number of lognormals as a trajectory-complexity feature
- Function-based trajectory synthesis
- GAN-based trajectory synthesis
- LSTM generator/discriminator
- Global mouse-dynamics features:
  - duration
  - distance
  - displacement
  - average angle
  - average velocity
  - movement efficiency
- Classifiers:
  - SVM
  - Random Forest
  - KNN
  - MLP
  - LSTM
  - GRU
  - GAN discriminator
- Fusion with traditional CAPTCHA / contextual bot signals

## Threat types covered

The paper is not organised around OWASP Automated Threat categories.

The direct threat type is bot evasion of human-verification or passive behavioural detection using synthetic mouse trajectories. It is most relevant to:
- CAPTCHA / human-verification bypass
- automated interaction that attempts to look human
- advanced browser automation requiring humanlike mouse movement

Relevant project/OAT mappings:
- indirect relevance to OAT categories where bots must interact with web controls, such as scraping, credential stuffing, scalping, carding, and fake account creation
- strongest direct relevance is not a specific abuse category but the behavioural-detection layer used across many automated threats

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates detection of automated mouse movement in a constrained human-computer interaction task. It is useful for understanding mouse dynamics as a behavioural signal and for showing how synthetic trajectories can be used both to harden detectors and to evaluate detectors under more realistic synthetic attacks.

- **What does it fail to represent?**  
  It does not evaluate full browser sessions, web-log features, API calls, transaction flows, account login, checkout, product drops, scraping journeys, or mobile app abuse. The mouse task is a controlled point-and-click sequence, not natural web browsing. The synthetic bots are trajectory generators, not complete bot operators integrated with Selenium, Playwright, Puppeteer, anti-detect browsers, cloud browsers, residential proxies, or AI agents. It does not assess production false-positive cost, latency, privacy/compliance constraints, or adversarial adaptation over time.

- **What additional evidence would be needed to go further?**  
  Evaluation on natural browsing sessions; integration with browser automation executing real web tasks; comparison with real bot tools and generated mouse events; testing against modern behavioural detectors; production-scale false-positive analysis; tests on touchscreen, trackpad, and accessibility-device inputs; evaluation of privacy and deployment constraints; combination with server-side and fingerprinting signals.

## What it cannot show

- It cannot show that mouse dynamics alone are enough for bot management.
- It cannot show that the method works against modern browser-native automation in production.
- It cannot show prevalence or business impact of mouse-trajectory evasion.
- It cannot show that GAN-generated mouse movement is used by real bot operators.
- It cannot show performance on transactional web abuse flows.
- It cannot show robustness against adversaries who know the feature set and optimise specifically against Sigma-Lognormal or Random Forest detection.
- It cannot replace web-log, fingerprinting, TLS, graph, or threat-intelligence evidence; it only covers one behavioural signal family.

## Project impact

- Strong academic source for the project’s behavioural-biometrics section.
- Useful counterbalance to Iliou et al. 2021/2022: Acien et al. focuses more deeply on mouse neuromotor modelling and benchmark construction.
- Provides a public benchmark source, which is important because much bot-detection work relies on private/vendor data.
- Supports the argument that synthetic data can be valuable for bot-detection evaluation, but also needs careful framing because synthetic tasks may not match production abuse.
- Useful for a section on “mouse dynamics can help, but it is only one signal.”
- Provides a defensible source for explaining why more realistic synthetic bots are needed when evaluating behavioural detectors.
- Should be cited with the limitation that the task is constrained mouse interaction, not full web bot management.
