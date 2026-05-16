import os
import requests
import google.generativeai as genai

def sync():
    # 1. Setup Gemini
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')

    # 2. Generate Deterministic Payload
    prompt = "Generate a strictly valid JSON object. Keys: 'ledger' (empty array), 'status' (string 1440), 'protocol' (string Jubilee-v1). No prose."
    response = model.generate_content(prompt)
    payload = response.text.strip().strip('```json').strip('```')

    # 3. Push to Vercel
    url = f"https://api.vercel.com/v1/edge-config/{os.environ['EDGE_CONFIG_ID']}/items"
    headers = {
        "Authorization": f"Bearer {os.environ['VERCEL_TOKEN']}",
        "Content-Type": "application/json"
    }
    # If using a Team account, add ?teamId= to the URL
    params = {}
    if os.environ.get("TEAM_ID"):
        params["teamId"] = os.environ["TEAM_ID"]

    data = {"items": [{"operation": "upsert", "key": "webster_state", "value": payload}]}
    
    r = requests.patch(url, headers=headers, json=data, params=params)
    print(f"Status: {r.status_code} - {r.text}")

if __name__ == "__main__":
    sync()
