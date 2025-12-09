# Implementation Plan - Liquity V2 Data & Visualizations

## Goal

Generate missing visualizations (Plots) and ensure data is correctly organized, matching the MakerDAO analysis standard.

## Proposed Changes

### 1. Collateral Analysis

- **Script Update**: `analyze_v2_collateral.py`
  - Add `matplotlib` to generate a **Pie Chart** of Collateral Composition.
  - Save plot to `collateral/plots/composition.png`.

### 2. Governance Analysis

- **Script Update**: `analyze_v2_governance.py`
  - Add `matplotlib` to generate a **Lorenz Curve** or Bar Chart of Top Voters.
  - Save plot to `governance/plots/voting_power.png`.

### 3. Operational Analysis

- **Script Update**: `analyze_frontends.py`
  - Add `matplotlib` to generate a **Bar Chart** of Frontend shares.
  - Save plot to `operational/plots/frontends.png`.
