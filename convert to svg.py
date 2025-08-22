#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert specific PDF figures to SVG (robust) for GitHub Pages.
- Tries Poppler (pdftocairo -svg -cropbox)
- If SVG looks blank, falls back to MuPDF (mutool draw -F svg)
- Also emits a PNG for reliable webpage rendering.

Prereqs (macOS):
  brew install poppler mupdf
"""

import re
import shutil
import subprocess
from pathlib import Path

# --- Input PDFs (exactly as you provided) ---
PDFS = [
    "/Users/mikemcrae/Documents/GitHub/mike-mcrae.github.io/images/paper2/01. Combined Monthly Event Study (Threat).pdf",
    "/Users/mikemcrae/Documents/GitHub/mike-mcrae.github.io/images/paper2/02. DDD Gab Gettr monthly(threat).pdf",
    "/Users/mikemcrae/Documents/GitHub/mike-mcrae.github.io/images/paper2/05.comparative timeseries ts gettr gab top decile vs bottom (threat).pdf",
]

VEC_TAG_RE = re.compile(r"<(path|polyline|polygon|rect|circle|ellipse|line|text)\b", re.I)

def check_tool(tool: str, tip: str = "") -> None:
    if shutil.which(tool) is None:
        raise SystemExit(f"Error: '{tool}' not found. {tip}")

def get_num_pages(pdf_path: Path) -> int:
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

def svg_looks_blank(svg_path: Path) -> bool:
    try:
        if not svg_path.exists():
            return True
        size = svg_path.stat().st_size
        if size < 1500:  # tiny file → likely blank
            return True
        txt = svg_path.read_text(errors="ignore")
        return VEC_TAG_RE.search(txt) is None
    except Exception:
        return True

def run_pdftocairo_svg(pdf: Path, page: int, out_base: Path, single: bool) -> Path:
    # Poppler export (CropBox avoids off-canvas content)
    out = (out_base.with_suffix(".svg") if single else Path(f"{out_base}_p{page}.svg"))
    cmd = [
        "pdftocairo", "-svg", "-cropbox",
        "-f", str(page), "-l", str(page),
        str(pdf), str(out_base if single else f"{out_base}_p{page}")
    ]
    subprocess.run(cmd, check=True)
    return out

def run_mutool_svg(pdf: Path, page: int, out_base: Path, single: bool) -> Path:
    # MuPDF export (handles tricky transparency/groups)
    # Writes pattern with %d; we request just one page via -s
    temp_pattern = f"{out_base}_mup-%d.svg" if not single else f"{out_base}_mup-%d.svg"
    cmd = ["mutool", "draw", "-F", "svg", "-o", temp_pattern, "-s", str(page), str(pdf)]
    subprocess.run(cmd, check=True)
    produced = Path(temp_pattern.replace("%d", str(page)))
    final = out_base.with_suffix(".svg") if single else Path(f"{out_base}_p{page}.svg")
    produced.replace(final)
    return final

def run_pdftocairo_png(pdf: Path, page: int, out_base: Path, single: bool) -> Path:
    # Reliable raster fallback for web display
    out = out_base.with_suffix(".png") if single else Path(f"{out_base}_p{page}.png")
    # Use -singlefile only for single-page export
    cmd = [
        "pdftocairo", "-png",
        "-f", str(page), "-l", str(page),
        str(pdf), str(out_base if single else f"{out_base}_p{page}")
    ]
    subprocess.run(cmd, check=True)
    return out

def convert_pdf(pdf_path: Path) -> None:
    if not pdf_path.exists():
        print(f"Skip (not found): {pdf_path}")
        return
    pages = get_num_pages(pdf_path)
    base = pdf_path.with_suffix("")
    single = (pages == 1)

    for p in range(1, pages + 1):
        out_base = base  # base name without suffix
        try:
            svg_path = run_pdftocairo_svg(pdf_path, p, out_base, single and p == 1)
            if svg_looks_blank(svg_path):
                # Try MuPDF if Poppler SVG looks empty
                print(f"Poppler SVG looked blank (page {p}); trying MuPDF…")
                svg_path = run_mutool_svg(pdf_path, p, out_base, single and p == 1)
                if svg_looks_blank(svg_path):
                    print(f"MuPDF SVG also looked blank (page {p}); exporting PNG fallback…")
                    png_path = run_pdftocairo_png(pdf_path, p, out_base, single and p == 1)
                    print(f"OK PNG: {png_path}")
                else:
                    print(f"OK MuPDF SVG: {svg_path}")
            else:
                print(f"OK Poppler SVG: {svg_path}")
        except subprocess.CalledProcessError as e:
            print(f"Vector export failed on page {p}: {e}. Exporting PNG fallback…")
            png_path = run_pdftocairo_png(pdf_path, p, out_base, single and p == 1)
            print(f"OK PNG: {png_path}")

def main():
    check_tool("pdfinfo", "Install Poppler: brew install poppler")
    check_tool("pdftocairo", "Install Poppler: brew install poppler")
    check_tool("mutool", "Install MuPDF: brew install mupdf")  # used as fallback

    for f in PDFS:
        convert_pdf(Path(f))

if __name__ == "__main__":
    main()
