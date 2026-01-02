
# DAI at the Crossroads: How Maker’s Design Balances Code, Markets, and Governance

*Where Maker’s Solvency Lives On-Chain (and Where It Doesn’t)*

> A three part technical series unpacking Maker’s architecture — from its on-chain reserves to its evolving sustainability model and the governance layer that now defines its credibility.  
> *Target audience — senior Solidity devs, protocol engineers, DeFi risk teams.*

---

# Intro

DAI remains one of the largest dollar-pegged tokens in crypto that isn’t issued by a bank or a fintech.  
Its reserve lives entirely on-chain, enforced by collateral and arithmetic rather than balance-sheet trust. Yet over the past few years, that arithmetic has been bent — and then formalized — by pragmatism.  

What began as emergency patches after Black Thursday has evolved into a permanent blueprint: Maker’s **Endgame** plan.

Vaults gave way to the Peg Stability Module, ETH to USDC, and the once-pure crypto-collateral model to a hybrid of smart contracts, custodial reserves, and real-world assets. Endgame doesn’t hide this trade-off — it institutionalizes it, treating hybridization as the only scalable path to sustainability.  

The result is a protocol that’s still mathematically elegant but philosophically split — crypto-native in logic, hybrid in balance sheet.  
The invariants inside the Vat still guarantee solvency, yet the meaning of “backed” has drifted. Where it once meant over-collateralized ETH, it now includes treasuries, legal wrappers, and off-chain credit — each introducing latency and trust into a system designed to remove both.  

This series traces that evolution through three layers:  
**Backing** — how Maker’s on-chain balance sheet actually works.  
**Sustainability** — when deterministic math stops guaranteeing solvency.  
**Governance** — the coordination layer that ultimately holds the peg together.  

Rather than rely on narratives or governance rhetoric, each part focuses on the mechanics that decide whether DAI remains solvent, stable, and credibly neutral — by math, by market, and by mandate.

---

# Part 1 — How DAI Is Really Backed  

> Inside Maker’s on-chain balance sheet (and why “backed” is now layered)

Every DAI is created inside a vault and enforced by immutable accounting. That design gives Maker an unusually tight, auditable definition of backing: tokens exist only because collateral is locked and debt is recorded on-chain.  

But the meaning of that “backing” has changed. Post-Black-Thursday pragmatism — formalized in Endgame — has hybridized the reserve: smart-contract guarantees remain, but part of what counts as collateral now lives off-chain.  

Part 1 unpacks that hybrid: how on-chain accounting maps to economic assets, what remains trustless, and where off-chain realities introduce latency, legal risk, and concentration.

---

## Endgame and the Hybrid Reserve  

Maker’s Endgame is not a minor roadmap footnote — it’s the architecture that redefines what Maker means by backing.  

When you read the contracts now, you see the same **Vat**, **Join**, and **Cat** structures. When you read the balance sheet, you see new rows: tokenized treasuries, custodial USD rails, and real-world revenue streams. That change matters because it changes the operational assumptions we can reasonably make when markets break.  

Endgame turned Maker from a single-domain system — pure crypto in, DAI out — into a layered balance sheet.  
ETH, WBTC, and other volatile assets still make up the decentralized core, but they’re now surrounded by stability buffers like USDC, tokenized treasuries, and real-world-asset vaults.

![image](https://hackmd.io/_uploads/BklhKc8Agg.png)

That shift came from hard lessons. On Black Thursday, ETH crashed faster than the system could liquidate it, leaving a deficit. The response was pragmatic: if DAI can be backed partly by assets that don’t crash with crypto, then the peg survives shocks better. So Maker started blending in stable, low-volatility collateral.  

It worked — volatility risk dropped — but the trade-off was obvious: Maker gained a safer balance sheet and lost a bit of its permissionless purity.  

Today, part of the backing sits on-chain, trustless and programmable. The rest exists off-chain, wrapped in legal contracts and custodial trust. The smart contracts still enforce the accounting, but enforcing value for those off-chain assets requires lawyers and intermediaries, not keepers and liquidators.  

This is the quiet truth of Endgame: the Vat still adds up, but what it measures now includes assets that don’t live entirely in the EVM.  
Endgame didn’t rewrite Maker’s contracts — it rewrote what those contracts represent.  
“Backed” still means the books balance, but part of that balance now depends on people, institutions, and off-chain law.

---

## How DAI Is Really Backed  

A robust primary-market should, among other things, keep reserve ratios above a floor, avoid exploitable discontinuities in redemptions, and ensure reserve exhaustion happens slowly — a useful checklist formalized in P-AMM research and reinforced by stochastic models of non-custodial stablecoins. That checklist will be our lens through this article.  

DAI isn’t minted out of thin air — every unit originates inside a vault that locks collateral via a `Join adapter` and tracks debt through the `Vat`. Collateral moves into the system using adapter contracts (`Joins`), and price data comes through the `Spotter`, which pulls from the `OSM`. When a vault becomes unsafe, the `Cat` (liquidation module) coordinates the liquidation process and hands the position off to an auction contract (`Flipper`/`Clipper`), which Keepers compete to buy.  

```solidity
interface IVat {
  function frob(bytes32 ilk, address urn, address usr, int256 dink, int256 dart) external; // adjust ink/art
  function grab(bytes32 ilk, address urn, address usr, address guy, int256 dink, int256 dart) external; // liquidation move
  function move(address src, address dst, uint256 wad) external; // transfer DAI balance
}
````

The `Vat` is the single source of truth — it stores collateral balances, normalized debt, surplus, and system debt. Keeping `Vat` small and correct is crucial to guaranteeing on-chain backing.

![image](https://hackmd.io/_uploads/ByxlrBI0gx.png)
*The overall picture of how the key concepts of DAI are interconnected. Red circles represent actors; colored circles are the three types of tokens (DAI, MKR, collateral); white circles are variables; rectangles denote actions or events.*

---

# Canonical Invariants & the Assumptions Behind Them

Maker enforces solvency through math, not goodwill.
Every vault, collateral type, and global balance is governed by a small set of on-chain invariants — equations that must always hold true for the system to remain solvent. These arithmetic guarantees define what “backed” means on-chain, but they only translate to real stability while the economic environment behaves within certain bounds.

At the vault level, the Vat tracks a minimal state:

| Variable | Meaning                             | Example    |
| -------- | ----------------------------------- | ---------- |
| ink      | collateral locked                   | 10 ETH     |
| art      | normalized debt                     | 1000 units |
| rate     | cumulative stability-fee multiplier | 1.035      |
| mat      | liquidation ratio (per ilk)         | 150%       |

Debt isn’t stored directly — it’s computed as
`debt = art * rate`

This keeps gas costs low and makes debt accrual deterministic, but it also means solvency depends on arithmetic precision, oracle freshness, and timing.
If `ink * price` falls below `art * rate * mat`, the vault is unsafe and must be liquidated.

---

## From Arithmetic to Dynamics

Formally, the stable price of DAI can be viewed as a dynamic ratio between aggregate demand and system-wide leverage:

$$Z_t = \frac{D_t}{L_t}$$

where (Z_t) is the DAI price, (D_t) represents demand for DAI, and (L_t) measures how much collateral value supports that debt.

Maker’s on-chain invariant — `ink * price ≥ art * rate * mat` — is simply the deterministic, per-vault projection of this equation. It holds while leverage stays bounded and demand changes smoothly. Once leverage exceeds a critical threshold — effectively when (L_t > \beta^{-1}) for a given collateral ratio (\beta) — the system crosses into a deleverage spiral: collateral auctions amplify price swings instead of containing them.

In this regime, liquidation itself becomes reflexive. Even though each vault’s math still balances, aggregate leverage increases faster than collateral can clear, expected losses rise, and the stable-price domain collapses.

---

### The Core Arithmetic Guarantees — and What They Assume

For each collateral type (ilk), Maker enforces:

$$ink \times price \ge art \times rate \times mat$$

as long as oracles update on time and vault owners act before breaching.
When either assumption fails — delayed oracles, clustered liquidations — multiple vaults fall below their thresholds together, stressing keeper liquidity and auction throughput faster than equilibrium models anticipate.

At the system level:

$$\sum (art \times rate) = vat.debt$$

ensures that all DAI supply maps back to outstanding debt.
But the invariant doesn’t guarantee collectability: during stress, auctions can clear far below oracle values. The books remain arithmetically correct, but the system records a deficit (`woe`) as realized collateral falls short. Surplus fees (`joy`) offset this gap until `joy < woe`, at which point MKR dilution becomes the recapitalization path:

$$vow.joy - vow.woe \ge 0$$

---

### When Deterministic Guarantees Lose Economic Meaning

These relationships hold perfectly inside their stable domain — when collateral returns behave as sub-martingales, i.e. expected to rise or stay constant.
In that regime, the system remains solvent in expectation.
But once collateral returns turn super-martingale (expected to fall), even flawless liquidation logic can’t maintain a $1 redemption.
The Vat continues to balance; what disappears is the statistical foundation that gave those balances economic value.

Maker’s post-crisis adaptations — the Peg Stability Module and later real-world-asset onboarding — can be understood as boundary adjustments: they widen the stability region by introducing collateral with lower volatility and near-zero correlation to crypto markets.
This stabilizes (L_t) and re-anchors (Z_t) — effectively trading some decentralization for a larger safe operating zone.

---

## Why These Invariants Still Matter

These equations make Maker unique: solvency is enforced on-chain and updated continuously.
But they also reveal its boundary — deterministic arithmetic guarantees only hold inside a probabilistic envelope defined by collateral behavior and market speed. Understanding where that envelope ends is key to designing future stablecoins that remain solvent not just on paper, but in motion.

---

# Liquidation: Where Solvency Meets Execution

Liquidation is the enforcement layer that turns Maker’s arithmetic into market motion. It’s the point where on-chain math collides with off-chain liquidity — where solvency is proven not by equations, but by whether the network can respond in time.

When a vault’s collateralization ratio drops below its liquidation threshold, the system seizes its collateral and auctions it for DAI. In Solidity terms, this is the moment the invariant `ink * price = art * rate * mat` fails, and solvency must be restored by external bidders.

The `Dog` contract triggers liquidation, moving collateral into an auction module. The collateral to sell becomes the **lot**; the debt plus penalty becomes the **tab**.

---

## The Auction Layer

The early system used the `Flipper` contract — an English auction with two stages.
Keepers first competed to offer higher DAI for a fixed amount of collateral (*tend*), and once the tab was covered, to take less collateral for the same DAI (*dent*). Each bid required its own transaction, and throughput depended entirely on mempool health.

In 2021, `Clipper` replaced it: a Dutch hybrid that begins at a high price and decays until a keeper buys. It sacrifices price discovery for clearance certainty — auctions now fill deterministically, even under congestion.

Both models serve the same purpose: converting unsafe vault debt into DAI. The difference lies in how much latency and bandwidth they can tolerate.

---

## Solvency in Motion

Consider a vault with **10 ETH** against **12 000 DAI** of debt, a **150%** liquidation ratio, and a **13%** penalty.
When ETH drops below **$1 800**, the vault becomes unsafe. The lot is 10 ETH; the tab is 13 560 DAI.

A `Flipper` auction bids DAI upward until the tab is met, then bids down the collateral. A `Clipper` auction starts around 1 356 DAI/ETH and decays until keepers step in. In both cases, once enough DAI is raised, debt is burned and any excess collateral returned.

This logic works flawlessly while oracles are timely, keepers have liquidity, and blockspace is cheap. When any of these break, liquidation slows; when all fail together, it fails outright.

---

## Black Thursday: Solvency in the Mempool

On **March 12–13, 2020**, those assumptions collapsed. ETH fell nearly **45%** in eight hours; gas fees exploded above **200 gwei**. The Oracle Security Module’s one-hour delay became a blind spot. Hundreds of vaults breached thresholds simultaneously, spawning thousands of auctions.

Each `Flipper` bid was a separate transaction. Keepers ran out of gas, ETH, or time. Many auctions expired unfilled, with collateral selling for zero. By the end of the event, Maker carried an **≈ 8.3 million DAI deficit** — its first protocol-level shortfall.

> **Figure 2 — Auction activity and effectiveness during Black Thursday (Mar 12–13, 2020)**
> *Bars:* auctions triggered per hour
> *Line:* percentage reaching completion
> *Overlay:* ETH price collapse
> *Source:* Kjäer (2021)
> *Alt text:* “Spike in auctions and collapse in auction coverage during Black Thursday.”

The system’s arithmetic remained intact — but its execution layer froze. Solvency by math survived; solvency by throughput did not.

---

## Reflexivity Under Stress

As Klages-Mundt (2023) later modeled, this is the hallmark of a **deleverage spiral**: liquidation demand rises super-linearly as liquidity supply collapses. When auctions cluster in time, bids slow, and redemptions feed each other, the system enters a reflexive regime.

Even with >150% collateralization, Maker hit its absorption limit. The Vat’s arithmetic still held, but its link to market reality snapped. Solvency by math persisted — solvency by execution did not.

---

## Aftermath and Adaptation

The crisis led to a full redesign of Maker’s liquidation architecture. `Flipper` gave way to `Clipper`, ensuring deterministic clearance under congestion. Keeper incentives (`tip`, `chip`) were added, and the **Peg Stability Module (PSM)** introduced as a first-line buffer against redemption spikes.

Over time, real-world assets and stable collateral further insulated DAI’s peg from liquidation cascades. Liquidation remains Maker’s proof of solvency — the point where balance-sheet math meets market bandwidth — but it’s no longer the system’s only stabilizer.

---

## Where Backing Ends and Sustainability Begins

Liquidation closes the loop on DAI’s backing. It shows how solvency is enforced, not just computed. But it also marks the edge of what *backed* can guarantee. Beyond it lies a network of dependent systems — oracles, keepers, and gas markets — whose coordination determines whether DAI’s math holds under stress.

That dependency is the bridge to the next part of this series. Liquidation keeps DAI solvent in arithmetic space; **sustainability** asks whether that solvency can survive time, latency, and human coordination.

---

**References**

* Kjäer, M. (2021). *Quantitative Analysis of MakerDAO’s Liquidation System.*
* Klages-Mundt, A. (2023). *Novel Financial Technologies for Stablecoins, Market Stability, and Network Analysis.*

```
