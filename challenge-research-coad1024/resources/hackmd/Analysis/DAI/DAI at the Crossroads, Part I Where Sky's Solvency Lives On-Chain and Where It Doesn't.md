Perfect! Let's build this. Here's the **complete revised Part I outline** with SVB crisis integrated as lighter treatment, ready for you to draft from.

---

# DAI at the Crossroads, Part I: Where Sky's Solvency Lives On-Chain (and Where It Doesn't)

## Complete Article Outline

---

### Front Matter

**Title:** DAI at the Crossroads, Part I: Where Sky's Solvency Lives On-Chain (and Where It Doesn't)

**Subtitle:** A three-part technical series unpacking Sky Ecosystem's (formerly MakerDAO) architecture—from its on-chain reserves to its evolving sustainability model and the governance layer that now defines its credibility.

**Target audience:** Senior Solidity devs, protocol engineers, DeFi risk teams.

**Cross-Article Continuity Table:** (Keep your existing shared definitions table—ink, art, rate, mat, spot, core invariant, Black Thursday, PSM, Global Settlement, MKR dilution)

---

### Introduction: The Evolution of "Backed" (~800 words)

DAI remains one of the largest dollar-pegged tokens in crypto that isn't issued by a bank or fintech. Its reserve lives entirely on-chain, enforced by collateral and arithmetic rather than balance-sheet trust. Yet over the past few years, that arithmetic has been bent—and then formalized—by pragmatism.

**The three phases of backing:**

1. **Pure crypto (2017-2020):** ETH-backed, over-collateralized vaults, liquidation cascades
2. **Hybrid emergency (2020-2023):** PSM introduced post-Black Thursday, USDC dependency grows to 60%+
3. **Endgame maturity (2023-2025):** SubDAOs distribute risk, RWAs provide uncorrelated yields, "backed" now means a portfolio

**The central tension:**
What began as emergency patches after Black Thursday has evolved into a permanent blueprint: Sky Ecosystem's Endgame plan. Vaults gave way to the Peg Stability Module (PSM), ETH to USDC, and the once-pure crypto-collateral model to a hybrid of smart contracts, custodial reserves, and real-world assets (RWA).

**What this article answers:**

- Where does backing actually live? (On-chain? Off-chain? Legal wrappers?)
- How do you verify it? (Vat accounting, oracles, liquidation enforcement)
- What does "backed" mean across different collateral types? (Trustless ETH vs custodial USDC vs legal-wrapped RWA)

**Forward setup:**

- Part I establishes *what* creates backing (mechanisms, invariants, enforcement)
- Part II analyzes *whether* that backing remains sustainable under repeated stress (Black Thursday deep-dive, Klages-Mundt regimes)
- Part III examines *who* controls what counts as backing (governance, SubDAOs, centralization risks)

**Bridge to Section 1:**
The story starts where all solvency guarantees begin—in the deterministic accounting layer that makes backing *verifiable* on-chain.

---

### 1. The Core Accounting Layer: Vat as Single Source of Truth (~1200 words)

**What this section establishes:** The foundational data structures that make backing verifiable and enforceable through smart contract logic.

#### 1.1 The Vat Contract: Sky's Ledger

**Core purpose:** Single source of truth for all collateral balances, debt positions, and system-wide solvency.

**Why it matters:** Unlike traditional finance where "reserves" are audited quarterly, Sky's reserves update every block (~12 seconds). The Vat makes this possible.

**Key design choice:** Non-upgradeable core. Interfaces (Join adapters, liquidation modules) can change, but Vat accounting logic is immutable. This creates trust in the arithmetic even as governance evolves the system around it.

#### 1.2 State Variables: What Gets Tracked

**Table: Core Vat Variables**

| Variable | Meaning | Units | Example | Why It Exists |
|----------|---------|-------|---------|---------------|
| `gem` | Unlocked collateral (deposited but not securing debt) | Token wei | 50 ETH | Separates "in wallet" from "in vault" |
| `ink` | Locked collateral securing a vault's debt | Token wei | 10 ETH | Determines liquidation eligibility |
| `art` | Normalized debt (before fee multiplier applied) | Internal units | 1000 units | Gas-efficient fee accrual |
| `rate` | Cumulative stability fee multiplier | Ray (10^27) | 1.035 × 10^27 | Converts normalized debt to real debt |
| `spot` | Liquidation price: `spot = oracle_price / mat` | Ray | 2000 DAI/ETH | Pre-computed for gas efficiency |

**The debt calculation:**

```
Real debt = art × rate
```

**Why normalized debt?** Charging stability fees to 10,000 vaults individually would cost millions in gas. Instead, update `rate` once globally—all vaults accrue fees automatically through the multiplier.

#### 1.3 The Fundamental Invariant

**Vault safety condition:**

```
ink × spot ≥ art × rate
```

**What this means in English:** "Collateral value (adjusted for liquidation buffer) must exceed debt (including accrued fees)."

**What makes this deterministic:**

- `ink`, `art`, `rate` are on-chain state—no trust required
- `spot` comes from oracle (Section 3)—trust in price feeds, not in Sky
- Inequality is checked by EVM—math can't be fudged

**Critical insight:** This invariant guarantees backing *arithmetically*. Whether it guarantees backing *economically* depends on whether `spot` reflects reality and whether liquidations can execute fast enough. Part II explores these constraints.

#### 1.4 Pedagogical Code: Simplified IVat Interface

```solidity
interface IVat {
    // Adjust vault position (collateral and/or debt)
    // dink > 0: lock more collateral (gem → ink)
    // dart > 0: mint more DAI (increases art)
    // Negative values reverse these operations
    function frob(
        bytes32 ilk,      // collateral type (e.g., "ETH-A")
        address urn,      // vault identifier
        address usr,      // collateral source/destination
        int256 dink,      // change in locked collateral
        int256 dart       // change in normalized debt
    ) external;
    
    // Confiscate collateral from unsafe vault (liquidation)
    // Only callable by authorized liquidation module (Dog)
    function grab(
        bytes32 ilk,
        address urn,
        address v,        // collateral destination (auction)
        address w,        // debt destination (Vow)
        int256 dink,      // collateral to seize (negative)
        int256 dart       // debt to cancel (negative)
    ) external;
    
    // Transfer internal DAI balances
    function move(
        address src,
        address dst,
        uint256 rad       // amount (in "rad" units, 10^45 precision)
    ) external;
}
```

**Design lesson box:**
> **Why `frob` combines collateral and debt operations:** Atomicity prevents exploits. If deposit and borrow were separate functions, an attacker could front-run price updates to create under-collateralized positions. Single function = single safety check.

**Setup for Section 2:** Now that we know *how* balances are tracked, Section 2 shows how collateral enters this accounting system.

---

### 2. Collateral Entry: How Value Enters the System (~1000 words)

**What this section shows:** The mechanical process of locking collateral, minting DAI/USDS, and managing vault positions.

#### 2.1 Join Adapters: The Entry Interface

**Why adapters exist:** Vat is non-upgradeable and collateral-agnostic. Join adapters translate between specific token standards (ERC-20, native ETH) and Vat's internal accounting.

**The separation of concerns:**

- **Join contract** = custodian (holds actual tokens)
- **Vat contract** = accountant (tracks who owns what)

**Security implication:** Even if a Join adapter is exploited, Vat accounting remains correct. You'd need to compromise Vat itself (immutable) to fake balances.

#### 2.2 Vault Lifecycle: From Creation to Closure

**State machine diagram (simplified ASCII):**

```
[Deposit collateral] → [Lock collateral + Mint DAI] → [Manage position]
                                                            ↓
                         [Close vault] ← [Repay debt + Unlock collateral]
                                    ↓
                         [Liquidation] (if unsafe)
```

**Worked Example: Creating an ETH-A Vault**

```solidity
// 1. User deposits 10 ETH into GemJoin
GemJoin_ETH.join(userAddress, 10 ether);
// Result: Vat.gem[ETH-A][user] = 10 ETH (unlocked)

// 2. User locks 10 ETH and mints 5000 DAI
// Assuming rate ≈ 1.0 (no fees accrued yet)
Vat.frob(
    "ETH-A",           // collateral type
    userUrn,           // vault identifier
    userAddress,       // collateral source
    int(10 ether),     // lock 10 ETH (dink > 0)
    int(5000 ether)    // mint 5000 DAI (dart > 0)
);
// Result:
//   Vat.ink[ETH-A][userUrn] = 10 ETH (locked)
//   Vat.art[ETH-A][userUrn] = 5000 units (normalized debt)
//   
// Safety check performed:
//   ink × spot ≥ art × rate
//   10 ETH × $2000/ETH ≥ 5000 DAI × 1.0
//   $20,000 ≥ $5,000 ✓
//   Collateral ratio: 400% (well above 150% liquidation threshold)

// 3. User withdraws DAI as ERC-20 token
DaiJoin.exit(userAddress, 5000 ether);
// Now user has 5000 DAI tokens in their wallet
```

**Design lesson box:**
> **Why DAI isn't minted immediately:** The `frob` call updates Vat's internal `dai` balance, not ERC-20 supply. This separates accounting (Vat) from token logistics (DaiJoin). Gas-efficient and enables flash-loan-resistant operations.

#### 2.3 Multi-Collateral Reality: Current Composition (October 2025)

**Table: Representative Collateral Profiles**

| Collateral Type | SubDAO | Liquidation Ratio | Stability Fee | Debt Ceiling | Risk Profile |
|-----------------|--------|-------------------|---------------|--------------|--------------|
| ETH-A | Core | 150% | 0.5-3% variable | ~20B USDS | High volatility, crypto-correlated |
| WBTC-A | Core | 150% | 4-6% | ~2B USDS | High volatility, crypto-correlated |
| USDC-A (PSM) | Spark | 101% | 0-0.1% | ~15B USDS | Low volatility, centralized (Circle) |
| RWA (T-bills, bonds) | Grove | 100-102% | 2-5% | ~1B USDS ($948M active) | Off-chain, legal-wrapped, 14% total |

**Current supply breakdown (Oct 2025):**

- Crypto-native: 38% (via Core SubDAO)
- Stablecoins: 22% (via Spark PSM)
- RWA: 14% ($948M, Grove SubDAO)
- Other: 26% (various, mixed)

Governance can adjust these parameters, but the backing types are fixed by design: trustless crypto, custodial stablecoins, and legal-wrapped real-world assets. Understanding this heterogeneity is crucial—'backed' no longer means one thing.

**Governance note:** *Each collateral type has adjustable parameters like liquidation ratio and debt ceiling—governance controls these.*

**Setup for Section 3:** Collateral is locked. Debt is minted. But how does the system *know* what that collateral is worth? That's where oracles enter.

---

### 3. Price Discovery: Oracle Architecture (~1100 words)

**What this section establishes:** How the system determines collateral value—the mechanism that makes the invariant *checkable*.

#### 3.1 The Oracle Pipeline

**Full architecture:**

```
Off-Chain Feeds (13+ sources) 
    ↓
Relayer Network (submits prices on-chain)
    ↓
Median Contract (computes median, not mean)
    ↓
OSM (Oracle Security Module: 1-hour delay)
    ↓
Spotter (adjusts by liquidation ratio: spot = price / mat)
    ↓
Vat (stores spot price for safety checks)
```

**Why this complexity?** Each layer solves a specific attack vector:

1. **Multiple feeds** → Require 51% compromise (not single oracle)
2. **Median aggregation** → Resist outlier manipulation
3. **1-hour delay** → Give users reaction time before liquidation
4. **Spotter calculation** → Pre-compute liquidation price (gas efficiency)

#### 3.2 The Median: Manipulation Resistance

**Why median, not mean?**

Consider 13 feeds reporting ETH price:

- 12 honest feeds: ~$2000
- 1 compromised feed: $10,000

**Mean:** $(12 × 2000 + 10000) / 13 = $2615$ (15% manipulation)  
**Median:** $2000 (no impact)

Attacker needs to compromise **7 of 13 feeds** (majority) to manipulate median. Much harder than corrupting one feed.

**Current configuration (2025):** ETH/USD uses 13 feeds, requires 7 signatures to update (configurable via governance).

#### 3.3 The OSM: One-Hour Delay Trade-off

**Purpose:** Vault owners get warning before liquidation. If oracle shows ETH crashed, they have ~1 hour to add collateral before `spot` price updates and liquidation becomes possible.

**The mechanism:**

```solidity
// OSM stores two prices:
uint128 cur;  // Current usable price (1 hour old)
uint128 nxt;  // Next price (just received from Median)

// Once per hour, anyone can call:
function poke() external {
    cur = nxt;              // Promote next → current
    nxt = Median.peek();    // Fetch fresh price
    emit LogValue(cur);
}
```

**Trade-off visualization:**

| Normal Market | Crash Event |
|---------------|-------------|
| ✅ Users have reaction time | ❌ Vat uses stale price during crash |
| ✅ Prevents flash-loan manipulation | ❌ Delay accumulates liquidation demand |
| ✅ Reduces false liquidations | ❌ "Dam burst" effect when price updates |

#### 3.4 When Oracle Lag Becomes Dangerous

**Black Thursday preview (detailed analysis in Part II):**

March 12, 2020 timeline:

- **10:00 UTC:** Real ETH price crashes to $110 (from $195)
- **10:00-11:00 UTC:** OSM still reports $195 (stale)
- Vaults appear safe when they're actually underwater
- **11:00 UTC:** OSM updates to $110
- **11:00-11:30 UTC:** Massive liquidation cascade (4,600 vaults)
- Network congestion + auction failures compound the problem

Oracle delays create a timing mismatch: vaults that are underwater in real-time appear safe on-chain until the OSM updates. This gap, while necessary for user protection, becomes dangerous during rapid price movements. Black Thursday exemplified this vulnerability

**Setup for Section 4:** We've shown how collateral enters (Section 2) and how price is discovered (Section 3). Section 4 shows what happens when `ink × spot < art × rate`—how the invariant is *enforced*.

---

### 4. Collateral Exit: Liquidation as Invariant Enforcement (~1300 words)

**What this section shows:** Liquidation isn't a bug—it's the *designed mechanism* to maintain backing when vault owners fail to manage positions.

#### 4.1 Liquidation Flow: From Detection to Settlement

**High-level pipeline:**

```
Unsafe Vault Detected
    ↓
Dog.bark() (confiscate collateral + debt)
    ↓
Vat.grab() (move to auction contract)
    ↓
Clipper.kick() (start Dutch auction)
    ↓
Keepers bid (price decays until someone accepts)
    ↓
Vow reconciles (surplus vs deficit)
```

#### 4.2 Detection: The Dog Contract

**Anyone can trigger liquidation:**

```solidity
Dog.bark(
    bytes32 ilk,      // collateral type
    address urn,      // vault to liquidate
    address kpr       // keeper (receives incentive)
)
```

**Safety check inside bark:**

```solidity
// Vault must be unsafe:
require(ink × spot < art × rate, "vault-safe");

// System must not be at liquidation capacity:
require(current_debt_under_auction < Dog.hole, "liquidation-limit-reached");
```

**Key parameters (configurable via governance):**

| Parameter | Meaning | Typical Value | Purpose |
|-----------|---------|---------------|---------|
| `chop` | Liquidation penalty added to debt | 13% | Covers auction costs, incentivizes vault health |
| `hole` | Max liquidation debt system-wide | ~100M USDS | Throttles cascade speed (post-Black Thursday) |
| `Hole[ilk]` | Max liquidation debt per collateral type | Per-ilk limits | Prevents single collateral overwhelming auctions |

**Design insight:** `hole` parameter didn't exist pre-Black Thursday. It was added because unlimited simultaneous liquidations overwhelm keeper liquidity. This is a *capacity constraint* recognition—Part II analyzes the bottleneck.

#### 4.3 Auction: Clipper (Dutch Auction Model)

**Evolution note:** Pre-2021 used English auctions (Flipper). Post-Black Thursday redesign switched to Dutch auctions (Clipper) for capital efficiency.

**Dutch auction mechanics:**

1. **Start high:** Auction begins at `buf × spot` (e.g., 130% of oracle price)
2. **Price decays:** Follows chosen curve (linear/exponential/stairstep)
3. **Keeper accepts:** First to accept current price wins
4. **Partial fills allowed:** Keepers can buy subset of collateral (capital efficiency)

**Price decay formula:**

```
price(t) = buf × spot × calc(t)

Where:
- buf = starting price multiplier (e.g., 1.3 = 30% above oracle)
- calc = decay function (governance chooses curve type)
- t = seconds since auction start
```

**Example parameters (ETH-A, 2025):**

- `buf`: 1.3 (starts 30% above oracle)
- `tail`: 21,600 seconds (6 hours max duration)
- `cusp`: 0.4 (resets if price drops below 40% of start)

Clipper vs Flipper: Clipper's partial-fill design allows keepers to recycle capital during cascades, enabling more auctions per unit of keeper liquidity. This matters during Black Thursday-like events when auction throughput becomes a bottleneck.

#### 4.4 Settlement: The Vow and System Reconciliation

**Vow tracks system-wide balance:**

```solidity
uint256 joy;  // Surplus DAI (from fees + successful auctions)
uint256 sin;  // Bad debt (from auction shortfalls)
uint256 ash;  // Debt queue (pending forgiveness after 6.5-day wait)
```

**Reconciliation logic:**

```solidity
if (joy > sin + hump) {
    // System has excess surplus beyond safety buffer
    Flapper.kick();  // Burn SKY with excess DAI
}

if (sin > joy + sump) {
    // System has bad debt after 6.5-day queue
    Flopper.kick();  // Mint and sell SKY to cover deficit
}
```

**This is the ultimate backstop:** DAI remains fully backed even if it requires **SKY dilution**. It formalizes "lender of last resort" without banks—shareholders (SKY holders) absorb tail risk through dilution.

**Black Thursday outcome :**

- ~$4-6M bad debt accumulated (auctions failed to cover)
- ~500k MKR minted and sold (~3% dilution of supply)
- System fully recapitalized within weeks
- The Vow mechanism converted this debt into SKY dilution—the designed recapitalization path when collateral auctions fail.

Liquidation works *when collateral auctions work*. But what if you could bypass auctions entirely? That's what the PSM does—and why it's both brilliant and dangerous.

---

### 5. Alternative Backing: The PSM Model (~1400 words)

**What this section reveals:** The PSM fundamentally changed what "backed" means—from "overcollateralized crypto" to "direct claims on centralized stablecoins."

#### 5.1 PSM vs Vaults: Two Backing Philosophies

**Table: Vault vs PSM Comparison**

| Dimension | Traditional Vault | PSM |
|-----------|-------------------|-----|
| **Collateral ratio** | 150%+ (overcollateralized) | 101% (near-parity) |
| **Revenue to protocol** | 2-5% annual stability fee | ~0.1% swap fee (minimal) |
| **Liquidation risk** | Yes (auction if unsafe) | No (always redeemable 1:1) |
| **Capital efficiency** | Low (must lock 150%+) | High (near 1:1) |
| **Decentralization** | High (crypto assets) | Low (USDC = Circle custody) |
| **Peg mechanism** | Indirect (arbitrage via mint/burn) | Direct (instant 1:1 swap) |

#### 5.2 PSM Mechanics: 1:1 Swaps

**Simplified interface:**

```solidity
interface IPSM {
    // User deposits USDC, receives DAI (1:1 minus fee)
    function sellGem(address usr, uint256 gemAmt) external;
    
    // User deposits DAI, receives USDC (1:1 minus fee)
    function buyGem(address usr, uint256 gemAmt) external;
}
```

**How it maintains peg:**

**Scenario 1: DAI > $1.00**

1. Arbitrageur mints DAI via PSM (deposit $1M USDC → receive 1M DAI)
2. Sells DAI on market for $1.02 per DAI
3. Profit: $20k (minus 0.1% fee = $1k → net $19k)
4. Result: Increased DAI supply → price falls toward $1

**Scenario 2: DAI < $1.00**

1. Arbitrageur buys DAI on market for $0.98 per DAI
2. Redeems via PSM (deposit 1M DAI → receive $1M USDC)
3. Profit: $20k (minus 0.1% fee = $1k → net $19k)
4. Result: Decreased DAI supply → price rises toward $1

**Capital velocity:** These trades execute in seconds, not hours (like vault liquidations). This is why PSM achieves ±0.1% peg stability vs ±5% pre-PSM.

#### 5.3 Why PSM Was Introduced: Black Thursday Context

**March 12, 2020 crisis :**

- ETH crashed 43% in hours
- 4,600 vaults liquidated
- Auctions failed to cover debt (70.5% couldn't reach `dent` phase per Kjaer)
- DAI price rose to $1.11 (short squeeze: everyone needed DAI to deleverage)

Governance responded with emergency parameter adjustments and debt auctions to recapitalize the system

**The problem PSM solves (procyclical → countercyclical supply), historical context (March 17, 2020 introduction):**
During crashes, *vault-based* DAI supply is *procyclical*:

- Collateral crashes → liquidations increase
- Liquidations burn DAI (remove from supply)
- DAI becomes scarce precisely when demand spikes
- Result: DAI depegs *upward* during crises

PSM makes supply *countercyclical*:

- DAI rises above $1 → arbitrageurs mint via PSM (increase supply)
- Instant, no liquidation needed
- Result: Peg restored in minutes, not days

**Historical note:** PSM was introduced March 17, 2020 (5 days post-Black Thursday) via emergency governance vote. USDC collateral went live despite decentralization concerns because *peg stability* became existential priority.

#### 5.4 March 2023: When the Backing Itself Failed (SVB Crisis)

**The scenario:** Unlike Black Thursday (collateral volatility) or typical depegs (supply/demand imbalance), the SVB crisis revealed **backing composition risk**—the collateral *itself* lost value due to off-chain failure.

**Timeline:**

| Date/Time | Event | DAI Impact |
|-----------|-------|------------|
| **March 10, 2023 (morning)** | Silicon Valley Bank (SVB) fails; FDIC seizes assets | Circle discloses $3.3B (~8% of reserves) frozen at SVB |
| **March 10 (afternoon)** | USDC depegs to $0.88 as redemption uncertainty spreads | DAI depegs to $0.88 in lockstep (60%+ USDC backing) |
| **March 11-12** | Panic across DeFi; USDC marketcap drops $10B+ in 48 hours | DAI holders unable to redeem at $1 via PSM (USDC itself impaired) |
| **March 13 (5am UTC)** | Fed/Treasury announce backstop; all SVB depositors made whole | USDC re-pegs to $1.00; DAI follows within hours |
| **March 14 onwards** | Circle confirms full redemption capacity restored | Both stablecoins return to $1.00±0.01 |

**What this event revealed:**
SVB was not a vault-liquidation failure or oracle problem—the collateral itself lost value due to off-chain institutional failure. PSM's instant redemption feature meant DAI holders and vault owners faced the same depeg risk. USDC's off-chain trust dependency became the limiting factor.

**Design lesson box:**

>The stability-decentralization trilemma exposed: Black Thursday proved pure crypto backing can't maintain peg during crashes. SVB proved centralized-stablecoin backing can't withstand off-chain shocks. Sky's response: diversified hybrid (crypto 38%, stablecoins 22%, RWA 14%). No single failure cascades system-wide, but complexity increases governance challenge.

1. **Compositional failure mode:** This wasn't a liquidation cascade (Black Thursday) or oracle failure—the *collateral itself* lost value. Liquidating USDC for DAI just concentrates the problem.

2. **Correlation risk:** DAI's peg is **coupled** to USDC's peg when USDC backs 60%+ of supply. No amount of crypto overcollateralization can hedge this.

3. **Speed of contagion:** Depeg propagated in <6 hours. Governance can't react fast enough when the backing itself fails.

4. **Off-chain legal risk:** USDC's value depends on Circle's bank relationships, FDIC insurance, Treasury interventions. These are *political* risks embedded in "stable" collateral.

**Design lesson box:**
> **The stability-decentralization trilemma:** Black Thursday proved you can't maintain peg with pure crypto backing during crashes. SVB proved you can't maintain peg with centralized backing during off-chain shocks. Sky's 2025 solution: **diversified hybrid** (crypto 38%, stablecoins 22%, RWA 14%). No single collateral failure cascades system-wide. The cost: complexity and mixed trust assumptions.

**Setup for Part II:** *"PSM solved Black Thursday's liquidation cascade but created SVB vulnerability. Part II analyzes the sustainability trade-off: Is lower revenue (0.1% PSM vs 3% vaults) and higher centralization risk (Circle dependency) worth the peg stability?"*

**Setup for Part III:** *"Governance chose USDC retention despite SVB crisis. Part III examines why: Is this pragmatic realism or mission drift? Do SubDAOs change the calculus by distributing risk across Spark (PSM), Core (crypto), and Grove (RWA)?"*

---

### 6. Terminal Backing: Global Settlement (~900 words)

**What this section proves:** Even if everything fails, DAI holders have a **deterministic claim** on collateral. This distinguishes Sky from algorithmic stablecoins with no terminal value.

#### 6.1 Emergency Shutdown Trigger

**Mechanism:**

- Requires 50,000 SKY (legacy MKR) deposited into Emergency Shutdown Module (ESM)
- SKY is **permanently burned** (irretrievable cost to trigger)
- Threshold = ~$5M at current prices (high bar to prevent abuse)

**Valid trigger reasons:**

1. Governance attack (malicious executive vote executed)
2. Oracle failure (price feeds compromised)
3. Critical smart contract vulnerability discovered
4. Black swan event (correlated collateral failure across all types)
5. Upgrade to new version (planned redeployment)

**Historical near-miss:** Black Thursday (March 12, 2020) came close to triggering ES. Governance chose emergency parameter adjustments + debt auction instead.

#### 6.2 Three-Phase Settlement Process

**Phase 1: System Freeze (Immediate)**

- All vault creation halts
- Oracle prices freeze at shutdown moment
- Ongoing auctions allowed to complete (fairness to keepers)
- Vat records final system state (snapshot)

**Phase 2: Vault Processing (Hours to days)**
Vault owners can **immediately** retrieve excess collateral:

```
excess_collateral = ink × spot - art × rate

if excess_collateral > 0:
    vault_owner.withdraw(excess_collateral)
```

Undercollateralized vaults contribute remaining collateral to DAI redemption pool.

**Phase 3: DAI Redemption (After processing period)**
DAI/USDS holders redeem for proportional share of **all collateral types**:

```
redemption_per_DAI[collateral_i] = total_collateral_i / total_DAI_supply

DAI_holder_receives = DAI_amount × Σ(redemption_per_DAI[i])
```

**Key property:** **First and last redeemers get identical rates.** No bank run dynamics. This is enforced by smart contract—you can't game redemption timing.

#### 6.3 Why This Matters: Terminal Value Floor

**Comparison to Terra/Luna (algorithmic stablecoin that failed):**

| Property | Sky DAI/USDS | Terra UST |
|----------|--------------|-----------|
| **Terminal value** | Collateral basket redemption | Zero (LUNA death spiral) |
| **Redemption guarantee** | Smart contract enforced | Mint/burn arbitrage (failed under stress) |
| **Backing location** | On-chain + legal wrappers | Purely algorithmic (no reserves) |

**Klages-Mundt theoretical context (detailed Part II):** Global Settlement serves as the "terminal period" in formal stablecoin models—the point where face value treatment of liabilities is enforced regardless of market conditions. Sky encodes this in Solidity; Terra relied on arbitrageur faith.

**The caveat:** Redemption is **pro-rata**. If system is 90% collateralized at shutdown (e.g., post-crash before recapitalization), DAI holders get $0.90 per DAI, not $1.00. This is still better than zero (algorithmic stablecoins) but worsethan guaranteed $1.00 (USDC with banking relationships).

**Example calculation (hypothetical ES after partial collateral loss):**

Assume at shutdown:

- Total DAI supply: 5B
- Collateral pool:
  - ETH: 1M ETH × $2000 = $2B
  - USDC: $1.5B
  - RWA (T-bills): $1B
  - Total: $4.5B

**System is 90% collateralized** ($4.5B backing / $5B supply)

Each DAI holder redeems for:

```
Per 1000 DAI:
- ETH: (1000 / 5B) × 1M ETH = 0.2 ETH = $400
- USDC: (1000 / 5B) × $1.5B = $300
- RWA: (1000 / 5B) × $1B = $200
Total value: $900 (not $1000)
```

**Why this still matters:** The $900 is **guaranteed and deterministic**. No governance vote needed. No trust required. The smart contracts enforce it. For DeFi, this deterministic floor is the difference between "stablecoin" and "speculative token."

#### 6.4 Post-Settlement Redeployment

**Global Settlement does NOT automatically redeploy Sky.** Protocol is open-source—anyone can fork and redeploy with modified parameters.

**Typical redeployment paths:**
Global Settlement does not automatically redeploy Sky. Protocol code is open-source—any party can fork and redeploy with different parameters. Historical precedent: Single-Collateral DAI (SCD) → Multi-Collateral DAI (MCD) transition (November 2019) used similar logic. Users could migrate via redemption into the new system.

**Historical precedent:** Single-Collateral DAI (SCD) → Multi-Collateral DAI (MCD) transition (Nov 2019) used similar logic. Old system shut down gracefully, users migrated via redemption + re-deposit in new system.

**Setup for Section 7:** Global Settlement proves backing exists at the terminal moment—but can the system survive *to* that moment without entering permanent dilution cycles? Section 7 introduces the formal framework that defines when backing is sustainable vs when it degrades.

---

### 7. Klages-Mundt Framework: What "Backed" Means Formally (~1000 words)

**What this section provides:** The mathematical vocabulary to distinguish "backed arithmetically" from "backed sustainably" from "backed in expectation."

**Scope note:** This section introduces the framework conceptually. Part II applies it to Black Thursday empirics and regime analysis. Keep this light—definitions only, no proofs.

#### 7.1 The Three Meanings of "Backed"

**1. Arithmetically backed (Vat invariant):**

```
∀ vaults: ink × spot ≥ art × rate
```

This is **always true** by construction (unsafe vaults get liquidated). The question isn't whether it holds—it's whether it means anything economically.

**2. Economically backed (auction solvency):**

```
∀ liquidations: auction_proceeds ≥ debt_owed
```

This is **conditionally true** depending on market microstructure (keeper liquidity, network throughput, oracle speed). Black Thursday proved this fails under stress.

**3. Backed in expectation (stochastic stability):**

```
E[collateral_value_tomorrow | info_today] ≥ collateral_value_today
```

This is the **probabilistic foundation** of sustainable backing. When this expectation flips negative, even perfect liquidations can't maintain solvency.

#### 7.2 Submartingales vs Supermartingales

**Submartingale (stable regime):**
Submartingale regime means "the system expects collateral value to stay stable or grow tomorrow, so backing holds in expectation." Liquidations can keep pace with value loss. Supermartingale means "the system expects collateral to lose value, so even perfect liquidations eventually can't keep up—backing degrades." This framework helps identify when mechanism design alone is insufficient.

**The critical threshold (Klages-Mundt's key result):**

There exists a **leverage ratio β^{-1}** where the system transitions from stable → unstable. Below this threshold, the stablecoin price is a **submartingale** (mean-reverts). Above it, the stablecoin price is a **supermartingale** (grows unstably).

**Intuition (not formal proof):**

- **Low leverage** (β^{-1} small): Few vaults at risk, small liquidations, ample collateral buffer → stable
- **High leverage** (β^{-1} large): Many vaults at risk, mass liquidations, demand spike for stablecoin → DAI price *rises* during crash (paradox) → forces more liquidations → spiral

**The Black Thursday paradox:**

- ETH crashed 43% → collateral lost value
- DAI *rose* to $1.11 → stablecoin gained value
- **Why?** Vault owners needed to repurchase DAI to deleverage → demand spike → short squeeze
- This is the mathematical signature of crossing into supermartingale regime

#### 7.3 How PSM and RWA Shift the Threshold

**The stability region (Klages-Mundt formalization):**

The critical threshold β^{-1} depends on:

1. **Collateral volatility** (σ): Higher σ → lower safe leverage
2. **Correlation** (ρ): Higher correlation across collateral → lower safe leverage  
3. **Liquidation speed** (τ): Slower liquidations → lower safe leverage
4. **Keeper liquidity** (L): Lower liquidity → lower safe leverage

**How Endgame architecture widens the stability region:**

| Mechanism | Effect on Parameters | Result |
|-----------|---------------------|--------|
| **PSM (USDC backing)** | Reduces effective σ (low-volatility collateral) | Raises β^{-1} threshold (more leverage sustainable) |
| **RWA diversification** | Reduces ρ (uncorrelated with crypto) | Raises β^{-1} threshold |
| **Clipper auctions** | Reduces τ (faster settlement) | Raises β^{-1} threshold |
| **L2 integration** | Increases throughput, reduces τ | Raises β^{-1} threshold |

**In English:** By mixing volatile crypto with stable USDC and uncorrelated RWA, Sky increases the amount of leverage the system can safely support before liquidation cascades become self-reinforcing.

**The trade-off formalized:**

- **Pure crypto** (2017-2020): High decentralization, narrow stability region (low β^{-1})
- **Hybrid model** (2020-2025): Lower decentralization, wide stability region (high β^{-1})
- **Endgame fragmentation** (2024+): Distributed decentralization risk, widest stability region

#### 7.4 Setup for Part II

"Part I has established the on-chain mechanisms that create verifiable backing: accounting (Vat), collateral entry (vault lifecycle), price discovery (oracles), enforcement (liquidation), and terminal settlement. These mechanisms are deterministic—they execute regardless of market conditions.

However, verifiable backing is different from sustainable backing. Mechanisms can be arithmetically correct while economically strained. The next test: can these mechanisms maintain backing when collateral prices crash, auctions overwhelm keeper liquidity, or off-chain events (like SVB) impair the backing collateral itself? Part II explores these bottlenecks."

---

### 8. The Hybrid Balance Sheet (October 2025) (~800 words)

**What this section synthesizes:** Current state snapshot showing how backing has evolved from pure crypto → emergency hybrid → mature diversified portfolio.

#### 8.1 Collateral Composition Table

**Table: Current Backing Breakdown (October 2025)**

| Collateral Type | % of Supply | Amount | SubDAO | Trust Model | Volatility | Liquidation Speed | Key Risk |
|-----------------|-------------|--------|--------|-------------|------------|-------------------|----------|
| **Crypto (ETH, WBTC, etc.)** | 38% | ~$2.6B | Core | Trustless (on-chain) | High (50%+ swings) | Fast (Dutch auction) | Correlated crash |
| **USDC (PSM)** | 22% | ~$1.5B | Spark | Circle custody | Low (<1% normal) | Instant (1:1 swap) | Centralized depeg (SVB) |
| **RWA (T-bills, bonds)** | 14% | $948M | Grove | Legal wrapper + custody | Very low | Slow (off-chain process) | Regulatory/legal |
| **Other (USDP, GUSD, etc.)** | 26% | ~$1.8B | Various | Mixed | Mixed | Mixed | Fragmentation risk |

**Total supply (October 2025):** ~$6.8B USDS (formerly DAI)

#### 8.2 The Evolution: Three Distinct Eras

**Timeline visualization:**

```
2017-2020: Pure Crypto Era
├─ ETH backing: 98%+
├─ Philosophy: Trustless > stability
└─ Crisis: Black Thursday (March 2020)
         ↓
2020-2023: Emergency Hybrid Era  
├─ USDC introduced via PSM
├─ Peak USDC: 60%+ of backing (2022)
├─ Philosophy: Stability > decentralization
└─ Crisis: SVB/USDC depeg (March 2023)
         ↓
2023-2025: Endgame Maturity
├─ Diversified: Crypto 38% / USDC 22% / RWA 14%
├─ SubDAOs distribute risk (Core/Spark/Grove)
├─ Philosophy: Pragmatic portfolio approach
└─ Status: No major crises (2023-2025)
```

**What changed between eras:**

| Dimension | Pure Crypto | Emergency Hybrid | Endgame Mature |
|-----------|-------------|------------------|----------------|
| **Largest single risk** | ETH crash (correlated) | USDC depeg (centralized) | Portfolio fragmentation |
| **Crisis response** | Manual parameter votes | PSM instant arbitrage | Automated + distributed |
Each era was shaped by the previous crisis. Pure crypto proved vulnerable to correlated crashes (Black Thursday). Heavy USDC exposure revealed centralization risk (SVB). Current diversification reflects both experiences.

#### 8.3 What "Backed" Means Across Collateral Types

**Verification matrix:**

| Collateral | How to Verify Backing | Who/What You Trust | Time to Liquidate | Failure Mode |
|------------|----------------------|-------------------|------------------|--------------|
| **ETH-A** | Query Vat state + etherscan | Ethereum consensus, oracle feeds | 6 hours (auction) | Price crash faster than liquidation |
| **USDC-A** | Query PSM reserves + Circle attestation | Circle, banking system, FDIC | Instant (swap) | Banking failure (SVB), regulatory freeze |
| **RWA** | Query Grove SubDAO + legal docs + custodian reports | Legal enforceability, custodian solvency, governance honesty | Days to weeks | Legal disputes, custodian bankruptcy, fraud |

The backing is now heterogeneous: ETH (trustless, on-chain verification), USDC (custodial, Circle attestation), and RWA (legal wrapper, off-chain custody). Verification methods differ because trust models differ. This is the current design choice.

**No single point of failure dominates** (by design). This is Endgame's core thesis: **diversified trust is more robust than pure trust**.

#### 8.5 Setup for Parts II and III

This hybrid balance sheet represents the current design choice: trade some revenue (PSM generates 0.1% vs 3% from vaults) and decentralization (USDC custody risk) for peg stability (instant PSM arbitrage). Whether this trade is sustainable under repeated crises is explored in Part II. Whether governance can manage this complexity without drift is examined in Part III.

---

### 9. Conclusion: Backing Is Necessary But Not Sufficient (~600 words)

Part I has established:

1. Where backing lives: The Vat accounting layer maintains the core invariant (ink × spot ≥ art × rate), enforced by liquidation logic. Collateral enters through Join adapters and exits through auctions or redemptions (PSM).
2. How backing is verified: Oracle infrastructure (Median → OSM → Spotter) provides the price signals that make the invariant checkable. Current composition: 38% crypto (trustless), 22% USDC (custodial), 14% RWA (legal wrapper).
3. How backing is enforced: Three mechanisms:

- Continuous enforcement: Liquidations triggered when `ink × spot < art × rate`
- Instant arbitrage: PSM swaps maintaining peg (learned from Black Thursday)
- Terminal guarantee: Global Settlement redeems DAI for proportional collateral share

4. When backing is certain: Global Settlement snapshot freezes the system and guarantees DAI holders a deterministic claim on collateral. Unlike algorithmic stablecoins (Terra, Luna), Sky encodes this floor in smart contracts.
5. How to define backing formally: The Klages-Mundt framework distinguishes three categories:

- Arithmetically backed: Vat invariant enforced by liquidation
- Economically backed: Auctions actually cover debt (sometimes fails under stress)
- Backed in expectation: Collateral expected to hold or grow (regime-dependent)

What Part I does NOT answer:

- Whether backing remains sustainable under stress: Black Thursday showed that arithmetically-backed invariants can coexist with auction failures. Part II analyzes these bottlenecks (oracle lag, keeper liquidity, network throughput, reputation cascade) that violate economic backing even when arithmetic holds.

- Whether governance can manage this complexity: SVB crisis revealed a gap between mechanism design (auctions, PSM, RWAs) and political reality (governance chose USDC retention despite revealed risk). Part III examines the coordination layer—how governance adapts parameters, how SubDAOs distribute risk, and what prevents drift toward unsustainable designs.
- Whether Endgame's diversification actually works: Theory suggests diversified backing (crypto + stablecoins + RWAs) is more robust than monolithic designs. Empirical validation awaits the next stress event.

The bottom line:

Sky's backing is verifiable and mechanically enforced. The system will never allow unsafe vaults to exist; the Vat invariant is as deterministic as Ethereum consensus. But deterministic mechanism doesn't guarantee sustainable economics or governance discipline. The next two parts expose these gaps.

---

## Appendices (Optional Additions)

### Appendix A: Glossary of Terms

(Your existing definitions from cross-article continuity—ink, art, rate, mat, spot, etc.)

### Appendix B: Contract Addresses (October 2025)

(Reference table for readers who want to verify on Etherscan)

### Appendix C: Future Work Directions

**Quantitative analyses that would complement Part I:**

1. **SVB Crisis Empirics (March 2023):**
   - PSM activity during USDC depeg (swap volumes, fee revenue)
   - DAI/USDC correlation analysis (how tight was lockstep?)
   - Governance response timing (proposal → vote → execution latency)
   - Post-crisis collateral rebalancing speed (60% → 22% USDC path)

2. **Comparative Stress Testing:**
   - Black Thursday (ETH crash) vs SVB Crisis (stablecoin depeg) vs September 2020 drawdown
   - Which collateral types showed resilience? Which amplified instability?
   - Did diversification thesis hold empirically?

3. **Oracle Delay Optimization:**
   - What's the Pareto frontier between user safety (longer delay) and liquidation effectiveness (shorter delay)?
   - Can machine learning models predict optimal delay based on volatility regime?

4. **PSM Capital Efficiency:**
   - How much keeper capital was locked during Black Thursday vs available now?
   - Does L2 integration (Arbitrum, Optimism) reduce throughput bottlenecks measurably?

These analyses would validate Endgame's architectural choices with empirical data, not just theoretical frameworks.

---

## Series Navigation

- **← You are here: Part I (Backing Mechanism)**
- → Next: Part II (Sustainability — When Stability Has to Pay for Itself)
- → Coming: Part III (Governance Evolution and Credible Neutrality)

---

## Meta Notes for Your Drafting Process

**What this outline gives you:**

1. **Clear boundaries:** Each section knows its job—don't let liquidation analysis (Part II) bleed into mechanism description (Part I)

2. **Forward pointers:** Every section sets up questions for Parts II/III without trying to answer them prematurely

3. **SVB integration:** Lighter treatment as requested (3 paragraphs in Section 5), with forward pointers to Parts II and III for deeper analysis

4. **Klages-Mundt positioning:** Introduced in Part I as *framework* (vocabulary and definitions), analyzed in Part II as *application* (regime boundaries, empirical validation)

5. **Consistent threading:** Black Thursday appears in multiple sections but always with forward pointer to Part II for full analysis

**Suggested word counts (for 8,000-10,000 word target):**

- Introduction: 800
- Section 1 (Vat): 1200
- Section 2 (Collateral): 1000
- Section 3 (Oracles): 1100
- Section 4 (Liquidation): 1300
- Section 5 (PSM + SVB): 1400
- Section 6 (Global Settlement): 900
- Section 7 (Klages-Mundt): 1000
- Section 8 (Balance Sheet): 800
- Conclusion: 600
- **Total: ~10,100 words**

**Next steps:**

1. Review this outline—does it match your vision?
2. Identify any sections that need expansion/contraction
3. I can help draft individual sections once outline is approved
4. Or proceed directly to drafting if this structure works

Let me know what adjustments you need!
