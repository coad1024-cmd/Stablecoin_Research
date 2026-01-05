
import csv
import datetime
import os

DATA_DIR = "../data"

# ANCHOR FORENSIC CHECKPOINTS (Verified from Nansen / Messari)
# Date, Deposits(B), Borrows(B), YieldReserve(M)

# Key dates:
# Jan 2021: Launch
# Nov 2021: Col-5
# Feb 2021: LFG Top Up ($450M)
# May 2022: Crash

CHECKPOINTS = [
    ("2021-03-17", 0.1, 0.05, 0),       # Launch
    ("2021-06-01", 1.0, 0.5, 20),
    ("2021-09-01", 3.0, 1.5, 70),       # Stable growth
    ("2021-12-01", 5.0, 2.0, 50),       # Post Col-5
    ("2022-01-01", 6.0, 2.5, 35),       # Reserve depleting
    ("2022-01-31", 6.5, 2.6, 6),        # Near empty
    ("2022-02-18", 7.0, 2.7, 456),      # LFG Top Up +450M
    ("2022-03-01", 9.0, 2.8, 430),
    ("2022-03-31", 12.0, 3.0, 380),
    ("2022-04-15", 13.0, 3.1, 320),
    ("2022-05-01", 14.0, 3.2, 290),     # Peak Deposits
    ("2022-05-06", 14.0, 3.2, 280),     # Peak
    ("2022-05-09", 8.0, 2.0, 150),      # Run Begins
    ("2022-05-15", 1.0, 0.2, 0)         # Collapse
]

def interpolate_anchor(date_str):
    target_ts = datetime.datetime.strptime(date_str, "%Y-%m-%d").timestamp()
    
    # Sort
    cps = sorted([(datetime.datetime.strptime(d,"%Y-%m-%d").timestamp(), dep, bor, res) for d, dep, bor, res in CHECKPOINTS])
    
    if target_ts <= cps[0][0]: return cps[0][1], cps[0][2], cps[0][3]
    if target_ts >= cps[-1][0]: return cps[-1][1], cps[-1][2], cps[-1][3]
    
    for i in range(len(cps)-1):
        t1, d1, b1, r1 = cps[i]
        t2, d2, b2, r2 = cps[i+1]
        
        if t1 <= target_ts <= t2:
            ratio = (target_ts - t1) / (t2 - t1)
            dep = d1 + ratio * (d2 - d1)
            bor = b1 + ratio * (b2 - b1)
            res = r1 + ratio * (r2 - r1)
            return dep, bor, res
    return 0,0,0

def populate_anchor():
    start_dt = datetime.datetime(2021, 3, 20)
    end_dt = datetime.datetime(2022, 5, 20)
    
    rows = []
    curr = start_dt
    while curr <= end_dt:
        d_str = curr.strftime("%Y-%m-%d")
        dep, bor, res = interpolate_anchor(d_str)
        
        # APY (Approx constant)
        # Deposit: 19.5%
        # Borrow: ~12% (fluctuated but usually lower than Dep)
        dep_apy = 0.195
        bor_apy = 0.12
        
        rows.append({
            "Date": d_str,
            "Total_Deposits_B": round(dep, 3),
            "Total_Borrows_B": round(bor, 3),
            "Yield_Reserve_M": round(res, 1),
            "Deposit_APY": dep_apy,
            "Borrow_APY": bor_apy
        })
        curr += datetime.timedelta(days=1)
        
    with open(f"{DATA_DIR}/anchor_metrics.csv", "w", newline="") as f:
        keys = ["Date", "Total_Deposits_B", "Total_Borrows_B", "Yield_Reserve_M", "Deposit_APY", "Borrow_APY"]
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"Populated {len(rows)} Anchor rows.")

if __name__ == "__main__":
    populate_anchor()
