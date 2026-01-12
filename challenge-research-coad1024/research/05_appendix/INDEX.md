# Canonical Research Artifacts

**Last Updated:** January 5, 2026

---

## Structure

```
research/00_canonical/
├── {Protocol}/
│   ├── Sustainability/
│   │   ├── Artifact/          ← Finalized documents
│   │   └── diagrams/          ← Supporting visualizations
│   ├── Backing Mechanism/
│   │   ├── Artifact/
│   │   └── diagrams/
│   └── Decentralization/
│       ├── Artifact/
│       └── diagrams/
```

---

## Artifact Matrix

| Protocol | Sustainability | Backing Mechanism | Decentralization |
|:---|:---|:---|:---|
| **Sky Ecosystem** | ✅ Complete | ✅ Complete | ✅ Complete |
| **Liquity V1 (LUSD)** | ✅ Complete | ✅ Complete | ✅ Complete |
| **Liquity V2 (BOLD)** | ✅ Complete | ✅ Complete | ✅ Complete |
| **Terra (UST)** | ⏳ Pending | ✅ Complete | ⏳ Pending |
| **Terra (UST)** | ⏳ Pending | ✅ Complete | ⏳ Pending |

---

## Sky Ecosystem / Sustainability (✅ Complete)

### Artifacts

| File | Type | Status |
|:---|:---|:---|
| `Sky_Sustainability_Profile_Jan2026.md` | Primary Profile | ✅ On-chain verified |
| `Sky-Economic-Sustainability.md` | Research Paper | ✅ 10 figures |
| `data/balance_sheet.json` | Data Source | Balance Sheet Estimates |
| `data/yield_metrics.csv` | Data Source | On-chain DSR |

### Key Verified Metrics (Block 24,171,462)

| Metric | Value | Source |
|:---|:---|:---|
| Combined Supply (DAI+USDS) | **$10.62B** | On-chain |
| DAI Supply | $4.22B | On-chain |
| USDS Supply | $6.40B | On-chain |
| USDC PSM Balance | **$3.99B** | On-chain (Pocket: 0x37305B1c...) |
| USDC Dependency | **37.6%** | Calculated |
| DSR APY | 1.25% | On-chain |
| Net Vow Position | −$34M | On-chain |
| Smart Burn Engine | $96M+ burned | CoinMarketCap |

---

## Sky Ecosystem / Decentralization (✅ Complete)

### Artifacts

| File | Type | Status |
|:---|:---|:---|
| `Sky_Decentralization_Profile_Jan2026.md` | Primary Profile | ✅ Framework v3.0 |
| `Sky-Decentralization-DeepDive.md` | Deep Dive Report | ✅ Stress Tested |
| `data/governance_delegation.json` | Data Source | MakerDAO API |
| `data/operational_liquidations.md` | Data Source | Bot Logs |

### Key Scorecard Metrics (Framework v3.0)

| Dimension | Score | Finding |
|:---|:---|:---|
| **Governance (G)** | 0.02 | 🔴 Plutocratic (Top-1 holds 86%) |
| **Collateral (C)** | 0.76 | 🔴 High Counterparty Risk (42%) |
| **Operational (O)** | 0.93 | 🟢 Competitive Keepers |
| **Emergency (E)** | 0.50 | 🟡 Whale-gated ESM |
| **Final Score** | **0.50** | 🔴 Effectively Centralized |

---

## Liquity Case Study (✅ Complete)

### Sustainability (V1 - The Reference)

| File | Status | Key Finding |
|:---|:---|:---|
| `Liquity_V1_Sustainability_Profile.md` | ✅ Complete | **Constrained**. 0% Yield. ETH-only. |

### Sustainability (V2 - The Risk)

| File | Status | Key Finding |
|:---|:---|:---|
| `Liquity_V2_Economic_Resilience.md` | ✅ Complete | "Yield via Pain". Market-driven rates. |

### Backing Mechanism (V1 - Platinum Standard)

| File | Status | Key Finding |
|:---|:---|:---|
| `Liquity_V1_Backing_Profile.md` | ✅ Complete | **Score 10/10**. 110% ETH. Kinetic Solvency. |
| `Liquity_V1_Backing_DeepDive.md` | ✅ Complete | Detailed Physics of Stability Pool. |

### Backing Mechanism (V2 - Federated)

| File | Status | Key Finding |
|:---|:---|:---|
| `Liquity_V2_Backing_Profile.md` | ✅ Complete | **Score 9/10**. Federated Architecture. |
| `Liquity_V2_Backing_DeepDive.md` | ✅ Complete | Detailed Analysis of Multi-Collateral Hub. |

### Decentralization (V1 - Platinum Standard)

| File | Status | Key Finding |
|:---|:---|:---|
| `Liquity_V1_Decentralization_Profile.md` | ✅ Complete | **Score 1.0/1.0**. Immutable. No Governance. |

### Decentralization (V2 - Risk Analysis)

| File | Status | Key Finding |
|:---|:---|:---|
| `Liquity_V2_Decentralization_Analysis.md` | ✅ Complete | **V2 Analysis**. Trades trustlessness for scale (LSTs). |

### Terra Case Study (Failed State)

* **Backing Mechanism (Algorithmic - FAILED)**
  * [Profile (Executive Verdict)](Terra/Backing%20Mechanism/Artifact/Terra_Backing_Profile.md)
  * [Deep Dive (Architecture & Death Spiral)](Terra/Backing%20Mechanism/Artifact/Terra_Backing_DeepDive.md)

### Comparison Metrics (3-Way Analysis)

| Metric | Sky Ecosystem | Liquity V1 (LUSD) | Liquity V2 (BOLD) |
|:---|:---|:---|:---|
| **Governance Model** | Delegated (MKR) | None (Immutable) | Initiative-Based (LQTY) |
| **Nakamoto Coefficient** | 1 (86% by Delegate) | N/A (No governance) | 1 (3 active voters) ⚠️ |
| **Collateral Risk** | High (USDC 70%+) | Zero (100% ETH) | Medium (80% RETH) ⚠️ |
| **Collateral HHI** | 7,200+ (Oligopoly) | 10,000 (Mono-asset) | 6,659 (High concentration) |
| **Total Equity** | ~$60M (Surplus Buffer) | $0 (Pass-through) | $0 (Pass-through) |
| **Governance Cost** | High (Delegates/CUs) | $0 | Low (Emissions only) |
| **Censorship Resistance** | Vulnerable (USDC freeze) | Unstoppable (Pure ETH) | Moderate (LST dependency) |
| **Data Verification** | ✅ On-chain verified | ✅ On-chain verified | ✅ Real mainnet snapshot |

**Key Findings:**

* **Sky**: Mature but centralized (USDC exposure, delegate concentration)
* **Liquity V1**: Censorship-resistant but economically stagnant (704% TCR, 95% supply contraction)
* **Liquity V2**: Bootstrapping phase with concerning concentration (1 governance voter, 80% RETH collateral)

### Data Provenance & Verification

**All metrics in this analysis use REAL on-chain data, verified via:**

| Protocol | Data Source | Verification Script | Snapshot Date |
|:---|:---|:---|:---|
| **Sky Ecosystem** | Ethereum Mainnet | `pipeline/scripts/data_fetchers/fetch_makerdao_data.py` | Jan 5, 2026 |
| **Liquity V1** | TroveManager Contract | `pipeline/scripts/data_fetchers/fetch_liquity_v2_onchain.js` | Jan 5, 2026 |
| **Liquity V2** | Mainnet Trove Snapshot | `analysis/Liquity/data/trove_snapshot_mainnet.csv` | Dec 9, 2025 |
| **V2 Operational** | Official Liquity API | `pipeline/scripts/data_fetchers/fetch_v2_operational_stats.js` | Jan 5, 2026 |

**Data Visualization Scripts:**

* **Decentralization Metrics**: `pipeline/scripts/visualization/generate_decentralization_plots.py`
* **Liquity Plots**: `pipeline/scripts/visualization/generate_liquity_plots.py`
* **MakerDAO/Sky Plots**: `pipeline/scripts/visualization/generate_makerdao_plots.py`

**Verification Standard:**

* ✅ **Real Data**: Direct blockchain queries or official API responses
* ⚠️ **Projections**: Clearly labeled where granular data unavailable (e.g., SP depositor distribution)
* 📊 **All data files** stored in respective `/data/` directories with timestamps and source attribution

---

## Usage

1. **For synthesis:** Use `Artifact/` folder contents
2. **For presentations:** Use `diagrams/` folder
3. **For deep reference:** Cross-check with `analysis/` folder

---

## Naming Convention

* `{Protocol}_{Topic}_Profile_{Date}.md` — Compact synthesis artifact
* `{Protocol}-{Topic}-DeepDive.md` — Detailed research paper
* Diagrams: Descriptive names (e.g., `revenue_composition.png`)
