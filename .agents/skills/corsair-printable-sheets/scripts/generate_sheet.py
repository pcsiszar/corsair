#!/usr/bin/env python3
"""
Corsair Printable Sheet Generator
Generates print-ready A4 HTML sheets containing the complete Corsair CSS design system,
typography, dark-mode styling, and print media rules for high-contrast B&W printing.
"""

import argparse
import sys
from pathlib import Path

MASTER_CSS = """/* ======================================================  TOKENS  */
:root {
    --black: #080a0c;
    --dark: #10131a;
    --mid: #181c24;
    --surface: #1d2130;
    --border: #2a3040;
    --border-light: #3a4256;
    --accent: #c8a84b;
    --accent-dim: #7a6428;
    --accent-glow: rgba(200, 168, 75, 0.15);
    --red: #a02828;
    --red-dim: #5c1616;
    --cyan: #29b6f6;
    --green: #4caf50;
    --text: #ccc7ba;
    --text-dim: #6a6458;
    --text-muted: #3e3c36;
    --stripe: rgba(200, 168, 75, 0.03);

    --font-title: 'Barlow Condensed', sans-serif;
    --font-body: 'Barlow', sans-serif;
    --font-mono: 'Share Tech Mono', monospace;
}

/* ======================================================  RESET  */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    font-size: 8pt;
}

body {
    font-family: var(--font-body);
    background: var(--black);
    color: var(--text);
    line-height: 1.25;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

/* ======================================================  PRINT STYLES  */
@page {
    size: A4 portrait;
    margin: 3.5mm;
}

@media print {
    body {
        background: #ffffff !important;
    }

    :root {
        --black: #ffffff;
        --dark: #ffffff;
        --mid: #ffffff;
        --surface: #ffffff;
        --border: #888888;
        --border-light: #cccccc;
        --accent: #000000;
        --accent-dim: #333333;
        --accent-glow: transparent;
        --red: #8b1a1a;
        --red-dim: #555555;
        --text: #000000;
        --text-dim: #333333;
        --text-muted: #666666;
        --stripe: transparent;
    }

    .page {
        background: #ffffff !important;
        box-shadow: none !important;
        padding: 0 !important;
        margin: 0 !important;
        border: none !important;
    }

    .page::before {
        display: none !important;
    }

    .mh-logo {
        background: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #000000 !important;
        clip-path: none !important;
        padding-right: 4mm !important;
        min-width: unset !important;
    }

    .mh-logo svg {
        fill: #000000 !important;
    }

    .card-hd {
        border-bottom-width: 1px !important;
    }

    .card-hd svg {
        fill: #000000 !important;
    }

    .id-field,
    .attr-block,
    .xc-block,
    .rank-box,
    .attr-box,
    .condition-circle,
    .g-slot,
    .pip,
    .pip-box,
    .d10-footprint,
    .trait-status .ub {
        background: #ffffff !important;
        border-color: #000000 !important;
        color: #000000 !important;
    }

    .skill-table th,
    .eq-table th,
    .data-table th {
        background: #ffffff !important;
        color: #000000 !important;
        border-bottom: 1px solid #000000 !important;
    }

    .skill-section-hd td {
        background: #f0f0f0 !important;
        color: #000000 !important;
        border-color: #000000 !important;
    }

    .fl,
    .note-line {
        border-bottom-color: #888888 !important;
    }

    .badge, .tag {
        border: 1px solid #000000 !important;
        color: #000000 !important;
        background: #ffffff !important;
    }
}

/* ======================================================  PAGE CONTAINER  */
.page {
    width: 210mm;
    min-height: 297mm;
    max-height: 297mm;
    margin: 0 auto;
    padding: 3.5mm 4.5mm;
    background: var(--dark);
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}

/* Hard sci-fi subtle grid background overlay */
.page::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(200, 168, 75, 0.016) 1px, transparent 1px),
        linear-gradient(90deg, rgba(200, 168, 75, 0.016) 1px, transparent 1px);
    background-size: 18px 18px;
    pointer-events: none;
}

/* ======================================================  MASTHEAD  */
.masthead {
    display: flex;
    align-items: stretch;
    margin-bottom: 2.5mm;
    border: 1px solid var(--accent-dim);
    background: var(--mid);
    flex-shrink: 0;
}

.mh-logo {
    background: var(--accent);
    color: var(--black);
    padding: 2mm 3.5mm;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    clip-path: polygon(0 0, calc(100% - 8px) 0, 100% 50%, calc(100% - 8px) 100%, 0 100%);
    padding-right: 10mm;
    min-width: 18mm;
    flex-shrink: 0;
}

.mh-logo svg {
    width: 18px;
    height: 18px;
    fill: var(--black);
}

.mh-logo .logo-text {
    font-family: var(--font-title);
    font-weight: 900;
    font-size: 5.5pt;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    margin-top: 1px;
}

.mh-title {
    padding: 2mm 3.5mm;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.mh-title h1 {
    font-family: var(--font-title);
    font-weight: 900;
    font-size: 14pt;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--accent);
    line-height: 1;
}

.mh-title .sub {
    font-family: var(--font-title);
    font-weight: 300;
    font-size: 6.8pt;
    letter-spacing: 0.25em;
    color: var(--text-dim);
    text-transform: uppercase;
    margin-top: 1px;
}

.mh-meta {
    border-left: 1px solid var(--border);
    padding: 2mm 3.5mm;
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-width: 50mm;
}

.mh-meta label {
    font-family: var(--font-title);
    font-size: 5.5pt;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--accent-dim);
    margin-bottom: 0.5mm;
}

.fl {
    border-bottom: 1px solid var(--border);
    min-height: 4.5mm;
}

/* ======================================================  LAYOUT GRIDS  */
.grid-main {
    display: grid;
    gap: 2mm;
    flex: 1;
    align-items: start;
}

.grid-1col { grid-template-columns: 1fr; }
.grid-2col { grid-template-columns: 1fr 1fr; }
.grid-3col { grid-template-columns: 1fr 1fr 1fr; }
.grid-split-left { grid-template-columns: 65mm 1fr; }
.grid-split-right { grid-template-columns: 1fr 65mm; }
.grid-split-equal { grid-template-columns: 1fr 1fr; }

/* ======================================================  CARDS  */
.card {
    background: var(--surface);
    border: 1px solid var(--border);
    margin-bottom: 2mm;
    display: flex;
    flex-direction: column;
}

.card:last-child {
    margin-bottom: 0;
}

.card-hd {
    background: var(--mid);
    border-bottom: 1.5px solid var(--accent-dim);
    padding: 1.2mm 2.2mm;
    display: flex;
    align-items: center;
    gap: 1.5mm;
    flex-shrink: 0;
}

.card-hd svg {
    width: 11px;
    height: 11px;
    fill: var(--accent);
    flex-shrink: 0;
}

.card-hd h2 {
    font-family: var(--font-title);
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--accent);
    flex: 1;
    line-height: 1;
}

.card-body {
    padding: 2mm;
    flex: 1;
}

.card-body.no-pad {
    padding: 0;
}

/* ======================================================  ATTRIBUTES & STATS  */
.attr-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5mm;
}

.attr-block {
    background: var(--mid);
    border: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 1.5mm;
    padding: 1mm 1.5mm;
}

.attr-box {
    width: 7mm;
    height: 7mm;
    border: 1.5px solid var(--accent-dim);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-title);
    font-size: 11pt;
    font-weight: 900;
    color: var(--accent);
    flex-shrink: 0;
    background: var(--surface);
}

.attr-meta {
    flex: 1;
    display: flex;
    flex-direction: column;
}

.attr-name {
    font-family: var(--font-title);
    font-size: 7pt;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text);
    line-height: 1;
}

.attr-code {
    font-family: var(--font-mono);
    font-size: 5.5pt;
    color: var(--text-dim);
    margin-top: 1px;
}

/* ======================================================  PIPS & TRACKERS  */
.pip-row {
    display: flex;
    gap: 2px;
    align-items: center;
}

.pip {
    width: 7px;
    height: 12px;
    border: 1px solid var(--accent-dim);
    background: var(--mid);
}

.pip.filled {
    background: var(--accent);
}

.condition-circle {
    width: 6mm;
    height: 6mm;
    border: 1px solid var(--border-light);
    border-radius: 50%;
    background: var(--mid);
    display: inline-flex;
    align-items: center;
    justify-content: center;
}

/* ======================================================  TABLES  */
.skill-table, .data-table {
    width: 100%;
    border-collapse: collapse;
}

.skill-table th, .data-table th {
    font-family: var(--font-title);
    font-size: 6.5pt;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--accent-dim);
    text-align: left;
    padding: 1.2mm 2mm;
    border-bottom: 1px solid var(--accent-dim);
    background: var(--mid);
}

.skill-table td, .data-table td {
    border-bottom: 1px solid var(--border);
    padding: 1.5mm 2mm;
    vertical-align: top;
    font-size: 7.2pt;
}

.skill-table tr:nth-child(even) td,
.data-table tr:nth-child(even) td {
    background: var(--stripe);
}

.skill-section-hd td {
    font-family: var(--font-title);
    font-size: 6.5pt;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--accent);
    background: var(--mid) !important;
    border-top: 1px solid var(--accent-dim);
    border-bottom: 1px solid var(--accent-dim);
    padding: 0.8mm 2mm !important;
    line-height: 1;
}

/* ======================================================  RULES TEXT & CALLOUTS  */
.rules-text {
    font-family: var(--font-body);
    font-size: 7.4pt;
    color: var(--text);
    line-height: 1.3;
}

.rules-text p {
    margin-bottom: 1mm;
}

.rules-text p:last-child {
    margin-bottom: 0;
}

.rules-text strong {
    color: var(--accent);
    font-weight: 600;
}

.rule-box {
    background: var(--mid);
    border-left: 2px solid var(--accent);
    padding: 1.2mm 2mm;
    margin-bottom: 1.5mm;
    font-size: 7.2pt;
}

.badge, .tag {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 5.5pt;
    padding: 0.5px 3px;
    border: 1px solid var(--border-light);
    color: var(--text-dim);
    text-transform: uppercase;
    background: var(--mid);
}

.badge.accent {
    border-color: var(--accent-dim);
    color: var(--accent);
}

.badge.red {
    border-color: var(--red-dim);
    color: var(--red);
}

/* ======================================================  PAGE FOOTER  */
.page-foot {
    font-family: var(--font-title);
    font-size: 6pt;
    letter-spacing: 0.3em;
    color: var(--text-muted);
    text-align: center;
    text-transform: uppercase;
    margin-top: auto;
    padding-top: 2mm;
    flex-shrink: 0;
}
"""

SVG_ICONS = {
    "corsair_logo": '<svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" /><circle cx="12" cy="12" r="1.5" /></svg>',
    "swords": '<svg viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>',
    "shield": '<svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "gear": '<svg viewBox="0 0 24 24"><path d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/></svg>',
    "crosshairs": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="22" y1="12" x2="18" y2="12"/><line x1="6" y1="12" x2="2" y2="12"/><line x1="12" y1="6" x2="12" y2="2"/><line x1="12" y1="22" x2="12" y2="18"/></svg>',
    "terminal": '<svg viewBox="0 0 24 24"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>',
}

def generate_html(title: str, subtitle: str, sheet_type: str = "reference", meta_label: str = "Document Code") -> str:
    """Generate the complete A4 HTML string based on template type."""

    meta_slot = f"""            <div class="mh-meta">
                <label>{meta_label}</label>
                <div class="fl"></div>
            </div>"""

    if sheet_type == "reference":
        body_content = f"""        <div class="intro-text rules-text" style="margin-bottom: 2mm;">
            <p><strong>{title}:</strong> Quick reference rules and operational procedures for standard operations.</p>
        </div>

        <div class="grid-main grid-1col">
            <div class="card">
                <div class="card-hd">
                    {SVG_ICONS['swords']}
                    <h2>Core Rules & Mechanics</h2>
                </div>
                <div class="card-body no-pad">
                    <table class="skill-table">
                        <thead>
                            <tr>
                                <th style="width: 30%;">Topic / Rule</th>
                                <th>Resolution & Effects</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="skill-section-hd">
                                <td colspan="2">Primary Operations</td>
                            </tr>
                            <tr>
                                <td>
                                    <div style="font-family: var(--font-title); font-weight: 700; color: var(--accent); text-transform: uppercase;">Standard Action</div>
                                    <div style="font-family: var(--font-mono); font-size: 5.5pt; color: var(--text-dim);">Cost: 1 AP · Simple Test</div>
                                </td>
                                <td class="rules-text">
                                    Roll dice pool equal to higher Attribute in pair. <strong>8+ is a Hit</strong>.
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="card">
                <div class="card-hd">
                    {SVG_ICONS['shield']}
                    <h2>Operational Reference</h2>
                </div>
                <div class="card-body rules-text">
                    <p>Specific situational notes and constraints go here. Formatted to preserve vertical space on A4.</p>
                </div>
            </div>
        </div>"""

    elif sheet_type == "character":
        body_content = f"""        <div class="grid-main grid-split-left">
            <!-- LEFT COLUMN: STATS & TRACKERS -->
            <div>
                <div class="card">
                    <div class="card-hd">
                        {SVG_ICONS['crosshairs']}
                        <h2>Attributes</h2>
                    </div>
                    <div class="card-body">
                        <div class="attr-grid">
                            <div class="attr-block">
                                <div class="attr-box">0</div>
                                <div class="attr-meta">
                                    <span class="attr-name">Strength</span>
                                    <span class="attr-code">PHYS / STR</span>
                                </div>
                            </div>
                            <div class="attr-block">
                                <div class="attr-box">0</div>
                                <div class="attr-meta">
                                    <span class="attr-name">Agility</span>
                                    <span class="attr-code">PHYS / AGI</span>
                                </div>
                            </div>
                            <div class="attr-block">
                                <div class="attr-box">0</div>
                                <div class="attr-meta">
                                    <span class="attr-name">Finesse</span>
                                    <span class="attr-code">PHYS / FIN</span>
                                </div>
                            </div>
                            <div class="attr-block">
                                <div class="attr-box">0</div>
                                <div class="attr-meta">
                                    <span class="attr-name">Knowledge</span>
                                    <span class="attr-code">MENT / KNO</span>
                                </div>
                            </div>
                            <div class="attr-block">
                                <div class="attr-box">0</div>
                                <div class="attr-meta">
                                    <span class="attr-name">Presence</span>
                                    <span class="attr-code">MENT / PRE</span>
                                </div>
                            </div>
                            <div class="attr-block">
                                <div class="attr-box">0</div>
                                <div class="attr-meta">
                                    <span class="attr-name">Instinct</span>
                                    <span class="attr-code">MENT / INS</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="card">
                    <div class="card-hd">
                        {SVG_ICONS['shield']}
                        <h2>Derived Stats & AP</h2>
                    </div>
                    <div class="card-body">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 2mm;">
                            <div>
                                <span style="font-family: var(--font-title); font-size: 6.5pt; text-transform: uppercase; color: var(--accent-dim);">Endurance:</span>
                                <strong style="color: var(--accent);">--</strong>
                            </div>
                            <div>
                                <span style="font-family: var(--font-title); font-size: 6.5pt; text-transform: uppercase; color: var(--accent-dim);">Willpower:</span>
                                <strong style="color: var(--accent);">--</strong>
                            </div>
                        </div>
                        <div style="display: flex; align-items: center; justify-content: space-between;">
                            <span style="font-family: var(--font-title); font-size: 6.5pt; text-transform: uppercase;">Action Points (3 Max):</span>
                            <div class="pip-row">
                                <div class="pip filled"></div>
                                <div class="pip filled"></div>
                                <div class="pip filled"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- RIGHT COLUMN: SKILLS & ABILITIES -->
            <div>
                <div class="card">
                    <div class="card-hd">
                        {SVG_ICONS['terminal']}
                        <h2>Abilities & Traits</h2>
                    </div>
                    <div class="card-body rules-text">
                        <p>Class abilities, modules, and special combat maneuvers go here.</p>
                    </div>
                </div>

                <div class="card">
                    <div class="card-hd">
                        {SVG_ICONS['gear']}
                        <h2>Gear & Equipment</h2>
                    </div>
                    <div class="card-body no-pad">
                        <table class="data-table">
                            <thead>
                                <tr>
                                    <th>Item</th>
                                    <th>Rating / Dice</th>
                                    <th>Tags / Notes</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Primary Weapon</td>
                                    <td>--</td>
                                    <td>Kinetic · Reliable</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>"""

    else:
        # Generic Handout / Sheet
        body_content = f"""        <div class="grid-main grid-1col">
            <div class="card">
                <div class="card-hd">
                    {SVG_ICONS['terminal']}
                    <h2>{title}</h2>
                </div>
                <div class="card-body rules-text">
                    <p>Enter printable handout text or structured reference data here. All standard Corsair design tokens and print-friendly styles are loaded.</p>
                </div>
            </div>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Corsair — {title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,300;0,400;0,600;0,700;0,900;1,400&family=Barlow:wght@300;400;600&family=Share+Tech+Mono&display=swap" rel="stylesheet" />
    <style>
{MASTER_CSS}
    </style>
</head>
<body>
    <div class="page">
        <!-- MASTHEAD -->
        <div class="masthead">
            <div class="mh-logo">
                {SVG_ICONS['corsair_logo']}
                <span class="logo-text">Corsair</span>
            </div>
            <div class="mh-title">
                <h1>{title}</h1>
                <div class="sub">{subtitle}</div>
            </div>
{meta_slot}
        </div>

        <!-- MAIN BODY CONTENT -->
{body_content}

        <!-- PAGE FOOTER -->
        <div class="page-foot">
            Corsair RPG · {title} · A4 System Document
        </div>
    </div>
</body>
</html>
"""
    return html

def main():
    parser = argparse.ArgumentParser(description="Generate Corsair A4 Printable HTML Sheets")
    parser.add_argument("--output", "-o", required=True, help="Destination .html file path")
    parser.add_argument("--title", "-t", default="System Reference", help="Sheet Title")
    parser.add_argument("--subtitle", "-s", default="Standard Reference Document", help="Sheet Subtitle")
    parser.add_argument("--type", choices=["reference", "character", "class", "crew", "handout"], default="reference", help="Sheet archetype")
    parser.add_argument("--meta", default="Designation", help="Label for right masthead box")
    parser.add_argument("--raw-css", action="store_true", help="Print raw CSS to stdout")

    args = parser.parse_args()

    if args.raw_css:
        print(MASTER_CSS)
        return

    out_path = Path(args.output).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    html_content = generate_html(
        title=args.title,
        subtitle=args.subtitle,
        sheet_type=args.type,
        meta_label=args.meta
    )

    out_path.write_text(html_content, encoding="utf-8")
    print(f"Successfully generated Corsair printable sheet at: {out_path}")

if __name__ == "__main__":
    main()
