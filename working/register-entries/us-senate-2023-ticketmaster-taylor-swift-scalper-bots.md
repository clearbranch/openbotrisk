# U.S. Senate Ticketmaster / Taylor Swift case (2023) - scalper bots, Verified Fan, and live-event ticketing

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded public-hearing PDFs and press PDF:
  - `Testimony - Berchtold - 2023-01-24.pdf`
  - `Bradish_SJC-Hearing_Live-Events_1.24.23.pdf`
  - `Microsoft Word - Bradish_SJC Hearing_Live Events_1.24.23.doc - Bradish_SJC-Hearing_Live-Events_1.24.23.pdf`
  - `Scalper bots caused Taylor Swift ticket chaos, Senate panel hears in testimony _ US Senate _ The Guardian.pdf`
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.
- **Source handling decision**: combine as one case entry. The two Bradish files are the same testimony/source family, so keep only one canonical Bradish citation. Use Berchtold’s Live Nation testimony as the primary bot-traffic claim source, Bradish/AAI as the competition/market-structure counter-frame, and the Guardian article as secondary press reporting of the hearing.

## Bibliographic

### Main source

- **Citation**: Berchtold, J. (2023). *Opening Statement of Joe Berchtold, President and Chief Financial Officer, Live Nation Entertainment, Inc.* United States Senate Judiciary Committee, 24 January 2023.
- **Source URL or path**: uploaded PDF `Testimony - Berchtold - 2023-01-24.pdf`.

### Supporting public-hearing source

- **Citation**: Bradish, K. (2023). *That’s the Ticket: Promoting Competition and Protecting Consumers in Live Entertainment*. Testimony before the United States Senate Committee on the Judiciary, 24 January 2023.
- **Source URL or path**: uploaded PDF `Bradish_SJC-Hearing_Live-Events_1.24.23.pdf`.
- **Duplicate note**: `Microsoft Word - Bradish_SJC Hearing_Live Events_1.24.23.doc - Bradish_SJC-Hearing_Live-Events_1.24.23.pdf` appears to be the same testimony/source family and should not be a separate register row.

### Supporting press source

- **Citation**: Aratani, L. (2023). *Scalper bots caused Taylor Swift ticket chaos, Senate panel hears in testimony*. The Guardian, 24 January 2023.
- **Source URL or path**: uploaded PDF `Scalper bots caused Taylor Swift ticket chaos, Senate panel hears in testimony _ US Senate _ The Guardian.pdf`.

## Category and treatment

- **Category**: public hearing / case evidence
- **Evidence basis**: public testimony / contested case account / secondary press reporting
- **Operational proximity**: observed-claim — strong evidence that a major ticketing platform publicly attributed a high-profile failure to bot/scalper traffic and access-code-server attack pressure; weaker as independently verified technical evidence because the key bot-volume and penetration claims come from Live Nation/Ticketmaster itself.
- **Tags**: Ticketmaster, Live-Nation, Taylor-Swift, Eras-Tour, Senate-hearing, scalper-bots, ticket-bots, Verified-Fan, access-code-servers, BOTS-Act, industrial-scalping, dynamic-pricing, secondary-ticketing, antitrust, live-events, OAT-005, OAT-013, OAT-021, OAT-006

## What it claims

### Berchtold / Live Nation testimony

- Live Nation says industrial-scale ticket scalping in concerts is a multi-billion-dollar problem and is largely enabled by bots acquiring tickets and reselling them on online secondary marketplaces.
- Ticketmaster says it created Verified Fan to get tickets to fans rather than scalpers using bots and invests millions in anti-bot technology each year.
- For the Taylor Swift Eras Tour presale, Live Nation says there was unprecedented demand and that Ticketmaster expected bot attacks.
- Live Nation says it was hit with three times more bot traffic than it had ever experienced.
- It says that for the first time in 400 Verified Fan onsales, bots attacked the Verified Fan access-code servers.
- It says the bots did **not** penetrate Ticketmaster’s systems or acquire tickets, but the attack required Ticketmaster to slow down and pause sales, causing a poor consumer experience.
- Berchtold accepts that Ticketmaster could have done better, including staggering sales over a longer period and setting fan expectations better.
- Live Nation calls for stronger BOTS Act enforcement, broader anti-bot rules, private civil enforcement, restrictions on speculative ticket sales, and all-in pricing.

### Bradish / American Antitrust Institute testimony

- AAI frames Live Nation-Ticketmaster as both a traditional monopoly and a modern dominant digital platform.
- AAI argues that Live Nation-Ticketmaster’s vertical integration across artist management, concert promotion, venues, and ticketing creates incentives to exclude rivals and impair secondary ticketing competition.
- AAI argues that conduct remedies in the 2010 consent order failed and that structural relief should be considered.
- AAI treats the Taylor Swift incident as likely connected to lack of innovation and weak incentives created by market power, rather than simply a bot-only failure.

### Guardian reporting

- The Guardian reports the hearing as a contested public account: Live Nation’s president blamed scalper bots and cyber-attacks, while senators and competitors pressed the market-power/monopoly angle.
- The article reports Berchtold’s key claim about three-times-higher bot traffic and Verified Fan access-code servers.
- It also reports criticism from senators and ticketing competitors that Ticketmaster should have had better bot controls or that bot-blaming obscures market-power issues.

## What evidence it provides

This case provides **public, high-proximity evidence of ticket-bot impact as claimed by the target platform**, plus **public counter-framing about market structure**.

It provides:

- a named high-profile incident: Taylor Swift Eras Tour presale / Ticketmaster, discussed at a U.S. Senate Judiciary Committee hearing on 24 January 2023;
- a primary statement from the platform operator describing bot traffic scale and system impact;
- a statement that bots targeted a specific class of defensive infrastructure: Verified Fan access-code servers;
- a statement that bots did not acquire tickets but still degraded the service by forcing sales slowdowns/pauses;
- public-policy framing around the BOTS Act, speculative sales, secondary ticketing, and all-in pricing;
- competition-policy testimony arguing that bot pressure cannot be separated from market structure, platform power, innovation incentives, and ticketing-market design.

It does **not** provide:

- raw traffic logs;
- independent technical forensic evidence;
- bot-source infrastructure details;
- detection rules or anti-bot architecture;
- proof that bots caused all failures;
- proof that bots successfully obtained tickets;
- evidence of specific bot tools, providers, proxies, CAPTCHA solvers, or account-farm methods;
- independent measurement of the claimed “three times” bot traffic.

## Key quantitative and factual details

| Detail | Source treatment |
|---|---|
| 2022 U.S. live music described by Live Nation as a $12bn industry | Live Nation testimony claim |
| Live Nation says concert scalping is a $5bn industry in concerts alone | Live Nation testimony claim |
| Ticketmaster says it invested over $1bn in capital to improve the system after the 2010 merger | Live Nation testimony claim |
| Ticketmaster says it invests millions each year in anti-bot technology | Live Nation testimony claim |
| Ticketmaster says the Taylor Swift onsale saw three times more bot traffic than it had ever experienced | Live Nation testimony claim; not independently verified here |
| Ticketmaster says bots attacked Verified Fan access-code servers for the first time in 400 Verified Fan onsales | Live Nation testimony claim |
| Ticketmaster says bots did not penetrate systems or acquire tickets | Live Nation testimony claim |
| Ticketmaster says it sold more than 2m tickets and demand could have filled 900 stadiums | Reported in Guardian; attributed to Ticketmaster |
| AAI says Ticketmaster had contracts for more than 80% of large venues in 2008 | AAI testimony citing prior sources |
| AAI says Live Nation-Ticketmaster made over 40 acquisitions from 2011–2022 | AAI testimony based on Crunchbase query |
| AAI says Ticketmaster maintained about 80% ticketing share and Live Nation about 60% concert-promotion share 13 years after merger | AAI testimony, with caveats from its cited sources |

## Signals or techniques mentioned

- ticket bots;
- scalper bots;
- industrial-scale ticket scalping;
- Verified Fan;
- Verified Fan access codes;
- access-code-server attack pressure;
- on-sale traffic surge;
- sale slowdown/pause as defensive response;
- anti-bot technology;
- cyber-attacks against onsales;
- online secondary marketplaces;
- speculative ticket sales;
- deceptive “official” resale URLs;
- dynamic pricing discussion;
- all-in pricing;
- resale-market restrictions;
- ticket transferability restrictions;
- ticket inventory release timing;
- platform integration and digital ticketing.

## Threat types covered

Directly relevant:

- ticket bots;
- scalper automation;
- high-demand on-sale abuse;
- secondary-market resale abuse;
- speculative ticket sales;
- access-code / queue / on-sale infrastructure pressure.

OWASP Automated Threat mappings:

- **OAT-005 Scalping** — primary mapping. The case is centrally about automated attempts to obtain limited high-demand tickets for resale.
- **OAT-013 Sniping** — secondary mapping where automated timing around ticket release matters, though the source does not emphasise last-second bidding.
- **OAT-021 Denial of Inventory** — relevant where ticket acquisition/holding/removal from primary availability affects real fans, though Berchtold says bots did not acquire tickets in this incident.
- **OAT-006 Expediting** — relevant because bots automate high-speed actions in a workflow designed for human fans.
- **OAT-015 Denial of Service** — partial relevance: the reported effect was system pressure requiring slowed/paused sales, but it is framed as scalper-bot traffic rather than a pure DoS campaign.
- **OAT-019 Account Creation** — possible but not directly evidenced.
- **OAT-009 CAPTCHA Defeat** — not evidenced in these files.

## What is strong

- Strong real-world case anchor for ticket bots and scalping.
- Strong for explaining that even failed bot attacks can degrade user experience if the platform must slow or pause sales.
- Strong for the “business-model plus defence” point: ticket bot abuse cannot be analysed only as a technical problem, because resale incentives, platform dominance, inventory design, access-code systems, and legal enforcement all matter.
- Strong public-policy source because it links bots to:
  - BOTS Act enforcement;
  - speculative ticket sales;
  - secondary ticketing;
  - transparency/all-in pricing;
  - market structure and antitrust.
- Useful complement to OWASP OAT: this is concrete sector evidence for OAT-005 Scalping and related inventory/ticketing abuse.

## What is weak or limited

- The central technical claim comes from Live Nation/Ticketmaster, which had an interest in attributing the failure to bots.
- There is no raw evidence for the bot-traffic volume, bot sources, tooling, detection method, or server impact.
- Ticketmaster says bots did not penetrate its systems or obtain tickets, so the case should not be used as evidence of successful bot acquisition in the Taylor Swift incident.
- The Guardian is secondary reporting, not technical evidence.
- Bradish/AAI is advocacy testimony focused on antitrust; useful but not neutral technical analysis.
- The case is U.S. live-event ticketing and may not generalise to all appointment-slot, retail, sneaker, or queueing systems.
- It does not show exact defences, false positives, or how Verified Fan was implemented.
- It does not show whether stronger anti-bot controls, staggered sales, architecture changes, or legal enforcement would have solved the event.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  High-demand ticketing abuse where automated scalper traffic attacks an on-sale process and defensive access-code infrastructure, creating service degradation and consumer harm.

- **What does it fail to represent?**  
  It does not represent a fully forensically verified technical incident. It also does not show a successful bot purchase workflow in this specific case, because Ticketmaster says bots failed to acquire tickets.

- **What additional evidence would be needed to go further?**  
  Ticketmaster logs; independent incident report; FTC/DOJ/state enforcement records; court filings under the BOTS Act; bot-operator evidence; proxy/CAPTCHA/account-farm evidence; and comparative data from other ticketing platforms or countries.

## What it cannot show

- It cannot prove the exact amount of bot traffic.
- It cannot prove bots were the only or primary cause of the failure.
- It cannot prove bots obtained tickets in the Taylor Swift event.
- It cannot show which bot tools or services were used.
- It cannot show whether Ticketmaster’s anti-bot defences were reasonable.
- It cannot show whether Live Nation’s market structure caused the failure.
- It cannot show which legislative remedy would be effective.
- It cannot replace technical incident reporting or enforcement-case evidence.

## Project impact

Use this as a **high-value ticket-bot / scalping case entry**.

Best uses:

- concrete case evidence for OAT-005 Scalping;
- show that bot traffic can damage a service even when it fails to acquire inventory;
- show that automated-abuse cases are often contested: platform operators may blame bots, while lawmakers/competitors focus on market structure and platform incentives;
- support discussion of ticketing/appointment-slot systems where demand exceeds supply;
- connect bot defence to non-technical remedies:
  - stronger enforcement;
  - market design;
  - all-in pricing;
  - speculative-sales bans;
  - resale-market rules;
  - structural/competition policy.

Do not use it as:

- proof that bots successfully bought Taylor Swift tickets;
- proof that Ticketmaster’s technical account is independently verified;
- proof that all failures were caused by bots;
- evidence of a specific bot method or bypass;
- general evidence for all bot categories.

## Relationship to other register entries

- **OWASP Automated Threat Handbook**: provides OAT-005 Scalping, OAT-013 Sniping, OAT-021 Denial of Inventory, OAT-006 Expediting.
- **Proxy ecosystem entries**: relevant because ticket bots often use distributed IP infrastructure, but these files do not prove proxy use in this case.
- **CAPTCHA-solving entries**: relevant to ticketing generally, but no CAPTCHA defeat is shown in these files.
- **ASVS / NIST / API Security**: useful for application controls around rate limiting, session integrity, business logic, and account/access-code protection.
- **DVSA / slot-sniping sources if added**: useful comparison because both involve scarce slots/tickets, queues, resale/booking incentives, and possible legal or market-design remedies.
- **Cloudflare/HUMAN/DataDome**: relevant for modern bot-management controls, but this case does not expose Ticketmaster’s detection architecture.

## Dual-use containment

Low-to-moderate dual-use. The sources discuss ticket bots and access-code servers, but do not provide operational bot methods. Keep use at the case-analysis, policy, and threat-category level. Do not infer or reconstruct bot workflows, access-code attacks, queue strategies, or bypass techniques.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `us-senate-2023-ticketmaster-taylor-swift-scalper-bots` |
| Title | *Ticketmaster / Taylor Swift Eras Tour Senate hearing: scalper bots, Verified Fan, and live-event ticketing* |
| Organisation / authors | Joe Berchtold / Live Nation; Kathleen Bradish / American Antitrust Institute; Guardian reporting |
| Year | 2023 |
| Category | public hearing / case evidence |
| Evidence basis | public testimony / contested case account / secondary press reporting |
| Operational proximity | observed-claim |
| Signals / techniques | scalper bots; ticket bots; Verified Fan; access-code servers; on-sale slowdown; secondary marketplaces; speculative sales; BOTS Act |
| Threat types | OAT-005 Scalping; OAT-013 Sniping; OAT-021 Denial of Inventory; OAT-006 Expediting; partial OAT-015 DoS-style service pressure |
| Project use | High-profile ticket-bot case showing scarce-inventory automation, platform stress, resale incentives, and contested policy framing |
| Main caution | Central bot-volume and failure-causation claims are platform testimony, not independent technical forensics; Ticketmaster says bots did not acquire tickets |
| Entry file | `us-senate-2023-ticketmaster-taylor-swift-scalper-bots.md` |
