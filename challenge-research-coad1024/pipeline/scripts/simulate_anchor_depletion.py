import csv
from datetime import datetime, timedelta

def simulate_anchor_depletion():
    """
    Simulates the depletion of the Anchor Yield Reserve leading up to the crash.
    Model assumes:
    - High fixed APY payout (19.5%)
    - Growing deposits vs stagnating borrows
    - The LFG injection in Feb 2022
    """
    
    # Simulation Window: Jan 1 2022 to May 15 2022
    start_date = datetime(2022, 1, 1)
    days = 135
    
    # Initial State (Approximate)
    deposits = 10_000_000_000.0 # 10B UST
    borrows = 2_500_000_000.0   # 2.5B UST
    reserve = 70_000_000.0      # 70M UST (Low before top up)
    
    anchor_rate = 0.195 / 365 # Daily rate
    borrow_rate = 0.12 / 365  # Daily income from borrowers (approx)
    staking_yield = 0.07 / 365 # Daily yield on collateral
    
    # LFG Injection
    injection_date = datetime(2022, 2, 18)
    injection_amount = 450_000_000.0
    
    data = []
    
    for i in range(days):
        current_date = start_date + timedelta(days=i)
        
        # Growth assumptions
        deposits += 50_000_000 # 50M daily inflow
        borrows += 5_000_000   # 5M daily borrow growth (slow)
        
        # Injection event
        if current_date.date() == injection_date.date():
            reserve += injection_amount
            
        # Daily Cashflow
        # Expense: Interest paid to depositors
        expense = deposits * anchor_rate
        
        # Income: Interest from borrowers + Staking rewards from collateral
        # Assuming collateral value ~ 2x borrows (LTV 50%)
        collateral_value = borrows * 2.0
        income = (borrows * borrow_rate) + (collateral_value * staking_yield)
        
        net_flow = income - expense
        reserve += net_flow
        
        # Stop if reserve hits 0 (insolvency)
        if reserve < 0:
            reserve = 0
            
        data.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "deposits": deposits,
            "borrows": borrows,
            "reserve": reserve,
            "net_flow": net_flow
        })

    # Save
    output_dir = "challenge-research-coad1024/analysis/Terra/data"
    import os
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_path = f"{output_dir}/anchor_depletion_sim.csv"
    
    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["date", "deposits", "borrows", "reserve", "net_flow"])
        writer.writeheader()
        writer.writerows(data)
        
    print(f"✅ Anchor simulation saved to {output_path}")

if __name__ == "__main__":
    simulate_anchor_depletion()
