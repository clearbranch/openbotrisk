# Tschacher (2021) - On the Architecture of Bot Detection Services

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF capture `SRC-077-tschacher-2021-architecture-of-bot-detection-services.pdf`.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.
- **Source handling decision**: keep as a standalone full entry. This is a useful architecture-level source that connects directly to the DataDome VM-obfuscation entry and to the wider client/server signal taxonomy.

## Bibliographic

- **Citation**: Tschacher, N. (2021). *On the Architecture of Bot Detection Services*. incolumitas.com. Published 18 July 2021.
- **Source URL or path**: uploaded PDF `SRC-077-tschacher-2021-architecture-of-bot-detection-services.pdf`.
- **Category**: public technical analysis / bot-detection architecture
- **Evidence basis**: technical explainer / architecture analysis / attacker-aware commentary
- **Operational proximity**: architecture — useful for explaining bot-detection signal layers and client/server trust boundaries, but not empirical telemetry, vendor performance evidence, or a validated detection design.
- **Tags**: bot-detection, passive-detection, client-side-detection, JavaScript-fingerprinting, browser-fingerprinting, TLS-fingerprinting, TCP-IP-fingerprinting, HTTP-headers, IP-reputation, cookies, sessions, behavioural-signals, JavaScript-obfuscation, JavaScript-VMs, client-server-security, spoofable-signals, rate-limiting, detection-architecture

## What it claims

- A passive bot-detection system tries to decide whether a website visitor is an automated program without interrupting the session with an explicit challenge such as CAPTCHA.
- “Automated program” is broad and includes simple scripts, real browsers driven by Playwright/Puppeteer, and physical mobile devices automated through ADB/Appium-style tooling.
- A website visitor doing a single page view gives much less evidence than a visitor performing a complex workflow such as logging into a bank and transferring money.
- The server should treat every message from the browser/client as potentially spoofed or tainted.
- Bot detection rarely has a single binary signal that proves “bot” or “human”; instead, systems identify and score users across multiple layers.
- The practical goal is often unique-user identification and rate limiting rather than perfect metaphysical classification of humanness.
- Detection can use IP address, TCP/IP fingerprints, TLS fingerprints, HTTP headers and header order/case, browser fingerprints, behavioural signals, cookies, and session IDs.
- JavaScript-collected data is especially important but also especially vulnerable because the client controls the JavaScript execution environment.
- Bot-detection vendors use JavaScript obfuscation, JavaScript virtual machines, and payload encryption/encoding to protect client-side signal collection.
- Protecting JavaScript is harder than protecting native binary code because it must remain ECMAScript-compatible, browser-compatible, performant, and eventually visible to the browser runtime.

## What evidence it provides

This is a **public technical explainer**, not an empirical paper.

It provides:

- a clear attacker model for browser-side bot detection;
- a useful diagram on page 2 showing the browser and JavaScript side as attacker-controlled and all client-to-server messages as tainted/spoofable;
- a layered walkthrough of a browsing session from DNS lookup to TCP/TLS handshake to HTTP request to JavaScript signal collection;
- a taxonomy of passive detection signals:
  - IP/subnet reputation;
  - DNS/proxy leak consistency;
  - TCP/IP fingerprinting;
  - latency/RTT/throughput;
  - TLS fingerprinting;
  - HTTP header fingerprints and proxy headers;
  - browser/JavaScript fingerprints;
  - behavioural events such as mouse/touch/keypress data;
  - cookies/session IDs;
- an explanation of why client-side detection code is obfuscated;
- a grounded statement that the delay between client-side signal collection and server-side decisioning creates practical limits;
- a useful distinction between single-page scraping and longer workflows where behavioural and intent data accumulate.

It does **not** provide:

- production telemetry;
- detection accuracy metrics;
- false-positive/false-negative rates;
- validated bot-management architecture;
- formal privacy/legal analysis;
- independent comparison of vendors;
- current 2026 vendor capability;
- evidence that any specific signal works reliably;
- evidence of abuse prevalence.

## Important visual/source evidence

- **Page 2** contains a simple attacker-model diagram: browser and JavaScript sit on the attacker-controlled side, while the web server is on the defender side; red arrows mark client-to-server messages as potentially tainted/spoofed.
- **Page 4** includes a TCP/TLS handshake diagram before the first page load, supporting the discussion that bot detection can begin before JavaScript runs.
- **Page 6** starts the JavaScript client-side detection section and explicitly lists JavaScript obfuscation, JavaScript virtual machines, and encryption/encoding of payloads as ways detection companies camouflage signal-collection libraries.
- **Page 6** also explains why JavaScript protection is hard: JavaScript is interpreted, must conform to ECMAScript, eventually reaches AST/runtime representation, must work across browsers, and must remain performant.

## Signals or techniques mentioned

- passive bot detection;
- active challenge systems such as CAPTCHA/hCAPTCHA as contrast;
- Playwright;
- Puppeteer;
- curl;
- shell scripts;
- Android Debug Bridge;
- Appium;
- DeviceFarmer/STF;
- DNS lookup and DNS leak consistency;
- IP address;
- subnet counters;
- IP reputation;
- spam/abuse databases;
- datacenter IP lookup;
- residential ISP checks;
- geolocation;
- ASN/organisation/registry lookup;
- reverse DNS;
- TCP/IP fingerprint;
- TCP options;
- latency/RTT/throughput;
- TLS fingerprint;
- TCP/TLS mismatch;
- HTTP fingerprint;
- HTTP header order/case;
- proxy headers;
- HTTP version;
- User-Agent/header consistency;
- JavaScript browser fingerprints;
- navigator properties;
- WebGL fingerprints;
- audio fingerprints;
- Picasso-style fingerprints;
- behavioural signals;
- mouse movements;
- touch events;
- key presses;
- cookies;
- session IDs;
- JavaScript obfuscation;
- JavaScript virtual machines;
- encoded/encrypted payloads;
- WebSockets;
- sendBeacon API.

## Threat types covered

The article is not organised around OWASP Automated Threat categories.

Directly relevant to:

- bot detection architecture;
- passive detection;
- client-side signal collection;
- browser automation detection;
- scraper detection;
- rate limiting of unique visitors.

Indirect OAT mappings:

- **OAT-011 Scraping** — strong relevance because single-page scraping and passive detection limits are discussed.
- **OAT-008 Credential Stuffing** — indirect relevance where login workflows provide more behavioural/session data.
- **OAT-019 Account Creation** — indirect relevance where browser/device/session risk scoring is used.
- **OAT-005 Scalping / OAT-013 Sniping / OAT-021 Denial of Inventory** — indirect relevance for high-demand workflows protected by bot detection.
- **OAT-009 CAPTCHA Defeat** — mentioned only as contrast with passive detection; not a CAPTCHA-defeat source.

## What is strong

- Very useful architecture source.
- Explains the client/server trust boundary plainly: client-provided data is not automatically trustworthy.
- Useful for connecting multiple evidence strands:
  - IP/proxy ecosystem;
  - TLS/JA4/protocol fingerprints;
  - HTTP/2/client coherence;
  - browser fingerprints;
  - cookies/sessions;
  - JavaScript client-side detection;
  - VM obfuscation and WASM-style protection.
- Strong complement to the DataDome VM-obfuscation entry because it explains why client-side detection libraries are exposed and why vendors may obfuscate or virtualise them.
- Useful as a “map of the detection stack” before more specific academic/vendor entries.
- Good for a simple-to-complex explanation: detection begins before the page loads, then accumulates more evidence as the browser sends requests and executes scripts.

## What is weak or limited

- Personal technical blog, not peer-reviewed.
- The author states they had not built a fully functional anti-bot system.
- Some statements are judgement-based or speculative.
- The source is from 2021 and should not be treated as current state-of-the-art for 2026 products.
- It contains reverse-engineering/bypass-oriented discussion that should not be reproduced operationally.
- It does not provide quantitative evaluation.
- It does not provide privacy/legal analysis.
- It should not be used as authoritative evidence that a given vendor works or fails.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  The architecture of passive bot detection as a multi-signal client/server problem, including the problem of detecting bots when all browser-provided data may be spoofed.

- **What does it fail to represent?**  
  It does not represent a production-grade bot-management system, live vendor telemetry, or measured detection accuracy. It is a conceptual/technical map.

- **What additional evidence would be needed to go further?**  
  Vendor telemetry, academic bot-detection evaluations, browser-fingerprinting studies, protocol-fingerprinting papers, privacy/legal reviews, and controlled tests against real bot-management systems.

## What it cannot show

- It cannot show bot prevalence.
- It cannot show detection performance.
- It cannot show that specific signals are sufficient.
- It cannot show that client-side detection can or cannot be bypassed.
- It cannot show current anti-bot product architecture.
- It cannot replace Cloudflare/HUMAN/DataDome vendor sources or academic bot-detection studies.
- It cannot establish legal/privacy acceptability of fingerprinting or behavioural collection.

## Project impact

Use this as a **full bot-detection architecture foundation entry**.

Best uses:

- introduce passive bot detection as a layered signal problem;
- explain client-side trust limits and spoofability;
- connect IP, TLS, HTTP, browser, session, and behavioural signals;
- support the “client-side detection is an attack surface” point;
- provide conceptual scaffolding for the DataDome VM-obfuscation, JA4/TLS, browser-fingerprinting, proxy, CAPTCHA, and ML detection entries.

Do not use it as:

- empirical evidence;
- vendor performance evidence;
- current product documentation;
- legal/privacy authority;
- operational bypass guidance.

## Relationship to other register entries

- **DataDome VM-based obfuscation**: direct complement. Incolumitas explains why exposed JS detection code is vulnerable; DataDome shows a vendor hardening response.
- **Pushan / VM deobfuscation**: relevant to the arms race around protected detection logic.
- **Xu et al. layered obfuscation**: stronger academic background for layered obfuscation as risk management.
- **JA4/TLS paper**: protocol-fingerprint source; Incolumitas provides architecture context.
- **Laperdrix / Berke browser fingerprinting**: browser/device-fingerprint foundations; Incolumitas shows where they fit in bot detection.
- **Proxy ecosystem entries**: IP reputation and proxy detection appear as early server-side signals.
- **NIST / ASVS / PortSwigger**: account/session controls and login-abuse context.
- **CAPTCHA entries**: active challenges sit beside passive detection; this source is mainly passive detection.

## Dual-use containment

High dual-use. The source discusses detection signals and reverse-engineering of client-side payloads. Use it as architecture and signal-taxonomy material only. Avoid reproducing step-by-step bypass, reverse-engineering, or spoofing instructions.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `tschacher-2021-architecture-of-bot-detection-services` |
| Title | *On the Architecture of Bot Detection Services* |
| Author | Nikolai Tschacher |
| Year | 2021 |
| Category | public technical analysis / bot-detection architecture |
| Evidence basis | technical explainer / architecture analysis / attacker-aware commentary |
| Operational proximity | architecture |
| Signals / techniques | IP reputation; TCP/IP fingerprints; TLS fingerprints; HTTP headers; browser fingerprints; JavaScript signals; behaviour; cookies; sessions; JS obfuscation; JavaScript VMs |
| Threat types | generic bot detection; especially scraping and browser automation; indirect relevance to credential stuffing/account creation/scalping where workflows collect more evidence |
| Project use | Full architecture foundation for passive bot detection and client-side signal trust limits |
| Main caution | Blog/explainer, not empirical or current product evidence; high dual-use if made operational |
| Entry file | `tschacher-2021-architecture-of-bot-detection-services.md` |
