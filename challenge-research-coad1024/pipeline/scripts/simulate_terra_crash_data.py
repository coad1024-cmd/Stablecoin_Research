import csv
import random
import os
from pathlib import Path
from datetime import datetime, timedelta

def simulate_death_spiral():
    # Simulation Parameters (May 7 - May 13, 2022)
    # 7 days, hourly data
    hours = 24 * 7
    start_date = datetime(2022, 5, 7)
    
    # Initialize arrays
    data = []
    luna_supply = 350_000_000.0
    luna_price = 80.0
    anchor_reserve = 450_000_000.0
    ust_peg = 1.0
    
    for i in range(hours):
        timestamp = start_date + timedelta(hours=i)
        
        # Anchor depletion
        drain_rate = 500_000 if i < 48 else 5_000_000
        anchor_reserve = max(0, anchor_reserve - drain_rate)
        
        # De-peg starts after 48 hours (May 9)
        if i > 48:
            panic_factor = (i - 48) / (hours - 48)
            ust_peg -= (0.01 * random.uniform(0.5, 1.5))
            
            # Death spiral mechanism:
            ust_burned = 10_000_000 * (1 - ust_peg) * 10
            luna_to_mint = ust_burned / max(0.000001, luna_price)
            
            luna_supply += luna_to_mint
            
            # LUNA price crash
            inflation_ratio = luna_supply / (luna_supply - luna_to_mint) if (luna_supply - luna_to_mint) > 0 else 1
            luna_price = luna_price / (inflation_ratio * (1 + 0.05 * panic_factor))
            
            # Floor prices
            if ust_peg < 0.05: ust_peg = 0.05 + random.uniform(0, 0.02)
            if luna_price < 0.0001: luna_price = 0.0001
        else:
            # Normal variance
            ust_peg = 1.0 + random.gauss(0, 0.001)
            luna_price += random.gauss(0, 0.5)
            # luna_supply stays same
            
        data.append({
            "timestamp": timestamp.isoformat(),
            "ust_peg": ust_peg,
            "luna_price": luna_price,
            "luna_supply": luna_supply,
            "anchor_reserve": anchor_reserve
        })

    # Save to directory
    output_dir = Path("challenge-research-coad1024/analysis/Terra/data")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / "crash_simulation.csv"
    with open(output_path, 'w', newline='') as csvfile:
        fieldnames = ["timestamp", "ust_peg", "luna_price", "luna_supply", "anchor_reserve"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
            
    print(f"✅ Simulation complete. Data saved to {output_path}")
    print(f"Final stats: UST=${ust_peg:.4f}, LUNA Supply={luna_supply:,.0f}")

if __name__ == "__main__":
    simulate_death_spiral()