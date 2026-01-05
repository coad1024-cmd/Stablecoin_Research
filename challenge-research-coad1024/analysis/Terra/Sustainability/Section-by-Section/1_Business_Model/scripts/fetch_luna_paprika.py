
import requests
import csv
import datetime
import os

# CONFIG
DATA_DIR = "../data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def fetch_paprika_luna():
    # ID: luna-terra (Check if correct)
    # Start: 2021-01-01
    url = "https://api.coinpaprika.com/v1/coins/luna-terra/ohlcv/historical"
    params = {
        "start": "2021-01-01",
        "end": "2022-06-01",
        "quote": "USD"
    }
    
    print("Fetching luna-terra from CoinPaprika...")
    try:
        resp = requests.get(url, params=params, timeout=15)
        # Check 404
        if resp.status_code == 404:
            print("404: Coin ID might be wrong. Trying 'lunc-terra-classic'?")
            # Maybe check coin list?
            return []
            
        resp.raise_for_status()
        data = resp.json()
        
        # Structure: list of {time_open, time_close, open, high, low, close, volume, market_cap}
        rows = []
        for d in data:
            date_str = d["time_open"][:10] # "2021-01-01T..."
            ts = int(datetime.datetime.strptime(date_str, "%Y-%m-%d").timestamp())
            
            p = d["close"]
            m = d.get("market_cap", 0)
            
            rows.append({
                "date": date_str,
                "timestamp": ts,
                "price": p,
                "market_cap": m
            })
            
        return rows

    except Exception as e:
        print(f"FAILED to fetch Paprika: {e}")
        return []

def save_csv(filename, rows):
    if not rows: return
    keys = rows[0].keys()
    with open(f"{DATA_DIR}/{filename}", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved {DATA_DIR}/{filename} ({len(rows)} rows)")

if __name__ == "__main__":
    rows = fetch_paprika_luna()
    if rows:
        save_csv("luna_mcap_empirical.csv", rows)
        # Check if we have mcap
        print("Sample Mcap:", rows[0]["market_cap"])
    else:
        print("No data.")
