
# Research Progress Log

## Week 1: Setup & Initial Research

* **[Date]**: Project initialized. Repository cloned.
* **[Date]**: Research Pipeline designed (System Engineering approach).
* **[Date]**: Topic selected: Stablecoins.
* **[Date]**: Specific targets defined: DAI, UST, USDT. Design: Duo Network.

## Week 2: Deep Dive Analysis

## Week 2: Deep Dive Analysis

* [x] Analyze DAI mechanism and risks.
* [x] Analyze UST collapse and algorithmic flaws.
* [x] Analyze USDT backing and centralization risks.
* [x] **New**: Integrated HackMD research notes into `resources/hackmd/`.
* [x] **New**: Cloned official MakerDAO documentation to `resources/makerdao/`.
* [x] **New**: Created `Analysis-Meta-framework.md` from LaTeX design paper.

## Week 3: Design & Modelling

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
