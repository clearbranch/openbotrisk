# Agent prompt — adding a reviewed entry to the evidence register

You project a **reviewed** per-source extraction entry into the evidence register (`literature-evidence-register.qmd`). You do not extract sources, judge scope, or write site content. By the time an entry reaches you, the author has already decided it belongs in the register — your job is faithful projection plus cross-index maintenance, append-only.

This is the middle link of the pipeline: `source-extraction-prompt` produces a per-source entry → **this prompt** projects it into the register → (later) a page-scoping step queries the register to decide which entries a site page needs.

The repo has `PROJECT.md`, `EVIDENCE-REVIEW.md`, and `GOVERNANCE.md` committed. **Read all three first** — they define scope, categories, and the append-only editorial discipline, and they are authoritative.

---

## INPUTS

The author provides:

- **Entry file path**: a reviewed entry under `working/register-entries/` — `<slug>.md`, or a versioned `<slug>.v2.md` / reconciled `<slug>.combined.md`
- **Register path**: the `.qmd` register to update
- **Optional — existing register id**: if the author already knows this entry is a re-extraction of a source already in the register, the `SRC-NNN` it attaches to

If the entry file or register path is missing, stop and ask.

---

## MODEL THIS PROMPT ENFORCES

- **One register id per distinct source.** Each distinct source is its own atomic row. Distinct sources from the same vendor are separate rows — they are **never folded together**.
- **Re-extraction ≠ new row.** Re-extracting a source (new prompt version, or a different agent) adds a *versioned file* under the **same** `SRC-NNN`; it does not create a second row, and it does not overwrite or delete the old file.
- **No pruning here.** Every reviewed entry the author hands you gets represented. Do **not** skip, drop, or merge on relevance or redundancy grounds — selection between overlapping sources is the page-writing step's job, not the register's.
- **Append-only.** Never silently overwrite an existing judgement; record changes in the update log.

---

## PROCESS

1. Read `PROJECT.md`, `EVIDENCE-REVIEW.md`, `GOVERNANCE.md`
2. Read the register: existing rows and ids, the four category sub-tables, the framing-distance ledger, the signals-and-techniques cross-index, the scarce-resource abuse index, the controlled-vocabulary appendix, and the update log
3. Read the entry file. Pull: bibliographic, `category`, `evidence basis`, `operational proximity`, `signals / techniques`, `threat types`, scarce-resource abuse fields if present, regulatory-constraint fields if present, the three-part `framing distance`, `what it cannot show`, `project impact`, and the **run-metadata block** (extraction agent, model, prompt version, date, source access)
4. **New source vs re-extraction.** Decide which:
   - *Same source* (same document / URL) as an existing row → **re-extraction.** Use that row's existing `SRC-NNN`. Add the new file to the row's `entry file` cell, update the `reconciliation` tag, do **not** create a new row, do **not** remove the older file or its provenance.
   - *Different source* (including another blog post or doc page from the same vendor) → **new row.** Assign the next `SRC-NNN` in the relevant category sub-table.
   - If you cannot tell which, **stop and ask** — do not guess.
5. **Inventory row.** Build or update the row using the register's controlled vocabulary (appendix). `provenance` = agent / model / prompt-version from the run-metadata block; if absent, `not recorded` (do not guess a model). Where a field is genuinely absent from the entry, use the register's honest tokens (`tbd`, `see entry`, `Not threat-specific`) rather than inventing. Lift `operational proximity` (the `capability` / `claimed` / `observed` / `measured` / `n/a` column, positioned after `evidence basis`) directly from the entry — **do not derive it from `evidence basis`**, the two are orthogonal. If the entry predates schema v3 and lacks the field, set `tbd — backfill from entry` rather than guessing
6. **Framing-distance ledger.** Append the source's ledger row (the three parts + `what it cannot show`). On a re-extraction that sharpens these, do not silently overwrite — note the change in the update log and preserve the prior content
7. **Signals-and-techniques cross-index.** Add the `SRC-NNN` to each technique-family row the entry's signals belong to. Introduce a new family row only if the entry genuinely covers a family not already listed — sparingly
8. **Scarce-resource abuse projection.** If the entry's scarce-resource section is `Not applicable — source does not concern scarce-resource abuse`, leave the scarce-resource abuse index untouched and do not force these fields onto the inventory row. If the entry concerns scarce-resource abuse, add or update one row in the scarce-resource abuse index:
   - `id` = the source's `SRC-NNN`
   - `tags` = `scarce-resource-abuse` plus every specific scarce-resource tag supported by the entry or source framing (`slot-sniping`, `limited-inventory`, `appointment-abuse`, `reservation-abuse`, `ticketing-abuse`, `inventory-hoarding`, `denial-of-inventory`, `scalping`, `queue-abuse`, `booking-flow-abuse`, `availability-polling`, `cancellation-monitoring`, `fast-booking`, `auto-booking`, `slot-resale`, `ticket-resale`, `reservation-resale`, `booking-transfer`, `account-preparation`)
   - `scarce_resource_targeted`, `abuse_phase`, `website_facing_action`, `evidence_of_use`, and `abuse_outcome` copied from the entry using the register appendix vocabulary
   Use `not stated in entry` for a scarce-resource field that is clearly relevant but absent; do not invent values. Keep `evidence_of_use` separate from `operational proximity`: `evidence_of_use` is the scarce-resource-specific use classification, while `operational proximity` remains the broader corpus-level capability-to-use axis.
9. **Regulatory-constraint projection.** If the entry's regulatory-constraint section is `Not applicable — source is not a regulatory-constraint source`, leave regulatory fields untouched and do not force them onto the inventory row. If the entry is tagged `regulatory-constraint`, verify:
   - `operational proximity` is `n/a`
   - `jurisdiction`, `currency`, and `constrains_technique` are present
   - `currency` includes an as-of date and the caveat `subject to change; not verified current`, or the honest token `as-of unknown — verify before use`
   - the entry does not state legal advice or compliance instructions
   Add the source to the relevant signals-and-techniques cross-index row named by `constrains_technique`. If the register later has a dedicated regulatory-constraint index, project the fields there; until then, preserve the fields in the row's project-impact / notes wording and the update-log line.
10. **Reconciliation tag** in the `entry file` cell:
   - first/only extraction → `[single]`
   - second+ extraction not yet reconciled → `[multiple — unreconciled]`; list all files; `canonical for citation` = latest version
   - a `.combined` file → `[combined]`; `canonical for citation` = the combined file; keep the source extractions listed
11. **Update log.** Append one dated line: which id was added, or which existing id gained a version; the source; agent / model / prompt version; and any field that changed on a re-extraction, including scarce-resource or regulatory-constraint index changes where applicable
12. Report back (see Definition of done). Do **not** commit or push — the author reviews the register diff first

---

## WORKED EXAMPLES

**New distinct source from a vendor already in the register.** Entry is a ScrapFly blog post on bypassing Imperva. ScrapFly is already `SRC-024` (general anti-scraping bypass). This post is a *different source* with distinct signal (Imperva's detection surface), so it gets its **own** new `SRC-NNN` in the threat-surface sub-table — it is **not** folded into SRC-024 and **not** skipped for overlapping with it. Add it to the framing-distance ledger and to the cross-index rows for "TLS / network fingerprints" and "fingerprint-inconsistency / evasion detection" as applicable. `reconciliation` = `[single]`.

**Re-extraction of an existing source.** Entry is `iliou-2022-thesis-advanced-web-bots.v2.md`, a v2 re-run of `SRC-011`. Do not create a new row. Add the `.v2.md` file to SRC-011's `entry file` cell, set `[multiple — unreconciled]`, update `provenance` to list both extractions, and if the v2 run sharpened the framing-distance cells, note that in the update log rather than overwriting. `canonical for citation` = the v2 file (latest). Later, if the author reconciles into `iliou-2022-thesis-advanced-web-bots.combined.md`, set `[combined]` and make the combined file canonical.

---

## STOP AND ASK CASES

- The entry file or register path doesn't resolve
- You cannot tell whether the entry is the *same* source as an existing row or a *different* one (versioning vs new row turns on this)
- The entry's `category` disagrees with where a same-source row already sits
- A re-extraction's `evidence basis` or `framing distance` materially contradicts the existing row for that source — flag the discrepancy as a reconciliation signal; do not silently overwrite
- The entry is missing fields the register needs (`evidence basis`, run-metadata) — flag; fill with honest tokens, do not invent
- The entry clearly concerns scarce-resource abuse but lacks the scarce-resource field block — flag; do not collapse it into generic scraping
- The entry looks out of scope or like it should have been rejected — the register is downstream of the scope decision, so surface it for the author rather than making the call here

When stopping, report what was attempted, the issue, and what decision is needed.

---

## CONSTRAINTS

| Do | Don't |
|---|---|
| One `SRC-NNN` per distinct source | Create a new row for a re-extraction of an existing source |
| Keep distinct sources from the same vendor as separate rows | Fold or merge distinct sources into one row |
| Represent every reviewed entry handed to you | Prune, skip, or drop on relevance / redundancy grounds — that is the page step |
| Add a re-extraction as a versioned file under the existing id | Overwrite or delete an older extraction file or its provenance |
| Pull provenance from the run-metadata block | Guess an agent or model version; use `not recorded` if absent |
| Use the appendix controlled vocabulary | Invent new `evidence basis` / `review state` / `reconciliation` values |
| Copy `operational proximity` from the entry, orthogonal to evidence basis | Derive proximity from evidence basis, or guess it for a pre-v3 entry (use `tbd`) |
| Carry scarce-resource fields into the scarce-resource abuse index only when relevant | Force scarce-resource fields onto unrelated sources, or treat scarce-resource abuse as a fifth category |
| Keep `evidence_of_use` distinct from `operational proximity` | Use `evidence_of_use` as a replacement for the broader proximity axis |
| Carry regulatory-constraint fields only when the entry is tagged `regulatory-constraint` | Treat legal/regulatory material as legal advice, compliance guidance, or a fifth evidence category |
| Set regulatory-constraint entries to `operational proximity: n/a` | Treat regulatory sources as evidence of abuse, prevalence, or control effectiveness |
| Append-only; log every change | Silently rewrite an existing judgement |
| Use honest tokens (`tbd`, `see entry`) for absent fields | Infer or pad a field the entry doesn't support |

---

## DEFINITION OF DONE

- The source is represented: a new row in the correct category sub-table, **or** a versioned file added under the correct existing `SRC-NNN`
- Inventory row uses controlled-vocabulary values, including `operational proximity` (lifted from the entry, not derived); `provenance` set (or `not recorded`)
- Framing-distance ledger and signals-and-techniques cross-index updated
- Scarce-resource abuse index updated when applicable, or left untouched when the entry marks the fields not applicable
- Regulatory-constraint fields projected when applicable, including jurisdiction, currency, constrained technique, `operational proximity: n/a`, and not-legal-advice caveat
- `reconciliation` tag set and `canonical for citation` determined
- One dated line appended to the update log
- No scope docs, entry files, or older extraction files modified; nothing committed or pushed

Report back with: the id added or updated, new-row vs versioned-file, `reconciliation` state, the cross-index rows touched, the update-log line, and any flags.

---

## OPERATING RULES

- Do not modify `PROJECT.md`, `EVIDENCE-REVIEW.md`, `GOVERNANCE.md`, `REPO.md`, or any `working/register-entries/` file
- Do not extract sources or write site / synthesis content — this prompt only projects an existing reviewed entry into the register
- Do not make scope or rejection judgements — surface them to the author
- Do not commit, push, or interact with any remote — the author reviews the register diff
- Do not improvise around missing information — ask
