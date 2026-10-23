#!/usr/bin/env python3
"""
Generate Chapter 07: Worlds of the Sphere (html/07_World_of_the_Sphere.html)
Spans exactly 36 pages: Pages 114 to 149 (18 two-page spreads).
Authoritative publication module translating rulebook/lore/ into print-ready A4 HTML.
"""

import sys
from pathlib import Path

# Add project root to sys.path so imports resolve
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scratch.ch07.part1_intro import get_part1_html
from scratch.ch07.part2_celestial import get_part2_html
from scratch.ch07.part3_gazetteers import get_part3_html
from scratch.ch07.part4_timeline import get_part4_html
from scratch.ch07.part5_colonies import get_part5_html
from scratch.ch07.part6_corporations import get_part6_html
from scratch.ch07.part7_underworld import get_part7_html
from scratch.ch07.part8_flotilla import get_part8_html
from scratch.ch07.part9_aliens import get_part9_html

def build_chapter_html():
    html_parts = []

    # HTML Head & Styles
    html_parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Corsair TTRPG — Chapter 07: Worlds of the Sphere</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400;1,700;1,800&family=Barlow:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,600&family=Orbitron:wght@600;700;800;900&family=Rajdhani:wght@500;600;700&family=Share+Tech+Mono&display=swap" rel="stylesheet">
    
    <!-- Shared Modular Stylesheets -->
    <link rel="stylesheet" href="../assets/css/corsair-variables.css">
    <link rel="stylesheet" href="../assets/css/corsair-typography.css">
    <link rel="stylesheet" href="../assets/css/corsair-components.css">
    <link rel="stylesheet" href="../assets/css/corsair-layout.css">
    <link rel="stylesheet" href="../assets/css/corsair-print.css">
</head>
<body class="book-screen-canvas">
""")

    # Append all 9 parts (54 pages total, Pages 114 to 167)
    html_parts.append(get_part1_html())
    html_parts.append(get_part2_html())
    html_parts.append(get_part3_html())
    html_parts.append(get_part4_html())
    html_parts.append(get_part5_html())
    html_parts.append(get_part6_html())
    html_parts.append(get_part7_html())
    html_parts.append(get_part8_html())
    html_parts.append(get_part9_html())

    html_parts.append("""</body>
</html>
""")

    return "".join(html_parts)

def main():
    output_path = Path("html/07_World_of_the_Sphere.html")
    print(f"Generating Chapter 07: Worlds of the Sphere -> {output_path}")
    html_content = build_chapter_html()
    output_path.write_text(html_content, encoding="utf-8")
    print(f"Successfully generated {output_path} ({len(html_content)} bytes)")

if __name__ == "__main__":
    main()
