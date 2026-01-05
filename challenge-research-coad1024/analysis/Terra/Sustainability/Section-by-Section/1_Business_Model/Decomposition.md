# 1. Business Model Decomposition

## Overview
Terra operated as an **Algorithmic Central Bank** with a dual-mandate:
1.  **Monetary Policy**: Maintain price stability of UST (Liability) via LUNA (Asset/Equity) dilution.
2.  **Fiscal Policy**: Subsidize demand via the Anchor Protocol (Yield Reserve).

Unlike a commercial bank where Liabilities (Deposits) are backed by Assets (Loans/Treasuries), Terra's Liabilities were backed by the **endogenous equity value** of the network itself.

---

## 2. Balance Sheet Analysis

### Liabilities (The Obligations)
*   **UST Supply**: At peak ~$18.7B.
*   **Nature**: Demand liabilities. Convertible on-demand for $\$1.00$ worth of LUNA.
*   **Duration**: Instant (0-duration).

### Assets (The Backing)
*   **LUNA Market Cap**: At peak ~$40B.
*   **Nature**: Volatile crypto-asset. 100% correlation to protocol health.
*   **Liquidity**: Limited by CEX order books (Binance, KuCoin).
*   **Exogenous Reserves**: ~$3B BTC (LFG) added late-stage.
    *   *Critical Flaw*: Reserves were <20% of liabilities.

### Revenue (The Income)
*   **Seigniorage**: When UST demand grew, LUNA was burned. This reduced LUNA supply, mechanically increasing LUNA price (assuming constant mc). This was "booked" as value accrual to LUNA holders.
*   **Swap Fees**: Tobin Tax (0.35%) and MinSpread (0.5%).
*   **Anchor Burrow Interest**: ~12% paid by borrowers on bLUNA/bETH.

### Costs (The Burn)
*   **Anchor Yield**: 19.5% paid to Depositors.
*   **Validators/Oracle Rewards**: Paid from Swap Fees.

---

## 3. The Structural Deficit (The "Ponzi" Element)

The core business model failure was the **Negative Carry** in Anchor.

$$ \text{Net Interest Margin (NIM)} = \text{Yield}_{\text{Assets}} - \text{Cost}_{\text{Liabilities}} $$

*   **Yield on Assets**: ~12% (Borrow interest from ~3B loans).
*   **Cost of Liabilities**: ~20% (Yield paid to ~14B deposits).

**The Gap**:
$$ \text{Deficit} \approx \$14B \times (20\% - 12\%) \approx \$1.1B / \text{year} $$

This deficit was funded not by organic revenue, but by **External Injection** (LFG Reserves) and **LUNA Sales**. The protocol was effectively selling its own equity (LUNA) to pay dividends (Anchor Yield) to attract creditors (UST holders).
