# Bot and Abuse Prevention — A Demystification Project

*Working scope document. Acts as the project's guiding statement of intent. Edits welcome; treat changes as deliberate scope decisions, not silent drift.*

---

## 1. What this project is

A long-horizon, open, written investigation of the **bot and abuse prevention** category of online security: the commercial and technical territory concerned with detecting and mitigating automated adversarial activity against legitimate web-facing systems.

The output is a public knowledge base — a Quarto-style website with supporting code, datasets where licensing permits, and reproducible analysis. The goal is to make a deliberately opaque category more legible to people trying to understand it.

This is information work, not product work. The project does not aim to evaluate vendors, produce buying recommendations, build a competing product, or advocate for specific policies. It aims to *map the territory honestly* — including the parts that cannot be entered with the tools and data available outside commercial vendors.

The project covers foundational concepts (what an IP is, how a user gets identified online, what kinds of models are used for detection) through to advanced topics (graph-based actor clustering, behavioural sequence modelling, the limits of public-data research) — bringing basic and advanced material into a single place rather than assuming readers already know one or the other.

---

## 2. Why this project exists

The bot and abuse prevention market is large, growing, and substantially opaque. Vendors describe their systems in marketing language that resists technical evaluation. Independent writing on what these systems actually do, how their techniques work, and where their genuine limits sit is sparse — partly because the practitioners who could write it are mostly employed by vendors, and partly because the category is structurally hostile to public technical disclosure (the moat is partly the opacity).

This creates a knowledge gap with practical consequences:

- Buyers cannot evaluate vendor claims on technical grounds
- Engineers cannot know what they could reasonably build versus what genuinely requires commercial telemetry
- Researchers entering the field have to reconstruct the territory from scratch
- Future open-source efforts have no shared reference point to build against
- Newcomers cannot find a clear path from "what is this category" through to "what are the open methodological questions"

The project addresses this gap directly. Not by exposing or critiquing vendors — public marketing claims are treated as evidence about the territory, not as targets — but by producing the kind of clear, honest, technically literate writing that the category currently lacks.

The project also accepts honestly what it cannot do. Commercial systems rely on cross-customer telemetry at scales that cannot be replicated from public data. Some claims are structurally unverifiable. Some techniques are genuine moats. Mapping those limits honestly is part of the work, not an obstacle to it.

---

## 3. Scope

### In scope

Bot and abuse activity against legitimate web flows, broadly defined to include:

- Bot detection and bot management (the canonical category)
- Credential stuffing and account takeover
- Fake account creation
- Web scraping (commercial, competitive, content-extraction, AI training)
- API abuse, including business-logic abuse via APIs
- Click fraud and ad fraud
- Inventory hoarding, scalping, and limited-stock attacks
- Loyalty programme and promotion abuse
- Gift card and stored-value attacks
- Carding and payment-flow abuse where bot-driven

The underlying problem structure across these: automated activity at scale, targeting endpoints and flows intended for human users, to extract value or cause harm.

The project also covers the evolving threat surface introduced by browser-native automation: cloud browser infrastructure, browser extensions, userscripts, and AI browser agents that operate inside otherwise-legitimate browser sessions. These represent a shift in the threat model that older bot detection material doesn't address well.

### Out of scope

Adjacent areas in cyber security that are *not* this project, even though they intersect with it:

- Network intrusion detection, lateral movement, APT analysis
- Malware analysis and reverse engineering
- Vulnerability research and exploit development
- Cryptography and secure protocol design
- Endpoint security, EDR, threat hunting
- Incident response and forensics
- Physical security, social engineering primarily targeting individuals
- Insider threat detection
- Broad information security governance, compliance frameworks
- IoT device botnets (Mirai-class) and DDoS at the network layer

These are excluded not because they are uninteresting but because they are different problems with different methods and different bodies of expertise. The project benefits from clear scope.

### Worked example

A mid-sized company with a booking-style transactional system is used as a recurring concrete example throughout. This includes ticketing, reservations, appointment scheduling, and similar flows where:

- Inventory or capacity is limited
- Transactions have real value
- The web/mobile interface is the primary attack surface
- Bot pressure is a known operational problem
- In-house security capacity is limited

This is illustrative, not constitutive. The analysis aims to be general; the booking example anchors abstract claims in a concrete case.

---

## 4. Audience

Primary audience: technically literate readers who want to understand the territory.

- Security engineers and application security practitioners thinking about whether and how to address bot pressure
- Independent researchers, including academic and industry researchers entering the space
- Engineers and architects evaluating what they could build versus what they would need to buy
- Future builders considering open-source contributions in adjacent areas
- Curious technical readers who want a clear map of an opaque category

Explicitly *not* the primary audience: procurement teams looking for vendor comparisons, executive decision-makers wanting buying advice, marketing teams seeking competitive intelligence.

The project does not write down to procurement audiences and does not aim to produce executive summaries. Where general-audience explanations are needed, they are provided as on-ramps to deeper material, not as the destination.

The project assumes readers may arrive with very different starting points — some knowing what an IP address is and little else, others well-versed in ML but new to abuse detection. Foundational and advanced material coexist; readers self-route to what they need.

---

## 5. The shape of the output

A Quarto-style website with the following high-level structure (subject to evolution as the project develops):

- **Project orientation** — what the project is, why it exists, scope and non-scope, how to read it
- **Foundations** — the basic concepts the rest of the project assumes: what an IP is and isn't, how users get identified across sessions, what kinds of signals defenders work with, what kinds of models get applied, what the basic threat actors are. Written for readers who may need this material in one place.
- **Background and landscape** — the threat model, the actors, the economics of bot activity, the commercial vendor landscape (cited as evidence about the territory, not characterised individually)
- **Technical territory** — what techniques exist, how they work, what their limits are. Organised by technique family (behavioural analysis, fingerprinting, infrastructure signals, graph/entity resolution, sequence modelling, etc.) rather than by vendor
- **Methodology investigations** — concrete experiments on public datasets demonstrating what current best-practice methodology can and cannot do. Each as a self-contained piece with its own write-up
- **What can and cannot be replicated from public data** — honest account of the boundary between what is buildable outside commercial telemetry and what is not
- **Reading list and primary sources** — the literature, vendor publications, conference talks, threat intelligence reports the project draws on
- **Open questions and gaps** — places where the territory is genuinely unmapped or where reasonable people disagree

The site is the deliverable. Code, notebooks, and datasets exist in service of the writing.

---

## 6. What the project is not

Worth stating explicitly to prevent drift:

- Not a vendor comparison or evaluation
- Not a product, even an open-source one, although the writing may enable future products
- Not a policy or advocacy project
- Not a buying guide
- Not a benchmark or leaderboard
- Not a research paper with a single contribution claim, although components may become publishable
- Not a methodology study, although methodology investigations are a component
- Not a critique of the commercial sector, although honest evaluation of public claims is part of the work
- Not a quick-fix resource — readers looking for "what should I deploy this quarter" are explicitly not the audience

---

## 7. Working principles

The project operates under a small set of principles that shape every decision:

**Honest about what cannot be done.** Where commercial systems rely on data scales or telemetry that cannot be replicated from public sources, this is stated plainly rather than worked around with weak substitutes. The boundary is itself useful information.

**Vendor material as evidence, not as subject.** Marketing claims, white papers, patent filings, conference talks, and case studies are sources of signal about what the field does. The project does not characterise individual vendors, evaluate their products, or make claims about their relative merit.

**Long horizon, no quick fixes.** The project optimises for durability of understanding rather than topicality. Current events, specific incidents, and short-term policy questions are addressed only where they illuminate the longer-running structure of the territory.

**Public data, open tooling, reproducible work.** Datasets are public and licensed for the use made of them. Code is open. Analysis is reproducible. Where the work depends on access that cannot be made open, this is flagged.

**Writing is the project.** Code without write-up is incomplete work. Experiments are not finished until they are documented in a form a reader unfamiliar with them can follow.

**Consistent editorial viewpoint.** The project does not require a literary authorial voice. It does require a consistent editorial viewpoint applied across every piece: demystification, methods before actors, public-data limits, careful treatment of vendor claims as evidence rather than as subject. Agent-assisted research and drafting is part of the working method; the author's role is to maintain the editorial viewpoint, not to be the prose stylist. Agent output is raw material; the editorial viewpoint is what makes it the project's.

**Each substantive page earns its place.** Every page passes the test: what does this clarify that a reader would not get by reading the relevant OWASP entry, a single vendor blog, or one academic paper alone? Pages that fail this test stay in working notes. Pages that pass it get published. This is the discipline that prevents the project from becoming a poorer OWASP.

**Honest scope, including admitting when work doesn't pay off.** Methodology experiments that fail to produce orthogonal signal are documented as findings, not hidden. Investigative threads that turn out to be dead ends are written up as dead ends.

---

## 8. Components

The project has several distinct components that develop over time. They are not strict phases — work in different components proceeds in parallel where useful — but they have a default ordering that reflects which work depends on which.

### 8.1 Foundations and evidence review

The substantial first component. Brings together the basic and advanced concepts the project relies on, drawn from open documentation, academic literature, vendor public materials, and threat intelligence sources. The reading is not preparation for the project — it is part of the project. Its written output forms a substantial part of the site.

Concretely, this component covers:

- Foundational concepts: IP addresses and their limits as identifiers, browser fingerprinting basics, how sessions and users get tracked across requests, what HTTP headers reveal, what TLS fingerprints add
- The threat taxonomy: who the actors are, what they want, what tools they use, how the threat surface has evolved
- The methods landscape: what kinds of detection approaches exist, what kinds of models get applied, what their assumptions are
- The vendor landscape: what commercial systems publicly claim to do, what's verifiable from independent sources
- The academic literature: a structured review covering the published work on bot detection, web abuse, and adjacent areas
- The browser-native automation shift: what cloud browser infrastructure (Browserbase and similar), browser extensions, userscripts, and AI browser agents change about the threat model

This component's output is foundational pages on the site, a reading register documenting what was read and what was extracted, and decision notes recording what the reading surfaced.

### 8.2 Methodology investigations on public datasets

A smaller component, illustrating what current best-practice technique can and cannot do without commercial telemetry. The methodology investigations follow a multi-layer architecture studied for what each layer adds rather than for raw performance:

| Layer | Question it answers |
|---|---|
| Supervised classification | Given labelled examples, what features carry signal? |
| Unsupervised individual anomaly | What's unusual about a single session against the normal population? |
| Behavioural / sequence | What can be learned from the pattern of actions a session takes? |
| Graph / group | What can be learned by clustering sessions by shared weak identifiers, and scoring groups as actors? |

Each layer is built simply rather than tuned to optimum. The interest is in how they compose, what each adds, where they disagree, and what conclusions are robust to methodology choices. Honest evaluation under noisy labels and grouped data dependence is part of the contribution.

Dataset selection for these investigations is its own piece of work — different public datasets support different layers, and no single public dataset adequately represents the operational problem. The methodology section includes a written assessment of dataset choice and the framing distance between each public dataset and real-world bot prevention work.

### 8.3 Controlled experiments (possible, pending the evidence review)

An explicit open possibility, not a commitment. The evidence review may surface that running controlled experiments — generating original data through automation tools (Browserbase, local Playwright/Selenium with varying stealth levels, browser extensions, AI agents) against the project's own controlled infrastructure — is the right way to demonstrate specific points the public datasets cannot illustrate.

What this would entail:

- A controlled test site (booking-style, matching the worked example)
- Full server-side logging including TLS fingerprints, HTTP headers, and behavioural data
- Automation runs across the taxonomy: HTTP scripts, local browser drivers, stealth browser tools, cloud browser infrastructure, browser extensions, AI agents
- Matched-pair data: what each automation approach looks like from the server side
- Analysis comparing the signals each approach leaves with what the literature claims defenders can detect

This is original research, not demystification per se. If undertaken, it would sit alongside the demystification work as evidence for specific claims rather than becoming the project's centre. The decision to proceed is deferred until the evidence review reveals whether it adds enough to the project to justify the cost (roughly 6-8 weeks for a minimum viable version, plus ongoing analysis time).

If the controlled experiments are run, their results are documented as a component of the site; if they are not run, the possibility is acknowledged in the limitations section.

---

## 9. What success looks like

Success is defined by what the project produces, not by whether anyone reads it. Specifically:

- A coherent public artefact that explains the territory clearly
- Honest acknowledgment of what can and cannot be done with public data and open tools
- Foundational material that brings basic and advanced concepts into one accessible place
- Methodology investigations that demonstrate current best-practice technique rigorously
- If pursued, controlled experiments that demonstrate specific claims the public data cannot
- Documentation of the reading and reasoning that informed the analysis
- A foundation that others could extend, cite, or build on if they chose to

External traction (readership, citations, adoption by builders of open-source alternatives) is welcome but not required for success. The project does not depend on reception to be worth doing.

---

## 10. Default ordering of work

The components have a default ordering that reflects dependencies between them. The ordering is not a strict commitment — work shifts as it makes sense — but it represents the current best understanding of what should happen first.

| Order | Component | Why this position |
|---|---|---|
| 1 | Project setup and orientation | Repo, site skeleton, scope confirmed |
| 2 | Foundations and evidence review (Component 8.1) | The substantive first body of work; informs everything else |
| 3 | Dataset assessment, written up | Builds on the foundations; informs methodology choices |
| 4 | Decision on controlled experiments (Component 8.3) | The evidence review reveals whether this is worth doing |
| 5 | Methodology investigations (Component 8.2) and/or controlled experiments (Component 8.3) | Concrete work supporting the foundational writing |
| 6 | Synthesis, cross-cutting findings, what's mapped and what isn't | Brings the components together |

This ordering can be revisited at any point. The discipline is that re-ordering is recorded as a decision, not made silently.

**Hard stopping conditions.** A re-scope conversation is triggered (not necessarily abandonment) when any of these occur:

- The evidence review reveals the territory is already substantially mapped by existing public writing
- A component passes its planned duration by more than 50% without producing a publishable artefact
- The project becomes a low-grade attention drain rather than active interest
- The work duplicates existing efforts rather than adding to them

---

## 11. Risks and failure modes

Honest assessment of how the project could fail:

**Scope drift.** Bot and abuse prevention is adjacent to several larger and louder categories (general cyber security, fraud prevention, identity management). The risk of being pulled into adjacent topics is real. Mitigation: the in-scope and out-of-scope sections of this document are a discipline, not a description. Changes are explicit edits.

**Demystification framing collapses into vendor critique.** The line between "explaining what vendors do" and "characterising specific vendors" is thin. Crossing it changes the project into something else with different legal and reputational risks. Mitigation: vendor material is cited as evidence about the field; individual vendors are not characterised.

**Reading load underestimated.** Background reading in an unfamiliar category takes longer than data work in a familiar one. Months of vendor publications, threat reports, conference talks, and academic literature are real work, not preamble. Mitigation: Component 8.1 has its own budget; reading is part of the work, not before the work.

**Agent-assisted content lacks voice.** Using agents heavily for first-pass research and drafting risks producing competent-but-generic content that lacks the project's perspective. Mitigation: agent output is raw material, not finished writing. Substantial editing, restructuring, and addition of authorial framing is part of every piece. The "writing is the project" principle includes "writing in the project's voice."

**Controlled experiments expand beyond scope.** If pursued, controlled experiments could grow into a full research project that subsumes the demystification work. Mitigation: experiments are scoped to demonstrate specific claims, not to be definitive contributions in themselves. The decision to proceed and the scope are recorded explicitly before any experimental work starts.

**Methodology investigations underdeliver.** Public datasets have framing distance from real bot prevention. Multi-layer architectures may not produce the clean comparative findings that motivate the structure. Mitigation: documented as findings rather than hidden as failures; the broader project does not depend on the methodology section alone.

**Writing lags experiments.** Common failure mode for technical projects. Mitigation: per-experiment writeup is part of the experiment's definition of done. No write-up means experiment not complete.

**The territory turns out to be already mapped.** Possible. The sanity check during early evidence review exists specifically to surface this before substantial work is invested. If true, the project either repositions around the gaps that remain, or stops.

**Outsider position dismissed.** Writing about a category as a technically literate outsider has a real risk of being dismissed by insiders. Mitigation: the outsider position is claimed explicitly rather than disguised; honest about what is and is not known from the position; engagement with insiders welcomed but not required for the work to be valuable.

---

## 12. Working method

A few practical choices that shape day-to-day operation:

**Repo structure.** Code, content, and site live together. Quarto handles the site build. Standard hygiene: pre-commit hooks, CI, branch-based PRs, no direct commits to main.

**Tooling default.** Python-first for analysis. Standard data stack (pandas, polars/DuckDB where scale demands, scikit-learn, gradient boosting, PyTorch Geometric or similar for graph work). Writing in Quarto markdown.

**Agent-assisted research.** Mechanical research, structured extraction, and first-pass drafts are delegated to coding agents (Codex, Claude Code) where this saves time. The brief is always scoped, the output is always reviewed, and the final content is always re-worked into the project's voice. Agent output is never published unedited.

**Per-piece definition of done.** Each substantive piece on the site is "done" when: it has a clear thesis, the supporting work is reproducible, the writing is read-through-able by the intended audience, includes explicit limitations and open questions, and reads as the project's own voice rather than as synthesised summary.

**Open by default.** Code, written analysis, and reproducibility material are public unless there is a specific reason to keep them private (e.g. dataset licensing that prohibits redistribution, in which case the analysis is published with pointers to the data rather than the data itself).

**Collaboration welcomed.** The project is structured to allow contributions from others — each subtopic can be a self-contained piece, and external contributors could plausibly take on specific threads. Contribution mechanics (PR process, contribution guidelines) are set up from the start, not retrofitted.

---

## 13. Open decisions

Items deferred to future scoping conversations:

- Specific dataset commitments for the methodology section (assessment in progress, write-up pending)
- Whether to run controlled experiments and at what scale (deferred to after evidence review)
- The browser-native automation taxonomy (built during writing, not adopted from external sources)
- Tooling specifics (which graph library, which workflow orchestration if any)
- Whether and how to engage with insider practitioners for review or feedback
- Public release strategy beyond "the site exists" — outreach is a separate decision
