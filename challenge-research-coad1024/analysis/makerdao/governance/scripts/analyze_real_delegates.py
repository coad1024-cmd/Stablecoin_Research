"""
Comprehensive MakerDAO Delegation Analysis from Real Data

This script analyzes real delegate data to compute:
- Total delegated MKR
- Delegated MKR per delegate address
- Top-1, Top-5, Top-10 delegates (by voting power)
- Delegation concentration (Gini coefficient)
- Effective delegate control thresholds
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

# Configuration
# Configuration
DATA_FILE = "analysis/makerdao/governance/data/delegates_with_delegators.json"
OUTPUT_DIR = "analysis/makerdao/governance"
PLOTS_DIR = os.path.join(OUTPUT_DIR, "plots")
RESULTS_FILE = os.path.join(OUTPUT_DIR, "delegation_analysis_real.json")

if not os.path.exists(PLOTS_DIR):
    os.makedirs(PLOTS_DIR)

def calculate_gini(values):
    """Calculate Gini coefficient for concentration analysis."""
    sorted_values = np.sort(values)
    n = len(values)
    if n == 0 or sorted_values.sum() == 0:
        return 0
    cum_values = np.cumsum(sorted_values)
    return (n + 1 - 2 * np.sum(cum_values) / cum_values[-1]) / n

def load_delegate_data(filepath):
    """Load and parse delegate data from JSON file."""
    print(f"Loading delegate data from: {filepath}")
    with open(filepath, 'r') as f:
        data = json.load(f)
    print(f"Loaded data for {len(data)} delegates")
    return data

def calculate_delegate_totals(delegate_data):
    """Calculate total delegated MKR for each delegate."""
    delegate_totals = {}
    
    for delegate_address, delegators in delegate_data.items():
        total_mkr = 0
        for delegator in delegators:
            deposits = delegator.get('deposits', '0')
            try:
                # Convert to float, handling string format
                total_mkr += float(deposits)
            except (ValueError, TypeError):
                continue
        
        delegate_totals[delegate_address] = total_mkr
    
    return delegate_totals

def analyze_delegation(delegate_totals):
    """Comprehensive delegation analysis."""
    print("\n" + "="*70)
    print("DELEGATION ANALYSIS - REAL DATA")
    print("="*70)
    
    # Create DataFrame sorted by delegated MKR
    df = pd.DataFrame(list(delegate_totals.items()), 
                      columns=['Delegate', 'Delegated_MKR'])
    df = df.sort_values('Delegated_MKR', ascending=False).reset_index(drop=True)
    
    # Filter out delegates with 0 or minimal delegation
    df_active = df[df['Delegated_MKR'] > 0.001].copy()
    
    total_delegated = df['Delegated_MKR'].sum()
    total_active_delegates = len(df_active)
    
    print(f"\n📊 OVERVIEW:")
    print(f"  Total Delegated MKR: {total_delegated:,.2f}")
    print(f"  Total Delegates: {len(df)} ({total_active_delegates} active)")
    print(f"  Mean Delegation: {df_active['Delegated_MKR'].mean():,.2f} MKR")
    print(f"  Median Delegation: {df_active['Delegated_MKR'].median():,.2f} MKR")
    
    # Calculate shares
    df_active['Share_%'] = (df_active['Delegated_MKR'] / total_delegated) * 100
    df_active['Cumulative_%'] = df_active['Share_%'].cumsum()
    
    # Top delegates
    print(f"\n🏆 TOP DELEGATES:")
    top_1_mkr = df_active.iloc[0]['Delegated_MKR'] if len(df_active) >= 1 else 0
    top_5_mkr = df_active.head(5)['Delegated_MKR'].sum()
    top_10_mkr = df_active.head(10)['Delegated_MKR'].sum()
    
    top_1_share = (top_1_mkr / total_delegated) * 100 if total_delegated > 0 else 0
    top_5_share = (top_5_mkr / total_delegated) * 100 if total_delegated > 0 else 0
    top_10_share = (top_10_mkr / total_delegated) * 100 if total_delegated > 0 else 0
    
    print(f"  Top 1:  {top_1_mkr:,.2f} MKR ({top_1_share:.2f}%)")
    print(f"  Top 5:  {top_5_mkr:,.2f} MKR ({top_5_share:.2f}%)")
    print(f"  Top 10: {top_10_mkr:,.2f} MKR ({top_10_share:.2f}%)")
    
    # Gini coefficient
    gini = calculate_gini(df_active['Delegated_MKR'].values)
    print(f"\n📈 CONCENTRATION:")
    print(f"  Delegation Gini: {gini:.4f}")
    
    # Effective control thresholds
    print(f"\n⚖️  EFFECTIVE CONTROL THRESHOLDS:")
    
    # Find how many delegates needed for different thresholds
    thresholds = {
        "33% (Blocking Minority)": 33,
        "51% (Simple Majority)": 51,
        "67% (Supermajority)": 67
    }
    
    control_analysis = {}
    for name, threshold in thresholds.items():
        delegates_needed = (df_active['Cumulative_%'] >= threshold).idxmax() + 1
        mkr_at_threshold = df_active[df_active['Cumulative_%'] >= threshold].iloc[0]['Cumulative_%']
        control_analysis[name] = {
            "threshold_pct": threshold,
            "delegates_needed": int(delegates_needed),
            "actual_pct": float(mkr_at_threshold)
        }
        print(f"  {name}: {delegates_needed} delegate(s) ({mkr_at_threshold:.2f}%)")
    
    # Top 10 detailed list
    print(f"\n📋 TOP 10 DELEGATES (Detailed):")
    print("-" * 70)
    for idx, row in df_active.head(10).iterrows():
        print(f"  #{idx+1}: {row['Delegate'][:10]}...{row['Delegate'][-6:]}")
        print(f"       {row['Delegated_MKR']:,.4f} MKR ({row['Share_%']:.2f}%)")
    
    results = {
        "total_delegated_mkr": float(total_delegated),
        "total_delegates": len(df),
        "active_delegates": total_active_delegates,
        "mean_delegation_mkr": float(df_active['Delegated_MKR'].mean()),
        "median_delegation_mkr": float(df_active['Delegated_MKR'].median()),
        "top_delegate_shares": {
            "top_1_mkr": float(top_1_mkr),
            "top_1_share_pct": float(top_1_share),
            "top_5_mkr": float(top_5_mkr),
            "top_5_share_pct": float(top_5_share),
            "top_10_mkr": float(top_10_mkr),
            "top_10_share_pct": float(top_10_share)
        },
        "concentration": {
            "gini_coefficient": float(gini)
        },
        "effective_control": control_analysis,
        "top_10_delegates": []
    }
    
    # Add top 10 to results
    for idx, row in df_active.head(10).iterrows():
        results["top_10_delegates"].append({
            "rank": idx + 1,
            "address": row['Delegate'],
            "delegated_mkr": float(row['Delegated_MKR']),
            "share_pct": float(row['Share_%'])
        })
    
    return results, df_active

def create_visualizations(df_active, results):
    """Create comprehensive visualizations."""
    print("\n📊 Generating Visualizations...")
    
    # Plot 1: Top 15 Delegates Bar Chart
    fig, ax = plt.subplots(figsize=(14, 7))
    top_15 = df_active.head(15).copy()
    top_15['Label'] = [f"#{i+1}" for i in range(len(top_15))]
    
    bars = ax.barh(top_15['Label'][::-1], top_15['Delegated_MKR'][::-1], 
                   color=sns.color_palette("viridis", len(top_15))[::-1])
    
    ax.set_xlabel('Delegated MKR', fontsize=12, fontweight='bold')
    ax.set_title('Top 15 MakerDAO Delegates by Voting Power (Real Data)', 
                 fontsize=14, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)
    
    # Add value labels
    for i, (idx, row) in enumerate(top_15[::-1].iterrows()):
        ax.text(row['Delegated_MKR'], i, f" {row['Delegated_MKR']:.1f} ({row['Share_%']:.1f}%)", 
                va='center', fontsize=9)
    
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "delegation_top15_real.png"), dpi=150)
    plt.close()
    print("  ✓ Saved: delegation_top15_real.png")
    
    # Plot 2: Concentration Analysis
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Cumulative distribution
    top_50 = df_active.head(50)
    ax1.plot(range(1, len(top_50)+1), top_50['Cumulative_%'], 
             marker='o', linewidth=2, markersize=4)
    ax1.axhline(y=33, color='orange', linestyle='--', label='33% (Blocking)', alpha=0.7)
    ax1.axhline(y=51, color='red', linestyle='--', label='51% (Majority)', alpha=0.7)
    ax1.axhline(y=67, color='darkred', linestyle='--', label='67% (Supermajority)', alpha=0.7)
    ax1.set_xlabel('Number of Delegates', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Cumulative % of Delegated MKR', fontsize=11, fontweight='bold')
    ax1.set_title('Delegate Power Concentration', fontsize=13, fontweight='bold')
    ax1.legend()
    ax1.grid(alpha=0.3)
    
    # Pie chart: Top 5 vs Others
    top_5_total = results['top_delegate_shares']['top_5_mkr']
    others = results['total_delegated_mkr'] - top_5_total
    
    sizes = [top_5_total, others]
    labels = [f'Top 5 Delegates\n({results["top_delegate_shares"]["top_5_share_pct"]:.1f}%)',
              f'All Others\n({100 - results["top_delegate_shares"]["top_5_share_pct"]:.1f}%)']
    colors = ['#FF6B6B', '#4ECDC4']
    explode = (0.05, 0)
    
    ax2.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', 
            startangle=90, explode=explode, textprops={'fontsize': 11, 'fontweight': 'bold'})
    ax2.set_title(f'Delegation Distribution\n(Gini: {results["concentration"]["gini_coefficient"]:.4f})', 
                  fontsize=13, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "delegation_concentration_real.png"), dpi=150)
    plt.close()
    print("  ✓ Saved: delegation_concentration_real.png")
    
    # Plot 3: Lorenz Curve for Delegation
    fig, ax = plt.subplots(figsize=(10, 8))
    
    sorted_mkr = np.sort(df_active['Delegated_MKR'].values)
    cum_delegates = np.arange(1, len(sorted_mkr) + 1) / len(sorted_mkr) * 100
    cum_mkr = np.cumsum(sorted_mkr) / sorted_mkr.sum() * 100
    
    ax.plot(cum_delegates, cum_mkr, linewidth=2.5, label=f'Lorenz Curve (Gini={results["concentration"]["gini_coefficient"]:.4f})')
    ax.plot([0, 100], [0, 100], 'k--', linewidth=1.5, label='Perfect Equality', alpha=0.5)
    ax.fill_between(cum_delegates, cum_mkr, cum_delegates, alpha=0.3, color='red', label='Inequality Area')
    
    ax.set_xlabel('Cumulative % of Delegates', fontsize=12, fontweight='bold')
    ax.set_ylabel('Cumulative % of Delegated MKR', fontsize=12, fontweight='bold')
    ax.set_title('Delegation Lorenz Curve (Real Data)', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(alpha=0.3)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "delegation_lorenz_real.png"), dpi=150)
    plt.close()
    print("  ✓ Saved: delegation_lorenz_real.png")

def main():
    """Main execution function."""
    print("="*70)
    print("  MakerDAO Delegation Analysis - Real On-Chain Data")
    print("="*70)
    
    # Load data
    delegate_data = load_delegate_data(DATA_FILE)
    
    # Calculate totals
    print("\nCalculating delegation totals per delegate...")
    delegate_totals = calculate_delegate_totals(delegate_data)
    
    # Analyze
    results, df_active = analyze_delegation(delegate_totals)
    
    # Create visualizations
    create_visualizations(df_active, results)
    
    # Add metadata
    results['metadata'] = {
        "analysis_date": datetime.now().isoformat(),
        "data_source": "Real MakerDAO delegate data from governance API",
        "data_file": DATA_FILE
    }
    
    # Save results
    with open(RESULTS_FILE, 'w') as f:
        json.dump(results, f, indent=4)
    
    print(f"\n{'='*70}")
    print(f"✅ Analysis Complete!")
    print(f"Results saved to: {RESULTS_FILE}")
    print(f"Visualizations saved to: {PLOTS_DIR}")
    print(f"{'='*70}")

if __name__ == "__main__":
    main()
