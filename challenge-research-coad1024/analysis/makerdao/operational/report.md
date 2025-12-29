# Operational Decentralization Report: MakerDAO Liquidators

## Executive Summary

Analysis of **100 liquidation attempts** (including both successful and failed transactions) reveals a **moderately unconcentrated** keeper ecosystem, with an HHI of approximately **1136**. The top keeper controls 27% of the activity, indicating significant but not overwhelming dominance.

## Key Metrics

| Metric | Value | Description |
| :--- | :--- | :--- |
| **Total Events** | 100 | Total liquidation attempts (Success + Error) |
| **Unique Keepers** | 24 | Number of distinct addresses participating |
| **Top Keeper Share** | 27% | Address: `0x008Ca3a9C52e0F0d9Ee94d310D20d67399d44f6C` |
| **CR3** | 47% | Market share of top 3 keepers |
| **CR5** | 60% | Market share of top 5 keepers |
| **HHI** | **1136** | Herfindahl-Hirschman Index |

## Interpretation (DOJ Standards)

- **HHI < 1500**: **Unconcentrated** (Current Status: 1136)
- **1500 < HHI < 2500**: Moderately Concentrated
- **HHI > 2500**: Highly Concentrated

## Conclusion

The operational layer for liquidations demonstrates a healthy level of decentralization when considering all attempts. The HHI of 1136 indicates a competitive environment where multiple keepers are actively attempting to liquidate positions, even if some attempts fail.
