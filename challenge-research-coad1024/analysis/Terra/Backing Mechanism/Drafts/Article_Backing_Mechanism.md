# Terra Analysis: The Backing Mechanism

> **Technical Disassembly**
> This document analyzes the mechanism design of the Terra protocol (classic-core), specifically the `x/market` and `x/oracle` modules. It rejects the simplified "Burn-and-Mint" narrative in favor of a rigorous examination of the **Constant Product Market Maker (CPMM)** logic and **Oracle Latency** vectors that mathematically guaranteed the system's collapse.

## 1. Introduction — The Elastic Supply Protocol

Terra was not a collateralized stablecoin. It was an **Elastic Supply Protocol** designed to absorb volatility through a dual-token system. The core thesis was that a sovereign economy needs a currency with elastic supply (UST) rather than fixed supply (Bitcoin) or external dependency (USDC).

To achieve this, the protocol established an algorithmic central bank: the **Market Module** (`x/market`). This module did not simply swap tokens 1:1. It operated a virtualized order book that priced liquidity based on system stress. The fatal flaw was not the concept of elasticity, but the specific parameterization of the **Feedback Control Loop** that failed to dampen oscillation during the May 2022 bank run.

---

## 2. The Engine: The Market Module (`x/market`)

The heart of the Terra backing mechanism was the `MsgSwap` handler. Contrary to popular belief, the protocol did not offer an infinite peg. It offered a swap facility priced by a **Virtual Liquidity Pool**.

### 2.1 The Virtual Liquidity Pool (CPMM)

The protocol maintained two virtual pools: `TerraPool` (UST) and `LunaPool` (LUNA). These pools did not hold actual tokens (funds were burned/minted), but their *virtual sizes* determined the exchange rate spread.

The mechanism used the **Constant Product** formula ($xy = k$) synonymous with Uniswap, but applied virtually to minting/burning:

$$CP = \text{BasePool}^2$$

Where `BasePool` was a governance parameter (initially set to `1,000,000 SDR` units).

When a user wanted to swap UST for LUNA (contraction), the system calculated the Ask Amount (LUNA) based on the deviation from this constant product:

$$\text{AskPool} = \frac{CP}{\text{OfferPool} + \text{OfferAmount}}$$

**Code Reference: `x/market/keeper/swap.go`**
```go
// constant-product, which by construction is square of base(equilibrium) pool
cp := basePool.Mul(basePool)
terraPoolDelta := k.GetTerraPoolDelta(ctx)
terraPool := basePool.Add(terraPoolDelta)
lunaPool := cp.Quo(terraPool)

// Get cp(constant-product) based swap amount
askBaseAmount := askPool.Sub(cp.Quo(offerPool.Add(baseOfferDecCoin.Amount)))
```

### 2.2 The Price of Stability: Spreads and Slippage

To discourage panic selling, the protocol imposed a **Stability Spread**. The spread was designed to widen as the deviation from the equilibrium (`BasePool`) increased.

The spread formula was:

$$\text{Spread} = \max\left(\frac{\text{BaseOffer} - \text{AskBase}}{\text{BaseOffer}}, \text{MinStabilitySpread}\right)$$

*   **MinStabilitySpread**: Hardcoded dampener (initially 2%, or 0.5% at various times).
*   **Effect**: As more people sold UST for LUNA, the `TerraPool` would swell (increasing `delta`), causing the `LunaPool` to shrink. This increased the slippage for subsequent sellers, theoretically halting a bank run by making exits prohibitively expensive.

**The Mechanical Failure:**
During the crash, the `BasePool` recovery period (`PoolRecoveryPeriod = 14,400 blocks` or ~24 hours) was too slow to reset the spread. However, the fatal error was **Proposal 1164**, which explicitly increased the `BasePool` size to reduce spreads, removing the system's only brake in a misguided attempt to "restore liquidity."

---

## 3. The Signal: The Oracle Module (`x/oracle`)

A decentralized central bank requires a price feed. Terra relied on a weighted median of validator votes. This introduced a critical latency termed the **Oracle VotePeriod**.

### 3.1 The VotePeriod Latency

Validators submitted exchange rate votes every **5 blocks** (~30 seconds).

**Code Reference: `x/oracle/types/params.go`**
```go
const (
    DefaultVotePeriod = core.BlocksPerMinute / 2 // 30 seconds
)
```

In normal markets, a 30-second delay is negligible. In a hyper-volatility event (Death Spiral), it is fatal.

### 3.2 The Oracle Front-Running Attack

The mismatch between the **On-Chain Oracle Price** and the **Off-Chain Market Price** created a risk-free arbitrage loop that accelerated the collapse.

**The Loop:**
1.  **Spot Market Crash**: LUNA drops from $80 to $60 on Binance in 10 seconds.
2.  **Oracle Lag**: The protocol still quotes LUNA at $80 for the remaining 20 seconds of the VotePeriod.
3.  **The Attack**: Arbitrageurs buy LUNA on Binance for $60.
4.  **The Mint**: They burn LUNA for UST on-chain. The protocol credits them $80 worth of UST (valuing LUNA at the stale price).
5.  **The Profit**: They sell the UST for USD.
    *   Cost: $60.
    *   Revenue: $80 (minus spreads).
    *   **Profit: $20 risk-free.**

This arbitrage did not stabilize the peg; it **printed uncovered liabilities**. The protocol issued UST backed by LUNA that the market knew was worthless, purely because the Oracle was too slow to mark it down.

---

## 4. Flow Control and Failure

### 4.1 Tobin Tax and Recovery Periods
The protocol included a **Tobin Tax** (default 0.25%) for non-volatility swaps (e.g., UST -> KRT). This was irrelevant during the crash.

The meaningful parameter was `PoolRecoveryPeriod`. The virtual pools were designed to "cool down" and reset to equilibrium over 24 hours.
```go
DefaultPoolRecoveryPeriod = core.BlocksPerDay // 14,400
```
This meant the system was designed to handle *impulses* of volatility, not sustained unidirectional flow.

### 4.2 Removing the Bulkheads (Prop 1164)
The ultimate undoing was the manual intervention by governance. As the peg faltered, the Terraform Labs team observed that the **Spread** (Limit 2) was capping minting capacity to ~$290M/day.

To "allow arbitrageurs to save the peg," they passed **Prop 1164**:
*   **BasePool**: Increased from 50M to 100M SDR.
*   **Effect**: This effectively lowered the slope of the CPMM curve.

**Result**: It opened the floodgates. Instead of a slow bleed, the "bulkheads" were removed, allowing billions of UST to be burned for LUNA instantly. This hyperinflated LUNA supply from 350M to 6.5Trillion in roughly 72 hours.

---

## 5. Systemic Failure: The Death Spiral Mechanics

The interaction of these modules created a deterministic path to zero.

### 5.1 The Reflexivity Trap
Terra's backing was endogenous.
$$\text{Solvency} = \frac{\text{MarketCap(LUNA)}}{\text{Supply(UST)}}$$
As long as $\text{Solvency} > 1$, the system works.
The moment $\text{Solvency} < 1$, the system is mathematically broken (Bank Run).

### 5.2 The Anchor Catalyst
Anchor Protocol acted as a **Leverage Engine**. By incentivizing UST locking (20% APY), it ballooned the UST supply to ~$18B, while the LUNA market cap was ~$30B.
When the "Run" started:
1.  Liquidity drained from Anchor (UST sold).
2.  UST de-pegged.
3.  The CPMM Spread failed to halt the flow (due to Prop 1164).
4.  The Oracle Lag allowed arbitrageurs to loot the remaining value.
5.  LUNA supply went vertical (Hyperinflation).
6.  LUNA price went to zero.

**Conclusion:**
Terra did not fail because of "FUD." It failed because its **Feedback Control System (`x/market`)** was manually disabled (Prop 1164) and its **Sensor Network (`x/oracle`)** was too slow to track the crash. It was a failure of control theory, implemented in code.
