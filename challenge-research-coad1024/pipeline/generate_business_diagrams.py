
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Set style
sns.set_theme(style="whitegrid")
OUTPUT_DIR = r"c:\Users\DELL\Desktop\Research Challenge\challenge-research-coad1024\analysis\Liquity\Sustainability\Diagrams"
DATA_PATH = r"c:\Users\DELL\Desktop\Research Challenge\challenge-research-coad1024\analysis\Liquity\data\trove_snapshot_sepolia.csv"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_1_weighted_avg_rate_timeseries():
    """
    Simulates a 30-day time series of Weighted Avg Borrow Rate.
    Reason: We don't have historical data, so we model the 'Expected Rate' relative to base rate volatility.
    """
    days = 30
    dates = pd.date_range(start="2024-01-01", periods=days)
    
    # Simulate data
    np.random.seed(42)
    base_rate = np.linspace(3, 4, days) + np.random.normal(0, 0.1, days)
    weth_rate = base_rate + 1.5 + np.random.normal(0, 0.2, days) # Higher variance
    lst_rate = base_rate + 0.5 + np.random.normal(0, 0.05, days) # Stable
    system_avg = (weth_rate * 0.6) + (lst_rate * 0.4) # Weighted

    plt.figure(figsize=(10, 6))
    plt.plot(dates, weth_rate, label="WETH Branch (High Vol)", color="#6c5ce7", linewidth=2)
    plt.plot(dates, lst_rate, label="LST Branch (Low Vol)", color="#00cec9", linewidth=2)
    plt.plot(dates, system_avg, label="System Weighted Avg", color="#2d3436", linewidth=3, linestyle="--")
    
    plt.title("Modelled Weighted Average Borrow Rate (30 Days)", fontsize=14, fontweight='bold')
    plt.ylabel("Interest Rate (%)", fontsize=12)
    plt.xlabel("Date", fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(OUTPUT_DIR, "1_weighted_avg_rate_timeseries.png"))
    plt.close()
    print("Generated Plot 1")

def plot_2_interest_rate_distribution():
    """
    Uses REAL extracted data from trove_snapshot_sepolia.csv to plot the distribution.
    """
    try:
        df = pd.read_csv(DATA_PATH)
        if df.empty:
            raise ValueError("CSV is empty")
        
        # Filter active troves (debt > 0)
        df = df[df['debt_bold'] > 0]
        
        plt.figure(figsize=(10, 6))
        # Plot histogram weighted by debt
        sns.histplot(data=df, x="interest_rate_pct", weights="debt_bold", bins=20, color="#0984e3", kde=True)
        
        # Overlay Risk Zone
        plt.axvspan(0, 2.0, color='red', alpha=0.1, label="Redemption Risk Zone (<2%)")
        
        plt.title("Distribution of Interest Rates (Weighted by Debt)", fontsize=14, fontweight='bold')
        plt.xlabel("Interest Rate (%)", fontsize=12)
        plt.ylabel("Total Debt (BOLD)", fontsize=12)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(os.path.join(OUTPUT_DIR, "2_interest_rate_distribution.png"))
        plt.close()
        print("Generated Plot 2")
    except Exception as e:
        print(f"Skipping Plot 2 (Data Read Error): {e}")

def plot_3_sp_vs_debt_heatmap():
    """
    Simulates Solvency Coverage Ratio (SP Depth vs Liquidatable Debt).
    """
    days = 20
    time = np.arange(days)
    
    # Model: SP drains as liquidations happen, Liquidatable debt spikes during crashes
    sp_depth = np.linspace(100, 80, days) # SP Draining
    risky_debt = np.linspace(20, 90, days) # Risky Debt Rising
    
    plt.figure(figsize=(10, 6))
    plt.fill_between(time, sp_depth, color="#00b894", alpha=0.4, label="Stability Pool Deposits")
    plt.fill_between(time, risky_debt, color="#d63031", alpha=0.4, label="Liquidatable Debt (ICR < 110%)")
    
    # Risk Crossover
    crossover = np.argwhere(risky_debt > sp_depth)
    if len(crossover) > 0:
        plt.axvline(x=crossover[0], color='black', linestyle='--', label="Insolvency Crossover")

    plt.title("Solvency Coverage: SP Depth vs. Risk", fontsize=14, fontweight='bold')
    plt.ylabel("Amount (M BOLD)", fontsize=12)
    plt.xlabel("Simulation Timesteps (Volatility Event)", fontsize=12)
    plt.legend(loc="upper left")
    plt.savefig(os.path.join(OUTPUT_DIR, "3_sp_vs_liquidatable_debt.png"))
    plt.close()
    print("Generated Plot 3")

def plot_4_unit_economics():
    """
    Bar chart comparing Bull/Neutral/Bear scenarios detailed in the report.
    """
    scenarios = ["Bull (6.5%)", "Neutral (3.5%)", "Bear (1.0%)"]
    gross_rev = np.array([19.5, 3.5, 0.5]) # Millions
    cost_sp = gross_rev * 0.75
    net_rev = gross_rev * 0.25
    incentive_cost = np.array([1.0, 0.5, 0.5]) # Estimated fixed/variable costs
    
    x = np.arange(len(scenarios))
    width = 0.35
    
    plt.figure(figsize=(10, 6))
    
    # Stacked Bar: SP Cost vs Net Rev
    p1 = plt.bar(x, cost_sp, width, label='SP Yield Cost (75%)', color='#dfe6e9')
    p2 = plt.bar(x, net_rev, width, bottom=cost_sp, label='Protocol Net Revenue (25%)', color='#00b894')
    
    # Line for Breakeven
    plt.plot(x, incentive_cost, color='red', marker='o', linewidth=2, label='Incentive/OpEx Threshold')
    
    plt.title("Unit Economics: Scenario Analysis", fontsize=14, fontweight='bold')
    plt.ylabel("Annual Revenue (Million $)", fontsize=12)
    plt.xticks(x, scenarios)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    
    plt.savefig(os.path.join(OUTPUT_DIR, "4_unit_economics_scenarios.png"))
    plt.close()
    print("Generated Plot 4")

def plot_5_stress_matrix():
    """
    3x3 Heatmap of Net Profit vs Incentive Spend.
    """
    # Rows: Rates (1.5%, 3.5%, 6.0%) assuming 100M Debt
    # Cols: Incentive Spend ($0, $0.5M, $1.0M)
    
    debt = 100 # M
    rates = [0.015, 0.035, 0.060]
    incentives = [0.0, 0.5, 1.0] # M
    
    matrix = []
    for r in rates:
        row = []
        gross = debt * r
        net_protocol = gross * 0.25
        for i in incentives:
            profit = net_protocol - i
            row.append(profit)
        matrix.append(row)
        
    matrix_np = np.array(matrix)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrix_np, annot=True, fmt=".2f", cmap="RdYlGn", center=0,
                xticklabels=["$0", "$0.5M", "$1.0M"],
                yticklabels=["Bear (1.5%)", "Neutral (3.5%)", "Bull (6.0%)"])
    
    plt.title("Stress Matrix: Net Profit (Million $)", fontsize=14, fontweight='bold')
    plt.xlabel("Incentive Spend", fontsize=12)
    plt.ylabel("Interest Rate Environment", fontsize=12)
    plt.savefig(os.path.join(OUTPUT_DIR, "5_stress_test_matrix.png"))
    plt.close()
    print("Generated Plot 5")

def plot_6_branch_contribution():
    """
    Stacked bar of Branch Revenue Contribution.
    """
    branches = ["WETH", "wstETH", "rETH"]
    # Hypothetical data
    gross_rev = np.array([5.0, 2.0, 0.5]) # Millions
    retained = gross_rev * 0.25
    sp_cost = gross_rev * 0.75
    
    plt.figure(figsize=(8, 6))
    plt.bar(branches, sp_cost, label="SP Yield (75%)", color='#b2bec3')
    plt.bar(branches, retained, bottom=sp_cost, label="Retained (25%)", color='#0984e3')
    
    plt.title("Branch Revenue Contribution", fontsize=14, fontweight='bold')
    plt.ylabel("Revenue (Million $)", fontsize=12)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.savefig(os.path.join(OUTPUT_DIR, "6_branch_contribution.png"))
    plt.close()
    print("Generated Plot 6")

if __name__ == "__main__":
    plot_1_weighted_avg_rate_timeseries()
    plot_2_interest_rate_distribution()
    plot_3_sp_vs_debt_heatmap()
    plot_4_unit_economics()
    plot_5_stress_matrix()
    plot_6_branch_contribution()
