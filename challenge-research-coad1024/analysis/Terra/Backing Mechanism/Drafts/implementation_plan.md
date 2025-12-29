# Implementation Plan - Rewrite Terra Backing Mechanism Analysis

## Goal Description
Rewrite `Article_Backing_Mechanism.md` to a high-technical standard, comparable to the Liquity V2 drafts. The content must be grounded in the Cosmos SDK code found in `terra-classic-core`. The narrative shifts from a historical summary to a **mechanical disassembly** of the protocol's failure.

## User Review Required
> [!IMPORTANT]
> **Mechanics vs History**: This rewrite focuses strictly on the *mechanism design* (CPMM, Oracle Latency, Virtual Pools). It will not cover the "social" history (Do Kwon's tweets, etc.) unless relevant to parameter changes.

## Proposed Changes

### [Analysis/Terra]

#### [MODIFY] [Article_Backing_Mechanism.md](file:///home/hash/Projects/Research Challenge/challenge-research-coad1024/analysis/Terra/Backing Mechanism/Article_Backing_Mechanism.md)

**New Structure:**

**1. Introduction: The Algorithmic Central Bank**
*   Define Terra not as a stablecoin but as an "Elastic Supply Protocol" governed by the `x/market` module.
*   Core thesis: "Volatility Absorption" via the LUNA market cap.

**2. The Market Module (`x/market`)**
*   **The Swap Mechanism**: NOT a 1:1 printer.
*   **The Virtual Pool Model**:
    *   Explain the **Constant Product Market Maker (CPMM)** logic found in `keeper/swap.go`.
    *   Formula: $CP = BasePool^2$.
    *   Formula: $\text{AskPool} = CP / \text{OfferPool}$.
*   **The Spread (Slippage)**:
    *   Explain how the protocol charged a spread to dampen volatility.
    *   Formula: $\text{Spread} = \max(\text{CPMM\_Spread}, \text{MinStabilitySpread})$.
    *   Cite `DefaultMinStabilitySpread` (Initial: 2%, later changed).

**3. The Price Feeder (`x/oracle`)**
*   **The VotePeriod**: Explain the 5-block (30s) delay logic found in `x/oracle/types/params.go`.
*   **Weighted Median**: How validators agreed on price.
*   **The Attack Vector**: "Front-running the Oracle."
    *   Step-by-step math of how an arbitrageur could mint LUNA at price $100 (Oracle) when real price was $80, instantly profiting and dumping.

**4. The Flow Control (Dampeners)**
*   **Tobin Tax**: Explain the fee on Terra<>Terra swaps (e.g. UST<>KRT).
*   **PoolRecoveryPeriod**: How the virtual pools reset ($14,400$ blocks).
*   **The Fatal Flaw**: Explain how Governance eventually *removed* the caps (Proposal 1164) to allow faster exits, effectively removing the "Bulkheads" and allowing the flood.

**5. Systemic Failure: The Death Spiral Mechanics**
*   **The Anchor Catalyst**: High leverage (bLUNA) + Liquidation Cascade.
*   **The Reflexivity Loop**:
    1.  UST De-pegs.
    2.  Arb burns UST -> Mints LUNA.
    3.  LUNA Supply Expands (Hyperinflation).
    4.  LUNA Price Drops (Dilution + Selling).
    5.  Oracle Latency Exploited (Printing extra LUNA).
    6.  Market Cap $\text{LUNA} < \text{Market Cap UST}$ (Insolvency).

## Verification Plan
*   **Manual Verification**:
    *   Verify all formulas against `terra-classic-core/x/market/keeper/swap.go`.
    *   Verify param defaults against `x/oracle/types/params.go`.
    *   Ensure the tone matches the ruthless, clinical style of the Liquity documents.
