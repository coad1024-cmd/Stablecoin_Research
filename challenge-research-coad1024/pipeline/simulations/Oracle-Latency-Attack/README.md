# Oracle Latency Attack Simulation

**Goal:** Model the Oracle Latency vulnerability from Terra V1 to understand attack profitability.

## Attack Vector (From Terra Deep Dive §3)

Terra's oracle uses a **Weighted Median** vote from validators with a ~30 second delay.

**Attack Mechanics:**

1. Oracle reports stale price (5 blocks / ~30 seconds old)
2. Attacker observes real-time market crash (e.g., LUNA drops 20%)
3. Attacker swaps UST for "overpriced" LUNA before oracle updates
4. Attacker extracts more value than the market supports

## Model Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| `VotePeriod` | 5 Blocks (~30s) | `x/oracle` module |
| `BasePool` | $1B | Initial virtual pool size |
| `MinSpread` | 0.5% | Tobin tax minimum |
| `OracleDelay` | 30 seconds | VotePeriod |
| `PriceCrashRate` | 20% in 15s | Stress scenario |

## Files

| File | Purpose |
|------|---------|  
| `oracle_attack_sim.py` | Core simulation logic |
| `config.py` | Model parameters (from Terra Core) |
| `cost_vs_profit.py` | **Cost vs Profitability analysis** |
| `visualize.py` | Generate analysis charts |
| `monte_carlo.py` | Stochastic scenario modeling |
| `combined_attacks.py` | Multi-vector attacks (Death Spiral, Flash Loan) |
| `results/` | Output charts (PNG) |

## Generated Charts

| Chart | Description |
|-------|-------------|
| `sensitivity_analysis.png` | Profit vs crash percentage |
| `attack_timeline.png` | Oracle lag visualization |
| `capital_sensitivity.png` | Profit scaling with capital |
| `spread_impact.png` | Tobin Tax effect on profitability |

## Research Questions

1. **Breakeven:** What price drop is needed for attack profitability?
2. **Optimal Timing:** How does oracle delay affect profit window?
3. **Defense:** Can faster oracles or circuit breakers prevent this?

## References

- [Terra Backing Deep Dive](../../research/00_canonical/Terra/Backing%20Mechanism/Artifact/Terra_Backing_DeepDive.md) - Section 3
- [Terra Core x/oracle](https://github.com/terra-money/classic-core/tree/main/x/oracle)
