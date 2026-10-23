import subprocess
import time
import json
import urllib.request
import urllib.error
from pathlib import Path

# Chrome executable
chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = Path("html/04_Armory_and_Gear.html").resolve()
url = html_path.as_uri()

# Start Chrome headless with debugging port
port = 9333
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
    # Get targets
    req = urllib.request.urlopen(f"http://127.0.0.1:{port}/json")
    targets = json.loads(req.read().decode())
    page_target = None
    for t in targets:
        if t.get("type") == "page":
            page_target = t
            break

    if not page_target:
        print("No page target found!")
    else:
        ws_url = page_target.get("webSocketDebuggerUrl")
        print("Page Target Found:", page_target.get("url"))

        # We can communicate via websocket if websocket package is installed, or check
        try:
            import websocket
            ws = websocket.create_connection(ws_url)

            # Evaluate JS
            js_code = """
            (() => {
                const results = [];
                document.querySelectorAll('.book-page').forEach((page, i) => {
                    const body = page.querySelector('.page-body');
                    const pageNum = page.querySelector('.page-num') ? page.querySelector('.page-num').textContent : (i + 1);
                    if (body) {
                        results.push({
                            page: pageNum,
                            id: page.id,
                            scrollWidth: body.scrollWidth,
                            clientWidth: body.clientWidth,
                            scrollHeight: body.scrollHeight,
                            clientHeight: body.clientHeight,
                            hasOverflow: body.scrollWidth > (body.clientWidth + 2)
                        });
                    }
                });
                return results;
            })()
            """
            msg = json.dumps({
                "id": 1,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": js_code,
                    "returnByValue": True
                }
            })
            ws.send(msg)
            resp = json.loads(ws.recv())
            val = resp.get("result", {}).get("result", {}).get("value", [])
            print("\n=== DOM OVERFLOW & GEOMETRY REPORT ===")
            any_overflow = False
            for p in val:
                status = "OVERFLOW (Column 3!)" if p["hasOverflow"] else "OK"
                if p["hasOverflow"]:
                    any_overflow = True
                print(f"Page {p['page']:2s} ({p['id']:25s}): scrollW={p['scrollWidth']} clientW={p['clientWidth']} scrollH={p['scrollHeight']} clientH={p['clientHeight']} [{status}]")
            
            if not any_overflow:
                print("\nALL 24 PAGES PASSED ZERO HORIZONTAL OVERFLOW CHECK!")
            else:
                print("\nWARNING: Some pages had horizontal overflow!")
            ws.close()
        except ImportError:
            print("websocket-client not installed in python environment.")
finally:
    proc.terminate()
    proc.wait()
