# Berke et al. (2025) - How Unique is Whose Web Browser?

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Berke, A., Bacis, E., Ghazi, B., Kamath, P., Kumar, R., Lassonde, R., Manurangsi, P., & Syed, U. (2025). *How Unique is Whose Web Browser? The Role of Demographics in Browser Fingerprinting among US Users*. Proceedings on Privacy Enhancing Technologies, 2025(1), 720–758. https://doi.org/10.56553/popets-2025-0038
- **Source URL or path**: `SRC-067-berke-2025-how-unique-whose-web-browser-demographics.pdf`
- **Publication venue**: Proceedings on Privacy Enhancing Technologies.
- **Publication year**: 2025.
- **Category**: academic
- **Evidence basis**: empirical-measurement / dataset paper
- **Operational proximity**: measured - original browser-attribute and demographic dataset collected from US participants; not observed malicious bot activity.
- **Tags**: browser-fingerprinting, demographics, privacy, tracking, passive-fingerprinting, user-agent, languages, webgl, screen-resolution, device-memory, entropy, anonymity-set, demographic-inference, open-data, prolific, fingerprintjs

## Relationship to Laperdrix / AmIUnique

This is best treated as a **successor/complement** to the Laperdrix / AmIUnique browser-fingerprinting line, not a duplicate.

The paper explicitly positions itself after Eckersley/Panopticlick, Laperdrix/AmIUnique, and Gómez-Boix. Its key contribution is not merely “browser fingerprints can be unique”; that is already established. Its contribution is that fingerprinting risk differs by demographic group, and browser attributes can themselves leak demographic information.

## What it claims

- Browser fingerprinting can identify and track users across websites without cookies by combining browser/device/configuration attributes.
- Prior major fingerprinting studies were important but limited because their user-level datasets were not publicly available and did not include demographics.
- The authors provide a dataset linking browser attributes, demographics, and survey responses from consenting US participants.
- Fingerprinting risk is not evenly distributed across demographic groups.
- Lower-income users and older users show greater overall fingerprinting risk in this dataset.
- User demographics such as gender, age, income, race, and Hispanic origin can be inferred from browser attributes commonly used for fingerprinting.
- More than 70% of participants said they were concerned about fingerprinting/tracking, but only 43% said they understood how it works.
- Showing participants the browser data being requested made them less likely to share it.

## What evidence it provides

- Original survey/measurement dataset:
  - 12,461 total survey participants.
  - 8,400 participants shared browser attribute data.
  - US residents, age 18+, recruited via Prolific.
  - Data collected in December 2023.
- Browser attributes collected using JavaScript, including FingerprintJS open-license v3 plus additional custom JavaScript.
- The paper analyses 13 browser attributes, including:
  - User-Agent;
  - Languages;
  - Timezone;
  - Screen resolution;
  - Platform;
  - Touch points;
  - Hardware concurrency;
  - Device memory;
  - WebGL vendor/renderer fields;
  - combined fingerprint hash.
- The overall fingerprint was unique for approximately 60% of users in the dataset.
- The paper compares risks across demographic groups using:
  - percent unique;
  - average anonymity set size;
  - entropy;
  - logistic regression;
  - simple machine-learning demographic prediction;
  - mutual information.

## Main quantitative details

| Measure | Reported value |
|---|---:|
| Total survey participants | 12,461 |
| Participants sharing browser data | 8,400 |
| Share rate | 67.4% |
| Share rate when shown browser data | 65.8% |
| Share rate when not shown browser data | 69.1% |
| Participants saying they understand fingerprinting | 43% |
| Participants concerned about fingerprinting/tracking | >70% |
| Unique combined fingerprint | ~60% |
| User-Agent distinct values | 434 |
| Screen-resolution distinct values | 572 |
| WebGL Unmasked Renderer distinct values | 654 |
| Combined fingerprint distinct values | 5,973 |
| Combined fingerprint entropy | 12.101 |

## Signals or techniques mentioned

- Browser fingerprinting
- Passive fingerprinting
- Active JavaScript fingerprinting
- User-Agent header
- Languages / Accept-Language-like signal
- Timezone
- Screen resolution
- Platform
- Touch points
- Hardware concurrency
- Device memory
- WebGL vendor
- WebGL unmasked vendor
- WebGL renderer
- WebGL unmasked renderer
- Plugins and fonts, collected but excluded from main analysis because browser changes have reduced their usefulness
- Entropy
- Anonymity set size
- Percent unique
- Mutual information
- Demographic inference from device/browser signals

## Threat types or risk types covered

- Cross-site tracking without cookies
- Passive server-side fingerprinting
- Active JavaScript-based fingerprinting
- Re-identification risk
- Demographic inference
- Potential discriminatory targeting or ad-delivery bias
- Unequal privacy risk across demographic groups

## What is strong

- Strong empirical update to the classic fingerprinting literature.
- Strong bridge between browser-fingerprinting privacy work and bot-detection privacy/governance work.
- Useful evidence that fingerprinting signals can carry demographic information, not just uniqueness/tracking information.
- Important correction to the older literature: estimates of fingerprinting risk can be biased if the participant population is demographically skewed.
- Useful for the project’s “fingerprinting is dual-use” point: the same signals can support bot detection, tracking, demographic inference, and potentially discriminatory targeting.
- Good source for explaining why “reduce entropy” alone may not be enough; an API can reduce uniqueness while still grouping users by demographics.

## What is weak or limited

- US-only sample; findings may not generalise to other countries.
- Prolific crowdworker sample, not a fully representative population sample.
- The sample overrepresents younger participants and underrepresents older users, Hispanic participants, and high-income households relative to US population benchmarks.
- Data collection was in December 2023; browser/device distributions change over time.
- The analysis uses a selected subset of attributes and does not represent every signal available to modern commercial fingerprinting or bot-detection systems.
- FingerprintJS open-license v3 was used rather than newer closed versions, which may limit comparability with current commercial fingerprinting.
- It does not study malicious actors, bot traffic, or anti-bot detection directly.
- It identifies risk but does not test mitigation strategies.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** The privacy and identifiability risk of browser/device attributes that are also used in bot detection, fraud detection, and anti-abuse systems.
- **What does it fail to represent?** It is not evidence of automated abuse, credential stuffing, scraping, ticket bots, or bot-management effectiveness.
- **What additional evidence would be needed to go further?** Operational bot-detection logs, controlled automation experiments, commercial fingerprinting studies, or longitudinal data showing how fingerprints persist and change over time.

## What it cannot show

- It cannot show that fingerprinting is being used maliciously in a particular system.
- It cannot show bot prevalence.
- It cannot show detection performance against bots.
- It cannot prove that a specific browser API change will fix demographic inference risk.
- It cannot establish GDPR/ePrivacy/AI Act compliance by itself.
- It cannot replace Laperdrix/AmIUnique for historical comparison, but it updates that line with demographic data.

## Project impact

Use this as a **core browser-fingerprinting foundation source**. It should sit alongside Laperdrix/AmIUnique, Eckersley/Panopticlick, Gómez-Boix, MDN User-Agent, and the Martínez Llamas et al. bot-detection/privacy review.

Best fit in the project:

- Foundations: what browser fingerprinting is.
- Privacy/governance: fingerprinting signals can be personal, unequal, and demographically informative.
- Detection methods: browser/device signals are attractive for bot detection, but not privacy-neutral.
- Limitations section: public fingerprinting datasets and volunteer samples can have demographic bias.

Do **not** use this as evidence of bot abuse or attack prevalence.

## Best placement in the evidence register

- Primary section: **Academic and research literature**
- Secondary section: **Browser fingerprinting foundations**
- Cross-links:
  - Laperdrix / AmIUnique;
  - Eckersley / Panopticlick;
  - Gómez-Boix;
  - MDN User-Agent;
  - Martínez Llamas et al. GDPR/AI Act bot-detection review;
  - Cloudflare Detection IDs / bot-detection engines;
  - Niespodd browser-fingerprinting GitHub entry.

## Possible register row

| Field | Value |
|---|---|
| Register id | `berke-2025-how-unique-whose-web-browser-demographics` |
| Title | *How Unique is Whose Web Browser? The Role of Demographics in Browser Fingerprinting among US Users* |
| Category | academic |
| Evidence basis | empirical-measurement / dataset paper |
| Operational proximity | measured |
| Tags | browser-fingerprinting; demographics; privacy; tracking; passive-fingerprinting; user-agent; languages; webgl; screen-resolution; device-memory; entropy; anonymity-set; demographic-inference; open-data; prolific; fingerprintjs |
| Project use | Empirical foundation for browser fingerprinting and unequal privacy risk across demographic groups |
| Main caution | Not bot-abuse evidence; US Prolific sample and Dec 2023 browser/device snapshot limit generalisability |
