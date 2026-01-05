import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import csv

# Base Paths (Relative to script execution from root)
base_dir = r"challenge-research-coad1024/analysis/makerdao/Sustainability/Diagrams"
paths = {
    "metrics": os.path.join(base_dir, "Key Metrics"),
    "triangle": os.path.join(base_dir, "Sustainability Triangle"),
    "regime": os.path.join(base_dir, "Formal Regime Analysis"),
    "ops": os.path.join(base_dir, "Operational and Regulatory")
}

# Ensure directories exist
for p in paths.values():
    os.makedirs(p, exist_ok=True)

# Style settings
plt.style.use('ggplot')
colors = {'blue': '#1f77b4', 'red': '#d62728', 'green': '#2ca02c', 'grey': '#7f7f7f', 'orange': '#ff7f0e', 'purple': '#9467bd'}

def load_data(csv_path):
    """
    Attempts to load financial data from a CSV file.
    Expected format: key,value
    """
    data = {}
    if not csv_path or not os.path.exists(csv_path):
        print("\033[93mWARNING: No valid CSV data found. Using HARDCODED SIMULATION inputs.\033[0m")
        return None
    
    try:
        with open(csv_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    try:
                        data[row[0].strip()] = float(row[1])
                    except ValueError:
                        pass
        print(f"\033[92mSuccessfully loaded real data from {csv_path}\033[0m")
        return data
    except Exception as e:
        print(f"\033[91mError reading CSV: {e}. Reverting to simulation.\033[0m")
        return None

def save_plot(fig, folder_key, filename):
    path = os.path.join(paths[folder_key], filename)
    fig.savefig(path, dpi=300, bbox_inches='tight')
    print(f"Saved {filename} to {paths[folder_key]}")
    plt.close(fig)

# ==========================================
# 1. Key Metrics & Health Indicators
# ==========================================

def plot_nim_waterfall_maker(data=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Load from data or use defaults (Approximated 2025 Financials)
    gross_yield = data.get('gross_yield', 5.5) if data else 5.5
    dsr_cost = data.get('dsr_cost', -3.5) if data else -3.5
    opex = data.get('opex', -0.5) if data else -0.5
    emissions = data.get('emissions', -0.2) if data else -0.2
    
    net_surplus = gross_yield + dsr_cost + opex + emissions
    
    values = [gross_yield, dsr_cost, opex, emissions, net_surplus]
    labels = ['Gross Yield (RWA+Fees)', 'DSR Cost', 'OpEx', 'Emissions', 'Net Protocol Surplus']
    
    # Calculate cumulative sums for waterfall
    cumulative = [0, gross_yield, gross_yield + dsr_cost, gross_yield + dsr_cost + opex, gross_yield + dsr_cost + opex + emissions, 0]
    
    # Plot
    for i in range(len(values)):
        color = colors['green'] if values[i] >= 0 else colors['red']
        if i == len(values) - 1: # Total
            color = colors['blue']
            bottom = 0
            
            # Draw connector for total
            prev_height = cumulative[i]
            ax.plot([i-1 + 0.4, i - 0.4], [prev_height, prev_height], 'k--', linewidth=0.5)

        else:
            bottom = sum(values[:i])
            # Draw connector
            if i > 0:
                 prev_height = sum(values[:i])
                 ax.plot([i-1 + 0.4, i - 0.4], [prev_height, prev_height], 'k--', linewidth=0.5)

        ax.bar(labels[i], values[i], bottom=bottom, color=color, edgecolor='black', width=0.6)

    ax.set_title(f"MakerDAO Net Interest Margin (NIM) Structure {'(SIMULATED)' if not data else '(REAL DATA)'}")
    ax.set_ylabel('Percentage Yield (%)')
    ax.axhline(0, color='black', linewidth=0.8)
    plt.xticks(rotation=15)
    
    save_plot(fig, "metrics", "nim_formula_schematic.png")

def plot_surplus_buffer_maker(data=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    months = np.arange(0, 36)
    # Maker Surplus growth is steadier due to RWA yield irrespective of bear market
    
    start_equity = data.get('start_equity', 50) if data else 50
    growth_rate = data.get('growth_rate', 2.0) if data else 2.0
    
    # Base growth
    base_growth = np.linspace(start_equity, start_equity + (36*growth_rate), 36) 
    # Volatility overlay (crypto fees)
    volatility = np.sin(months * 0.5) * 10
    
    surplus = base_growth + volatility
    
    ax.plot(months, surplus, color=colors['green'], linewidth=2.5, label='Surplus Buffer ($M)')
    
    # Survival Threshold
    ax.axhline(y=30.0, color=colors['red'], linestyle='--', linewidth=2, label='Survival Threshold (OpEx/Risk)')
    
    ax.fill_between(months, 0, 30.0, color=colors['red'], alpha=0.1)
    ax.fill_between(months, 0, surplus, color=colors['green'], alpha=0.05)
    
    ax.text(6, start_equity + 10, 'RWA Yield Stabilizes Growth', fontsize=10, ha='center', bbox=dict(facecolor='white', alpha=0.7))
    ax.text(24, start_equity + (24*growth_rate) - 10, 'Crypto Fee Volatility\nDampened by RWAs', fontsize=10, ha='center', bbox=dict(facecolor='white', alpha=0.7))
    
    ax.set_title('MakerDAO Surplus Buffer Growth (RWA Era)')
    ax.set_xlabel('Months')
    ax.set_ylabel('Surplus Equity ($M)')
    ax.legend()
    
    save_plot(fig, "metrics", "surplus_buffer_growth.png")

def plot_cogs_maker(data=None):
    fig, ax = plt.subplots(figsize=(8, 6))
    
    categories = ['Competitor (Pure Crypto)', 'MakerDAO (Hybrid)']
    
    # Defaults
    maker_cost = data.get('maker_capital_cost', 0.85) if data else 0.85
    maker_opex = data.get('maker_opex', 0.1) if data else 0.1
    
    capital_cost = [0.1, maker_cost] 
    opex = [0.2, maker_opex] 
    execution = [0.05, 0.05]
    
    # Stacked Bar
    ax.bar(categories, capital_cost, label='Cost of Capital (DSR)', color=colors['orange'])
    ax.bar(categories, opex, bottom=capital_cost, label='OpEx / Governance', color=colors['blue'])
    ax.bar(categories, execution, bottom=np.array(capital_cost)+np.array(opex), label='Execution', color=colors['grey'])
    
    ax.set_title('Unit Economics: Cost of Goods Sold (COGS)')
    ax.set_ylabel('Cost per $1 Revenue')
    ax.legend()
    
    save_plot(fig, "metrics", "cogs_breakdown.png")

# ==========================================
# 2. Sustainability Triangle & Ops
# ==========================================

def plot_triangle_radar_maker(data=None):
    categories = ['Collateral Quality', 'Incentive Mechanics', 'Governance/Backstop']
    N = len(categories)
    
    s_col = data.get('score_collateral', 4.5) if data else 4.5
    s_inc = data.get('score_incentives', 4.5) if data else 4.5
    s_gov = data.get('score_governance', 4.0) if data else 4.0
    
    values = [s_col, s_inc, s_gov] 
    values += values[:1] 
    
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    ax.plot(angles, values, linewidth=2, linestyle='solid', color=colors['purple'])
    ax.fill(angles, values, color=colors['purple'], alpha=0.2)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_yticks([1, 2, 3, 4, 5])
    
    ax.set_title('MakerDAO Sustainability Triangle assessment', y=1.1)
    
    save_plot(fig, "triangle", "sustainability_triangle_diagram.png")

def plot_variance_regime_maker():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Maker has a wider stable regime due to RWAs
    tcr = np.linspace(1.05, 2.0, 100) 
    # Variance is lower for Maker due to uncorrelated assets
    variance = 0.005 / ((tcr - 1.02)**2) # Stabilizes faster
    
    ax.plot(tcr*100, variance, color=colors['blue'], linewidth=2)
    
    ax.set_xlim(200, 105) 
    ax.set_ylim(0, 5)
    
    ax.axvline(x=110, color='black', linestyle='--', label='Liquidation Ratio')
    
    ax.text(170, 0.5, 'Stable Regime\n(RWA Anchored)', ha='center', color='green')
    ax.text(115, 3.0, 'Unstable Regime\n(Deleveraging)', ha='center', color='red')
    
    ax.set_title('Regime Transition: Price Variance (RWA Buffered)')
    ax.set_xlabel('Collateral Ratio %')
    ax.set_ylabel('Price Variance')
    ax.legend()
    
    save_plot(fig, "regime", "variance_regime_plot.png")

def plot_regulatory_radar_maker(data=None):
    categories = ['Censorship\nResistance', 'Compliance\nFriction', 'Asset Seizure\nRisk', 'Regulatory\nMoat']
    N = len(categories)
    
    stats = [
        data.get('reg_censorship', 2.0) if data else 2.0,
        data.get('reg_friction', 4.5) if data else 4.5,
        data.get('reg_seizure', 4.5) if data else 4.5,
        data.get('reg_moat', 5.0) if data else 5.0
    ]
    stats += stats[:1]
    
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    ax.plot(angles, stats, linewidth=2, linestyle='solid', label='MakerDAO (Endgame)', color=colors['red'])
    ax.fill(angles, stats, color=colors['red'], alpha=0.2)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    
    ax.set_title('MakerDAO Regulatory Risk Profile', y=1.1)
    
    save_plot(fig, "ops", "regulatory_risk_radar.png")

def plot_incentive_roi_maker(data=None):
    fig, ax = plt.subplots(figsize=(8, 6))

    categories = ['RWA Yields', 'Crypto Fees', 'SubDAO Emissions']
    values = [
        data.get('roi_rwa', 3.0) if data else 3.0,
        data.get('roi_crypto', 1.5) if data else 1.5,
        data.get('roi_emissions', 0.8) if data else 0.8
    ]

    ax.bar(categories, values, color=[colors['green'], colors['blue'], colors['red']], width=0.5)
    ax.axhline(1.0, color='black', linestyle='--', linewidth=0.8, label='Breakeven')

    ax.set_title('Capital Efficiency (ROI) by Channel')
    ax.set_xlabel('Source')
    ax.set_ylabel('Revenue per $1 Cost/Risk')
    ax.legend()

    save_plot(fig, "metrics", "incentive_efficiency_roi.png")
    
def plot_keeper_breakeven_maker(data=None):
     # Same logic as Liquity but higher revenue base due to larger vaults
    fig, ax = plt.subplots(figsize=(10, 6))
    gas_gwei = np.linspace(10, 500, 100)
    cost_usd = gas_gwei * 0.8 # Higher gas usage for Maker complex vaults
    
    rev_base = data.get('keeper_revenue', 400) if data else 400
    revenue_usd = np.full_like(gas_gwei, rev_base) 
    
    ax.plot(gas_gwei, revenue_usd, color=colors['green'], label='Fixed Compensation')
    ax.plot(gas_gwei, cost_usd, color=colors['red'], label='Gas Cost')
    
    idx = np.argwhere(np.diff(np.sign(revenue_usd - cost_usd))).flatten()
    if len(idx) > 0:
        ax.plot(gas_gwei[idx], revenue_usd[idx], 'ko')
        
    ax.fill_between(gas_gwei, cost_usd, revenue_usd, where=(revenue_usd > cost_usd), color='green', alpha=0.1)
    
    ax.set_title('Keeper Profitability (MakerDAO Complex Vaults)')
    ax.set_xlabel('Gas Price (Gwei)')
    ax.legend()
    save_plot(fig, "triangle", "keeper_breakeven_plot.png")

if __name__ == "__main__":
    csv_input = None
    if len(sys.argv) > 1:
        csv_input = sys.argv[1]
    
    data = load_data(csv_input)
    
    print("Generating MakerDAO Sustainability plots...")
    plot_nim_waterfall_maker(data)
    plot_surplus_buffer_maker(data)
    plot_cogs_maker(data)
    plot_incentive_roi_maker(data)
    plot_triangle_radar_maker(data)
    plot_variance_regime_maker() # Analytical, no data needed
    plot_regulatory_radar_maker(data)
    plot_keeper_breakeven_maker(data)
    print("Done.")
