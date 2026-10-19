---
name: corsair-book-publishing
description: >-
  Architectural rules, token budget optimization, modular HTML chapter structure, CSS design system separation, markdown-to-HTML translation pipeline, and print assembly script for Corsair TTRPG book publishing. Use whenever creating, formatting, updating, or compiling multi-page rulebook HTML chapters or the master printable publication.
---

# Corsair Book Publishing & HTML Architecture Pipeline

This skill governs the translation of Corsair's markdown rulebook sources (`rulebook/**/*.md`, ~159,000 words across 66 files) into commercial-grade, print-ready HTML chapters and compiled PDF editions without blowing LLM context windows.

---

## 1. Golden Rules for Book Publishing

1. **Strict Rulebook Markdown Fidelity**:
   In accordance with repository canon rules, official publication HTML files must maintain **verbatim fidelity** to the markdown source documents (`rulebook/**/*.md`). Never rewrite mechanics, summarize away nuances, change die sizes, alter action costs, or drift from established lore. Layout adapts for aesthetics, but rules text remains exact.
2. **Never Author Monolithic Master Files for Editing**:
   The complete 159k-word rulebook produces ~350,000–500,000 tokens of formatted HTML (~2.5 MB). A single monolithic file will exceed or saturate context windows, cause browser DOM sluggishness, and make AI surgical edits brittle. 
   * **Always author and edit in Act/Chapter modules** (~10k–35k tokens each).
   * **Always assemble the master print book via automation script** right before PDF export.
3. **Externalize All CSS (Zero Inline Style Duplication)**:
   Never include inline `<style>` blocks in chapter HTML files. All typography, colors, table styling, HUD navigation, and print rules must be imported from shared stylesheets in `assets/css/` or `rulebook/assets/css/`. This eliminates ~4,000 tokens of duplicate boilerplate per chapter.
4. **Hardcover Print Geometry & Signatures**:
   Physical rulebooks are printed in **16-page signatures**. 
   * Standard density targets **~550 words per page** (text + ~20-25% tables/art), producing an exact **320-page hardcover** (20 signatures), matching industry benchmarks like D&D 5e PHB.
   * Deluxe illustrated density targets **~420 words per page** (~35% art), producing a **432-page book** (27 signatures).
5. **Zero Hyperlinks in Publication HTML**:
   Never include `<a>` tags or standalone document pointer sentences (e.g. *"For the standalone rules document, see..."*) in publication HTML files. The target output is print-ready PDF and physical print where external links are non-functional. Inline any necessary context directly.
6. **Multi-Column 70–75% Capacity Budget & 3rd-Column Prevention**:
   In fixed-height CSS multi-column layouts (`columns: 2; height: 297mm; overflow: hidden;`), content exceeding column 2 generates a hidden 3rd column that gets sliced vertically along the right page margin. To ensure zero overflow under Windows 125% DPI scaling and browser font expansions, budget content at **70–75% of nominal capacity** (~1,150–1,250px vertical content, or ~550–650 words). Never pair a large indivisible callout (`break-inside: avoid;`) with dense text that forces column balancing to overflow.
7. **Continuous Flow & Banner Frugality**:
   Subchapters must flow continuously across spreads. Do not force page breaks after each `###` header. Use visual banners only for major chapter openers (once per chapter) to avoid consuming vertical space.

---

## 2. Shared CSS Design System Architecture

All chapter files link to standard modular stylesheets:

```html
<link rel="stylesheet" href="../assets/css/corsair-variables.css">
<link rel="stylesheet" href="../assets/css/corsair-typography.css">
<link rel="stylesheet" href="../assets/css/corsair-components.css">
<link rel="stylesheet" href="../assets/css/corsair-layout.css">
<link rel="stylesheet" href="../assets/css/corsair-print.css">
```

### Stylesheet Responsibilities:
* `corsair-variables.css`: Design tokens, palette (`--amber-primary: #d97706;`, `--stage-bg: #0d1117;`, `--page-bg: #ffffff;`), and font families (`Barlow Condensed`, `Barlow`, `Rajdhani`, `Share Tech Mono`).
* `corsair-typography.css`: Heading hierarchies (`h1`–`h4`), drop caps, body text leading (1.35), paragraph indentations, and running headers.
* `corsair-components.css`: Data tables, stat blocks, callout containers (integrated with `corsair-graphic-assets`), tags, and status badges.
* `corsair-layout.css`: 2-column layout grid (`columns: 2; column-gap: 8mm;`), figure spanning (`column-span: all;`), HUD navigation bars.
* `corsair-print.css`: Strict `@media print` rules:
  ```css
  @media print {
      @page {
          size: A4 portrait; /* or 8.5in 11in */
          margin: 15mm 12mm 18mm 12mm;
          @bottom-center { content: counter(page); }
      }
      body { background: #ffffff !important; color: #000000 !important; }
      .book-nav, .hud-banner { display: none !important; }
      .chapter-title-spread { break-before: right; }
      .keep-together { break-inside: avoid; }
  }
  ```

---

## 3. The 12-Chapter Modular Map

Translate the 66 markdown files into 12 discrete chapter HTML files. This keeps every file small, manageable, and token-friendly:

| File Name | Word Count | Token Estimate | Source Markdown Files | Content Description |
| :--- | :---: | :---: | :--- | :--- |
| `00_Front_Matter.html` | ~5,250 w | ~10,000 tok | `Rulebook.md`, `character/Player_Characters.md` | Cover, Credits, Master TOC, What is Corsair, Gaming Principles |
| `01_Core_Mechanics.html` | ~7,025 w | ~14,000 tok | `core/*.md`, `combat/*.md` | Dice, Attributes, Tests, Gambits, Contests, Teamwork, Combat |
| `02_Character_Creation.html` | ~7,600 w | ~15,000 tok | `character/*.md` | Creation Steps, Traits Catalog, Advancement XP, Condition Tracks |
| `03_Classes.html` | ~19,950 w | ~36,000 tok | `classes/*.md` | Chassis Overview, Conduit, Hazard, Pilot, Vanguard, Weaver |
| `04_Armory_and_Gear.html` | ~11,180 w | ~22,000 tok | `equipment/*.md` | Load tiers, Melee, Firearms, Armor, Gear, Exotic Hardware |
| `05_Starships.html` | ~9,620 w | ~19,000 tok | `ships/*.md` | Ship Hulls, Space Combat, Naval Weapons, Modules, Hangar Bay |
| `06a_GM_Operations.html` | ~22,500 w | ~40,000 tok | `gm/Time*.md`, `gm/Downtime.md`, `gm/Stealth*.md`, `gm/Chases*.md` | Pacing, Downtime Gigs, Stealth, Pursuit Tracks |
| `06b_GM_Bestiary.html` | ~20,480 w | ~36,000 tok | `gm/Bestiary.md`, `gm/Social*.md`, `gm/Investigation*.md`, `gm/NPC*.md`, `gm/Mission*.md` | 18 Bestiary Threat Cards, Social Negotiation, Clue Nets, Generator |
| `07_World_of_the_Sphere.html` | ~31,385 w | ~52,000 tok | `lore/Introduction.md`, `lore/locations/*.md`, `lore/factions/*.md`, `lore/Timeline.md` | Sphere Architecture, Worlds, 5 Sovereign Factions, 518 AA Timeline |
| `08_Forbidden_Archives.html` | ~6,613 w | ~12,000 tok | `lore/forbidden_archives/*.md` | Classified Lore: Precursors, Singularity, Monoliths, Secret Timeline |
| `09_Fiction_Anthology.html` | ~17,390 w | ~28,000 tok | `stories/*.md` | 4 Novellas: *Space Tourism*, *Post-War*, *Great Tithe*, *27th Hour* |
| `10_Appendices_and_Index.html` | ~4,000 w | ~8,000 tok | Reference sheets, Index | Effects Table, Quick Combat Flow, Index, Blank Sheets |

---

## 4. Markdown-to-HTML Component Patterns

When converting markdown elements into HTML, use standard semantic structures:

### 4.1. Rules Tables
```html
<div class="table-container keep-together">
    <div class="table-header">Firearms — Heavy Ballistic Ordnance</div>
    <table class="rules-table">
        <thead>
            <tr>
                <th>Weapon</th>
                <th>AP</th>
                <th>Range</th>
                <th>Damage</th>
                <th>Load</th>
                <th>Traits & Effects</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="bold">Rotary Cannon</td>
                <td>3</td>
                <td>Medium</td>
                <td>2d8 Piercing</td>
                <td>Heavy</td>
                <td>Automatic, Cumbersome, Shred 2</td>
            </tr>
        </tbody>
    </table>
</div>
```

### 4.2. Callouts & Narrative Quotes
Integrate with the callout containers generated via [`corsair-graphic-assets`](file:///c:/Users/csisz/IdeaProjects/corsair/.agents/skills/corsair-graphic-assets/SKILL.md):
```html
<div class="callout callout-amber keep-together">
    <div class="callout-title">The Shepherd's Invariant</div>
    <p>Every jump creates a fracture; the question is not whether the hull survives the displacement, but whether the memory of where you were survives the arrival.</p>
</div>
```

### 4.3. Gameplay Examples
All narrative gameplay examples and tactical walkthroughs must use `.example-box` with an `.example-title` header (Avionics Cyan accent bar):
```html
<div class="example-box keep-together">
    <div class="example-title">Contest Example</div>
    <p>Returning to our gunslinger Jax: suppose Jax attacks a security drone...</p>
</div>
```
Multi-step combat walkthroughs (such as *Combined Mechanics in Action*) must be fully enclosed inside `.example-box` across all steps rather than styling only the opening paragraph.

---

## 5. Master Book Assembler Pipeline

The master compilation script is located at:
[`.agents/skills/corsair-book-publishing/scripts/assemble_book.py`](file:///c:/Users/csisz/IdeaProjects/corsair/.agents/skills/corsair-book-publishing/scripts/assemble_book.py)

### Automated Workflow:
1. Iterates through the 12 chapter files in sequence.
2. Strips `<DOCTYPE>`, `<html>`, `<head>`, and `<nav class="book-nav">` tags.
3. Injects each chapter body into a `<section class="book-chapter" id="...">` wrapper.
4. Generates a compiled `dist/Corsair_Core_Rulebook_Master.html` ready for browser viewing or headless Chromium PDF generation:
   ```powershell
   python .agents/skills/corsair-book-publishing/scripts/assemble_book.py
   ```
5. To export individual chapters or the master compilation to PDF via the automated export script:
   ```powershell
   python .agents/skills/corsair-book-publishing/scripts/export_pdf.py --input html/00_Front_Matter.html --output html/00_Front_Matter.pdf
   ```

---

## 6. HTML to PDF Conversion & Print Engine Invariants

### 6.1. Headless Chromium vs. WeasyPrint
* **Avoid WeasyPrint on Windows**: WeasyPrint requires native C-libraries (`libgobject-2.0-0.dll`, Pango, and Cairo). On standard Windows Python installations without a manually configured GTK3 runtime, WeasyPrint fails with an `OSError`.
* **Standardize on Headless Chromium**: `chrome --headless=new` or `msedge --headless=new` runs the exact same rendering engine as the browser. It natively supports web fonts (`Orbitron`, `Barlow Condensed`, `Share Tech Mono`), CSS Grid (`.two-column-grid`), CSS multi-column balancing (`column-fill: balance;`), SVG masks, and background images with 100% fidelity.

### 6.2. Strict Print Geometry to Prevent Page Doubling
When generating multi-page PDFs where HTML pages have fixed dimensions (e.g. `210mm × 297mm`), `@page` margins MUST be set to `0`:
```css
@page {
    size: A4 portrait;
    margin: 0;
}
```
**Why this invariant matters:**
If `@page` defines margins (such as `margin: 14mm 12mm 16mm 12mm;`) while `.book-page` has a fixed height of `297mm`, the printable area shrinks to `267mm`. The browser prints `267mm` on page 1, spills the remaining `30mm` onto page 2, and then triggers `break-after: page;`—**doubling every single page into two physical sheets**.

With `@page { margin: 0; }`, the print viewport matches the physical A4 sheet exactly:
```css
.book-page {
    width: 210mm !important;
    height: 297mm !important;
    max-width: 210mm !important;
    min-height: 297mm !important;
    max-height: 297mm !important;
    box-sizing: border-box !important;
    margin: 0 !important;
    padding: 16mm 14mm 16mm 14mm !important;
    break-after: page !important;
    page-break-after: always !important;
    overflow: hidden !important;
}

.cover-page {
    padding: 0 !important;
    background-color: #061124 !important;
    background-image: url('../backgrounds/bg_astrometric_lattice_blue.jpg') !important;
}
```

### 6.3. Automated Page Validation
The `export_pdf.py` script automatically runs `pypdf` after printing to verify:
1. Exact total page count matching chapter spreads.
2. Physical media box dimensions matching ISO A4 (`209.89mm × 297.01mm`).

### 6.4. Multi-Column Containment & Overflow Verification
In Chromium multi-column layouts (`.two-columns`), any overflow in Column 2 causes the browser to create Column 3 off-screen, creating sliced character fragments along the right margin.

**Containment Invariants:**
1. **DPI Headroom:** Windows 125% DPI rendering increases line heights by ~10–12%. Always leave at least 25% height buffer on every page.
2. **Break-Inside Balancing:** Avoid putting multiple `.keep-together` (`break-inside: avoid;`) boxes on the same page. If an indivisible box cannot fit in the remainder of Column 1, column balancing pushes it to Column 2, easily overfilling Column 2 into Column 3.
3. **Automated Verification:** Before finalizing any chapter HTML, test programmatically or via browser subagent that:
   ```javascript
   document.querySelectorAll('.book-page').forEach((page, i) => {
       const body = page.querySelector('.page-body');
       if (body && body.scrollWidth > body.clientWidth) {
           console.error(`Page ${i + 1} (${page.id}) has horizontal overflow / Column 3!`);
       }
   });
   ```

### 6.5. Fiction & Interlude Layout Architecture (Single-Column Standard)
Unlike rules chapters, fiction novellas and narrative interludes must **never use multi-column grids** (`columns: 2`). In dialogue-heavy text, browser column balancing creates erratic vertical splits and massive empty voids in column bottoms.

* **Single-Column Fiction Container**:
  Use `.fiction-page-body` with strict geometry:
  - Width: `100%; max-width: 172mm; margin: 0 auto;`
  - Typography: `font-size: 9.2pt; line-height: 1.40;`
  - Paragraph spacing: `margin-bottom: 2.0mm;`
* **Zero Unsolicited Content Padding**:
  Never invent municipal dossiers, appendices, or lore sidebars to pad out an even page count. Let the canonical story text define the page budget.

### 6.6. Vertical Line-Unit Budgeting (Preventing Page Voids & Spills)
Do not budget page capacity purely by raw word count. A single dialogue line (`"No," he said.`) takes up an entire visual line (~4.5mm) plus paragraph margin (~2.0mm) = **6.5mm for 3 words**, whereas a dense prose paragraph packs 15–20 words into the same vertical height.

**Visual Line Formula for A4 (297mm height, 245mm printable window):**
1. **Target Page Budget**:
   - **Opener Page** (with title banner & drop cap): **32–36 visual lines**.
   - **Standard Body Page**: **38–42 visual lines**.
   - *Result*: Guarantees a natural, professional 20–25mm breathing margin above the running footer without empty voids (>40mm) or accidental 1-line page overflows.
2. **Visual Line Equivalents**:
   - 1 full line of prose (~95–100 characters): `1.0 line unit`.
   - Dialogue paragraph (1–2 sentences): `1.5 line units` (line + paragraph gap).
   - Paragraph break (`margin-bottom: 2.0mm`): `+0.5 line unit`.
   - Chapter / Interlude Banner: `~8–10 line units`.
3. **Automated Verification**:
   Inspect the compiled PDF with `pypdf` / `export_pdf.py` immediately after rendering. If `page_count` exceeds target by 1, reduce by 1–2 paragraphs to prevent trailing orphan spills.



