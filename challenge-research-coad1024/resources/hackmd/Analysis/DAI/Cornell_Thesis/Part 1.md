
### **Part I**

**Sections 1–3**

1. Orientation
2. Definitions
3. Dimensions of Sustainability (7 dimensions minimum)

### **Part II**

**Sections 4–6**
4. Metrics, Models, Critical Conditions
5. Design Patterns & Anti-Patterns
6. Assumption Audit & Robustness

### **Part III**

**Sections 7–9**
7. Document-specific vs Generalizable Insights
8. Conceptual Map (ASCII included)
9. Top Non-Obvious Insights (ranked)

### **Part IV**

**Extra Tasks**

1. Math & notation audit
2. Tests & simulation experiments
3. 10-item actionable checklist for protocol teams

---

# ✅ Proceeding with **Part I now: Sections 1–3**

---

# **1. Orientation**

## **1.1 Main purpose of the dissertation**

The dissertation aims to develop **formal, mathematical, and computational frameworks** to understand:

1. **Stablecoin stability and instability**, especially deleveraging spirals, endogenous price feedbacks, and speculator incentives (Ch.2–4).
   – e.g., “deleveraging spirals… lead to faster collateral drawdown” (Ch.2, p.59)
2. **Network-wide financial contagion**, cascading failures, and sensitivity under uncertainty (Ch.5–7).
   – e.g., “agents in economic networks face intrinsic uncertainty… small uncertainties can lead to huge uncertainties about risks” (Ch.7, p.330).

It bridges **cryptoeconomics**, **monetary theory**, **financial network analysis**, and **algorithmic design**, with emphasis on *rigorous characterization* of stable/unstable regimes.

## **1.2 Primary audience and context**

The thesis is written for:

* **Protocol designers** building non-custodial stablecoins
* **Regulators and financial stability policymakers**
* **Researchers** applying stochastic processes, network theory, and economic modeling

The work is explicitly *theory + simulation + algorithmics*: stochastic models (Ch.2), dynamic models & attacks (Ch.3), capital-structure economics (Ch.4), contagion fixed points (Ch.5), algorithmic interventions (Ch.6), and perturbation bounds (Ch.7).

## **1.3 Core thesis re: stablecoins and sustainability**

### **Thesis (textual evidence)**

Across Ch.2–4, the dissertation argues that *non-custodial stablecoin stability is contingent and fragile*, because price dynamics, liquidation processes, and collateral feedbacks create **domains of stable vs unstable behavior**:

* “We formally characterize domains that can be interpreted as stable and unstable” (Ch.2, p.59).
* “These deleveraging spirals… lead to faster collateral drawdown… and higher price variance” (Ch.2, p.59).
* “Stablecoins… exhibit significantly volatility… modeling reveals unique risks” (Ch.4, p.141–142).

### **Mapping to sustainability**

**Stablecoin sustainability**, in this context, means **the design’s ability to maintain solvency, peg stability, and functioning incentives across shocks**, without relying on discretionary external support.

The dissertation shows that sustainability requires:

* **Robust collateralization dynamics** resistant to deleveraging
* **Governance and oracle structures** that prevent manipulation
* **Network-level resilience** when embedded in broader DeFi ecosystems
* **Incentive compatibility across agents** (issuers, holders, liquidators, miners)

Sustainability is *not* inherent—there are parameter domains where the same system becomes unstable.

---

# **2. Definitions (explicit + implicit)**

The dissertation rarely uses the term “sustainability” explicitly for stablecoins. Instead, it uses terms like *stability*, *resilience*, *solvency*, *liquidity*, *incentive security*, *economic stability* (Ch.4 §4.5).

Below, I extract explicit text + inferred definitions.

---

## **2.1 Explicit definitions/uses**

### **Stability / Stable Domain**

* “We formally characterize domains that can be interpreted as stable and unstable” (Ch.2 p.59).
* “Stablecoin behaves in a stable way when restricted to a certain region” (Ch.2 p.59).

### **Instability**

* “Price variance is distinctly greater in the unstable domain” (Ch.2 p.59).

### **Solvency / Collateral shortfall**

* “Faster collateral drawdown, and potentially shortfalls” (Ch.2 p.59).

### **Liquidity**

* “Liquidity problems from deleveraging… drying of stablecoin liquidity” (Ch.4 p.157).

### **Incentive Security** *(explicitly defined)*

Ch.4, Question 4.1:

> “Is there mutually profitable continued participation across all required parties?” (Ch.4 p.158).

### **Economic Stability** *(explicitly defined)*

Ch.4, Question 4.2:

> “Do the incentives actually lead to stable outcomes?” (Ch.4 p.158).

---

## **2.2 Implicit definitions (inferred with citations)**

Derived from models and simulations:

### **Sustainability ≈ persistence of solvency + peg-fitting incentives across shocks**

**Evidence:**

* “Deleveraging spirals… resemble short squeezes… lead to faster collateral drawdown… higher variance” (Ch.2 p.59). → sustainability requires avoiding deleveraging regions.

### **Sustainability = bounded price variance**

In Ch.2, stable domain has bounded quadratic variation; unstable domain does not.
**Inference from:** formal bounds on large deviations (Ch.2 §2.5) and submartingale spirals.

### **Sustainability = no profitable attacks that break peg or incentives**

**Evidence:**

* Ch.3 describes “profitable arbitrage-like attacks… may induce volatility… risks to blockchain consensus” (Ch.3 p.78).

### **Sustainability = governance solvability** (no cycles, no manipulation)

**Evidence:**

* Governance attacks and oracle manipulation discussed in Ch.4 (Sec 4.3.3).
* Network governance failures highlighted in Ch.5 Remark 5.1 (p.235).

### **Sustainability = low sensitivity to parameter/structure errors**

**Evidence:**

* “small uncertainties can lead to huge uncertainties… high sensitivity” (Ch.7 p.330).

---

## **2.3 Synthesized working definition**

### **Working Definition: Sustainability in a stablecoin (per dissertation)**

**A stablecoin is sustainable if it maintains solvency, stable pricing, and incentive-compatible participation across shocks, with bounded sensitivity to market and network perturbations.**

This definition incorporates all the required dimensions because the dissertation repeatedly shows systems fail when *any* of these break.

---

## **2.4 Necessary conditions (derived from dissertation)**

### **Condition 1 — Incentive feasibility across agents**

*All required parties (speculators, holders, liquidators, miners, governors) must have profitable continued participation.*
— Based on explicit Question 4.1 (Ch.4 p.158).

### **Condition 2 — Avoidance of deleveraging unstable domain**

*Collateralization, liquidity, and demand elasticity must keep the system in the “stable domain” where large deviations are bounded.*
— From Ch.2 stable vs unstable domains (p.59).

### **Condition 3 — Robustness to cascading failures and parameter uncertainty**

*Risk propagation in the wider DeFi network must remain bounded and not amplify minor shocks.*
— From Ch.5–7 on cascades and high sensitivity (Ch.7 p.330).

---

# **3. Dimensions of Sustainability**

For each dimension, I provide:
(1) short name, (2) role, (3) mechanisms/tradeoffs, (4) citations from the dissertation.

The structure maps the dissertation’s terminology to the 7 required dimensions.

---

## **3.1 Economic / Financial Sustainability**

### **Role**

Ensures collateralization, liquidation mechanics, leverage decisions, and market clearing dynamics produce solvency and bounded risk.

### **Mechanisms**

* Over-collateralization factor **β** and speculator decisions (Ch.2 §2.2).
* Endogenous stablecoin price dynamics affecting liquidation cost (Ch.2 §2.5).
* Liquidation feedback loops and cost > $1 (Ch.2 p.59).
* Deleveraging spirals (submartingale) causing collateral drawdown.

### **Key tradeoffs**

* Higher β reduces risk but lowers capital efficiency.
* Lower elasticity or liquidity increases instability probability.
* Liquidation design shifts risk between holders vs speculators.

### **Citations**

Ch.2 pp.12–60; Ch.4 §4.2–4.4.

---

## **3.2 Peg / Market Stability**

### **Role**

Maintains stablecoin price near $1 with bounded variance.

### **Mechanisms**

* Speculative issuance ∆t and endogenous price Zt (Ch.2 §2.2).
* Liquidity drying in crisis (Ch.3 §3.1).
* Price variance bounds in stable vs unstable domain (Ch.2 §2.5).
* Attacks exploiting liquidation auctions (Ch.3 p.78).

### **Tradeoffs**

* Higher demand elasticity stabilizes price but requires off-chain liquidity.
* More speculators → more resilience but correlated shocks can wipe them out.

---

## **3.3 Risk & Shock Absorption**

### **Role**

Absorbs volatility in collateral markets without triggering spirals.

### **Mechanisms**

* Speculator’s optimal collateral decision increases with volatility (Ch.2 p.59).
* Endogenous collateral fire-sale risk (Ch.2 §2.6).
* Liquidity + liquidation mechanics (Ch.4 p.157).

### **Tradeoffs**

* Risk transferred between stablecoin holders, speculators, miners.
* More automatic liquidation = faster deleveraging but less insolvency risk.

---

## **3.4 Governance & Institutional Sustainability**

### **Role**

Ensures oracle correctness, liquidation rules, settlement processes, and governance decisions remain stable under manipulation.

### **Mechanisms**

* Governance-based global settlement (Ch.2 §2.2).
* Oracle manipulation risks (Ch.4 §4.3.3).
* Multi-solution governance disputes (Ch.5 Remark 5.1, p.235).

### **Tradeoffs**

* Decentralization vs speed/efficiency.
* More algorithmic rules → less flexibility but more predictable.

---

## **3.5 Technical / Operational Sustainability**

### **Role**

Handles transaction congestion, auction execution, and system-level throughput during crises.

### **Mechanisms**

* Congestion leads to failed liquidations (Ch.2 §2.2, p.22–23).
* Mempool manipulation causing near-zero liquidation prices (Ch.3 p.78).
* On-chain execution delays cause liquidity mismatch.

### **Tradeoffs**

* More complex auctions vs latency
* Liveness vs safety constraints

---

## **3.6 Ecosystem & Adoption Sustainability**

### **Role**

Stablecoin must remain useful and integrated in DeFi ecosystems.

### **Mechanisms**

* STBL demand elasticity (Ch.2 §2.2).
* Collateral correlations across DeFi (Ch.4 §4.5).
* Network contagion via lending, DEXs (Ch.4 §4.5.4).

### **Tradeoffs**

* Network effects increase adoption but amplify contagion.
* Integrations create “sticky” demand but reduce liquidity mobility.

---

## **3.7 Regulatory & Legal Sustainability**

### **Role**

Considers regulatory compatibility, legal clarity of custodial vs non-custodial structures, and systemic risk considerations.

### **Mechanisms**

* Custodial stablecoins resemble money market funds/narrow banks (Ch.4 §4.2).
* Regulatory stability risks discussed in Ch.4 introduction (citing [3]) (Ch.4 p.141).
* Endogenous collateral systems risk being classified as unregistered money-like liabilities.

### **Tradeoffs**

* Compliance increases trust but reduces decentralization.
* Full decentralization reduces legal clarity but protects censorship resistance.

---
