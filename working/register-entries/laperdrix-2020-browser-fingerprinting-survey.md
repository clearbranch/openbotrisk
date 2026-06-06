# Laperdrix et al. (2020) - Browser Fingerprinting: A survey

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF files.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Laperdrix, P., Bielova, N., Baudry, B., & Avoine, G. (2020). *Browser Fingerprinting: A survey*. ACM Transactions on the Web, 14(2), Article 8, 1–33. https://doi.org/10.1145/3386040
- **Canonical uploaded source**: `Lape-etal-20-TWEB.pdf`
- **Alternate uploaded source**: `1905.01051v2.pdf` — arXiv v2 preprint, November 2019.
- **Category**: academic
- **Evidence basis**: review / methods-taxonomy / foundations
- **Operational proximity**: foundational - literature survey and taxonomy, not observed-use measurement.
- **Tags**: browser-fingerprinting, device-fingerprinting, user-agent, http-headers, javascript-apis, canvas, webgl, audiocontext, fonts, plugins, extensions, entropy, anonymity-sets, panopticlick, amiunique, tracking, privacy, defences

## Source handling

The two uploaded PDFs represent the same source family. The TWEB/ACM-formatted 2020 paper should be the canonical register source. The arXiv v2 PDF should be noted as the preprint/alternate version, not added as a second extraction row.

This is also distinct from:

- Laperdrix et al. (2016), *Beauty and the Beast: Diverting Modern Web Browsers to Build Unique Browser Fingerprints* / AmIUnique empirical study.
- Berke et al. (2025), *How Unique is Whose Web Browser?*, which updates the fingerprinting line with demographics and an open dataset.

## What it claims

- Browser fingerprinting collects information through a browser to build a device/browser fingerprint.
- Fingerprinting is stateless compared with cookies because it does not require a unique identifier stored in the browser.
- Browser fingerprinting is rooted in normal web functionality: browsers have always exposed information to improve compatibility and user experience.
- Modern browser APIs expanded the fingerprinting surface by exposing device, graphics, audio, storage, extension, and configuration details.
- Browser fingerprinting cannot be fixed with a simple patch because it emerges from the diversity and functionality of the web platform.
- The paper surveys how fingerprinting works, how uniqueness is evaluated, how it is used, and what defences exist.

## What evidence it provides

- A survey-level definition of browser/device fingerprints and browser fingerprinting.
- Historical explanation of why fingerprinting became possible:
  - User-Agent header and compatibility signalling;
  - JavaScript bridging browser and native environment;
  - modern web APIs such as Canvas, WebGL, Web Audio, WebRTC, Geolocation, WebAssembly, and browser extensions.
- A summary of major fingerprinting studies:
  - Mayer’s 2009 small-scale study;
  - Eckersley / EFF Panopticlick;
  - Laperdrix / AmIUnique;
  - Gómez-Boix et al. large-scale publisher study.
- A taxonomy of fingerprint attributes and sources:
  - HTTP headers;
  - JavaScript-accessible browser/device state;
  - plugins;
  - fonts;
  - local/session storage;
  - timezone;
  - screen resolution and colour depth;
  - platform;
  - Canvas;
  - WebGL;
  - ad-block detection;
  - extensions;
  - AudioContext;
  - Battery Status API;
  - JavaScript conformance;
  - CSS querying;
  - benchmarking.
- An explanation of standard evaluation metrics:
  - Shannon entropy;
  - normalised entropy;
  - anonymity sets.
- A survey of defences:
  - blocking access to attributes;
  - spoofing / lying;
  - randomisation;
  - introducing noise;
  - standardisation / making users look alike;
  - browser-level and extension-level defences.
- Discussion of practical challenges:
  - usability trade-offs;
  - breakage risk;
  - arms race between fingerprinting and anti-fingerprinting;
  - business and legislative pressures.

## Signals or techniques mentioned

- User-Agent
- Accept / Accept-Language / Accept-Encoding headers
- Cookie and storage support
- localStorage and sessionStorage
- timezone
- screen resolution and colour depth
- plugins
- fonts
- HTTP header list/order
- platform
- Do Not Track
- Canvas rendering
- WebGL vendor and renderer
- AudioContext
- browser extensions
- extension side effects
- JavaScript engine conformance
- CSS properties
- font metrics
- CPU/GPU benchmarking
- Battery Status API
- ad-block detection

## Threat types or risk types covered

- cross-site tracking without cookies
- stateless device identification
- browser/device re-identification
- passive and active fingerprinting surfaces
- web tracking
- privacy loss through browser uniqueness
- fingerprinting as a complement to cookies or authentication
- fingerprinting as dual-use security/fraud signal

## Main quantitative details summarised by the paper

| Study / source | Reported detail |
|---|---:|
| Mayer 2009 | 1,278 of 1,328 clients uniquely identified in a small study |
| Panopticlick / Eckersley 2010 | 470,161 fingerprints; 83.6% unique; 94.2% unique when Flash/Java enabled |
| AmIUnique / Laperdrix et al. 2016 | 118,934 fingerprints; 89.4% desktop unique; 81% mobile unique |
| Gómez-Boix et al. 2018 / Hiding in the Crowd | 1,816,776 desktop and 251,166 mobile fingerprints; much lower uniqueness than volunteer studies |
| FP-Stalker / Vastel et al. | Fingerprints evolve over time; linking can track devices across changes for meaningful periods |

## What is strong

- Strongest broad foundation source for browser fingerprinting.
- Good entry point for readers who need the basics without jumping straight into attacker tooling or vendor docs.
- Useful for explaining why fingerprinting is not just “one header” or “one cookie replacement”; it is a combination of many browser/device signals.
- Good bridge between MDN foundations and bot-detection vendor documents.
- Useful for showing that fingerprinting has legitimate and illegitimate/security and privacy uses.
- Useful for explaining why browser-fingerprinting evidence should be handled carefully: uniqueness depends on the population sampled, the attributes collected, and time.

## What is weak or limited

- This is a survey, not a primary measurement study.
- It does not provide new 2026 data.
- It does not measure modern anti-bot systems or current AI-agent/browser-automation traffic.
- It does not directly observe malicious scraping, credential stuffing, ticket bots, or slot-sniping.
- Some API surfaces and browser behaviours have changed since publication.
- It deliberately focuses on information collected through the browser and does not deeply cover IP/geolocation or packet-level network fingerprinting.
- It is a foundation source; later sources are needed for current web-bot detection, GDPR/AI Act compliance, AI crawlers, agentic automation, and commercial bot-management controls.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** The browser/device fingerprinting layer used in tracking, fraud detection, bot detection, and privacy-invasive identification.
- **What does it fail to represent?** It does not show current bot abuse volume, operational attacker behaviour, vendor detection efficacy, or legal/enforcement outcomes.
- **What additional evidence would be needed to go further?** Current vendor telemetry, independent in-the-wild measurement, bot-detection/privacy review papers, and operational sources showing how fingerprinting is used in anti-abuse systems.

## What it cannot show

- It cannot prove browser fingerprinting is used maliciously on a particular website.
- It cannot quantify current prevalence.
- It cannot show modern anti-bot detection performance.
- It cannot establish compliance under GDPR, ePrivacy, or the AI Act.
- It cannot replace empirical papers such as AmIUnique, Hiding in the Crowd, or Berke et al. 2025.

## Project impact

Use this as a **core browser-fingerprinting foundation source**. It should probably sit in the foundations or academic-literature section and be cross-linked to:

- MDN User-Agent / HTTP headers / cookies;
- Berke et al. 2025 demographics/fingerprinting paper;
- Martínez Llamas et al. 2025 bot detection/privacy/GDPR/AI Act review;
- Cloudflare detection engines / Detection IDs;
- Niespodd browser-fingerprinting GitHub entry;
- scraper-side bypass sources that discuss browser fingerprints and header consistency.

It supports the project’s simple-to-complex structure: start with User-Agent and HTTP headers, then browser APIs, then fingerprint combinations, then privacy/governance and bot-detection use.

## Best placement in the evidence register

- Primary section: **Foundations** or **Academic and research**
- Secondary section: **Browser fingerprinting foundations**
- Not a threat-surface observed-use source.

## Possible register row

| Field | Value |
|---|---|
| Register id | `laperdrix-2020-browser-fingerprinting-survey` |
| Title | *Browser Fingerprinting: A survey* |
| Category | academic |
| Evidence basis | review / methods-taxonomy / foundations |
| Operational proximity | foundational |
| Tags | browser-fingerprinting; device-fingerprinting; user-agent; http-headers; javascript-apis; canvas; webgl; audiocontext; fonts; plugins; extensions; entropy; anonymity-sets; panopticlick; amiunique; tracking; privacy; defences |
| Project use | Core foundation source for browser/device fingerprinting concepts, attributes, metrics, history, and defences |
| Main caution | Survey/foundation source; not observed bot-abuse evidence or current anti-bot performance evidence |
