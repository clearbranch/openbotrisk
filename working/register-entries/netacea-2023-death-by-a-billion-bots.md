# Death by a Billion Bots: The Accumulating Business Cost of Malicious Automation — Netacea 2023

## Bibliographic

- **Citation**: Netacea. (2023). *Death by a Billion Bots: The Accumulating Business Cost of Malicious Automation*. Netacea report.
- **Source URL or path**: `SRC-007-netacea-2023-death-by-a-billion-bots.pdf`
- **Date accessed**: 2026-05-31
- **Category**: vendor
- **Tags**: vendor, survey, business-impact, malicious-automation, credential-stuffing, scraping, scalping, sniping, fake-account-creation, gift-card-fraud, api-abuse, mobile-apps, bot-management, detection-lag, threat-surface

## What it claims

- Malicious automation is a growing business problem that targets legitimate online flows such as checkouts, logins, inventory searches, gift card redemptions, websites, APIs, and mobile applications.
- The report claims that the annual cost of bots is approximately $85.6 million per attacked company per year, based on surveyed organisations' estimates of online revenue loss.
- Netacea reports that surveyed businesses perceive Russia and China as major origin locations for malicious automated attacks, with 53% of attacks said to originate from Russia or China.
- The report claims that attack surfaces are broadening: mobile applications, websites, and APIs are all targeted, with API targeting increasing fastest since 2020.
- Netacea reports that 99% of companies that detected automated attacks said attack volumes had increased over the last year.
- The top three attack types reported are sniping, credential stuffing/account checking, and scraping.
- The report claims malicious automation has an attritional business impact, unlike traditional high-profile cyber incidents: losses accumulate through revenue leakage, customer churn, reputational damage, infrastructure costs, and operational burden.
- The report claims detection and response are slow: the average time to realise a malicious automated attack is around four months, with nearly all organisations taking more than a month to respond.
- Netacea argues that bot risk should receive greater board-level and strategic attention because its cumulative business impact is often hidden across departments.
- The report argues that businesses need more intelligent AI-driven bot defences, but this claim is tied to Netacea's commercial positioning.

## What evidence it provides

- The report is based on a survey of 440 executive stakeholders across 10 sectors in the UK and US. The surveyed enterprises are described as having average online revenue of $1.9 billion.
- It provides survey percentages by attack origin, attack surface, attack type, financial impact, detection time, and sector.
- It gives trend comparisons for 2020, 2021, and 2022 for several attack types and surfaces, but the report does not expose the underlying dataset, survey instrument, sampling frame, weighting, or raw responses.
- It uses Netacea's BLADE framework definitions for several attack types, including sniper bots, credential stuffing, scraping, fake account creation, gift card fraud, and scalping.
- It includes expert commentary from Netacea staff and an external academic commentator, but these are interpretive sections rather than independent empirical tests.
- It cites external reports for contextual comparison with ransomware payments, breach costs, dwell time, and cyber/geopolitical claims, but the core bot-impact figures are based on Netacea-commissioned survey evidence.
- The report does not provide technical detection experiments, model performance, telemetry samples, or independently verifiable bot-classification methodology.

## Signals or techniques mentioned

- Attack surfaces: websites, mobile applications, APIs.
- Business flows: checkouts, logins, inventory searches, gift card redemptions, account signup, auctions, payment and stored-value validation.
- Threat categories: sniping, credential stuffing/account checking, scraping, fake account creation, gift card cracking/fraud, scalping.
- Infrastructure and origin concepts: geographic origin of malicious traffic, infrastructure located in Russia, China, Vietnam, Europe, the US, UK, other Americas, Africa, and the Middle East.
- Detection/response concepts: average time to realise an attack, response lag, detection gaps, business impact measurement.
- No concrete detection signals are described in depth. The report does not meaningfully discuss TLS fingerprints, browser fingerprints, header order, JavaScript probes, behavioural biometrics, proxy detection, mouse dynamics, graph clustering, or specific machine-learning models.
- The final product page claims Netacea combines edge-computed analysis, detection, response, and threat intelligence, but this is high-level product language rather than technical evidence.

## Threat types covered

The report maps well onto several OWASP Automated Threats / business-logic abuse categories, though it uses Netacea/BLADE naming rather than OWASP OAT naming throughout.

- Credential stuffing / account checking — close to OWASP OAT-008 Credential Stuffing and broader account takeover.
- Scraping — close to OWASP OAT-011 Scraping.
- Scalping — close to OWASP OAT-005 Scalping.
- Sniping — time-based bidding or last-action automation; related to expediting and business-logic abuse.
- Fake account creation — close to OWASP OAT-019 Account Creation.
- Gift card cracking/fraud — close to carding / token or stored-value enumeration, related to OWASP OAT-001 Carding and OAT-style value validation attacks.
- API abuse — treated as an expanding surface rather than a single attack type.
- Mobile-app abuse — treated as an expanding surface rather than a single attack type.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  This source approximates how a bot-management vendor frames malicious automation as a business-risk category for large online enterprises. It is useful for understanding vendor-side claims about business impact, perceived attack-type prevalence, affected surfaces, detection lag, and the translation of bot activity into business language. It is especially relevant to the project's recurring booking/transactional-system example because it focuses on legitimate web-facing flows being abused at scale: login, checkout, account creation, gift cards, stock/inventory lookup, and bidding/timing behaviours.

- **What does it fail to represent?**  
  It does not represent independent measurement of bot prevalence or detection effectiveness. The evidence is survey-based and vendor-produced, not a public telemetry dataset or reproducible technical study. Respondents' estimates of revenue loss, origin location, attack type, and detection lag may reflect internal classification practices, commercial tooling, recall bias, and sector-specific assumptions. The report does not explain how respondents distinguished bot types, how origin was attributed through proxies or compromised infrastructure, or how estimated financial losses were calculated. It also drifts into geopolitical interpretation and board-level risk framing, which are less central to the project's methods-first scope.

- **What additional evidence would be needed to go further?**  
  To use the claims more strongly, the project would need access to the survey questionnaire, sampling and weighting details, raw or aggregated response tables, definitions supplied to respondents, and independent corroboration from non-vendor sources. For technical claims, it would need telemetry-based studies showing how bot attacks were identified, what signals were used, how false positives were handled, and how attacks were mapped to business losses. For origin-location claims, it would need methodology that accounts for proxies, cloud hosting, residential proxy networks, compromised devices, and attribution uncertainty.

## What it cannot show

- It cannot show the true prevalence of malicious automation across the wider web, because it surveys a selected population of large UK and US enterprises.
- It cannot show that bots cost the average company $85.6 million per year in a generalisable sense; this is a survey-derived estimate for the sampled organisations and depends on self-reported online revenue impact.
- It cannot show that Russia, China, or Vietnam are the real controlling locations of attackers. At best, it reports perceived or detected origin infrastructure, which may be affected by proxying, hosting location, residential networks, and compromised devices.
- It cannot show that Netacea's product or AI-driven defences achieve the claimed performance; the report does not provide an independent product evaluation.
- It cannot show which detection signals work, because it does not describe the technical detection pipeline in enough detail.
- It cannot show how malicious automation differs from broader cyber incidents at a technical level; its traditional-cyber comparison is a business-risk framing rather than a technical taxonomy.
- It should not be used as evidence for named threat actors, geopolitical attribution, or criminal economics; those areas sit outside the project's core methods-focused scope.

## Project impact

- Useful as a vendor/industry evidence source for the Background and landscape section: it shows how bot-management vendors translate malicious automation into business impact, customer satisfaction, detection lag, and board-level risk language.
- Provides a survey-based vendor reference for threat categories relevant to the project: credential stuffing, scraping, scalping, sniping, fake account creation, gift card fraud, API abuse, and mobile-app abuse.
- Supports the project's claim that bot abuse is not just a website problem: Netacea frames mobile applications and APIs as major and growing attack surfaces.
- Supports the project's public-data-limits theme: the report makes strong claims based on private/vendor-side survey evidence, but the underlying telemetry and classification methods are not open.
- Should be cited cautiously and explicitly as vendor survey evidence, not independent prevalence evidence or detection-performance evidence.
- The origin-location and geopolitical interpretation should either be omitted from site synthesis or heavily caveated, because the project's scope excludes named actors and broader geopolitical cyber framing.
- The most reusable part is the business-framing contrast: malicious automation often produces cumulative, distributed losses rather than a single visible incident. This is useful for explaining why bot abuse can be operationally important yet hard to measure.
- This source helps define what vendor reports are good for in the register: public evidence of industry framing and claimed business impact, not proof of technical effectiveness.
