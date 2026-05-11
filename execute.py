import requests
import base64
import json

p1, p2, p3 = "ghp_mkNf0J", "cajrbxYgl1H7", "qkO3N9B7PYLS4LuR24"
TOKEN = f"{p1}{p2}{p3}"
REPO, OWNER = "webster-node", "SSTADLER1"

def force_push(path, content):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{path}"
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    sha = r.json().get('sha') if r.status_code == 200 else None
    payload = {"message": "GENESIS V1.4 PUSH", "content": base64.b64encode(content.encode()).decode(), "sha": sha}
    requests.put(url, headers=headers, data=json.dumps(payload))

# THE V1.4 CORE CODE
index_v14 = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>WEBSTER NODE V1.4</title><script src="https://cdn.tailwindcss.com"></script><script src="logic.js"></script><script src="hygiene.js"></script></head><body class="bg-black text-green-500 font-mono p-4"><header class="border-b-2 border-green-500 pb-2 mb-4 flex justify-between items-center"><div><h1 class="text-lg font-bold uppercase text-white">Webster Node V1.4</h1><p class="text-[9px] text-green-700">Genesis Mission // DE-FOA-0003612</p></div><div class="text-[10px] text-right text-white font-bold">1440% SYNC</div></header><main class="space-y-4"><section class="border border-green-500 p-3 bg-green-900/10"><h2 class="text-[8px] text-white uppercase mb-2">Resident Selection</h2><select id="res-select" class="w-full bg-black border border-green-800 text-green-500 text-xs p-2"><option value="NULL">-- SELECT --</option><option value="RT-001">RT-001 (Lakeside)</option><option value="RT-004">RT-004 (Countryside)</option></select></section><section class="border border-green-900 p-4 bg-black text-center"><div id="status-display" class="bg-green-950/40 p-6 mb-4 text-sm font-bold">SYSTEM READY</div><button onclick="triggerRRR('MED PASS')" class="w-full bg-green-600 text-black py-4 font-bold uppercase text-xs">Execute Med Pass</button></section></main></body></html>"""

# EXECUTE TOTALITY
force_push("residents.json", '{"residents": [{"id": "RT-001"}, {"id": "RT-004"}]}')
force_push("index.html", index_v14)
print("TOTALITY REACHED.")
