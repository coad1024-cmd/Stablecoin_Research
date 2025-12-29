# analyze_keepers.py
import pandas as pd
import os
from collections import Counter

def analyze():
    # Resolve paths relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, "../data")
    
    possible_paths = [
        os.path.join(data_dir, "maker_liquidators_raw.csv"),
        "maker_liquidators_raw.csv",
    ]
    
    df = None
    for p in possible_paths:
        if os.path.exists(p):
            df = pd.read_csv(p)
            print(f"Loaded data from {p}")
            break
            
    if df is None:
        print("Error: Could not find maker_liquidators_raw.csv")
        return

    # normalize actor column name
    if 'actor' not in df.columns:
        # try fallback keys
        if 'liquidator_address' in df.columns:
            df['actor'] = df['liquidator_address']
        elif 'taker' in df.columns:
            df['actor'] = df['taker']
        else:
            print("Error: No actor column found. Inspect CSV.")
            return

    # Analyze All Attempts (User's request)
    print(f"Total rows: {len(df)}")
    
    def calc_metrics(dataframe, label):
        counts = dataframe['actor'].value_counts()
        total = counts.sum()
        if total == 0:
            return {}, counts
            
        shares = (counts / total * 100)
        hhi = ((shares/100)**2).sum() * 10000
        
        return {
            f"{label}_total": int(total),
            f"{label}_unique": int(len(counts)),
            f"{label}_top1_share": float(shares.iloc[0]) if len(shares)>0 else 0,
            f"{label}_top3_share": float(shares.head(3).sum()),
            f"{label}_top5_share": float(shares.head(5).sum()),
            f"{label}_hhi": float(hhi),
            f"{label}_top_actor": counts.index[0] if len(counts)>0 else None
        }, counts

    metrics_all, counts_all = calc_metrics(df, "all")
    
    # Analyze Success Only
    if 'status' in df.columns:
        df_success = df[df['status'] == 'Success']
    else:
        df_success = df
        
    metrics_success, counts_success = calc_metrics(df_success, "success")
    
    out = {**metrics_all, **metrics_success}

    print("Analysis Results:")
    print(out)
    
    # Save summary (Using All Attempts as per user preference for 100 events)
    out_csv = os.path.join(data_dir, "maker_liquidators_summary.csv")
    os.makedirs(os.path.dirname(out_csv), exist_ok=True)
    
    if not counts_all.empty:
        pd.DataFrame({
            "actor": counts_all.index,
            "n_liquidations": counts_all.values,
            "pct": (counts_all/metrics_all['all_total']*100).values
        }).to_csv(out_csv, index=False)

    print(f"Wrote {out_csv}")

if __name__ == "__main__":
    analyze()
