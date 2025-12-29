
import csv
import datetime
import os

DATA_DIR = "../data"

# Known Supply Checkpoints (Source: Terra Station / Messari Reports)
# 2021-01-01: ~484M
# 2021-10-01: ~400M (Columbus-5 Burn)
# 2022-01-01: ~360M
# 2022-04-01: ~350M (Peak)
# 2022-05-07: ~345M (Pre-depeg)
# 2022-05-12: ~1.5B (Hyperinflation Start)
# 2022-05-13: ~15B
# 2022-05-14: ~6.5T

CHECKPOINTS = {
    "2021-01-01": 484_000_000,
    "2021-07-01": 420_000_000,
    "2021-11-01": 390_000_000, # Post Col-5
    "2022-01-01": 360_000_000,
    "2022-04-01": 350_000_000,
    "2022-05-01": 345_000_000,
    "2022-05-08": 346_000_000,
    "2022-05-10": 360_000_000,
    "2022-05-11": 1_000_000_000,
    "2022-05-12": 10_000_000_000,
    "2022-05-13": 6_500_000_000_000,
    "2022-06-01": 6_500_000_000_000
}

def interpolate_supply(date_str):
    # This is a naive piecewise linear interpolation
    # Good enough for "Reconstructed" baseline
    
    # 1. Convert checkpoints to ts
    sorted_cps = sorted([(datetime.datetime.strptime(k,"%Y-%m-%d").timestamp(), v) for k,v in CHECKPOINTS.items()])
    
    target_dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    target_ts = target_dt.timestamp()
    
    # Check bounds
    if target_ts <= sorted_cps[0][0]: return sorted_cps[0][1]
    if target_ts >= sorted_cps[-1][0]: return sorted_cps[-1][1]
    
    # Find span
    for i in range(len(sorted_cps)-1):
        t1, v1 = sorted_cps[i]
        t2, v2 = sorted_cps[i+1]
        
        if t1 <= target_ts <= t2:
            ratio = (target_ts - t1) / (t2 - t1)
            return v1 + ratio * (v2 - v1)
            
    return 0

def augment():
    if not os.path.exists(f"{DATA_DIR}/luna_price_empirical.csv"):
        print("Price data missing.")
        return
        
    with open(f"{DATA_DIR}/luna_price_empirical.csv", "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
    out_rows = []
    headers = reader.fieldnames + ["est_supply", "est_mcap"]
    
    for r in rows:
        price = float(r["price"])
        supply = interpolate_supply(r["date"])
        mcap = price * supply
        
        r["est_supply"] = supply
        r["est_mcap"] = mcap
        out_rows.append(r)
        
    with open(f"{DATA_DIR}/luna_mcap_empirical.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(out_rows)
        
    print(f"Augmented {len(out_rows)} rows.")

if __name__ == "__main__":
    augment()
