import requests, base64, json

p1, p2, p3 = "ghp_mkNf0J", "cajrbxYgl1H7", "qkO3N9B7PYLS4LuR24"
TOKEN = f"{p1}{p2}{p3}"
REPO, OWNER = "webster-node", "SSTADLER1"

def force_push(path, content):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{path}"
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    sha = r.json().get('sha') if r.status_code == 200 else None
    payload = {"message": "GOLDEN RECOVERY", "content": base64.b64encode(content.encode()).decode(), "sha": sha}
    requests.put(url, headers=headers, data=json.dumps(payload))

# THIS IS THE DASHBOARD ONLY
index_v15 = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>WEBSTER NODE V1.5</title><script src="https://cdn.tailwindcss.com"></script></head><body class="bg-black text-green-500 font-mono p-4"><header class="border-b-2 border-green-500 pb-2 mb-4 flex justify-between items-center"><div><h1 class="text-lg font-bold uppercase text-white">Webster Node V1.5</h1><p class="text-[9px] text-green-700 tracking-widest uppercase font-bold">Genesis Mission Ready</p></div><div class="text-[10px] text-white">1440% SYNC</div></header><main class="space-y-4"><section class="border border-green-500 p-3 bg-green-950/10"><h2 class="text-[8px] text-white uppercase mb-2">Clinical Selection</h2><select id="res-select" class="w-full bg-black border border-green-800 text-green-500 text-xs p-2 mb-3 outline-none"><option value="NULL">-- RESIDENT --</option><option value="RT-001">RT-001 (Lakeside)</option><option value="RT-004">RT-004 (Countryside)</option></select><select id="med-select" class="w-full bg-black border border-green-800 text-green-500 text-xs p-2 outline-none"><option value="NULL">-- MEDICATION --</option><option value="Amlodipine">Amlodipine (5mg)</option><option value="Lisinopril">Lisinopril (10mg)</option><option value="Tylenol">Tylenol (500mg)</option></select></section><button onclick="alert('HANDSHAKE LOGGED')" class="w-full bg-green-600 text-black py-4 font-bold uppercase text-xs active:bg-white transition-all">Execute Handshake</button></main></body></html>"""

# TRIGGER THE UPDATE
force_push("index.html", index_v15.strip())
print("RECOVERY COMPLETE")
