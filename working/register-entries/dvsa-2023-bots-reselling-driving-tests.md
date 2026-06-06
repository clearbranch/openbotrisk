# How we're dealing with bots and the reselling of driving tests - DVSA 2023

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: Codex
- **Model name + version, if known**: GPT-5
- **Source access**: full text
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Ryder, L. / Driver and Vehicle Standards Agency. (2023, June 29). *How we're dealing with bots and the reselling of driving tests*. Despatch for driver and rider trainers. https://despatch.blog.gov.uk/2023/06/29/how-were-dealing-with-bots-and-the-reselling-of-driving-tests/. Accessed 2026-06-06.
- **Source URL or path**: https://despatch.blog.gov.uk/2023/06/29/how-were-dealing-with-bots-and-the-reselling-of-driving-tests/
- **Date accessed**: 2026-06-06
- **Category**: threat-surface
- **Evidence basis**: threat-intel (victim/platform-side observed-use account)
- **Operational proximity**: observed - DVSA reports bots exploiting its own live driving-test booking service, but the post does not provide independent measurement, traffic counts, or detection logs.
- **Tags**: scarce-resource-abuse, appointment-abuse, slot-sniping, limited-inventory, inventory-hoarding, booking-flow-abuse, availability-polling, cancellation-monitoring, fast-booking, auto-booking, slot-resale, behavioural, challenge-response

## What it claims

- High waiting times for driving-test appointments have led to increased use of automated bots that exploit DVSA's driving-test booking service.
- Bots can be programmed to search for and reserve driving-test appointments, and they can work faster than humans.
- Organisations use bots to find and secure available appointment slots more quickly than individual customers.
- Some organisations hold driving-test appointments until they can resell them at a higher price, which makes it harder for test-ready learners to find appointments at suitable dates and times.
- DVSA uses CAPTCHA when it suspects a user may be a bot and also uses unspecified advanced bot-protection measures.
- DVSA does not disclose details of the advanced measures because doing so could help people evade them.
- Bot mitigation creates a balancing problem: measures intended to stop automated access can inconvenience genuine learner drivers and approved driving instructors (ADIs), including through an "error 15" access problem after a recent service change.
- DVSA says the technologies used by profiteers continue to advance and can often be adjusted around changes DVSA makes.
- DVSA is using education and communication to encourage learners to use official booking channels and to be careful with third-party services that may collect personal data.
- DVSA says some businesses exploit the ADI booking and test-management service, and that it introduced stricter terms and conditions on 2023-01-09 and tightened monitoring of that system.
- DVSA planned further ADI-service controls, including stopping users from using the service if they cancel 20% or more of tests in the 10 working days before the test, and suspending accounts without a linked ADI.

## What evidence it provides

The source is a platform-side operational account from DVSA, the organisation running the driving-test booking service. It provides first-party claims that bots are exploiting the booking service, that appointments are being held and resold at inflated prices, and that DVSA has had to deploy anti-bot controls.

The post gives concrete examples of mitigation classes: CAPTCHA when bot suspicion is raised, unspecified advanced bot protection, monitoring of ADI-service usage, terms-and-conditions changes introduced on 2023-01-09, planned cancellation-rate restrictions, planned account-linkage requirements, and user education through official channels.

The post does not provide traffic volumes, bot counts, detection metrics, resale-market measurements, false-positive rates, or technical details of the advanced bot-protection measures. Its evidence basis is therefore DVSA's own observed operational account, not an independently measured study.

Public comments are visible on the page, but this extraction uses the DVSA-authored post as the source evidence and does not treat comments as verified substantiation.

## Signals or techniques mentioned

- Automated software programs that mimic human behaviour.
- Searching for driving-test appointments.
- Reserving driving-test appointments.
- Fast booking relative to individual human customers.
- Holding appointment inventory for later resale.
- CAPTCHA challenges when a user is suspected to be a bot.
- Unspecified advanced bot-protection measures.
- Differentiation between bots and genuine learners / ADIs.
- False-positive or customer-friction symptom: "error 15" after a recent service change.
- Monitoring usage of the ADI booking and test-management system.
- Terms-and-conditions controls and account controls for ADI-linked accounts.
- Cancellation-rate rule: planned restriction for users cancelling 20% or more of tests in the 10 working days before the test.

## Threat types covered

Scarce-resource appointment abuse: automated capture, holding, and resale of driving-test appointment slots. This maps most closely to OWASP-style denial of inventory / scalping patterns, but the source's own object is a public-service appointment slot rather than retail inventory or tickets.

## Scarce-resource abuse fields

- **Scarce resource targeted**: appointment
- **Abuse phase**: monitoring / booking / holding / resale / cancellation exploitation
- **Website-facing action**: polling availability / completing booking / holding inventory / reselling
- **Evidence of use**: observed-use
- **Abuse outcome**: ordinary users blocked / inventory unavailable / inflated resale price / degraded fairness / operational load
- **What the source cannot show**: The source cannot show prevalence, the share of bookings affected, the exact automation mechanism, the identity or intent of particular operators, whether all third-party cancellation-finding services use bots, detection efficacy, false-positive rate, or generality beyond DVSA's driving-test booking platform.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** Victim/platform-side observation of appointment-slot abuse in a real booking system where the scarce resource is a driving-test appointment. It directly illuminates the operational pattern of fast automated slot search/reservation, holding appointments, resale at inflated prices, anti-bot countermeasures, and customer friction caused by mitigation.
- **What does it fail to represent?** It does not expose raw telemetry, detection rules, bot tooling, bot operator workflows, resale-market data, or independent measurement. It names control classes but intentionally withholds advanced bot-protection details. It is one public-service booking platform under backlog pressure, so it does not by itself represent ticketing, private-sector reservations, product drops, or appointment systems with different account and transfer rules.
- **What additional evidence would be needed to go further?** Booking-service telemetry quantifying bot attempts, successful automated bookings, resale-linked bookings, false positives, and post-control changes; independent or regulatory evidence about resale markets; technical detail on the signals used without creating bypass instructions; and comparable accounts from other appointment or booking platforms.

## What it cannot show

- That the problem's prevalence can be quantified from public information; the post says the use of bots rose but gives no count or rate.
- That any specific anti-bot measure is effective; CAPTCHA and advanced bot protection are named, but performance is not reported.
- That all appointment resellers or cancellation-finding services use bots; the post warns about third-party services but does not classify every such service as automated abuse.
- That the same pattern generalises to all scarce-resource booking systems; the source is specific to DVSA driving-test appointments.
- That the legal status of resale is the same in other scarce-resource domains; the post says this practice is unfair but not illegal in the DVSA context.
- That users receiving "error 15" were bots; the post explicitly frames this as genuine-user inconvenience caused by bot mitigation.

## Project impact

- Provides a strong victim/platform-side observed-use source for scarce-resource appointment abuse.
- Supports the project's distinction between generic scraping and scarce-resource abuse: the bot activity matters because it captures a limited transactional resource, not merely because it retrieves availability information.
- Gives a concrete booking-flow example for the recurring booking-style worked example in `PROJECT.md`.
- Supplies cautious evidence for mitigation trade-offs: anti-bot measures can create false-positive or access-friction symptoms for genuine users.
- Useful for the evidence register's scarce-resource index with `scarce_resource_targeted=appointment`, `evidence_of_use=observed-use`, and operational proximity `observed`.
