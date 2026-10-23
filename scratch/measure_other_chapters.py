import subprocess
import time
import json
import urllib.request
import websocket
from pathlib import Path

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

for ch in ["01_Core_Mechanics.html", "02_Character_Creation.html"]:
    html_path = Path("html", ch).resolve()
    url = html_path.as_uri()

    port = 9336
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
        print(f"\n=== {ch} ===")
        for p in val:
            print(f"Page {p['page']:2s}: BottomGap={p['bottomGapMm']:6s}mm  Fill={p['fillPercent']}")
        ws.close()
    finally:
        proc.terminate()
        proc.wait()
