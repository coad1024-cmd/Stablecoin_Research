# ε — Loss Absorption & Resolution Appendix

*(Non-Canonical / Engineering-Grade / Intentionally Exhaustive)*

---

## 0. Purpose and Scope

This document exists to **absorb complexity that must not appear in the canonical submission**.

It explicitly models:

* operational failures,
* legal and custodial disruptions,
* coordination delays,
* non-deterministic resolution processes.

This document **does not**:

* propose a production stablecoin,
* guarantee user protection,
* claim full on-chain enforceability,
* eliminate trust.

Its sole purpose is to make **loss allocation explicit, bounded, and non-discretionary** under non-market failures.

---

## 1. Design Position

### 1.1 What ε Is

ε is a **tokenized, junior, loss-absorbing buffer** whose only function is to absorb **non-market losses** that cannot be addressed through price mechanisms.

ε represents:

* explicit subordination,
* explicit loss ownership,
* explicit failure acknowledgment.

ε is **not** a hedge.
ε is **not** insurance.
ε is **not** a confidence mechanism.

ε exists so that losses are **visible, finite, and allocated**.

---

### 1.2 What ε Is Not (Hard Exclusions)

ε MUST NOT:

* stabilize the peg,
* influence market price,
* restore confidence,
* signal solvency,
* provide yield,
* act as collateral,
* participate in governance,
* trigger parameter changes,
* enable discretionary intervention.

Any design in which ε does any of the above is **out of scope** and **invalid** relative to the PMOTL limit case.

---

## 2. Threat Model (Non-Market Failures Only)

This model assumes **zero collateral price volatility**.
Only residual risks are considered.

### 2.1 Enumerated Threats

The following events are explicitly modeled:

1. **Smart Contract Exploit**
   * unauthorized mint
   * unauthorized burn
   * accounting corruption
   * logic bypass

2. **Custodial Failure**
   * asset mismanagement
   * operational error
   * internal fraud

3. **Legal Intervention**
   * asset freeze
   * seizure
   * injunction
   * forced transfer

4. **Settlement Failure**
   * delayed redemption
   * halted settlement rails
   * correspondent banking failure

5. **Fraud Discovery**
   * reserve misrepresentation
   * double counting
   * hidden liabilities

6. **Jurisdictional Conflict**
   * cross-border claims
   * conflicting court orders
   * regulatory deadlock

These threats are **assumed inevitable at scale**.

---

## 3. Loss Classification

All losses fall into exactly one category:

| Loss Type          | Market-Based | Covered by ε |
| ------------------ | ------------ | ------------ |
| Price decline      | ❌            | ❌            |
| Slippage           | ❌            | ❌            |
| Exploit loss       | ❌            | ✅            |
| Legal freeze       | ❌            | ✅            |
| Custody error      | ❌            | ✅            |
| Fraud revelation   | ❌            | ✅            |
| Coordination delay | ❌            | ⚠️ (partial) |

If a loss cannot be classified cleanly, the model **does not apply**.

---

## 4. ε State Machine (Explicit)

### 4.1 States

```
NORMAL
  |
  | Non-market loss detected
  v
IMPAIRED
  |
  | Loss ≤ ε capacity
  v
ABSORBED
  |
  | Accounting updated
  v
NORMAL

IMPAIRED
  |
  | Loss > ε capacity
  v
EXHAUSTED
  |
  | External resolution
  v
RESOLVED | LIQUIDATED
```

---

### 4.2 State Descriptions

#### NORMAL
* Stablecoin fully backed
* ε fully intact
* No intervention

#### IMPAIRED
* Non-market loss confirmed
* Loss magnitude assessed
* No discretionary action permitted

#### ABSORBED
* ε reduced by loss amount
* Stablecoin balances unchanged
* No parameter changes allowed

#### EXHAUSTED
* ε fully depleted
* No further on-chain absorption possible
* Stablecoin remains solvent in accounting terms
* Liveness and redemption depend on external processes

#### RESOLVED / LIQUIDATED
* Loss allocation finalized off-chain
* System either continues or winds down
* Outside scope of protocol logic

---

## 5. Timing & Latency (Non-Ideal Reality)

This model explicitly acknowledges **temporal mismatch**.

| Event            | On-Chain Response | Off-Chain Process | Expected Latency |
| ---------------- | ----------------- | ----------------- | ---------------- |
| Exploit detected | immediate         | investigation     | days             |
| Legal freeze     | none              | court action      | weeks            |
| Custody recovery | none              | litigation        | months           |
| Fraud resolution | none              | bankruptcy        | years            |

**Key insight:**
ε absorbs *magnitude*, not *time*.

---

## 6. On-Chain Effects (What Actually Happens)

When ε is hit:
* ε balance is reduced or burned
* Stablecoin balances remain unchanged
* No minting occurs
* No redemption rules change
* No governance hooks are activated

When ε is exhausted:
* No automatic halts are triggered
* No emergency mint occurs
* No hidden backstop exists

Anything beyond accounting is **outside the model**.

---

## 7. Explicit Non-Goals (Repeated for Emphasis)

This system does **not** guarantee:
* uninterrupted redemption,
* immediate recovery,
* capital preservation,
* fairness of legal outcomes,
* jurisdictional neutrality.

The only guarantee is:

> Losses are not hidden.

---

## 8. Comparison to Common Failure Patterns

| Pattern             | Why It Fails       | ε Response |
| ------------------- | ------------------ | ---------- |
| Insurance tokens    | reflexive collapse | rejected   |
| Governance bailouts | discretion panic   | rejected   |
| Yield buffers       | mispriced risk     | rejected   |
| “Temporary pauses”  | trust erosion      | rejected   |

ε refuses to **pretend safety**.

---

## 9. Relationship to the Canonical Paper

The canonical paper:
* defines the PMOTL limit,
* proves degeneracy under σ² → 0,
* states necessary structure.

This appendix:
* absorbs operational mess,
* models ugly failure paths,
* prevents accidental overclaim.

They are intentionally asymmetric.

---

## 10. Final Statement (No Comfort Offered)

ε does not save systems.
ε does not protect users from pain.
ε does not replace law or trust.

ε exists so that:
* losses are explicit,
* allocation is bounded,
* discretion is minimized,
* and failure is not disguised as stability.

If this is unacceptable, the PMOTL model is not appropriate.

---

## 11. Cross-Reference: Failure of Canonical Assumptions

This appendix serves as the dedicated failure handler for the assumptions defined in **Section 2** of the canonical paper.

| Canonical Assumption (Sec 2) | Failure Mode (Appendix) | Handling Mechanism |
| :--- | :--- | :--- |
| **1. Zero Price Volatility** ($\sigma^2=0$) | **Negative Yield / Decay** | **Excluded**: Price risk is not covered by $\epsilon$. If $ drops due to market value, PMOTL definition invalidates. |
| **2. Legal Enforceability** | **Legal Intervention** (Sec 2.1) | **Absorbed**: $\epsilon$ pays for seizures/freezes. |
| **3. HQLA Liquidity** | **Settlement Failure** (Sec 2.1) | **Absorbed**: $\epsilon$ covers bridge/custody failures. |
| **4. Atomic Mint/Burn** | **Smart Contract Exploit** (Sec 2.1) | **Absorbed**: $\epsilon$ covers logic bypass or accounting corruption. |
| **5. Rational Arbitrage** | **Coordination Delay** (Sec 3) | **Partial**: $\epsilon$ cannot force arbitrage but covers operational friction preventing it. |

**Zero Leakage Statement:**
Any failure not covered by the table above (e.g., market crash of reserve assets) is a fundamental violation of the PMOTL limit case and requires a different architectural model (e.g., MakerDAO/Liquity) rather than a loss buffer.

---

## 12. Protocol Implementation Reference (Upstream)

This section maps the abstract structural invariants of the canonical paper to concrete Solidity implementation logic.

### 12.1 PMOTL Contract Invariants

1.  **Conservation of Reserves (Minting)**
    `mint(amount)` MUST revert unless:
    *   `msg.sender` provides cryptographic proof of atomic reserve deposit (e.g., atomic settlement callback), OR
    *   The transaction atomically transfers an equivalent value of reserve tokens to the protocol.
    *   `ReserveBalance_new == ReserveBalance_old + amount`

2.  **Permissionless Redemption**
    `redeem(amount)` MUST be callable by any address holding stablecoins.
    *   **MUST NOT** depend on off-chain approvals or governance whitelists.
    *   **MUST** settle atomically (same-block reserve transfer) or revert.

3.  **Solvency Check (Terminal State)**
    If `TotalReserves < TotalSupply` at any state transition, the contract MUST enter a **Terminal State** (e.g., wind-down or pro-rata claim).
    *   *Constraint*: $A(t) < L(t) \implies \text{ActiveState} = \text{False}$

### 12.2 Forbidden Function List

The following functions are strictly **forbidden** in a PMOTL contract. Their presence negates the non-volatile classification:

*   `pause()` / `freeze()`: Introduces discretionary liquidity risk.
*   `setMintingCap()` (via Governance): Introduces discretionary supply constraints.
*   `rescueToken()`: Violates the conservation of reserves if applied to backing assets.
*   `upgradeTo()` (Proxy Pattern): Introduces critical dependency on the upgrade key/multisig, violating the deterministic nature of the limit case.
*   `liquidate()`: There are no collateral positions to liquidate; reserves are held directly.

### 12.3 The Trust Boundary of $\epsilon$

The Junior Capital Buffer ($\epsilon$) represents the **boundary of on-chain enforceability**.
*   **On-Chain**: The protocol can enforce that $\epsilon$ is first-loss (subordinated).
*   **Off-Chain**: The protocol **cannot** enforce that $\epsilon$ is replenished.

**Critical Spec**: The obligation to replenish $\epsilon$ is legal/social, not cryptographic. A PMOTL protocol essentially reduces to a **Trustless Wrapper requiring Trusted Capital**.
