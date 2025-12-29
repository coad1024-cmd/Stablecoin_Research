# Research Task Tracker

## 1. Analysis Module (3/3 Complete)

### A. MakerDAO (Done)

- [x] **Data Pipeline**: `fetch_makerdao_data.py` (Real Mainnet Data).
- [x] **Sustainability**: Generated "Business Model" plots (Unit Economics, Stress Matrix).
- [x] **Decentralization**: Analyzed Voter Turnout and Gini.

### B. Liquity V2 (Done)

- [x] **Data Pipeline**: `fetch_liquity_v2_data.py` (Multi-Branch Mainnet).
- [x] **Parity**: Achieved visualization parity with MakerDAO.
- [x] **Verification**: Validated Collateral HHI and Governance Gini.

### C. Terra / UST (Done)

- [x] **Structure**: Created Analysis directories.
- [x] **Backing Analysis**: `analysis/Terra/Backing Mechanism/Article_Backing_Mechanism.md`.
- [x] **Sustainability Analysis**: `analysis/Terra/Sustainability/Article_Sustainability.md`.
- [x] **Decentralization Analysis**: `analysis/Terra/Decentralization/Article_Decentralization.md`.
- [x] **Data Support**:
    - `simulate_terra_crash_data.py`: Death Spiral mechanics.
    - `simulate_anchor_depletion.py`: Yield Reserve runway model.

---

## 2. Design Module (1/2 Complete)

### A. Risk-Free Environment (Done)

- [x] **Concept**: "Unity" (1:1 Wrapper). Documented in `stablecoins.md`.

### B. Risky Collateral Environment (Pending)

- [x] **Literature Review**: Studied Tranched/Senior-Junior structures (e.g., Tranchess).
- [ ] **Concept**: "Duo" / Tranche System.
- [ ] **Design Spec**: Define mechanics for Senior/Junior tranches to isolate volatility.

---

## 3. Modelling Module (Complete)

- [x] **Attack Simulation**: Modelled Cost vs Profit of Terra De-peg.
- [x] **Documentation**: Findings integrated into `research/stablecoins.md`.

---

## 4. Pipeline Finalization (Done)

- [x] **Consolidation**: Scripts moved to `pipeline/scripts`.
- [x] **Templates**: Updated `01_analysis.md` to Gold Standard.
