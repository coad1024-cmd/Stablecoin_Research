# 1. Data Acquisition Plan (Strict Empirical)

## Overview
This plan defines the sources and methodologies for acquiring verifiable historical data for the Terra/LUNA collapse (May 2022). All simulation is strictly forbidden. We rely on public archive nodes and historical market data APIs.

---

## Metric 1: Net Interest Margin (NIM)
**Definition:** Anchor Deposits rate vs Yield Reserve depletion.
**Primary Source (On-chain):**
*   **Terra Classic LCD:** `https://terra-classic-lcd.publicnode.com`
*   **Contract:** Anchor Overseer `terra1tmnqgvg567ypvsvk6rwsga3srp7e3lg6u0elp8`
*   **Query:** `epoch_state` (stores deposit_rate) or `market` contract state.
*   **Fields:** `deposit_rate`, `borrow_rate`.
**Secondary Source (Off-chain):**
*   **Coingecko:** ANC Price (proxy for governance sentiment, though not direct NIM).
**Blind Spot:** Granular reserve values (`yield_reserve`) might require deep archive queries (WASM state export). If unavailable, we will mark as UNPRODUCIBLE.

## Metric 2: Effective Collateralization Ratio (ECR)
**Definition:** `(LUNA_Mcap * 0.7 + LFG_Reserves) / UST_Supply`.
**Primary Source:**
*   **Coingecko API:**
    *   ID: `terra-luna` (now `terra-luna-classic`) vs `terra-usd` (now `terra-classic-usd`).
    *   Fields: `market_caps` (daily/hourly).
    *   Resolution: Hourly during crash (May 7-13).
**LFG Reserves:**
*   **LFG Public Wallet:** `bc1q...` (Bitcoin). We will use verifiable third-party snapshots (Glassnode/Twitter LFG official disclosures) if direct chain parsing is rate-limited.

## Metric 3: Exit Coverage Ratio (XCR)
**Definition:** `Curve3Pool_Liquidity / Anchor_Exit_Flows`.
**Primary Source:**
*   **Curve API (Ethereum):** Historical pool stats for 3pool (if available).
*   **Proxy:** Coingecko/Binance `Volume` for UST.
*   **Failure Cond:** If Curve historical balances are not exposed via free API, we mark UNPRODUCIBLE.

## Metric 4: Redemption Friction Curve
**Definition:** On-chain swap spread.
**Primary Source:**
*   **Terra Classic LCD:** `x/market` module params.
*   **Endpoint:** `/terra/market/v1beta1/params`
*   **History:** We need historical param changes (Prop 1164). This requires querying governance proposals.
    *   `/cosmos/gov/v1beta1/proposals/1164`

## Metric 5: Oracle Deviation
**Definition:** Validator Votes vs Binance Spot.
**On-chain Source:**
*   **Terra LCD:** `/terra/oracle/v1beta1/denoms/uusd/exchange_rate` (Historical requires archive node with `x-cosmos-block-height` header).
**Off-chain Source:**
*   **Binance API:** `LUNCUSDT` (or equivalent legacy symbol) 1m klines.
**Join:** Timestamp alignment.

## Metric 6: Reflexivity Evidence
**Definition:** Supply expansion vs Price.
**Primary Source:**
*   **Coingecko/LCD:** LUNA Circulating Supply vs Price.

---

## Execution Strategy
1.  **Fetch Scripts:** Run `fetch_market_data.py` (Coingecko/Binance) -> `data/market_history.csv`.
2.  **On-Chain Scripts:** Run `fetch_chain_state.py` (LCD) -> `data/chain_state.csv`.
3.  **Visualization:** Generate plots ONLY if data exists.
