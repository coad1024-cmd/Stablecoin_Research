"""
Oracle Latency Attack Visualization

Generates charts showing attack profitability across different scenarios.

Author: Research Challenge Team
Date: January 2026
"""

import matplotlib.pyplot as plt
import numpy as np
from oracle_attack_sim import run_attack_simulation, TerraOracle, TerraMarketModule
import config


def plot_sensitivity_analysis():
    """
    Generate sensitivity analysis chart showing profit vs crash percentage.
    """
    crash_percentages = np.arange(0.01, 0.61, 0.01)  # 1% to 60%
    net_profits = []
    gross_profits = []
    spreads = []
    
    for crash_pct in crash_percentages:
        result = run_attack_simulation(crash_pct)
        net_profits.append(result.net_profit)
        gross_profits.append(result.gross_profit)
        spreads.append(result.spread_paid * 100)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Plot 1: Profit vs Crash
    ax1.axhline(y=0, color='gray', linestyle='--', alpha=0.5, label='Breakeven')
    ax1.plot(crash_percentages * 100, np.array(gross_profits) / 1e6, 
             'b-', linewidth=2, label='Gross Profit')
    ax1.plot(crash_percentages * 100, np.array(net_profits) / 1e6, 
             'r-', linewidth=2, label='Net Profit')
    ax1.fill_between(crash_percentages * 100, 0, np.array(net_profits) / 1e6,
                     where=np.array(net_profits) > 0, alpha=0.3, color='green', 
                     label='Profitable Zone')
    ax1.fill_between(crash_percentages * 100, 0, np.array(net_profits) / 1e6,
                     where=np.array(net_profits) <= 0, alpha=0.3, color='red',
                     label='Unprofitable Zone')
    
    ax1.set_xlabel('LUNA Price Crash (%)', fontsize=12)
    ax1.set_ylabel('Profit ($M)', fontsize=12)
    ax1.set_title('Oracle Latency Attack Profitability vs Price Crash', fontsize=14)
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 60)
    
    # Plot 2: Spread vs Crash (shows Tobin Tax effect)
    ax2.bar(crash_percentages * 100, spreads, width=1, alpha=0.7, color='orange')
    ax2.axhline(y=config.MIN_SPREAD * 100, color='green', linestyle='--', 
                label=f'Min Spread ({config.MIN_SPREAD*100}%)')
    ax2.axhline(y=config.MAX_SPREAD * 100, color='red', linestyle='--',
                label=f'Max Spread ({config.MAX_SPREAD*100}%)')
    
    ax2.set_xlabel('LUNA Price Crash (%)', fontsize=12)
    ax2.set_ylabel('Stability Spread / Tobin Tax (%)', fontsize=12)
    ax2.set_title('Stability Spread Response to Crash Severity', fontsize=14)
    ax2.legend(loc='upper left')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 60)
    
    plt.tight_layout()
    plt.savefig('results/sensitivity_analysis.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[+] Saved: results/sensitivity_analysis.png")


def plot_attack_timeline():
    """
    Visualize the attack timeline showing oracle lag.
    """
    # Simulate a 20% crash
    initial_price = 1.0
    crash_pct = 0.20
    final_price = initial_price * (1 - crash_pct)
    
    # Timeline
    times = np.linspace(0, 45, 100)
    
    # Real price (crashes in first 15 seconds)
    real_prices = []
    for t in times:
        if t < 15:
            # Linear crash
            price = initial_price - (initial_price - final_price) * (t / 15)
        else:
            price = final_price
        real_prices.append(price)
    
    # Oracle price (updates every 30 seconds)
    oracle_prices = []
    last_update_price = initial_price
    for t in times:
        if t >= 30:
            oracle_prices.append(final_price)  # Oracle catches up
        else:
            oracle_prices.append(initial_price)  # Still reporting old price
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(times, real_prices, 'r-', linewidth=2.5, label='Real LUNA Price')
    ax.plot(times, oracle_prices, 'b--', linewidth=2.5, label='Oracle Price (30s Delay)')
    
    # Attack window
    ax.axvspan(15, 30, alpha=0.2, color='yellow', label='Attack Window')
    ax.axvline(x=15, color='orange', linestyle=':', label='Attack Time (Optimal)')
    ax.axvline(x=30, color='green', linestyle=':', label='Oracle Update')
    
    # Annotations
    ax.annotate('Crash Complete\n(Real: $0.80)', xy=(15, 0.80), 
                xytext=(20, 0.70), fontsize=10,
                arrowprops=dict(arrowstyle='->', color='red'))
    ax.annotate('Oracle Still\nReports $1.00', xy=(15, 1.0), 
                xytext=(5, 1.05), fontsize=10,
                arrowprops=dict(arrowstyle='->', color='blue'))
    ax.annotate('Arbitrage\nOpportunity\n(20%)', xy=(22, 0.90), fontsize=11,
                ha='center', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
    
    ax.set_xlabel('Time (seconds)', fontsize=12)
    ax.set_ylabel('LUNA Price ($)', fontsize=12)
    ax.set_title('Oracle Latency Attack Timeline (20% Crash Scenario)', fontsize=14)
    ax.legend(loc='lower left')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 45)
    ax.set_ylim(0.5, 1.15)
    
    plt.tight_layout()
    plt.savefig('results/attack_timeline.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[+] Saved: results/attack_timeline.png")


def plot_capital_sensitivity():
    """
    Show how attack profit scales with capital deployed.
    """
    capitals = np.logspace(5, 9, 50)  # $100K to $1B
    crash_scenarios = [0.10, 0.20, 0.30, 0.50]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for crash_pct in crash_scenarios:
        net_profits = []
        for capital in capitals:
            result = run_attack_simulation(crash_pct, attacker_capital=capital)
            net_profits.append(result.net_profit)
        
        ax.semilogx(capitals / 1e6, np.array(net_profits) / 1e6, 
                    linewidth=2, label=f'{crash_pct:.0%} Crash')
    
    ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('Attacker Capital ($M)', fontsize=12)
    ax.set_ylabel('Net Profit ($M)', fontsize=12)
    ax.set_title('Attack Profit vs Capital Deployed (Different Crash Scenarios)', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('results/capital_sensitivity.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[+] Saved: results/capital_sensitivity.png")


def plot_spread_impact():
    """
    Show how different spread parameters affect attack viability.
    """
    crash_percentages = np.arange(0.05, 0.55, 0.05)
    min_spreads = [0.001, 0.005, 0.01, 0.02, 0.05]  # 0.1% to 5%
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    original_min_spread = config.MIN_SPREAD
    
    for min_spread in min_spreads:
        config.MIN_SPREAD = min_spread
        breakeven_crashes = []
        
        for crash_pct in crash_percentages:
            result = run_attack_simulation(crash_pct)
            breakeven_crashes.append(result.net_profit / 1e6)
        
        ax.plot(crash_percentages * 100, breakeven_crashes, 
                linewidth=2, marker='o', label=f'Min Spread {min_spread*100:.1f}%')
    
    # Reset config
    config.MIN_SPREAD = original_min_spread
    
    ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5, label='Breakeven')
    ax.set_xlabel('LUNA Price Crash (%)', fontsize=12)
    ax.set_ylabel('Net Profit ($M)', fontsize=12)
    ax.set_title('Impact of Tobin Tax (Min Spread) on Attack Profitability', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('results/spread_impact.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[+] Saved: results/spread_impact.png")


def generate_all_charts():
    """Generate all visualization charts."""
    import os
    os.makedirs('results', exist_ok=True)
    
    print("\n[*] Generating Oracle Latency Attack Visualizations...\n")
    
    plot_sensitivity_analysis()
    plot_attack_timeline()
    plot_capital_sensitivity()
    plot_spread_impact()
    
    print("\n[+] All charts saved to results/ folder")


if __name__ == "__main__":
    generate_all_charts()
