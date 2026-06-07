# Ticketmaster v. Prestige Entertainment West (2018-2019) - ticket bots, dummy accounts, CAPTCHA, and legal remedies

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded legal/case PDFs:
  - `TicketmasterPrestigeEntertainment20180131.pdf`
  - `Ticketmaster Reaches Settlement with Ticket Broker over Unauthorized Use of Automated Bots - Insights - Proskauer Rose LLP.pdf`
  - `2021-01-14-GT-ACC-InternetLawYIR-Database Protection.pdf`
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.
- **Source handling decision**: keep as a separate case entry from the 2023 U.S. Senate / Taylor Swift case. This is earlier chronologically, but stronger as legal case evidence of alleged ticket-bot purchase activity and court/settlement treatment.

## Bibliographic

### Primary legal source

- **Citation**: *Ticketmaster L.L.C. v. Prestige Entertainment, Inc., Prestige Entertainment West, Inc., Renaissance Ventures LLC, Nicholas Lombardi, and Steven K. Lichtman*, Case No. 2:17-cv-07232-ODW (JCx), Order Granting in Part and Denying in Part Defendants’ Motion to Dismiss, Central District of California, 31 January 2018.
- **Source URL or path**: uploaded PDF `TicketmasterPrestigeEntertainment20180131.pdf`.

### Settlement summary source

- **Citation**: Neuburger, J. (2019). *Ticketmaster Reaches Settlement with Ticket Broker over Unauthorized Use of Automated Bots*. New Media and Technology Law Blog / Proskauer Rose LLP, 24 July 2019.
- **Source URL or path**: uploaded PDF `Ticketmaster Reaches Settlement with Ticket Broker over Unauthorized Use of Automated Bots - Insights - Proskauer Rose LLP.pdf`.

### Legal context source

- **Citation**: Ballon, I. C. (2021). *Data Scraping, Database Protection and the Use of Bots and Artificial Intelligence to Gather Content and Information*. Excerpt from *E-Commerce and Internet Law: Treatise with Forms*, 2nd ed., ACC Internet Law Year in Review, 14 January 2021.
- **Source URL or path**: uploaded PDF `2021-01-14-GT-ACC-InternetLawYIR-Database Protection.pdf`.

## Category and treatment

- **Category**: legal case / observed-use allegation / settlement
- **Evidence basis**: court pleadings/order / litigation allegations / settlement summary / legal analysis
- **Operational proximity**: legally observed-claim — stronger than generic commentary because it involves specific litigation, detailed pleaded facts, and settlement injunctions; still not a final trial finding that every allegation was true.
- **Tags**: Ticketmaster, Prestige Entertainment, ticket-bots, scalping, dummy-accounts, CAPTCHA, access-controls, CFAA, DMCA, CDAFA, BOTS-Act, breach-of-contract, fraud, anti-scalping-law, website-access, scraping-law, automated-ticket-purchasing, OAT-005, OAT-009, OAT-006, OAT-021

## What it claims

### Ticketmaster allegations accepted as pleaded facts at motion-to-dismiss stage

The January 2018 court order records Ticketmaster’s allegations that:

- Ticketmaster sells live-event tickets through its website, mobile app, and call centres.
- Demand for tickets can exceed supply, creating intense competition when tickets are released.
- Ticketmaster uses countermeasures including purchase limits, request-speed limits, and CAPTCHA to discourage automated ticket-purchasing bots.
- Defendants allegedly used bots and dummy accounts to navigate Ticketmaster’s website and mobile app to buy large quantities of tickets.
- Defendants allegedly used colocation facilities, high-speed bandwidth, random number/letter generators, and other evasive methods.
- Bots allegedly allowed defendants to reserve or purchase tickets at speeds impossible for a human consumer to match.
- Tickets were allegedly resold on third-party platforms such as StubHub for profit.
- Ticketmaster estimated that from January 2015 to September 2016 defendants made at least 313,528 orders using 9,047 different accounts.
- Ticketmaster estimated that for certain shows defendants bought between 30% and 40% of available inventory.

These are strong allegations in a filed case, but the motion-to-dismiss order treats factual allegations as true for that procedural stage. They are not equivalent to a fully adjudicated trial finding.

### 2018 court-order treatment

The January 2018 order is useful because it shows how different legal theories fared:

- Ticketmaster brought claims including breach of contract, copyright infringement, DMCA, fraud, aiding and abetting fraud, inducing breach of contract, intentional interference, CFAA, CDAFA, and New York anti-scalping-law claims.
- The court dismissed the copyright infringement claim where it was based on bot use, excessive page refreshes/ticket requests, or server load, because those limits did not implicate an exclusive copyright right.
- The court dismissed CFAA and CDAFA claims with leave to amend, partly because the cease-and-desist letter did not clearly revoke access authorization and because mere terms-of-use violations were not enough under Ninth Circuit authority.
- The court allowed DMCA-related theory to remain sufficiently pleaded at that stage, and later sections recognise the case as involving CAPTCHA/access-control circumvention issues.
- The court allowed breach-of-contract and fraud claims to proceed sufficiently at the pleading stage.

### 2019 settlement summary

The Proskauer summary reports that Ticketmaster reached a settlement with Prestige in July 2019, ending litigation over alleged automated bulk ticket purchases.

The reported settlement terms included:

- Prestige permanently enjoined from using ticket-bot software to search for, reserve, or purchase tickets on Ticketmaster’s site or app at rates faster than human users using ordinary browsers or mobile apps.
- Prestige barred from circumventing CAPTCHA or other access-control measures used to enforce ticket-purchase limits and purchasing order rules.
- Prestige barred from violating Ticketmaster terms of use, conspiring to violate them, or engaging in other prohibited activity.

The same source reports that Ticketmaster earlier settled with the alleged bot software developer, with injunction terms against creating ticket-bot programs, exceeding web-page request limits, circumventing CAPTCHA/human-detection measures, creating fake accounts, or violating Ticketmaster copyrights.

### Ballon legal-treatise context

The Ballon/Greenberg Traurig excerpt places the case inside a broader legal framework for scraping, databases, bots, AI agents, website access, CFAA, DMCA, the BOTS Act, trespass, contract, and copyright.

Useful points from that source:

- U.S. database/scraping law is a patchwork: copyright, contract, misappropriation, trespass, CFAA, DMCA, Lanham Act, trade secret, and specific ticket-bot laws.
- The BOTS Act applies narrowly to online event ticket sales and prohibits circumvention of ticket-purchasing security or access controls used to enforce purchase limits and order rules.
- The Ticketmaster/Prestige case is used as an example of sophisticated bot allegations, including recurring reserve requests, rapid regeneration of reserves, masking bot behaviour, mobile-app evasion, and alleged need to study site/app code.
- The source also warns that lawful scraping and database protection are fact-specific and cannot be reduced to a single universal rule.

## What evidence it provides

This case provides relatively strong **legal-case evidence of alleged ticket-bot behaviour** and **legal response mechanisms**.

It provides:

- named parties;
- case number and federal court order;
- detailed pleaded bot-use allegations;
- time window and scale estimates from Ticketmaster;
- alleged use of dummy accounts;
- alleged automated purchasing/reserving activity;
- alleged evasion of Ticketmaster countermeasures;
- settlement/injunction terms against ticket-bot software and CAPTCHA/access-control circumvention;
- legal-theory handling across contract, fraud, CFAA, CDAFA, DMCA, copyright, and anti-scalping law.

It does **not** provide:

- raw bot logs;
- technical detection data;
- source code for bots;
- independent measurement of bot traffic;
- final trial findings proving all factual allegations;
- bot-market details;
- proof of proxy/CAPTCHA-solver provider use;
- general prevalence of ticket bots.

## Key factual/legal details

| Detail | Treatment |
|---|---|
| Alleged time period | January 2015 to September 2016 |
| Alleged order count | at least 313,528 orders |
| Alleged account count | 9,047 different accounts |
| Alleged show-level impact | 30-40% of available inventory for certain shows |
| Alleged techniques | bots, dummy accounts, high-speed infrastructure, random generators, evasive methods |
| Platform surfaces | Ticketmaster website and mobile app |
| Controls mentioned | ticket limits, request-speed rules, CAPTCHA, access-control measures |
| Legal claims | contract, copyright, DMCA, fraud, inducing breach, interference, CFAA, CDAFA, anti-scalping law |
| Settlement outcome | permanent injunction against bot software and CAPTCHA/access-control circumvention |
| Main caution | many operational facts are allegations; settlement is not full technical adjudication |

## Signals or techniques mentioned

- automated ticket bot software;
- dummy accounts;
- account creation/use at scale;
- website automation;
- mobile-app automation;
- CAPTCHA circumvention;
- access-control circumvention;
- page request limits;
- ticket reserve requests;
- recurring reserve requests;
- rapid reserve regeneration;
- high-speed bandwidth;
- colocation facilities;
- random number/letter generators;
- bot masking;
- behaviour that appears closer to normal use;
- purchase limits;
- refresh/request interval limits;
- third-party resale platforms;
- terms-of-use restrictions;
- cease-and-desist notice;
- copyright/code access theory;
- CFAA/CDAFA unauthorised-access theory;
- DMCA anti-circumvention theory;
- BOTS Act context.

## Threat types covered

Directly relevant:

- ticket scalping;
- automated ticket search/reserve/purchase;
- dummy account use;
- CAPTCHA/access-control circumvention;
- bulk purchase for secondary resale;
- inventory capture for scarce live-event tickets.

OWASP Automated Threat mappings:

- **OAT-005 Scalping** — primary mapping. The alleged behaviour is automated acquisition of limited tickets for resale.
- **OAT-006 Expediting** — bots allegedly carried out ticket reserve/purchase actions faster than human users.
- **OAT-009 CAPTCHA Defeat** — directly relevant through CAPTCHA and human/bot distinction measures.
- **OAT-021 Denial of Inventory** — relevant because alleged bulk reservations/purchases removed tickets from availability for ordinary fans.
- **OAT-019 Account Creation** — relevant through dummy accounts, though the court-order snippets focus on account use/creation rather than registration infrastructure.
- **OAT-015 Denial of Service** — secondary/partial relevance through disproportionate load and request limits, but this is not framed as a pure DoS case.
- **OAT-011 Scraping** — legal sources connect the case to unwanted scraping/website access, but the core behaviour is ticket purchasing rather than content scraping.

## What is strong

- Stronger observed-use/legal source than the 2023 Senate/Taylor Swift hearing for the claim that ticket bots were allegedly used to buy/reserve tickets at scale.
- Good case evidence for the full scarce-inventory abuse pattern:
  - demand exceeds supply;
  - purchasing limits exist;
  - bots attempt to move faster than humans;
  - dummy accounts spread activity;
  - tickets are resold for profit;
  - defensive controls include CAPTCHA, request limits, and access controls;
  - legal remedies include injunctions and contract/fraud/anti-circumvention theories.
- Good source for showing that automated abuse can be pursued through multiple legal routes, not only the BOTS Act.
- Good bridge between bot detection and law: terms of use, access-control circumvention, technical barriers, and statutory claims all matter.
- Useful for comparing with the Taylor Swift Senate case:
  - Prestige = alleged successful bulk purchase/resale pattern;
  - Taylor Swift Senate = platform-claimed bot pressure that allegedly did not acquire tickets but degraded service.

## What is weak or limited

- Many technical facts are allegations rather than trial-proven facts.
- Settlement does not necessarily establish liability or admit all allegations.
- The Proskauer blog is a secondary legal commentary source.
- The Ballon excerpt is a legal treatise/context source, not a primary court record.
- The January 2018 court order is procedural: it decides motions to dismiss, not final merits.
- It does not reveal exact bot architecture, detection method, proxy use, CAPTCHA-solving method, or account-farm process.
- It is U.S.-specific and legally specific; do not generalise directly to UK/EU law without separate sources.
- It does not measure prevalence of ticket bots across the wider market.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  Automated acquisition of scarce live-event tickets using bots and dummy accounts, followed by resale on secondary markets.

- **What does it fail to represent?**  
  It does not represent independent technical forensics or current bot capability. It is strongest as legal-case evidence of alleged conduct and legal response.

- **What additional evidence would be needed to go further?**  
  Final judgment text if available, complaint/amended complaint, technical expert evidence, bot logs, anti-bot incident reports, enforcement records under the BOTS Act, reseller data, and comparable non-U.S. cases.

## What it cannot show

- It cannot prove every Ticketmaster allegation was true.
- It cannot show exact bot implementation.
- It cannot show current ticket-bot methods.
- It cannot show proxy/CAPTCHA-solver use unless those facts appear in other sources.
- It cannot quantify the overall prevalence of ticket bots.
- It cannot show whether Ticketmaster’s controls were adequate.
- It cannot establish UK/EU legal treatment.
- It cannot replace OWASP OAT for taxonomy or PortSwigger/NIST/ASVS for control guidance.

## Project impact

Use this as a **high-value ticket-bot legal case entry**.

Best uses:

- concrete case evidence for OAT-005 Scalping;
- legal example of ticket-bot injunctions;
- support the “scarce inventory + automation + resale market” pattern;
- compare with Taylor Swift Senate case to distinguish successful alleged acquisition from platform-stress bot traffic;
- support the point that bot problems are not just technical: terms, law, enforcement, platform design, inventory rules, and resale incentives matter;
- strengthen the slot/ticket/inventory abuse section.

Do not use it as:

- current technical-bot capability evidence;
- prevalence evidence;
- proof of all allegations;
- operational guidance;
- UK legal authority;
- a source for bot implementation methods.

## Relationship to other register entries

- **U.S. Senate Ticketmaster / Taylor Swift 2023**: related but separate. Senate case is public-policy/incident claim; Prestige case is litigation/settlement around alleged bulk purchase/resale.
- **OWASP Automated Threat Handbook**: maps to OAT-005, OAT-006, OAT-009, OAT-021, OAT-019.
- **CAPTCHA-solving ecosystem**: relevant to OAT-009 but this case does not identify specific commercial solvers.
- **Proxy ecosystem entries**: relevant to distributed bot operations, but this case does not directly prove residential proxy use.
- **ASVS / NIST / API Security**: useful for control framing: rate limits, session/account integrity, anti-automation, transaction rules.
- **Ballon legal context**: broader scraping/database/bot law; useful but should not replace primary legal documents.

## Dual-use containment

Moderate dual-use. The case names broad methods such as dummy accounts, high-speed infrastructure, CAPTCHA/access-control circumvention, and request regeneration. Use it at the level of legal case facts and threat taxonomy. Avoid reconstructing bot workflows, reserve-request strategies, CAPTCHA circumvention methods, or account-generation methods.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `ticketmaster-prestige-2018-2019-ticket-bots-settlement` |
| Title | *Ticketmaster v. Prestige Entertainment: ticket bots, dummy accounts, CAPTCHA, and settlement injunctions* |
| Organisation / authors | U.S. District Court C.D. Cal.; Proskauer; Ian C. Ballon / Greenberg Traurig |
| Year | 2018-2019 case, 2021 legal context |
| Category | legal case / observed-use allegation / settlement |
| Evidence basis | court pleadings/order / litigation allegations / settlement summary / legal analysis |
| Operational proximity | legally observed-claim |
| Signals / techniques | ticket bots; dummy accounts; CAPTCHA; access controls; purchase limits; reserve requests; request-rate limits; high-speed infrastructure; terms of use |
| Threat types | OAT-005 Scalping; OAT-006 Expediting; OAT-009 CAPTCHA Defeat; OAT-021 Denial of Inventory; OAT-019 Account Creation; partial OAT-015 DoS-style load |
| Project use | Strong ticket-bot legal case showing scarce-inventory automation and legal remedies |
| Main caution | Allegations and settlement, not full technical forensic proof or trial finding; not current capability/prevalence evidence |
| Entry file | `ticketmaster-prestige-2018-2019-ticket-bots-settlement.md` |
