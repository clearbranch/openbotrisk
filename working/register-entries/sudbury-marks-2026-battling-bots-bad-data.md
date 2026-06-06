# Sudbury & Marks (2026) - Battling bots and bad data

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Sudbury, A. W., & Marks, M. (2026). *Battling bots and bad data: enhancing data quality in online surveys*. Quality & Quantity. https://doi.org/10.1007/s11135-026-02749-3
- **Source URL or path**: `Battling_bots_and_bad_data_enhancing_data_quality_.pdf`
- **Publication status**: peer-reviewed journal article. Received 14 April 2025; accepted 28 March 2026.
- **Category**: academic
- **Evidence basis**: empirical-methods / review-informed case study
- **Operational proximity**: measured - applies bot and attention-check controls to an online survey and reports eliminations; not direct evidence of malicious web abuse against commercial sites.
- **Tags**: online-surveys, bots, bad-data, captcha, recaptcha, attention-checks, qualtrics, open-ended-questions, speed-checks, ip-checks, data-quality, survey-fraud

## What it claims

- Online survey delivery increases exposure to bots and inattentive respondents compared with controlled paper, phone, or lab settings.
- Bots can compromise online research, especially where public links and monetary incentives are involved.
- More sophisticated bots may slow completion, scroll, attempt CAPTCHA recognition, and avoid hidden questions.
- No single bot-detection method is sufficient; researchers should combine platform controls, survey design, and post-survey evaluation.
- Attention checks and consistency checks are also necessary because bad data can come from inattentive humans, not only bots.

## What evidence it provides

- The paper uses the authors’ own 2021 Qualtrics survey on vaccination and risk aversion as a case study.
- It used multiple layers: Qualtrics platform screening, CAPTCHA/reCAPTCHA, an open-ended image question, demographic quota screens, attention checks embedded in an incentivised risk task, consistency checks, duplicate/IP-related checks, and speed checks.
- From 4,453 respondents who consented and entered the survey, only 711 were retained as quality responses, or 15.97%.
- Bot-detection questions eliminated a relatively small share: 112 failed/did not continue after CAPTCHA and 43 failed the open-ended ball-count bot check.
- The main attention check eliminated more respondents: 1,208 failed the incentivised risk-task attention checks, or 27.13% of respondents who entered the relevant stage.
- Post-survey analysis eliminated 49 completed observations for issues including duplicate responses, inconsistent answers, missing/invalid data, Qualtrics-related flags, and speeding.
- Figure 1 is useful because it visualises the attrition pathway from consent to final quality completes.
- Figures 2 and 3 show the actual CAPTCHA and ball-count bot-check used.
- Table 3 gives post-survey elimination reasons, and Table 4 shows correlations between error flags.

## Signals or techniques mentioned

- CAPTCHA / reCAPTCHA
- cursor movement and typing-behaviour scoring
- open-ended bot-detection questions
- attention checks
- consistency checks
- demographic cross-checks
- quota screening
- speed checks
- page-time / completion-time checks
- IP and location checks
- duplicate response checks
- cultural checks
- platform-level fraud controls
- Qualtrics profile consistency checks

## Threat types covered

- bot responses in paid online surveys
- low-quality human responses
- insufficient effort responding
- duplicate participation
- quota-gaming / misrepresented demographic responses
- public-link survey fraud
- survey data contamination

## Main quantitative details

| Measure | Reported value |
|---|---:|
| Survey clicks | 5,748 |
| Respondents entering after consent | 4,453 in main flow/figure |
| Failed CAPTCHA / did not continue | 112 / 2.51% |
| Failed ball-count bot check | 43 / 0.97% |
| Eliminated by quota / failed to complete demographic screen | 1,995 / 44.8% |
| Failed risk-task attention checks | 1,208 / 27.13% |
| Eliminated in post-survey analysis | 49 / 1.1% |
| Failed to complete after quota | 335 / 7.52% |
| Final retained quality completes | 711 / 15.97% |

## What is strong

- Strong for the survey-research strand: it gives concrete evidence that online survey data can be heavily degraded without layered quality controls.
- Strong for showing that “bot problem” and “bad data problem” overlap but are not identical.
- Useful evidence that CAPTCHA alone is weak as a complete quality-control strategy.
- Useful evidence that post-hoc checks can detect problems missed by front-end bot screens.
- Useful as a review-type bridge because it cites several relevant studies on MTurk quality problems, bot detection, CAPTCHA limitations, speed checks, IP/location checks, and attention checks.

## What is weak or limited

- The survey was not designed as an experiment comparing detection methods, order effects, or alternative combinations. The authors explicitly note they evaluate a layered design rather than experimentally varying the checks.
- The survey dates from 2021, so the bot environment may differ from 2026.
- It is not a commercial anti-bot-web-defence paper; the domain is online survey quality.
- It does not prove that each eliminated respondent was a bot or malicious actor.
- Attention-check failures may reflect misunderstanding or task difficulty as well as inattentiveness.
- The article contains a small apparent inconsistency: one section says 4,458 gave consent, while the figure/main reported base is 4,453.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** Automated and low-quality participation in incentivised online surveys, especially where rewards create a motive to complete forms at scale.
- **What does it fail to represent?** It does not represent scraper activity against protected websites, credential stuffing, ticket bots, AI agents, or bot-management vendor telemetry.
- **What additional evidence would be needed to go further?** Platform telemetry, controlled experiments comparing check types, newer 2026 data, or studies directly measuring bot automation in survey panels.

## What it cannot show

- It cannot show internet-wide bot prevalence.
- It cannot show effectiveness of Cloudflare/HUMAN/DataDome-style bot-management systems.
- It cannot prove detected bad responses were all bots.
- It cannot establish attacker tooling, business models, or intent.
- It cannot validate CAPTCHA/reCAPTCHA performance outside this survey context.

## Project impact

Use this as a **review-informed academic case study** for the “bad data / survey fraud / form automation” part of the project. It strengthens the argument that bot-like automation is not only a cybersecurity problem: it can also damage research data quality. It also supports a layered-defence framing: platform controls, survey design, and post-survey checks all contribute, but none is sufficient alone.

## Best placement in the evidence register

- Evidence section: **Survey/data-quality abuse**
- Secondary section: **Detection methods and layered controls**
- Do not place as main evidence for commercial web scraping, credential stuffing, ticket bots, or AI-agent traffic.

## Possible register row

| Field | Value |
|---|---|
| Register id | `sudbury-marks-2026-battling-bots-bad-data` |
| Title | *Battling bots and bad data: enhancing data quality in online surveys* |
| Category | academic |
| Evidence basis | empirical-methods / review-informed case study |
| Operational proximity | measured |
| Tags | online-surveys; bots; bad-data; captcha; recaptcha; attention-checks; qualtrics; open-ended-questions; speed-checks; ip-checks; data-quality; survey-fraud |
| Project use | Evidence that bots and inattentive respondents degrade online survey data and require layered quality controls |
| Main caution | Survey-quality domain; not direct evidence of web-scraping abuse or commercial bot-defence efficacy |
