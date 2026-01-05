# Formal Regime Analysis: The Physics of Stability

**Goal**: Apply the Klages-Mundt (2023) theoretical framework to define the mathematical bounds of Liquity V2's stability. We move beyond "Audit Secure" to "Economically Secure."

---

## 1. The Framework: Stable vs. Unstable Regimes

Stablecoins are not binary (Safe/Unsafe). They exist in distinct dynamic regimes defined by the behavior of their volatility.

### A. The Stable Regime (Bounded Variance)
*   **Definition**: A state where the variance of the stablecoin price ($Z_t$) is bounded and mean-reverting.
*   **Condition**: Collateral levels ($N_t$) are sufficiently high to dampen exogenous shocks.
*   **Liquity V2 Context**: When `TCR > 150%`, the system absorbs ETH price shocks via the Stability Pool without triggering a feedback loop.

### B. The Unstable Regime (Volatility Amplification)
*   **Definition**: A state where the sensitivity of the stablecoin price to collateral shocks exceeds 1 ($\partial h / \partial \rho > 1$).
*   **The "Variance Explosion"**: In this regime, a 1% drop in ETH leads to a $>1\%$ deviation in the BOLD peg (or implied cost of capital).
*   **Trigger**: When `TCR` approaches `MCR` (110%) and the Stability Pool is empty.

**Visual Reference**:
![Variance Regime Plot](../Diagrams/Formal%20Regime%20Analysis/variance_regime_plot.png)
*Figure 1: The Transition from Stable to Unstable Regime. X-axis: Collateral Ratio. Y-axis: Price Volatility (Variance). Note the exponential spike as CR approaches 110%.*

---

## 2. The Submartingale Failure Mode (The "Deleveraging Spiral")

The most critical insight from Klages-Mundt (Section 2.5.3) is that stability is impossible if the collateral asset price process $(X_t)$ is **not a submartingale** (i.e., if $E[X_{t+1}] < X_t$).

### A. The Mechanism
1.  **Negative Drift**: Market expects ETH to fall (Negative drift).
2.  **Rational Exit**: Borrowers rush to close positions (buy BOLD) to save equity.
3.  **Liquidity Crunch**: If BOLD sellers evaporate (holding for redemption), a **Short Squeeze** occurs ($Z_t > 1.05$).
4.  **Insolvency Acceleration**: The rising liability value ($Z_t$) combined with falling asset value ($X_t$) accelerates insolvency faster than linear models predict.

### B. Liquity V2 Defense
*   **Redemption Mechanism**: This is the primary counter-force. It caps $Z_t$ at $1.00 (technically slightly higher due to fees).
*   **Critique**: Redemptions work *if* there is liquidity. In a true spiral, if redemption assumes 1:1 payout but the backing collateral is crashing faster than the block time, the "Economic Peg" breaks even if the "Contract Peg" holds.

**Visual Reference**:
![Submartingale Spiral Flow](../Diagrams/Formal%20Regime%20Analysis/submartingale_spiral_flow.png)
*Figure 2: The Feedback Loop of a Deleveraging Spiral. Negative Expectation -> Repayment Demand -> Liability Appreciation -> Faster Insolvency.*

---

## 3. Path Dependence & Hysteresis

Stability is not just about the *current* state, but the *history* (which determines the initial conditions).

*   **Theorem 2.6 (Variance Ordering)**: Explicitly states that for two states $s$ and $u$ differing only in initial collateral $N_{t-1}$, if $N^s > N^u$, then $Var(Z^s_t) < Var(Z^u_t)$.
*   **Implication for Liquity**: A system that has suffered collateral drawdown (lower $N_{t-1}$) is mathematically more volatile than one with healthy collateral, *even if the external market conditions are identical*. This defines "Recovery Mode" (CR < 150%) as a distinct regime of amplified variance.

---

## 4. Conclusion: The Mathematical Hard Limit

Liquity V2 cannot survive a scenario where:
1.  ETH enters a sustained freefall (Submartingale).
2.  **AND** The Stability Pool is depleted.
3.  **AND** Gas prices prevent timely Redistribution.

Under these conditions, the system mathematically *must* fail (break peg downward), regardless of the code quality.
