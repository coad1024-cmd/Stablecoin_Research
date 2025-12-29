
import requests

def debug_yields():
    # Search for Anchor
    url = "https://yields.llama.fi/pools"
    try:
        resp = requests.get(url)
        data = resp.json()
        # content in 'data' list
        matches = []
        for p in data['data']:
            if "Anchor" in p['project'] and p['chain'] == 'Terra Classic':
                matches.append(p)
                
        print(f"Found {len(matches)} Anchor Terra Classic pools.")
        for m in matches:
            print(f"Symbol: {m['symbol']}, ID: {m['pool']}, TVL: {m['tvlUsd']}")
            
    except Exception as e:
        print(e)
            
if __name__ == "__main__":
    debug_yields()
