
import requests
import csv
import datetime
import os
import time

DATA_DIR = "../data"

def fetch_luna_hour():
    # CryptoCompare HistoHour
    # May 7 2022 to May 14 2022
    end_ts = 1652486400 
    all_data = []
    
    # Iterate backwards
    current_to_ts = end_ts
    
    # We need ~7 days * 24 = 168 points. Limit 2000 covers it in 1 call.
    
    url = "https://min-api.cryptocompare.com/data/v2/histohour"
    params = {
        "fsym": "LUNC", # Try LUNC
        "tsym": "USD",
        "limit": 2000,
        "toTs": current_to_ts
    }
    
    print(f"Fetching to {current_to_ts}...")
    try:
        resp = requests.get(url, params=params, timeout=10)
        data = resp.json()
        
        # Check success
        if data.get("Response") != "Success":
             print("Error:", data.get("Message"))
             # Retry LUNA
             params["fsym"] = "LUNA"
             resp = requests.get(url, params=params)
             data = resp.json()

        history = data['Data']['Data']
        all_data = history
        
    except Exception as e:
        print(e)
            
    # Filter for May 7 to May 14
    start_ts_filter = 1651881600 # May 7 00:00
    
    filtered = [d for d in all_data if d['time'] >= start_ts_filter]
    
    # Save
    with open(f"{DATA_DIR}/luna_price_hour.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["time", "date", "close", "high", "low", "open", "volumefrom", "volumeto", "conversionType", "conversionSymbol"])
        writer.writeheader()
        for d in filtered:
            d['date'] = datetime.datetime.fromtimestamp(d['time']).strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow(d)
            
    print(f"Saved {len(filtered)} hourly rows.")

if __name__ == "__main__":
    fetch_luna_hour()
