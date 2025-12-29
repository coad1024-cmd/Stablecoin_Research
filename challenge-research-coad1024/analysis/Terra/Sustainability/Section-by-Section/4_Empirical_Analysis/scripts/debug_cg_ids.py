
import requests
import json

def find_ids():
    url = "https://api.coingecko.com/api/v3/coins/list"
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
        
        matches = []
        for c in data:
            if c["id"].startswith("terra"):
                matches.append(c)
                
        print(f"Found {len(matches)} matches starting with 'terra':")
        for m in matches:
            print(f"ID: {m['id']}, Symbol: {m['symbol']}, Name: {m['name']}")
            
    except Exception as e:
        print(e)

if __name__ == "__main__":
    find_ids()
