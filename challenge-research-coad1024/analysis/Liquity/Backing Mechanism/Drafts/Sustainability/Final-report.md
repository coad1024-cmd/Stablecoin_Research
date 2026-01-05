# Liquity (LUSD) — Decentralization & Risk Analysis

## Executive Summary

Liquity (LUSD) represents the "purist" approach to decentralized stablecoins: governance-free, immutable, and mathematically rigid. Unlike MakerDAO's "hybrid" model (decentralized tech, centralized assets), Liquity achieves **full decentralization** at the cost of capital efficiency and flexibility.

---

# 1. Analysis

## A. Backing Mechanism

Liquity uses a unique "Trove" system with **ETH as the sole collateral** (in V1).

* **Minimum Collateral Ratio (MCR)**: 110%. This is significantly lower than MakerDAO's 130-150%, enabled by instant, algorithmic liquidations.
* **Stability Pool**: Instead of auctions, Liquity uses a pool of LUSD deposited by users to instantly absorb debt from liquidated Troves.
* **Redemption**: A hard price floor. Any user can redeem 1 LUSD for $1 of ETH (minus fees) at any time. This creates a direct arbitrage loop that prevents LUSD from trading significantly below $1.
* **Recovery Mode**: If the Total Collateral Ratio (TCR) falls below 150%, the system aggressively liquidates risky Troves (up to 150% CR) to restore solvency.

## B. Sustainability

Liquity operates on a **one-time fee** model rather than continuous interest rates (V1).

* **Revenue**: Generated from Borrowing Fees (0.5% - 5%) and Redemption Fees.
* **LQTY Token**: Captures 100% of protocol revenue. Stakers earn LUSD and ETH. This aligns incentives without needing governance to manage a treasury.
* **Long-term Viability**: The lack of interest rates makes LUSD attractive for long-term leverage but less flexible for monetary policy. V2 introduces user-set interest rates to address this.

## C. Decentralization

Liquity is arguably the most decentralized stablecoin in existence.

* **Immutable Contracts**: No admin keys. No governance voting. The rules are set in stone.
* **Frontend Operators**: Liquity has no official frontend. It relies on a network of third-party operators (incentivized by LQTY) to host web interfaces. This makes the protocol censorship-resistant at the access layer.
* **Oracle**: Relies on Chainlink (primary) and Tellor (fallback). This is the main external dependency.

---

# 2. Design

## A. Ideal Stablecoin (No Liquidation Risk)

**Concept: "The Yield-Bearing Wrapper"**
In a world where collateral cannot lose value, the focus shifts to efficiency.

* **Mechanism**: 1:1 Minting. Protocol holds the asset.
* **Yield**: The protocol stakes/lends the underlying asset and distributes 100% of yield to stablecoin holders.
* **Result**: A "Savings Stablecoin" that appreciates in value or pays dividends, with zero solvency risk.

## B. Stablecoin with Highly Risky Collateral

**Concept: "The Fortress Protocol"**
In a world of high volatility, the system must be paranoid.

* **Hyper-Overcollateralization**: 500% MCR.
* **Tranche System**:
  * **Senior Token ($1 Peg)**: Protected by Junior capital.
  * **Junior Token (Leverage)**: Absorbs first 50% of losses.
* **Circuit Breakers**: Minting pauses during high volatility; Redemptions stay open.
* **Protocol-Owned Insurance**: 50% of fees go to a permanent insurance fund.

---

# 3. Modelling: De-Peg Attack Feasibility

**Scenario**: An attacker attempts to force LUSD to trade at **$0.90** (breaking the peg) by selling massive amounts of LUSD.

**Defense**: The Redemption Mechanism allows arbitrageurs to buy LUSD at $0.90 and redeem it for $1 of ETH.

### Simulation Results

We simulated a 48-hour attack where the attacker sells enough LUSD to keep the price at $0.90.

* **Attacker Strategy**: Sell LUSD whenever Price > $0.90.
* **System Response**: Arbitrageurs buy LUSD and redeem. This increases the **Base Rate** (Redemption Fee).
* **Outcome**:
  * **Total LUSD Redeemed**: ~68 Million
  * **Attacker Cost**: ~$6.8 Million (Loss from selling at discount)
  * **Base Rate**: Spikes to ~9.4%

### Cost vs. Profit

* **Cost**: The attacker loses ~$0.10 for every dollar sold.
* **Profit**: To profit, the attacker needs a short position. However, since the Redemption mechanism acts as a "black hole" for cheap LUSD, the price is unlikely to stay low unless the attacker drains the entire system's liquidity or pushes the fee to 100%.
* **Conclusion**: The attack is **economically infeasible** for profit. The cost to suppress the price is directly proportional to the volume, and the Redemption mechanism ensures that for every dollar sold, the attacker subsidizes an arbitrageur.

![De-Peg Simulation Plot](modelling/depeg_simulation_plot.png)

---

# Summary Scorecard

| Dimension | Score | Summary |
| :--- | :--- | :--- |
| **Backing** | **5/5** | Pristine ETH collateral. 110% MCR is efficient yet safe. |
| **Sustainability** | **4/5** | Fee model is robust, though lack of interest rates (V1) limits policy tools. |
| **Decentralization** | **5/5** | Gold standard. Immutable, governance-free, decentralized frontends. |
| **Overall** | **4.7/5** | The most resilient decentralized stablecoin, trading flexibility for security. |
