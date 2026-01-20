# Pricing Algorithm for Stablecoins

This document outlines the valuation methodology and the numerical algorithm used to price the **Class A Stablecoin**, as described in the research paper *Designing Stablecoins*.

## 1. The Mathematical Problem

The core challenge in pricing the Class A coin is that its future cash flows depend on **path-dependent resets**.

- The coin behaves like a bond with a coupon rate $R$.
- **Regular Payouts** occur every $T$ days.
- **Upward Resets** occur if the Class B value becomes too high (leverage decreases).
- **Downward Resets** occur if the Class B value becomes too low (protection buffer thins).

When any of these events occur, the system "resets": payments are made, and the coin's state is effectively re-initialized (often mapping back to $t=0$). This creates a **recursive** valuation structure where the value at the current time depends on the value at the "reset" time (which is conceptually $t=0$).

### 1.1 State Variables

We model the price $W_A(t, S)$ as a function of two state variables:

1. $t$: The **time elapsed** since the last reset or payout ($0 \le t \le T$).
2. $S$: The **relative price** of the underlying ETH ($S_t = \frac{P_t}{\beta_t P_0}$).

### 1.2 The Pricing Equation (PDE)

Between resets, the value $W_A(t, S)$ follows the standard Black-Scholes partial differential equation (since the underlying ETH follows a Geometric Brownian Motion).

$$
\frac{\partial W_A}{\partial t} + rS \frac{\partial W_A}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 W_A}{\partial S^2} - r W_A = 0
$$

Where:

- $r$ is the risk-free interest rate.
- $\sigma$ is the volatility of ETH.
- The domain is $0 \le t < T$ and $H_d(t) < S < H_u(t)$.

### 1.3 The Boundaries

The domain of $S$ is time-dependent, bounded by the reset conditions:

1. **Lower Barrier (Downward Reset)**:
    $$ H_d(t) = \frac{1}{2}(H_d^{param} + 1 + Rt) $$
    If $S$ hits this level, Class A is partially liquidated.

2. **Upper Barrier (Upward Reset)**:
    $$ H_u(t) = \frac{1}{2}(H_u^{param} + 1 + Rt) $$
    If $S$ hits this level, Class A receives accrued coupons and resets.

---

## 2. The Algorithm

Since the boundary conditions depend on the solution itself (specifically $W_A(0, \cdot)$), we cannot solve this in a single backward pass like a standard option. We must use an **Iterative Fixed-Point Algorithm**.

### The Iterative Procedure (Algorithm 1)

**Goal:** Find the function $W_A(t, S)$ such that propagating it forward (or solving backward) returns the *same* initial function.

**Step 1: Initialization**

- Make an initial guess for the value function at time $t=0$. A simple guess is the face value.
  $$ W_A^{(0)}(0, S) = 1 $$
- Set iteration counter $k = 1$.

**Step 2: Solve the PDE (The Iteration Step)**
Given the solution from the previous step, $W_A^{(k-1)}(0, S)$, we define the **boundary values** for the current step $k$:

1. **Terminal Condition (at $t=T$):**
    At the regular payout time $T$, the holder gets the coupon $RT$ plus a "new" coin. The relative price $S$ drops by $RT/2$.
    $$ W_A^{(k)}(T, S) = RT + W_A^{(k-1)}\left(0, S - \frac{RT}{2}\right) $$

2. **Upper Boundary Condition (at $S = H_u(t)$):**
    On upward reset, the holder gets accrued coupon $Rt$ plus a reset coin (value at $t=0, S=1$).
    $$ W_A^{(k)}(t, H_u(t)) = Rt + W_A^{(k-1)}(0, 1) $$

3. **Lower Boundary Condition (at $S = H_d(t)$):**
    On downward reset, the holder gets accrued coupon $Rt$, plus a partial principal payback based on the leverage buffer.
    $$ W_A^{(k)}(t, H_d(t)) = Rt + (1 - H_d^{param}) + H_d^{param} \cdot W_A^{(k-1)}(0, 1) $$

With these boundaries fixed (using the known values from step $k-1$), **solve the PDE** backwards from $t=T$ to $t=0$ to find the new surface $W_A^{(k)}(t, S)$.

**Step 3: Check Convergence**

- Compare the new solution at $t=0$ with the previous guess:
  $$ \text{Error} = \sup_S | W_A^{(k)}(0, S) - W_A^{(k-1)}(0, S) | $$
- If the error is smaller than a tolerance (e.g., $10^{-4}$), **Stop**. The converged result is the fair price.
- If not, set $W_A^{(k-1)} = W_A^{(k)}$ and repeat Step 2.

## 3. Intuition

Imagine you satisfy the "steady state" of the coin.

- You assume the coin is worth $X$ dollars today.
- You fast-forward to all possible future scenarios (Payout, Reset Up, Reset Down).
- In each scenario, you receive some cash + a "fresh" coin.
- You value that "fresh" coin using your assumption $X$.
- You discount all those future payoffs back to today.
- If the result is exactly $X$, your assumption was correct. If not, you adjust your assumption and try again.

This mathematical guarantee (Theorem 3.2 in the paper) ensures that this logic converges to a unique, fair price.

## 4. Relationship to Bonding Curves

A frequent question is whether this system can be treated as a **Bonding Curve**.

**Short Answer: No, but it can be adapted into one.**

### 4.1 Fundamental Differences

1. **Issuance vs. Trading**:
    - **Bonding Curves (e.g., Uniswap):** The contract acts as a market maker, quoting a buy/sell price for the token at all times. The contract *is* the liquidity.
    - **This System (Class A/B):** The contract only handles **Splitting** (Deposit ETH $\to$ Get A+B) and **Merging** (Redeem A+B $\to$ Get ETH). It does *not* offer a price for just Class A. You must find a counterparty for that.

2. **Accounting NAV vs. Market Price**:
    - The contract calculates a deterministic **Net Asset Value (NAV)** (e.g., $1 + Rt$) for internal accounting.
    - It uses this NAV **only** to trigger Resets. It will **never** buy or sell the coin at this NAV.
    - The *market price* is floating and determined by the PDE algorithm above.

### 4.2 How to Adapt it into a Bonding Curve

To make this user experience feel like a bonding curve (where a user can just "buy Class A" from a contract), you would need to build a **Wrapper AMM**:

1. **The Wrapper**: A smart contract that holds Class B inventory.
2. **The Pricing Oracle**: The AMM uses the solution to the **Periodic PDE** (calculated off-chain or via a simplified on-chain approximation) as its target price.
3. **The Flow**:
    - User sends ETH to Wrapper.
    - Wrapper interacts with the Core Contract to split ETH into A + B.
    - Wrapper keeps B (or sells it elsewhere).
    - Wrapper sends A to the user at the calculated **PDE Market Price**.

In this setup, the **PDE Algorithm** acts as the bonding curve function.

## 5. Why do we need this algorithm? (vs. Smart Contract Price)

A common confusion is: *"If the Smart Contract defines the price (NAV), why do we need a complex PDE to calculate a 'Market Price'?"*

### 5.1 The Smart Contract Price is NOT the Trading Price

The smart contract calculates a **Net Asset Value (NAV)** using a simple formula:
$$ \text{NAV}_t = 1 + R \times t $$
This NAV is used **only** for internal logic (to decide *when* to trigger a reset). The contract does **not** guarantee liquidity at this price. You cannot walk up to the contract at any time $t$ and swap your coin for $\text{NAV}_t$ in ETH.

### 5.2 The Market Price reflects Risk

If you want to sell your coin **before** a reset happens, you must sell it to another trader in the open market. That trader will not pay the exact NAV. They will discount the price based on risk:

1. **Risk of Loss**: There is a chance ETH crashes tomorrow, triggering a **Downward Reset**. In that scenario, the holder might only get $\$0.90$ back instead of the expected $\$1.00$.
2. **Time Value**: The coupon is only paid *at the end* of the period.

**The Pricing Algorithm** calculates what a rational trader should accept as a fair price today, accounting for the probability of all future crashes (downward resets) and payouts (upward resets).

### 5.3 Why "Periodic"? (The Loop)

The unique feature of this stablecoin is that it **Resets**.

- When a reset happens (e.g., Upward Reset), the contract clears the slate.
- The coin arguably becomes "brand new" again (time $t$ resets to $0$, price ratio $S$ resets to $1$).

This creates a logic loop:
> *"To know what the coin is worth **today**, I need to know what it will be worth **immediately after the next reset**. But immediately after the next reset, it will be identical to the coin I have **today**!"*

We use a **Periodic PDE** to solve this "chicken and egg" problem. We mathematically force the value at the *end* of the cycle to match the value at the *start* of the cycle.

## 6. Does this logic hold for other Stablecoins?

**Yes.** The distinction between **Target Price** (or Net Asset Value) and **Market Price** exists in almost every stablecoin, though the mechanisms differ.

### 6.1 The General Rule

For *any* stablecoin, the "Peg" (e.g., $1.00) is just a **Target**. The **Market Price** is whatever traders are willing to pay on an exchange (e.g., Binance, Uniswap).

| Stablecoin Type | "Relative/Book Price" (Target) | Why Market Price Deviates | Mechanism to Align Prices |
| :--- | :--- | :--- | :--- |
| **Fiat-Backed** (USDC, USDT) | **$1.00** (Reserves) | **Liquidity & Trust**: If fear rises that the bank account is empty, price drops to $0.98. | Arbitrageurs buy at $0.98, redeem for \$1.00 (from issuer). |
| **CDP** (DAI) | **$1.00** (Target) | **Supply/Demand**: If everyone wants DAI to buy ETH, price goes to \$1.01. | Arbitrageurs mint DAI at \~$1.00 and sell at \$1.01. |
| **Liquity** (LUSD) | **$1.00** (Face Value) | **Redemption Zones**: Price floats freely between $\approx \$0.995$ and $\$1.10$. | Hard mechanism (redemption) only kicks in at boundaries. Market price floats in between. |
| **This Periodic Design** | **$1 + Rt$** (NAV) | **Time to Reset**: You are "locked" until the next reset/payout. | The price reflects the *yield* you will earn while waiting. |

### 6.2 Key Difference: Fighting vs. Embracing Deviation

- **Most Stablecoins (DAI, USDC)**: Try to **minimize** the deviation. They want Market Price $\approx$ Target Price *always*.

- **This Design**: **Accepts** the deviation. It behaves more like a **Bond** than a spot **Currency**.
  - A zero-coupon bond with face value $\$100$ might trade at $\$98$ today.
  - That $\$2$ gap isn't a "broken peg"; it's the **interest rate** (time value of money).
  - Similarly, this stablecoin's price deviation is mathematically compensated by the coupon $R$. The PDE calculates exactly what that deviation *should* be.

## 7. Architecture Components (from Section 2 of the Paper)

The research paper describes the architecture in terms of **Core** and **Supplementary** components.

### 7.1 Core Components (Minimal Viable Product)

These components are required for the basic functioning of the Class A (Stable) and Class B (Leveraged) coins.

1. **The Dual-Class Structure**:
    - **Class A (Stablecoin)**: A fixed-income instrument acting like a bond. It has a principal guarantee (protected by resets) and receives periodic coupons.
    - **Class B (Leveraged Coin)**: A speculative instrument that acts like a leveraged position (initial leverage $\approx 2x$). It absorbs the volatility of the underlying asset.

2. **The Custodian Smart Contract**:
    - Holds the underlying asset (ETH).
    - Manages the **Split** (locking ETH to mint A+B) and **Merge** (burning A+B to unlock ETH).
    - Maintains the state variables: $\beta_t$ (conversion factor) and $v_t$ (time since last reset).

3. **Payment Events (The Reset Mechanism)**:
    - **Regular Payout**: Occurs every $T$ days. Pays accrued coupons to Class A.
    - **Upward Reset**: Triggered when Class B value rises to $H_u$ (high leverage profit). Resets leverage to initial state (2x) and distributes profits.
    - **Downward Reset**: Triggered when Class B value drops to $H_d$ (low buffer). Partially liquidates Class A to preserve capital and resets leverage to 2x.

### 7.2 Supplementary Components (Extensions)

These components extend the system for greater stability or market incentives.

1. **Further Splitting (Tranching)**:
    - **Class A' (Money Market Coin)**: Created by splitting Class A. It is even safer than Class A, designed to be ultra-stable (like a money market account).
    - **Class B'**: The subordinated tranche of Class A.

2. **Subsidy Mechanism (Optional)**:
    - A modification where Class A holders pay a portion of their coupon to Class B holders.
    - **Purpose**: To incentivize demand for Class B (leverage seekers) during low-volatility periods, ensuring the system remains balanced.

3. **Pricing/Valuation Oracle**:
    - The **Periodic PDE Pricing Algorithm** (described in this document) is necessary for secondary market participants to fairly value the coins, even though the smart contract itself does not use it.

### 7.3 Infrastructure Components (Required for Real-World Implementation)

While the paper focuses on the theoretical design, a real-world deployment on Ethereum would require these additional infrastructure components:

1. **The On-Chain Oracle (Price Feed)**:
    - The smart contract needs the real-time price of ETH ($P_t$) to calculate $V_B$ and determine if a reset is triggered.
    - **Distinction**: This is different from the *PDE Pricing Oracle*. The Contract needs the *spot price of ETH*. The Market needs the *fair price of Class A*.

2. **Keeper Network (Automation Bots)**:
    - The paper states resets are "triggered automatically." On Ethereum, smart contracts cannot self-execute.
    - **Component**: A network of external bots ("Keepers") that monitor the state and call the `triggerReset()` function when conditions are met, likely incentivized by a small bounty or arbitrage opportunity.

3. **Secondary Market Liquidity (The Exchange)**:
    - The core contract only allows minting/redeeming in pairs ($A+B$).
    - **Component**: An external exchange (Uniswap Pool or Order Book) is **critical** for users who only want to buy Class A (Stablecoin) without holding Class B. This is where the *Pricing Algorithm* becomes useful.

4. **Governance Module (Optional but likely)**:
    - Who sets the Coupon Rate $R$? Who sets the Reset Thresholds $H_u, H_d$?
    - In a static deployment, these are immutable. In a dynamic system, a Governance Contract (DAO) would be a component to adjust these parameters in response to market conditions.
    At the regular payout time $T$, the holder gets the coupon $R\cdotT$ plus a "new" coin. The relative price $S$ drops by $RT/2$.
