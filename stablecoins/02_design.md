## 2. Design

### A. Scenario 1: Environment without Liquidation Risk

*Constraint: How would you design an ideal stablecoin in a world where collateral cannot lose value?*

**Proposed Architecture: "Unity" (1:1 On-Chain Wrapper)**

* **Core Mechanism**: Issue stablecoins at a perfect **1:1 ratio** against any deposited asset. Since collateral value is static/up-only, over-collateralization is obsolete.
* **Advantage**: **100% Capital Efficiency**. 1 ETH ($2000) mints 2000 Unity. No liquidations, no auctions.
* **Trade-off**: None in this theoretical world.

### B. Scenario 2: Environment with Highly Risky Collateral

*Constraint: How would you design a stablecoin where all collateral is highly volatile and prone to liquidation?*

**Proposed Architecture: "Duo Network" (Dual-Tranche Structure)**

* **Core Mechanism**: Splits the volatile collateral (e.g., ETH) into two distinct tokens:
    1. **Class A (Stable)**: Absorbs minimal volatility, maintains $1.00 peg.
    2. **Class B (Volatile)**: Absorbs *all* the volatility (leverage). Acts as a buffer for Class A.
* **Mitigation Strategy**: **Coupon/Reset Mechanism**. If Class B value drops too low, the system resets or converts Class A into a coupon to restore the ratio.
* **Trade-off**: **Liquidity Constraints**. Class A stability depends entirely on the demand for Class B (leverage seekers). If no one wants leverage, Class A cannot be minted/maintained efficiently.
