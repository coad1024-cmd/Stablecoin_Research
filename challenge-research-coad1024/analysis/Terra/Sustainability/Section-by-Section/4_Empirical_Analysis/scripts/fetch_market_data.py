
import requests
import csv
import time
import os
import datetime

DATA_DIR = "../data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def fetch_coingecko_history(coin_id, days="max"):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days,
        "interval": "daily"
    }
    
    print(f"Fetching {coin_id} from CoinGecko...")
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        
        prices = data.get("prices", [])
        mcaps = data.get("market_caps", [])
        vols = data.get("total_volumes", [])
        
        # Structure: [timestamp, value]
        # We align by index assuming same length and sorted order
        rows = []
        for i in range(len(prices)):
            ts = prices[i][0]
            p = prices[i][1]
            m = mcaps[i][1] if i < len(mcaps) else 0
            v = vols[i][1] if i < len(vols) else 0
            
            # Convert ts (ms) to YYYY-MM-DD
            dt = datetime.datetime.fromtimestamp(ts/1000.0)
            date_str = dt.strftime("%Y-%m-%d")
            
            rows.append({
                "date": date_str,
                "timestamp": ts,
                "price": p,
                "market_cap": m,
                "volume": v,
                "coin_id": coin_id
            })
            
        return rows
        
    except Exception as e:
        print(f"FAILED to fetch {coin_id}: {e}")
        return []

def save_csv(filename, rows):
    if not rows:
        return
    keys = rows[0].keys()
    with open(f"{DATA_DIR}/{filename}", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved {filename} ({len(rows)} rows)")

if __name__ == "__main__":
    # 1. Fetch LUNC (ID: terra-luna)
    lunc_rows = fetch_coingecko_history("terra-luna", days="max")
    # Filter 2021-2022
    lunc_filtered = [r for r in lunc_rows if "2021-01-01" <= r["date"] <= "2022-06-01"]
    save_csv("lunc_history_cg.csv", lunc_filtered)

    # 2. Fetch USTC (ID: terrausd)
    ustc_rows = fetch_coingecko_history("terrausd", days="max")

    # Filter 2021-2022
    ustc_filtered = [r for r in ustc_rows if "2021-01-01" <= r["date"] <= "2022-06-01"]
    save_csv("ustc_history_cg.csv", ustc_filtered)
    
    print("Market data fetch complete.")
