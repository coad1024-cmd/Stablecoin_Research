# Model Explainer Outline: Algo-Attack-Model Deep Dive

## 1. Introduction (The What)

* **Definition**: The Algo-Attack Model is a specialized simulation framework built on top of `DualTokenSim`.
* **Core Purpose**: To model, execute, and analyze a "Death Spiral" de-pegging event on a dual-token algorithmic stablecoin (modeled after Terra/Luna).
* **Objective**: To move beyond theoretical risk to quantifiable economic analysis, specifically focusing on the feasibility and profitability of a deliberate attack.

## 2. The "Why": Motivation & Significance

* **The Fragility of Algos**: Contextualize the writeup within existing research (MakerDAO/Liquity are over-collateralized; this model explores under-collateralized/algorithmic risks).
* **The Soros Attack Vector**: Why modeling "bad actors" is crucial for security. It’s not just about the protocol breaking; it's about *incentivizing* it to break.
* **Educational & Research Value**: Providing a sandbox for Senior Solidity Devs and Researchers to visualize the feedback loops between Stablecoin Peg, Collateral Supply, and Price.

## 3. The "How": System Mechanics & Architecture

### A. The Environment (`DualTokenSim`)

* **Market Structure**:
  * 3 Liquidity Pools: Stable/Ref (USD), Collat/Ref (USD), Stable/Collat.
  * **Agents**:
    * **Arbitrageurs**: The "keepers" trying to close price gaps.
    * **Random Traders**: Providing noise and liquidity.
    * **Virtual Liquidity Pool**: Managing the mint/burn dynamics.

### B. The Malicious Actor (`Attacker` Class)

* **Design**: A new agent introduced specifically for this research.
* **Capabilities**:
  * **Wallet**: Holds initial capital (Stablecoins, Reference tokens).
  * **Swap**: Can execute massive dumps to shock the pool.
  * **Short Selling**: The critical addition. The ability to `open_short` on the Collateral Token.
  * **PnL Tracking**: Real-time calculation of Portfolio Value (Assets + Unrealized Short PnL).

### C. The Attack Anatomy (Step-by-Step)

1. **Preparation**: Attacker accumulates a significant position (e.g., 500M Stablecoins) and opens short positions on the Collateral Token.
2. **The Trigger (Day 10)**: The Attacker executes a massive `swap` (Dump) of Stablecoins into the Liquidity Pool.
3. **The Propagation (The Death Spiral)**:
    * Stablecoin Price dumps (< $1.00).
    * Arbitrageurs buy cheap Stablecoin and redeem it for Collateral.
    * **Minting Flood**: The protocol mints new Collateral to honor redemptions.
    * **Hyper-Inflation**: Collateral supply explodes -> Price crashes.
4. **The Payoff**: The Attacker closes their Collateral shorts at near-zero prices, generating massive profit that outweighs the loss from dumping the Stablecoin.

## 4. Key Insights & Data

* **Leverage is the Multiplier**: Discussing the finding that a simple dump is often net-negative for the attacker without the short position.
* **Metrics**:
  * Stablecoin Price deviation.
  * Collateral Price crash curve.
  * Attacker PnL (Profit and Loss).

## 5. Conclusion

* Summary of the model's utility.
* Final thoughts on designing "Anti-Fragile" stablecoins.
