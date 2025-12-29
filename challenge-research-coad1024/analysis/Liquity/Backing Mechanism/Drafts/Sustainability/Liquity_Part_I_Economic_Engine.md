
# Liquity Sustainability Analysis - Part I: The Economic Engine

**Last Updated:** December 8, 2024
**Protocol Version:** Liquity V2 (BOLD) & V1 (LUSD)
**Framework:** Sustainability Requirement (Pillar I)

---

## 1. Business Model Decomposition

Liquity operates as a **Credit Facility**, issuing debt (LUSD/BOLD) against collateral (ETH/LSTs). Its business model has evolved significantly from V1 to V2 to address the "Zero Interest Rate Policy" (ZIRP) era's end.

### 1.1 The Pivot: From "One-Time Fee" to "Continuous Revenue"

| Feature | Liquity V1 (LUSD) | Liquity V2 (BOLD) | Impact on Sustainability |
| :--- | :--- | :--- | :--- |
| **Pricing Model** | **One-time Issuance Fee** (0.5% - 5%) + 0% Interest | **User-Set Interest Rates** (0.5% - 250%) | **V2 is Sustainable.** V1's revenue is event-driven (minting/redemption), making it essentially "long duration" revenue recognized upfront. V2 generates continuous cash flow. |
| **Revenue Usage** | 100% to Staking Contract (LQTY Stakers) | **75% to Stability Pool / 25% to Liquidity Incentives** | V2 is "Self-Sustaining." It uses revenue to buy its own liquidity (PIL), reducing reliance on inflationary token emissions. |
| **Collateral** | ETH Only (Immutable) | ETH + LSTs (wstETH, rETH) | Diversification reduces single-asset correlation risk but introduces smart contract risk. |

### 1.2 Revenue Streams (The Inflow)

#### A. Interest Revenue (The V2 Engine)

In V2, the core revenue driver is the **User-Set Interest Rate**.

* **Mechanism:** Borrowers set their own rate to avoid redemptions.
* **Flow:**
  * $\approx 75\%$ flows to **Stability Pool Depositors** (Real Yield).
  * $\approx 25\%$ flows to **Protocol Incentivized Liquidity (PIL)** (Growth).
* **Sustainability Verdict:** This aligns strict liability matching. The cost of liability (yield to BOLD holders) is directly funded by the asset yield (borrower interest).

#### B. Premature Adjustment Fees

* **Description:** A penalty charged if a borrower adjusts their interest rate more frequently than every 7 days.
* **Amount:** Equivalent to 7 days of interest.
* **Purpose:** Prevents "front-running" redemptions (adjusting rate up just before a redemption tick and down immediately after).

#### C. Liquidation Penalties (Failure Revenue)

* **V2 Penalty:** 5% of collateral.
* **Distribution:**
  * Offset against burnt debt (Stability Pool).
  * Remaining collateral claimed by the borrower (unlike V1 where it was redistributed).
  * *Note:* Redistribution only happens if SP is empty.

### 1.3 Cost Structure (The Outflow)

#### A. The Cost of Liabilities (Peg maintenance)

* **V1 Cost:** 0% (LUSD pays no yield).
  * *Hidden Cost:* Opportunity cost. In high-rate environments, LUSD breaks downward because holding it costs 5% (vs owning T-Bills).
* **V2 Cost:** Variable Yield (Paid to BOLD holders).
  * *Correction:* V2 fixes V1's flaw by passing interest revenue to holders, ensuring $Demand_{BOLD}$ exists even when rates are high.

#### B. Incentive Emissions (LQTY)

* **V1:** Heavy reliance on LQTY emissions to incentivize the Stability Pool.
* **V2:** Moves towards **Protocol Incentivized Liquidity (PIL)**. By using 25% of *real revenue* to bribe liquidity gauges (Curve/Uniswap), Liquity V2 reduces dependency on printing LQTY. This is the **"Real Yield"** shift.

---

## 2. Key Metrics & Health Indicators

To assess the long-term viability, we track these distinct metrics.

### 2.1 Net Interest Margin (NIM) Proxy

For V2, we define NIM as the spread between Borrower Rates and Liquidity Costs.

$$
NIM_{V2} = Rate_{Borrower} - (Yield_{StabilityPool} + Cost_{LiquidityBribes})
$$

* **Positive Flywheel:** If $Rate_{Borrower}$ increases, $Yield_{SP}$ increases, attracting more BOLD depositors -> Deeper Liquidity -> Safer Peg.

### 2.2 The "Cost of Goods Sold" (COGS)

* **V1 COGS:** Zero marginal cost to mint, but high "Security Cost" (paid in equity/LQTY dilution).
* **V2 COGS:** The "Revenue Share." The protocol gives up 100% of its interest revenue (75% to users, 25% to liquidity). It retains **0%** for a treasury.
  * *Risk:* Liquity has no "Retained Earnings." It is a pass-through entity. It builds no war chest for black swan insurance beyond the Stability Pool.

### 2.3 Surplus Buffer

* **MakerDAO:** Holds a surplus buffer (DAI in treasury) to absorb bad debt.
* **Liquity (V1 & V2):** **Buffer = 0.**
  * *Mechanism:* Bad debt is socialized immediately via the Stability Pool or Redistribution. There is no protocol equity to burn first.
  * *Implication:* Total efficiency, but total user socialization of risk.

---

## 3. Preliminary Conclusion (Part I)

Liquity V2 represents a massive leap in **Economic Sustainability** over V1. By switching from a one-time fee model (which fails in high-rate environments) to a continuous interest rate model, it creates a **perpetual revenue engine**.

However, its **"Pass-Through"** nature (distributing 100% of revenue) means it does not build a sovereign treasury. Its survival depends entirely on the game-theoretic balance of its users, not on a balance sheet of accumulated profits.
