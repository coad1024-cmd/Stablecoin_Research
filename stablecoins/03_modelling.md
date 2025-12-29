## 3. Modelling

### Scenario: Terra Luna (UST) De-Peg Event

*Objective: Model the cost of attack vs. potential profit for an attacker triggering the UST/LUNA death spiral.*

#### Assumptions

* **UST Supply ($S$)**: $18,000,000,000 (at peak).
* **Curve Pool Liquidity ($L$)**: ~$300,000,000 (3-pool).
* **Attacker Capital ($C$)**: ~$1,000,000,000 (Accumulated UST + Short positions).

#### The Attack Loop (The Death Spiral)

```mermaid
graph TD
    A[Start: Attacker Dumps UST on Curve] -->|Imbalance| B(UST De-pegs < $0.98)
    B -->|Panic| C{Anchor Depositors Exit?}
    C -->|Yes| D[Burn UST -> Mint LUNA]
    D -->|LUNA Supply Explodes| E[LUNA Price Crashes]
    E -->|Market Cap Flip| F[LUNA Market Cap < UST Supply]
    F -->|Insolvency| G[UST Value -> $0.00]
    G -->|Close Shorts| H[Massive Profit]
```

#### Cost vs. Profit Analysis

$$ \text{Cost} = \text{Slippage on Dump} + \text{Borrow Fees (BTC/LUNA)} \approx \$300M $$

$$ \text{Profit} = (\text{Short LUNA Gains}) + (\text{Short BTC Gains}) \approx \$1B+ $$

**Feasibility Conclusion**:

* **Vulnerability**: The mechanism relied on LUNA market cap > UST supply. When LUNA crashed, the backing evaporated.
* **Attack Viability**: **High**. The liquidity on Curve was thin compared to the massive supply in Anchor. A concentrated dump was sufficient to trigger the panic.
