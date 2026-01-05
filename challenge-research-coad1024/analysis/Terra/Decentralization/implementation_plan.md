# Implementation Plan: Terra Decentralization Forensic Audit

## Objective
Execute a rigorous empirical evaluation of **Terra (Pre-Crash)** against the `Decentralization-Framework-General.md`. The goal is to quantify the "Decentralization Theater" — the gap between the DAO's design and its actual control structure under stress.

## Framework Alignment

We will populate the 4 orthogonal dimensions (G, B, O, C) with forensic data.

---

### 1. Governance Decentralization (G) - `1_Governance/`
**Framework metric:** Voting Power Distribution (Gini), Top-N Concentration, Latency.
**Terra Forensic Task:**
*   **Validator Forensics:** Reconstruct the Active Validator Set (Top 130) from May 1, 2022.
*   **Metrics to Calculate:**
    *   **Nakamoto Coefficient:** Min validators required to halt the chain (>33%).
    *   **Oligarchy Score:** % of power held by Top 10.
    *   **Turnout Analysis:** Did the "Community" vote on Prop 1164, or just the elite?

### 2. Backing Decentralization (B) - `2_Backing/`
**Framework metric:** Custody Concentration, Counterparty Exposure.
**Terra Forensic Task:**
*   **The LFG Black Box:** Investigate the Luna Foundation Guard structure.
*   **Metrics to Calculate:**
    *   **Signer Concentration:** 7 Signers managed $3B+ reserves (Ratio = 7 People / $3B).
    *   **Exogenous Dependency:** 100% reliance on Bitcoin (Correctional Risk).
    *   **Endogenous Feedback:** Quantify the "LUNA Backing LUNA" loop.

### 3. Operational Decentralization (O) - `3_Operational/`
**Framework metric:** Oracle Diversity, Infrastructure dependencies.
**Terra Forensic Task:**
*   **Oracle Forensics:** Analyze `x/oracle` vote transactions.
    *   **Homogeneity:** Did validators run independent price feeders or copy-paste scripts?
    *   **Latency:** Measure the "Oracle Lag" (30s) vs Market Crash Speed.

### 4. Control-Path Decentralization (C) - `4_Control/`
**Framework metric:** Emergency Powers, Automated vs Discretionary.
**Terra Forensic Task:**
*   **The Chain Halt:** Analyze the May 12, 2022 shutdown.
    *   **The Decision:** Was it an on-chain proposal or a TFL instruction?
    *   **The Kill Switch:** Who physically patched the nodes?

---

## Artifacts & Deliverables

1.  **Forensic Datasets (`/data` in each folder):**
    *   `validator_snapshot_may2022.csv` (G)
    *   `lfg_wallet_signers.md` (B)
    *   `oracle_vote_lag.csv` (O)

2.  **Visualizations (`/diagrams`):**
    *   `fig_validator_lorenz.svg`: Visualizing the Oligarchy.
    *   `fig_lfg_centralization.svg`: The 7-signer bottleneck.
    *   `fig_control_path.mermaid`: The "Soft Power" hierarchy.

3.  **Final Report:** `Article_Decentralization.md` containing the scored "Decentralization Vector" (G, B, O, C).

## Execution Sequence

1.  **Phase 1 (G):** Generate Validator Snapshot & Calculate Nakamoto.
2.  **Phase 2 (B):** Document LFG Signers & Endogenous Ratio.
3.  **Phase 3 (O/C):** Synthesize Oracle Lag & Chain Halt evidence.
4.  **Phase 4:** Score and Verdict.
