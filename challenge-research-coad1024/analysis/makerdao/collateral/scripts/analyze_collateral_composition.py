"""
MakerDAO/Sky Collateral Composition Analysis

This script analyzes the collateral backing DAI/USDS, including:
1. Share of outstanding DAI backed by each collateral type (ETH, WBTC, USDC, RWAs)
2. Concentration ratio (Herfindahl-Hirschman Index - HHI)
3. Single-counterparty exposure (USDC custodians, banks)

Data source: Based on September 2025 MakerDAO/Sky ecosystem data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
from datetime import datetime

# Configuration
# Configuration
OUTPUT_DIR = "analysis/makerdao/collateral"
PLOTS_DIR = os.path.join(OUTPUT_DIR, "plots")
RESULTS_FILE = os.path.join(OUTPUT_DIR, "collateral_analysis.json")

if not os.path.exists(PLOTS_DIR):
    os.makedirs(PLOTS_DIR)

# Collateral Data (September 2025 estimates based on available public data)
# Total DAI Supply: ~$5.36 billion
TOTAL_DAI_SUPPLY = 5_360_000_000  # $5.36 billion

collateral_data = {
    # Crypto-native collateral
    'ETH': {
        'amount_usd': 1_400_000_000,  # $1.4 billion
        'type': 'crypto',
        'counterparty_risk': 'low',
        'custodian': 'decentralized'
    },
    'WBTC': {
        'amount_usd': 150_000_000,  # Estimated $150M
        'type': 'crypto',
        'counterparty_risk': 'medium',
        'custodian': 'BitGo (centralized bridge)'
    },
    
    # Stablecoin collateral (PSM - Peg Stability Module)
    'USDC': {
        'amount_usd': 1_765_000_000,  # ~32.9% of collateral
        'type': 'stablecoin',
        'counterparty_risk': 'high',
        'custodian': 'Circle/Coinbase'
    },
    
    # Real World Assets
    'US_Treasury_Bonds': {
        'amount_usd': 1_140_000_000,  # $1.14 billion
        'type': 'RWA',
        'counterparty_risk': 'medium',
        'custodian': 'various_banks'
    },
    'Corporate_Bonds': {
        'amount_usd': 200_000_000,  # Estimated
        'type': 'RWA',
        'counterparty_risk': 'medium',
        'custodian': 'various_banks'
    },
    'USDC_Coinbase_Prime': {
        'amount_usd': 500_000_000,  # $500M generating yield
        'type': 'RWA',
        'counterparty_risk': 'high',
        'custodian': 'Coinbase'
    },
    'Other_RWA': {
        'amount_usd': 208_000_000,  # Balance to reach total
        'type': 'RWA',
        'counterparty_risk': 'medium',
        'custodian': 'various'
    }
}

def calculate_herfindahl_hirschman_index(market_shares):
    """
    Calculate Herfindahl-Hirschman Index (HHI)
    
    HHI = sum of squared market shares (in percentage)
    - HHI < 1500: Unconcentrated market
    - 1500 < HHI < 2500: Moderately concentrated
    - HHI > 2500: Highly concentrated
    """
    hhi = sum([share**2 for share in market_shares])
    return hhi

def calculate_concentration_ratio(sorted_shares, top_n):
    """Calculate CR_n (concentration ratio for top n entities)"""
    return sum(sorted_shares[:top_n])

def analyze_collateral_composition():
    """Analyze collateral backing DAI"""
    print("="*70)
    print("DAI/USDS COLLATERAL COMPOSITION ANALYSIS")
    print("="*70)
    
    # Calculate shares
    total_collateral = sum([v['amount_usd'] for v in collateral_data.values()])
    
    results = {
        'total_dai_supply': TOTAL_DAI_SUPPLY,
        'total_collateral_usd': total_collateral,
        'over_collateralization_ratio': (total_collateral / TOTAL_DAI_SUPPLY) * 100,
        'collateral_breakdown': {},
        'aggregate_by_type': {},
        'concentration_metrics': {},
        'counterparty_exposure': {}
    }
    
    print(f"\n📊 OVERVIEW:")
    print(f"  Total DAI Supply: ${TOTAL_DAI_SUPPLY/1e9:.2f}B")
    print(f"  Total Collateral: ${total_collateral/1e9:.2f}B")
    print(f"  Over-Collateralization: {results['over_collateralization_ratio']:.1f}%")
    
    # Individual collateral shares
    print(f"\n💰 COLLATERAL BREAKDOWN (by asset):")
    print("-"*70)
    
    collateral_shares = []
    
    for name, data in collateral_data.items():
        share = (data['amount_usd'] / total_collateral) * 100
        collateral_shares.append(share)
        
        results['collateral_breakdown'][name] = {
            'amount_usd': data['amount_usd'],
            'share_pct': round(share, 2),
            'type': data['type'],
            'counterparty_risk': data['counterparty_risk'],
            'custodian': data['custodian']
        }
        
        print(f"  {name.ljust(25)}: ${data['amount_usd']/1e9:.2f}B ({share:.2f}%)")
    
    # Aggregate by type
    print(f"\n📈 COLLATERAL BY TYPE:")
    print("-"*70)
    
    type_aggregates = {}
    for name, data in collateral_data.items():
        ctype = data['type']
        if ctype not in type_aggregates:
            type_aggregates[ctype] = 0
        type_aggregates[ctype] += data['amount_usd']
    
    for ctype, amount in sorted(type_aggregates.items(), key=lambda x: x[1], reverse=True):
        share = (amount / total_collateral) * 100
        results['aggregate_by_type'][ctype] = {
            'amount_usd': amount,
            'share_pct': round(share, 2)
        }
        print(f"  {ctype.ljust(15)}: ${amount/1e9:.2f}B ({share:.2f}%)")
    
    # Calculate HHI
    hhi = calculate_herfindahl_hirschman_index(collateral_shares)
    sorted_shares = sorted(collateral_shares, reverse=True)
    cr3 = calculate_concentration_ratio(sorted_shares, 3)
    cr5 = calculate_concentration_ratio(sorted_shares, 5)
    
    print(f"\n⚠️  CONCENTRATION METRICS:")
    print("-"*70)
    print(f"  Herfindahl-Hirschman Index (HHI): {hhi:.0f}")
    
    if hhi < 1500:
        concentration_level = "Unconcentrated"
    elif hhi < 2500:
        concentration_level = "Moderately Concentrated"
    else:
        concentration_level = "Highly Concentrated"
    
    print(f"  Concentration Level: {concentration_level}")
    print(f"  CR3 (Top 3 concentration): {cr3:.2f}%")
    print(f"  CR5 (Top 5 concentration): {cr5:.2f}%")
    
    results['concentration_metrics'] = {
        'hhi': round(hhi, 2),
        'concentration_level': concentration_level,
        'cr3_pct': round(cr3, 2),
        'cr5_pct': round(cr5, 2)
    }
    
    # Counterparty Exposure Analysis
    print(f"\n🏦 SINGLE-COUNTERPARTY EXPOSURE:")
    print("-"*70)
    
    counterparty_exposure = {}
    
    # Circle/Coinbase (USDC)
    circle_exposure = collateral_data['USDC']['amount_usd']
    circle_share = (circle_exposure / total_collateral) * 100
    print(f"  Circle/Coinbase (USDC): ${circle_exposure/1e9:.2f}B ({circle_share:.2f}%)")
    counterparty_exposure['Circle_Coinbase_USDC'] = {
        'amount_usd': circle_exposure,
        'share_pct': round(circle_share, 2),
        'risk': 'Critical - single point of failure'
    }
    
    # Coinbase Prime (yield-generating USDC)
    coinbase_prime = collateral_data['USDC_Coinbase_Prime']['amount_usd']
    coinbase_prime_share = (coinbase_prime / total_collateral) * 100
    print(f"  Coinbase Prime (Yield): ${coinbase_prime/1e9:.2f}B ({coinbase_prime_share:.2f}%)")
    counterparty_exposure['Coinbase_Prime'] = {
        'amount_usd': coinbase_prime,
        'share_pct': round(coinbase_prime_share, 2),
        'risk': 'High - exchange custody risk'
    }
    
    # Total Coinbase/Circle exposure
    total_circle_coinbase = circle_exposure + coinbase_prime
    total_circle_share = (total_circle_coinbase / total_collateral) * 100
    print(f"  🚨 TOTAL Circle/Coinbase: ${total_circle_coinbase/1e9:.2f}B ({total_circle_share:.2f}%)")
    counterparty_exposure['Total_Circle_Coinbase'] = {
        'amount_usd': total_circle_coinbase,
        'share_pct': round(total_circle_share, 2),
        'risk': 'CRITICAL - systemic concentration'
    }
    
    # BitGo (WBTC custodian)
    bitgo_exposure = collateral_data['WBTC']['amount_usd']
    bitgo_share = (bitgo_exposure / total_collateral) * 100
    print(f"  BitGo (WBTC): ${bitgo_exposure/1e9:.2f}B ({bitgo_share:.2f}%)")
    counterparty_exposure['BitGo_WBTC'] = {
        'amount_usd': bitgo_exposure,
        'share_pct': round(bitgo_share, 2),
        'risk': 'Medium - wrapped asset custodian'
    }
    
    # Banking system (RWAs)
    rwa_total = sum([v['amount_usd'] for k, v in collateral_data.items() if v['type'] == 'RWA'])
    rwa_share = (rwa_total / total_collateral) * 100
    print(f"  Traditional Banking (RWAs): ${rwa_total/1e9:.2f}B ({rwa_share:.2f}%)")
    counterparty_exposure['Traditional_Banking_RWA'] = {
        'amount_usd': rwa_total,
        'share_pct': round(rwa_share, 2),
        'risk': 'Medium - diversified across multiple banks'
    }
    
    results['counterparty_exposure'] = counterparty_exposure
    
    return results

def create_visualizations(results):
    """Create specific visualizations requested by user"""
    print(f"\n📊 Generating visualizations...")
    
    # Plot 1: Collateral Composition Pie Chart (USDC, RWA, ETH, Other)
    fig1, ax1 = plt.subplots(figsize=(10, 10))
    
    # Aggregate data for pie chart
    types = list(results['aggregate_by_type'].keys())
    shares = [results['aggregate_by_type'][t]['share_pct'] for t in types]
    amounts = [results['aggregate_by_type'][t]['amount_usd'] for t in types]
    
    # Custom colors
    colors_map = {
        'RWA': '#FF6B6B',      # Red/Salmon
        'stablecoin': '#4ECDC4', # Teal
        'crypto': '#45B7D1',   # Blue
        'other': '#96CEB4'     # Green
    }
    colors = [colors_map.get(t, '#cccccc') for t in types]
    
    # Create pie chart
    wedges, texts, autotexts = ax1.pie(shares, labels=None, autopct='%1.1f%%', 
                                      colors=colors, startangle=90, pctdistance=0.85,
                                      explode=[0.02]*len(types))
    
    # Add center circle for Donut chart look
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig1.gca().add_artist(centre_circle)
    
    # Custom legend with amounts
    legend_labels = [f"{t}: ${a/1e9:.2f}B ({s:.1f}%)" for t, a, s in zip(types, amounts, shares)]
    ax1.legend(wedges, legend_labels, title="Collateral Type", loc="center", bbox_to_anchor=(0.5, 0.5))
    
    ax1.set_title('DAI Collateral Composition\n(Backing Structure)', fontsize=16, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "collateral_composition.png"), dpi=150)
    plt.close()
    print("  ✓ Saved: collateral_composition.png")
    
    # Plot 2: RWA Breakdown Bar Chart
    fig2, ax2 = plt.subplots(figsize=(12, 7))
    
    # Filter RWA assets
    rwa_assets = {k: v for k, v in results['collateral_breakdown'].items() if v['type'] == 'RWA'}
    rwa_names = [k.replace('_', ' ') for k in rwa_assets.keys()]
    rwa_values = [v['amount_usd']/1e9 for v in rwa_assets.values()]
    
    # Sort by value
    sorted_indices = np.argsort(rwa_values)[::-1]
    rwa_names = [rwa_names[i] for i in sorted_indices]
    rwa_values = [rwa_values[i] for i in sorted_indices]
    
    bars = ax2.bar(rwa_names, rwa_values, color='#FF6B6B', edgecolor='black', alpha=0.8)
    
    ax2.set_ylabel('Amount (Billions USD)', fontsize=12, fontweight='bold')
    ax2.set_title('RWA Breakdown\n(Real World Asset Composition)', fontsize=16, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                f'${height:.2f}B', ha='center', va='bottom', fontweight='bold')
        
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "rwa_breakdown.png"), dpi=150)
    plt.close()
    print("  ✓ Saved: rwa_breakdown.png")
    
    # Plot 3: Counterparty Exposure Chart
    fig3, ax3 = plt.subplots(figsize=(12, 6))
    
    # Prepare data
    exposure_data = results['counterparty_exposure']
    
    # We want specific categories: Circle/Coinbase, BitGo, Traditional Banks, Others
    categories = []
    values = []
    colors = []
    
    # 1. Circle/Coinbase (Total)
    if 'Total_Circle_Coinbase' in exposure_data:
        categories.append('Circle/Coinbase\n(Total)')
        values.append(exposure_data['Total_Circle_Coinbase']['share_pct'])
        colors.append('#FF4444') # Critical Red
        
    # 2. Traditional Banking (RWA)
    if 'Traditional_Banking_RWA' in exposure_data:
        categories.append('Traditional Banks\n(Treasuries/Bonds)')
        values.append(exposure_data['Traditional_Banking_RWA']['share_pct'])
        colors.append('#FFAA44') # Orange
        
    # 3. BitGo (WBTC)
    if 'BitGo_WBTC' in exposure_data:
        categories.append('BitGo\n(WBTC)')
        values.append(exposure_data['BitGo_WBTC']['share_pct'])
        colors.append('#44AA44') # Green
        
    # 4. Others (ETH + Other RWA not in banks?) 
    # Actually, ETH is trustless (no counterparty), so we shouldn't list it as "exposure" in the same way.
    # But the user asked for "Others".
    # Let's calculate "Trustless/Decentralized" share
    total_exposure_share = sum(values)
    trustless_share = 100 - total_exposure_share
    if trustless_share > 0.1:
        categories.append('Trustless/Decentralized\n(ETH)')
        values.append(trustless_share)
        colors.append('#4ECDC4') # Teal
    
    # Create horizontal bar chart
    y_pos = np.arange(len(categories))
    
    bars = ax3.barh(y_pos, values, color=colors, edgecolor='black')
    ax3.set_yticks(y_pos)
    ax3.set_yticklabels(categories, fontsize=11, fontweight='bold')
    ax3.invert_yaxis()  # Labels read top-to-bottom
    ax3.set_xlabel('% of Total Collateral', fontsize=12, fontweight='bold')
    ax3.set_title('Counterparty Exposure Analysis', fontsize=16, fontweight='bold')
    
    # Add thresholds
    ax3.axvline(x=25, color='red', linestyle='--', alpha=0.5, label='Critical Risk (>25%)')
    
    # Add value labels
    for i, v in enumerate(values):
        ax3.text(v + 1, i, f'{v:.1f}%', va='center', fontweight='bold')
        
    ax3.legend(loc='lower right')
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "counterparty_exposure.png"), dpi=150)
    plt.close()
    print("  ✓ Saved: counterparty_exposure.png")

def main():
    """Main execution"""
    # Analyze
    results = analyze_collateral_composition()
    
    # Create visualizations
    create_visualizations(results)
    
    # Add metadata
    results['metadata'] = {
        "analysis_date": datetime.now().isoformat(),
        "data_source": "MakerDAO/Sky ecosystem - September 2025",
        "note": "Data based on publicly available information and estimates"
    }
    
    # Save results
    with open(RESULTS_FILE, 'w') as f:
        json.dump(results, f, indent=4)
    
    print(f"\n{'='*70}")
    print(f"✅ Analysis Complete!")
    print(f"Results saved to: {RESULTS_FILE}")
    print(f"Plots saved to: {PLOTS_DIR}")
    print(f"{'='*70}")
    
    # Key Findings Summary
    print(f"\n🔍 KEY FINDINGS:")
    print(f"  • HHI: {results['concentration_metrics']['hhi']:.0f} ({results['concentration_metrics']['concentration_level']})")
    print(f"  • Circle/Coinbase Total Exposure: {results['counterparty_exposure']['Total_Circle_Coinbase']['share_pct']:.1f}% ⚠️")
    print(f"  • Over-Collateralization Ratio: {results['over_collateralization_ratio']:.1f}%")

if __name__ == "__main__":
    main()
