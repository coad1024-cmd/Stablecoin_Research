# Liquity at the Crossroads: Where LUSD's Solvency Lives On-Chain

## Front Matter

**Title:** Liquity at the Crossroads: Where LUSD's Solvency Lives On-Chain
**Subtitle:** A deep dive into Liquity's "purist" architecture—from its immutable accounting to its unique "hard peg" mechanisms and the mathematical invariants that define its solvency.
**Target Audience:** Senior Solidity devs, protocol engineers, DeFi risk teams.

---

### Introduction: The "Purist" Approach to Backing

While MakerDAO evolved into a "hybrid" central bank managing a diversified portfolio of crypto and Real World Assets (RWAs), Liquity took the opposite path: **hyper-specialization**. It is a protocol designed to do one thing perfectly—issue interest-free loans against Ether—and then stop changing.

**The three pillars of Liquity's backing:**

1. **Immutable Accounting:** No governance can change the rules. The contract logic is set in stone.
2. **Hard Peg via Redemption:** A direct arbitrage mechanism that forces the peg without relying on centralized PSMs.
3. **Collective Solvency:** A two-step liquidation mechanism (Stability Pool + Redistribution) that socializes risk instantaneously rather than relying on slow auctions.

**What this article answers:**

* Where does the backing actually live? (The `ActivePool` and `DefaultPool` architecture).
* How is it verified? (The `TroveManager` accounting).
* What happens when the system breaks? (Recovery Mode and the 150% TCR threshold).

---

### 1. The Core Accounting Layer: ActivePool vs. DefaultPool

**What this section establishes:** The foundational data structures that make LUSD's backing verifiable on-chain.

#### 1.1 The Dual-Pool Architecture

Unlike Maker's single `Vat` ledger, Liquity splits its solvency state into two distinct contracts to handle the lifecycle of debt.

* **`ActivePool`**: The "healthy" state. It holds the total ETH collateral and tracks the total LUSD debt of all *active* Troves.
  * *Invariant:* `ActivePool.ETH` = Sum of all active Troves' collateral.
* **`DefaultPool`**: The "purgatory" state. It holds the collateral and debt of *liquidated* Troves that are pending redistribution.
  * *Purpose:* When a Trove is liquidated and not fully absorbed by the Stability Pool, its assets move here before being pushed to other borrowers.

#### 1.2 State Variables: The Source of Truth

The `TroveManager` contract is the ultimate ledger for individual positions.

**Core Struct: `Trove`**

```solidity
struct Trove {
    uint debt;  // Amount of LUSD borrowed
    uint coll;  // Amount of ETH locked
    uint stake; // Used for redistribution logic
    enum Status { nonExistent, active, closedByOwner, closedByLiquidation, closedByRedemption }
}
```

**The Fundamental Invariant:**
For the system to be solvent, the following must hold globally:

```
(ActivePool.ETH + DefaultPool.ETH) * Price > (ActivePool.LUSD + DefaultPool.LUSD)
```

Specifically, the Total Collateral Ratio (TCR) must ideally stay above 150% to avoid Recovery Mode.

---

### 2. Collateral Entry: The Trove Mechanism

**What this section shows:** How value enters the system and creates LUSD.

#### 2.1 Opening a Trove

Users interact with the `BorrowerOperations` contract, which acts as the interface layer (similar to Maker's `Join` adapters).

**Workflow:**

1. **User sends ETH**: Calls `openTrove` with ETH value.
2. **Accounting Update**:
    * `ActivePool` receives ETH.
    * `TroveManager` updates user's `coll` and `debt`.
    * `LUSDToken` mints coins to the user's address.
3. **Fee**: A one-time *Borrowing Fee* (0.5% - 5%) is added to the debt. This is distinct from Maker's continuous stability fee.

**Design Lesson:**
> **Why no interest?** Continuous interest requires continuous state updates (or lazy evaluation). By charging a one-time fee, Liquity simplifies the accounting logic, making the contracts more gas-efficient and predictable—a requirement for immutability.

---

### 3. Price Discovery: The Dual-Oracle Safety Net

**What this section establishes:** How the system knows the value of `ActivePool.ETH`.

#### 3.1 Chainlink + Tellor

Liquity employs a "safety-first" oracle architecture in the `PriceFeed` contract.

* **Primary**: Chainlink. Updates on 0.5% deviation or 3-hour heartbeat.
* **Fallback**: Tellor. A decentralized, miner-based oracle.

#### 3.2 The Logic of Distrust

The system actively monitors Chainlink for failure states:

1. **Frozen**: No update for >4 hours.
2. **Broken**: Response is 0, invalid timestamp, or >50% deviation from previous price *without* Tellor confirming.

**Switching Logic:**
If Chainlink is deemed "broken," the system automatically switches to Tellor. It only switches back when both oracles are live and within 5% of each other. This prevents "oracle poisoning" attacks where a single feed is manipulated to trigger false liquidations.

---

### 4. Collateral Exit: Stability Pool & Redistribution

**What this section shows:** The unique two-step mechanism that replaces Dutch auctions.

#### 4.1 The Stability Pool (The Shock Absorber)

Instead of searching for buyers *after* a liquidation (like Maker's auctions), Liquity lines up buyers *beforehand*.

* **Mechanism**: Users deposit LUSD into the Stability Pool.
* **Liquidation**: When a Trove is liquidated, the required LUSD is *burned* from the pool to repay the debt. The Trove's ETH is transferred to the pool depositors.
* **Benefit**: Instant settlement. No auction latency. No reliance on market liquidity during a crash.

**Mathematical Formula:**
For a depositor $i$ with share $D_i$ of total pool $D_{total}$:

* Debt Absorbed: $L_{debt} \times \frac{D_i}{D_{total}}$
* ETH Gained: $E_{coll} \times \frac{D_i}{D_{total}}$

#### 4.2 Redistribution (The Systemic Backstop)

If the Stability Pool is empty, the system falls back to **Redistribution**. The debt and collateral of the liquidated Trove are distributed among *all active Troves*.

* **Logic**: If you hold a Trove, you are effectively insuring the system.
* **Impact**: Your debt increases, but your collateral increases by a larger value (since liquidated Troves have >100% CR). You experience a net gain in equity, but a decrease in CR.

---

### 5. The Hard Peg: Redemption Mechanism

**What this section reveals:** Why LUSD trades closer to $1 than other decentralized stablecoins.

#### 5.1 Direct Arbitrage

Unlike Maker's PSM which relies on a centralized asset (USDC), Liquity creates a hard price floor using its own collateral.

* **The Promise**: Any LUSD holder can redeem 1 LUSD for $1 worth of ETH (minus redemption fee).
* **The Mechanism**: The protocol takes the LUSD, burns it, and *confiscates* the equivalent amount of ETH from the riskiest Trove (lowest CR).
* **The Result**: LUSD cannot trade significantly below $1, because arbitrageurs will buy it for $0.98 and redeem it for $1.00 of ETH.

**Design Lesson:**
> **Solvency vs. User Experience:** Redemption is harsh for the borrower (they lose their ETH exposure), but it is absolute for the peg. It prioritizes the *money* (LUSD) over the *borrower*.

---

### 6. Terminal Defense: Recovery Mode

**What this section proves:** The system's defense against "Black Swan" events.

#### 6.1 The 150% Threshold

If the Total Collateral Ratio (TCR) falls below 150%, the system enters **Recovery Mode**.

* **Rule Change**: Troves with CR < 150% can now be liquidated.
* **Goal**: Rapidly deleverage the system to restore the 150% buffer.
* **Borrower Defense**: To be safe in Recovery Mode, you must maintain >150% CR.

**Comparison to Maker:**
Maker relies on governance to adjust risk parameters during a crisis. Liquity relies on a pre-programmed algorithmic response. It is ruthless but predictable.

---

### 7. Conclusion: The Solvency Verdict

Liquity represents a distinct philosophy in DeFi backing: **Resilience through Simplicity**.

* **MakerDAO** achieves stability through **diversification** (RWA, USDC) and **active management**. It is a hedge fund.
* **Liquity** achieves stability through **mechanism design** (Stability Pool, Redemption) and **immutability**. It is a protocol.

The backing of LUSD is not just the ETH in the `ActivePool`; it is the game-theoretic assurance that the Stability Pool will absorb shocks, and the Redemption mechanism will enforce the floor, all without a single governance vote.
