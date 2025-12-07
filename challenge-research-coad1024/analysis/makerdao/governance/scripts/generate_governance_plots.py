import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuration
INPUT_CSV = "analysis/makerdao/governance/data/maker_poll_turnout_enriched.csv"
PLOTS_DIR = "analysis/makerdao/governance/plots"

def generate_plots():
    if not os.path.exists(INPUT_CSV):
        print(f"Error: {INPUT_CSV} not found.")
        return

    # Load Data
    df = pd.read_csv(INPUT_CSV)
    
    # Ensure directory exists
    if not os.path.exists(PLOTS_DIR):
        os.makedirs(PLOTS_DIR)

    # Set style
    sns.set_style("whitegrid")
    plt.rcParams.update({'font.size': 12})

    # 1. Turnout Distribution Histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(df['turnout_pct'], bins=20, kde=True, color='#4ECDC4', edgecolor='black')
    plt.title('Distribution of MKR Voter Turnout (%)', fontsize=16, fontweight='bold')
    plt.xlabel('Turnout (% of Total Supply)', fontsize=14)
    plt.ylabel('Frequency (Number of Polls)', fontsize=14)
    plt.axvline(df['turnout_pct'].median(), color='#FF6B6B', linestyle='--', label=f'Median: {df["turnout_pct"].median():.2f}%')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, 'turnout_distribution.png'), dpi=150)
    plt.close()
    print("Generated: turnout_distribution.png")

    # 2. Top Delegate Share Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['top_delegate_share_pct'], bins=20, kde=True, color='#FF6B6B', edgecolor='black')
    plt.title('Distribution of Top Delegate Dominance', fontsize=16, fontweight='bold')
    plt.xlabel('Top Delegate Share (% of Vote)', fontsize=14)
    plt.ylabel('Frequency (Number of Polls)', fontsize=14)
    plt.axvline(df['top_delegate_share_pct'].median(), color='#4ECDC4', linestyle='--', label=f'Median: {df["top_delegate_share_pct"].median():.2f}%')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, 'delegate_dominance_distribution.png'), dpi=150)
    plt.close()
    print("Generated: delegate_dominance_distribution.png")

    # 3. Scatter Plot: MKR Voted vs Unique Voters
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='unique_voters', y='mkr_voted', alpha=0.7, s=100, color='#845EC2')
    plt.title('MKR Voted vs. Unique Voters', fontsize=16, fontweight='bold')
    plt.xlabel('Unique Voters (Count)', fontsize=14)
    plt.ylabel('Total MKR Voted', fontsize=14)
    
    # Add trend line
    sns.regplot(data=df, x='unique_voters', y='mkr_voted', scatter=False, color='gray', line_kws={'linestyle':'--'})
    
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, 'turnout_vs_voters_scatter.png'), dpi=150)
    plt.close()
    print("Generated: turnout_vs_voters_scatter.png")

if __name__ == "__main__":
    generate_plots()
