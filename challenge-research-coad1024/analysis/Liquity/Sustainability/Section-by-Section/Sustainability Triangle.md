# The Sustainability Triangle: Systemic Resilience

**Goal**: Analyze the interacting feedback loops that determine whether the protocol stabilizes or collapses under stress. This framework is adapted from the "Trinity of Stability" model.

---

## 1. The Model: Three Pillars of Stability

A stablecoin system is only as strong as its weakest link. We evaluate Liquity V2 across three interconnected pillars.

**Visual Reference**:
![The Sustainability Triangle](../Diagrams/Sustainability%20Triangle/sustainability_triangle_diagram.png)
*Figure 1: The Sustainability Triangle. Vertices: Collateral Quality (Asset), Incentive Mechanics (Behavior), Governance/Backstop (Resolution).*

---

## 2. Pillar I: Collateral Quality (The Asset Layer)

This pillar assesses the "Hardness" of the backing assets.

### A. Asset Composition
Liquity V2 introduces multi-collateral support (WETH, wstETH, rETH).
*   **Correlation Risk**: High. All assets are effectively "Long ETH".
*   **Liquidity Profile**: Deep. ETH and LSTs have the deepest liquidity on Ethereum.

### B. The "LST Loop" Risk
*   **Mechanism**: Users borrowing BOLD against wstETH to buy more wstETH (Looping).
*   **Risk**: In a de-pegging event (stETH < ETH), these positions become insolvent faster than the Oracle can update.
*   **Mitigation**: Higher MCR (Minimum Collateral Ratio) for LSTs compared to WETH.

---

## 3. Pillar II: Incentive Mechanisms (The Behavioral Layer)

This pillar assesses whether the protocol pays enough to incentivize defense.

### A. Keeper Economics
Keepers are the "Garbage Collectors" of the system. They liquidate bad debt.
*   **Profit Equation**: $\text{Profit} = (\text{Collateral Seized} - \text{Debt Repaid}) - \text{Gas Cost}$.
*   **The "Gas Spike" Threat**: If Ethereum Gas > 500 gwei, small liquidations become unprofitable.
*   **V2 Solution**: Dynamic gas compensation (prepaid by borrower).

**Visual Reference**:
![Keeper Breakeven Plot](../Diagrams/Sustainability%20Triangle/keeper_breakeven_plot.png)
*Figure 2: Profitability threshold for Keepers at varying Gas Prices. The "Death Zone" indicates where bad debt accumulates because liquidations are unprofitable.*

### B. Redemption Arbitrage
*   **Mechanism**: If BOLD < $1.00, arbitrageurs buy BOLD and redeem it for $1.00 of ETH.
*   **Effectiveness**: This is a "Hard Peg" mechanism. It forces the price back to $1.00 but relies on arbitrageurs having capital efficiency.

---

## 4. Pillar III: Governance & Backstop (The Resolution Layer)

When the algorithm fails, how is the system rescued?

### A. Immutable "Governance"
Liquity V2 is largely immutable.
*   **Pros**: No "Human Error" risk. No bad votes.
*   **Cons**: No "Emergency Brake". If a bug or economic exploit is found, the protocol cannot pause.

### B. The Equity Backstop (Dilution)
*   **Mechanism**: If the Stability Pool is empty, debt is **Redistributed** to other borrowers.
*   **The "Death Spiral" Risk**: Redistribution lowers the collateral ratio of healthy borrowers. If this causes *them* to be liquidated, a cascade begins.

**Visual Reference**:
![Redistribution Cascade Diagram](../Diagrams/Sustainability%20Triangle/redistribution_cascade.png)
*Figure 3: System dynamics during a Redistribution event. Showing the flow of Bad Debt from insolvent Troves to healthy Troves.*

---

## 5. Synthesis: The Weakest Link

| Pillar | Rating | Justification |
| :--- | :--- | :--- |
| **Collateral** | A- | ETH/LSTs are pristine, but highly correlated. |
| **Incentives** | B+ | Strong hard mechanisms, but reliant on active Keepers/Arbs. |
| **Governance** | N/A | Immutability is a double-edged sword. High security, low adaptability. |

**Conclusion**: The system's primary fragility lies in **Pillar II (Incentives)** during periods of extreme L1 congestion, where the "Hard Peg" mechanics might become too expensive to execute.
