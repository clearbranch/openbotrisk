# Playwright, Puppeteer, and Selenium documentation: baseline browser automation frameworks — 2026

## Bibliographic

- **Citation**: Microsoft Playwright, Google Chrome for Developers / Puppeteer, and Selenium. (2026). Official documentation for Playwright, Puppeteer, and Selenium WebDriver.
- **Source URL or path**:
  - https://playwright.dev/docs/intro
  - https://playwright.dev/docs/library
  - https://pptr.dev/
  - https://www.selenium.dev/documentation/
  - https://www.selenium.dev/documentation/webdriver/
- **Date accessed**: 2026-06-01
- **Category**: open-source browser automation frameworks / baseline tooling
- **Tags**: Playwright, Puppeteer, Selenium, Selenium-WebDriver, browser-automation, end-to-end-testing, Chromium, Firefox, WebKit, Chrome, WebDriver, WebDriver-BiDi, Chrome-DevTools-Protocol, CDP, headless-browser, headed-browser, browser-contexts, locators, actions, network-interception, screenshots, testing, scraping-adjacent, automation-supply-side, public-data-limits

## What it claims

- Playwright is an end-to-end testing framework and browser automation library for modern web apps.
- Playwright supports Chromium, WebKit, and Firefox on Windows, Linux, and macOS, locally or in CI, headless or headed.
- Playwright Library provides unified APIs for launching and interacting with browsers directly.
- Puppeteer is a JavaScript library providing a high-level API to control Chrome or Firefox over Chrome DevTools Protocol or WebDriver BiDi.
- Puppeteer runs headless by default.
- Selenium WebDriver is a browser automation framework with driver-based control of browsers and support across several languages and browsers.
- Selenium documentation exposes browser automation concepts including drivers, remote WebDriver, browser options, waits, locators, interactions, navigation, cookies, frames, windows, Actions API, BiDi, CDP, Grid, and test-practice guidance.
- These frameworks are legitimate test-automation tools. They are also the baseline technology layer on which many scraping, bot, stealth, and browser-agent systems are built.

## What evidence it provides

The evidence is official documentation, not threat research.

### Playwright

Playwright’s official docs describe it as an end-to-end test framework for modern web apps, bundling a test runner, assertions, isolation, parallelization, and tooling. It supports Chromium, WebKit, and Firefox across Windows, Linux, and macOS, locally or in CI, and can run headless or headed.

The Playwright Library docs are particularly relevant because they show direct browser automation outside the test-runner framing. The example launches Chromium, creates a browser context, opens a page, routes/blocks image requests, navigates to a URL, checks the page title, and closes the context/browser.

Relevant capabilities from the docs index and examples include:

- browser launching
- browser contexts
- pages
- device emulation
- network routing/interception
- locators
- actions
- assertions
- screenshots
- downloads
- frames
- dialogs
- JavaScript evaluation
- authentication state
- traces
- videos
- UI mode and debugging
- CI execution
- headed/headless execution

Playwright matters for this project because it provides a high-level, reliable, cross-browser automation layer. It is not an evasion tool by itself, but it is often used as the base layer underneath browser agents, scraping platforms, and stealth wrappers.

### Puppeteer

Puppeteer’s official docs describe it as a JavaScript library providing a high-level API to control Chrome or Firefox over Chrome DevTools Protocol or WebDriver BiDi. Puppeteer runs headless by default.

The basic example launches a browser, opens a page, navigates to a URL, sets a viewport, presses a keyboard key, fills a search field through a locator, clicks a search result, evaluates page text, and closes the browser.

Relevant capabilities from the docs and example include:

- launching Chrome/Firefox
- headless browser control
- Chrome DevTools Protocol
- WebDriver BiDi
- page creation
- navigation
- viewport control
- keyboard input
- locators
- clicking
- DOM text extraction
- screenshots/PDFs and other common browser automation tasks through the wider API
- MCP integration through Chrome DevTools MCP

Puppeteer matters for this project because it is one of the most common bases for browser bots, scraping scripts, automation agents, and stealth tooling. The separate `puppeteer-extra-plugin-stealth` entry builds directly on this ecosystem.

### Selenium

Selenium’s documentation presents WebDriver as the core browser automation interface. The docs expose a broad browser automation surface:

- drivers
- browser-specific options
- remote WebDriver
- browser support for Chrome, Edge, Firefox, Safari, and others
- waits
- elements and locators
- interactions
- navigation
- alerts
- cookies
- frames
- windows
- virtual authenticators
- Actions API for keyboard, mouse, pen, and wheel inputs
- WebDriver BiDi
- CDP access
- Selenium Grid for remote/distributed execution
- test-practice guidance

The Selenium docs also include “discouraged” testing practices, including Captchas, link spidering, 2FA, email/social-network dependencies, and performance testing. That is useful because Selenium’s own test-automation guidance acknowledges that some site features are unsuitable or risky to automate in ordinary tests.

Selenium matters because it is the older and widely known browser automation standard. It is also the base layer for tools such as `undetected-chromedriver` and SeleniumBase UC Mode.

## Signals or techniques mentioned

- Browser automation
- End-to-end testing
- Headless execution
- Headed execution
- Chromium
- Chrome
- Firefox
- WebKit
- Safari
- Edge
- Browser drivers
- WebDriver
- WebDriver BiDi
- Chrome DevTools Protocol
- Remote WebDriver
- Selenium Grid
- Browser contexts
- Pages
- Device emulation
- Viewport control
- Network routing/interception
- Request blocking
- Locators
- DOM querying
- Form filling
- Keyboard input
- Mouse input
- Wheel input
- Navigation
- Cookies
- Frames
- Windows/tabs
- Alerts/dialogs
- JavaScript evaluation
- Screenshots
- PDFs
- Downloads
- Tracing
- Video/session recording
- Authentication state
- CI execution
- Parallel execution
- MCP / Chrome DevTools MCP
- Virtual authenticators
- Actions API

## Threat types covered

The official docs are not abuse reports. They primarily describe legitimate browser testing and automation.

However, the same capabilities can be used in or adapted for:

- scraping
- account creation
- login automation
- credential stuffing workflows, if paired with credentials and target logic
- checkout automation
- scalping / inventory hoarding
- form spam
- data extraction from JavaScript-heavy sites
- authenticated workflow automation
- AI-agent web interaction
- automation testing of bot defences
- synthetic monitoring

Relevant OWASP Automated Threat mappings, depending on use:

- OAT-008 Credential Stuffing
- OAT-011 Scraping
- OAT-019 Account Creation
- OAT-020 Denial of Inventory / scalping
- browser automation as a cross-cutting capability rather than a threat type itself

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  These docs approximate the baseline technical capability layer. They show what a normal developer can do with mainstream open-source browser automation: launch browsers, click, type, navigate, manage sessions/cookies, intercept network requests, emulate devices, run headless/headed, and scale tests across CI or Grid. Modern scraping platforms, browser agents, and stealth tools often build on these primitives.

- **What does it fail to represent?**  
  These docs do not describe malicious use, anti-bot evasion, residential proxies, CAPTCHA solving, fingerprint spoofing, or production bypass. Playwright, Puppeteer, and Selenium are legitimate testing and automation frameworks. Using them does not automatically imply abuse. The docs also do not prove that automation can evade modern bot management.

- **What additional evidence would be needed to go further?**  
  Studies comparing vanilla framework sessions with real user sessions; fingerprint-diff tests; detection-rate tests against Cloudflare, DataDome, HUMAN/PerimeterX, Kasada, Arkose, Akamai, Imperva, and Netacea; comparisons with stealth plugins, undetected ChromeDriver, Nodriver, anti-detect browsers, cloud browsers, residential proxies, and CAPTCHA solvers; abuse-flow tests for login, registration, checkout, scraping, and APIs.

## What it cannot show

- It cannot show that these frameworks are mainly used for abuse.
- It cannot show that vanilla browser automation bypasses anti-bot systems.
- It cannot show that headless sessions look like normal human browser sessions.
- It cannot show IP reputation, TLS fingerprint, behavioural realism, account history, or device history.
- It cannot show production false-negative rates for defenders.
- It cannot replace evidence from stealth/evasion tooling, scraping infrastructure, vendor anti-bot docs, or academic anti-bot studies.

## Project impact

- Essential baseline source for the project.
- These frameworks define the base layer of the taxonomy:
  - Selenium / WebDriver automation
  - Puppeteer / CDP automation
  - Playwright / cross-browser automation
- They should sit before the stealth/tooling layers:
  - `undetected-chromedriver`
  - `puppeteer-extra-plugin-stealth`
  - Playwright stealth wrappers
  - Nodriver / SeleniumBase UC Mode / Camoufox
  - cloud browsers and web-unlocker APIs
  - browser agents and AI-agent runtimes
- Useful for explaining why “bot” does not just mean HTTP requests:
  - modern bots can execute JavaScript
  - keep cookies/session state
  - click and type
  - run in real browser engines
  - emulate devices
  - intercept network traffic
  - execute multi-step workflows
- Important caveat: this is capability infrastructure, not intent evidence.
- Should be cited as official documentation for baseline automation capability, not as evidence of malicious activity or bypass success.
