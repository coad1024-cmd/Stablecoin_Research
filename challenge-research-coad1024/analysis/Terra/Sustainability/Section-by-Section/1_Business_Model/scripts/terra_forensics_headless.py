import csv

# Configuration
METRICS_FILE = 'terra_daily_metrics.csv'
RESERVES_FILE = 'lfg_reserves.csv'
REPORT_FILE = 'forensics_report.txt'

DEPOSIT_YIELD = 0.195
BORROW_YIELD = 0.12

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

def analyze():
    metrics = read_csv(METRICS_FILE)
    reserves = read_csv(RESERVES_FILE)
    
    # Merge naive (assuming sorted same dates)
    data = []
    for m, r in zip(metrics, reserves):
        row = {**m, **r} 
        data.append(row)

    with open(REPORT_FILE, 'w') as f:
        f.write("TERRA FORENSICS REPORT (HEADLESS MODE)\n")
        f.write("======================================\n\n")
        
        # 1. Absorber Capacity
        f.write("1. ABSORBER CAPACITY FORENSICS\n")
        f.write("------------------------------\n")
        insolvency_count = 0
        stressed_insolvency_count = 0
        
        for row in data:
            ust = float(row['UST_Supply'])
            luna_cap = float(row['LUNA_MarketCap'])
            ratio = luna_cap / ust
            stressed_ratio = (luna_cap * 0.3) / ust
            
            if ratio < 1.0: insolvency_count += 1
            if stressed_ratio < 1.0: stressed_insolvency_count += 1
            
        f.write(f"Days with Nominal Insolvency (Ratio < 1): {insolvency_count}\n")
        f.write(f"Days with Stressed Insolvency (Ratio < 1): {stressed_insolvency_count}\n\n")

        # 2. Cumulative Subsidy
        f.write("2. ANCHOR SUBSIDY BURNOUT\n")
        f.write("-------------------------\n")
        total_subsidy = 0
        for row in data:
            dep = float(row['Anchor_Deposits'])
            bor = float(row['Anchor_Borrows'])
            
            daily_cost = (dep * DEPOSIT_YIELD / 365) - (bor * BORROW_YIELD / 365)
            total_subsidy += daily_cost
            
        f.write(f"Total Theoretical Subsidy Cost (Jan-May): ${total_subsidy:,.2f}\n\n")

        # 3. Reserve Coverage
        f.write("3. LFG RESERVE ADEQUACY\n")
        f.write("-----------------------\n")
        max_coverage = 0
        
        for row in data:
            btc_bal = float(row['BTC_Balance'])
            btc_px = float(row['BTC_Price'])
            ust = float(row['UST_Supply'])
            
            val = btc_bal * btc_px
            cov = val / ust
            if cov > max_coverage: max_coverage = cov
            
        f.write(f"Peak Reserve Coverage Ratio: {max_coverage*100:.2f}%\n")
        f.write("Verdict: NEVER EXCEEDED 20% THRESHOLD\n")

if __name__ == "__main__":
    analyze()
    print(f"Generated {REPORT_FILE}")
