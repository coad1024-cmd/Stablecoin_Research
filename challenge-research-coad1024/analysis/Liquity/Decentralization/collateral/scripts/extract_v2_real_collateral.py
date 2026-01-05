import pandas as pd
import json
import os

# Paths
ROOT_DIR = "/home/hash/Projects/Research Challenge/challenge-research-coad1024"
DATA_PATH = os.path.join(ROOT_DIR, "analysis/Liquity/data/trove_snapshot_mainnet.csv")
OUTPUT_PATH = os.path.join(ROOT_DIR, "research/00_canonical/Liquity/02_V2_BOLD/Decentralization/data/collateral_data_v2_real.json")

# ETH Price approximation (Jan 2026)
ETH_PRICE_USD = 3150  # Approximate market price

def main():
    print("Loading V2 Trove Snapshot...")
    df = pd.read_csv(DATA_PATH)
    
    # Group by branch (collateral type)
    branch_stats = df.groupby('branch').agg({
        'coll_ether': 'sum',
        'debt_bold': 'sum'
    }).reset_index()
    
    # Calculate TVL and shares
    branch_stats['tvl_usd'] = branch_stats['coll_ether'] * ETH_PRICE_USD
    total_tvl = branch_stats['tvl_usd'].sum()
    branch_stats['share'] = branch_stats['tvl_usd'] / total_tvl
    
    # Calculate HHI
    hhi = (branch_stats['share'] * 100).pow(2).sum()
    
    # Build composition
    composition = []
    for _, row in branch_stats.iterrows():
        composition.append({
            "asset": row['branch'],
            "type": "LST" if row['branch'] in ['WSTETH', 'RETH'] else "Native Crypto",
            "collateral_amount": float(row['coll_ether']),
            "tvl_usd": float(row['tvl_usd']),
            "share": float(row['share']),
            "share_percent": f"{row['share'] * 100:.2f}%",
            "debt_bold": float(row['debt_bold'])
        })
    
    output = {
        "status": "Real On-Chain Data",
        "source": "analysis/Liquity/data/trove_snapshot_mainnet.csv",
        "timestamp": "2025-12-09T22:57:00Z",  # From CSV
        "note": "Extracted from V2 mainnet trove snapshot. Only 3 active branches (ETH, WSTETH, RETH) as of snapshot date.",
        "total_tvl_usd": float(total_tvl),
        "total_debt_bold": float(branch_stats['debt_bold'].sum()),
        "hhi": float(hhi),
        "composition": composition
    }
    
    # Save
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(output, f, indent=4)
    
    print(f"\n{'='*60}")
    print("✅ REAL V2 Collateral Data Extracted")
    print(f"{'='*60}")
    print(f"Total TVL: ${total_tvl:,.0f}")
    print(f"HHI: {hhi:.2f}")
    print("\nComposition:")
    for item in composition:
        print(f"  {item['asset']:8s}: {item['share_percent']:>7s} (${item['tvl_usd']:>12,.0f})")
    print(f"\nSaved to: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
