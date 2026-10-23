import subprocess
import time
import json
import urllib.request
import websocket
from pathlib import Path

def test_interlude_dom():
    chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    html_path = Path("html/06b_Interlude_Space_Tourism.html").resolve()
    url = html_path.as_uri()

    port = 9346
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
                const body = page.querySelector('.fiction-page-body') || page.querySelector('.page-body');
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

        print(f"{'Page':<6} {'ID':<26} {'UsedH':<8} {'Fill':<8} {'Gap(mm)':<10} {'Overflow':<10} {'Status'}")
        print("-" * 80)
        for row in val:
            p_fill = float(row['fill'].replace('%', ''))
            overflow = row['overflowPx']
            status = "[OK]" if (75.0 <= p_fill <= 95.0 and overflow == 0) else ("[OVERFLOW]" if overflow > 0 or p_fill > 98.0 else "[LOW FILL]")
            print(f"P{row['page']:<5} {row['id']:<26} {row['usedH']}px    {row['fill']:<8} {row['gapMm']}mm     {overflow}px       {status}")
    finally:
        proc.terminate()

if __name__ == "__main__":
    test_interlude_dom()
