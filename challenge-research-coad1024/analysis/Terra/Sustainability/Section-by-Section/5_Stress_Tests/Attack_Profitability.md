# The Economics of Attack: Profitability Analysis

This report quantifies the economic incentives for attacking the Terra protocol. By modeling the attack as a leveraged short position executed during a liquidity crisis, we demonstrate that the attack was not only "theoretically possible" but **highly rational** ($EV \gg 0$).

## 1. Parameters of the "Soros Trade"

The attack mirrors the 1992 George Soros trade against the Bank of England: overwhelm the central bank's limited reserves with leveraged selling pressure.

*   **Capital Deployed:** $500,000,000 (Seed Equity).
*   **Leverage:** 2.0x (Implied via Futures/Perps).
*   **Total Short Exposure:** $1,000,000,000.
    *   **UST Short:** $700M (Betting on De-peg).
    *   **LUNA Short:** $300M (Betting on Hyperinflation).
*   **Cost of Capital:** $4.6M (Interest calculated at 20% APR for 10 days).

## 2. Execution Trace

We simulated the trade execution using `calculate_attack_roi.py` assuming standard market conditions for borrowing and liquidity depletion.

### Phase 1: Deployment (Pre-Crash)
*   **Borrow:** 700M UST @ $1.00.
*   **Borrow:** 3.75M LUNA @ $80.00.
*   **Action:** Sell borrowed assets into the Curve Pool and Binance Order Book.
*   **Impact:** The $400M+ sell pressure breaks the Curve peg ($0.98), triggering the panic.

### Phase 2: Defense Exhaustion
*   LFG deploys $3B BTC reserves.
*   The attacker waits. The LFG reserves are finite; the short position is open-ended.
*   Once reserves are gone, LUNA hyperinflates to defend the peg.

### Phase 3: Exit (The Bottom)
*   **UST Exit:** Repurchased at $0.05 (95% drop).
*   **LUNA Exit:** Repurchased at $0.0001 (99% drop).

## 3. Financial Results

| Metric | Value |
| :--- | :--- |
| **Total Revenue (UST Leg)** | **$ 665,000,000** |
| **Total Revenue (LUNA Leg)** | **$ 300,000,000** |
| **Financing Cost** | **$ (4,657,534)** |
| **Net Profit** | **$ 960,342,465** |
| **ROI** | **192%** |

## 4. Verdict: The asymmetric Bet

The trade offered an asymmetric payoff profile:
*   **Downside (Peg Holds):** Loss of interest + spread (~$10M).
*   **Upside (Peg Breaks):** ~$1 Billion Profit.
*   **Risk/Reward Ratio:** 1:100.

**Historical Comparison:**
The profiability is roughly equivalent to George Soros's famous 1992 trade against the British Pound (~$1B Profit). This confirms that Terra failed not due to "irrational malice" but due to **rational market incentives**.
