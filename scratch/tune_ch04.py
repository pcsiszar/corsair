import subprocess
import time
import json
import urllib.request
import websocket
from pathlib import Path

def test_ch04_dom():
    chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    html_path = Path("html/04_Armory_and_Gear.html").resolve()
    url = html_path.as_uri()

    port = 9339
    proc = subprocess.Popen([chrome_exe, "--headless=new", f"--remote-debugging-port={port}", "--remote-allow-origins=*", "--disable-gpu", "--no-sandbox", url])
    try:
        time.sleep(2)
        req = urllib.request.urlopen(f"http://127.0.0.1:{port}/json")
        targets = json.loads(req.read().decode())
        page_target = [t for t in targets if t.get("type") == "page"][0]
        ws = websocket.create_connection(page_target["webSocketDebuggerUrl"])
        
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
                        if (r.bottom > lowestBottom) lowestBottom = r.bottom;
                    });
                    const bodyHeight = rect.height;
                    const usedHeight = lowestBottom - rect.top;
                    const bottomGapMm = (footerTop - lowestBottom) * 25.4 / 96;
                    const fillPercent = ((usedHeight / bodyHeight) * 100).toFixed(1);
                    const overflowPx = body.scrollWidth - body.clientWidth;
                    results.push({
                        page: pageNum,
                        id: page.id,
                        bodyH: Math.round(bodyHeight),
                        usedH: Math.round(usedHeight),
                        gapMm: bottomGapMm.toFixed(1),
                        fill: fillPercent + '%',
                        overflowPx: overflowPx
                    });
                }
            });
            return results;
        })()
        """
        ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js_code, "returnByValue": True}}))
        resp = json.loads(ws.recv())
        val = resp.get("result", {}).get("result", {}).get("value", [])
        ws.close()
        return val
    finally:
        proc.terminate()
        proc.wait()

if __name__ == "__main__":
    metrics = test_ch04_dom()
    print(f"{'Page':6s} {'ID':32s} {'BodyH':7s} {'UsedH':7s} {'GapMm':8s} {'Fill%':7s} {'Overflow'}")
    print("-" * 80)
    for m in metrics:
        status = "OK" if m['overflowPx'] == 0 and float(m['gapMm']) <= 45 else "NEEDS TUNE"
        print(f"Page {m['page']:2s} {m['id']:32s} {m['bodyH']:5d}px {m['usedH']:5d}px {m['gapMm']:6s}mm {m['fill']:6s} {m['overflowPx']:4d}px  [{status}]")
