# Comodo ModSecurity WAF Rules Update: The 2026 Solution / SBB-WAF-Rules

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: partial — the GitHub repository, README, guide, and main rules file were accessible; the `stopbadbots.com` homepage returned 403 and the specific StopBadBots page identified by search could not be fetched directly in this environment.
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: StopBadBots / sminozzi. 2025. *Comodo ModSecurity WAF Rules Update: The 2026 Solution* / *SBB-WAF-Rules*. GitHub repository and StopBadBots project page. Repository maintainer: StopBadBots.com. Main rules file version 1.1, last updated 15 August 2025.
- **Source URL or path**: `https://github.com/sminozzi/SBB-WAF-Rules`; associated website supplied by author: `https://stopbadbots.com/`; repository README links to `https://stopbadbots.com/sbb-waf-rules/`.
- **Date accessed**: 2026-06-06
- **Category**: vendor
- **Evidence basis**: tooling-readme
- **Operational proximity**: capability — the repository contains a defensive ruleset and documentation for detecting and blocking classes of bot, scanner, and web-application abuse. It claims real-world refinement and improved blocking, but it does not provide traffic logs, denominators, validation metrics, or an independently checkable measurement basis.
- **Tags**: vendor, defensive-tooling, open-source-tooling, waf, modsecurity, comodo-waf, ruleset, bot-blocking, user-agent, blocklist, ai-crawler, scanner-detection, reconnaissance, behavioural-thresholds, wordpress, xmlrpc, sensitive-files, directory-traversal, rce, xss, false-positives, small-site-defence

## What it claims

- The source presents SBB-WAF-Rules as a free custom ModSecurity ruleset designed to enhance, not replace, the Comodo WAF ruleset.
- It says the rules are not a standalone firewall and should only be used with Comodo's core rules already in place.
- It claims the default Comodo WAF is a strong foundation, but that modern threats include behaviour-based bot scanning, probing, and brute-force attempts that need additional proactive controls.
- It claims the SBB ruleset can double the number of blocked threats when combined with the old Comodo rules.
- It describes a multi-layered defence model combining external blocklists, behavioural checks, and signature-based web-application attack rules.
- It says the ruleset uses three external data files: unwanted bot and AI crawler user agents, known web shell filenames, and sensitive or restricted filenames.
- It claims the behavioural rules can identify and block reconnaissance patterns such as excessive 404s, rapid `HEAD` requests, and direct access by IP address.
- It claims the ruleset provides protections against several web-application attack classes, including remote code execution, PHP object injection, cross-site scripting, directory traversal, PHAR deserialization, XXE, prototype pollution, and restricted-file access.
- It says blocking bad bots and obvious attacks early can reduce CPU, RAM, and database load.
- It claims the ruleset was built and refined from analysis of real-world traffic and attack vectors from high-traffic websites.
- It says the original Comodo WAF is discontinued and has not received rule updates since early 2024.
- It claims the SBB-WAF rules are a stable and updated free ruleset for 2025, with new versions released as needed.
- It says the ruleset was developed using more than 10 years of data from the StopBadBots WordPress plugin, which the source says helps reduce false positives on popular platforms.
- It says users may need to tune behavioural thresholds, allowed HTTP methods, scanner/user-agent rules, and external data files to avoid false positives.
- It states a policy of blocking major AI company crawlers by default, while allowing site owners to permit them by editing the `bad-bots.data` file.
- It argues that direct requests to a server's IP address are often associated with automated scanning and should be blocked to reduce low-quality or malicious traffic.
- It says users should deploy the ruleset in logging-only mode first, monitor ModSecurity logs, and then tune rules to their environment.

## What evidence it provides

- The strongest evidence is the repository content itself: a ModSecurity configuration file with named rule blocks and external data files. This demonstrates that the claimed defensive capability exists at the code/ruleset level.
- The README states the tool is specifically a Comodo WAF enhancement and not a standalone firewall. This supports the dependency and deployment-scope claim.
- The README and guide describe rule families covering external blocklists, excessive 404 counters, excessive `HEAD` request handling, user-agent analysis, direct-IP `Host` header blocking, sensitive-file access, directory traversal, command-like arguments, object injection, PHAR patterns, and other request-pattern checks.
- The main rules file provides implementation-level evidence for the presence of specific ModSecurity rules and rule IDs. It includes a ruleset summary with version 1.1 and a stated last update of 15 August 2025.
- The guide provides explanatory rationale for why behavioural thresholds and external lists may need tuning. This supports the source's own caveat that false positives are possible and environment-specific.
- The claim that Comodo WAF is discontinued is asserted in the README. The extraction did not independently verify Comodo's maintenance status.
- The claim that the rules can double blocked threats is asserted by the maintainer. The source does not provide the test design, baseline traffic, sample size, sites, time window, raw counts, false-positive rate, or reproduction method.
- The claim that the ruleset was refined from real-world traffic and high-traffic websites is asserted by the maintainer. No examples, logs, anonymised datasets, or measurement methodology are provided.
- The claim of more than 10 years of WordPress plugin data is asserted by the maintainer. The source does not provide the underlying data, number of sites, representativeness, or validation metrics.
- The repository metadata visible during extraction showed a small public repo footprint, including 46 commits, 8 stars, 1 fork, and no published GitHub releases. These are not quality measures, but they are useful context for treating the source cautiously.
- The StopBadBots website could not be directly fetched in this environment, so website-specific claims beyond what appears in the GitHub repository and search result snippet were not extracted.

## Signals or techniques mentioned

- ModSecurity / WAF rule-based request inspection.
- Comodo WAF augmentation.
- External user-agent blocklists.
- AI crawler blocking by default.
- Known web-shell filename lists.
- Sensitive and restricted filename lists.
- Behavioural counters for excessive 404s.
- Rate-limiting or blocking excessive `HEAD` requests.
- Blocking requests where the `Host` header is a literal IP address.
- HTTP method allow-listing.
- WordPress `xmlrpc.php` blocking.
- Suspicious user-agent substring detection.
- Command-line client user-agent detection.
- Vulnerability scanner user-agent detection.
- Missing `Accept` header detection.
- Access attempts to `wp-config`, readme, debug logs, and other sensitive files.
- Directory traversal detection in headers and arguments.
- Shell-command terms in request arguments.
- PHP object injection pattern detection.
- Cookie-based PHP object injection detection.
- PHAR deserialization pattern detection.
- XXE pattern detection.
- Prototype pollution pattern detection.
- Local rule tuning and logging-only deployment for false-positive management.

## Threat types covered

- Bad-bot traffic and unwanted crawlers.
- AI crawler scraping.
- Vulnerability scanning and reconnaissance.
- Directory and file brute forcing.
- WordPress brute-force and `xmlrpc.php` abuse.
- Direct-IP scanning.
- Command-line scripted requests.
- Vulnerability scanner traffic.
- Sensitive-file probing.
- Web shell discovery attempts.
- Cross-site scripting.
- Directory traversal.
- Remote code execution patterns.
- PHP object injection.
- PHAR deserialization.
- XXE.
- Prototype pollution.
- General web-application attack filtering.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** It approximates the small-site and self-managed-server defence layer: what a webmaster or small operator might deploy when relying on ModSecurity, legacy Comodo WAF rules, WordPress hardening, blocklists, and simple behavioural thresholds. It is useful for understanding practical, low-cost defensive controls against scanners, bad bots, AI crawlers, and common probing patterns.
- **What does it fail to represent?** It does not represent commercial bot-management telemetry, browser fingerprinting systems, behavioural ML, entity-resolution approaches, or cross-customer intelligence. It also does not show real-world prevalence, attack volume, or validated blocking effectiveness. Its claims are maintainer claims attached to a tool, not independent evidence that the controls work at scale.
- **What additional evidence would be needed to go further?** Useful follow-up would include a reproducible evaluation against real or replayed traffic; false-positive and false-negative analysis; independent testing against current bot/scanner traffic; comparison with standard Comodo/OWASP CRS baselines; validation of the Comodo-update claim; maintenance/release history; and examples of deployment outcomes from operators with anonymised logs.

## What it cannot show

- It cannot show that the ruleset doubles blocked threats in a generalisable way.
- It cannot show low false positives, because no false-positive measurement is provided.
- It cannot show that the blocklists are comprehensive, current, or accurately classified.
- It cannot show that user-agent blocking reliably detects modern bots, because sophisticated automation can spoof or rotate user-agent strings.
- It cannot show that the ruleset handles browser-native automation or AI agents operating through real browsers.
- It cannot show whether Comodo WAF is truly discontinued without independent confirmation.
- It cannot show that the ruleset is safe for all sites, APIs, WordPress plugins, or control panels; the guide itself says tuning may be needed.
- It cannot show production-scale effectiveness or adoption.
- It cannot show independent observed abuse; it is a defensive tooling source with maintainer claims about real-world basis.

## Project impact

- This is not a strong current-trend or observed-use source. It is better treated as defensive tooling / capability evidence.
- It is useful for a project section on the lower end of the defence stack: WAF rules, blocklists, user-agent filters, scanner heuristics, and rule tuning.
- It helps show the gap between simple bot controls and the harder browser-native/agentic problem: many controls here focus on headers, request methods, obvious scanner behaviour, direct-IP probing, and known filenames rather than high-fidelity browser-session identity.
- It is useful as evidence that AI crawlers are now being folded into default blocklists and treated by some small-site tooling as unwanted automation.
- It supports a practical point: public defensive tooling often mixes security controls, bot blocking, AI-crawler policy, WordPress hardening, and performance protection in one ruleset.
- It should be cited as a maintainer's open-source defensive ruleset and documentation, not as proof of effectiveness or prevalence.
- It should not be over-weighted. The repo has limited public adoption signals, no releases, no published evaluation, and unverified efficacy claims.

## Possible register row

| Field | Value |
|---|---|
| Register id | `stopbadbots-2025-sbb-waf-rules` |
| Title | *Comodo ModSecurity WAF Rules Update: The 2026 Solution / SBB-WAF-Rules* |
| Category | vendor |
| Evidence basis | tooling-readme |
| Operational proximity | capability |
| Tags | vendor; defensive-tooling; waf; modsecurity; comodo-waf; bot-blocking; ai-crawler; scanner-detection; blocklist; wordpress |
| Project use | Defensive-tooling example for simple WAF/blocklist/behavioural controls |
| Main caution | Maintainer claims only; website inaccessible during extraction; no independent effectiveness, prevalence, or false-positive evidence |
