# Agent prompt — source extraction for evidence review

You are extracting evidence from a single source for the `openbotrisk` project. Output is a structured register entry. This is not synthesis or drafting — that is a separate task. Extract what the source says and the metadata the project needs.

The repo already exists with `PROJECT.md`, `EVIDENCE-REVIEW.md`, and `GOVERNANCE.md` committed. **Read all three before doing anything.** They define scope, the extraction fields, and the editorial discipline, and they are the single source of truth. Treat them as authoritative. The condensed dossier below is an orientation aid, not a replacement for reading them — where the dossier and the committed docs disagree, the committed docs win.

---

## CONDENSED PROJECT DOSSIER (orientation only — the three repo docs are authoritative)

**What the project is.** An open, written investigation of the *bot and abuse prevention* category: detecting and mitigating automated adversarial activity against legitimate web-facing systems. The output is a public Quarto site plus reproducible code. It is information work, not product work, not vendor evaluation, not advocacy. The goal is to map the territory honestly, including the parts that cannot be entered with public data and open tools.

**Methods, not actors.** A technique described abstractly is in scope; a campaign attributed to a named actor is out. A vendor explaining *how* they detect credential stuffing is in; a threat-intel report naming a group is out. Out of scope also: criminal economics, specific incidents, vendor comparison, broader cyber (malware, intrusion, vuln research, EDR, IR), IoT/network-layer DDoS.

**Named targets vs named actors.** A named *target* site — e.g. a "how to scrape `<site>`" writeup — is not out of scope the way a named *actor* is. But extract it only for its territory-level content: what anti-bot system the target runs, what signals it exposes, what *class* of bypass is claimed. Do not extract the operational target-specific scraping steps. If a source is purely operational how-to with no territory-level signal (no detection mechanism, no signal taxonomy, no defender behaviour), flag it for skip per EVIDENCE-REVIEW §3 rather than extracting it. A named detection *vendor* whose product is being bypassed (e.g. a "bypass Imperva" writeup) is a defender, not an out-of-scope actor — extract it as threat-surface evidence about that vendor's detection surface.

**Vendor material is evidence, not subject.** Marketing claims, white papers, case studies, and patents are signal about what the field *claims* to do. The project does not characterise or rank individual vendors. Vendor efficacy numbers are vendor-measured and unverifiable from outside unless independently corroborated.

**Four evidence categories** (EVIDENCE-REVIEW §2), each with different source types and reading methods:

- `foundations` — basic concepts (IPs, fingerprinting basics, headers, TLS, sessions). Read efficiently; settled material.
- `vendor` — bot/abuse-prevention companies' public material. Read with explicit awareness of bias; separate claim from substantiation.
- `academic` — peer-reviewed / pre-print work. Structured extraction; anchor on Iliou (2021/2022) and OWASP.
- `threat-surface` — attacker tooling, automation infrastructure, the browser-native-automation / AI-agent shift. Read with awareness of source provenance; none of the three corners (scraper-side, vendor-side, independent) is neutral.

**Framing distance is the project's central analytical move** (EVIDENCE-REVIEW §5). Public datasets, vendor blogs, academic papers, and commercial telemetry are *not* equivalent evidence. Each approximates the real problem differently and fails to represent it differently. Naming this per source is what keeps the project's position visible. This is the most important field below.

**Capability is not use** (the `operational proximity` axis, schema v3). "This tool/technique exists" is weaker evidence than "it is observed against real sites." Record proximity (`capability` / `claimed` / `observed` / `measured` / `n/a`) separately from evidence basis: the corpus skews heavily to capability and claimed, `observed` is mostly vendor telemetry, and real measurement against targets is rare. Do not let a mature tooling market stand in for evidence of real-world use.

---

## INPUTS

The author provides:

- **Source identifier**: URL for web sources, or relative path for locally archived sources
- **Category**: one of `foundations`, `vendor`, `academic`, `threat-surface`
- **Optional notes**: any context about why this source is being read, what to focus on, what to ignore

If any of these are missing or ambiguous, stop and ask.

---

## PROCESS

1. Read `PROJECT.md`, `EVIDENCE-REVIEW.md`, and `GOVERNANCE.md` in the repo
2. Access the source. For URLs, fetch the page. For PDFs, read the document. If access fails, stop and report
3. Identify the source type and key bibliographic metadata
4. **Existing-source check.** Check whether *this exact source* (same document / URL) is already extracted in `working/register-entries/`. If it is, this is a re-extraction, not a new entry — follow the filename / versioning convention (a new versioned file under the same register id), and do not create a second register row. If it is a *different* source — even another blog post or doc page from the same vendor — it gets its **own atomic entry**, provided it is in scope and carries territory-level signal. Distinct sources are kept separate; do **not** fold them together, and do **not** skip a distinct source just because it overlaps an existing entry — selecting between overlapping entries is the page-writing step's job, not this one. The only reasons to skip are out-of-scope (PROJECT §3) or purely operational how-to with no territory-level signal (see Named targets above). Flag any genuine judgement call to the author rather than deciding alone
5. Read the source enough to fill the extraction fields below honestly — not skimming, not exhaustive
6. Produce a register entry following the structure below. For a new source, create `working/register-entries/<slug>.md`. For a re-extraction of a source already extracted, follow the project's filename / versioning convention (a new versioned file alongside the existing one) rather than overwriting it
7. Do not modify the main reading register (`quarto/.../literature-evidence-register.qmd` or `working/reading-register.md`) — the author merges entries manually after review
8. Report back with the file path of the entry and any flags raised

---

## EXTRACTION DISCIPLINE (agent-facing hard rules)

These operationalise GOVERNANCE §7 and EVIDENCE-REVIEW §4 at extraction time, so the constraints bind while you extract rather than only being caught at the author's review.

- **Attribution per claim.** Every bullet in "What it claims" must be something *this source* actually says. Do not blend in general field knowledge, do not merge in what other sources say, do not produce a confident-sounding claim no single passage supports. If you are synthesising across the source's sections, that is fine; if you are reaching beyond the source, stop.
- **Citation integrity.** Never emit a citation, DOI, or URL you have not confirmed resolves to the thing you are citing. If a reference is implied but you cannot confirm it, write the partial reference and flag it as unverified. Inventing a plausible-looking citation is the single worst failure mode here.
- **Claim vs substantiation.** For vendor and threat-surface sources especially, separate what is *claimed* from what is *evidenced*. Mark vendor detection-rate / efficacy / prevalence figures as vendor-measured and not independently verifiable unless the source cites an external basis. Mark open-source-tool README claims as maintainer claims, not independent test results.
- **Use explicit absence tokens.** Where a field cannot be filled from the source content, write `Not stated` or `Cannot determine from source` and say briefly why. Do not infer, do not pad, do not guess to make the entry look complete.
- **Source-quality check.** If the source is low-substance marketing with no technical content, or is out of scope per EVIDENCE-REVIEW §3 (named actors, criminal economics, broader cyber), do not extract it — flag it for skip/rejection with the reason (see Stop-and-ask).
- **No over-claim from a single source.** Findings preserve the source's scope. A controlled study does not "prove" production behaviour; a vendor claim does not establish a capability works.
- **Operational proximity, set honestly and orthogonally.** Record how close the source is to *observed abuse against a real target* (`capability` / `claimed` / `observed` / `measured` / `n/a`), independent of rigour. The common error is to read a rigorous controlled experiment as `observed` or `measured`; it is `capability` unless it measures real-target activity. Vendor capability docs are `capability`; vendor "we stop X" / bypass-vendor "works against Y" claims and self-report surveys are `claimed`; vendor telemetry reports are `observed` (vendor-measured); honey-site and in-the-wild studies are `measured`. Do not infer use from the existence of a capability.
- **Dual-use, no-recipe at extraction.** For bypass, anti-detect, and evasion sources (and operational detail inside legal/victim records), extract *that* a technique or bypass class exists and its proximity — not a reproducible procedure. Do not transcribe working evasion code, step-by-step bypass sequences, or target-specific operational steps into the entry (this extends the Named-targets rule above to all attacker-side sources). Capture the signal families and detection surfaces named, the class of bypass claimed, and the framing distance; leave the recipe in the source. Publication-side enforcement of this is GOVERNANCE §4/§7.
- **Scarce-resource abuse is not generic scraping.** If a source concerns slot sniping, appointment abuse, reservation abuse, ticket scalping, product-drop abuse, inventory hoarding, denial of inventory, queue abuse, booking-flow abuse, cancellation monitoring, limited-inventory abuse, or fast booking automation, record the scarce-resource fields separately. Availability polling may be scraping-like, but the abuse pattern is competition for a scarce transactional resource.

---

## OUTPUT STRUCTURE

The entry follows this template exactly. Every field is filled. If a field genuinely doesn't apply (rare), say so explicitly with reasoning rather than leaving blank.

```markdown
# <Title of source>

## Extraction run metadata

- **Extraction date**: YYYY-MM-DD
- **Extraction agent**: Claude Code / Codex / Claude / ChatGPT / Gemini / other
- **Model name + version, if known**: e.g. Claude Opus 4.x / GPT-x / not stated (do not guess a version)
- **Source access**: full text / partial / abstract-only / paywalled — stopped
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Full reference. For academic: authors, year, title, venue, DOI if available. For vendor: organisation, title, URL, date accessed. For threat-surface: as appropriate to source type.
- **Source URL or path**: Direct link to the source, or relative path if archived
- **Date accessed**: YYYY-MM-DD
- **Category**: One of foundations / vendor / academic / threat-surface
- **Evidence basis**: One of empirical-academic / empirical-operational / survey / vendor-claim / capability-doc / tooling-readme / methods-taxonomy / taxonomy / threat-intel / legal-record (see register appendix for definitions). This is the field that lets the register distinguish a controlled experiment from a marketing claim.
- **Operational proximity**: One of capability / claimed / observed / measured / n/a (see register appendix). How close the source sits to *observed abuse against a real target* — **orthogonal** to evidence basis, which records rigour. A controlled lab PoC is `capability` here however rigorous it is; vendor production telemetry is `observed`; a honey-site or in-the-wild measurement is `measured`; a taxonomy or non-bot-use foundation is `n/a`. Give the value and one sentence justifying it. If the source mixes levels, record the highest it *independently* supports and note the mix.
- **Tags**: Topic tags as relevant. Include `standards` if the source is an RFC, W3C spec, or similar canonical reference. Other useful tags: `taxonomy`, `survey`, `methods`, `behavioural`, `fingerprinting`, `infrastructure`, `cloud-browser`, `ai-agent`, `tls`, `entity-resolution`, etc. For scarce-resource sources, include `scarce-resource-abuse` plus relevant specific tags from the register appendix. Use existing tags if they fit; introduce new ones sparingly.

## What it claims

The substantive claim(s) the source makes, in extracted form. Bullet points, one claim per bullet. Use the source's own framing rather than the project's. If the source makes many claims, prioritise the load-bearing ones — claims that bear on the source's argument or that the project might cite.

Do not embed the project's opinion in this section. Just what the source says. (See Extraction discipline: attribution per claim.)

## What evidence it provides

For each significant claim, what the source offers to support it: experiments, datasets, case studies, references to other sources, or none. If a claim has no supporting evidence beyond assertion, say so. If the source is itself reporting empirical results, summarise the empirical basis (sample size, time period, method). Distinguish claim from substantiation explicitly for vendor and tooling sources.

## Signals or techniques mentioned

Specific technical content the source describes. Bullet points. Examples of what goes here:

- Specific signals: TLS fingerprints, JA3/JA4, click cadence, mouse trajectory, navigator.webdriver, header order, etc.
- Specific methods: XGBoost, autoencoders, isolation forest, graph neural networks, sequence models, rule-based heuristics, etc.
- Specific infrastructure: cloud browser services, anti-detect browsers, residential proxy networks, etc.

This field exists so future searches across the register can find which sources cover which technical material. Name the signal/method/infrastructure concretely — these populate the register's signals-and-techniques cross-index, so vague phrasing here breaks searchability.

## Threat types covered

Which OWASP OAT categories (e.g. OAT-001 Carding, OAT-008 Credential Stuffing, OAT-011 Scraping) or similar abuse categories the source addresses. If the source does not map to OAT, describe in the project's vocabulary (credential stuffing, scalping, scraping, account takeover, click fraud, etc.). If the source is method/infrastructure-only with no specific threat type, write `Not threat-specific`.

## Scarce-resource abuse fields

If the source concerns scarce-resource abuse — including slot sniping, appointment abuse, reservation abuse, ticket scalping, product-drop abuse, inventory hoarding, denial of inventory, queue abuse, booking-flow abuse, cancellation monitoring, limited-inventory abuse, or fast booking automation — record the following fields separately.

If the source does not concern scarce-resource abuse, write `Not applicable — source does not concern scarce-resource abuse`.

- **Scarce resource targeted**: appointment / ticket / reservation / product / booking / queue position / other
- **Abuse phase**: monitoring / account preparation / queue entry / booking / holding / transfer / resale / no-show / cancellation exploitation
- **Website-facing action**: polling availability / entering queue / solving challenge / completing booking / holding inventory / changing booking / transferring booking / reselling
- **Evidence of use**: measured-use / observed-use / vendor-measured / legal-record / regulatory-record / market-evidence / capability-only / controlled-PoC. This is a scarce-resource-specific classification and does not replace `Operational proximity`.
- **Abuse outcome**: ordinary users blocked / inventory unavailable / inflated resale price / no-show / degraded fairness / distorted metrics / operational load
- **What the source cannot show**: Be explicit about whether the source cannot show prevalence, intent, automation, hostile use, detection efficacy, or generality beyond one platform/vendor/customer.

Do not collapse scarce-resource abuse into generic scraping. Availability polling may be scraping-like, but the abuse pattern is competition for a scarce transactional resource.

## Framing distance

This is the most important analytical field. Three parts:

- **What real-world bot/abuse problem does this source approximate?** What part of the operational territory does the source actually illuminate? Be specific.
- **What does it fail to represent?** What's absent, simplified, or biased about how the source approaches the territory? Common gaps include: missing adversarial pressure, controlled vs production data, single-site vs cross-site, missing commercial telemetry, dated threat model, etc.
- **What additional evidence would be needed to go further?** What would a reader need to actually understand the territory beyond what this source provides?

Be honest. The project's analytical position depends on naming framing distance per source explicitly. Avoid generic phrases like "limited generalisability" — say *what* doesn't generalise and *why*.

## What it cannot show

The limits of the source — what readers should not conclude from it alone. Examples: "high accuracy on this dataset does not generalise to production traffic," "vendor claims about detection rates are not independently verifiable," "academic threat models pre-date AI browser agents." Distinct from framing distance in that this field names specific over-claims to avoid.

## Project impact

How this source affects the project's writing or taxonomy. Bullet points. Examples:

- "Provides the technical detail for the Foundations page on browser fingerprinting"
- "Vendor claim X is cited as evidence of what the field claims to do, with caveat that it is unverified"
- "Contradicts source Y's framing of credential stuffing detectability; worth surfacing the disagreement"
- "Read but offers nothing new beyond what is already in the register" (legitimate finding — record and move on)

If the source was read and rejected as not useful for the project, this field is where that decision is recorded with the reason.
```

---

## WORKED EXAMPLE

A fictional but representative example showing what a good entry looks like. Use this as the bar.

```markdown
# Detection of Advanced Web Bots via Mouse Movement Analysis — Smith et al. 2023

## Extraction run metadata

- **Extraction date**: 2026-05-31
- **Extraction agent**: Claude Code
- **Model name + version, if known**: Claude Opus 4.8
- **Source access**: full text
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Smith, J., Jones, A. (2023). Detection of advanced web bots via mouse movement analysis. *Journal of Web Security*, 12(3), 145-167. DOI: 10.1234/jws.2023.12.3.145
- **Source URL or path**: https://doi.org/10.1234/jws.2023.12.3.145
- **Date accessed**: 2026-05-31
- **Category**: academic
- **Evidence basis**: empirical-academic (controlled study)
- **Operational proximity**: capability — a controlled study on a custom test site; demonstrates the detection is feasible in a lab, not that this abuse is observed against real targets (rigour is captured by evidence basis, not here)
- **Tags**: behavioural, methods, advanced-bots, mouse-dynamics

## What it claims

- Mouse trajectory entropy and pause distribution distinguish human users from advanced bot frameworks in a controlled study
- Standard browser automation tools (Selenium, Puppeteer) produce mouse trajectories with significantly lower entropy than human users
- A CNN trained on mouse trajectory images outperforms classical statistical features at distinguishing the two classes
- Detection accuracy drops by 15-20% when bot trajectories are augmented with GAN-generated humanlike movement

## What evidence it provides

Controlled study with 200 human participants and 1000 bot sessions across three automation frameworks. Mouse movements collected via JavaScript probe on a custom test site over six weeks in 2022. Reports classification accuracy, precision, recall, ROC-AUC for several model variants on a held-out test set.

Empirical basis: single-site test environment, recruited human participants paid via Prolific. No production traffic, no real adversarial bots. All metrics are within-study held-out, not external.

## Signals or techniques mentioned

- Mouse trajectory features: entropy, pause distribution, velocity profile, acceleration
- CNN on rasterised trajectory images
- Statistical baselines: SVM with engineered features
- GAN-based trajectory generation as adversarial test
- Standard automation tools: Selenium, Playwright, Puppeteer

## Threat types covered

Advanced web bots in the sense of OWASP OAT-021 (Denial of Inventory) and OAT-005 (Scalping) contexts — bot operators using browser automation to mimic human behaviour for value-extraction purposes. Does not address credential stuffing or scraping specifically.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?** Detection of standard browser automation tools (Selenium, Puppeteer, Playwright) being used against a controlled site, where the automation is not specifically engineered to evade detection.
- **What does it fail to represent?** Production traffic with real adversarial pressure. Stealth automation tools (Puppeteer-stealth, undetected-chromedriver). Cloud browser services. Browser extensions and AI agents. Cross-site behavioural signals. The "humans" are paid participants in a controlled task, not representative of production users.
- **What additional evidence would be needed to go further?** Production data with real bot/human mix, evaluation against modern stealth automation, longitudinal data showing how detection survives adversarial adaptation.

## What it cannot show

- That the reported accuracy generalises to production traffic — the controlled setting biases toward easier detection
- That CNN-on-mouse-trajectory is the right approach in operational settings (cost, latency, evasion resistance not assessed)
- That mouse movement alone is sufficient — the paper does not test fusion with other signals
- That the 15-20% adversarial degradation is the worst case — GAN-based augmentation is one specific adversarial strategy, not the strongest possible

## Project impact

- Provides empirical anchor for the Technical territory page on behavioural detection — concrete claim that mouse-based detection is feasible in controlled settings
- Reinforces the project's framing-distance point: "high accuracy in controlled studies does not transfer cleanly to production"
- Cited on the Behavioural detection methods page as one of several sources documenting the mouse-trajectory approach
- The GAN augmentation result is worth surfacing as evidence that adversarial evaluation matters even when omitted from baseline studies
```

---

## STOP AND ASK CASES

In any of these situations, stop and report back rather than proceeding:

- The source identifier doesn't resolve (broken URL, missing file, paywall)
- The source is much longer than expected and would require its own multi-pass treatment (long books, multi-volume technical references)
- The source's category is unclear — it doesn't fit cleanly into foundations / vendor / academic / threat-surface
- A required extraction field genuinely cannot be filled from the source content
- The source claims something that contradicts another entry already in `working/register-entries/` — flag the contradiction rather than silently resolving
- It is ambiguous whether this is the *same* source as an existing entry (so you cannot tell whether to version it or create a new entry) — ask. (Distinct sources from the same vendor are kept as their own entries; never fold them, and do not skip a distinct source for overlapping with another)
- The source is a target-specific how-to (e.g. "how to scrape `<named site>`") that is purely operational with no territory-level signal — flag for skip per EVIDENCE-REVIEW §3 rather than extracting operational steps
- The source appears to be out of scope per `PROJECT.md` Section 3
- The source contains material from a category explicitly out of scope (named threat actors, criminal economics, broader cyber) — flag rather than extract
- Citations or bibliographic metadata are ambiguous (missing author, missing date, multiple plausible references)
- The source's reading method per `EVIDENCE-REVIEW.md` Section 4 seems to require an approach beyond what this prompt covers
- Any other ambiguity that would require the author's judgement rather than the agent's

When stopping, report:

- What was attempted
- What the issue is
- What additional information or decision is needed from the author

Do not invent answers. Do not skip fields. Do not make scope judgements on the author's behalf.

---

## CONSTRAINTS

| Do | Don't |
|---|---|
| Read all three scope documents before starting | Skip context-reading because the task seems clear |
| Give each distinct source its own atomic entry; version a re-extraction of the same source | Fold two distinct sources into one entry, or skip a distinct source because it overlaps another |
| Record extraction agent, model, date, and access status in the run-metadata block | Leave provenance blank or guess a model version |
| Use the source's own framing in "What it claims" | Insert project opinion into the claims field |
| Attribute every claim to this one source | Blend in field knowledge or other sources' claims |
| Mark vendor/efficacy/prevalence numbers as vendor-measured | Repeat vendor numbers as if independently established |
| Confirm citations resolve before emitting them | Invent a plausible-looking DOI or URL |
| Use `Not stated` / `Cannot determine from source` for absent fields | Infer or pad to make the entry look complete |
| Set `Evidence basis` honestly | Label a marketing claim as if it were a study |
| Be specific in framing distance | Use generic phrases like "limited generalisability" |
| Use existing tags where possible | Invent new tags casually |
| Flag contradictions with prior entries | Silently resolve disagreements between sources |
| Cite by stable identifier where available (DOI, archived URL) | Cite by transient links that may rot |
| Set `Operational proximity` orthogonally to evidence basis | Read a rigorous controlled study as `observed`/`measured`, or infer use from capability |
| Extract that a bypass technique exists and its proximity | Transcribe working evasion code or step-by-step bypass recipes into the entry |
| Report runtime and any access issues | Optimise for appearing successful |

---

## DEFINITION OF DONE

The extraction is complete when:

- An entry file exists at `working/register-entries/<slug>.md` with all fields filled
- The run-metadata block records agent, model (or `not stated`), date, access status, and prompt version
- The slug is descriptive (e.g. `iliou-2022-thesis.md`, `cloudflare-bot-management-2024.md`)
- Every claim in "What it claims" is something the source actually says
- `Evidence basis` is set and matches what the source actually is
- `Operational proximity` is set (`capability` / `claimed` / `observed` / `measured` / `n/a`), justified in one sentence, and not conflated with evidence basis
- Scarce-resource abuse fields are filled when relevant, or explicitly marked not applicable
- "Framing distance" is specific, not generic
- Bibliographic metadata is complete and accurate, and any unverifiable citation is flagged
- The author can read the entry and know whether to read the source themselves

Report back with:

- The file path of the entry
- Runtime
- Any "stop and ask" cases that were not actually blocking but worth flagging
- Anything notable about the source that doesn't fit the template fields but the author should know

---

## OPERATING RULES

- Do not modify `PROJECT.md`, `EVIDENCE-REVIEW.md`, `GOVERNANCE.md`, `REPO.md`
- Do not write to the published register or `working/reading-register.md` — the author merges entries manually
- Do not commit, do not push, do not interact with any remote
- Do not produce site content, synthesis pages, or anything beyond the register entry
- Do not improvise around missing information — ask
- Stay within scope per `PROJECT.md` Section 3 — flag out-of-scope sources rather than extracting
