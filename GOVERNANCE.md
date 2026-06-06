# Governance and AI Usage

*Working document. Defines how the project is produced, particularly the role of AI agents and the author's editorial discipline. Companion to PROJECT.md (scope) and EVIDENCE-REVIEW.md (evidence review scope). Edits welcome; treat changes as deliberate decisions.*

---

## 1. Purpose

This document records how openbotrisk is produced. The project uses AI agents extensively for research, extraction, and drafting; the author is the editor, reviewer, and accountable decision-maker for what is published. This document defines what that means in practice, so the working method is transparent to readers and reviewers, and so the discipline holds in practice rather than only in principle.

The project is information work, not journalism and not original research. The author's responsibility is for what gets published — accuracy, scope, honest acknowledgment of limits — not for personally writing every word.

---

## 2. The author's role

The project uses AI agents extensively for extraction, drafting, and coding. The author acts as editor, reviewer, and accountable decision-maker for what is published.

In practice this means:

- The author defines scope (PROJECT.md, EVIDENCE-REVIEW.md, this document)
- The author writes the prompts that agents work from, or reviews and edits prompts before they run
- The author reviews agent output per the discipline defined below
- The author verifies load-bearing claims against their cited sources
- The author makes the call on what gets published
- The author owns errors — they are not blamed on agents

Agents reduce the labour cost of reading, extraction, drafting, and implementation. The author remains accountable for published claims, verifies load-bearing claims, and makes all scope and publication decisions.

The trade is explicit: depth of personal engagement is traded for breadth of coverage and time-to-publish. This trade is defensible for this project given its information-work framing, but only if the editorial discipline below is real.

---

## 3. Where agents are used

AI agents (coding agents such as Claude Code and Codex; chat-based assistants such as Claude and ChatGPT for advice and second-opinion work) are used across the project. Specifically:

| Task | Agent role | Author role |
|---|---|---|
| Scope documents | Drafting on request; second-opinion review | Original framing, final decisions |
| Source extraction | Primary | Review, verification of load-bearing claims |
| First-pass synthesis across sources | Primary | Review, restructuring |
| Code for data analysis and methodology investigations | Primary | Review, decisions about what to investigate |
| Site content first drafts | Primary | Editorial review per checklist below |
| Editorial review itself | Not used | Author only |
| Scope decisions and project direction | Not used | Author only |
| The discipline of this document | Not used | Author only |

The principle: agents do extraction, synthesis, drafting, and code. Authors decide scope, verify load-bearing claims, review output, and own publication.

### Content types and their author engagement

Different content types warrant different levels of author engagement:

| Content type | Author engagement | Examples |
|---|---|---|
| Reference / foundations | Light editorial review | Basic concept pages, "what is an IP address" |
| Extracted source content | Editorial review against checklist | Reading register entries, vendor claim catalogues |
| Synthesis pages | Author-specified outline, agent drafts, editorial review | Most site content connecting multiple sources |
| Argument pages | Author-drafted or author-outlined heavily, agent assists | The distinctive framings — "why X" pieces that carry the project's analytical position |

The argument pages are where the project earns its position. They get more author attention than synthesis pages. Examples of argument pages this project will need:

- Why IP addresses are weak identifiers
- Why browser fingerprints are useful but unstable
- Why public datasets underrepresent commercial telemetry
- Why browser-native automation changes the human/bot boundary
- Why fraud datasets help but do not equal bot-management data
- Where graph and entity methods fit in abuse prevention

These pages carry the project's distinctive contribution. They are author-led even when agents help with drafting.

---

## 4. Editorial review per piece

Every piece published to the site gets reviewed by the author before publication. The review is not a rewrite. It is a defined check.

### Editorial checklist

For each piece, the author checks:

**Load-bearing claims verified.** Factual claims that bear on the piece's argument are personally verified by the author against their cited sources. Not every claim is independently re-researched, but claims that load the argument get verified.

**What this clarifies beyond available sources.** Each substantive page passes the test: what does this clarify that a reader would not get by reading the relevant OWASP entry, a single vendor blog, or one academic paper alone? Pages that fail this test stay in working notes; pages that pass it get published.

**Scope discipline.** The piece stays within the project's stated scope (PROJECT.md Section 3). If it strays into out-of-scope territory (actors, economics, broader cyber), the straying is removed or the scope document is updated explicitly.

**Honest acknowledgment of limits.** Where the piece makes claims that public data or open analysis cannot fully support, this is acknowledged. Where commercial systems do things that cannot be replicated, this is stated rather than worked around with weak substitutes.

**No generic-summary patterns.** Agent output sometimes collapses into "balanced overview" prose that lists positions without taking one. The project has framings (demystification, methods-not-actors, public-data limits) that should be visible in the writing. Pieces that have been smoothed into generic summary are pushed back.

**Sources cited where required.** Every factual claim that could be checked has a source. Every quoted vendor claim links to the public statement. General field knowledge does not need citation; specific claims do.

**Consistent editorial viewpoint.** The project does not require a literary authorial voice. It does require a consistent editorial viewpoint: demystification, methods before actors, public-data limits, careful treatment of vendor claims. Pieces that drift from this viewpoint are pushed back.

**Dual-use containment.** Where a piece draws on bypass, anti-detect, or evasion sources (or operational detail inside legal/victim records), the author confirms it records *that* a technique exists and its operational proximity, not a working procedure. Specifically: no step-by-step bypass or working evasion code is reproduced; the piece does not synthesise details from several sources into a more complete how-to than any single source provides (the **aggregation hazard** — the specific risk for a project that reads widely across attacker-side material); and where a source cannot be used without an operational recipe, the piece summarises the claim and links out. A piece that fails this stays in working notes. This is the publication-side counterpart to the extraction-time no-recipe rule (`source-extraction-prompt`) and the scope rule in `EVIDENCE-REVIEW.md` §3.

### Editorial review note

Every published page has an editorial review note recorded in working notes (PR description or `working/review-notes/`). The template:

```
## Editorial review note

- Load-bearing claims checked:
- Sources rejected or treated cautiously:
- Main limitation:
- What this page adds beyond source summary:
- Dual-use containment (no reproduced recipe; aggregation hazard checked):
```

The "What this page adds" answer also appears as a single visible line on the page itself — at the top or bottom, depending on flow — so readers can see the project's claim about why the page exists. The other fields stay in working notes.

If the author cannot answer "what this page adds beyond source summary" with something specific, the page does not publish. This is the operational mechanism that protects the project from being a poorer OWASP.

### What the review is not

The review does *not* require:

- Re-researching every source from scratch
- Rewriting for prose quality unless the prose is misleading
- Verifying every citation by reading the original (load-bearing only)
- Restructuring unless the structure is genuinely wrong
- Adding original analysis to agent-drafted content if the content is already in line with project framings

The review is a check, not a re-write. The agent does the writing; the author does the editorial decision and verifies what matters.

### Rubber-stamping flag

If the author reviews five pieces in a row without finding anything substantive to push back on, something is wrong. Either the agent output is suspiciously perfect (unlikely) or the review has become rubber-stamping. The author commits to noticing this and to actively looking for what's wrong with each piece, not approving by default.

If a stretch of pieces really are clean, this is also worth noting — it may indicate that prompts have stabilised and the agent has converged on a useful pattern. But "rubber stamp" remains the default suspicion.

---

## 5. Defining the operational principles

The project's working principles (PROJECT.md Section 7) are operationalised here.

### Load-bearing vs peripheral claims

A claim is **load-bearing** when:

- It supports an argument the page is making
- It would change a reader's understanding if false
- It is specific (named vendors, named techniques, specific numbers)
- It contradicts or extends what other sources say

A claim is **peripheral** when:

- It is general field knowledge any technically literate reader would recognise
- It is supporting context, not part of the argument
- It is broadly consistent with multiple sources without being specific

The author personally verifies load-bearing claims against cited sources. Peripheral claims get review-only.

### "Thorough"

A claim does not appear on the site unless at least one source supports it and that source has been read. Agent-assisted extraction counts as reading provided the extraction was reviewed by the author.

For load-bearing claims, the author personally checks the cited source says what the claim says. For peripheral claims, agent extraction reviewed by the author is sufficient.

### "Reference anything important"

Every factual claim that could be checked is sourced. Specifically:

- Vendor claims: linked to the public statement (blog post, white paper, documentation) where the vendor made the claim
- Academic findings: cited to the paper, with author and year; preferably with DOI or stable URL
- Statistics and numbers: sourced to the publication that produced them
- Technical mechanisms: sourced to documentation, RFC, or canonical reference where one exists

What does not need citation:

- General technical knowledge that a technically literate reader would recognise (HTTP has headers, JavaScript runs in browsers)
- The project's own analysis and synthesis (clearly framed as such)
- Common-knowledge facts about the internet's structure

### "Double-check things"

Three classes of claim get explicit author verification beyond agent extraction:

- Claims about what specific vendors say: verified against the original source
- Claims about academic findings that bear on the project's argument: verified against the original paper, not against summaries
- Technical claims that could mislead if wrong: sanity-checked against at least one independent source

For other claims, agent extraction reviewed by the author is sufficient.

---

## 6. Transparency commitments

The project commits to making its working method visible.

**Reading register is public.** Every source read has a register entry, including sources read and rejected. Lives at `working/reading-register.md`, also published on the site.

**Decision log is public.** Substantive decisions about scope, methodology, and direction are logged in `working/decisions.md` with rationale.

**Agent prompts are committed.** The prompts used to direct agents on research and drafting work are committed to the repository, so readers can see what instructions produced what output.

**A "How this is produced" page exists.** The site has a clearly-labelled page explaining the working method, the role of AI agents, the author's editorial role, and the limits of the approach. This is not buried in fine print; it's prominent in the site's orientation material.

**Per-page "what this adds" statements are visible.** Each substantive page carries a visible single-line statement of what it clarifies beyond available sources. The full editorial review note stays in working notes.

**Errata are visible.** When errors are found post-publication, they are corrected with visible record (date of correction, what changed, why). Not silently rewritten. The errata page lives at a stable URL.

**Honest framing of the trade.** The site does not pretend the work was personally researched and written when it wasn't. The "How this is produced" page makes the trade explicit: agent-assisted production enables a project that would not happen with traditional methods, and the author is responsible for what gets published.

---

## 7. What can go wrong with this method

Honest assessment of failure modes specific to the agent-assisted approach.

**Agent hallucination.** Agents can produce plausible-sounding content that is factually wrong. Mitigation: load-bearing claims get author verification against cited sources. Agent output is treated as a first draft to be checked, not as authoritative.

**Citation hallucination.** Agents can produce plausible-sounding citations that don't exist. Mitigation: any citation that appears for the first time in agent output gets the author checking the source actually exists and says what the agent claims it says. This is a specific check, not a general aspiration.

**Generic summary collapse.** Agent output gravitates toward "balanced overview" prose that lists positions without taking one, and that fails to apply the project's specific framings. Mitigation: editorial checklist includes a check for this pattern; the "what this page adds" test forces a substantive answer per page; pushed-back pieces get re-prompted with specific framing instructions.

**Voice drift.** With high agent automation, the site's prose may end up smooth and competent but generic. Mitigation: this is partly accepted as the cost of the working method. The project commits to consistent editorial viewpoint rather than distinctive prose voice.

**Rubber-stamping.** The author's review can collapse into nominal approval over time. Mitigation: explicit flag (five pieces with zero substantive changes = something wrong), explicit checklist that has to be applied rather than gestured at, "what this page adds" forced answer per page.

**Scope drift through accumulation.** Each individual agent output may look in-scope, but the accumulation of small drifts can shift the project. Mitigation: scope is owned by author, codified in PROJECT.md, checked at each editorial review, revisited periodically as a deliberate exercise.

**Source quality drift.** Agents may cite weak sources (low-quality blogs, marketing material, content farms) where stronger sources exist. Mitigation: editorial check on source quality is part of the review; prompts include source-quality guidance.

**Over-claim from synthesis.** Agent synthesis across multiple sources can produce confident-sounding claims that no single source actually supports. Mitigation: synthesised claims are checked against the underlying sources; "the literature suggests X" gets pushed back unless X is genuinely traceable.

**Aggregation into a how-to (dual-use).** A demystification project that reads widely across scraper-side, bypass, and evasion material can, by synthesising scattered operational details, end up a more complete bypass guide than any single source it cites — even when each source individually is within scope. This is distinct from over-claim: the synthesis may be *accurate* and still be the problem. Mitigation: the §4 dual-use containment check; record technique existence and operational proximity, not procedure; never aggregate operational steps across sources; link out rather than reproduce. The `operational proximity` axis in the register makes the attacker-side sources easy to find and audit for this.

---

## 8. What's deliberately not in this document

A few things this document does not commit to, with honest reasons:

- **Personal verification of every source.** This would defeat the purpose of agent-assisted production. The trade is explicit: load-bearing claims get verified, peripheral claims do not.
- **Original analysis on every page.** Many pages are synthesis of others' work. The project's contribution is in the synthesis, the framings, the argument pages, and the editorial selection — not in producing novel research everywhere.
- **Distinctive authorial prose voice.** The author is editorially responsible, not necessarily authorially distinctive in prose style. Consistent editorial viewpoint, yes; distinctive voice signature, no.
- **Guaranteed accuracy.** The project does not promise zero errors. It promises that errors are corrected when found, visibly, with record.
- **Real-time updates as the field changes.** The project is a long-horizon information artefact. Snapshots and dated material are acceptable; chasing currency is not.

---

## 9. Review and revision of this document

This document is itself subject to review. As the working method matures, the discipline may need updating. The discipline for updating:

- Changes are explicit edits committed to the repository, with commit messages explaining what changed and why
- Substantive changes (new categories of agent work, weakening of review discipline, etc.) are flagged in the decision log
- The "How this is produced" page on the site stays in sync with this document; if they diverge, the public page wins for what readers see, but this document is fixed to match

If the discipline isn't working in practice — if errors are leaking through, if the review is becoming rubber-stamping, if voice has drifted to something embarrassing — the response is to tighten the discipline, not to lower the standards. Lowering standards while continuing to publish would be the project's failure mode.