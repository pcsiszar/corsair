import subprocess
import time
import json
import urllib.request
import websocket
from pathlib import Path

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = Path("html/04_Armory_and_Gear.html").resolve()
url = html_path.as_uri()

port = 9338
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
            if (body) {
                results.push({
                    page: pageNum,
                    id: page.id,
                    clientWidth: body.clientWidth,
                    scrollWidth: body.scrollWidth,
                    overflowPx: body.scrollWidth - body.clientWidth,
                    hasCol3: body.scrollWidth > body.clientWidth + 5
                });
            }
        });
        return results;
    })()
    """
    ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js_code, "returnByValue": True}}))
    resp = json.loads(ws.recv())
    val = resp.get("result", {}).get("result", {}).get("value", [])
    print(f"{'Page':6s} {'ID':30s} {'ClientW':8s} {'ScrollW':8s} {'Overflow':10s} {'HasCol3?'}")
    print("-" * 75)
    for p in val:
        print(f"Page {p['page']:2s} {p['id']:30s} {p['clientWidth']:6d}px {p['scrollWidth']:6d}px {p['overflowPx']:8d}px {str(p['hasCol3']):8s}")
    ws.close()
finally:
    proc.terminate()
    proc.wait()
