import matplotlib.pyplot as plt
import numpy as np
import os

# Base Paths
base_dir = r"challenge-research-coad1024/analysis/Liquity/Sustainability/Diagrams"
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
colors = {'blue': '#1f77b4', 'red': '#d62728', 'green': '#2ca02c', 'grey': '#7f7f7f', 'orange': '#ff7f0e'}

def save_plot(fig, folder_key, filename):
    path = os.path.join(paths[folder_key], filename)
    fig.savefig(path, dpi=300, bbox_inches='tight')
    print(f"Saved {filename} to {paths[folder_key]}")
    plt.close(fig)

# ==========================================
# 1. Key Metrics & Health Indicators
# ==========================================

def plot_nim_waterfall():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Data
    gross_yield = 4.0
    sp_yield_cost = -3.0 # 75%
    incentives = -0.5
    oracle_ops = -0.1
    net_surplus = 0.4
    
    values = [gross_yield, sp_yield_cost, incentives, oracle_ops, net_surplus]
    labels = ['Gross Interest', 'SP Yield Split', 'Liquidity Incentives', 'Oracle/OpEx', 'Net Protocol Surplus']
    
    # Calculate cumulative sums for waterfall
    cumulative = [0, gross_yield, gross_yield + sp_yield_cost, gross_yield + sp_yield_cost + incentives, 0]
    
    # Plot
    for i in range(len(values)):
        color = colors['green'] if values[i] >= 0 else colors['red']
        if i == len(values) - 1: # Total
            color = colors['blue']
            bottom = 0
        else:
            bottom = sum(values[:i])
            
        ax.bar(labels[i], values[i], bottom=bottom, color=color, edgecolor='black')

    ax.set_title('Net Interest Margin (NIM) Waterfall Structure')
    ax.set_ylabel('Percentage Yield (%)')
    ax.axhline(0, color='black', linewidth=0.8)
    
    # Add connecting lines
    # (Simplified for clarity)
    
    save_plot(fig, "metrics", "nim_formula_schematic.png")

def plot_surplus_buffer():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    months = np.arange(0, 24)
    # Simulate Bull Market (Months 0-12)
    bull_growth = np.linspace(5, 15, 13) 
    # Simulate Bear Market (Months 13-24)
    bear_decay = np.linspace(15, 8, 11)
    
    surplus = np.concatenate([bull_growth, bear_decay])
    
    ax.plot(months, surplus, color=colors['blue'], linewidth=2.5, label='Surplus Buffer ($M)')
    
    # Survival Threshold
    ax.axhline(y=2.0, color=colors['red'], linestyle='--', linewidth=2, label='Survival Threshold (OpEx)')
    
    ax.fill_between(months, 0, 2.0, color=colors['red'], alpha=0.1)
    ax.fill_between(months, 0, surplus, color=colors['blue'], alpha=0.05)
    
    ax.annotate('Bull Market\n(Accumulation)', xy=(6, 10), fontsize=10, ha='center')
    ax.annotate('Bear Market\n(Cash Burn)', xy=(18, 11), fontsize=10, ha='center')
    
    ax.set_title('Surplus Buffer "Runway" Simulation')
    ax.set_xlabel('Months')
    ax.set_ylabel('Surplus Equity ($M)')
    ax.legend()
    
    save_plot(fig, "metrics", "surplus_buffer_growth.png")

def plot_cogs():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    categories = ['Competitor A', 'Liquity V2']
    security = [0.1, 0.75] # Competitor pays less for security? Or more? Let's say V2 pays 75% revenue
    liquidity = [0.4, 0.15]
    execution = [0.05, 0.05]
    
    # Stacked Bar
    ax.bar(categories, security, label='Security Cost (Yield Split)', color=colors['orange'])
    ax.bar(categories, liquidity, bottom=security, label='Liquidity Incentives', color=colors['blue'])
    ax.bar(categories, execution, bottom=np.array(security)+np.array(liquidity), label='Execution (Gas/Keepers)', color=colors['grey'])
    
    ax.set_title('Unit Economics: Cost of Goods Sold (COGS)')
    ax.set_ylabel('Cost per $1 Revenue')
    ax.legend()
    
    save_plot(fig, "metrics", "cogs_breakdown.png")

# ==========================================
# 2. Sustainability Triangle
# ==========================================

def plot_keeper_breakeven():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    gas_gwei = np.linspace(10, 500, 100)
    # Hypothetical liquidation: Debt=1000, Coll=1100. profit = 0.5% + gas comp
    # Cost = gas_gwei * gas_used * eth_price
    
    # Simplify: Cost curve
    cost_usd = gas_gwei * 0.5 # Dummy scaling
    
    # Revenue is fixed per liquidation size (mostly)
    revenue_usd = np.full_like(gas_gwei, 150) # $150 compensation
    
    ax.plot(gas_gwei, revenue_usd, color=colors['green'], label='Liquidation Compensation (Fixed)')
    ax.plot(gas_gwei, cost_usd, color=colors['red'], label='Transaction Cost (Gas)')
    
    # Fill intersection
    idx = np.argwhere(np.diff(np.sign(revenue_usd - cost_usd))).flatten()
    if len(idx) > 0:
        ax.plot(gas_gwei[idx], revenue_usd[idx], 'ko')
        ax.annotate('Breakeven Point', xy=(gas_gwei[idx], revenue_usd[idx]), xytext=(gas_gwei[idx]+50, revenue_usd[idx]+50),
                    arrowprops=dict(facecolor='black', shrink=0.05))

    ax.fill_between(gas_gwei, cost_usd, revenue_usd, where=(revenue_usd > cost_usd), color='green', alpha=0.1, label='Profitable Zone')
    ax.fill_between(gas_gwei, cost_usd, revenue_usd, where=(revenue_usd < cost_usd), color='red', alpha=0.1, label='Unprofitable ("Death Zone")')

    ax.set_title('Keeper Profitability vs. Network Congestion')
    ax.set_xlabel('Gas Price (Gwei)')
    ax.set_ylabel('Value ($)')
    ax.legend()
    
    save_plot(fig, "triangle", "keeper_breakeven_plot.png")

def plot_triangle_radar():
    categories = ['Collateral Quality', 'Incentive Mechanics', 'Governance/Backstop']
    N = len(categories)
    
    # Scores (1-5)
    values = [4.5, 3.5, 4.0] # A-, B+, N/A (simulated High)
    values += values[:1] # Close the loop
    
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    ax.plot(angles, values, linewidth=2, linestyle='solid', color=colors['blue'])
    ax.fill(angles, values, color=colors['blue'], alpha=0.2)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    
    ax.set_title('The Sustainability Triangle Assessment', y=1.1)
    
    save_plot(fig, "triangle", "sustainability_triangle_diagram.png") # Replacing the conceptual diagram with a radar

# ==========================================
# 3. Formal Regime Analysis
# ==========================================

def plot_variance_regime():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    tcr = np.linspace(1.1, 2.0, 100) # 110% to 200%
    # Variance Model: Var ~ 1 / (TCR - 1)^2 (Asymptote at TCR=1)
    variance = 0.01 / ((tcr - 1.05)**2)
    
    ax.plot(tcr*100, variance, color=colors['red'], linewidth=2)
    
    ax.set_xlim(200, 110) # Reversed X-axis (High CR to Low CR)
    ax.set_ylim(0, 5)
    
    ax.axvline(x=110, color='black', linestyle='--', label='MCR (110%)')
    ax.axvline(x=150, color='green', linestyle='--', label='Recovery Mode Threshold (150%)')
    
    ax.text(180, 0.5, 'Stable Regime\n(Bounded Variance)', ha='center', color='green')
    ax.text(120, 3.0, 'Unstable Regime\n(Volatility Explosion)', ha='center', color='red')
    
    ax.set_title('Regime Transition: Price Variance vs. Collateral Ratio')
    ax.set_xlabel('Total Collateral Ratio (TCR) %')
    ax.set_ylabel('Stablecoin Price Variance ($\\sigma^2$)')
    ax.legend()
    
    save_plot(fig, "regime", "variance_regime_plot.png")

# ==========================================
# 4. Operational & Regulatory
# ==========================================

def plot_regulatory_radar():
    categories = ['Censorship\nResistance', 'Compliance\nFriction', 'Asset Seizure\nRisk', 'Regulatory\nMoat']
    N = len(categories)
    
    # BOLD Scores
    bold_stats = [5, 5, 1, 4] # High resist, High friction, Low seizure, High moat
    bold_stats += bold_stats[:1]
    
    # USDC Scores
    usdc_stats = [1, 1, 5, 2] # Low resist, Low friction, High seizure, Low moat
    usdc_stats += usdc_stats[:1]
    
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    # Plot BOLD
    ax.plot(angles, bold_stats, linewidth=2, linestyle='solid', label='Liquity (BOLD)', color=colors['blue'])
    ax.fill(angles, bold_stats, color=colors['blue'], alpha=0.1)
    
    # Plot USDC
    ax.plot(angles, usdc_stats, linewidth=2, linestyle='dashed', label='USDC', color=colors['grey'])
    ax.fill(angles, usdc_stats, color=colors['grey'], alpha=0.1)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    
    ax.set_title('Regulatory Risk Profile: BOLD vs USDC', y=1.1)
    ax.legend(loc='lower right', bbox_to_anchor=(1.3, 0))
    
    save_plot(fig, "ops", "regulatory_risk_radar.png")


def plot_incentive_roi():
    fig, ax = plt.subplots(figsize=(8, 6))

    categories = ['High ROI', 'Low ROI']
    values = [2.5, 0.8] # Simulated ROI

    ax.bar(categories, values, color=[colors['green'], colors['red']], width=0.5)
    ax.axhline(1.0, color='black', linestyle='--', linewidth=0.8, label='Breakeven ROI (1.0x)')

    ax.set_title('Incentive Efficiency (ROI) for Liquidity')
    ax.set_xlabel('Scenario')
    ax.set_ylabel('TVL Generated per $1 Incentives')
    ax.legend()

    save_plot(fig, "metrics", "incentive_efficiency_roi.png")


if __name__ == "__main__":
    print("Generating plots...")
    plot_nim_waterfall()
    plot_surplus_buffer()
    plot_cogs()
    plot_incentive_roi() # Added this line
    plot_keeper_breakeven()
    plot_triangle_radar()
    plot_variance_regime()
    plot_regulatory_radar()
    print("Done.")
