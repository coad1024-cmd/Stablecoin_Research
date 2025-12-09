
---

# ✅ Meta-Framework for Comparative Analysis (over-collateralized stablecoins)

**Scoring:** each metric 0–10 (10 = most resilient / decentralized / desirable). State measurement assumptions.

---

## 1. Collateral Exogeneity

**Definition:** How independent collateral value is from the protocol’s own economics.
**Why it matters:** Prevents recursive collapse.
**Measure:** 10 = major market asset (ETH, BTC); 0 = endogenous (protocol token).

---

## 2. Collateral Liquidity & Depth

**Definition:** USD liquidity available for the collateral near 1% slippage.
**Why it matters:** Determines price impact during liquidations.
**Measure:** Map measured liquidity bands to 0–10 (document source & snapshot time).

---

## 3. Redemption Elasticity

**Definition:** Protocol-level ability to convert stablecoin → collateral/value on-chain.
**Why it matters:** Provides a protocol-enforced price floor.
**Measure:** 10 = guaranteed 1:1 on-chain redemption; 0 = market-only peg maintenance.

---

## 4. Deleveraging Resilience

**Definition:** How well the system absorbs sharp collateral shocks without system-wide insolvency.
**Why it matters:** Tests Black-Thursday style scenarios.
**Measure checklist (score by completeness & speed): presence of stability pool(s), instant offset vs auction speed, branch/market isolation, circuit breakers.

---

## 5. Oracle Robustness

**Definition:** Price-feed diversity, aggregation, and anti-manipulation logic.
**Why it matters:** Price data integrity is first-order for collateralized systems.
**Measure:** Count independent sources, aggregation method, fallback logic, circuit breakers → convert to 0–10.

---

## 6. Governance Centralization

**Definition:** Degree to which a small set of actors can alter protocol state, emergency parameters, or execution paths. *Higher score = more decentralized.*
**Why it matters:** Centralized emergency control can create moral hazard, censorship risk, and governance-latency failure modes.

**Measurement (quantitative + qualitative):**

* **Voting concentration:** top-10 / top-50 token holder %; compute Gini coefficient of voting token. (Quantitative)
* **Emergency power scope:** existence of multisig / timelock / pause roles and exact powers (list them). (Qualitative→mapped to 0–10)
* **Upgradeability surface:** whether core contracts are proxyable and how upgrades are authorized (multi-sig, governance vote, timelock). (Qualitative→mapped)
* **Operational dependence on off-chain actors:** are key ops (oracle relayers, keeper registries) subject to centralized operators? (Qualitative)

**Scoring rules (examples):**

* 9–10: Immutable core logic OR upgrade path requires broad, dispersed quorum + long timelock; emergency powers extremely constrained.
* 6–8: Upgrades via governance with measurable token dispersion; emergency multisig exists but tightly constrained and public.
* 3–5: Large holders dominate votes; short timelocks; emergency multisig with broad powers.
* 0–2: Small set of addresses can unilaterally change core parameters or drain/ pause funds.

*(Document the exact data sources and compute the numeric parts; map the qualitative findings to numeric scores with brief justification.)*

---

## 7. Loss-Absorption Mechanisms

**Definition:** Size & efficacy of buffers that soak up bad debt (stability pools, surplus, reserve tranches).
**Why it matters:** Prevents socialization and insolvency.
**Measure:** Relative buffer size vs system debt, speed of deployment, and size of junior tranche / auction recovery potential.

---

## 8. Operational Transparency & Auditability

**Definition:** On-chain verifiability of reserves, published audits, and parameter visibility.
**Why it matters:** Transparency reduces panic, supports market arbitrage, and enables reproducible stress tests.
**Measure:** 10 = realtime on-chain proofs + public audits + open dashboards; 0 = opaque custodial attestations only.

---

# How to use this framework (practical)

1. For each protocol, compute/collect:

   * on-chain liquidity snapshots (for metric 2),
   * token distribution & top holder shares (for 6),
   * stability pool sizes, reserve numbers (for 7),
   * oracle feed lists and aggregation method (for 5).
2. Map raw numbers → 0–10 with explicit banding rules (e.g., liquidity > $200M@1% → 10; $100M → 8; etc.).
3. Provide a 1–2 line justification for each score (so graders can audit).
4. Produce a radar chart + a compact table for the submission.

---
