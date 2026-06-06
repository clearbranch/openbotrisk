# Cloudflare - Bot Management

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: live official Cloudflare developer documentation.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Cloudflare. 2026. *Bot Management - Cloudflare bot solutions docs*. Cloudflare Developers. Accessed 2026-06-06.
- **Source URL or path**: `https://developers.cloudflare.com/bots/get-started/bot-management/`
- **Date accessed**: 2026-06-06
- **Category**: vendor
- **Evidence basis**: capability-doc
- **Operational proximity**: capability - defensive product documentation.
- **Tags**: cloudflare, bot-management, bot-score, waf-custom-rules, workers, bot-analytics, endpoint-policy, enterprise-bot-detection

## What it claims

- Bot Management is an Enterprise paid add-on for identifying automated traffic, taking actions, and viewing analytics.
- It generates a per-request bot score from 1 to 99; Cloudflare says scores below 30 are commonly associated with bot traffic.
- Customers can use bot score in WAF custom rules or Workers, for example challenging low-scoring requests on a login endpoint while allowing traffic on a public blog.
- Customers can analyse scores in Bot Analytics or Logs to tune rules over time.
- Cloudflare recommends enabling automatic updates to its machine-learning models for Enterprise customers.

## What evidence it provides

- Strong vendor evidence for how modern bot management is operationalised: per-request scoring, endpoint-specific rules, analytics feedback, and action selection.
- Supports the project argument that bot defence has moved beyond binary block/allow decisions.
- Useful for explaining why the same traffic may be treated differently depending on endpoint sensitivity.

## Signals or techniques mentioned

- bot score
- WAF custom rules
- Workers
- Bot Analytics
- logs
- verified bots
- JavaScript detections
- static-resource protection
- machine-learning model updates

## Threat types covered

- bot traffic
- login automation
- application abuse
- endpoint-specific automated abuse
- unwanted access to protected resources

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** Bot traffic management on production websites, especially where different paths have different abuse risk.
- **What does it fail to represent?** It does not report measured success rates, detection error rates, or independent validation.
- **What additional evidence would be needed to go further?** Cloudflare logs/telemetry studies, customer case studies with denominators, independent red-team evaluations, or academic measurement.

## What it cannot show

- It cannot prove that a bot score threshold is correct for a given site.
- It cannot show whether a request below score 30 is malicious.
- It cannot validate Cloudflare’s ML model performance.
- It cannot show real-world attack prevalence.

## Project impact

Use this as the primary Cloudflare entry for per-request scoring and policy action. It fits the “simple to complex” explanation: basic rule → score → endpoint-specific rule → analytics feedback loop.

## Possible register row

| Field | Value |
|---|---|
| Register id | `cloudflare-2026-bot-management` |
| Title | *Bot Management - Cloudflare bot solutions docs* |
| Category | vendor |
| Evidence basis | capability-doc |
| Operational proximity | capability |
| Tags | cloudflare; bot-management; bot-score; waf-custom-rules; workers; bot-analytics; endpoint-policy; enterprise-bot-detection |
| Project use | Evidence of per-request scoring and endpoint-specific bot policy |
| Main caution | Product documentation; does not independently validate model accuracy or effectiveness |
