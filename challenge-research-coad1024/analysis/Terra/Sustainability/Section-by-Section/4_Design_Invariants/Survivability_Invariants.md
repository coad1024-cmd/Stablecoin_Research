# 4. Design Invariants: The Physics of Survivable Stablecoins

This analysis has empirically demonstrated that Terra's collapse was not a "black swan" or a "market manipulation," but a **deterministic mechanical failure**. The system violated fundamental control theory invariants.

Any future algorithmic stablecoin must respect these three "Laws of Survivability" to avoid the same fate.

---

## Invariant 1: The Oracle Latency Bound (Nyquist Stability)

**Problem:** Using a 30-second oracle to price a 1-second asset.
**Empirical Proof:** [Figure 3.2 (Oracle Deviation)](../3_Operational_Bottlenecks/Critical_Failures.md#31-oracle-latency-sensor-lag) showed that when LUNA price volatility exceeded the Oracle refresh rate, the protocol effectively subsidized arbitrageurs to drain the treasury.

### The Invariant
$$ f_{\text{oracle}} \ge 2 \cdot f_{\text{volatility}} $$

*   **$f_{\text{oracle}}$**: The frequency of on-chain price updates.
*   **$f_{\text{volatility}}$**: The maximum frequency of significant price changes (e.g., >1% moves).

**Implementation Rule:**
If the Oracle cannot update fast enough (e.g., block time limits), the **System Must Halt**.
*   **Safety Mechanism:** Compare $\Delta Price_{\text{CEX}}$ vs $\Delta Price_{\text{Oracle}}$. If divergence > Threshold, pause redemptions automatically.

---

## Invariant 2: The Liquidity Reaction Bound

**Problem:** Minting caps ($293M/day) were static while exit demand ($1.2B/day) was dynamic.
**Empirical Proof:** [Figure 3.1 (Liquidity Throttle)](../3_Operational_Bottlenecks/Critical_Failures.md#32-liquidity-throttle-removal-cpmm-expansion) showed that rigid caps forced a "Hard Default" (Peg Loss) instead of a "Soft Default" (Slippage), leading to panic.

### The Invariant
$$ \text{Reserves} \ge \text{MaxDailyOutflow} \times \text{ReactionTime} $$

*   **Reserves**: *Exogenous* assets only (BTC/USDC). Endogenous assets (LUNA) count as 0 during a crisis (See [Figure 2: ECR](../2_Key_Metrics/Health_Indicators.md#6-effective-collateralization-ratio-ecr)).
*   **Reaction Time**: Time required for governance or automated circuit breakers to deploy extraordinary measures (e.g., 7 Days).

**Implementation Rule:**
Solvency is a function of time. If Governance takes 7 days to deploy reserves, you must hold 7 days of peak-outflow liquidity on-chain.
*   **Terra Case:** Held < 2 Days of liquidity vs a 7-day governance cycle.

---

## Invariant 3: The Convexity Principle (Anti-Death Spiral)

**Problem:** Making it cheaper to exit as the door gets crowded.
**Empirical Proof:** [Section 3.3 (Prop 1164)](../3_Operational_Bottlenecks/Critical_Failures.md#32-liquidity-throttle-removal-cpmm-expansion) showed that increasing the BasePool (lowering slippage) accelerated the hyperinflation.

### The Invariant
$$ \frac{d(\text{Spread})}{d(\text{Volume})} > 0 $$

*   **Spread**: The cost to redeem stablecoin for collateral.
*   **Volume**: The magnitude of redemption demand.

**Implementation Rule:**
The redemption curve must be **strictly convex**.
*   Small redemptions $\to$ Low Slippage ($1 \approx 1$).
*   Massive redemptions $\to$ Punitive Slippage ($1 \approx 0.5$).
*   **Never** manually intervene to lower the cost of exit during a run. This effectively subsidizes whales at the expense of remaining holders.

---

## Summary of Findings

| Metric | Terra's Value | Safe Invariant | Verdict |
| :--- | :--- | :--- | :--- |
| **Oracle Lag** | 30s Blocks vs 1s Crash | Real-time / Pause | **Violated** |
| **Exogenous Ratio** | 0.15 (BTC/UST) | > 1.0 (Liquid) | **Violated** |
| **Redemption Cost** | Lowered (Prop 1164) | Must Increase | **Violated** |

**Conclusion:**
Terra did not fail because of "FUD" or "Attackers". It failed because it was engineered to be unstable in specific regimes. These invariants define the "Safe Operating Envelope" for any future design.
