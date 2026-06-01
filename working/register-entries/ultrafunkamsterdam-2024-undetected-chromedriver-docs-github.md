# undetected-chromedriver documentation and GitHub repository — ultrafunkamsterdam 2021–2024

## Bibliographic

- **Citation**: ultrafunkamsterdam. (2021–2024). `undetected-chromedriver`: Custom Selenium ChromeDriver / zero-config ChromeDriver patch. GitHub / PyPI.
- **Source URL or path**:
  - https://github.com/ultrafunkamsterdam/undetected-chromedriver
  - https://pypi.org/project/undetected-chromedriver/
- **Date accessed**: 2026-06-01
- **Category**: open-source automation tooling / Selenium evasion tooling
- **Tags**: undetected-chromedriver, Selenium, ChromeDriver, Chromium, browser-automation, headless-Chrome, anti-detection, bot-mitigation-bypass, Cloudflare, DataDome, Imperva, Distil, Botprotect, IP-reputation, Chrome-DevTools-Protocol, CDP, webdriver, anti-bot-evasion, open-source-tooling, public-data-limits

## What it claims

- `undetected-chromedriver` is an open-source Python package that patches Selenium ChromeDriver to reduce automation detection.
- The GitHub README describes it as an “optimized Selenium Chromedriver patch” that does not trigger anti-bot services such as Distil, Imperva, DataDome, Botprotect.io, and Cloudflare IUAM.
- It automatically downloads and patches the ChromeDriver binary.
- It is presented as a near drop-in replacement for ordinary Selenium ChromeDriver.
- The project supports Chrome and other Chromium-based browsers, including Brave with some configuration.
- The README explicitly says it does not hide the user’s IP address, and that datacenter IPs or poor IP reputation may still fail.
- The README includes version history showing the anti-detection mechanism being rewritten, with a shift away from removing/renaming variables and toward preventing them from being injected in the first place.
- The README states that headless support has been patched, but also repeatedly treats headless mode as more fragile/unsupported.
- This is strong open-source capability evidence for Selenium-based anti-detection tooling. It is not evidence that the tool reliably bypasses current commercial systems.

## What evidence it provides

The evidence comes from the GitHub README and PyPI package page.

### Core purpose

The README describes the package as a Selenium ChromeDriver patch intended not to trigger several named anti-bot services. It specifically names:

- Distil Network
- Imperva
- DataDome
- Botprotect.io
- Cloudflare IUAM

The basic usage is minimal:

- import `undetected_chromedriver as uc`
- create `uc.Chrome()`
- use it like a Selenium driver

This matters because anti-detection is packaged as a developer-friendly replacement layer over standard Selenium, rather than as a separate complex framework.

### IP reputation caveat

The README gives a major caveat: the package does not hide IP address. It says running from datacenter IPs, or from a home IP with poor reputation, may still fail.

This is useful because it matches broader evidence from anti-bot vendors and scraping infrastructure: browser-fingerprint evasion is only one layer. IP reputation, proxy quality, request history, behaviour, cookies, and account/session state still matter.

### Anti-detection mechanism

The changelog says version 3.4.0 rewrote the anti-detection mechanism. Instead of removing and renaming variables, the package prevents those variables from being injected in the first place.

This is important because it shows the anti-detection logic is not only cosmetic browser-surface patching. It attempts to intervene earlier in the ChromeDriver/automation signal path.

### Headless mode

The README includes headless examples and says later versions patched headless mode to be “undetected”, but also calls headless unsupported or work-in-progress in several places.

That makes the source useful but also internally cautious: headless browser automation is a moving detection surface, especially as Chrome versions change.

### Chrome DevTools Protocol / event support

The README includes “expert mode” examples using low-level Chrome DevTools Protocol events. It shows the driver can subscribe to network events such as:

- `Network.requestWillBeSent`
- `Network.dataReceived`

This is relevant because modern automation/evasion tooling often combines WebDriver-style control with CDP-level observability and manipulation.

## Signals or techniques mentioned

- Selenium
- ChromeDriver
- Patched ChromeDriver binary
- Automatic driver download and patching
- Chromium browser support
- Brave browser support
- Headless Chrome
- Headless detection
- Automation-detection algorithms
- Preventing automation variables from being injected
- WebDriver/ChromeDriver detection surface
- Chrome DevTools Protocol
- CDP events
- Network request events
- Request headers
- User-Agent
- sec-ch-ua headers
- Accept-Language
- HTTP/2 request context in examples
- Cloudflare “under attack mode” test site
- IP reputation
- Datacenter IP risk
- Home IP reputation risk
- Persistent user data directory / Chrome profile
- Version-specific Chrome handling
- Selenium 4 compatibility
- Click-safe helper method
- Frame/element handling convenience functions

## Threat types covered

The package is generic browser-automation evasion tooling, not an abuse-specific tool.

Potentially enabled or adjacent workflows:

- scraping
- login automation
- account takeover workflows, if combined with credentials
- credential stuffing workflows
- fake account creation
- checkout automation
- scalping / inventory hoarding
- form automation
- automated interaction with sites protected by basic bot-mitigation services
- AI-agent/browser-agent workflows built on Selenium
- testing anti-bot or automation-detection systems

Relevant OWASP Automated Threat mappings:

- OAT-008 Credential Stuffing, if used for login automation
- OAT-011 Scraping
- OAT-019 Account Creation
- OAT-020 Denial of Inventory / scalping
- evasion/anti-detection as a cross-cutting capability

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  It approximates the open-source Selenium anti-detection layer. It shows that developers can take familiar Selenium code and swap in a patched driver designed to reduce ChromeDriver automation detection. That is important because Selenium remains widely known and accessible, even if newer tooling such as Playwright/Puppeteer and cloud-browser platforms are now common.

- **What does it fail to represent?**  
  It does not prove malicious use. Selenium and ChromeDriver are widely used for testing, QA, research, and legitimate browser automation. It also does not prove current bypass capability against Cloudflare, DataDome, Imperva, HUMAN/PerimeterX, Kasada, Arkose, Akamai, Netacea, or other modern systems. The README claims are project-maintainer claims, not independent evaluation. Named services and test outcomes may be stale.

- **What additional evidence would be needed to go further?**  
  Independent tests against current anti-bot systems; comparison against vanilla Selenium, Puppeteer, Playwright, `puppeteer-extra-plugin-stealth`, Nodriver, SeleniumBase UC Mode, anti-detect browsers, cloud browsers, and scraping APIs; tests with different IP reputations, residential proxies, mobile proxies, persistent profiles, cookies, account histories, and behavioural patterns; fingerprint-diff studies against real Chrome; longitudinal tests across Chrome/ChromeDriver versions.

## What it cannot show

- It cannot show that `undetected-chromedriver` reliably bypasses current production anti-bot systems.
- It cannot show that bypass claims from earlier README versions remain true.
- It cannot show that headless mode is robust.
- It cannot hide or repair IP reputation, proxy quality, behavioural realism, cookies, or account history.
- It cannot show that public or maintainer-run tests generalise to real production systems.
- It cannot show that the package is mainly used for abuse.
- It cannot replace empirical studies of evasive bot traffic, browser fingerprint inconsistency, behavioural biometrics, or TLS/JA4 fingerprinting.

## Project impact

- Strong open-source Selenium evasion-tooling source.
- Complements the `puppeteer-extra-plugin-stealth` entry:
  - `puppeteer-extra-plugin-stealth` patches browser JavaScript/API surfaces for Puppeteer/Playwright-style automation.
  - `undetected-chromedriver` patches the Selenium ChromeDriver layer and tries to prevent automation variables being injected.
- Useful for the automation taxonomy:
  - vanilla Selenium / WebDriver
  - patched Selenium / undetected ChromeDriver
  - Puppeteer/Playwright stealth plugins
  - Nodriver/SeleniumBase UC mode/Camoufox style tools
  - anti-detect browsers
  - cloud-browser infrastructure
  - scraping APIs and web unlockers
  - AI-agent browser stacks
- Supports the claim that bot detection is not only about HTTP traffic or mouse movement. It also involves browser-control artefacts, WebDriver/ChromeDriver markers, headless behaviour, version mismatches, IP reputation, and network/session context.
- Should be cited as open-source capability/evasion evidence, not proof of abuse or production bypass reliability.
