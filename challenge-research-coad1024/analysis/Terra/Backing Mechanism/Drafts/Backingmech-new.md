
---
# The Terra–LUNA Backing Mechanism

### A Mechanical Description of the System as Implemented

## 1. What “Backing” Meant in Terra

Terra did not employ collateral in the conventional sense. There were no segregated reserves guaranteeing redemption of UST at par. Instead, Terra implemented a **convertibility-based backing mechanism** in which the stablecoin (UST) was backed by the **protocol’s ability to expand and contract supply through LUNA**, its native staking and governance token.

Backing, in Terra, therefore did **not** mean asset coverage. It meant **operational convertibility**: the protocol committed to exchanging 1 UST for 1 USD worth of LUNA (and vice versa) at oracle prices, subject to spread constraints. The credibility of UST rested on whether this conversion mechanism could clear demand under stress.

This section describes that mechanism exactly as it existed on-chain.

---

## 2. The Balance-Sheet Structure Implied by the Protocol

At any point in time, Terra’s economic structure can be summarized as:

* **Liabilities:** UST in circulation
* **Absorber / Equity:** LUNA market capitalization
* **Conversion Mechanism:** Mint–burn swaps via the Market module
* **External Assets:** None required for baseline operation

UST was a **zero-duration demand liability**. Holders could attempt to exit at any time by converting UST into LUNA through the protocol. There were no maturity constraints, lockups, or redemption queues enforced by default.

LUNA functioned as the **residual claimant**. When UST demand increased, LUNA supply contracted (burned). When UST demand fell, LUNA supply expanded (minted). This made LUNA the system’s loss-absorbing instrument.

Crucially, the absorber was **endogenous**: the value of LUNA depended on the health and scale of the Terra economy itself.

---

## 3. The Market Module (`x/market`): Convertibility as Backing

### 3.1 Virtual Liquidity Pools

UST–LUNA conversion did not occur at a fixed rate. Instead, Terra implemented a **virtual constant-product market maker (CPMM)**.

The protocol maintained two virtual pools:

* `TerraPool` (UST side)
* `LunaPool` (LUNA side)

These pools did not hold real assets. They were accounting variables used to compute **slippage and spread**. The invariant was defined as:

$$CP = \text{BasePool}^2$$


where `BasePool` was a governance-controlled parameter defining the equilibrium depth of the system.

At equilibrium:

$$\text{TerraPool} = \text{LunaPool} = \text{BasePool}$$


When UST was sold into the system (UST → LUNA), the TerraPool increased, forcing the LunaPool to shrink in order to preserve the constant product. This automatically worsened the exchange rate for subsequent sellers.

Backing, therefore, was not binary. It was **depth-dependent**.

---

### 3.2 Spread as the Primary Defense Mechanism

The system imposed a **stability spread** on swaps. The spread widened as the system moved away from equilibrium.

Mechanically:

* Small redemptions cleared near par
* Large redemptions incurred rapidly increasing slippage
* The goal was to make large exits progressively more expensive

This spread was the **only built-in brake** against a mass exit. There was no circuit breaker, no redemption cap per address, and no queueing mechanism beyond the CPMM curve.

The effectiveness of backing was therefore directly tied to:

* the chosen `BasePool`
* the recovery period of the virtual pools
* the willingness of market participants to accept LUNA under dilution

---

## 4. Oracle Dependence: Pricing the Backing Instrument

All conversions relied on prices supplied by the **Oracle module (`x/oracle`)**.

Validators submitted exchange-rate votes at fixed intervals (`VotePeriod`). The Market module always used the **last finalized oracle price**, not a live market feed.

This meant:

* UST–LUNA swaps were priced using **discrete, delayed data**
* The protocol assumed that oracle prices remained representative within each vote period

The backing mechanism therefore depended not only on market depth, but on **oracle latency**. Convertibility was defined at *yesterday’s* price, not the instantaneous one.

This is not a flaw by itself—it is simply a design choice with consequences.

---

## 5. The Role of LUNA Supply Elasticity

LUNA had **no hard supply cap**. Its supply expanded or contracted solely in response to UST demand.

From a mechanical perspective:

* UST contraction = LUNA issuance
* UST expansion = LUNA burn

This made LUNA functionally equivalent to **equity issuance during redemptions**. When UST holders exited, the system paid them by diluting LUNA holders.

Backing, therefore, was not a stock of assets but a **commitment to issue equity at the oracle price**.

---

## 6. Anchor’s Interaction with the Backing Mechanism

Anchor Protocol was not part of the Market module, but it materially affected backing by shaping **UST demand**.

Anchor offered a high, stable yield on UST deposits. This caused:

* sustained growth in UST supply
* a large fraction of UST becoming yield-motivated rather than transactional

From the perspective of backing:

* Anchor increased the size of liabilities
* without increasing absorber capacity exogenously
* while reinforcing expectations of stability

The backing mechanism itself did not distinguish between “organic” UST demand and “incentivized” demand. All UST was equally redeemable.

---

## 7. Exogenous Reserves: Not Part of the Core Mechanism

Bitcoin reserves accumulated by the Luna Foundation Guard were **not part of the protocol’s base backing logic**.

They:

* were not algorithmically integrated into redemption
* were not required for UST minting or burning
* were deployed discretionarily, off-chain or via ad-hoc interventions

As implemented, the Terra protocol remained fundamentally a **convertibility-backed system**, not a reserve-backed one. Exogenous reserves modified outcomes at the margin but did not redefine the mechanism.

---

## 8. What the Backing Mechanism Guaranteed—and What It Did Not

The Terra backing mechanism guaranteed:

* Continuous convertibility at oracle prices
* Slippage that increased with system stress
* Automatic loss absorption via LUNA dilution

It did **not** guarantee:

* Asset coverage of liabilities
* A minimum redemption value under extreme flow
* Independence between liabilities and absorber value
* Protection against oracle lag

UST was backed insofar as the system could **clear redemptions through dilution without destroying confidence in LUNA**.

That was the entire contract.

---

## 9. Summary: Backing as a Dynamic Constraint, Not a Reserve

Terra’s backing mechanism can be summarized precisely:

> UST was backed by the protocol’s ability to issue LUNA at oracle prices under a depth-dependent CPMM constraint.

This backing was:

* endogenous
* reflexive
* sensitive to flow, not stock
* governed by a small number of parameters (`BasePool`, spreads, oracle cadence)

Understanding Terra requires abandoning the idea that backing is a pile of assets. In Terra, backing was a **dynamic control system**, whose stability depended on whether dilution could remain credible under stress.

This section describes that system as it existed—nothing more, nothing less.

---

If you want, next we can:

* tighten this further into a **formal mechanism specification**
* add a **one-page mathematical abstraction**
* or integrate this cleanly with your sustainability framework without leaking hindsight

You’re very close to something genuinely solid.
