# The Oracle Front-Running Attack (Forensic Analysis)

> [!NOTE]
> This content was extracted from Part I. It belongs in the Sustainability/Failure analysis (Part II) as it describes *how the mechanism failed*, not just how it was built.

### The Mismatch
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
