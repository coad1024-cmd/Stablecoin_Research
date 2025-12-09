import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import csv

# Base paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "..", "data", "onchain_snapshot.csv")
DIAGRAMS_DIR = os.path.join(SCRIPT_DIR, "..", "Diagrams", "Business Decomposition")

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def load_real_data():
    """Lengths real data from onchain_snapshot.csv if available."""
    data = {
        "dsr_cost": 1.25, # Default fallback
        "gross_yield": 4.5, # Default fallback (Blended)
        "total_debt": 4000000000, # 4B
        "surplus": 60000000 # 60M
    }
    
    if os.path.exists(DATA_PATH):
        print(f"Loading Real Data from {DATA_PATH}")
        try:
            with open(DATA_PATH, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if not row: continue
                    key, val = row[0], float(row[1])
                    if key == "dsr_cost": data["dsr_cost"] = abs(val) # CSV stores as negative
                    # Add more mapping if CSV expands
        except Exception as e:
            print(f"Error reading CSV: {e}")
            
    return data

def main():
    print("Generating MakerDAO Business Decomposition Plots...")
    ensure_dir(DIAGRAMS_DIR)
    real_data = load_real_data()
    
    # Common Style
    plt.style.use('seaborn-v0_8-whitegrid')
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
    
    # 1. Weighted Avg Rate Timeseries (Historical)
    # Reconstructing the narrative: 2023 Arb Gap -> EDSR -> 2024 Equilibrium -> 2025 Normalization
    dates = pd.date_range(start='2023-01-01', periods=24, freq='M')
    
    # Synthetic historical data based on known events
    dsr_hist = [1.0]*6 + [3.49]*3 + [5.0]*6 + [5.0]*6 + [real_data['dsr_cost']]*3 # Dropping to 1.25 recently
    rwa_hist = [4.0]*6 + [4.5]*6 + [5.2]*6 + [5.0]*3 + [4.5]*3
    crypto_hist = [1.5]*12 + [6.0]*6 + [7.5]*6
    
    plt.figure(figsize=(10, 6))
    plt.plot(dates, rwa_hist, label='RWA Yield (Gov Bonds)', color='green', linewidth=2)
    plt.plot(dates, crypto_hist, label='Crypto Vault Fee (ETH/WBTC)', color='purple', linewidth=2, linestyle='--')
    plt.plot(dates, dsr_hist, label='DSR (Cost of Capital)', color='red', linewidth=2)
    
    plt.fill_between(dates, dsr_hist, rwa_hist, alpha=0.1, color='green', label='NIM Spread')
    
    plt.title('1. Historical Rate Evolution: The "Cost of Carry" Cycle')
    plt.ylabel('APY (%)')
    plt.legend()
    plt.savefig(os.path.join(DIAGRAMS_DIR, "1_weighted_avg_rate_timeseries.png"))
    plt.close()
    
    # 2. Interest Rate Distribution (Current Snapshot)
    # MakerDAO has bifurcated rates: Low RWA, High Crypto
    categories = ['RWA (T-Bills)', 'Core Vaults (ETH-A)', 'Lite Vaults (ETH-C)', 'PSM (USDC)']
    rates = [4.5, 6.5, 7.5, 0.0]
    weights = [2.5, 1.0, 0.5, 1.0] # Billions
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, rates, color=['green', 'purple', 'purple', 'grey'])
    plt.title(f'2. Interest Rate Distribution (Current DSR: {real_data["dsr_cost"]}%)')
    plt.ylabel('APY (%)')
    plt.axhline(y=real_data['dsr_cost'], color='red', linestyle='--', label='Cost of Capital (DSR)')
    
    # Add volume labels
    for bar, w in zip(bars, weights):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f'{w}B', ha='center')
        
    plt.legend()
    plt.savefig(os.path.join(DIAGRAMS_DIR, "2_interest_rate_distribution.png"))
    plt.close()

    # 3. Surplus Buffer vs Liquidatable Debt
    # Visualizing the "Capital Buffer" geometry
    debt_levels = np.linspace(0, 5000, 100) # 0 to 5B
    required_buffer = debt_levels * 0.05 # 5% safe buffer rule of thumb
    current_surplus = 60 # 60M
    
    plt.figure(figsize=(10, 6))
    plt.plot(debt_levels, required_buffer, 'k--', label='Target Buffer (5% coverage)')
    plt.axhline(y=current_surplus, color='green', linewidth=2, label='Current Surplus (~60M)')
    plt.fill_between(debt_levels, 0, current_surplus, alpha=0.2, color='green')
    
    # Intersection "Risk Zone"
    risk_start = current_surplus / 0.05
    plt.axvline(x=risk_start, color='red', linestyle=':', label=f'Risk Threshold ({risk_start:.0f}M Debt)')
    
    plt.title('3. Surplus Buffer Capacity vs Total Risk')
    plt.xlabel('Total Risk Assets ($M)')
    plt.ylabel('Surplus Buffer ($M)')
    plt.legend()
    plt.savefig(os.path.join(DIAGRAMS_DIR, "3_sp_vs_liquidatable_debt.png"))
    plt.close()

    # 4. Unit Economics Scenarios (The Missing Link)
    # Profit per 1 DAI under Bull/Bear
    scenarios = ['Current (Low DSR)', 'Bear (High DSR)', 'Bull (High Crypto Fee)']
    
    # Yields
    yield_rwa = np.array([4.5, 3.0, 4.5])
    yield_crypto = np.array([6.5, 7.0, 9.0])
    # Costs
    cost_dsr = np.array([real_data['dsr_cost'], 4.0, 2.0])
    cost_ops = np.array([0.5, 0.5, 0.5])
    
    # Net
    net_margins = (yield_rwa * 0.6 + yield_crypto * 0.4) - (cost_dsr * 0.7) - cost_ops # Simple weighted model
    
    plt.figure(figsize=(10, 6))
    x = np.arange(len(scenarios))
    width = 0.35
    
    plt.bar(x - width/2, yield_rwa * 0.6 + yield_crypto * 0.4, width, label='Gross Yield (Blended)', color='green')
    plt.bar(x + width/2, cost_dsr * 0.7 + cost_ops, width, label='Total Cost (DSR+Ops)', color='red')
    
    # Net line
    plt.plot(x, net_margins, color='black', marker='o', linewidth=2, label='Net Margin')
    
    plt.xticks(x, scenarios)
    plt.ylabel('cents per 1 DAI (%)')
    plt.title('4. Unit Economics: Profitability per Unit DAI')
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.savefig(os.path.join(DIAGRAMS_DIR, "4_unit_economics_scenarios.png"))
    plt.close()

    # 5. Stress Test Matrix (Heatmap)
    # X Axis: Crypto Market Crash (-%), Y Axis: T-Bill Yields (%)
    t_bill_rates = [0.5, 1.5, 3.0, 4.5, 6.0]
    crypto_crash = [0, -20, -40, -60, -80]
    
    # Solvency Score (Conceptual Model)
    # Low T-Bill = Low Rev. High Crash = Liquidation Risk.
    matrix = []
    for t in t_bill_rates:
        row = []
        for c in crypto_crash:
            # Score 0-100. 
            # High T-Bill (t) helps. severe crash (c) hurts.
            score = 50 + (t * 5) - (abs(c) * 0.8)
            row.append(score)
        matrix.append(row)
        
    plt.figure(figsize=(8, 6))
    im = plt.imshow(matrix, cmap='RdYlGn', origin='lower')
    plt.colorbar(im, label='Solvency Score')
    plt.xticks(range(len(crypto_crash)), [f'{x}%' for x in crypto_crash])
    plt.yticks(range(len(t_bill_rates)), [f'{x}%' for x in t_bill_rates])
    plt.xlabel('Crypto Market Drawdown')
    plt.ylabel('RWA (T-Bill) Yields')
    plt.title('5. Stress Test Matrix: The "Stagflation" Risk')
    plt.savefig(os.path.join(DIAGRAMS_DIR, "5_stress_test_matrix.png"))
    plt.close()

    # 6. Revenue Composition
    # RWA vs Crypto vs Fees
    labels = ['RWA (T-Bills)', 'Crypto Vaults', 'PSM Fees', 'Liquidation Fees']
    sizes = [60, 30, 5, 5] # Approx percentage
    
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['green', 'purple', 'grey', 'red'])
    plt.title('6. Revenue Composition (Heavily RWA Dependent)')
    plt.savefig(os.path.join(DIAGRAMS_DIR, "6_revenue_composition.png"))
    plt.close()

    print("✅ All 6 Business Plots Generated Successfully.")

if __name__ == "__main__":
    main()
