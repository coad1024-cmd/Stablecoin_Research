
import requests
import json
import os
import time

DATA_DIR = "../data"
LCD_URL = "https://terra-classic-lcd.publicnode.com"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def fetch_oracle_params(height=None):
    """
    Fetches Oracle Params (VotePeriod etc).
    """
    url = f"{LCD_URL}/terra/oracle/v1beta1/params"
    headers = {}
    if height:
        headers["x-cosmos-block-height"] = str(height)
    
    print(f"Fetching Oracle Params (Height: {height})...")
    try:
        resp = requests.get(url, headers=headers, timeout=5)
        if resp.status_code == 200:
            return resp.json()
        print(f"Error {resp.status_code}: {resp.text}")
    except Exception as e:
        print(f"Connection Failed: {e}")
    return None

def fetch_market_params(height=None):
    """
    Fetches Market Params (Pool info, etc).
    """
    url = f"{LCD_URL}/terra/market/v1beta1/params"
    headers = {}
    if height:
        headers["x-cosmos-block-height"] = str(height)
        
    print(f"Fetching Market Params (Height: {height})...")
    try:
        resp = requests.get(url, headers=headers, timeout=5)
        if resp.status_code == 200:
            return resp.json()
        print(f"Error {resp.status_code}: {resp.text}")
    except Exception as e:
        print(f"Connection Failed: {e}")
    return None

if __name__ == "__main__":
    # May 7 2022 Block Height approx: ~7,500,000 (Terra Classic)
    # We will try to fetch params. Archive nodes usually allow querying old heights.
    # If the public node is NOT an archive node, this will fail (500/400).
    
    # Target Height: May 1 2022
    # Block time ~6s. 
    # Exact height needs lookup, but we'll try a known range or just 'latest' to see if endpoint works,
    # then report capability.
    
    print("--- TESTING LCD ARCHIVE CAPABILITY ---")
    
    # 1. Latest Params (Baseline)
    latest_oracle = fetch_oracle_params()
    if latest_oracle:
        with open(f"{DATA_DIR}/oracle_params_latest.json", "w") as f:
            json.dump(latest_oracle, f, indent=2)
            print("Saved oracle_params_latest.json")
            
    # 2. Historical Params (May 2022) - Approx Height 7,600,000
    # Terra Classic Col-5 upgrade was around block 4.7M (Sep 2021).
    # May 2022 is roughly block 7.5M - 7.7M.
    target_height = 7600000 
    
    hist_oracle = fetch_oracle_params(target_height)
    if hist_oracle:
        with open(f"{DATA_DIR}/oracle_params_7600000.json", "w") as f:
             json.dump(hist_oracle, f, indent=2)
             print("SUCCESS: Endpoint supports archive queries!")
    else:
        print("FAILURE: Endpoint does not support historical archive queries.")
        # Create empty failure marker
        with open(f"{DATA_DIR}/ARCHIVE_NODE_ACCESS_FAILED", "w") as f:
            f.write("Public LCD does not allow x-cosmos-block-height for 7600000.")
