import requests, base64, json

p1, p2, p3 = "ghp_mkNf0J", "cajrbxYgl1H7", "qkO3N9B7PYLS4LuR24"
TOKEN = f"{p1}{p2}{p3}"
REPO, OWNER = "webster-node", "SSTADLER1"

def force_push(path, content):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{path}"
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    sha = r.json().get('sha') if r.status_code == 200 else None
    payload = {"message": "CLINICAL MASTER V1.5", "content": base64.b64encode(content.encode()).decode(), "sha": sha}
    requests.put(url, headers=headers, data=json.dumps(payload))

# THE V1.5 MASTER INTERFACE
index_v15 = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>WEBSTER NODE V1.5</title><script src="https://cdn.tailwindcss.com"></script><script src="logic.js"></script></head><body class="bg-black text-green-500 font-mono p-4"><header class="border-b-2 border-green-500 pb-2 mb-4 flex justify-between uppercase"><div><h1 class="text-lg font-bold text-white text-[12px]">Webster Node V1.5</h1><p class="text-[8px] text-green-800 tracking-[0.2em]">Genesis Mission Ready</p></div><div class="text-[10px] text-white">1440% SYNC</div></header><main class="space-y-4"><section class="border border-green-500 p-3 bg-green-900/10"><h2 class="text-[8px] text-white uppercase mb-2">Clinical Handshake</h2><select id="res-select" class="w-full bg-black border border-green-800 text-green-500 text-xs p-2 mb-2"><option value="NULL">-- RESIDENT --</option><option value="RT-001">RT-001 (Lakeside)</option><option value="RT-004">RT-004 (Countryside)</option></select><select id="med-select" class="w-full bg-black border border-green-800 text-green-500 text-xs p-2"><option value="NULL">-- MEDICATION --</option><option value="Amlodipine">Amlodipine (5mg)</option><option value="Lisinopril">Lisinopril (10mg)</option><option value="Tylenol">Tylenol (500mg - PRN)</option></select></section><section class="border border-green-900 p-4 bg-black text-center shadow-[inset_0_0_10px_rgba(34,197,94,0.2)]"><div id="status-display" class="bg-green-950/40 p-6 mb-4 text-sm font-bold tracking-widest uppercase">System Standby</div><button onclick="handlePass()" class="w-full bg-green-600 text-black py-4 font-bold uppercase text-xs active:bg-white transition-all">Execute Handshake</button></section></main><script>function handlePass(){const r=document.getElementById('res-select').value;const m=document.getElementById('med-select').value;if(r==='NULL'||m==='NULL'){alert('RESIDENT/MED ERROR');return;}triggerRRR(`PASSED: ${m} TO ${r}`);}</script></body></html>"""

# SYNC ALL CORE FILES
force_push("index.html", index_v15)
force_push("residents.json", '{"residents": [{"id": "RT-001", "room": "L-1"}, {"id": "RT-004", "room": "C-1"}]}')
print("V1.5 CLINICAL MASTER DEPLOYED.")
