import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def simulate_depeg_attack(
    total_supply=100_000_000,  # 100M LUSD
    target_price=0.90,         # Attacker wants to hold price here
    initial_base_rate=0.0,
    half_life_hours=12,
    alpha=0.5,
    market_depth_per_cent=1_000_000, # $1M to move price 1 cent
    simulation_hours=48
):
    """
    Simulates the cost of maintaining a de-peg against the Redemption Mechanism.
    """
    
    dt_min = 10 # 10 minute steps
    steps = int(simulation_hours * 60 / dt_min)
    
    base_rate = initial_base_rate
    decay_factor = 0.5 ** (dt_min / (half_life_hours * 60))
    
    results = []
    
    cumulative_attacker_cost = 0
    cumulative_redemptions = 0
    
    for step in range(steps):
        # 1. Decay Base Rate
        base_rate = base_rate * decay_factor
        
        # 2. Calculate Effective Redemption Price
        # Fee = BaseRate + 0.5% (min)
        current_fee = base_rate + 0.005
        redemption_price = 1.0 - current_fee
        
        # 3. Arb Opportunity
        # If Target Price < Redemption Price, Arbs will buy and redeem
        arb_volume = 0
        attacker_sell_volume = 0
        
        if target_price < redemption_price:
            # Arbs want to buy up to the price where arbitrage closes
            # Price gap
            price_gap = redemption_price - target_price
            
            # Volume needed to close the gap (Market Depth)
            # Assuming linear depth: Volume = Gap * Depth * 100 (cents)
            potential_arb_volume = price_gap * 100 * market_depth_per_cent
            
            # Cap arb volume per step (e.g., limited by block space or capital)
            # Let's say max 5% of supply per hour -> ~0.8% per 10 mins
            max_arb_volume = total_supply * 0.008 
            
            actual_arb_volume = min(potential_arb_volume, max_arb_volume)
            
            # Attacker must SELL this amount to keep price at target
            attacker_sell_volume = actual_arb_volume
            
            # Attacker Cost: Sells at TargetPrice, could have sold at 1.0 (theoretically) 
            # or simply the loss vs fair value. 
            # Real cost: Slippage + Fees. 
            # Simplified: Cost = Volume * (1 - TargetPrice)
            # This represents the "subsidy" the attacker pays to Arbs.
            cost = attacker_sell_volume * (1.0 - target_price)
            cumulative_attacker_cost += cost
            
            # 4. Execute Redemption
            # Base Rate Increase
            base_rate_increase = alpha * (actual_arb_volume / total_supply)
            base_rate += base_rate_increase
            
            cumulative_redemptions += actual_arb_volume
            
        results.append({
            "time_hours": step * dt_min / 60,
            "base_rate": base_rate,
            "redemption_price": redemption_price,
            "attacker_cost": cumulative_attacker_cost,
            "total_redeemed": cumulative_redemptions
        })
        
    return pd.DataFrame(results)

# Run Simulation
df = simulate_depeg_attack()

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(df['time_hours'], df['base_rate'], label='Base Rate')
plt.plot(df['time_hours'], df['redemption_price'], label='Redemption Price (Net)', linestyle='--')
plt.axhline(y=0.90, color='r', linestyle=':', label='Target Price ($0.90)')
plt.title('Liquity De-Peg Simulation: Base Rate vs Time')
plt.ylabel('Rate / Price')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(df['time_hours'], df['attacker_cost'] / 1_000_000, label='Cumulative Cost (Millions)', color='orange')
plt.title('Attacker Cost to Maintain $0.90 Peg')
plt.xlabel('Hours')
plt.ylabel('Cost ($M)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('depeg_simulation_plot.png')

# Save results to markdown
with open('simulation_results.md', 'w') as f:
    f.write("# De-Peg Simulation Results\n\n")
    f.write("Scenario: Attacker tries to hold LUSD at $0.90 for 48 hours.\n\n")
    f.write(df.tail(1).to_markdown(index=False))
    f.write("\n\n## Interpretation\n")
    f.write("As the attacker sells to suppress the price, arbitrageurs buy and redeem.\n")
    f.write("This spikes the **Base Rate**, making redemption more expensive.\n")
    f.write("Eventually, the Redemption Price drops below $0.90 (Fee > 10%).\n")
    f.write("At this point, arbitrage stops, and the attacker can hold the peg with zero cost (assuming no other buyers).\n")
    f.write("However, the initial cost to push the rate that high is significant.\n")
