# State of Agentic Traffic – May 2026: Financial services agentic traffic continues to climb, more than doubling this month

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: full text from attached PDF export of HUMAN blog page
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Kaiserman, Aviad / HUMAN Security. 2026. *State of Agentic Traffic – May 2026: Financial services agentic traffic continues to climb, more than doubling this month*. HUMAN Blog, 4 June 2026.
- **Source URL or path**: local uploaded PDF: `State of Agentic Traffic - May 2026_ Financial services agentic traffic continues to climb, more than doubling this month - HUMAN Security.pdf`; original public URL not stated in the PDF export.
- **Date accessed**: 2026-06-06
- **Category**: vendor
- **Evidence basis**: empirical-operational
- **Operational proximity**: observed — the source reports traffic observed across HUMAN Sightline Cyberfraud Defense in May 2026; however, this is vendor-measured agentic-traffic telemetry, not independent measurement and not necessarily observed malicious abuse.
- **Tags**: vendor, empirical-operational, observed, ai-agent, agentic-traffic, behavioural, user-agent-attribution, publisher-integration, policy-controls, financial-services, e-commerce, travel, media, route-categorisation

## What it claims

- HUMAN presents *State of Agentic Traffic* as a monthly benchmark on how AI agents appear across the web, covering agent mix, sector destinations, and activity patterns observed across the HUMAN Defense Platform.
- The May 2026 report says agentic traffic declined by 4.3% month over month, while the blocking rate increased from 8.2% in April to nearly 9% in May.
- The report interprets the rising blocking rate as evidence of a slow but growing use of policy controls to direct or restrict agentic activity.
- Comet Browser and Atlas remained the largest sources of observed agentic traffic in May 2026, accounting for 46.98% and 20.29% of traffic respectively, while both declined in absolute traffic volume compared with April.
- The Claude Chrome Extension increased its share of observed agentic traffic from 17.3% in April to 18.6% in May, and its absolute traffic volume grew by 2.6%.
- ChatGPT Agent was relatively stable month over month, while Genspark represented 2.9% of observed agentic traffic and grew by 18.2% in absolute volume.
- Media, e-commerce, and travel were the main destination sectors for observed agentic traffic in May 2026, together accounting for nearly 98% of observed traffic.
- Financial services represented only about 1% of observed agentic traffic, but the source says financial-services agentic traffic grew by 124% month over month from April to May.
- The report says more than three-quarters of observed agentic activity, 76.4%, was concentrated in product and search routes such as product listings, article reading, and searches.
- The report says remaining observed activity was distributed across account routes, authentication routes, content engagement, miscellaneous actions, and checkout/payment flows.
- The source states that current agent activity is primarily discovery and research oriented rather than transaction-completion oriented.
- HUMAN claims most analytics tools cannot distinguish AI agents from human visitors, identify specific agents, or classify their intent.
- HUMAN describes AgenticTrust as a trust and control layer for AI agents that provides session visibility, intent classification, and adaptive policy enforcement.

## What evidence it provides

- The source gives vendor telemetry from HUMAN Sightline Cyberfraud Defense during May 2026.
- For traffic mix by operator, it provides a chart and percentages for observed agentic traffic sources: Comet Browser, Atlas, Claude Chrome Extension, ChatGPT Agent, Genspark, Browserbase, Browsersec Cloud, Hyperbrowser Cloud, AgentCore Browser, and Manus AI.
- For sector distribution, it provides a chart and percentages for media, e-commerce, travel, financial services, SaaS, streaming/gaming, healthcare, ads, federal/government, and education.
- For page-category distribution, it provides a chart and percentages for products/search, account, authentication, content, other, checkout, and financial routes.
- The methodology section states that agent identification combines behavioural signal analysis, user-agent attribution, and publisher-level integration where available.
- The methodology section states that sector and route categorisation reflect the destination endpoint, not the agent operator's intent.
- The source does not provide raw traffic volumes, number of protected sites, customer mix, geographical distribution, uncertainty intervals, details of classification rules, validation metrics, false-positive rates, or independent verification.
- The product claims about AgenticTrust are not supported with independent evaluation or case-study evidence in this source.

## Signals or techniques mentioned

- Behavioural signal analysis.
- User-agent attribution.
- Publisher-level integration.
- Agent/operator attribution by named source: Comet Browser, Atlas, Claude Chrome Extension, ChatGPT Agent, Genspark, Browserbase, Browsersec Cloud, Hyperbrowser Cloud, AgentCore Browser, Manus AI.
- Blocking rate as an aggregate control/policy metric.
- Sector/destination classification.
- Route/category classification by destination endpoint: product/search, account, authentication, content, checkout/payment, other.
- Session visibility, intent classification, and adaptive policy enforcement are mentioned as AgenticTrust product capabilities.

## Threat types covered

- Not threat-specific in the OWASP OAT sense. The source covers observed AI-agent traffic and agentic automation rather than a defined attack class.
- Relevant project vocabulary: AI-agent traffic, browser-native automation, content retrieval, search/product discovery, potential scraping or data-access pressure, account-route exposure, authentication-route exposure, checkout/payment-route exposure.
- Possible adjacent OAT relevance: scraping and transaction abuse, but the source does not explicitly classify the observed traffic as these threats and does not establish malicious intent.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** It approximates the emerging operational problem of AI agents and browser-like agentic tools interacting with real websites at production scale. It is useful for showing which agent operators appear in one vendor's telemetry, which sectors receive that traffic, and which route categories it reaches.
- **What does it fail to represent?** It does not represent internet-wide agentic traffic, because the data is limited to HUMAN's visibility and customers. It does not establish malicious intent, attack success, business impact, or whether traffic should be treated as abuse. Its own methodology says sector and route labels describe the destination endpoint, not the agent operator's intent. It also lacks raw denominators and validation detail, so the percentages cannot be converted into independent prevalence estimates.
- **What additional evidence would be needed to go further?** To go beyond this source, the project would need independent measurement of AI-agent traffic across a defined sample of websites, raw or normalised traffic denominators, validation of agent-identification methods, site-level case studies showing business impact, and evidence distinguishing legitimate agent access from scraping, fraud, or other abuse.

## What it cannot show

- It cannot show that AI agents are generally malicious, because the source reports traffic and blocking, not intent or harm.
- It cannot show internet-wide prevalence of agentic traffic, because it reflects HUMAN-observed traffic only.
- It cannot show whether financial services faces a large absolute agentic-traffic burden, because financial services is reported as roughly 1% of observed agent traffic despite growing 124% month over month.
- It cannot show that the reported blocking rate corresponds to malicious traffic; blocking may reflect site policy, customer preference, or risk tolerance.
- It cannot show how accurately HUMAN identifies specific agents, because the classification method is only described at a high level.
- It cannot show transaction completion, account compromise, or abuse success; route categorisation only shows destination endpoint categories.
- It cannot independently validate HUMAN product claims about AgenticTrust.

## Project impact

- Useful as a current vendor-telemetry source for the browser-native automation / AI-agent shift.
- Stronger for showing observed agentic traffic patterns than for proving bot abuse or malicious behaviour.
- Provides concrete route categories that could help the project structure a section on where AI agents touch web applications: product/search, account, authentication, content, checkout/payment.
- Provides named agent/operator examples to include in the project's agentic-traffic taxonomy, with a caveat that the source is vendor-observed and time-specific.
- Supports the project's framing that the human/bot boundary is becoming harder to define, but only as vendor evidence and not as independent proof.
- Should be cited alongside broader sources such as Thales and Akamai reports, but kept distinct because this source is specifically about agentic traffic rather than all bad bots, DDoS, or account-takeover activity.
- Do not use this source for broad claims about market-wide prevalence, attack success, or the overall threat posed by AI agents without corroborating evidence.
