def run():
    print("---------------------------------------------------")
    print("  TERRA ATTACK PROFITABILITY MODEL (SOROS SCENARIO)")
    print("---------------------------------------------------")

    # --- Assumptions ---
    # The attacker identifies that $500M is needed to break the Curve pool.
    # To be safe, they amass a $1B Short Position on LUNA and UST.
    
    initial_capital = 500_000_000.0  # $500M Seed Capital
    leverage = 2.0                   # 2x Leverage
    total_short_size = initial_capital * leverage # $1B Short
    
    # Split Short: 70% UST (The Peg), 30% LUNA (The Collateral)
    short_ust = total_short_size * 0.70
    short_luna = total_short_size * 0.30
    
    print(f"Initial Capital: ${initial_capital:,.2f}")
    print(f"Leverage: {leverage}x")
    print(f"Total Short Exposure: ${total_short_size:,.2f}")
    print(f"  - Short UST: ${short_ust:,.2f}")
    print(f"  - Short LUNA: ${short_luna:,.2f}")
    
    # --- Market Entry (Pre-Crash) ---
    entry_price_ust = 1.00
    entry_price_luna = 80.00
    
    # Borrowed Quantities
    borrowed_ust = short_ust / entry_price_ust
    borrowed_luna = short_luna / entry_price_luna
    
    print("\n--- Positions Opened ---")
    print(f"  - Borrowed {borrowed_ust:,.0f} UST @ ${entry_price_ust}")
    print(f"  - Borrowed {borrowed_luna:,.0f} LUNA @ ${entry_price_luna}")
    
    # --- The Cost of Attack ---
    # Interest for borrowing over ~10 days (assuming high rates due to utilization)
    apr_ust = 0.20  # 20% borrow cost
    apr_luna = 0.10 # 10% borrow cost
    duration_days = 10
    
    interest_cost_ust = (short_ust * apr_ust) * (duration_days / 365)
    interest_cost_luna = (short_luna * apr_luna) * (duration_days / 365)
    total_cost = interest_cost_ust + interest_cost_luna
    
    print("\n--- Attack Costs (10 Days) ---")
    print(f"  - Interest UST: ${interest_cost_ust:,.2f}")
    print(f"  - Interest LUNA: ${interest_cost_luna:,.2f}")
    print(f"  - Total Financing Cost: ${total_cost:,.2f}")
    
    # --- The Trigger ---
    print("\n[ACTION] Dzu ping $400M UST on Curve... Peg Breaks.")
    print("[EVENT] LFG Deploys Reserves... Failed.")
    print("[EVENT] Hyperinflation Triggers...")
    
    # --- Market Exit (Post-Crash) ---
    # Scenario: Attacker closes shorts at the bottom
    exit_price_ust = 0.05       # UST trades at 5 cents
    exit_price_luna = 0.0001    # LUNA trades at effectively zero
    
    # Repurchase Cost
    repurchase_cost_ust = borrowed_ust * exit_price_ust
    repurchase_cost_luna = borrowed_luna * exit_price_luna
    
    total_revenue_ust = short_ust - repurchase_cost_ust
    total_revenue_luna = short_luna - repurchase_cost_luna
    
    total_gross_profit = total_revenue_ust + total_revenue_luna
    net_profit = total_gross_profit - total_cost
    
    roi = (net_profit / initial_capital) * 100
    
    print("\n--- Positions Closed ---")
    print(f"  - Repurchased UST @ ${exit_price_ust}: Cost ${repurchase_cost_ust:,.2f}")
    print(f"  - Repurchased LUNA @ ${exit_price_luna}: Cost ${repurchase_cost_luna:,.2f}")
    
    print("\n--- PnL Summary ---")
    print(f"  - Gross Profit UST: ${total_revenue_ust:,.2f}")
    print(f"  - Gross Profit LUNA: ${total_revenue_luna:,.2f}")
    print(f"  - Net Profit: ${net_profit:,.2f}")
    print(f"  - Return on Investment (ROI): {roi:.2f}%")
    
    # Soros Equivalent
    uk_pound_profit = 1_000_000_000 # Soros made $1B
    print(f"\n--- Comparative Analysis ---")
    print(f"  - Soros (1992): ~$1 Billion Profit")
    print(f"  - Terra Attacker: ~${net_profit/1_000_000_000:.2f} Billion Profit")
    
    if net_profit > uk_pound_profit:
        print("  VERDICT: More profitable than the Bank of England attack.")
    else: 
        print("  VERDICT: Comparable to the Bank of England attack.")

if __name__ == "__main__":
    run()
