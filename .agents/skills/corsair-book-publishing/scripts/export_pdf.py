#!/usr/bin/env python3
"""
Export Corsair HTML rulebook chapters or master compilation to print-ready A4 PDF via headless Chromium.
"""

import os
import sys
import shutil
import argparse
import subprocess
from pathlib import Path

def find_chromium_browser():
    """Locate Google Chrome or Microsoft Edge on Windows, Linux, or macOS."""
    # 1. Environment variable override
    env_browser = os.environ.get("CHROME_BIN") or os.environ.get("BROWSER_BIN")
    if env_browser and Path(env_browser).exists():
        return env_browser

    # 2. Standard Windows installation paths
    windows_candidates = [
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
        Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
        Path(os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")),
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    ]
    for candidate in windows_candidates:
        if candidate.exists():
            return str(candidate)

    # 3. macOS paths
    mac_candidates = [
        Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
        Path("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
    ]
    for candidate in mac_candidates:
        if candidate.exists():
            return str(candidate)

    # 4. PATH lookup
    for bin_name in ["google-chrome", "chrome", "chromium", "chromium-browser", "msedge", "edge"]:
        path = shutil.which(bin_name)
        if path:
            return path

    return None

def verify_pdf(pdf_path: Path):
    """Inspect and report PDF page count and physical geometry."""
    try:
        import pypdf
        reader = pypdf.PdfReader(str(pdf_path))
        page_count = len(reader.pages)
        print(f"\n[VERIFICATION] PDF Validation via pypdf:")
        print(f"  Total Pages: {page_count}")
        for i, page in enumerate(reader.pages):
            box = page.mediabox
            w_mm = float(box.width) * 25.4 / 72.0
            h_mm = float(box.height) * 25.4 / 72.0
            is_a4 = abs(w_mm - 210.0) < 1.0 and abs(h_mm - 297.0) < 1.0
            status = "ISO A4 OK" if is_a4 else f"NON-STANDARD ({w_mm:.1f}x{h_mm:.1f}mm)"
            print(f"  Page {i+1:02d}: {w_mm:6.2f}mm x {h_mm:6.2f}mm [{status}]")
    except ImportError:
        print("\n[NOTE] Install 'pypdf' (pip install pypdf) for automated page dimension validation.")

def export_pdf(html_file: Path, pdf_file: Path):
    if not html_file.exists():
        print(f"Error: Source HTML file '{html_file}' does not exist.", file=sys.stderr)
        sys.exit(1)

    browser = find_chromium_browser()
    if not browser:
        print("Error: Could not locate Chrome or Edge executable.", file=sys.stderr)
        print("Please install Google Chrome or Microsoft Edge, or set CHROME_BIN environment variable.", file=sys.stderr)
        sys.exit(1)

    pdf_file.parent.mkdir(parents=True, exist_ok=True)
    html_url = html_file.resolve().as_uri()

    print(f"Exporting HTML to print-ready A4 PDF:")
    print(f"  Source HTML: {html_file.resolve()}")
    print(f"  Target PDF:  {pdf_file.resolve()}")
    print(f"  Browser:     {browser}")

    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_file.resolve()}",
        html_url
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during PDF printing: {e.stderr}", file=sys.stderr)
        sys.exit(1)

    if not pdf_file.exists():
        print(f"Error: Target PDF file was not created.", file=sys.stderr)
        sys.exit(1)

    size_kb = pdf_file.stat().st_size / 1024.0
    print(f"  Status:      SUCCESS ({size_kb:.1f} KB)")
    verify_pdf(pdf_file)

def main():
    parser = argparse.ArgumentParser(description="Export Corsair HTML chapter or master book to PDF via headless Chromium.")
    parser.add_argument("--input", "-i", required=True, help="Input HTML file path (e.g. html/00_Front_Matter.html)")
    parser.add_argument("--output", "-o", help="Output PDF file path (default: same stem as input with .pdf extension)")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path.with_suffix(".pdf")

    export_pdf(input_path, output_path)

if __name__ == "__main__":
    main()
