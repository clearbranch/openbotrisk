"""Centralised filesystem paths for the openbotrisk project.

Import these instead of recomputing ``Path(__file__).resolve().parents[...]``
in every script or notebook::

    from openbotrisk.config import REPO_ROOT, DATA_DIR, IMAGE_DIR

``REPO_ROOT`` is resolved relative to this file, so every path here is correct
regardless of the current working directory. Per-experiment generated-data
directories are defined in each experiment from ``EXPERIMENTS_DIR``.
"""

from __future__ import annotations

from pathlib import Path

# This file lives at <repo>/src/openbotrisk/config.py, so the repo root is two
# levels above the package directory.
REPO_ROOT = Path(__file__).resolve().parents[2]

SRC_DIR = REPO_ROOT / "src"
EXPERIMENTS_DIR = REPO_ROOT / "experiments"
SITE_DIR = REPO_ROOT / "site"

# Top-level data directory and the shared methodology-figure output directory.
DATA_DIR = REPO_ROOT / "data"
IMAGE_DIR = SITE_DIR / "methodology" / "images"
