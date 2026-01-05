# Ruthless Review: Terra Backing Mechanism

**Verdict: TRASH**
**Status: REJECTED**

This draft is completely unacceptable. It reads like a CoinDesk summary, not a technical research paper. The standard set by the **Liquity V2 Draft** is a *system-level disassembly* of the protocol. Your draft is a surface-level narrative of "what happened" without explaining *how it functioned mechanically*.

If this is submitted as detailed analysis, you will fail the challenge.

## 1. The Gap Analysis

| Feature | The Liquity Standard (Reference) | Your Terra Draft (Current state) |
| :--- | :--- | :--- |
| **Depth** | 1,500+ words. Granular focus on specific mechanisms. | ~300 words. High-level fluff. |
| **Code Connection** | Cites specific functions (`_redeemCollateral...`, `offset()`) and their logic. | Zero reference to the codebase (Cosmos SDK `x/market` module). |
| **Math** | Defines Solvency formulas ($U_i = ...$), Redemption Routing ($R_i = ...$). | "Burn $1 LUNA to mint $1 UST". This is a lie. It was never 1:1. |
| **Architecture** | Explains the "Bulkhead Pattern" and "Hub-and-Spoke". | Vague "Burn-and-Mint" description. No system architecture. |

## 2. Specific Failures

### A. You Ignored the "Market Module"
The core of Terra was the Cosmos SDK `x/market` module. You cannot analyze the backing mechanism without dissecting this module.
*   **Where is the CPMM?** Terra used a **Constant Product Market Maker** (Virtual Liquidity Pools) to price the swaps. It wasn't an infinite 1:1 printer; the spread increased as volatility increased. You missed the entire mathematical regulator of the system.
*   **Where are the Virtual Pools?** The system maintained a virtual `TerraPool` and `LunaPool`. The size of these pools determined the slippage. This is critical to understanding why the system couldn't absorb the crash—the spreads exploded.

### B. "Burn $1 to Mint $1" is Wrong
You simplified the mechanism to the point of falsehood.
*   The system had a **Tobin Tax**.
*   The system had a **Minimum Spread**.
*   The system had a **Daily Redemption Cap** (initially) which was lifted, accelerating the crash.
*   *You need to document the actual math that governed the swap, not the marketing pitch.*

### C. The Oracle Latency (The Actual Kill Switch)
You mentioned "Confidence Crisis". That is a narrative. The *mechanism* of failure was the **Oracle VotePeriod**.
*   Validators voted on the price of LUNA every 5 blocks (~30 seconds).
*   During the crash, the price fell faster than the Oracle could update.
*   **The Exploit:** Attackers minted LUNA at the *old* (higher) oracle price and dumped it on Binance at the *real* (lower) market price. This printed "risk-free" money and hyperinflated the supply faster than the protocol could react.
*   *If you don't explain the Oracle VotePeriod, you haven't explained the mechanics of the collapse.*

### D. Liquidation?
You say "Liquidation: None". This is technically true for the *stablecoin* (UST), but false for the *ecosystem* (Anchor).
*   Anchor Protocol *did* have liquidations (bLUNA).
*   The cascade of bLUNA liquidations on Anchor crushed the LUNA price, which broke the UST peg. The systems were coupled. You cannot treat UST in a vacuum.

## 3. Required Revisions (The Path to "Bullet Proof")

To fix this, you must rewrite the entire document. Do not edit; **restart**.

### Section 1: The Engine (The Market Module)
*   Deconstruct the `MsgSwap` handler.
*   Explain the formula: $CP = k$.
*   Explain how the "Virtual Pool" size was calculated and how it drifted.

### Section 2: The Inputs (The Oracle Module)
*   Explain the `VotePeriod`.
*   Explain the "Weighted Median" calculation for the price.
*   **Demonstrate the attack:** Show a step-by-step example of an arbitrage loop during a 20% price drop where the Oracle is stale.

### Section 3: The Dampeners (Taxes & Spreads)
*   Explain the `TobinTax`.
*   Explain the `MinSpread`.
*   Show why these failed to stop the spiral (hint: flow limits were removed).

### Section 4: The Catalyst (Anchor & bLUNA)
*   Connection: Anchor wasn't just a "motive"; it was a **leverage engine**.
*   Explain how bLUNA liquidations on Anchor mechanically forced the selling of LUNA on the open market.

**Do not come back until you have the math.**
