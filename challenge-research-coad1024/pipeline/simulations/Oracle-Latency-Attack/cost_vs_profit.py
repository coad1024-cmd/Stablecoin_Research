"""
Cost vs Profitability Analysis for Oracle Latency Attack

Calculates:
- Attack Costs: Capital, gas, slippage, opportunity cost
- Expected Profits: Gross and net
- Break-even Analysis: Minimum crash for profitability
- ROI Metrics: Return on capital, Sharpe-like ratio

Based on: research/04_modelling/attack_vs_profitability.md

Author: Research Challenge Team
Date: January 2026
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Tuple
import config
from oracle_attack_sim import run_attack_simulation


@dataclass
class AttackCosts:
    """Breakdown of all attack costs."""
    capital_deployed: float     # UST spent on attack
    gas_cost: float             # Blockchain transaction fees
    slippage_cost: float        # Price impact / slippage
    spread_cost: float          # Tobin Tax (Stability Spread)
    opportunity_cost: float     # Alternative yield on capital
    total_cost: float           # Sum of all costs
    

@dataclass
class AttackProfitability:
    """Complete cost vs profit analysis."""
    scenario_name: str
    crash_percentage: float
    
    # Costs
    costs: AttackCosts
    
    # Revenue
    gross_revenue: float        # LUNA sold at market price
    
    # Profit
    gross_profit: float         # Revenue - Capital
    net_profit: float           # Gross - All Costs
    
    # Metrics
    roi: float                  # Net Profit / Capital Deployed
    profit_margin: float        # Net Profit / Gross Revenue
    cost_efficiency: float      # Total Cost / Gross Revenue
    break_even_crash: float     # Minimum crash for profitability
    
    # Risk-adjusted
    risk_reward_ratio: float    # Expected Profit / Max Loss


def calculate_opportunity_cost(
    capital: float,
    duration_hours: float = 1.0,
    annual_yield: float = 0.20  # 20% APY (Anchor-like yield)
) -> float:
    """
    Calculate opportunity cost of locking capital for attack.
    
    Assumes capital could have earned yield elsewhere (e.g., Anchor Protocol).
    """
    hourly_rate = annual_yield / (365 * 24)
    return capital * hourly_rate * duration_hours


def calculate_attack_costs(
    capital: float,
    spread_rate: float,
    slippage_rate: float = config.SLIPPAGE_TOLERANCE,
    gas_usd: float = config.GAS_COST_USD,
    attack_duration_hours: float = 1.0
) -> AttackCosts:
    """
    Calculate all costs associated with the attack.
    """
    # Direct costs
    spread_cost = capital * spread_rate
    slippage_cost = capital * slippage_rate
    gas_cost = gas_usd * 2  # Swap + Sell transactions
    
    # Opportunity cost
    opportunity_cost = calculate_opportunity_cost(capital, attack_duration_hours)
    
    total_cost = spread_cost + slippage_cost + gas_cost + opportunity_cost
    
    return AttackCosts(
        capital_deployed=capital,
        gas_cost=gas_cost,
        slippage_cost=slippage_cost,
        spread_cost=spread_cost,
        opportunity_cost=opportunity_cost,
        total_cost=total_cost
    )


def find_break_even_crash(
    capital: float = config.ATTACKER_CAPITAL,
    precision: float = 0.001
) -> float:
    """
    Binary search to find minimum crash percentage for profitable attack.
    """
    low, high = 0.0, 1.0
    
    while high - low > precision:
        mid = (low + high) / 2
        result = run_attack_simulation(mid, attacker_capital=capital)
        
        if result.net_profit > 0:
            high = mid
        else:
            low = mid
    
    return high


def analyze_attack_profitability(
    crash_percentage: float,
    capital: float = config.ATTACKER_CAPITAL,
    scenario_name: str = "Default"
) -> AttackProfitability:
    """
    Complete cost vs profitability analysis for a single scenario.
    """
    # Run base simulation
    result = run_attack_simulation(crash_percentage, attacker_capital=capital)
    
    # Calculate detailed costs
    costs = calculate_attack_costs(
        capital=capital,
        spread_rate=result.spread_paid
    )
    
    # Revenue = LUNA sold at real market price
    gross_revenue = result.luna_sold_value
    
    # Profits
    gross_profit = gross_revenue - capital
    net_profit = result.net_profit
    
    # Metrics
    roi = net_profit / capital if capital > 0 else 0
    profit_margin = net_profit / gross_revenue if gross_revenue > 0 else 0
    cost_efficiency = costs.total_cost / gross_revenue if gross_revenue > 0 else float('inf')
    
    # Risk metrics
    max_loss = capital  # Worst case: lose everything
    risk_reward = net_profit / max_loss if max_loss > 0 else 0
    
    # Break-even (only calculate once, cache for others)
    break_even = find_break_even_crash(capital)
    
    return AttackProfitability(
        scenario_name=scenario_name,
        crash_percentage=crash_percentage,
        costs=costs,
        gross_revenue=gross_revenue,
        gross_profit=gross_profit,
        net_profit=net_profit,
        roi=roi,
        profit_margin=profit_margin,
        cost_efficiency=cost_efficiency,
        break_even_crash=break_even,
        risk_reward_ratio=risk_reward
    )


def run_cost_benefit_analysis() -> Dict[str, AttackProfitability]:
    """
    Run comprehensive cost vs profitability analysis across scenarios.
    """
    scenarios = {
        "Minor Volatility": 0.05,
        "Moderate Stress": 0.10,
        "Significant Crash": 0.20,
        "Severe Crash": 0.30,
        "Flash Crash": 0.50,
    }
    
    results = {}
    
    print("\n" + "=" * 80)
    print("COST VS PROFITABILITY ANALYSIS - ORACLE LATENCY ATTACK")
    print("=" * 80)
    print(f"Capital Deployed: ${config.ATTACKER_CAPITAL:,.0f}")
    print(f"Min Spread (Tobin Tax): {config.MIN_SPREAD:.2%}")
    print(f"Slippage Tolerance: {config.SLIPPAGE_TOLERANCE:.2%}")
    print("-" * 80)
    
    for name, crash_pct in scenarios.items():
        analysis = analyze_attack_profitability(crash_pct, scenario_name=name)
        results[name] = analysis
    
    # Print summary table
    print(f"\n{'Scenario':<20} | {'Crash':>6} | {'Gross P&L':>12} | {'Costs':>12} | {'Net P&L':>12} | {'ROI':>8}")
    print("-" * 80)
    
    for name, a in results.items():
        print(f"{name:<20} | {a.crash_percentage:>5.0%} | ${a.gross_profit:>10,.0f} | ${a.costs.total_cost:>10,.0f} | ${a.net_profit:>10,.0f} | {a.roi:>7.2%}")
    
    print("-" * 80)
    
    # Print break-even analysis
    break_even = list(results.values())[0].break_even_crash
    print(f"\nBREAK-EVEN ANALYSIS:")
    print(f"  Minimum crash for profitability: {break_even:.1%}")
    print(f"  At break-even, ROI = 0%")
    
    return results


def print_detailed_cost_breakdown(analysis: AttackProfitability):
    """
    Print detailed cost breakdown for a single scenario.
    """
    a = analysis
    c = a.costs
    
    print("\n" + "=" * 60)
    print(f"DETAILED COST BREAKDOWN: {a.scenario_name}")
    print("=" * 60)
    print(f"Crash Scenario: {a.crash_percentage:.0%}")
    print("-" * 60)
    
    print("\nCOSTS:")
    print(f"  Capital Deployed:   ${c.capital_deployed:>15,.2f}")
    print(f"  Spread (Tobin Tax): ${c.spread_cost:>15,.2f}  ({c.spread_cost/c.capital_deployed:.2%})")
    print(f"  Slippage:           ${c.slippage_cost:>15,.2f}  ({c.slippage_cost/c.capital_deployed:.2%})")
    print(f"  Gas Fees:           ${c.gas_cost:>15,.2f}")
    print(f"  Opportunity Cost:   ${c.opportunity_cost:>15,.2f}")
    print(f"  ----------------------------")
    print(f"  TOTAL COSTS:        ${c.total_cost:>15,.2f}  ({c.total_cost/c.capital_deployed:.2%})")
    
    print("\nREVENUE:")
    print(f"  Gross Revenue:      ${a.gross_revenue:>15,.2f}")
    
    print("\nPROFIT:")
    print(f"  Gross Profit:       ${a.gross_profit:>15,.2f}")
    print(f"  Net Profit:         ${a.net_profit:>15,.2f}")
    
    print("\nMETRICS:")
    print(f"  ROI:                {a.roi:>15.2%}")
    print(f"  Profit Margin:      {a.profit_margin:>15.2%}")
    print(f"  Cost Efficiency:    {a.cost_efficiency:>15.2%}")
    print(f"  Risk/Reward:        {a.risk_reward_ratio:>15.4f}")
    
    print("\nVERDICT:", end=" ")
    if a.net_profit > 0:
        print(f"[PROFITABLE] Net gain of ${a.net_profit:,.2f}")
    else:
        print(f"[UNPROFITABLE] Net loss of ${abs(a.net_profit):,.2f}")
    
    print("=" * 60)


def run_sensitivity_to_costs():
    """
    Analyze how changes in cost parameters affect profitability.
    """
    print("\n" + "=" * 80)
    print("SENSITIVITY ANALYSIS: COST PARAMETERS")
    print("=" * 80)
    
    base_crash = 0.20  # 20% crash scenario
    capital = config.ATTACKER_CAPITAL
    
    # Vary spread
    print("\n1. TOBIN TAX (Min Spread) Sensitivity:")
    print(f"   {'Spread':>8} | {'Net P&L':>12} | {'ROI':>8} | {'Status':>12}")
    print("   " + "-" * 50)
    
    spreads = [0.001, 0.005, 0.01, 0.02, 0.05, 0.10]
    original_spread = config.MIN_SPREAD
    
    for spread in spreads:
        config.MIN_SPREAD = spread
        result = run_attack_simulation(base_crash, attacker_capital=capital)
        status = "Profitable" if result.net_profit > 0 else "Loss"
        roi = result.net_profit / capital
        print(f"   {spread:>7.2%} | ${result.net_profit:>10,.0f} | {roi:>7.2%} | {status:>12}")
    
    config.MIN_SPREAD = original_spread
    
    # Vary slippage
    print("\n2. SLIPPAGE Sensitivity:")
    print(f"   {'Slippage':>8} | {'Net P&L':>12} | {'ROI':>8} | {'Status':>12}")
    print("   " + "-" * 50)
    
    slippages = [0.001, 0.005, 0.01, 0.02, 0.05]
    original_slippage = config.SLIPPAGE_TOLERANCE
    
    for slippage in slippages:
        config.SLIPPAGE_TOLERANCE = slippage
        result = run_attack_simulation(base_crash, attacker_capital=capital)
        status = "Profitable" if result.net_profit > 0 else "Loss"
        roi = result.net_profit / capital
        print(f"   {slippage:>7.2%} | ${result.net_profit:>10,.0f} | {roi:>7.2%} | {status:>12}")
    
    config.SLIPPAGE_TOLERANCE = original_slippage
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    # Full cost-benefit analysis
    results = run_cost_benefit_analysis()
    
    # Detailed breakdown for 20% crash
    analysis_20 = analyze_attack_profitability(0.20, scenario_name="20% Crash (Terra Collapse Level)")
    print_detailed_cost_breakdown(analysis_20)
    
    # Cost sensitivity
    run_sensitivity_to_costs()
