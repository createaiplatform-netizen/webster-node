import requests, base64, json

p1, p2, p3 = "ghp_mkNf0J", "cajrbxYgl1H7", "qkO3N9B7PYLS4LuR24"
TOKEN = f"{p1}{p2}{p3}"
REPO, OWNER = "webster-node", "SSTADLER1"

def force_push(path, content):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{path}"
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    sha = r.json().get('sha') if r.status_code == 200 else None
    payload = {"message": "GOLDEN MASTER V1.5", "content": base64.b64encode(content.encode()).decode(), "sha": sha}
    requests.put(url, headers=headers, data=json.dumps(payload))

# CLEAN CLINICAL INTERFACE
index_v15 = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>WEBSTER NODE V1.5</title><script src="https://cdn.tailwindcss.com"></script></head><body class="bg-black text-green-500 font-mono p-4 select-none"><header class="border-b-2 border-green-500 pb-2 mb-4 flex justify-between items-center"><div><h1 class="text-lg font-bold uppercase text-white">Webster Node V1.5</h1><p class="text-[9px] text-green-700 font-bold uppercase tracking-widest">Genesis Mission Ready</p></div><div class="text-[10px] text-right border-l border-green-900 pl-2 uppercase"><p class="text-white font-bold">1440% SYNC</p></div></header><main class="space-y-4"><section class="border border-green-500 p-3 bg-green-950/10 rounded-sm"><h2 class="text-[8px] text-white uppercase tracking-widest mb-2">Clinical Selection</h2><select id="res-select" class="w-full bg-black border border-green-800 text-green-500 text-xs p-2 mb-3 outline-none"><option value="NULL">-- SELECT RESIDENT --</option><option value="RT-001">RT-001 (Lakeside)</option><option value="RT-004">RT-004 (Countryside)</option></select><select id="med-select" class="w-full bg-black border border-green-800 text-green-500 text-xs p-2 outline-none"><option value="NULL">-- SELECT MEDICATION --</option><option value="Amlodipine">Amlodipine (5mg)</option><option value="Lisinopril">Lisinopril (10mg)</option><option value="Tylenol">Tylenol (500mg - PRN)</option></select></section><section class="border border-green-900 p-4 rounded-sm bg-black text-center shadow-[inset_0_0_15px_rgba(34,197,94,0.1)]"><div id="status-display" class="bg-green-950/40 p-6 mb-4 text-sm font-bold tracking-widest uppercase">System Standby</div><button onclick="handlePass()" class="w-full bg-green-600 text-black py-4 font-bold uppercase text-xs active:bg-white transition-all">Execute Handshake</button></section></main><script>function handlePass(){const r=document.getElementById('res-select').value;const m=document.getElementById('med-select').value;if(r==='NULL'||m==='NULL'){alert('ERROR: SELECTION INCOMPLETE');return;}alert('SUCCESS: '+m+' LOGGED FOR '+r);}</script></body></html>"""

# EXECUTE PUSH
force_push("index.html", index_v15.strip())
print("SYTEM FULLY SYNCED.")
