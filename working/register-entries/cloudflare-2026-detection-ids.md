# Cloudflare - Detection IDs

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: live official Cloudflare developer documentation.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Cloudflare. 2026. *Detection IDs - Cloudflare bot solutions docs*. Cloudflare Developers. Accessed 2026-06-06.
- **Source URL or path**: `https://developers.cloudflare.com/bots/additional-configurations/detection-ids/`
- **Date accessed**: 2026-06-06
- **Category**: vendor
- **Evidence basis**: capability-doc
- **Operational proximity**: capability - customer-facing control and logging documentation.
- **Tags**: cloudflare, detection-ids, detection-tags, header-order, bot-management, waf-custom-rules, logpush, bot-analytics, configurable-heuristics

## What it claims

- Detection IDs are static rules that detect predictable bot behaviour with no overlap with human traffic.
- Each ID maps to a detection method such as heuristics, verified-bot detections, or anomaly detections.
- One example given is detecting when a client sends headers in a different order than the browser it claims to be.
- A request can trigger multiple Detection IDs.
- Detection IDs can be used in custom rules, advanced rate limiting, transform rules, Workers, Bot Analytics, Security Analytics, and Logpush.

## What evidence it provides

- Useful for a concrete example of a low-level detection signal: inconsistency between claimed browser identity and header ordering.
- Supports a key project claim: modern bot detection looks for coherence across layers, not only individual fields such as User-Agent.
- Shows how detections become operational controls: detection signal → analytics/logging → rule expression → block/challenge/allow/alternate content.

## Signals or techniques mentioned

- detection IDs
- detection tags
- claimed-browser consistency
- HTTP header order
- heuristics
- verified-bot detections
- anomaly detections
- Logpush
- WAF custom rules
- Workers

## Threat types covered

- predictable bot behaviour
- header-order mismatch
- browser impersonation
- bot traffic against specific endpoints
- false-positive management through configurable heuristics

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** Operational bot detection where individual low-level signals are exposed for rule-making and troubleshooting.
- **What does it fail to represent?** It does not expose the full list of detection IDs, the exact rules, or performance data.
- **What additional evidence would be needed to go further?** Real logs showing triggered IDs, independent tests against browser automation tools, or Cloudflare case studies with outcome metrics.

## What it cannot show

- It cannot prove that a specific Detection ID has zero overlap with human traffic in all settings.
- It cannot show the false-positive rate for header-order checks.
- It cannot show whether bots can adapt to these checks.
- It cannot establish prevalence.

## Project impact

Use this as the concrete Cloudflare entry for “coherence checks”. It is useful beside sources discussing User-Agent spoofing, TLS/HTTP fingerprints, and scraper-side advice about aligning request layers.

## Possible register row

| Field | Value |
|---|---|
| Register id | `cloudflare-2026-detection-ids` |
| Title | *Detection IDs - Cloudflare bot solutions docs* |
| Category | vendor |
| Evidence basis | capability-doc |
| Operational proximity | capability |
| Tags | cloudflare; detection-ids; detection-tags; header-order; bot-management; waf-custom-rules; logpush; bot-analytics; configurable-heuristics |
| Project use | Concrete example of browser-impersonation/coherence detection |
| Main caution | No independent validation or false-positive metrics |
