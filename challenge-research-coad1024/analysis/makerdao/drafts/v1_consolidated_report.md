# MakerDAO (Sky Ecosystem): A Comprehensive Analysis of Solvency, Sustainability, and Decentralization

## Executive Summary

This report consolidates a three-part analysis of the Sky Ecosystem (formerly MakerDAO), evaluating its architecture through the lenses of mechanical solvency, economic sustainability, and operational decentralization.

**Verdict:** Sky is a **hybrid entity**. It has successfully transitioned from a pure crypto-collateralized protocol to a diversified, solvency-focused central bank. However, this transition has come at the cost of decentralization, introducing significant custodial and regulatory dependencies that are not fully mitigated by its governance structure.

---

# Part I: The Mechanics of Solvency (Backing)

*How the system guarantees value on-chain.*

## 1. The Core Accounting Layer

The foundation of Sky's solvency is the **Vat** contract, which maintains a single source of truth for all collateral (`ink`) and debt (`art`). The system enforces a fundamental invariant:

$$ \text{ink} \times \text{spot} \ge \text{art} \times \text{rate} $$

Where:

* `ink`: Locked collateral balance.
* `spot`: Collateral price (safety-adjusted).
* `art`: Normalized debt.
* `rate`: Cumulative interest index.

This invariant is deterministic. If it is violated, the system triggers **liquidation** (the `Dog` contract), confiscating collateral to cover the debt.

## 2. The Evolution of Collateral

Sky has evolved through three distinct backing eras:

1. **Pure Crypto (2017-2020):** ETH-only. Trustless but volatile. Failed during Black Thursday (March 2020) due to correlation risk.
2. **Emergency Hybrid (2020-2023):** Heavy reliance on USDC (up to 60%) via the Peg Stability Module (PSM). Stabilized the peg but introduced custodial risk (SVB crisis).
3. **Endgame Maturity (2025):** A diversified portfolio approach.
    * **Crypto (38%):** ETH, WBTC (Trustless, Volatile).
    * **Stablecoins (22%):** USDC (Custodial, Stable).
    * **RWAs (14%):** T-bills, Bonds (Off-chain, Yield-bearing).

**Critique:** The "backed" claim is now heterogeneous. "Backing" means different things for ETH (on-chain value) vs. RWA (legal claim). The system is no longer trustless; it is a **managed portfolio of risks**.

## 3. Terminal Solvency: Global Settlement

Unlike algorithmic stablecoins (e.g., Terra), Sky has a deterministic "end game." **Global Settlement** freezes the system and allows DAI holders to redeem collateral pro-rata. This provides a **terminal value floor**, ensuring DAI is a claim on assets, not just faith.

---

# Part II: The Economics of Sustainability

*Can the system survive repeated stress?*

## 1. The Sustainability Triangle

Solvency is not enough; the system must be sustainable. This requires balancing three feedback loops:

1. **Collateral Quality:** Volatility and liquidity constraints.
2. **Incentives:** Stability fees and auction efficiency.
3. **Governance:** Emergency response and parameter tuning.

**The Bottleneck:** During crises (e.g., Black Thursday), these loops can invert. Collateral crashes, auctions fail due to network congestion, and governance is too slow to react.

## 2. Regime Transitions (Klages-Mundt Framework)

Formal analysis reveals two distinct regimes:

* **Stable Regime (Submartingale):** Collateral is expected to hold value. Liquidations work.
* **Unstable Regime (Supermartingale):** Collateral crashes. Deleveraging spirals occur (DAI price rises as collateral falls).

**Critical Insight:** The transition happens when leverage is too high relative to liquidity. Sky's "Endgame" widens the stable region by diversifying into uncorrelated assets (RWAs) and using the PSM as a buffer.

## 3. The Cost of Stability

The PSM (USDC backing) solved the Black Thursday liquidity crisis but introduced a new cost: **Revenue Opportunity Cost**.

* Vaults pay ~3-5% fees.
* PSM pays ~0% fees.
* **Result:** 22% of supply (PSM) generates minimal revenue.
* **Mitigation:** RWAs (T-bills) are the new yield engine, generating ~$50M/year to fund surplus and buybacks.

**Critique:** Sky has effectively become a **tokenized hedge fund**. It takes USDC deposits, buys T-bills, and keeps the spread. This is a viable business model, but it is fundamentally different from the original "decentralized credit facility" vision.

---

# Part III: The Reality of Decentralization

*Who actually controls the system?*

## 1. Governance Centralization (Score: 1/5)

* **Inequality:** Gini coefficient of **0.99**. Top 1% hold 90% of MKR.
* **Delegation:** Top 5 delegates control **99%** of voting power.
* **Verdict:** Governance is a **plutocracy**. A single entity or coalition can unilaterally dictate protocol changes.

## 2. Collateral Centralization (Score: 1.5/5)

* **Custodial Risk:** ~74% of backing (USDC + RWAs) depends on off-chain entities (Circle, Coinbase, Custodians).
* **Censorship Risk:** Regulators can freeze 74% of the collateral book.
* **Verdict:** DAI is **not censorship-resistant**. It inherits the regulatory surface area of its underlying assets.

## 3. Operational Decentralization (Score: 2.5/5)

* **Keepers:** Healthy diversity (HHI 1136). Liquidations are competitive.
* **Oracles:** Heavy reliance on Chainlink (>90%). A single point of failure.
* **Verdict:** The "machinery" (liquidations) is decentralized, but the "inputs" (oracles, assets) are not.

---

# Final Conclusion

Sky (MakerDAO) has evolved into a **robust, solvent, but centralized** financial infrastructure.

* **Strengths:**
  * **Proven Solvency:** Survived Black Thursday and SVB.
  * **Economic Sustainability:** RWA yields provide a sustainable revenue model.
  * **Terminal Safety:** Global Settlement guarantees a value floor.

* **Weaknesses:**
  * **Governance Capture:** Extreme centralization of voting power.
  * **Regulatory Exposure:** Heavy dependence on US-domiciled assets (USDC, T-bills).
  * **Identity Crisis:** It is no longer "decentralized money" in the purist sense; it is **on-chain commercial banking**.

**Recommendation:** Users should treat DAI as a **transparent, over-collateralized stablecoin**, but NOT as a censorship-resistant store of value comparable to Bitcoin or LUSD.
