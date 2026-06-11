# Hacking Google reCAPTCHA v3 using Reinforcement Learning — Akrout et al. 2019

## Bibliographic

- **Citation**: Akrout, I., Feriani, A., & Akrout, M. (2019). Hacking Google reCAPTCHA v3 using Reinforcement Learning. arXiv:1903.01003v3.
- **Source URL or path**: SRC-020-akrout-2019-recaptcha-v3-reinforcement-learning.pdf
- **Date accessed**: 2026-05-31
- **Category**: academic
- **Tags**: recaptcha-v3, CAPTCHA, reinforcement-learning, evasion, mouse-movement, behavioural, human-verification, grid-world, PyAutoGUI, Selenium-limits, public-data-limits

## What it claims

- Google reCAPTCHA v3, which returns a risk score rather than showing an explicit challenge, can be attacked using reinforcement learning.
- The task can be formulated as a grid-world Markov Decision Process where the agent learns to move the mouse to the reCAPTCHA checkbox and click it.
- The authors claim high success rates: 97.4% on a 100 × 100 grid and 96.7% on a 1000 × 1000 screen resolution.
- Larger movement cell sizes reduce success rates, likely because large jumps look less humanlike to reCAPTCHA.
- A divide-and-conquer strategy can extend the trained policy to larger screen resolutions without retraining for every grid size.
- Selenium was ineffective in their setup because reCAPTCHA appeared to detect browser automation artefacts and returned low scores.
- The authors instead used a normal browser launched from the command line and controlled mouse movement using PyAutoGUI.
- Tor/proxy-like routing and not being logged into a Google account affected reCAPTCHA scores in their observations.
- The paper should be read as an early proof-of-concept attack on reCAPTCHA v3, not as a general bot-management bypass.

## What evidence it provides

The paper reports an RL-based experimental attack against Google reCAPTCHA v3.

The authors model the environment as:
- **State space**: possible mouse positions on the web page
- **Action space**: up, left, right, down
- **Goal**: reach and click the reCAPTCHA checkbox
- **Reward/score**: feedback from reCAPTCHA v3, with a high score treated as success

The agent starts from a random position in a top-left or top-right region of the browser window. It moves across a grid until reaching the reCAPTCHA checkbox or a horizon limit. The agent is trained using the REINFORCE policy-gradient algorithm with:
- discount factor γ = 0.99
- two fully connected policy-network layers
- learning rate 10^-3
- batch size 2000

The authors evaluate success over 1000 runs and treat a reCAPTCHA score of 0.9 as a successful pass.

Reported results:
- 97.4% success on a 100 × 100 grid
- more than 90% success across tested larger resolutions using divide-and-conquer
- 96.7% success on a 1000 × 1000 screen resolution
- performance declines as grid cell size increases, with cell size 10 causing detection in more than 20% of test runs

Important implementation details:
- Initial Selenium-based attempts produced low scores, even for a human user, suggesting Selenium/browser automation artefacts were detected.
- The final environment avoided browser automation tools.
- The authors used PyAutoGUI to control the mouse.
- The environment was not connected through a proxy or VPN.
- It was not logged into a Google account.
- Tor produced low scores in their observations.
- A connected Google account increased scores compared with no Google account, according to their experiments.

The evidence is direct but narrow: it tests one reCAPTCHA v3 interaction setup in 2019, not a broad range of sites, actions, or modern anti-bot deployments.

## Signals or techniques mentioned

- reCAPTCHA v3 risk score
- mouse movement path
- grid-world formulation
- Markov Decision Process
- REINFORCE policy-gradient algorithm
- up / left / right / down action space
- randomised starting position
- grid cell size
- divide-and-conquer grid decomposition
- PyAutoGUI mouse control
- Selenium automation artefacts
- WebDriver automated headers
- browser automation detection
- Tor / proxy impact
- Google account context impact
- screen resolution sensitivity
- reCAPTCHA score threshold of 0.9

## Threat types covered

The paper is not organised around OWASP Automated Threat categories.

The direct threat type is CAPTCHA / human-verification bypass, specifically reCAPTCHA v3 score manipulation through learned mouse movement.

Relevant project/OAT mappings:
- cross-cutting mitigation bypass rather than a single OAT category
- relevant to any automated threat that relies on passing reCAPTCHA or similar behavioural risk scoring
- indirectly relevant to credential stuffing, account creation, scraping, scalping, carding, and spam where reCAPTCHA is used as a control

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates an automated agent trying to obtain a high reCAPTCHA v3 score by producing mouse movement that looks sufficiently human to the scoring system. It is useful because it demonstrates that behavioural risk scoring itself can become an adversarial learning target.

- **What does it fail to represent?**  
  It does not evaluate full web-abuse workflows such as login, checkout, scraping, account creation, or payment abuse. It only models movement to a reCAPTCHA checkbox, not broader human browsing behaviour. It does not test against modern reCAPTCHA behaviour after 2019, Enterprise configurations, site-specific score calibration, repeated activity across pages, account reputation, browser fingerprinting at current maturity, residential proxy use, cloud browser automation, or commercial bot-management stacks. The method relies on a specific experimental setup and cannot be assumed to work unchanged today.

- **What additional evidence would be needed to go further?**  
  Current replication against modern reCAPTCHA v3/Enterprise deployments; tests across multiple websites and site actions; evaluation with realistic browser fingerprints, cookies, accounts, IP reputation, and repeated sessions; integration into real browser automation performing abuse workflows; comparison with modern Playwright/Puppeteer/Chrome DevTools approaches; measurement of false positives, lockouts, score drift, and site-specific thresholds.

## What it cannot show

- It cannot show that reCAPTCHA v3 is generally broken in current deployments.
- It cannot show that this method works today without replication.
- It cannot show success against reCAPTCHA Enterprise or site-specific score policies.
- It cannot show production-scale feasibility for real bot campaigns.
- It cannot show bypass of complete bot-management stacks that combine reCAPTCHA with fingerprints, IP reputation, server-side behaviour, account reputation, or graph signals.
- It cannot show that RL is necessary; the task may partly reflect path-smoothing or movement-resolution effects rather than deep strategic behaviour.
- It cannot establish prevalence or business impact.

## Project impact

- Useful academic source for the project’s CAPTCHA / behavioural-risk evasion section.
- Supports the argument that passive behavioural scoring can be attacked, not just traditional image/audio CAPTCHA.
- Provides a bridge between reCAPTCHA evasion and the Iliou RL evasion paper: Akrout applies RL to mouse movement / reCAPTCHA scoring, while Iliou et al. apply RL to web-log browsing behaviour.
- Useful for explaining why browser automation artefacts matter: the authors’ failed Selenium attempt is a concrete example of automation fingerprints affecting scores.
- Should be cited cautiously because it is a 2019 proof-of-concept against one setup, not current general evidence.
- Reinforces the project’s “framing distance” point: an impressive success percentage in a narrow adversarial setup should not be treated as a general statement about modern bot-defence effectiveness.
