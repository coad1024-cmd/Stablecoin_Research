# Key Metrics & Health Indicators

**Goal**: Establish the quantitative dashboard for assessing Liquity V2's long-term sustainability. This section defines the critical financial ratios and health indicators that distinguish a solvent protocol from a profitable business.

---

## 1. Net Interest Margin (NIM)

In banking, NIM reveals how much a lender earns in interest compared to what it pays out to depositors. For Liquity V2, this is the primary measure of **Operational Profitability**.

### A. The Formula
Unlike V1 (one-time fees), V2 is a spread business.

$$ \text{NIM} = \text{WeightedAvgBorrowRate} - (\text{SP Yield Split} + \text{Liquidity Incentives} + \text{Oracle Costs}) $$

Where:
*   **WeightedAvgBorrowRate**: The gross interest paid by borrowers.
*   **SP Yield Split**: The fixed 75% of interest redirected to the Stability Pool.
*   **Liquidity Incentives**: The annualized cost of LQTY emissions or bribes paid to liquidity pools (Curve/Uniswap).
*   **Oracle Costs**: Operational overhead for price feeds.

### B. The Sustainability Threshold
For the protocol to be sustainable without burning equity:
$$ \text{NIM} > 0 $$

If $\text{NIM} < 0$, the protocol is subsidizing borrowers or liquidity providers from its treasury (or future equity value), effectively operating as a venture-subsidized product rather than a self-sustaining utility.

**Visual Reference**:
![NIM Schematic](../Diagrams/Key%20Metrics/nim_formula_schematic.png)
*Figure 1: Visual breakdown of the Net Interest Margin flow, showing the waterfall of revenue from Borrowers to SP, LPs, and finally the Protocol Surplus.*

---

## 2. The Surplus Buffer (Equity)

The Surplus Buffer represents the accumulated retained earnings of the protocol. It acts as the "Capital Buffer" or "Rainy Day Fund."

### A. Role in Cycle Management
Stablecoins are cyclical.
*   **Bull Market**: High demand = High Rates = Buffer Accumulation.
*   **Bear Market**: Low demand = Low Rates = Buffer Depletion (paying fixed costs like Keepers/Oracles).

### B. Critical Metric: "Runway"
$$ \text{Runway (Months)} = \frac{\text{Current Surplus Buffer}}{\text{Monthly Fixed OpEx}} $$

This metric answers: *If all revenue stopped today, how long could the protocol keep the lights on?*

**Visual Reference**:
![Surplus Buffer Growth](../Diagrams/Key%20Metrics/surplus_buffer_growth.png)
*Figure 2: Hypothetical projection of Surplus Buffer growth during a Bull Market and drawdown during a Bear Market, highlighting the critical "Survival Threshold".*

---

## 3. Cost of Goods Sold (COGS) per 1 BOLD

This metric standardizes costs to the unit level, allowing comparison with other stablecoins like DAI or USDe.

### A. Components
1.  **Security Cost**: The yield paid to the Stability Pool (75% of revenue). This is the cost of insuring the peg.
2.  **Liquidity Cost**: The incentives paid to maintain secondary market depth (Peg liquidity).
3.  **Execution Cost**: Gas subsidies for Keepers.

### B. Efficiency Ratio
$$ \text{Efficiency Ratio} = \frac{\text{Non-Interest Expense}}{\text{Net Revenue}} $$

A lower ratio indicates a more efficient protocol. If the ratio > 100%, the protocol spends more on operations/incentives than it earns.

**Visual Reference**:
![COGS Breakdown](../Diagrams/Key%20Metrics/cogs_breakdown.png)
*Figure 3: A breakdown of the cost components for every 1 BOLD minted. Comparing Security Costs (SP) vs. Liquidity Costs (Incentives).*

---

## 4. System Health Indicators

Beyond pure financials, these indicators measure the robustness of the system's core promise: Stability.

### A. Peg Strength (Deviation)
*   **Metric**: Standard Deviation of Price ($\sigma_p$) over a 30-day window.
*   **Goal**: Minimize $\sigma_p$.
*   **Sustainability Check**: High volatility implies the redemption mechanism or liquidity pools are inefficient, requiring higher incentives (Cost) to fix.

### B. Bad Debt Ratio
*   **Metric**: $\frac{\text{Debt in Troves with ICR < 110\%}}{\text{Total Debt}}$.
*   **Risk**: If this ratio rises significantly above the SP coverage, the system faces "Redistribution Risk" (Socialized losses).

### C. Incentive Efficiency (ROI)
*   **Metric**: $\frac{\text{New TVL Generated}}{\text{$1 of Incentives Spent}}$.
*   **Goal**: $> 1.0$. If $< 1.0$, the protocol is paying more than $\$1$ to acquire $\$1$ of liquidity, which is unsustainable.

**Visual Reference**:
![Incentive Efficiency Chart](../Diagrams/Key%20Metrics/incentive_efficiency_roi.png)
*Figure 4: Return on Investment (ROI) for Liquidity Incentives. A comparison of efficient vs. inefficient incentive spending regimes.*

---

## 5. Summary Dashboard

| Metric | Target / Healthy Range | Warning Signal |
| :--- | :--- | :--- |
| **NIM** | $> 0.50\%$ | Negative |
| **Surplus Buffer Runway** | $> 24 \text{ Months}$ | $< 6 \text{ Months}$ |
| **Peg Deviation ($\sigma$)** | $< 0.005$ | $> 0.01$ |
| **Bad Debt Ratio** | $0\%$ | $> 5\%$ of SP Depth |
| **Incentive ROI** | $> 2.0x$ | $< 1.0x$ |
