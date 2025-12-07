import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# Ensure the source directory is in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from source.liquidity_pools.constant_product_formula import ConstantProductFormula
from source.liquidity_pools.liquidity_pool import LiquidityPool
from source.liquidity_pools.simple_virtual_liquidity_pool import SimpleVirtualLiquidityPool
from source.purchase_generators.seignorage_model_purchase_generator import SeignorageModelPurchaseGenerator
from source.Tokens.algorithmic_stablecoin import AlgorithmicStablecoin
from source.Tokens.collateral_token import CollateralToken
from source.Tokens.reference_token import ReferenceToken
from source.simulations.three_pools_simulation import ThreePoolsSimulation
from source.attacker import Attacker
from tqdm import tqdm

def calculate_volatility_array(volumes_daily, total_iterations_per_day, sqrt_2_pi=0.7979):
    volume_values_daily = [volume / total_iterations_per_day for volume in volumes_daily]
    volume_array = np.repeat(volume_values_daily, total_iterations_per_day)
    volatility_array = volume_array / sqrt_2_pi
    return volatility_array.tolist()

try:
    # --- Configuration ---
    iterations_per_day = 1440
    
    attack_day = 5
    attack_iteration = attack_day * iterations_per_day
    attack_swap_amount = 500_000_000 
    
    # STRATEGY: Short Amount (USD Value)
    # The attacker bets 1B USD that Collateral Token will crash - High Leverage
    short_position_size_usd = 1_000_000_000 

    stablecoin_initial_price = 1.0 
    stablecoin_initial_supply = 18_490_738_908
    stablecoin_initial_free_supply = stablecoin_initial_supply * 0.5
    stablecoin_pool_fee = 0.03

    collateral_initial_price = 80.0 
    collateral_initial_supply = 345_341_994.7
    collateral_initial_free_supply = collateral_initial_supply * 0.5
    collateral_pool_fee = 0.03

    vlp_stablecoin_base_quantity = 6.7215e7
    vlp_pool_fee = 0.0
    pool_recovery_period = 36

    volumes_daily_stablecoin = [
        547686207.2, 566644084.6, 574239250.7, 453049346.2, 612280606.5, 733858936.5,
        649583067.2, 1335178681, 2025913193, 2809970941
    ]
    volumes_daily_collateral = [
        1712121334, 1788318413, 1955818800, 1302497178, 1941974963, 2276428168,
        2178573977, 3054299674, 5108105142, 6306976142
    ]

    number_of_iterations = iterations_per_day * len(volumes_daily_collateral)
    
    volatility_array_stablecoin = calculate_volatility_array(volumes_daily_stablecoin, iterations_per_day)
    volatility_array_collateral = calculate_volatility_array(volumes_daily_collateral, iterations_per_day)

    cpf = ConstantProductFormula()

    stablecoin = AlgorithmicStablecoin(name="AS",
                                       peg=1.0,
                                       initial_price=stablecoin_initial_price,
                                       initial_supply=stablecoin_initial_supply,
                                       initial_free_supply=stablecoin_initial_free_supply)

    collateral = CollateralToken(name="CT",
                                 initial_price=collateral_initial_price,
                                 initial_supply=collateral_initial_supply,
                                 initial_free_supply=collateral_initial_free_supply,
                                 algorithmic_stablecoin=stablecoin)

    reference = ReferenceToken(name="USD")

    stablecoin_pool_quantity = stablecoin_initial_supply - stablecoin_initial_free_supply
    stablecoin_pool_reference_quantity = stablecoin_pool_quantity * stablecoin_initial_price

    collateral_pool_quantity = collateral_initial_supply - collateral_initial_free_supply
    collateral_pool_reference_quantity = collateral_pool_quantity * collateral_initial_price

    stablecoin_pool = LiquidityPool(token_a=stablecoin,
                                    token_b=reference,
                                    quantity_token_a=stablecoin_pool_quantity,
                                    quantity_token_b=stablecoin_pool_reference_quantity,
                                    formula=cpf,
                                    fee=stablecoin_pool_fee)

    collateral_pool = LiquidityPool(token_a=collateral,
                                    token_b=reference,
                                    quantity_token_a=collateral_pool_quantity,
                                    quantity_token_b=collateral_pool_reference_quantity,
                                    formula=cpf,
                                    fee=collateral_pool_fee)

    virtual_pool = SimpleVirtualLiquidityPool(stablecoin=stablecoin,
                                              collateral=collateral,
                                              stablecoin_base_quantity=vlp_stablecoin_base_quantity,
                                              formula=cpf,
                                              fee=vlp_pool_fee,
                                              pool_recovery_period=int(pool_recovery_period))

    stablecoin_purchase_generator = SeignorageModelPurchaseGenerator(token=stablecoin,
                                                                     volatility=volatility_array_stablecoin,
                                                                     delta_variation=lambda x: 1 / x - 1,
                                                                     threshold=0.05,
                                                                     pool_fee=stablecoin_pool_fee)

    collateral_purchase_generator = SeignorageModelPurchaseGenerator(token=collateral,
                                                                     volatility=volatility_array_collateral,
                                                                     delta_variation=lambda x: 1 / x - 1,
                                                                     threshold=0.05,
                                                                     pool_fee=collateral_pool_fee)

    # --- Attacker Setup ---
    attacker_initial_wallet = {
        stablecoin: attack_swap_amount * 1.5, 
        reference: 0.0
    }
    attacker = Attacker(initial_wallet=attacker_initial_wallet)
    
    print(f"Attacker Initial Portfolio Value (USD): {attacker.get_portfolio_value():,.2f}")

    # Custom Simulation Loop to Control Steps
    simulation = ThreePoolsSimulation(stablecoin_token=stablecoin,
                                      collateral_token=collateral,
                                      reference_token=reference,
                                      stablecoin_pool=stablecoin_pool,
                                      collateral_pool=collateral_pool,
                                      virtual_pool=virtual_pool,
                                      stablecoin_purchase_generator=stablecoin_purchase_generator,
                                      collateral_purchase_generator=collateral_purchase_generator,
                                      number_of_iterations=number_of_iterations)
    
    # We override the run_simulation to inject our manual steps without modifying the class
    # No, better to just run the loop manually or subclass. 
    # Let's write the loop manually here since we need fine control over the attacker actions sequence.
    
    simulation_data = {
        "stablecoin_price_history": [],
        "collateral_price_history": [],
        "attacker_pnl_history": []
    }
    
    initial_pnl = attacker.get_portfolio_value()
    
    with tqdm(total=number_of_iterations, desc="Simulation Progress", unit="iter") as pbar:
        for iteration in range(number_of_iterations):
            
            # --- ATTACK SEQUENCE ---
            if iteration == attack_iteration:
                print(f"\n[!] Day {attack_day}: LAUNCHING ATTACK")
                
                # 1. Open Short Position on Collateral Token
                # Convert USD size to Token Amount
                short_amount = short_position_size_usd / collateral.price
                attacker.open_short(collateral, short_amount)
                print(f"    - Opened SHORT on CT: {short_amount:,.2f} tokens (@ ${collateral.price:.2f})")
                
                # 2. Dump Stablecoin to trigger Spiral
                print(f"    - Dumping {attack_swap_amount:,.2f} AS...")
                attacker.swap(stablecoin_pool, stablecoin, attack_swap_amount)
                print(f"    - Dump Complete. New AS Price: ${stablecoin.price:.4f}")

            # Capture Data
            simulation_data["stablecoin_price_history"].append(stablecoin.price)
            simulation_data["collateral_price_history"].append(collateral.price)
            simulation_data["attacker_pnl_history"].append(attacker.get_portfolio_value() - initial_pnl)
            
            # Standard Market Steps
            simulation.market_simulator.execute_random_purchases()
            
            # Update Progress
            pbar.update(1)
            
            # Optional: Close short at the end
            if iteration == number_of_iterations - 1:
                 print("\n[!] Closing Short Position...")
                 pnl = attacker.close_short(collateral)
                 print(f"    - Short Closed. PnL from Short: ${pnl:,.2f}")

    final_pnl = attacker.get_portfolio_value() - initial_pnl
    print(f"\nAttacker Final Total PnL (USD): {final_pnl:,.2f}")
    
    # --- Plotting ---
    print("Saving plots...")
    output_dir = "simulation_results"
    os.makedirs(output_dir, exist_ok=True)
    
    # Use a cleaner style and larger fonts
    plt.figure(figsize=(14, 18), dpi=100)
    plt.rcParams.update({'font.size': 12})
    
    # Stability
    plt.subplot(3, 1, 1)
    plt.plot(simulation_data["stablecoin_price_history"], label="Stablecoin (AS) Price", color="#1f77b4", linewidth=2)
    plt.axvline(x=attack_iteration, color='r', linestyle='--', label='Attack Start')
    plt.title("Stablecoin Peg Stability", fontsize=16, fontweight='bold')
    plt.ylabel("Price ($)", fontsize=14)
    plt.xlabel("Iterations", fontsize=12)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.legend(loc='upper right')
    
    # Collateral
    plt.subplot(3, 1, 2)
    plt.plot(simulation_data["collateral_price_history"], label="Collateral (CT) Price", color="#ff7f0e", linewidth=2)
    plt.axvline(x=attack_iteration, color='r', linestyle='--', label='Attack Start')
    plt.title("Collateral Token Price (Short Target)", fontsize=16, fontweight='bold')
    plt.ylabel("Price ($)", fontsize=14)
    plt.xlabel("Iterations", fontsize=12)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.legend(loc='upper right')
    
    # PnL
    plt.subplot(3, 1, 3)
    # Highlight the zero line
    plt.axhline(y=0, color='black', linewidth=1, linestyle='-')
    plt.plot(simulation_data["attacker_pnl_history"], label="Attacker Cumulative PnL", color="#2ca02c", linewidth=2)
    plt.axvline(x=attack_iteration, color='r', linestyle='--', label='Attack Start')
    plt.title("Attacker Profit/Loss", fontsize=16, fontweight='bold')
    plt.ylabel("PnL ($)", fontsize=14)
    plt.xlabel("Iterations", fontsize=12)
    
    # Format Y-axis for PnL to be readable (e.g. Millions)
    current_values = plt.gca().get_yticks()
    plt.gca().set_yticklabels(['${:,.0f}M'.format(x/1e6) for x in current_values])
    
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.legend(loc='upper left')

    plt.tight_layout(pad=3.0)
    plt.savefig(os.path.join(output_dir, "profitable_attack_metrics.png"), bbox_inches='tight')
    print(f"Plot saved to {os.path.abspath(os.path.join(output_dir, 'profitable_attack_metrics.png'))}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
