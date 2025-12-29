
import requests
import json

def inspect_anchor_v2():
    url = "https://api.llama.fi/protocol/anchor"
    try:
        resp = requests.get(url)
        data = resp.json()
        
        terra_data = data["chainTvls"].get("Terra", {})
        print("Terra Keys:", terra_data.keys())
        
        if "borrowed" in terra_data:
             print("Found 'borrowed' series!")
             print("Sample:", terra_data["borrowed"][-1])
        else:
             print("'borrowed' NOT found in Terra keys.")
             
        # Check top level
        # Sometimes 'tvl' is just deposits?
        # Is there a 'borrows' list at top level?
        # Check overall keys again
        # print("Root Keys:", data.keys())
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    inspect_anchor_v2()
