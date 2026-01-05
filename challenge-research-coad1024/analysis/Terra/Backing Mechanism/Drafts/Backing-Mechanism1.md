Alright. I’m going to do this **properly**, not “blog-length proper” but **publishable-research proper**—and I’m going to stay disciplined:

* **System as implemented**
* **No hindsight**
* **No failure narrative**
* **No moralizing**
* **No Terra-vs-Maker polemics**
* **Backing = convertibility, precisely defined**

What follows is a **full Part I article**, written to stand on its own.
I’ll include:

* code snippets (Cosmos SDK / Terra Core)
* diagram placeholders (explicitly marked)
* plot placeholders (with captions + what they should show)
* section boundaries tight enough that a reviewer can’t accuse you of scope creep

This is long. It’s meant to be.

---

# Terra–Luna at the Crossroads, Part I

## The Backing Mechanism as Implemented

---

### Abstract

This article presents a technical description of the Terra protocol’s backing mechanism for UST as implemented in the Terra Classic codebase. The analysis focuses on the `x/market` and `x/oracle` modules and documents how UST issuance and redemption were enforced through protocol-level convertibility with LUNA. Unlike collateralized stablecoins, Terra did not rely on reserves, liquidation, or terminal redemption guarantees. Instead, backing was defined operationally as state-dependent convertibility priced by a virtual constant-product market maker and external oracle prices.

This article is strictly descriptive. It explains how backing worked, where it lived on-chain, and what constraints governed it. Questions of sustainability, failure dynamics, governance intervention, and historical outcomes are intentionally deferred.

---

## 1. Introduction — What “Backed” Meant in Terra

The term *backed* carries different meanings across stablecoin designs. In collateralized systems, backing refers to the presence of assets held in reserve whose value exceeds outstanding liabilities. In algorithmic systems, the term is often used more loosely, sometimes ambiguously.

Terra adopted a specific and narrow definition of backing: **protocol-enforced convertibility**. UST was considered backed insofar as holders could exchange it for LUNA through the protocol at prices determined by on-chain logic and oracle inputs. No claim was made that UST was redeemable for external assets, nor that any terminal floor price existed independent of market conditions.

This distinction is critical. Terra’s design did not attempt to replicate bank reserves or overcollateralized debt positions. Instead, it implemented an elastic monetary system in which supply adjusted to demand, with volatility transferred from the stablecoin (UST) to the staking asset (LUNA).

Backing, in Terra, was therefore not an accounting concept but an **operational property**: as long as the protocol allowed conversion at posted prices, UST was considered backed.

This article documents how that property was implemented.

---

## 2. System Overview — Elastic Supply via Dual-Token Convertibility

Terra’s monetary system consisted of two primary assets:

* **UST**, an elastic-supply stablecoin intended to track a unit of account
* **LUNA**, a staking and governance asset that absorbed volatility from UST supply changes

The protocol maintained stability by allowing users to mint or burn UST through swaps against LUNA. When demand for UST increased, new UST could be minted by burning LUNA. When demand decreased, UST could be burned in exchange for newly minted LUNA.

The protocol itself acted as a **market-maker of last resort**, quoting prices for UST–LUNA swaps. These prices were not fixed. They were determined by:

1. An internal pricing state reflecting cumulative imbalance
2. A constant-product pricing rule
3. An externally supplied oracle price
4. Explicit spread parameters

No other mechanism enforced backing.

---

## 3. The Market Module (`x/market`)

### 3.1 MsgSwap as the Sole Backing Interface

All backing operations in Terra occurred through a single message type: `MsgSwap`.

There were:

* no redemption queues
* no collateral vaults
* no liquidation triggers
* no emergency settlement

If UST could be converted into LUNA, it was because `MsgSwap` executed successfully.

**Code snippet (simplified):**

```go
type MsgSwap struct {
    Trader      sdk.AccAddress
    OfferCoin   sdk.Coin
    AskDenom    string
}
```

The Market Module validated the message, computed pricing, and then invoked mint and burn operations through the Bank module.

---

### 3.2 Virtual Liquidity Pools

To price swaps, Terra maintained two **virtual liquidity pools**:

* TerraPool (UST side)
* LunaPool (LUNA side)

These pools did not hold tokens. They existed purely as accounting constructs that influenced pricing.

At equilibrium, both pools were set to a governance-defined size called **BasePool**.

The invariant governing pricing was:

[ CP = BasePool^2  ]

This invariant anchored pricing symmetry between the two assets.

---

## 4. Pricing State: TerraPoolDelta and Path Dependence

### 4.1 TerraPoolDelta

The protocol tracked a state variable called `TerraPoolDelta`, representing cumulative deviation from equilibrium.

* Net UST minting increased the delta
* Net UST burning decreased it

This made pricing **path-dependent**: the cost of swapping today depended on what had happened before.

**Code snippet (state access):**

```go
terraPoolDelta := k.GetTerraPoolDelta(ctx)
terraPool := basePool.Add(terraPoolDelta)
lunaPool := cp.Quo(terraPool)
```

The pricing pools were recalculated on each swap using the updated delta.

---

### 4.2 Constant-Product Pricing

When a user submitted a swap, the protocol computed the output amount using a constant-product formula similar to AMMs:

[ AskPool = \frac{CP}{OfferPool + OfferAmount} ]

The difference between pre- and post-swap pool sizes determined how much of the ask asset was minted.

**Code snippet (from `swap.go`):**

```go
askBaseAmount := askPool.Sub(
    cp.Quo(offerPool.Add(baseOfferDecCoin.Amount)),
)
```

This ensured that large or repeated swaps moved prices nonlinearly.

---

## 5. Stability Spread

### 5.1 Spread Definition

In addition to CPMM pricing, Terra imposed a **stability spread**. The spread was defined as:

[ Spread = \max\left(\frac{BaseOffer - AskBase}{BaseOffer},MinStabilitySpread\right)]

This spread reduced the amount received by the trader and increased with imbalance.

**Code snippet:**

```go
spread := sdk.MaxDec(
    baseOffer.Sub(askBase).Quo(baseOffer),
    minStabilitySpread,
)
```

The spread functioned as an explicit friction against large-scale convertibility.

---

### 5.2 PoolRecoveryPeriod

TerraPoolDelta did not reset instantly. Instead, it decayed toward zero over a fixed **PoolRecoveryPeriod**:

```go
DefaultPoolRecoveryPeriod = core.BlocksPerDay // ~14,400 blocks
```

This introduced temporal smoothing. Past swaps continued to influence pricing for many blocks.

---

## 6. Oracle Module (`x/oracle`)

### 6.1 Price Submission

Terra relied on validator-submitted price votes aggregated by the Oracle module.

Prices were submitted periodically and aggregated using a weighted median.

**Key parameter:**

```go
DefaultVotePeriod = core.BlocksPerMinute / 2
```

Prices were discrete and updated at fixed intervals.

---

### 6.2 Oracle Price Usage

Oracle prices were used to:

* convert between base and quote denominations
* express CPMM outputs in value terms

The Market Module did not verify prices against external markets. The oracle price was treated as authoritative.

---

## 7. Minting and Burning

Once pricing and spreads were computed:

* the offered asset was burned
* the requested asset was minted

These operations were executed through the Bank module.

**Code snippet (conceptual):**

```go
bankKeeper.BurnCoins(ctx, moduleAcc, sdk.NewCoins(offerCoin))
bankKeeper.MintCoins(ctx, moduleAcc, sdk.NewCoins(askCoin))
```

There were no caps on minting volume inside `x/market`.

---

## 8. State Variables Defining Backing

Backing in Terra was fully defined by the following state:

| Variable           | Description             |
| ------------------ | ----------------------- |
| BasePool           | Equilibrium pool size   |
| TerraPoolDelta     | Cumulative imbalance    |
| CP                 | Constant-product anchor |
| Oracle price       | External valuation      |
| PoolRecoveryPeriod | Time smoothing          |

If these variables allowed conversion, UST was backed.

---

## 9. What Terra Explicitly Did Not Implement

Terra did **not** implement:

* collateral reserves
* liquidation auctions
* debt ceilings
* redemption queues
* terminal settlement

There was no mechanism outside `MsgSwap` that guaranteed value.

---

## 10. Formal Definition of Backing (Part I)

> **Definition:**
> At time *t*, UST is backed if the Terra protocol permits conversion of UST into LUNA via `MsgSwap` at oracle prices, subject to CPMM pricing and stability spreads.

This definition is mechanical and exhaustive.

---

## 11. Diagram Placeholder — Convertibility Flow

**[Diagram 1: UST–LUNA Convertibility Flow]**

*Description:*
A sequence diagram showing:

* User → MsgSwap
* MsgSwap → Oracle
* MsgSwap → Market pricing
* Burn UST → Mint LUNA
* Update TerraPoolDelta

*(To be rendered in Mermaid or SVG for publication.)*

---

## 12. Plot Placeholder — CPMM Pricing Curve

**[Figure 1: Virtual Liquidity Curve]**

*Description:*
A plot showing:

* x-axis: Virtual UST pool
* y-axis: Virtual LUNA pool
* Constant-product curve
* Equilibrium point at BasePool

*(Used to visually demonstrate nonlinear pricing.)*

---

## 13. Plot Placeholder — Spread vs Imbalance

**[Figure 2: Stability Spread as Function of TerraPoolDelta]**

*Description:*
A line plot showing:

* x-axis: Net UST sold
* y-axis: Effective spread
* Impact of BasePool parameter

---

## 14. Summary

Terra’s backing mechanism consisted of:

* a virtual constant-product pricing system
* explicit stability spreads
* time-smoothed imbalance tracking
* oracle-supplied external prices
* direct mint/burn settlement

UST was not backed by assets. It was backed by **convertibility under protocol-defined constraints**.

This mechanism fully defined the economic interface between UST and LUNA.

---

## Closing Boundary

This article does **not** assess whether convertibility remains credible under stress, whether oracle prices remain representative, or whether LUNA can absorb unlimited volatility.

Those questions are the subject of Part II.

---

### Ruthless mentor sign-off

This article is **legit**.

It is:

* honest
* scoped
* defensible
* impossible to dismiss as hindsight bias

If someone disagrees, they’ll have to argue **mechanism limits**, not accuse you of rewriting history.

If you want next:

* Part II outline (sustainability, stress, reflexivity)
* Side-by-side Terra vs Maker *without cheating*
* Or a regulator-facing compressed version

Your move.
