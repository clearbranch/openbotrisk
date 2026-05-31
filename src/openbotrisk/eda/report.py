"""Markdown report writer for EDA outputs."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


SECTIONS = [
    "Access",
    "Structure",
    "Schema",
    "Label",
    "Identifier inventory",
    "Temporal structure",
    "Missing data",
    "Quirks and observations",
    "Reproduction",
]


def write_report(
    stats: Dict[str, Any],
    dataset_name: str,
    output_path: str | Path,
) -> Path:
    """Write a markdown report for a dataset.

    ``stats`` must contain one key per section name (case-sensitive) holding
    the markdown body for that section. Missing sections are written as
    ``_(not produced)_``.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [f"# EDA: {dataset_name}", ""]
    for section in SECTIONS:
        lines.append(f"## {section}")
        body = stats.get(section)
        if body is None or str(body).strip() == "":
            lines.append("_(not produced)_")
        else:
            lines.append(str(body).rstrip())
        lines.append("")

    output_path.write_text("\n".join(lines))
    return output_path
