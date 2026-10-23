import subprocess
import time
import json
import urllib.request
import websocket
from pathlib import Path

import sys

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
default_file = "html/04_Armory_and_Gear.html"
target_arg = sys.argv[1] if len(sys.argv) > 1 else default_file
html_path = Path(target_arg).resolve()
url = html_path.as_uri()

port = 9335
proc = subprocess.Popen([
    chrome_exe,
    "--headless=new",
    f"--remote-debugging-port={port}",
    "--remote-allow-origins=*",
    "--disable-gpu",
    "--no-sandbox",
    url
])

try:
    time.sleep(2)
    req = urllib.request.urlopen(f"http://127.0.0.1:{port}/json")
    targets = json.loads(req.read().decode())
    page_target = [t for t in targets if t.get("type") == "page"][0]
    ws_url = page_target["webSocketDebuggerUrl"]

    ws = websocket.create_connection(ws_url)

    js_code = """
    (() => {
        const results = [];
        document.querySelectorAll('.book-page').forEach((page, i) => {
            const pageNum = page.querySelector('.page-num') ? page.querySelector('.page-num').textContent.trim() : (i + 1);
            const body = page.querySelector('.page-body');
            const footer = page.querySelector('.page-running-footer');
            const footerTop = footer ? footer.getBoundingClientRect().top : 0;
            
            // Find lowest bottom coordinate of all elements in body
            let lowestBottom = 0;
            if (body) {
                const rect = body.getBoundingClientRect();
                Array.from(body.querySelectorAll('*')).forEach(el => {
                    const r = el.getBoundingClientRect();
                    if (r.bottom > lowestBottom) {
                        lowestBottom = r.bottom;
                    }
                });
                const bodyHeight = rect.height;
                const usedHeight = lowestBottom - rect.top;
                const bottomGapPx = footerTop - lowestBottom;
                const bottomGapMm = bottomGapPx * 25.4 / 96;
                const fillPercent = ((usedHeight / bodyHeight) * 100).toFixed(1);
                results.push({
                    page: pageNum,
                    id: page.id,
                    bodyHeight: Math.round(bodyHeight),
                    usedHeight: Math.round(usedHeight),
                    bottomGapMm: bottomGapMm.toFixed(1),
                    fillPercent: fillPercent + '%'
                });
            }
        });
        return results;
    })()
    """
    msg = json.dumps({
        "id": 1,
        "method": "Runtime.evaluate",
        "params": {"expression": js_code, "returnByValue": True}
    })
    ws.send(msg)
    resp = json.loads(ws.recv())
    val = resp.get("result", {}).get("result", {}).get("value", [])
    print(f"{'Page':5s} {'ID':26s} {'BodyH':7s} {'UsedH':7s} {'BottomGap':12s} {'Fill%':6s}")
    print("-" * 70)
    for p in val:
        print(f"Page {p['page']:2s} {p['id']:26s} {p['bodyHeight']:5d}px {p['usedHeight']:5d}px {p['bottomGapMm']:8s}mm {p['fillPercent']:6s}")
    ws.close()
finally:
    proc.terminate()
    proc.wait()
