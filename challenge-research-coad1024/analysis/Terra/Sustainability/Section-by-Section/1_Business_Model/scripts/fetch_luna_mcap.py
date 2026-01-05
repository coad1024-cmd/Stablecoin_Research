
import requests
import csv
import datetime
import os

# CONFIG
DATA_DIR = "../data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def fetch_coincap_luna():
    # ID: terra-luna
    url = "https://api.coincap.io/v2/assets/terra-luna/history"
    params = {
        "interval": "d1",
        # Start/End can be specified in ms timestamps if needed, or get all
        # 1609459200000 = Jan 1 2021
        # 1654041600000 = June 1 2022
        "start": 1609459200000,
        "end": 1654041600000
    }
    
    print("Fetching terra-luna from Coincap...")
    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        
        # data["data"] is a list of {priceUsd, time, date, circulatingSupply?, date}
        # Coincap history usually provides priceUsd. Does it provide Market Cap?
        # Often history only has price. Let's check structure.
        # IF history only has price, we are stuck needing supply again.
        
        # Let's try and see. If keys missing, we will know.
        rows = []
        if "data" in data:
            for d in data["data"]:
                # d keys: priceUsd, time, date.
                # Is marketCapUsd in history? Usually no for coincap history endpoint.
                # But let's check.
                
                ts = int(d["time"])
                price = float(d["priceUsd"])
                
                # Check if market cap exists? 
                # If not, we need Supply.
                # Coincap assets/{id} gives CURRENT supply.
                # History endpoint usually just price.
                
                dt = datetime.datetime.fromtimestamp(ts/1000.0)
                date_str = dt.strftime("%Y-%m-%d")
                
                rows.append({
                    "date": date_str,
                    "timestamp": ts,
                    "price": price,
                    # Placeholder if mcap missing
                    "raw_entry": d
                })
        
        return rows

    except Exception as e:
        print(f"FAILED to fetch Coincap: {e}")
        return []

if __name__ == "__main__":
    rows = fetch_coincap_luna()
    if rows:
        print(f"Fetched {len(rows)} rows.")
        print("Sample keys:", rows[0]["raw_entry"].keys())
    else:
        print("No data.")
