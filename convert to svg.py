#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 10:26:46 2025

@author: mikemcrae
"""

#!/usr/bin/env python3
"""
Convert specific PDF figures to SVG for GitHub Pages using Poppler's pdftocairo.

Prerequisite (macOS):
  brew install poppler

Why pdftocairo?
  It preserves vector graphics from PDF → SVG (no rasterization), ideal for plots.
"""

import os
import subprocess
from pathlib import Path

# --- Input PDFs (exactly as you provided) ---
PDFS = [
    "/Users/mikemcrae/Documents/GitHub/mike-mcrae.github.io/images/paper2/01. Combined Monthly Event Study (Threat).pdf",
    "/Users/mikemcrae/Documents/GitHub/mike-mcrae.github.io/images/paper2/02. DDD Gab Gettr monthly(threat).pdf",
    "/Users/mikemcrae/Documents/GitHub/mike-mcrae.github.io/images/paper2/05.comparative timeseries ts gettr gab top decile vs bottom (threat).pdf",
]

def check_tool(tool: str) -> None:
    try:
        subprocess.run([tool, "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except (OSError, subprocess.CalledProcessError):
        raise SystemExit(
            f"Error: '{tool}' not found. On macOS, install Poppler via:\n  brew install poppler"
        )

def get_num_pages(pdf_path: Path) -> int:
    """Use 'pdfinfo' (from Poppler) to get page count. Fallback to 1 if unavailable."""
    try:
        out = subprocess.run(
            ["pdfinfo", str(pdf_path)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True
        ).stdout
        for line in out.splitlines():
            if line.strip().lower().startswith("pages:"):
                return int(line.split(":", 1)[1].strip())
    except Exception:
        pass
    return 1  # conservative fallback

def convert_pdf_to_svg(pdf_path: Path) -> None:
    if not pdf_path.exists():
        print(f"Skip (not found): {pdf_path}")
        return

    pages = get_num_pages(pdf_path)
    out_base = pdf_path.with_suffix("")  # path without .pdf

    if pages == 1:
        # Single page → single SVG
        cmd = [
            "pdftocairo",
            "-svg",
            "-f", "1",
            "-l", "1",
            str(pdf_path),
            str(out_base),  # pdftocairo appends .svg automatically
        ]
        subprocess.run(cmd, check=True)
        print(f"OK: {pdf_path.name} → {out_base.with_suffix('.svg').name}")
    else:
        # Multi-page → one SVG per page with _p{n}.svg suffix
        for p in range(1, pages + 1):
            out_base_page = Path(f"{out_base}_p{p}")
            cmd = [
                "pdftocairo",
                "-svg",
                "-f", str(p),
                "-l", str(p),
                str(pdf_path),
                str(out_base_page),
            ]
            subprocess.run(cmd, check=True)
        print(f"OK: {pdf_path.name} → {pages} SVG files ({out_base.name}_p1.svg …)")

def main():
    # Ensure required tools exist
    check_tool("pdftocairo")
    check_tool("pdfinfo")

    for f in PDFS:
        convert_pdf_to_svg(Path(f))

if __name__ == "__main__":
    main()
