"""
MakerDAO/Sky Voter Turnout Analysis (Real Data)

This script analyzes voter turnout using a CSV export of real proposal data.
It calculates:
1. Weighted Turnout % (MKR Voted / Total Supply)
2. Turnout Statistics (Avg, Median, Min, Max)
3. Delegate Dominance (if data available)

Input: analysis/makerdao/governance/data/real_voter_turnout.csv
Output: 
- analysis/makerdao/governance/plots/voter_turnout_real.png
- Console Report
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# Configuration
DATA_DIR = "analysis/makerdao/governance/data"
PLOTS_DIR = "analysis/makerdao/governance/plots"
INPUT_FILE = os.path.join(DATA_DIR, "real_voter_turnout.csv")
RESULTS_FILE = os.path.join(DATA_DIR, "turnout_analysis_real.json")

# Constants
TOTAL_MKR_SUPPLY = 872290  # Updated based on Feb 2025 data

def load_data():
    """Load turnout data from CSV."""
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: Input file not found: {INPUT_FILE}")
        print("Please create this file with columns: poll_id, title, date, mkr_voted, unique_voters, top_delegate_share_pct")
        sys.exit(1)
        
    try:
        df = pd.read_csv(INPUT_FILE)
        # Ensure date is datetime
        df['date'] = pd.to_datetime(df['date'])
        return df
    except Exception as e:
        print(f"❌ Error loading CSV: {e}")
        sys.exit(1)

def analyze_turnout(df):
    """Calculate turnout metrics."""
    print(f"\n📊 Analyzing {len(df)} proposals...")
    
    # Calculate Turnout %
    df['turnout_pct'] = (df['mkr_voted'] / TOTAL_MKR_SUPPLY) * 100
    
    # Statistics
    stats = {
        'avg_turnout': df['turnout_pct'].mean(),
        'median_turnout': df['turnout_pct'].median(),
        'min_turnout': df['turnout_pct'].min(),
        'max_turnout': df['turnout_pct'].max(),
        'avg_unique_voters': df['unique_voters'].mean(),
        'avg_top_delegate_share': df['top_delegate_share_pct'].mean() if 'top_delegate_share_pct' in df.columns else 0
    }
    
    return df, stats

def generate_visualizations(df, stats):
    """Generate turnout charts."""
    if not os.path.exists(PLOTS_DIR):
        os.makedirs(PLOTS_DIR)
        
    # Plot 1: Turnout Over Time
    plt.figure(figsize=(12, 6))
    
    # Sort by date
    df_sorted = df.sort_values('date')
    
    plt.plot(df_sorted['date'], df_sorted['turnout_pct'], marker='o', linestyle='-', linewidth=2, color='#4ECDC4')
    plt.axhline(y=stats['avg_turnout'], color='#FF6B6B', linestyle='--', label=f'Average ({stats["avg_turnout"]:.2f}%)')
    
    plt.title('MakerDAO Governance Voter Turnout (Real Data)', fontsize=14, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Turnout (% of Total MKR Supply)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.xticks(rotation=45)
    
    # Add value labels
    for x, y in zip(df_sorted['date'], df_sorted['turnout_pct']):
        plt.text(x, y + 0.1, f'{y:.1f}%', ha='center', va='bottom', fontsize=9)
        
    plt.tight_layout()
    output_path = os.path.join(PLOTS_DIR, "voter_turnout_real.png")
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"  ✓ Saved plot: {output_path}")

def print_report(df, stats):
    """Print the final report table and save to file."""
    
    report_lines = []
    report_lines.append("# 🗳️  VOTER TURNOUT ANALYSIS REPORT")
    report_lines.append(f"Generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    report_lines.append(f"## 📈 SUMMARY METRICS")
    report_lines.append(f"- **Average Turnout:** {stats['avg_turnout']:.2f}%")
    report_lines.append(f"- **Median Turnout:**  {stats['median_turnout']:.2f}%")
    report_lines.append(f"- **Max Turnout:**     {stats['max_turnout']:.2f}%")
    report_lines.append(f"- **Avg Unique Voters:** {stats['avg_unique_voters']:.0f}")
    if stats['avg_top_delegate_share'] > 0:
        report_lines.append(f"- **Avg Top Delegate Share:** {stats['avg_top_delegate_share']:.1f}%")
        
    report_lines.append(f"\n## 📋 PROPOSAL BREAKDOWN (Top 50 by Date)")
    report_lines.append(f"| Date | ID | MKR Voted | Turnout | Voters | Title |")
    report_lines.append(f"|---|---|---|---|---|---|")
    
    # Filter for rows with actual data (mkr_voted > 0)
    df_real = df[df['mkr_voted'] > 0].sort_values('date', ascending=False)
    
    for _, row in df_real.head(50).iterrows():
        title = row['title'][:50] + "..." if len(row['title']) > 50 else row['title']
        # Escape pipes in title
        title = title.replace("|", "-")
        report_lines.append(f"| {row['date'].strftime('%Y-%m-%d')} | {row['poll_id']} | {row['mkr_voted']:,.0f} | {row['turnout_pct']:.2f}% | {row['unique_voters']} | {title} |")
        
    report_lines.append(f"\n## 🧠 INTERPRETATION")
    if stats['avg_turnout'] < 5:
        report_lines.append("> 🔴 **CRITICAL:** Extremely low turnout (<5%). Governance is highly centralized or apathetic.")
    elif stats['avg_turnout'] < 15:
        report_lines.append("> 🟡 **WARNING:** Low turnout (5-15%). Governance relies heavily on a few active delegates.")
    else:
        report_lines.append("> 🟢 **HEALTHY:** Moderate to high turnout (>15%). Active governance participation.")
        
    if stats['avg_unique_voters'] < 50:
        report_lines.append("\n> 🔴 **CRITICAL:** Very few unique voters (<50). Risk of capture by a small cabal.")

    # Join and print/save
    report_content = "\n".join(report_lines)
    print(report_content)
    
    # Save to file
    reports_dir = "analysis/makerdao/governance/reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
        
    output_path = os.path.join(reports_dir, "voter_turnout_analysis.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report_content)
    print(f"\n✅ Saved report to: {output_path}")

def main():
    df = load_data()
    df, stats = analyze_turnout(df)
    generate_visualizations(df, stats)
    print_report(df, stats)

if __name__ == "__main__":
    main()
