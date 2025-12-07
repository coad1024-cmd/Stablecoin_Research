# Research Pipeline: Master Workflow

## Overview

This pipeline allows for rapid generation of research reports for the "Wonderland" challenge.

## Steps

### 1. Initialization

1. Create a new directory: `research/[topic_name]/`.
2. Copy all files from `pipeline/templates/` to `research/[topic_name]/`.

### 2. Execution

1. **Analysis**: Open `01_analysis.md`. Fill in the comparison matrix and deep dive sections for your chosen assets.
2. **Design**: Open `02_design.md`. Select the 2 scenarios required by the `README.md` for your topic. Write the architecture.
3. **Modelling**: Open `03_modelling.md`. Choose an attack vector. Define the variables and logic. Update the Mermaid diagram.

### 3. Operational Analysis (New Module)

1. **Setup**: Create `analysis/[protocol]/operational/` directory.
2. **Data Acquisition**:
    - **Liquidators**: Use `scan_liquidators.py` (Web3) or Dune SQL export.
    - **Custodians**: Obtain collateral snapshot (e.g., `collateral_snapshot.json`).
3. **Execution**:
    - Run `analyze_keepers.py` to compute HHI and concentration metrics.
    - Run `rwa_custodians.py` to assess RWA exposure.
4. **Visualization**: Generate charts (`keeper_concentration.png`, `rwa_custodian_exposure.png`).

### 4. Assembly

1. Create a final file `research/[topic_name].md`.
2. Concatenate the content of `01`, `02`, `03`, and Operational Analysis into this file.
3. Add a Title and Introduction.

### 5. Verification

1. Open `pipeline/requirements_matrix.md`.
2. Go through each item and verify your final report complies.

## Pipeline Changelog

Track all changes to the workflow, templates, and infrastructure here.

| Date | Version | Change Description | Rationale |
| :--- | :--- | :--- | :--- |
| **2025-11-26** | v1.7 | **Operational Decentralization Module** | Added standardized workflow for analyzing liquidator and custodian concentration (Scripts + Visualization). |
| **2025-11-24** | v1.6 | **DeepSeek-OCR Integration** | Cloned DeepSeek-OCR for high-quality PDF conversion with proper math/table/image support. Requires GPU setup. |
| **2025-11-24** | v1.5 | **PDF Conversion Tool** | Initial conversion using `pymupdf4llm` - converted 9/12 PDFs but quality insufficient for academic papers. |
| **2025-11-24** | v1.4 | **Formatted Meta-Framework** | Converted LaTeX design paper to standard Markdown (`Analysis-Meta-framework.md`) and integrated into index. |
| **2025-11-24** | v1.3 | **Integrated MakerDAO Docs** | Cloned official `mcd-docs-content` and `intro-docs` to `resources/makerdao/` for offline reference. |
| **[Current Date]** | v1.2 | **Added HackMD Import Script** | User requested ability to pull content from HackMD. Added `pipeline/scripts/pull_hackmd.py`. |
| **[Current Date]** | v1.1 | **Added PDF Directory** (`resources/pdfs/`) | Centralized storage for research papers was needed. |
| **[Current Date]** | v1.0 | **Initial Release** | Established Templates (01-03), Master Workflow, and Requirements Matrix. |

## Tools & Scripts

- **HackMD Importer**: Run `python pipeline/scripts/pull_hackmd.py <url>` to download a note to `resources/hackmd/`.
- **Liquidator Scanner**: `analysis/makerdao/operational/scripts/scan_liquidators.py`
- **Keeper Analyzer**: `analysis/makerdao/operational/scripts/analyze_keepers.py`
