# Terra Decentralization Analysis

This analysis evaluates **Terra (UST/LUNA)** (pre-crash) using the standardized G-B-O-C decentralization framework.

**Methodological Premise:**
> **Decentralization is evaluated as control distribution under adversarial conditions.**
> *Did the DAO run the chain during the crash, or did a centralized committee take over?*

---

## 1. Governance Decentralization (G)

**Question:** Who could modify protocol parameters?
**Terra Claim:** "Community Governed via LUNA Staking."

### Empirical Verification
*   **Validator Concentration:**
    *   **Nakamoto Coefficient:** **3**. (Only 3 entities required to halt the chain).
    *   **Top 1 Dominance:** **20.4%** (Single entity control).
    *   **Gini Coefficient:** **0.67** (High Inequality).
    *   **Visual:** See `1_Governance/diagrams/fig_validator_lorenz.svg`.
*   **TFL Influence:**
    *   **Soft Power:** TFL delegated >20M LUNA to "friendly" validators, implicitly controlling their votes.
    *   **Veto Power:** With ~20% direct/indirect control, TFL held an effective veto on any proposal requiring >33% blocking stake.

**Verdict:**
**Functionally Centralized.** While 130 validators existed, the "Validator Oligarchy" (Top 3) held absolute power over consensus.

---

## 2. Backing / Collateral Decentralization (B)

**Question:** Who controlled the reserves?
**Terra Claim:** "Decentralized Reserve (LFG)."

### Empirical Verification
*   **Collateral Composition:** BTC (Exogenous) + LUNA (Endogenous) + AVAX/BNB.
*   **Custody Control (LFG):**
    *   **Structure:** 7-Member Council ("Signers of the Multi-sig").
    *   **The 7 Signers:** Do Kwon, Nicholas Platias, Kanav Kariya, Remi Tetot, Jose Maria Macedo, Hashed Rep, Dunam.
    *   **Concentration Metric:** **$428,000,000** decision power per human signer (Total $3B).
    *   **Execution:** Manual. Reserves were moved via human coordination (WhatsApp/Signal), not smart contract triggers.
    *   **Visual:** See `2_Backing/diagrams/fig_lfg_centralization.svg`.

**Verdict:**
**Committee Centralized.** The "Decentralized Reserve" was legally and technologically a discretionary hedge fund managed by 7 individuals.

---

## 3. Operational Decentralization (O)

**Question:** Who executed the price feed and liquidations?
**Terra Claim:** "Decentralized Oracle Module."

### Empirical Verification
*   **Oracle Source:** 130 Validators.
*   **Concentration:**
    *   **Code Monoculture:** >95% of validators ran the standard TFL `oracle-feeder` sidecar.
    *   **Failure Mode:** "130 Signers, 1 Brain". When the code hit edge cases, all oracles failed simultaneously.
    *   **Visual:** See `3_Operational/diagrams/fig_oracle_homogeneity.svg`.

**Verdict:**
**Operationally Unified.** The theoretical diversity of validators was nullified by the homogeneity of their software stack.

---

## 4. Control-Path Decentralization (C)

**Question:** Who halted the chain?

### Empirical Verification
*   **Event:** May 12, 2022 Chain Halt (Block 7,603,700).
*   **Mechanism:** Social consensus via Discord + Git Patch.
*   **Coordinator:** Terraform Labs (TFL) issued the instruction; Validators complied within <1 hour.
*   **Sovereignty:** The chain did not follow the longest chain rule; it followed the "Admin" instruction.

**Verdict:**
**Discretionary Control.** The ability to coordinatedly halt the chain proves that Terra was closer to a managed database than a sovereign blockchain.

---

## Stress Test Scenarios

### Scenario 1: The De-Peg Event (May 2022)
*   **G:** Validators deferred to TFL leadership.
*   **B:** LFG manually deployed reserves (Centralized execution).
*   **O:** Oracles lagged (Operational Failure).
*   **C:** Chain was halted manually (Centralized Control).

---

## Final Scorecard (Forensic Audit)

| Dimension | Score (1-5) | Summary |
| :--- | :--- | :--- |
| **G** (Governance) | **1/5** | **Oligarchy.** Top 3 validators controlled consensus (Nakamoto=3). |
| **B** (Backing) | **1/5** | **Committee.** $3B Reserve managed by 7-person multi-sig. |
| **O** (Operational)| **2/5** | **Monoculture.** 130 nodes ran identical TFL codebase. |
| **C** (Control) | **1/5** | **Managed.** TFL possessed effective "Kill Switch" power. |

*Verdict: **THEATER OF DECENTRALIZATION**.*
Terra operated with the *aesthetics* of a DAO (Voting, Validators) but the *mechanics* of a Centralized Fintech App.
