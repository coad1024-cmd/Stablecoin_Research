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

## 2. Design Module (1/2 Complete)

### A. Risk-Free Environment (Done)
- [x] **Concept**: "Unity" (1:1 Wrapper). Documented in `stablecoins.md`.

### B. Risky Collateral Environment (Pending)
- [x] **Literature Review**: Studied Tranched/Senior-Junior structures (e.g., Tranchess).
- [x] **Concept**: "Duo" / Tranche System.
- [x] **Design Spec**: Define mechanics for Senior/Junior tranches to isolate volatility.

## 3. Modelling Module (Complete)
- [x] **Attack Simulation**: Modelled Cost vs Profit of Terra De-peg.
- [x] **Documentation**: Findings integrated into `research/stablecoins.md`.

## 4. Pipeline Finalization (Done)
- [x] **Consolidation**: Scripts moved to `pipeline/scripts`.
- [x] **Templates**: Updated `01_analysis.md` to Gold Standard.

## 5. Infrastructure Overhaul (Jan 2026) (Done)
- [x] **Root Cleanup**: Removed duplicate scripts and research folders.
- [x] **Resource Organization**: Consolidated `resources/` into `literature`, `protocols`, and `notes`.
- [x] **Pipeline Structure**: Created distinct categories (`data_fetchers`, `visualization`, etc.).
- [x] **Environment**: Moved `node_modules` to `pipeline/`.
- [x] **Link Integrity**: Fixed 8+ broken path references in documentation.
- [x] **History Reconstruction**: Rebuilt `progress_log.md` with reconstructed dates (Nov-Dec 2025) based on file forensics.

## 6. Academic Rigor & Citations (Next Priority)
*See `research/appendix/citation_resources/CITATION_IMPLEMENTATION_PLAN.md`*

- [x] **Priority 1 (Synthesis)**: Implement citations in `Final-Comparative-Report.md`.
- [x] **Priority 2 (Deep Dives)**: Implement citations in `Sky-Economic-Sustainability.md` etc.
- [x] **Master References**: Create `research/00_canonical/MASTER_REFERENCES.md`.
- [ ] **Verification**: Test all anchor links.
- [ ] **Priority 3 (Profiles)**: Implement citations in `Sky_Decentralization_Profile_Jan2026.md` etc.
