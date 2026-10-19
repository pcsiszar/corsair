import urllib.request, json, threading, queue, os

def test():
    q = queue.Queue()
    req = urllib.request.Request('http://[::1]:6767/sse', headers={'Accept': 'text/event-stream'})

    def read_sse():
        with urllib.request.urlopen(req) as response:
            for line in response:
                line_str = line.decode('utf-8').strip()
                if line_str.startswith('data:'):
                    try: q.put(json.loads(line_str[5:].strip()))
                    except: q.put(line_str[5:].strip())

    threading.Thread(target=read_sse, daemon=True).start()
    session_endpoint = q.get(timeout=5)
    while not isinstance(session_endpoint, str) or not session_endpoint.startswith('/'):
        session_endpoint = q.get(timeout=5)
    post_url = 'http://localhost:6767' + session_endpoint

    def send_rpc(msg):
        data = json.dumps(msg).encode('utf-8')
        r = urllib.request.Request(post_url, data=data, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(r) as res: pass

    def wait_for_id(req_id, timeout=30):
        while True:
            item = q.get(timeout=timeout)
            if isinstance(item, dict) and item.get('id') == req_id:
                return item

    send_rpc({'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {'protocolVersion': '2024-11-05', 'capabilities': {}, 'clientInfo': {'name': 'Antigravity', 'version': '1.0.0'}}})
    wait_for_id(1)
    send_rpc({'jsonrpc': '2.0', 'method': 'notifications/initialized'})

    # Test script in Affinity
    test_js = r"""
const { Document } = require('/document.js');
const { NodeChildrenOnly, NodeChildType } = require('/nodes.js');

const docs = Array.from(Document.all);
console.log("Open documents count:", docs.length);
if (docs.length > 0) {
    const doc = docs[0];
    console.log("Document session UUID:", doc.sessionUuid);
    const spreads = Array.from(new NodeChildrenOnly(doc.rootNode.handle, NodeChildType.Spread, false));
    console.log("Spread count:", spreads.length);
}
"""
    send_rpc({'jsonrpc': '2.0', 'id': 2, 'method': 'tools/call', 'params': {'name': 'execute_script', 'arguments': {'script': test_js}}})
    res = wait_for_id(2)
    print("Result:", res.get('result', {}).get('content', [{}])[0].get('text', ''))

if __name__ == '__main__':
    test()
