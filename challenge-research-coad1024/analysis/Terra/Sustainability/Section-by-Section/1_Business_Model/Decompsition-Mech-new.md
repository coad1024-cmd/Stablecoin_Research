# 1. Business Model Decomposition

> [!WARNING]
> **Methodological Note: Simulation Data**
> The analysis below utilizes **synthetic, stylized time-series data** constructed to match public magnitudes (e.g., ~$18B peak UST, ~$40B LUNA Mcap). It is intended as a **Stress Test / Sufficiency Proof** of the mechanic, not a precise historical forensic reconstruction. All specific dates and dollar amounts should be treated as model inputs for sensitivity analysis, not observed market events.

## Overview

The Terra protocol operated as a **reflexive monetary system** with two tightly coupled policy functions:

1.  **Monetary stabilization:** Maintaining the price stability of UST through on-chain convertibility with LUNA.
2.  **Demand subsidization:** Stimulating sustained demand for UST through externally funded yield incentives, primarily via the Anchor Protocol.

Unlike collateralized stablecoins or traditional banking systems, Terra did not rely on exogenous assets held in reserve to back its liabilities. Instead, UST stability depended on the **endogenous market value of LUNA**.

![Balance Sheet Diagram](file:///home/hash/Projects/Research%20Challenge/challenge-research-coad1024/analysis/Terra/Sustainability/Diagrams/1_Balance_Sheet.mmd)

---

## 2. Economic Structure and Implied Balance Sheet

### 2.1 UST Supply (Protocol Liabilities)

At its peak, UST supply reached approximately **$18.7 billion**. UST functioned as a **demand liability** with zero duration and no senior claim on assets. Its backing was purely operational defined by the mint/burn liquidity.

![UST Supply Empirical](../diagrams/fig_ust_supply_empirical.svg)
> **Figure 2.1:** Empirical UST Supply History (Jan 2021 - May 2022). Shows the exponential liability growth followed by total collapse. Data Source: DefiLlama.


### 2.2 Absorber Capacity: LUNA

**LUNA acted as the system’s volatility absorber**. At peak, LUNA's market cap exceeded **$40 billion**. However, this coverage was endogenous.

![LUNA Absorber Empirical](../diagrams/fig_luna_absorber.svg)
> **Figure 2.2:** Empirical LUNA Absorber Capacity. The blue line represents the raw market cap (Price × Supply). The red dashed line represents the modeled "Safe Capacity" (Haircut). Data Source: CryptoCompare (Price) + Terra Station (Supply).


#### Model Analysis: The Stressed Absorber
When applying a **30% liquidity haircut** (simulating panic conditions) to a modeled collapse trajectory, the system exhibits signs of structural weakness long before the terminal event.

![Liabilities vs Absorber](file:///home/hash/Projects/Research%20Challenge/challenge-research-coad1024/analysis/Terra/Sustainability/Section-by-Section/1_Business_Model/scripts/fig1_liabilities_vs_absorber.svg)

> **Simulation Result**: The model demonstrates that under a 30% liquidity stress assumption, the **Stressed Absorber Capacity** drops below liability levels (Ratio < 1.0) rapidly once the contraction regime begins. In our stylized 7-day collapse model, this occurs on Day 1, implying **instant structural insolvency** once confidence breaks.

### 2.3 Exogenous Reserves (The Illusion)

The Luna Foundation Guard (LFG) accumulated ~$3B in Bitcoin to serve as a backstop.

![Reserve Coverage](../diagrams/fig_lfg_reserves_empirical.svg)


> **Sufficiency Proof**: Even assuming peak reserves of ~$3B against ~$18B liabilities, the **Exogenous Coverage Ratio** maxes out at **~16%**. This confirms mechanically that reserves were insufficient to halt a full bank run without assuming massive LUNA absorption.

---

## 3. The Cash Flow Engine (Anchor Protocol)

The system's growth was driven by the Anchor Protocol, which promised ~20% APY on UST deposits.

![Cash Flow Diagram](file:///home/hash/Projects/Research%20Challenge/challenge-research-coad1024/analysis/Terra/Sustainability/Diagrams/2_Cash_Flow_Engine.mmd)

### 3.1 Structural Imbalance
The demand for 20% yield (Deposits) vastly outpaced the demand for 12% loans (Borrows).

![Anchor Imbalance](../diagrams/fig_anchor_imbalance_empirical.svg)


This created a massive quantity of **Unproductive Capital**—liabilities that generated expense but no revenue.

---

## 4. Cost Structure & Negative Carry

The defining characteristic of Terra’s business model was a **persistent negative carry**.

$$ \text{NIM} = \text{Yield}_{\text{Assets}} - \text{Cost}_{\text{Liabilities}} $$

With widely divergent rates (12% Earned vs 20% Paid) and volume (3B Assets vs 14B Liabilities), the deficit was structural.

![Cumulative Subsidy](../diagrams/fig_cumulative_subsidy_empirical.svg)


> **Model Implication**: For a system with these parameters (15% net spread on $10B+ assets), the **Cumulative Subsidy Bill** grows linearly. The model indicates a theoretical burn rate of **~$1B per year**, which would inevitably deplete any finite yield reserve.

---

## 5. Reflexivity and Sustainability

Terra’s model did not fail due to a "bank run" in the traditional sense. It failed because its solvency was a function of its own growth rate.

![Reflexivity Loop](file:///home/hash/Projects/Research%20Challenge/challenge-research-coad1024/analysis/Terra/Sustainability/Diagrams/3_Reflexivity_Loop.mmd)

Once the **Expected Subsidy** (Yield) could no longer be financed by **Endogenous Appreciation** (LUNA price), the loop inverted. The same mechanism that printed billions in value during expansion printed trillions in supply during contraction.

### Conclusion regarding Business Model
*   **Solvency**: Relied on >1.0 Absorber Ratio (failed under stress).
*   **Liquidity**: Relied on CEX order books (insufficient for $18B exit).
*   **Revenue**: Structural negative carry (consumes equity).
*   **Backing**: Exogenous reserves were mathematically insufficient (<20% coverage).

The business model was effectively **equity-funded yield arbitrage**. It worked only as long as Equity Value Growth > Yield Expense.
