# Agentic Visibility: How to See AI Agents in Your Traffic

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: full text from attached PDF export of HUMAN blog page
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: McArtney, Ian / HUMAN Security. 2026. *Agentic Visibility: How to See AI Agents in Your Traffic*. HUMAN Blog, 20 April 2026.
- **Source URL or path**: local uploaded PDF: `Agentic Visibility_ How to See AI Agent Traffic.pdf`; original public URL not stated in the PDF export and not independently confirmed during extraction.
- **Date accessed**: 2026-06-06
- **Category**: vendor
- **Evidence basis**: capability-doc
- **Operational proximity**: capability — the source primarily describes HUMAN's claimed capability to identify, classify, measure, and control AI-agent traffic. It cites separate HUMAN benchmark figures about AI traffic growth, but this source itself is not a production telemetry report and does not independently evidence observed abuse against targets.
- **Tags**: vendor, capability-doc, ai-agent, agentic-visibility, ai-agent-traffic, browser-native-automation, agent-classification, trust-classification, cryptographic-verification, http-message-signatures, key-directories, session-analysis, route-analysis, marketing-analytics, bot-vs-human, agent-governance

## What it claims

- HUMAN claims AI agents are actively browsing websites, researching products, comparing options, and interacting with digital environments used for marketing measurement and revenue generation.
- The source says HUMAN's 2026 *State of AI Traffic & Cyberthreat Benchmark Report* found AI-driven traffic grew 187% in 2025, automated traffic expanded eight times faster than human traffic year over year, and agent-driven traffic grew 7,851% in 2025.
- The source claims most organisations have limited visibility into this activity because traditional analytics tools were not built to distinguish humans, traditional bots, and AI agents.
- It claims this visibility gap can distort performance data, attribution, and customer journey analysis.
- It defines **agentic visibility** as the ability to identify, classify, and measure AI-agent traffic as a distinct website visitor segment, separate from human users and traditional bots.
- It says agentic visibility has three requirements: identification of AI-agent requests, classification of verified agents versus spoofed/abusive/unknown automation, and measurement of volume, navigation, and intent.
- HUMAN describes its Sightline platform as providing an AI Agents Monitoring Dashboard that shows total AI-agent request volume, monitored or allowed sessions, named agents interacting with a site, routes those agents navigate, and last-seen activity.
- The source says teams can drill down from aggregate traffic to individual sessions to see how a specific agent navigated the site, what it searched for, and whether it completed its task.
- It distinguishes AI agents from scrapers by claiming a scraper pulls pages on a schedule, while an AI agent acts on behalf of a user, navigates interactively, reasons about what it finds, and often completes a task such as search, comparison, purchase, or booking.
- HUMAN claims grouping AI agents and scrapers together obscures distinctions that matter for performance data, customer journey mapping, and fraud analysis.
- It claims Sightline identifies and classifies AI agents as a separate category of visitors from both humans and traditional bots.
- It says this lets teams understand how much traffic is agent-driven, separate agent activity from human engagement, and avoid contaminating performance data with blended signals.
- The source claims Sightline can show routes targeted by agents, session activity patterns, generated pageviews, traffic distribution over time, and individual navigation paths.
- HUMAN describes a trust-based classification model for AI agents: High Trust, Medium Trust, and Low Trust.
- High Trust agents are described as cryptographically verified on each request using mechanisms such as HTTP Message Signatures and key directories; they consistently identify themselves and show limited or no evidence of abuse, but trust can be lowered if behaviour becomes malicious.
- Medium Trust agents are described as not yet cryptographically verified but having stable identity signals or private indicators, requiring ongoing monitoring before promotion to High Trust.
- Low Trust agents are described as unverified, easily spoofable, inconsistent in declaring identity, potentially associated with abuse or deprecated signals, and often recommended for blocking or heavy restriction.
- The source claims AI agents are now a measurable audience segment that can be analysed using traffic distribution, unique visitors, request volume, and engagement patterns.
- It frames the operational progression as **Visibility → Understanding → Control**, with AgenticTrust providing enforcement and control when organisations choose to block or restrict malicious or low-trust agents.
- The source says AI agents create both opportunity and risk for brands and agencies: without visibility, organisations face distorted metrics, unclear attribution, and potential abuse from inauthentic agents.

## What evidence it provides

- The source provides a vendor product explanation and dashboard screenshots rather than an independently evaluated study.
- The headline growth figures for AI-driven traffic and agent-driven traffic are attributed to HUMAN's separate 2026 *State of AI Traffic & Cyberthreat Benchmark Report*; this blog source does not reproduce the benchmark methodology or raw data.
- The dashboard screenshots show example product outputs: trusted AI-agent lists, named agents such as Atlas, ChatGPT Agent, Comet Browser, Browsersec Cloud, and Flow, route targeting, traffic volume over time, allowed versus blocked requests, and individual Atlas sessions.
- The screenshots provide concrete examples of what HUMAN says can be displayed, but the source does not state whether the screenshots are real customer data, demo data, anonymised data, or illustrative mock-ups.
- The source explains trust classes and names some classification inputs, including cryptographic verification, key directories, stable identity signals, private indicators, behavioural evidence of abuse, and spoofable user-agent strings.
- It does not provide validation metrics, false-positive or false-negative rates, sample size, site coverage, customer mix, geographic coverage, classifier details, independent audit results, or comparison against alternative analytics tools.
- It does not provide evidence that the claimed dashboard capabilities improve security outcomes, marketing attribution, or fraud detection in practice.
- The source's distinction between AI agents and scrapers is asserted as a conceptual framing; it is not supported by a dataset showing separable behaviour classes.

## Signals or techniques mentioned

- AI-agent identification as distinct from human users and traditional bots.
- Trust-based agent classification: High Trust, Medium Trust, Low Trust.
- Cryptographic verification per request.
- HTTP Message Signatures.
- Key directories.
- Stable identity signals.
- Private indicators.
- Detection of spoofed, abusive, unknown, or unverified automation.
- User-agent ambiguity and reuse of abusable user-agent strings.
- Route/category analysis.
- Session-level analysis.
- Individual navigation path reconstruction.
- Request-volume monitoring.
- Unique visitor grouping.
- Pageview and engagement-pattern analysis.
- Allowed, monitored, blocked, or restricted agent-session states.
- Policy enforcement through AgenticTrust.

## Threat types covered

- Not threat-specific in the OWASP OAT sense. The source is primarily about AI-agent visibility and classification rather than a specific abuse pattern.
- Adjacent project vocabulary: AI-agent traffic, browser-native automation, agentic commerce, content retrieval, search/product discovery, analytics contamination, spoofed agents, low-trust automation, scraping-adjacent behaviour, inauthentic automation.
- Possible adjacent OAT relevance: scraping, transaction abuse, and account/checkout-flow exposure, but the source does not establish that the observed or classified traffic is malicious or map it directly to OWASP Automated Threat categories.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** It approximates the defender-side problem of seeing and governing AI-agent traffic as a new class of website visitor. It is useful for understanding how at least one major bot-management vendor is framing the move from binary bot/human analytics toward agent identity, trust classification, route-level visibility, and policy control.
- **What does it fail to represent?** It does not represent independent evidence of AI-agent prevalence, attack volume, or abuse outcomes. It is a vendor product blog and therefore selects details that support HUMAN's commercial framing. It does not expose the detection model, validation procedure, error rates, denominators, or the boundary cases where AI agents, crawlers, scrapers, assistants, browser automation, and malicious bots overlap. It also frames AI agents as conceptually distinct from scrapers more cleanly than may be true operationally.
- **What additional evidence would be needed to go further?** Useful next evidence would include independent measurement of AI-agent traffic across a defined sample of sites; validation of agent identification against ground truth; false-positive and false-negative rates for trust classes; comparison of cryptographically verified versus unverified agents in real traffic; evidence on whether route/session visibility changes defensive or business decisions; and standards documentation for HTTP Message Signatures or agent-authentication mechanisms if those become load-bearing claims.

## What it cannot show

- It cannot show that AI-agent traffic is internet-wide at the stated scale; the traffic-growth figures are imported from a separate HUMAN benchmark report.
- It cannot show that AI agents are generally malicious, because the source is about visibility and classification, not proven abuse.
- It cannot show that Sightline accurately identifies AI agents, because no validation results or error rates are provided.
- It cannot show that High/Medium/Low Trust classifications reliably predict risk, because the trust model is described but not empirically evaluated.
- It cannot show that traditional analytics tools universally fail at AI-agent identification; this is asserted in general terms.
- It cannot show that AI agents and scrapers are always separable categories; the source presents this as a product framing, but operational behaviours can overlap.
- It cannot show actual enforcement outcomes from AgenticTrust, because no case study or measured before/after result is provided.
- It cannot establish business impact from AI-agent traffic beyond the general risks of distorted metrics, attribution gaps, and potential abuse.

## Project impact

- Useful as a vendor capability source for the project's section on AI-agent visibility and the browser-native / agentic automation shift.
- Strong for showing how the vendor category is reframing the old bot-versus-human split into human / traditional bot / AI-agent traffic.
- Provides a compact vocabulary for a possible project subsection: identify, classify, measure, then control.
- Provides concrete control concepts for the taxonomy: cryptographic verification, trust tiers, session drill-down, route targeting, and policy enforcement.
- Lower evidential weight than HUMAN's monthly *State of Agentic Traffic* source, Thales' bad-bot report, or Akamai telemetry reports because this source is primarily product positioning rather than telemetry.
- Should be cited as evidence of what HUMAN claims its product category can do, not as independent evidence that these controls work or that AI agents are widely abusive.
- The source is worth keeping despite marketing content because it gives useful terminology and shows how a vendor is operationalising AI-agent governance.
- If HTTP Message Signatures or key directories become important in the Foundations or Technical territory pages, add canonical standards/protocol sources rather than relying on this vendor blog alone.
