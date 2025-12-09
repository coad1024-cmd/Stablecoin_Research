# Sustainability Triangle (MakerDAO)

**Goal**: Analyze the three coupled feedback loops that define MakerDAO's systemic resilience.

**Diagram**: The Sustainability Triangle
![Triangle Radar](../Diagrams/Sustainability%20Triangle/sustainability_triangle_diagram.png)

---

## Loop 1: Collateral Quality (The Anchor)

* **Composition**: Hybrid (Crypto + RWA).
* **Strength**: High diversification. US Treasuries do not crash when ETH crashes.
* **Weakness**: **Censorship Risk**. A freeze on the USDC/RWA portion (Loop 1 failure) forces the system to rely entirely on Loop 3 (Governance) to switch collateral types or fork.

## Loop 2: Incentive Mechanics (The Engine)

* **Mechanism**: DSR (Demand side) and Stability Fees (Supply side).
* **Strength**: **Active DSR**. Maker can manually raise the DSR to 15% (as done previously) to defend the peg by soaking up supply.
* **Weakness**: **Keepers**. Relying on auction keepers for complex RWA liquidations is impossible. RWA liquidations are legal processes, not on-chain auctions. This breaks the automation of Loop 2.

**Diagram**: Keeper Profitability
![Keeper Breakeven](../Diagrams/Sustainability%20Triangle/keeper_breakeven_plot.png)

## Loop 3: Governance & Backstop (The Pilot)

* **Mechanism**: Active voting, Emergency Shutdown, Debt Auctions (MKR/SKY dilution).
* **Strength**: **Flexibility**. Governance can negotiate legal deals, hire trustees, and pivot strategy.
* **Weakness**: **Dependency**. MakerDAO *cannot* function without active governance. If governance is captured or deadlocked, the RWA portfolio cannot be managed.

---

## Synthesis: The Triangle Assessment

| Loop | Score | Assessment |
| :--- | :--- | :--- |
| **Collateral** | 3.5/5 | Stable but Centralized. |
| **Incentives** | 4.5/5 | Very strong monetary policy tools. |
| **Governance** | 2.0/5 | High friction, high capture risk. |

**Verdict**: MakerDAO trades **Governance Minimization** for **Economic Resilience**. It is a "Managed Economy" rather than an "Automated Protocol."
