# De-Peg Simulation Results

Scenario: Attacker tries to hold LUSD at $0.90 for 48 hours.

|   time_hours |   base_rate |   redemption_price |   attacker_cost |   total_redeemed |
|-------------:|------------:|-------------------:|----------------:|-----------------:|
|      47.8333 |   0.0940985 |           0.901803 |     6.83617e+06 |      6.83617e+07 |

## Interpretation
As the attacker sells to suppress the price, arbitrageurs buy and redeem.
This spikes the **Base Rate**, making redemption more expensive.
Eventually, the Redemption Price drops below $0.90 (Fee > 10%).
At this point, arbitrage stops, and the attacker can hold the peg with zero cost (assuming no other buyers).
However, the initial cost to push the rate that high is significant.
