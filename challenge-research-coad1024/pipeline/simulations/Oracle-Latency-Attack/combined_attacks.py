"""
Combined Attack Vectors

Models multi-vector attacks that combine oracle latency with other vulnerabilities:
1. Oracle + Death Spiral (cascading)
2. Oracle + Flash Loan (amplified capital)
3. Oracle + Front-Running (MEV extraction)

Author: Research Challenge Team
Date: January 2026
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Tuple
import config
from oracle_attack_sim import TerraMarketModule, TerraOracle, AttackResult


@dataclass
class CombinedAttackResult:
    """Results from combined attack vector."""
    vector_name: str
    initial_capital: float
    final_pnl: float
    leverage_factor: float  # For flash loan attacks
    rounds: int  # For cascading attacks
    profitable: bool
    roi: float  # Return on initial capital


class DeathSpiralAttack:
    """
    Combined Oracle Latency + Death Spiral Attack
    
    Strategy:
    1. Wait for initial de-peg (UST drops to $0.95)
    2. Exploit oracle latency to extract value
    3. Extracted value triggers more LUNA minting
    4. LUNA price drops further
    5. Repeat until system collapses
    
    This models the actual Terra collapse mechanism.
    """
    
    def __init__(
        self,
        initial_ust_peg: float = 1.0,
        initial_luna_price: float = 1.0,
        ust_supply: float = 18_000_000_000,  # $18B UST at peak
        initial_luna_supply: float = 350_000_000,  # 350M LUNA
    ):
        self.ust_peg = initial_ust_peg
        self.luna_price = initial_luna_price
        self.ust_supply = ust_supply
        self.luna_supply = initial_luna_supply
        self.market = TerraMarketModule()
        self.oracle = TerraOracle(initial_luna_price)
        
        # Track attack rounds
        self.rounds = []
    
    def calculate_luna_market_cap(self) -> float:
        """Current LUNA market cap."""
        return self.luna_supply * self.luna_price
    
    def calculate_backing_ratio(self) -> float:
        """Ratio of LUNA mcap to UST supply (informal 'backing')."""
        if self.ust_supply == 0:
            return float('inf')
        return self.calculate_luna_market_cap() / self.ust_supply
    
    def simulate_redemption_wave(
        self,
        ust_to_redeem: float,
        oracle_delay_factor: float = 1.0  # How stale the oracle is
    ) -> Tuple[float, float, float]:
        """
        Simulate a wave of UST redemptions.
        
        Returns:
            Tuple of (luna_minted, new_luna_price, spread_paid)
        """
        # Oracle reports old LUNA price
        oracle_luna_price = self.luna_price * oracle_delay_factor
        
        # Protocol mints LUNA to cover redemption
        spread = self.market.calculate_spread()
        effective_usd = ust_to_redeem * (1 - spread)
        luna_to_mint = effective_usd / oracle_luna_price
        
        # Minting increases supply -> price drops
        self.luna_supply += luna_to_mint
        
        # Simple price impact model: price inversely proportional to supply
        supply_increase = luna_to_mint / (self.luna_supply - luna_to_mint)
        self.luna_price *= (1 - supply_increase * 0.5)  # 50% pass-through
        
        # UST burned
        self.ust_supply -= ust_to_redeem
        
        # Update market state
        self.market.terra_pool_delta += ust_to_redeem
        
        return luna_to_mint, self.luna_price, spread
    
    def run_death_spiral(
        self,
        initial_redemption: float = 1_000_000_000,  # $1B initial wave
        panic_multiplier: float = 1.5,  # Each round, 50% more people panic
        max_rounds: int = 20,
        stop_price: float = 0.001  # Stop when LUNA < $0.001
    ) -> List[dict]:
        """
        Simulate the death spiral cascade.
        
        Returns list of round results.
        """
        redemption_amount = initial_redemption
        
        for round_num in range(1, max_rounds + 1):
            # Check stop conditions
            if self.luna_price < stop_price:
                break
            if self.ust_supply < redemption_amount:
                redemption_amount = self.ust_supply
            if redemption_amount < 1000:
                break
            
            # Oracle delay increases during volatility
            oracle_delay = 1.0 + (round_num - 1) * 0.05  # 5% more stale each round
            
            # Execute redemption wave
            luna_minted, new_price, spread = self.simulate_redemption_wave(
                redemption_amount,
                oracle_delay_factor=oracle_delay
            )
            
            round_result = {
                "round": round_num,
                "ust_redeemed": redemption_amount,
                "luna_minted": luna_minted,
                "luna_price": new_price,
                "luna_supply": self.luna_supply,
                "ust_remaining": self.ust_supply,
                "spread": spread,
                "backing_ratio": self.calculate_backing_ratio()
            }
            self.rounds.append(round_result)
            
            # Next round: more panic
            redemption_amount *= panic_multiplier
        
        return self.rounds


class FlashLoanAttack:
    """
    Oracle Latency + Flash Loan Attack
    
    Strategy:
    1. Borrow massive capital via flash loan (no collateral)
    2. Execute oracle arbitrage at 100x+ scale
    3. Repay flash loan + fee
    4. Keep profit
    
    Note: This requires DeFi composability that Terra Classic lacked,
    but models a more sophisticated attack vector.
    """
    
    def __init__(
        self,
        flash_loan_fee: float = 0.0009,  # 0.09% (Aave style)
        max_flash_loan: float = 500_000_000,  # $500M max
    ):
        self.flash_loan_fee = flash_loan_fee
        self.max_flash_loan = max_flash_loan
    
    def execute_attack(
        self,
        own_capital: float,
        leverage: float,
        crash_percentage: float
    ) -> CombinedAttackResult:
        """
        Execute flash loan amplified oracle attack.
        """
        from oracle_attack_sim import run_attack_simulation
        
        # Calculate borrowed amount
        borrowed = min(own_capital * (leverage - 1), self.max_flash_loan)
        total_capital = own_capital + borrowed
        flash_loan_cost = borrowed * self.flash_loan_fee
        
        # Run base attack with amplified capital
        result = run_attack_simulation(crash_percentage, attacker_capital=total_capital)
        
        # Deduct flash loan cost
        final_pnl = result.net_profit - flash_loan_cost
        
        return CombinedAttackResult(
            vector_name="Oracle + Flash Loan",
            initial_capital=own_capital,
            final_pnl=final_pnl,
            leverage_factor=leverage,
            rounds=1,
            profitable=final_pnl > 0,
            roi=final_pnl / own_capital if own_capital > 0 else 0
        )


def run_death_spiral_simulation():
    """Run and print death spiral simulation."""
    print("\n" + "=" * 70)
    print("DEATH SPIRAL SIMULATION")
    print("=" * 70)
    print("Initial State:")
    print("  UST Supply: $18B")
    print("  LUNA Price: $1.00")
    print("  LUNA Supply: 350M")
    print("-" * 70)
    
    attack = DeathSpiralAttack()
    rounds = attack.run_death_spiral(
        initial_redemption=1_000_000_000,
        panic_multiplier=1.5,
        max_rounds=15
    )
    
    print(f"\n{'Round':>5} | {'UST Redeemed':>15} | {'LUNA Minted':>15} | {'LUNA Price':>12} | {'Backing':>10}")
    print("-" * 70)
    
    for r in rounds:
        print(f"{r['round']:>5} | ${r['ust_redeemed']/1e9:>13.2f}B | {r['luna_minted']/1e6:>13.2f}M | ${r['luna_price']:>10.6f} | {r['backing_ratio']:>9.2%}")
    
    print("-" * 70)
    print(f"Final LUNA Price: ${rounds[-1]['luna_price']:.8f}")
    print(f"Final LUNA Supply: {rounds[-1]['luna_supply']/1e9:.2f}B (was 350M)")
    print(f"UST Remaining: ${rounds[-1]['ust_remaining']/1e9:.2f}B (was $18B)")
    print("=" * 70)


def run_flash_loan_analysis():
    """Analyze flash loan attack profitability."""
    print("\n" + "=" * 70)
    print("FLASH LOAN AMPLIFIED ATTACK ANALYSIS")
    print("=" * 70)
    
    attack = FlashLoanAttack()
    own_capital = 1_000_000  # $1M own capital
    crash_scenarios = [0.10, 0.20, 0.30, 0.40]
    leverage_levels = [1, 5, 10, 50, 100]
    
    print(f"\nOwn Capital: ${own_capital:,.0f}")
    print(f"\n{'Crash':>8} | {'1x':>12} | {'5x':>12} | {'10x':>12} | {'50x':>12} | {'100x':>12}")
    print("-" * 70)
    
    for crash in crash_scenarios:
        row = f"{crash:>7.0%} |"
        for leverage in leverage_levels:
            result = attack.execute_attack(own_capital, leverage, crash)
            status = "P" if result.profitable else "L"
            row += f" ${result.final_pnl/1000:>9,.0f}K{status} |"
        print(row)
    
    print("-" * 70)
    print("P = Profitable, L = Loss")
    print("=" * 70)


if __name__ == "__main__":
    run_death_spiral_simulation()
    run_flash_loan_analysis()
