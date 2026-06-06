# How long does it take to get owned? — Wardle 2019

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: full text from uploaded PDF
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Wardle, D. 2019. *How long does it take to get owned?* Technical Report RHUL-ISG-2019-4, Information Security Group, Royal Holloway University of London, 27 March 2019. Submitted as part of the MSc in Information Security. Supervisor: Jorge Blasco Alis.
- **Source URL or path**: local uploaded PDF: `techreport-davidwardle.pdf`
- **Date accessed**: 2026-06-06
- **Category**: academic
- **Evidence basis**: empirical-academic
- **Operational proximity**: measured — the report conducted an in-the-wild honey-identity experiment by publishing fake credentials on paste sites and observing unauthorised account access. It measures response to planted leaked credentials, not production credential-stuffing prevalence or bot automation directly.
- **Tags**: empirical-academic, measured-use, credential-stuffing, leaked-credentials, account-takeover, honeypots, honey-identities, honeytokens, paste-sites, password-reuse, login-monitoring, unauthorised-access, webmail, 2fa, user-agent, ip-address, bot-measurement-limits

## What it claims

- The report investigates the use of stolen credentials by measuring how long it takes for leaked credentials to be used after publication.
- The report argues that credential stuffing is a serious threat because it automates login attempts against unbreached websites using stolen credentials.
- The project designed a framework for creating fake online identities, called honey identities, with accounts and a digital footprint whose value lies in being attacked or compromised.
- The experiment published credentials for eleven fake identities on paste websites and monitored their use over roughly six weeks.
- The experiment recorded five events of unauthorised access, with the fastest occurring 34 minutes after the relevant password leak.
- The source says the honey identities were monitored using service-provided signals such as new-login emails, 2FA SMS verification alerts, login history / recent activity pages, account activity, credential checks, data downloads, honeytokens, and custom scripts where possible.
- The report says only a limited number of web services were suitable for the honey-identity design because of ethical, practical, technical, terms-of-service, registration, and monitoring constraints.
- The final chosen services included a mix of public web services and a private server / fictional company setup used to support the honey identities.
- The experiment used several paste formats, including database-like dumps, email-password pairs, links to files, and Dropbox shared-folder bait, rather than waiting for a real breach.
- The report found no evidence of further account activity after most intruders gained access and notes that this resembled the "Curious" category from earlier leaked-Gmail-account research.
- The author warns that reported IP-derived locations and browser details should be treated cautiously because user-agent strings can be spoofed and IP geolocation can be inaccurate or hidden through proxies or VPNs.
- The author states that the result set is too small to draw strong trends, and that the experiment mainly validated the framework and monitoring infrastructure.
- The report concludes that the work provides a platform for further experimentation, but that stronger honey identities, more varied publication methods, more accounts, and longer observation periods would be needed.

## What evidence it provides

- The source provides a full MSc technical report with background literature review, design, implementation, experiment description, results, discussion, and appendices containing source code and paste-file examples.
- Empirical basis: credentials for eleven fake identities were published online via paste websites and monitored for six weeks.
- Observed results: five intruders / unauthorised access events were recorded. Table 5.8 reports time-to-use after leak as 0:36, 1:00, 99:34, 635:09, and 648:55 hours for the five intruders.
- Monitoring evidence came from service alerts and logs: Gmail login notifications and activity, Dropbox login notifications / 2FA SMS, login history, server access logs, and available browser / IP details.
- The source reports that one intruder attempted Dropbox login after using leaked Gmail / email-related credentials, but 2FA prevented full Dropbox access.
- The source reports some contextual indicators about intruder activity: in one case a Gmail account showed Google search activity, and in another the same IP address viewed the fictional website and the relevant honey identity profile.
- The source provides explicit limitations: short six-week observation period, only paste websites used as a leak channel, small number of identities, small number of observed intruders, constrained service selection, and uncertainty over paste visibility and search-indexing.
- The source uses earlier academic work, especially Onaolapo et al.'s honey Gmail account study, as a comparator for monitoring and behaviour categories.
- The source does not provide a production platform dataset, a commercial anti-bot telemetry feed, or a labelled bot/human dataset.
- The source does not prove that the observed accesses were automated; it observes unauthorised use of leaked credentials and records some browser/IP/session signals.

## Signals or techniques mentioned

- Credential stuffing as automated login attempts against unbreached websites using stolen credentials.
- Honey identities: fake digital identities built from attributes and multiple accounts.
- Honeypot accounts.
- Honeytokens, including embedded URLs and secondary credentials.
- Paste sites / public data sinks for leaked credentials.
- Email-password pair pastes.
- Database-dump-like pastes.
- Password hashes, including MD5 and salted MD5 examples.
- Dropbox shared-folder bait.
- New-login notification emails.
- 2FA SMS verification alerts.
- Login history / recent activity pages.
- Credential validity checks.
- Account activity monitoring.
- Email forwarding to central monitoring inbox.
- Web server access logs.
- IP addresses and geolocation.
- HTTP user-agent strings.
- Browser / operating-system details.
- Google Apps Script as a possible monitoring mechanism.
- SMTP sinkhole / outgoing email containment in related work.
- Paste visibility, archive pages, search indexing, and dump-monitoring bots.
- Proxies, VPNs, and location malleability as cautions around interpreting access records.
- Password reuse and partial password reuse.
- Have I Been Pwned-style breached-password checking.

## Threat types covered

- Credential stuffing / use of leaked credentials.
- Account takeover risk.
- Password reuse across services.
- Stolen credential trading / public credential dumps.
- Unauthorised account access.
- Webmail account compromise.
- Possible credential validation / curiosity accesses.
- The source is adjacent to OWASP OAT-008 Credential Stuffing and account takeover, but its empirical experiment measures unauthorised use of planted credentials rather than full-scale automated credential stuffing campaigns.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** It approximates what happens after credentials are leaked into public paste-style channels: whether someone finds them, how quickly they are tried, what account-access signals are visible, and how a honey-account infrastructure can observe unauthorised access. This is directly useful for the project's credential-stuffing / account-takeover strand because it offers independent measured-use evidence rather than vendor telemetry.
- **What does it fail to represent?** It does not represent production-scale credential stuffing against real platforms, commercial anti-bot detection, organised account-checking infrastructure, residential proxies at scale, browser-native automation, API-first login flows, AI agents, or modern credential-stuffing-as-a-service tooling. The experiment is small, dated, short, paste-site-only, and based on artificial identities rather than real breached accounts. It also cannot reliably separate human curiosity, manual credential checking, and automated credential-stuffing bots.
- **What additional evidence would be needed to go further?** Larger honey-identity experiments, longer observation windows, multiple leak channels including forums / breach markets / code repositories / misconfigured storage, richer server-side telemetry, controlled variation in account value and digital-footprint realism, partnership data from service providers, and modern measurement against API login endpoints and bot-management systems.

## What it cannot show

- It cannot show market-wide or internet-wide prevalence of credential stuffing.
- It cannot show that most leaked credentials are used quickly; the observed sample is only five intruders.
- It cannot show whether the observed accesses were automated bots, manual credential seekers, or a mix.
- It cannot show how modern credential-stuffing infrastructure behaves against current bot-management systems.
- It cannot show the effectiveness of any vendor product or anti-bot control.
- It cannot show how attacks behave against financial, ticketing, booking, or high-value production systems because the experiment used artificial identities and selected services constrained by ethics and feasibility.
- It cannot show strong trends by geography, browser, operating system, or intruder type because IP, location, and user-agent signals are weak and the sample is tiny.
- It cannot show that paste sites remain the primary route for leaked credentials; the source itself notes that paste-site conditions and popularity change over time.
- It cannot show that hashes are ignored in general; its lack of hash-paste logins is a small-sample result.

## Project impact

- High-value source for an independent measured-use lane on credential reuse and account takeover.
- Useful counterweight to vendor telemetry: it is not commercial-scale, but it is transparent and methodologically explicit.
- Strong source for explaining honey accounts / honey identities as a method for observing credential misuse.
- Supports a project point that public-data measurement is possible, but only as an approximation with sharp limits.
- Useful for a page or sidebox on "what public researchers can measure" versus what commercial bot-management vendors can see.
- Helps separate "credential stuffing capability exists" from "credential misuse was observed in this specific honey experiment".
- Useful caution source for weak identifiers: IP geolocation and user-agent data are informative but spoofable / ambiguous.
- Good companion to vendor account-takeover reports: vendor reports show production telemetry; Wardle 2019 shows an open, reproducible research-style method with much smaller scale.
- Not a current-trend source. Its value is methodological and observed-use, not contemporary coverage of agentic automation or modern bot tooling.
- Should be cited with caution: "Wardle observed five unauthorised accesses in a six-week honey-identity experiment", not "leaked credentials are usually used within 34 minutes".

## Possible register row

| Field | Value |
|---|---|
| Register id | `wardle-2019-how-long-does-it-take-to-get-owned` |
| Title | *How long does it take to get owned?* |
| Category | academic |
| Evidence basis | empirical-academic |
| Operational proximity | measured |
| Tags | credential-stuffing; account-takeover; leaked-credentials; honeypots; honey-identities; paste-sites; password-reuse; measured-use |
| Project use | Independent measured-use evidence for leaked credential use and honey-account methodology |
| Main caution | Small, dated, paste-site-only honey experiment; observes unauthorised access, not necessarily automated bot traffic |
