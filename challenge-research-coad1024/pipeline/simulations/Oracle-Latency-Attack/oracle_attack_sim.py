"""
Oracle Latency Attack Simulation

Models the profitability of exploiting Terra's 30-second oracle delay
during rapid price crashes. Based on Terra Backing Deep Dive Section 3.

Attack Vector:
1. Oracle reports stale LUNA price (30s old)
2. Real LUNA price crashes (e.g., 20% in 15s)
3. Attacker swaps UST -> LUNA at "old" high price
4. Attacker sells LUNA at real market price
5. Profit = (Oracle_Price - Real_Price) * Amount - Costs

Author: Research Challenge Team
Date: January 2026
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Tuple
import config


@dataclass
class OracleState:
    """Represents the oracle's knowledge of LUNA price."""
    reported_price: float       # What oracle reports (stale)
    real_price: float           # Actual market price
    last_update_time: float     # Timestamp of last oracle update
    

@dataclass
class AttackResult:
    """Results of a single attack simulation."""
    attack_time: float          # When attack was executed
    ust_spent: float            # UST used for attack
    luna_received: float        # LUNA received from swap
    luna_sold_value: float      # USD from selling at real price
    spread_paid: float          # Tobin tax paid (%)
    gross_profit: float         # Before costs
    net_profit: float           # After gas + slippage
    profitable: bool            # Net profit > 0


class TerraMarketModule:
    """
    Simulates Terra's x/market module with virtual AMM.
    
    Key mechanics:
    - Virtual pools track UST/LUNA imbalance (TerraPoolDelta)
    - Stability spread increases with selling pressure
    - No actual reserves - just mathematical variables
    """
    
    def __init__(self, base_pool: float = config.BASE_POOL_USD):
        self.base_pool = base_pool
        self.terra_pool_delta = 0  # Tracks deviation from equilibrium
        
    def calculate_spread(self) -> float:
        """
        Calculate current stability spread (Tobin tax).
        
        Spread = max(MinSpread, UST_Sold / BasePool)
        
        Higher selling pressure -> higher spread -> more expensive to exit
        """
        pool_imbalance = abs(self.terra_pool_delta) / self.base_pool
        return max(config.MIN_SPREAD, min(pool_imbalance, config.MAX_SPREAD))
    
    def swap_ust_to_luna(
        self, 
        ust_amount: float, 
        oracle_luna_price: float
    ) -> Tuple[float, float]:
        """
        Swap UST for LUNA using the virtual AMM.
        
        Returns:
            Tuple of (luna_received, spread_paid)
        """
        # Calculate spread before swap
        spread = self.calculate_spread()
        
        # After spread, how much USD value is converted
        effective_usd = ust_amount * (1 - spread)
        
        # LUNA received = Effective USD / Oracle LUNA Price
        # (Protocol uses STALE oracle price - the exploit!)
        luna_received = effective_usd / oracle_luna_price
        
        # Update pool delta (more UST sold = higher spread next time)
        self.terra_pool_delta += ust_amount
        
        return luna_received, spread


class TerraOracle:
    """
    Simulates Terra's x/oracle module with weighted median voting.
    
    Key mechanics:
    - Price updates every VotePeriod (~30 seconds)
    - Price is ALWAYS stale by up to VotePeriod
    - Creates arbitrage window during rapid price changes
    """
    
    def __init__(self, initial_luna_price: float = 1.0):
        self.reported_price = initial_luna_price
        self.real_price = initial_luna_price
        self.last_update_time = 0.0
        
    def update_real_price(self, new_price: float, current_time: float):
        """Update the actual market price (not what oracle reports)."""
        self.real_price = new_price
        
    def update_oracle(self, current_time: float):
        """
        Simulate oracle update (happens every VotePeriod).
        
        Oracle "catches up" to real price.
        """
        self.reported_price = self.real_price
        self.last_update_time = current_time
        
    def get_state(self) -> OracleState:
        return OracleState(
            reported_price=self.reported_price,
            real_price=self.real_price,
            last_update_time=self.last_update_time
        )
    
    @property
    def price_delta(self) -> float:
        """Difference between stale oracle and real price."""
        return self.reported_price - self.real_price
    
    @property
    def arbitrage_opportunity(self) -> float:
        """Percentage profit opportunity from oracle staleness."""
        if self.real_price <= 0:
            return 0
        return (self.reported_price - self.real_price) / self.real_price


def simulate_price_crash(
    initial_price: float,
    crash_percentage: float,
    crash_duration: float,
    timestep: float = 1.0
) -> List[Tuple[float, float]]:
    """
    Generate a price crash trajectory.
    
    Returns list of (time, price) tuples.
    """
    final_price = initial_price * (1 - crash_percentage)
    num_steps = int(crash_duration / timestep)
    
    prices = []
    for i in range(num_steps + 1):
        t = i * timestep
        # Linear crash (could model exponential for more realism)
        price = initial_price - (initial_price - final_price) * (t / crash_duration)
        prices.append((t, max(price, 0.001)))  # Floor at 0.001
    
    return prices


def run_attack_simulation(
    crash_percentage: float,
    attacker_capital: float = config.ATTACKER_CAPITAL,
    verbose: bool = False
) -> AttackResult:
    """
    Simulate a single oracle latency attack.
    
    Timeline:
    1. t=0: Oracle updates, LUNA price = $1.00
    2. t=0 to t=15s: LUNA crashes to $0.80 (20% drop)
    3. t=15s: Attacker sees real price, oracle still shows $1.00
    4. Attacker swaps UST -> LUNA at $1.00 oracle price
    5. Attacker sells LUNA at $0.80 real price
    6. t=30s: Oracle updates (too late!)
    """
    initial_luna_price = 1.0
    
    # Initialize components
    oracle = TerraOracle(initial_luna_price)
    market = TerraMarketModule()
    
    # Simulate price crash
    crash_trajectory = simulate_price_crash(
        initial_price=initial_luna_price,
        crash_percentage=crash_percentage,
        crash_duration=config.CRASH_DURATION_SECONDS
    )
    
    # Apply crash to oracle's "real price" (oracle doesn't know yet!)
    for t, price in crash_trajectory:
        oracle.update_real_price(price, t)
    
    # Oracle still reports OLD price!
    oracle_state = oracle.get_state()
    
    if verbose:
        print(f"Oracle Price: ${oracle_state.reported_price:.4f}")
        print(f"Real Price:   ${oracle_state.real_price:.4f}")
        print(f"Arb Opportunity: {oracle.arbitrage_opportunity:.2%}")
    
    # Execute attack
    ust_spent = attacker_capital
    luna_received, spread_paid = market.swap_ust_to_luna(
        ust_amount=ust_spent,
        oracle_luna_price=oracle_state.reported_price
    )
    
    # Sell LUNA at real market price
    luna_sold_value = luna_received * oracle_state.real_price
    
    # Calculate profit
    gross_profit = luna_sold_value - ust_spent
    gas_costs = config.GAS_COST_USD * 2  # Swap + Sell
    slippage_costs = luna_sold_value * config.SLIPPAGE_TOLERANCE
    net_profit = gross_profit - gas_costs - slippage_costs
    
    return AttackResult(
        attack_time=config.CRASH_DURATION_SECONDS,
        ust_spent=ust_spent,
        luna_received=luna_received,
        luna_sold_value=luna_sold_value,
        spread_paid=spread_paid,
        gross_profit=gross_profit,
        net_profit=net_profit,
        profitable=net_profit > 0
    )


def run_sensitivity_analysis() -> dict:
    """
    Run attack simulations across different crash scenarios.
    
    Returns dict mapping crash_percentage -> AttackResult
    """
    results = {}
    
    print("=" * 60)
    print("ORACLE LATENCY ATTACK - SENSITIVITY ANALYSIS")
    print("=" * 60)
    print(f"Attacker Capital: ${config.ATTACKER_CAPITAL:,.0f}")
    print(f"Oracle Delay: {config.ORACLE_DELAY_SECONDS}s")
    print(f"Crash Duration: {config.CRASH_DURATION_SECONDS}s")
    print("-" * 60)
    
    for crash_pct in config.PRICE_CRASH_SCENARIOS:
        result = run_attack_simulation(crash_pct)
        results[crash_pct] = result
        
        status = "[PROFITABLE]" if result.profitable else "[UNPROFITABLE]"
        print(f"Crash {crash_pct:5.0%}: Net P&L = ${result.net_profit:>12,.2f} | Spread = {result.spread_paid:.2%} | {status}")
    
    print("-" * 60)
    
    # Find breakeven
    profitable_crashes = [c for c, r in results.items() if r.profitable]
    if profitable_crashes:
        min_profitable = min(profitable_crashes)
        print(f"[!] Minimum crash for profitability: {min_profitable:.0%}")
    else:
        print("[i] No profitable attack found in tested scenarios")
    
    return results


if __name__ == "__main__":
    print("\n[X] TERRA ORACLE LATENCY ATTACK SIMULATION\n")
    
    # Single attack example
    print("Example Attack (20% crash):")
    print("-" * 40)
    result = run_attack_simulation(0.20, verbose=True)
    print(f"\nUST Spent:      ${result.ust_spent:,.2f}")
    print(f"LUNA Received:  {result.luna_received:,.4f}")
    print(f"LUNA Sold For:  ${result.luna_sold_value:,.2f}")
    print(f"Spread Paid:    {result.spread_paid:.2%}")
    print(f"Gross Profit:   ${result.gross_profit:,.2f}")
    print(f"Net Profit:     ${result.net_profit:,.2f}")
    print(f"Profitable:     {'[YES]' if result.profitable else '[NO]'}")
    
    print("\n")
    
    # Sensitivity analysis
    run_sensitivity_analysis()
