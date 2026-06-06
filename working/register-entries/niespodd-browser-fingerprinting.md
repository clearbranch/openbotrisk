# Avoiding bot detection: How to scrape the web without getting blocked? / browser-fingerprinting

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: partial-to-full — the GitHub repository landing page and raw README were accessible; the repository's browser-fingerprinting tester page loaded but did not expose useful parsed text in this environment. Linked third-party tools, services, and test pages were not individually extracted.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: niespodd. Undated / ongoing. *Avoiding bot detection: How to scrape the web without getting blocked?* / *browser-fingerprinting*. GitHub repository. Accessed 2026-06-06.
- **Source URL or path**: `https://github.com/niespodd/browser-fingerprinting`; raw README accessed at `https://raw.githubusercontent.com/niespodd/browser-fingerprinting/main/README.md`; associated tester page: `https://niespodd.github.io/browser-fingerprinting/`.
- **Date accessed**: 2026-06-06
- **Category**: threat-surface
- **Evidence basis**: tooling-readme
- **Operational proximity**: claimed — the README is mostly a curated anti-detection / scraping-evasion guide and tooling catalogue. It says its technical findings are based on observations from running scraping scripts for several months against major anti-bot vendors, but it does not provide raw traffic, test design, target details, denominators, success rates, or independent validation. For tool existence, it supports capability; for effectiveness against real systems, it is maintainer-claimed.
- **Tags**: threat-surface, browser-fingerprinting, fingerprinting, anti-detection, scraper-side, evasion, headless-browser, puppeteer, playwright, selenium, stealth-browser, residential-proxy, proxy-rotation, captcha, tls, ja3, ja4, behavioural, webgl, fonts, client-hints, webdriver, tooling-catalogue, vendor-landscape, dual-use

## What it claims

- The source presents anti-bot systems as having evolved from simple IP/geolocation controls toward more advanced browser-parameter and behavioural analysis.
- It claims that scraping protected sites has become more difficult and costly, but remains possible.
- It organises scraping and anti-detection needs by use case, including short-lived unauthenticated scraping, geo-restricted access, long-lived authenticated sessions, JavaScript-based detection, browser-fingerprinting-based detection, target-specific detection, and simple custom defences on smaller sites.
- It claims short-lived, unauthenticated scraping can often rely on rotating IP pools, while long-lived authenticated automation needs more stable infrastructure and repeatable browser fingerprints.
- It claims JavaScript-based detection can sometimes be bypassed with popular stealth/evasion libraries, but that more advanced browser-fingerprinting systems require a more complete, natural-looking fingerprint surface.
- It claims some sites use target-specific detection surfaces, creating a market for specialised bot software rather than generic scrapers.
- It lists proxy providers, scraping-as-a-service platforms, CAPTCHA-solving services, anti-bot vendors, stealth browsers, automation frameworks, stealth libraries, and fingerprint test pages as part of the practical anti-detection ecosystem.
- It says some stealth-browser or anti-detect software may contain malware and should be used with caution.
- It claims its technical findings are based on several months of running web-scraping scripts against websites protected by major anti-bot solution vendors.
- It describes `puppeteer-extra-plugin-stealth` as helpful for some browser-exposed signals, but incomplete against deeper or cross-layer signals.
- It claims that some automation leaks cannot be reliably hidden using JavaScript-level patches alone and that deeper approaches patch the automation library, the browser-debugging transport, or the browser binary.
- It identifies a range of detection surfaces that can expose automation or fingerprint inconsistency, including client hints, `navigator` and `window` properties, native browser extensions, host operating-system consistency, browser dimensions, worker-thread behaviour, WebGL, WebRTC, high-resolution timing, behavioural detection, font rendering, network latency, battery APIs, and mobile sensors.
- It claims custom browser profiles and anti-detect browsers can create inconsistencies when their browser builds lag real browser releases or when profile settings are misconfigured.
- It argues that anti-bot tools mainly reduce cheap or unspecialised bot traffic rather than making scraping impossible.
- It separates anti-bot detection into binary detection of obvious automation and traffic clustering of more advanced traffic that tries to look human.
- It argues that blocking advanced bot-like traffic is risky when bots mimic real users, because false positives may block legitimate visitors.
- It treats CAPTCHA and gateway controls as friction layers that can be worked around through external solving services, rather than as definitive separation of humans and bots.

## What evidence it provides

- The source itself is evidence that a public, curated scraper-side anti-detection knowledge base exists and is popular enough to have a visible GitHub footprint. The GitHub page showed roughly 5k stars, hundreds of forks, and open issues during extraction. These are adoption signals, not evidence of correctness.
- The README provides a structured taxonomy of anti-detection use cases and maps each to a practical infrastructure or tooling class. This supports its value as a threat-surface taxonomy source.
- The README links to numerous tool categories and named examples: proxy services, scraping platforms, CAPTCHA-solving services, anti-bot vendors, stealth browsers, stealth automation libraries, and fingerprint testing sites. This supports the claim that the evasion ecosystem is broad and modular.
- The README provides maintainer observations about where particular anti-detection approaches fall short, especially around cross-layer inconsistencies and browser-fingerprint surfaces. These are not accompanied by raw test results, logs, targets, or reproducible methodology.
- The statement that findings are based on months of scraping against protected sites is a maintainer claim. It is useful proximity context but should not be treated as independent measurement.
- The list of anti-bot vendors is a non-exhaustive market map, not an evaluation of vendor performance.
- The list of stealth browsers and evasion libraries is a capability catalogue. It does not establish that any listed tool works reliably, safely, or legally.
- The README includes explicit warnings that some stealth software may contain malware. This is useful source self-caveating but not substantiated with examples.
- The repository includes an associated browser-fingerprinting tester page, but the page could not be meaningfully extracted as text in this environment, so tester-specific claims were not analysed.
- The source contains affiliate/sponsor links and direct offers of support for scraping-specific problems. This is relevant to provenance and bias: the source is not neutral academic evidence.

## Signals or techniques mentioned

- IP geolocation filtering.
- Rotating IP pools.
- Region-specific IP pools.
- Repeatable IP pools for long-lived sessions.
- Stable browser fingerprints.
- JavaScript-based bot detection.
- Browser fingerprinting.
- Natural-looking browser-fingerprint surfaces.
- Target-specific detection surfaces.
- Scraping-as-a-service infrastructure.
- Residential and data-centre proxy use.
- CAPTCHA solving as a service.
- Anti-bot vendor identification / tester tooling.
- Stealth browsers and anti-detect browsers.
- Puppeteer, Playwright, Selenium, and Chrome DevTools Protocol automation.
- Stealth plugins and automation-library patches.
- Browser-binary patches and custom browser builds.
- Client hints.
- `navigator` and `window` properties.
- Browser plugins and native extensions.
- Host operating-system consistency across network and browser layers.
- Browser viewport / outer-dimension consistency.
- Worker-thread / hardware-concurrency consistency.
- WebGL profiling.
- WebRTC / RTCPeerConnection leaks behind proxies.
- High-resolution timing APIs.
- Behavioural event detection.
- Font fingerprinting and font-rendering differences.
- Network-latency and DNS timing signals.
- Battery API and mobile sensor signals.
- TLS fingerprint test pages, including JA3 / JA4-style references.
- Browser-extension probing.
- Traffic clustering.
- False-positive risk when blocking advanced mimicry traffic.

## Threat types covered

- Web scraping.
- Scraper-side anti-detection.
- Browser-fingerprint evasion.
- Headless-browser automation.
- Social-media automation.
- Long-lived authenticated automation.
- Geo-restricted scraping.
- Product/e-commerce scraping.
- Sneaker/e-commerce botting as a referenced example.
- CAPTCHA bypass/outsourcing as a friction-reduction technique.
- Proxy-based evasion.
- Residential-proxy-based blending.
- Automation framework detection and evasion.
- False-positive/legitimate-user blocking risk from defensive clustering.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** It approximates the attacker-side and scraper-side knowledge market: how people trying to automate access think about anti-bot systems, what signals they believe matter, what tools they compare, and what kinds of infrastructure they assemble. It is especially useful for mapping the public evasion ecosystem around browser fingerprinting, proxies, headless browsers, stealth automation, CAPTCHA solving, and test pages.
- **What does it fail to represent?** It does not provide independent evidence of abuse prevalence, tool effectiveness, vendor failure rates, or deployment outcomes. It is not a controlled experiment, not a vendor telemetry report, and not a defender-side description of detection design. It is also advocacy-flavoured and commercially entangled through sponsor and affiliate links.
- **What additional evidence would be needed to go further?** A stronger basis would require controlled measurement across defined target classes, explicit test protocols, success/failure rates, time windows, traffic volumes, false-positive observations, and independent reproduction. Defender-side corroboration would also be needed to assess whether the claimed detection surfaces match production practice.

## What it cannot show

- It cannot show internet-wide use of the listed techniques.
- It cannot show that any named stealth browser, proxy provider, or scraping platform works reliably.
- It cannot show that a specific anti-bot vendor can or cannot detect a given technique.
- It cannot show prevalence of browser-fingerprint evasion in production abuse.
- It cannot separate legitimate scraping, grey-market scraping, and malicious abuse.
- It cannot show success rates, block rates, false-positive rates, or evasion durability over time.
- It cannot validate its own claim that anti-bot systems only reduce cheap bot traffic.
- It cannot establish that anti-bot systems are ineffective in general; that is the maintainer's viewpoint, not an independently supported finding.
- It cannot be used as a how-to in project prose without dual-use containment. The project should extract the signal families and tooling ecosystem, not reproduce operational bypass steps.

## Project impact

- This is a high-value **threat-surface** source because it directly shows the public scraper-side mental model of bot detection and browser fingerprinting.
- It is useful as a bridge between academic/vendor descriptions of detection signals and the public tooling ecosystem that tries to counter them.
- It supports the project's point that anti-bot work is an arms race: browser fingerprints, TLS/network signals, behavioural signals, and proxy infrastructure are discussed together rather than as isolated techniques.
- It is useful for a page on the **evasion ecosystem** or **browser-native automation threat surface**, but it should be handled with strong no-recipe discipline.
- It is also useful for showing the difference between capability evidence and use evidence. The repository demonstrates public capability knowledge and tooling awareness; it does not prove observed use against real sites at scale.
- It should not be used for legal, ethical, or efficacy conclusions except as evidence of what the scraper-side field claims and discusses publicly.
- It should be cited cautiously because the source is opinionated, dual-use, partly commercially linked, and not independently validated.

## Possible register row

| Field | Value |
|---|---|
| Register id | `niespodd-browser-fingerprinting` |
| Title | *Avoiding bot detection: How to scrape the web without getting blocked? / browser-fingerprinting* |
| Category | threat-surface |
| Evidence basis | tooling-readme |
| Operational proximity | claimed |
| Tags | threat-surface; browser-fingerprinting; scraper-side; evasion; proxy-rotation; residential-proxy; stealth-browser; puppeteer; playwright; selenium; captcha; tls; behavioural; dual-use |
| Project use | Public scraper-side/evasion mental model and tooling-ecosystem map |
| Main caution | Dual-use source; maintainer claims and tool catalogue, not independent prevalence or effectiveness evidence |
