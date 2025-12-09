# Stablecoin Research: Analysis, Design, and Modelling

## 1. Analysis (Status: 2/3 Complete)

### Objective

Compare 3 of the most relevant stablecoins: **MakerDAO (DAI)**, **Liquity V2 (BOLD)**, and **Terra (UST)**.

### Comparison Matrix

| Feature | MakerDAO (DAI/USDS) | Liquity V2 (BOLD) | Terra (UST) [PENDING] |
| :--- | :--- | :--- | :--- |
| **Backing Type** | **Hybrid RWA** | **Crypto-Native** | *Algorithmic (Seigniorage)* |
| **Sustainability** | **Volume Business** | **Spread Business** | *Ponzi / Subsidy* |
| **Decentralization** | **Pragmatic** (Delegated) | **Purist** (Immutable) | *Validator Heavy* |

### Deep Dive

#### A. MakerDAO (Completed)

* **Backing**: Transitioned to Hybrid RWA to scale. T-Bills provide 60% of revenue.
* **Sustainability**: "Cost of Carry" model. Profitable but relies on active management of DSR vs Asset Yield. (See `analysis/makerdao/Sustainability`).
* **Decentralization**: Low Nakamoto (Delegates). High Gini.

#### B. Liquity V2 (Completed)

* **Backing**: Pure Crypto (ETH/LSTs). No RWA.
* **Sustainability**: User-set rates create organic equilibrium. Immune to "Stagflation". (See `analysis/Liquity`).
* **Decentralization**: High (~0.3 Gini). Governance-free.

#### C. Terra / UST (Next Up)

* **Status**: Analysis Pending.
* **Focus**: Post-mortem of the interaction between Anchor Protocol yields and LUNA burn mechanism.

---

## 2. Design (Status: 1/2 Complete)

### A. Environment without Liquidation Risk (Completed)

* **Constraint**: Collateral cannot lose value.
* **Proposal**: **"Unity" (1:1 Wrapper)**.
  * **Mechanism**: If assets are essentially risk-free (e.g., Tokenized Gold in a stable world), 1:1 backing is optimal. No need for over-collateralization or auctions. Capital efficiency = 100%.

### B. Environment with Highly Risky Collateral (Pending)

* **Constraint**: All collateral is highly volatile.
* **Status**: Design Pending.
* **Direction**: Likely a "Tranche" system (Senior/Junior) to isolate volatility.

---

## 3. Modelling (Status: Complete)

### Scenario: Algo-Stablecoin De-Peg (Terra/UST)

* **Objective**: Model cost of attack vs profit.
* **Model**:
  * **Cost**: Slippage on Curve Dump + Short Fees ($300M).
  * **Profit**: Shorting LUNA + BTC ($1B+).
  * **Conclusion**: The attack was economically rational. When Collateral (Endogenous LUNA) market cap falls below Stablecoin Supply, the system is mathematically insolvent.
* **Code**: See `Algo-Attack-Model` directory.
