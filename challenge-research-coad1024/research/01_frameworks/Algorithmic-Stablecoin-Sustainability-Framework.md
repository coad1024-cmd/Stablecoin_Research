# Framework for Analysis: Sustainability of Algorithmic Stablecoins

**Version:** 2.0 (Hybrid: LEGO + Operational)  
**Date:** January 2026  
**Scope:** Algorithmic (endogenous) stablecoins without external collateral  
**Based On:** Stablecoin LEGO Framework (arXiv:2506.17622v1) + Operational Bottleneck Analysis

> [!IMPORTANT]
> This framework is designed for **algorithmic stablecoins** (e.g., Terra UST, AMPL, FRAX algorithmic portion). For overcollateralized stablecoins (DAI, LUSD), use `Stablecoin-Sustainability-Framework.md`.

---

## Claim Classification

| Type | Definition | Verification |
|------|-----------|--------------|
| **A** | On-chain verifiable | Direct contract query |
| **A'** | External verifiable | API/web with date |
| **B** | Derived with assumptions | Calculated from A + A' |
| **C** | Interpretive judgment | Structural classification |
| **D** | Labeled scenario | Not predictions |

---

## Part I: Dynamic Risk Model (Stablecoin LEGO)

*Source: arXiv:2506.17622v1*

### 1.1 System State Equation

```
dS(t)/dt = f(UP(t), DN(t), Internal)
```

Where:

- **S(t)** = Stablecoin state (market cap, peg deviation)
- **UP(t)** = Upstream risk factors (external threats)
- **DN(t)** = Downstream ecosystem composition

### 1.2 Upstream Risk Factors (UP(t))

| Risk Category | Impact Objects | Data Source |
|--------------|----------------|-------------|
| **Price Fluctuation** | Peg deviation, collateral volatility | CoinGecko, on-chain |
| **Smart Contract** | Audit status, past exploits | Audit reports, rekt.news |
| **Peripheral Factors** | Oracle, governance, custody | Contract analysis |

**Scoring:** `UP(t) = Σ wₖ × mₖ(t)` where wₖ = weight, mₖ = metric value

### 1.3 Downstream Ecosystem (DN(t))

Analyze top 1000 holders to determine **risk archetype**:

| Archetype | Concentration | Primary Risk | Example |
|-----------|--------------|--------------|---------|
| **DeFi-Centric** | >90% in DeFi | Contagion cascade | UST/Anchor |
| **Exchange-Centric** | >90% on CEXs | Custodial/counterparty | FDUSD |
| **Whale-Dominated** | >90% in whale wallets | Bank run by few actors | TUSD |
| **Diversified** | <70% any category | Distributed risk | USDC |

---

## Part II: Business Model Decomposition

### 2.1 Revenue Sources

| Source | Description | For Algo Stables |
|--------|-------------|------------------|
| **Seigniorage** | Mint/burn spread | Primary revenue |
| **Yield Subsidy** | External yield offered to holders | Often unsustainable |
| **Protocol Fees** | Transaction/swap fees | Secondary |

### 2.2 Cost Structure

| Cost | Description | Death Spiral Indicator |
|------|-------------|----------------------|
| **Redemption Dilution** | Backstop token minting | If accelerating: G > 1 |
| **Yield Burn** | Subsidy costs | If Yield > Revenue: unsustainable |
| **Operational** | Gas, keepers, legal | Fixed drain |

### 2.3 Sustainability Test

```
Sustainability Score = Revenue - Costs - Dilution
```

| Score | Status |
|-------|--------|
| Positive | Self-sustaining |
| Negative but covered by reserves | Runway limited |
| Negative with no reserves | Dead on arrival |

---

## Part III: Key Metrics

### 3.1 Reflexivity Gain (G)

**The death spiral detector.**

```
G = (ΔBackstopSupply / ΔRedemptions) × (ΔBackstopPrice / ΔBackstopSupply)
```

| G Value | Regime | Outcome |
|---------|--------|---------|
| G < 1 | Stabilizing | Recoverable |
| G = 1 | Neutral | Edge of collapse |
| G > 1 | Destabilizing | Death spiral inevitable |

### 3.2 Exit Coverage Ratio (XCR)

```
XCR = Available Liquidity / Stress Exit Demand
```

| XCR | Interpretation |
|-----|----------------|
| > 2 | Orderly exits possible |
| 1-2 | Limited capacity |
| < 1 | Disorderly exit regime |

### 3.3 Demand Concentration (DC)

```
DC = (TVL in Top Protocol / Total Stablecoin Demand) × 100%
```

| DC | Risk Level |
|----|------------|
| < 30% | Diversified |
| 30-70% | Concentrated |
| > 70% | **Critical**: Single point of failure |

*Terra Example: Anchor = ~72% of UST demand. When Anchor's 20% APY became unsustainable, UST died.*

---

## Part IV: Operational Bottlenecks

### 4.1 Oracle Latency

| Metric | Formula | Alert |
|--------|---------|-------|
| Bias | (Oracle - Market) / Market | > 5% |
| Lag | Time difference | > 30s during volatility |

### 4.2 Redemption Friction

| Condition | Problem |
|-----------|---------|
| On-chain cost > Exchange cost | Arbitrage disabled, death spiral accelerates |
| Spread > 10% at volume | Exit blocked, panic intensifies |

### 4.3 Endogenous Backstop Collapse

| Signal | Meaning |
|--------|---------|
| Mint velocity >> historical | Run in progress |
| Backstop price inversely correlated with supply | Reflexivity confirmed |

---

## Part V: Stress Tests

### Test 1: Bank Run (10% Supply Exit / 24h)

| Metric | Pass | Fail |
|--------|------|------|
| Spread escalation | < 20% | > 50% |
| Backstop supply increase | < 50% | > 200% |
| G value | < 1 | > 1 |

### Test 2: Yield Collapse

**Scenario:** Primary yield source (e.g., Anchor) drops to 0%.

| Metric | Pass | Fail |
|--------|------|------|
| Demand retention | > 50% | < 20% |
| Price within 1 week | > $0.95 | < $0.80 |

### Test 3: Oracle Manipulation (5-min 30% lag)

| Metric | Pass | Fail |
|--------|------|------|
| Extractable value | < 1% TVL | > 5% TVL |
| Circuit breaker | Triggers | None |

---

## Part VI: Final Verdict Scorecard

| Dimension | Weight | Metrics |
|-----------|--------|---------|
| **Upstream Risk (UP)** | 25% | Contract security, oracle, price stability |
| **Downstream Risk (DN)** | 25% | Holder concentration, DeFi exposure |
| **Reflexivity (G)** | 25% | Death spiral dynamics |
| **Operations (OP)** | 25% | Oracle latency, redemption friction |

**Composite Rating:**

- 🟢 **Robust**: All dimensions pass stress tests
- 🟡 **Moderate**: 1-2 failures, survivable with fixes
- 🔴 **Critical**: 3+ failures, not sustainable

---

## References

<span id="ref-lego-sok"></span>Liu, Z., et al. (2025). *[SoK: Stablecoin Designs, Risks, and the Stablecoin LEGO](https://arxiv.org/abs/2506.17622)*. arXiv:2506.17622.

<span id="ref-klages"></span>Klages-Mundt, A., & Minca, A. (2022). *[While Stability Lasts: A Stochastic Model of Non-Custodial Stablecoins](https://arxiv.org/abs/2004.01304)*. arXiv:2004.01304.

<span id="ref-calandra"></span>Calandra, F., et al. (2023). *[Algorithmic Stablecoins: A Simulator for the Dual-Token Model](https://ieeexplore.ieee.org/document/11114693)*. IEEE Access.
