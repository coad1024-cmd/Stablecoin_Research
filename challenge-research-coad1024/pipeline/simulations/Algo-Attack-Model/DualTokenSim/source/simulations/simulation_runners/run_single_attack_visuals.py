
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

def calculate_volatility_array(volumes_daily, total_iterations_per_day, sqrt_2_pi=0.7979):
    volume_values_daily = [volume / total_iterations_per_day for volume in volumes_daily]
    volume_array = np.repeat(volume_values_daily, total_iterations_per_day)
    volatility_array = volume_array / sqrt_2_pi
    return volatility_array.tolist()

def run_visual_attack_simulation():
    # --- Configuration ---
    iterations_per_day = 14400 
    
    # Attack Parameters for Visuals (Fixed specific scenario)
    attack_day = 10
    attack_swap_amount = 500_000_000 # 500M USD Dump
    short_amount_collateral = 2_000_000 # 2M Tokens Short
    
    attack_iteration = attack_day * iterations_per_day

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

    # Reduced volume data for simulation
    volumes_daily_stablecoin = [
        547686207.2, 566644084.6, 574239250.7, 453049346.2, 612280606.5, 733858936.5,
        649583067.2, 1335178681, 2025913193, 2809970941, 4905955011, 7679819164,
        9392162783, 1285921756, 376460753.5, 335182961.8, 389081589.1, 264405278.3,
        173247622.4, 102877376.6
    ]
    volumes_daily_collateral = [
        1712121334, 1788318413, 1955818800, 1302497178, 1941974963, 2276428168,
        2178573977, 3054299674, 5108105142, 6306976142, 10452679386, 11564567908,
        15924391896, 1900824923, 8213042862, 4009983321, 3319818663, 1530284129,
        872930871.1, 645836243.7
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
    
    attacker.open_short(collateral, short_amount_collateral)

    simulation = ThreePoolsSimulation(stablecoin_token=stablecoin,
                                      collateral_token=collateral,
                                      reference_token=reference,
                                      stablecoin_pool=stablecoin_pool,
                                      collateral_pool=collateral_pool,
                                      virtual_pool=virtual_pool,
                                      stablecoin_purchase_generator=stablecoin_purchase_generator,
                                      collateral_purchase_generator=collateral_purchase_generator,
                                      number_of_iterations=number_of_iterations,
                                      attacker=attacker,
                                      attack_iteration=attack_iteration,
                                      attack_swap_amount=attack_swap_amount)

    print("Running Simulation for Plots...")
    results = simulation.run_simulation()
    
    # --- Plotting ---
    output_dir = "simulation_results/single_attack"
    os.makedirs(output_dir, exist_ok=True)
    
    iterations = range(len(results["stablecoin_price_history"]))
    
    # 1. Collateral Price and Supply Collapse (Subplots)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)
    
    # Price
    ax1.plot(iterations, results["collateral_price_history"], color='orange', label='Collateral Price')
    ax1.axvline(x=attack_iteration, color='red', linestyle='--', label='Attack Start')
    ax1.set_ylabel('Price (USD)')
    ax1.set_title('Collateral Price Collapse')
    ax1.legend()
    ax1.grid(True)
    
    # Supply
    ax2.plot(iterations, results["collateral_supply_history"], color='brown', label='Collateral Supply')
    ax2.axvline(x=attack_iteration, color='red', linestyle='--', label='Attack Start')
    ax2.set_xlabel('Iterations')
    ax2.set_ylabel('Supply (Tokens)')
    ax2.set_title('Collateral Supply Inflation')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "collateral_collapse_subplots.png"))
    plt.close()
    
    # 2. Stablecoin Price over time
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, results["stablecoin_price_history"], color='blue', label='Stablecoin Price')
    plt.axvline(x=attack_iteration, color='red', linestyle='--', label='Attack Start')
    plt.title('Stablecoin Price De-peg')
    plt.xlabel('Iterations')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "stablecoin_price_depeg.png"))
    plt.close()

    # 3. Attacker Portfolio Value over time
    # Check if portfolio history exists (it should with our modification)
    if "attacker_portfolio_history" in results and results["attacker_portfolio_history"]:
        plt.figure(figsize=(10, 6))
        plt.plot(iterations, results["attacker_portfolio_history"], color='green', label='Attacker Portfolio Value')
        plt.axvline(x=attack_iteration, color='red', linestyle='--', label='Attack Start')
        plt.title('Attacker Portfolio Value Over Time')
        plt.xlabel('Iterations')
        plt.ylabel('Portfolio Value (USD)')
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(output_dir, "attacker_portfolio_history.png"))
        plt.close()
    else:
        print("Warning: Attacker portfolio history not found in results.")

    print(f"Plots saved to {os.path.abspath(output_dir)}")
    
    # --- Print Metrics for User ---
    # --- Print Metrics for User ---
    
    if "attacker_portfolio_history" in results and results["attacker_portfolio_history"]:
        initial_val = results["attacker_portfolio_history"][0]
        final_val = results["attacker_portfolio_history"][-1]
        pnl = results["attacker_pnl"]
        roi = (pnl / initial_val) * 100 if initial_val != 0 else 0
        
        print("\n" + "="*40)
        print(f"ATTACK RESULTS (Single Run - Day {attack_day})")
        print(f"{'='*40}")
        print(f"Initial Portfolio Value: ${initial_val:,.2f}")
        print(f"Final Portfolio Value:   ${final_val:,.2f}")
        print(f"Net Profit/Loss (PnL):   ${pnl:,.2f}")
        print(f"Return on Investment:    {roi:.2f}%")
        print("="*40 + "\n")

if __name__ == "__main__":
    run_visual_attack_simulation()
