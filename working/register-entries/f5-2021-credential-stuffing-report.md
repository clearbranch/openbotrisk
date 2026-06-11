# F5 Labs 2021 Credential Stuffing Report

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: Claude (chat interface)
- **Model name + version, if known**: Claude Opus 4.8
- **Source access**: full text (provided as a PDF rendering of the F5 Labs web article)
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Vinberg, S. & Overson, J. (2021). *2021 Credential Stuffing Report.* F5 Labs (Threats / Top Risks). Additional contributors: Woods, Ghosemajumder, Boddy, Pompon, Koritz. Published 2021-02-09. Prior editions were published as the *Credential Spill Report* by Shape Security (now part of F5).
- **Source URL or path**: provided as `SRC-034-f5-2021-credential-stuffing-report.pdf` (uploaded). Canonical URL is an F5 Labs (`f5.com/labs`) article; the exact path was **not captured in the provided file — flag as unverified**, confirm before citing on the site.
- **Date accessed**: 2026-06-06
- **Category**: vendor (F5/Shape; the tooling sections also carry threat-surface relevance)
- **Evidence basis**: threat-intel; empirical-operational (vendor-measured) — a vendor threat report that combines open-source credential-spill aggregation with an operational measurement study run on the vendor's own production systems
- **Operational proximity**: `observed` (vendor-measured). The Collection X analysis quantifies credential-stuffing activity against four real Fortune 500 production sites, and the spill statistics observe the supply side via open-source aggregators; both are vendor / vendor-adjacent telemetry, not independent measurement, so this caps at `observed` rather than `measured` — the register reserves `measured` for independent honey-site / in-the-wild studies (cf. SRC-015). This is currently the strongest non-academic observed-use evidence for credential stuffing specifically.
- **Tags**: credential-stuffing, account-takeover, credential-theft, automation-tooling, behavioural-evasion, attacker-economy

## What it claims

- Credential spill *incidents* nearly doubled between 2016 and 2020, while the total *volume* of spilled credentials trended down; average spill size fell from ~63M records (2016) to ~17M (2020). F5 reads "more frequent but smaller" as a market maturing, not defenders winning.
- 2020 still saw ~1.86 billion credentials spilled.
- Plaintext storage was responsible for the largest share of spilled credentials over the prior three years (~42.6%); the long-discredited MD5 hash remained in use.
- Detection is poor: across 96 incidents with enough data to compare breach vs discovery dates, median time to discovery was 120 days and average 327 days; spills are frequently found on the dark web before the breached organisation discloses.
- Tracing "Collection X" (a ~9-billion-credential aggregate posted to dark-web forums in January 2019) across four Fortune 500 customers: of 2.9B credentials used against the four sites in a year, ~900M (≈1 in 3) matched Collection X; of those, 610M were used by legitimate customers, 370M by attackers, and 80M by both. Compromised credentials showed up in legitimate human use most often at banks.
- Credential abuse follows a five-stage lifecycle relative to public disclosure (slow/quiet → ramp-up → blitz → drop-off → reincarnation).
- Attackers sit on a sophistication spectrum; F5 defines sophistication as the ability to blend in with genuine users, and notes attackers escalate sophistication (and cost) only when a target's defences force it.
- A maturing, low-cost tooling/service ecosystem — network-level request scripts, headless-browser automation, behaviour-generating no-code tools, and human CAPTCHA-solving "microwork" — drives attack cost down and threatens existing controls.
- "Fuzzing" (trying common variations of a spilled username) is more common among sophisticated attackers and mostly occurs *before* public disclosure of the spill.
- Recommends anti-automation platforms plus operational best practices (compromised-credential checks, reduced login-failure feedback, diurnal-pattern and login-success-rate monitoring, cross-organisation signal sharing, security/marketing coordination).

## What evidence it provides

- **Spill statistics (Figs 1–9)**: derived from open-source aggregators (Have I Been Pwned, DeHashed, Under the Breach) plus press releases. F5 notes this captures only *disclosed* spills and explicitly excluded incidents where the organisation withheld counts (Reddit, GitHub, Dell). So the supply-side numbers observe disclosed spills, not a complete census.
- **The Collection X lifecycle analysis**: operational measurement using Shape Enterprise Defense (then protecting ~2B accounts), comparing Collection X usernames against credential-stuffing traffic at four Fortune 500 customers (two banks, one food & beverage, one retailer) — ~72B login transactions over 12 months, six months either side of disclosure. Real production telemetry, but vendor-run and not independently reproducible.
- **Tooling claims** (Sentry MBA; headless Chrome / Puppeteer; puppeteer-extra-stealth; Browser Automation Studio; microwork platforms): described from F5/Shape's observation of attacker tooling and Shape's telemetry (e.g., BAS usage growth observed in 2019). Field observation, not controlled testing.
- **Password-storage findings**: inferred from disclosed incidents where the storage method was known; F5 cautions the data is a partial view and warns against causal over-reading (e.g., not concluding bcrypt is weak from its prevalence among 2020 spills).

## Signals or techniques mentioned

- Attacker sophistication tiers: network-level request forgery → headless-browser automation → human-behaviour simulation → real-human (microwork) solving.
- Tooling named, as field evidence of capability (not as instructions): Sentry MBA (HTTP-level, proxy rotation, CAPTCHA OCR, multi-stage requests); headless Chrome / Puppeteer; the puppeteer-extra-stealth evasion architecture; Browser Automation Studio (no-code behaviour generation, compile-and-resell ecosystem); CAPTCHA-solving "microwork" platforms.
- Evasion surfaces referenced: the `navigator.webdriver` automation flag (and that it gets bypassed), WebGL/canvas fingerprint suppression, generated human-like mouse/keyboard behaviour, and an outdated user-agent string as a tell of an older toolchain.
- Defender-side signals: login success-rate drops (normal human rates cited at ~60–80%), password-reset request spikes, diurnal-pattern deviation, and cross-organisation / cross-account behavioural anomalies as account-takeover indicators.
- Fuzzing as a username-variation technique (described at the class level; specific variation patterns deliberately not reproduced — see dual-use note in What it cannot show).

## Threat types covered

- **OAT-008 Credential Stuffing** (primary); **OAT-007 Credential Cracking** / brute force (adjacent); **account takeover**; and login/sign-up abuse generally (the tooling is described as targeting "any site with a login or sign-up form"). The credential theft/spill supply side is context, not itself an OAT detection target.

## Framing distance

- **What real-world problem does it approximate?** The credential-stuffing slice of the abuse landscape end-to-end: supply (spills) and demand (real attack traffic against large consumer login flows), plus the attacker tooling/sophistication gradient. The Collection X study is a rare real-world quantification of how much login traffic to major sites is driven by compromised credentials.
- **What does it fail to represent?** It is one vendor's telemetry from its large enterprise customers (Fortune 500 banks/retail/F&B) — not the mid-sized booking-style target the project uses as its worked example, not the general web, and not independently audited. Supply-side spill data covers only disclosed spills. Tooling observations are 2020-era (Sentry MBA legacy; BAS several Chrome versions behind) and predate the cloud-browser / AI-agent shift. No methodology detail sufficient for an outsider to reproduce the measurement.
- **What additional evidence would be needed to go further?** Independent (non-vendor) measurement of credential-stuffing prevalence; data from smaller organisations without commercial telemetry; current-era tooling (post-2020 stealth stacks, cloud browsers, AI agents); and external testing of the defender-side detection-efficacy claims.

## What it cannot show

- It cannot establish web-wide prevalence: the figures are vendor-measured against four large customers plus disclosed spills only. "≈1 in 3 logins matched Collection X" is specific to those four Fortune 500 sites in that window, not the internet.
- It cannot independently validate the tooling or efficacy claims — they are F5/Shape observations, not controlled tests.
- The password-storage shares (e.g. 42.6% plaintext) describe disclosed incidents with a known storage method, not all breaches; F5 itself warns against causal reading.
- **Out-of-scope material in the source was deliberately not extracted** (EVIDENCE-REVIEW §3): named incidents/actors (SolarWinds, FireEye) and the criminal resale-market economics (who profits, dark-web pricing and money flow) are excluded; only the technique, lifecycle, tooling-cost, and proximity content was taken. The one legal/enforcement reference (the first major credential-stuffing conviction) is recorded only as "such convictions exist," with the actor and case detail stripped per the legal-record rule.
- **Dual-use containment applied**: the report contains a small automation code snippet, an explicit list of username-fuzzing variations, and step-level tool walkthroughs. None of these were transcribed. This entry records *that* the capabilities and bypass classes exist and their signal families, not any reproducible procedure.

## Project impact

- Primary **observed-use anchor for credential stuffing** — the F5/Shape credential-stuffing report named in the register's observed-use lane (Queued). It moves the credential-stuffing claim from `claimed`/`capability` evidence toward `observed`, with the vendor-measured caveat explicit.
- Supports a Background/landscape point that compromised-credential reuse is a measurable fraction of real login traffic at large consumer sites — cited as vendor telemetry, with the framing distance to the booking-style example stated.
- Corroborates the attacker sophistication gradient (the Iliou simple→advanced taxonomy) from an operational/vendor angle, and supports the in-scope cost-of-automation economics (Sentry MBA free; BAS ~$80/yr; microwork ~$0.10–0.60 per task).
- Doubles as a **calibration case for the v3 proximity axis**: strong, quantified vendor telemetry that still caps at `observed`, not `measured`, because it is not independent.
- Use flags for the register/page step: confirm the canonical URL before citation; treat every figure as vendor-measured; do not reproduce the tooling/fuzzing detail.
