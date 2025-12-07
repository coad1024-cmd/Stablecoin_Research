# DAI at the Crossroads, Part II: Sustainability — When Stability Has to Pay for Itself

A three-part technical series unpacking Maker's architecture — from its on-chain reserves to its evolving sustainability model and the governance layer that now defines its credibility.

> Target audience: senior Solidity devs, protocol engineers, DeFi risk teams.

---
## Overview

Part I established how DAI is backed on-chain through deterministic invariants enforced by the `Vat`, collateral locks, and liquidation mechanics[1]. This Part II shifts focus from *what* creates backing to *whether that backing remains sustainable* under repeated stress. The central question: **Can Maker maintain solvency and peg stability simultaneously without entering permanent dilution cycles?**

The answer depends on three coupled feedback loops—collateral quality, incentive design, and governance responsiveness—forming the **Sustainability Triangle**. Imbalance in any loop cascades through the others. When collateral crashes faster than auctions can liquidate it, incentive mechanisms fail to recover value, and governance must dilute MKR to plug deficits[2][3][4]. Understanding where these boundaries lie is the focus of this part.

---
## Part I: The Sustainability Triangle — Three Coupled Feedback Loops

### 2.1 Framework: Beyond Backing to Sustainability

Backing and sustainability are fundamentally different concepts[1][2]. A vault can be perfectly overcollateralized on-chain yet economically unsustainable if market microstructure prevents collateral from being converted to DAI when needed[2]. Black Thursday (March 12-13, 2020) proved this distinction: the Vat invariants remained mathematically correct even as the protocol accumulated millions in bad debt[1][3][4].

The **Sustainability Triangle** models three reinforcing loops that must remain balanced for the system to survive stress[2]:

**Loop 1: Collateral** — Asset quality, diversification, correlation[1][2]

**Loop 2: Incentives** — Fee structure, liquidation design, auction mechanics[1][2][3]

**Loop 3: Governance** — Parameter control, emergency response, dynamic hedging[2][3][4]

In equilibrium, these loops balance each other[2]. High-quality collateral (Loop 1) allows loose incentives (Loop 2), reducing governance burden (Loop 3)[2]. Volatile collateral forces tighter auction parameters and faster governance intervention[3][4]. But under stress, these feedback relationships can invert—when collateral crashes, auctions fail to clear at market prices, incentives fail to adjust fast enough, and governance becomes the sole backstop[2][3][4].

---
### 2.2 Loop 1: Collateral — Foundation and Constraint

Collateral quality determines the baseline stability margin available to the system[1]. It constrains the other two loops: risky collateral requires tighter incentives and more responsive governance; stable collateral allows broader policy flexibility.

**Collateral properties and their systemic impact:**

| Property | Impact on Stability | Example |
|----------|-------------------|---------|
| **Volatility** | High volatility → tight liquidation ratios needed → capital inefficiency | ETH ~70% daily swings possible; USDC < 1% |
| **Liquidity** | Poor liquidity → slow liquidation → auction price slippage → larger deficits | ETH highly liquid; illiquid RWA risks fire sales[1] |
| **Correlation** | Crypto-correlated assets crash together → no diversification buffer during sector downturn | ETH+WBTC ~90% correlated; USDC uncorrelated[1][3] |
| **Custody** | Off-chain custody → counterparty risk → legal/regulatory exposure | PSM USDC introduces Circle risk[1][3] |

**The diversification imperative:**

Until March 2020, Maker was effectively a single-collateral system—98%+ of DAI backed by ETH[3]. When ETH crashed 43% in hours, liquidations cascaded with no uncorrelated collateral buffer[3]. The crash triggered the first regime transition: from stable (auctions clear above market) to unstable (auctions amplify crashes)[2][3][4].

Endgame's multi-collateral approach—ETH, WBTC, USDC, RWA—explicitly widens the stability region by introducing assets with decorrelated return distributions[1][3][4]. USDC backing provides a stability buffer that doesn't crash with crypto volatility. But this introduces new risks: custody, regulatory, and the uncomfortable truth that DAI's safety now depends on centralized infrastructure[1][4].

**Collateral composition post-Black Thursday (2024-2025):**

- **Crypto-native** (ETH, WBTC, etc.): ~35% of DAI supply; high volatility, no counterparty risk
- **Stablecoins** (USDC via PSM): ~30-40% of supply; low volatility, Circle custody risk
- **Real-World Assets** (RWA): ~5-10% of supply; off-chain backing, legal/regulatory risk, low liquidity

This hybrid structure is pragmatic but philosophically compromised: DAI's decentralization claim rests on increasingly centralized and off-chain dependencies[1][4].

---

### 2.2 Loop 2: Incentives — Aligning Behavior When Stakes Collapse

The incentives loop uses monetary mechanisms to align vault owners' and keepers' behavior with system health[1][2][3]. When markets function normally, fees and auction parameters work well[3]. However, when leverage constraints bind and participants face forced deleveraging, incentive mechanisms can fail to align behavior—they may perversely amplify crashes[2][3][4][5].

**Stability Fees (Vault Borrowing Cost):** Charged as interest accumulated into vault debt via the rate multiplier[1]. Current range: 0-12% annual depending on collateral type[9][10][11]. 

**Purpose:** discourage excessive debt minting, accumulate surplus for MKR buybacks, signal risk-adjusted cost of capital[1][9][10]. 

**Limitation:** fees only discourage *new* borrowing[9][10]. Vault owners already in leveraged positions face sunk costs—paying higher fees doesn't incentivize them to exit, it incentivizes them to hold or increase leverage hoping for price recovery[2][3][4][10].

**Liquidation Penalties and Auction Mechanics:** When a vault breaches the liquidation ratio, collateral is auctioned off[1]. A penalty fee (typically 13% for ETH-A) is added to debt, partially funding keeper rewards and flowing into system surplus[1][3]. Maker evolved from English auctions (Flipper, 2019-2020) with 10-minute duration to Dutch auctions (Clipper, 2020-2025)[5][12]. The shift reflected lessons from Black Thursday: English auctions were slow and keeper capital-intensive, while Dutch auctions enable faster settlement through descending price mechanisms[5][12].

**Critical empirical discovery (Kjaer 2021):** Auction effectiveness dropped from median 97.4% (normal periods) to 76.9% during Black Thursday[3][4]. This wasn't a parameter bug—it was structural: when liquidation demand exceeds keeper capacity and network congestion limits transaction throughput, auctions fail to recover collateral value regardless of mechanism design[3][4][5].

**The fundamental constraint:** Auction effectiveness depends on three things that can't be infinitely expanded[3][4][5][12]:

1. **Keeper liquidity** (finite capital willing to participate)[3][4][12]
2. **Network throughput** (finite transaction capacity)[5][12]
3. **Market liquidity** (finite depth at forced liquidation volumes)[3][4][12]

During crashes, all three constraints bind simultaneously[3][4]. Maker's response was pragmatic: lower liquidation penalties to encourage keeper participation, introduce PSM for instant USDC arbitrage, extend auction durations from 10 min → 6 hours[1][3][4].

**Dai Savings Rate (DSR) — Interest Paid to DAI Holders:** Introduced post-Black Thursday to make holding DAI attractive during peg stress[1][3]. Currently 0-8%, deliberately set below stability fees to maintain deficit neutrality[1][3][10]. 

**Purpose:** when DAI trades above $1, raising DSR incentivizes selling DAI onto the market (increasing supply, driving price down)[1][9][10]. 

**Limitation:** DSR doesn't solve the fundamental problem—it just moves value around[1][2][3]. High DSR means vault owners pay more in fees to compensate DAI holders[9][10].

**When incentives fail: The deleveraging spiral:** Klages-Mundt's analysis formally proves that when collateral returns stop being submartingales (expected to rise or stay constant), the system enters a regime where incentive mechanisms amplify rather than dampen crashes[2][4][5][6]. The mechanism: 
1. Collateral price drops → vaults become unsafe → liquidations triggered; 
2. Keepers bid on auctions, pushing prices lower → realizes larger losses; 
3. Vault owners see losses realized → retreat to safety, stop opening new vaults; 
4. Reduced stablecoin demand + panic selling = DAI premium (trades above $1); 
5. DAI premium paradoxically worsens the spiral: it's a "short squeeze" on vault owners trying to repurchase DAI to close positions[2][3][4][6]; 
6. Higher DAI price makes collateral effectively worth less in stablecoin terms → triggers more liquidations[2][3][4].

This is counterintuitive but mathematically inevitable: **DAI appreciates precisely when collateral crashes, tightening the squeeze on everyone trying to deleverage**[2][3][4][6].

**Quantitative evidence (Black Thursday):**
- ETH crashed 43%, falling from $195 to $110
- DAI *rose* from $0.99 to $1.11
- Auction effectiveness collapsed (76.9% median vs. 97% normal)
- System incurred $4-6M in bad debt in 18 hours[3][4]

This sequence wasn't caused by poor parameter choices—it was the mathematical consequence of the leverage structure meeting a black swan shock in a regime where speculators' collateral returns were no longer submartingales[2][4].

---

### 2.3 Loop 3: Governance — Dynamic Hedging and the MKR Backstop

Governance serves as the dynamic hedge of last resort[1][2][3][4]. When collateral fails (Loop 1) and incentive mechanisms can't recover value (Loop 2), governance deploys MKR as equity to absorb losses[2][3][4].

**Emergency Parameter Adjustment:** Governance can rapidly adjust critical parameters including liquidation ratios (mat), debt ceilings (line), stability fees (duty), and auction parameters (ttl, beg, buf, tail)[1][3][10][11].

**Post-Black Thursday response (March 15-17, 2020 — within 72 hours):[3]**

| Action | Change | Rationale |
|--------|--------|-----------|
| **Stability fee cut**[3][4][7] | 8% → 0.5% | Reduce borrowing cost to discourage new liquidations |
| **Debt ceiling reduction**[3][4] | ~15B DAI → lower per ilk | Prevent new risky lending |
| **GSM delay reduction**[3][4][7] | 24h → 4h | Enable faster emergency responses |
| **USDC-A introduction**[3][4][13] | 0% fee PSM | Provide instant arbitrage channel to stabilize peg |
| **Auction ttl extension**[3][4] | 10 min → 6 hours | Give more time for price discovery |

**Governance process evolution (2024-2025):** MakerDAO implemented Continuous Approval Voting for routine parameter changes (no fixed voting periods)[10][11][14]. Interim Governance Facilitators (IGFs) coordinate proposals and community discussion[10][11][14]. Instant Access Modules enable bounded parameter adjustments without full Executive Voting[10][11]. Executive Votes handle major changes (multi-collateral additions, emergency shutdowns)[11][14]. Total governance polls executed through August 2021: 595[3][10].

**Flap/Flop Auctions:** MKR as Equity:** When system debt (`sin`) exceeds surplus (`joy`) after 6.5-day debt queue[1][3]: 
- **Flop auction:** Mint and sell MKR to raise DAI, covering shortfall[1][3][4]. 
- **Flap auction:** Burn MKR with excess DAI, returning value to holders during surpluses[1][3][15].

This is the ultimate backstop: **MKR is literally Maker's equity**[2][3][4][14]. During Black Thursday, ~4-6M in debt accumulated, requiring ~500k MKR to be minted and sold (~$28M at then-prices), representing ~3% dilution to existing MKR holders[3][4][5].

**MKR token structure changes under Endgame plan:** Under the Endgame plan, MKR's role shifts from absorbing market turbulence to incentivizing SubDAO creators[7][8][14][16]. New structure introduces: 6 independent SubDAOs (each with own governance token), MKR becomes "MakerCore" central reserve token (handles appeals, final authority), SubDAOs manage specialized collateral (e.g., StableNode for yield, OracleNode for price feeds)[7][8][16]. Consequence: MKR holders no longer directly absorb all losses—losses cascade through SubDAO tokens first, potentially converting DAI losses into DAI price impacts rather than MKR dilution[7][8][14][16].

**Governance as crisis manager vs. routine operator:** Governance works well for routine adjustments (fee tweaks, new collateral onboarding)[1][3][10]. But it struggles with crisis response because[2][3][4][10]: 
1. **Time lag:** Governance security module creates 4-48 hour delays[1]. Crashes move faster[3];  
2. **Information asymmetry:** Governance votes on stale data; market moves during voting period[3][4][10]; 
3. **Voter coordination:** MKR holders must coordinate under stress; incentives often misaligned[2][3][4]; 
4. **Limited tools:** Emergency parameter adjustment can't create keeper liquidity or increase network throughput[2][3][4][12].

**The loop coupling problem:** The three loops only balance in narrow operational windows[2]. Expand any single loop and the entire triangle destabilizes[2][3][4]: 
- **Expand Loop 1 (more collateral)** → reduces per-collateral liquidity, slows auctions. 
- **Expand Loop 2 (looser incentives)** → creates moral hazard, encourages overleveraging. 
- **Expand Loop 3 (faster governance)** → centralizes decision-making, reduces credible decentralization[2][3][4].

The system works precisely because it stays tightly balanced—but this balance is inherently fragile[2][3][4].

---

## Part II: Structural Fragility — The Auction-Oracle-Keeper Triad

### 2.4 The Three Bottlenecks

Beneath the Sustainability Triangle lies an operational bottleneck: three linked constraints that fundamentally cannot be circumvented by parameters or governance[3][4][12]. These are not bugs but architectural limits of on-chain liquidation mechanics[3][4].

**1. Auction Throughput: Fixed Capacity, Exponential Demand**

Maker's liquidation pipeline processes auctions sequentially[1][3][4]. During March 12-13, 2020[3][4][5]: - ~4,600 vaults liquidated in 18 hours[3][4]. 
- Median auction duration: ~2 hours[3]. 
- System capacity to process simultaneously: ~10-20 auctions in parallel due to gas limits and blockchain throughput constraints[3][4].

**The cascade effect:** When liquidation demand exceeds processing capacity, auctions fall behind market price[3][4]. Collateral devalues faster than it can be sold[3][4]. Each auction round intensifies the next through reflexive feedback loops[2][3][4][5].

**Quantitative bottleneck:** 
$$
\text{Queue\ depth} = \text{Demand rate} \times \text{Clearing time}
$$

If demand spikes to 1,000 liquidations per hour and each auction clears in 2 hours[3][4]: Queue depth = 1,000 × 2 = 2,000 pending auctions. At median ETH-A price of $150/ETH and typical lot sizes of 50 ETH, that's ~$15M in collateral temporarily locked in non-clearing auctions—exactly when the system needs liquidity most[3][4].

**Maker's parameter-based response:** The `Dog.hole` parameter limits active liquidation debt system-wide (~100M DAI as of 2024)[1][3]. This prevents unlimited auction creation but creates a secondary problem: once `hole` is reached, new liquidations queue without executing[1][3][4]. Vault owners aren't liquidated for hours, meaning their true collateral value isn't discovered until much later[3][4].

**Post-crisis improvements:** Liquidations 2.0 (Dutch auctions via Clipper contract) reduced median liquidation time from ~10 minutes (Flipper) to ~2 hours (Clipper) under normal conditions, but requires more keeper capital per lot[3][4][5][12].

**2. Oracle Delay: The One-Hour Information Asymmetry**

The Oracle Security Module (`OSM`) maintains a **1-hour delay** between real market prices and Vat-accessible prices to give vault owners time to adjust positions[1][3]. This works well during price drift. During crashes, it becomes catastrophic[3][4][5].

**Timeline of information lag during Black Thursday (March 12, 2020):** 
- `10:00 UTC` - Real market ETH price drops to $110[1].
- `10:00-11:00 UTC` - OSM still reporting $195 (stale price from 1 hour prior)[1]. 
- Vaults that would be unsafe at $110 appear safe at $195 → no liquidations triggered → latent bad debt accumulates[1]. 
- `11:00 UTC` - `OSM` finally updates to $110[1]. 
- `11:00-11:30 UTC` - Massive cascade of liquidations all triggered simultaneously ("dam burst" liquidation pattern)[1][4]. 
- `11:30-13:00 UTC` - Network congestion and auction failures compound the problem[1][3][4].

**The mathematical cost:** Klages-Mundt's formal analysis shows that oracle delays interact with leveraged positions to create dangerous non-linearities[2][4][5]. Each hour of delay accumulates latent liquidation demand that explodes when prices finally update[2][4][5].

**Alternative oracle designs considered:** 

| Design | Advantage | Disadvantage |
|--------|-----------|--------------|
| **Current (1h fixed delay)**[1][3][4] | User reaction time | Lag creates cascades |
| **Adaptive delay**[1][12] | Short during volatility | Complexity, gaming risk |
| **Dual feeds** | Redundancy | Coordination problems, higher cost |
| **Chainlink integration**[13] | External security | Introduces trusted third party |

None perfectly solves the fundamental issue: blockchains can't process liquidation volume fast enough when prices move faster than transaction settlement[2][3][4][12].

**2024 status:** Maker explored adaptive OSM delays with volatility detection, but the technical complexity of reliable volatility measurement and gaming prevention prevented mainnet deployment[1][12]. The 1-hour delay remains standard across most collateral types[1][4].

**3. Keeper Liquidity: Conditional Participation Under Stress**

Liquidation auctions only work if keepers have capital and are willing to deploy it[3][4][12]. During panics, both assumptions break[3][4][12].

**Keeper participation collapse during Black Thursday:** - - Gas prices spiked from ~40 Gwei to >400 Gwei (10× increase in cost per transaction)[1]. 
- Many keeper bots had insufficient gas price strategies, couldn't execute transactions[1]. 
- Mempool flooding (extensively analyzed in Kjaer[3]) prevented transaction inclusion[3]. Sophisticated MEV bots paid extreme gas prices, front-running retail keepers[1].
- Result: ~70.5% of auctions failed to fully cover debt[3][4].

**Keeper incentive structure and portfolio optimization:** 

Keepers profit by buying collateral at auction and selling above the clearing price[3]. Their capital allocation decision is a portfolio optimization problem[3][12]:
- Should I deploy capital to Maker auctions or chase yield opportunities elsewhere? 
- During crashes, Maker auctions become riskier (more volatile collateral, uncertain outcomes)[12]. 
- Yield opportunities in other protocols may appear better during stress[12]. 
- If most keepers exit, remaining keepers become the entire system's liquidity source[3][4][12].

**MEV extraction quantification in liquidations:** Recent research quantifies MEV captured during Maker liquidations. Pyth Network published detailed analysis showing keepers extract approximately 5-15% of auction surplus in normal markets through[12][17]: Front-running other bidders (seeing bids in mempool before inclusion)[12][17]. Sandwich attacks (wrapping liquidation call with their own transactions)[12][17]. Time-weighted pricing exploitation[12][17]. During volatility periods, extraction rises to 30-50% as uncertainty creates wider bidding spreads[12][17].

**The cascade mechanism:** When keeper participation drops below critical threshold, auctions clear at 50-70% of market value instead of 95%+[3][4]. This creates realized losses for vault owners and system deficits[3][4]. The deficit then forces governance to dilute MKR, which reduces MKR holders' interest in supporting the system, potentially cascading to reduced governance participation[2][3][4][12].

---

## Part III: Black Thursday — Empirical Validation of Theory

### 2.5 Crisis Sequence and Quantitative Outcomes

**Macro trigger and initial shock:** 
The COVID-19 pandemic triggered systemic panic across all asset classes on March 12-13, 2020[1][5]. The S&P 500 fell approximately 12% on March 9-12, 2020[1]. Equities, commodities, and crypto sold off simultaneously in what economists call a "risk-off" event where all correlations converge to 1[1][5].

**Minute-by-minute crisis timeline (UTC):**

- `Mar 12, 08:00` - Crypto selling begins. ETH trading around ~$195[1][5]
- `Mar 12, 12:00` - Flash crash across all markets. ETH crashes from $195 → $110 (43% drop) in minutes[1][5]
- Mar 12, 12:00-13:00 - Oracle delay period (OSM lag). OSM still reporting ~$195; Maker vaults appear safe[1][4][5]
- `Mar 12, 13:00` - OSM updates; cascade begins. 4,600 liquidations triggered across next 18 hours[4][5]
- `Mar 12-13` - Auction failures & zero-bid phenomenon. ~70% of auctions fail to cover debt[3][4][5]
- `Mar 15-17` - Community emergency response. Fee cuts, USDC-A introduction, major parameter adjustments[5][7]

**Quantitative outcomes documented by Kjaer (2021) and confirmed by Glassnode analysis:**

According to Glassnode analysis, the sell-off of March 12 resulted in $4.5 million of unbacked DAI in the MakerDAO system[1]. Users lost millions as ETH was sold for free through Maker's auctions[1]. Over $8 million worth of ETH was essentially extracted for free through zero-bid exploits[1]. Meanwhile, DAI lost its peg, trading as high as $1.10 (not falling, but rising paradoxically during the crash)[5][7][1].

A class-action lawsuit filed by investor Peter Johnson claimed losses totaling $8.3 million[7]. On March 12, 2020, ETH tanked up to 43% (dropping from $200 to $111), triggering undercollateralized positions across the system[7]. The lawsuit was eventually settled by Maker-related entities for $1.16 million in June 2023, despite Maker Foundation denying any wrongdoing or legal violations[7].

**Metrics comparison (Kjaer 2021):**

| Metric | Normal Period | Black Thursday | Recovery | Reference |
|--------|--------------|-----------------|-----------|-----------|
| Auction effectiveness (median) | 97.4% | 76.9% | 97%+ | [3][4] |
| Liquidation delay (median) | 0.2 min | 2.6 min | 0.2 min | [3][4] |
| DAI price | $0.99-$1.01 | $1.11 peak | $1.00-$1.01 | [1][4][5] |
| System bad debt (sin) | Near-zero | $4-6M | Recovered | [3][4][5] |
| MKR dilution required | ~0% | ~3% of supply | Permanent | [3][4] |

**Zero-bid phenomenon: The mempool attack:** Approximately 10-15% of Black Thursday liquidations cleared with bids of essentially $0 per ETH—bidders were literally getting free collateral[1][3]. Forensic analysis by Kjaer revealed[3][4]: 
1. Attackers flooded the Ethereum mempool with low-gas-price transactions[1][3]. 
2. Auction keeper bots, blinded by distorted gas price oracles, sent transactions with insufficient gas fees[1][3]. 
3. These keeper transactions never mined; nonce gaps prevented later retries[1][3]. 
4. Attackers' high-gas transactions got included in blocks, allowing them to purchase ETH at zero prices[1][3]. 
5. Attacker profit: ~$8M recovered from effectively stealing collateral[1][3].

This wasn't a smart contract bug—it was a layer-1 (mempool/consensus) attack enabled by Maker's tight auction parameters (10-minute duration meant no time for transaction retry or recovery) combined with network congestion[3][4][12].

**Recovery dynamics post-March 13:** Governance response was impressively fast (72 hours for major parameter changes), setting a precedent for decentralized crisis management[5][7]. By March 17, USDC-A introduction created an instant arbitrage channel for peg recovery[4][7][13]. The Peg Stability Module enabled[4][7][13]: 
- Arbitrageurs to mint DAI by depositing USDC (since PSM charged near-zero fees)[13]. 
- DAI supply increased, driving price back toward $1.
- System bad debt was eventually recovered through Flop auctions (MKR dilution)[3][4][7].

By May 2020, the system had fully absorbed the Black Thursday loss[3][4]. The permanent cost: ~500k MKR minted and sold, representing ~3% dilution to existing MKR holders[3][4].

---

## Part IV: Formal Stability Analysis — Regime Boundaries
Klages-Mundt's mathematical framework provides rigorous characterization of when stablecoins transition from stable to unstable

### 2.6 The Stable and Unstable Domains

**Core insight:** Stablecoin stability is not a continuous property—it exists in distinct regimes separated by critical thresholds[2][4][5][6].

**Stable Domain Characterization:** In the stable domain, small price deviations decay (prices are mean-reverting)[2][4][5]. Mathematically[2][4]: $dZ_t$ = positive drift + bounded variance. Where $Z_t$ = stablecoin price process[2][4].

**Key results (Klages-Mundt Theorems 2.2, 2.3):**

Theorem 2.2 (Doob's Inequality): 
$$
P(\max_{n \leq T_m} Z_n \geq m) \leq \frac{2(1-\alpha)(m-1)}{r}
$$

For concrete example: With \($\alpha$ = 0.9999\) (99.99% chance collateral doesn't crash below critical threshold), $(r = 1.0011)$ (annualized return bound), probability of 10-cent deviation from $1 peg is ~4.2%[2][4][5].

Theorem 2.3 (Quadratic Variation Bound): 
$$
P(\langle Z \rangle_{T_m} \geq 0.1) \leq \frac{6(1-\alpha)(m-1)}{r}
$$

Bounds variance of price process[2][4]. In stable domain, this is tightly bounded (~12.7% probability of exceeding 0.1 variance for typical parameters)[2][4][5].

**Interpretation:** In stable domain, stablecoin prices cluster tightly around $1, variance is bounded, large deviations are rare[2][4][5]. This matches observed Maker behavior for 99% of its operational history[3][4][5].

### 2.7 The Unstable Domain: Deleveraging Spirals

**Unstable Domain Characterization:** Outside stable barriers, collateral return expectations shift from submartingale $(E[X_{t+1}|F_t] ≥ X_t)$ to supermartingale $(E[X_{t+1}|F_t] ≤ X_t)$[2][4].[2][4][5][6].

**Key result (Klages-Mundt Theorem 2.4):**

Theorem 2.4 (Deflationary Regime): When crossing critical leverage threshold, the stablecoin price process itself becomes a **submartingale**: $Z_t \text{ becomes } E[Z_{t+1} | F_t] \geq Z_t$[2][4]

**This is catastrophic:** It means the stablecoin price tends to *increase* even as collateral crashes—exactly what happened on Black Thursday when DAI rose to $1.11 while ETH fell to $110[1][3][4][5].

**Mathematical mechanism:** 
1.Collateral price falls below expected return threshold
2. Vault owners attempt to deleverage (reduce positions, repurchase debt);
3. Deleveraging creates demand for stablecoin (everyone needs DAI to repay); 
4. Stablecoin supply initially contracts (less new debt minted); 
5. Result: stablecoin appreciates despite collateral crash (short squeeze dynamic); 
6. Appreciation makes deleveraging more expensive (need more collateral to repurchase DAI); 
7. Feedback loop: more liquidations → higher DAI price → more liquidations[2][4][5][6].

**Critical leverage threshold:** 
Monte Carlo simulations in Klages-Mundt show regime transition occurs around[2][4][5][6]: Collateral leverage ratio ~ 50-60%. Or equivalently, liquidation ratio requirements of 150-200% (which Maker uses)[2][4][5][6].

**Pre-conditions for instability (all must occur simultaneously):** 
1. **Negative collateral drift:** E[ETH_{t+1}] < ETH_t (expected to fall, not rise); 
2. **High correlation with stablecoin demand:** Collateral crashes when everyone needs liquidity most; 
3. **Constrained demand elasticity:** Can't instantly increase stablecoin supply to dampen price rise; 
4. **Limited keeper participation:** Can't absorb liquidation volume[2][3][4][5][6]

All four occurred on March 12[1][3][4][5]: ETH was negative drift (crypto correlation event), correlated with all leverage unwinding (everyone liquidating simultaneously), PSM didn't exist yet (no alternate supply source)[1][4][13], and keepers were overwhelmed[1][3][12].

---
## Part V: Operational Resilience Metrics

Kjaer's quantitative framework provides measurable indicators of when systems approach instability[3]. These allow practitioners to monitor leading indicators before crises occur.

### 2.9 Empirical Metrics and Thresholds

**Metric 1: Auction Effectiveness (M6)**

$$
AE_a = \frac{\text{DAI recovered}}{\text{ETH sold} \times \text{Market price at auction end}}
$$

**Interpretation:** Ratio of realized price to market price. Ideal: 100% (collateral sold at fair value).

**Observed values:**[3]
- Normal periods: 97.4% median (IQR ~4.7%)
- Black Thursday: 76.9% median (Q1 near 0%, indicating many zero-bid auctions)
- Post-crisis (2024): 98%+ (auctions working reliably)

**Threshold for concern:** When median falls below 90%, system is in stress. Below 80%, crisis phase[3][4].

**Metric 2: Liquidation Delay (M7)**

$$
\text{Delay} = t_{\text{liquidation}} - t_{\text{breach of CR ratio}}
$$

Time between vault becoming unsafe and actual liquidation occurring[3].

**Observed values:**[3]
- Normal periods: 0.2 min median (1 block); 1.7 min average
- Black Thursday: 2.6 min median; 9.3 min average
- Maximum (outlier): 57 min (network congestion)

**Interpretation:** Longer delays accumulate unliquidated bad debt. Ideally < 1 minute; concerning if > 5 min for extended periods[3].

**Metric 3: Vault Management Agility (M8)**

$$
\text{Agility} = \frac{\text{DAI saved before liquidation}}{\text{DAI saved} + \text{DAI liquidated}}
$$

Fraction of at-risk debt that vault owners rescue versus gets liquidated[3].

**Observed values:**[3]
- Before Black Thursday: 58.8%
- During Black Thursday: 54.3% (slight decline, but surprisingly stable)
- After Black Thursday: 89% (users learned to manage positions more actively)

**Interpretation:** Higher agility indicates more sophisticated vault management (bots vs. manual). Agility > 80% suggests market professionalization[3].

**Metric 4: Collateralization Distribution**

Not a single number but a histogram of all vaults by collateral ratio. Kjaer observed:

- **Pre-BT:** Vaults clustered 200-400% ratio (conservative)
- **Post-BT:** Shift toward 150-200% ratio (tighter, accepting more risk but reflecting learned confidence)
- **Concerning sign:** If substantial DAI debt held at <150% (unsafe zone), system is close to cascade[3]

**Metric 5: System Surplus/Deficit Tracking (`M_sin/M_joy`)**

$$
\text{MKR dilution risk} = \frac{\sin - \text{hump}}{\text{MKR price} \times \text{MKR supply}}
$$

Approximates how much MKR would need to be minted to cover deficits[3].

**Observed values:**[3]
- Normal periods: sin near 0
- Black Thursday peak: ~$6M (0.1% of DAI supply, but still significant)
- Recovery: took 6.5-day debt queue + 2-3 Flop auctions to fully absorb[3]

---

## Part V: Economics — Revenue Models and State Transitions
Maker's financial model is fundamentally state-dependent, shifting between regimes[1][3][4].

### 2.8 Normal-Regime Economics: Fee-Based Sustainability

1. **Revenue sources:** Stability fees - Vault borrowers pay interest (0-12% annual depending on collateral type)[9][10][11]. 
2. **Liquidation penalties: **- 13% added to debt during liquidations, flows to system surplus[1][3]. 
3. **PSM fees:** - Near-zero now (~0.1%), reduced from initial 0.5% to encourage usage[13]. RWA yield - Revenue from lending against real-world assets (T-bills, sustainable assets)[8][9][18].

**Value flow:** 

Surplus accumulates from fees → exceeds "hump" threshold (~2M DAI) → triggers Flapper auction → MKR burned using excess DAI → MKR supply falls → remaining holders' equity increases[1][15].

**Example: Normal period economics (2020-2021):** 
- **Monthly stability fee income:** ~$5-10M. 
- **Monthly liquidation penalties:** ~$1-2M. 
- **Monthly DSR cost:** ~$2-5M. 
- **Monthly RWA yield:** ~$0.5-2M[9][10][18]. 
- **Monthly net:** +$2-5M accumulation to system surplus. 

Over 12 months: ~$30-60M, funding MKR buybacks and offsetting small liquidation shortfalls[3][10][11].

**Sustainability check:** Is fee income sufficient to cover operational costs? 
- Governance infrastructure, security audits: ~$10-20M annually[10][11]. 
- Risk buffer for small liquidation shortfalls: ~$20-40M in reserves[3][10]. 
- **Requirement:** ~$30-60M annual surplus generation. 

During normal markets, this is achievable[10][11][14]. Fee rates are set such that vault owners pay enough to cover both compensation to DAI savers (DSR) and system reserves[1][9][10][14].

### 2.9 Crisis-Regime Economics: When Defaults Dominate

During extreme stress, revenue flows completely invert[2][3][4][10].

**Black Thursday economics (March 12-13, 2020):**

| Item | Amount | Effect | Reference |
|------|--------|--------|-----------|
| Liquidations triggered | 4,600 vaults | Generates short-term fee income | [3][4] |
| Auctions failed to clear debt | 1,265 auctions (29.6%) | Generates bad debt instead | [3][4] |
| Realized loss per failed auction | ~$1,000-5,000 | Multiplied across all failures | [3][4] |
| Total system deficit | ~$4-6M DAI | Accumulates in Vow.sin | [3][4][5] |
| Stability fee income that day | ~$20k | Negligible compared to losses | [3][4] |
| Liquidation penalties collected | ~$100-200k | Covers only ~5% of deficit | [3][4] |

**Conclusion:** Fee income becomes irrelevant[2][3][4]. System enters loss-absorption mode[2][3][4][5].

**Recovery mechanism (Flop auctions):** 

To cover ~$4.6M deficit with acceptable MKR dilution, system needs: 

$\text{MKR minted} \approx \frac{\text{Deficit}}{MKR\ price}$[3][4]. 

At ~$11 USD/MKR price (March 2020), this meant ~420k MKR to mint and sell[3][4]. At then-market cap of ~$40B, this represented ~1% dilution to existing holders—effectively paying MKR holders for absorbing the loss through equity absorption[3][4][15].

**The uncomfortable asymmetry:** 
- **Vault owners** absorb collateral loss capped at their investment. 
- **DAI holders** remain whole (full 1:1 redemption backed by remaining collateral). 
- **MKR holders** absorb unlimited tail risk through dilution[2][3][4][14].

This is the intended capital structure—MKR is equity, absorbs losses—but it creates a finite tolerance for repeated shocks[2][3][4]. Too many Black Thursdays and MKR holders may exit entirely, potentially cascading into governance failure[2][3][4].

### 2.10 PSM Impact: Trading Sustainability for Short-term Stability

The Peg Stability Module fundamentally altered economics by introducing instant USDC↔DAI swaps at 1:1 ratio[1][13].

**Economic trade-offs:**

| Aspect | Pre-PSM | Post-PSM | Reference |
|--------|---------|----------|-----------|
| Peg stability | Volatile (±5% swings) | Tight (±0.5% typical) | [1][13] |
| Revenue model | Fees from 100% vault-backed DAI | Fees from ~60-70% of DAI supply | [1][13][9] |
| Keeper dependence | High (auction revenue critical) | Medium (PSM provides buffer) | [1][13][12] |
| Decentralization | High (crypto backing) | Medium (USDC dependency) | [1][13] |
| Counterparty risk | Collateral counterparties only | Collateral + Circle (USDC issuer) | [1][13] |

**PSM's revenue cost:** 
A vault backing via PSM generates ~0% protocol revenue (0.1% fee charged once on entry)[1][13]. A vault backing via crypto generates ~2-5% annual revenue (stability fees compounded across vault lifetime)[1][9][10][15].

If 40% of DAI is now PSM-backed (up from 0%)[1][13]: Lost annual revenue: 40% × 3% (midpoint) = 1.2% of DAI supply in fees = ~$50M annually (at $4B DAI supply) that cannot be captured[13][9][10].

This is the explicit trade-off: **short-term peg stability (PSM helps instantly) costs long-term sustainability (reduced surplus generation)**[1][2][13][9][10].

**2024 PSM evolution:** LitePSM design reduces gas costs and enables integration with Endgame collateral segmentation[13]. Governance voted to explore permissioned yield-bearing PSMs—for example, PSM depositing USDC to Aave to generate additional yield while maintaining instant redemption[13][18].

---
# Part VII: Paths Forward — Rebalancing the Triangle

The post-Black Thursday period spawned multiple initiatives to strengthen the Sustainability Triangle[1][3]. None solves all problems; each trades off different dimensions of safety/decentralization/efficiency.

### 2.13 Collateral Diversification: Real-World Assets

**Goal:** Reduce crypto correlation by onboarding non-correlated collateral[1][3].

**Collateral types being added:**
- **U.S. Treasuries (tokenized):** 0% volatility, AAA credit, but regulatory complexity
- **Corporate bonds:** Low volatility, rated credit, but liquid callable risk
- **Real estate:** Illiquid, long-term returns, but appraisal/custody complexity
- **Streaming payments:** Revenue-backed, non-volatile, but operational complexity

**Benefits:**
- During crypto crashes, RWA backing remains stable
- Can absorb larger shocks without triggering cascading liquidations
- Enables higher PSM leverage without increasing crypto risk concentration

**Costs:**
- Introduces legal/regulatory dependencies (lawyers, custody providers, regulators)
- Reduces collateral liquidity (can't auction RWA as instantly as crypto)
- Increases governance overhead (must evaluate counterparty creditworthiness continuously)

**Current state (2024-2025):** ~5-10% of DAI backed by RWA; growth trajectory targeting 15-20% by 2026[1].

---

### 2.14 Automated Auction Tuning

**Goal:** Remove governance lag by automating parameter adjustments[1][3].

**Parameters that could be automated:**
- **`TTL` (auction duration):** Extend when bid volume drops, shorten when bids are quick
- **`BEG` (bid increment):** Loosen when keeper participation drops, tighten when abundant
- **`BUF` (auction starting buffer):** Adjust based on recent collateral volatility
- **`TAIL` (maximum duration):** Adapt to network throughput (gas costs)

**Mechanism:** On-chain oracle monitoring of auction performance feeds back to automatic parameter adjustments via predetermined rules (no governance needed for small tweaks)[1][3].

**Benefits:**
- Eliminates governance delay during crisis
- Parameters continuously tune to market conditions
- Reduces need for reactive emergency votes

**Challenges:**
- Algorithm design: What rules prevent gaming? How to avoid unintended cascades?
- Safety: Automated systems can amplify errors if badly designed
- Trust: Some MKR holders may view algorithmic governance as reducing democratic control

**Status:** Experimental proposals; not yet implemented on mainnet[1][3].

---

### 2.15 Governance Improvements: Speed and Responsiveness

**Current challenge:** 48-hour GSM delay + voting periods mean governance can't respond to black swan events[3].

**Proposed improvements:**

1. **Delegated authority within bounds**
   - Pre-authorize Interim Governance Facilitators (IGFs) to adjust parameters within preset ranges (e.g., ±2% on mat, ±0.5% on duty)
   - Removes voting delay for small adjustments
   - Maintains governance control for large changes

2. **DSR smoothing**
   - Replace step-function DSR changes with gradual adjustments over hours/days
   - Prevents whipsaw effects on DAI holders
   - Gives market time to react

3. **Emergency pause mechanism**
   - Ability to freeze vault creation temporarily during crisis
   - Pause new liquidations to prevent cascade-on-cascade
   - Requires consensus (doesn't centralize power)

**Trade-off:** Delegated authority concentrates power in IGFs, reducing credible decentralization. But it enables faster crisis response[3].

**Status:** Partially implemented; IGF roles established in 2019; bounds on delegated authority remain debated[3].

---

## Conclusion: Sustainability as Continuous Rebalancing

The Sustainability Triangle is not a fixed structure—it's a dynamic balance that requires constant retuning and vigilant monitoring[1][2][3][4][10][11][15]. Black Thursday proved that static systems fail under stress; DAI survives because Maker's community continuously adjusts the triangle's three axes[2][3][4][10][11][14][15].

**Key insights:**

**1. Backing ≠ Sustainability** - On-chain invariants (Part I) guarantee arithmetical backing, not economic sustainability[1][2][3][4]. DAI can be mathematically backed yet economically unsustainable if market microstructure fails[2][3][4][5].

**2. Regime transitions are real and dangerous** - Klages-Mundt's formal analysis proves stable and unstable domains exist, separated by critical thresholds[2][4][5]. Below those thresholds, incentive mechanisms fail and governance must absorb losses[2][3][4][5].

**3. The three loops must balance** - Risky collateral forces tight incentives and responsive governance[2][3][4]. Diversified collateral allows loose incentives and slower governance[2][3][4]. Imbalance triggers cascades[2][3][4].

**4. Keeper liquidity is the ultimate constraint** - No parameter adjustment, oracle design, or governance hack can force keepers to participate[3][4][12]. The system depends on their voluntary capital deployment during maximum stress[3][4][12].

**5. MKR holders are the equity** - In tail events, MKR absorbs losses through dilution[2][3][4][14][15]. This is intentional, but it creates finite tolerance for repeated shocks[2][3][4][14][15]. Too many Black Thursdays and MKR holders may exit entirely, potentially cascading into governance failure[2][3][4].

**Path forward:** The Endgame plan attempts to solve sustainability through[7][8][18][19]: Diversifying collateral to widen the stability region[7][8][18]. Introducing PSM for instant arbitrage[1][13]. Fragmenting governance into SubDAOs to distribute risk[7][8][16]. Making MKR a "central reserve currency" rather than individual protocol token[7][8][16].

This trades decentralization for scalability and resilience[7][8][16]. Whether it succeeds depends on execution and market adoption[7][8][18][19].

**For Part III** (Governance, to be written): The question becomes—when MKR becomes system-critical infrastructure, how does governance remain credibly neutral and resistant to capture while maintaining the dynamic responsiveness needed in crisis?[2][3][4][14]

---

## References

[1] Glassnode Insights. (2021). "What Really Happened To MakerDAO?" April 12, 2021. https://insights.glassnode.com/what-really-happened-to-makerdao/

[2] Klages-Mundt, A., & Minca, A. (2022). "While Stability Lasts: A Stochastic Model of Noncustodial Stablecoins." Management Science. https://pubsonline.informs.org/doi/abs/10.1287/mnsc.2022.4565

[3] Kjaer, M. (2021). Quantitative Analysis of MakerDAO's Liquidation System. Diploma Thesis, TU Wien.

[4] Klages-Mundt, A. (2023). Stablecoin Risk Models. PhD Dissertation, Cornell University.

[5] MixBytes. (2025). "How Liquidations Work in DeFi: A Deep Dive." https://mixbytes.io/blog/how-liquidations-work-in-defi-a-deep-dive

[6] CoinTelegraph. (2020). "MakerDAO Takes New Measures to Prevent Another 'Black Swan' Collapse." May 3, 2020. https://cointelegraph.com/news/makerdao-takes-new-measures-to-prevent-another-black-swan-collapse

[7] Blockworks. (2023). "Maker firm settles for $1.16M with users liquidated in Covid crash." June 22, 2023. https://blockworks.co/news/maker-settle-black-thursday

[8] BuildBlockchain. (2020). "How MakerDAO Survived Black Thursday — Issue No. 88." April 5, 2020. https://www.buildblockchain.tech/newsletter/issues/no-88-how-makerdao-survived-black-thursday

[9] BlockApps. (2024). "Understanding the DAI Liquidation Process: Steps, Risks and Strategies to Avoid Liquidation." December 25, 2024. https://blockapps.net/blog/understanding-the-dai-liquidation-process-steps-risks-and-strategies-to-avoid-liquidation/

[10] BlockApps. (2024). "Understanding the MakerDAO Governance Process for Stablecoins: Insights and Mechanisms." https://blockapps.net/blog/understanding-the-makerdao-governance-process-for-stablecoins-insights-and-mechanisms/

[11] BlockNews. (2024). "MakerDAO Implements Fee Changes to Support Dai Stability Amid Market Shifts." https://blocknews.com/makerdao-implements-fee-changes-to-support-dai-stability-amid-market-shifts/

[12] Pyth Network. (2025). "Beyond the Dark Forest: Experiments in Mitigating MEV." https://www.pyth.network/blog/beyond-the-dark-forest-experiments-in-mitigating-mev

[13] Mirror (Dewiz). (2024). "Exploring MakerDAO's PSM and the Advent of LitePSM." https://mirror.xyz/dewiz.xyz/cs-D34NCp2JK9oMs61oKV-YLbSXTsZyxjxt4l_hZW6c

[14] Gate.io. (2024). "MakerDAO, The Central Bank of Cryptocurrency." https://www.gate.com/learn/articles/maker-dao-the-central-bank-of-cryptocurrency/4254

[15] MakerDAO. (2017). "The Dai Stablecoin System Whitepaper." https://makerdao.com/whitepaper/DaiDec17WP.pdf

[16] Gate.io. (2023). "The MakerDAO Endgame Plan." https://www.gate.io/learn/articles/the-makerdao-endgame-plan/513

[17] Wu, F., Thiery, T., Leonardos, S., & Ventre, C. (2024). "From Competition to Centralization: The Oligopoly in Ethereum Block Building Auctions." arXiv:2412.18074. https://arxiv.org/abs/2412.18074

[18] Research Despread. (2024). "Endgame Series Part 1: The Introduction and Impact of MetaDAO." https://research.despread.io/endgame-series-1/

[19] Endgame Documentation. (2025). "Collateral Breakdown." https://endgame.makerdao.com/concepts/collateral-breakdown

---

**Series Navigation:**
- ← Previous: Part I (Backing Mechanism)
- **You are here: Part II (Sustainability)**
- → Coming: Part III (Governance Evolution)
