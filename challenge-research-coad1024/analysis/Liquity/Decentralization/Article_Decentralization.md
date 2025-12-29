# Liquity Decentralization Analysis

This analysis evaluates **Liquity (LUSD)** using the standardized G-B-O-C decentralization framework.

**Methodological Premise:**
> **Decentralization is evaluated as control distribution under adversarial conditions.**

Liquity represents a unique "Governance Minimized" architecture. This report empirically verifies if that architectural intent translates to effective decentralization in practice.

---

## 1. Governance Decentralization (G)

**Question:** Who can modify protocol parameters?
**Liquity Claim:** "Immutable. No Admin Keys."

### Empirical Verification
*   **Parameter Modifiability:** [PENDING: Verify if `BorrowingFee`, `MCR` are hardcoded or adjustable]
*   **Admin Keys:** [PENDING: Check Etherscan for owner addresses on `TroveManager`]
*   **Upgradeability:** [PENDING: Are contacts behind Proxies?]

**Verdict:**
[PENDING]

---

## 2. Backing / Collateral Decentralization (B)

**Question:** What backs LUSD?
**Liquity Claim:** "ETH Only. No RWAs. No USDC."

### Empirical Verification
*   **Collateral Composition:** 100% ETH (design invariant).
*   **Concentration:**
    *   **Trove Distribution:** [PENDING: Gini Coeff of ETH locked]
    *   **Stability Pool Share:** [PENDING: % of LUSD in Stability Pool held by top 10 addresses]
*   **Correlation Risk:** High (ETH correlates with Crypto Market).

**Verdict:**
[PENDING]

---

## 3. Operational Decentralization (O)

**Question:** Who runs the interface and liquidations?
**Liquity Claim:** "Decentralized Frontends. No Official Web Interface."

### Empirical Verification
*   **Frontend Diversity:**
    *   Count of active Frontends: [PENDING]
    *   HHI of Frontend Kickback Rates: [PENDING]
*   **Oracle Reliance:**
    *   Primary: Chainlink.
    *   Fallback: Tellor.
    *   Logic: [PENDING: Verify switchover conditions]

**Verdict:**
[PENDING]

---

## 4. Control-Path Decentralization (C)

**Question:** Who controls Recovery Mode?

### Empirical Verification
*   **Trigger:** Automated (TCR < 150%).
*   **Human Discretion:** None? [PENDING: verify]

**Verdict:**
[PENDING]

---

## Stress Test Scenarios

### Scenario 1: ETH Flash Crash (-50%)
*   **G:** Immutable (Pass).
*   **B:** ETH value drops.
*   **O:** Do liquidators scale? [PENDING]
*   **C:** Recovery Mode activation.

### Scenario 2: Chainlink Freeze
*   **O:** Switch to Tellor? [PENDING]

---

## Final Scorecard

| Dimension | Score (1-5) | Summary |
| :--- | :--- | :--- |
| **G** (Governance) | ? | ? |
| **B** (Backing) | ? | ? |
| **O** (Operational)| ? | ? |
| **C** (Control) | ? | ? |

*Status: **PENDING DATA ACQUISITION***
