import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# CONFIGURATION & CONSTANTS
# ==========================================
METRICS_FILE = 'terra_daily_metrics.csv'
RESERVES_FILE = 'lfg_reserves.csv'

# Regime Definitions
COLLAPSE_START = '2022-05-07'
COLLAPSE_END = '2022-05-12'

# Conservative APY Approximations
# NOTE: In reality, Anchor rates fluctuated. We use a conservative
# baseline to estimate structural deficit. 
# Realized cost was often higher due to "Yield Reserve" top-ups.
DEPOSIT_YIELD = 0.195  # 19.5% APY
BORROW_YIELD = 0.12    # 12.0% APY

def add_regime_shading(plt_obj):
    """Adds shading for the collapse window."""
    plt_obj.axvspan(COLLAPSE_START, COLLAPSE_END, color='gray', alpha=0.2, label='Collapse Window')

def plot_absorber_capacity(df):
    """
    Task 1: The Absorber Ratio
    Tests if LUNA Market Cap was sufficient to absorb UST liabilities.
    Includes a 'Stressed' metric assuming 70% liquidity haircut during panic.
    """
    plt.figure(figsize=(12, 6))
    
    # Primitives
    df['AbsorberRatio'] = df['LUNA_MarketCap'] / df['UST_Supply']
    
    # Stressed Model: Assume only 30% of Market Cap is accessible liquidity in a crash
    df['Stressed_LUNA_Cap'] = df['LUNA_MarketCap'] * 0.3
    df['Stressed_AbsorberRatio'] = df['Stressed_LUNA_Cap'] / df['UST_Supply']
    
    # Plot Stock Variables
    plt.plot(df['Date'], df['LUNA_MarketCap'], label='LUNA Market Cap (Nominal)', color='blue')
    plt.plot(df['Date'], df['Stressed_LUNA_Cap'], label='LUNA Market Cap (Stressed 30%)', color='cyan', linestyle=':')
    plt.plot(df['Date'], df['UST_Supply'], label='UST Supply (Liabilities)', color='red', linewidth=2)
    
    # Highlight Exhaustion
    exhaustion = df[df['AbsorberRatio'] < 1.0]
    if not exhaustion.empty:
        plt.scatter(exhaustion['Date'], exhaustion['UST_Supply'], color='black', marker='x', label='Absorber Capacity Exhausted (<1.0)')

    add_regime_shading(plt)
    
    plt.title('Absorber Capacity: Nominal vs Stressed LUNA Liquidity')
    plt.ylabel('USD Value')
    plt.legend(loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.savefig('fig1_absorber_capacity.png')
    print("Generated fig1_absorber_capacity.png")

def plot_cumulative_subsidy(df):
    """
    Task 2: Cumulative Subsidy (Negative Carry)
    Visualizes the structural cash burn required to maintain Anchor yields.
    """
    plt.figure(figsize=(12, 6))
    
    # Flow Calculations
    # Daily Subsidy = Outflow (Depositor Pay) - Inflow (Borrower Pay)
    df['Daily_Outflow'] = df['Anchor_Deposits'] * (DEPOSIT_YIELD / 365.0)
    df['Daily_Inflow'] = df['Anchor_Borrows'] * (BORROW_YIELD / 365.0)
    df['Daily_Subsidy'] = df['Daily_Outflow'] - df['Daily_Inflow']
    
    # Cumulative Sum
    df['Cumulative_Subsidy'] = df['Daily_Subsidy'].cumsum()
    
    plt.plot(df['Date'], df['Cumulative_Subsidy'], color='darkred', linewidth=2, label='Cumulative Subsidy Cost')
    plt.fill_between(df['Date'], df['Cumulative_Subsidy'], color='red', alpha=0.1)
    
    add_regime_shading(plt)

    plt.title('Anchor Protocol: Cumulative Structural Deficit (Equity-Funded Subsidy)')
    plt.ylabel('USD Cumulative Deficit')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('fig2_cumulative_subsidy.png')
    print("Generated fig2_cumulative_subsidy.png")

def plot_flow_dominance(df):
    """
    Task 3: Flow Dominance (Exit Pressure vs Absorption)
    Tests if daily exit flow exceeded the system's capacity to absorb it.
    """
    plt.figure(figsize=(12, 6))
    
    # Calculate Exit Pressure (Daily decrease in UST supply = Redemptions/Exits)
    # We take negative diff because drop in supply = exit
    df['Exit_Pressure'] = -df['UST_Supply'].diff().clip(upper=0) 
    
    # Absorption Capacity (7-day rolling average of LUNA Mcap)
    df['Absorption_Capacity'] = df['LUNA_MarketCap'].rolling(7).mean()
    
    # Ratio
    df['Flow_Ratio'] = df['Exit_Pressure'] / df['Absorption_Capacity']
    
    # Plot on dual axis? No, ratio is cleaner.
    plt.plot(df['Date'], df['Flow_Ratio'], label='Exit Pressure / Market Cap', color='purple')
    
    # Thresholds
    plt.axhline(y=0.05, color='orange', linestyle='--', label='Warning (5% Cap)')
    plt.axhline(y=0.10, color='red', linestyle='--', label='Critical (10% Cap)')
    
    add_regime_shading(plt)
    
    plt.title('Flow Dominance: Exit Pressure vs Absorber Capacity')
    plt.ylabel('Flow Ratio')
    plt.legend()
    plt.semilogy() # Log scale often helps see the spike
    plt.grid(True, alpha=0.3, which='both')
    plt.savefig('fig3_flow_dominance.png')
    print("Generated fig3_flow_dominance.png")

def plot_reflexivity(df):
    """
    Task 4: Reflexivity Test (Rolling Correlation)
    Empirically demonstrates that LUNA value was tied to UST expansion.
    """
    plt.figure(figsize=(12, 6))
    
    df['dUST'] = df['UST_Supply'].pct_change()
    df['dLUNA_MC'] = df['LUNA_MarketCap'].pct_change()
    
    # 30-day Rolling Correlation
    df['RollingCorr'] = df['dUST'].rolling(window=30).corr(df['dLUNA_MC'])
    
    plt.plot(df['Date'], df['RollingCorr'], label='30-Day Rolling Correlation (UST Supply vs LUNA Mcap)', color='blue')
    plt.axhline(y=0, color='black', linewidth=1)
    plt.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
    
    add_regime_shading(plt)
    
    plt.title('Reflexivity Test: Correlation of Liabilities vs Equity')
    plt.ylabel('Correlation Coefficient')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('fig4_reflexivity.png')
    print("Generated fig4_reflexivity.png")

def plot_reserve_coverage(df_metrics, df_reserves):
    """
    Task 5: Reserve Coverage
    """
    plt.figure(figsize=(12, 6))
    
    # Merge
    merged = pd.merge(df_metrics, df_reserves, on='Date', how='left').fillna(0)
    
    # Warning Check
    if merged['BTC_Balance'].sum() == 0:
        plt.text(0.5, 0.5, "WARNING: LFG RESERVES DATA MISSING\nCoverage assumed 0%", 
                 horizontalalignment='center', verticalalignment='center', 
                 transform=plt.gca().transAxes, fontsize=14, color='red', alpha=0.5)
        print("WARNING: LFG reserves set to zero — coverage plot is illustrative only.")

    merged['Reserve_Value'] = merged['BTC_Balance'] * merged['BTC_Price']
    merged['Coverage_Ratio'] = merged['Reserve_Value'] / merged['UST_Supply']
    
    plt.plot(merged['Date'], merged['Coverage_Ratio'], label='LFG Reserve Coverage', color='green')
    plt.axhline(y=0.20, color='gray', linestyle='--', label='20% Threshold')
    
    add_regime_shading(plt)
    
    plt.title('Reserve Adequacy: Exogenous Backing vs Liabilities')
    plt.ylabel('Coverage Ratio (1.0 = 100%)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('fig5_reserve_coverage.png')
    print("Generated fig5_reserve_coverage.png")

if __name__ == "__main__":
    print("Terra Forensics Tool (Publication Grade)")
    print("---------------------------------------")
    
    try:
        # Load Data
        df = pd.read_csv(METRICS_FILE, parse_dates=['Date'])
        
        # Load Reserves (Mock or Real)
        try:
            df_reserves = pd.read_csv(RESERVES_FILE, parse_dates=['Date'])
        except FileNotFoundError:
            # Create empty frame for template purposes
            df_reserves = pd.DataFrame({'Date': df['Date'], 'BTC_Balance': 0.0, 'BTC_Price': 0.0})
            
        # Execute Pipeline
        plot_absorber_capacity(df)
        plot_cumulative_subsidy(df)
        plot_flow_dominance(df)
        plot_reflexivity(df)
        plot_reserve_coverage(df, df_reserves)
        
        print("\nAll figures generated successfully.")
        
    except FileNotFoundError:
        print(f"CRITICAL ERROR: {METRICS_FILE} not found.")
        print("Please populate this file using the Data Extraction guidelines.")
