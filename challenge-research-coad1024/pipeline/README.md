# Research Pipeline

This directory contains the data processing, analysis, and visualization pipeline for the Stablecoin Research Challenge.

## Directory Structure

```
pipeline/
├── README.md                    # This file
├── scripts/                     # All Python scripts organized by function
│   ├── data_fetchers/          # Data acquisition scripts
│   ├── converters/             # Format conversion utilities
│   ├── visualization/          # Plotting and diagram generation
│   ├── simulation/             # Economic simulation scripts
│   ├── operational/            # Operational analysis (keepers, liquidators)
│   └── utilities/              # General utility scripts
├── templates/                   # Document templates
├── tools/                       # External tools (DeepSeek-OCR, marker, marker-api)
└── docs/                        # Pipeline documentation

```

## Script Categories

### 📥 Data Fetchers (`scripts/data_fetchers/`)
Scripts for acquiring data from various sources:

**Python Scripts:**
- `fetch_liquity_v2_data.py` - Fetches Liquity V2 on-chain data
- `fetch_makerdao_data.py` - Fetches MakerDAO/Sky on-chain data
- `fetch_terra_resources.py` - Fetches Terra historical data
- `fetch_hackmd_api.py` - Fetches documents from HackMD API

**JavaScript/Node.js Scripts:**
- `fetch_liquity_v2_onchain.js` - Direct on-chain Liquity V2 data fetcher (Web3)
- `fetch_v2_operational_stats.js` - Liquity V2 operational statistics
- `fetch_v2_stability_pools.js` - Liquity V2 stability pool analytics

### 🔄 Converters (`scripts/converters/`)
Format conversion utilities:
- `convert_pdfs.py` - Batch PDF to Markdown conversion
- `convert_html_to_md.py` - HTML to Markdown converter
- `convert_liquity_wp.py` - Liquity whitepaper converter
- `convert_terra_pdfs.py` - Terra-specific PDF converter
- `convert_selected_pdfs.py` - Selective PDF conversion
- `convert_new_pdf.py` - Single PDF converter
- `convert_iterative.py` - Iterative conversion utility

### 📊 Visualization (`scripts/visualization/`)
Plotting and diagram generation:
- `generate_liquity_plots.py` - Liquity-specific visualizations
- `generate_makerdao_plots.py` - MakerDAO/Sky visualizations
- `generate_terra_plots.py` - Terra analysis plots
- `generate_business_diagrams.py` - Business model diagrams
- `generate_decentralization_plots.py` - Decentralization metrics visualization

### 🎮 Simulation (`scripts/simulation/`)
Economic simulation models:
- `simulate_anchor_depletion.py` - Anchor protocol depletion model
- `simulate_terra_crash_data.py` - Terra collapse simulation

### ⚙️ Operational Analysis (`scripts/operational/`)
Real-time operational metrics:
- `analyze_keepers.py` - Keeper market analysis
- `plot_keepers.py` - Keeper visualization
- `scan_liquidators.py` - Liquidator scanning
- `run_dune_query.py` - Dune Analytics query runner
- `rwa_custodians.py` - RWA custodian analysis
- `plot_rwa_custodians.py` - RWA custodian plots
- `convert_etherscan_csv.py` - Etherscan data converter
- `test_connection.py` - API connection tester

### 🛠️ Utilities (`scripts/utilities/`)
General-purpose utilities:
- `cleanup_dai.py` - DAI data cleanup
- `organize_notes.py` - Research notes organizer
- `pull_hackmd.py` - HackMD document puller

## External Tools (`tools/`)

Third-party dependencies for document processing:
- **DeepSeek-OCR**: OCR processing for documents
- **marker**: PDF to Markdown conversion tool
- **marker-api**: API wrapper for marker

> **Note**: The `tools/` directory (~16MB) contains external dependencies and can be excluded from version control if needed.

## Usage Examples

### Fetch Latest Data
```bash
# Fetch Liquity V2 data
python scripts/data_fetchers/fetch_liquity_v2_data.py

# Fetch MakerDAO data
python scripts/data_fetchers/fetch_makerdao_data.py
```

### Generate Visualizations
```bash
# Generate all MakerDAO plots
python scripts/visualization/generate_makerdao_plots.py

# Generate business diagrams
python scripts/visualization/generate_business_diagrams.py
```

### Run Simulations
```bash
# Simulate Terra crash
python scripts/simulation/simulate_terra_crash_data.py
```

### Convert Documents
```bash
# Convert PDFs to Markdown
python scripts/converters/convert_pdfs.py
```

## Documentation

- **[Master Workflow](docs/master_workflow.md)**: Complete research workflow
- **[Requirements Matrix](docs/requirements_matrix.md)**: Script dependencies

## Dependencies

**Python** dependencies vary by script. Common requirements include:
- `pandas`, `numpy` - Data processing
- `matplotlib`, `seaborn` - Visualization
- `web3`, `eth-utils` - Blockchain interaction
- `requests` - API calls
- `markdownify` - HTML conversion

**Node.js** dependencies (for JavaScript scripts):
- `ethers` or `web3.js` - Blockchain interaction
- `@ethersproject/providers` - RPC providers

## Notes

- All scripts are designed to run independently
- Output typically goes to `../research/` or `../analysis/` directories
- Some scripts require API keys (Dune, Etherscan, etc.) - configure in environment variables
- The pipeline supports both historical analysis and real-time data fetching

## Maintenance

Last reorganized: January 5, 2026
Structure: Organized by functional category for easier navigation
