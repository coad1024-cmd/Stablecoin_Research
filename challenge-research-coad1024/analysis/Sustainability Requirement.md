# Framework for Analysis: Sustainability of Overcollateralized Stablecoins

## Purpose

This document provides a comprehensive framework for writing a **Sustainability Analysis Article** for any overcollateralized stablecoin (e.g., LUSD, RAI, DAI). "Sustainability" here is defined not just as current solvency, but as the system's ability to survive and persist over the long term through market cycles, regulatory shifts, and economic stress.

This framework synthesizes the **"Sustainability Triangle"** model (interacting feedback loops) with the **"Dual Mandate"** concept (profit vs. stability) from the broader research meta-framework.

---

## Part I: The Economic Engine (Viability)

*Focus: Can the protocol pay its bills and independent of speculation?*

### 1. The Business Model Decomposition

Analyze the protocol as a business. It issues liabilities (stablecoins) and holds assets (collateral).

* **Revenue Sources:**
  * **Stability Fees / Interest:** The cost to borrow. (Deep dive: Is this competitive? Is it variable or fixed? Does it cover costs?)
  * **Liquidation Penalties:** Revenue generated from failures. (Warning: high reliance here = predatory model).
  * **Yield on Collateral:** Does the protocol capture yield from underlying assets (e.g., RWA yield, Staking yield)?
  * **Protocol-Owned Liquidity (POL) Returns:** Revenue from AMM positions.
* **Cost Structure:**
  * **User Savings Rate:** Cost paid to stablecoin holders (e.g., DSR).
  * **Incentive Emissions:** Cost of governance tokens emitted to subsidize liquidity. **Critical Metric:** If Emissions > Revenue, the system is bleeding equity to sustain the peg.
  * **Operational Expenses:** Oracle costs, keepers, governance delegations, audits.

### 2. Key Metrics & Health Indicators

* **Net Interest Margin (NIM):** `(Weighted Avg Yield on Assets) - (Weighted Avg Cost of Liabilities)`. Positive NIM is required for long-term survival.
* **Surplus Buffer:** The absolute size of the system's equity cushion (e.g., Maker's Surplus Buffer). How long can the system survive with zero revenue?
* **Cost of Goods Sold (COGS) Equivalent:** The direct cost to mint 1 unit of stablecoin vs the revenue it generates.

---

## Part II: The Sustainability Triangle (Systemic Resilience)

*Focus: How do the core feedback loops interact under stress? Based on the MakerDAO/Sky model.*

### Loop 1: Collateral Quality

* **Asset Composition:** Breakdown by type (Crypto-native, Stablecoins, RWAs).
* **Correlation Risks:** Are the assets correlated with each other? Are they correlated with the governance token? (e.g., internal loops like LUNA).
* **Liquidity Profile:** Can the collateral be sold deep enough in the open market during a crash?

### Loop 2: Incentive Mechanisms

* **Alignment:** Do incentives (fees, penalties) actually encourage the right behavior during a crash?
  * *The Trap:* Raising fees during a crash might force liquidations rather than repayment.
* **Keeper Economics:** Are liquidations profitable for third parties? If gas prices spike 100x (Solana/Ethereum congestion), do keepers still run?

### Loop 3: Governance & Backstop

* **Response Latency:** How fast can the protocol change parameters (Fees, Debt Ceilings)?
  * *Metric:* `Governance Delay` vs `Market Crash Speed`.
* **The Equity Backstop:** In a deficit, how is it covered?
  * *Debt Auctions:* Minting governance tokens (dilution).
  * *Insurance Fund:* Pre-funded reserve.
  * *Haircuts:* Direct loss to stablecoin holders (redeemable at < $1).

---

## Part III: Formal Regime Analysis (The Klages-Mundt Framework)

*Focus: Mathematical bounds of stability based on Klages-Mundt (2023).*

### 1. The Stable Regime (Bounded Variance)

Defined by **Theorem 2.6 (Variance Ordering)**:

* **Condition:** The system remains stable *only* if collateral levels ($N_t$) are sufficient to dampen shocks.
* **Key Insight:** Stability is **path-dependent**. If the system starts with lower collateral (e.g., after a series of bad liquidations), the future price variance is *strictly higher* ($Var(Z_t^s) < Var(Z_t^u)$).
* **Operational Definition:** A regime where small collateral shocks result in bounded, mean-reverting deviations in the stablecoin price ($Z_t$).

### 2. The Unstable Regime (Volatility Amplification)

Defined by **Theorem 2.5 (Sensitivity)**:

* **Volatility Amplification:** When collateral drops below a critical threshold, the sensitivity of the stablecoin price to collateral shocks exceeds 1 ($\partial h / \partial \rho > 1$).
* **Implication:** The stablecoin becomes *more* volatile than the backing asset itself. This characterizes a complete failure of the stabilization mechanism (e.g., "The Variance Explosion").
* **Constraint:** The variance approximation increases by order of $R_t^{-2}$ (inverse square of return), meaning volatility explodes non-linearly as returns approach zero.

### 3. The Submartingale Failure Mode (Deleveraging Spiral)

* **The Hard Constraint:** Stability is mathematically impossible if the collateral price process ($X_t$) is not a **submartingale** ($E[X_{t+1}] \ge X_t$).
* **The Mechanism (Section 2.5.3):**
    1. **Negative Drift:** Speculators expect collateral to fall ($E[X_{t+1}] < X_t$).
    2. **Exit:** Speculators refuse to mint (supply contracts) or exit positions.
    3. **Short Squeeze:** Demand for repayment (to close vaults) remains, but supply vanishes. Stablecoin price rises ($Z_t > 1$).
    4. **Insolvency:** The appreciation of liabilities ($Z_t$) coincident with depreciation of assets ($X_t$) accelerates insolvency faster than linear models predict.
* **Critical Threshold:** The "Stable Region" ceases to exist entirely when expectations turn negative, regardless of current overcollateralization.

---

## Part IV: Operational & Regulatory Sustainability

*Focus: External existential threats.*

### 1. Operational Bottlenecks

* **Oracle Infrastructure:** Reliance on centralized feeds (Chainlink) vs internal. Latency risks.
* **Auction Throughput:** Capacity of the system to process concurrent liquidations. (e.g., MakerDAO Black Thursday congestion).

### 2. Regulatory Survivability (The Moat)

* **Censorship Resistance:** Can the protocol freeze assets? (USDC dependency).
* **MiCA/Compliance Cost:** If regulations require capital buffers (e.g., 2% equity), can the protocol afford it?
* **Off-Ramp Dependency:** Does the system rely on specific banking partners that could be de-banked?

---

## Writing Guidelines for the Article

1. **Evidence-Based:** Do not trust whitepapers. Use on-chain data (Dune, Etherscan) to verify revenue and collateral claims.
2. **Comparative Context:** Always benchmark the subject against a standard (e.g., "Unlike LUSD's immutable governance, X uses...").
3. **Visuals:**
    * *Revenue vs Expenses Chart (Historical)*.
    * *Collateral Composition (Risk Weighted)*.
    * *The Sustainability Triangle Diagram*.
4. **Tone:** rigorously analytical, skeptical, institutional-grade. Avoid marketing fluff.

## Recommended References

* **General:** `Analysis-Meta-framework.md` (Pillar II).
* **Case Study:** `analysis/makerdao/DAI_1&2/Updated Part II Sustainability When Stability Has to Pay for Itself.md` (for deep dive on Regime Boundaries).
* **Theoretical:** Klages-Mundt & Minca papers (for Deleveraging Spirals).
