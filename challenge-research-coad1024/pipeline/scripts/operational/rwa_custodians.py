# rwa_custodians.py
import json
import pandas as pd
import os

def process_custodians():
    # Resolve paths relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Target: analysis/makerdao/collateral/data/collateral_snapshot.json
    # Script: analysis/makerdao/operational/scripts/
    # Relative: ../../collateral/data/
    json_path = os.path.join(script_dir, "../../collateral/data/collateral_snapshot.json")
    
    if not os.path.exists(json_path):
        print(f"Error: Could not find collateral_snapshot.json at {json_path}")
        # Try finding it in the project root or other locations if needed
        return

    try:
        with open(json_path, 'r') as f:
            j = json.load(f)
            
        rows = []
        # Check structure - assuming 'collateral_breakdown' key exists based on instructions
        data_source = j.get('collateral_breakdown', {})
        if not data_source:
             # Fallback if structure is different (e.g. list or direct dict)
             data_source = j if isinstance(j, dict) else {}
             
        for k, v in data_source.items():
            if isinstance(v, dict):
                rows.append({
                    "asset": k,
                    "amount_usd": v.get("amount_usd"),
                    "share_pct": v.get("share_pct"),
                    "custodian": v.get("custodian"),
                    "type": v.get("type"),
                })
        
        if rows:
            out_csv = os.path.join(script_dir, "../data/rwa_custodians.csv")
            os.makedirs(os.path.dirname(out_csv), exist_ok=True)
            pd.DataFrame(rows).to_csv(out_csv, index=False)
            print(f"Saved {out_csv}")
        else:
            print("No rows extracted. Check JSON structure.")
            
    except Exception as e:
        print(f"Error processing JSON: {e}")

if __name__ == "__main__":
    process_custodians()
