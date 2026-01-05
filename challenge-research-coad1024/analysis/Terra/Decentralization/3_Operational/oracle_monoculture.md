# Operational Forensics: Oracle Monoculture

## Hypothesis
While 130 validators submitted prices, they were not independent "eyes". They ran identical software (`oracle-feeder`) sourced from a single repo, effectively centralizing the "Truth" mechanism.

## Evidence

1.  **Software Homogeneity:**
    *   **Repo:** `terra-project/oracle-feeder` (Maintained by TFL).
    *   **Usage:** >95% of validators ran this standard sidecar.
    *   **Source:** Binance API / CoinGecko API was hardcoded in the feeder config.

2.  **Failure Mode:**
    *   When the feeder logic encountered volatility limits (or CEX API limits), *all* validators failed simultaneously or reported identical stale data.
    *   This implies the effective number of "Independent Oracles" was **1** (The Codebase), not 130.

## Verified Metric
*   **Codebase Gini:** 1.0 (Absolute Centralization).
*   **Effective Independent Feeds:** < 5.
