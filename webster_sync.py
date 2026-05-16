import os
import requests
import google.generativeai as genai

def sync():
    # 1. Setup Gemini with current model
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')

    # 2. Generate Deterministic Payload
    prompt = "Generate a strictly valid JSON object. Keys: 'ledger' (empty array), 'status' (string 1440), 'protocol' (string Jubilee-v1). No prose, just the raw JSON."
    response = model.generate_content(prompt)
    
    # Clean the response to ensure no markdown backticks break the JSON
    payload_str = response.text.strip()
    if payload_str.startswith("```"):
        payload_str = payload_str.split("```")[1]
        if payload_str.startswith("json"):
            payload_str = payload_str[4:]
    payload_str = payload_str.strip()

    # 3. Push to Vercel
    url = f"https://api.vercel.com/v1/edge-config/{os.environ['EDGE_CONFIG_ID']}/items"
    headers = {
        "Authorization": f"Bearer {os.environ['VERCEL_TOKEN']}",
        "Content-Type": "application/json"
    }
    
    # Add teamId if it exists in your secrets
    params = {}
    if os.environ.get("TEAM_ID"):
        params["teamId"] = os.environ["TEAM_ID"]

    # Upsert the key 'webster_state'
    data = {
        "items": [
            {
                "operation": "upsert",
                "key": "webster_state",
                "value": payload_str
            }
        ]
    }
    
    r = requests.patch(url, headers=headers, json=data, params=params)
    print(f"Operational Status: {r.status_code}")
    print(f"Response: {r.text}")

if __name__ == "__main__":
    sync()
