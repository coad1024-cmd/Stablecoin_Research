# Liquity Analysis

## 1. Backing Mechanism

Liquity is a decentralized borrowing protocol that allows users to draw interest-free loans against Ether used as collateral. Loans are paid out in **LUSD** (a USD pegged stablecoin) and need to maintain a minimum collateral ratio of **110%**.

### Core Components

* **Troves**: Individual debt positions where users lock ETH and mint LUSD.
* **Stability Pool**: The first line of defense against liquidations. LUSD holders deposit tokens here to absorb debt from liquidated Troves. In return, they receive the collateral (ETH) from the liquidated Troves and LQTY rewards.
* **Redemption Mechanism**: A hard price floor mechanism. Any LUSD holder can redeem LUSD for ETH at face value ($1), minus a redemption fee. This creates a direct arbitrage opportunity if LUSD trades below $1.
* **Recovery Mode**: Triggered when the Total Collateral Ratio (TCR) of the system falls below **150%**. In this mode, Troves with collateral ratios between 110% and the TCR can be liquidated, incentivizing deleveraging.

### Comparison to MakerDAO

Unlike MakerDAO, which accepts multiple collateral types (USDC, WBTC, RWAs), Liquity is **ETH-only** (in V1). This reduces regulatory risk and contagion risk from other assets but limits scalability to the growth of ETH.

## 2. Sustainability

Liquity's sustainability model relies on one-time fees rather than continuous interest rates (in V1).

* **Revenue Sources**:
  * **Borrowing Fee**: A one-time fee charged when minting LUSD (typically 0.5% - 5%).
  * **Redemption Fee**: A fee charged when redeeming LUSD for ETH.
* **Tokenomics (LQTY)**:
  * LQTY is the secondary token used to incentivize frontend operators and Stability Pool depositors.
  * LQTY stakers capture **100%** of the protocol's revenue (borrowing and redemption fees).
  * This creates a direct correlation between protocol usage and token value, without the need for governance buybacks or burns.

## 3. Decentralization

Liquity is designed to be one of the most decentralized stablecoins.

* **Governance-Free**: The core smart contracts are **immutable**. There is no governance voting to change parameters (like MCR, fees, etc.). This eliminates the "human factor" and governance attack vectors.
* **Frontend Operators**: Liquity does not run its own frontend. Instead, it incentivizes third-party operators to host frontends by rewarding them with a share of LQTY tokens. This ensures censorship resistance at the access layer.
* **Oracle Dependence**: Liquity relies on Chainlink for ETH/USD price feeds, with Tellor as a fallback. While this introduces an external dependency, the dual-oracle system mitigates risk.
