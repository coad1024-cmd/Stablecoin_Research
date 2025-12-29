# Terra Analysis: Sustainability and the Anchor Protocol

## 1. Introduction
The sustainability of the Terra ecosystem was inextricably linked to the Anchor Protocol. Marketed as a "savings protocol" offering a stable ~20% APY, Anchor became the primary demand sink for UST. This report analyzes the economic model of Anchor, the misalignment between its revenue and obligations, and the inevitable depletion of its yield reserve that precipitated the collapse.

## 2. The Anchor Business Model
Anchor operated as a money market on the Terra blockchain.
*   **Depositors**: Users deposited UST to earn a stable yield (Target: 19.5% - 20.5%).
*   **Borrowers**: Users bonded assets (bLUNA, bETH) to borrow UST.
*   **Yield Source**: The yield paid to depositors was sourced from:
    1.  Interest paid by borrowers.
    2.  Staking rewards from the bonded collateral (e.g., LUNA staking rewards).

### A. The Yield Gap
For the system to be sustainable, the income from interest and staking rewards must equal or exceed the interest paid to depositors.
$$ \text{Income} = (\text{Total Borrowed} \times \text{Borrow Rate}) + (\text{Total Collateral} \times \text{Staking Yield}) $$
$$ \text{Expense} = \text{Total Deposits} \times \text{Anchor Rate (20\%)} $$

In practice, during the bull market, demand for leverage was high, but not high enough to cover the massive influx of deposits chasing the 20% risk-free rate.

## 3. The Yield Reserve: A Finite Runway
To maintain the fixed 20% rate during periods where Income < Expense, Anchor utilized a "Yield Reserve" (a pool of UST).
*   **Surplus**: When Income > Expense, excess UST flowed into the reserve.
*   **Deficit**: When Expense > Income, UST was drawn from the reserve to pay depositors.

By early 2022, the disparity between deposits (approx. $14B) and borrowings (approx. $3B) was extreme. The protocol was bleeding millions of dollars daily from the Yield Reserve.

### A. The LFG Bailout
In February 2022, the Yield Reserve neared depletion. The Luna Foundation Guard (LFG) intervened with a $450M injection to recapitalize the reserve. This act, while extending the runway, signaled that the protocol was not organiclly sustainable and relied on external subsidization—a classic characteristic of a Ponzi-like structure when dependent on new capital inflows (via LUNA sales) to pay existing yield.

## 4. Sensitivity Analysis: The "Unwind" Problem
The sustainability crisis wasn't just about running out of money; it was about the *behavioral* response to a rate cut.
*   **Scenario**: If the Yield Reserve emptied, the Anchor Rate would drop to the "natural" rate (estimated at ~4-5% or lower).
*   **Reaction**: Capital flight. As the rate dropped, "mercenary capital" would exit UST to find yield elsewhere.
*   **Impact on Peg**: Massive selling of UST for other stablecoins or LUNA would stress the LUNA mint/burn mechanism. The system required LUNA liquidity to absorb these exits.

## 5. Conclusion: Subsidized Stability
Terra's sustainability was an illusion financed by the appreciation of LUNA. The high Anchor rate served as a marketing expense to bootstrap network effects (Metcalfe's Law). However, by failing to dynamically adjust the rate downwards as deposits grew, the protocol created a liability it could not honor. The collapse was not just a technical failure of the peg, but a fundamental insolvency of the central bank (Anchor) governing the currency.
