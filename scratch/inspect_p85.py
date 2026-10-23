import subprocess
import time
import json
import urllib.request
import websocket

def inspect():
    chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    proc = subprocess.Popen([chrome_exe, "--headless=new", "--remote-debugging-port=9342", "--remote-allow-origins=*", "--disable-gpu", "--no-sandbox", "file:///C:/Users/csisz/IdeaProjects/corsair/html/05_Starships.html"])
    time.sleep(2)
    req = urllib.request.urlopen("http://127.0.0.1:9342/json")
    targets = json.loads(req.read().decode())
    page_target = [t for t in targets if t.get("type") == "page"][0]
    ws = websocket.create_connection(page_target["webSocketDebuggerUrl"])
    
    js = """
    (() => {
        const page = document.querySelector('#bridge-roles-and-seats');
        const body = page.querySelector('.page-body');
        const rect = body.getBoundingClientRect();
        return Array.from(body.children).map(c => {
            const r = c.getBoundingClientRect();
            return {
                tag: c.tagName,
                text: c.textContent.trim().slice(0, 35),
                left: Math.round(r.left - rect.left),
                top: Math.round(r.top - rect.top),
                bottom: Math.round(r.bottom - rect.top),
                right: Math.round(r.right - rect.left)
            };
        });
    })()
    """
    ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
    msg = json.loads(ws.recv())
    res = msg.get("result", {}).get("result", {}).get("value")
    ws.close()
    proc.terminate()
    proc.wait()
    for item in res:
        print(f"{item['tag']:4s} L:{item['left']:3d} R:{item['right']:3d} T:{item['top']:3d} B:{item['bottom']:3d} | {item['text']}")

if __name__ == "__main__":
    inspect()
