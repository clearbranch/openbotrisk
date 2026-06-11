# Web Bot Detection Evasion Using Generative Adversarial Networks — Iliou et al. 2021

## Bibliographic

- **Citation**: Iliou, C., Kostoulas, T., Tsikrika, T., Katos, V., Vrochidis, S., & Kompatsiaris, I. (2021). Web Bot Detection Evasion Using Generative Adversarial Networks. *IEEE International Conference on Cyber Security and Resilience (CSR 2021)*. IEEE.
- **Source URL or path**: SRC-013-iliou-2021-csr-web-bot-detection-evasion-gans.pdf
- **Date accessed**: 2026-05-31
- **Category**: academic
- **Tags**: advanced-bots, evasion, GAN, DCGAN, mouse-biometrics, touchscreen-biometrics, behavioural, CNN, adversarial-evaluation, humanlike-behaviour, public-data-limits

## What it claims

- Mouse-movement and touchscreen-trajectory based bot detection can be effective, but bots may evade these defences by generating humanlike trajectories.
- Web bots can use Generative Adversarial Networks (GANs) to generate images of mouse or touchscreen trajectories similar to human trajectories.
- GAN-generated trajectories can be used by bots to reduce the effectiveness of detection systems that classify trajectory images with CNNs.
- The evasion approach remains effective even when the web server is aware of the attack method and uses the same GAN architecture/configuration in training.
- Mouse trajectories from web browsing are harder to model than constrained touchscreen digit-drawing trajectories because web browsing behaviour varies more across users.
- GAN-generated outputs tend to be simpler trajectories, which may limit their usefulness for complex real-world browser actions.
- The result supports the broader claim that bot detection should be evaluated against adaptive adversaries, not only against fixed heuristic bots.

## What evidence it provides

The paper evaluates GAN-based evasion against a CNN-based behavioural detector.

The detector represents mouse or touchscreen trajectories as images. Mouse/touch points are collected as coordinate-time sequences, converted into two-dimensional matrices, normalised, and fed into a CNN classifier. The paper uses a simple CNN architecture with convolution, max-pooling, flattening, and dense softmax layers.

The evasive bots use a Deep Convolutional Generative Adversarial Network (DCGAN) to generate trajectory images. The generator maps random latent vectors into new trajectory images; the discriminator tries to distinguish real human trajectory images from generated ones. The paper uses TensorFlow and Keras for the CNN and GAN implementation.

The evaluation uses two datasets:
- **Web dataset**: human browsing data from 27 subjects browsing a controlled web server with 110 Wikipedia-derived pages across 11 topics. Each subject created two sessions of 15-20 minutes. The dataset is available upon request.
- **HuMIdb dataset**: touchscreen interaction data from more than 600 users, with this paper using the task where users drew digits 0-9 on mobile devices.

The datasets are split into three user-disjoint sets so that the web server and evasive bots train on different human behaviours. Images are rescaled to 56x56, and experiments are repeated five times to account for GPU randomness.

The detection framework performs very well when trained/tested against GAN-generated images from its own setup:
- Web dataset average balanced accuracy: 0.985
- HuMIdb average balanced accuracy: 0.996
- Web dataset average recall: 0.999
- HuMIdb average recall: 0.995

Against evasive bots trained on different human images, detection recall drops:
- Web dataset average recall: 0.452
- HuMIdb average recall: 0.937

This means the detector still catches many generated touchscreen digit traces, but performs much worse on web mouse trajectories. The authors interpret this as evidence that GAN-based trajectory generation can make bots more evasive, especially for web browsing mouse behaviour.

The paper also includes qualitative examples of human and GAN-generated trajectory images. The examples suggest that generated web mouse trajectories are relatively simple compared with the full range of human movement.

## Signals or techniques mentioned

- Mouse trajectory coordinates
- Touchscreen trajectory coordinates
- Timestamped trajectory sequences
- Per-point time delta / dwell value
- Trajectory images / two-dimensional matrices
- JavaScript-based trajectory collection
- CNN-based bot detection
- DCGAN-based evasion
- Generator and discriminator networks
- Latent vectors sampled from a Gaussian distribution
- TensorFlow
- Keras
- Pillow image rescaling
- 56x56 downsampled trajectory images
- Selenium and browser automation as background
- Browser fingerprinting as background
- CAPTCHA / reCAPTCHA as background
- Browser-like fingerprint evasion as background
- Humanlike browsing behaviour
- GAN-generated mouse movements
- GAN-generated touchscreen movements

## Threat types covered

The paper is not organised by OWASP OAT category.

The experimental focus is behavioural evasion by advanced bots, especially:
- scraping / content harvesting bots that crawl web servers while trying to appear human
- mobile web bots attempting to pass human-interaction style checks based on touchscreen trajectories

Relevant project/OAT mappings:
- closest to OWASP OAT-011 Scraping for the web crawling scenario
- related to CAPTCHA / human-verification bypass, although the paper is not about solving conventional image CAPTCHA challenges
- potentially relevant to scalping, credential stuffing, carding, and account abuse only insofar as those attacks may use browser automation that needs humanlike interaction traces

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  The paper approximates an adaptive adversary trying to evade behavioural bot detection by synthesising humanlike mouse or touch trajectories. It is useful for the project because it turns behavioural detection from a static classification problem into an adversarial problem: once defenders use mouse/touch trajectories, bot operators may try to generate similar traces.

- **What does it fail to represent?**  
  The evaluation is controlled. It does not test live adversaries, production traffic, transactional web flows, or modern bot infrastructure. The web dataset is based on users browsing Wikipedia-derived pages, not login, checkout, booking, account creation, product-drop, or payment flows. The bots generate trajectory images, but the paper does not fully demonstrate operational integration into a browser automation stack performing arbitrary web tasks. The generated web trajectories appear relatively simple, and the authors note this may be a limitation for complex actions. The setup does not include residential proxies, anti-detect browsers, Playwright/Puppeteer stealth tooling, browser extensions, cloud browsers, mobile-app automation at production scale, or AI browser agents.

- **What additional evidence would be needed to go further?**  
  Evidence from bots that integrate generated trajectories into actual browser sessions; tests against modern behavioural detectors using production-style data; evaluation on realistic transactional flows; adversarial testing where the detector and generator update over time; comparison with RL-based evasion and hand-coded humanlike movement; measurement of detection latency, false positives, and cost; testing against mobile-app bot defences and API-backed flows.

## What it cannot show

- It cannot show that GAN-generated trajectories are sufficient to evade commercial bot-management systems.
- It cannot show that generated images translate cleanly into realistic browser or mobile interaction events during real task execution.
- It cannot show production performance under realistic user diversity, traffic volumes, or adversarial pressure.
- It cannot show that the technique generalises to modern browser-native automation, anti-detect browsers, cloud browser services, browser extensions, or AI browser agents.
- It cannot show that mouse/touchscreen behavioural detection is broken; it shows that one class of behavioural detector can be weakened in a controlled adversarial setup.
- It cannot show prevalence: there is no evidence here that real bot operators were using this exact GAN approach in the wild.
- It cannot show business impact or operational detectability across bot categories such as credential stuffing, scalping, account creation, or carding.

## Project impact

- Provides a focused academic source for the project’s evasion/adversarial-pressure framing.
- Supports the claim that behavioural bot detection should not be assessed only against simple heuristic bots.
- Complements Iliou et al. 2021 on web logs + mouse behavioural biometrics by testing an evasion path against mouse/touch trajectory detection.
- Useful for the Technical territory section on behavioural biometrics and the limitations of mouse/touch-based detection.
- Useful for a methodology note on adversarial evaluation: detection performance should be tested against adaptive generators, not only held-out static examples.
- Should be cited carefully: it demonstrates possible evasion in a controlled setup, not observed industrial-scale evasion.
- Reinforces the project’s public-data-limits point: academic adversarial experiments can expose mechanisms, but they do not replace production telemetry or modern tooling evaluation.
