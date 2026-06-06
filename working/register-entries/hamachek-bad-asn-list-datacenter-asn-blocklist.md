# bad-asn-list — open-source ASN blocklist for cloud/hosting/colo traffic (Hamachek)

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: Claude (chat interface)
- **Model name + version, if known**: Claude Opus 4.8
- **Source access**: README full text (fetched); the `bad-asn-list.csv` dataset and helper scripts were not individually inspected
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Hamachek, B. *bad-asn-list: An open source list of ASNs known to belong to cloud, managed hosting, and colo facilities.* GitHub repository `brianhama/bad-asn-list` (MIT license). ~496 stars, 117 forks, 34 commits at access.
- **Source URL or path**: `https://github.com/brianhama/bad-asn-list` (fetched 2026-06-06; resolves). Artifacts: `bad-asn-list.csv`, `cloudflare list.txt`, builder scripts.
- **Date accessed**: 2026-06-06
- **Publication date**: not stated in README; context (the "Nearby" social network, GeoLite2 reference) suggests ~2019–2020 vintage — **flag as unverified**; matters for the efficacy claim (see What it cannot show).
- **Category**: threat-surface — **flagged judgment call** (second instance, after the Wikimedia entry): this is a *defensive-tooling artifact + first-party operator account*, which maps poorly onto foundations/vendor/academic/threat-surface. Filed under threat-surface (operator/target side) as least-bad. Two such sources now strain the vocab — reinforces the case for an explicit "operator/first-party" or "defensive-tooling" category or tag.
- **Evidence basis**: tooling-readme; empirical-operational (first-party, anecdotal/self-reported) — an open-source defensive dataset whose README is a single operator's narrative justification, not a study.
- **Operational proximity**: `observed` (first-party, anecdotal). The README reports real abuse against the author's own real service (account-creation spam/scam/fraud) and a deployed mitigation. It caps well within `observed` — and is the weakest `observed` in the corpus: a single individual, a social-network signup flow, no data beyond one self-reported figure, no methodology. The mitigation-efficacy claim (~90%) is itself only `claimed`-grade. The blocklist *contents* are reference data (n/a for proximity).
- **Tags**: fake-account-creation, datacenter-ip, asn-reputation, network-origin, residential-proxy, detection-signal, tooling, operator-account

## What it claims

- The author ran a social network ("Nearby"); past ~500K monthly active users, spam/scam/bot account-creation traffic became unmanageable.
- Detection methods tried and reported as ineffective or impractical: generic detection (too many false positives/negatives), requiring a Facebook profile for signup, Google sign-in, and a paid commercial service (MaxMind — reported as effective but too expensive at their scale).
- Key realisation: almost all the bad traffic originated from hosting/colo/cloud-provider ASNs — including VPN traffic, since VPNs exit through hosting facilities.
- Mitigation: at account creation, look up the ASN owning the request IP and block (or fraud-score) if it appears on a hand-built list of known hosting/colo/cloud ASNs. Reported result: ~90% of the bad traffic vanished, with — per the author — little legitimate traffic blocked.
- Implementation guidance: load the list into a DB/memory; resolve request IP → ASN (e.g. via MaxMind's free GeoLite2 ASN DB); block / increase fraud score on a hit.
- The list is open-sourced for reuse with community pull requests.

## What evidence it provides

- A reusable artifact: a maintained (community-PR) open-source CSV mapping of cloud/hosting/colo ASNs, plus Cloudflare-format and numeric-only derivatives and builder scripts.
- A single operator's narrative: which signup defences failed for them, and that datacenter-origin blocking solved ~90% of their account-creation abuse. No dataset, no methodology, no false-positive/negative measurement, no time series — an anecdote, not a study.

## Signals or techniques mentioned

- **Network-origin / ASN-reputation signal**: classifying traffic by whether its source IP belongs to a datacenter/hosting/colo/cloud ASN vs a residential/mobile network — used here as a near-binary block/fraud-score signal at account creation.
- The observation that VPN egress is itself hosting-origin (so datacenter-ASN blocking also catches most VPN traffic).
- IP→ASN resolution via MaxMind GeoLite2 ASN database as the lookup mechanism.
- Prior (rejected) signals: social-login gating (Facebook/Google), generic behavioural detection, a paid commercial reputation API.

## Threat types covered

Primary: **fake account creation** (OAT-019 / account-creation abuse) on a signup flow. The datacenter-origin signal itself is **cross-cutting** — the same network-origin heuristic is a standard input signal across credential stuffing, scraping, scalping, ATO, and carding, so the technique generalises well beyond the fake-account context the README describes.

## Framing distance

- **What real-world problem does it approximate?** Whether a simple, cheap network-origin heuristic (block datacenter/hosting ASNs) can suppress automated abuse on a consumer signup flow — and one operator's report that it largely did. It is a concrete, real instance of a foundational detection signal.
- **What does it fail to represent?** It is a single individual's anecdote on a social-network signup flow circa ~2019–2020, with one self-reported efficacy figure and no measurement. A booking/e-commerce or API-heavy target has very different false-positive exposure to datacenter-IP blocking (legitimate cloud-hosted API clients, corporate egress, carrier-grade NAT, privacy users). Crucially, it predates the mainstreaming of **residential-proxy** evasion — the technique's standalone efficacy has since eroded precisely because attackers moved off datacenter IPs to defeat lists like this one.
- **What additional evidence would be needed to go further?** Independent measurement of datacenter-blocking efficacy and false-positive rate by target type and era; current data on what fraction of abuse still originates from datacenter ASNs vs residential proxies; and list freshness/coverage validation (ASN ownership drifts).

## What it cannot show

- It cannot establish efficacy beyond the author's own site; ~90% is self-reported, single-site, single-flow, undated, no methodology.
- It cannot show the false-positive rate ("little legitimate traffic blocked" is an unquantified operator impression, and is context-specific to a consumer social signup).
- It cannot speak to **current** efficacy: the Wikimedia and FP-Agent entries are direct counter-evidence that sophisticated abuse has shifted to residential proxies spanning hundreds of millions of IPs *specifically to evade datacenter-ASN blocking* — so a circa-2019 "90% solved" should not be read as a present-day result.
- The list's coverage/freshness is unverified (community-maintained, ASN ownership changes over time).
- No actor/campaign attribution, no criminal-economics detail, and no attack recipe — dual-use containment is not engaged (a defensive blocklist; the ASNs it names are already trivially known to attackers).

## Project impact

- **The canonical worked example of the network-origin / ASN-reputation detection signal** for a Foundations/Techniques page — a real, open-source, widely-forked instance of "datacenter-IP blocking," with an operator's own account of why they reached for it and what else failed first (a useful demystification arc: social-login gating and generic detection didn't work; network origin did).
- **The "before" anchor in the datacenter-blocking → residential-proxy arms race.** This is the defense that residential proxies exist to evade. It pairs directly with the Wikimedia entry (operator: residential proxies now defeat datacenter/IP-based limits) and FP-Agent (agents running from residential networks) to tell a complete, vendor-free arms-race story across three sources: cheap network-origin blocking worked → attackers moved to residential egress → network origin alone no longer suffices, pushing defenders toward behavioural detection.
- **Low-rigour observed-use colour**: a practitioner data point that hosting-origin traffic once dominated account-creation abuse on at least one real consumer service — filed as anecdotal, not as a prevalence claim.
- **Possible methodology/tooling resource** for the project's own dataset EDA: an ASN→datacenter-flag enrichment is a reasonable feature to compute over any traffic dataset; this list (or its provenance) is a candidate input, with the freshness caveat.
- **Flags**: (1) second source straining the category vocab (operator/defensive-tooling) — consider formalising a tag; (2) publication date unverified (~2019–2020) and material to the efficacy reading; (3) the ~90% efficacy is dated, single-site, anecdotal — frame as historical, with the residential-proxy sources as the counterweight; (4) proximity `observed` but at the anecdotal floor — do not overweight relative to the measured/operator sources.
