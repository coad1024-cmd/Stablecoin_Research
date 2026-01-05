# Liquity V2: The Economics of Modular Solvency

**Authors**: Research Challenge Team
**Date**: January 2026
**Series**: Part II (Sustainability)

---

## Abstract

This paper analyzes the economic security model of Liquity V2 (BOLD), a multi-collateral stablecoin protocol. Unlike its predecessor, which relied on a static one-time fee, V2 introduces a continuous **User-Set Interest Rate** mechanism to price risk dynamically. We formalize the protocol's solvency constraints using the Klages-Mundt (2023) framework, demonstrating that the system achieves stability *if and only if* the Stability Pool yield split ($Y_{sp} = 75\%$) effectively capitalizes the defense layer against submartingale asset price shocks. We further quantify the **Net Interest Margin (NIM)** efficiency required to sustain immutable operations in a competitive yield environment.

> [!IMPORTANT]
> **Methodology Statement**: This analysis leverages **Agent-Based Simulation (ABS)** and theoretical game-theoretic modeling. As Liquity V2 is a novel architecture, empirical mainnet data is unavailable. All projections assume rational actor behavior under defined constraints.

---

## 1. Introduction

The fundamental challenge of decentralized stablecoin design is the **Capital Efficiency vs. Solvency Trilemma**. Protocols must choose two:
1.  **Capital Efficiency**: Minimizing collateral requirements.
2.  **Hard Solvency**: Guaranteeing atomic liquidations without governance intervention.
3.  **Exogenous Collateral**: Accepting assets (ETH, LSTs) with independent volatility.

Liquity V1 solved this by sacrificing capital efficiency (high collateral processing friction) for extreme solvency. Liquity V2 attempts to reclaim efficiency via a "Modular Liability" architecture. This report questions whether the economic engine of V2—specifically its revenue model—is robust enough to fund its own defense.

### 1.1 The Sustainability Triangle

We structure our analysis around three orthogonal vectors of risk, formalized as the **Sustainability Triangle**:

![The Sustainability Triangle](../Diagrams/Sustainability%20Triangle/sustainability_triangle_diagram.png)
*Figure 1: The Sustainability Triangle. A protocol remains solvent only if it maintains structural integrity across Asset Quality (Collateral), Behavioral Incentives (Keepers), and Resolution Mechanisms (Backstops).*

---

## 2. The Business Model: Shadow Banking on Chain

Liquity V2 moves beyond the "Protocol" paradigm into "Shadow Banking." It does not merely facilitate debt; it manages a balance sheet where it must actively price the cost of its liability (BOLD) against the yield of its assets (Borrower Interest).

### 2.1 Constraint Analysis

Unlike custodial competitors (e.g., MakerDAO, Ethena), Liquity V2 operates under strict immutability constraints that bound its revenue potential:

*   **No Rehypothecation**: $\text{Yield}_{Asset} \rightarrow \text{User}$. The protocol cannot monetize the collateral yield (e.g., stETH staking rewards).
*   **Immutable Parameters**: Governance cannot arbitrarily wide spreads to recapitalize the system during crises.

### 2.2 Revenue Formulation

The protocol's primary revenue stream is the **Weighted Average Borrow Rate** ($r_{avg}$). This is not set by a central bank (DAO) but emerges from an auction-like mechanism where users bid for "Redemption Protection."

$$ r_{avg} = \frac{\sum_{i=1}^{N} D_i \cdot r_i}{D_{total}} $$

Where $D_i$ is the debt of Trove $i$ and $r_i$ is the user-selected rate.

![Interest Rate Distribution](../Diagrams/Business%20decompostion/2_interest_rate_distribution.png)
*Figure 2: Distribution of Borrower Interest Rates ($r_i$). Rational actors cluster their rates just above the "Redemption Threshold" defined by $r_{cutoff}$.*

### 2.3 The Cost of Goods Sold (COGS)

We define the protocol's "Cost of Goods Sold" as the direct expense required to maintain the peg. In V2, this is the yield paid to Stability Pool depositors to incentivize them to cover bad debt risk.

$$ \text{COGS}_{BOLD} = r_{avg} \cdot Y_{sp} + \text{Incentives}_{Liquidity} $$

Given the immutable parameter $Y_{sp} = 0.75$, the protocol retains a theoretical maximum gross margin of **25%**.

![COGS Breakdown](../Diagrams/Key%20Metrics/cogs_breakdown.png)
*Figure 3: Unit Economics of 1 BOLD. The majority of revenue (75%) is algorithmically redirected to the solvency layer (Stability Pool).*

---

## 3. Financial Health & Key Metrics

To assess long-term viability, we derive the **Net Interest Margin (NIM)** of the protocol. This metric serves as the primary indicator of whether the system is self-sustaining or reliant on equity dilution (LQTY inflation).

### 3.1 Net Interest Margin (NIM)

$$ \text{NIM} = r_{avg} \cdot (1 - Y_{sp}) - \frac{\text{OpEx} + \text{Emissions}}{D_{total}} $$

> [!NOTE]
> **The Profitability Threshold**: For the protocol to avoid burning equity, we must have $\text{NIM} > 0$. This implies that the 25% retained interest must exceed the cost of all secondary liquidity incentives on Curve/Uniswap.

![NIM Schematic](../Diagrams/Key%20Metrics/nim_formula_schematic.png)
*Figure 4: The Flow of Funds. Revenue is partitioned at the source, with the protocol's surplus acting as the residual claimant.*

### 3.2 The Surplus Buffer

The protocol's resilience is a function of its accumulated equity, or **Surplus Buffer**. This buffer must absorb fixed operating costs (Oracle fees, Keeper gas subsidies) during "Bear Regimes" where $r_{avg} \rightarrow 0$.

![Surplus Buffer Growth](../Diagrams/Key%20Metrics/surplus_buffer_growth.png)
*Figure 5: Surplus Buffer Dynamics. The system acts as a counter-cyclical accumulator, harvesting value during high-volatility Bull markets to survive low-volatility Bear markets.*

---

## 4. Formal Regime Analysis

Drawing on Klages-Mundt (2023), we formally define the stability boundaries of the system.

### 4.1 Stability Regimes

We define the system state $S_t$ as a function of the Total Collateral Ratio ($TCR$) and the Stability Pool Depth ($D_{sp}$).

*   **Stable Regime ($\mathcal{R}_{stable}$)**: $Var(P_{BOLD}) < \epsilon$ where $TCR > 150\%$.
*   **Volatile Regime ($\mathcal{R}_{volatile}$)**: $TCR \in [110\%, 150\%]$. Variance amplifies as collateral buffers thin.
*   **Unstable Regime ($\mathcal{R}_{unstable}$)**: $TCR \rightarrow 110\%$ AND $D_{sp} \rightarrow 0$.

![Variance Regime Plot](../Diagrams/Formal%20Regime%20Analysis/variance_regime_plot.png)
*Figure 6: Phase Transition of Price Variance. As the system approaches the critical collateral threshold ($MCR$), volatility ($Z_t$) explodes non-linearly.*

### 4.2 The Submartingale Condition

A critical failure mode exists if the collateral asset $X_t$ follows a defined submartingale process (expected value decreases over time) while system liquidity is constrained.

$$ E[X_{t+1} | X_t] < X_t $$

In this scenario, a "Deleveraging Spiral" can occur:
1.  **Rational Exit**: Borrowers repay to preserve equity.
2.  **Liquidity Squeeze**: Demand for BOLD repayment exceeds supply $S_{BOLD}$.
3.  **Peg Break**: $P_{BOLD} > 1.05$, forcing insolvencies.

![Submartingale Spiral](../Diagrams/Formal%20Regime%20Analysis/Regime_Variant_1.png)
*Figure 7: The Deleveraging Feedback Loop. Negative price drift triggers a liquidity crunch that accelerates insolvency.*

---

## 5. Operational Risk Quantified

Finally, we assess the non-economic "Existential Threats" posed by infrastructure and regulation.

### 5.1 The Oracle Dependency
The system's "Epistemic Security" relies entirely on the liveness of Chainlink oracles. A freeze $>4h$ results in a halt of the liquidation engine.

![Oracle Dependency Map](../Diagrams/Operational%20and%20Regulatory/Operational_Variant_1.png)
*Figure 8: Critical Path Analysis of Oracle Dependencies.*

### 5.2 Regulatory Arbitrage vs. Compliance
Liquity V2 positions itself as a "hard" primitive. By eschewing RWA (Real World Asset) backing, it incurs a capital efficiency penalty but gains a "Censorship Resistance Premium."

![Regulatory Risk Radar](../Diagrams/Operational%20and%20Regulatory/regulatory_risk_radar.png)
*Figure 9: Relative Regulatory Risk Profile (BOLD vs. USDC).*

---

## Conclusion

The economic sustainability of Liquity V2 rests on a single mechanism design wager: **That the market will pay a premium for immutable, non-custodial leverage.**

Our analysis suggests that while the **Business Model** is highly cyclical and potentially loss-making in low-volatility regimes, the **Mechanism Design** is robust. The 75% Yield Split effectively creates a "Defense Tax" that scales linearly with risk, automating the capitalization of the system's solvency layer.

**Verdict**: Technically Solvent, Economically Cyclical.

*Part III of this series will examine the Decentralization & Censorship Resistance properties of the V2 federation.*
