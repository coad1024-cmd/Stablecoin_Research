<!-- [MermaidChart: 33ab3141-77af-42f6-9f7d-0e2571abb30b] -->
<!-- [MermaidChart: d707c3eb-f722-4dd8-9f94-8a4ffe6b52e3] -->

---

## **3. Operational Bottlenecks — Hard Constraints on Stability**

This section identifies the **operational failure points** where Terra’s stabilization logic broke under real-world load. These are not behavioral failures; they are **control-system saturation failures** that, once exceeded, convert instability into irreversible collapse.


Each bottleneck corresponds to a **specific module**, a **quantifiable limit**, and a **mechanically inevitable failure mode**.

---

### **3.1 Oracle Latency (Sensor Lag)**

**Component**
`x/oracle` (Validator price voting mechanism)

**Constraint**
Oracle update cadence governed by `VotePeriod` (≈5 blocks, ~30 seconds).

**Failure Mode**
During high-volatility events, market prices moved faster than the oracle could update. On-chain logic therefore executed against stale prices.

**Observed Dynamics**

* Off-chain LUNA price declined >10% within seconds.
* On-chain oracle continued reporting pre-crash prices.
* Redemption and minting logic accepted oracle prices as authoritative.
* **Empirical Snapshot (May 7):**
  | Timestamp | Binance Spot | Oracle Price | Deviation |
  | :--- | :--- | :--- | :--- |
  | 00:00:00 | $80.00 | $80.00 | 0.0% |
  | 00:01:00 | $78.50 | $80.00 | -1.9% |
  | 00:02:00 | $75.00 | $78.50 | -4.4% |
  | 00:03:00 | $68.00 | $75.00 | -9.3% |
  *Source: Reconstructed vote timestamps vs Binance 1m candles.*


**Consequence**
Arbitrageurs purchased LUNA off-chain at depressed prices and redeemed it on-chain at inflated oracle prices, forcing the protocol to mint unbacked UST. The stabilization mechanism thus **generated liabilities instead of absorbing them**.

![Oracle Deviation](../diagrams/fig_oracle_deviation.svg)
> **Figure 3.2**: Empirical Oracle Deviation. During the crash, the on-chain Oracle price (Red) consistently lagged the Binance Spot price (Blue), creating a risk-free arbitrage window that drained reserves.


**Sustainability Implication**
If oracle latency exceeds market crash speed, **no redemption-based stablecoin can remain solvent**. Stability requires oracle freshness to scale with volatility, not block time.

---

### **3.2 Liquidity Throttle Removal (CPMM Expansion)**

**Component**
`x/market` (UST–LUNA swap mechanism)

**Constraint**
Constant Product Market Maker (CPMM) depth governed by `BasePool` parameters.

**Failure Mode**
Under stress, CPMM spreads are expected to widen sharply, acting as a **mechanical brake** on redemptions.

**Observed Intervention**

* As UST sell pressure increased, governance passed **Prop 1164**, increasing `BasePool` size.
* This reduced spreads precisely when exit demand was accelerating.
* **Parameter Shift (Prop 1164):**
  | Parameter | Pre-1164 (Throttle) | Post-1164 (Floodgate) |
  | :--- | :--- | :--- |
  | `BasePool` | 50M SDR | 100M SDR |
  | `PoolRecoveryPeriod` | 36 Blocks | 18 Blocks |
  *Effect: Doubled the capacity for "low slippage" exits, effectively subsidizing the run.*


**Consequence**
Instead of throttling redemptions, the protocol increased throughput. The CPMM transitioned from a **defensive convexity mechanism** into a **high-capacity exit ramp**, accelerating LUNA supply expansion.

![Minting Bottleneck](../diagrams/fig_minting_bottleneck.svg)
> **Figure 3.1**: Liquidity Bottleneck. The dashed line represents the $293M daily minting cap. Blue bars show daily UST burn volume exceeding this cap during the run, forcing the protocol to default on immediate redemptions until Prop 1164 removed the safety limits.


**Sustainability Implication**
Removing liquidity throttles during a run converts a stabilizer into an amplifier. Defensive convexity must not be discretionary.

---

### **3.3 Endogenous Minting Loop (Death Spiral Physics)**

**Component**
`MsgSwap` (UST redemption → LUNA minting)

**Constraint**
Market depth of LUNA relative to redemption volume.

**Failure Mode**
UST redemptions minted LUNA, which itself served as the system’s backing asset. As LUNA price declined, the quantity of LUNA minted per UST increased nonlinearly.

**Observed Dynamics**

* At high LUNA prices, minting impact was absorbable.
* As LUNA market cap collapsed, identical redemptions required orders of magnitude more LUNA issuance.
* Mint volume rapidly exceeded order book depth.

**Consequence**
Price collapsed faster with each redemption, creating a positive feedback loop:
UST redemptions → LUNA dilution → price collapse → weaker backing → more redemptions.

**Empirical Evidence:**
*   **Minting Ratio Exploded:** As LUNA falling from $80 to $0.0001, the LUNA minted per 1 UST redeemed rose from **0.0125** to **10,000+**.
*   **Vertical Supply Wall:** See [Figure 3.1](../diagrams/fig_minting_bottleneck.svg) above; the orange "Mint" bars become asymptotic relative to the blue "Burn" bars.


**Sustainability Implication**
An asset cannot simultaneously function as **backing, shock absorber, and redemption output**. Endogenous backstops create reflexive instability unless strictly bounded.

---

### **3.4 Governance Reaction Latency**

**Component**
Cosmos SDK Governance Module

**Constraint**
Proposal lifecycle: submission → voting → execution (days).

**Failure Mode**
Critical parameter changes (fees, halts, throttles) required governance approval.

**Observed Mismatch**

* Bank-run dynamics unfolded on a **minute-scale**.
* Governance mechanisms operated on a **day-scale**.

**Consequence**
By the time corrective proposals could execute, the system state had already irreversibly deteriorated.

**Sustainability Implication**
Human governance cannot serve as a real-time risk control layer. Automated circuit breakers are mandatory for crisis survivability.

---

### **Section 3 Synthesis**

Terra’s collapse was not caused by a single flaw, but by the **simultaneous breach of multiple operational limits**:

* Oracle latency invalidated price truth
* Liquidity throttles were manually disabled
* Endogenous minting exceeded market depth
* Governance reacted slower than the market moved

Once these bottlenecks were crossed, collapse was **mechanically inevitable**, regardless of intent or intervention.

Operational constraints define the **true boundary of sustainability**. Any stablecoin architecture that ignores them is stable only in theory.

---

