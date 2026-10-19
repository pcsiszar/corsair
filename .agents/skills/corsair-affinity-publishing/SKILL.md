---
name: corsair-affinity-publishing
description: >-
  Standard operating procedures, DTP layout rules, Book architecture, and native Affinity MCP
  scripting recipes for publishing Corsair TTRPG books in Affinity Publisher. Use whenever
  generating, laying out, automating, styling, or rendering native .afpub and .afbook publications.
---

# Corsair Affinity Publishing & MCP Automation Pipeline

This skill governs the production of commercial-grade, print-ready TTRPG books, chapters, and spreads for Corsair using **Affinity Publisher (v3.2+)**, its embedded **Model Context Protocol (MCP)** server, and JavaScript DOM scripting.

---

## 1. Golden Rules & Invariants

1. **Strict Rulebook Markdown Fidelity**:
   In accordance with repository canon rules, all content flowing into Affinity Publisher documents must maintain **verbatim fidelity** to the markdown source documents (`rulebook/**/*.md`). Never rewrite mechanics, summarize away nuances, alter die sizes, change action costs, or drift from established 518 AA lore. Layout and styling adapt for high-end tabletop aesthetics, but the technical prose remains exact.

2. **Modular Book Architecture (`.afbook`) vs. Monolithic File Trap**:
   **Never build a 200–300+ page TTRPG rulebook in a single `.afpub` file.**
   - Monolithic `.afpub` files degrade UI responsiveness, multiply save times, increase risk of project-wide file corruption, and complicate version control.
   - **The Chapter Pattern**: Author individual chapters as discrete `.afpub` files (e.g., `00_Front_Matter.afpub`, `01_Core_Mechanics.afpub`, `02_Character_Creation.afpub`, `03_Classes.afpub`).
   - **Master Container**: Assemble all chapter files inside an Affinity Book container (`.afbook`).
   - **Style Source Synchronization**: Designate `01_Core_Mechanics.afpub` (or `_Style_Source.afpub`) as the **Style Source** in the Book panel. Pushing style updates from this source harmonizes Text Styles, swatches, and Preflight Profiles across all linked chapters in seconds.
   - **Global Harvest**: The `.afbook` container automatically generates unified, cross-document Tables of Contents, Index markers, and sequential page numbers.

3. **The Mandatory MCP Preamble Handshake**:
   In every Affinity MCP session, you **MUST** call `read_sdk_documentation_topic` with `filename: "preamble"` before executing scripts or reading other SDK topics. The Affinity MCP server strictly rejects subsequent tool calls if this initial handshake is skipped.

4. **Desktop Sandbox & Asset Staging Pattern**:
   Affinity scripts run within an application sandbox that can only access files in the user's Desktop directory (`Application.userDesktopPath`).
   - **Staging Inbound**: Orchestration scripts (Python) must copy art assets, logos, and raw data from the repository workspace to `~/Desktop/corsair_generated_assets/` before launching the Affinity JS script.
   - **Staging Outbound**: The Affinity script saves the document to `Application.userDesktopPath + '/<filename>.afpub'`. The orchestration script immediately copies the completed `.afpub` and preview renders back to the repository (e.g., `affinity/`).

5. **2-Column Baseline Grid & Continuous Flow**:
   - TTRPG rulebooks rely on 2-column spreads for readability. Always activate and snap body text to the **Document Baseline Grid** (e.g., 13 pt grid for 10.5 pt text with 13 pt leading). This keeps horizontal lines aligned across columns and spreads even when broken by subheadings or tables.
   - Never force text into isolated disconnected frames. Link frames using `DocumentCommand.createLinkTextFrame(col1, col2)` so copy flows naturally.

6. **Autonomous Visual QA Loop**:
   Never assume a scripted spread laid out cleanly. Always capture the document's `sessionUuid` from `execute_script` and immediately call `render_spread` for every generated spread. Inspect the exported base64 JPEG to verify column balance, ensure no overset text (red eye/badge), check contrast, and validate gutter clearance.

7. **Spread-Wide Column Balancing & Two-Column Density**:
   - Never allow one column to end halfway down a page while adjacent columns or facing pages are congested or overset.
   - Calculate vertical content requirements across the full facing spread. Sequence subchapters logically across Column 1 and Column 2 of both pages so that both columns reach comfortably down toward the bottom margin.
   - When placing full-width callout cards (e.g., Elevator Pitch), calculate total text line heights plus padding to ensure the bounding box never overflows or collides with the column frames below it.

---

## 2. Corsair Print Geometry & Technical Grid

All Corsair rulebooks target standard **A4 Facing Spreads** at **300 DPI** with a **3 mm bleed**.

### Mathematical Coordinate Invariants (300 DPI)

```javascript
// Document Canvas (A4 at 300 DPI)
const PW = 2480.31; // Single page width in points/pixels
const PH = 3507.87; // Single page height in points/pixels

// Margins (Asymmetric for Hardcover Binding Creep)
const M_T      = 160.0; // Top / Head Margin
const M_B      = 180.0; // Bottom / Foot Margin
const M_OUTER  = 160.0; // Outer Margin (Left on Left page, Right on Right page)
const M_GUTTER = 190.0; // Spine Gutter Margin (Right on Left page, Left on Right page)

// Column Grid
const COL_W     = 1030.0; // Standard column width
const COL_GAP   = 70.0;   // Inter-column gap
const CONTENT_W = COL_W * 2 + COL_GAP; // 2130.0 pt printable width

// Left Page Coordinates (Spread Left)
const L_COL1_X = M_OUTER;                         // 160.0
const L_COL2_X = M_OUTER + COL_W + COL_GAP;       // 1260.0

// Right Page Coordinates (Spread Right: Offset by PW)
const R_COL1_X = PW + M_GUTTER;                   // 2670.31
const R_COL2_X = PW + M_GUTTER + COL_W + COL_GAP; // 3770.31
```

### 2.1. Preamble & Author Note Layout
Author notes, prefaces, and preambles (e.g., `Acknowledgments.md`) should use an elegant, centered **single-column layout** (`w = 1750 pt` on 2480 pt A4, centered at `x = 365 pt`) rather than two columns. Personal acknowledgments, special thanks, and legal licensing must flow continuously within this single story, separated by clean headings or subtle rules rather than disjointed colored alert boxes.

---

## 3. The Hard Sci-Fi Visual Design System

Affinity Publisher scripts must instantiate the standardized Corsair visual design tokens:

### 3.1. Palette Tokens
```javascript
const { RGBA8 } = require('/colours.js');

const colDarkVoid       = RGBA8(10, 14, 23);     // #0A0E17 Deep space void
const colNavyCard       = RGBA8(15, 23, 42);     // #0F172A Tactical card background
const colPaperBg        = RGBA8(248, 250, 252);  // #F8FAFC Crisp reading paper
const colBodyText       = RGBA8(15, 23, 42);     // #0F172A Deep charcoal body text
const colAmber          = RGBA8(245, 158, 11);   // #F59E0B Caution / thruster amber
const colAmberDark      = RGBA8(217, 119, 6);    // #D97706 Deep amber / headers
const colAmberBox       = RGBA8(254, 249, 235);  // #FEF9EB Warm amber callout background
const colAmberBoxBorder = RGBA8(245, 158, 11);   // #F59E0B Amber callout border
const colCyan           = RGBA8(6, 182, 212);    // #06B6D4 Sensor cyan
const colCyanDark       = RGBA8(2, 132, 199);    // #0284C7 Deep beacon blue
const colCyanBox        = RGBA8(240, 249, 255);  // #F0F9FF Cool cyan callout background
const colCyanBoxBorder  = RGBA8(56, 189, 248);   // #38BDF8 Cyan callout border
const colSlate          = RGBA8(100, 116, 139);  // #64748B Secondary metadata
const colSlateDark      = RGBA8(51, 65, 85);     // #334155 Borders / structural dividers
const colSlateLight     = RGBA8(226, 232, 240);  // #E2E8F0 Hairlines & grids
const colWhite          = RGBA8(255, 255, 255);  // #FFFFFF Pure white
```

### 3.2. Typography Fonts & Roles
```javascript
const { FontFamily } = require('/fonts.js');

const bahnFamily    = FontFamily.all.find(f => f.name === 'Bahnschrift');
const segoeFamily   = FontFamily.all.find(f => f.name === 'Segoe UI');
const consolasFam   = FontFamily.all.find(f => f.name === 'Consolas');

const fontDisplay    = bahnFamily  ? bahnFamily.getFont(14)  : null; // Bahnschrift Bold
const fontHeading    = bahnFamily  ? bahnFamily.getFont(12)  : null; // Bahnschrift Bold Condensed
const fontSubHeading = bahnFamily  ? bahnFamily.getFont(9)   : null; // Bahnschrift SemiBold Condensed
const fontLabel      = bahnFamily  ? bahnFamily.getFont(6)   : null; // Bahnschrift Condensed
const fontMono       = consolasFam ? consolasFam.getFont(1)  : null; // Consolas Bold / Tech Mono
const fontBody       = segoeFamily ? segoeFamily.getFont(4)  : null; // Segoe UI Regular
const fontBodyBold   = segoeFamily ? segoeFamily.getFont(8)  : null; // Segoe UI Bold
const fontBodyItalic = segoeFamily ? segoeFamily.getFont(5)  : null; // Segoe UI Italic
```

### 3.3. Heading Scale & Spacing Invariants (300 DPI / 3508 pt Canvas)
On a 3508 pt canvas, body text is 28–30 pt. Subheadings that use default or small `spaceBefore` (e.g. 30–50 pt) visually merge into preceding paragraphs. Always adhere to these scale and spacing invariants:

- **H1 (Chapter Openers)**: 62 pt Bahnschrift Bold Condensed (`colNavyCard`), 2 pt horizontal accent rule (`colAmber`) below.
- **H2 (Major Sections)**: 56–58 pt Bahnschrift Bold Condensed (`colNavyCard`), `spaceBefore: 80–90 pt`, `spaceAfter: 18 pt`, `isSumBeforeAndAfterSpace: true`.
- **H3 (Subchapters & Topics)**: 44–46 pt Bahnschrift Bold Condensed (`colAmberDark` or `colNavyCard`), `spaceBefore: 70–80 pt`, `spaceAfter: 16 pt`, `isSumBeforeAndAfterSpace: true`.
- **H3 at Column Top**: When an H3 starts at the very top of a column, set `spaceBefore: 0 pt` (`paH3Top`).
- **Body Text**: 28–30 pt Segoe UI Regular (`colBodyText`), `relativeLeading: 1.44–1.46`, `spaceAfter: 16–18 pt`.

---

## 4. Master Spread Architecture

Affinity Publisher documents must establish standard master spreads using `NodeChildType.MasterSpread`:

1. **A-Master (Standard Rules Spread)**:
   - **Running Header (Verso / Left Page)**: Clean Book Title (e.g., `CORSAIR ROLEPLAYING GAME` or `CORSAIR`) in 20 pt Bahnschrift Condensed (`colSlate`), underscored by a `colSlateLight` hairline. Never insert fake telemetry or slash tags (e.g., `// SYSTEM SPECIFICATIONS // 518 AA`).
   - **Running Header (Recto / Right Page)**: Clean Chapter Title (e.g., `WELCOME TO CORSAIR` or `CORE RULES ENGINE`) in 20 pt Bahnschrift Condensed (`colSlate`), underscored by a `colSlateLight` hairline.
   - **Running Footers**: Thin hairline above footers, clean folio / page number (`colAmberDark` or `colSlate`) on outer margins. Omit arbitrary volume/chapter slash tags.
2. **B-Master (Chapter Opener)**:
   - Header suppressed; full-width chapter title banner, introductory narrative deck, and bottom pagination.
3. **C-Master (Full Bleed Artwork)**:
   - Blank master without headers, footers, or margins.

```javascript
const { NodeChildrenOnly, NodeChildType } = require('/nodes.js');
const masterSpreads = Array.from(new NodeChildrenOnly(doc.rootNode.handle, NodeChildType.MasterSpread, false));
const ms = masterSpreads[0]; // A-Master
```

---

## 5. Scripting Component Recipes

### 5.1. Rectangular Callout Box with Accent Tab
```javascript
const { Shape, ShapeType, ShapeCornerType } = require('/shapes.js');
const { ShapeNodeDefinition } = require('/nodes.js');
const { Rectangle } = require('/geometry.js');
const { FillDescriptor } = require('/fills.js');

function addCalloutBox(target, x, y, w, h, bgCol, borderCol, tabCol) {
    // 1. Strictly rectangular base frame (No chamfers or octagons)
    const shape = Shape.create(ShapeType.Rectangle);
    shape.topLeft.cornerType = ShapeCornerType.None;
    shape.topRight.cornerType = ShapeCornerType.None;
    shape.bottomLeft.cornerType = ShapeCornerType.None;
    shape.bottomRight.cornerType = ShapeCornerType.None;
    const rect = new Rectangle(x, y, w, h);
    const fill = FillDescriptor.createSolid(bgCol);
    const stroke = borderCol ? FillDescriptor.createSolid(borderCol) : null;
    doc.addNode(ShapeNodeDefinition.create(shape, rect, fill, stroke, borderCol ? 1.5 : null, null), target);

    // 2. Solid vertical left accent tab
    if (tabCol) {
        const tabShape = Shape.create(ShapeType.Rectangle);
        tabShape.topLeft.cornerType = ShapeCornerType.None;
        tabShape.topRight.cornerType = ShapeCornerType.None;
        tabShape.bottomLeft.cornerType = ShapeCornerType.None;
        tabShape.bottomRight.cornerType = ShapeCornerType.None;
        doc.addNode(ShapeNodeDefinition.create(tabShape, new Rectangle(x, y, 10, h), FillDescriptor.createSolid(tabCol)), target);
    }
}
```

### 5.2. Rectangular Header Plate & Dossier Block
```javascript
function addDossierBlock(target, x, y, w, h, bgCol = colNavyCard, borderCol = colCyanDark, accentTabCol = colAmber) {
    const shape = Shape.create(ShapeType.Rectangle);
    shape.topLeft.cornerType = ShapeCornerType.None;
    shape.topRight.cornerType = ShapeCornerType.None;
    shape.bottomLeft.cornerType = ShapeCornerType.None;
    shape.bottomRight.cornerType = ShapeCornerType.None;
    const rect = new Rectangle(x, y, w, h);
    doc.addNode(ShapeNodeDefinition.create(shape, rect, FillDescriptor.createSolid(bgCol), FillDescriptor.createSolid(borderCol), 1.5, null), target);

    if (accentTabCol) {
        const tab = Shape.create(ShapeType.Rectangle);
        tab.topLeft.cornerType = ShapeCornerType.None;
        tab.topRight.cornerType = ShapeCornerType.None;
        tab.bottomLeft.cornerType = ShapeCornerType.None;
        tab.bottomRight.cornerType = ShapeCornerType.None;
        doc.addNode(ShapeNodeDefinition.create(tab, new Rectangle(x, y, 12, h), FillDescriptor.createSolid(accentTabCol)), target);
    }
}
```

### 5.3. Linked Two-Column Text Frames
```javascript
const { FrameTextNodeDefinition } = require('/nodes.js');
const { StoryBuilder } = require('/storybuilder.js');
const { DocumentCommand } = require('/commands.js');

// 1. Build Story with Content
const sb = StoryBuilder.create();
sb.setToFrameTextDefaultStyle(doc.dpi, doc.format);
// ... populate sb with headings, paragraphs, and styles ...

// 2. Create Column 1 Text Frame with the Story
const defCol1 = FrameTextNodeDefinition.createFromStoryBuilder({ x: L_COL1_X, y: 320, width: COL_W, height: 2800 }, sb);
doc.addNode(defCol1, targetSpread);
const col1Node = targetSpread.lastChild;

// 3. Create Column 2 Empty Text Frame
const sbCol2 = StoryBuilder.create();
sbCol2.setToFrameTextDefaultStyle(doc.dpi, doc.format);
const defCol2 = FrameTextNodeDefinition.createFromStoryBuilder({ x: L_COL2_X, y: 320, width: COL_W, height: 2800 }, sbCol2);
doc.addNode(defCol2, targetSpread);
const col2Node = targetSpread.lastChild;

// 4. Thread Text Flow from Column 1 into Column 2
doc.executeCommand(DocumentCommand.createLinkTextFrame(col1Node, col2Node));
```

### 5.4. Native Table Creation (`TableTextNodeDefinition`)
```javascript
const { TableTextNodeDefinition } = require('/nodes.js');
const { HardBreakType } = require('/story.js');
const { Selection, TextSelection } = require('/selections.js');

function createTable(targetSpread, x, y, width, height, numCols, numRows, dataRows) {
    const box = { x, y, width, height };
    const def = TableTextNodeDefinition.create(box, { width: numCols, height: numRows });
    doc.addNode(def, targetSpread);
    const table = targetSpread.lastChild;

    // Populate cells via TableCell break boundaries
    // ... insert dataRows matching row/column cell order ...
}
```

---

## 6. Python MCP Dispatcher & QA Verification Template

To execute scripts and perform automated visual QA from Python, use this proven orchestration template:

```python
import urllib.request, json, threading, queue, os, shutil, base64, re

def build_affinity_publication():
    # 1. Stage Assets to Desktop Sandbox
    desktop_staging = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'corsair_staging')
    os.makedirs(desktop_staging, exist_ok=True)
    # ... copy art / bitmaps into desktop_staging ...

    # 2. Establish SSE Connection
    q = queue.Queue()
    url = 'http://[::1]:6767/sse'
    req = urllib.request.Request(url, headers={'Accept': 'text/event-stream'})

    def read_sse():
        with urllib.request.urlopen(req) as resp:
            for line in resp:
                s = line.decode('utf-8').strip()
                if s.startswith('data:'):
                    try: q.put(json.loads(s[5:].strip()))
                    except: q.put(s[5:].strip())

    threading.Thread(target=read_sse, daemon=True).start()
    session_endpoint = q.get(timeout=5)
    while not isinstance(session_endpoint, str) or not session_endpoint.startswith('/'):
        session_endpoint = q.get(timeout=5)
    post_url = 'http://localhost:6767' + session_endpoint

    def send_rpc(msg):
        data = json.dumps(msg).encode('utf-8')
        r = urllib.request.Request(post_url, data=data, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(r): pass

    def wait_for(req_id, timeout=60):
        while True:
            item = q.get(timeout=timeout)
            if isinstance(item, dict) and item.get('id') == req_id:
                return item

    # 3. Mandatory Handshake
    send_rpc({'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {'protocolVersion': '2024-11-05', 'capabilities': {}, 'clientInfo': {'name': 'Antigravity', 'version': '1.0.0'}}})
    wait_for(1)
    send_rpc({'jsonrpc': '2.0', 'method': 'notifications/initialized'})
    
    # Invariant: Read preamble
    send_rpc({'jsonrpc': '2.0', 'id': 2, 'method': 'tools/call', 'params': {'name': 'read_sdk_documentation_topic', 'arguments': {'filename': 'preamble'}}})
    wait_for(2)

    # 4. Execute JavaScript DOM Layout Script
    js_code = """
    // ... Javascript DOM script ...
    console.log('SESSION_UUID=' + doc.sessionUuid);
    """
    send_rpc({'jsonrpc': '2.0', 'id': 3, 'method': 'tools/call', 'params': {'name': 'execute_script', 'arguments': {'script': js_code}}})
    res = wait_for(3, timeout=90)
    output = res.get('result', {}).get('content', [{}])[0].get('text', '')

    # 5. Extract Session UUID & Copy Generated Document
    m = re.search(r'SESSION_UUID=([A-Fa-f0-9\-]+)', output)
    doc_uuid = m.group(1) if m else None

    # Mirror desktop afpub back to repository
    desktop_afpub = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'Corsair_Core_Rulebook.afpub')
    dest_afpub = r"c:\Users\csisz\IdeaProjects\corsair\affinity\Corsair_Core_Rulebook.afpub"
    if os.path.exists(desktop_afpub):
        shutil.copy2(desktop_afpub, dest_afpub)

    # 6. Autonomous Visual QA Loop: Render Every Spread
    if doc_uuid:
        for spread_idx in range(4): # Loop over spreads
            send_rpc({'jsonrpc': '2.0', 'id': 10 + spread_idx, 'method': 'tools/call', 'params': {'name': 'render_spread', 'arguments': {'document_session_uuid': doc_uuid, 'spread_index': spread_idx}}})
            sp_res = wait_for(10 + spread_idx, timeout=30)
            c_list = sp_res.get('result', {}).get('content', [])
            if c_list and c_list[0].get('data'):
                img_data = base64.b64decode(c_list[0]['data'])
                preview_path = f"affinity/spread_{spread_idx}_preview.jpg"
                with open(preview_path, 'wb') as f:
                    f.write(img_data)
                print(f"Spread {spread_idx} rendered to {preview_path} for visual inspection.")

if __name__ == '__main__':
    build_affinity_publication()
```

---

## 7. Spread Inspection & Preflight Checklist

When evaluating rendered spread previews (`spread_*_preview.jpg`):

- [ ] **No Overset Text**: Confirm that no text frame terminates with a red overset marker or missing copy.
- [ ] **Baseline Grid Alignment**: Verify horizontal alignment of body text lines across columns.
- [ ] **Gutter Creep Safety**: Confirm that all inner column text remains at least 190 pt (16 mm) away from the spine center fold.
- [ ] **Heading Keep Rules**: Ensure no headers sit alone at the bottom of a column without at least 2 lines of body text below them.
- [ ] **Rectangular & Accent Alignment**: Confirm clean rectangular geometry (`ShapeCornerType.None`) and vertical color accent tabs align flush with text frame boundaries without chamfers or octagons.
- [ ] **Contrast Verification**: Ensure dark text (`colNavyCard`) on light pages (`colPaperBg`) and light text (`colAmber`/`colCyan`) on dark cards have high contrast for readability.
