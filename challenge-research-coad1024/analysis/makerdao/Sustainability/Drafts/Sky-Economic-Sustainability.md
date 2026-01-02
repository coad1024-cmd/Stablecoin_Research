# Sky Ecosystem: Structural Analysis of Hybrid Solvency (Part II)

**Authors**: Research Challenge Team
**Date**: January 2026
**Series**: Sky Research Series (Part II)

---

## Abstract

This paper provides a critical economic analysis of the Sky Ecosystem's transition from a crypto-native stablecoin protocol to a hybrid "Shadow Banking" entity. While the integration of Real-World Assets (RWAs) has stabilized the peg effectively, it has introduced a fundamental inversion in the protocol's unit economics. We demonstrate that the shift to a **Net Interest Margin (NIM)** business model has created a dependency on exogenous interest rate regimes, specifically the spread between US Treasuries and DeFi yield expectations. This report argues that the current "Endgame" strategy is not merely an optimization but a structural necessity to offset margin compression through massive scale.

> [!IMPORTANT]
> **Critical Lens**: This analysis challenges the assumption that "backed" equals "sustainable." It highlights the existential risks posed by regulatory capture vectors (Loop 1) and the fragility of the Net Interest Margin under contracting rate environments.

---

## 1. Introduction: The Capital Efficiency Paradox

The "Sustainability Trilemma" posits a necessary trade-off between Capital Efficiency, Solvency, and Decentralization. Sky's evolution represents a deliberate strategic pivot towards Efficiency and Solvency at the direct expense of Decentralization.

![Sustainability Triangle](../Diagrams/Sustainability%20Triangle/sustainability_triangle_diagram.png)
*Figure 1: The Sustainability Triangle. The system prioritizes Asset Stability (Loop 1) and Monetary Policy (Loop 2) over minimizing Governance/Counterparty Risk (Loop 3).*

*   **Loop 1 (Collateral)**: The inclusion of RWAs (14% of backing) introduces **Censorship Vectors**. Unlike on-chain assets, these reserves are subject to "Legal Latency"—seizure or freezing order risks that cannot be mitigated by smart contracts.
*   **Loop 2 (Incentives)**: The DSR (Dai Savings Rate) functions as a direct cost of capital. In a competitive yield environment, this cost is dictated by market forces rather than protocol policy.
*   **Loop 3 (Governance)**: The SubDAO architecture distributes operational risk but does not eliminate the central regulatory nexus of the RWA trustees.

---

## 2. The Business Model: Implicit Shadow Banking

Sky has effectively evolved into an on-chain Shadow Bank. Its core business is no longer "trustless lending" but rather a **Carry Trade**: sourcing liquidity via stablecoin issuance (Liabilities) and deploying it into yield-bearing RWAs (Assets).

### 2.1 Revenue Model Inversion

The protocol's revenue composition has shifted from excessive-margin volatility fees to thin-margin risk-free rates. Two distinct eras emerge:
1.  **The Volatility Era (2019-2022)**: High fees charged on crypto-leverage demand. Revenue was counter-cyclical to asset prices.
2.  **The Yield Era (2023-Present)**: Revenue is derived almost exclusively from the RWA portfolio, making the protocol pro-cyclical to US Interest Rates.

![Revenue Composition](../Diagrams/Business%20Decomposition/6_revenue_composition.png)
*Figure 2: Revenue Composition. The structural shift from volatility-based fees (Blue) to asset-based yield (Green) highlights the protocol's new dependency on traditional financial markets.*

### 2.2 The "Price-Taker" Dynamic

Unlike a monopoly protocol, Sky is now a price-taker availability. To retain Total Value Locked (TVL), the DSR must effectively match the "Risk-Free Rate of DeFi" established by competitors (e.g., Ethena, Aave).

![Interest Rate Distribution](../Diagrams/Business%20Decomposition/2_interest_rate_distribution.png)
*Figure 3: Rate Distribution. User behavior is highly elastic; capital flight occurs rapidly when the DSR falls below the competitive equilibrium.*

---

## 3. Financial Health: Margin Compression Analysis

The viability of Sky's model rests on its **Net Interest Margin (NIM)**—the spread between RWA Yields and the DSR Cost.

### 3.1 The 50bps Constraint

$$ \text{NIM} \approx \text{Yield}_{RWA} - \text{Cost}_{DSR} $$

With T-Bills yielding ~5.0% and competitive pressures forcing a ~4.5% DSR, the protocol operates on a ~0.5% margin. This places the protocol in a **Volume Trap**:
*   To sustain $50M in fixed Operational Expenditure (OpEx), the protocol requires a minimum of **$10 Billion** in earning assets.
*   Falling below this threshold necessitates spending equity (Surplus Buffer) to maintain operations.

![NIM Schematic](../Diagrams/Key%20Metrics/nim_formula_schematic.png)
*Figure 4: Net Interest Margin Flow. The protocol acts as a pass-through entity, retaining only a fraction regarding the yield it generates.*

### 3.2 Subsidized Growth via COGS

The issuance of SubDAO tokens (e.g., Spark) effectively functions as a "Customer Acquisition Cost" (CAC). This creates a fragility: if token emissions cease, the "effective yield" for users drops, potentially triggering capital flight and deleveraging the system.

![COGS Breakdown](../Diagrams/Key%20Metrics/cogs_breakdown.png)
*Figure 5: Unit Economics. A significant portion of "revenue" is effectively subsidized by equity dilution (token emissions).*

---

## 4. Formal Regime Analysis: Exogenous Rate Dependence

Applying the Klages-Mundt stability framework reveals a critical vulnerability to macroeconomic shifts.

### 4.1 The Unstable Domain

The system remains stable only so long as **External Risk-Free Rates $\ge$ Internal DeFi Yield Costs**.
*   **The Inversion Risk**: If the Federal Reserve cuts rates (lowering RWA yield) while crypto-native demand remains high (keeping DSR costs high), the NIM turns negative.
*   **Consequence**: The protocol begins to bleed surplus. Without a "Borrowing Demand" revival (crypto-native lending), there is no mechanism to offset this loss.

![Regime Variance](../Diagrams/Formal%20Regime%20Analysis/variance_regime_plot.png)
*Figure 6: Stability Regimes. The "Unstable Domain" (Red) represents a negative carry environment where equity burn is required to maintain the peg.*

---

## 5. Operational Resilience: Verification Gaps

While the economic model has risks, the operational layer introduces distinct "Trust Assumptions."

### 5.1 Throughput Latency vs. Verification

The reliance on Layer 2 scaling (Arbitrum, Base) for liquidation throughput introduces a dependency on **Sequencer Liveness**. A failure in the L2 infrastructure during a market crash would render the `Clipper` (Auction Mechanism) partially inoperable, creating a backlog regarding bad debt.

### 5.2 The Oracle "Blind Spot"

The continued use regarding the 1-hour OSM delay, while protective against flash loan attacks, creates an informational asymmetry. In a hyper-volatility event, the system may be technically insolvent for up to 60 minutes before the protocol "realizes" the price update, preventing timely liquidations.

---

## Conclusion: The Imperative of Scale

The transformation of MakerDAO into Sky represents a pragmatic acceptance of market realities. The "Pure Crypto" lending model could not scale to meet global demand for stablecoins.

**Key Findings:**
1.  **Structural Pivot**: The transition to a "Shadow Bank" model is complete. The protocol's health is now correlated with macro-interest rates rather than crypto-volatility.
2.  **Margin Fragility**: The reliance on thin NIMs necessitates massive scale ($20B+ TVL) to ensure long-term sustainability.
3.  **Governance Centralization**: The management of off-chain RWA collateral inevitably concentrates power, contradicting the ethos of decentralization but satisfying the requirement for stability.

**Final Verdict**: Sky has successfully achieved **Economic Solvency** at the cost of **Sovereignty**. It is a robust financial machine, but one that is now inextricably linked to the traditional banking system it sought to replace.

---

### Series Navigation
*   [← Part I: Backing Mechanism (The Architecture)](../Backing%20Mechanism/Drafts/Sky-Backing-Mechanism.md)
*   **Part II: Economic Sustainability (The Audit)** (You are here)
*   [Part III: Decentralization Risk (The Governance)](../Decentralization/Drafts/Decentralization-Risk.md) (Coming Soon)
