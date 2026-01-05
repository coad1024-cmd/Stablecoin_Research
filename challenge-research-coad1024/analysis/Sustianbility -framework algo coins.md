
---

# 1) Business-Model Decomposition — treat the protocol like a bank

Break the protocol into liabilities (stablecoins issued) and assets + income (what backs them and how the protocol earns).

Actors: Users, Arbitrageurs/Keepers, Governance, Custodians, Oracles, Market Makers.

Revenue sources (how the protocol *pays* for resilience):

* **Seigniorage / Spread Gains** — profit from mint/burn arbitrage and AMM spread capture.
* **Stability Fees / Borrowing Rates** — fees charged for issuing stablecoins via collateralized positions.
* **Liquidation Penalties** — one-off revenue from undercollateralized positions.
* **Yield on Reserves / RWA Income** — interest earned on treasuries, T-bills, staking yields.
* **Protocol-Owned Liquidity (POL) Returns** — fees/impermanent loss from AMMs.

Costs (what drains equity during stress):

* **Redemption / Swap Costs** (including mint/burn costs, bank/custody fees).
* **Keeper Incentives & Gas** during mass liquidations.
* **Dilution / Token minting to cover bad debt** (shareholder loss path).
* **Operational & legal expenses** (audits, custodians, compliance).

**Design trade-off principle:** anything that *lowers short-term peg pain* (e.g., raising BasePool, lowering spreads, instant low-fee redemptions into an endogenous asset) can increase long-term insolvency risk unless matched by credible exogenous reserves.

---

# 2) Key Metrics & Health Indicators

---

## 1. Net Interest Margin (NIM)

**Definition**

```
NIM = WeightedAvgYieldOnAssets − WeightedAvgCostOfLiabilities
```

**Unit:** % annualized

**Interpretation**

NIM measures whether the protocol can sustain its liabilities without external subsidy. A persistently negative NIM implies that the system is funding stability through equity dilution, reserve drawdown, or deferred losses.

**Alert**

* `NIM < 0` for 30 consecutive days → governance intervention required.

---

## 2. True Buffer Capacity (Exogenous vs. Endogenous)

**Definitions**

```
ExogenousBuffer = HardReserves − StressScenarioLosses
EndogenousAbsorption = MarketCap × LiquidityHaircut
```

```
BufferDays = ExogenousBuffer / AvgDailyOutflows
```

**Unit:** USD; days

**Interpretation**

Only **exogenous buffers** (cash, treasuries, BTC reserves) provide true solvency protection. Endogenous absorption (native token market cap) degrades during stress and must not be treated as a reserve.

**Alerts**

* `BufferDays < 7` → elevated insolvency risk
* Reliance on EndogenousAbsorption as primary buffer → structural fragility

---

## 3. Exit Coverage Ratio (XCR)

**Definition**

```
XCR = AvailableMarketLiquidity / StressExitDemand
```

**Unit:** Ratio

**Interpretation**

XCR measures whether exit demand can be absorbed without nonlinear price collapse. It generalizes liquidation coverage for overcollateralized systems and redemption depth for algorithmic systems.

**Stress Target**

* `XCR ≥ 2` under a 1-in-100, 24-hour stress scenario

**Alert**

* `XCR < 1` → disorderly exit regime likely

---

## 4. Redemption Friction Sensitivity (ϕ)

**Model**

```
s(x) = s₀ + φ · (RedemptionVolume / RecoveryCapacity)
```

Where:

* `s(x)` = effective redemption spread
* `φ` = friction sensitivity parameter

**Unit:** Dimensionless

**Interpretation**

ϕ governs how rapidly exits become expensive as volume increases. Excessive friction disables arbitrage and can convert stabilization mechanisms into failure accelerants.

**Alert**

* `φ > 0.5` **and** RedemptionVolume spikes → immediate peg fragility

---

## 5. Oracle Deviation & Latency Statistics

**Metrics**

```
OracleBiasₜ = Median(OraclePriceₜ) / ExchangeMidₜ − 1
OracleStdDev = rolling σ(OraclePrice)
OracleLag = ExchangePriceₜ − OraclePriceₜ
```

**Unit:** %

**Alerts**

* `|OracleBias| > 5%` → restrict critical mint/redeem operations
* OracleStdDev spike → widen safety margins
* Persistent oracle lag during negative price shocks → high-risk state

---

## 6. Effective Collateralization Ratio (ECR)

**Definition**

```
ECR = EffectiveBackingValue / StablecoinLiabilities
```

EffectiveBackingValue must be computed using conservative haircuts, adverse price impact, and time-to-liquidate assumptions.

**Unit:** Ratio

**Interpretation**

Spot collateralization is insufficient. The **trajectory** of ECR is more important than its instantaneous value.

**Alert**

* `d(ECR)/dt < 0` and accelerating → run dynamics likely

---

## 7. Spread Elasticity & Exit Cost at Scale

**Method**

Compute the spread curve `Spread(x)` for increasing net exit sizes.

**Key Properties**

* Absolute exit cost for large trades
* Convexity of the spread curve

**Alert**

* Low or declining `Spread(large x)` → insufficient defense against large exits

---

## 8. Correlation & Concentration Risk

**Metrics**

* Correlation matrix across backing assets
* Top-N counterparty exposure (%)

**Alerts**

* High correlation between backing asset value and stablecoin demand → terminal risk
* > 25% reliance on a single oracle, custodian, or venue → cascade vulnerability

---

## 9. Governance Reaction Latency

**Definition**

```
GovLatency = Median(Time from Proposal → Execution)
```

**Comparison Benchmark**

```
MarketCrashSpeed = 99th-percentile drawdown time
```

**Alert**

* `GovLatency ≫ MarketCrashSpeed` → automated backstops required

---

## 10. Reflexivity Gain (System-Level)

**Conceptual Definition**

Reflexivity Gain (G) measures how much a stabilization action amplifies underlying stress.

**Interpretation**

* `G < 1` → stabilizing regime
* `G > 1` → destabilizing (death-spiral) regime

**Alert**

* Sustained `G > 1` → structural failure is inevitable

---

## **3. Operational Bottlenecks — Where Stability Breaks in Practice**

This section identifies the **operational constraints** that determine whether a theoretically stable mechanism survives real-world stress. These are not abstract risks; they are **hard system limits** that, once breached, convert instability into irreversible collapse.

Each bottleneck is specified by:

* **Failure mode**
* **Observable signal**
* **Stress condition**
* **Design implication**

---

### **3.1 Oracle Latency & Integrity**

**Failure Mode**
When on-chain prices lag fast off-chain moves, redemption and liquidation logic executes against **obsolete state**, enabling risk-free extraction of protocol value.

**Terra Reality**
Terra’s oracle relied on validator voting with a VotePeriod cadence. During the LUNA crash, price updates lagged centralized exchanges by tens of seconds while prices moved >30% in minutes. This allowed arbitrageurs to mint liabilities against stale prices, accelerating insolvency.

**Observable Signal**

* Oracle bias exceeding tolerance:
  [
  \text{OracleBias}*t = \frac{P*{\text{oracle}} - P_{\text{market}}}{P_{\text{market}}}
  ]

**Stress Condition**

* Large price moves within a single oracle update window (≥20–50%).
* Validator participation degradation during congestion.

**Design Implication**

* Oracle freshness must scale with volatility, not block time.
* If oracle bias exceeds threshold, **critical actions (mint, redeem, liquidate)** must halt or switch to conservative pricing.
* No algorithmic stablecoin can survive if oracle lag is unbounded under stress.

---

### **3.2 Auction Throughput & Keeper Capital**

**Failure Mode**
Liquidation demand exceeds keeper capital and auction throughput, turning orderly deleveraging into disorderly fire sales.

**Terra Reality**
UST redemptions indirectly forced massive LUNA issuance and liquidation. Available market depth and keeper capacity were insufficient to absorb flows, especially under chain congestion.

**Observable Signal**

* Liquidation backlog growth
* Auction clearance times diverging from assumptions
* Clearing prices collapsing beyond modeled slippage

**Stress Condition**

* Concurrent liquidations during network congestion
* Keeper capital drawdown coinciding with price volatility

**Design Implication**

* Auction throughput must exceed worst-case liquidation demand.
* Systems must include throttles, partial fills, and rate limits.
* “Infinite mint + market absorbs it” is not a valid assumption.

---

### **3.3 Redemption Mechanics That Do Not Scale**

**Failure Mode**
Volume-sensitive redemption fees suppress on-chain arbitrage precisely when it is needed to stabilize the peg.

**Terra Reality**
As UST redemptions surged, Terra’s spreads rose sharply (up to ~60%), making on-chain arbitrage uneconomic. Peg repair shifted to centralized exchanges, where it became destabilizing instead of corrective.

**Observable Signal**

* On-chain redemption volume collapses while off-chain selling spikes
* Redemption cost exceeds secondary-market exit cost

**Stress Condition**

* Large redemption waves (>5–10% supply)
* Rapid spread escalation under volume

**Design Implication**

* Peg defense must remain **cheaper than secondary-market exit**.
* Redemption friction must be bounded and predictable.
* Mechanisms that “block exits” under stress do not create stability — they create panic.

---

### **3.4 Endogenous Backstops (Self-Referential Assets)**

**Failure Mode**
Using the same asset as both **backing and absorption mechanism** creates reflexive dilution loops.

**Terra Reality**
UST redemptions minted LUNA. Increased LUNA supply depressed price, reducing backing value and requiring even more minting — a classic positive feedback loop leading to hyperinflation.

**Observable Signal**

* Mint velocity accelerating faster than market depth
* Backing asset price falling as supply increases

**Stress Condition**

* Redemptions exceed market capacity to absorb newly minted tokens
* Backing asset demand collapses simultaneously

**Design Implication**

* Endogenous assets cannot serve as primary crisis backstops.
* Hard caps, circuit breakers, or exogenous buffers are mandatory.
* If minting the backstop worsens solvency, the system is mathematically unstable.

---

### **3.5 UX & Execution Friction**

**Failure Mode**
If only sophisticated actors can execute protocol-level arbitrage quickly, retail holders exit via exchanges, shifting stabilization into destabilization.

**Terra Reality**
Retail users could not efficiently redeem UST on-chain during stress. They sold on centralized exchanges instead, worsening de-pegging and draining liquidity.

**Observable Signal**

* Rising exchange sell pressure while on-chain redemptions stagnate
* Widening gap between peg deviation and protocol response

**Stress Condition**

* High volatility combined with complex or slow redemption UX
* Congested chains during crisis periods

**Design Implication**

* Stability mechanisms must be usable under stress by non-experts.
* If peg defense requires sophistication, the system will fail socially before it fails economically.

---

### **Section 3 Synthesis**

Terra did not fail because its **monetary logic** was misunderstood; it failed because its **operational assumptions were violated simultaneously**:

* Oracles lagged
* Liquidity was insufficient
* Redemption incentives inverted
* Endogenous backing collapsed
* Human reaction time exceeded market speed

Operational bottlenecks define the **true stability boundary** of an algorithmic stablecoin. Any sustainability framework that ignores them is incomplete.


---

# 4) Regulatory Survivability (The Moat) — what policy/regulatory realities kill you

This is not optional. Map your legal counterparty exposure and have contingency paths.

Checklist (each must be quantified and stress-tested):

1. **Custody & Banking Exposure** — % reserves in any single bank/custodian; can they be frozen? (SVB → USDC freeze → contagion). Target: no single banking counterparty > X% (X small; <10% recommended). 

2. **Legal Enforceability of RWAs** — Are RWA claims legally accessible under a bankruptcy run? Time to enforce legal claims (days/weeks).

3. **Censorship & Compliance Risk** — Are on-chain assets subject to compliance freezes? If yes, you cannot promise instant redemption to holders globally.

4. **Regulatory Capital Expectations** — simulate a scenario where regulators require a capital buffer (e.g., 2–5% of liabilities). Can the protocol meet that without diluting governance token catastrophically?

5. **On-Ramp/Off-Ramp Dependencies** — If your peg relies on a bridge to fiat rails or regulated stablecoins, model de-banking as an explicit scenario.

---

# 5) Stress Tests & Red Lines — what to run automatically

Run these daily as part of CI for protocol health:

* **Flash Crash 30-min test**: 50% collateral price drop in 30 min → measure auctions required, keeper capital drained, residual bad debt, NIM, BufferDays.
* **Bank Freeze test**: 30% of custodial reserves frozen for 72 hours → simulate redemption and peg dynamics. (SVB/USDC scenario). 
* **Whale Exit test**: single buyer sells X% of supply in 24h (X = 10%, 25%, 50%) → compute Spread(→ cost) and ECR after. If Spread low enough to allow cheap exit you’ve got a design hole. 

**Hard red lines (examples)**: BufferDays < 3; OracleBias > 10%; LCR < 1 under 1-in-100 stress → automatic emergency modes (pause redemptions, increase fees capped, circuit-break auctions).

---

# 6) Concrete quick-wins & design recommendations

1. **Cap floating redemption fees** and prefer *quantity-limited fixed-fee windows* rather than fee functions that explode with volume. (Terra’s floating fees killed arbitrage). 

2. **Add exogenous reserve pools (small but real fiat/USDC/Treasury buffer)** that can be used only under pre-specified emergency conditions; simulate governance-to-execute latency. Hybrid designs (partial reserve) materially improve survivability. See simulation proposals and reserve pool findings.

3. **Oracle hardening**: multi-feed median + stale-price detector + emergency stop on excessive deviation. Implement circuit-breakers that block mint/redemptions if OracleBias > threshold.

4. **Auction redesign**: partial-fill Dutch auctions + per-asset `hole` limits + keeper incentive augmentation under stress.

5. **Limit endogenous minting during redemptions** (avoid minting massive supply of the backstop token as the only redemption path).

---

# 7) Quick implementation snippets (compute metrics yourself)

```python
# pseudo-code (conceptual)
def nim(yield_assets, weights_assets, cost_liabilities, weights_liab):
    return sum([y*w for y,w in zip(yield_assets, weights_assets)]) - sum([c*w for c,w in zip(cost_liabilities, weights_liab)])

def buffer_days(surplus_usd, avg_daily_outflows_usd):
    return surplus_usd / (avg_daily_outflows_usd + 1e-9)

def oracle_bias(oracle_price, exchange_price):
    return oracle_price / exchange_price - 1.0
```

Wire these into a dashboard, and set automated alerts to governance and on-call ops.

---

# 8) Final blunt verdict

Algorithmic stablecoins *can* be made more robust — but only by admitting and engineering around two harsh facts:

1. **Sensors (oracles) are slow and can be gamed.** If your stabilization mechanism depends on a stale on-chain price while the off-chain market moves fast, you will print liabilities. Design must either remove that dependence or add exogenous reserves/circuit breaks. 

2. **Self-referential backstops (minting the system’s own token to pay redemptions) create reflexive dilution loops.** Unless you cap supply growth or add exogenous capital, hyperinflation is a deterministic possibility. Terra’s LUNA inflation/dilution loop is the textbook example. 

Use the metrics and stress tests above as your acceptance criteria. If your design fails any of the major stress tests, it’s trash for production — and you should either re-engineer the mechanism (add real reserves, cap minting, fix oracles) or kill it.

---
