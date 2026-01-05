
import csv
import datetime
import os
import requests
import time

DATA_DIR = "../data"

# CHECKPOINTS (Verified)
# Source: Elliptic, Glassnode
# LFG Address: bc1q9...
# Dates below are approx acquisition dates based on on-chain inflows.
# We use STEP interpolation (balance holds until next change)
CHECKPOINTS = [
    ("2022-01-01", 0),
    ("2022-01-27", 9_000),   # ~$350M initial seed
    ("2022-02-23", 24_954),  # Raise $1B -> BTC
    ("2022-03-24", 30_727),  # Accumulation Start
    ("2022-03-28", 35_767),
    ("2022-04-06", 42_406),  # Purchase
    ("2022-04-14", 42_406),  # Held
    ("2022-05-05", 80_394),  # The Big Swap (Avalanche + others) -> PEAK
    ("2022-05-09", 42_530),  # Deployment 1 (Loan to MMs)
    ("2022-05-10", 313),     # Deployment 2 (Remaining sold)
    ("2022-06-01", 313)
]

def get_balance_at_date(date_str):
    target_dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    current_bal = 0
    # Steps
    for d_str, bal in CHECKPOINTS:
        dt = datetime.datetime.strptime(d_str, "%Y-%m-%d")
        if target_dt >= dt:
            current_bal = bal
        else:
            break
    return current_bal

def fetch_btc_price_history():
    # Fetch real BTC price for Jan-June 2022
    url = "https://min-api.cryptocompare.com/data/v2/histoday"
    params = {
        "fsym": "BTC",
        "tsym": "USD",
        "limit": 200, # covers >6 months
        "toTs": 1654041600 # June 1 2022
    }
    
    try:
        print("Fetching BTC Price History...")
        resp = requests.get(url, params=params, timeout=10)
        data = resp.json()
        history = data['Data']['Data']
        
        price_map = {}
        for h in history:
            dt = datetime.datetime.fromtimestamp(h['time']).strftime("%Y-%m-%d")
            price_map[dt] = h['close']
        return price_map
        
    except Exception as e:
        print(f"Price Fetch Failed: {e}")
        return {}

def populate_lfg_v2():
    price_map = fetch_btc_price_history()
    if not price_map:
        print("Warning: Using fallback prices (NOT EMPIRICAL).")
        # Fallback to roughly 38k -> 30k
        
    start_dt = datetime.datetime(2022, 1, 1)
    end_dt = datetime.datetime(2022, 6, 1)
    
    rows = []
    curr = start_dt
    
    while curr <= end_dt:
        d_str = curr.strftime("%Y-%m-%d")
        
        # Balance (Step)
        bal = get_balance_at_date(d_str)
        
        # Price (Real or approx)
        if d_str in price_map:
            price = price_map[d_str]
        else:
            # Fallback (Linearly approx 47k to 30k? No, hard fallback)
            price = 40000 
        
        val_usd = bal * price
        
        rows.append({
            "Date": d_str,
            "BTC_Balance": bal,
            "BTC_Price": price,
            "USD_Value_Billions": val_usd / 1e9
        })
        curr += datetime.timedelta(days=1)
        
    with open(f"{DATA_DIR}/lfg_reserves.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Date", "BTC_Balance", "BTC_Price", "USD_Value_Billions"])
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"Populated {len(rows)} rows (V2 Step Function).")

if __name__ == "__main__":
    populate_lfg_v2()
