# Business Model Decomposition (MakerDAO)

**Goal**: Analyze MakerDAO not just as a protocol, but as a "Central Bank" business. This document dissects the Economic Engine: Revenue (RWAs/Fees), Costs (DSR), Liabilities (DAI), and Constraints.

---

## 1. Business Model Design Constraints (The "Upper Bound")

Unlike Liquity, MakerDAO operates as a discretionary credit facility with active treasury management.

### A. Rehypothecation (RWA Monetization)

* **Advantage**: MakerDAO *does* monetize the backing assets.
* **Mechanism**: It takes USDC from the PSM and invests it in US Treasuries (via Clydesdale/BlockTower/Andromeda). It creates "Double-Dip" revenue:
  * Users mint DAI (0% fee for PSM).
  * Maker invests backing in T-bills (5% yield).
  * Maker keeps the spread (Yield - DSR).
* **Business Impact**: This is the primary revenue driver in the "Endgame" era.

### B. Mutable Design (Active Governance)

**Revenue Composition**:
![Revenue Split](../Diagrams/Business%20Decomposition/6_revenue_composition.png)
**Interest Rate Distribution**:
![Rate Distribution](../Diagrams/Business%20Decomposition/2_interest_rate_distribution.png)

* **Constraint**: Parameters (Rates, DSR, Collateral types) are actively managed.

* **Constraint**: Parameters (Rates, DSR, Collateral types) are actively managed.
* **Business Impact**:
  * **Cyclical Pricing**: Can hike rates to suppress demand or lower DSR to widen margins.
  * **Political Risk**: Active management introduces lobbying, governance attacks, and principal-agent problems.

---

## 2. The Liability Structure: Demand for DAI/USDS

### A. DSR as the Cost of Capital

* **Savings Rate**: DAI pays a native savings rate (DSR).
* **Demand Driver**: Users hold DAI/USDS primarily for *yield*. Competitors (sDAI, USDe) force Maker to keep DSR high.
* **Cost**: The DSR is a direct "Interest Expense" for the protocol. If DSR > Asset Yield, the protocol bleeds equity.

### B. DAI Velocity

* **Transactional Demand**: Low (mostly used for yield farming).
* **Leverage Demand**: High (used to buy more crypto).

---

## 3. Revenue Source: The Asset Side

### A. RWA Portfolio (The Cash Cow)

* **Source**: Monetized USDC in Real World Assets.
* **Yield**: ~4-5% (Risk-Free Rate).
* **Volume**: ~$1-2 Billion monetized.
* **Revenue**: ~$50-100M annual.

### B. Crypto-Native Fees (The Volatility Play)

* **Source**: Stability Fees on ETH/WBTC vaults.
* **Yield**: 3-8% (Variable).
* **Volume**: ~$1-2 Billion.
* **Revenue**: Highly cyclical (Booms in Bull markets, crashes in Bear).

---

## 4. Expanded Cost Structure (The "COGS")

### A. DSR (Cost of Liabilities)

* **Definition**: Interest paid to DAI holders.
* **Rate**: Variable (currently ~5%).
* **Impact**: Limits the Net Interest Margin (NIM).

### B. SubDAO Emissions (Endgame)

* **Mechanism**: Farming rewards (NewStable, NewGovToken) to incentivize activity.
* **Cost**: Dilution of the ecosystem token supply.

### C. Operational Overhead

* **Real World Legal**: Lawyers, Trust structures, Audits for RWAs.
* **Oracle Feeds**: Chronic cost.
* **Keepers**: Gas compensation.

---

## 5. Unit Economics of 1 DAI

![Unit Economics](../Diagrams/Business%20Decomposition/4_unit_economics_scenarios.png)

For every 1 DAI minted via RWA:

* **Gross Revenue**: 5% (T-Bill Yield)
* **Direct Cost**: 3.5% (DSR)
* **Net Revenue**: 1.5% (NIM)
* **OpEx**: Legal + Governance.

**Diagram**: Cost of Goods Sold Breakdown
![COGS Breakdown](../Diagrams/Key%20Metrics/cogs_breakdown.png)

---

## 6. Sensitivity Analysis Matrix

![Stress Matrix](../Diagrams/Business%20Decomposition/5_stress_test_matrix.png)
![Surplus Risk](../Diagrams/Business%20Decomposition/3_sp_vs_liquidatable_debt.png)

| Asset Yield | Low DSR (1%) | High DSR (5%) |
| :--- | :--- | :--- |
| **Bear (2%)** | Profit | **Loss** |
| **Neutral (5%)** | Super-Profit | Breakeven |
| **Bull (8%)** | Mega-Profit | Profit |

---

## 7. Data Collection Plan

To audit this business model:

* **On-Chain**: `Pot` contract (dsr), `Vat` (debt), `Jug` (fees).
* **Off-Chain**: RWA trustee reports (monthly attestation).

 ---

## 8. Historical Analysis (2023-2024)

 This sections analyzes the *Cost of Carry* dynamics during the critical RWA pivoting phase.

### Phase 1: The Arbitrage Gap (Early 2023)

* **State**: US T-Bills rose to >4% while DSR remained at 1%.
* **Result**: Massive surplus generation (~$80M annualized run-rate). MakerDAO captured almost the entire spread.
* **Risk**: Users left DAI for sDAI/USDC to capture yield elsewhere, shrinking the supply.

### Phase 2: The EDSR Response (Mid 2023)

* **Action**: Construction of the Enhanced DSR (EDSR) to hike rates to 5-8% temporarily.
* **Impact**: Stopped the bleeding of TVL.
* **Cost**: NIM compressed to near zero (or negative) for short periods to "buy back" liquidity.
* **Lesson**: You cannot capture the spread forever. Eventually, you must pass 80-90% of the RWA yield to the user to maintain demand.

### Phase 3: The Endgame Equilibrium (2024)

![Historical Rates](../Diagrams/Business%20Decomposition/1_weighted_avg_rate_timeseries.png)

* **State**: DSR stabilized at 5%. RWA Yield at 5.5%.

* **State**: DSR stabilized at 5%. RWA Yield at 5.5%.
* **Margin**: Thin but high volume (~50 bps spread on $3B+ RWA).
* **Sustainability Verdict**: The model shifted from "High Margin / Low Vol" to "Low Margin / High Vol". The protocol is now a **Volume Business**, dependent on keeping RWA assets >$2B to cover fixed costs.
