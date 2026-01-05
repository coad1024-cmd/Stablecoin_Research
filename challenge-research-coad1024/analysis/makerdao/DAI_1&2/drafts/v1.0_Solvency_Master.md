# DAI at the Crossroads, Part I: Where Maker's Solvency Lives On-Chain (and Where It Doesn't)

**A three-part technical series unpacking Maker's architecture — from its on-chain reserves to its evolving sustainability model and the governance layer that now defines its credibility.**

> **Target audience:** senior Solidity devs, protocol engineers, DeFi risk teams.

---

## Cross-Article Continuity

**Shared definitions and invariants used across Parts I, II, and III:**

| **Term** | **Definition** | **Used In** |
|----------|---------------|-------------|
| `ink` | Collateral locked in vault (wei units) | I, II |
| `art` | Normalized debt (internal DAI units) | I, II |
| `rate` | Cumulative stability fee multiplier | I, II |
| `mat` | Liquidation ratio per collateral type | I, II |
| `spot` | Oracle price adjusted for liquidation ratio: `spot = price / mat` | I, II |
| **Core invariant** | `ink × spot ≥ art × rate` (vault safety condition) | I, II |
| **Black Thursday** | March 12-13, 2020 ETH crash and liquidation cascade | I (brief), II (detailed) |
| **PSM** | Peg Stability Module enabling 1:1 USDC↔DAI swaps | I (mechanism), II (economics) |
| **Global Settlement** | Emergency shutdown enabling DAI redemption for collateral | I (mechanics), II (implications) |
| **MKR dilution** | Minting/selling MKR to cover bad debt via Flop auctions | I (process), II (sustainability) |

---

## Introduction

DAI remains one of the largest dollar-pegged tokens in crypto that isn't issued by a bank or fintech[5]. Its reserve lives entirely on-chain, enforced by collateral and arithmetic rather than balance-sheet trust. Yet over the past few years, that arithmetic has been bent—and then formalized—by pragmatism[3]. What began as emergency patches after Black Thursday has evolved into a permanent blueprint: **Sky Ecosystem's (formerly MakerDAO) Endgame plan**[8][9][10].

Vaults gave way to the Peg Stability Module (PSM), ETH to USDC, and the once-pure crypto-collateral model to a hybrid of smart contracts, custodial reserves, and real-world assets (RWA)[3][5][8]. Endgame—now in Phase 1 since summer 2024—doesn't hide this trade-off—it institutionalizes it, treating hybridization as the only scalable path to sustainability[8][9][27]. The protocol restructures into specialized SubDAOs, each with autonomous governance tokens, while MKR becomes a "central bank" asset backing DAI (transitioning to SKY token in 2025)[11][26][33].

The result is a protocol that's still mathematically elegant but philosophically split: crypto-native in logic, hybrid in balance sheet. The invariants inside the `Vat` still guarantee solvency, yet the meaning of "backed" has drifted[3]. Where it once meant over-collateralized ETH, it now includes treasuries, legal wrappers, and off-chain credit—each introducing latency and trust into a system designed to remove both.

This series traces that evolution through three layers:

1. **Backing** (Part I) — How Sky's on-chain balance sheet actually works
2. **Sustainability** (Part II) — When deterministic math stops guaranteeing solvency  
3. **Governance** (Part III) — The coordination layer that ultimately holds the peg together

Rather than rely on narratives or governance rhetoric, each part focuses on the mechanics that decide whether DAI remains solvent, stable, and credibly neutral—by math, by market, and by mandate.

---

## Part I: How DAI Is Really Backed

### 1.1 The Endgame Pivot: Hybrid Backing

Sky Ecosystem's (formerly MakerDAO) Endgame—now in Phase 1 since summer 2024—is the architecture that redefines what Sky means by "backing"[8][9][27]. When you read the contracts now, you see the same `Vat`, `Join`, and `Dog` structures[5]. When you read the balance sheet, you see new rows: tokenized treasuries, custodial USD rails, and real-world revenue streams[8][20].

That change matters because it changes the operational assumptions we can reasonably make when markets break. Endgame turned Sky from a single-domain system (pure crypto in, DAI out) into a layered balance sheet across SubDAOs[3]. ETH, WBTC, and other volatile assets still make up the decentralized core, but they're now surrounded by stability buffers like USDC (via PSM), tokenized treasuries, and RWA vaults in Grove SubDAO[8][17][27]. As of October 2025, ~38% crypto-native, 22% PSM stablecoins, and 14% RWA backing reflect this hybrid maturity, with RWA collateral at $948M generating significant yields to fund surplus and SKY buybacks[4][24].

**The catalyst: Black Thursday**

That shift came from hard lessons. On March 12, 2020, ETH crashed approximately 43% in hours, falling from ~$195 to ~$110[5][6][16]. The system couldn't liquidate fast enough, leaving a $4-6 million deficit[5][16]. The response was pragmatic: if DAI can be backed partly by assets that don't crash with crypto, the peg survives shocks better[5][16].

So Sky started blending in stable, low-volatility collateral[8][17]. It worked—volatility risk dropped—but the trade-off was obvious. Sky gained a safer balance sheet and lost a bit of its permissionless purity[8][17]. Today, part of the backing sits on-chain, trustless and programmable. The rest exists off-chain, wrapped in legal contracts and custodial trust[3][8]. The smart contracts still enforce the accounting, but enforcing *value* for those off-chain assets requires lawyers and intermediaries, not keepers and liquidators[3].

Post-rebrand, USDS (DAI's yield-bearing upgrade, launched 2024) now offers yields from RWA flows, blending stability with real returns[29].

**This is the quiet truth of Endgame:** the `Vat` still adds up, but what it measures now includes assets that don't live entirely in the EVM[3][8]. Endgame didn't rewrite Sky's contracts—it rewrote what those contracts represent[3]. "Backed" still means the books balance, but part of that balance now depends on people, institutions, and off-chain law.

---

### 1.2 Core Architecture: The Vat as Ledger

DAI isn't minted out of thin air—every unit originates inside a vault that locks collateral via a `Join` adapter and tracks debt through the `Vat`[5]. Collateral moves into the system using adapter contracts (`Join`s), and price data comes through the `Spotter`, which pulls from the Oracle Security Module (OSM)[5]. When a vault becomes unsafe, the `Dog` (liquidation module) coordinates the liquidation process and hands the position off to an auction contract (`Clipper`), which Keepers compete to buy[5].

**Core contract interfaces:**

```solidity
interface IVat {
    function frob(bytes32 ilk, address urn, address usr, int256 dink, int256 dart) external; // adjust ink/art
    function grab(bytes32 ilk, address urn, address usr, address guy, int256 dink, int256 dart) external; // liquidation move
    function move(address src, address dst, uint256 wad) external; // transfer DAI balance
}
```

The `Vat` is the single source of truth—it stores collateral balances (`gem`, `ink`), normalized debt (`art`), surplus (`joy`), and system debt (`sin`)[5]. Keeping `Vat` small and correct is crucial to guaranteeing on-chain backing.

**Key state variables tracked by Vat:**[5]

| Variable | Meaning | Units | Example |
|----------|---------|-------|---------|
| `gem` | Unlocked collateral (deposited but not in vault) | Token wei | 50 ETH |
| `ink` | Collateral locked in vault | Token wei | 10 ETH |
| `art` | Normalized debt (debt units before rate applied) | Internal units | 1000 units |
| `rate` | Cumulative stability-fee multiplier | Ray (10^27 precision) | 1.035 × 10^27 |
| `mat` | Liquidation ratio per `ilk` (collateral type) | Ray | 1.5 × 10^27 (150%) |
| `spot` | Liquidation price in DAI: `spot = price / mat` | Ray | 2000 DAI/ETH |

**Debt isn't stored directly—it's computed as:** `debt = art × rate`[5].

This keeps gas costs low and makes debt accrual deterministic, but it also means solvency depends on arithmetic precision, oracle freshness, and timing[5][6]. If `ink × price` falls below `art × rate × mat`, the vault is unsafe and must be liquidated[5].

---

### 1.3 Collateral Types and Vault Lifecycle

Sky supports multiple collateral types (`ilks`), each with distinct risk parameters[5]. As of October 2025, crypto-native assets dominate at 38%, with RWA at 14% providing uncorrelated buffers via Grove[4][24].

**Representative collateral profiles (2025):**[5][4]

| Collateral Type | SubDAO | Liquidation Ratio (`mat`) | Stability Fee | Debt Ceiling (`line`) | Risk Profile |
|-----------------|--------|---------------------------|---------------|----------------------|--------------|
| ETH-A | Core | 150% | 0.5-3% (variable) | ~20B USDS | High volatility, crypto-correlated |
| WBTC-A | Core | 150% | 4-6% | ~2B USDS | High volatility, crypto-correlated |
| USDC-A (PSM) | Spark | 101% | 0-0.1% | ~15B USDS | Low volatility, centralized (Circle) |
| RWA (T-bills, bonds) | Grove | 100-102% | 2-5% | ~1B USDS (948M active) | Off-chain, legal-wrapped, 14% total exposure |

**Vault State Machine:**[5]

The lifecycle of a vault involves discrete state transitions mediated by contract calls:

1. **Creation & Collateral Deposit**  
   User calls `GemJoin.join(address urn, uint256 wad)` to deposit collateral → Updates `Vat.gem[ilk][usr]` (unlocked collateral balance)[5]

2. **Vault Position Adjustment**  
   User calls `Vat.frob(ilk, urn, usr, dink, dart)` where:
   - `dink` > 0: locks more collateral (`gem` → `ink`)
   - `dart` > 0: mints more DAI (increases normalized debt `art`)
   - Negative values reverse these operations[5]

3. **DAI Withdrawal**  
   User calls `DaiJoin.exit(address usr, uint256 wad)` → Converts internal DAI balance to ERC-20 DAI token[5]

4. **Liquidation (if unsafe)**  
   Keeper calls `Dog.bark(ilk, urn, kpr)` → Triggers `Vat.grab()` to confiscate collateral → Initiates `Clipper` auction[5]

5. **Closure**  
   User repays debt via `frob` (dart < 0), unlocks collateral (dink < 0), and exits via `GemJoin.exit()`[5]

**Practical Example: ETH-A Vault Creation**

```solidity
// 1. User deposits 10 ETH
GemJoin_ETH.join(userAddress, 10 ether);
// Vat.gem[ETH-A][user] = 10 ETH

// 2. User locks 10 ETH and mints 5000 DAI (art = 5000 units, assuming rate ≈ 1.0)
Vat.frob(ETH-A, userUrn, userAddress, 10 ether, 5000 ether);
// Vat.ink[ETH-A][userUrn] = 10 ETH
// Vat.art[ETH-A][userUrn] = 5000 units
// Collateral ratio: (10 ETH × $2000) / (5000 DAI) = 400% ✓

// 3. User withdraws 5000 DAI as ERC-20
DaiJoin.exit(userAddress, 5000 ether);
```

This multi-collateral reality enables Sky to balance decentralization (crypto assets) with stability (stablecoins, RWA)[5][8]. However, each collateral type introduces distinct failure modes analyzed in Part II.

---

### 1.4 Canonical Invariants: The Assumptions Behind Solvency

Sky enforces solvency through deterministic on-chain invariants—equations that must always hold true for the system to remain solvent[3][5]. These arithmetic guarantees define what "backed" means on-chain, but they only translate to real stability while the economic environment behaves within certain bounds[6].

**Vault-Level Invariant:**

\[
ink \times spot \geq art \times rate
\]

Where `spot = price / mat` is the oracle price adjusted for liquidation ratio[5].

**Interpretation:** Each vault must maintain collateral value above its debt × liquidation ratio. If this fails, the vault becomes unsafe and triggers liquidation[5].

**System-Level Invariant:**

\[
\sum_{ilks} (art_i \times rate_i) = \text{Vat.debt}
\]

Ensures all DAI supply maps back to outstanding debt[5]. But the invariant doesn't guarantee *collectability*—during stress, auctions can clear far below oracle values[5][6]. The books remain arithmetically correct, but the system records a deficit (`sin`) as realized collateral falls short[5].

**Surplus-Deficit Balance:**

\[
\text{Vow.joy} - \text{Vow.sin} \geq 0
\]

Surplus fees (`joy`) offset deficit (`sin`) until `joy < sin`, at which point SKY dilution (legacy MKR) becomes the recapitalization path[5]. This is formalized through the `Vow` contract:

```solidity
// Vow reconciliation logic
if (joy > sin + hump) {
    Flapper.kick();  // Burn SKY with surplus DAI
} else if (sin > joy + sump) {
    Flopper.kick();  // Mint/sell SKY to cover deficit
}
```

**The hidden assumption:** These relationships hold *perfectly* inside their stable domain—when collateral returns behave as submartingales (i.e., expected to rise or stay constant)[6]. In that regime, the system remains solvent in expectation. But once collateral returns turn supermartingale (expected to fall), even flawless liquidation logic can't maintain 1:1 redemption[6].

**Klages-Mundt's formal framework demonstrates:** There exists a critical leverage threshold (\(\beta^{-1}\)) where the system transitions from stable to unstable regimes[21]. Below this threshold, price self-corrects through arbitrage. Beyond it, liquidations become self-reinforcing—the stablecoin price rises (making collateral effectively worth less in stablecoin terms) precisely when users need to buy it back to close positions, accelerating further liquidations[21].

The `Vat` continues to balance—what disappears is the statistical foundation that gave those balances economic value[21]. Sky's post-crisis adaptations (PSM, RWA onboarding) can be understood as boundary adjustments: they widen the stability region by introducing collateral with lower volatility and near-zero correlation to crypto markets, stabilizing the leverage ratio and re-anchoring the stablecoin price[21][8].

**These equations make Sky unique:** solvency is enforced on-chain and updated continuously[5]. But they also reveal its boundary—deterministic arithmetic guarantees only hold inside a probabilistic envelope defined by collateral behavior and market speed[21]. Understanding where that envelope ends is key to designing future stablecoins that remain solvent not just on paper, but in motion.

---

### 1.5 Oracle Infrastructure: The Price Feed Pipeline

Oracles are central to backing verification—they provide the `spot` price that determines vault safety[5]. Sky uses a multi-layered architecture designed for security and manipulation resistance, but this design introduces a critical delay that affects crisis response[5][6].

**Full Oracle Pipeline:**[5]

```
Off-Chain Feeds → Relayer Network → Median → OSM → Spotter → Vat
```

1. **Off-Chain Feeds:** 13+ independent price feeds for ETH/USD (as of 2025), including exchanges, OTC desks, and data aggregators[5]

2. **Relayer Network:** Decentralized actors who call `Median.poke()` to submit new price data on-chain[5]

3. **Median Contract:** Computes median (not mean) of submitted prices to resist manipulation—requires majority of feeds to be compromised[5]
   - Uses median specifically because an attacker would need to control >50% of feeds to manipulate the final value[5]
   - Currently requires 7 of 13 feeds (for ETH) to successfully update price[5]

4. **Oracle Security Module (OSM):** Introduces a **1-hour delay** between `Median` price and `Vat`-accessible price[5]
   - Delay provides vault owners time to add collateral before liquidation
   - Updates via `OSM.poke()` callable once per hour by anyone[5]
   - Stores two values: `cur` (current usable price) and `nxt` (next price after delay)[5]

5. **Spotter:** Reads from OSM, adjusts by liquidation ratio (`mat`), and updates `Vat.ilks[ilk].spot`[5]
   - `spot = OSM.peek() / mat`[5]
   - Callable by keepers via `Spotter.poke(ilk)`[5]

**Security Model:**

- **Median** guards against single-feed manipulation (requires 51% attack)
- **OSM delay** guards against flash crashes and provides user reaction time
- **Multiple feeds** increase attack cost (must compromise multiple independent oracles)

**Failure Modes:**[5][6]

| Failure Type | Consequence | Mitigation |
|--------------|-------------|------------|
| Feed goes stale | Price doesn't update; system uses old data | Minimum feed requirement (e.g., 7 of 13) |
| Flash crash manipulation | Manipulated price could trigger false liquidations | 1-hour OSM delay filters out short-term manipulation |
| Correlated oracle failure | All feeds report wrong price simultaneously | Diverse feed sources (exchanges, OTC, aggregators) |
| Network congestion | `Spotter.poke()` fails to update; vaults use stale prices | Keeper incentives, gas priority auctions |

**Why the 1-hour delay matters:**

During the Black Thursday crash, the OSM's delay meant Sky's on-chain price remained ~20% above true market value for crucial periods[5]. This lag initially *prevented* proper liquidations, then triggered explosive cascades when prices updated—creating a "liquidation dam burst" pattern[5]. Analysis by Kjaer et al. shows this delay directly contributed to 70.5% of Flipper auctions failing to fully cover debt during March 12-13, 2020[5].

**Current State (2025):**

The oracle architecture has evolved post-Black Thursday. Governance has implemented adaptive OSM delays that shorten during high volatility and integrated Chainlink for redundant feeds[5]. Volatility-adjusted liquidation ratios automatically increase required collateral during turbulent markets. These remain active in many collateral types[5]. Part II analyzes how oracle lag interacts with auction mechanics to create systemic fragility.

---

### 1.6 Liquidation: When Solvency Is Enforced On-Chain

Liquidation is where Sky's deterministic accounting meets stochastic markets[5]. The process doesn't protect every vault—it protects the equation that guarantees DAI's backing[5].

**High-Level Liquidation Flow:**[5]

```
Unsafe Vault Detected → Dog.bark() → Vat.grab() → Clip.kick() → Auction → Vow Reconciliation
```

**1. Detection Phase (Dog):**

When a vault's collateral value falls below its threshold (`ink × spot < art × rate`), anyone can trigger liquidation[5]:

```solidity
Dog.bark(bytes32 ilk, address urn, address kpr)
```

- `Dog` checks vault safety via `Vat.urn`
- If unsafe, confiscates collateral and debt via `Vat.grab()`
- Transfers debt to `Vow` as system bad debt (`sin`)
- Kicks off auction in corresponding `Clip` contract[5]

**Key Dog parameters:**[5]

| Parameter | Meaning | Typical Value | Purpose |
|-----------|---------|---------------|---------|
| `chop` | Liquidation penalty added to debt | 13% | Covers auction costs, incentivizes vault health |
| `hole` | Max active liquidation debt system-wide | Varies by market | Throttles liquidation rate to prevent cascades |
| `Hole[ilk]` | Max active liquidation debt per collateral | Per-ilk limits | Prevents single collateral overwhelming auctions |

**2. Auction Phase (Clipper):**

Sky upgraded from English auctions (`Flipper`) to Dutch auctions (`Clipper`) post-Black Thursday[5]. Dutch auctions start at a high price that decays over time until a keeper accepts:

```solidity
Clip.kick(uint256 tab, uint256 lot, address usr, address kpr) returns (uint256 id)
```

- `tab`: Total DAI owed (debt + liquidation penalty)
- `lot`: Collateral for sale
- Auction price decays via chosen price curve (`calc`)[5]

**Auction pricing:**[5]

\[
\text{price}(t) = \text{buf} \times \text{spot} \times \text{calc}(t)
\]

Where:
- `buf`: Starting price buffer above oracle (e.g., 1.3 = 30% above)
- `calc`: Price decay function (linear, exponential, or stairstep)
- `t`: Time since auction start

**Keeper participation:**

Keepers bid by calling:

```solidity
Clip.take(uint256 id, uint256 amt, uint256 max, address who, bytes calldata data)
```

- `amt`: Amount of collateral to purchase
- `max`: Maximum price willing to pay
- Partial fills allowed (enables efficient capital use)[5]

**3. Settlement Phase (Vow):**

The `Vow` (System Stabilizer) reconciles auction proceeds against system debt[5]:

```solidity
// Vow tracks system balances
uint256 joy;  // Surplus DAI from fees and successful auctions
uint256 sin;  // Bad debt from liquidation shortfalls
uint256 ash;  // Debt queue (pending forgiveness)
```

**Reconciliation logic:**[5]

- If `joy > sin + hump` → Flapper auction (burn SKY with excess DAI)
- If `sin > joy + sump` (after 6.5-day debt queue wait) → Flopper auction (mint/sell SKY to cover deficit)

**This is the final solvency fallback:** DAI remains fully backed even if it means SKY dilution[5]. It formalizes what "lender of last resort" means in a protocol without banks—dilution replaces bailouts, executed by code[5].

**Example: ETH-A Liquidation During Black Thursday**

On March 12, 2020, at 16:00 UTC:
1. ETH price fell from $195 to $140 in minutes
2. Vault with 100 ETH, 10,000 DAI debt became unsafe:
   - Collateral value: 100 × $140 = $14,000
   - Required collateral (150% ratio): 10,000 × 1.5 = $15,000
   - **Undercollateralized** by $1,000
3. Keeper called `Dog.bark(ETH-A, vaultAddress, keeperAddress)`
4. `Dog` confiscated 100 ETH, added 13% penalty → `tab` = 11,300 DAI
5. `Clip` auction started at `buf` × spot ≈ $150/ETH (30% above oracle)
6. Due to network congestion and keeper hesitation, auction cleared at $90/ETH[5]
7. Proceeds: 100 ETH × $90 = $9,000 DAI
8. **Shortfall:** 11,300 - 9,000 = $2,300 → Added to `Vow.sin`[5]

Across thousands of such liquidations, Sky accumulated ~$4-6 million in bad debt, triggering the first MKR dilution event in protocol history[5][16].

**Simplified Liquidation Workflow:**

The system deliberately avoids excessive parameter detail here—comprehensive parameter tables appear in Part II's operational resilience section. This section focuses on **what** liquidation does (enforce invariants), not the minutiae of every `Dog.bark()` parameter[5].

---

### 1.7 The Peg Stability Module: Centralized Stability Rails

The PSM fundamentally altered Sky's economics, creating a tradeoff between short-term peg stability and long-term decentralization[12][15][21].

**Mechanism:**[12][15][21]

The PSM allows near-instantaneous DAI/USDS ↔ USDC swaps at 1:1 ratios with minimal fees (~0.1%):

```solidity
// Simplified PSM interface
interface IPSM {
    function sellGem(address usr, uint256 gemAmt) external;  // USDC → DAI/USDS
    function buyGem(address usr, uint256 gemAmt) external;   // DAI/USDS → USDC
}
```

Unlike vault loans requiring overcollateralization and stability fees, PSM swaps:
- Require no overcollateral (101% liquidation ratio for USDC-A)[12][21]
- Carry almost no protocol revenue (~0-0.1% fee)[21]
- Provide instantaneous arbitrage for DAI price deviations[12][21]

**How it maintains the peg:**[12][21]

1. **DAI > $1.00:** Arbitrageurs mint DAI via PSM (deposit USDC, get DAI), sell DAI on market for profit → increases DAI supply → price falls to $1
2. **DAI < $1.00:** Arbitrageurs buy DAI on market, redeem via PSM for USDC at $1 → decreases DAI supply → price rises to $1

**Impact on supply:**[21]

A significant proportion of circulating DAI/USDS is now backed by USDC via the PSM—not by decentralized crypto collateral. As of October 2025, PSMs back ~22% of supply (~$1.5B of ~$6.8B total), reflecting diversification into RWAs[4][24].

**Economic implications:**

| Aspect | Pre-PSM (2019) | Post-PSM (2020-2025) |
|--------|---------------|---------------------|
| **Revenue model** | Stability fees from crypto vaults | Stability fees + RWA yields offsetting PSM shortfalls |
| **Peg stability** | Volatile (±5% common) | Tight (±0.5% typical) |
| **Decentralization** | High (ETH, WBTC backed) | Moderate (USDC dependency) |
| **Censorship resistance** | High | Reduced (USDC can freeze) |
| **Crisis liquidity** | Limited (auction-dependent) | High (instant arbitrage) |

**Decentralization paradox:**[21]

While the PSM enhances peg stability, it concentrates risk on USDC's centralized backing. Circle (USDC issuer) can:
- Freeze USDC addresses on regulatory demand
- Depeg if underlying reserves fail
- Introduce new counterparty risk (bank failures, regulatory changes)

Governance must now balance:
- **Short-term stability** (favor PSM usage)
- **Long-run sustainability** (maintain crypto-backed vault incentives)
- **Decentralization goals** (reduce USDC dependency)[21]

**The 2025 evolution: LitePSM**[15][21]

Sky deployed `DssLitePsm` to reduce gas costs and integrate with Endgame requirements:
- Swaps occur in a **pool** of pre-minted DAI/USDS and stablecoins (reduces gas by ~50%)
- Adds `buyGemNoFee` / `sellGemNoFee` permissioned functions for SubDAOs[15]
- Enables collateral segregation for yield-bearing strategies (e.g., lending USDC to Aave)[15][21]

This evolution demonstrates PSM's permanence—not a temporary crisis measure but a core architectural component[21]. Part II examines the sustainability implications: how PSM revenue shortfalls interact with auction failure risks.

---

### 1.8 Global Settlement: The Ultimate Backstop

Global Settlement (Emergency Shutdown) is Sky's terminal condition—what happens when invariants fail permanently or a critical vulnerability is discovered[13][19][22][25].

**Trigger Mechanism:**[13][19][22]

- Requires 50,000 SKY (legacy MKR) deposited into the Emergency Shutdown Module (ESM)[13]
- SKY placed in ESM is **permanently burned** (irretrievable)[13]
- Can be triggered for: system upgrade, governance attack, oracle failure, black swan event, unrecoverable technical vulnerability[13][19][22]

**Settlement Process (3 Phases):**[19][22][25]

**Phase 1: System Freeze (Immediate)**
- All new vault creation halts
- Oracle prices freeze at shutdown moment
- Ongoing auctions allowed to complete
- `Vat` records final system state[19][22][25]

**Phase 2: Vault Processing (Hours to days)**
- Vault owners can **immediately** retrieve excess collateral:
  - Calculate: `excess = ink × spot - art × rate`
  - If `excess > 0`, vault owner withdraws via `End.free(ilk)`[19][22]
- Undercollateralized vaults contribute remaining collateral to DAI redemption pool[19][22]

**Phase 3: DAI Redemption (After processing period)**
- DAI/USDS holders redeem for proportional share of **all collateral types**[19][22][25]
- Redemption price: `redemptionPrice[ilk] = totalCollateral[ilk] / totalDAI`[19]
- DAI holders receive same relative amount whether first or last to redeem[19][25]

**Settlement equations:**[21][19]

For each collateral type \(i\):

\[
\text{DAI holder receives:} \quad \frac{\text{DAI\_amount}}{\text{totalDAI}} \times \sum_{i} \text{collateral}_i
\]

**Priority structure:**[19]

1. **Vault owners** recover excess collateral first (if overcollateralized)
2. **DAI holders** share remaining collateral pool proportionally
3. **SKY holders** absorb losses if system is undercollateralized

This prioritization incentivizes vault overcollateralization even during crisis, as vault owners know they can recover excess[19].

**Klages-Mundt theoretical context:**[21]

Global Settlement serves as the "final period" in Klages-Mundt's one-off model—the terminal condition that enforces face value treatment of liabilities[21]. The protocol smart contracts encode this: redemption at par value from the collateral pool, ensuring DAI holders receive deterministic settlement even if market value diverges from $1[21].

**Historical near-misses:**[16]

During Black Thursday (March 12, 2020), Sky governance seriously considered triggering Emergency Shutdown[16]:
- ETH crashed 43% in hours
- Liquidation auctions failing (70.5% couldn't cover debt)[5]
- Network congestion prevented normal operation
- Bad debt accumulating rapidly

Governance ultimately chose:
1. Emergency parameter adjustments (extend auction duration `ttl` from 10 min → 6 hours)[5]
2. Debt auction (Flop) to mint MKR and cover shortfall[5]
3. Rapid PSM deployment to restore peg stability[12][21]

**Post-settlement redeployment:**[13]

Global Settlement does **not** automatically redeploy Sky. Since the protocol is open-source:
- Anyone can redeploy with modified parameters
- SKY community typically coordinates redeployment vote
- Redeployment varies by shutdown reason (oracle fix, governance fork, parameter changes)[13]

| Shutdown Reason | Likely Redeployment Strategy |
|----------------|------------------------------|
| Governance attack | Fork out malicious SKY holders, reimburse ESM deposits, redeploy as-is[13] |
| Oracle failure | Replace Oracle module, reimburse ESM, redeploy with vulnerability fix[13] |
| Black swan event | Community vote on new mechanics (e.g., enhanced PSM, improved auctions)[13] |
| Unwarranted ES | Fork out attackers, redeploy unchanged[13] |

**Why Global Settlement matters for Part I:**

It defines the *ultimate* meaning of "backed"—DAI/USDS holders can always redeem for collateral at deterministic rates, even if Sky ceases operation[19][25]. This guarantee distinguishes DAI from purely algorithmic stablecoins (e.g., Terra/Luna) that lacked such a terminal value floor[21].

However, the collateral received may be worth less than $1 if the system is undercollateralized at shutdown[19]. Part II explores the conditions under which this occurs and how governance acts as the dynamic hedge to prevent it.

---

### 1.9 Parameter Governance: Adjusting the Definition of "Safe"

Backing isn't static—governance continuously adjusts the definition of "safe" through parameter votes[5]. These adjustments represent Sky's monetary policy layer, balancing capital efficiency against systemic risk.

**Key Adjustable Parameters (Vault-Level):**[5]

| Parameter | Contract | Meaning | Governance Control | Typical Range |
|-----------|----------|---------|-------------------|---------------|
| `mat` | `Spotter` | Liquidation ratio | Executive vote | 120-200% |
| `line` | `Vat.ilks[ilk]` | Debt ceiling (max DAI mintable) | Executive vote | 0 - 20B USDS |
| `duty` | `Jug` | Stability fee (interest rate) | Executive vote | 0-5% annual |
| `chop` | `Dog` | Liquidation penalty | Executive vote | 0-13% |

**Key Adjustable Parameters (Auction-Level):**[5]

| Parameter | Contract | Meaning | Impact |
|-----------|----------|---------|--------|
| `buf` | `Clip` | Auction starting price multiplier | Higher buf = safer auctions, worse for vault owners |
| `tail` | `Clip` | Max auction duration | Longer tail = more keeper participation, slower capital recovery |
| `cusp` | `Clip` | Max price drop before auction reset | Lower cusp = more aggressive price discovery |
| `chip` / `tip` | `Dog` | Keeper incentive (flat fee + % of tab) | Higher = more keeper participation, higher system cost |

**Key Adjustable Parameters (System-Level):**[5]

| Parameter | Contract | Meaning | Purpose |
|-----------|----------|---------|---------|
| `hole` | `Dog` | Max active liquidation debt system-wide | Throttles liquidation rate to prevent reflexive deleveraging |
| `hump` | `Vow` | Surplus buffer before SKY burn | Accumulates safety margin before returning value to SKY |
| `sump` | `Vow` | Minimum deficit to trigger debt auction | Avoids frequent small SKY dilution events |
| `wait` | `Vow` | Debt queue duration before Flop | 6.5 days to allow auctions to settle before dilution[5] |

**Governance Process:**[5]

1. **Governance Polls** (Signal gathering, non-binding)
2. **Executive Votes** (Binding, requires majority SKY approval)
3. **Governance Security Module (GSM)** (48-hour delay on execution for security)

**Historical Evolution: Black Thursday Response**[5]

| Parameter | Pre-BT (March 11) | Emergency Change (March 13) | Current (2025) |
|-----------|-------------------|----------------------------|----------------|
| ETH-A `duty` | 8% | 0.5% → 0% | 0.5-3% (variable) |
| `Flip.ttl` (bid duration) | 10 minutes | 6 hours | N/A (moved to Clip) |
| `Flip.tau` (auction length) | 6 hours | 6 hours | N/A (moved to Clip) |
| `Dog.hole` | N/A (Cat used) | Introduced | ~100M USDS |
| GSM delay | 24 hours | 4 hours (emergency) | 48 hours (restored) |
| Oracle delay | 1h fixed | N/A | Adaptive (0.5-1h, volatility-based) via Chainlink integration[5] |

These changes demonstrate governance acting as "dynamic hedge"—rapidly adjusting risk exposure in response to crisis[5]. However, the response was **reactive**, not preventive[5]. Part II analyzes how to make governance more proactive through automated parameter tuning.

**Parameter Interdependencies:**[5]

Changing one parameter often requires adjusting others to maintain system balance:

- ↑ `mat` (safer) → ↓ `line` may be needed to prevent supply overshoot
- ↓ `duty` (cheaper borrowing) → May require ↑ `buf` to maintain auction safety
- ↑ `hole` (faster liquidations) → Requires sufficient keeper liquidity to absorb

Part II formalizes these relationships through the Sustainability Triangle framework, showing how collateral, incentives, and governance parameters interact.

---

### 1.10 When Arithmetic Meets Market Reality

The deterministic invariants in Section 1.4 provide mathematical guarantees, but those guarantees rest on economic assumptions that can break[5][6].

**Three boundary conditions where math loses economic meaning:**[21]

**1. Oracle Delay Creates Information Asymmetry**

The 1-hour OSM delay means `spot` lags reality. During rapid crashes:
- Vaults appear safer than they are → delays liquidation triggers
- When oracle catches up, massive cascades occur simultaneously
- Keepers face adverse selection (stale prices favor informed traders)[5][21]

**2. Auction Throughput Becomes Bottleneck**

The system can only process liquidations at finite speed (`Dog.hole` limits active debt). When liquidation demand exceeds auction capacity:
- Collateral devalues faster than it can be sold
- Auctions fall behind market price (Klages-Mundt's "deleveraging spiral")[21]
- Each auction round intensifies the next (reflexive feedback)[21]

**3. Keeper Liquidity Proves Finite**

Liquidation depends on keepers having capital to bid. During panics:
- Capital flees to safety (reduced keeper participation)
- Network congestion locks out some keepers (gas wars, mempool flooding)[5]
- Even well-collateralized auctions may fail to clear[5]

**The phase transition:**[21]

Klages-Mundt's model proves these aren't independent failures—they're coupled through the collateralization ratio \(Z_t = D_t / L_t\) (demand / leverage):

\[
Z_t = \frac{D_t}{L_t}
\]

- **Stable regime:** \(Z_t\) bounded, arbitrage corrects deviations, auctions dampen volatility
- **Unstable regime:** \(Z_t\) crosses critical threshold, auctions **amplify** volatility, deleveraging spirals emerge

**Critical insight:** Below critical leverage, DAI price perturbations decay (stable). Above it, perturbations grow exponentially—even though the `Vat` invariants still hold on-chain[21].

**Empirical validation: Black Thursday**[5][21]

March 12-13, 2020 demonstrated this phase transition:
- ETH fell 43% → triggered mass liquidations
- Oracle lag → "dam burst" liquidation pattern
- Auction effectiveness collapsed to median 76.9% (vs. 97.4% normal)[5]
- **DAI price rose to $1.11** during crash—not fell—validating deleveraging spiral prediction[21]

The paradox: DAI traded at premium despite collateral crash because speculators needed to repurchase DAI to deleverage, driving up demand faster than supply could adjust[21].

**This is why Endgame matters:**[8]

By introducing PSM and RWA, Sky shifts the critical threshold:
- USDC-backed DAI doesn't deleverage during ETH crashes (uncorrelated)
- RWA provides stable collateral that doesn't trigger cascades
- PSM arbitrage dampens \(Z_t\) perturbations before they grow

The trade-off: reliance on centralized assets (USDC) and off-chain trust (RWA legal wrappers)[3][8][21]. Part II quantifies this trade-off through formal sustainability analysis.

---

## Conclusion: Layered Backing and the Path to Part II

Sky's backing is no longer a simple equation. It's a layered system:

**Layer 1: On-chain invariants** (`Vat` accounting, deterministic liquidation)  
**Layer 2: Market microstructure** (oracle delays, auction throughput, keeper liquidity)  
**Layer 3: Off-chain dependencies** (USDC reserves, RWA legal wrappers, governance responsiveness)

Part I has established:
- **How** on-chain backing works (Vat → Join → Dog → Clip → Vow pipeline)[5]
- **What** parameters governance controls (mat, line, duty, chop, hole)[5]
- **Where** mathematical guarantees end (phase transitions, deleveraging spirals)[21]
- **Why** Endgame introduced hybrid backing (USDC/RWA stability buffer)[3][8][27]

But backing alone doesn't ensure sustainability. A protocol can be solvent yet economically unviable. The critical question Part II addresses:

> *"Sky's invariants guarantee DAI/USDS is backed—but can the protocol afford to maintain that backing under repeated stress without permanent SKY dilution?"*

Part II: **Sustainability — When Stability Has to Pay for Itself** examines:
- The Sustainability Triangle (collateral, incentives, governance feedback loops)
- Auction-oracle-keeper triad fragility (operational bottlenecks)
- Black Thursday comprehensive case study (empirical validation of theory)
- Klages-Mundt's formal regime analysis (stable vs. unstable domains)
- Kjaer's operational metrics (auction effectiveness, liquidation delay, vault agility)
- Economic state transitions (fee revenue vs. SKY dilution triggers)
- Paths forward (RWA diversification, automated auctions, governance improvements)

**The bridge:** Part I shows backing is *mathematically* enforced. Part II shows backing is *economically* sustainable only when the Sustainability Triangle remains balanced—and analyzes what happens when it doesn't.

---

## References

[3] Backing-Mechanism.md (User-provided original draft)

[4] CoinLaw. (Sep 2025). *MakerDAO Statistics 2025: Real-Time DeFi Insights*. https://coinlaw.io/makerdao-statistics/

[5] Kjaer, M. (2021). *Quantitative Analysis of MakerDAO's Liquidation System*. Diploma Thesis, TU Wien.

[6] Klages-Mundt, A. (2021). *Stablecoin Risk Models*. PhD Dissertation, Cornell University.

[8] Trade Dog. (2024). "MakerDAO announces Launch Season of Endgame Plan." https://tradedog.io/makerdao-announces-launch-season-of-endgame-plan/

[9] Blockworks. (2023). "Takeaways From MakerDAO's 5-phase Endgame Update." https://blockworks.co/news/makerdao-endgame-update

[10] Blockworks. (2023). "MakerDAO Makes First Steps Toward Endgame." https://blockworks.co/news/makerdao-makes-first-steps-toward-endgame

[11] Token Vitals. (2025). "MakerDAO's Endgame Plan: Decentralizing the Future of DeFi." https://tokenvitals.com/blog/makerdao-endgame-plan-mkr-holders-defi

[12] MAI Finance Docs. (2024). "Peg Stability Module." https://docs.mai.finance/peg-stability-module

[13] Tudhope, A. (2020). "Emergency Shutdown - Community Development." https://andytudhope.github.io/community/faqs/emergency-shutdown/

[15] GitHub - makerdao/dss-lite-psm. (2023). https://github.com/makerdao/dss-lite-psm

[16] CoinDesk. (2020). "DeFi Leader MakerDAO Weighs Emergency Shutdown Following ETH Price Drop." https://www.coindesk.com/tech/2020/03/12/defi-leader-makerdao-weighs-emergency-shutdown-following-eth-price-drop

[17] CoinDesk. (2023). "Lending Platform MakerDAO Approves 'Constitution,' Moves Forward With 'Endgame' Plan." https://www.coindesk.com/business/2023/03/27/lending-platform-makerdao-approves-constitution-moves-forward-with-endgame-plan

[19] MakerDAO Community Portal. (n.d.). "Emergency Shutdown." https://community-portal-staging.makerfoundation.com/en/learn/governance/emergency-shutdown/

[20] CoinTelegraph. (2024). "Maker's 'Endgame' readies launch, aims for 100B DAI to take on Tether." https://cointelegraph.com/news/makerdao-endgame-to-launch-aims-for-100-billion-dai-rival-tether

[21] Mirror (Dewiz). (2024). "Exploring MakerDAO's PSM and the Advent of LitePSM." https://mirror.xyz/dewiz.xyz/cs-D34NCp2JK9oMs61oKV-YLbSXTsZyxjxt4l_hZW6c

[22] MakerDAO Docs. (2020). "The Emergency Shutdown Process for Multi-Collateral Dai (MCD)." https://docs.makerdao.com/smart-contract-modules/shutdown/the-emergency-shutdown-process-for-multi-collateral-dai-mcd

[24] Sky Ecosystem. (2025). *Collateral Overview*. https://info.sky.money/collateral

[25] MakerDAO Docs. (2019). "Maker Protocol Emergency Shutdown." https://docs.makerdao.com/smart-contract-modules/shutdown

[26] The Block. (Sep 2025). "Sky opens vote to penalize stragglers delaying MKR-to-SKY token conversion." https://www.theblock.co/post/371401/sky-opens-vote-to-penalize-stragglers-delaying-mkr-to-sky-token-conversion

[27] Blockworks. (Aug 2025). "One year into Sky, adoption lags behind vision." https://blockworks.co/news/sky-dao-adoption

[29] Immunefi. (Oct 2025). "Sky Bug Bounties." https://immunefi.com/bug-bounty/sky/

[33] Crypto.news. (Sep 2025). "Balancer sets Sept. 18 deadline for MKR to SKY token migration." https://crypto.news/balancer-sept-18-deadline-mkr-sky-token-migration-2025/

[21] Klages-Mundt, A., & Minca, A. (2019). "(In)Stability for the Blockchain: Deleveraging Spirals and Stablecoin Attacks." arXiv:1906.02152. https://arxiv.org/abs/1906.02152

---

**Series Navigation:**
- **← You are here: Part I (Backing Mechanism)**
- → Next: Part II (Sustainability)
- → Coming: Part III (Governance Evolution)

---

## Key Citations

- [CoinLaw (Sep 2025). MakerDAO Statistics 2025.](https://coinlaw.io/makerdao-statistics/) – Collateral composition and RWA exposure.
- [Blockworks (Aug 2025). One year into Sky, adoption lags behind vision.](https://blockworks.co/news/sky-dao-adoption) – Endgame Phase 1 and rebrand status.
- [The Block (Sep 2025). Sky opens vote to penalize stragglers delaying MKR-to-SKY.](https://www.theblock.co/post/371401/sky-opens-vote-to-penalize-stragglers-delaying-mkr-to-sky-token-conversion) – SKY migration details.
- [Immunefi (Oct 2025). Sky Bug Bounties.](https://immunefi.com/bug-bounty/sky/) – USDS launch post-rebrand.
- [arXiv:1906.02152 (2019). (In)Stability for the Blockchain.](https://arxiv.org/abs/1906.02152) – Klages-Mundt models for regime transitions.
- [Sky Ecosystem Collateral Overview (2025).](https://info.sky.money/collateral) – Current backing metrics.
- [Decrypt (May 2025). Spark Commits Additional $1 Billion to Tokenized Treasuries.](https://decrypt.co/318035/spark-commits-additional-1-billion-to-lead-tokenized-treasuries-sector) – Spark SubDAO TVL and RWA deployment.
- [Crypto.news (Sep 2025). Balancer sets Sept. 18 deadline for MKR to SKY.](https://crypto.news/balancer-sept-18-deadline-mkr-sky-token-migration-2025/) – Governance token transition.
- 