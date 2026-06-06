# Cloudflare - Bot detection engines

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: live official Cloudflare developer documentation.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Cloudflare. 2026. *Bot detection engines - Cloudflare bot solutions docs*. Cloudflare Developers. Accessed 2026-06-06.
- **Source URL or path**: `https://developers.cloudflare.com/bots/concepts/bot-detection-engines/`
- **Date accessed**: 2026-06-06
- **Category**: vendor
- **Evidence basis**: methods-taxonomy
- **Operational proximity**: capability - vendor description of detection methods and data sources.
- **Tags**: cloudflare, bot-detection, heuristics, javascript-detections, machine-learning, anomaly-detection, bot-score, browser-signals, headers, session-characteristics

## What it claims

- Cloudflare uses multiple detection engines because simple and sophisticated bots require different detection strategies.
- Simple bots can be caught by pattern matching against known signatures; sophisticated bots require machine learning and behavioural analysis.
- The heuristics engine processes all requests and matches against malicious fingerprints.
- JavaScript Detections identify headless browsers and other malicious fingerprints using lightweight invisible JavaScript injection on the client side.
- The Machine Learning engine distinguishes human and bot traffic and maps a predicted probability of being human to the 1-99 Bot Score.
- Model inputs include request features, headers, session characteristics, and browser signals.

## What evidence it provides

- Strong Cloudflare source for the “defence is layered” point.
- Aligns with the academic taxonomy already in the register: network/request features, headers, browser signals, JavaScript execution, ML, and behavioural/anomaly-style approaches.
- Useful as a vendor-side mirror of scraper-side bypass sources. The same layers appear from the defender perspective: headers, sessions, browser signals, fingerprints, and client-side scripts.

## Signals or techniques mentioned

- known signatures
- heuristic checks
- malicious fingerprints
- invisible JavaScript injection
- headless-browser detection
- headers
- session characteristics
- browser signals
- supervised machine learning
- bot score
- anomaly detection / outlier detection

## Threat types covered

- simple automation
- headless-browser automation
- sophisticated bots
- traffic that mimics legitimate users
- malicious fingerprints

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** Production detection of automated web traffic across Cloudflare-protected properties.
- **What does it fail to represent?** It gives a product-method summary but not the full model, input list, validation method, false-positive rate, false-negative rate, or independent audit.
- **What additional evidence would be needed to go further?** Independent detection-efficacy tests, field telemetry with denominators, model audit material, or site-specific detection logs.

## What it cannot show

- It cannot prove that JavaScript Detections catch all headless browsers.
- It cannot prove the ML engine performs well against adaptive bots.
- It cannot show what data is necessary versus excessive from a privacy standpoint.
- It cannot show real-world prevalence or attacker intent.

## Project impact

Use this as a central source for the defensive-methods taxonomy. It shows why your project should not treat “bot detection” as one thing.

## Possible register row

| Field | Value |
|---|---|
| Register id | `cloudflare-2026-bot-detection-engines` |
| Title | *Bot detection engines - Cloudflare bot solutions docs* |
| Category | vendor |
| Evidence basis | methods-taxonomy |
| Operational proximity | capability |
| Tags | cloudflare; bot-detection; heuristics; javascript-detections; machine-learning; anomaly-detection; bot-score; browser-signals; headers; session-characteristics |
| Project use | Defensive-methods taxonomy and bridge to scraper-side evasion layers |
| Main caution | Vendor description of methods; not independent performance evidence |
