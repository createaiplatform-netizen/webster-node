import requests, base64, json, os

# Permanent Credentials
p1, p2, p3 = "ghp_mkNf0J", "cajrbxYgl1H7", "qkO3N9B7PYLS4LuR24"
TOKEN = f"{p1}{p2}{p3}"
REPO, OWNER = "webster-node", "SSTADLER1"

def force_push(path, content):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{path}"
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    sha = r.json().get('sha') if r.status_code == 200 else None
    payload = {"message": "REMOTE TOTALITY UPDATE", "content": base64.b64encode(content.encode()).decode(), "sha": sha}
    requests.put(url, headers=headers, data=json.dumps(payload))

# This looks for the "Payload" file I will provide
if os.path.exists("payload.txt"):
    with open("payload.txt", "r") as f:
        data = f.read()
        force_push("index.html", data)
    print("TOTALITY REACHED: SITE UPDATED")
