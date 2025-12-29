# 5. Stress Tests & Scenario Analysis

This section constructs a formal stress test of the Terra protocol, integrating the **RiskDAO "Stability Stress Test"** framework and **Briola et al. (Toffalini)** agent-based modeling.

## 1. Theoretical Framework: The Stability Condition

Following the RiskDAO methodology, the stability of an algorithmic stablecoin is defined by the probability of survival under stochastic demand shocks.

**The Stability Inequality:**
$$ \Delta S_{out} \le \min\left( L_{curve} + L_{CEX}, \rho \cdot M_{cap} \right) $$

Where:
*   $\Delta S_{out}$: Net Outflow Shock (Selling Pressure).
*   $L_{curve}$: On-chain liquidity depth (Curve 3Pool).
*   $L_{CEX}$: Off-chain liquidity depth (Binance).
*   $M_{cap}$: Market Cap of the Collateral Token (LUNA).
*   $\rho$: Slippage Coefficient (Elasticity of LUNA price to minting).

**The Death Spiral Condition ($G > 1$):**
A system enters a death spiral when the **Reflexivity Gain ($G$)** exceeds unity:
$$ G = \frac{\partial (\text{Panic})}{\partial (\text{Price})} \times \frac{\partial (\text{Price})}{\partial (\text{Supply})} > 1 $$
When $G > 1$, every unit of minting (to stabilize UST) causes a drop in LUNA price that induces *more* than one unit of additional panic selling.

---

## 2. Methodology: Agent-Based Simulation (Briola Framework)
We model the protocol's response using three agent classes identified in **Briola et al. (Anatomy of a Failure)**:
*   **Arbitrageurs (Type A):** Profit-maximizing, latency-sensitive. Exploit Price Spreads ($P_{oracle} \neq P_{mkt}$).
*   **Whales (Type W):** Large holders capable of single-handedly shifting the $L_{curve}$ ratio.
*   **HODLers (Type H):** Passive capital with a "Confidence Threshold" ($C_t$). They convert to Sellers when Peg < $0.95.

---

## 3. Scenario A: The Single-Whale Shock (Baseline)
**Scenario:** A single entity dumps $400M UST (approx 2% of supply) into the Curve pool in <10 minutes.

### Simulation Trace
1.  **Trigger:** $400M Sell Order.
2.  **Imbalance:** Curve Pool Ratio shifts to **80% UST**.
3.  **Price Impact:** Spot UST drops to **$0.97**.
4.  **Mechanism Response:**
    *   Arbitrageurs buy UST at $0.97 \to$ Mint LUNA.
    *   **Absorption:** LUNA Market Cap ($30B) absorbs $400M dilution (1.3% impact).
    *   **Reflexivity:** $G < 1$. Market confidence holds.

**Verdict:** **Pass.** The protocol satisfies the Stability Inequality ($\Delta S_{out} \ll \rho \cdot M_{cap}$).

---

## 4. Scenario B: The "Soros" Coordinated Attack (The Crash)
**Scenario:** A coordinated attack exploiting **Oracle Latency** (Toffalini's "latency arbitrage") and **Liquidity Cascades**.

### Simulation Trace
1.  **Trigger:** Curve Imbalance forced to 85% ($500M Sell).
2.  **Correlation Shock:** Attacker shorts LUNA futures.
3.  **The "RiskDAO" Cascade:**
    *   LUNA Price drops 20% due to shorting.
    *   **New Collateral Capacity:** $M_{cap}$ shrinks from $30B \to $20B.
    *   **The Flippening:** $M_{cap}$ approaches UST Supply ($18B$).
4.  **Oracle Exploit (3.2):**
    *   LUNA crashing 10% per minute.
    *   Oracle reports price $P_{t-30s}$ (Higher).
    *   **Infinite Money Glitch:** Arbitrageurs mint "phantom value," accelerating inflation.
5.  **Result:**
    *   **Insolvency:** $\Delta S_{out} > M_{cap}$.
    *   **Bank Run:** Type H agents (HODLers) exit en masse.

**Verdict:** **Fail.** The system has no mechanism to halt a reflexive death spiral once the "Flippening" ($M_{cap} < \text{Liabilities}$) occurs.

---

## 5. Sensitivity Analysis (Toffalini Matrix)

| Variable | Critical Threshold | Source Theory |
| :--- | :--- | :--- |
| **Curve Imbalance** | > 65% UST | **Briola (Clustering)** |
| **Oracle Latency** | > 15s | **Toffalini (Arb)** |
| **BasePool Spread** | Low (Prop 1164) | **Control Theory ($G$)** |

## 6. Conclusion
Applying the **RiskDAO** and **Briola** frameworks reveals that Terra's stability was an artifact of "Fair Weather" conditions.
*   **Theoretical Failure:** The design lacked a "Circuit Breaker" for $G > 1$ scenarios.
*   **Empirical Failure:** Governance (Prop 1164) actively removed the only friction (Spread) that could have dampened the spiral.
