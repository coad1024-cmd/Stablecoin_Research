# Stablecoin Sustainability Framework (Legacy Version 1.0)

**Version:** 1.0 (Pre-Standardization)
**Status:** Deprecated (See V2.0 for Canonical)

---

## Purpose

This document provides a comprehensive framework for writing a **Sustainability Analysis Article** for any overcollateralized stablecoin (e.g., LUSD, RAI, DAI). "Sustainability" here is defined not just as current solvency, but as the system's ability to survive and persist over the long term through market cycles, regulatory shifts, and economic stress.

This framework synthesizes the **"Sustainability Triangle"** model (interacting feedback loops) with the **"Dual Mandate"** concept (profit vs. stability) from the broader research meta-framework.

---

## Part I: The Economic Engine (Viability)

*Focus: Can the protocol pay its bills and independent of speculation?*

## Comparison Methodology

This framework generates individual sustainability profiles that can be synthesized into comparative insights.

### Analysis Dimensions

**Dimension 1: Economic Viability**
- Revenue model classification and sustainability ratios
- Cost structure and capital efficiency
- Dependency on speculative vs organic demand

**Dimension 2: Collateral Regime Stability**
- Asset composition and concentration risk
- Liquidation mechanism robustness
- Reflexivity and internal collateral loops

**Dimension 3: Governance & Adaptability**
- Parameter mutability and response speed
- Governance concentration and attack surface
- Crisis response mechanisms

### 1. The Business Model Decomposition

Analyze the protocol as a business. It issues liabilities (stablecoins) and holds assets (collateral).

* **Revenue Sources:**
  * **Stability Fees / Interest:** The cost to borrow.
  * **Liquidation Penalties:** Revenue generated from failures.
  * **Yield on Collateral:** Does the protocol capture yield from underlying assets?
  * **Protocol-Owned Liquidity (POL) Returns:** Revenue from AMM positions.
* **Cost Structure:**
  * **User Savings Rate:** Cost paid to stablecoin holders.
  * **Incentive Emissions:** Cost of governance tokens emitted to subsidize liquidity.

### 2. Key Metrics & Health Indicators

#### A. Liquidation Dependency Ratio (LDR)

**Critical Metric for Sustainability:**
```
LDR = Liquidation Revenue / Total Revenue
```
- **LDR > 0.5** = High dependency
- **LDR < 0.2** = Low dependency

#### B. Net Interest Margin (NIM)

```
NIM = (Weighted Avg Yield on Assets) - (Weighted Avg Cost of Liabilities)
```

#### C. Collateral Concentration (Herfindahl Index)

```
HHI = Σ(share_i)²
```

#### D. Surplus Buffer Runway

```
Runway (months) = Surplus Buffer / Monthly Operating Costs
```

---

## Part II: The Sustainability Triangle (Systemic Resilience)

*Focus: How do the core feedback loops interact under stress?*

### Loop 1: Collateral Quality
* Asset Composition Breakdown.
* Correlation Risks.

### Loop 2: Incentive Mechanisms
* Alignment of fees during crashes.
* Keeper Economics robustness.

### Loop 3: Governance & Backstop
* Response Latency vs Market Crash Speed.
* The Equity Backstop (Minting/Dilution).

---

## Part III: Stress Test Framework (Operational Bounds)

Test each protocol against historical stress scenarios.

1.  **Test 1: The 70% Collateral Crash** (Black Thursday Equivalent).
2.  **Test 2: The Liquidity Freeze** (FTX/3AC Equivalent).
3.  **Test 3: The Collateral Contagion** (USDC Depeg Equivalent).

**Evaluation Criteria:**
- ✅ **Robust:** Survived with <1% bad debt, peg ±2%.
- ⚠️ **Degraded:** Survived with 1-5% bad debt.
- ❌ **Failed:** >5% bad debt or permanent peg break.

---

## Part IV: Operational & Regulatory Sustainability

### 1. Operational Bottlenecks
* Oracle Infrastructure Risks.
* Auction Throughput Capacity.

### 2. Regulatory Survivability
* Censorship Resistance (USDC dependency).
* Compliance Cost (MiCA capital buffers).
* Off-Ramp Dependency.

---

## Part V: Comparative Synthesis Guidelines

### Type Classification
* **Type A:** Liquidation-Dependent (>30% revenue).
* **Type B:** Yield-Capturing (>50% yield).
* **Type C:** Fee-Based (>50% fees).
* **Type D:** Subsidized (Emissions > Revenue).

### Conclusion
Map the viable design space:
* Which approaches are fundamentally viable?
* What tradeoffs are inevitable?
