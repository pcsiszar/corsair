---
name: corsair-printable-sheets
description: >-
  Guide and generator for creating print-ready A4 HTML sheets (handouts, rules quick references, character sheets, class sheets, and crew sheets) for Corsair. Use this skill FIRST whenever asked to create a new printable sheet or handout. Always ensures content fits neatly onto an A4 page.
---

# Corsair Printable Sheet Guide & Design System

This skill defines the workflow, CSS design system, component library, and automated generator for creating single-page **A4 print-ready HTML documents** (character sheets, class sheets, crew sheets, rules reference sheets, handouts, and GM aids) for Corsair.

---

## 1. Golden Rules for Sheet Creation

1. **Always Use the Generator Script First**:
   Always scaffold a new sheet by invoking the provided Python script to ensure all CSS custom properties, Google Fonts, print media rules, and layout structures are included without omissions:
   ```powershell
   python .agents/skills/corsair-printable-sheets/scripts/generate_sheet.py --output "rulebook/path/My_Sheet.html" --title "Sheet Title" --subtitle "Sheet Subtitle" --type reference
   ```
2. **Strict A4 Single-Page Fit**:
   Sheets are intended to be printed directly onto standard **A4 paper (210mm × 297mm)**.
   * Total content height MUST NOT exceed **297mm**.
   * Base font size should be calibrated between **7.5pt and 8.5pt**.
   * Line-height must stay compact (**1.2 to 1.35**).
   * Spacing and padding must use millimeter units (**1.5mm – 3.5mm**).
   * Keep paragraphs concise and avoid excessive vertical margins.
   * The page uses `display: flex; flex-direction: column;` with `.page-foot { margin-top: auto; }` to anchor the footer at the bottom of the 297mm box.
3. **Screen Dark Mode vs. Print Clean B&W**:
   * **Screen / PDF Viewing**: Uses Corsair's signature dark sci-fi palette (dark slate `#10131a`, gold accents `#c8a84b`, and subtle grid background).
   * **Physical Print**: Automatically switches via `@media print` to crisp, ink-friendly pure white backgrounds (`#ffffff`), dark borders (`#888888`), and black text/fills (`#000000`) for high-contrast legible printing.

---

## 2. Generator Script Reference

The generator script is located at:
[`.agents/skills/corsair-printable-sheets/scripts/generate_sheet.py`](file:///c:/Users/csisz/IdeaProjects/corsair/.agents/skills/corsair-printable-sheets/scripts/generate_sheet.py)

### CLI Arguments:
* `--output`, `-o` *(required)*: Target path for the output `.html` file.
* `--title`, `-t`: Main document title in the masthead (e.g., `"Combat Quick Reference"`).
* `--subtitle`, `-s`: Subtitle underneath the title (e.g., `"Actions, Range Bands & Tactical Maneuvers"`).
* `--type`: Archetype template:
  * `reference`: Tables, action definitions, rules text, callout boxes.
  * `character`: Attribute grid (STR, AGI, FIN, KNO, PRE, INS), derived stats, AP tracker, abilities, gear table.
  * `class`: Class-specific mechanics, modular abilities, power pools.
  * `crew`: Ship stations, system ratings, crew rosters.
  * `handout`: Clean layout for in-universe documents, lore briefings, mission logs.
* `--meta`: Text for the right-side masthead field (e.g., `"Player / Character"`, `"Designation"`, `"Security Clearance"`).
* `--raw-css`: Emits the complete reusable CSS code to stdout.

---

## 3. Reusable CSS Tokens & Design Architecture

### Color Variables (`:root`)
| Token | Dark Palette | Print Value | Description |
| :--- | :--- | :--- | :--- |
| `--black` | `#080a0c` | `#ffffff` | Background / Base dark |
| `--dark` | `#10131a` | `#ffffff` | Page container background |
| `--mid` | `#181c24` | `#ffffff` | Card headers, table headers, inner blocks |
| `--surface` | `#1d2130` | `#ffffff` | Card backgrounds |
| `--border` | `#2a3040` | `#888888` | Standard component borders |
| `--border-light` | `#3a4256` | `#cccccc` | Subtle division lines |
| `--accent` | `#c8a84b` | `#000000` | Gold primary brand accent |
| `--accent-dim` | `#7a6428` | `#333333` | Subdued gold borders & headers |
| `--accent-glow` | `rgba(200,168,75,0.15)` | `transparent` | Subtle glowing highlights |
| `--red` | `#a02828` | `#8b1a1a` | Alert / Danger / Damage accent |
| `--text` | `#ccc7ba` | `#000000` | Primary readable text |
| `--text-dim` | `#6a6458` | `#333333` | Secondary labels & codes |
| `--text-muted` | `#3e3c36` | `#666666` | Footers & de-emphasized metadata |
| `--stripe` | `rgba(200,168,75,0.03)` | `transparent` | Zebra striping for table rows |

### Typography
* **Headers & Labels**: `'Barlow Condensed', sans-serif` (Weights: `300`, `600`, `700`, `900`). Uppercase tracking (`letter-spacing: 0.1em - 0.35em`).
* **Body Text**: `'Barlow', sans-serif` (Weights: `300`, `400`, `600`).
* **Data / Codes / Systems**: `'Share Tech Mono', monospace`.

---

## 4. Standard Component Catalog

### 4.1. Masthead
Features the clipped chevron logo, title/subtitle, and field lines:
```html
<div class="masthead">
    <div class="mh-logo">
        <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" /><circle cx="12" cy="12" r="1.5" /></svg>
        <span class="logo-text">Corsair</span>
    </div>
    <div class="mh-title">
        <h1>Document Title</h1>
        <div class="sub">Document Subtitle</div>
    </div>
    <div class="mh-meta">
        <label>Designation</label>
        <div class="fl"></div>
    </div>
</div>
```

### 4.2. Card Container
Cards are the primary container for sections, grouping headings with content:
```html
<div class="card">
    <div class="card-hd">
        <svg viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
        <h2>Section Heading</h2>
    </div>
    <div class="card-body rules-text">
        <p>Content text goes here.</p>
    </div>
</div>
```

### 4.3. Attribute Box
Square rating indicator for Attributes and Ratings:
```html
<div class="attr-block">
    <div class="attr-box">5</div>
    <div class="attr-meta">
        <span class="attr-name">Strength</span>
        <span class="attr-code">PHYS / STR</span>
    </div>
</div>
```

### 4.4. Pips & Trackers
For Action Points, health, shields, or ammunition:
```html
<div class="pip-row">
    <div class="pip filled"></div>
    <div class="pip filled"></div>
    <div class="pip"></div>
</div>
```

### 4.5. Tables
High-density tables with zebra striping and subsection banner rows:
```html
<table class="skill-table">
    <thead>
        <tr>
            <th style="width: 30%;">Item / Rule</th>
            <th>Description & Resolution</th>
        </tr>
    </thead>
    <tbody>
        <tr class="skill-section-hd">
            <td colspan="2">Category Name</td>
        </tr>
        <tr>
            <td>
                <div style="font-family: var(--font-title); font-weight: 700; color: var(--accent); text-transform: uppercase;">Action Name</div>
                <div style="font-family: var(--font-mono); font-size: 5.5pt; color: var(--text-dim);">Cost: 1 AP</div>
            </td>
            <td class="rules-text">
                Rules explanation here.
            </td>
        </tr>
    </tbody>
</table>
```

### 4.6. Callouts & Badges
```html
<div class="rule-box">
    <strong>Important:</strong> Critical rule reminder or modifier condition.
</div>

<span class="badge accent">Action Effect</span>
<span class="badge red">Hazard</span>
```

---

## 5. Workflow for Creating a New Sheet

1. **Plan Content Layout & Space Budget**:
   * Determine key sections (Masthead, Tables, Stat Blocks, Rules text, Notes).
   * Decide on column structure (`grid-1col`, `grid-2col`, `grid-split-left`, etc.).
2. **Run Generator**:
   ```powershell
   python .agents/skills/corsair-printable-sheets/scripts/generate_sheet.py --output "rulebook/<category>/<Sheet_Name>.html" --title "<Title>" --subtitle "<Subtitle>" --type <reference|character|class|crew|handout>
   ```
3. **Fill Custom Content**:
   * Insert game mechanics, rules, and tables into the generated HTML.
   * Adhere strictly to the [`corsair-core-rules`](file:///c:/Users/csisz/IdeaProjects/corsair/.agents/skills/corsair-core-rules/SKILL.md) and [`corsair-writing-style`](file:///c:/Users/csisz/IdeaProjects/corsair/.agents/skills/corsair-writing-style/SKILL.md).
4. **Verify Single-Page Constraint**:
   * Check that total content fits inside the single A4 page (`210mm × 297mm`).
   * Trim text or adjust padding (`margin-bottom: 1.5mm - 2.5mm`) if content overflows.
