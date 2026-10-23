import subprocess
import time
import json
import urllib.request
import websocket
from pathlib import Path

def test_ch06_dom():
    chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    html_path = Path("html/06_Downtime_and_Operations.html").resolve()
    url = html_path.as_uri()

    port = 9345
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
    results = test_ch06_dom()
    print(f"{'Page':<6} {'ID':<30} {'UsedH':<8} {'Fill':<8} {'Gap(mm)':<10} {'Overflow':<10} {'Status'}")
    print("-" * 80)
    for r in results:
        fill_val = float(r['fill'].replace('%', ''))
        status = "OK"
        if fill_val < 80.0:
            status = "LOW FILL"
        elif fill_val > 96.0 or r['overflowPx'] > 0:
            status = "OVERFLOW"
        print(f"P{r['page']:<5} {r['id']:<30} {r['usedH']}px    {r['fill']:<8} {r['gapMm']}mm     {r['overflowPx']}px       [{status}]")
