# Algo-Attack-Model

This repository contains the simulation model used to analyze algorithmic stablecoin attacks.

## Fork Origin
This codebase is a fork of the **DualTokenSim** project, originally designed to simulate dual-token algorithmic stablecoin systems (Stablecoin + Volatile Collateral).

## What Was Added
We have extended the simulation to support **detailed single-trace analysis** of attack scenarios, specifically focusing on the Terra/Luna style death spiral.

### New Features & Scripts
1.  **Attacker Portfolio Tracking**:
    *   Modified `source/simulations/three_pools_simulation.py` to track the `attacker_portfolio_history` at every iteration step.
    *   Allows for precise calculation of PnL and ROI over time, not just at the start and end.

2.  **Single Attack Visualization Script** (`run_single_attack_visuals.py`):
    *   A dedicated runner script that executes a specific attack scenario (e.g., Day 10 Attack, $500M Swap, 2M Short).
    *   **Generates Plots**:
        *   `collateral_collapse_subplots.png`: Visualizes the simultaneous price crash and supply hyperinflation.
        *   `stablecoin_price_depeg.png`: Tracks the stablecoin's loss of peg ($1.00 -> $0.00).
        *   `attacker_portfolio_history.png`: Tracks the attacker's equity growth during the crash.
    *   **PnL Reporting**: Automatically calculates and prints specific Net Profit and ROI figures for the single run.

3.  **Simulation Results**:
    *   New directory `simulation_results/single_attack/` storing the generated artifacts.

## What Was NOT Changed
The core economic primitives and simulation logic remain identical to the original DualTokenSim to ensure validity:

*   **AMM Logic**: `ConstantProductFormula` (x*y=k) remains untouched.
*   **Liquidity Pools**: The mechanism for `LiquidityPool` and `VirtualLiquidityPool` (VLP) is unchanged.
*   **Arbitrage Logic**: The internal arbitrageur (`ThreePoolsArbitrageOptimizer`) still functions exactly as defined in the original paper.
*   **Purchase Generators**: The stochastic market noise (`SeignorageModelPurchaseGenerator`) uses the original volatility models.
*   **Original Runners**: Scripts like `run_attack_simulation.py` (used for sensitivity analysis heatmaps) were kept intact to allow for cross-validation.
