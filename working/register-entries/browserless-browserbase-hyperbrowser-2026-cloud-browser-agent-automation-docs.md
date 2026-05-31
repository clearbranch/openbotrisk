# Browserless, Browserbase, and Hyperbrowser documentation: cloud browsers, browser agents, stealth, proxies, CAPTCHA solving, and large-scale automation — 2026

## Bibliographic

- **Citation**: Browserless, Browserbase, and Hyperbrowser. (2026). Cloud browser and browser-agent documentation.
- **Source URL or path**:
  - https://docs.browserless.io/
  - https://docs.browserless.io/browserql/bot-detection/stealth
  - https://docs.browserless.io/ai-integrations/browser-use/python
  - https://docs.browserbase.com/
  - https://docs.browserbase.com/use-cases/agents
  - https://docs.browserbase.com/use-cases/automating-form-submissions
  - https://www.hyperbrowser.ai/docs/home
  - https://www.hyperbrowser.ai/docs/introduction
  - https://www.hyperbrowser.ai/docs/sandboxes/introduction
- **Date accessed**: 2026-06-01
- **Category**: automation platform / cloud-browser infrastructure
- **Tags**: Browserless, Browserbase, Hyperbrowser, cloud-browsers, browser-agents, browser-automation, Playwright, Puppeteer, Selenium, Browser-Use, Stagehand, Claude-Computer-Use, OpenAI-CUA, Gemini-Computer-Use, MCP, BrowserQL, stealth, fingerprint-evasion, CAPTCHA-solving, residential-proxies, session-management, persistent-sessions, live-view, session-recording, scraping, form-submission, login-automation, AI-agents, agentic-browsers, public-data-limits

## What it claims

- Browserless, Browserbase, and Hyperbrowser provide managed cloud browsers for automation, scraping, browser agents, testing, and web-data workflows.
- These platforms expose browser sessions through standard automation interfaces such as Playwright, Puppeteer, Selenium, Chrome DevTools Protocol, and higher-level agent frameworks.
- Browserless explicitly markets BrowserQL as a stealth automation GraphQL API with CAPTCHA solving, fingerprint evasion, and human-behaviour simulation for sites that actively resist bots.
- Browserless provides a stealth route that applies browser fingerprint mitigations and entropy injection with no extra configuration.
- Browserless documentation shows configuration for bot-protected sites using stealth mode, residential proxies, and automatic CAPTCHA solving for reCAPTCHA, hCaptcha, and Cloudflare Turnstile.
- Browserbase positions itself as a platform for agents that browse and interact with the web like humans, with cloud browsers, search, fetch, sandbox runtime, and access to LLMs.
- Browserbase states that agents can log into third-party tools, take action on a user’s behalf, pull live data from authenticated or bot-blocking sites, and run parallel workloads across thousands of sessions.
- Browserbase has specific documentation for automating form submissions at scale, including logins, registrations, data entry, and checkouts.
- Hyperbrowser positions itself as fast cloud browsers for AI agents, large-scale scraping, and session management.
- Hyperbrowser explicitly advertises “Ultra Stealth Mode” for extra evasion from bot detection, plus proxy configuration, CAPTCHA solving, static IPs, profiles, recordings, live view, extensions, and AI-agent integrations.
- These sources are not anti-bot detection papers. They are direct evidence that commercial automation infrastructure now packages cloud browsers, stealth, proxies, CAPTCHA handling, session persistence, observability, and AI-agent integrations as normal developer features.

## What evidence it provides

The evidence is product documentation from automation providers, not independent measurement.

### Browserless

Browserless documentation describes several relevant product surfaces:

- **BrowserQL**: a GraphQL API for stealth automation, advertised as including CAPTCHA solving, fingerprint evasion, and human behaviour simulation for sites that actively resist bots.
- **Browsers as a Service**: managed cloud browsers that can be controlled by existing Puppeteer or Playwright code over WebSocket.
- **REST APIs**: screenshot, PDF, scraping, search, crawl, and export endpoints.
- **AI integrations**: Browser Use, Stagehand, LangChain, Vercel AI SDK, Claude Agent SDK, OpenAI SDK/CUA, Anthropic SDK/CUA, n8n, Make, Zapier, OpenClaw, and other frameworks.
- **MCP support**: Browserless can be connected to AI tools for full browser automation.

The Browserless stealth-route page says `/stealth/bql` is a hardened BrowserQL endpoint that applies comprehensive browser fingerprint mitigations and entropy injection automatically.

The Browserless Browser Use integration page is especially direct. It includes examples for:

- connecting Browser Use agents to Browserless cloud browsers
- using an LLM-backed agent to browse and answer a task
- using stealth mode and residential proxies for bot-protected sites
- enabling automatic CAPTCHA solving
- combining stealth, proxy, and CAPTCHA-solving features for compatibility with bot-protected sites

This makes Browserless a strong source for the project’s “automation-as-a-service / evasion-as-feature” category.

### Browserbase

Browserbase documentation frames the platform as infrastructure for agents that browse and interact with the web like humans. It lists:

- cloud browsers
- web search
- page fetching
- sandbox runtime
- access to LLMs
- browser sessions
- Browser API
- Fetch API
- Search API
- Functions for scheduled/on-demand agent execution
- Model Gateway
- Playwright, Puppeteer, Selenium, Stagehand, LangChain, CrewAI, and other integrations

The Browserbase browser-agents page states that agents can:

- browse anything a human can do in a browser
- stay logged in through persistent contexts
- allow inspection through live view and session recording
- access sites that require authentication or block bots through Agent Identity
- run parallel workloads across thousands of browser sessions
- navigate portals, fill forms, submit data, log into third-party tools, and take action on a user’s behalf

The form-submission page states that Browserbase can automate logins, registrations, data entry, and checkouts using Stagehand or Playwright in cloud browsers, including workflows involving dynamic content, authentication, and bot protection.

This is useful evidence that browser-agent infrastructure is moving toward legitimate enterprise/developer use cases, while also overlapping with the same action space as abusive automation: login, account creation, checkout, forms, authenticated data extraction, and bot-blocking sites.

### Hyperbrowser

Hyperbrowser documentation describes a cloud browser platform for running automated browser sessions at scale. It says users can control Chrome browsers in the cloud using Puppeteer, Playwright, or Hyperbrowser SDKs.

The docs index and introduction list relevant capabilities:

- cloud browser sessions
- Playwright, Puppeteer, and Selenium connections
- computer actions
- stealth mode
- proxy configuration
- multi-region support
- CAPTCHA solving
- ad blocking
- profiles
- static IPs
- recordings
- live view
- browser extensions
- file upload/download
- scraping, crawl, and extract APIs
- AI-agent integrations with Browser Use, Claude Computer Use, OpenAI CUA, Gemini Computer Use, and HyperAgent
- MCP and other integrations

The Hyperbrowser introduction explicitly describes “Ultra Stealth Mode” as an advanced stealth mode for extra evasion from bot detection.

The sandboxes documentation describes isolated cloud environments for agentic workflows with fast startup times, custom images, local filesystem access, volumes, and process execution. This matters because browser agents increasingly need not just a browser, but a full controlled runtime around the browser.

## Signals or techniques mentioned

- Cloud browsers
- Managed browser sessions
- Browser-as-a-service
- Chrome DevTools Protocol
- Playwright
- Puppeteer
- Selenium
- Browser Use
- Stagehand
- LangChain
- CrewAI
- Vercel AI SDK
- Claude Agent SDK
- Claude Computer Use
- OpenAI CUA
- Anthropic CUA
- Gemini Computer Use
- OpenClaw
- MCP
- BrowserQL
- GraphQL browser automation
- REST scraping/search/crawl APIs
- Stealth route
- Stealth mode
- Ultra Stealth Mode
- Browser fingerprint mitigations
- Entropy injection
- Fingerprint evasion
- Human behaviour simulation
- Residential proxies
- Proxy configuration
- Static IPs
- CAPTCHA solving
- reCAPTCHA solving
- hCaptcha solving
- Cloudflare Turnstile solving
- Persistent contexts / persistent sessions
- Session management
- Live view
- Session recording
- Browser profiles
- Browser extensions
- File upload/download
- Sandboxed runtime
- Cloud functions for agents
- Scheduled or on-demand agent execution
- Large-scale concurrent sessions
- Form filling
- Login automation
- Registration automation
- Checkout automation
- Authenticated data retrieval
- Agent identity
- Search and fetch APIs
- Markdown page extraction
- Web scraping/crawling/extraction APIs

## Threat types covered

These docs are not written as abuse reports, but the capabilities overlap with many automated-threat workflows.

Potentially enabled or adjacent abuse categories:

- Scraping and crawling
- Authenticated scraping
- Account creation / registration automation
- Form spam
- Credential stuffing / login automation
- Account takeover workflows, if combined with credentials
- Checkout automation
- Scalping / inventory hoarding
- Carding/payment abuse, if combined with stolen payment data
- CAPTCHA bypass / challenge handling
- Evasion of browser-fingerprint and bot-detection checks
- AI-agent web task execution
- Automated interaction with portals and third-party tools
- Synthetic user journeys
- Data extraction from sites without APIs

Relevant OWASP Automated Threat mappings:

- OAT-008 Credential Stuffing
- OAT-011 Scraping
- OAT-019 Account Creation
- OAT-020 Denial of Inventory / scalping
- OAT-003 Ad Fraud only indirectly, if used for scripted ad/traffic workflows
- OAT-014 Vulnerability Scanning only indirectly, if paired with recon workflows
- CAPTCHA/challenge bypass as cross-cutting evasion
- AI-agent/browser-agent automation as a modern cross-cutting category

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  These sources approximate the supply side of modern browser automation infrastructure. They show that developers can rent cloud browsers, connect Playwright/Puppeteer/Selenium or AI-agent frameworks, persist sessions, inspect runs, use proxies, solve CAPTCHAs, and apply stealth/fingerprint-evasion options without building their own browser cluster. That is directly relevant to the project’s “what can modern bots be?” question.

- **What does it fail to represent?**  
  The docs do not prove abuse. These are legitimate automation platforms and can be used for testing, data retrieval, internal workflows, accessibility, QA, and authorised agents. The documentation does not provide prevalence, malicious intent, anti-bot success rates, or real-world abuse outcomes. Some claims are marketing/product claims rather than measured evidence. It also does not show how well stealth features work against Cloudflare, DataDome, HUMAN, Kasada, Arkose, Akamai, Imperva, or other defences.

- **What additional evidence would be needed to go further?**  
  Independent tests of Browserless/Browserbase/Hyperbrowser sessions against anti-bot services; fingerprint comparison between cloud sessions and real browsers; experiments with and without stealth/proxies/CAPTCHA solving; abuse-flow simulations for login, account creation, checkout, scraping, and APIs; provider policies and enforcement data; comparisons with open-source Playwright/Puppeteer/Selenium run locally; study of AI-agent safety controls and website-side detection.

## What it cannot show

- It cannot show that these platforms are mainly used for abuse.
- It cannot show that their stealth features reliably bypass anti-bot systems.
- It cannot show that CAPTCHA solving succeeds consistently across target sites.
- It cannot show production false-negative rates for defenders.
- It cannot prove that AI agents using these platforms are indistinguishable from humans.
- It cannot establish bot prevalence or business impact.
- It cannot replace academic studies or independent anti-bot evaluations.
- It cannot show the providers’ internal abuse-prevention enforcement, unless separate policy/transparency material is obtained.

## Project impact

- Very strong source family for the automation-supply-side section.
- These docs support a taxonomy layer that sits between simple scripts and bespoke malware:
  - managed cloud browsers
  - browser automation frameworks
  - browser-agent platforms
  - stealth/fingerprint-evasion services
  - residential proxy integration
  - CAPTCHA-solving integration
  - persistent authenticated sessions
  - cloud sandboxes and agent runtimes
- Useful counterweight to vendor anti-bot material:
  - Cloudflare, DataDome, HUMAN, Kasada, and Arkose show the defender/product side.
  - Browserless, Browserbase, and Hyperbrowser show the automation infrastructure side.
- Supports the decision to include AI agents and cloud-browser platforms in scope.
- Good evidence for why the project taxonomy should not stop at:
  - HTTP scripts
  - Selenium
  - Puppeteer/Playwright
  It should include:
  - browser-as-a-service
  - agentic browser infrastructure
  - stealth/fingerprint-evasion routes
  - proxy and CAPTCHA-solving integration
  - persistent session/state management
  - sandboxed agent runtimes
- Should be cited as capability/infrastructure evidence, not as proof of malicious use.
