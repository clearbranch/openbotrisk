# Quo vadis, crawlers? Progress and what's next on safeguarding our infrastructure (Wikimedia)

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: Claude (chat interface)
- **Model name + version, if known**: Claude Opus 4.8
- **Source access**: full text (fetched from the live page; HTML blog post, no individual byline captured)
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Wikimedia Foundation (2026). *Quo vadis, crawlers? Progress and what's next on safeguarding our infrastructure.* Diff (Wikimedia Foundation blog), 2026-03-26.
- **Source URL or path**: `https://diff.wikimedia.org/2026/03/26/quo-vadis-crawlers-progress-and-whats-next-on-safeguarding-our-infrastructure/` (fetched 2026-06-06; resolves). Companion/prior post (~2025, "one year ago") referenced but not captured — candidate follow-up source.
- **Date accessed**: 2026-06-06
- **Category**: threat-surface — **flagged judgment call**: this is a *first-party operator account*, which does not map cleanly to foundations/vendor/academic/threat-surface. Filed under threat-surface as the least-bad fit (target/operator-side evidence of abuse + defence). May motivate an explicit "operator / first-party" category or tag (see Project impact).
- **Evidence basis**: empirical-operational (first-party, self-reported); threat-intel — a site operator's narrative account of abuse against its own infrastructure plus one quantified operational figure; not a rigorous study, not independently verifiable.
- **Operational proximity**: `observed` (first-party operator-reported). Wikimedia reports real abuse against its own real infrastructure (the most *direct* observed-abuse-against-a-named-target vantage in the register so far — operator reporting abuse against itself). It caps at `observed`, not `measured`, because it is self-reported operator telemetry with a single headline figure and no independent/controlled quantification — the same ceiling applied to vendor telemetry (cf. the F5 entry).
- **Tags**: scraping, ai-crawler, residential-proxy, rate-limiting, bot-detection, infrastructure, operator-account

## What it claims

- Automated traffic to Wikimedia projects has risen sharply, driven largely by crawlers extracting content to train generative-AI systems; crawlers hit every part of the ecosystem (articles, media, developer platforms), risking system overload and degraded experience for readers and contributors.
- A structural imbalance: more content extraction, fewer humans contributing back (partly because LLM search summaries/chatbots reduce click-through to sources) — a web-wide "more bot traffic, fewer human users" trend Wikimedia says it is also seeing.
- Wikimedia's response prioritises access for humans and "mission-oriented" traffic: updated robot policy, improved bot detection/defence, investment in API infrastructure, and steering high-volume commercial reusers to paid Wikimedia Enterprise rather than scraping.
- Operational result: Wikimedia is currently **blocking or throttling ~25% of all automated requests from crawlers that don't adhere to its policies (up to billions of requests/day)**, and expects this to rise as detection improves. Global API rate limits began rolling out, with a second phase planned April 2026.
- Access model is **identification-tiered**: stronger identification → higher rate limits; crawling and API use remain allowed within the robot policy; higher-rate scraping is generally restricted while higher API limits are "easily" obtainable for identified bots/tools.
- The new generation of bots behaves adversarially: sending requests as fast as possible, spoofing real-browser identities, and circumventing rate limits — a departure from traditional crawlers (search engines) that slowed on errors, self-identified, and returned visitors via indexing.
- Evasion has shifted to **residential proxies**: as operators tightened limits on datacentre/individual sources, crawl operators began buying access to people's home/mobile connections to hide extraction inside legitimate browsing traffic; these networks can span hundreds of millions of IPs, leaving operators little they can do, and are framed as the main driver of the web-wide rise in "verify you're a human" challenges.
- Next steps: scale detection for fast-changing behaviour (e.g. residential proxies), fine-tune API limits, build an Attribution API, and harden media infrastructure against heavy scraping.

## What it provides

- A first-party operator narrative with one quantified operational datapoint (~25% of non-compliant automated requests blocked/throttled; "up to billions of requests per day").
- A described (not benchmarked) defence architecture: updated robot policy, identification-tiered API rate limits, a paid high-volume channel (Wikimedia Enterprise), and ongoing detection improvements.
- An operator-side characterisation of the current adversary (AI-training crawlers, identity spoofing, rate-limit circumvention, residential-proxy evasion).

## Signals or techniques mentioned

- Adversary behaviours: ignoring robots.txt / historical crawler norms, maximal request rates, real-browser identity spoofing, rate-limit circumvention.
- Evasion infrastructure: **residential-proxy networks** (home/mobile connections sold to hide extraction in legitimate traffic; hundreds of millions of IPs) — described at the class level, no operational detail.
- Defences: robot-policy updates, identification-tiered API rate limiting, a dedicated high-volume paid channel (Enterprise), bot detection/defence tooling, a planned Attribution API, media-infrastructure hardening.
- Implicit detection challenge: readers, contributors, responsible bots, and abusive bots share the same access points, so defences must avoid impeding humans — a constraint shaping the whole approach.

## Threat types covered

Primarily **scraping / aggressive crawling** (OAT-011 Scraping) for AI-training data, with a **resource-exhaustion / infrastructure-strain** dimension (volumetric crawling degrading service). Residential-proxy evasion is cross-cutting infrastructure relevant to many abuse types, not an OAT itself. Note: this is *content scraping against an open knowledge platform*, not the credential-stuffing / ATO / scalping abuse types or the booking-system target archetype the project uses as its worked example.

## Framing distance

- **What real-world problem does it approximate?** What large-scale AI-training scraping looks like from a major content platform's operational vantage, and one operator's tiered-identification + rate-limiting + detection response, as of early 2026. It is a rare *named-operator* account of observed abuse against its own infrastructure.
- **What does it fail to represent?** It is a non-rigorous first-party blog: no methodology, a single self-reported headline figure, no subtype breakdown, no detection-signal detail, no independent verification. The target is an open, mission-driven knowledge platform (free content; explicit goals of not impeding readers/contributors and not tracking users) — so both the abuse type (content scraping for AI) and the defence calculus differ materially from a commercial booking/e-commerce target. It speaks to scraping/crawling, not credential stuffing, ATO, or scalping.
- **What additional evidence would be needed to go further?** Independent measurement of the same traffic; data from commercial targets; abuse-subtype breakdown; detection-method detail; and before/after or false-positive data on the defence's efficacy.

## What it cannot show

- It cannot establish prevalence beyond Wikimedia's own infrastructure; the ~25% blocked/throttled figure is self-reported and platform-specific.
- It cannot demonstrate defence efficacy rigorously — no false-positive rate, no before/after, no independent audit.
- The "residential proxies span hundreds of millions of IPs" and "main cause of human-verification challenges" statements are operator assertions/inferences, not measured figures.
- Its relevance to the project's core abuse types (credential stuffing, ATO, scalping) is **indirect** — via the shared evasion infrastructure (residential proxies, identity spoofing), not via the scraping abuse itself.
- No actor/campaign attribution and no criminal-economics detail to strip; the residential-proxy "business model" is referenced only as an evasion-infrastructure category (in-scope territory), not as money-flow detail. Dual-use containment is not engaged — there are no recipes or exploit detail in the source.

## Project impact

- **First first-party operator account in the register** — a named target's own observed-use evidence, distinct from vendor material and academic measurement. It broadens the observed-use lane with an operator vantage the corpus otherwise lacks.
- **Independent (operator-side) corroboration of two vendor claims**: that residential-proxy / IP-rotating botnets defeat IP-based and WAF rate limiting (corroborates SRC-010 HUMAN's WAF-insufficiency point from a non-vendor source), and that modern bots spoof browser identities and ignore robots.txt/rate limits. Valuable precisely because it is not a vendor selling the remedy.
- **Concrete observed datapoint** for a Background/landscape section: a major platform blocks/throttles ~25% of non-compliant automated requests (billions/day) and is rolling out tiered API rate limits — operator-reported, attributed as such.
- **Anchor for the AI-crawler / AI-shift section**: operator-side evidence of the AI-training-scraping surge and the residential-proxy evasion shift; pairs with the FP-Agent entry (agent detectability) and the OpenWPM entry (detection-side measurement) to give the AI-shift thread vendor-free corroboration from three angles.
- Illustrates the **identification-tiered access** defence pattern (stronger identification → higher limits; paid high-volume channel) and the robots.txt / rate-limit / WAF insufficiency argument — useful for a Defences/Foundations page.
- **Proximity calibration**: a third worked example of the axis — arguably the most *direct* observed-abuse-against-a-named-target source so far (operator reporting abuse against itself), yet still `observed` not `measured` because self-reported and unquantified beyond one figure. Sits alongside F5 (vendor `observed`) and the academic `measured` sources.
- **Flags**: (1) category fit is a judgment call — consider an explicit operator/first-party category or tag if more such accounts arrive; (2) treat ~25% and "billions/day" as operator-reported, not independently verified; (3) a prior (~2025) Wikimedia post is referenced and is a candidate companion source.
