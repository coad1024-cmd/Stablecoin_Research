
# Research Progress Log

## Week 1: Setup & Initial Research (Nov 3 - Nov 9)

* **2025-11-03**: Project initialized. Repository cloned.
* **2025-11-04**: Research Pipeline designed (System Engineering approach).
* **2025-11-05**: Topic selected: Stablecoins.
* **2025-11-07**: Specific targets defined: DAI, UST, USDT. Design: Duo Network.

## Week 2: Deep Dive Analysis (Nov 10 - Nov 16)

* [x] Analyze DAI mechanism and risks.
* [x] Analyze UST collapse and algorithmic flaws.
* [x] Analyze USDT backing and centralization risks.
* [x] **New**: Integrated HackMD research notes into `resources/notes/hackmd/`.
* [x] **New**: Cloned official MakerDAO documentation to `resources/protocols/Sky_Ecosystem/`.
* [x] **New**: Created `Analysis-Meta-framework.md` from LaTeX design paper.

## Week 3: Design & Modelling (Nov 17 - Nov 23)

* [ ] Draft "Duo Network" adaptation for Volatile Collateral scenario.
* [ ] Refine Terra Luna De-peg Model (Math & Logic).

## Current Session (2025-11-24): Resource Integration & Tool Setup

* [x] **Formatted Meta-Frameworks**: Converted LaTeX design paper to `Analysis-Meta-framework.md` and `Stablecoin-meta-framework.md`.
* [x] **Updated Changelogs**: Maintained `master_workflow.md` changelog with v1.3-v1.5 entries.
* [/] **PDF Conversion Setup**: Converted 9/12 PDFs using `pymupdf4llm` - quality insufficient for academic papers.
  * Converted 9 PDFs with basic quality (math/tables/images poorly formatted)
  * Cloned DeepSeek-OCR for high-quality conversion (requires GPU setup)
  * Created `PDF_CONVERSION_STATUS.md` with setup instructions

## Week 4: Final Report

* [ ] Assemble final report.
* [ ] Peer review and formatting.

## Current Session (2025-11-26): Operational Decentralization Analysis

* [x] **Setup**: Created `analysis/makerdao/operational` structure.
* [x] **Data Acquisition**:
  * Attempted Dune/Web3 methods (failed due to API limits).
  * **Success**: Used browser subagent to scrape Etherscan for initial sample.
  * **Success**: Processed user-provided Etherscan CSV (`export-advanced-filtered...`).
* [x] **Liquidator Analysis**:
  * Analyzed 100 liquidation attempts.
  * Found **HHI of 1136** (Unconcentrated) and **Top Keeper Share of 27%**.
  * Generated `keeper_concentration.png`.
* [x] **RWA Analysis**:
  * Created `rwa_custodians.py` and visualization script.
  * Generated `rwa_custodian_exposure.png` (currently using placeholder data).
* [x] **Reporting**: Created `report.md` and updated `walkthrough.md`.

## Current Session (2025-11-26): Pipeline Refinement & Organization

* [x] **File Organization**: Cleaned root directory, moved logs to `logs/` and data to `analysis/.../data`.
* [x] **Pipeline Update**:
  * Updated `master_workflow.md` with Operational Analysis module.
  * Migrated analysis scripts to `pipeline/scripts/operational/` for reuse.
  * Cleaned up `progress_log.md`.

## Session (2025-12-09): Liquity V2 Data
* [x] **Data Snapshot**: Acquired V2 collateral data (Dec 9 TS).

## Session (2025-12-29): Terra Attack Analysis & Validation
* [x] **Modeling**: Simulated "Death Spiral" mechanics (`simulate_terra_crash_data.py`).
* [x] **Profitability**: Modeled Attack Cost vs Profit (Soros Scenario).
* [x] **Validation**: Compared simulation vs historical forensic data.

## Session (2025-12-31): Stablecoin Design Analysis
* [x] **Boundary Analysis**: Finalized "Non-Volatile" vs "Volatile" limit cases.
* [x] **Review**: Refined design artifacts based on feedback.

## Session (2026-01-02): Sky & Liquity Verification
* [x] **Sky**: Synthesized Economic Sustainability Report (Part II).
* [x] **Liquity V2**: Integrated operational stats and verified decentralization metrics.
* [x] **Report**: Enhanced `INDEX.md` with 3-way comparison data.

## Current Session (2026-01-05): Major Infrastructure Overhaul

### 1. Pipeline Consolidation
* [x] **Root Cleanup**: Merged root `/scripts` into locally organized `/pipeline` directory.
* [x] **New Categories**: Added `scripts/data_fetchers` (JS/Py), `scripts/visualization`.
* [x] **Documentation**: Created comprehensive `pipeline/README.md` and `.gitignore`.

### 2. Research Structure Standardization
* [x] **Duplicate Removal**: Eliminated duplicate research folders (`02_design_limit_cases`, `04_modelling`) from root; canonical versions preserved in `research/`.
* [x] **Archive Strategy**: Created `research/archive/` and `research/planning/` for clean workspace management.
* [x] **Context Management**: Moved LLM context files to hidden `.agent/` directory.

### 3. Resources Reorganization (`resources/`)
* [x] **Protocol Docs**: Consolidated Liquity, Terra, and Sky Ecosystem (MakerDAO) into `resources/protocols/`.
* [x] **Literature**: Merged papers and PDF conversions into `resources/literature/`.
* [x] **Notes**: Moved HackMD and raw notes to `resources/notes/`.
* [x] **Index**: Rebuilt `resources/index.md` with correct relative paths.

### 4. Code & Reference Integrity
* [x] **Node Environment**: Moved `package.json` and `node_modules` to `pipeline/` to de-clutter root.
* [x] **Path Updates**: Updated 8+ references in `CITATION_STYLE_GUIDE.md`, `INDEX.md`, and Python scripts to point to new directory locations.

### 5. Final Workspace Optimization
* [x] **Root Directory**: Moved `planning` and `archive` to root level for easier access and separation from canonical `research`.
* [x] **Archive Strategy**: Consolidated old drafts and cleanup artifacts into `archive/drafts/` and `archive/analysis_cleanup/`.
* [x] **Task Tracking**: Centralized project management in `planning/current_task.md`.
* [x] **Final State**: Root directory now contains only 5 key folders (`pipeline`, `research`, `analysis`, `resources`, `planning`, `archive`) + `README.md`.

---

## Session (2026-01-05): Sky Profile On-Chain Verification

### 1. Deep Verification Initiative
* [x] **Claim-Complete Framework**: Implemented 4-type claim classification (A/B/C/D) for falsifiability.
* [x] **Script Development**: Created `verify_sky_claims.py` for direct Ethereum mainnet contract calls.
* [x] **USDC Hunt**: Discovered USDC held in **PSM Pocket** (`0x37305B1cD...`), not main LitePSM contract.

### 2. Multi-Chain Verification (9 Chains)
* [x] **Chains Checked**: Ethereum, Arbitrum, Optimism, Base, Polygon, Gnosis, zkSync, Avalanche, BNB.
* [x] **Results**:
  | Metric | Web Claimed | On-Chain Verified |
  |:---|:---|:---|
  | Combined Supply | $15.07B | **$11.34B** |
  | DAI | $5.36B | **$4.95B** |
  | USDS | $9.71B | **$6.40B** |
  | USDC PSM | $3.93B | **$3.99B** ✅ |
* [x] **Finding**: Web sources overstated by **$3.73B (~33%)**.

### 3. Profile Updates
* [x] **Sky Profile**: Updated with on-chain verified $11.34B baseline, 35.2% USDC dependency.
* [x] **Final-Comparative-Report.md**: Corrected Sky ecosystem size and USDC %.
* [x] **INDEX.md**: Added complete metrics table with block number.

### 4. Artifact Cleanup
* [x] **Moved to Archive**: `VERIFICATION_REPORT_Jan2026.md`, `ON_CHAIN_VERIFICATION_FINAL_Jan2026.md`.
* [x] **Canonical Atrifact**: Now contains only 2 core docs.

### 5. Scripts Created
* `pipeline/scripts/verification/verify_sky_claims.py` — Ethereum mainnet verification
* `pipeline/scripts/verification/hunt_missing_usdc.py` — PSM address investigation
* `pipeline/scripts/verification/verify_multichain_supply.py` — 9-chain supply check
