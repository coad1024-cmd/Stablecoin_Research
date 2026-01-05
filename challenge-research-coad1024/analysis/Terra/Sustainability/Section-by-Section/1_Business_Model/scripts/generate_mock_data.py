import csv
import random
import datetime

# Mock Dates: Jan 1 2022 to May 15 2022
start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2022, 5, 15)
delta = datetime.timedelta(days=1)

dates = []
curr = start_date
while curr <= end_date:
    dates.append(curr.isoformat())
    curr += delta

n = len(dates)
crash_start_idx = n - 8 # May 7ish

header = ['Date', 'UST_Supply', 'LUNA_MarketCap', 'LUNA_Price', 'Anchor_Deposits', 'Anchor_Borrows', 'LUNA_Volume']
rows = []

for i, d in enumerate(dates):
    # UST Supply: Steady 10B -> 18B, then burn
    if i < crash_start_idx:
        ust = 10e9 + (8e9 * (i / crash_start_idx))
    else:
        # Crash burn
        factor = (i - crash_start_idx) / 8
        ust = 18e9 - (7e9 * factor) # drops to 11B
    
    # LUNA Mcap: 30B -> 40B, then crash
    if i < crash_start_idx:
        luna_mc = 30e9 + (10e9 * (i / crash_start_idx)) + random.uniform(-1e9, 1e9)
        luna_px = 80 + (30 * (i / crash_start_idx))
    else:
        # Crash
        luna_mc = 40e9 * (0.1 ** (i - crash_start_idx)) # Exponential decay
        luna_px = 110 * (0.1 ** (i - crash_start_idx))

    # Anchor
    dep = 10e9 + (4e9 * (i/n))
    bor = 2e9 + (1e9 * (i/n))
    
    vol = luna_mc * 0.1

    rows.append([d, ust, luna_mc, luna_px, dep, bor, vol])

with open('terra_daily_metrics.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print("Generated terra_daily_metrics.csv (No Pandas)")

# LFG Reserves
header_res = ['Date', 'BTC_Balance', 'BTC_Price']
rows_res = []
for i, d in enumerate(dates):
    btc_px = 40000 - (10000 * (i/n))
    bal = 0
    if i > 60: bal = 40000 # Bought in march
    if i > 120: bal = 80000 # Bought in may
    if i > crash_start_idx + 2: bal = 0 # Sold
    
    rows_res.append([d, bal, btc_px])

with open('lfg_reserves.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header_res)
    writer.writerows(rows_res)

print("Generated lfg_reserves.csv (No Pandas)")
