import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# Ensure the source directory is in the path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
sys.path.append(os.getcwd())

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

def run_phase_simulation(phase_name, short_size_usd, output_filename):
    print(f"\n--- Running {phase_name} (Short Size: ${short_size_usd:,.0f}) ---")
    
    # --- Configuration ---
    iterations_per_day = 1440
    attack_day = 5
    attack_iteration = attack_day * iterations_per_day
    attack_swap_amount = 500_000_000 
    
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

    volumes_daily_stablecoin = [547686207.2, 566644084.6, 574239250.7, 453049346.2, 612280606.5, 733858936.5, 649583067.2, 1335178681, 2025913193, 2809970941]
    volumes_daily_collateral = [1712121334, 1788318413, 1955818800, 1302497178, 1941974963, 2276428168, 2178573977, 3054299674, 5108105142, 6306976142]

    number_of_iterations = iterations_per_day * len(volumes_daily_collateral)
    
    volatility_array_stablecoin = calculate_volatility_array(volumes_daily_stablecoin, iterations_per_day)
    volatility_array_collateral = calculate_volatility_array(volumes_daily_collateral, iterations_per_day)

    cpf = ConstantProductFormula()

    stablecoin = AlgorithmicStablecoin(name="AS", peg=1.0, initial_price=stablecoin_initial_price, initial_supply=stablecoin_initial_supply, initial_free_supply=stablecoin_initial_free_supply)
    collateral = CollateralToken(name="CT", initial_price=collateral_initial_price, initial_supply=collateral_initial_supply, initial_free_supply=collateral_initial_free_supply, algorithmic_stablecoin=stablecoin)
    reference = ReferenceToken(name="USD")

    stablecoin_pool_quantity = stablecoin_initial_supply - stablecoin_initial_free_supply
    stablecoin_pool_reference_quantity = stablecoin_pool_quantity * stablecoin_initial_price
    collateral_pool_quantity = collateral_initial_supply - collateral_initial_free_supply
    collateral_pool_reference_quantity = collateral_pool_quantity * collateral_initial_price

    stablecoin_pool = LiquidityPool(token_a=stablecoin, token_b=reference, quantity_token_a=stablecoin_pool_quantity, quantity_token_b=stablecoin_pool_reference_quantity, formula=cpf, fee=stablecoin_pool_fee)
    collateral_pool = LiquidityPool(token_a=collateral, token_b=reference, quantity_token_a=collateral_pool_quantity, quantity_token_b=collateral_pool_reference_quantity, formula=cpf, fee=collateral_pool_fee)
    virtual_pool = SimpleVirtualLiquidityPool(stablecoin=stablecoin, collateral=collateral, stablecoin_base_quantity=vlp_stablecoin_base_quantity, formula=cpf, fee=vlp_pool_fee, pool_recovery_period=int(pool_recovery_period))

    stablecoin_purchase_generator = SeignorageModelPurchaseGenerator(token=stablecoin, volatility=volatility_array_stablecoin, delta_variation=lambda x: 1 / x - 1, threshold=0.05, pool_fee=stablecoin_pool_fee)
    collateral_purchase_generator = SeignorageModelPurchaseGenerator(token=collateral, volatility=volatility_array_collateral, delta_variation=lambda x: 1 / x - 1, threshold=0.05, pool_fee=collateral_pool_fee)

    # --- Attacker Setup ---
    attacker_initial_wallet = {stablecoin: attack_swap_amount * 1.5, reference: 0.0}
    attacker = Attacker(initial_wallet=attacker_initial_wallet)
    
    simulation = ThreePoolsSimulation(stablecoin_token=stablecoin, collateral_token=collateral, reference_token=reference, stablecoin_pool=stablecoin_pool, collateral_pool=collateral_pool, virtual_pool=virtual_pool, stablecoin_purchase_generator=stablecoin_purchase_generator, collateral_purchase_generator=collateral_purchase_generator, number_of_iterations=number_of_iterations)
    
    simulation_data = {"stablecoin_price_history": [], "collateral_price_history": [], "attacker_pnl_history": []}
    initial_pnl = attacker.get_portfolio_value()
    
    # Run
    for iteration in tqdm(range(number_of_iterations), desc=f"Simulating {phase_name}", unit="iter"):
        if iteration == attack_iteration:
            if short_size_usd > 0:
                short_amount = short_size_usd / collateral.price
                attacker.open_short(collateral, short_amount)
            attacker.swap(stablecoin_pool, stablecoin, attack_swap_amount)

        simulation_data["stablecoin_price_history"].append(stablecoin.price)
        simulation_data["collateral_price_history"].append(collateral.price)
        simulation_data["attacker_pnl_history"].append(attacker.get_portfolio_value() - initial_pnl)
        
        simulation.market_simulator.execute_random_purchases()
        
        if iteration == number_of_iterations - 1:
             if short_size_usd > 0:
                 attacker.close_short(collateral)

    final_pnl = attacker.get_portfolio_value() - initial_pnl
    print(f"Final PnL: ${final_pnl:,.2f}")
    
    # Plotting
    output_dir = "simulation_results"
    os.makedirs(output_dir, exist_ok=True)
    
    plt.figure(figsize=(14, 18), dpi=100)
    plt.rcParams.update({'font.size': 12})
    
    # Stability
    plt.subplot(3, 1, 1)
    plt.plot(simulation_data["stablecoin_price_history"], label="Stablecoin (AS) Price", color="#1f77b4", linewidth=2)
    plt.axvline(x=attack_iteration, color='r', linestyle='--', label='Attack Start')
    plt.title(f"{phase_name}: Stablecoin Peg Stability", fontsize=16, fontweight='bold')
    plt.ylabel("Price ($)", fontsize=14)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.legend(loc='upper right')
    
    # Collateral
    plt.subplot(3, 1, 2)
    plt.plot(simulation_data["collateral_price_history"], label="Collateral (CT) Price", color="#ff7f0e", linewidth=2)
    plt.axvline(x=attack_iteration, color='r', linestyle='--', label='Attack Start')
    plt.title(f"{phase_name}: Collateral Token Price", fontsize=16, fontweight='bold')
    plt.ylabel("Price ($)", fontsize=14)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.legend(loc='upper right')
    
    # PnL
    plt.subplot(3, 1, 3)
    plt.axhline(y=0, color='black', linewidth=1, linestyle='-')
    plt.plot(simulation_data["attacker_pnl_history"], label="Attacker Cumulative PnL", color="#2ca02c", linewidth=2)
    plt.axvline(x=attack_iteration, color='r', linestyle='--', label='Attack Start')
    plt.title(f"{phase_name}: Attacker Profit/Loss (Final: ${final_pnl:,.0f})", fontsize=16, fontweight='bold')
    plt.ylabel("PnL ($)", fontsize=14)
    current_values = plt.gca().get_yticks()
    
    # Safety check for empty or zero ticks to avoid warnings
    if len(current_values) > 0:
         plt.gca().set_yticklabels(['${:,.0f}M'.format(x/1e6) for x in current_values])

    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.legend(loc='upper left')

    plt.tight_layout(pad=3.0)
    plt.savefig(os.path.join(output_dir, output_filename), bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    # Phase 1: Raw Dump (No Short)
    run_phase_simulation("Phase 1 (Raw Dump)", 0, "phase1_results.png")
    
    # Phase 2: Soros Strategy ($300M Short)
    run_phase_simulation("Phase 2 (Soros Strategy)", 300_000_000, "phase2_results.png")
    
    # Phase 3: High Leverage ($1B Short)
    run_phase_simulation("Phase 3 (High Leverage)", 1_000_000_000, "phase3_results.png")
