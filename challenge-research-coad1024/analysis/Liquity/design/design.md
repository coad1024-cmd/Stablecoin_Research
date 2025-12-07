# Stablecoin Design Scenarios

## 1. Environment Without Liquidation Risk

**Scenario**: A world where collateral assets cannot lose value (e.g., strictly non-decreasing value assets).

### Design: "The Yield-Bearing Wrapper"

Since solvency risk is eliminated (collateral value $\ge$ debt value always), the primary focus shifts to **capital efficiency** and **liquidity**.

* **Mechanism**: 1:1 Peg.
  * User deposits $1 worth of Asset A.
  * Protocol mints 1 Unit of Stablecoin S.
* **No Over-collateralization**: MCR = 100%. There is no need for a buffer since the asset cannot drop below the debt value.
* **Yield Generation**:
  * Since the protocol holds the underlying asset, and the asset is "risk-free" in terms of principal loss, the protocol can focus on maximizing yield (if the asset generates yield) or simply holding it.
  * **Rebasing**: The stablecoin supply could automatically increase as the collateral value increases (if it's an appreciating asset), distributing value to holders.
* **Redemption**: Instant 1:1 redemption.
* **Advantages**: Maximum capital efficiency. Zero liquidation penalties.

## 2. Environment With Highly Risky Collateral

**Scenario**: All collateral assets are highly volatile and prone to rapid crashes (e.g., meme coins, highly volatile crypto).

### Design: "The Fortress Protocol" (Tranched Risk & Hyper-Collateralization)

To survive in a high-volatility environment, the system must prioritize **solvency buffers** and **rapid reaction speeds**.

* **Mechanism 1: Hyper-Overcollateralization**
  * **MCR**: 500% or higher. To mint $100 of stablecoin, you need $500 of collateral. This provides a massive buffer against 80% drawdowns.
* **Mechanism 2: Risk Tranching (Senior/Junior)**
  * **Senior Tranche (The Stablecoin)**: Has first claim on collateral. Protected by the Junior tranche.
  * **Junior Tranche (The Shield)**: Users who want leverage deposit collateral to mint Junior tokens. They absorb the first X% of losses. In exchange, they earn high yields from borrowing fees.
* **Mechanism 3: Protocol-Owned Liquidity (POL) as Insurance**
  * A significant portion of fees (minting/redemption) is directed to a "System Surplus Buffer" that sits outside the user troves. This acts as a backstop if individual troves fail.
* **Mechanism 4: Dynamic Circuit Breakers**
  * If volatility (measured by oracle variance) exceeds a threshold, **Minting is paused** to prevent users from entering at inflated prices.
  * **Redemptions remain open** to allow exit.
* **Mechanism 5: Dutch Auction Liquidations**
  * Instead of fixed-discount liquidations, use fast Dutch auctions to clear bad debt at the best possible market price, minimizing loss for the borrower and the system.
