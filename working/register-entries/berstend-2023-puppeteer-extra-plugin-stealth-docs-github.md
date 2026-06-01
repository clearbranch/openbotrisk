# puppeteer-extra-plugin-stealth documentation and GitHub repository — berstend / puppeteer-extra 2018–2023

## Bibliographic

- **Citation**: Berstend. (2018–2023). `puppeteer-extra-plugin-stealth`: A plugin for `puppeteer-extra` and `playwright-extra` to prevent detection. GitHub / npm.
- **Source URL or path**:
  - https://github.com/berstend/puppeteer-extra/tree/master/packages/puppeteer-extra-plugin-stealth
  - https://raw.githubusercontent.com/berstend/puppeteer-extra/master/packages/puppeteer-extra-plugin-stealth/readme.md
  - https://www.npmjs.com/package/puppeteer-extra-plugin-stealth
- **Date accessed**: 2026-06-01
- **Category**: open-source automation tooling / evasion tooling
- **Tags**: puppeteer-extra-plugin-stealth, puppeteer-extra, playwright-extra, Puppeteer, Playwright, headless-Chromium, browser-automation, stealth, evasion, browser-fingerprinting, headless-detection, navigator.webdriver, user-agent, Accept-Language, chrome.runtime, iframe.contentWindow, navigator.plugins, webgl.vendor, media.codecs, reCAPTCHA-v3, public-bot-tests, anti-detect, cat-and-mouse, open-source-tooling, public-data-limits

## What it claims

- `puppeteer-extra-plugin-stealth` is a plugin for `puppeteer-extra` and `playwright-extra` intended to prevent detection of automated browser sessions.
- The README describes it as applying multiple “evasion techniques” to make detection of headless Puppeteer harder.
- The plugin is modular: individual evasions can be enabled, disabled, tested, or required separately.
- The README claims `puppeteer-extra` with stealth passes all public bot tests known to the maintainer at the time.
- The README explicitly frames browser automation detection as a cat-and-mouse game.
- It acknowledges that it is probably impossible to prevent all detection of headless Chromium, but argues the goal is to make detection cost-prohibitive or too false-positive-prone.
- The README claims stealth can help with maintaining a more normal reCAPTCHA v3 score, while warning that reCAPTCHA scores are site-specific and affected by many other factors such as past behaviour and IP address.
- This is not vendor marketing from a bot-management company. It is open-source evidence that anti-detection/evasion has been packaged as a reusable developer plugin.

## What evidence it provides

The evidence comes from the plugin README and GitHub repository structure.

### Core plugin purpose

The README states that the plugin is for `puppeteer-extra` and `playwright-extra` and is designed to prevent detection.

It gives an example where normal Puppeteer code is modified by adding:

- `puppeteer-extra`
- `puppeteer-extra-plugin-stealth`
- `puppeteer.use(StealthPlugin())`

The rest of the Puppeteer usage remains normal. That matters because the anti-detection functionality is presented as a drop-in layer over ordinary browser automation.

### Modularity and evasion catalogue

The GitHub package directory contains an `evasions` folder. The README says:

- all evasion techniques are enabled by default through the main stealth plugin
- the plugin exposes `availableEvasions`
- the plugin exposes `enabledEvasions`
- specific evasions can be disabled
- individual evasion plugins can be required directly

This provides direct evidence that “stealth” is not one technique. It is a bundle of browser-surface modifications.

### Named evasion surfaces from the README / changelog

The README and older changelog name several browser-detection surfaces:

- `user-agent-override`
- `navigator.vendor`
- `navigator.webdriver`
- `iframe.contentWindow`
- `accept-language`
- `media.codecs`
- `chrome.runtime`
- `navigator.plugins`
- `webgl.vendor`
- `window.outerdimensions`

The README also refers to:

- `HeadlessChrome` in the user agent as an obvious detection surface
- `Accept-Language` header capitalization and request interception as detectable
- ES6 Proxies for `navigator.webdriver` to pass `instanceof` tests
- emulation of plugins and MIME types
- spoofing proprietary media codec availability
- fixing missing outer window dimensions in headless mode
- WebGL vendor differences in headless Chromium

These are concrete examples of browser-fingerprint and JavaScript-runtime inconsistencies that automation tooling tries to patch.

### Public bot tests

The README says stealth passes public bot tests and references several public test sites or test suites, including:

- bot.sannysoft.com
- fpscanner
- areyouheadless
- Intoli/headless test material
- headless-cat-n-mouse

These public tests are useful smoke tests but are not equivalent to production anti-bot evaluation.

### reCAPTCHA v3 score claim

The README claims stealth seems to help with maintaining a normal reCAPTCHA v3 score. It also explicitly warns that the official test should be taken with a grain of salt because reCAPTCHA v3 scores are calculated per site and depend on other factors such as past behaviour and IP address.

This is a useful internal caveat. It supports a careful reading: the plugin may reduce obvious automation signals, but it does not guarantee human-equivalent risk scoring.

## Signals or techniques mentioned

- Puppeteer
- Playwright
- Headless Chromium
- `puppeteer-extra`
- `playwright-extra`
- Drop-in plugin architecture
- Stealth plugin
- Modular evasions
- Specific evasion enabling/disabling
- Public bot tests
- Headless browser detection
- Browser fingerprint inconsistencies
- JavaScript runtime inconsistencies
- `HeadlessChrome` user-agent marker
- User-agent override
- `Accept-Language` header behaviour/capitalisation
- `navigator.webdriver`
- ES6 Proxy handling
- `navigator.vendor`
- `navigator.plugins`
- MIME type emulation
- `webgl.vendor`
- `window.outerWidth` / `window.outerHeight`
- `window.outerdimensions`
- `chrome.runtime`
- `iframe.contentWindow`
- `media.codecs`
- Proprietary codec spoofing
- reCAPTCHA v3 score effects
- Cat-and-mouse adaptation
- Cost-imposition framing for defenders and attackers

## Threat types covered

The plugin is a generic browser-automation evasion layer, not an abuse-specific tool.

Potentially enabled or adjacent automated-threat workflows:

- scraping
- form automation
- account creation
- login automation
- credential stuffing workflows, if combined with credential lists and request logic
- checkout automation
- scalping / inventory hoarding
- ad verification or ad fraud, depending on use
- automated data extraction from sites using simple browser-fingerprint checks
- CAPTCHA/risk-score evasion assistance, indirectly
- AI-agent/browser-agent sessions using Puppeteer/Playwright stacks

Relevant OWASP Automated Threat mappings:

- OAT-008 Credential Stuffing, if used for login automation
- OAT-011 Scraping
- OAT-019 Account Creation
- OAT-020 Denial of Inventory
- anti-detection/evasion as a cross-cutting capability rather than a threat type itself

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates the tooling layer between ordinary headless-browser automation and anti-detect browser infrastructure. It shows that known headless-browser fingerprints can be patched through a reusable open-source plugin, and that evasion techniques can be modularised, tested, and composed.

- **What does it fail to represent?**  
  It does not prove malicious use. Puppeteer and Playwright are legitimate automation tools, and stealth plugins can be used for testing, QA, scraping public data, or research. It also does not show success against modern commercial bot-management systems such as Cloudflare, DataDome, HUMAN/PerimeterX, Kasada, Arkose, Akamai, Imperva, or Netacea. Public bot tests are not production anti-bot evaluations.

- **What additional evidence would be needed to go further?**  
  Independent tests of `puppeteer-extra-plugin-stealth` against modern anti-bot vendors; comparison with vanilla Puppeteer, Playwright, Selenium, anti-detect browsers, cloud browsers, Browserless/ScrapFly/Bright Data; tests with and without residential proxies, CAPTCHA solvers, persistent profiles, and human-like behaviour; fingerprint-diff studies against real Chrome; abuse-flow tests for login, registration, scraping, and checkout.

## What it cannot show

- It cannot show that stealth reliably bypasses modern anti-bot systems.
- It cannot show that public bot-test success translates to production success.
- It cannot show that reCAPTCHA v3 or similar risk systems will treat sessions as human.
- It cannot show that the plugin is mainly used for abuse.
- It cannot show robustness against active defender adaptation.
- It cannot show TLS/JA3/JA4 consistency, IP reputation, residential proxy quality, behavioural realism, or account-history effects.
- It cannot replace empirical studies such as FP-Inconsistent, Iliou et al., Acien et al., or TLS/JA4 studies.

## Project impact

- Strong open-source tooling evidence.
- Important because it demonstrates that stealth/evasion is not only a commercial scraping-platform feature; it also exists as reusable open-source automation infrastructure.
- Useful for the project taxonomy:
  - simple HTTP scripts
  - vanilla headless browsers
  - browser automation plus stealth plugin
  - anti-detect browsers / cloud browsers
  - proxy and CAPTCHA-solving layers
  - AI-agent/browser-agent stacks
- Good bridge source between:
  - academic browser-fingerprint papers such as FP-Inspector and Andriamilanto
  - vendor anti-bot docs such as Cloudflare/DataDome/HUMAN/Kasada
  - automation supply-side docs such as Browserless, ScrapFly, Bright Data, Browserbase, and Hyperbrowser
- Supports the claim that bot detection is partly an inconsistency-detection problem: defenders look for mismatches in browser APIs, headers, plugins, codecs, WebGL, iframe behaviour, and automation markers; attackers patch those mismatches.
- Should be cited as open-source capability/evasion evidence, not proof of abuse or production bypass success.
