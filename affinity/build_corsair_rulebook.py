import urllib.request, json, threading, queue, os, shutil, sys

def run_corsair_design_pipeline():
    print("=== Step 1: Staging Visual Assets to Desktop ===")
    desktop_assets = r"C:\Users\csisz\Desktop\corsair_generated_assets"
    os.makedirs(desktop_assets, exist_ok=True)
    
    brain_dir = r"C:\Users\csisz\.gemini\antigravity-ide\brain\c99daf52-339a-40f8-8971-932b97af1b76"
    
    cover_art_src = os.path.join(brain_dir, "corsair_ship_void_1792321839886.jpg")
    emblem_src = os.path.join(brain_dir, "corsair_tactical_patch_1792321861339.jpg")
    
    cover_art_dest = os.path.join(desktop_assets, "cover_starship.jpg")
    emblem_dest = os.path.join(desktop_assets, "tactical_emblem.jpg")
    
    if os.path.exists(cover_art_src):
        shutil.copy2(cover_art_src, cover_art_dest)
        print(f"  [OK] Staged cover art: {cover_art_dest} ({os.path.getsize(cover_art_dest)} bytes)")
    else:
        print(f"  [ERROR] Cover art not found at: {cover_art_src}")
        return

    if os.path.exists(emblem_src):
        shutil.copy2(emblem_src, emblem_dest)
        print(f"  [OK] Staged tactical emblem: {emblem_dest} ({os.path.getsize(emblem_dest)} bytes)")
    else:
        print(f"  [ERROR] Emblem not found at: {emblem_src}")
        return

    # Stage background image from assets/backgrounds
    repo_dir = r"c:\Users\csisz\IdeaProjects\corsair"
    bg_gravity_src = os.path.join(repo_dir, "assets", "backgrounds", "bg_gravity_contours.jpg")
    bg_gravity_dest = os.path.join(desktop_assets, "bg_gravity_contours.jpg")
    if os.path.exists(bg_gravity_src):
        shutil.copy2(bg_gravity_src, bg_gravity_dest)
        print(f"  [OK] Staged gravity contours background: {bg_gravity_dest} ({os.path.getsize(bg_gravity_dest)} bytes)")
    else:
        print(f"  [ERROR] Background not found at: {bg_gravity_src}")
        return

    desktop_afpub = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'Corsair_Core_Rulebook.afpub')
    if os.path.exists(desktop_afpub):
        try: os.remove(desktop_afpub)
        except: pass

    print("\n=== Step 2: Connecting to Affinity MCP Server ===")
    q = queue.Queue()
    url = 'http://[::1]:6767/sse'
    req = urllib.request.Request(url, headers={'Accept': 'text/event-stream'})

    def read_sse():
        with urllib.request.urlopen(req) as response:
            for line in response:
                line_str = line.decode('utf-8').strip()
                if line_str.startswith('data:'):
                    try:
                        q.put(json.loads(line_str[5:].strip()))
                    except:
                        q.put(line_str[5:].strip())

    threading.Thread(target=read_sse, daemon=True).start()
    session_endpoint = q.get(timeout=5)
    while not isinstance(session_endpoint, str) or not session_endpoint.startswith('/'):
        session_endpoint = q.get(timeout=5)
    post_url = 'http://localhost:6767' + session_endpoint
    print(f"  Connected to SSE session: {session_endpoint}")

    def send_rpc(msg):
        data = json.dumps(msg).encode('utf-8')
        r = urllib.request.Request(post_url, data=data, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(r) as res:
            pass

    def wait_for_id(req_id, timeout=30):
        while True:
            item = q.get(timeout=timeout)
            if isinstance(item, dict) and item.get('id') == req_id:
                return item

    # Initialize
    send_rpc({'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {'protocolVersion': '2024-11-05', 'capabilities': {}, 'clientInfo': {'name': 'Antigravity', 'version': '1.0.0'}}})
    wait_for_id(1)
    send_rpc({'jsonrpc': '2.0', 'method': 'notifications/initialized'})
    print("  MCP Handshake initialized.")

    # Read Preamble
    send_rpc({'jsonrpc': '2.0', 'id': 2, 'method': 'tools/call', 'params': {'name': 'read_sdk_documentation_topic', 'arguments': {'filename': 'preamble'}}})
    wait_for_id(2)
    print("  Preamble loaded.")

    print("\n=== Step 3: Executing Refined Sci-Fi TTRPG Design Script ===")

    js_script = r"""
const { Application } = require('/application.js');
const { Document, NewDocumentOptions, RasterFormat, ColourSpaceType, UnitType } = require('/document.js');
const { FontFamily } = require('/fonts.js');
const { GlyphAtts, GlyphAttDoubleType } = require('/glyphatts.js');
const { ParagraphAtts, ParagraphAttDoubleType, ParagraphAlignXType } = require('/paragraphatts.js');
const { StoryBuilder } = require('/storybuilder.js');
const { Bitmap } = require('/rasterobject.js');
const { Transform, Rectangle } = require('/geometry.js');
const { Shape, ShapeType, ShapeCornerType } = require('/shapes.js');
const { ShapeNodeDefinition, FrameTextNodeDefinition, ImageNodeDefinition, NodeChildrenOnly, NodeChildType } = require('/nodes.js');
const { RGBA8 } = require('/colours.js');
const { FillDescriptor } = require('/fills.js');
const { DocumentCommand } = require('/commands.js');
const { LTRB } = require('/documentproperties.js');

// 1. Close open documents
for (const d of Array.from(Document.all)) {
    try { d.close(); } catch(e){}
}

// 2. Load Generated Visual Assets from Desktop
const assetsPath = Application.userDesktopPath + '/corsair_generated_assets';
console.log('Loading visual assets from:', assetsPath);

const bmCover = Bitmap.loadFromFile(assetsPath + '/cover_starship.jpg');
const bmEmblem = Bitmap.loadFromFile(assetsPath + '/tactical_emblem.jpg');
const bmBgGravity = Bitmap.loadFromFile(assetsPath + '/bg_gravity_contours.jpg');

// 3. Typography Configuration
const bahnFamily = FontFamily.all.find(f => f.name === 'Bahnschrift');
const segoeFamily = FontFamily.all.find(f => f.name === 'Segoe UI');
const consolasFamily = FontFamily.all.find(f => f.name === 'Consolas');

const fontDisplay     = bahnFamily ? bahnFamily.getFont(14) : null; // Bahnschrift Bold
const fontHeading     = bahnFamily ? bahnFamily.getFont(12) : null; // Bahnschrift Bold Condensed
const fontSubHeading  = bahnFamily ? bahnFamily.getFont(9)  : null; // Bahnschrift SemiBold Condensed
const fontLabel       = bahnFamily ? bahnFamily.getFont(6)  : null; // Bahnschrift Condensed
const fontMono        = consolasFamily ? consolasFamily.getFont(1) : (bahnFamily ? bahnFamily.getFont(6) : null);
const fontBody        = segoeFamily ? segoeFamily.getFont(4) : null; // Segoe UI Regular
const fontBodyBold    = segoeFamily ? segoeFamily.getFont(8) : null; // Segoe UI Bold
const fontBodyItalic  = segoeFamily ? segoeFamily.getFont(5) : null; // Segoe UI Italic

// 4. Color System
const colDarkVoid        = RGBA8(10, 14, 23);     // #0A0E17 Deep space void
const colNavyCard        = RGBA8(15, 23, 42);     // #0F172A Tactical card background
const colPaperBg         = RGBA8(248, 250, 252);  // #F8FAFC Crisp reading paper
const colBodyText        = RGBA8(15, 23, 42);     // #0F172A Deep charcoal text
const colAmber           = RGBA8(245, 158, 11);   // #F59E0B Caution / thruster amber
const colAmberDark       = RGBA8(217, 119, 6);    // #D97706 Deep amber
const colAmberBox        = RGBA8(254, 249, 235);  // #FEF9EB Warm amber callout background
const colAmberBoxBorder  = RGBA8(245, 158, 11);   // #F59E0B
const colCyan            = RGBA8(6, 182, 212);    // #06B6D4 Sensor cyan
const colCyanDark        = RGBA8(2, 132, 199);    // #0284C7 Deep beacon blue
const colCyanBox         = RGBA8(240, 249, 255);  // #F0F9FF Cool cyan callout background
const colCyanBoxBorder   = RGBA8(56, 189, 248);   // #38BDF8
const colSlate           = RGBA8(100, 116, 139);  // #64748B Secondary / metadata
const colSlateDark       = RGBA8(51, 65, 85);     // #334155 Borders / rules
const colSlateLight      = RGBA8(226, 232, 240);  // #E2E8F0 Hairlines
const colWhite           = RGBA8(255, 255, 255);  // #FFFFFF Pure white

// 5. Document Architecture: A4 Facing Spreads (5 Pages = Cover + 2 Full Spreads)
const opts = NewDocumentOptions.createDefault();
opts.width = 210;
opts.height = 297;
opts.dpi = 300;
opts.colourSpace = ColourSpaceType.RGB;
opts.format = RasterFormat.RGBA8;
opts.isFacing = true;
opts.isMultiPage = true;
opts.isDoublePageStart = false; // Right page start (Spread 0 is single Cover)
opts.pageCount = 5;
opts.createMaster = true;
opts.marginsEnabled = true;
opts.margins = new LTRB(16, 16, 16, 19);

const doc = Document.createFromOptions(opts);
console.log('Document created successfully. Spread count:', doc.spreadCount);

// 6. Mathematical Dimensions at 300 DPI
const PW = 2480.31;
const PH = 3507.87;

const M_T = 160.0;
const M_B = 180.0;
const M_OUTER = 160.0;
const M_GUTTER = 190.0;

const COL_W = 1030.0;
const COL_GAP = 70.0;
const CONTENT_W = COL_W * 2 + COL_GAP; // 2130.0 pt

// Left page columns
const L_COL1_X = M_OUTER;                         // 160.0
const L_COL2_X = M_OUTER + COL_W + COL_GAP;       // 1260.0

// Right page columns
const R_COL1_X = PW + M_GUTTER;                   // 2670.31
const R_COL2_X = PW + M_GUTTER + COL_W + COL_GAP; // 3770.31

// STRICTLY RECTANGULAR GEOMETRY UTILITIES
function addImage(target, x, y, w, h, bitmap) {
    const imgDef = ImageNodeDefinition.create(RasterFormat.RGBA8);
    imgDef.bitmap = bitmap;
    const sx = w / bitmap.width;
    const sy = h / bitmap.height;
    imgDef.transform = Transform.createScale(sx, sy).translate(x, y);
    doc.addNode(imgDef, target);
}

function addRect(target, x, y, w, h, fillCol) {
    const shape = Shape.create(ShapeType.Rectangle);
    shape.topLeft.cornerType = ShapeCornerType.None;
    shape.topRight.cornerType = ShapeCornerType.None;
    shape.bottomLeft.cornerType = ShapeCornerType.None;
    shape.bottomRight.cornerType = ShapeCornerType.None;
    const rect = new Rectangle(x, y, w, h);
    const fill = FillDescriptor.createSolid(fillCol);
    const def = ShapeNodeDefinition.create(shape, rect, fill, null, null, null);
    doc.addNode(def, target);
}

function addBorder(target, x, y, w, h, strokeCol, strokeW = 1.0) {
    const shape = Shape.create(ShapeType.Rectangle);
    shape.topLeft.cornerType = ShapeCornerType.None;
    shape.topRight.cornerType = ShapeCornerType.None;
    shape.bottomLeft.cornerType = ShapeCornerType.None;
    shape.bottomRight.cornerType = ShapeCornerType.None;
    const rect = new Rectangle(x, y, w, h);
    const stroke = FillDescriptor.createSolid(strokeCol);
    const def = ShapeNodeDefinition.create(shape, rect, null, stroke, strokeW, null);
    doc.addNode(def, target);
}

function addTextFrame(target, x, y, w, h, populateFn) {
    const sb = StoryBuilder.create();
    sb.setToFrameTextDefaultStyle(doc.dpi, doc.format);
    populateFn(sb);
    const def = FrameTextNodeDefinition.createFromStoryBuilder({ x, y, width: w, height: h }, sb);
    doc.addNode(def, target);
}

function addCalloutBox(target, x, y, w, h, fillCol, strokeCol, tabCol) {
    addRect(target, x, y, w, h, fillCol);
    if (strokeCol) {
        addBorder(target, x, y, w, h, strokeCol, 1.5);
    }
    if (tabCol) {
        addRect(target, x, y, 10, h, tabCol);
    }
}

function addChapterHeader(target, pageX, y, titleText) {
    addTextFrame(target, pageX, y, CONTENT_W, 68, sb => {
        const ga = sb.glyphAtts;
        if (fontHeading) ga.font = fontHeading;
        ga.height = 62;
        ga.brushFill = FillDescriptor.createSolid(colNavyCard);
        sb.setGlyphAtts(ga);
        sb.addText(titleText);
    });
    addRect(target, pageX, y + 74, CONTENT_W, 2, colAmber);
}


// =========================================================================
// 7. MASTER SPREAD: CLEAN, PROFESSIONAL RUNNING HEADERS & FOOTERS
// =========================================================================
console.log("Establishing Master Spread A-Master...");
const masterSpreads = Array.from(new NodeChildrenOnly(doc.rootNode.handle, NodeChildType.MasterSpread, false));
const masterSpread = masterSpreads[0];

// Left Page Master (Verso) - Technical Background Image (Gravity Contours)
addImage(masterSpread, 0, 0, PW, PH, bmBgGravity);

// Right Page Master (Recto) - Technical Background Image (Gravity Contours, Normal Orientation)
addImage(masterSpread, PW, 0, PW, PH, bmBgGravity);

// Left Page Master (Verso) - Clean Book Title Header
addRect(masterSpread, L_COL1_X, 160, CONTENT_W, 1, colSlateLight);
addTextFrame(masterSpread, L_COL1_X, 120, CONTENT_W, 30, sb => {
    const ga = sb.glyphAtts;
    if (fontHeading) ga.font = fontHeading;
    ga.height = 20;
    ga.brushFill = FillDescriptor.createSolid(colSlate);
    sb.setGlyphAtts(ga);
    sb.addText("CORSAIR ROLEPLAYING GAME");
});
addRect(masterSpread, L_COL1_X, 3330, CONTENT_W, 1, colSlateLight);

// Right Page Master (Recto) - Clean Chapter Header
addRect(masterSpread, R_COL1_X, 160, CONTENT_W, 1, colSlateLight);
addTextFrame(masterSpread, R_COL1_X, 120, CONTENT_W, 30, sb => {
    const ga = sb.glyphAtts;
    if (fontHeading) ga.font = fontHeading;
    ga.height = 20;
    ga.brushFill = FillDescriptor.createSolid(colSlate);
    sb.setGlyphAtts(ga);
    sb.addText("WELCOME TO CORSAIR");
});
addRect(masterSpread, R_COL1_X, 3330, CONTENT_W, 1, colSlateLight);


// =========================================================================
// 8. SPREAD 0: PAGE 1 (COVER)
// =========================================================================
const spreads = Array.from(doc.spreads);
const spread0 = spreads[0];
console.log("Composing Spread 0 (Cover)...");

addImage(spread0, 0, 0, PW, PH, bmCover);

// Clean Rectangular Hairline Frame
addBorder(spread0, 60, 60, PW - 120, PH - 120, colAmber, 1.5);
addBorder(spread0, 75, 75, PW - 150, PH - 150, colNavyCard, 0.5);

// Corner crosshairs
function addCoverCrosshair(x, y) {
    addRect(spread0, x - 20, y, 40, 2, colAmber);
    addRect(spread0, x, y - 20, 2, 40, colAmber);
}
addCoverCrosshair(60, 60);
addCoverCrosshair(PW - 60, 60);
addCoverCrosshair(60, PH - 60);
addCoverCrosshair(PW - 60, PH - 60);

// Rectangular Title Plate
const titleBoxY = 240;
const titleBoxH = 340;
addRect(spread0, 130, titleBoxY, PW - 260, titleBoxH, colNavyCard);
addBorder(spread0, 130, titleBoxY, PW - 260, titleBoxH, colAmber, 2.0);
addRect(spread0, 130, titleBoxY, 12, titleBoxH, colAmber);

addTextFrame(spread0, 170, titleBoxY + 30, PW - 340, 170, sb => {
    const ga = sb.glyphAtts;
    if (fontDisplay) ga.font = fontDisplay;
    ga.height = 145;
    ga.brushFill = FillDescriptor.createSolid(colWhite);
    sb.setGlyphAtts(ga);
    sb.addText("CORSAIR");
});

addTextFrame(spread0, 175, titleBoxY + 235, PW - 350, 50, sb => {
    const ga = sb.glyphAtts;
    if (fontHeading) ga.font = fontHeading;
    ga.height = 36;
    ga.brushFill = FillDescriptor.createSolid(colAmber);
    sb.setGlyphAtts(ga);
    sb.addText("A TABLETOP ROLEPLAYING GAME OF VOID SURVIVAL & CAMARADERIE");
});

// Bottom Console Dossier Bar (Clean, Rectangular, No Made-Up Slashes)
const consoleY = PH - 500;
const consoleH = 180;
addRect(spread0, 130, consoleY, PW - 260, consoleH, colNavyCard);
addBorder(spread0, 130, consoleY, PW - 260, consoleH, colCyanDark, 1.5);
addRect(spread0, 130, consoleY, 12, consoleH, colAmber);

// Integrated Tactical Patch Emblem
addImage(spread0, 170, consoleY + 20, 140, 140, bmEmblem);

// Clean credits
addTextFrame(spread0, 350, consoleY + 36, PW - 520, 45, sb => {
    const ga = sb.glyphAtts;
    if (fontHeading) ga.font = fontHeading;
    ga.height = 36;
    ga.brushFill = FillDescriptor.createSolid(colAmber);
    sb.setGlyphAtts(ga);
    sb.addText("CORE RULEBOOK");
});

addTextFrame(spread0, 350, consoleY + 92, PW - 520, 40, sb => {
    const ga = sb.glyphAtts;
    if (fontHeading) ga.font = fontHeading;
    ga.height = 28;
    ga.brushFill = FillDescriptor.createSolid(colWhite);
    sb.setGlyphAtts(ga);
    sb.addText("AUTHOR & LEAD DESIGNER: PÉTER CSISZÁR");
});


// =========================================================================
// 9. SPREAD 1: PAGE 2 (PREAMBLE - SINGLE COLUMN) & PAGE 3 (TABLE OF CONTENTS)
// =========================================================================
const spread1 = spreads[1];
console.log("Composing Spread 1: Single-Column Preamble & Rectangular Master TOC...");

// --- PAGE 2 (LEFT): PREAMBLE IN ELEGANT SINGLE COLUMN SETUP ---
const p2ColW = 1750.0;
const p2ColX = (PW - p2ColW) / 2.0; // Centered on page = 365.15 pt

// Chapter Heading
addTextFrame(spread1, p2ColX, 180, p2ColW, 70, sb => {
    const ga = sb.glyphAtts;
    if (fontHeading) ga.font = fontHeading;
    ga.height = 62;
    ga.brushFill = FillDescriptor.createSolid(colNavyCard);
    sb.setGlyphAtts(ga);
    sb.addText("Preamble: A Note From the Author");
});
addRect(spread1, p2ColX, 260, p2ColW, 2, colAmber);

// Unified Single Column StoryBuilder for all 6 paragraphs of the Preamble, Special Thanks, and Legal
const sbPreamble = StoryBuilder.create();
sbPreamble.setToFrameTextDefaultStyle(doc.dpi, doc.format);

const gaPreBody = GlyphAtts.create();
if (fontBody) gaPreBody.font = fontBody;
gaPreBody.height = 30;
gaPreBody.brushFill = FillDescriptor.createSolid(colBodyText);

const paPre = ParagraphAtts.create();
paPre.relativeLeading = 1.48;
paPre.spaceAfter = 20;

sbPreamble.setGlyphAtts(gaPreBody);
sbPreamble.setParagraphAtts(paPre);

const preambleParas = [
    "Funnily enough, my first tabletop roleplaying game wasn't Dungeons & Dragons. It was some obscure hungarian game called M.A.G.U.S., which if anything, helped me get a feel what I don't want from a roleplaying game. My second, and the first one I learned to run as a GM was Shadowrun. You might be able to spot a few influences here and there. I thoroughly fell in love with the setting but the rules were a bit too crunchy for my taste. That's when I started to experiment with rulesets. I probably tried to hack Shadowrun to be more friendly at least three separate times if not more.",
    "Along the lines I discovered other games, systems, and game designers, each bringing something new to the table, but my other big muse was Blades in the Dark. John Harper's brilliant work was exactly on the opposite end of the spectrum when it came to complexity. You could create a character in less than fifteen minutes if you wanted to, and both you and your group had a clear identity and goal you were working toward. I still hope one day I get to be a player and not a game master in a Forged in the Dark game. That said...",
    "I still found myself tinkering with the rules, trying to make them more complex this time around. I realised what I really wanted was somewhere in the middle. Something that could elegantly handle all the curveballs that players could throw at it with relatively simple mechanics. And somewhere along the line I ended up thinking, \"what if I tried my hand at making my own system from scratch?\" This is the result of that thought.",
    "But this is the furthest I can go on without admitting how I'm standing on the shoulders of giants. I've already mentioned Shadowrun, and Blades in the Dark, but Dungeons and Dragons, Daggerheart, the Star Wars TTRPGs by Fantasy Flight Games were all crucial inputs to the final mechanics.",
    "As far as the setting goes, where to even begin? I loved Destiny, Horizon Zero Dawn, Mass Effect, Guardians of the Galaxy, The Expanse and many more. I knew there were many other sci-fi settings out there, but I was really hoping that this specific idea of blending space fantasy with hard sci-fi would be original enough to stand out.",
    "That said, it would have amounted to nothing if I didn't have help. From Large Language models too, putting so much words to, well, not paper but disk, but also, those people that listened to my pitches, rants, and ramblings, and gave me feedback along the way. Who were kind enough to sit down and play this with me when it was even bigger of a mess than it is now. I know most of you never expected yourself to appear in any sort of credits, but I hope this brings you some joy, or at least a good chuckle."
];

for (const p of preambleParas) {
    sbPreamble.addText(p);
    sbPreamble.addParagraphBreak();
}

// Special Thanks
const gaThanksBold = GlyphAtts.create();
if (fontBodyBold) gaThanksBold.font = fontBodyBold;
gaThanksBold.height = 30;
gaThanksBold.brushFill = FillDescriptor.createSolid(colNavyCard);

const paThanks = ParagraphAtts.create();
paThanks.spaceBefore = 24;
paThanks.spaceAfter = 14;
paThanks.relativeLeading = 1.48;

sbPreamble.setGlyphAtts(gaThanksBold);
sbPreamble.setParagraphAtts(paThanks);
sbPreamble.addText("Special thanks to: ");
sbPreamble.setGlyphAtts(gaPreBody);
sbPreamble.addText("Fábián János, Bangó Dávid");
sbPreamble.addParagraphBreak();

sbPreamble.setGlyphAtts(gaPreBody);
sbPreamble.addText("And an even bigger thanks to my wife and love of my life, Farkas Ágnes. I borrowed your ear more times than I can count, and you played a bigger role in making this a reality than anyone else.");
sbPreamble.addParagraphBreak();

// Legal & Licensing Header
const gaLegalH = GlyphAtts.create();
if (fontHeading) gaLegalH.font = fontHeading;
gaLegalH.height = 42;
gaLegalH.brushFill = FillDescriptor.createSolid(colNavyCard);

const paLegalH = ParagraphAtts.create();
paLegalH.spaceBefore = 36;
paLegalH.spaceAfter = 14;
paLegalH.isSumBeforeAndAfterSpace = true;

sbPreamble.setGlyphAtts(gaLegalH);
sbPreamble.setParagraphAtts(paLegalH);
sbPreamble.addText("Legal & Licensing");
sbPreamble.addParagraphBreak();

// Legal bullet points
const gaLegalBody = GlyphAtts.create();
if (fontBody) gaLegalBody.font = fontBody;
gaLegalBody.height = 27;
gaLegalBody.brushFill = FillDescriptor.createSolid(colBodyText);

const paLegalBody = ParagraphAtts.create();
paLegalBody.relativeLeading = 1.44;
paLegalBody.spaceAfter = 12;

sbPreamble.setGlyphAtts(gaLegalBody);
sbPreamble.setParagraphAtts(paLegalBody);

sbPreamble.addText("•  Author & Lead Designer: Péter Csiszár");
sbPreamble.addParagraphBreak();
sbPreamble.addText("•  Version: 0.0.1");
sbPreamble.addParagraphBreak();
sbPreamble.addText("•  License: Corsair is published under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).");
sbPreamble.addParagraphBreak();
sbPreamble.addText("•  Copyright: © Péter Csiszár. You are free to share, copy, redistribute, and adapt this material in any medium or format for non-commercial purposes, provided appropriate credit is given.");

// Single Column Frame: Holds all preamble content cleanly from y=300 to y=3300 (height=3000 pt)
const defPreCol = FrameTextNodeDefinition.createFromStoryBuilder({ x: p2ColX, y: 300, width: p2ColW, height: 3000 }, sbPreamble);
doc.addNode(defPreCol, spread1);

// Page 2 Running Footer Page Number
addTextFrame(spread1, p2ColX + p2ColW - 100, 3365, 100, 40, sb => {
    const ga = sb.glyphAtts;
    if (fontHeading) ga.font = fontHeading;
    ga.height = 28;
    ga.brushFill = FillDescriptor.createSolid(colAmberDark);
    const pa = sb.paragraphAtts;
    pa.alignXType = ParagraphAlignXType.Right;
    sb.setGlyphAtts(ga);
    sb.setParagraphAtts(pa);
    sb.addText("ii");
});


// --- PAGE 3 (RIGHT): MASTER TABLE OF CONTENTS (CLEAN RECTANGULAR BLOCKS) ---
addChapterHeader(spread1, R_COL1_X, 180, "Table of Contents");

function formatTocBlock(targetX, targetY, w, actTitle, actSub, actPage, items) {
    const headerH = 88;
    const itemH = 78;
    const bodyH = items.length * itemH + 20;
    const totalH = headerH + bodyH;

    // Header bar (Rectangular)
    addRect(spread1, targetX, targetY, w, headerH, colNavyCard);
    addTextFrame(spread1, targetX + 22, targetY + 14, w - 140, 38, sb => {
        const ga = sb.glyphAtts;
        if (fontHeading) ga.font = fontHeading;
        ga.height = 32;
        ga.brushFill = FillDescriptor.createSolid(colAmber);
        sb.setGlyphAtts(ga);
        sb.addText(actTitle.toUpperCase());
    });
    addTextFrame(spread1, targetX + 22, targetY + 52, w - 140, 26, sb => {
        const ga = sb.glyphAtts;
        if (fontHeading) ga.font = fontHeading;
        ga.height = 22;
        ga.brushFill = FillDescriptor.createSolid(colSlate);
        sb.setGlyphAtts(ga);
        sb.addText(actSub);
    });
    addTextFrame(spread1, targetX + w - 120, targetY + 24, 102, 38, sb => {
        const ga = sb.glyphAtts;
        if (fontHeading) ga.font = fontHeading;
        ga.height = 28;
        ga.brushFill = FillDescriptor.createSolid(colCyan);
        const pa = sb.paragraphAtts;
        pa.alignXType = ParagraphAlignXType.Right;
        sb.setGlyphAtts(ga);
        sb.setParagraphAtts(pa);
        sb.addText(actPage);
    });

    // Body content card (Rectangular)
    addRect(spread1, targetX, targetY + headerH, w, bodyH, colPaperBg);
    addRect(spread1, targetX, targetY + totalH, w, 1, colSlateDark);

    // Item titles
    addTextFrame(spread1, targetX + 22, targetY + headerH + 16, w - 96, bodyH - 28, sb => {
        const ga = sb.glyphAtts;
        if (fontBody) ga.font = fontBody;
        ga.height = 29;
        ga.brushFill = FillDescriptor.createSolid(colBodyText);
        const pa = sb.paragraphAtts;
        pa.relativeLeading = 1.48;
        pa.spaceAfter = 16;
        sb.setGlyphAtts(ga);
        sb.setParagraphAtts(pa);
        for (let i = 0; i < items.length; i++) {
            sb.addText("•  " + items[i].title);
            if (i < items.length - 1) sb.addParagraphBreak();
        }
    });

    // Page numbers
    addTextFrame(spread1, targetX + w - 74, targetY + headerH + 16, 56, bodyH - 28, sb => {
        const ga = sb.glyphAtts;
        if (fontHeading) ga.font = fontHeading;
        ga.height = 29;
        ga.brushFill = FillDescriptor.createSolid(colAmberDark);
        const pa = sb.paragraphAtts;
        pa.alignXType = ParagraphAlignXType.Right;
        pa.relativeLeading = 1.48;
        pa.spaceAfter = 16;
        sb.setGlyphAtts(ga);
        sb.setParagraphAtts(pa);
        for (let i = 0; i < items.length; i++) {
            sb.addText(items[i].page);
            if (i < items.length - 1) sb.addParagraphBreak();
        }
    });

    return totalH;
}

// Page 3 Left Column (Col 1): Act 0, Act I, Act II
let tocY1 = 300;
tocY1 += formatTocBlock(R_COL1_X, tocY1, COL_W, "Act 0: System Introduction", "Frontier Orientation, Foundations & Roadmap", "Page 1", [
    { title: "Chapter 00: Front Matter & Overview", page: "1" },
    { title: "Who Are the Corsairs?", page: "1" },
    { title: "What is a Roleplaying Game?", page: "2" },
    { title: "What You'll Need to Play", page: "2" },
    { title: "Reader's Guide: How to Use This Book", page: "2" }
]) + 60;

tocY1 += formatTocBlock(R_COL1_X, tocY1, COL_W, "Act I: Core Rules & Engine", "Attributes, Tests, Action Economy & Tactical Effects", "Page 7", [
    { title: "Chapter 01: Core Mechanics & Resolution", page: "7" },
    { title: "Attributes & Attribute Pairs", page: "8" },
    { title: "Simple, Success & Complex Tests", page: "10" },
    { title: "Upgrades, Downgrades & Gambits", page: "13" },
    { title: "Scenes, Pacing & Action Points", page: "15" },
    { title: "Effects & Tactical Triggers", page: "17" },
    { title: "Interlude: 27th Hour", page: "23" }
]) + 60;

tocY1 += formatTocBlock(R_COL1_X, tocY1, COL_W, "Act II: Characters & Chassis", "Operative Conception, Lineages & MANTLE Rigs", "Page 25", [
    { title: "Chapter 02: Character Creation", page: "25" },
    { title: "Traits & Lineages Catalog", page: "31" },
    { title: "Advancement & Career Milestones", page: "35" },
    { title: "Chapter 03: Classes & The MANTLE System", page: "39" },
    { title: "The Five Chassis: Conduit, Hazard, Pilot, Vanguard, Weaver", page: "41" },
    { title: "Interlude: Post-War Headaches", page: "79" }
]);

// Page 3 Right Column (Col 2): Act III, Act IV, Act V
let tocY2 = 300;
tocY2 += formatTocBlock(R_COL2_X, tocY2, COL_W, "Act III: Operations & Hardware", "Dynamic Combat, Armory, Starships & Downtime Gigs", "Page 81", [
    { title: "Tactical Combat & Dynamic Cover", page: "81" },
    { title: "Chapter 04: The Armory & Equipment", page: "87" },
    { title: "Firearms, Melee, Armor & Exotic Hardware", page: "91" },
    { title: "Chapter 05: Starships & Naval Operations", page: "101" },
    { title: "The 24-Hour Downtime Cycle & Gigs", page: "115" },
    { title: "Interlude: Great Tithe", page: "121" }
]) + 60;

tocY2 += formatTocBlock(R_COL2_X, tocY2, COL_W, "Act IV: Worlds of the Sphere", "Planetary Gazetteer, Factions, Flotilla & Canon Lore", "Page 125", [
    { title: "Chapter 07: Worlds of the Sphere", page: "125" },
    { title: "Planetary Gazetteer & Clusters", page: "127" },
    { title: "Sovereign Powers, Corps & The Flotilla", page: "135" },
    { title: "Timeline of Arrival (0 to 518 AA)", page: "149" },
    { title: "Interlude: Space Tourism", page: "155" }
]) + 60;

tocY2 += formatTocBlock(R_COL2_X, tocY2, COL_W, "Act V: Running the Game & Lore", "GM Toolkit, Bestiary Statblocks & Mission Generator", "Page 161", [
    { title: "Chapter 06A: Operational Systems", page: "161" },
    { title: "Chapter 06B: Bestiary & Threat Cards", page: "171" },
    { title: "The Procedural Mission Generator", page: "185" },
    { title: "Chapter 08: The Forbidden Archives", page: "193" },
    { title: "Chapter 10: Reference & Index", page: "201" }
]);

// Page 3 Running Footer Page Number
addTextFrame(spread1, R_COL1_X + CONTENT_W - 100, 3365, 100, 40, sb => {
    const ga = sb.glyphAtts;
    if (fontHeading) ga.font = fontHeading;
    ga.height = 28;
    ga.brushFill = FillDescriptor.createSolid(colAmberDark);
    const pa = sb.paragraphAtts;
    pa.alignXType = ParagraphAlignXType.Right;
    sb.setGlyphAtts(ga);
    sb.setParagraphAtts(pa);
    sb.addText("iii");
});


// =========================================================================
// 10. SPREAD 2: PAGE 4 (WELCOME & CELL) & PAGE 5 (WHAT IS AN RPG & READER'S GUIDE)
// =========================================================================
const spread2 = spreads[2];
console.log("Composing Spread 2: Prominent Headings, Generous Spacing, Balanced Columns...");

// Common Typographic Styles for Spreads
// Major Section Heading (H2): 58 pt, Navy, 90 pt spaceBefore, 18 pt spaceAfter
const gaH2 = GlyphAtts.create();
if (fontHeading) gaH2.font = fontHeading;
gaH2.height = 58;
gaH2.brushFill = FillDescriptor.createSolid(colNavyCard);

const paH2 = ParagraphAtts.create();
paH2.spaceBefore = 90;
paH2.spaceAfter = 18;
paH2.isSumBeforeAndAfterSpace = true;

const paH2Top = ParagraphAtts.create();
paH2Top.spaceBefore = 0;
paH2Top.spaceAfter = 18;

// Subchapter Heading (H3): 46 pt, Amber, 80 pt spaceBefore, 16 pt spaceAfter
const gaH3 = GlyphAtts.create();
if (fontHeading) gaH3.font = fontHeading;
gaH3.height = 46;
gaH3.brushFill = FillDescriptor.createSolid(colAmberDark);

const paH3 = ParagraphAtts.create();
paH3.spaceBefore = 80;
paH3.spaceAfter = 16;
paH3.isSumBeforeAndAfterSpace = true;

const paH3Top = ParagraphAtts.create();
paH3Top.spaceBefore = 0;
paH3Top.spaceAfter = 16;

// Subchapter Heading Cyan variant (H3)
const gaH3Cyan = GlyphAtts.create();
if (fontHeading) gaH3Cyan.font = fontHeading;
gaH3Cyan.height = 46;
gaH3Cyan.brushFill = FillDescriptor.createSolid(colCyanDark);

// Body text: 30 pt, 1.46 leading, 18 pt spaceAfter
const gaBody = GlyphAtts.create();
if (fontBody) gaBody.font = fontBody;
gaBody.height = 30;
gaBody.brushFill = FillDescriptor.createSolid(colBodyText);

const paBody = ParagraphAtts.create();
paBody.relativeLeading = 1.46;
paBody.spaceAfter = 18;

const gaBoldText = GlyphAtts.create();
if (fontBodyBold) gaBoldText.font = fontBodyBold;
gaBoldText.height = 30;
gaBoldText.brushFill = FillDescriptor.createSolid(colNavyCard);

const gaItalic = GlyphAtts.create();
if (fontBodyItalic) gaItalic.font = fontBodyItalic;
gaItalic.height = 29;
gaItalic.brushFill = FillDescriptor.createSolid(colSlate);

const paItalic = ParagraphAtts.create();
paItalic.spaceBefore = 0;
paItalic.spaceAfter = 14;
paItalic.relativeLeading = 1.42;


// --- PAGE 4 (LEFT): WELCOME TO CORSAIR ---
addChapterHeader(spread2, L_COL1_X, 180, "Welcome to Corsair");

// Full Width Elevator Pitch (Rectangular, Clean, Ample Height to Prevent Text Overflow)
const pitchY = 270;
const pitchH = 380;
addCalloutBox(spread2, L_COL1_X, pitchY, CONTENT_W, pitchH, colAmberBox, colAmberBoxBorder, colAmberDark);
addTextFrame(spread2, L_COL1_X + 34, pitchY + 24, CONTENT_W - 68, pitchH - 44, sb => {
    const gaTitle = sb.glyphAtts;
    if (fontHeading) gaTitle.font = fontHeading;
    gaTitle.height = 34;
    gaTitle.brushFill = FillDescriptor.createSolid(colAmberDark);
    const pa = sb.paragraphAtts;
    pa.spaceAfter = 12;
    pa.relativeLeading = 1.34;
    sb.setGlyphAtts(gaTitle);
    sb.setParagraphAtts(pa);
    sb.addText("The Elevator Pitch");
    sb.addParagraphBreak();

    const gaLead = sb.glyphAtts;
    if (fontBodyBold) gaLead.font = fontBodyBold;
    gaLead.height = 28;
    gaLead.brushFill = FillDescriptor.createSolid(colNavyCard);
    sb.setGlyphAtts(gaLead);
    sb.addText("Corsair is a tabletop roleplaying game of high-stakes frontier adventure, tactical problem-solving, and found-family camaraderie, set against the vast backdrop of a macro-engineered cosmos.");
    sb.addParagraphBreak();

    const gaB = sb.glyphAtts;
    if (fontBody) gaB.font = fontBody;
    gaB.height = 26;
    gaB.brushFill = FillDescriptor.createSolid(colBodyText);
    const paB = sb.paragraphAtts;
    paB.relativeLeading = 1.42;
    sb.setGlyphAtts(gaB);
    sb.setParagraphAtts(paB);
    sb.addText("You and your crew portray a Corsair Cell: licensed, independent operatives flying a versatile starship with a cross-jurisdictional charter. When local planetary law ends at the clouds and the naval peacekeepers of the Flotilla are light-hours away, your sponsors call on you. Whether you are investigating corporate sabotage in a spinning orbital arcology, braving derelict Precursor ruins for lost technology, negotiating tense standoffs across a fraying border, or scraping together enough fuel credits to keep your reaction thrusters burning, your crew stands as the thin line holding a young civilization together.");
});

// PAGE 4 COLUMN 1: Who Are the Corsairs? + The Sphere at a Glance + Your Role: The Corsair Cell
const sbP4Col1 = StoryBuilder.create();
sbP4Col1.setToFrameTextDefaultStyle(doc.dpi, doc.format);

// Section: Who Are the Corsairs? (H2: 58 pt)
sbP4Col1.setGlyphAtts(gaH2);
sbP4Col1.setParagraphAtts(paH2Top);
sbP4Col1.addText("Who Are the Corsairs?");
sbP4Col1.addParagraphBreak();

// Subheading: The Sphere at a Glance (H3: 46 pt, generous spaceBefore)
sbP4Col1.setGlyphAtts(gaH3);
sbP4Col1.setParagraphAtts(paH3);
sbP4Col1.addText("The Sphere at a Glance");
sbP4Col1.addParagraphBreak();

sbP4Col1.setGlyphAtts(gaBody);
sbP4Col1.setParagraphAtts(paBody);
sbP4Col1.addText("The game takes place within the Sphere, a breathtaking engineered solar system featuring over a hundred terrestrial, habitable worlds and moons locked in tight binary orbits around colossal gas giants, all circling a quiet Orange Dwarf star.");
sbP4Col1.addParagraphBreak();

sbP4Col1.addText("Circa five hundred years ago, automated seed arks brought the survivors of four dying worlds into this seemingly abandoned system. Arriving as the Newcomers, humanity and three alien lineages—the cold-blooded, crested Naga, the dense-skinned Craggen, and the chlorophyllic Sylvan—made their first historic landfall on a fertile moon appropriately named Landfall. Over five centuries of shared survival, exploration, and cultural blending across the moons, six natural hybrid lineages took root alongside them: Drakelings, Elves, Gnomes, Dwarves, Kobolds, and Trolls.");
sbP4Col1.addParagraphBreak();

sbP4Col1.addText("Today, civilization spans dozens of bustling worlds, gleaming orbital transfer stations, and remote mining habitats. Yet the laws of nature remain stubbornly grounded. There is no faster-than-light warp drive; ships burn continuous fusion engines along calculated orbital curves. There is no artificial gravity plating; you stay grounded either through the axial acceleration of your ship's thrusters, the gentle centrifugal spin of a habitat drum, or the solid click of magnetic boots against steel decks. And in the vacuum of space, waste heat is as dangerous as an enemy round.");
sbP4Col1.addParagraphBreak();

// Subheading: Your Role: The Corsair Cell (H3: 46 pt, with 80 pt spaceBefore!)
sbP4Col1.setGlyphAtts(gaH3);
sbP4Col1.setParagraphAtts(paH3);
sbP4Col1.addText("Your Role: The Corsair Cell");
sbP4Col1.addParagraphBreak();

sbP4Col1.setGlyphAtts(gaBody);
sbP4Col1.setParagraphAtts(paBody);
sbP4Col1.addText("Civilization across the moons is divided by a historic treaty: planetary governments hold total jurisdiction within their atmospheric gravity wells, while the peacekeeping fleet known as the Flotilla polices the open void and interstellar shipping lanes. This separation creates a glaring legal seam. Smugglers, corporate raiders, rogue mercenaries, and political conspirators routinely commit crimes under planetary clouds and burn into orbit, daring local authorities to chase them past their legal boundaries.");
sbP4Col1.addParagraphBreak();

sbP4Col1.addText("To bridge this seam, authorities grant independent charters to Corsairs—small, autonomous crews given cross-jurisdictional warrants to cross from planetary mud to the cold vacuum of orbit without getting bogged down in red tape.");

// Column 1 Frame on Page 4 (Starts at y=700 safely below Elevator Pitch, height=2620 pt)
const defP4Col1 = FrameTextNodeDefinition.createFromStoryBuilder({ x: L_COL1_X, y: 700, width: COL_W, height: 2620 }, sbP4Col1);
doc.addNode(defP4Col1, spread2);


// PAGE 4 COLUMN 2: 3 Cell Pillars + What is a Roleplaying Game? + The Conversational Cycle
const sbP4Col2 = StoryBuilder.create();
sbP4Col2.setToFrameTextDefaultStyle(doc.dpi, doc.format);

// Lead text for Pillars
sbP4Col2.setGlyphAtts(gaBody);
sbP4Col2.setParagraphAtts(paBody);
sbP4Col2.addText("As players, you form a Corsair Cell—a tight-knit crew of 3 to 5 specialists sharing an agile starship. Every cell is distinct:");
sbP4Col2.addParagraphBreak();

// The 3 Pillars
sbP4Col2.setGlyphAtts(gaBoldText);
sbP4Col2.addText("•  Conflicting Sponsors: ");
sbP4Col2.setGlyphAtts(gaBody);
sbP4Col2.addText("Legitimate Corsairs are typically backed by multiple, competing sponsors—such as a Flotilla naval commander, a planetary governor, a commercial trading guild, or an independent labor union. By balancing competing patrons, your crew maintains its operational independence.");
sbP4Col2.addParagraphBreak();

sbP4Col2.setGlyphAtts(gaBoldText);
sbP4Col2.addText("•  The Omni-Role Ethos: ");
sbP4Col2.setGlyphAtts(gaBody);
sbP4Col2.addText("You are practical survivors, not rigid archetypes. While every operative has specialized training or hardware rigs, no Corsair is locked into a single duty. Every member of the crew knows how to draw a sidearm in a corridor firefight, monitor a sensor array, pilot a shuttle, patch a ruptured environmental suit, and haggle for spare parts at an orbital bazaar.");
sbP4Col2.addParagraphBreak();

sbP4Col2.setGlyphAtts(gaBoldText);
sbP4Col2.addText("•  Freedom of Approach: ");
sbP4Col2.setGlyphAtts(gaBody);
sbP4Col2.addText("Whether your crew acts as principled investigators, gritty salvage hounds, diplomatic fixers, or razor-sharp troubleshooters, how you tackle your contracts is entirely up to you.");
sbP4Col2.addParagraphBreak();

// Section: What is a Roleplaying Game? (H2: 58 pt, with generous 90 pt spaceBefore!)
sbP4Col2.setGlyphAtts(gaH2);
sbP4Col2.setParagraphAtts(paH2);
sbP4Col2.addText("What is a Roleplaying Game?");
sbP4Col2.addParagraphBreak();

sbP4Col2.setGlyphAtts(gaBody);
sbP4Col2.setParagraphAtts(paBody);
sbP4Col2.addText("A roleplaying game (RPG) is a collaborative storytelling experience. You and your friends create characters to portray, and together you navigate a living world full of adventure, intrigue, and danger.");
sbP4Col2.addParagraphBreak();

sbP4Col2.addText("One player takes on the role of the Game Master (GM). The GM is the primary storyteller, the referee of the rules, and the voice of the non-player characters (NPCs) that inhabit the void. The other players portray the Player Characters (PCs), the specialist operatives who make up the Corsair crew and drive the story forward.");
sbP4Col2.addParagraphBreak();

// Subheading: The Conversational Cycle (H3: 46 pt, with 80 pt spaceBefore!)
sbP4Col2.setGlyphAtts(gaH3Cyan);
sbP4Col2.setParagraphAtts(paH3);
sbP4Col2.addText("The Conversational Cycle");
sbP4Col2.addParagraphBreak();

sbP4Col2.setGlyphAtts(gaBody);
sbP4Col2.setParagraphAtts(paBody);
sbP4Col2.addText("The game unfolds through a natural conversation across four essential steps:");
sbP4Col2.addParagraphBreak();

const cycleSteps = [
    { num: "1. The GM describes the situation: ", desc: "The environment, sensory details of the scene, and any imminent hazards or NPCs present." },
    { num: "2. The players declare their intent: ", desc: "You state what your characters do, say, or attempt—whether moving into cover, overriding an airlock seal, or negotiating terms with a tense frontier marshal." },
    { num: "3. The mechanics determine uncertain outcomes: ", desc: "When an action is routine, it simply succeeds. But when an outcome is uncertain, dangerous, or contested, the dice hit the table using the rules outlined in this book." },
    { num: "4. The GM describes the consequences: ", desc: "The fiction moves forward, the scene shifts, and the conversation continues." }
];

for (const s of cycleSteps) {
    sbP4Col2.setGlyphAtts(gaBoldText);
    sbP4Col2.addText(s.num);
    sbP4Col2.setGlyphAtts(gaBody);
    sbP4Col2.addText(s.desc);
    sbP4Col2.addParagraphBreak();
}

sbP4Col2.setGlyphAtts(gaBody);
sbP4Col2.addText("There are no winners or losers in a roleplaying game. The goal is to collaborate, face tactical challenges, and tell a memorable, cinematic story together.");

// Column 2 Frame on Page 4 (Starts at y=700 safely below Elevator Pitch, height=2620 pt)
const defP4Col2 = FrameTextNodeDefinition.createFromStoryBuilder({ x: L_COL2_X, y: 700, width: COL_W, height: 2620 }, sbP4Col2);
doc.addNode(defP4Col2, spread2);

// Page 4 Running Footer Page Number
addTextFrame(spread2, L_COL1_X + CONTENT_W - 100, 3365, 100, 40, sb => {
    const ga = sb.glyphAtts;
    if (fontHeading) ga.font = fontHeading;
    ga.height = 28;
    ga.brushFill = FillDescriptor.createSolid(colAmberDark);
    const pa = sb.paragraphAtts;
    pa.alignXType = ParagraphAlignXType.Right;
    sb.setGlyphAtts(ga);
    sb.setParagraphAtts(pa);
    sb.addText("1");
});


// --- PAGE 5 (RIGHT): ESSENTIALS & READER'S GUIDE ---
// Top Block: What You'll Need to Play (Col 1) and The Principle of Narration (Col 2)
const p5TopY = 180;

// Typographic styles for Page 5 Essentials
const gaEssBody = GlyphAtts.create();
if (fontBody) gaEssBody.font = fontBody;
gaEssBody.height = 27;
gaEssBody.brushFill = FillDescriptor.createSolid(colBodyText);

const paEssBody = ParagraphAtts.create();
paEssBody.relativeLeading = 1.38;
paEssBody.spaceAfter = 10;

const gaEssBold = GlyphAtts.create();
if (fontBodyBold) gaEssBold.font = fontBodyBold;
gaEssBold.height = 27;
gaEssBold.brushFill = FillDescriptor.createSolid(colNavyCard);

// Page 5 Column 1 Top: What You'll Need to Play (Finishes cleanly by y=780)
addTextFrame(spread2, R_COL1_X, p5TopY, COL_W, 620, sb => {
    sb.setGlyphAtts(gaH3);
    sb.setParagraphAtts(paH3Top);
    sb.addText("What You'll Need to Play");
    sb.addParagraphBreak();

    sb.setGlyphAtts(gaEssBody);
    sb.setParagraphAtts(paEssBody);
    sb.addText("To play Corsair, you will need a few essentials:");
    sb.addParagraphBreak();

    const essentials = [
        { title: "Dice: ", desc: "Three polyhedral die types: eight-sided (d8), ten-sided (d10), and twelve-sided (d12) dice. A handful of d10s is ideal." },
        { title: "Character & Crew Sheets: ", desc: "Printable sheets for recording operative attributes, skills, equipment, and starship modules." },
        { title: "Pencils & Scratch Paper: ", desc: "For tracking notes, tactical sketches, Action Points, Wounds, and ammunition." },
        { title: "Tokens or Markers: ", desc: "Simple counters (coins, poker chips) for tracking Action Points and tactical positions." },
        { title: "A Group of Friends: ", desc: "Designed for 3 to 5 players, including the Game Master." }
    ];

    for (const ess of essentials) {
        sb.setGlyphAtts(gaEssBold);
        sb.addText("•  " + ess.title);
        sb.setGlyphAtts(gaEssBody);
        sb.addText(ess.desc);
        sb.addParagraphBreak();
    }
});

// Page 5 Column 2 Top: The Principle of Narration (Clean Rectangular Callout Card)
const narrCardH = 460;
addCalloutBox(spread2, R_COL2_X, p5TopY + 15, COL_W, narrCardH, colCyanBox, colCyanBoxBorder, colCyanDark);
addTextFrame(spread2, R_COL2_X + 34, p5TopY + 45, COL_W - 68, narrCardH - 60, sb => {
    const gaT = sb.glyphAtts;
    if (fontHeading) gaT.font = fontHeading;
    gaT.height = 36;
    gaT.brushFill = FillDescriptor.createSolid(colCyanDark);
    const pa = sb.paragraphAtts;
    pa.spaceAfter = 14;
    pa.relativeLeading = 1.36;
    sb.setGlyphAtts(gaT);
    sb.setParagraphAtts(pa);
    sb.addText("The Principle of Narration");
    sb.addParagraphBreak();

    const gaB = sb.glyphAtts;
    if (fontBody) gaB.font = fontBody;
    gaB.height = 28;
    gaB.brushFill = FillDescriptor.createSolid(colBodyText);
    const paB = sb.paragraphAtts;
    paB.relativeLeading = 1.44;
    sb.setGlyphAtts(gaB);
    sb.setParagraphAtts(paB);
    sb.addText("Dice never roll in a vacuum. A roll represents physical friction: boots catching against grated decking, capacitors whining under peak load, or thruster gimbal bearings fighting reaction torque.");
    sb.addParagraphBreak();
    sb.addText("Always describe what your character physically does in the fiction before picking up the dice.");
});

// Reader's Guide Section Header spanning across both columns (starts at y=860, with 80 pt clear air above)
const guideHeaderY = 860;
addTextFrame(spread2, R_COL1_X, guideHeaderY, CONTENT_W, 68, sb => {
    const ga = sb.glyphAtts;
    if (fontHeading) ga.font = fontHeading;
    ga.height = 58;
    ga.brushFill = FillDescriptor.createSolid(colNavyCard);
    sb.setGlyphAtts(ga);
    sb.addText("Reader's Guide: How to Use This Book");
});
addRect(spread2, R_COL1_X, guideHeaderY + 70, CONTENT_W, 2, colAmber);

// Lead paragraph below header
addTextFrame(spread2, R_COL1_X, guideHeaderY + 88, CONTENT_W, 70, sb => {
    const ga = sb.glyphAtts;
    if (fontBody) ga.font = fontBody;
    ga.height = 29;
    ga.brushFill = FillDescriptor.createSolid(colBodyText);
    const pa = sb.paragraphAtts;
    pa.relativeLeading = 1.44;
    sb.setGlyphAtts(ga);
    sb.setParagraphAtts(pa);
    sb.addText("This rulebook is organized into five functional sections designed to take you from foundational mechanics to active campaign play, interleaved with narrative fiction capturing the lived reality of the void:");
});

// Two-column flow for Reader's Guide Parts I to V (starts at y=1050 safely below lead paragraph)
const guidePartsY = 1050;
const guidePartsH = 2270;

// Column 1: Part I & Part II
const sbGuideCol1 = StoryBuilder.create();
sbGuideCol1.setToFrameTextDefaultStyle(doc.dpi, doc.format);

// Part I: Core Rules & Engine
sbGuideCol1.setGlyphAtts(gaH3);
sbGuideCol1.setParagraphAtts(paH3Top);
sbGuideCol1.addText("Part I: Core Rules & Engine");
sbGuideCol1.addParagraphBreak();

sbGuideCol1.setGlyphAtts(gaItalic);
sbGuideCol1.setParagraphAtts(paItalic);
sbGuideCol1.addText("The fundamental mechanics that power every test, decision, and scene in the game.");
sbGuideCol1.addParagraphBreak();

sbGuideCol1.setGlyphAtts(gaBody);
sbGuideCol1.setParagraphAtts(paBody);
sbGuideCol1.addText("•  Core Mechanics: Foundational rules of Attributes, Attribute Pairs, Simple Tests (binary success), Success Tests (degree of achievement), Complex Tests (action + quality), Upgrades, Downgrades, Contests, Gambits, and Teamwork.");
sbGuideCol1.addParagraphBreak();
sbGuideCol1.addText("•  Scenes, Pacing & Action Points: Zooming between Day-to-Day shifts and Moment-to-Moment rounds, the 3 Action Point economy, turn swaps, teamwork actions, and delayed actions.");
sbGuideCol1.addParagraphBreak();
sbGuideCol1.addText("•  Effects: Activating dynamic tactical opportunities by sacrificing Hits on Action Rolls (Chain, Upgrade/Downgrade, Blocker) and Success Rolls (Crit, Push).");
sbGuideCol1.addParagraphBreak();
sbGuideCol1.addText("•  Interlude: A Point of Order on the Twenty-Seventh Hour.");
sbGuideCol1.addParagraphBreak();

// Part II: Character Creation & Classes (H3 with 70 pt spaceBefore!)
sbGuideCol1.setGlyphAtts(gaH3);
sbGuideCol1.setParagraphAtts(paH3);
sbGuideCol1.addText("Part II: Character Creation & Classes");
sbGuideCol1.addParagraphBreak();

sbGuideCol1.setGlyphAtts(gaItalic);
sbGuideCol1.setParagraphAtts(paItalic);
sbGuideCol1.addText("Everything you need to conceive, build, and advance your Corsair operative.");
sbGuideCol1.addParagraphBreak();

sbGuideCol1.setGlyphAtts(gaBody);
sbGuideCol1.setParagraphAtts(paBody);
sbGuideCol1.addText("•  Player Characters: Core Attributes, Derived Attributes, Skills, and Condition (wounds and stress).");
sbGuideCol1.addParagraphBreak();
sbGuideCol1.addText("•  Character Creation: Step-by-step procedures for assigning attributes, training skills, and choosing starting equipment.");
sbGuideCol1.addParagraphBreak();
sbGuideCol1.addText("•  Traits & Lineages: Origin traits, cultural adaptations, and operational quirks that distinguish operative physiology.");
sbGuideCol1.addParagraphBreak();
sbGuideCol1.addText("•  Classes & MANTLE Rigs: The five operational chassis: Conduit, Hazard, Pilot, Vanguard, and Weaver.");
sbGuideCol1.addParagraphBreak();
sbGuideCol1.addText("•  Advancement: How operatives earn experience, refine skills, upgrade attributes, and achieve career milestones.");
sbGuideCol1.addParagraphBreak();
sbGuideCol1.addText("•  Interlude: Post War Head- and Heartaches.");

const defGuideCol1 = FrameTextNodeDefinition.createFromStoryBuilder({ x: R_COL1_X, y: guidePartsY, width: COL_W, height: guidePartsH }, sbGuideCol1);
doc.addNode(defGuideCol1, spread2);


// Column 2: Part III, Part IV, Part V
const sbGuideCol2 = StoryBuilder.create();
sbGuideCol2.setToFrameTextDefaultStyle(doc.dpi, doc.format);

// Part III: Advanced Operations
sbGuideCol2.setGlyphAtts(gaH3);
sbGuideCol2.setParagraphAtts(paH3Top);
sbGuideCol2.addText("Part III: Advanced Operations");
sbGuideCol2.addParagraphBreak();

sbGuideCol2.setGlyphAtts(gaItalic);
sbGuideCol2.setParagraphAtts(paItalic);
sbGuideCol2.addText("Tactical systems, armaments, voidcraft, and operational downtime.");
sbGuideCol2.addParagraphBreak();

sbGuideCol2.setGlyphAtts(gaBody);
sbGuideCol2.setParagraphAtts(paBody);
sbGuideCol2.addText("•  Tactical Combat: Movement, grid and abstract occupancy, close-quarters combat (CQC), dynamic cover, and damage resolution.");
sbGuideCol2.addParagraphBreak();
sbGuideCol2.addText("•  Personal Armory & Hardware: Catalogs of Firearms, Melee Weapons, Armor, Field Gear, and rare Precursor Exotic Hardware.");
sbGuideCol2.addParagraphBreak();
sbGuideCol2.addText("•  Starships & Space Combat: Comprehensive rules for Starship Operations, Brachistochrone burns, Ship Weapons, Internal Modules, and The Hangar Bay.");
sbGuideCol2.addParagraphBreak();
sbGuideCol2.addText("•  Downtime & Operations: The 24-hour downtime cycle, shifts, long rests, medical recovery, starship maintenance, and freelance gigs.");
sbGuideCol2.addParagraphBreak();
sbGuideCol2.addText("•  Interlude: The Mathematics of the Great Tithe.");
sbGuideCol2.addParagraphBreak();

// Part IV: Worlds of the Sphere (H3 with 70 pt spaceBefore!)
sbGuideCol2.setGlyphAtts(gaH3);
sbGuideCol2.setParagraphAtts(paH3);
sbGuideCol2.addText("Part IV: Worlds of the Sphere");
sbGuideCol2.addParagraphBreak();

sbGuideCol2.setGlyphAtts(gaItalic);
sbGuideCol2.setParagraphAtts(paItalic);
sbGuideCol2.addText("The celestial gazetteer, faction dossiers, history, and fiction of the setting.");
sbGuideCol2.addParagraphBreak();

sbGuideCol2.setGlyphAtts(gaBody);
sbGuideCol2.setParagraphAtts(paBody);
sbGuideCol2.addText("•  Planetary Gazetteer: Macro-engineering of the Sphere, the Newcomer heartland in the Fume Cluster, Landfall, and the X'ara Cluster.");
sbGuideCol2.addParagraphBreak();
sbGuideCol2.addText("•  Factions & Powers: Dossiers on the Sovereign Colonies, Megacorporations, the Flotilla, and the Underworld.");
sbGuideCol2.addParagraphBreak();
sbGuideCol2.addText("•  The Corsairs & Timeline: The legal mandate of Corsairs, the 500-year history since arrival, and master anthology Stories of the Sphere.");
sbGuideCol2.addParagraphBreak();
sbGuideCol2.addText("•  Interlude: Space Tourism.");
sbGuideCol2.addParagraphBreak();

// Part V: Running the Game (H3 with 70 pt spaceBefore!)
sbGuideCol2.setGlyphAtts(gaH3);
sbGuideCol2.setParagraphAtts(paH3);
sbGuideCol2.addText("Part V: Running the Game");
sbGuideCol2.addParagraphBreak();

sbGuideCol2.setGlyphAtts(gaItalic);
sbGuideCol2.setParagraphAtts(paItalic);
sbGuideCol2.addText("Procedures, campaign structures, threat rosters, and mission generators.");
sbGuideCol2.addParagraphBreak();

sbGuideCol2.setGlyphAtts(gaBody);
sbGuideCol2.setParagraphAtts(paBody);
sbGuideCol2.addText("•  Running the Game: Core guidelines for Time Management, Social Interactions, Stealth & Infiltration, Investigation, Chases & Pursuits, and Tracks.");
sbGuideCol2.addParagraphBreak();
sbGuideCol2.addText("•  Threats of the Sphere: Tactical profiles and statblocks for corporate security, pirates, drone swarms, void horrors, and NPC Guidelines.");
sbGuideCol2.addParagraphBreak();
sbGuideCol2.addText("•  Missions & Contracts: Procedural Mission Generator and Open Play Contracts.");

const defGuideCol2 = FrameTextNodeDefinition.createFromStoryBuilder({ x: R_COL2_X, y: guidePartsY, width: COL_W, height: guidePartsH }, sbGuideCol2);
doc.addNode(defGuideCol2, spread2);

// Page 5 Running Footer Page Number
addTextFrame(spread2, R_COL1_X + CONTENT_W - 100, 3365, 100, 40, sb => {
    const ga = sb.glyphAtts;
    if (fontHeading) ga.font = fontHeading;
    ga.height = 28;
    ga.brushFill = FillDescriptor.createSolid(colAmberDark);
    const pa = sb.paragraphAtts;
    pa.alignXType = ParagraphAlignXType.Right;
    sb.setGlyphAtts(ga);
    sb.setParagraphAtts(pa);
    sb.addText("2");
});

// Save to Desktop sandbox path first
const savePath = Application.userDesktopPath + '/Corsair_Core_Rulebook.afpub';
console.log('SESSION_UUID=' + doc.sessionUuid);
console.log('Saving document to:', savePath);
doc.saveAs(savePath);
console.log('Document successfully saved!');
"""

    send_rpc({
        'jsonrpc': '2.0',
        'id': 3,
        'method': 'tools/call',
        'params': {'name': 'execute_script', 'arguments': {'script': js_script}}
    })
    res = wait_for_id(3, timeout=60)
    content = res.get('result', {}).get('content', [{}])[0].get('text', '')
    print("Affinity JS Output:\n", content)

    # Extract session UUID
    import re
    m = re.search(r'SESSION_UUID=([A-Fa-f0-9\-]+)', content)
    doc_uuid = m.group(1) if m else None
    print(f"Captured Document Session UUID: {doc_uuid}")

    # Move from Desktop to repo affinity/
    repo_dir = r"c:\Users\csisz\IdeaProjects\corsair"
    desktop_afpub = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'Corsair_Core_Rulebook.afpub')
    dest_afpub = os.path.join(repo_dir, 'affinity', 'Corsair_Core_Rulebook.afpub')
    if os.path.exists(desktop_afpub):
        shutil.copy2(desktop_afpub, dest_afpub)
        print(f"\n[OK] Saved and mirrored native project to: {dest_afpub} ({os.path.getsize(dest_afpub)} bytes)")

    print("\n=== Step 4: Rendering and Exporting Visual Previews of All Spreads ===")
    import base64

    if doc_uuid:
        for sp_idx in range(3):
            send_rpc({
                'jsonrpc': '2.0',
                'id': 10 + sp_idx,
                'method': 'tools/call',
                'params': {'name': 'render_spread', 'arguments': {'document_session_uuid': doc_uuid, 'spread_index': sp_idx}}
            })
            sp_res = wait_for_id(10 + sp_idx, timeout=30)
            c_list = sp_res.get('result', {}).get('content', [])
            if c_list:
                img_b64 = c_list[0].get('data') or c_list[0].get('text', '')
                if img_b64 and len(img_b64) > 100:
                    preview_filename = f"spread_{sp_idx}_cover.jpg" if sp_idx == 0 else (
                        f"spread_{sp_idx}_preamble_toc.jpg" if sp_idx == 1 else f"spread_{sp_idx}_intro_guide.jpg"
                    )
                    out_path = os.path.join(repo_dir, 'affinity', preview_filename)
                    with open(out_path, 'wb') as f:
                        f.write(base64.b64decode(img_b64))
                    print(f"  [OK] Exported visual preview: {preview_filename} ({os.path.getsize(out_path)} bytes)")
                else:
                    print(f"  [WARN] Spread {sp_idx} render returned empty or error: {img_b64[:100]}")
    else:
        print("  [WARN] No document UUID captured; skipping render_spread.")

    print("\n=== Brand New Corsair Rulebook Generation Complete! ===")

if __name__ == '__main__':
    run_corsair_design_pipeline()
