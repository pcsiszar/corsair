import subprocess
import time
import json
import urllib.request
import websocket
from pathlib import Path

def test_ch07_dom():
    chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    html_path = Path("html/07_World_of_the_Sphere.html").resolve()
    url = html_path.as_uri()

    port = 9347
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
                const body = page.querySelector('.page-body') || page.querySelector('.fiction-page-body');
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

def main():
    pages = test_ch07_dom()
    print(f"{'Page':<6} {'ID':<26} {'UsedH':<8} {'Fill':<8} {'Gap(mm)':<10} {'Overflow':<10} {'Status'}")
    print("-" * 80)
    for p in pages:
        overflowPx = p['overflowPx']
        fillPercent = p['fill'].replace('%', '')
        status = "[OVERFLOW]" if overflowPx > 0 else ("[LOW FILL]" if float(fillPercent) < 70.0 else "[OK]")
        print(f"P{p['page']:<5} {p['id']:<26} {p['usedH']}px    {p['fill']:<8} {p['gapMm']}mm     {overflowPx}px       {status}")

if __name__ == "__main__":
    main()
