## 1. Analysis

### Objective

Compare Liquity (LUSD) with MakerDAO (DAI), focusing on their architectural and economic differences.

### Comparison Matrix

| Feature | Liquity (LUSD) | MakerDAO (DAI) |
| :--- | :--- | :--- |
| **Type/Mechanism** | Decentralized Borrowing Protocol (ETH-only collateral) | Multi-Collateral CDP (ETH, WBTC, USDC, RWA) |
| **Key Metric** | MCR: 110% (Normal Mode) | MCR: 130-150% (Vault dependent) |
| **Governance** | **Governance-Free** (Immutable Contracts) | **Active Governance** (MKR Voting) |
| **Peg Mechanism** | Hard Price Floor via Redemption | Soft Peg via Interest Rates (DSR/SF) |
| **Liquidation** | Instant via Stability Pool | Auctions (Dutch) |
| **Fees** | One-time Borrowing/Redemption Fee | Continuous Stability Fee (Interest) |

### Deep Dive

#### A. Backing Mechanism

* **Liquity**:
  * **Collateral**: Exclusively **Ether (ETH)** in V1. This eliminates risks associated with centralized assets (USDC, WBTC) or RWAs, making LUSD a "purist" decentralized stablecoin.
  * **Troves**: Individual debt positions. Users lock ETH and mint LUSD.
  * **Stability Pool**: The primary liquidation mechanism. Users deposit LUSD to absorb debt from liquidated Troves instantly. In return, they receive the collateral (ETH) and LQTY rewards. This avoids the latency and slippage of auctions.
  * **Redemption**: A hard price floor mechanism. Any LUSD holder can redeem LUSD for ETH at face value ($1 minus fees). This creates a direct arbitrage loop, ensuring LUSD $\ge$ $1 (minus fee).
  * **Recovery Mode**: If TCR < 150%, the system liquidates risky Troves (up to 150% CR) to restore solvency.

* **MakerDAO**:
  * **Collateral**: Diversified basket including volatile crypto (ETH, WBTC) and centralized RWAs (US Treasury Bills, USDC).
  * **Auctions**: Liquidations are handled via Dutch auctions, which can be slower and depend on market liquidity at the time of the auction.
  * **PSM**: The Peg Stability Module (PSM) allows 1:1 swaps with USDC, effectively hard-pegging DAI to USDC but introducing centralization risk.

#### B. Sustainability

* **Liquity**:
  * **Fee Model**: Charges a **one-time Borrowing Fee** (0.5% - 5%) and a **Redemption Fee**. There are no continuous interest rates (in V1).
  * **Revenue**: 100% of fees go to **LQTY stakers**. There is no protocol treasury or surplus buffer managed by governance.
  * **Incentives**: LQTY is issued to Stability Pool depositors and Frontend Operators. This aligns incentives for growth and security without indefinite inflation (LQTY supply is capped).

* **MakerDAO**:
  * **Fee Model**: Charges continuous **Stability Fees** (interest) on debt.
  * **Revenue**: Fees are used to burn MKR (buyback) and fund the Surplus Buffer.
  * **Expenses**: MakerDAO has significant operational costs (Core Units, delegates) funded by the protocol.

#### C. Decentralization

* **Liquity**:
  * **Immutable**: The core smart contracts are immutable. No admin keys, no upgrades, no governance voting. This protects the protocol from "human" vectors of attack or regulatory pressure on a governance body.
  * **Frontend Operators**: Liquity has **no official frontend**. It relies on a network of third-party operators (incentivized by LQTY) to host interfaces. This ensures censorship resistance at the access layer; if one frontend is taken down, others remain.
  * **Oracle**: Relies on Chainlink (primary) and Tellor (fallback).

* **MakerDAO**:
  * **Governance**: Heavily relies on MKR holders to set risk parameters, onboard collateral, and manage the protocol. This introduces "governance attack" vectors and centralization tendencies (delegate concentration).
  * **Assets**: Significant exposure to centralized assets (USDC, RWAs) means the protocol can be censored or frozen by centralized entities (e.g., Circle, Coinbase).
