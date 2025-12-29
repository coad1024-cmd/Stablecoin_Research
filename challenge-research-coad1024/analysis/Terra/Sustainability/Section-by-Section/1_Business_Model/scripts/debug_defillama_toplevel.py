
import requests
import json

def inspect_defillama_toplevel():
    url = "https://stablecoins.llama.fi/stablecoin/3"
    try:
        resp = requests.get(url)
        data = resp.json()
        
        # Check Top-Level Tokens
        if "tokens" in data:
            print(f"Top Level 'tokens' is type: {type(data['tokens'])}")
            if isinstance(data['tokens'], list) and len(data['tokens']) > 0:
                print(f"Sample Entry: {data['tokens'][0]}")
                print(f"Count: {len(data['tokens'])}")
                # Check date range
                first = data['tokens'][0]
                last = data['tokens'][-1]
                print(f"Range: {first.get('date')} to {last.get('date')}")
        
        # Check if there is another candidate
        print("Keys:", data.keys())

    except Exception as e:
        print(e)

if __name__ == "__main__":
    inspect_defillama_toplevel()
