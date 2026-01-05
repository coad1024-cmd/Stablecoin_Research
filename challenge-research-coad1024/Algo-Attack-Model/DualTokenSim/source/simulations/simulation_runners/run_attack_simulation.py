import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import pandas as pd # New import for data handling
import seaborn as sns # New import for visualization

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

def run_single_attack_simulation(attack_day, attack_swap_amount, short_amount_collateral):
    try:
        # --- Configuration ---
        iterations_per_day = 14400 
        
        # --- Attack Parameters ---
        attack_iteration = attack_day * iterations_per_day
        # attack_swap_amount is passed as argument
        # short_amount_collateral is passed as argument

        stablecoin_initial_price = 1.0 # Pegged initially
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

        # Reduced volume data for faster but representative simulation (first 20 days)
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
        
        # Attacker opens a short position on the collateral token before the attack
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

        # print("Running Simulation...") # Removed for cleaner output during sensitivity analysis
        results = simulation.run_simulation()
        
        # --- Analysis ---
        # Attacker closes the short position after the attack
        short_pnl = attacker.close_short(collateral)

        final_pnl = results["attacker_pnl"] + short_pnl
        
        # --- Plotting --- # Removed for sensitivity analysis, will plot aggregated results
        # output_dir = "simulation_results"
        # os.makedirs(output_dir, exist_ok=True)
        # plt.figure(figsize=(12, 6))
        # ... (plotting code) ...
        # plt.savefig(os.path.join(output_dir, "attack_simulation_metrics.png"))
        
        return final_pnl

    except Exception as e:
        # print(f"Error in simulation run: {e}") # Keep errors for debugging
        # import traceback
        # traceback.print_exc()
        return np.nan # Return NaN for failed simulations


if __name__ == "__main__":
    # --- Sensitivity Analysis Parameters ---
    short_amounts = [1_000_000, 2_000_000, 3_000_000] # Example short amounts for collateral token
    swap_amounts = [300_000_000, 500_000_000, 700_000_000] # Example stablecoin dump amounts
    attack_days = [5, 10, 15] # Example attack days

    # --- Results File ---
    output_dir = "sensitivity_analysis_results"
    os.makedirs(output_dir, exist_ok=True)
    results_file = os.path.join(output_dir, "pnl_results.npy")

    # --- Load or Initialize Results ---
    if os.path.exists(results_file):
        print(f"Loading existing results from {results_file}")
        pnl_results = np.load(results_file)
    else:
        print("Initializing new results array.")
        pnl_results = np.zeros((len(short_amounts), len(swap_amounts), len(attack_days)))

    print("Starting Sensitivity Analysis...")
    # --- Run Simulations ---
    for i, short_amount in enumerate(short_amounts):
        for j, swap_amount in enumerate(swap_amounts):
            for k, attack_day in enumerate(attack_days):
                # Check if this simulation has already been run
                if pnl_results[i, j, k] != 0:
                    print(f"Skipping simulation for: Short={short_amount}, Swap={swap_amount}, Day={attack_day} (already run)")
                    continue

                print(f"Running simulation for: Short={short_amount}, Swap={swap_amount}, Day={attack_day}")
                pnl = run_single_attack_simulation(attack_day, swap_amount, short_amount)
                pnl_results[i, j, k] = pnl

                # Save results after each simulation
                np.save(results_file, pnl_results)
                print(f"Saved intermediate results to {results_file}")

    print("\nSensitivity Analysis Complete. Results:")
    print(pnl_results)

    # --- Visualization ---
    # Plotting heatmap for PnL vs Short Amount and Swap Amount (averaged over attack days)
    avg_pnl_over_days = np.nanmean(pnl_results, axis=2) # Average PnL across different attack days

    plt.figure(figsize=(10, 8))
    plt.imshow(avg_pnl_over_days, cmap='viridis', origin='lower',
               extent=[swap_amounts[0], swap_amounts[-1], short_amounts[0], short_amounts[-1]],
               aspect='auto')
    plt.colorbar(label='Attacker PnL (USD)')
    plt.xlabel('Stablecoin Dump Amount (USD)')
    plt.ylabel('Collateral Short Amount (Tokens)')
    plt.title('Attacker PnL (Avg. over Attack Days) vs. Attack Parameters')
    plt.xticks(swap_amounts, [f'{s/1e6:.0f}M' for s in swap_amounts])
    plt.yticks(short_amounts, [f'{s/1e6:.0f}M' for s in short_amounts])
    plt.grid(True, which="both", color="w", linestyle="-", linewidth=0.5)
    plt.savefig(os.path.join(output_dir, "pnl_heatmap_short_swap.png"))
    plt.show()

    # Further plots could be generated, e.g., PnL vs Attack Day for specific short/swap amounts

    # --- 3D Surface Plot ---
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Create a meshgrid for the X and Y axes
    X, Y = np.meshgrid(swap_amounts, short_amounts)

    # Plot the surface
    ax.plot_surface(X, Y, avg_pnl_over_days, cmap='viridis')

    ax.set_xlabel('Stablecoin Dump Amount (USD)')
    ax.set_ylabel('Collateral Short Amount (Tokens)')
    ax.set_zlabel('Attacker PnL (USD)')
    ax.set_title('Attacker PnL vs. Attack Parameters')

    # Format ticks
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x/1e6:.0f}M'))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y/1e6:.0f}M'))
    ax.zaxis.set_major_formatter(plt.FuncFormatter(lambda z, _: f'{z/1e6:.0f}M'))

    plt.savefig(os.path.join(output_dir, "pnl_3d_surface.png"))
    plt.show()

    print(f"Sensitivity analysis plots saved to {os.path.abspath(output_dir)}")
