import os
import requests
import datetime

def sync():
    # 1. Capture the "Pulse" (Bot Metadata)
    now = datetime.datetime.utcnow().isoformat()
    
    # This is the Bot's active memory state
    bot_payload = {
        "identity": "Sara-Agent-v1",
        "status": "1440",
        "last_pulse": f"{now}Z",
        "protocol": "Jubilee-v1",
        "facilities": {
            "Lakeside_Trinity": "ACTIVE",
            "Countryside_Living": "ACTIVE",
            "Kapes_Lakeside": "STANDBY"
        },
        "ledger": ["System Initialized", "Node Synchronized", "Bot Online"]
    }

    # 2. Push to Vercel (The Bot's Memory)
    url = f"https://api.vercel.com/v1/edge-config/{os.environ['EDGE_CONFIG_ID']}/items"
    headers = {
        "Authorization": f"Bearer {os.environ['VERCEL_TOKEN']}",
        "Content-Type": "application/json"
    }
    
    params = {}
    if os.environ.get("TEAM_ID"):
        params["teamId"] = os.environ["TEAM_ID"]

    data = {
        "items": [
            {
                "operation": "upsert",
                "key": "webster_state",
                "value": bot_payload
            }
        ]
    }
    
    print(f"Bot Pulse Initiated: {now}")
    r = requests.patch(url, headers=headers, json=data, params=params)
    
    if r.status_code == 200:
        print("Success: Bot and Node are now Synchronized.")
    else:
        print(f"Sync Failure: {r.text}")

if __name__ == "__main__":
    sync()
