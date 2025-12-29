# Protocol Analysis Template (Gold Standard)

## 1. Objective

Conduct a rigorous, data-driven comparison of [PROTOCOL_A] (e.g., MakerDAO) vs [PROTOCOL_B] (e.g., Liquity).
**Constraint**: All analysis must be backed by **Real On-Chain Data** or verifiable mathematical models. No "Vaporware" or "Hallucinations".

## 2. Directory Structure Setup

Ensure the analysis follows this validated structure:

```
analysis/[PROTOCOL_NAME]/
├── Final-report.md                 # Executive Summary (Executive Level)
├── data/                           # CSV Snapshots (e.g., trove_snapshot_mainnet.csv)
├── Sustainability/
│   ├── Section-by-Section/         # Detailed Reports
│   │   ├── Business Decomposition.md
│   │   └── Key Metrics.md
│   ├── Diagrams/                   # PNG Visualizations (Mandatory)
│   └── scripts/                    # Generation Scripts (e.g., generate_business_plots.py)
└── Decentralization/
    ├── collateral/                 # HHI, Exposure Analysis
    ├── governance/                 # Gini, Nakamoto Analysis
    └── scripts/                    # Analysis Scripts
```

## 3. Data Pipeline Requirement

* **Do NOT** use hardcoded values for live metrics.
* **MUST** create a fetch script (e.g., `pipeline/fetch_[protocol]_data.py`).
* **Source**: Connect to Ethereum Mainnet RPCs (e.g., LlamaRPC).
* **Output**: Save raw data to `analysis/[PROTOCOL]/data/snapshot.csv`.

## 4. Sustainability Analysis (The "Business Model")

The report **MUST** include the following visualizations in `Business Decomposition.md`:

1. **Unit Economics**: Profit/Loss per unit of debt (Visualizing Margins).
2. **Stress Matrix**: Solvency Heatmap under dual-shock scenarios (e.g., Rates Drop + Crypto Crash).
3. **Revenue Composition**: Pie chart of revenue sources (Backing Yield vs Fees).
4. **Historical Rate Evolution**: Timeseries of Cost of Capital vs Asset Yield ("Cost of Carry").

## 5. Decentralization Analysis

Quantify "Decentralization" using standard metrics derived from on-chain snapshots:

* **Governance**: Gini Coefficient, Nakamoto Coefficient, Lorenz Curve.
* **Collateral**: HHI Score, Counterparty Exposure (e.g., Lido vs Native).
* **Operational**: Diversity of Frontends/Keepers.

## 6. Comparison Matrix

| Dimension | [PROTOCOL_A] | [PROTOCOL_B] | Winner |
| :--- | :--- | :--- | :--- |
| **Business Model** | [Margin/Vol] | [Margin/Vol] | [Verdict] |
| **Resilience** | [Stress Score] | [Stress Score] | [Verdict] |
| **Decentralization** | [Gini/HHI] | [Gini/HHI] | [Verdict] |

## 7. Artifact Checklist

- [ ] `fetch_data.py` (Pipeline)
* [ ] `snapshot.csv` (Evidence)
* [ ] `generate_plots.py` (Visualization)
* [ ] `Final-report.md` (Synthesis)
