
import requests
import csv
import datetime
import os

# CONFIG
DATA_DIR = "../data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def fetch_cc_luna():
    # CryptoCompare LUNA usually refers to the original or LUNC.
    # LUNC symbol exists?
    # endpoints: histoday
    
    url = "https://min-api.cryptocompare.com/data/v2/histoday"
    
    # Try LUNA first (might be LUNA2.0 now). Try LUNC.
    # "LUNA" on CC might be LUNA2.
    # Let's try LUNC.
    
    params = {
        "fsym": "LUNC",
        "tsym": "USD",
        "limit": 2000
    }
    
    print("Fetching LUNC from CryptoCompare...")
    try:
        resp = requests.get(url, params=params, timeout=15)
        data = resp.json()
        
        if data["Response"] != "Success":
            print(f"Error: {data['Message']}")
            # Try LUNA (Legacy?)
            print("Retrying with symbol 'LUNA'...")
            params["fsym"] = "LUNA"
            resp = requests.get(url, params=params, timeout=15)
            data = resp.json()
            
        if data["Response"] != "Success":
             print("Failed.")
             return []
             
        # Extract Data
        # data['Data']['Data'] -> list of {time, close, open, high, low, volumefrom, volumeto}
        # CryptoCompare does NOT give Market Cap in history.
        # We need Supply to get Mcap.
        
        # WE NEED SUPPLY.
        # Can we fetch supply history?
        # If not, we can try to approximate supply.
        # But user demands "Empirical: raw mcap".
        
        # If I can't get Mcap, I can't do section 2.2 empirically without external data import.
        
        # Let's look at the result.
        history = data['Data']['Data']
        rows = []
        for h in history:
            ts = h["time"]
            price = h["close"]
            
            # DATE
            dt = datetime.datetime.fromtimestamp(ts)
            date_str = dt.strftime("%Y-%m-%d")
            
            # We don't have supply here. 
            # If I can't find Mcap API, I will have to use a known supply curve (Modelled) 
            # OR ask the user to provide the CSV.
            
            rows.append({
                "date": date_str,
                "timestamp": ts,
                "price": price,
                "market_cap": 0 # Missing
            })
            
        return rows

    except Exception as e:
        print(f"FAILED to fetch CC: {e}")
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
    rows = fetch_cc_luna()
    if rows:
        # Filter 2021-2022
        filtered = [r for r in rows if "2021-01-01" <= r["date"] <= "2022-06-01"]
        save_csv("luna_price_empirical.csv", filtered)
    else:
        print("No data.")

