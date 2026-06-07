# Background landscape pages — fixed pack

This pack removes YAML `description:` fields and uses body `::: {.lead}` blocks instead.

Each `.qmd` page includes:

- no `description:` field in YAML
- `format.html.css: background.css`
- subtle source labels using `[Source]{.source-ref}`
- a `## Sources used on this page` section
- a `::: {.next-page}` navigation block, except the final page points back to the index

Suggested order:

1. index.qmd
2. threat-model.qmd
3. booking-style-system.qmd
4. adversary-model.qmd
5. economics-of-automation.qmd
6. commercial-defender-landscape.qmd
7. ai-agent-shift.qmd
