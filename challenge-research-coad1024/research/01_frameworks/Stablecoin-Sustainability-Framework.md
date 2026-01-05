# Framework for Analysis: Sustainability of Overcollateralized Stablecoins

## Purpose

This document provides a comprehensive framework for writing a **Sustainability Analysis Article** for any overcollateralized stablecoin (e.g., LUSD, RAI, DAI). "Sustainability" here is defined not just as current solvency, but as the system's ability to survive and persist over the long term through market cycles, regulatory shifts, and economic stress.

This framework synthesizes the **"Sustainability Triangle"** model (interacting feedback loops) with the **"Dual Mandate"** concept (profit vs. stability) from the broader research meta-framework.

---

## Part I: The Economic Engine (Viability)

*Focus: Can the protocol pay its bills and independent of speculation?*

## Comparison Methodology

This framework generates individual sustainability profiles that can be synthesized into comparative insights.

### Analysis Dimensions

**Dimension 1: Economic Viability**
- Revenue model classification and sustainability ratios
- Cost structure and capital efficiency
- Dependency on speculative vs organic demand

**Dimension 2: Collateral Regime Stability**
- Asset composition and concentration risk
- Liquidation mechanism robustness
- Reflexivity and internal collateral loops

**Dimension 3: Governance & Adaptability**
- Parameter mutability and response speed
- Governance concentration and attack surface
- Crisis response mechanisms

### Protocol-Specific Adaptations

This framework is based on MakerDAO architecture but adapts for:

- **Immutable protocols** (e.g., LUSD): Skip governance sections, focus on parameter constraints
- **Novel liquidation mechanisms** (e.g., crvUSD): Modify Loop 2 to analyze soft liquidation economics  
- **Hybrid models**: Document deviations from pure overcollateralization

### Evidence Standards

- All revenue/cost data must be verified from on-chain sources (Dune, Token Terminal, protocol dashboards)
- Historical stress tests cite specific dates and price data
- When data is unavailable, mark as `[DATA UNAVAILABLE]` rather than estimate
- Every claim must have a source citation with URL and access date

### 1. The Business Model Decomposition

Analyze the protocol as a business. It issues liabilities (stablecoins) and holds assets (collateral).

* **Revenue Sources:**
  * **Stability Fees / Interest:** The cost to borrow. (Deep dive: Is this competitive? Is it variable or fixed? Does it cover costs?)
  * **Liquidation Penalties:** Revenue generated from failures. (Warning: high reliance here = predatory model).
  * **Yield on Collateral:** Does the protocol capture yield from underlying assets (e.g., RWA yield, Staking yield)?
  * **Protocol-Owned Liquidity (POL) Returns:** Revenue from AMM positions.
* **Cost Structure:**
  * **User Savings Rate:** Cost paid to stablecoin holders (e.g., DSR).
  * **Incentive Emissions:** Cost of governance tokens emitted to subsidize liquidity. **Critical Metric:** If Emissions > Revenue, the system is bleeding equity to sustain the peg.
  * **Operational Expenses:** Oracle costs, keepers, governance delegations, audits.

### 2. Key Metrics & Health Indicators

#### A. Liquidation Dependency Ratio (LDR)

**Critical Metric for Sustainability:**

```
LDR = Liquidation Revenue / Total Revenue
```

**Interpretation:**
- **LDR > 0.5** = High dependency (protocol requires user failure to survive)
- **LDR 0.2-0.5** = Moderate dependency  
- **LDR < 0.2** = Low dependency (sustainable without liquidations)

For protocols with novel mechanisms (soft liquidations, no-liquidation designs), document how they avoid this dependency or transfer the cost elsewhere.

#### B. Net Interest Margin (NIM)

The spread between asset yield and liability cost:

```
NIM = (Weighted Avg Yield on Assets) - (Weighted Avg Cost of Liabilities)
```

- Positive NIM is required for long-term survival
- NIM < 0.5% indicates a "volume business" requiring massive scale
- Compare NIM across market cycles (bull vs bear)

#### C. Collateral Concentration (Herfindahl Index)

Measures diversification risk:

```
HHI = Σ(share_i)²
```

Where share_i is the percentage of each collateral type.

- **HHI > 0.5** = Highly concentrated (single point of failure risk)
- **HHI 0.25-0.5** = Moderate concentration
- **HHI < 0.25** = Well diversified

#### D. Surplus Buffer Runway

How long can the protocol survive with zero revenue?

```
Runway (months) = Surplus Buffer / Monthly Operating Costs
```

**Minimum safe threshold:** 12 months of runway

#### E. Capital Efficiency Ratio

```
Capital Efficiency = Total Stablecoin Supply / Total Collateral Value
```

- Higher ratio = more capital efficient
- But efficiency trades off against safety margin
- Compare against competitors to assess competitiveness

---

## Part II: The Sustainability Triangle (Systemic Resilience)

*Focus: How do the core feedback loops interact under stress? Based on the MakerDAO/Sky model.*

### Loop 1: Collateral Quality

* **Asset Composition:** Breakdown by type (Crypto-native, Stablecoins, RWAs).
* **Correlation Risks:** Are the assets correlated with each other? Are they correlated with the governance token? (e.g., internal loops like LUNA).
* **Liquidity Profile:** Can the collateral be sold deep enough in the open market during a crash?

### Loop 2: Incentive Mechanisms

* **Alignment:** Do incentives (fees, penalties) actually encourage the right behavior during a crash?
  * *The Trap:* Raising fees during a crash might force liquidations rather than repayment.
* **Keeper Economics:** Are liquidations profitable for third parties? If gas prices spike 100x (Solana/Ethereum congestion), do keepers still run?

### Loop 3: Governance & Backstop

* **Response Latency:** How fast can the protocol change parameters (Fees, Debt Ceilings)?
  * *Metric:* `Governance Delay` vs `Market Crash Speed`.
* **The Equity Backstop:** In a deficit, how is it covered?
  * *Debt Auctions:* Minting governance tokens (dilution).
  * *Insurance Fund:* Pre-funded reserve.
  * *Haircuts:* Direct loss to stablecoin holders (redeemable at < $1).

---

## Part III: Stress Test Framework (Operational Bounds)

Rather than theoretical regime definitions, test each protocol against historical stress scenarios and document actual performance.

### Standard Stress Tests

#### Test 1: The 70% Collateral Crash (Black Thursday Equivalent)

**Scenario:**
- Primary collateral drops 70% in 48 hours (e.g., ETH $1,200 → $360)
- Gas prices spike 10-50x normal
- Liquidation throughput is constrained

**Evaluation Criteria:**
- Does the protocol maintain peg within ±5%?
- Is there bad debt accumulation? How much?
- Do liquidation mechanisms function under gas pressure?
- Can governance respond before insolvency?

**For DAI:** Document March 12-13, 2020 performance
**For LUSD:** Document any 70%+ ETH drawdowns since launch (May 2021)
**For crvUSD:** Protocol launched post-crypto winter, mark as `[UNTESTED]`

#### Test 2: The Liquidity Freeze (FTX/3AC Equivalent)

**Scenario:**
- Major CEX delisting or freeze (e.g., FTX collapse)
- DEX liquidity drops 80% as LPs exit
- No new minting for 30+ days

**Evaluation Criteria:**
- Can users exit positions at reasonable cost?
- Does stablecoin trade at significant discount?
- Does protocol survive with frozen demand?
- Are there bank run dynamics (redemption queues)?

**For all protocols:** Search for November 2022 FTX collapse impact

#### Test 3: The Collateral Contagion (USDC Depeg Equivalent)

**Scenario:**
- Major stablecoin collateral (USDC) experiences temporary depeg to $0.88
- Affects all protocols using USDC as collateral or in liquidity pools
- Lasts 48-72 hours (March 10-13, 2023)

**Evaluation Criteria:**
- Does the system remain solvent with degraded collateral?
- Can liquidations process accurately with stablecoin volatility?
- Does governance emergency response work?
- Do users lose funds or get liquidated unfairly?

**For DAI:** Critical test due to high USDC exposure via PSM
**For LUSD:** No USDC exposure, should be unaffected
**For crvUSD:** Check collateral composition for USDC exposure

### Historical Performance Documentation Requirements

For each stress event, document:

1. **Date and Duration:** Exact timestamps
2. **Price Data:** Min/max prices during event (with source)
3. **Peg Stability:** Stablecoin price range during crisis
4. **Bad Debt:** Total amount of undercollateralized positions (if any)
5. **Governance Response:** What actions were taken? How quickly?
6. **User Impact:** Liquidations, losses, locked funds
7. **Sources:** Links to governance forums, Dune dashboards, articles

### Stress Test Scoring

Rate each protocol's performance:

- ✅ **Robust:** Survived with <1% bad debt, peg held within ±2%
- ⚠️ **Degraded:** Survived with 1-5% bad debt OR temporary peg loss >5%
- ❌ **Failed:** >5% bad debt OR permanent peg break OR system halt

### For New Protocols (No Historical Data)

If protocol launched after major stress events:

1. Mark as `[UNTESTED IN SEVERE STRESS]`
2. Note this as an explicit risk factor
3. Conduct theoretical analysis: "Based on mechanism design, we predict..."
4. Compare mechanism to proven protocols: "Similar to [X] which performed [Y]"

### Regime Transition Analysis (Klages-Mundt Framework)

**For protocols with sufficient historical data**, analyze variance behavior:

**Stable Regime Indicators:**
- Stablecoin volatility remains below collateral volatility
- Small collateral shocks produce bounded price deviations
- System maintains mean-reversion to peg

**Unstable Regime Indicators:**
- Stablecoin volatility EXCEEDS collateral volatility
- Deleveraging spirals emerge
- Reflexive feedback loops amplify shocks

**Submartingale Failure Mode:**
- Market expectations turn negative on collateral
- Speculator exit creates supply contraction
- Demand for redemption while supply vanishes = price spike above peg
- Appreciation of liabilities concurrent with depreciation of assets

**Document which regime the protocol operated in during each stress test.**

---

## Part IV: Operational & Regulatory Sustainability

*Focus: External existential threats.*

### 1. Operational Bottlenecks

* **Oracle Infrastructure:** Reliance on centralized feeds (Chainlink) vs internal. Latency risks.
* **Auction Throughput:** Capacity of the system to process concurrent liquidations. (e.g., MakerDAO Black Thursday congestion).

### 2. Regulatory Survivability (The Moat)

* **Censorship Resistance:** Can the protocol freeze assets? (USDC dependency).
* **MiCA/Compliance Cost:** If regulations require capital buffers (e.g., 2% equity), can the protocol afford it?
* **Off-Ramp Dependency:** Does the system rely on specific banking partners that could be de-banked?

---

## Part V: Comparative Synthesis Guidelines

After analyzing individual protocols, synthesize findings to extract insights about the design space.

### Step 1: Pattern Identification

Look for recurring tradeoffs across all analyzed protocols:

- **Immutability vs Adaptability:** Can the protocol respond to crises vs. is it censorship resistant?
- **Capital Efficiency vs Security:** Lower collateral ratios vs. higher safety margins?
- **Decentralization vs Scalability:** Pure crypto collateral vs. RWA integration?
- **Revenue Sustainability vs User Cost:** Protocol profitability vs. competitive fee rates?

Document which protocols make which tradeoffs and why.

### Step 2: Design Philosophy Clustering

Group protocols by their fundamental approach:

**Cluster A: Minimalist/Immutable**
- Philosophy: Prioritize censorship resistance and predictability
- Example: LUSD with fixed parameters
- Tradeoff: Cannot adapt to black swans

**Cluster B: Adaptive/Governed**
- Philosophy: Prioritize crisis response and scalability
- Example: DAI with active governance
- Tradeoff: Governance becomes regulatory attack surface

**Cluster C: Hybrid/Experimental**
- Philosophy: Test novel mechanisms for better capital efficiency
- Example: crvUSD with soft liquidations
- Tradeoff: Untested in severe stress, unknown tail risks

### Step 3: Sustainability Model Classification

Classify each protocol's economic foundation:

**Type A: Liquidation-Dependent (>30% revenue from penalties)**
- Requires continuous user failure to generate income
- Revenue is counter-cyclical (increases in bear markets)
- Risk: Predatory dynamics, user misalignment

**Type B: Yield-Capturing (>50% revenue from collateral yield)**
- Monetizes backing assets (RWAs, staking yield)
- Revenue is exogenous (depends on macro rates)
- Risk: Regulatory capture of yield sources

**Type C: Fee-Based (>50% revenue from stability fees)**
- Revenue from organic usage (minting/borrowing)
- Revenue is pro-cyclical (increases in bull markets)
- Risk: Demand volatility, competitor pressure

**Type D: Subsidized (token emissions > revenue)**
- Protocol burns equity to subsidize operations
- Unsustainable long-term without transition
- Risk: Death spiral if emissions end

### Step 4: Metric Comparison Table

Create a standardized comparison:

| Metric | Protocol A | Protocol B | Protocol C |
|--------|-----------|-----------|-----------|
| **Economic Viability** |
| Liquidation Dependency Ratio | X% | Y% | Z% |
| Net Interest Margin | X% | Y% | Z% |
| Surplus Buffer Runway | X mo | Y mo | Z mo |
| **Collateral Stability** |
| Herfindahl Index (Concentration) | X | Y | Z |
| Reflexivity Risk | Yes/No | Yes/No | Yes/No |
| Liquidation Mechanism | Type | Type | Type |
| **Governance & Adaptability** |
| Parameter Mutability | High/Med/Low | High/Med/Low | High/Med/Low |
| Response Latency | X hours | Y hours | Z hours |
| Governance Concentration | High/Med/Low | High/Med/Low | High/Med/Low |
| **Stress Test Performance** |
| 70% Crash Test | ✅/⚠️/❌ | ✅/⚠️/❌ | ✅/⚠️/❌ |
| Liquidity Freeze Test | ✅/⚠️/❌ | ✅/⚠️/❌ | ✅/⚠️/❌ |
| Collateral Contagion Test | ✅/⚠️/❌ | ✅/⚠️/❌ | ✅/⚠️/❌ |

### Step 5: Key Insight Extraction

Your synthesis should answer:

1. **Which sustainability model is most robust long-term?**
   - Under which conditions? (Bear vs bull, high vs low rates)
   
2. **What tradeoffs are inevitable vs which are design choices?**
   - Are some risks inherent to overcollateralization?
   - Or can better design eliminate them?

3. **Do any protocols solve problems others cannot?**
   - Novel mechanisms that work?
   - Clever governance structures?

4. **What does this reveal about the future of stablecoins?**
   - Convergence toward a dominant model?
   - Or permanent diversity for different use cases?

### Step 6: Design Space Mapping

The goal is not to declare a "winner" but to map the **viable design space**:

- Which approaches are fundamentally viable?
- Which are only viable under specific conditions?
- Which are doomed regardless of execution?

Create a framework that helps future protocol designers understand:
- "If you want X property, you must accept Y tradeoff"
- "If you're designing for Z market condition, choose A architecture"

This is the ultimate value of comparative analysis.

---

## Writing Guidelines for the Article

1. **Evidence-Based:** Do not trust whitepapers. Use on-chain data (Dune, Etherscan) to verify revenue and collateral claims.
2. **Comparative Context:** Always benchmark the subject against a standard (e.g., "Unlike LUSD's immutable governance, X uses...").
3. **Visuals:**
    * *Revenue vs Expenses Chart (Historical)*.
    * *Collateral Composition (Risk Weighted)*.
    * *The Sustainability Triangle Diagram*.
4. **Tone:** rigorously analytical, skeptical, institutional-grade. Avoid marketing fluff.

## Recommended References

* **General:** `Analysis-Meta-framework.md` (Pillar II).
* **Case Study:** `analysis/makerdao/DAI_1&2/Updated Part II Sustainability When Stability Has to Pay for Itself.md` (for deep dive on Regime Boundaries).
* **Theoretical:** Klages-Mundt & Minca papers (for Deleveraging Spirals).
