# FTC Brings First-Ever Cases Under the BOTS Act

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: full text from attached PDF export of FTC press release; public FTC URL independently resolved during extraction
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Federal Trade Commission. 2021. *FTC Brings First-Ever Cases Under the BOTS Act: Ticket brokers will face partially suspended judgment of more than $31 million in civil penalties*. FTC press release, 22 January 2021.
- **Source URL or path**: `https://www.ftc.gov/news-events/news/press-releases/2021/01/ftc-brings-first-ever-cases-under-bots-act`; local uploaded PDF: `FTC Brings First-Ever Cases Under the BOTS Act _ Federal Trade Commission.pdf`
- **Date accessed**: 2026-06-06
- **Category**: threat-surface
- **Evidence basis**: legal-record
- **Operational proximity**: observed — the source is an enforcement/legal record describing alleged real-world use of ticket-buying automation against actual online ticketing flows. It should still be framed as FTC allegations and proposed consent orders, not as independent technical measurement by this project.
- **Tags**: legal-record, observed-use, ticket-bots, scalping, limited-stock-attacks, inventory-hoarding, purchase-limit-circumvention, account-creation, ip-obfuscation, fake-accounts, credit-cards, ticketmaster, bots-act, enforcement, business-logic-abuse

## What it claims

- The FTC says it took legal action against three New York-based ticket brokers that allegedly used automated software to buy tens of thousands of tickets for popular concerts and sporting events.
- The FTC says the brokers subsequently resold those tickets to fans at higher prices and made millions of dollars from the resale activity.
- The source states that this was the first FTC case brought under the Better Online Ticket Sales Act, enacted in 2016.
- The FTC states that the BOTS Act gives it authority to take enforcement action against individuals and companies using bots or other means to circumvent online ticket-purchase limits.
- The FTC alleges the defendants purchased more than 150,000 tickets for popular events.
- The FTC alleges the defendants used automated ticket-buying software to search for and reserve tickets automatically.
- The FTC alleges the defendants used software to conceal IP addresses.
- The FTC alleges the defendants used hundreds of fictitious Ticketmaster accounts and credit cards to evade posted ticket limits.
- The FTC says the proposed settlement included more than $31 million in civil penalties, partially suspended because of inability to pay, with more than $3.7 million to be paid.
- The proposed orders prohibit further BOTS Act violations, including using methods to evade ticket limits, using false identities to buy tickets, or using bots to facilitate ticket purchases.
- The FTC says the complaints and proposed consent decrees were filed by the Department of Justice on the FTC's behalf in the U.S. District Court for the Eastern District of New York.

## What evidence it provides

- The source is an FTC press release summarising enforcement actions, proposed settlements, and the alleged conduct underlying those actions.
- The strongest evidence it provides is legal/enforcement evidence that ticket-buying automation was alleged to have been used in real commercial ticket-resale operations, not merely that the capability exists.
- The source gives scale indicators: more than 150,000 tickets allegedly purchased, more than $31 million in civil penalties entered in proposed judgments, and more than $3.7 million in payments after partial suspension.
- The source identifies the relevant mechanism categories at a high level: automated searching/reserving, IP-address concealment, fictitious accounts, multiple credit cards, and purchase-limit circumvention.
- The source does not provide raw logs, detection methods, bot code, account-linking analysis, or the full complaints/orders inside the PDF export.
- The source uses legal language: several claims are allegations in an enforcement action and settlement context. It should not be written as if it were an independent technical study or a fully litigated factual finding.
- The source provides no systematic prevalence estimate for ticket bots, scalping bots, or bot-driven limited-stock abuse outside the named enforcement actions.

## Signals or techniques mentioned

- Automated ticket-buying software.
- Automated ticket search.
- Automated ticket reservation.
- IP-address concealment.
- Fictitious Ticketmaster accounts.
- Use of multiple credit cards.
- Circumvention of event ticket-purchase limits.
- Resale of tickets bought through allegedly unlawful means.
- False identity use in purchase flows.
- Bot-assisted purchasing against a primary ticketing platform.
- Limited-stock inventory capture.

## Threat types covered

- Ticket scalping / ticket bots.
- Inventory hoarding in limited-stock transactional systems.
- Purchase-limit circumvention.
- Business-logic abuse of ticketing purchase flows.
- Automated account / identity abuse.
- IP-obfuscation-assisted automation.
- Resale-market abuse enabled by primary-market automation.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** It approximates the real operational problem of bots acting against scarce-inventory ticketing flows: automated purchase attempts, account and payment-identity scaling, IP obfuscation, and resale monetisation. It is valuable because it is a legal/enforcement record tied to alleged real-world conduct, not just a vendor or tooling claim.
- **What does it fail to represent?** It does not provide technical implementation detail, detection data, platform-side telemetry, or prevalence. It is specific to ticket resale and the U.S. BOTS Act context. It also sits in legal-allegation language: the project should not overstate it as a neutral measurement study or a complete technical account.
- **What additional evidence would be needed to go further?** The full complaints, consent decrees, and court documents; platform-side detection records; ticketing-platform engineering postmortems; independent studies of ticket bot prevalence; and comparable enforcement records from other jurisdictions or sectors such as booking, appointments, or high-demand retail drops.

## What it cannot show

- It cannot show how common ticket bots are across the ticketing industry.
- It cannot show the success rate of ticketing platforms' bot defences.
- It cannot show which specific detection signals identified the alleged automation.
- It cannot show whether similar techniques are used in appointment booking, retail drops, or other limited-stock systems without additional sources.
- It cannot show the full technical architecture of the bots, accounts, payment methods, or proxy/IP-concealment setup.
- It cannot show that every secondary-market reseller uses bots.
- It cannot show that legal enforcement alone fixes ticket-bot abuse.
- It should not be used as a procedural source for bypassing ticketing controls; the useful project signal is the class of abuse and the legal/enforcement proximity.

## Project impact

- This is a high-value observed-use source for the project's limited-stock / booking / slot-sniping strand.
- It gives stronger evidence than a vendor explainer because it records enforcement action over alleged real-world use of automation against ticketing systems.
- It supports the project's point that scarce-inventory abuse is not only a theoretical bot-management category; it has generated concrete legal enforcement.
- It is useful alongside vendor explainers such as DataDome's ticket-bot article: the FTC source gives proximity to real-world use, while the vendor article supplies a broader methods taxonomy.
- It is a good candidate for a short sidebox on BOTS Act enforcement and the legal attempt to break the ticket-bot business model.
- It should be cited with careful wording: "FTC alleged" or "FTC enforcement action stated", not "proved" unless the underlying orders are separately checked.

## Possible register row

| Field | Value |
|---|---|
| Register id | `ftc-2021-first-bots-act-cases` |
| Title | *FTC Brings First-Ever Cases Under the BOTS Act* |
| Category | threat-surface |
| Evidence basis | legal-record |
| Operational proximity | observed |
| Tags | legal-record; observed-use; ticket-bots; scalping; purchase-limit-circumvention; fake-accounts; ip-obfuscation; business-logic-abuse |
| Project use | Observed-use / enforcement evidence for ticket bot abuse and limited-stock automation |
| Main caution | Enforcement press release; allegations and proposed orders, not a technical measurement study |
