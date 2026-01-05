# === Compute MKR Voter Turnout from poll CSV ===
# Paste this into Anti-Gravity IDE and run.
# Input CSV assumed at: analysis/makerdao/governance/data/real_voter_turnout.csv
# Outputs:
#   analysis/makerdao/governance/data/maker_poll_turnout_enriched.csv
#   analysis/makerdao/governance/data/maker_poll_turnout_summary.json
#   (optional) analysis/makerdao/governance/plots/turnout_hist.png  and analysis/makerdao/governance/plots/topdelegate_hist.png

import pandas as pd
import json
import os
import matplotlib.pyplot as plt

INPUT_CSV = "analysis/makerdao/governance/data/real_voter_turnout.csv"
OUTPUT_CSV = "analysis/makerdao/governance/data/maker_poll_turnout_enriched.csv"
SUMMARY_JSON = "analysis/makerdao/governance/data/maker_poll_turnout_summary.json"
PLOTS_DIR = "analysis/makerdao/governance/plots"

# --- SET TOTAL MKR SUPPLY HERE ---
# Updated based on web search (Feb 2025 approx supply)
TOTAL_MKR_SUPPLY = 872290.0

def enrich_data():
    if not os.path.exists(INPUT_CSV):
        print(f"Error: {INPUT_CSV} not found.")
        return

    # Read CSV
    df = pd.read_csv(INPUT_CSV)

    # Ensure numeric
    df['mkr_voted'] = pd.to_numeric(df['mkr_voted'], errors='coerce').fillna(0)
    df['unique_voters'] = pd.to_numeric(df['unique_voters'], errors='coerce').fillna(0)
    df['top_delegate_share_pct'] = pd.to_numeric(df['top_delegate_share_pct'], errors='coerce').fillna(0)

    # Compute turnout percent
    df['turnout_pct'] = df['mkr_voted'] / TOTAL_MKR_SUPPLY * 100

    # Flags & basic checks
    df['anomaly_mkr_gt_supply'] = df['mkr_voted'] > TOTAL_MKR_SUPPLY
    LOW_TURNOUT_THRESHOLD = 1.0  # percent; change if you want
    df['low_turnout'] = df['turnout_pct'] < LOW_TURNOUT_THRESHOLD

    # Summary stats
    summary = {}
    summary['TOTAL_MKR_SUPPLY_used'] = TOTAL_MKR_SUPPLY
    summary['n_polls'] = int(len(df))
    summary['avg_turnout_pct'] = float(df['turnout_pct'].mean())
    summary['median_turnout_pct'] = float(df['turnout_pct'].median())
    summary['max_turnout_pct'] = float(df['turnout_pct'].max())
    summary['min_turnout_pct'] = float(df['turnout_pct'].min())
    summary['pct_polls_below_1pct'] = float((df['turnout_pct'] < 1.0).sum() / len(df) * 100)
    summary['pct_polls_below_5pct'] = float((df['turnout_pct'] < 5.0).sum() / len(df) * 100)
    summary['mean_top_delegate_share_pct'] = float(df['top_delegate_share_pct'].mean())
    summary['median_top_delegate_share_pct'] = float(df['top_delegate_share_pct'].median())
    summary['polls_with_anomalies_count'] = int(df['anomaly_mkr_gt_supply'].sum())
    summary['polls_with_anomalies'] = df.loc[df['anomaly_mkr_gt_supply'], ['poll_id','title','mkr_voted','turnout_pct']].to_dict(orient='records')

    # Save enriched CSV and summary
    # Ensure directory exists
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
    
    df.to_csv(OUTPUT_CSV, index=False)
    with open(SUMMARY_JSON, 'w') as f:
        json.dump(summary, f, indent=2)

    print("Wrote:", OUTPUT_CSV)
    print("Wrote:", SUMMARY_JSON)
    print("Summary (preview):")
    print(json.dumps(summary, indent=2))

    # Optional: simple histograms saved as PNG (uncomment if you want them)
    try:
        if not os.path.exists(PLOTS_DIR):
            os.makedirs(PLOTS_DIR)

        # turnout histogram
        plt.figure(figsize=(6,4))
        plt.hist(df['turnout_pct'].dropna(), bins=30, color='#4ECDC4', edgecolor='black')
        plt.title('Distribution of MKR Turnout % per Poll')
        plt.xlabel('Turnout %')
        plt.ylabel('Number of Polls')
        plt.tight_layout()
        plt.savefig(os.path.join(PLOTS_DIR, 'turnout_hist.png'))
        plt.close()

        # top delegate share histogram
        plt.figure(figsize=(6,4))
        plt.hist(df['top_delegate_share_pct'].dropna(), bins=30, color='#FF6B6B', edgecolor='black')
        plt.title('Distribution of Top Delegate Share % per Poll')
        plt.xlabel('Top Delegate Share %')
        plt.ylabel('Number of Polls')
        plt.tight_layout()
        plt.savefig(os.path.join(PLOTS_DIR, 'topdelegate_hist.png'))
        plt.close()

        print(f"Saved turnout_hist.png and topdelegate_hist.png in {PLOTS_DIR}")
    except Exception as e:
        print("Skipping plots (matplotlib not available?). Error:", e)

if __name__ == "__main__":
    enrich_data()
