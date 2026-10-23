import urllib.request
import json
import websocket

tabs = json.loads(urllib.request.urlopen('http://localhost:9222/json').read())
tab = next(t for t in tabs if '04_Armory' in t.get('url', ''))
ws = websocket.create_connection(tab['webSocketDebuggerUrl'])

js = """
(() => {
    const pages = ['small-arms-handguns-smgs', 'firearms-rifles-heavy', 'melee-weapons-fundamentals', 'armor-medium-heavy-action'];
    let res = {};
    for (let pid of pages) {
        const el = document.getElementById(pid);
        let bad = [];
        for (let c of el.querySelectorAll('*')) {
            if (c.scrollWidth > c.clientWidth + 2) {
                bad.push({tag: c.tagName, cls: c.className.slice(0, 30), sw: c.scrollWidth, cw: c.clientWidth, txt: c.textContent.slice(0, 40).trim()});
            }
        }
        res[pid] = bad;
    }
    return JSON.stringify(res, null, 2);
})()
"""

ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js}}))
val = json.loads(ws.recv())['result']['result']['value']
print(val)
ws.close()
