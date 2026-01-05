## Liquity V2 Mechanism Design Review



Omer Goldberg
```
omer@chaoslabs.xyz

```


Shai Kritz

```
shai@chaoslabs.xyz

```


Barry Fried
```
barryfried@chaoslabs.xyz

```


Yonatan Haimowitz

```
haimo.yonatan@chaoslabs.xyz

```

October 2024


# **Contents**

1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

2 Simulation Logic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.2 Mathematical Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.3 Fitting the Parameters Using Ordinary Least Squares (OLS) . . . . . . . . . . . . . . 3
3 Interest Rate Logic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.1 Base Rate Derivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.2 Determining the External Market(s) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.3 Cox-Ingersoll-Ross Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
4 Trove Logic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
4.1 Initial Interest Rate Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

4.2 Initial LTV Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

4.3 Leverage Demand . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.4 Borrowing Demand Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
4.5 Analysis of Scenarios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
4.6 Borrowing Demand Scalar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
4.7 New Trove Owners . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

4.8 Stability Pool and Base Rate Arbitrage . . . . . . . . . . . . . . . . . . . . . . . . . . 10
5 Parameters and Protocol Logic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
5.1 Stability Pool Yield Split . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
5.2 Minimum Borrow Rate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

5.3 Redemption Fee . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
5.4 Ordered Set of Troves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

5.5 Target Debt in Front . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
5.6 Global Redemption Risk . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
5.7 Lowering Interest Rates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
5.8 BOLD Above Peg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
5.9 Monte-Carlo Runs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

6 Simulation Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

6.1 Sweep Parameter Combinations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
6.2 Key Derived Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
6.3 Arbitrage Agent Elasticity and Speed of Redemption Fee Decay . . . . . . . . . . . . 15
6.4 Aggressiveness in Borrowing Demand and Speed of Redemption Fee Decay . . . . . . 17
6.5 Elasticity of Stability Pool Coupled with Elasticity of Trove Owner Interest Rate Adjustments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
6.6 Protocol Incentives and Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

6.7 Modeling Additional Trove Operations . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
7 Results and Insights . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
7.1 Implementing a Minimum Interest Rate . . . . . . . . . . . . . . . . . . . . . . . . . . 26
7.2 BOLD Downward Price Pressure and Redemption Risks: Less Aggressive Redemption
Fees . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

7.3 Modeling Different LSTs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
8 Appendix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30


1


### **Disclaimer**

This document is purely informational and does not constitute an invitation to acquire any security, an
appeal for any purchase or sale, or an endorsement of any financial instrument. Neither is it an assertion of
the provision of investment consultancy or other services by Chaos Labs Inc. References to specific securities
should not be perceived as recommendations for any transaction, including buying, selling, or retaining
any such securities. Nothing herein should be regarded as a solicitation or offer to negotiate any security,
future, option, or other financial instrument or to extend any investment advice or service to any entity in
any jurisdiction. The contents of this document should not be interpreted as offering investment advice or
presenting any opinion on the viability of any security, and any advice to purchase, dispose of or maintain
any security in this report should not be acted upon. The information contained in this document should
not form the basis for making investment decisions.
While preparing the information presented in this report, we have not considered individual investors’ specific
investment requirements, objectives, and financial situations. This information does not account for the
specific investment goals, financial status, and individual requirements of the recipient of this information,
and the investments discussed may not be suitable for all investors. Any views presented in this report
by us were prepared based on the information available when these views were written. Additional or
modified information could cause these views to change. All information is subject to possible rectification.
Information may rapidly become unreliable for various reasons, including market or economic changes.


2


### **1 Introduction**

In decentralized finance (DeFi), ensuring stability and efficiency in collateralized debt position (CDP) stablecoin protocols is essential for maintaining user confidence and long-term sustainability. Liquity V2, a
decentralized borrowing protocol, has gained recognition for its innovative autonomous interest rate mechanism, which allows users to freely and continuously determine their own interest rates. Rates will be
dynamically adjusted in response to potential redemptions to maintain system resilience, particularly when
the market perceives the stablecoin as being worth less than $1. As the DeFi landscape evolves, the challenge of adapting these mechanisms to fluctuating market conditions while preserving decentralization and
minimizing risk remains critical.
This paper presents a comprehensive design review of Liquity V2, with a focus on its interest rate and
redemption mechanisms, as well as the stability pool dynamics that shape borrowing demand, interest rates,
and system incentives. The primary objective is to simulate and analyze the interactions between key
variables—such as trove owner behavior, interest rate adjustments, and redemption fees—to evaluate the
system’s robustness. Through detailed scenario analysis and stress testing, the paper aims to provide rec
- mmendations for optimizing protocol parameters, balancing user participation incentives, and mitigating
adverse outcomes during periods of market stress.

### **2 Simulation Logic**


**2.1** **Background**


**Stochasticity (Ornstein-Uhlenbeck Process)**


The Ornstein-Uhlenbeck (OU) process is a continuous-time stochastic process widely used to model the
mean-reverting behavior of financial variables, leveraging historical data perceived in the relevant field. In

- ur instance, it is particularly useful in modeling the expected externally-priced interest rate behavior, as
well as the expected external leverage demand within the system, in an effort to apply theoretical real-world
scenarios with the dynamics perceived in the Liquity system with varying parameter values. We indicate
that deviations from the mean are temporary and the spread will revert to its average level over time.


**2.2** **Mathematical Background**


The OU process is defined by the following stochastic differential equation (SDE):


_dXt_ = _θ_ ( _µ −_ _Xt_ ) _dt_ + _σdWt_


Where:


  - _Xt_ is the variable of interest at time _t_


  - _θ_ is the rate of mean reversion


  - _µ_ is the long-term mean level


  - _σ_ is the volatility parameter


  - _Wt_ is a Wiener process or standard Brownian motion


**2.3** **Fitting the Parameters Using Ordinary Least Squares (OLS)**


To fit the parameters of the OU process, we discretize the SDE and use ordinary least squares (OLS)
regression on the discretized version, formally denoted as the Euler-Maruyama method.


3


**Discretized Version of the OU Process**


The discretized version of the OU process over short time intervals ∆ _t_ is given by:



_Xt_ +∆ _t_ = _Xt_ + _θ_ ( _µ −_ _Xt_ )∆ _t_ + _σ√_


where _ϵt ∼N_ (0 _,_ 1) is a n.i.i.d. random variable.
Rearranging terms, we get:


_Xt_ +∆ _t −_ _Xt_ = _θ_ ( _µ −_ _Xt_ )∆ _t_ + _σ√_


This can be written as:



∆ _tϵt_


∆ _tϵt_



∆ _Xt_ = _θ_ ( _µ −_ _Xt_ )∆ _t_ + _σ√_


where ∆ _Xt_ = _Xt_ +∆ _t −_ _Xt_ .


**OLS Regression**


To fit the parameters _θ_ and _µ_ using OLS, we define:


∆ _Xt_ = _α −_ _βXt_ + _ηt_


Where:


  - _α_ = _θµ_ ∆ _t_


  - _β_ = _θ_ ∆ _t_



∆ _tϵt_




- _ηt_ = _σ√_



∆ _tWt_



We can estimate _α_ and _β_ by performing OLS regression on the observed data. The parameters of the OU
process can then be recovered as:


_θ_ = _[β]_

∆ _t_


_α_
_µ_ =
_θ_ ∆ _t_


2

~~�~~ _ηt_

_σ_ =

            - _n_ ∆ _t_

Where _n_ is the number of observations.

### **3 Interest Rate Logic**


**3.1** **Base Rate Derivation**


The Base Rate _ρt_ can be defined as the effective market-priced interest rate outside of the Liquity system
at a given time _t_ . As a result, the user-set interest rate behavior within the Liquity V2 system is generally
expected to hover around _ρt_, given the limitations otherwise employed through redemption events if the
rates are deviated too much from the market price, implying arbitrage.
The Base Rate _ρt_ represents the effective market-priced interest rate outside of the Liquity system at a
given time _t_ . Consequently, user-set interest rates within the Liquity V2 system are generally expected to
align closely with _ρt_ . Significant deviations from this market rate are mitigated by redemption events, which
enforce adjustments and prevent arbitrage opportunities.


4


**3.2** **Determining the External Market(s)**


We leverage aggregate market data from Aave v2 and v3 protocols over the past year to determine the DeFi
Base Rate. This includes a 14-day smoothed weighted average rate to provide a stable continuous rate that
filters out short-term noise from inflows and outflows. The data is gathered from all significant stablecoin
markets on Aave, with the aggregation performed as follows:



_N_

 - _i_ =1 _[W][i]_ [(] _[t][ −]_ _[k]_ [∆] _[t]_ [)] _[R][i]_ [(] _[t][ −]_ _[k]_ [∆] _[t]_ [)]

- ~~�~~ _Ni_ =1 _[W][i]_ [(] _[t][ −]_ _[k]_ [∆] _[t]_ [)]







_ρt_ = [1]

_T_



_T/_ ∆ _t_



_k_ =0



Where _Ri_ ( _t_ ) is the interest rate of the _i_ th stablecoin market at time _t_, _Wi_ ( _t_ ) is the relative size of market _i_
at time _t_, _N_ is the total number of markets considered, ∆ _t_ is the time interval for smoothing (e.g., daily),
and _T_ is the smoothing period (14 days).
While DeFi protocols such as MakerDAO provide a governance-configured deterministic “savings rate,”
formally known as the Dai Savings Rate (DSR), there are multiple fundamental issues in using it to define

_ρ_ :


1. **Size** : With about $1B locked in the DSR, it is just a fraction of the cumulative deposits on the Aave
Protocol, which amount to $3B.


2. **Market-Priced Fluctuations** : Interest rates on Aave actively represent market sentiment in real
time, allowing the variance to be freely modeled and realized accordingly during large spikes or drawdowns in demand.


Therefore, we leverage the weighted aggregate stablecoin borrow APY on Aave v2 and v3 as the historical
data used in Ordinary Least Squares (OLS) regression, determining the optimized parameter values for
the modified Ornstein-Uhlenbeck process, known as the Cox-Ingersoll-Ross (CIR) model, to model the rate
accordingly.


Figure 1: Aave V2/V3 Cumulative Stablecoin Liquidity and DSR over time


5


Figure 2: Weighted Aggregate Stablecoin Borrow APY Aave V2 & V3 Ethereum


**3.3** **Cox-Ingersoll-Ross Model**


The Cox-Ingersoll-Ross (CIR) model is an important tool in finance for modeling interest rates. As a modified
version of an Ornstein-Uhlenbeck process, the CIR model incorporates a square root term to ensure nonnegativity and heteroskedasticity. The discretized version of the CIR model can be expressed using the
following equation for a given time step ∆ _ρt_ :



_ρt_ +∆ _rt_ = _ρt_ + _θ_ ( _µ −_ _Xt_ )∆ _t_ + _σ_ _[√]_ ~~_ρ_~~ _t√_ ∆ _tϵt_


where _ϵt ∼N_ (0 _,_ 1) is a standard n.i.i.d. random variable, such that:



∆ _ρt_ = _θ_ ( _µ −_ _Xt_ )∆ _t_ + _σ_ _[√]_ ~~_ρ_~~ _t√_



∆ _tϵt_



Key characteristics of the CIR model include its ability to ensure non-negativity and heteroskedasticity in
the interest rate process. The term _[√]_ ~~_ρ_~~ _t_ ensures that the interest rate _rt_ remains non-negative, a significant
advantage over models like the Vasicek model, which do not inherently prevent negative interest rates.
Additionally, the presence of _[√]_ ~~_ρ_~~ _t_ in the variance term means that the model accounts for changing variability
in interest rates. When _ρt_ is close to zero, the impact of the random shock term _ϵt_ is dampened, aligning
with real-world observations where very low interest rates tend to exhibit lower volatility.

### **4 Trove Logic**


**4.1** **Initial Interest Rate Distribution**


In the Liquity V2 system, trove owners have the autonomy to set their own interest rates, constrained
by redemption requirements. We define the initial distribution of interest rates as a normal distribution
_r ∼_ _N_ ( _µ, σ_ [2] ), centered around the initial optimized interest rate such that _ρ_ 0 = _µ_ .


6


**4.2** **Initial LTV Distribution**


To model the distribution of Loan-to-Value ratios (LTVs), which represents the ratio of debt to collateral,
we employ an approximately normal Beta distribution _LTV ∼_ _B_ ( _α, β_ ). The parameters _α_ and _β_ - f the Beta
distribution are chosen to match the desired LTV distribution. For approximating a normal distribution, we
set _α_ = _β_, thereby implicitly setting _µ ≈_ 0 _._ 5, given the confined distribution within the [0 _,_ 1] range, with a
variance of 1
4(2 _α_ +1) [. This distribution is further adjusted to adhere to the maximum LTV constraint allowed]
within the protocol, typically 91%, thereby shaping user behavior accordingly.


**4.3** **Leverage Demand**


_λ_ is a normalized value representing the global demand for leverage among participants contributing to the
borrowing of stablecoins. This demand is modeled as an Ornstein-Uhlenbeck (OU) process, with parameters
fitted based on historical funding rates observed on ETH/USDT Binance Perpetual Futures (Perps).


**Historical Leverage Demand**


The historical leverage demand is defined as the normalized equivalent of the 8-hour funding rate on Binance,
expressed as:


_Funding_ ~~_R_~~ _atet_
_λt_ =
max _t′∈_ [0 _,T_ ]( _Funding_ ~~_R_~~ _atet′_ )


Here, _λt_ represents the normalized funding rate at time _t_, scaled by the maximum funding rate observed

- ver the period [0 _, T_ ]. This normalization ensures that _λt_ ranges between [ _−_ 1 _,_ 1] and provides a standardized
measure of leverage demand.
The funding rate ( _Funding_ ~~_R_~~ _atet_ ) reflects the rate at which users are willing to pay to long or short ETH. It
captures the cost or reward of maintaining a leveraged position, indicating the market’s appetite for leverage

- ver time. The traditional binary nature of the 8-hour funding rate, which is either positive or negative
above a minimal threshold, simplifies the representation by focusing on the directional demand for leverage
rather than precise deviations from the basis.


Figure 3: Historical Leverage Demand (Binance ETH/USDT Perpetual Contracts)


7


**4.4** **Borrowing Demand Function**


We define the infinitesimal change in borrowing demand at a given timestep, _dλ_ ˜ _i,t_, as a function of the global
leverage demand, _λt_, and the relative difference between the borrower’s interest rate, _ri,t_, and the base rate,
_ρt_ . This approach is crucial in isolating the effective demand for borrowing on Liquity from the rest of
the market. By considering both the interest rate employed by the user relative to the global rate, we can
capture the advantage of borrowing on Liquity compared to the global market. Additionally, by accounting
for the global demand for leverage as a whole, we obtain a comprehensive view of the borrowing dynamics.
The following differential equation expresses the model:



˜ _[BOLD]_
_dλi,t_ = _λt ×_ _[ρ][t][ ×]_ _USD_



_USD_ _[−]_ _[r][i,t]_



_dt_
_ri,t_



where _i_ indexes the specific trove, and _BOLD/USD_ indicates the market price of BOLD. This component
is critical as it defines the market value of the obtained capital after swapping minted BOLD on the open
market.
To simulate troves adjusting their debt positions over time based on their comfort LTV _LTVc,i_, we begin
by having all troves open positions at time˜ _t_ 0 at their respective _LTVc,i_ . Each trove’s borrowing demand
_λi,t_ is thus inherently influenced by their respective interest rate _ri,t_ . This borrowing demand is effectively
adjusted over time according to an exponentially decaying function with respect to the trove’s LTV, and is
bounded by a maximum LTV _max_ ~~_L_~~ _TV_ .
At each time _t_, the LTV of trove _i_ is updated by adding the value of _λ_ [˜] _i,t_ to its LTV at the previous time
step _t −_ 1. Formally, this can be expressed as:


_∀LTVt < max_ ~~_L_~~ _TV,_ _LTVi,t_ = _LTVi,t−_ 1 + _dλ_ [˜] _i,t_


Whereby each trove _i_ initially starts with _LTVi,t_ 0 = _LTVc,i_ . The borrowing demand is normalized to an
infinitesimally small value _dt_, which is given by _[T]_ _n_ [, where] _[ T]_ [ is the total time of the simulation and] _[ n]_ [ is the]

number of time intervals. This normalized demand is then added to the LTV of each trove at the previous
time step, provided that the LTV remains below the maximum threshold _max_ ~~_L_~~ _TV_ .
In practical terms, this means that the relative increase or decrease in a borrower’s LTV will depend on their
current LTV. For example, a borrower with an LTV of 0 _._ 8 at _t −_ 1 will experience a smaller relative change
compared to a borrower with an LTV of 0 _._ 5, assuming both face the same interest rates. This is because the
effective increase in their borrowing position decreases as their LTV increases, following an exponentially
decaying pattern.
By dividing _LT Vdλ_ [˜] _i,t_ [, we ensure that the relative adjustment in the trove’s debt size naturally decays with the]
size of the position at _t −_ 1. This reflects a more gradual adjustment for troves with higher initial LTVs,
maintaining stability in the system over time.


**4.5** **Analysis of Scenarios**


We consider four distinct scenarios based on the signs of _λt_ and the term - _ρt ×_ _[BOLD]_ _USD_ _[−]_ _[r][i,t]_ - :


  - **Scenario 1:** _λt >_ 0 **and** _ρt ×_ _[BOLD]_ _USD_ _[−]_ _[r][i,t][ >]_ [ 0]

_dλ_ [˜] _i,t >_ 0
In this scenario, there is positive demand for leverage, and borrowing costs through troves are advantageous compared to alternative lending protocols. This results in an increase in borrowing demand.


  - **Scenario 2:** _λt >_ 0 **and** _ρt ×_ _[BOLD]_ _USD_ _[−]_ _[r][i,t][ <]_ [ 0]

_dλ_ [˜] _i,t <_ 0
Despite positive leverage demand, borrowing costs through troves are higher than the base rate. Users
will reduce their borrowing demand and seek more cost-effective leverage strategies.


  - **Scenario 3:** _λt <_ 0 **and** _ρt ×_ _[BOLD]_ _USD_ _[−]_ _[r][i,t][ >]_ [ 0]

_dλ_ [˜] _i,t <_ 0
Here, negative leverage demand indicates market risk aversion or pessimism. Even with advantageous


8


borrowing costs through troves, users are cautious about taking on additional debt due to potential
risks, and they are repaying their debts as a consequence.


  - **Scenario 4:** _λt <_ 0 **and** _ρt ×_ _[BOLD]_ _USD_ _[−]_ _[r][i,t][ <]_ [ 0]

_dλ_ [˜] _i,t <_ 0
Despite negative leverage demand, higher borrowing costs through troves compared to the market
compel users to reduce their borrowing demand. The absolute value of the interest rate differential is
considered in this scenario.


By examining these scenarios, we gain insight into the nuanced behaviors of users under varying market
conditions and their influence on borrowing demand. This approach provides a detailed understanding

- f the dynamics shaping borrowing behavior in response to changes in leverage demand and interest rate
differentials.


**4.6** **Borrowing Demand Scalar**


To adequately represent the various behavioral tendencies of users within the protocol, we define a scalar
_η ∈_ R [+] . This scalar serves as a measure of the level of aggressiveness in user behavior within the system.
By adjusting _η_, we can model and analyze how the system performs under different scenarios, ranging from
conservative to aggressive user strategies. This allows us to capture the full spectrum of possible interactions
and their impacts on the system’s stability and performance.
Plotting the relative change in LTV with varying scalar values, and assuming _dt_ = 1 day:


Figure 4: Daily Relative Change in LTV, _λ_ = 20%, _ri_ = 15%, _ρ_ = 10%


As _λ_ and _ρ_ scale, while the respective LTV of a user remains on the lower end, the relative change in LTV
will scale accordingly, converging at a faster rate as LTV approaches the maximum. The scalar _η_ amplifies
this effect, representing the aggressiveness of user behavior.
User behavioral changes based on the difference between _ρ_ and _ri_ are critical. This is characterized by
the LTV increasing as a function of the global leverage demand, the absolute deviation between rates, and
the overall aggressiveness of users within the Liquity system. The parameter _η_ plays a crucial role in this


9


context, enhancing the sensitivity of LTV changes to these factors and providing a comprehensive view of
the system’s response under various user behaviors.


**4.7** **New Trove Owners**


The system initializes all positions at time _t_ 0 based on an initial distribution of Loan-to-Value (LTV) ratios.
It adjusts debts according to borrowing demand, modifying the effective LTV based on changes in borrowing
demand and ETH price fluctuations. To model collateral inflows over time, new positions are initialized

- r existing positions are closed at intervals determined by the relationship between _ρt_ and the respective
interest rate of a trove owner _ri_, reflecting a percentage change in the total debt within the system. These
new positions adhere to distributed comfort levels of LTV and are subject to respective interest rates as a
function of targeted debt _D_ . Mathematically, this can be expressed as:







_Dt_ = _Dt−_ 1 _×_








_[BOLD]_
1 + _[ρ][t][ ×]_ _USD_



_USD_ _[−]_ _[r][i,t]_



_ri,t_



This model captures the behavior of new users who mint BOLD to generate yield within the protocol. When
the conditions are favorable, characterized by a positive deviation between _ρt_ and the respective interest
rates, these users are incentivized to take on new debt to maximize their returns. Conversely, in adverse
conditions, where the deviation is negative, these users are likely to revert their course, closing their positions
to avoid unfavorable outcomes.


**4.8** **Stability Pool and Base Rate Arbitrage**


To realistically model the inflows and outflows to and from the stability pool, given by the yield deviation
from the base rate, an aggregate SP agent deposits BOLD if _SP_ ~~_A_~~ _PY > ρ_, and withdraws funds otherwise.
The size of the deposited/withdrawn amount is randomized with an expected value proportional to the
relative difference between the yield and the base rate.
Defining a random variable ∆ _SP_ ( _t_ ) that represents the net change (deposit or withdrawal) in the Stability
Pool at time _t_, the decision to deposit or withdraw is modeled as:



∆ _SP_ ( _t_ ) =



E[ _SP_ ~~_A_~~ _PY_ ( _t_ ) _−_ _ρ_ ( _t_ )] _· Z_ if _SP_ ~~_A_~~ _PY_ ( _t_ ) _> ρ_ ( _t_ )

- _−_ E[ _ρ_ ( _t_ ) _−_ _SP_ ~~_A_~~ _PY_ ( _t_ )] _· Z_ if _SP_ ~~_A_~~ _PY_ ( _t_ ) _≤_ _ρ_ ( _t_ )



where _Z_ is a n.i.i.d random variable that captures the stochasticity of the deposit/withdrawal size, following
a distribution centered around the expected difference E[ _SP_ ~~_A_~~ _PY_ ( _t_ ) _−_ _ρ_ ( _t_ )].
Regarding the newly minted BOLD as a function of _λ_ [˜] _t_, we adopt probabilistic assumptions analogous to
those used in the interest rate adjustment process. This approach ensures that each user’s yield optimization
coincides precisely with the timing of the interest rate adjustment. Consequently, the aggregate SP agent
will allocate the newly generated capital into the SP for all _ri < ρ < SP_ ~~_A_~~ _PY_ at a given time _t_ . In other
words, for all borrowers who expand their debts, the additional BOLD will be absorbed by the SP as long
as _ρ < SP_ _APY_ .

### **5 Parameters and Protocol Logic**


**5.1** **Stability Pool Yield Split**


In the Liquity V2 design, the system aims to efficiently and scalably incentivize the stability pool by directing
a fixed percentage of the aggregate interest into it. This approach helps the stability pool maintain a relative
percentage of backing that aligns with the underlying risks of the protocol.
When there is high demand for leverage on the underlying collateral asset, the expected relative aggregate
interest rate paid by trove owners will increase due to the implied redemption risk. Consequently, this results
in a higher relative and absolute yield for the stability pool. Conversely, during periods of low demand for
leverage, trove interest rates will decrease, leading to a smaller relative stability pool size.


10


The percentage of the total revenue allocated to the stability pool, denoted as % _SP_, is crucial for defining
the optimal stability pool size under adverse conditions. This parameter needs to be examined from the
perspective of the various agents involved to ensure appropriate incentives during different market scenarios.


**5.2** **Minimum Borrow Rate**


The minimum borrow rate _rmin_ is defined at the protocol level as the minimum borrow rate for which a
respective trove owner can take on. With the introduction of automated interest rate strategies with respect
to redemption risk as a function of the BOLD oracle price, we examine the effect of potential outcomes under
various minimum borrow rate values.


**5.3** **Redemption Fee**


Much like Liquity V1, in order to create a dynamically bounded game-theoretical mechanism to deter users
from taking advantage of the system’s market-priced leniencies, such as setting interest rates that are too
low, Liquity V2 introduces a similar redemption mechanism that effectively deters the price from going
below a specific threshold, subject to the effective redemption fee and the democratized constraint within
the system. This works by permissionlessly incentivizing any external actor to maintain the system stability
by buying up discounted BOLD and redeeming for user collateral at a $1 fixed rate, subject to a dynamic
redemption fee _ft_ at some time of redemption _j_ .


_f_ ( _tj_ ) = _fmin_ + _b_ ( _tj_ )


Where _fmin_ is the minimum redemption fee, and _b_ ( _tj_ ) is a dynamic fee component that scales with respect
to the redeemed amount _m_ relative to the total supply _n_, subject to a scaling parameter _α_ :


_b_ ( _tj_ ) = _b_ ( _tj−_ 1) + _α ×_ _[m]_

_n_

For instance, assuming _fmin_ = 0 _._ 5% and _α_ = 0 _._ 5, the dynamic redemption fee linearly scales as follows:


Figure 5: Dynamic Redemption Fee Increase


Thereby calculating the effective collateral _c_ - btained with respect to the oracle price in USD _pc_ ( _t_ ) as follows:


11


_c_ = _m × pc_ ( _tj_ ) _×_ (1 _−_ _f_ ( _tj_ ))


**Redemption Fee Decay**


On the contrary, the dynamic fee component _b_ ( _t_ ) decays exponentially over time subject to some decay speed
parameter _β_ that dictates how fast the fee decays:


_b_ ( _ti_ ) = _b_ ( _ti−_ 1) _× β_ [∆] _[t]_


Where ∆ _t_ is the time span (modeled as hours) at which the dynamic fee decays over time. In the plot below,
we model various _β_ values, subject to some half-life, indicating the speed of fee decay. Note that Liquity V1
employed a _β_ value with a half-life of 12 hours, or approximately 0.944.


Figure 6: Dynamic Redemption Fee Decay wrt Time for Different _β_ Values


**5.4** **Ordered Set of Troves**


Unlike Liquity V1, where redemption queue ordering is defined with respect to the collateral ratio of the
user in Last In, First Out fashion (LIFO), Liquity V2 orders troves with respect to the respective interest
rate of the user.
Let _Q_ = _{π_ 1 _, π_ 2 _, . . ., πn}_ such that _r_ ( _π_ 1) _≤_ _r_ ( _π_ 2) _≤_ _. . . ≤_ _r_ ( _πn_ ), with each trove _π ∈_ _Q_ having an associated
interest rate _r_ ( _π_ ) and debt size _D_ ( _π_ ).
For a given redemption amount _m_, the subset _Qm ⊆_ _Q_ is redeemed against, such that:



where,



_S_ ( _Qm_ ) =        - _D_ ( _π_ ) _≤_ _m_

_π∈Qm_


_Qm_ = _{π ∈_ _Q_ : _S_ ( _Qm_ ) _≤_ _m_ and _S_ ( _Qm ∪{π}_ ) _> m_ for any _π /∈_ _Qm}_


12


ensuring that the selected troves do not exceed the redemption limit _m_, and _Qm_ is the largest possible subset
that can be redeemed up to _m_ (i.e., partial inclusion of troves that satisfy this constraint).


**5.5** **Target Debt in Front**


As a trove owner, the act of being redeemed against effectively fully or partially siphons away the ETH/LST
collateral put up in exchange for repaying BOLD liabilities at a 1:1 rate, with some small error with respect to
the market price of BOLD that is approximately _f_ ( _tj_ ) _∗_ _[D]_ _m_ [(] _[π]_ [)] [, under the assumption that the redeemer acted]

rationally and redeemed until no longer profitable. However, this partially or completely neutralizes the
implied delta exposure of the trove owner, thereby deterring the initial targeted portfolio strategy employed.
Thus, given the set of troves is ordered with respect to the interest rate of a respective user, when a trove _π_ is
initialized within the simulation, the implementation logic defines a target debt in front coefficient _θ ∈_ [0 _,_ 1]
to avoid being redeemed against that is n.i.i.d through an approximately normal beta distribution.


**5.6** **Global Redemption Risk**


When the price of BOLD scales downward, thus leading to redemption events, users will naturally attempt
to revert to _θ_ and thus target some higher interest rate. As a result of the user payoff, we model the global
redemption risk _γ ∈_ [0 _,_ 1] as a normalizing sweep parameter that dictates the probability of reversion to _θ_ .
_γ_ is thus defined as the relative redemption volume within a 7-day time-frame against a defined maximum
EMA redemption volume:



_γt_ = min



_t_

   - _i_ = _t−_ 6 _[m][i]_
max ~~E~~ MA ~~r~~ edemption ~~v~~ - lume _[,]_ [ 1]

- 


The result for this coefficient is then capped at 1, as can be interpreted above, ensuring that _γt_ remains
within the range of 0 to 1, where a higher value indicates a higher relative redemption risk.
When taking the relative difference between the current and target debt in front, we implicitly model the
elasticity of a respective trove owner _k_, subject to his initial targeting games, such that users with lower _θ_
values will, in expectation, exhibit more elasticity and thus will aim to update interest rates and minimize
their interest accrual accordingly. Unlike V1’s ordering dynamics with respect to the LTV of the position,
whereby a user only had to be aware of redemption risks and collateral price drawdowns, Liquity V2’s

- rdering can alternatively be modeled through an implicit minimization problem subject to _θ_ . In other
words, the effective interest rate employed by an updating user to make their interest rate cheaper while
adhering to redemption ordering will be _ϵ_ greater than the trove owner just below, in order to optimize for
both interest rate minimization and risk of redemption minimization:



minimize _r_ ( _πk, θk_ )
subject to _r_ ( _πk, θk_ ) _≥_ _r_ ( _πk−_ 1) + _ϵ_

    - _[D]_ [(] _[π][i]_ [)]



_πi∈Q,πi<πk_ _[D]_ [(] _[π][i]_ [)]

~~�~~ _[D]_ [(] _[π][i]_ [)]



_πi∈Qi_ _[D]_ _k_ [(] _[π][i]_ [)] _≥_ _θk_




- _πi∈Q,πi<πk_ _[D]_ [(] _[π]_ _i_ [)]



_padj↑t_ = (1 _−_




~~�~~ _πi∈θQk_ _[D]_ [(] _[π]_ _i_ [)] ) _× γt_



Where _padj↑_ indicates the probability of adjustment and thus a higher relative trove interest rate.


**5.7** **Lowering Interest Rates**


Conversely, if the price of BOLD maintains a healthy value within the simulation, thereby inducing minimal
redemption volume, while _θ_ is less than the current debt in front, then users will naturally attempt to
minimize their interest rates back to the target with a probability equivalent to the absolute deviation
between the market priced rate _ρt_ and the respective trove interest rate _rk,t_, with an additional probability

- f reducing rate sweep parameter _ϕ_ . Thus, the optimization problem has the following constraints:


13


minimize _r_ ( _πk, θk_ )
subject to _r_ ( _πk, θk_ ) _≥_ _r_ ( _πk−_ 1) + _ϵ_

    - _[D]_ [(] _[π][i]_ [)]



_πi∈Q,πi<πk_ _[D]_ [(] _[π][i]_ [)]

~~�~~ _[D]_ [(] _[π][i]_ [)]



_π_ ~~�~~ _i_ _πi∈Qi_ _[D]_ _k_ [(] _[π][i]_ [)] _≥_ _θk_

_padj↓t_ = ( _rk_ ( _t_ ) _−_ _ρ_ ( _t_ )) _× ϕ_



Thus, the probability of adjusting rate is directly correlated with the underlying volatility that _ρ_ introduces,
thereby indicating a more efficient market when _ρt_ is higher.


**5.8** **BOLD Above Peg**


A third condition arises in the event that the BOLD price goes above peg, such that the risk of redemption
is seen as highly unlikely, and thus troves will no longer adhere to _θ_ - r any of the conditions or constraints
defined earlier, and alternatively decrease their interest rates to the minimum value defined. Formally:


minimize _r_ ( _πk_ ) = _rmin_
subject to _BOLD/USD >_ $1 _._ 01
_padjt_ = _ϕ_


Given that automated strategies are expected to frequently adjust interest rates according to the optimization
logic in expectation, the probability of adjusting the rate becomes significantly higher. This is due to
the continuous monitoring and real-time decision-making capabilities of these automated systems, which
allow them to react swiftly to changes in market conditions and maintain optimal positions based on their
programmed criteria.


**5.9** **Monte-Carlo Runs**


For each point in the parameter space, we sample the random variables and processes specified above 1000
times:


  - Base rate and leverage demand - CIR and OU processes correlated with a 0.5 coefficient.


  - ETH price - GBM process.


  - Initial LTV distribution.


  - Initial borrowing rate distribution.


  Stop loss/take profit distribution.


  - Rate adjustment - binomial with a parameter proportional to the distance from target debt in front.


**Result Representation**


  - The presented results are the 95th percentile of the relevant metric.


  - For minimum BOLD price, and redeemed amount, the results presented were measured over the sample
that yielded the 95th percentile redemption volume.


  - For bad debt, max BOLD price, minimum TCR, liquidations, and redeemed amount, the results
presented were measured over the sample that yielded the 95th percentile bad debt.

### **6 Simulation Results**


**6.1** **Sweep Parameter Combinations**


In our exploration of this novel protocol, we are immersed in a highly theoretical environment where key
parameters delineate the system’s overall flexibility and responsiveness. Our approach involves constructing


14


matrices that encompass a wide array of sweep parameters across diverse market scenarios, as well as isolated
stress scenarios that help us further understand the protocol dynamics during adverse instances. This
meticulous simulation framework aims to illuminate the anticipated reactions of users within the system. By
scrutinizing these simulations, we seek to extract vital metrics that serve as barometers of protocol health.
Furthermore, these insights will guide us in formulating precise recommendations for optimizing specific
parameter values. This rigorous process not only enhances our understanding of user behavior but also
fortifies our ability to foster a resilient and adaptive protocol design.


**6.2** **Key Derived Parameters**


We utilize the following derived parameters, at both the protocol level and the agent level, to define various
scenarios:


  - _β_ = decay speed of redemption fee.


  - _η_ = borrowing demand scalar.


  - _ϕ_ = probability of reducing rate.


 - ∆ _SP_ = Aggregate Stability Pool agent elasticity.


  - _rmin_ = minimum borrow rate.


 - % _SP_ = stability pool yield split.


**6.3** **Arbitrage Agent Elasticity and Speed of Redemption Fee Decay**


**Parameters Swept** ∆ _SP_ and _β_


**Rationale:**

The elasticity of the stability pool yield relative to the base rate, combined with varying redemption decay
speeds, significantly impacts the system’s behavior. Increased elasticity allows the system to more effectively
minimize the deviation between the global interest rate and the stability pool yield. This heightened efficiency
can lead to instances of large redemptions, particularly during significant spikes in base rates. These large
redemptions increase outflows, potentially causing downward price movements. Understanding and managing
this elasticity is crucial for maintaining system stability and mitigating the risks associated with rapid interest
rate changes, as well as addressing the impact of liquidations on stability pool contraction.
In this context, the speed of redemption decay becomes imperative in maintaining the peg. Faster decay
speeds can help quickly absorb the selling pressure and stabilize the system by reducing the amount of
BOLD in circulation more rapidly. Conversely, slower decay speeds may prolong the period of instability,
as the system takes longer to adjust to the increased selling pressure and restore equilibrium. **Interesting**


**Metrics**


  - total ~~r~~ edeemed amount - represents the relative redemption volume concerning the total BOLD supply
at initialization. The values in the cells indicate the proportion of BOLD that has been redeemed
relative to the initial total supply of BOLD.


  - min BOLD Price.


15


Figure 7: Heatmap of total redeemed amount for various combinations of decay speed and aggregate SP
agent elasticity.


16


Figure 8: Heatmap of minimum BOLD price for various combinations of decay speed and aggregate SP
agent elasticity.


**6.4** **Aggressiveness in Borrowing Demand and Speed of Redemption Fee Decay**


**Parameters Swept** : _η_ and _β_
**Rationale** : The aggressiveness in user borrowing demand, coupled with varying redemption decay speeds,
plays a significant role in the system’s dynamics. When users aggressively amplify their Loan-to-Value
(LTV) ratios and mint new debt, it can result in heightened selling pressure on BOLD, as well as increased
liquidation events. This increased selling pressure can trigger redemption events, where users redeem BOLD
for the underlying collateral to restore the desired collateralization levels.
**Metrics:**


  - Min BOLD Price


17


  - total ~~r~~ edeemed amount


  - bad ~~d~~ ebt


  - total ~~l~~ iquidated ~~a~~ mount


Figure 9: Min BOLD Price Heatmap Figure 10: Total Redeemed Amount Heatmap


**Impact of Minimum Borrow Rates**


Below, we present two sets of heatmaps: on the left-hand side, the system operates under a minimum
borrow rate of 0%, while on the right-hand side, it operates under a minimum borrow rate of 0.5%. These
visualizations illustrate the impact of different minimum borrow rates on the system’s performance.



Figure 11: Bad Debt with a Minimum Borrow
Rate of 0%



Figure 12: Bad Debt with a Minimum Borrow
Rate of 0.5%



18


Figure 13: Total Liquidated Amount with a Minimum Borrow Rate of 0%



Figure 14: Total Liquidated Amount with a Minimum Borrow Rate of 0.5%



Importantly, the heatmaps reveal a significant decrease in the accrual of bad debt in the worst-case scenarios
when the minimum borrow rate is set at 0.5%. This observation suggests that a higher minimum borrow
rate enhances the system’s resilience during adverse market conditions.


**6.5** **Elasticity of Stability Pool Coupled with Elasticity of Trove Owner Interest**
**Rate Adjustments**


**Parameters Swept** : ∆ _SP_ and _ϕ_
**Rationale:** Trove owner elasticity refers to the likelihood that trove owners will reduce their rates in
response to changes in the base rate at any given step. This elasticity indicates how sensitive trove owners
are to fluctuations in the base rate, influencing their decisions to adjust borrowing rates accordingly. On the

- ther hand, aggregate SP agent elasticity pertains to the probabilistic reaction of the stability pool agent to
deviations between the base rate and the stability pool yield. This elasticity measures how the stability pool
agent responds to discrepancies in yield, adjusting their actions to maintain equilibrium within the system.
Together, these elasticities play an important role in determining the overall responsiveness and stability of
the system in reaction to varying market conditions.
**Metrics:**


  - Max BOLD Price


  - Stability Pool Size


  - Redemption volume


19


Figure 15: Total Redeemed Amount
Figure 16: Max BOLD Price


Figure 17: Min Bold Price


20


**6.6** **Protocol Incentives and Limitations**


**Parameters Swept:** % _SP_ and _rmin_
**Rationale:**

Gauge the optimal level of incentives given to the SP coupled with the minimum borrowing rate defined
for trove owners, such that the system is adequately incentivized and maintains sufficient backing in the
worst-case scenario.


**Metrics:**


  - Min BOLD Price


  - Stability Pool Size


  - Redemption volume


Figure 18: Total Redeemed Amount


21


Intuitively, one could define the minimum borrow rate as an absolute revenue threshold for the protocol.
Concurrently, the stability pool yield split serves as an explicit incentive mechanism to supply idle capital to
the stability pool, ensuring it maintains an adequate percentage of the total BOLD supply. Consequently,
when there is less gross revenue going to the protocol and a smaller percentage of revenue accruing to the
stability pool, it inherently leads to an increase in redemption events. With a reduced internal incentive to
hold onto BOLD, due to limited yield sources, and the minimum borrowing rate converging to lower levels
when the BOLD price scales above a certain threshold, more redemption events are triggered. This dynamic
underscores the importance of balancing revenue distribution and incentive mechanisms to maintain system
stability and minimize excessive redemptions.


Figure 19: Min BOLD Price


The BOLD price, while not following as much of a gradient, naturally provides a relationship between its
value and the total redeemed amount. Similar to the total redeemed amount, as the stability pool yield split
gets smaller, the incentive to hold minted BOLD instead of selling to take advantage of leverage elsewhere,


22


as well as buy on the open market for non-redemption purposes, decreases.


Figure 20: Min Stability Pool Size


In terms of the minimum stability pool size, however, the pattern is quite different. While a low minimum
borrow rate coupled with a low stability pool yield split makes it such that the total capital in the stability
pool converges to a low value, one would think that the larger the absolute revenue (i.e., minimum borrow
rate) coupled with a high stability pool yield split would lead to a larger stability pool as a result. However,
according to our results, a minimum borrow rate that is too high will lead to adverse outcomes relative to
a lower minimum borrow rate, as the relative incentive to mint new capital when leverage demand is high
thus diminishes comparatively.


23


**6.7** **Modeling Additional Trove Operations**


To further optimize the value for minimum borrowing rates, we have added these critical trove operations,
which are more reflective of realistic users:


  - **Stop loss**  - acceptable percentage change from the opening price. Troves stop loss distribution is
sampled out of a normal distribution. We have attempted to use historical V1 data to estimate the
parameters of the distribution.


  - **Adjusting LTV**  - repaying loan to return to comfort LTV. Adjusting LTV each time step t is binomial
with a probability:



_p_ = _ϕ ∗_ _LTVi,t −_ _LTVc,i_

                     - ��� _LTVc,i_




- ���



Where trove responsiveness is the same parameter _ϕ_ used when adjusting the interest rate.


Unsurprisingly, introducing these actions has mitigated bad debt significantly (0 for any reasonable selection

- f stop losses and responsiveness parameters). However, in order to get a sense of the effect of minimum
borrowing rate at a working point, we have used a “stressed” stop loss distribution with mean = 0 _._ 6, std
= 0 _._ 05, and a synthetic ETH price path of an 80% drawdown over 2 weeks, as shown in the charts below:


Figure 21: Stop Loss Distribution Figure 22: ETH Price


24


**Results**



Figure 23: Bad Debt in Millions


Figure 24: Max BOLD Price


25


While it’s difficult to model users’ responsiveness under high volatility regimes and translate the parameter
to the actual probability of a trove to adjust LTV and avoid liquidation, it is clear based on historical data
that we should expect significant repayments and lower bad debt than in previous simulations. We also see
the effect of the repayments on BOLD price, with increasing demand.

### **7 Results and Insights**


**7.1** **Implementing a Minimum Interest Rate**


We mathematically analyze the dynamics observed among the agents to gain insights into defining a minimum
interest rate. This analysis stems from the continuously incentivized stability pool yield, which results in
high variance in stress scenarios, and the strategic interest rate adjustments that can lead to detrimental

- utcomes within the protocol. By understanding these dynamics, we can better define and implement
a minimum interest rate that balances incentives and stability, mitigating the risks associated with high
variance in stability pool yields and the implications of strategic interest rate setting.


**BOLD Upward Price Pressure and Stability Pool Dynamics**


The stability pool APY jumps stemming from the percentage of cumulative interest rates when the stability
pool contracts due to liquidation events. Mathematically speaking,


_∀t ∈_ _T, SPt−_ 1 _> SPt | Liquidationt →_ _APYt > APYt−_ 1


Here, _SPt_ represents the size of the stability pool at time _t_ . During periods of significant liquidations, the
deviation between _SPt−_ 1 and _SPt_, or ∆ _SPt_, increases, causing ∆ _APYt_ to rise as well. This relationship
is crucial as it illustrates how the protocol incentivizes stability and risk mitigation during market stress,
aligning the evolving interests of users who provide liquidity to the stability pool.


**Impact of Expected Stability Pool Size and Yield Split on APY Variance**


The size of the stability pool _SPt_ directly impacts the magnitude of APY changes. Smaller pools exhibit
more significant percentage changes in APY compared to larger pools, given the same absolute change in
liquidated assets. Formally, the expected deviation in APY ∆ _APYt_ as a function of the yield split % _SP_ can
be expressed as:


∆ _APYt_ = _APYt −_ _APYt−_ 1 _∝_ _f_ (% _SP_ ) _×_ [∆] _[SP][t]_

_SPt−_ 1

Where _f_ (% _SP_ ) is a monotonically decreasing function of the yield split, and the cumulative annualized gross
revenue within the protocol is defined as Σ _[n]_ _i_ _[r]_ [(] _[π][i]_ [)] _[ ×][ D]_ [(] _[π][i]_ [). Under the assumption that] _[ APY][t][−]_ [1][(%] _[SP]_ [1][) =]
_APYt−_ 1(% _SP_ 2), indicating converged stability pool sizes varying with % _SP_, alongside constant relative
liquidation sizes and redeemed trove interest rates, the relative expected deviation between APY values thus
decreases monotonically with the yield split % _SP_ :




[∆] _[APY][t]_ (% _SP_ 1) _≥_ [∆] _[APY][t]_

_APYt−_ 1 _APYt−_



_∀_ % _SP_ 1 _,_ % _SP_ 2 _∈_ [0 _,_ 1] _,_ % _SP_ 1 _≤_ % _SP_ 2 _⇒_ [∆] _[APY][t]_



(% _SP_ 2)
_APYt−_ 1



Naturally, for smaller stability pools, the absolute change ∆ _SPt_ represents a larger percentage change.
Formally, if the expected stability pool sizes E[ _SPt−_ 1(% _SP_ 1)] and E[ _SPt−_ 1(% _SP_ 2)] are such that
E[ _SPt−_ 1(% _SP_ 1)] _<_ E[ _SPt−_ 1(% _SP_ 2)], given by % _SP_, we have:


∆ _SPt_ ∆ _SPt_
E[ _SPt−_ 1(% _SP_ 1)] _[>]_ E[ _SPt−_ 1(% _SP_ 2)]


Therefore, the relative change in the stability pool size is more significant for smaller pools in expectation.
This implies that for smaller pools, the impact of ∆ _SPt_ is amplified, leading to greater fluctuations in APY.
Given that the expected stability pool size E[ _SPt−_ 1] is a function of the yield split _α_, the impact of liquidation
events on the relative APY and the relative size of the stability pool is dual-faceted:


26


1. The relative change in APY decreases with increasing % _SP_ .


2. The relative size of the stability pool decreases more significantly for smaller pools, which is the case
when % _SP_ is smaller due to less continuous incentives.


Thus, during rapid collateral price declines where _SP →_ 0, _APY →∞_, smaller stability pool sizes converge
faster and exhibit higher yield variance compared to larger pools in expectation. This dynamic is compounded
by trove owners rapidly repaying debt during such downturns, influencing overall system stability and asset
pricing.


**Comparing Liquity V1 Borrow Fee Dynamics to Liquity V2 Interest Rates**


Moreover, comparing borrowing dynamics between Liquity V1 and Liquity V2 reveals contrasting approaches
to managing borrower incentives and system stability. In Liquity V1, the upfront borrow fee of 0.5% acts as
an effective deterrent against short-term speculative borrowing. This fee structure ensures that borrowers
consider the economic viability of their positions relative to market volatility and potential liquidation risks.
The fee structure implicitly defines an extrapolated Borrow APY based on the expected duration of trove
positions, thereby influencing borrowing behaviors during volatile market conditions, as seen below:


Figure 25: Effective Borrow APY on Liquity V1


Conversely, Liquity V2 trove owners can adjust interest rates dynamically and autonomously, which can
impact system health during stress scenarios. Managing risk-adjusted revenue and preventing rent-seeking
behaviors during market downturns are critical, necessitating a balanced approach to borrowing fees to
maintain system stability. Our borrowing demand mechanism and the initialization of new troves assume that
highly elastic users can take on free debt, thereby potentially negatively affecting the system’s risk-adjusted
health during a market downturn due to minimal proportional interest contributions to the dwindling stability
pool.
In a stress scenario where liquidations and implicit debt repayments occur continuously, it is assumed that
the automated interest strategy for a large subset of users will adjust automatically if the BOLD price exceeds
a specific threshold. Consequently, the aggregate risk-adjusted revenue for new deposits inhibits the stability


27


pool’s rebounding effect and can lead to additional outflows and liquidation events, resulting in bad debt
accrual. As demonstrated in stress test results and Monte Carlo simulations, to mitigate the potential for
rent-seeking behavior during significant market downturns, we recommend instituting a minimum interest
rate of 0.5%. This fee should strike a balance between not overly taxing the incentive to mint new capital
when leverage demand is high while simultaneously protecting against adverse outcomes.


**7.2** **BOLD Downward Price Pressure and Redemption Risks: Less Aggressive**
**Redemption Fees**


Our simulation results indicate that decreasing the dynamic fee constraint _β_ resulted in no discernible increase
in redemption volumes and thus a minimal contraction in the BOLD supply. Despite these relatively minor
changes, the fee adjustment had a substantial impact on improving peg stability, particularly on the downside.
This enhanced stability prompted users to adapt their behavior in ways that are markedly different from the
patterns observed in V1.


**V1 Dynamics**


In V1, avoiding redemption explicitly increased short-term peg stability because trove owners would initiate
an LUSD buy on the open market. In a similar simulation environment for V2, the objective function can
be defined as follows:



minimize _CR_ ( _πk, θk_ )
subject to _CR_ ( _πk, θk_ ) _≥_ _CR_ ( _πk−_ 1) + _ϵ_

    - _[D]_ [(] _[π][i]_ [)]



_πi∈Q,πi<πk_ _[D]_ [(] _[π][i]_ [)]

~~�~~ _[D]_ [(] _[π][i]_ [)]



_πi∈Qi_ _[D]_ _k_ [(] _[π][i]_ [)] _≥_ _θk_








- _πi∈Q,πi<πk_ _[D]_ [(] _[π]_ _i_ [)]



_padj↑t_ =



1 _−_





~~�~~ _πi∈Q_ _[D]_ [(] _[π]_ _i_ [)]

_θk_



_× γt_



In this context, rate minimization is replaced with LTV minimization. Trove owners buy and repay LUSD

- n the open market until _θ_ is satisfied, allowing the LUSD price to rebound independently. The precise
amount of LUSD to be bought up can be mathematically represented through the following equation:



∆ _LUSD_ = _D_ ( _πk, t −_ 1) _×_ 1 _−_ _[CR]_ [(] _[π][k][,][ t][ −]_ [1][)]

                 - _CR_ ( _πk, t_ )


Thereby explicitly contributing to peg reversion.







**Constructing a Middle Ground Between BOLD and Traditional CDP Stablecoins**


In contrast, traditional decentralized stablecoins like Aave’s GHO and MakerDAO’s DAI employ a ’soft peg’
mechanism. They incentivize trove owners to repay debt at a cheaper rate through market purchases in
the event of a depeg and periodically adjust interest rate parameters to maintain a $1 equilibrium. This
approach aligns with market-priced interest rates to inhibit extractive behavior that can negatively impact
peg health.
Liquity’s BOLD introduces a democratized, autonomous, and algorithmic approach, characterized by very
low interest rates and dynamic fee peg constraints based on relative redemption volumes over specific periods.
Consequently, the minimum BOLD price is highly sensitive to the decay speed of these dynamic fees; less
restrictive fee dynamics lead to lower prices, influenced by user-driven adjustments within the system due
to the underlying autonomy.
Our simulations indicate that the overall redemption volume within the system typically remains unaffected
by the decay speed. This is because risk-taking trove owners do not actively purchase BOLD on the open
market, unlike in V1. Instead, this necessitates users to fine-tune the aggressiveness of their interest rate
strategies to manage redemption risks, which are expected to oscillate around the market-priced interest

rate.

Therefore, we recommend implementing a lower _β_ value than V1’s 0.944 and adopting a more conservative
dynamic fee approach. This strategy aims to mitigate extractive behaviors within the protocol and enhance


28


peg stability while simultaneously managing typical debt incentives, liquidation risks, and debt payoffs
(incentives/haircuts) associated with CDP stablecoins.


**7.3** **Modeling Different LSTs**


**Stability Pool Implications**


The passive nature of the continuously incentivized stability pool in internalizing liquidation events significantly reduces reliance on on-chain liquidity, thereby mitigating negative externalities that occur within
a short timeframe. Our extreme stress tests demonstrate that a stability pool capable of internalizing a
substantial amount of debt effectively buffers the system against sudden shocks and market volatility. This
includes mitigating the impact of sudden ETH price drops within a very short time window, as well as
adverse decorrelation events, such as slashing, that occur within the protocol and the dynamics surrounding
these events.


**User Behavior and External Pricing**


User behavior is expected to remain consistent whether using a Liquid Staking Token (LST) or ETH, as
the underlying mechanisms and incentives remain largely unchanged. By overlaying highly correlated price
trajectories within simulations, we can project similar probabilistic outcomes for both assets. Following the
Shanghai upgrade, the pricing of LSTs has converged closely with ETH, driven by a fundamental change in
market confidence and thus improved liquidity.
This convergence has been reflected in lending protocols such as Aave, which have already begun pricing LSTs
1:1 with ETH in their oracles. Furthermore, these protocols have introduced a generalized ”e-mode” for a
subset of LSTs with extremely high theoretical Loan-to-Value (LTV) ratios, operating under the assumption
that the underlying debt asset is correlated (such as ETH). This adoption of ”e-mode” demonstrates a
recognition of the convergence between LST and ETH prices and highlights the enhanced liquidity and
market confidence in LSTs post-Shanghai upgrade.
The inherent concentration of ETH/LST liquidity on decentralized exchanges (DEXes) facilitates a precise
definition of the relative LST collateral through the redemption process. This mechanism ensures that arbitrageurs can effectively redeem LSTs when necessary, as the liquidity structure supports seamless exchanges.
Furthermore, the inverse correlation between liquidations and redemption events provides additional stability
to the system, mitigating risks associated with large-scale liquidations.
However, it is crucial to qualitatively assess each LST to determine its viability as collateral on the Liquity
platform. Factors such as the stability of the LST, the reliability of the underlying staking protocol, and
market acceptance must be considered. This assessment ensures that only robust and dependable LSTs are
utilized, maintaining the integrity and resilience of the collateral system


29


### **8 Appendix**

Below, we present a stress scenario in which the price of ETH experiences a 70% decline over the course of
half a year. The simulation is governed by the configuration of specific parameter values. We compare two
distinct scenarios under the same seed: one with no minimum borrow rate and the other with a minimum
borrow rate of 0.5%. The accompanying plots provide insight into how the system reacts in both scenarios.

```
{

  "n_sims": 1,

  "iterations": 4350,
  "debt_scalar": {"min_value": 1, "max_value": 2, "samples": 1},
  "volatility_scalar": {"min_value": 1, "max_value": 1, "samples": 1},
  "stability_pool_ratio": {"min_value": 0.8, "max_value": 0.8, "samples": 1},
  "amm_pool_ratio": {"min_value": 0.2, "max_value": 0.3, "samples": 1},
  "block_number": 14758892,

  "debug": True,
  "initial_price": 2500,
  "correlation_coefficient": {"min_value": 0.5, "max_value": 0.8, "samples": 1},
  "eth_vol": 0.01,
  "probability_of_reducing_rate": {
    "min_value": 0.005,

    "max_value": 0.01,

    "samples": 1
  },
  "proportion_of_yield_mean": {
    "min_value": 0.005,

    "max_value": 0.01,

    "samples": 1
  },

  "ema_days": 24,
  "max_redemption_risk": 1000000,
  "borrowing_demand_scalar": {"min_value": 20, "max_value": 100, "samples": 1},
  "decay_speed": {"min_value": 0.94, "max_value": 0.99, "samples": 1},
  "ltv_parameters": {"alpha": 2.94, "beta": 2.922, "loc": -0.047, "scale": 1},
  "mcr": {"min_value": 1.2, "max_value": 1.2, "samples": 1},
  "stability_pool_yield_split": {
    "min_value": 0.5,

    "max_value": 0.9,

    "samples": 1
  },
  "min_borrowing_rate": {"min_value": 0.0000001, "max_value": 0.005, "samples": 2},
  "proportion_of_yield_std": 0.001,
  "version": 1,

  "seed": 14

}

```

30


Figure 26: ETH Price Trajectory Figure 27: Initial Trove LTV Distribution


Figure 28: Initial Trove Rate Distribution


31


**No Minimum Borrow Rate**


Figure 29: Base Rate, Stability Pool and Peg Dynamics Over Time


Figure 30: Final Rate Distribution Figure 31: Final LTV Distribution


Figure 32: CR and Total Debt Over Time Figure 33: Stability Pool Size Over Time


32


Figure 34: Total Liquidated Collateral Amount Figure 35: Total Minted/Redeemed BOLD Amount


Figure 36: Total Burned Debt Amount Figure 37: Rate Adjustments Over Time


Figure 38: Bad Debt Over Time


33


**0.5% Minimum Borrow Rate**


Figure 39: Base Rate, Stability Pool and Peg Dynamics Over Time


Figure 40: Final LTV Distribution Figure 41: Final Rate Distribution


Figure 42: CR and Total Debt Over Time Figure 43: Stability Pool Size Over Time


34


Figure 44: Total Liquidated Collateral Amount Figure 45: Total Minted/Redeemed BOLD Amount


Figure 46: Total Burned Debt Amount Figure 47: Rate Adjustments Over Time


Figure 48: Bad Debt Over Time


35


**About Chaos Labs**


Chaos Labs is a cloud-based platform that develops risk management and economic security tools
for decentralized finance (DeFi) protocols. The platform leverages sophisticated and scalable simulations
to stress test protocols in adverse and turbulent market conditions. By partnering with DeFi protocols,
Chaos Labs aims to create innovative solutions that enhance the efficiency of DeFi marketplaces. The
Chaos Labs team exhibits exceptional talent and represents diverse expertise, encompassing esteemed
researchers, engineers, and security professionals. Chaos Labs has garnered its experience and skills
from renowned organizations, including Google, Meta, Goldman Sachs, Instagram, Apple, Amazon, and
Microsoft. Additionally, the team boasts members who have served in esteemed cyber-intelligence and
security military units, further contributing to their unparalleled capabilities. You can explore our past and

- ngoing projects for customers like Aave, GMX, Benqi, dYdX, Uniswap, Maker, and more in the Research
and Blog sections of our website.


36


