
---

# The Terra Protocol: Architecture of an Algorithmic Sovereign Economy

**Module Reference: The Backing Mechanism**

## Abstract

The Terra protocol (Classic) represents a distinct class of decentralized ledger architectures known as **Elastic Supply Protocols**. Unlike custodial stablecoins (e.g., USDC), which rely on legal convertibility of fiat reserves, or over-collateralized crypto-backed stablecoins (e.g., DAI), which rely on liquidation engines to maintain solvency, Terra utilizes an **Algorithmic Market Module** to manage the money supply.

The system functions as a decentralized central bank. It achieves price stability for its liability token (TerraUSD/UST) not by guaranteeing redemption, but by providing a deterministic, on-chain liquidity facility for swapping between the liability and the equity token (LUNA). This document provides a forensic architectural analysis of the **Backing Mechanism**, specifically the **Virtual Automated Market Maker (vAMM)** defined in the `x/market` module and the **Sensor Network** defined in the `x/oracle` module.

---

## Part I: Conceptual Architecture

To understand the code within `x/market`, one must first define the control theory principles governing the system. The Terra protocol is designed as a **Closed-Loop Control System**.

### 1.1 Seigniorage Shares and the Dual-Token Model

The protocol separates the functions of money into two distinct assets, creating a relationship analogous to a central bank's balance sheet:

1. **The Liability (UST):** A unit of account pegged to a fiat target (SDR/USD). The system seeks to keep the supply of UST perfectly elastic; supply must expand and contract instantly to match demand at the price of $1.00.
2. **The Equity (LUNA):** A variable-supply asset that absorbs the volatility of the system. LUNA represents the "Seigniorage Shares" of the network. It captures value when the economy grows (via swap fees and burn scarcity) and dilutes value when the economy contracts (via minting to absorb UST).

### 1.2 The Absorption Assumption

The core thesis of the backing mechanism is **Volatility Absorption**. The protocol assumes that for every unit of UST selling pressure, there exists a quantity of LUNA liquidity sufficient to absorb it.

The protocol enforces this via a mechanism called the **Market Module**. It replaces the "Cash Window" of a traditional bank with a cryptographic swap facility. Users do not trade with each other; they trade with the system state itself.

* **Expansion (Minting):** When UST > $1.00, the protocol allows users to burn $1 of LUNA to mint 1 UST.
* **Contraction (Burning):** When UST < $1.00, the protocol allows users to burn 1 UST to mint $1 of LUNA.

While often described as "Burn and Mint," the technical implementation is a **Constant Product Market Maker (CPMM)**.

---

## Part II: The Engine — The Market Module (`x/market`)

**Source Code Scope:** `classic-terra/core/x/market`

The `x/market` module is the state machine that governs the swap logic. Unlike a Decentralized Exchange (DEX) like Uniswap, the Market Module does not possess Liquidity Provider (LP) tokens or hold asset reserves. It utilizes **Virtual Liquidity Pools**.

### 2.1 The Virtual Liquidity Model

In the `x/market` KVStore, the system maintains variables that represent the *depth* of the market. These pools are mathematical constructs used solely for pricing.

The pricing mechanism is derived from the Uniswap Constant Product formula:


In the Terra source code (specifically `keeper/swap.go`), this is implemented using a square-root relationship derived from a governance parameter called `BasePool`.

#### The Constant Product ()

The constant product  is defined as the square of the `BasePool`:


* **`BasePool`**: Defined in `x/market/types/params.go`.
* *Default Value:* 50,000,000 SDR (Special Drawing Rights).
* *Role:* This parameter sets the "stiffness" of the swap curve. A higher `BasePool` simulates deeper liquidity, resulting in lower slippage for large trades. A lower `BasePool` increases slippage, making the peg more rigid but the system more volatile for large exits.



### 2.2 The State Variable: `TerraPoolDelta`

The system does not track the total supply of UST in the virtual pool directly. Instead, it tracks the *deviation* from equilibrium using a delta variable.

**Variable:** `TerraPoolDelta` ()
**Location:** `x/market/keeper/keeper.go` (KVStore Key: `TerraPoolDeltaKey`)

The virtual pool sizes for any given block are calculated dynamically:

1. **Virtual UST Pool (`TerraPool`):**


2. **Virtual LUNA Pool (`LunaPool`):**



#### Logic Flow:

* When the system is in equilibrium, . Therefore, `TerraPool` = `BasePool` and `LunaPool` = `BasePool`. The exchange rate is effectively 1:1 (ignoring oracle price).
* When a user **sells UST** (Contraction), they increase the `TerraPool` size. The system updates state: .
* This makes the `TerraPool` larger and the `LunaPool` smaller, shifting the price along the  curve.

### 2.3 The Stability Spread (Pricing Volatility)

The protocol prevents immediate depletion of reserves during a bank run by implementing a **Spread Fee**. This fee is dynamic and functions as an automatic stabilizer. As selling pressure increases, the cost of exiting the system increases.

**Function:** `ComputeSwap` in `x/market/keeper/swap.go`.

The spread is calculated using the following logic:

Which simplifies to:


* **`MinStabilitySpread`**: A hardcoded floor parameter (e.g., 0.5% or 2.0%). This ensures that even in equilibrium, there is a cost to using the protocol's liquidity.
* **The Volatility Multiplier**: The term  represents the ratio of net selling pressure to total market depth.
* *Example:* If `BasePool` is 50M and users have net-sold 25M UST (), the spread is  or 50%.
* *System Intent:* This mechanism is designed to halt a bank run by making the "redemption" of UST for LUNA prohibitively expensive as the exit queue grows.



### 2.4 The Recovery Mechanism (`PoolRecoveryPeriod`)

The protocol assumes that volatility is impulsive (short-term) rather than systemic. Therefore, the `TerraPoolDelta` is designed to decay back to zero over time. This resets the liquidity pools to their equilibrium state.

**Logic:** EndBlocker execution in `x/market/abci.go`.
**Parameter:** `PoolRecoveryPeriod` (defined in `x/market/types/params.go`), typically set to `BlocksPerDay` (approx. 14,400 blocks).

**The Decay Formula:**
At the end of every block, the protocol executes:


This creates an exponential decay half-life.

* **Engineering Consequence:** If selling pressure stops, the spread will slowly return to `MinStabilitySpread` over 24 hours.
* **Vulnerability:** If selling pressure is *sustained* at a rate matching the decay rate, the spread will never spike, allowing continuous drainage of value at a low fixed cost.

---

## Part III: The Sensor — The Oracle Module (`x/oracle`)

**Source Code Scope:** `classic-terra/core/x/oracle`

The Market Module (`x/market`) is mathematically self-contained regarding liquidity curves, but it is blind to the external exchange rate of LUNA vs. Fiat. It requires an exogenous price feed to determine how much LUNA to mint for $1 of UST. This is the role of the **Oracle Module**.

### 3.1 The Consensus Vote (`MsgAggregateExchangeRateVote`)

Terra uses its validator set as a distributed sensor network. Rather than relying on Chainlink or centralized API feeds, the protocol requires validators to actively vote on the exchange rate of LUNA against various fiat denominations (USD, KRW, SDR) in every block cycle.

#### The Vote Period

Validators do not vote in every block. They vote in windows to reduce network congestion.
**Parameter:** `VotePeriod` (defined in `x/oracle/types/params.go`).
**Value:** **5 Blocks** (approximately 30 to 35 seconds).

This introduces a critical **Latency Vector**. The price used by the blockchain is always a lagging indicator of the real-time market price, delayed by at least 30 seconds (plus block processing time).

### 3.2 The Oracle Front-Running Attack (Forensic Analysis)

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

### 3.3 The Commit-Reveal Scheme

To prevent validators from "lazy voting" (copying the votes of large validators), the system enforces a Commit-Reveal scheme.

1. **Prevote (`MsgAggregateExchangeRatePrevote`):**
In the first half of the window, a validator submits a SHA256 hash:
`Hash(ExchangeRate + Salt + ValidatorAddress)`
This commits them to a price without revealing it to the network.
2. **Vote (`MsgAggregateExchangeRateVote`):**
In the subsequent `VotePeriod`, the validator submits the plaintext `ExchangeRate` and `Salt`. The protocol hashes these and checks if they match the stored Prevote.

### 3.4 Aggregation Logic: The Weighted Median

Once votes are revealed, the protocol must distill a single "Reference Price" from the noisy data.

**Function:** `Pb.Ballot.Power()` in `x/oracle/keeper/ballot.go`.

The system does not use the Mean (Average), which is susceptible to skewing by extreme outliers. It uses the **Weighted Median**:

1. Votes are sorted by price.
2. The "Power" of each vote is the validator's bonded stake (LUNA).
3. The protocol iterates through the sorted list until the cumulative stake power exceeds 50% of the total voting power.
4. The price at this threshold is the Reference Price.

**Security Implication:** To manipulate the Oracle price, an attacker would need to control >50% of the active staking power (billions of dollars), making it resistant to minority collusion.

### 3.5 The Reward Band and Slashing

The protocol aligns incentives using a "Schelling Point" game.
**Parameter:** `RewardBand` (e.g., 0.02 or 2%).

* **Winners:** Validators whose votes fall within the `RewardBand` (standard deviation) of the Weighted Median receive a portion of the swap fees collected by the Market Module (`RewardPool`).
* **Losers:** Validators who vote outside the band (or fail to reveal) are recorded as a "Miss."
* **Slashing:** If a validator misses too many votes within a `SlashWindow`, they are jailed and their stake is slashed (typically 0.01%). This forces high-availability operation of price feeder bots.

---

## Part IV: Execution Flow — The `MsgSwap` Lifecycle

To fully document the backing mechanism, we must trace the atomic execution of a swap transaction where a user redeems UST for LUNA (peg defense).

**Scenario:** User sends `MsgSwap` to burn 1,000 UST and mint LUNA.

### Step 1: Ingress and Validation

The transaction enters the mempool and is processed by the `x/market` `MsgServer`.
**Code:** `x/market/keeper/msg_server.go`  `Swap`.

The keeper validates:

* The `OfferCoin` is valid (UST).
* The `AskDenom` is valid (LUNA).
* The User has sufficient balance.

### Step 2: Price Resolution

The Market Keeper calls the Oracle Keeper to retrieve the exchange rate.
**Code:** `oracleKeeper.GetTerraExchangeRate(ctx, denom)`.

* *Critical Constraint:* This function returns the price established at the *end of the previous VotePeriod*. If the real-world price has crashed 20% in the last 10 seconds, this function returns the *old, higher* price.

### Step 3: Swap Computation (`ComputeSwap`)

The keeper calculates the amount of LUNA to mint.

1. **Retrieve State:** Load `TerraPoolDelta` () and `BasePool`.
2. **Calculate Constant Product ():** .
3. **Determine Virtual Pools:**
4. **Calculate Output (Constant Product Logic):** The protocol uses the standard AMM logic:
5. **Calculate Spread:**
6. **Final Output:**



### Step 4: State Update and Asset Movement

1. **Update Delta:** The `TerraPoolDelta` is increased by the `OfferAmount` (1,000 UST).
`k.SetTerraPoolDelta(ctx, delta.Add(offerAmount))`
2. **Burn Liability:** The `x/bank` module burns 1,000 UST from the user's address.
`bankKeeper.BurnCoins(ctx, ...)`
3. **Mint Equity:** The `x/bank` module mints `MintAmount` LUNA to the user's address.
`bankKeeper.MintCoins(ctx, ...)`
4. **Treasury Handling:** The `SpreadFee` is sent to the `Oracle` module to reward validators.

### Step 5: EndBlocker (Liquidity Reset)

At the end of the block, the `x/market` EndBlocker triggers the decay function.
`k.SetTerraPoolDelta(ctx, delta * (1 - decay))`
This prepares the system for the next block, slightly lowering the cost of entry/exit for future users.

---

## Part V: Analysis of System Parameters

The behavior of the Terra backing mechanism is entirely deterministic based on the configuration of specific governance parameters. A technical audit of the system requires analyzing these values.

| Parameter | Module | Go Variable | Function/Impact |
| --- | --- | --- | --- |
| **BasePool** | `x/market` | `BasePool` | **Liquidity Depth.** Defines the slope of the constant product curve. Increasing this parameter (via governance) flattens the curve, reducing slippage and effectively increasing the minting capacity of the system per block. |
| **PoolRecoveryPeriod** | `x/market` | `PoolRecoveryPeriod` | **Memory Duration.** Determines how long the system "remembers" a trade. A short period resets liquidity quickly; a long period keeps spreads high during sustained volatility. |
| **MinStabilitySpread** | `x/market` | `MinStabilitySpread` | **Base Tax.** The minimum cost of using the algorithmic swap. |
| **VotePeriod** | `x/oracle` | `VotePeriod` | **Sensor Latency.** The granularity of price updates. This is the primary vector for "Front-Running" attacks where arbitrageurs exploit the difference between CEX prices and the lagging on-chain price. |
| **RewardBand** | `x/oracle` | `RewardBand` | **Consensus Tolerance.** How much disagreement is allowed between validators regarding the price of assets. |

## Conclusion

The Terra (Classic) protocol backing mechanism is a sophisticated implementation of control theory applied to monetary economics. It replaces the discretionary open market operations of a central bank with a deterministic, code-based **Virtual Automated Market Maker**.

The system relies on the interaction between the **Sensor (Oracle)** and the **Actuator (Market Swap)**. Stability is probabilistically maintained by the **Spread Fee**, which functions as a feedback loop to dampen oscillation (volatility). The system's solvency is not enforced by asset reservation, but by the assumption that the `x/market` parameters (`BasePool`, `RecoveryPeriod`) can be tuned to ensure that the rate of LUNA dilution never exceeds the rate of value capture from the ecosystem's growth.

---

### Notes for the Researcher

This document avoids historical analysis of the May 2022 de-peg event to adhere to the "Reference Document" constraint. However, for research purposes, it is vital to note that **Proposal 1164** modified the `BasePool` and `PoolRecoveryPeriod` parameters.

* **Pre-1164:** `BasePool` was 50M SDR.
* **Post-1164:** `BasePool` was increased to 100M SDR.

Referring to the formulas in **Section 2.3**, doubling the `BasePool` implies that for the same amount of selling pressure (), the Spread is halved. This modification mathematically reduced the system's "damping" force, allowing for faster capital flight at lower cost. This correlation between parameter configuration and system failure is the primary subject of study for algorithmic stability researchers.