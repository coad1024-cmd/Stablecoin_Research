# The Economics of Algorithmic Stablecoin Attacks

*A quantitative analysis of profitable de-pegging strategies against dual-token systems*

---

## The Thesis

**Algorithmic stablecoins backed by endogenous collateral are structurally exploitable.** A sufficiently capitalized adversary can profitably attack these systems by combining a trigger mechanism (selling stablecoins to break the peg) with a capture mechanism (shorting the collateral token to monetize the collapse). The attack is not psychological—it is economic.

This analysis uses the DualTokenSim framework ([Calandra et al., 2024](#ref-calandra)) to quantify the conditions under which a de-peg attack becomes profitable. The findings generalize to any dual-token seigniorage design, including the architecture that failed in Terra/Luna.

---

## Part I: Theoretical Foundation

### The Dual-Token Mechanism

A dual-token algorithmic stablecoin consists of two assets:

- **Stablecoin (AS):** Target price fixed at $1, backed by the promise of redemption.
- **Collateral Token (CT):** A volatile endogenous asset used to absorb demand shocks.

The peg is maintained through a mint-burn facility: 1 AS can always be redeemed for $1 worth of CT at oracle price. When AS trades below peg, arbitrageurs burn AS to mint CT, contracting stablecoin supply and (theoretically) restoring the peg.

The mechanism works in both directions under normal conditions. The failure mode emerges under stress.

### The Death Spiral

When confidence erodes, the redemption mechanism becomes reflexive:

1. AS price falls below peg
2. Redemptions accelerate (arbitrageurs burn AS for CT)
3. CT supply inflates (each redemption mints new CT)
4. CT price collapses (supply inflation exceeds demand)
5. Redemption value falls (CT is worth less)
6. Confidence collapses further
7. Return to step 1

This is the **death spiral**—a positive feedback loop where the mechanism designed to stabilize the peg instead accelerates its destruction. The critical insight is that this loop is *deterministic* once triggered. The stabilization math, running faithfully, executes the protocol's own destruction.

### The Attacker's Position

A rational attacker does not profit from breaking the peg alone. Profit arises from **positioning against the consequences** of the peg break.

The attack structure is:

| Component | Action | Economic Effect |
|:----------|:-------|:----------------|
| **Trigger** | Large AS sell | Incurs slippage loss; breaks the peg |
| **Capture** | CT short position | Gains from collateral collapse |

The attack is profitable when:

$$\text{Short Profit} > \text{Trigger Cost}$$

This is a classic asymmetric payoff: fixed downside (slippage on the dump), variable upside (gains scale with leverage on the short).

---

## Part II: The Simulation Framework

### DualTokenSim ([Calandra et al., 2024](#ref-calandra))

The experiments build on DualTokenSim, an open-source simulator for dual-token stablecoins. The framework models:

- **Three constant-product AMM pools:** AS/USD, CT/USD, and a virtual liquidity pool (the mint-burn facility)
- **Stochastic trading:** Users trade with Gaussian-distributed order sizes, with parameters shifting under panic conditions
- **Arbitrage:** An optimizer continuously exploits price differentials across pools

The simulator captures the core dynamics of Terra-style systems: endogenous collateral backing, automated redemption, and the reflexive death spiral.

### Extensions for Attack Analysis

To model adversarial behavior, we introduced:

1. **Attacker agent:** A capitalized actor capable of executing large AS dumps and holding CT short exposure
2. **Portfolio tracking:** Time-series logging of attacker portfolio value throughout the simulation
3. **PnL decomposition:** Separation of dump losses from short gains

The core protocol mechanics remain unchanged from the original DualTokenSim implementation. The extensions are purely observational and adversarial.

---

## Part III: The Experiments

We conducted three experiments, each testing a progressively refined attack strategy.

### Experiment 1: The Raw Dump

**Hypothesis:** A large stablecoin sell, without hedging, will break the peg and allow the attacker to profit from the chaos.

**Setup:**

- Attacker capital: 500M AS
- CT short position: None
- Trigger iteration: 150,000 (simulated ~10 days into the run)

**Results:**

| Metric | Value |
|:-------|------:|
| AS price (post-attack) | ~$0.60 |
| CT price (post-attack) | ~$15 (from $80) |
| Attacker PnL | **−$87M** |

**Analysis:** The attack *works*—the peg breaks, the death spiral initiates, collateral collapses. But the attacker loses money. The slippage on selling 500M AS into a finite-liquidity pool exceeds any recoverable value.

**Conclusion:** Destruction is expensive. You cannot profit from a crash using only the asset you're crashing.

---

### Experiment 2: Short + Dump (The Soros Strategy)

**Hypothesis:** The exploitable value in a death spiral is not the stablecoin (which stabilizes around $0.50–$0.90) but the collateral token (which approaches zero). By shorting CT before triggering the dump, the attacker can capture this value.

**Setup:**

- Attacker capital: 500M AS
- CT short position: $300M notional
- Trigger iteration: 150,000

**Results:**

| Metric | Value |
|:-------|------:|
| CT price collapse | ~$80 → ~$1 (−98%) |
| Short profit | +$157M |
| Dump loss | −$89M |
| **Net PnL** | **+$68M** |

**Analysis:** The dynamics are identical to Experiment 1—same peg break, same death spiral. The difference is that the attacker is now positioned to *benefit* from the collapse rather than merely *cause* it. The short position converts the protocol's failure into the attacker's gain.

The breakeven point occurs when CT has lost approximately 60% of its value. Everything beyond that is profit.

---

### Experiment 3: Maximum Leverage

**Hypothesis:** If the death spiral is deterministic once triggered, the attacker should maximize short exposure. The trigger cost is fixed; the upside scales with leverage.

**Setup:**

- Attacker capital: 500M AS
- CT short position: $1B notional
- Trigger iteration: 150,000

**Results:**

| Metric | Value |
|:-------|------:|
| CT price collapse | ~$80 → ~$0.50 (−99%) |
| Short profit | +$507M |
| Dump loss | −$96M |
| **Net PnL** | **+$411M** |

**Analysis:** The dump cost remains approximately constant (the slippage saturates once the peg is decisively broken). But the short profit scales linearly with position size. With 3× the short exposure of Experiment 2, the attacker achieves 6× the net profit.

This is the core asymmetry: the attack has a **fixed cost** (break the peg) and a **variable upside** (capture the collapse with leverage).

---

## Part IV: Sensitivity Analysis

To generalize beyond single runs, we conducted a parameter sweep across two dimensions:

- **X-axis:** Stablecoin dump size (trigger capital)
- **Y-axis:** CT short size (capture leverage)

The resulting heatmap reveals the **profitability frontier**:

![PnL Sensitivity Heatmap](images/pnl_heatmap.png)

**Key observations:**

1. **The Loss Zone (bottom region):** Small short positions cannot overcome the dump cost. The attacker loses money regardless of trigger size.

2. **The Breakeven Line:** A diagonal threshold separates profitable from unprofitable configurations. Below this line, shorting merely offsets losses; above it, profits scale with leverage.

3. **The Profit Zone (top region):** Net PnL scales linearly with short size while trigger cost saturates. The limiting factor is not capital to break the peg—it's liquidity to short the collateral.

**Strategic implication:** The attack's feasibility depends on **CT borrowing markets**. If an attacker cannot source sufficient short exposure, the attack fails even with unlimited trigger capital.

---

## Part V: Model Limitations

The simulation makes simplifying assumptions that affect real-world applicability:

| Assumption | Model Behavior | Reality |
|:-----------|:---------------|:--------|
| **Reference asset stability** | USD price fixed at $1 | USDC/USDT can de-peg during systemic stress |
| **Binary panic behavior** | Traders switch to panic mode at 95¢ threshold | Panic is a gradient with dip buyers at psychological levels |
| **Closed market** | Price determined only by simulated pools | CEX price discovery often leads on-chain prices |
| **Zero-friction arbitrage** | Instant execution, no gas costs | Network congestion spikes during crises |
| **Infinite collateral demand** | Statistical buy orders persist at any price | Demand for failed project tokens often drops to zero |

These limitations mean the model likely *understates* attack profitability in some scenarios (panic is more severe in reality) and *overstates* it in others (short liquidity may not exist).

---

## Part VI: Conclusions

### Finding 1: Direct Attacks Are Unprofitable

A large stablecoin dump, without positioning, is a net loss. The attacker pays slippage to destroy the system and receives nothing in return. This explains why casual panic selling—while harmful—does not constitute a profitable attack.

### Finding 2: Profitability Requires Collateral Shorting

The capture mechanism is essential. The attack only becomes profitable when the attacker holds short exposure to the collateral token. The stablecoin dump is merely the *trigger*; the short is the *payoff*.

### Finding 3: The Payoff Is Asymmetric

Once the death spiral initiates, it runs to completion. This makes the attack a binary bet with capped downside (trigger cost) and scalable upside (short profit). Rational attackers will maximize leverage, not trigger size.

### The Strategic Implication

Dual-token algorithmic stablecoins are not merely *risky*—they are **structurally exploitable**. The mechanism that maintains the peg becomes the mechanism that destroys it, and this destruction can be monetized by any actor with sufficient capital and short access.

The defense is not governance or community trust—these are irrelevant at the speed of a death spiral. The defense is **exogenous collateral**: reserves that do not lose value during the crisis and cannot be minted into existence by the failing protocol itself.

---

## References

<span id="ref-calandra"></span>**[1]** Calandra, F., Rossi, F., Fabris, F., & Bernardo, M. (2024). *Algorithmic Stablecoins: A Simulator for the Dual-Token Model in Normal and Panic Scenarios*. [IEEE Access](https://ieeexplore.ieee.org/document/11114693).

<span id="ref-dualtokensim"></span>**[2]** FedericoCalandra. (2023). *DualTokenSim Repository*. [GitHub](https://github.com/FedericoCalandra/DualTokenSim).

<span id="ref-fork"></span>**[3]** Internal Research. (2026). *Attack-Modelling Fork with Adversarial Extensions*. [GitHub](https://github.com/coad1024-cmd/Stablecoin_Research/tree/main/challenge-research-coad1024/Algo-Attack-Model).

---

<div align="center">

| [Previous] | Home | [Next] |
|:---|:---:|---:|
| [Non-Volatile Collateral Design](../03_Final-submission/Design/Non-Volatile.md) | [Table of Contents](../03_Final-submission/README.md) | — |

</div>
