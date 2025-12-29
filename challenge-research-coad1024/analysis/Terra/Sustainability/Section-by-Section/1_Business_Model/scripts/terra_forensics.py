import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# CONFIGURATION
# ==========================================
METRICS_FILE = 'terra_daily_metrics.csv'
RESERVES_FILE = 'lfg_reserves.csv'

# Regime Definitions
# Note: We focus on Structural Diagnostics, not microstructure collapse
COLLAPSE_START = '2022-05-07' 

# Conservative rates for subsidy calculation
DEPOSIT_YIELD = 0.195   # 19.5% APY
BORROW_YIELD = 0.12     # 12% APY

# Liquidity stress assumption
LIQUIDITY_HAIRCUT = 0.30   # 30% accessible

# ==========================================
# HELPERS
# ==========================================
def require_columns(df, cols, name):
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise ValueError(f"{name} missing columns: {missing}")

def standard_chart_style(ax, title, xlabel='', ylabel=''):
    ax.set_title(title, fontsize=12, fontweight='bold', pad=15)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# ==========================================
# PLOT 1: UST Liabilities vs Absorber (Stock View)
# ==========================================
def plot_liabilities_vs_absorber(df):
    """
    Visual Contract:
    - UST Supply (Liabilities)
    - LUNA Market Cap (Nominal Absorber)
    - Stressed LUNA Cap (Realistic Absorber)
    - NO spreads, NO oracle latency
    """
    require_columns(df, ['Date', 'UST_Supply', 'LUNA_MarketCap'], "Metrics")
    
    df['Stressed_LUNA_Cap'] = df['LUNA_MarketCap'] * LIQUIDITY_HAIRCUT
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(df['Date'], df['UST_Supply'], label='UST Liabilities (Demand)', color='#D62728', linewidth=2)
    ax.plot(df['Date'], df['LUNA_MarketCap'], label='LUNA Market Cap (Nominal Absorber)', color='#1F77B4', linewidth=1.5)
    ax.plot(df['Date'], df['Stressed_LUNA_Cap'], label='LUNA Stressed Capacity (30%)', color='#1F77B4', linestyle=':', linewidth=1.5)
    
    ax.fill_between(df['Date'], df['UST_Supply'], df['Stressed_LUNA_Cap'], 
                    where=(df['UST_Supply'] > df['Stressed_LUNA_Cap']), 
                    color='red', alpha=0.1, label='Structural Insolvency Risk')

    standard_chart_style(ax, 'The Balance Sheet: Liabilities vs. Absorber Capacity', ylabel='USD Value (Billions)')
    ax.legend(loc='upper left', frameon=False)
    
    plt.savefig('fig1_liabilities_vs_absorber.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated Plot 1: Liabilities vs Absorber")

# ==========================================
# PLOT 2: Anchor Deposits vs Borrows (Structural Imbalance)
# ==========================================
def plot_anchor_imbalance(df):
    """
    Visual Contract:
    - Anchor Deposits (Liability)
    - Anchor Borrows (Asset)
    - Gap visualization
    """
    require_columns(df, ['Date', 'Anchor_Deposits', 'Anchor_Borrows'], "Metrics")
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(df['Date'], df['Anchor_Deposits'], label='Deposits (Yield Seekers)', color='#FF7F0E', linewidth=2)
    ax.plot(df['Date'], df['Anchor_Borrows'], label='Borrows (Revenue Source)', color='#2CA02C', linewidth=2)
    
    ax.fill_between(df['Date'], df['Anchor_Deposits'], df['Anchor_Borrows'], 
                    color='gray', alpha=0.1, label='Unproductive Capital (Subsidy Required)')
    
    standard_chart_style(ax, 'Anchor Protocol: The Structural Imbalance', ylabel='USD Value (Billions)')
    ax.legend(loc='upper left', frameon=False)
    
    plt.savefig('fig2_anchor_imbalance.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated Plot 2: Anchor Imbalance")

# ==========================================
# PLOT 3: Cumulative Anchor Subsidy (Negative Carry)
# ==========================================
def plot_cumulative_subsidy(df):
    """
    Visual Contract:
    - Cumulative subsidy required
    - Economic Subsidy (Conservative) label
    """
    require_columns(df, ['Date', 'Anchor_Deposits', 'Anchor_Borrows'], "Metrics")
    
    # Calculate Flows
    daily_cost = df['Anchor_Deposits'] * (DEPOSIT_YIELD / 365.0)
    daily_revenue = df['Anchor_Borrows'] * (BORROW_YIELD / 365.0)
    daily_subsidy = daily_cost - daily_revenue
    cumulative_subsidy = daily_subsidy.cumsum()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(df['Date'], cumulative_subsidy, color='#8C564B', linewidth=2, label='Estimated Economic Subsidy (Conservative)')
    ax.fill_between(df['Date'], cumulative_subsidy, color='#8C564B', alpha=0.1)
    
    standard_chart_style(ax, 'Cumulative Equity Consumed for Stability', ylabel='USD Value')
    ax.legend(loc='upper left', frameon=False)
    
    plt.savefig('fig3_cumulative_subsidy.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated Plot 3: Cumulative Subsidy")

# ==========================================
# PLOT 4: Reflexivity Test (Regime Correlation)
# ==========================================
def plot_reflexivity(df):
    """
    Visual Contract:
    - Rolling correlation (30D)
    - Split by Expansion/Contraction
    """
    require_columns(df, ['Date', 'UST_Supply', 'LUNA_MarketCap'], "Metrics")
    
    df['dUST'] = df['UST_Supply'].pct_change()
    df['dLUNA'] = df['LUNA_MarketCap'].pct_change()
    
    # Define Regimes
    expansion = df[df['dUST'] > 0].copy()
    contraction = df[df['dUST'] < 0].copy()
    
    # Calculate Rolling Correlations
    # Note: Rolling on filtered data creates gaps, so we calc on full then mask
    rolling_corr = df['dUST'].rolling(30).corr(df['dLUNA'])
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(df['Date'], rolling_corr, color='gray', alpha=0.3, label='30D Correlation (Raw)')
    
    # Highlight Regimes
    # We plot correlation only where the regime holds, or simplified: 
    # Just show that correlation is POSITIVE during growth (Reflexive Up)
    # and POSITIVE during crash (Reflexive Down)
    # The user asked for "Split into Expansion/Contraction regime".
    
    ax.scatter(expansion['Date'], [rolling_corr[i] for i in expansion.index], 
               s=10, color='blue', alpha=0.5, label='Expansion Regime (Reflexive Up)')
    
    ax.scatter(contraction['Date'], [rolling_corr[i] for i in contraction.index], 
               s=10, color='red', alpha=0.5, label='Contraction Regime (Reflexive Down)')

    standard_chart_style(ax, 'Reflexivity Test: Correlation of Liabilities & Absorber', ylabel='Correlation Coeff')
    ax.axhline(0, color='black', linewidth=1)
    ax.legend(loc='upper left', frameon=False)
    
    plt.savefig('fig4_reflexivity.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated Plot 4: Reflexivity Test")

# ==========================================
# PLOT 5: Reserve Coverage Ratio (Illusion)
# ==========================================
def plot_reserve_coverage(df_metrics, df_reserves):
    """
    Visual Contract:
    - Reserves / UST Supply
    - Highlight < 20%
    """
    merged = pd.merge(df_metrics, df_reserves, on='Date', how='left').fillna(0)
    
    merged['Reserve_Val'] = merged['BTC_Balance'] * merged['BTC_Price']
    merged['Coverage'] = merged['Reserve_Val'] / merged['UST_Supply']
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(merged['Date'], merged['Coverage'], color='green', linewidth=2, label='LFG Reserve Coverage')
    ax.axhline(0.2, color='red', linestyle='--', label='20% Threshold (Critical)')
    
    standard_chart_style(ax, 'Reserve Adequacy: The Illusion of Backing', ylabel='Coverage Ratio (1.0 = 100%)')
    ax.legend(loc='upper left', frameon=False)
    
    plt.savefig('fig5_reserve_coverage.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated Plot 5: Reserve Coverage")

# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":
    print("Terra Business Model Decomposition - Visual Contract Generator")
    print("------------------------------------------------------------")
    
    # Load Data
    try:
        df = pd.read_csv(METRICS_FILE, parse_dates=['Date'])
        # Handle case where Reserves might be missing or empty
        try:
            df_reserves = pd.read_csv(RESERVES_FILE, parse_dates=['Date'])
        except FileNotFoundError:
             df_reserves = pd.DataFrame({'Date': df['Date'], 'BTC_Balance': 0, 'BTC_Price': 0})

        # Execute Plot Contract
        plot_liabilities_vs_absorber(df)
        plot_anchor_imbalance(df)
        plot_cumulative_subsidy(df)
        plot_reflexivity(df)
        plot_reserve_coverage(df, df_reserves)
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please run the Data Pipeline to generate input CSVs.")

