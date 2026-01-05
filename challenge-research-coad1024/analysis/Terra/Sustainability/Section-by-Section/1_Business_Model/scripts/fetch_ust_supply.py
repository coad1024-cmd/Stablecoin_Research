
import requests
import csv
import datetime
import os

if not os.path.exists("../data"):
    os.makedirs("../data")

def fetch_defillama_ust():
    url = "https://stablecoins.llama.fi/stablecoin/3"
    print("Fetching UST data from DefiLlama (ID: 3)...")
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        
        rows = []
        
        # USE TOP LEVEL 'tokens' LIST
        # This contains the aggregate circulating supply across all chains (or primary)
        # which matches the required "Total Supply" metric.
        
        if "tokens" in data and isinstance(data["tokens"], list):
             tokens_list = data["tokens"]
             
             for entry in tokens_list:
                 ts = int(entry["date"])
                 # Standard format: {'date': ts, 'circulating': {'peggedUSD': val}}
                 if "circulating" in entry and "peggedUSD" in entry["circulating"]:
                     val = float(entry["circulating"]["peggedUSD"])
                     
                     dt = datetime.datetime.fromtimestamp(ts)
                     date_str = dt.strftime("%Y-%m-%d")
                     
                     rows.append({
                        "date": date_str,
                        "timestamp": ts,
                        "est_supply": val
                     })
        
        rows.sort(key=lambda x: x["timestamp"])
        return rows

    except Exception as e:
        print(f"FAILED to fetch DefiLlama: {e}")
        return []

def save_csv(filename, rows):
    if not rows: return
    keys = rows[0].keys()
    with open(f"../data/{filename}", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved ../data/{filename} ({len(rows)} rows)")

if __name__ == "__main__":
    rows = fetch_defillama_ust()
    
    # Filter for 2021-2022 (Expansion through Collapse)
    # 2021-01-01 to 2022-06-01
    filtered = [r for r in rows if "2021-01-01" <= r["date"] <= "2022-06-01"]
    
    if filtered:
        save_csv("ust_supply_empirical.csv", filtered)
    else:
        print("No data found.")
