import os
import requests

def sync():
    # 1. Hard-coded Deterministic Payload (The Golden Build State)
    # This removes the dependency on the Gemini API for this specific sync.
    payload_str = '{"ledger": [], "status": "1440", "protocol": "Jubilee-v1"}'

    # 2. Push to Vercel
    url = f"https://api.vercel.com/v1/edge-config/{os.environ['EDGE_CONFIG_ID']}/items"
    headers = {
        "Authorization": f"Bearer {os.environ['VERCEL_TOKEN']}",
        "Content-Type": "application/json"
    }
    
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
    
    print(f"Initiating push to Edge Config: {os.environ['EDGE_CONFIG_ID']}")
    r = requests.patch(url, headers=headers, json=data, params=params)
    
    print(f"Operational Status: {r.status_code}")
    if r.status_code == 200:
        print("Success: Webster Node Synchronized.")
    else:
        print(f"Error Detail: {r.text}")

if __name__ == "__main__":
    sync()
