import subprocess
import time
import json
import urllib.request
import websocket
from pathlib import Path

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = Path("html/04_Armory_and_Gear.html").resolve()
url = html_path.as_uri()

port = 9334
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
        const p76 = document.getElementById('firearms-rifles-heavy');
        const body = p76.querySelector('.page-body');
        const tables = p76.querySelectorAll('table');
        const tableInfo = Array.from(tables).map(t => ({
            class: t.className,
            scrollWidth: t.scrollWidth,
            clientWidth: t.clientWidth,
            offsetWidth: t.offsetWidth
        }));
        const children = Array.from(body.children).map(c => ({
            tag: c.tagName,
            class: c.className,
            scrollWidth: c.scrollWidth,
            clientWidth: c.clientWidth,
            offsetWidth: c.offsetWidth,
            scrollHeight: c.scrollHeight,
            offsetHeight: c.offsetHeight
        }));
        return {
            bodyScrollW: body.scrollWidth,
            bodyClientW: body.clientWidth,
            tableInfo,
            children
        };
    })()
    """
    msg = json.dumps({
        "id": 1,
        "method": "Runtime.evaluate",
        "params": {"expression": js_code, "returnByValue": True}
    })
    ws.send(msg)
    resp = json.loads(ws.recv())
    val = resp.get("result", {}).get("result", {}).get("value", {})
    print(json.dumps(val, indent=2))
    ws.close()
finally:
    proc.terminate()
    proc.wait()
