
import requests
import json
import time

def check_llama_prices():
    # DefiLlama Coins API
    # https://coins.llama.fi/chart/{coins}?start={start}&span={span}&period={period}&searchWidth={searchWidth}
    
    # Coin ID: coingecko:terra-luna
    # Start: 1609459200 (Jan 1 2021)
    # Span: 500 (Days)
    # Period: 1d
    
    url = "https://coins.llama.fi/chart/coingecko:terra-luna?start=1609459200&span=600&period=1d"
    
    print(f"Fetching {url}...")
    try:
        resp = requests.get(url, timeout=10)
        # Verify status
        if resp.status_code != 200:
             print(f"Error {resp.status_code}: {resp.text}")
             return

        data = resp.json()
        print("Keys:", data.keys())
        
        if "coins" in data:
            coin_data = data["coins"].get("coingecko:terra-luna", {})
            prices = coin_data.get("prices", [])
            print(f"Found {len(prices)} price points.")
            if prices:
                print("Sample:", prices[0])
                print("Last:", prices[-1])
                
    except Exception as e:
        print(e)

if __name__ == "__main__":
    check_llama_prices()
