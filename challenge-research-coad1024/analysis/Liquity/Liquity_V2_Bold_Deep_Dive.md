# Liquity V2 (Bold): The Adaptive Hard Peg

## Front Matter

**Title:** Liquity V2 (Bold): The Adaptive Hard Peg
**Subtitle:** How Liquity evolved from a rigid, single-collateral protocol to a multi-collateral, market-driven system without sacrificing immutability.
**Target Audience:** DeFi architects, mechanism designers, risk analysts.

---

### Introduction: From "Purist" to "Adaptive"

Liquity V1 (LUSD) was a masterpiece of **rigid minimalism**. It accepted only ETH, charged a one-time fee, and had no governance. It was designed to be "finished" upon deployment.

Liquity V2 (Bold) represents a paradigm shift. It retains the core philosophy of **immutability** (no governance voting on parameters) but introduces **adaptability** through market mechanisms. Instead of hard-coding values, it lets the market set them.

**The Core Evolution:**

* **V1**: One-time fee (0.5-5%) set by algorithm.
* **V2**: Continuous interest rate set by **users**.

This change transforms Liquity from a static utility into a dynamic marketplace for borrowing.

---

### 1. Multi-Collateral Architecture: The Branch Model

V1 was a monolith. V2 is a federation.

#### 1.1 The Collateral Registry

At the top level sits the `CollateralRegistry`. It does not hold funds; it acts as the router.

* **Function**: Maps collateral tokens (WETH, rETH, wstETH) to their respective `TroveManager` addresses.
* **Routing**: Directs BOLD redemptions to the appropriate branch based on system health (see Section 3).

#### 1.2 Isolated Branches

Each collateral type lives in its own "Branch". A Branch is a self-contained replica of the Liquity system:

* **Components**: Own `TroveManager`, `ActivePool`, `DefaultPool`, and `StabilityPool`.
* **Isolation**: Bad debt in the rETH branch does not directly drain the WETH branch's Stability Pool.
* **Unified Liability**: All branches mint the *same* BOLD token. This concentrates liquidity while segregating collateral risk.

**Design Lesson:**
> **Risk Segmentation**: By isolating Stability Pools, V2 ensures that LST de-pegs (e.g., stETH de-pegging from ETH) only damage the specific branch's depositors, not the entire protocol.

---

### 2. The Interest Rate Market: User-Set Rates

The most radical change in V2 is the removal of the algorithmic one-time fee.

#### 2.1 The Mechanism

When opening a Trove, the borrower **chooses their own interest rate**.

* **Range**: `[INTEREST_RATE_MIN, INTEREST_RATE_MAX]`
* **Incentive**: Why pay more? **Redemption Protection.**

#### 2.2 SortedTroves by Rate

In V1, Troves were sorted by Collateral Ratio (CR). Riskiest Troves (lowest CR) were redeemed first.
In V2, Troves are sorted by **Interest Rate**.

* **Lowest Rate**: First in line for redemption (highest risk of losing exposure).
* **Highest Rate**: Last in line (protected).

**The Game Theory:**
Borrowers effectively bid for "protection" from redemption.

* **Bear Market / Peg < $1**: Arbitrageurs redeem BOLD. Borrowers raise rates to avoid being hit.
* **Bull Market / Peg > $1**: No redemptions. Borrowers lower rates to minimize costs.

This creates a **market-clearing price** for BOLD borrowing that naturally adjusts to supply and demand, without a governance committee setting the "Base Rate".

#### 2.3 Batch Management

To avoid gas-intensive micro-management, V2 introduces **Interest Batch Managers**.

* Users delegate rate management to a Batch Manager.
* The Manager updates the rate for thousands of Troves in a single transaction.
* This enables "managed vaults" similar to Yearn, but purely for interest rate optimization.

---

### 3. Redemption 2.0: "Unbackedness" Routing

With multiple collateral types, which one should be redeemed?

#### 3.1 The "Unbackedness" Metric

The system aims to redeem from the branch that is most "unbacked" by its Stability Pool.

* **Metric**: `Outside Debt = Total Branch Debt - BOLD in Branch Stability Pool`
* **Logic**: If a branch has little BOLD in its SP, it is fragile. Redemptions should target it to reduce its debt load.

#### 3.2 Routing Algorithm

A redemption of `X` BOLD is split across branches proportional to their Outside Debt.
$$Redeem_i = X \times \frac{OutsideDebt_i}{\sum OutsideDebt}$$

This ensures that redemptions purely improve the systemic health of the protocol, balancing the risk load across branches.

#### 3.3 Zombie Troves

In V1, a redemption that left a Trove with dust debt would close it.
In V2, because Troves are sorted by *rate* (not CR), a redemption might hit a high-CR Trove. Closing it would be unfair and potentially lower the branch's TCR.

**Solution**: The Trove remains open but is tagged as a **Zombie**.

* **Status**: `debt < MIN_DEBT`.
* **Restrictions**: Cannot be redeemed further. Must be topped up or closed by owner.
* **Purpose**: Prevents "dust clogging" attacks where an attacker creates thousands of tiny Troves to grief redeemers.

---

### 4. Safety Upgrades

#### 4.1 Removal of Recovery Mode

V1 had a global "Recovery Mode" when TCR < 150%.
V2 removes this binary mode. Instead, it relies on:

1. **Branch-Specific MCR**: Each LST can have a different Minimum Collateral Ratio.
2. **Critical Collateral Ratio (CCR)**: Borrowing is restricted below this level, but existing Troves aren't liquidated solely for being below CCR (unlike V1 Recovery Mode).

#### 4.2 Collateral Branch Shutdown

A new nuclear option for catastrophic failure (e.g., Oracle failure or LST collapse).

* **Trigger**: Oracle failure or extreme price drop.
* **Effect**:
  * Borrowing freezes.
  * **Urgent Redemptions** enabled: 0% fee, 1% collateral bonus.
  * Goal: Empty the branch of debt as fast as possible.

---

### 5. Comparison Matrix: V1 vs V2

| Feature | Liquity V1 (LUSD) | Liquity V2 (Bold) |
| :--- | :--- | :--- |
| **Collateral** | ETH only | WETH, rETH, wstETH (Isolated Branches) |
| **Cost** | One-time Fee (0.5-5%) | Continuous Interest (User-set) |
| **Redemption Priority** | Lowest CR (Riskiest) | Lowest Interest Rate (Cheapest) |
| **Governance** | None (Immutable) | None (Immutable + Market Driven) |
| **Peg Mechanism** | Hard Peg via Redemption | Hard Peg via Redemption + Interest Rate Demand |
| **Safety Net** | Recovery Mode (150% TCR) | Branch Shutdown + CCR Restrictions |

---

### Conclusion

Liquity V2 proves that **immutability does not mean stagnation**. By replacing hard-coded parameters (like the base rate algorithm) with market-driven mechanisms (user-set interest rates), Bold creates a protocol that can adapt to any market condition without requiring a DAO vote. It is the "System Engineering" answer to the "Governance" problem.
