# Business Model Decomposition

**Goal**: Analyze Liquity V2 not just as a protocol, but as a business. This document dissects the Economic Engine: Revenue, Costs, Liabilities, and Constraints.

---

## 1. Business Model Design Constraints (The "Upper Bound")

Before analyzing revenue variables, we must define the hard limits imposed by the protocol's design. These constraints strictly cap Liquity V2's revenue potential compared to competitors, defining the "upper bound" of its profitability.

### A. No Rehypothecation (No Yield Capture)

* **Constraint**: Liquity *intentionally* does not capture the staking yield from LST collateral (wstETH, rETH). All yield flows directly to the user (the Trove owner).
* **Business Impact**: Unlike MakerDAO (which monetizes RWA yields) or Aave (which lends out collateral), Liquity’s revenue is strictly limited to borrower interest fees. It cannot monetize the asset side of its balance sheet.
* **Implication**: The "Revenue Ceiling" is significantly lower than protocols that can "double-dip" (charging borrow fees + earning collateral yield).

### B. Immutable Design (No Discretionary Policy)

* **Constraint**: Parameters (fees, rules, algorithm logic) are largely immutable or algorithmically determined. Governance cannot arbitrarily raise fees to capture more value during bull markets.
* **Business Impact**:
  * **No Risk Premium**: Cannot price-in specific asset risks manually.
  * **No Cyclical Pricing**: Cannot aggressively hike rates to maximize revenue during liquidity crunches beyond what the algorithm dictates.
  * **Competitive Rigidity**: Cannot quickly lower rates to undercut a new competitor without a full migration.

---

## 2. The Liability Structure: Demand for BOLD

A business model is Assets (Loans) vs. Liabilities (Stablecoins). We must understand why users hold the liability (BOLD) given its cost of capital.

### A. BOLD Holding Incentives vs. Opportunity Cost

* **No Savings Rate**: BOLD does **not** pay a native savings rate (SSR) to holders.
* **Opportunity Cost**: Holding BOLD implies a massive opportunity cost relative to:
  * **DAI**: Pays ~5-8% DSR.
  * **USDC**: Earns supply APY in Aave/Compound.
  * **USDe**: Earns delta-neutral funding yields.
* **Demand Drivers**: Who holds BOLD, and why?
  * **Redemption Arbitrageurs**: Buying BOLD < $1 to redeem for $1 of ETH.
  * **Liquidity Miners**: Earning LQTY or partner incentives.
  * **Stability Pool Depositors**: Seeking the 75% yield split from borrower interest.
  * **LPs**: Market makers in Curve/Uniswap pools (incentivized).

### B. Cost of Capital

* **Nominal Cost**: Near-zero (Protocol pays 0% interest directly to BOLD holders).
* **Implicit Cost**: The "cost" is the need to massive incentivize liquidity. If natural demand is low (due to no DSR), the protocol must spend heavily on **Liquidity Incentives** (LQTY emissions) to maintain deep peg liquidity.

---

## 3. Revenue Source: Borrower Interest Rates (The "Asset Side")

This is the primary (and almost exclusive) revenue driver. unlike V1's one-off fee, V2 introduces continuous, user-set interest rates.

### A. Core Mechanics

1. **User-Set Rates**: Users ($r_i$) set their own interest rates.
2. **Distribution**: Modeled as a Normal distribution $r \sim N(\mu, \sigma^2)$ centered around the external Base Rate ($\rho$).
3. **Incentive**: Users keep rates competitive to avoid being at the "bottom" of the redemption queue (lowest rates redeemed first).
4. **Weighted Average Rate**: $\text{AvgRate} = \frac{\sum (D_i \times r_i)}{D_{\text{total}}}$.

### B. Data & Verification

* **On-Chain**: `TroveManager` (per-trove rates), `ActivePool` (aggregates).
* **Simulation**: Chaos Labs CIR Model (simulating external base rate gravity).

#### Where to get it

* **On-chain data**: `TroveManager` contract (per-trove granularity), `ActivePool` (system-wide aggregates).
* **Tools**: Dune Analytics, Etherscan.
* **Simulation**: Chaos Labs Mechanism Design Review (CIR Base Rate Model, Borrowing Demand Elasticity).

---

## 4. Other Revenue Sources

While borrower interest is king, secondary streams exist but are limited.

### A. Liquidation & Redemption Fees

* **Mechanism**: Fees on redemptions (starts at 0.5%, scales with volume) and penalties on liquidations.
* **Allocation**: In V2, a portion of system yield flows to the **Stability Pool**.
* **Sustainability Check**: If the protocol relies on liquidation penalties for solvency, it is a "predatory" model. We must confirm interest revenue dominates penalties.

### B. Collateral Yields (LSTs)

* **Constraint Confirmation**: As noted in Section 1, Liquity does **not** take a spread on LSTs. This section confirms that `Protocol_LST_Yield = 0`.

---

## 5. Expanded Cost Structure (The "COGS")

To determine viability, we must deduct all costs—implicit and explicit.

### A. Stability Pool Yield Split (The "Wages of Security")

* **Definition**: The cost paid to Stability Pool depositors to secure the system against bad debt.
* **Parameter**: `SP_YIELD_SPLIT`. Configured to **75%** (`750000000000000000`).
* **Implication**: 75% of Gross Interest Revenue is automatically redirected to the SP.
* **Effective Gross Margin**: The protocol retains only **~25%** of interest income.

### B. Liquidity Incentives (The "Customer Acquisition Cost")

* **Steady-State Cost**: To compete with sDAI/USDe, BOLD–USDC pools on Curve/Uniswap require constant incentivization.
* **Expense**: Paid in **LQTY emissions** (equity dilution) or **Protocol Revenue** (if redirected).
* **Sustainability Check**: The system is only sustainable if `Retained Interest Revenue > Value of Liquidity Incentives`.

### C. Keeper Incentives

* **Mechanism**: Gas compensation (200 BOLD + ETH).
* **Risk**: If gas prices spike (L1 congestion), prepaid amounts may be insufficient. The protocol implicitly relies on MEV or token upside to keep keepers active in extreme volatility.

### D. Operational Overhead

* **Oracle Feeds**: Costs for Chainlink or other feeds (often subsidized, but a long-term liability).
* **Governance Maintenance**: DAO tooling, multi-sig operations.

---

## 6. Market Positioning & Competitive Analysis

| Competitor | Revenue Model | Cost Model | Threat to BOLD |
| :--- | :--- | :--- | :--- |
| **MakerDAO (DAI)** | High RWA Yields + Fees | High DSR cost | **High**: Can subsidize sDAI yield to steal BOLD demand. |
| **Frax** | AMOs + RWA + POL | High FXS inflation | **Medium**: More flexible, but higher regulatory risk. |
| **Aave (GHO)** | Interest Spread | Discounted rates | **Medium**: Internalizes liquidity, low cost of capital. |
| **Ethena (USDe)** | Delta-neutral basis yield | Funding rate risk | **High**: Extremely high yield attracts all idle stablecoin capital. |

**Differentiation**:
> **BOLD is the only stablecoin whose revenue model is entirely endogenous to Ethereum.**
> It requires no RWAs (regulatory risk), no human governance (principal-agent risk), and no discretionary monetary policy. Its "Business Model" is selling **pure, trustless leverage**.

---

## 7. Unit Economics of 1 BOLD

For every 1 BOLD minted, the unit economics are:

* **Gross Revenue**: $r_i$ (Borrower Interest Rate)
* **Direct Cost (COGS)**: $0.75 \times r_i$ (Stability Pool Yield Split)
* **Net Revenue (Protocol)**: $0.25 \times r_i$
* **OpEx**: Liquidity Incentives + Governance Overhead.

**Profitability Condition**:
$$ (0.25 \times r_i \times D_{total}) > (\text{Value of LQTY Emissions} + \text{Oracle Costs}) $$

---

## 8. Revenue Volatility & Cyclicality

Interest revenue is highly cyclical and correlated with the **Ether/Crypto Market Cycle**:

* **Bull Market**: High Leverage Demand ($\lambda$) $\rightarrow$ High Rates ($r_i$) + High Debt ($D$) $\rightarrow$ **Record Revenue**.
* **Bear Market**: De-leveraging $\rightarrow$ Low Rates (to avoid redemptions) + Low Debt $\rightarrow$ **Revenue Collapse**.
* **Implication**: The Protocol must accumulate a massive **Surplus Buffer** during Bull Markets to survive the Bear Market "revenue drought."

---

## 9. Inter-Branch Revenue Dynamics

Liquity V2 is multi-collateral. Revenue quality differs by branch:

* **WETH Branch (The "Trading Engine")**:
  * High Volatility $\rightarrow$ High Borrowing Demand $\rightarrow$ High Revenue.
  * High Turnover (Trading leverage).
* **LST Branches (The "Savings Engine")**:
  * Lower Volatility (Yield framing) $\rightarrow$ Passive Leverage (Looping).
  * **Risk**: "Sticky" debt that doesn't generate high interest rates, requiring SP liquidity subsidization.
  * **Sustainability Question**: Does the WETH branch cross-subsidize the LST branches?

---

## 10. Protocol Solvency Under Stress (Stress Tests)

Solvency is not just Assets > Liabilities, but **Cash Flow Solvency**.

1. **The "Zombie" Scenario**:
    * Rates drop to 0% due to low demand.
    * SP Yield drops to 0%.
    * Liquidity dries up (LPs exit).
    * **Result**: Peg breaks downward; protocol enters dormancy.

2. **The "Oracle Failure" Scenario**:
    * If an LST oracle fails, the branch freezes.
    * Interest revenue stops, but system liabilities remain.

3. **Low SP Deposit Scenario**:
    * If `SP Deposits < Liquidatable Debt`.
    * Liquidations fail $\rightarrow$ Bad Debt redistribution $\rightarrow$ Loss of confidence spiral.

---

## 11. Key Metrics & Health Indicators

1. **Net Interest Margin (NIM)**:
    * Formula: $\text{NIM} = \text{WeightedAvgBorrowRate} \times (1 - \text{SP\_YIELD\_SPLIT})$
    * This represents the *net* income retained by the protocol after paying for security (SP).

2. **Surplus Buffer**:
    * The accumulated equity in the system (e.g., in `CollSurplusPool` or similar reserves). This is the "Rainy Day Fund."

---

## 12. Summary: Long-Run Sustainability Conditions

For Liquity V2 (BOLD) to be sustainable, the following conditions must be met:

1. **Demand Sufficiency**: Borrowing demand must be sufficient to maintain $r_i$ substantially above 0%.
2. **SP Capitalization**: The 75% Yield Split must act as a sufficient "wage" to keep Stability Pool providers deposited, even without LQTY incentives.
3. **Incentive Disciplne**: The value of LQTY emissions used to rent liquidity must NOT exceed the 25% Net Revenue retained by the protocol over a full cycle.
4. **Adoption**: BOLD must achieve sufficient utility/velocity to be held without a DSR, otherwise the cost of capital (liquidity incentives) becomes infinite.

---

# Part 2: Engineering & Risk Specification

This section translates the business model into engineering requirements, quantitative thresholds, and data collection standards.

## 13. Concrete Data Definitions (ABI & Event Mapping)

To audit the business model, we map each economic metric to its exact on-chain source.

| Metric | Source Contract | Variable / Function / Event | Calculation Method |
| :--- | :--- | :--- | :--- |
| **Global Weighted Interest** | `ActivePool` | `aggWeightedDebtSum` (uint256) | Read directly. Represents $\sum (D_i \times r_i)$. |
| **Global Principal Debt** | `ActivePool` | `aggRecordedDebt` (uint256) | Read directly. Represents total principal. |
| **Pending Interest** | `ActivePool` | `calcPendingAggInterest()` | Call view function. Adds accrued but unminted interest. |
| **Weighted Avg Rate** | `ActivePool` | N/A (Derived) | `aggWeightedDebtSum / aggRecordedDebt` (scaled by 1e18). |
| **SP Yield Split** | `ActivePool` | `SP_YIELD_SPLIT` (constant) | Read constant (set to 75%). |
| **Per-Trove Rate** | `TroveManager` | `Troves[troveId].annualInterestRate` | Iterate `getTroveFromTroveIdsArray` for distribution. |
| **Liquidation Event** | `TroveManager` | `Liquidation` (Event) | Sum `_collGasCompensation` + `_collToSendToSP` + `_collToRedistribute` for total seized. |
| **Redemption Volume** | `TroveManager` | `Redemption` (Event) | Sum `_attemptedBoldAmount` vs `_actualBoldAmount`. |

## 14. Quantitative Stress Thresholds

These are the specific "Doomsday" triggers where the business model breaks.

| Scenario | Trigger Mechanism | Quantitative Threshold | Consequence |
| :--- | :--- | :--- | :--- |
| **Zombie Apocalypse** | Low Rates + Low Demand | `AvgRate < 0.5%` AND `TotalDebt < 5M BOLD` | Revenue < Operating Costs of Keepers/Frontend. Protocol likely pauses or relies on governance subsidy. |
| **SP Insolvency** | Large Liquidation > SP Depth | `SP_Deposits < Liquidatable_Debt_At_Risk` | Liquidations bypass SP to **Redistribution**. Socializes losses to all borrowers, potentially triggering a "Redistribution Spiral" (Active users leave). |
| **Oracle Freeze** | Chainlink Stale Price | `lastUpdateTime > 4 hours` (Timeout) | Branch freezes. 0 Interest Revenue during freeze. 0 Liquidations (Bad Debt Risk). |
| **Profitability Flip** | Incentive Overspend | `Value(LQTY Emissions) > 25% * Interest_Revenue` | The protocol is operating at a Net Loss (burning equity to rent revenue). |

## 15. Sensitivity Analysis Matrix

We model the **Protocol Net Profit (Annualized)** under varying conditions.
*Assumption: Total Debt = 100M BOLD.*

| Avg Interest Rate | Low SP Deposits (Zero Yield Split Cost) | Healthy SP (75% Yield Split Cost) | High Incentive Spend (-$500k/yr) |
| :--- | :--- | :--- | :--- |
| **Bear (1.5%)** | $1.5M | $375k | **-$125k (Loss)** |
| **Neutral (3.5%)** | $3.5M | $875k | $375k |
| **Bull (6.0%)** | $6.0M | $1.5M | $1.0M |

* **Key Insight**: In a Bear scenario with high incentive spending, the protocol is **unprofitable**. The "Surplus Buffer" must cover this gap.

## 16. Unit Economics: Numeric Worked Examples

The "Economics of 1 BOLD" applied to realistic market phases.

### Case A: Bull Market (Maximum Extraction)

* **Context**: ETH rallying, high leverage demand.
* **Inputs**: AvgRate = 6.5%, Total Debt = 300M BOLD, SP Deposits = 200M.
* **Economics**:
  * Gross Revenue: $19.5M / year.
  * Cost (SP Yield 75%): -$14.625M.
  * **Net Revenue (Protocol)**: **$4.875M / year**.
  * *Result*: Rapid accumulation of Surplus Buffer.

### Case B: Bear Market (Survival Mode)

* **Context**: Post-crash, deleveraging.
* **Inputs**: AvgRate = 1.0%, Total Debt = 50M BOLD, SP Deposits = 40M.
* **Economics**:
  * Gross Revenue: $500k / year.
  * Cost (SP Yield 75%): -$375k.
  * **Net Revenue (Protocol)**: **$125k / year**.
  * *Result*: Barely covers operational overhead (Keepers/Oracles).

## 17. Branch Revenue Split Methodology

Since V2 is multi-collateral, we must detect "Cross-Subsidy".

**Methodology**:

1. **Calculate Branch Revenue ($R_b$)**: $R_b = \sum_{i \in Branch} (D_i \times r_i)$.
2. **Calculate Branch Cost ($C_b$)**: $C_b = R_b \times 0.75 + \text{LiquidityIncentives}_b$.
3. **Net Contribution**: $N_b = R_b - C_b$.

**Hypothesis**: The **WETH Branch** will have a high $N_{WETH}$ (high rates), while **LST Branches** (wstETH) may have neutral or negative $N_{LST}$ if the protocol aggressively incentivizes LST liquidity to compete with Ethena/Maker.

## 18. Operational Risks Quantified

* **Oracle Outage Costs**:
  * If WETH oracle fails for 24 hours:
  * Lost Revenue = $\frac{1}{365} \times \text{AnnualRevenue}$.
  * *Example*: At 100M Debt @ 4%, a 24h outage costs ~$11k in lost revenue per day.
* **Keeper Failure**:
  * If gas > 200 gwei, simple liquidations cost > prepaid compensation.
  * *Risk*: Bad debt accumulates until MEV opportunity > Gas Cost.

## 19. Assumptions Table & Provenance

| Parameter | Value | Source | Note |
| :--- | :--- | :--- | :--- |
| `SP_YIELD_SPLIT` | 75% (0.75 ether) | `ActivePool` / Docs | Immutable split to SP. |
| `MIN_DEBT` | 2000 BOLD | `BorrowerOperations` | Sets minimum scale per trove. |
| `LIQUIDATION_PENALTY_SP` | 5% (simulated) | `TroveManager` | Varies, but standard assumption. |
| `MCR` (WETH) | 110% | `AddressesRegistry` | Minimum Collateral Ratio. |
| `CCR` | 150% | `AddressesRegistry` | Critical Collateral Ratio (Recovery Mode). |

## 20. Data Collection Plan (Pseudo-SQL)

To generate the charts for this analysis:

```sql
-- 1. Distribution of Interest Rates
SELECT
    trove_id,
    interest_rate / 1e16 as annual_rate_percent,
    debt_amount / 1e18 as debt_bold
FROM liquity_v2_ethereum.TroveManager_evt_TroveUpdated
WHERE block_time = current_date
AND status = 'Active'

-- 2. System Weighted Average Rate (TimeSeries)
SELECT
    date_trunc('day', block_time),
    avg(agg_weighted_debt_sum / agg_recorded_debt) as daily_avg_rate
FROM liquity_v2_ethereum.ActivePool_call_mintAggInterest
GROUP BY 1

-- 3. Stability Pool Depth vs. Liabilities
SELECT
    date,
    sp_bold_balance,
    liquidatable_debt -- (Sum of debt where ICR < 110%)
FROM liquity_v2_analytics.risk_dashboard
---

## 8. Revenue Volatility & Cyclicality

Interest revenue is highly cyclical and correlated with the **Ether/Crypto Market Cycle**:

* **Bull Market**: High Leverage Demand ($\lambda$) $\rightarrow$ High Rates ($r_i$) + High Debt ($D$) $\rightarrow$ **Record Revenue**.
* **Bear Market**: De-leveraging $\rightarrow$ Low Rates (to avoid redemptions) + Low Debt $\rightarrow$ **Revenue Collapse**.
* **Implication**: The Protocol must accumulate a massive **Surplus Buffer** during Bull Markets to survive the Bear Market "revenue drought."

---

## 9. Inter-Branch Revenue Dynamics

Liquity V2 is multi-collateral. Revenue quality differs by branch:

* **WETH Branch (The "Trading Engine")**:
  * High Volatility $\rightarrow$ High Borrowing Demand $\rightarrow$ High Revenue.
  * High Turnover (Trading leverage).
* **LST Branches (The "Savings Engine")**:
  * Lower Volatility (Yield framing) $\rightarrow$ Passive Leverage (Looping).
  * **Risk**: "Sticky" debt that doesn't generate high interest rates, requiring SP liquidity subsidization.
  * **Sustainability Question**: Does the WETH branch cross-subsidize the LST branches?

---

## 10. Protocol Solvency Under Stress (Stress Tests)

Solvency is not just Assets > Liabilities, but **Cash Flow Solvency**.

1. **The "Zombie" Scenario**:
    * Rates drop to 0% due to low demand.
    * SP Yield drops to 0%.
    * Liquidity dries up (LPs exit).
    * **Result**: Peg breaks downward; protocol enters dormancy.

2. **The "Oracle Failure" Scenario**:
    * If an LST oracle fails, the branch freezes.
    * Interest revenue stops, but system liabilities remain.

3. **Low SP Deposit Scenario**:
    * If `SP Deposits < Liquidatable Debt`.
    * Liquidations fail $\rightarrow$ Bad Debt redistribution $\rightarrow$ Loss of confidence spiral.

---

## 11. Key Metrics & Health Indicators

1. **Net Interest Margin (NIM)**:
    * Formula: $\text{NIM} = \text{WeightedAvgBorrowRate} \times (1 - \text{SP\_YIELD\_SPLIT})$
    * This represents the *net* income retained by the protocol after paying for security (SP).

2. **Surplus Buffer**:
    * The accumulated equity in the system (e.g., in `CollSurplusPool` or similar reserves). This is the "Rainy Day Fund."

---

## 12. Summary: Long-Run Sustainability Conditions

For Liquity V2 (BOLD) to be sustainable, the following conditions must be met:

1. **Demand Sufficiency**: Borrowing demand must be sufficient to maintain $r_i$ substantially above 0%.
2. **SP Capitalization**: The 75% Yield Split must act as a sufficient "wage" to keep Stability Pool providers deposited, even without LQTY incentives.
3. **Incentive Disciplne**: The value of LQTY emissions used to rent liquidity must NOT exceed the 25% Net Revenue retained by the protocol over a full cycle.
4. **Adoption**: BOLD must achieve sufficient utility/velocity to be held without a DSR, otherwise the cost of capital (liquidity incentives) becomes infinite.

---

# Part 2: Engineering & Risk Specification

This section translates the business model into engineering requirements, quantitative thresholds, and data collection standards.

## 13. Concrete Data Definitions (ABI & Event Mapping)

To audit the business model, we map each economic metric to its exact on-chain source.

| Metric | Source Contract | Variable / Function / Event | Calculation Method |
| :--- | :--- | :--- | :--- |
| **Global Weighted Interest** | `ActivePool` | `aggWeightedDebtSum` (uint256) | Read directly. Represents $\sum (D_i \times r_i)$. |
| **Global Principal Debt** | `ActivePool` | `aggRecordedDebt` (uint256) | Read directly. Represents total principal. |
| **Pending Interest** | `ActivePool` | `calcPendingAggInterest()` | Call view function. Adds accrued but unminted interest. |
| **Weighted Avg Rate** | `ActivePool` | N/A (Derived) | `aggWeightedDebtSum / aggRecordedDebt` (scaled by 1e18). |
| **SP Yield Split** | `ActivePool` | `SP_YIELD_SPLIT` (constant) | Read constant (set to 75%). |
| **Per-Trove Rate** | `TroveManager` | `Troves[troveId].annualInterestRate` | Iterate `getTroveFromTroveIdsArray` for distribution. |
| **Liquidation Event** | `TroveManager` | `Liquidation` (Event) | Sum `_collGasCompensation` + `_collToSendToSP` + `_collToRedistribute` for total seized. |
| **Redemption Volume** | `TroveManager` | `Redemption` (Event) | Sum `_attemptedBoldAmount` vs `_actualBoldAmount`. |

## 14. Quantitative Stress Thresholds

These are the specific "Doomsday" triggers where the business model breaks.

| Scenario | Trigger Mechanism | Quantitative Threshold | Consequence |
| :--- | :--- | :--- | :--- |
| **Zombie Apocalypse** | Low Rates + Low Demand | `AvgRate < 0.5%` AND `TotalDebt < 5M BOLD` | Revenue < Operating Costs of Keepers/Frontend. Protocol likely pauses or relies on governance subsidy. |
| **SP Insolvency** | Large Liquidation > SP Depth | `SP_Deposits < Liquidatable_Debt_At_Risk` | Liquidations bypass SP to **Redistribution**. Socializes losses to all borrowers, potentially triggering a "Redistribution Spiral" (Active users leave). |
| **Oracle Freeze** | Chainlink Stale Price | `lastUpdateTime > 4 hours` (Timeout) | Branch freezes. 0 Interest Revenue during freeze. 0 Liquidations (Bad Debt Risk). |
| **Profitability Flip** | Incentive Overspend | `Value(LQTY Emissions) > 25% * Interest_Revenue` | The protocol is operating at a Net Loss (burning equity to rent revenue). |

## 15. Sensitivity Analysis Matrix

We model the **Protocol Net Profit (Annualized)** under varying conditions.
*Assumption: Total Debt = 100M BOLD.*

| Avg Interest Rate | Low SP Deposits (Zero Yield Split Cost) | Healthy SP (75% Yield Split Cost) | High Incentive Spend (-$500k/yr) |
| :--- | :--- | :--- | :--- |
| **Bear (1.5%)** | $1.5M | $375k | **-$125k (Loss)** |
| **Neutral (3.5%)** | $3.5M | $875k | $375k |
| **Bull (6.0%)** | $6.0M | $1.5M | $1.0M |

* **Key Insight**: In a Bear scenario with high incentive spending, the protocol is **unprofitable**. The "Surplus Buffer" must cover this gap.

## 16. Unit Economics: Numeric Worked Examples

The "Economics of 1 BOLD" applied to realistic market phases.

### Case A: Bull Market (Maximum Extraction)

* **Context**: ETH rallying, high leverage demand.
* **Inputs**: AvgRate = 6.5%, Total Debt = 300M BOLD, SP Deposits = 200M.
* **Economics**:
  * Gross Revenue: $19.5M / year.
  * Cost (SP Yield 75%): -$14.625M.
  * **Net Revenue (Protocol)**: **$4.875M / year**.
  * *Result*: Rapid accumulation of Surplus Buffer.

### Case B: Bear Market (Survival Mode)

* **Context**: Post-crash, deleveraging.
* **Inputs**: AvgRate = 1.0%, Total Debt = 50M BOLD, SP Deposits = 40M.
* **Economics**:
  * Gross Revenue: $500k / year.
  * Cost (SP Yield 75%): -$375k.
  * **Net Revenue (Protocol)**: **$125k / year**.
  * *Result*: Barely covers operational overhead (Keepers/Oracles).

## 17. Branch Revenue Split Methodology

Since V2 is multi-collateral, we must detect "Cross-Subsidy".

**Methodology**:

1. **Calculate Branch Revenue ($R_b$)**: $R_b = \sum_{i \in Branch} (D_i \times r_i)$.
2. **Calculate Branch Cost ($C_b$)**: $C_b = R_b \times 0.75 + \text{LiquidityIncentives}_b$.
3. **Net Contribution**: $N_b = R_b - C_b$.

**Hypothesis**: The **WETH Branch** will have a high $N_{WETH}$ (high rates), while **LST Branches** (wstETH) may have neutral or negative $N_{LST}$ if the protocol aggressively incentivizes LST liquidity to compete with Ethena/Maker.

## 18. Operational Risks Quantified

* **Oracle Outage Costs**:
  * If WETH oracle fails for 24 hours:
  * Lost Revenue = $\frac{1}{365} \times \text{AnnualRevenue}$.
  * *Example*: At 100M Debt @ 4%, a 24h outage costs ~$11k in lost revenue per day.
* **Keeper Failure**:
  * If gas > 200 gwei, simple liquidations cost > prepaid compensation.
  * *Risk*: Bad debt accumulates until MEV opportunity > Gas Cost.

## 19. Assumptions Table & Provenance

| Parameter | Value | Source | Note |
| :--- | :--- | :--- | :--- |
| `SP_YIELD_SPLIT` | 75% (0.75 ether) | `ActivePool` / Docs | Immutable split to SP. |
| `MIN_DEBT` | 2000 BOLD | `BorrowerOperations` | Sets minimum scale per trove. |
| `LIQUIDATION_PENALTY_SP` | 5% (simulated) | `TroveManager` | Varies, but standard assumption. |
| `MCR` (WETH) | 110% | `AddressesRegistry` | Minimum Collateral Ratio. |
| `CCR` | 150% | `AddressesRegistry` | Critical Collateral Ratio (Recovery Mode). |

## 20. Data Collection Plan (Pseudo-SQL)

To generate the charts for this analysis:

```sql
-- 1. Distribution of Interest Rates
SELECT
    trove_id,
    interest_rate / 1e16 as annual_rate_percent,
    debt_amount / 1e18 as debt_bold
FROM liquity_v2_ethereum.TroveManager_evt_TroveUpdated
WHERE block_time = current_date
AND status = 'Active'

-- 2. System Weighted Average Rate (TimeSeries)
SELECT
    date_trunc('day', block_time),
    avg(agg_weighted_debt_sum / agg_recorded_debt) as daily_avg_rate
FROM liquity_v2_ethereum.ActivePool_call_mintAggInterest
GROUP BY 1

-- 3. Stability Pool Depth vs. Liabilities
SELECT
    date,
    sp_bold_balance,
    liquidatable_debt -- (Sum of debt where ICR < 110%)
FROM liquity_v2_analytics.risk_dashboard
```

## 21. Regulatory Note

* **Advantage**: BOLD is backed 100% by ETH/LSTs. It holds no RWAs (Treasuries, Corporate Bonds). It falls under "Asset-Referenced Tokens" (MiCA) or "Overcollateralized Stablecoins" rather than "E-Money Tokens" or Securities.
* **Risk**: It has no "blacklist" or "freeze" function at the token level (Immutable), making it resistant to OFAC compliance, which implies institutional adoption hurdles.

---

## 22. Required Visualizations (Figure List)

To communicate this analysis effectively, the following charts are required (to be included in Section 1 and Executive Summary):

1. **Weighted Avg Borrow Rate (Time Series)**
    * *X-Axis*: Time (Day/Week). *Y-Axis*: Interest Rate (%).
    * *Series*: System-wide Avg, WETH Branch Avg, wstETH Branch Avg.
    * *Purpose*: Visualizes revenue quality and trend direction.

2. **Interest Rate Distribution (Histogram)**
    * *X-Axis*: Interest Rate buckets (e.g., 2%, 2.5%, etc.). *Y-Axis*: Debt Volume (BOLD).
    * *Overlay*: "Redemption Risk Zone" (Bottom 10% of rates).
    * *Purpose*: Shows how "efficient" the market is (clustering vs dispersion).

3. **Stability Pool vs. Liquidatable Debt (Heatmap/Area)**
    * *X-Axis*: Time. *Y-Axis*: BOLD Amount.
    * *Areas*: Total SP Deposits (Green) vs. Debt with ICR < 110% (Red).
    * *Purpose*: Visualizes "Solvency Coverage Ratio" (Risk of Redistribution).

4. **Unit Economics Bars (Scenario Comparison)**
    * *Category*: Bull / Neutral / Bear.
    * *Stacked Bar*: Gross Interest (Top), SP Yield Cost (Middle), Protocol Net Revenue (Bottom).
    * *Line*: Breakeven Threshold (Incentive Cost).
    * *Purpose*: Proves profitability (or lack thereof) in each regime.

5. **Stress-Test Matrix (Heatmap)**
    * *Rows*: Interest Rate Scenarios (1% - 6%). *Cols*: Incentive Spend ($0 - $5M).
    * *Cell*: Net Profit/Loss ($). Color scale Red (Loss) to Green (Profit).
    * *Purpose*: Identifies the "Safety Zone" for incentive spending.

6. **Branch Contribution (Stacked Bar)**
    * *X-Axis*: Branch (WETH, wstETH, rETH).
    * *Stack*: Gross Revenue ($), Retained Share ($).
    * *Purpose*: Identifies the "Cash Cow" branch vs "Loss Leader" branches.
