# Formal Regime Analysis (MakerDAO)

**Goal**: Apply the Klages-Mundt stability framework to MakerDAO's RWA-heavy model.

---

## 1. The Stable Regime (RWA Anchored)

In the standard Klages-Mundt model, stability depends on the collateral ratio ($CT_t$) staying high.

For MakerDAO, the **Stable Regime is widened** by RWAs.

* **Logic**: US Treasuries have 0 volatility relative to the peg (USD).
* **Effect**: The "Variance Explosion" typically seen at 110% CR is dampened because 40-50% of the backing is non-volatile.
* **Result**: Maker can safely operate at lower collateral ratios (e.g., 101% for PSM) without entering the Unstable Regime.

**Diagram**: Variance Regime
![Variance Regime](../Diagrams/Formal%20Regime%20Analysis/variance_regime_plot.png)

## 2. The Unstable Regime (Deleveraging Spirals)

Despite RWAs, Maker is still vulnerable to **Submartingale Failure** if:

1. **Crypto Crash**: ETH/BTC collateral plunges, triggering auctions.
2. **RWA Freeze**: If regulators freeze the RWA portion, effectively $CT_t$ drops instantly.

### The "RWA De-peg" Spiral

If the market loses confidence in the RWA custody (e.g., Silicon Valley Bank style failure):

1. DAI holders rush to exit to ETH.
2. PSM drains.
3. Remaining backing is illiquid RWAs.
4. **Result**: DAI de-pegs downward, and Governance cannot sell RWAs fast enough.

---

## 3. Regime Thresholds

| Parameter | Threshold | Outcome |
| :--- | :--- | :--- |
| **RWA %** | > 80% | **Centralized Stablecoin** (e.g., Circle wrapper). |
| **Volatile %** | > 80% | **Standard DeFi Risk** (Deleveraging spirals). |
| **Ideal Mix** | ~50/50 | Maximum width of Stable Regime. |
