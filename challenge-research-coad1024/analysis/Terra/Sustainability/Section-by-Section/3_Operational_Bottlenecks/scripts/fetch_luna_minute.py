
import requests
import csv
import datetime
import os
import time

DATA_DIR = "../data"

def fetch_luna_minute():
    # CryptoCompare HistoMinute
    # May 7 2022 to May 13 2022
    # End Timestamp: May 14 00:00 UTC = 1652486400
    # Limit: 2000 points per call. 
    # Minutes in 7 days = 7 * 24 * 60 = 10080.
    # We need ~6 calls.
    
    end_ts = 1652486400 
    all_data = []
    
    # Iterate backwards
    current_to_ts = end_ts
    
    for _ in range(6):
        url = "https://min-api.cryptocompare.com/data/v2/histominute"
        params = {
            "fsym": "LUNC", # Try LUNC or LUNA
            "tsym": "USD",
            "limit": 2000,
            "toTs": current_to_ts
        }
        
        print(f"Fetching to {current_to_ts}...")
        try:
            resp = requests.get(url, params=params, timeout=10)
            data = resp.json()
            if data["Response"] != "Success":
                print("Error from API:", data.get("Message"))
                # Fallback to LUNA?
                if "LUNC" in params["fsym"]:
                     print("Retrying with LUNA...")
                     params["fsym"] = "LUNA"
                     resp = requests.get(url, params=params)
                     data = resp.json()

            history = data['Data']['Data']
            if not history: break
            
            all_data = history + all_data # Prepend because we go backwards
            current_to_ts = history[0]['time'] # New end is start of this batch
            
            time.sleep(0.5)
            
        except Exception as e:
            print(e)
            break
            
    # Filter for May 7 to May 13
    start_ts_filter = 1651881600 # May 7 00:00
    
    filtered = [d for d in all_data if d['time'] >= start_ts_filter]
    
    # Save
    with open(f"{DATA_DIR}/luna_price_minute.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["time", "date", "close", "high", "low", "open", "volumefrom", "volumeto", "conversionType", "conversionSymbol"])
        writer.writeheader()
        for d in filtered:
            d['date'] = datetime.datetime.fromtimestamp(d['time']).strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow(d)
            
    print(f"Saved {len(filtered)} minute-level rows.")

if __name__ == "__main__":
    fetch_luna_minute()
