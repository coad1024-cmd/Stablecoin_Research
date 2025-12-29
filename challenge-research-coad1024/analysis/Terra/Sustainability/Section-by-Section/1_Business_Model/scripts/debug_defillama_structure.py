
import requests
import json
import pprint

def inspect_defillama():
    url = "https://stablecoins.llama.fi/stablecoin/3"
    try:
        resp = requests.get(url)
        data = resp.json()
        print("Top Level Keys:", data.keys())
        if "chainBalances" in data:
            print("Chain Balances Keys:", data["chainBalances"].keys())
            # Peek at one entry in Terra Classic
            if "Terra Classic" in data["chainBalances"]:
                terra_data = data["chainBalances"]["Terra Classic"]
                print("Terra Classic Type:", type(terra_data))
                if isinstance(terra_data, dict):
                     print("Terra Classic Dict Keys:", terra_data.keys())
                     if "tokens" in terra_data:
                         print("Sample Token Entry:", terra_data["tokens"][0])
                elif isinstance(terra_data, list):
                     print("Sample List Entry:", terra_data[0])
            elif "Terra" in data["chainBalances"]:
                 print("Terra Found!")
        
        # Check if 'totalCirculatingUSD' is nested or named differently
    except Exception as e:
        print(e)

if __name__ == "__main__":
    inspect_defillama()
