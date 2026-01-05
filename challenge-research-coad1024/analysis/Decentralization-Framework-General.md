Below is a **formal, protocol-agnostic section template** you can drop directly into a research paper, report, or long-form article.

It is written to be:

* **Reusable** across Terra, Maker, Liquity, FRAX, etc.
* **Stress-aware** (not ideology-driven)
* **Auditable** (forces metrics, data, and thresholds)
* **Submission-ready** (academic / policy / protocol review)

You can copy-paste this and then fill in values per protocol.

---

# X. Decentralization Analysis Framework for Stablecoin Protocols

## Methodological Premise

> **Decentralization is evaluated as control distribution under adversarial conditions, not as architectural intent in steady state.**

This section assesses decentralization as a **state-dependent property** of the system, focusing on who retains **decision authority, execution power, and control over redemption outcomes** during periods of market stress.

A protocol may appear decentralized under normal conditions while exhibiting strong centralization when volatility, liquidity shocks, or governance urgency arise. This analysis explicitly targets those regimes.

---

## Dimensions of Decentralization

Decentralization is decomposed into **four orthogonal dimensions**. Failure or concentration in any single dimension compromises the system’s effective decentralization.

Let the decentralization state be represented as a vector:

[
D = (G, B, O, C)
]

Where:

* **G** = Governance decentralization
* **B** = Backing (Collateral) decentralization
* **O** = Operational decentralization
* **C** = Control-path decentralization

Each dimension is evaluated independently.

---

## 1. Governance Decentralization (G)

**Question:**
Who can modify protocol parameters, alter redemption rules, onboard/remove collateral, or trigger emergency actions?

### Metrics

* Voting power distribution (Gini coefficient)
* Top-N concentration (% of voting power held by top 5 / 10 / 20 addresses)
* Delegate concentration (if delegation exists)
* Voter participation rate
* Governance latency:

  * Proposal submission → execution
  * Emergency vs standard governance paths

### Stress Interpretation

Governance is considered **operationally centralized** if:

* A small coalition can unilaterally pass or block critical changes, or
* Governance latency exceeds the timescale of a crisis (minutes–hours).

> Governance that cannot act within the crisis half-life does not meaningfully contribute to decentralization under stress.

---

## 2. Backing / Collateral Decentralization (B)

**Question:**
What ultimately backs redemptions, and how independent are those backing sources?

### Metrics

* Collateral composition (% by asset class)
* Concentration ratio (HHI over collateral types)
* Counterparty exposure:

  * Number of issuers
  * Number of custodians / legal entities
* Correlation structure:

  * Corr(collateral value, stablecoin demand)
* Endogenous vs exogenous backing share

### Stress Assumption

* **Endogenous assets** (protocol-issued or reflexive assets) are assumed to contribute **zero effective backing** during systemic stress.

### Stress Interpretation

Backing is considered centralized if:

* A small number of off-chain entities control redemption-critical assets, or
* Collateral assets fail simultaneously due to correlation or regulatory action.

---

## 3. Operational Decentralization (O)

**Question:**
Who actually executes liquidations, arbitrage, price discovery, and peg defense in real time?

### Components Evaluated

* **Price Oracles**

  * Number of independent oracle sources
  * Source overlap (shared exchanges or feeds)
  * Update frequency vs observed volatility
* **Liquidity Executors**

  * Liquidators / keepers / arbitrageurs
  * Volume share of top N executors
* **Infrastructure Dependencies**

  * Reliance on specific chains, bridges, APIs, or CEXs

### Metrics

* Oracle concentration and latency
* Executor concentration during stress periods
* Liquidity venue concentration

### Stress Interpretation

Operational decentralization collapses if:

* Execution power concentrates into a small set of professional actors, or
* Oracle freshness fails to keep pace with market movements.

> Under stress, execution centralizes faster than governance.

---

## 4. Control-Path Decentralization (C)

**Question:**
Who can halt, override, or reconfigure the system during emergencies?

### Metrics

* Existence of emergency controls (pause, shutdown, guardians)
* Number of signers / keys required
* Human discretion vs automated triggers
* Transparency and accountability of emergency actions

### Stress Interpretation

A protocol is **control-centralized** if:

* Emergency powers concentrate in a committee, foundation, or multisig, or
* Critical actions require off-chain coordination unavailable during crises.

This does not imply poor design, but it **must be acknowledged explicitly**.

---

## Decentralization Envelope

> **A protocol is decentralized only within a bounded operating envelope.**

Outside this envelope:

* Governance slows or centralizes
* Liquidity provision concentrates
* Control paths collapse to discretionary actors

This analysis identifies:

* The size of that envelope
* The conditions under which decentralization fails
* Which dimension fails first

---

## Stress Test Scenarios (Required)

Each protocol must be evaluated under at least **two adversarial scenarios**:

1. **Market Shock**

   * ≥30–50% collateral drawdown within hours
2. **Liquidity Shock**

   * Loss of top liquidity venues or executors
3. **Operational Shock** (optional but recommended)

   * Oracle failure or executor withdrawal

For each scenario:

* Identify who retains control
* Identify which decentralization dimension collapses
* Document irreversible failure paths

---

## Reporting Standard (Checklist)

A submission-ready decentralization section must include:

* Explicit definitions of G, B, O, C
* Quantitative metrics for each dimension
* At least one stress scenario with analysis
* Clear statement of where decentralization fails
* No reliance on architectural intent alone

---

## Interpretation Rule

> **If a protocol is centralized in any dimension during stress, it is effectively centralized in that regime.**

Decentralization claims must therefore be **conditional**, not absolute.

---

If you want next, I can:

* Apply this template **cleanly to Terra** (pure decentralization, no sustainability overlap)
* Apply it **side-by-side** to Terra vs Maker
* Turn this into a **one-page scoring table + diagram** for fast readers

Just tell me which direction to go.
