
import requests
import json

def inspect_anchor():
    # DefiLlama slug for Anchor is likely 'anchor-protocol' or 'anchor'
    # List: https://api.llama.fi/protocols
    
    # Try direct slug 'anchor'
    url = "https://api.llama.fi/protocol/anchor"
    try:
        print(f"Fetching {url}...")
        resp = requests.get(url)
        if resp.status_code == 404:
             print("404. Trying 'anchor-protocol'...")
             url = "https://api.llama.fi/protocol/anchor-protocol"
             resp = requests.get(url)
             
        data = resp.json()
        print("Keys:", data.keys())
        
        # Check for TVL (Deposits) and Borrowed
        # Usually data['tvl'] list and data['chainTvls']['Terra Classic']['tvl'] etc.
        # But for lending protocols, is there 'borrowed'?
        
        if "chainTvls" in data:
            print("Chains:", data["chainTvls"].keys())
            if "Terra Classic" in data["chainTvls"]:
                terra = data["chainTvls"]["Terra Classic"]
                print("Terra Keys:", terra.keys())
                # 'tvl' is usually deposits + collateral? Or just deposits?
                # 'borrowed' might be a separate key if tracked.
                if "borrowed" in terra:
                    print("Found 'borrowed' history!")
                else:
                    print("'borrowed' key NOT found in chainTvls.")
                    
        # Sometimes 'tokensInUsd' or similar.
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    inspect_anchor()
