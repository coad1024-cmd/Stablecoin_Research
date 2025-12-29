# Data Extraction Pipeline: The "Defensible" Standard

This document outlines the rigorous methodology for reconstructing the Terra crash forensics data. It rejects "eyeballing" in favor of reproducible, peer-verifiable data sources.

## 1. The Strategy: "Three Worlds"
We source data from three distinct environments and join them on `Date` (UTC).

| World | Data Points | Source | Method |
| :--- | :--- | :--- | :--- |
| **Market** | UST Supply, LUNA Mcap, LUNA Price | **CoinGecko** | Public API |
| **On-Chain** | Anchor Deposits, Anchor Borrows | **Dune Analytics** | SQL Queries |
| **Off-Chain** | LFG BTC Reserves | **LFG Disclosures** | Manual Construction |

---

## 2. Market Data (CoinGecko)

We use the CoinGecko API to reconstruct valid daily closes.

### Python Extraction Logic
```python
from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()

def get_market_chain(coin_id, vs='usd', days='max'):
    # Fetch historical market chart
    data = cg.get_coin_market_chart_by_id(coin_id, vs_currency=vs, days=days)
    
    # Parse Market Caps
    df = pd.DataFrame(data['market_caps'], columns=['timestamp', 'market_cap'])
    df['Date'] = pd.to_datetime(df['timestamp'], unit='ms').dt.date
    
    # Group by Date and take the LAST entry (Close)
    return df.groupby('Date')['market_cap'].last().reset_index()

# Execution
luna_mc = get_market_chain('terra-luna')
ust_supply = get_market_chain('terrausd') 
```

---

## 3. Anchor Data (Dune Analytics)

We query the indexed Terra Classic state to get precise daily balances.

### Target Tables
*   `anchor_protocol.daily_state` (or equivalent community abstraction)

### SQL Query
```sql
-- Dune Logic for Anchor Deposits & Borrows
SELECT
    DATE(block_time) AS Date,
    SUM(deposits) AS Anchor_Deposits,  -- Total aUST supply * exchange rate
    SUM(borrows) AS Anchor_Borrows     -- Total stablecoins borrowed
FROM anchor_protocol.daily_metrics     -- Conceptual table, verify specific Dune instance
WHERE block_time > '2021-01-01'
GROUP BY 1
ORDER BY 1 ASC
```

*Verification*: `Anchor_Deposits` must peak > $14B in April 2022.

---

## 4. LFG Reserves (Manual Construction)

Since reserves were held off-chain or in non-standard multi-sigs, we manually reconstruct the timeline from LFG transparency reports.

### The Construction Table
| Date | BTC Balance | Note |
| :--- | :--- | :--- |
| 2022-01-01 | 0 | No reserves |
| 2022-02-01 | 42,406 | "LFG Formation" |
| 2022-03-22 | 30,727 | Accumulation phase |
| 2022-05-05 | 80,394 | Peak Reserves |
| 2022-05-10 | 313 | Deploying defense |
| 2022-05-16 | 313 | Post-crash |

*Method*: Forward-fill these discrete values to create a daily series.

---

## 5. The Join (Final Artifact)
Join all datasets on `Date` (UTC).

**Sanity Checks**:
1.  `UST_Supply` > 15B (Peak)
2.  `Anchor_Deposits` > 10B (Peak)
3.  `LUNA_MarketCap` > 30B (Peak)

If these checks fail, the data source is corrupted.
