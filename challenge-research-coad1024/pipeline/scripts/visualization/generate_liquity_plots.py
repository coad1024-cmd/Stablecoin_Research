import requests
import pandas as pd
import json
import os
import matplotlib.pyplot as plt

# Base paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "..", "data") # analysis/Liquity/data
PLOTS_DIR = os.path.join(SCRIPT_DIR, "..", "plots")
CSV_PATH = os.path.join(DATA_DIR, "trove_snapshot_mainnet.csv")

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def fetch_lst_data():
    """
    Fetches Collateral composition. 
    Prioritizes REAL MAINNET CSV if available.
    Falls back to SIMULATION if missing.
    """
    if os.path.exists(CSV_PATH):
        print(f"✅ Found Real Data at {CSV_PATH}")
        try:
            df = pd.read_csv(CSV_PATH)
            # Group by branch
            # We use 'coll_ether' as the value metric (assuming 1 ETH = 1 unit of value for distribution)
            result = df.groupby('branch')['coll_ether'].sum().reset_index()
            # Rename for compatibility
            result.columns = ['asset', 'tvl'] 
            
            # Add type
            def get_type(asset):
                if "ETH" == asset: return "Crypto"
                return "LST"
            
            result['type'] = result['asset'].apply(get_type)
            return result
        except Exception as e:
            print(f"❌ Error reading CSV: {e}. Reverting to Simulation.")
    
    print("⚠️ Using SIMULATED Data (Real data mismatch or file missing).")
    data = [
        {"asset": "WETH", "tvl": 400_000, "type": "Crypto"},
        {"asset": "wstETH", "tvl": 450_000, "type": "LST"},
        {"asset": "rETH", "tvl": 100_000, "type": "LST"},
        {"asset": "osETH", "tvl": 30_000, "type": "LST"}
    ]
    return pd.DataFrame(data)

def calculate_hhi(df):
    total_tvl = df['tvl'].sum()
    if total_tvl == 0: return 0
    
    df['share'] = df['tvl'] / total_tvl
    df['squared_share'] = df['share'] ** 2
    hhi = df['squared_share'].sum() * 10000
    return hhi

def main():
    print("Starting Collateral Analysis...")
    ensure_dir(PLOTS_DIR)
    
    df = fetch_lst_data()
    print("\nCollateral Composition:")
    print(df)
    
    hhi = calculate_hhi(df)
    print(f"\nHHI Score: {hhi:.2f}")
    
    # 1. Composition Plot
    plt.figure(figsize=(10, 6))
    labels = df['asset']
    sizes = df['tvl']
    # Dynamic colors
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0'][:len(labels)]
    
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title(f"Liquity V2 Collateral Composition ({'REAL' if os.path.exists(CSV_PATH) else 'SIMULATED'})")
    plt.savefig(os.path.join(PLOTS_DIR, "collateral_composition.png"))
    print("Saved collateral_composition.png")
    plt.close()

    # 2. Counterparty Exposure
    # Map assets to Risk Categories
    risk_map = {
        "ETH": "Native (Trustless)",
        "WETH": "Native (Trustless)",
        "wstETH": "Lido (DAO Risk)",
        "rETH": "RocketPool (Node Ads)",
        "osETH": "Stakewise (Vaults)"
    }
    
    df['Category'] = df['asset'].map(risk_map).fillna("Other (Unknown)")
    exposure = df.groupby('Category')['tvl'].sum()
    
    plt.figure(figsize=(10, 6))
    exposure.plot(kind='bar', color=['green', 'orange', 'blue', 'red', 'purple'][:len(exposure)])
    plt.title('Liquity V2 Counterparty Exposure')
    plt.ylabel('TVL (ETH)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "counterparty_exposure.png"))
    print("Saved counterparty_exposure.png")
    plt.close()

    # 3. Collateral Type Breakdown
    type_exposure = df.groupby('type')['tvl'].sum()
    plt.figure(figsize=(8, 8))
    plt.pie(type_exposure, labels=type_exposure.index, autopct='%1.1f%%', colors=['lightgreen', 'salmon'], startangle=90)
    plt.title('Collateral Type Breakdown (Crypto vs LST)')
    plt.savefig(os.path.join(PLOTS_DIR, "collateral_type_breakdown.png"))
    print("Saved collateral_type_breakdown.png")
    plt.close()

if __name__ == "__main__":
    main()
