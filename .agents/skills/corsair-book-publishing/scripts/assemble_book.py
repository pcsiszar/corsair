#!/usr/bin/env python3
"""
Assemble Corsair Core Rulebook HTML chapters into a single master publication file for PDF printing.
"""

import os
import re
import sys
import argparse
from pathlib import Path

CHAPTER_SEQUENCE = [
    "00_Front_Matter.html",
    "01_Core_Mechanics.html",
    "01b_Interlude_27th_Hour.html",
    "02_Character_Creation.html",
    "02b_Interlude_Great_Tithe.html",
    "03_Classes.html",
    "04_Armory_and_Gear.html",
    "05_Starships.html",
    "06a_GM_Operations.html",
    "06b_GM_Bestiary.html",
    "07_World_of_the_Sphere.html",
    "08_Forbidden_Archives.html",
    "09_Fiction_Anthology.html",
    "10_Appendices_and_Index.html"
]

def assemble(html_dir: Path, output_file: Path):
    if not html_dir.exists():
        print(f"Error: Directory '{html_dir}' does not exist.", file=sys.stderr)
        sys.exit(1)

    print(f"Reading chapters from: {html_dir}")
    chapters_content = []
    found_chapters = 0

    for ch_name in CHAPTER_SEQUENCE:
        ch_path = html_dir / ch_name
        if not ch_path.exists():
            print(f"  [SKIPPED] {ch_name} (file not yet created)")
            continue

        print(f"  [ADDING]  {ch_name}")
        content = ch_path.read_text(encoding="utf-8")
        
        # Extract body content
        body_match = re.search(r"<body[^>]*>(.*?)</body>", content, re.DOTALL | re.IGNORECASE)
        body_inner = body_match.group(1) if body_match else content

        # Strip navigation bars
        body_inner = re.sub(r'<nav class=[\'"]book-nav[\'"].*?</nav>', '', body_inner, flags=re.DOTALL | re.IGNORECASE)

        # Normalize relative asset paths for dist/ (one level up instead of two)
        body_inner = body_inner.replace('../../assets/', '../assets/')

        chapter_id = Path(ch_name).stem
        section_html = f'\n<!-- CHAPTER START: {ch_name} -->\n<section class="book-chapter" id="{chapter_id}">\n{body_inner.strip()}\n</section>\n'
        chapters_content.append(section_html)
        found_chapters += 1

    if found_chapters == 0:
        print("Warning: No matching chapter files were found to assemble.", file=sys.stderr)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    master_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Corsair — Core Rulebook (Master Edition)</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400;1,700;1,800&family=Barlow:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,600&family=Orbitron:wght@600;700;800;900&family=Rajdhani:wght@500;600;700&family=Share+Tech+Mono&display=swap" rel="stylesheet">
    
    <!-- Shared Publication Stylesheets -->
    <link rel="stylesheet" href="../assets/css/corsair-variables.css">
    <link rel="stylesheet" href="../assets/css/corsair-typography.css">
    <link rel="stylesheet" href="../assets/css/corsair-components.css">
    <link rel="stylesheet" href="../assets/css/corsair-layout.css">
    <link rel="stylesheet" href="../assets/css/corsair-print.css">
</head>
<body class="rulebook-master">
{''.join(chapters_content)}
</body>
</html>
"""

    output_file.write_text(master_html, encoding="utf-8")
    print(f"\nSuccessfully compiled master book publication:")
    print(f"  Destination: {output_file.resolve()}")
    print(f"  Chapters included: {found_chapters}/{len(CHAPTER_SEQUENCE)}")

def main():
    parser = argparse.ArgumentParser(description="Assemble modular Corsair HTML chapters into a master printable publication.")
    parser.add_argument("--input-dir", "-i", default="rulebook/html", help="Directory containing modular chapter HTML files (default: rulebook/html)")
    parser.add_argument("--output", "-o", default="dist/Corsair_Core_Rulebook_Master.html", help="Destination master HTML file (default: dist/Corsair_Core_Rulebook_Master.html)")
    args = parser.parse_args()

    assemble(Path(args.input_dir), Path(args.output))

if __name__ == "__main__":
    main()
