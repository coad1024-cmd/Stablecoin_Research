# Sustainability Profile: Sky Ecosystem (DAI/USDS)

**Date:** January 5, 2026
**Analyst:** Research Challenge Team
**Framework Version:** 1.0 (Post-Refactor)
**Data Source:** On-chain contract calls (DAI ERC20, Pot, Vow) via Ethereum Mainnet RPC + DefiLlama/Makerburn cross-reference.

> **Note:** Sky is the rebranded MakerDAO protocol. This analysis covers DAI (legacy) and USDS (new) stablecoins under unified Sky governance.

## 1. Executive Summary

Sky (formerly MakerDAO) has evolved from a liquidation-dependent protocol into a **Yield-Capturing Shadow Bank (Type B)**. Its primary sustainability mechanism is no longer the liquidation of risky collateral, but the arbitration of the spread (NIM) between RWA yields and the DeFi risk-free rate (DSR/SSR).

**Sustainability Scorecard:**
*   **Economic Viability:** ⚠️ **Transitional** (SBE burning $96M+ SKY, but Q1 2025 showed $5M loss)
*   **Collateral Stability:** ⚠️ Moderate (RWA latency + USDC dependency)
*   **Governance:** ⚠️ Centralized (Endgame restructuring in progress)
*   **Legacy Debt:** ❌ **$281M unbacked debt in Vow** (historical, not actively cleared)

---

## 2. Economic Viability (The Engine)

### Business Model Classification
**Type B: Yield-Capturing.**
Historically a "Type C" (Fee-based) protocol, MakerDAO successfully pivoted to monetizing its collateral backing (RWAs). While 2025 saw a resurgence of crypto-native lending revenues (>50%), the **structural floor** of the protocol's solvency is provided by the RWA portfolio.

### Key Metrics (January 2026)

| Metric | Value | Source | Sustainability Signal |
| :--- | :--- | :--- | :--- |
| **DAI Total Supply** | **4.22 Billion** | On-chain (`totalSupply()`) | ERC20 total; "circulating" is ~3.7B per Makerburn. |
| **DSR APY** | **1.25%** | On-chain (`Pot.dsr()`) | ✅ **Verified.** |
| **Net Interest Margin (NIM)** | **~3.75%** | Calculated | Asset Yield ~5% - DSR 1.25% = Strong spread. |
| **Collateral Concentration (HHI)** | **0.29** | Calculated | **Moderate.** ETH (~35%), USDC-PSM (~33%), RWAs (~23%). |
| **Surplus Buffer (hump)** | **DISABLED** | On-chain (`Vow.hump() = MAX_UINT256`) | ⚠️ Old Flapper mechanism deprecated. |
| **Vow DAI Balance** | **$247M** | On-chain (`Vat.dai(Vow)`) | Current surplus funds. |
| **Vow Sin (Bad Debt)** | **$281M** | On-chain (`Vat.sin(Vow)`) | ❌ Legacy unbacked debt. |
| **Net Vow Position** | **-$34M DEFICIT** | Calculated | Vow has more debt than surplus. |
| **Smart Burn Engine (SBE)** | **$96M+ burned** | CoinMarketCap (Feb 2025 - Jan 2026) | ✅ Burning ~$1M/day of SKY tokens. |

*   **Capital Efficiency:** Moderate. RWAs allow 1:1 backing efficiency but regulatory constraints limit velocity.
*   **LDR (2023):** **< 0.4%** — Liquidation revenue was $0.4M out of ~$113M total (Steakhouse Financial). Indicates **non-liquidation-dependent** business model.

### Smart Burn Engine (SBE) — New Sustainability Mechanism

Sky replaced the traditional "Flapper" surplus auctions with the **Smart Burn Engine**:

| SBE Metric | Value | Source |
| :--- | :--- | :--- |
| **Launch Date** | February 2025 | Governance |
| **Daily Burn Rate** | ~$1M USDS worth of SKY | CoinMarketCap |
| **Total Burned (Feb 2025 - Jan 2026)** | **>$96 Million** | CoinMarketCap |
| **Supply Reduction** | ~3.2% of circulating SKY | Official Stats |
| **Funding Source** | Self-sustaining (staking rewards + fees) | OKX |

**Implication:** The old `hump`-based surplus mechanism is deprecated. Sustainability is now measured by SBE burn rate, not surplus buffer size.

---

## 3. Collateral Regime Stability (Stress Tests)

MakerDAO operates in a **Hybrid Regime**, relying on both crypto-native overcollateralization (ETH) and legal trust assumptions (RWA/USDC).

### Historical Stress Performance

#### Test 1: The 70% Collateral Crash (Black Thursday 2020)
*   **Status:** ⚠️ **Degraded / Recovered**
*   **Event:** ETH dropped ~50%, Gas spiked.
*   **Failure:** Liquidation auctions failed due to congestion/keeper capital constraints. **~5.67M DAI bad debt** accumulated.
*   **Resolution:** Protocol minted MKR to recapitalize. Peg restored.
*   **Implication:** Demonstrated that on-chain liquidation guarantees are probabilistic, not deterministic.

#### Test 2: The Collateral Contagion (USDC Depeg 2023)
*   **Status:** ⚠️ **Degraded**
*   **Event:** USDC depegged to $0.88.
*   **Exposure:** DAI was ~54.5% backed by USDC.
*   **Failure:** DAI depegged to ~$0.88, tracking its collateral.
*   **Resolution:** Emergency governance parameters (1% swap fee) enacted *post-facto*. Peg returned only when US Gov bailed out SVB/Circle.
*   **Implication:** MakerDAO cannot structurally withstand a failure of its centralized collateral partners.

#### Test 3: Liquidity Freeze (FTX November 2022)
*   **Status:** ✅ **Robust**
*   **Event:** Market-wide liquidity contraction following FTX/Alameda collapse.
*   **Peg:** ✅ Maintained (no significant deviation, unlike USDT which dropped to $0.985).
*   **Supply Impact:** -5% (~$300M single-day reduction as users repaid debt).
*   **Liquidations:** Only **26 vaults** liquidated (1.2M DAI) — orderly deleveraging.
*   **Bad Debt:** **$0** — No protocol losses attributable to FTX.
*   **Source:** Galaxy Research, Defi Explore.
*   **Implication:** DeFi overcollateralization model proved resilient where CeFi failed.

---

## 4. Governance & Adaptability

### Operational Structure
*   **Regime:** Active Governance (DAO + Delegates).
*   **Mutability:** High. Parameters (Rates, Debt Ceilings) can be changed within ~24-48 hours (GSM pause).
*   **Crisis Response:** Proven capability to pass "Emergency Executive Votes" (e.g., during USDC depeg).

### Risks
*   **Regulatory Attack Surface:** The integration of billions in RWAs creates a localized nexus for regulation. The "Endgame" strategy attempts to obfuscate this via SubDAOs, but the *economic* dependency remains.
*   **Complexity:** The transition to "Sky" introduces massive systemic complexity, increasing the probability of unforeseen mechanism bugs or governance/economic arbitrage exploits.

---

## 5. Synthesis: The Tradeoff

Sky has traded **Censorship Resistance** for **Scale and Revenue**, but the transition is **incomplete**:

### Wins:
*   **SBE is functional** — $96M+ burned in 11 months, ~3.2% supply reduction
*   **Revenue model validated** — Crypto-native lending reclaimed >50% of revenue in 2025
*   **Governance proved responsive** — Emergency votes during crises (USDC depeg, FTX)

### Unresolved Risks:
*   **$281M legacy bad debt** sits unbacked in Vow — no active clearance mechanism
*   **Q1 2025 showed $5M loss** — Migration costs (DAI→USDS incentives) exceed revenue
*   **Net Vow position is -$34M** — More liability than equity in the core accounting contract
*   **Centralized counterparty risk** — US Fed, Circle, and regulators still control destiny

### Honest Verdict:

| Aspect | Status |
|:---|:---|
| **Peg Stability** | ✅ Maintained |
| **Transaction Throughput** | ✅ Functional |
| **Economic Sustainability** | ⚠️ **In Transition** — SBE offsets losses but legacy debt remains |
| **Decentralization** | ❌ **Compromised** — RWA dependency, SubDAO complexity |

**Final Assessment:** Sky is a **functional financial machine** with significant **technical debt** (both literal and metaphorical). The SBE demonstrates a path to sustainability, but the -$34M Vow deficit and $281M uncleared bad debt are liabilities any serious analysis must acknowledge.
