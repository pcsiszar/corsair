import subprocess, time, json, urllib.request, websocket
from pathlib import Path

# Test with single-column on page-body
rows1 = "".join([f'<tr><td class="td-d100">{i:02d}</td><td class="td-title">Gig Title {i}</td><td class="td-desc">Detailed situation and description for odd job {i}.</td><td class="td-test">Instinct + Know</td></tr>' for i in range(1, 26)])
rows2 = "".join([f'<tr><td class="td-d100">{i:02d}</td><td class="td-title">Gig Title {i}</td><td class="td-desc">Detailed situation and description for odd job {i}.</td><td class="td-test">Instinct + Know</td></tr>' for i in range(26, 51)])

html = f"""<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="../assets/css/corsair-variables.css">
<link rel="stylesheet" href="../assets/css/corsair-typography.css">
<link rel="stylesheet" href="../assets/css/corsair-components.css">
<link rel="stylesheet" href="../assets/css/corsair-layout.css">
<link rel="stylesheet" href="../assets/css/corsair-print.css">
<style>
.gig-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; width: 100%; }}
.g-table {{ width: 100%; border-collapse: collapse; font-size: 6.7pt; line-height: 1.18; }}
.g-table th {{ background: rgba(16,20,26,0.95); color: var(--amber-dark); padding: 1.5px 3px; font-weight: 700; text-align: left; border-bottom: 1px solid var(--amber-dark); }}
.g-table td {{ padding: 1.5px 3px; border-bottom: 1px solid rgba(255,255,255,0.06); vertical-align: top; }}
.td-d100 {{ font-family: var(--font-mono); font-weight: 700; color: var(--amber-dark); width: 18px; }}
.td-title {{ font-family: var(--font-heading); font-weight: 700; color: var(--text-bright); width: 75px; }}
.td-desc {{ color: var(--text-dim); }}
.td-test {{ font-family: var(--font-mono); font-size: 6.2pt; color: var(--cyan-bright); white-space: nowrap; text-align: right; width: 70px; }}
</style>
</head>
<body class="book-screen-canvas">
<div class="book-page spread-bg-1" id="test-p">
    <div class="page-running-header"><span>Act III</span><span>Chapter 06</span></div>
    <div class="page-body single-column" style="margin-top: 1mm;">
        <div style="font-family: var(--font-heading); font-size: 10pt; font-weight: 700; color: var(--amber-dark); margin-bottom: 2mm; border-bottom: 1.5px solid var(--amber-dark); padding-bottom: 1.5px;">GIGS 01–50</div>
        <div class="gig-grid">
            <table class="g-table">
                <thead><tr><th class="td-d100">d100</th><th class="td-title">Title</th><th class="td-desc">Situation</th><th class="td-test">Test</th></tr></thead>
                <tbody>{rows1}</tbody>
            </table>
            <table class="g-table">
                <thead><tr><th class="td-d100">d100</th><th class="td-title">Title</th><th class="td-desc">Situation</th><th class="td-test">Test</th></tr></thead>
                <tbody>{rows2}</tbody>
            </table>
        </div>
        <div class="callout callout-cyan" style="margin-top: 2.5mm;">
            <div class="callout-title">Dockside Rumors</div>
            <p style="font-size: 7.9pt; line-height: 1.34; margin: 0;">Dockside rumors and gossip across the concourse.</p>
        </div>
    </div>
    <div class="page-running-footer"><span>Vol I</span><span class="page-num">100</span></div>
</div>
</body>
</html>"""

Path("scratch/test_grid.html").write_text(html, encoding="utf-8")

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
url = Path("scratch/test_grid.html").resolve().as_uri()
port = 9350
proc = subprocess.Popen([chrome_exe, "--headless=new", f"--remote-debugging-port={port}", "--remote-allow-origins=*", "--disable-gpu", "--no-sandbox", url])
try:
    time.sleep(2)
    req = urllib.request.urlopen(f"http://127.0.0.1:{port}/json")
    targets = json.loads(req.read().decode())
    page_target = [t for t in targets if t.get("type") == "page"][0]
    ws = websocket.create_connection(page_target["webSocketDebuggerUrl"])
    js = """
    (() => {
        const body = document.querySelector('.page-body');
        const footer = document.querySelector('.page-running-footer');
        let lowest = 0;
        Array.from(body.querySelectorAll('*')).forEach(el => {
            const r = el.getBoundingClientRect();
            if (r.bottom > lowest) lowest = r.bottom;
        });
        const rect = body.getBoundingClientRect();
        return {
            usedH: Math.round(lowest - rect.top),
            bodyH: Math.round(rect.height),
            fill: ((lowest - rect.top) / rect.height * 100).toFixed(1) + '%',
            overflowPx: body.scrollWidth - body.clientWidth,
            scrollW: body.scrollWidth,
            clientW: body.clientWidth
        };
    })()
    """
    ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
    resp = json.loads(ws.recv())
    print(resp["result"]["result"]["value"])
finally:
    proc.terminate()
