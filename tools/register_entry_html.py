#!/usr/bin/env python3
"""Build ignored HTML review pages for evidence register entries.

The generated files are local review artifacts. They are written under
``working/register-entry-html/``, which is ignored by git.
"""

from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTER = ROOT / "site/reading/evidence-register.qmd"
DEFAULT_ENTRIES = ROOT / "working/register-entries"
DEFAULT_OUTPUT = ROOT / "working/register-entry-html"


@dataclass(frozen=True)
class RegisterRow:
    register_id: str
    category: str
    source: str
    org_authors: str
    year: str
    evidence_basis: str
    operational_proximity: str
    signals_techniques: str
    threat_types: str
    provenance: str
    review_state: str
    project_impact: str
    entry_cell: str
    entry_file: Path | None


def split_markdown_row(line: str) -> list[str]:
    """Split a simple pipe-table row.

    The register tables do not use escaped structural pipes, so this keeps the
    parser intentionally small and predictable.
    """

    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return [strip_inline_markup(cell) for cell in cells]


def strip_inline_markup(value: str) -> str:
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("**", "").replace("*", "")
    return value.strip()


def extract_md_filenames(value: str) -> list[str]:
    return re.findall(r"`([^`]+\.md)`", value)


def without_download_suffix(name: str) -> str:
    return re.sub(r"\(\d+\)(?=\.md$)", "", name)


def resolve_entry_file(entry_cell: str, entries_dir: Path) -> Path | None:
    filenames = extract_md_filenames(entry_cell)
    for filename in filenames:
        candidates = [
            entries_dir / filename,
            entries_dir / without_download_suffix(filename),
        ]
        for candidate in candidates:
            if candidate.exists():
                return candidate
    return None


def parse_inventory(register_path: Path, entries_dir: Path) -> list[RegisterRow]:
    text = register_path.read_text(encoding="utf-8")
    rows: list[RegisterRow] = []
    in_inventory = False
    category = ""

    for line in text.splitlines():
        if line.startswith("## Extraction inventory"):
            in_inventory = True
            continue
        if in_inventory and line.startswith("## Framing-distance ledger"):
            break
        if not in_inventory:
            continue

        heading = re.match(r"^###\s+(.+)$", line)
        if heading:
            category = heading.group(1).strip()
            continue

        if not line.startswith("| SRC-"):
            continue

        cells = split_markdown_row(line)
        if len(cells) != 12:
            continue
        entry_cell = line.strip().strip("|").split("|")[-1].strip()
        rows.append(
            RegisterRow(
                register_id=cells[0],
                category=category,
                source=cells[1],
                org_authors=cells[2],
                year=cells[3],
                evidence_basis=cells[4],
                operational_proximity=cells[5],
                signals_techniques=cells[6],
                threat_types=cells[7],
                provenance=cells[8],
                review_state=cells[9],
                project_impact=cells[10],
                entry_cell=strip_inline_markup(entry_cell),
                entry_file=resolve_entry_file(entry_cell, entries_dir),
            )
        )

    return rows


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return slug or "entry"


def inline_markdown(value: str) -> str:
    escaped = html.escape(value)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    escaped = re.sub(
        r"(https?://[^\s<]+)",
        r'<a href="\1">\1</a>',
        escaped,
    )
    return escaped


def render_table(lines: list[str]) -> str:
    rows = [split_markdown_row(line) for line in lines]
    header = rows[0]
    body = rows[2:]
    out = ["<table>", "<thead><tr>"]
    out.extend(f"<th>{inline_markdown(cell)}</th>" for cell in header)
    out.append("</tr></thead>")
    out.append("<tbody>")
    for row in body:
        out.append("<tr>")
        out.extend(f"<td>{inline_markdown(cell)}</td>" for cell in row)
        out.append("</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


def markdown_to_html(markdown: str) -> str:
    output: list[str] = []
    paragraph: list[str] = []
    list_open = False
    quote_open = False
    code_open = False
    code_lines: list[str] = []
    table_lines: list[str] = []

    def close_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            output.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")
            paragraph = []

    def close_list() -> None:
        nonlocal list_open
        if list_open:
            output.append("</ul>")
            list_open = False

    def close_quote() -> None:
        nonlocal quote_open
        if quote_open:
            output.append("</blockquote>")
            quote_open = False

    def close_table() -> None:
        nonlocal table_lines
        if table_lines:
            output.append(render_table(table_lines))
            table_lines = []

    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()

        if line.startswith("```"):
            close_paragraph()
            close_list()
            close_quote()
            close_table()
            if code_open:
                output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
                code_lines = []
                code_open = False
            else:
                code_open = True
            continue

        if code_open:
            code_lines.append(line)
            continue

        if re.match(r"^\|.*\|$", line):
            close_paragraph()
            close_list()
            close_quote()
            table_lines.append(line)
            continue
        close_table()

        if not line.strip():
            close_paragraph()
            close_list()
            close_quote()
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            close_paragraph()
            close_list()
            close_quote()
            level = len(heading.group(1))
            output.append(f"<h{level}>{inline_markdown(heading.group(2))}</h{level}>")
            continue

        if line.startswith(">"):
            close_paragraph()
            close_list()
            if not quote_open:
                output.append("<blockquote>")
                quote_open = True
            output.append(f"<p>{inline_markdown(line.lstrip('> '))}</p>")
            continue

        item = re.match(r"^\s*[-*]\s+(.+)$", line)
        if item:
            close_paragraph()
            close_quote()
            if not list_open:
                output.append("<ul>")
                list_open = True
            output.append(f"<li>{inline_markdown(item.group(1))}</li>")
            continue

        close_list()
        close_quote()
        paragraph.append(line)

    close_paragraph()
    close_list()
    close_quote()
    close_table()
    if code_open:
        output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")

    return "\n".join(output)


def page_shell(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    body {{
      color: #17202a;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.55;
      margin: 0 auto;
      max-width: 1160px;
      padding: 2rem;
    }}
    a {{ color: #005ea8; }}
    table {{
      border-collapse: collapse;
      font-size: 0.92rem;
      margin: 1rem 0 1.5rem;
      width: 100%;
    }}
    th, td {{
      border: 1px solid #d8dee4;
      padding: 0.45rem 0.55rem;
      text-align: left;
      vertical-align: top;
    }}
    th {{ background: #f6f8fa; }}
    code {{
      background: #f6f8fa;
      border-radius: 4px;
      padding: 0.1rem 0.25rem;
    }}
    pre {{
      background: #f6f8fa;
      border: 1px solid #d8dee4;
      border-radius: 6px;
      overflow-x: auto;
      padding: 1rem;
    }}
    blockquote {{
      border-left: 4px solid #d8dee4;
      color: #57606a;
      margin-left: 0;
      padding-left: 1rem;
    }}
    .review-meta {{
      background: #f6f8fa;
      border: 1px solid #d8dee4;
      border-radius: 6px;
      padding: 1rem;
    }}
    .missing {{ color: #9a3412; font-weight: 600; }}
    .muted {{ color: #57606a; }}
  </style>
</head>
<body>
{body}
</body>
</html>
"""


def entry_filename(row: RegisterRow) -> str:
    return f"{row.register_id}-{slugify(row.source)[:72]}.html"


def render_entry_page(row: RegisterRow, output_dir: Path) -> str:
    filename = entry_filename(row)
    entry_file_display = (
        row.entry_file.relative_to(ROOT).as_posix() if row.entry_file else row.entry_cell
    )
    metadata_rows = [
        ("Register id", row.register_id),
        ("Source", row.source),
        ("Category", row.category),
        ("Org / authors", row.org_authors),
        ("Year", row.year),
        ("Evidence basis", row.evidence_basis),
        ("Operational proximity", row.operational_proximity),
        ("Review state", row.review_state),
        ("Description", row.project_impact),
        ("Entry file", entry_file_display),
    ]
    metadata = "\n".join(
        f"<tr><th>{html.escape(key)}</th><td>{inline_markdown(value)}</td></tr>"
        for key, value in metadata_rows
    )
    if row.entry_file:
        entry_html = markdown_to_html(row.entry_file.read_text(encoding="utf-8"))
    else:
        entry_html = (
            '<p class="missing">No matching working entry file was found for this register row.</p>'
        )

    body = f"""
<p><a href="index.html">Back to index</a></p>
<h1>{html.escape(row.register_id)}: {html.escape(row.source)}</h1>
<div class="review-meta">
<table>
<tbody>
{metadata}
</tbody>
</table>
</div>
<hr>
{entry_html}
"""
    (output_dir / filename).write_text(
        page_shell(f"{row.register_id}: {row.source}", body),
        encoding="utf-8",
    )
    return filename


def render_index(rows: list[RegisterRow], links: dict[str, str], output_dir: Path) -> None:
    table_rows = []
    for row in rows:
        link = links.get(row.register_id)
        html_link = (
            f'<a href="{html.escape(link)}">HTML</a>'
            if link
            else '<span class="missing">missing</span>'
        )
        md_link = (
            f'<a href="../register-entries/{html.escape(row.entry_file.name)}">Markdown</a>'
            if row.entry_file
            else '<span class="missing">missing</span>'
        )
        table_rows.append(
            "<tr>"
            f"<td>{html.escape(row.register_id)}</td>"
            f"<td>{html.escape(row.source)}</td>"
            f"<td>{inline_markdown(row.project_impact)}</td>"
            f"<td>{html.escape(row.category)}</td>"
            f"<td>{html.escape(row.evidence_basis)}</td>"
            f"<td>{html.escape(row.operational_proximity)}</td>"
            f"<td>{html.escape(row.review_state)}</td>"
            f"<td>{html_link}</td>"
            f"<td>{md_link}</td>"
            "</tr>"
        )

    missing = [row for row in rows if row.entry_file is None]
    missing_note = ""
    if missing:
        missing_note = (
            f'<p class="missing">{len(missing)} register rows could not be matched to working '
            "entry files. They still appear in the index for review.</p>"
        )

    body = f"""
<h1>Register Entry Review HTML</h1>
<p class="muted">Generated from <code>site/reading/evidence-register.qmd</code> and
<code>working/register-entries/</code>. These files are local review artifacts and are
ignored by git.</p>
{missing_note}
<table>
<thead>
<tr>
  <th>Register id</th>
  <th>Source</th>
  <th>Description</th>
  <th>Category</th>
  <th>Evidence basis</th>
  <th>Operational proximity</th>
  <th>Review state</th>
  <th>HTML</th>
  <th>Markdown</th>
</tr>
</thead>
<tbody>
{''.join(table_rows)}
</tbody>
</table>
"""
    (output_dir / "index.html").write_text(
        page_shell("Register Entry Review HTML", body),
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--entries", type=Path, default=DEFAULT_ENTRIES)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    rows = parse_inventory(args.register, args.entries)
    args.output.mkdir(parents=True, exist_ok=True)

    links: dict[str, str] = {}
    for row in rows:
        links[row.register_id] = render_entry_page(row, args.output)
    render_index(rows, links, args.output)

    print(f"Wrote {len(rows)} entry pages plus index to {args.output}")
    missing_count = sum(row.entry_file is None for row in rows)
    if missing_count:
        print(f"Warning: {missing_count} register rows did not match a working entry file")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
