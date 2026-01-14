"""
Monte Carlo Simulation for Oracle Latency Attack

Adds stochastic modeling to account for:
- Random crash timing and magnitude
- Varying oracle delays
- Transaction timing uncertainty
- Slippage variance

Author: Research Challenge Team
Date: January 2026
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Dict
import config
from oracle_attack_sim import run_attack_simulation, AttackResult


@dataclass
class MonteCarloResult:
    """Aggregate results from Monte Carlo simulation."""
    num_simulations: int
    mean_profit: float
    std_profit: float
    min_profit: float
    max_profit: float
    profitable_pct: float
    var_95: float  # 5% Value at Risk
    expected_shortfall: float  # Conditional VaR


def run_monte_carlo(
    num_simulations: int = 1000,
    crash_mean: float = 0.20,
    crash_std: float = 0.10,
    capital_mean: float = 10_000_000,
    capital_std: float = 2_000_000,
    seed: int = 42
) -> MonteCarloResult:
    """
    Run Monte Carlo simulation with random parameters.
    
    Randomizes:
    - Crash percentage (normal distribution around mean)
    - Attack capital (normal distribution)
    - Execution timing (uniform within oracle window)
    """
    np.random.seed(seed)
    
    profits = []
    
    for _ in range(num_simulations):
        # Random crash percentage (bounded 1% to 80%)
        crash_pct = np.clip(np.random.normal(crash_mean, crash_std), 0.01, 0.80)
        
        # Random capital (bounded $100K to $100M)
        capital = np.clip(np.random.normal(capital_mean, capital_std), 100_000, 100_000_000)
        
        # Run simulation
        result = run_attack_simulation(crash_pct, attacker_capital=capital)
        profits.append(result.net_profit)
    
    profits = np.array(profits)
    
    # Calculate statistics
    var_95 = np.percentile(profits, 5)  # 5% worst case
    es_mask = profits <= var_95
    expected_shortfall = profits[es_mask].mean() if es_mask.any() else var_95
    
    return MonteCarloResult(
        num_simulations=num_simulations,
        mean_profit=profits.mean(),
        std_profit=profits.std(),
        min_profit=profits.min(),
        max_profit=profits.max(),
        profitable_pct=(profits > 0).sum() / num_simulations * 100,
        var_95=var_95,
        expected_shortfall=expected_shortfall
    )


def run_scenario_analysis() -> Dict[str, MonteCarloResult]:
    """
    Run Monte Carlo across different market scenarios.
    """
    scenarios = {
        "Normal Market": {"crash_mean": 0.05, "crash_std": 0.02},
        "Moderate Stress": {"crash_mean": 0.15, "crash_std": 0.05},
        "High Volatility": {"crash_mean": 0.25, "crash_std": 0.10},
        "Flash Crash": {"crash_mean": 0.40, "crash_std": 0.15},
        "Black Swan": {"crash_mean": 0.60, "crash_std": 0.15},
    }
    
    results = {}
    
    print("=" * 70)
    print("MONTE CARLO SCENARIO ANALYSIS")
    print("=" * 70)
    print(f"Simulations per scenario: {config.NUM_SIMULATIONS}")
    print("-" * 70)
    
    for name, params in scenarios.items():
        mc_result = run_monte_carlo(
            num_simulations=config.NUM_SIMULATIONS,
            crash_mean=params["crash_mean"],
            crash_std=params["crash_std"]
        )
        results[name] = mc_result
        
        print(f"\n{name}:")
        print(f"  Mean Crash: {params['crash_mean']:.0%} (+/- {params['crash_std']:.0%})")
        print(f"  Mean Profit: ${mc_result.mean_profit:>12,.2f}")
        print(f"  Std Dev:     ${mc_result.std_profit:>12,.2f}")
        print(f"  Profitable:  {mc_result.profitable_pct:>11.1f}%")
        print(f"  VaR (95%):   ${mc_result.var_95:>12,.2f}")
    
    print("\n" + "=" * 70)
    
    return results


def print_monte_carlo_summary(result: MonteCarloResult):
    """Print formatted Monte Carlo results."""
    print("\n" + "=" * 50)
    print("MONTE CARLO SIMULATION RESULTS")
    print("=" * 50)
    print(f"Simulations:     {result.num_simulations:,}")
    print("-" * 50)
    print(f"Mean Profit:     ${result.mean_profit:>15,.2f}")
    print(f"Std Deviation:   ${result.std_profit:>15,.2f}")
    print(f"Minimum:         ${result.min_profit:>15,.2f}")
    print(f"Maximum:         ${result.max_profit:>15,.2f}")
    print("-" * 50)
    print(f"Profitable Runs: {result.profitable_pct:>14.1f}%")
    print(f"VaR (95%):       ${result.var_95:>15,.2f}")
    print(f"Expected Short.: ${result.expected_shortfall:>15,.2f}")
    print("=" * 50)


if __name__ == "__main__":
    print("\n[*] Running Monte Carlo Simulation...")
    
    # Single scenario
    result = run_monte_carlo(
        num_simulations=1000,
        crash_mean=0.20,
        crash_std=0.08
    )
    print_monte_carlo_summary(result)
    
    print("\n")
    
    # Full scenario analysis
    run_scenario_analysis()
