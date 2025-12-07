## While Stability Lasts: A Stochastic Model of Non-Custodial Stablecoins [∗]

Ariah Klages-Mundt [†] Andreea Minca [‡]


June 8, 2022


**Abstract**


The ‘Black Thursday’ crisis in cryptocurrency markets demonstrated deleveraging risks in

   - ver-collateralized non-custodial stablecoins. We develop a stochastic model that helps explain
deleveraging crises in these over-collateralized systems. In our model, the stablecoin supply is
decided by speculators who optimize the profitability of a leveraged position while incorporating
the forward-looking cost of collateral liquidations, which involves the endogenous price of the
stablecoin. We formally characterize regimes that are interpreted as stable and unstable for the
stablecoin. We prove bounds on quadratic variation and the probability of large deviations in
the stable domain and we demonstrate distinctly greater price variance in the unstable domain.
We identify a deflationary deleveraging spiral by means of a submartingale. These deleveraging spirals, which resemble short squeezes, lead to faster collateral drawdown (and potential
shortfalls) and are accompanied by higher price variance, as experienced on Black Thursday.
We conclude by discussing non-custodial ways in which the issues raised in this paper can be
mitigated.

### **1 Introduction**


On March 12, 2020, called ‘Black Thursday’ during the COVID-19 market panic, cryptocurrency
prices dropped _∼_ 50% in the day. [1] This was accompanied by cascading liquidations on cryptocurrency leverage platforms, including both centralized platforms like exchanges and new decentralized
finance (DeFi) platforms that facilitate on-chain over-collateralized lending. Among many events
from this day, the story of Maker’s stablecoin Dai stands out, which entered a deflationary deleveraging spiral (akin to a short squeeze on Dai). This triggered high volatility of the ‘stable’ asset
and a breakdown of the collateral liquidation process. Due to market illiquidity exacerbated by
network congestion, some collateral liquidations were performed at near-zero prices. As a result,
the system developed a collateral shortfall, which prompted an emergency response and had to be
made up by selling new equity-like tokens to recapitalize MakerDAO [2020a].
During this time, there was a huge demand for Dai. It became a much riskier and more volatile
asset, yet traded at a high premium and fetched lending rates in the mid double digits. Leveraged
speculators, who must repurchase Dai in order to deleverage their positions, were exhausting Dai


∗This paper is based on work supported by NSF CAREER award #1653354 and the Bloomberg Fellowship. We
thank Dominik Harz, Georgios Konstantopoulos, the anonymous referees for valuable feedback that helped improve
the paper.

  - Cornell University, Center for Applied Mathematics, Ithaca, NY, 14853, USA, email: `aak228@cornell.edu` .

  - Cornell University, School of Operations Research and Information Engineering, Ithaca, NY, 14850, USA, email:

`acm299@cornell.edu` .
1This occurred while writing up the first draft of this paper.


1


Figure 1: Stablecoin supply.


liquidity, driving up the price of Dai and subsequently increasing the cost of future deleveraging
(we discuss some further causes that led to market illiquidity in developing the model in the next
section). These speculators began to realize that, in these conditions, they face concrete risk that
a debt reduction of $1 could cost a significant premium. Eventually, a new exogenously stable
asset–the USD-backed custodial stablecoin USDC–had to be brought in as a new collateral type to
stabilize the system Coindesk [2020].


**1.1** **Stablecoins**


A stablecoin is a cryptocurrency with added economic structure that aims to stabilize price/purchasing
power. For a recent overview of stablecoins, see Bullmann et al. [2019], Klages-Mundt et al. [2020]
and the references therein. Stablecoins are meant to bootstrap price stability into cryptocurrencies
as a stop-gap measure for adoption. They also serve as mechanics to avoid fiat to crypto conversions, which are rather costly. This is in fact a key motivation for their use, hence the system can
remain ‘fully decentralized’.
Stablecoins are either _custodial_ and rely on custodians to hold reserve assets off-chain (e.g., $1
per coin) or _non-custodial_ and set up a risk transfer market through smart contracts, which are
programs that execute on the blockchain computer. Custodial stablecoins include Tether, USDC,
and the proposed Diem/Libra and can often be viewed analogously to narrow banks or money
market funds in terms of underlying structure. Alternatively, non-custodial stablecoins aim to
retain the property of reduced counterparty/censorship risk. Figure 1 illustrates the market share

- f the main stablecoins. The largest three are custodial stablecoins (USDT, USDC, BUSD) whereas

- nly one non-custodial stablecoin, Dai, is among the top four stablecoins in terms of market share.


Non-custodial stablecoins have a wide design space, which is captured in the taxonomy of
Klages-Mundt et al. [2020]. A key dimension in this design space is the source of value backing
the stablecoin. This ranges from exogenous asset backing, where assets have value unrelated to the
system, to endogenous asset backing, where assets are like ‘system equity’ and have value that is
circular with the system itself. This latter class, which is often ill-defined as ‘algorithmic’, often
blurs the line with being effectively unbacked, as the value of endogenous assets can spiral to zero
if confidence is broken. This latter type includes the Terra UST stablecoin that collapsed in May
2022 Bloomberg [2022]. These stablecoins that are fully or partly endogenously backed can largely
be understood using generalizations of currency peg models, such as Morris and Shin [1998], for
which the risks of currency runs and speculative attacks are well studied. These existing tools help
to understand these systems and how they (usually) fail, considering that the ‘economies’ around


2


these stablecoins are quite fragile.
In contrast, non-custodial stablecoins that are backed by exogenous assets have greater similarities to non-custodial forms of the current monetary system of commercial bank money, as discussed
in Klages-Mundt et al. [2020]. In this paper, we focus on new risks that arise in these types of
stablecoins, which require further study. Stablecoins of this type transfer risk from stablecoin holders to speculators, who hold leveraged collateralized positions in cryptocurrencies. [2] The speculator
represents any actor (usually automated) who has an incentive to issue the coin. [3] Such actor issues the stablecoin continuously by locking in collateral. The incentive to issue (or redeem) coin
is captured by the speculators’ return expectations including potential liquidation costs and the
endogenous stablecoin price.
The collateralization structure is different for non-custodial stablecoins than for the custodial

- nes. It is similar to a tranche structure, in which stablecoins act like senior debt while speculators
are akin the buyers of the junior tranche of a CDO. In contrast to the classical case, the ‘CDO’ issue
is dynamic and by anyone in the system. We refer the reader to the Dai white paper MakerDAO

[2017]. The white paper describes how _anyone could generate Dai using that system_ by leveraging
Ethereum (ETH) as collateral through smart contracts known as Collateralized Debt Positions
(CDPs).
A dynamic and automatic deleveraging process balances positions if collateral value deviates too
much, as determined by a price feed. Two major risks in non-custodial stablecoins emerge around
market structure collapse and price feed and governance manipulation. In this paper, we focus
completely on the market structure risk, assuming that price feeds, governance, and the underlying
blockchain perform as expected. [4]

In addition to the COVID-19 panic, the effects of these risks are also witnessed in bitUSD,
Steem Dollars, and NuBits, which suffered serious depegging events in 2018 Klages-Mundt [2018],
and Terra and Synthetix, which suffered price feed manipulation attacks in 2019 (Synthetix [2019b],
Synthetix [2019a], Terra Research [2019]). Similar manipulations were also observed on the bZx
lending protocol in 2020 (PeckShield [2020a], PeckShield [2020b]). Many similar examples of mechanism failures and exploitations occurred through the rest of 2020 (see Klages-Mundt et al. [2020],
Werner et al. [2021]). Stablecoins currently serve a central role in an increasingly complex decentralized finance environment, involving composability with other DeFi platforms. In addition,
many other blockchain assets, such as synthetic and cross-chain assets, rely on the basic mechanism
behind stablecoins, which we explore further in the discussion section.


**1.2** **This paper**


In this paper, we construct a stochastic model of over-collateralized non-custodial stablecoins, with
an endogenous price (Section 2). The system is based on a speculator who solves an optimization
problem accounting for potential returns from leverage as well as potential liquidation costs. The
speculator decides the supply of stablecoins secured by its collateral position while considering
demand for the stablecoin. Our interest in non-custodial stablecoins lies in understanding deleveraging spirals when the price and stablecoin issue is endogenous and the collateral management is
decentralized. In this case, a deleveraging spiral results from the intertwining of a short squeeze in
the stablecoin price and a liquidation spiral of the collateral. This is in contrast to potential liquidation crises in custodial coins such as Tether and USDC or ‘algorithmic’ stablecoins such as Terra


2
‘Leverage’ means that speculators holds _>_ 1 _×_ initial assets but face new liabilities.
3They are part a form of ‘keepers’ in the MakerDAO protocol.
4Note, however, that blockchain congestion can serve to decrease elasticity in the market structure, which we
discuss in the model construction.


3


UST (which coincidentally also had a partial custodial reserve). Custodial stablecoins maintain
stability through arbitrageurs who mint and redeem for assets with the custodian. Unbacked or
partially backed stablecoins like Terra UST instead are subject to death spiral risks from runs and
speculative attacks due to insolvency. In both of these cases, classical models for money market
funds and currency pegs apply well. [5] We focus on the non-custodial variant involving exogenous

- ver-collateralization, whose risks are yet to be analyzed rigorously.
We derive fundamental results about non-custodial stablecoins in our model, including economic
limits to the speculator’s behavior, in Section 3. In Section 4 we develop the primary results of
the paper: we analytically characterize regions in which the stablecoin can be intepreted as stable
(Theorems 1 and 2) and unstable (Theorems 4 and 5), and a region in which a deleveraging spiral

- ccurs that can cause liquidity problems in a crisis (Theorem 3). These deleveraging spirals, which
resemble short squeezes, are counterintuitive as they lead to stablecoin price appreciation during
times of shock, whereas we might otherwise expect prices to depreciate given the riskier state of
the system. Further, this appreciation is detrimental: it leads to faster collateral drawdown, and
potentially shortfalls, as more collateral is required to fulfill liquidations and is accompanied by
higher price variance.
The context for our analytical results is a model with a single speculator facing imperfectly
elastic demand for the stablecoin; however, many of the methods can extend to generalized settings.
In Section 5, we consider idealized settings that lead to ‘perfect’ stability properties.
We discuss in Section 6 a seeming contradiction that arises: while the goal is to make decentralized non-custodial stablecoins, these can only be fully stabilized from deleveraging effects by
adding uncorrelated assets, which are currently centralized/custodial. This is a consequence of our
instability results in Section 4 and, as introduced in Section 5, the absence of a stable region in
idealized settings when underlying asset markets deviate from a submartingale setting. We suggest
an alternative: a buffer to dampen deleveraging effects without directly incorporating custodial
assets. This buffer works by separating those who are willing to have stablecoins swapped to custodial assets in a crisis (in return for an ongoing yield from option buyers) from those who require
full decentralization.

Non-custodial stablecoins such as Dai, Rai, and Liquity have since moved in directions such as
this to overcome the issues we illustrate in this paper.


**1.3** **Relation to Prior Work**


While there is a rich literature on related financial instruments, there is limited research directly
applicable to stablecoins. Cao et al. [2021] are the first to point out the analogy of stablecoins to
Collateralized Loan Obligations, and contribute to the securitization literature by proposing designs
in the decentralized context. They use option pricing theory and PDE methods for valuation of
their new design features. Our work is complimentary: we analyze the stability over time of these

new securities.
A simple stablecoin model is developed in Klages-Mundt and Minca [2021] and introduces the
concept of deleveraging spirals, which later materialized on Black Thursday. This paper supersedes
that model and its results. Whereas the model in Klages-Mundt and Minca [2021] doesn’t directly
account for the actual repurchase price in deleveraging–instead delegating to a risk constraint in


5The recent collapse  - f the peg in TerraUSD, see e.g., `[https://www.wsj.com/articles/](https://www.wsj.com/articles/cryptocurrency-terrausd-falls-below-fixed-value-triggering-selloff-11652122461)`
`[cryptocurrency-terrausd-falls-below-fixed-value-triggering-selloff-11652122461](https://www.wsj.com/articles/cryptocurrency-terrausd-falls-below-fixed-value-triggering-selloff-11652122461)` can be modeled
similarly to the run on money market funds in the financial crisis, Kacperczyk and Schnabl [2013], or currency peg
attacks, Morris and Shin [1998]. In particular, restoring the peg relies on open market operations by an entity
running the reserve fund, such as Luna Foundation in the case of the TerraUSD stablecoins.


4


the optimization–we set up a stochastic process model in this paper that includes forward-looking
liquidation prices in the speculator’s optimization. Our analytical results supersede Klages-Mundt
and Minca [2021] in the following ways:


  - We formally characterize a deleveraging spiral as a submartingale, whereas their paper lacks
a formal treatment.


  - We give stability results in terms of probabilities of large deviations and quadratic variation

   - f the price process.


  - An unstable region is conjectured in their paper, backed by simulation. We formally prove
distinct price variances in stable and unstable regions.


Evans [2019] analyzes credit risk stemming from collateral type in Maker’s stablecoin Dai. cLabs

[2019], Platias and DiMaggio [2019] model stability in Terra and Celo stablecoins under Brownian
motion scenarios in the absence of endogenous market feedback effects that motivate this paper.
Huo et al. [2022], Klages-Mundt et al. [2020] discuss models of governance and oracle attack surfaces
for non-custodial stablecoins. More generally in the context of decentralized finance, Werner et al.

[2021] treat the governance extractable value.
Detrio [2015] discusses stablecoin concepts based on monetary policy and hedging strategies
and introduces methods for enhancing liquidity using combinatorial auctions and automated market makers. Lipton et al. [2018] studied custodial stablecoins and considers the use of hedging
techniques to build an asset-backed cryptocurrency. Gudgeon et al. [2020] explores the robustness

- f decentralized lending protocols to shocks and liquidations. Chitra [2020] explores competition
between decentralized lending yields and staking yields in proof-of-stake blockchains. However,
these do not model a stablecoin mechanism with endogenous price behavior.
Harz et al. [2019] designs a reputation system for crypto-economic protocols to reduce collateral
requirements. This does not readily apply to understanding stablecoin collaterals, however, as it
requires identification of ‘good’ behavior and, additionally, stablecoin speculators face leveraged
exchange rate bets and will have reason to provide greater than minimal collateral. This additionally
motivates our model to understand how liquidation effects affect speculator decisions.
Stablecoins share similarities with currency peg models, e.g., Guimaraes and Morris [2007],
Morris and Shin [1998]. In these models, the government plays a mechanical market making role to
seek stability and is not a player in the game. In contrast, in non-custodial stablecoins, decentralized
speculators take the market making role. They issue/withdraw stablecoins to optimize profits and
are not committed to maintaining a peg. In a stablecoin, the best we can hope is that the protocol
is well-designed and that the peg is maintained with high probability through incentives. A fully
strategic model would be a complicated (and likely intractable) dynamic game.
There are also similarities with collateral and debt security markets and repurchase agreements.
These have also experienced unprecedented stress in the COVID-19 market panic, during which
even 30-year US government bonds–normally highly liquid–have been difficult to trade Rennison
et al. [2020]. Such debt securities differ from stablecoins in that dollars are borrowed against the
collateral as opposed to a new instrument, like a stablecoin, with an endogenous price. These debt
security markets do, however, demonstrate that liquidity in the underlying markets can dry up in
crises even in highly liquid markets. Stablecoins face this liquidity risk in the underlying market
as well as an endogenous price effect on the stable asset.
The problem resembles classical market microstructure models (e.g., O’Hara [1997]); it is a
multi-period system with agents subject to leverage constraints that take recurring actions according to their objectives. In contrast, the stablecoin setting has no exogenously stable asset that


5


is efficiently and instantly available. Instead, agents make decisions that endogenously affect the
price of the ‘stable’ asset and affect future incentives.

### **2 Model**


Our model is very closely related to Maker’s stablecoin Dai MakerDAO [2017] as well as newer
stablecoins by UMA, Reflexer, and Liquity. Crucially, these stablecoins are backed by overcollateralization in assets that have value exogenous to the stablecoin system as opposed to assets whose value is circularly derived from the stablecoin itself. There are two primary feedback
effects to consider in these stablecoins: (1) feedback of deleveraging on an endogenous stablecoin
price, and (2) feedback of deleveraging on collateral price. We focus on the former. The latter can
be described using existing deleveraging models (e.g., this is considered in the stablecoin context
in Gudgeon et al. [2020]). We later discuss how our model can be adapted to incorporate these
endogenous effects on collateral in Section 6.
The model contains a stablecoin market and two assets: a risky asset (ETH) [6] with exogenous
price _Xt_ and an ETH-collateralized stablecoin STBL with endogenous price _Zt_ . The stablecoin
market connects stablecoin holders, who seek stability, and speculators, who make leveraged bets
backing STBL. The STBL protocol requires the STBL supply to be over-collateralized in ETH by
collateral factor _β_ .
In order to focus on the effects of speculator decisions in this paper, we simplify the stablecoin
holder demand as exogenous with constant unit price-elasticity. This is equivalent to a fixed STBL
demand _D_ in dollar terms, though not quantity. Note that there is no direct redemption process
for stablecoin holders aside from a global settlement/shutdown of the system at par value, which
can be triggered by a governance process (see MakerDAO [2017]).
From a practical perspective, STBL demand is not elastic, at least short-term, even if it were
in principle elastic longer-term. A significant portion of stablecoin supplies are locked in other
applications, like lending protocols and lotteries. These applications promise (in some sense) value
safety in over-collateralization, but don’t guarantee liquidity to withdraw. Additionally, Ethereum
transactions cannot be executed in parallel; during volatile times, transactions can be delayed due
to congestion, causing timely trades (especially involving transfer to/from centralized exchanges) to
fail. This occurs even if, in principle, there is liquidity in these markets. On the other hand, longerterm demand elasticity will naturally depend on the presence of good uncorrelated alternatives. [7]

The speculator has ETH locked in the system and decides the STBL supply, which represents
a liability against its locked collateral. At the start of step _t_, there are _Lt−_ 1 STBL coins in supply.
The speculator holds _Nt−_ 1 ETH and chooses to change the STBL supply by ∆ _t_ = _Lt −Lt−_ 1.
If ∆ _t >_ 0, the speculator sells new STBL on the market for ETH at the market clearing price
_Zt_ . This increases the ETH position _Nt_ . If ∆ _t <_ 0, the speculator buys STBL on the market,
reducing _Nt_ . We denote by _N_ [¯] _t_ the speculator’s locked collateral. Informed by limitations of actual
implementations, we formalize the process ( _N_ [¯] _t_ ) based on ( _Nt_ ). [8] The speculator decides _Lt_ by

- ptimizing expected profitability in the next period based on expectations about ETH returns and
the cost of collateral liquidation if the collateral factor is breached.


6We designate the risky collateral asset as ETH for simplicity. In principle, it could be another cryptoasset or
even outside of a cryptocurrency setting.
7From another perspective, a strategic stablecoin holder would take into account expectations about speculator
issuance and ability to maintain the price target and expectations about a global settlement. This is outside of our
model as formulated.
8In principle, the speculator’s decision could be extended to deciding ¯ _Nt_ in addition to ∆ _t_ . Note however that
this would make most sense if the speculator’s position is further extended to include multiple assets.


6


In this way, the speculator myopically optimize for the next period. A simplification of our
model is a one-off game, which hosts a single period of decision-making before the system is settled
in the final period. In this case, the myopic setup is parallel to major single period games in finance
(e.g., Diamond and Dybvig [1983], Dybvig and Zender [1991], Guimaraes and Morris [2007], Morris
and Shin [1998], Parlatore [2016]). Our results make significant contributions over the existing state

- f research on stablecoins, describing different system behavior depending on initial conditions in

- ne-off games. The more general multi-period form of our model then describes a dynamic process
composed of a series of one-off games with changing initial conditions. Our results also apply more
generally to this multi-period setting, where they are stronger than simply a series of the one-off
version of the results. Both of these contribute to stablecoin modeling as there are not better
candidates for multi-period models at this point, although we later discuss ideas toward adapting
the model into a multi-period control problem.
Given supply and demand, the STBL market clears by setting demand equal to supply in dollar
terms. This yields the clearing price _Zt_ = _LDt_ [.][9][ This clearing equation is related to the quantity]
theory of money and is similar to the clearing in automated market makers Angeris et al. [2020]
but processed in batch.


**2.1** **Formal setup**


We formalize the model as follows. We define the following _parameters_ :


  - _D_ = STBL demand in dollar value (equivalent to constant unit price-elasticity)


  - _β_ = collateral factor for ETH


  - _α ≥_ 1 = liquidation cost multiple (reflecting the fee paid to liquidators)


The system is composed of the following _processes_ :


  - ( _Xt_ ) _t≥_ 0 = exogenous ETH price process in dollars.


  - _Lt_ = stablecoin supply at time _t_ that obeys


_Lt_ = _ζ_ + _Lt−_ 1 + ∆ _t,_


where _Lt−_ 1 _>_ 0 is the speculator’s STBL liabilities from the previous period, ∆ _t_ is the
speculator’s change in liabilities at time _t_ (such that _Lt_ = _Lt−_ 1 + ∆ _t_ ), and _ζ_ is a real number
that modifies circulating supply


  - _Nt_ = speculator’s ETH position at time _t_, including collateral


  - _N_ [¯] _t_ = speculator’s locked ETH collateral at time _t_ (and start of time _t_ + 1)


  - ( _Yt_ ) _t≥_ 0 = speculator’s value process


  - _Zt_ = _L_ _[D]_ _t_ [defines the STBL price process.]


9We can consider constant elasticity STBL demand functions that depend on _Zt_ . Letting _q_ be the quantity

- f STBL demanded at $1 price and assuming a constant price elasticity _−γ <_ 0, the dollar-denominated demand
function is _D_ ( _Zt_ ) = _ZtQ_ ( _Zt_ ) = _Ztq/_ (1 _−_ _γ_ (1 _−_ _Zt_ )) _._ for _γ_ = 1 we obtain the case of constant dollar denominated

demand. In clearing the market, the generalized price process is a linear transformation _Zt_ = _γ_ [1] - _Lqt_ _[−]_ [1] - + 1.


7


We take ( _Ft_ ) _t≥_ 0 to be the natural filtration where _Ft_ = _σ_ ( _X_ 0 _, . . ., Xt, L_ 0 _, . . ., Lt_ ). The system is
driven by the process ( _Xt_ ) subject to the speculator’s decisions ∆ _t_ (equivalently _Lt_ given _Lt−_ 1).
The parameter _ζ_ modifies circulating STBL supply. This could come from an outside amount

- f STBL not created by the speculator (a positive adjustment), or some STBL could essentially be
locked (a negative adjustment). As formulated, our model applies to a system that can be described
with monopolistic agents, or where agents behave similarly (have similar beliefs). With _ζ >_ 0, the
model becomes similar to having heterogeneous agents. Whereas, in general to do this, we would
have to consider both heterogeneous beliefs about the future as well as different _ζ_ s, which together
would be intractable, _ζ_ provides a way to aggregate these various effects in a simpler model. In
particular, we suggest a positive _ζ_ may make numerical results more applicable to real settings.
To simplify the exposition of analytical results going forward, we simplify to the case that _β_ = [3] 2

(the collateral factor used in Maker’s Dai stablecoin) and _ζ_ = 0. _Note that under these conditions,_
_and in the remainder of the paper, we use Lt and Lt interchangeably_ .


**2.2** **Collateral constraint**


The collateral constraint requires the collateral locked in the system to be _≥_ a factor of _β_ times
by liabilities. It applies in both a pre-decision and post-decision sense. The _pre-decision_ version
determines when a liquidation occurs: a liquidation is triggered at the start of time _t_ if the following
condition is breached

¯
_Nt−_ 1 _Xt ≥_ _βLt−_ 1 _._


The _post-decision_ version constrains the speculator’s decision-making, limiting _Lt_ such that


_N_ ¯ _tXt ≥_ _βLt._


Note that the nominal stablecoin price ($1) is used in these constraints instead of the real price
because these are encoded by the protocol’s smart contracts as one of the means toward incentivizing
the $1 target. [10] The collateral factor could be dynamic, in the sense that the governance of the
protocol could vote to change its value. Proposals to change the collateral factor are in practice
infrequent, see `[https://makerdao.world/en/learn/vaults/liquidation/](https://makerdao.world/en/learn/vaults/liquidation/)`, so we consider here
a constant factor. We leave it for future research to model the governance’s decision.


**2.3** **Speculator decides** ∆ _t_ **taking into account real liability value**


We assume the speculator is risk-neutral and optimizes its next-period expected value, taking into
account expectations around liquidations. In particular, this means that the speculator takes into
account the real cost of deleveraging its liabilities in the event it needs to reduce its position in the
next time step and doesn’t simply measure the nominal value of liabilities. Its value at time _t_ is its
nominal equity at the start of period (pre-decision), adjusted by a liquidation effect that describes
how the real value deviates from nominal in the event that the speculator needs to deleverage.
That is

_Yt_ = _Nt−_ 1 _Xt −_ _Lt−_ 1 _−_ liquidation effect _._


A liquidation effect is outlined in a following subsection.


10Conceptually, outside of this model, this has the effect of upper bounding the stablecoin price at _β_ as an arbitrage

- pportunity would be created otherwise.


8


Note that _Nt_ is a function of the decision variable ∆ _t_, and recall _Lt_ = _Lt−_ 1 +∆ _t_ . The speculator
decides ∆ _t_ (equivalently _Lt_ given _Lt−_ 1) to optimize next-period expected value subject to the postdecision collateral constraint in the current period:


max E[ _Yt_ +1 _|Ft_ ]
∆ _t_

s.t. _N_ ¯ _tXt ≥_ _βLt._


Thus the speculator accounts for the expected deviation of real from nominal liability value. If
the expected liquidation effect is small —for instance if the probability that the speculator needs to
deleverage next period is small— then the speculator treats _Lt_ near face value in the optimization
for a mix of short- and long-term reasons. As long as speculators can survive liquidation, they can
expect to dispose of liabilities near face value longer-term when markets are liquid. The protocol
smart contracts also add a precedent for treating liabilities at face value: it is encoded in this way
in the collateral constraint and in the event of global settlement of the system, which is intended to
be be triggered should the system diverge too significantly from the intended structure (and which
would occur in the final period of the one-off version).


**2.4** **Speculator’s collateral at stake**


We consider that the speculator decides on a level of participation as a component of their entire
portfolio. This takes place in a separate optimization problem outside the scope of this model (although we discuss how it could be extended later). The speculator’s level of participation amounts
to the initial collateral at the start of our model–for simplicity, we say this also includes any
amount they have decided beforehand may be accessible to top up collateral later. The speculator’s behavior in our model amounts to maximizing the expected value of this component of their
portfolio. On the other hand, if this were the speculator’s entire portfolio, we note that the story
may be different–e.g., they may want to maximize expected log values as in the Kelly criterion and
would probably choose to participate differently, as is common in problems of leverage if the whole
portfolio is at stake.
We take the speculator’s collateral at stake at the start of time _t_ + 1 to be _N_ [¯] _t_ = _Nt−_ 1 minus
any collateral liquidation that happens at time _t_ . This is consistent with the speculator’s collateral
being blocked: it cannot be used to repurchase STBL in the same step. This means that the
speculator (1) has an outside amount (or is able to borrow) to repurchase STBL if ∆ _t <_ 0 and
then later repays this from unlocking collateral and (2) can’t post proceeds of new STBL issuance
(∆ _t >_ 0) as collateral within the same step.
While there are settings in which we could alternatively use _Nt_ as the collateral at stake at
the start of _t_ + 1 (e.g., if flash loans are used), the choice of _Nt−_ 1 additionally leads to a simpler
exposition of results as it decouples the collateral from the decision variable.


**2.5** **Collateral liquidation mechanics**


In time _t_ + 1, the pre-decision collateral constraint is _N_ [¯] _tXt_ +1 _≥_ _βLt_ . If this is breached, then
the speculator’s collateral is partially liquidated, if possible, to repurchase an amount _ℓt_ +1 _>_ 0 of
STBL. In real protocols, liquidation amounts are automated by an algorithm and will inherently be
first order estimates of the amount needed to rebalance the debt position as the algorithm will not
be able to know the actual market structure and price impact. For instance, liquidations in Maker
and Compound release a certain amount of debt to be repaid, and unlock a corresponding amount

- f collateral that an arbitrager can use to rebalance the debt position (both decided algorithmically


9


in Compound [2019] and MakerDAO [2017], and the latter decided through auction in Maker’s
newer version MakerDAO [2019]). Consistent with these protocols, we set the amount of debt
that needs to be repaid in a liquidation to be _N_ ¯ _tXt_ +1 _−_ _ℓt_ +1 = _β_ ( _Lt −_ _ℓt_ +1). With _β_ = [3] 2 [, this amount is] _ℓt_ +1 of STBL such that post liquidation we have

_ℓt_ +1 = _[β][L][t][ −]_ _[N]_ [¯] _[t][X][t]_ [+1] = 3 _Lt −_ 2 _N_ [¯] _tXt_ +1 _._

_β −_ 1


We interpret this as the protocol’s encoded estimate, using nominal stablecoin price, of how much
collateral it should liquidate in an ‘auction’ to deleverage, similar to Maker. Our model simplifies
the auction to settle on the endogenous stablecoin market. Other liquidation algorithms could also
be considered and would lead to similar qualitative effects.
In a time step with a liquidation, the liquidation forces an upper bound ∆ _t_ +1 _≤−ℓt_ +1 as this
amount would, in the real protocol, be unlocked for arbitrageurs. But the speculator could choose
to repurchase more STBL to further reduce leverage. The repurchase of _ℓt_ +1 through the liquidation
mechanism is subject to a liquidation cost multiple _α ≥_ 1–i.e., the effective repurchase price is _α×_
the STBL market price. The purpose of this fee is that, in real stablecoin systems, liquidations are
performed by arbitrageurs who capture this fee.
Notice that the STBL market price will itself be affected by liquidations. Depending on market
impact, which the algorithms can only observe sequentially, the liquidation may be insufficient to
fully rebalance the debt position back to the collateral constraint. If this occurs, then the issue
will be taken into account with further liquidations in subsequent time steps. The parameter _β_
in real systems is intended to provide safety in such events so that the system does not become
under-collateralized.

Two thresholds are relevant at time _t_ for calculating expectations of a liquidation effect at time
_t_ + 1. These are non-time-dependent functions of the random variable _Lt_ :

_b_ ( _Lt_ ) := _[β]_ ~~¯~~ _[L][t]_

_Nt_



1
_c_ ( _Lt_ ) :=
2 _N_ ~~[¯]~~ _t_



_α_ [2] _D_ [2] + 4 _αDLt_ + _L_ [2] _t_ _[−]_ _[α][D]_ [ +] _[ L][t]_ _._

- ~~[�]~~ 


The threshold _b_ ( _Lt_ ) gives the highest _t_ + 1 ETH price that breaches the collateral constraint while
the threshold _c_ ( _Lt_ ) gives the _t_ + 1 ETH price that consumes the entirety of the speculator’s locked
collateral in a liquidation repurchase due to the effect on STBL repurchase price. [11] Below this level,
the speculator cannot meet the collateral demand even by liquidating everything. The formulation

- f _b_ ( _Lt_ ) follows directly from the collateral constraint; the formulation of _c_ ( _Lt_ ) follows from equating
the repurchase cost of liquidation _ℓt_ +1 to _N_ [¯] _tXt_ +1 and solving for _Xt_ +1.
If _c_ ( _Lt_ ) _≤_ _Xt_ +1 _≤_ _b_ ( _Lt_ ), then the liquidation effect is _ℓt_ +1 _−_ _ℓt_ +1 _Lt−Dℓt_ +1 _[α]_ [. This represents a]

repurchase of _ℓt_ +1 STBL (reducing collateral by the repurchase price _Lt−Dℓt_ +1 [with liquidation fee]
factor _α_ ) and subsequent reduction of the speculator’s liabilities by the _ℓt_ +1. The variables _Lt_ +1
and _Nt_ are affected similarly. [12] If _Xt_ +1 _< c_ ( _Lt_ ), then the speculator’s collateral position is zeroed

- ut in the liquidation. We define the corresponding events


_At_ = _{Xt_ +1 _≥_ _b_ ( _Lt_ ) _}_


_Bt_ = _{c_ ( _Lt_ ) _≤_ _Xt_ +1 _< b_ ( _Lt_ ) _}._


11The probability of a large deviation like this is not zero. For instance, it could represent the possibility of a
contentious hard fork that splits ETH value.
12Note that _Nt_ is affected because this is the locked collateral at time _t_ + 1. Alternatively, working with _Nt_ +1 as
locked collateral, we would update _Nt_ +1.


10


**2.6** **System of random variables**


Putting all the pieces together, we have the following system of random variables driven by the
random process ( _Xt_ ):


_Xt_



_αD_

_Yt_ +1 = [∆] _[t][D][X][t]_ [+1] + ( _N_ [¯] _tXt_ +1 _−_ _Lt_ ) 1 _At∪Bt_ + 1 _Bt_ (3 _Lt −_ 2 _N_ [¯] _tXt_ +1) 1 _−_

_LtXt_     - 2 _N_ ~~[¯]~~ _tXt_ +1 _−_ 2 _Lt_







_β_ 1 _Xt_ _−_ _Lt−_ 1� if _Xt ≥_ _[β]_ _N_ ~~¯~~ _[L]_ _t_ _[t]_ _−_ _[−]_ 1 [1]



∆ _[∗]_ _t_ [=]










¯
min - arg max∆ _t_ E[ _Yt_ +1 _|Ft_ ] _,_ _Nt−β_ 1 _Xt_



_t_ _,_ _β_ _−_ _N_ ~~¯~~ _t−_ 1

min - arg max∆ _t_ E[ _Yt_ +1 _|Ft_ ] _, −_ (3 _Lt−_ 1 _−_ 2 _N_ [¯] _t−_ 1 _Xt_ )� if _Xt <_ _[β]_ _N_ ~~¯~~ _[L]_ _t_ _[t]_ _−_ _[−]_ 1 [1]



 _t_ _,_ _−_ _−_ _−_ _N_ ~~¯~~ _t−_ 1

_Lt_ = _Lt−_ 1 + ∆ _[∗]_ _t_



_Nt_ =


_N_ ¯ _t_ =



_Nt−_ 1 + ∆ _[∗]_ _t_ _XZtt_ if _Xt ≥_ _[β]_ _N_ ~~¯~~ _[L]_ _t_ _[t]_ _−_ _[−]_ 1 [1]

- _Nt−_ 1 + _X_ _[Z][t]_ _t_ [(∆] _[t]_ [ + (1] _[ −]_ _[α]_ [)(3] _[L][t][−]_ [1] _[ −]_ [2 ¯] _[N][t][−]_ [1] _[X][t]_ [))] if _Xt <_ _[β]_ _N_ ~~¯~~ _[L]_ _t_ _[t]_ _−_ _[−]_ 1 [1]



_Nt−_ 1 if _Xt ≥_ _[β]_ _N_ ~~¯~~ _[L]_ _t_ _[t]_ _−_ _[−]_ 1 [1]

- _Nt−_ 1 _−_ _α_ (3 _Lt−_ 1 _−_ 2 _N_ [¯] _t−_ 1 _Xt_ ) if _Xt <_ _[β]_ _N_ ~~¯~~ _[L]_ _t_ _[t]_ _−_ _[−]_ 1 [1]




_−_ _t_ _Xt_ _N_ ~~¯~~ _t−_ 1

_Nt−_ 1 + _[Z][t]_ if _Xt <_ _[β]_ ~~¯~~ _[L][t][−]_ [1]

[(∆] _[t]_ [ + (1] _[ −]_ _[α]_ [)(3] _[L][t][−]_ [1] _[ −]_ [2 ¯] _[N][t][−]_ [1] _[X][t]_ [))]




_−_ ~~¯~~

_Nt−_ 1
_Nt−_ 1 _−_ _α_ (3 _Lt−_ 1 _−_ 2 _N_ [¯] _t−_ 1 _Xt_ ) if _Xt <_ _[β]_ ~~¯~~ _[L][t][−]_ [1]



_X_ _[Z][t]_ _t_ [(∆] _[t]_ [ + (1] _[ −]_ _[α]_ [)(3] _[L][t][−]_ [1] _[ −]_ [2 ¯] _[N][t][−]_ [1] _[X][t]_ [))] if _Xt <_ _[β]_ _N_ ~~¯~~ _[L][t]_ _−_ _[−]_ [1]



~~¯~~
_Nt−_ 1



~~¯~~
_Nt−_ 1



_Zt_ = _[D]_ _._

_Lt_



In the above, the first case for ∆ _[∗]_ _t_ [comes from maximizing expected value subject to the post-]
decision collateral constraint while the second cases for ∆ _[∗]_ _t_ [,] _[ N][t]_ [, and ¯] _[N][t]_ [apply the liquidation effects]
that occur during time _t_ .

### **3 Foundational Results**


In this section, we derive foundational results about the model that we will use to prove the primary
results of the paper in the next section.


**3.1** **Assumptions**


We begin by defining the assumptions we will use in the rest of the paper.


**Assumption 1.** ( _Xt_ ) _is a submartingale with respect to_ ( _Ft_ ) _and is independent from_ ( _Lt_ ) _and_
( _Nt_ ) _._


A submartingale is a stochastic process in which the expected future value, conditioned on all
prior values, is greater than or equal to the current value. The submartingale assumption can
be relaxed somewhat while preserving some results. It is useful, though not necessarily critical,
in our proof of problem concavity. However, the results are most meaningful in a setting like a
submartingale, which always provides a fundamental reason that a speculator might desire leverage.
In such a setting, it is _conceivable_ that the stablecoin could maintain a dollar peg, whereas in long
periods of negative expected returns, the stablecoin concept falls apart as no speculators will want
to participate. As noted in the introduction, such a deviation from the submartingale setting
appears to have occurred in March 2020.


**Assumption 2.** _Each Xt_ +1 _has a conditional probability distribution given Ft, which admits a_
_density function ft that is continuous almost surely._


11


Equivalently, we consider the process in terms of returns _Rt_, where _Xt_ +1 = _XtRt_ +1. Conditioned

- n _Ft_, then _Rt_ +1 admits density function _gt_ . In the i.i.d. setting for ( _Rt_ ), the time dependence can
be dropped. For most results, we do not need to assume i.i.d.


**Assumption 3.** _There is some upper bound r ≥_ sup _n_ E[ _Rn|Fn−_ 1] _._


The next assumption is needed to interchange derivative and integration operators. It also
translates to an upper bound on _Lt_ and a lower bound on _Nt−_ 1.


**Assumption 4.** _There is some upper bound u ≥_ _c_ ( _Lt_ ) _for all Lt._


The next assumption ensures that the STBL price is bounded away from infinity.


**Assumption 5.** _Lt ≥_ _v >_ 0 _for some v._


The next assumption simplifies repurchase considerations. It is reasonable given a reasonable
bound _r_ - n expected returns.


**Assumption 6.** _The liquidation premium factor α is sufficiently high that the repurchase price in_
_a liquidation is >_ 1 _almost surely._


The next assumption translates to a reasonable condition on _X_ distributions considering _b_ ( _Lt_ )
is linearly increasing whereas _c_ ( _Lt_ ) decreases with _Lt_ .


**Assumption 7.** P( _Bt|Ft_ ) = P _c_ ( _Lt_ ) _≤_ _Xt_ +1 _≤_ _b_ ( _Lt_ ) _|Ft_ _is increasing in Lt._

            -            

Define _ψ_ ( _Lt_ ) := E[ _Yt_ +1 _|Ft_ ]. Note that _ψ_ could have a subscript _t_, or equivalently other time
_t_ inputs ( _N_ [¯] _t, Xt, gt_ ), but we relax notation as we only use it in the context of time _t_ . The next
assumption ensures that _ψ_ is concave in _Lt_, a result that we prove in Proposition 1. When
this is not met, the model starts in a strange region in which the speculator’s objective can be
non-concave and real and nominal liability values can be disassociated. This is an artifact of the
simplified structure of demand in the model, which we would expect to adapt in such a setting.
Thus we expect the model to not apply well outside of this assumption. Live stablecoin systems
that remain operational readily satisfy this assumption.



**Assumption 8.** 2( _NcαDtNc−Ltt_ ) [2] _[≤]_ [2] _[ (note][ L][t][ ≥]_ [27] 46




[27] 46 _[α][D][ (or][ αZ][t][ ≤]_ 27 [46]



27 _[is sufficient).]_



Live stablecoin systems readily satisfy this assumption. [13]

Additionally, the next assumption ensures that _ψ_ is _strictly_ concave in _Lt_, which we also prove
in Proposition 1. Notice that this means that _either_ the submartingale inequality is strict at time
_t_ - r there is non-zero probability that a liquidation is triggered in the next step. Given that the
latter is certainly reasonable, this assumption is not much stronger than the basic submartingale
assumption.


**Assumption 9.** _Either_ E[ _Rt_ +1 _|Ft_ ] _>_ 0 _or_ P( _Bt|Ft_ ) = P _c_ ( _Lt_ ) _≤_ _Xt_ +1 _≤_ _b_ ( _Lt_ ) _|Ft_ _>_ 0 _._

                     -                      

While strict concavity of _ψ_ is not necessary for all results, it does simplify the analysis considerably. More generally, concavity of _ψ_ could reasonably be expected in many settings, and so the
assumptions can probably be relaxed. Informally, reasonable distributions for _Xt_ will have concentration about the center. In this case, moving ∆ _t_ in the positive direction, expected liabilities
increase faster than revenue from new STBL issuance. Moving ∆ _t_ in the negative direction, the
cost to buyback grows faster than the decrease in expected liabilities.


13Recall that _α ≥_ 1 is the liquidation cost multiple (reflecting the fee paid to liquidators). Assuming _α_ = 1 _._ 05, the
sufficient condition in Assumption 8 is implied by _Zt <_ 1 _._ 62, which is verified in practice for all live stablecoins.


12


**3.2** **Concavity and scale invariance**


Our first result is to prove that _ψ_ ( _Lt_ ) is concave in _Lt_ .


**Proposition 1.** _Given Assumptions 1-8, ψ_ ( _Lt_ ) := E[ _Yt_ +1 _|Ft_ ] _is concave in Lt._
_Further, given additional Assumption 9, ψ_ ( _Lt_ ) _is_ strictly _concave in Lt._

```
                  [Link to Proof]

```

In deriving some results, it will be useful to make assumptions about the scale of the system.
The next result shows that results about _Zt_ should translate to differently scaled systems, validating
that such results will describe the STBL price process more generally. In the following, we define
_h_ to output _Lt_ as a function of the system state.


**Proposition 2.** _Consider a system setup_ ( _Lt−_ 1 _, D, Nt−_ 1) _with ETH price process_ ( _Xt_ ) _. For γ >_ 0 _,_


_h_ ( _γLt−_ 1 _, γD, γNt−_ 1 _, Xt_ ) = _γh_ ( _Lt−_ 1 _, D, Nt−_ 1 _, Xt_ )

_h_ ( _Lt−_ 1 _, D,_ _γ_ [1] _[N][t][−]_ [1] _[, γX][t]_ [) =] _[ h]_ [(] _[L][t][−]_ [1] _[,][ D][, N][t][−]_ [1] _[, X][t]_ [)] _[.]_


_As a result, the STBL price process_ ( _Zt_ ) _is equivalent across these system rescalings._

```
                  [Link to Proof]

```


Under these condtions, we can interchange derivative and integration operators in _[∂][ψ]_



Under these condtions, we can interchange derivative and integration operators in _∂Lt_ [according]

to Leibniz integral rules (a variation of dominated convergence theorems). The speculator’s choice

- f _Lt_ will fulfill the first order condition of _∂∂Lψt_ [= 0. From concavity, we can then conclude that]
the speculator chooses to increase the STBL supply when _[∂][ψ]_ [(] _[L][t][−]_ [1][)] _[ >]_ [ 0 and to decrease the STBL]



the speculator chooses to increase the STBL supply when _∂Lt_ [(] _[L][t][−]_ [1][)] _[ >]_ [ 0 and to decrease the STBL]

supply when _∂∂Lψt_ [(] _[L][t][−]_ [1][)] _[ <]_ [ 0.]
Note that we can derive sufficient conditions for these events using Lemma 2 from the Appendix.
Such conditions can be useful as concrete interpretations of the events and can be checked against
incoming data. That said, these general sufficient conditions are far from necessary if we are given
additional information about the return distributions.



**3.3** **Economic limits to speculator behavior**


We now present some fundamental results that bound the speculator’s decision-making. These
results will be useful in developing the primary results of the paper in the next section. The next
result introduces a lower bound to the speculator’s STBL supply decision that arises from the
fundamental price impact of repurchasing STBL.


**Proposition 3.** _Suppose the pre-decision collateral constraint is met at time t. There is a com-_
_putable lower bound to_ ∆ _t._


We can interpret the lower bound in terms of a balance sheet constraint describing when the
speculator’s ETH position is exhausted in a repurchase. We give the specific bound in the proof but
note that it is not especially useful on its own. Given information about the returns distribution
and the level of current collateral and considering _∂_ _[∂]_ _L_ _[ψ]_ _t_ [, much better bounds are possible. Note that]

if _ζ >_ 0 is high enough, the lower bound may be the speculator’s entire debt position, which would
be expected in a liquid environment with heterogeneous agents.


13


```
                  [Link to Proof]

```

The next result provides a useful upper bound to the speculator decision _Lt_ . The result is
derived from incentives to issue STBL. Intuitively, it says that if supply is below this bound, then
a speculator may see a profitable opportunity to expand supply. It’s simply not profitable to issue
more STBL than this bound. This doesn’t mean that the speculator decides to achieve the bound,
however, as it underestimates the liquidation costs that the speculator might face. [14] Notice that
the bound is strongest when we have _κ ∼_ 1.


**Proposition 4.** _Suppose either of the following hold for given κ:_







_Xt_

- _c_ _[b]_ ( [(] _L_ _[L]_ _t_ _[t]_ ) [)]

_Xt_



_αDN_ [¯] _tXtz_

- 3 _−_ 2( _N_ ~~[¯]~~ _tXtz−Lt_ ) [2] - _gt_ ( _z_ ) _dz ≤_ 0 _and_ P( _At ∪_ _Bt|Ft_ ) _≥_ _κ_ _[−]_ [1] _>_ 0




  - 1 _≥_ P( _At|Ft_ ) _−_ 2 P( _Bt|Ft_ ) _≥_ _κ_ _[−]_ [1] _>_ 0 _._


_Then Lt ≤_ ~~�~~ _κLt−_ 1 _D_ E[ _Xt_ +1 _|Ft_ ] _/Xt._


`[Link to Proof]` .


The first condition comes from the derivative of the expected liquidation effect with respect
to _Lt_ taking _β_ = [3] 2 [. The integrand can be interpreted as the effective leverage change in a given]

liquidation. This quantity is _<_ 0 evaluated at _b_ ( _Lt_ ) (small liquidations effectively reduce leverage)
whereas it is _>_ 0 evaluated at _c_ ( _Lt_ ) (in very large liquidations, leverage reduction may not be
effective due to effect on repurchase price). The integral condition then says that, in expectation,
liquidations effectively reduce leverage. This is a reasonable assumption given a starting state of
sufficient over-collateralization, since reasonable distributions of _Xt_ +1 will place most mass in the
integral around _b_ ( _Lt_ ) as opposed to _c_ ( _Lt_ ), which is a tail event.
The second (alternative) condition says that the probability of having a liquidation is sufficiently
smaller than not having a liquidation.
This result holds if _either_   - f the two conditions hold, both of which could be checked in datadriven modeling. We will formalize an assumption like the first condition in the next section.
Similar results going forward could be derived instead using a variation on the second condition.

### **4 Stable and Unstable Domains**


The primary results of the paper characterize regions in which the stablecoin price process can be
interpreted as ‘stable’ and ‘unstable’. In this section, we derive these results for the given model

- f a single speculator facing imperfectly elastic demand for STBL. In the next section, we consider
generalizations of the model and how these results will differ given different design and market

structures.


14The model as formulated does not incorporate an interest rate paid by the speculator on issued STBL (the
‘stability fee’ in Dai). Additionally, it does not incorporate a possible yield if the speculator creates STBL to lend on
a lending platform as opposed to selling on the market. Under either of these extensions, Proposition 4 would change
by an appropriate factor.


14


**4.1** **Domain barriers/Stopped processes**


We first establish results in terms of barriers. While the stablecoin process is within certain barriers,
we prove that it behaves in ways that are interpretable as ‘stable’ and ‘unstable’. These barriers
are generally stopping times, and we proceed by considering the stopped processes.
Assume that in the initial condition we have E   - _L_ 11 _[|F]_ [0]   - _≤_ _L_ 10 [. We define the following stopping]
times:


1 1

  - _τ_ is the hitting time of E  - _Lt_ +1 _[|F][t]_  - _>_ _Lt_


  - _Tm_ is the hitting time of _Zt > m_, for _m ≥_ _Z_ 0


  - _S_ 1 is the hitting time of E[ _Lt_ +1 _|Ft_ ] _< Lt_


  - _S_ 2 is the hitting time of E[ _Lt_ +1 _|Ft_ ] _≥Lt_ such that _S_ 2 _> S_ 1.


As we will see, while the stablecoin mechanism is working as intended, we generally expect the
STBL supply to increase (equivalently in this setting, the STBL price to decrease, though in slow
and bounded way). With this context in mind, _τ_ represents the first time we _expect_ the STBL
price to increase. Notice that this is an expectation of reciprocal of supply, a convex function, and
so through Jensen’s inequality, this is weaker than expecting the speculator to deleverage/reduce
supply. In particular, we have _τ ≤_ _S_ 1.
Note that the expectations of the process are not necessarily the same as the movements of the
process: _τ_ does not necessarily correspond to the first time the process actually increases in price.
We track this with _Tm_, the time the STBL price breaches a given level above _Z_ 0, which may be
before or after _τ_ .

The stopping times _S_ 1 and _S_ 2 track when expectations about STBL supply change. These can
be equivalently stated (and calculated in a data-driven model) based on expectations about the
derivative of E[ _Yt_ +2 _|Ft_ ] with respect to _Lt_ +1 evaluated at _Lt_, similarly to the discussion from the
previous section on concavity.
Before proceeding, we formalize stopped versions of assumptions in Proposition 4. The interpretation of these assumptions is the same as discussed in the previous section. Note that the results
going forward could also apply more generally subject to additional stopping times embedding these
assumptions. For notational simplicity, we just present the results subject to the stopping times
already defined with the assumptions given.


**Assumption 10.** _For t ≤_ _τ_ _,_ P( _At ∪_ _Bt|Ft_ ) = P( _Xt_ +1 _≥_ _c_ ( _Lt_ ) _|Ft_ ) _≥_ _κ_ _[−]_ [1] _>_ 0 _._



**Assumption 11.** _For t ≤_ _τ_ _,_ - _c_ _[b]_ ( [(] _XtL_ _[L]_ _t_ _[t]_ ) [)]

_Xt_



_αDN_ [¯] _tXtz_

- 3 _−_ 2( _N_ ~~[¯]~~ _tXtz−Lt_ ) [2] - _gt_ ( _z_ ) _dz ≤_ 0 _._



Notice that _κ_ will be _>_ 1 but _∼_ 1 as _X < c_ ( _Lt_ ) is a low probability event.
Recall that the STBL price _Zt_ is a function of collateral value, expectations about ETH returns,
and expectations of liquidation costs (related to tail risks). These factors enter the speculator’s
supply decision, which then enters _Zt_ . Going forward, we will explore how changes in these affect
the STBL price process.


15


**4.2** **‘Stable’ domain**



Subject to the barriers _τ_ and _Tm_, the stablecoin process can be interpreted as stable in the following
ways. In this domain, we derive bounds on large price movements and quadratic variation. We
show below that for realistic values of parameters, the bounds are sufficiently powerful in practice.
Our first result bounds _Zt_ under the condition _TZ_ 0 _> τ_ . Conditioned on this, the price is
contained within small variation–e.g., consider _Z_ 0 = 1 and consider _κr_ [1] _[∼]_ [1. Recall that] _[ r]_ [ represents]

E[ _Xt_ +1]
the upper bound on returns, _r_ = sup _t_ _Xt_, whereas _κ_ _[−]_ [1] is a lower bound for the probability that

the collateral is not exhausted in a liquidation event, P( _Xt_ +1 _≥_ _c_ ( _Lt_ ) _|Ft_ ) _≥_ _κ_ _[−]_ [1] .



**Proposition 5.** _If TZ_ 0 _> τ_ _, then_


_Z_ 0 _≥_ _Zt∧τ ≥_




~~�~~



_D_ _D_
_κLt∧τ_ _−_ 1 _r_ _[≥]_ 2 _[t]_



2 _[t]_ _−_ 1
( _κDr_ ) 2 ~~_[t]_~~



2 ~~_[t]_~~ _L_



1
2 ~~_[t]_~~
0



_._



_Furthermore for any t, Lt∧τ ≤_ _κDr and Zt∧τ ≥_ _κr_ 1 _[.]_

```
                  [Link to Proof]

```

The condition _TZ_ 0 _> τ_ introduces dependence on future events. As such, we can’t conclude
with the information at time _t_ that the _t_ + 1 price is bounded in this way.
However, we can bound our expectations on the _t_ +1 price given the information at time _t_ ( _Ft_ ).
This approach relies on the fact that the versions of the process behave as submartingales in the
stopped setting.


**Proposition 6.** ( _Lt∧τ_ ) _is a submartingale bounded above and_ ( _Zt∧τ_ ) _is a supermartingale bounded_
_below. Thus they converge almost surely._

```
                  [Link to Proof]

```

An immediate bound on expected price comes from the fact that stopped version of _Zt_ is a
supermartingale. This is the first result of the next proposition. Additionally, with a stronger
assumption on ( _Xt_ ) that conditional expectation of returns is non-decreasing within the domain
barriers, we can bound the expected price further.


**Proposition 7.** _The process_ ( _Zt∧τ_ _∧TZ_ 0 ) _is bounded in expectation by_

_Z_ 0 _≥_ E[ _Zt∧τ_ _∧TZ_ 0 ] _≥_ _κr_ [1] _[.]_


_Further, assuming that for t < τ_ _,_ (E[ _Rt_ +1 _|Ft_ ]) _is non-decreasing, then for t ≤_ _τ_ _,_



_Zt−_ 1 _≥_ E[ _Zt∧τ_ _|Ft−_ 1] _≥_




~~�~~



_D_

_κLt−_ 1 E[ _Rt|Ft−_ 1] _[.]_


```
                  [Link to Proof]

```

Going forward, we will work with a variation on the price process


_Zt_ _[′]_ [:=] _[ |][m][ −]_ _[Z][t][|]_ for given _m ≥_ _Z_ 0 _._


Using _m_ = 1, this has concrete interpretation as the absolute price deviation from the stablecoin
peg. The stopped version of this process has the useful property of being a non-negative submartingale. In addition, ( _Zt_ _[′]_ [) shares similar large deviation and quadratic variation properties with (] _[Z][t]_ [),]
which we explore in the remainder of this subsection.


16


**Lemma 1.** _The stopped process_ ( _Zt_ _[′]_ _∧τ_ _∧Tm_ [)] _[ is a non-negative submartingale.]_

```
                  [Link to Proof]

```

We define the maximum process over some process ( _θt_ ) as _θN_ _[∗]_ [= max] _[t][≤][N][ |]_ [Θ] _[t][|]_ [. The next result]
bounds the expected maximum of the deviation process ( _Zt_ ).


**Proposition 8.** _Suppose m ≥_ _Z_ 0 _. Denote E_ := E[ _Zτ_ _∧Tm −_ _m|Zτ_ _∧Tm > m_ ] _. Suppose any one of_
_the following conditions holds:_


1 1

  - _κr_ _[> m][ and][ E >]_ _κr_ _[−]_ _[m]_


1

  - _κr_ [=] _[ m][ and][ E >]_ [ 0]


1

  - _κr_ _[< m][ and][ E][ ≥]_ [0] _[.]_

_Then_ E[ _Zτ_ _[′∗]_ _∧Tm_ []] _[ ≤]_ [2] - _m −_ _κr_ [1] - _._

```
                  [Link to Proof]

```

The value ( _m −_ _κr_ [1] [) describes the range of the domain considered. Prior to] _[ T][m]_ [, we know that]

the price falls in this range. The nontrivial part is describing what happens at the stopping time
as it _exceeds_ this range if the stop is triggered by _Tm_ . The value _E_ is the expected deviation at the
stopping time _given_ that _Tm_ triggers the stop. By definition, we have that _E >_ 0. Given reasonable
_κ_, _r_, and _m_, the condition for Proposition 8 is satisfied quite broadly. For instance, the concrete
instance with _m_ = 1 is satisfied since _κr_ 1 _[<]_ [ 1 taking into account the above discussion on] _[ κ]_ [.]
Notice that the analysis for the proof can lead to better bounds if we have more information
about _E_ - r _p_ := P( _Zτ_ _∧Tm ≤_ _m_ ), e.g., by incorporating information from other results above or from
knowledge about the distributions of ( _Xt_ ), such as from historical data. Additionally, the analysis
can be used to bound either _E_ - r _p_ given bounds on the other.
We now state the first main results of the paper. Our next result applies Doob’s inequality to
bound the probability of large deviations in the stopped process.


**Theorem 1.** _For m ≥_ _Z_ 0 _and ϵ >_ 0 _,_



P - _n≤_ max _τ_ _∧Tm_ _[Z]_ _n_ _[′]_ _[> ϵ]_ - _≤_ 2 _ϵ_ _[−]_ [1] - _m −_ _κr_ [1]



_._



```
                  [Link to Proof]

```

The result can be quite powerful. Consider the concrete case of _m_ = 1, in which case _Zt_ _[′]_
describes the deviation from the peg, and take (arguably reasonable) _κ_ _[−]_ [1] = 0 _._ 999 (99 _._ 9% chance
_Xt_ won’t drop below _c_ ( _Lt_ )) and _r_ annualized as 1.5 (daily _r_ = 1 _._ 0011). Then the probability that
the stablecoin deviates from the peg by more than 0.1 is P( _Zτ_ _[′∗]_ _∧T_ 1 _[>]_ [ 0] _[.]_ [1)] _[ ≤]_ [0] _[.]_ [042.]
Our next result derives from a form of Burkholder’s inequality that applies to non-negative
submartingales. We define the quadratic variation of ( _Zt_ _[′]_ [) by]




[ _Z_ _[′]_ ] _t_ :=



_t_

- ( _Zk_ _[′]_ _[−]_ _[Z]_ _k_ _[′]_ _−_ 1 [)][2] _[.]_


_k_ =1



The quadratic variation is a stochastic process that measures how spread out the underlying process
is. Its expectation at time _t_ is related to the variance at that time, supposing variance is defined–
in particular, they are equal if the underlying process is a martingale. The result bounds the
probability of large quadratic variation in the stopped process. In essence, with high probability,
the quadratic variation can’t be _too far_ away from the expected maximum.


17


**Theorem 2.** _Suppose m ≥_ _Z_ 0 _and ϵ >_ 0 _. Then_




[ _Z_ _[′]_ ] _τ_ _∧Tm > ϵ_ _≤_ 6 _ϵ_ _[−]_ [1] _m −_ [1]

     -     - _κr_



P - ~~�~~



_κr_



_._



```
                  [Link to Proof]

```

This result is also quite powerful. Considering the same setting as above, we have


P( ~~�~~ [ _Z_ _[′]_ ] _τ_ _∧T_ 1 _>_ 0 _._ 1) _≤_ 0 _._ 127


in the stable domain.

Bounds on the expectation of quadratic variation can also be obtained using a more classical
form of Burkholder’s inequality, albeit with stronger assumptions. We develop this idea in the next
remark.


**Remark 1.** _There is an additional form of Burkholder’s inequality that extends to non-negative_
_p_ [�]
_submartingales. If we are additionally given a useful bound on_ E - � _Zτ_ _[′]_ _∧Tm_ - _for some_ 1 _< p < ∞_
_(for instance, if we have some distribution assumptions on_ ( _Xt_ ) _), then we can apply Lemma 3.1 in_
_Burkholder [1973] to derive the following bound on quadratic variation expectations:_



1
_p_ 9 _p_ 2 _p_ [�] _p_ [1]

[1] _≤_ 1 _−_ _p_ _[−]_ [1] [E] - � _Zτ_ _[′]_ _∧Tm_ 


_p_ [�] _p_ [1]
E [ _Z_ _[′]_ ] _τ_ _∧Tm_ 
 - �



_p ._



_A topic of ongoing research is obtaining the Best constants/bounds in Burkholder’s inequality,_
_which may be able to tighten the bound. The classical two-sided Burkholder inequailty may not_
_extend to non-negative submartinagales. In general, only the first half of the Burkholder inequality_
_(bounding expectations about quadratic variation by the maximum) extends to this setting and only_
_for_ 1 _< p < ∞. This contrasts with Proposition 2, where we can derive results about probability of_
_large quadratic variation of non-negative submartingales for the p_ = 1 _case. From a practical point_

_of view, this may be sufficient._


Notice that with an effective bound on the expectation of quadratic variation (QV) of the entire
stable process, we have by law of large numbers


_QV_

_→_ 0 as _n →∞._
_n_


So the longer the process is stable, the smaller the variability.
As we’ve characterized this ‘stable’ domain based on _τ_ and _Tm_, an exit from this region corresponds to either a change in expectations ( _τ_ ) or a large deviation event ( _Tm_ ). In actual applications,
we will know when these stopping times arrive (or will at least have good measures of it, when
hard to directly observe). These could be used by system stakeholders as indicators that the local
regime is changing. Statistical analysis on historical data could also predict how likely we are to
see such indicators in coming steps.


**4.3** **‘Unstable’ domain**


We now characterize how the stablecoin can be interpreted as unstable outside of the barriers
described above. The intuition here is that the speculator’s position is nearer to _c_ ( _Lt_ ) and _b_ ( _Lt_ ),
and so expected costs of liquidation increase and are more sensitive to the threshold proximity,


18


in addition to being driven by the volatile process ( _Xt_ ). The remaining results in this section
characterize a deflationary regime that is connected with instability in terms of forward-looking
variance of stablecoin prices and large deviations. In this regime, we observe deleveraging spirals,
which resemble short squeezes, and are counterintuitive as they lead to stablecoin price appreciation
during times of collateral shock and lead to faster collateral drawdown.
Our next result characterizes a deflationary regime defined by stopping times _S_ 1 and _S_ 2. In
such a setting, an opposite behavior occurs compared to the stable region: ( _Zt_ ) behaves as a
submartingale, tending to increase in price. The submartingale nature of the stablecoin price
underpins the short squeezes within _deleveraging spirals_ .


**Theorem 3.** _Restarting the process at S_ 1 _, we have that_ ( _Lt∧S_ 2) _is a supermartingale and_ ( _Zt∧S_ 2)
_is a submartingale._

```
                  [Link to Proof]

```

The previous result guarantees that the process, after crossing _S_ 1, enters a deflationary regime
in a precise sense. This deflationary regime can be triggered by the factors affecting _S_ 1, such as
any of the following: shocks to collateral levels, increased expectations around deleveraging costs,

- r depressed ETH expectations. Similarly to the results above, in real applications, these stopping
times can be used by stablecoin stakeholders as indicators that the local regime is changing and to
statistically estimate the probable lengths of such deleveraging spirals.
The intuition behind deleveraging spirals is illustrated in Figure 2. In an equilibrium, the
stablecoin supply is matched to demand. As a first wave of speculator liquidations occur, whether
voluntary deleveraging or automated by the protocol, collateral is used to repurchase the stablecoin
to reduce the supply. In an imperfectly elastic market, this causes an imbalance in demand relative
to supply, and an increase in stablecoin price is needed to reduce demand. This has an amplifying
effect, however, in follow-on rounds of liquidations: more collateral is needed to reduce supply by
the same amount because of the increased stablecoin price, and each round of liquidations continues
to increase the stablecoin price.
Black Thursday in March 2020 provides strong evidence of deleveraging spirals in the Dai
stablecoin. ETH price crashed _∼_ 50% on 12 March 2020 (Figure 3a) This triggered a wave of
liquidations in Dai, as well as other cryptocurrency systems. These liquidations led to a cornering
effect from deleveraging spirals in the Dai market, as shown in Figure 3b. Speculators faced
premiums in excess of 10% to deleverage during the crisis and lingering premiums _>_ 2% several
weeks after. The cornering effect is also supported by lending rates on Dai, which reached high
double digits during the crisis (Figure 3c). Maker was also affected by global mempool flooding on
Ethereum during the crisis, which caused many Dai liquidation auctions to clear at near zero prices.
This had the effect of amplifying the deleveraging effect on collateral and led to a $4m shortfall in
the system. See Blocknative [2020], Topbottom [2020] for more details. Many market participants
were surprised in this crisis that Dai traded at significant premiums despite the much riskier state

- f Maker in terms of collateral and liquidations, which our model explains as deleveraging spirals.


**Remark 2.** _(Interaction with cascading liquidations) A different type of deleveraging spiral can_

_occur in debt security models when the collateral asset price is endogenous to the model and can_
_be depressed from the market impact of liquidations (e.g., fire sales). In this context, liquidations_
_can cascade with a first round of liquidations triggering a follow-up rounds due to the impact on_
_the collateral market. Conceptually, when this endogenous collateral effect is added to our model,_
_the two deleveraging spiral types amplify each other. In particular, when the price of the stablecoin_
_increases from the effects described above, more collateral must be liquidated to deleverage the same_


19


Figure 2: Illustration of deleveraging spirals. In liquidations, collateral is used to reduce supply.
Stablecoin price rises in response to imbalance with demand. This has an amplifying effect in
follow-on liquidations.


(a) (b)


(c)


Figure 3: Black Thursday in March 2020. (a) _∼_ 50% ETH price crash (OnChainFX). (b) Deleveraging effects on Dai price and volatility (OnChainFX). (c) Deleveraging effects on Dai lending rate
(LoanScan)


20


_amount, and this greater collateral liquidation has a higher impact on the collateral asset market,_
_which can trigger further liquidations cyclically in larger size than with the fire sale effect solely._
_We discuss how to endogenize collateral asset prices to the model in the Appendix._


We now derive practical tools that will connect these regimes containing deleveraging spirals
with instability in terms of forward-looking price variance of the stablecoin, and which do not
require the detection of whether _S_ 1 has occurred. This formalizes the high price variation observed
in Dai during and after Black Thursday. We begin in the next remark by setting up a variance
estimation idea based on Taylor approximation.


**Remark 3.** _(Estimating variances) Taylor approximations can be applied to estimate the variances_

_of the stablecoin process. Consider Xt_ = _Xt−_ 1 _Rt for return Rt ≥_ 0 _. For notational clarity, define_ [15]


_h_ ( _ρ, n_ ) := arg max
_Lt_ [E][[] _[Y][t]_ [+1] _[|F][t]_ [] =] _[ L][t][,]_


_where ρ, n are realizations of Rt,_ _N_ [¯] _t. Variance in stablecoin supply follows_


2
_Var_ ( _Lt|Ft−_ 1) _≈_ _h_ _[′]_ [ �] E[ _Rt|Ft−_ 1] _,_ _N_ [¯] _t_           - _Var_ ( _Rt|Ft−_ 1)


_and the stablecoin price_ _**variance approximation**_ _is_


_Var_ ( _Zt|Ft−_ 1) _≈_ _[D][h][′]_ [(][E][[] _[R][t][|][F][t][−]_ [1][]] _[,]_ [ ¯] _[N][t]_ [)][2] _Var_ ( _Rt|Ft−_ 1) _._ (1)

E[ _Lt|Ft−_ 1] [4]


_This is given informally, but could in principle be formalized using two steps of compounded Taylor_
_approximation error. The approximation error is arguably moderate considering that our domain_
_is bounded away from singularities (e.g., our lower bound results on L)._


This variance approximation (Eq. 1 in Remark 3) is low in the stable domain and can be
high in the unstable domain, as formalized in the following Theorem 4. We introduce a few
more assumptions that we use only in deriving the remaining results in this section. All of these
assumptions come down to assumed properties of the _Rt_ distribution.


**Assumption 12.** _The post-decision collateral constraint at time t is not binding in the speculator’s_

_maximization._


This first assumption means that the speculator’s objective fully accounts for the post-decision
collateral constraint (i.e., by maximizing the objective, the speculator by extension also satisfies
the constraint). This is reasonable unless expected returns are excessively high.


**Assumption 13.** _Returns Rt−_ 1 _and Rt are independent._


**Assumption 14.** _ψ is twice continuously differentiable._


This last assumption restricts the density _gt_ . We now present the result, which applies the
implicit function theorem to derive the derivatives of _h_, which describe the sensitivity of _h_ to price
and collateral level.


**Theorem 4.** _Under the above assumptions, the following hold:_


_1._ _∂_ _∂_
_∂ρ_ _[h]_ [(] _[ρ, n]_ [)] _∂n_ _[h]_ [(] _[ρ, n]_ [)] _[ exist;]_


15As in the case of _ψ_, _h_ could have a subscript _t_ (or equivalently other time _t_ inputs), but we relax notation as we

- nly use in the context of time _t_ .


21


[1]

_ρ_ _[for][ ρ][ ≥]_ _X_ _[b][t]_ _t_ _[−]_ _−_ [1] 1



_2._ _∂_ [1]
_∂ρ_ _[h]_ [(] _[ρ, n]_ [)] _[ ≥]_ [0] _[ and is increasing in][ −][ρ][ by order of]_ _ρ_




_[t][−]_ [1]

_Xt−_ 1 _[,][ L][t][ >]_ [ 8] _[;]_



_n_ [1] _[for][ n][ ≥]_ _[b]_ _X_ _[t][−]_ [1]



_3._ _∂_ [1]
_∂n_ _[h]_ [(] _[ρ, n]_ [)] _[ ≥]_ [0] _[ and is increasing in][ −][n][ by order of]_ _n_




_[t][−]_ [1]

_Xt_ _[,][ L][t][ >]_ [ 8] _[;]_



_4. ∃ε with_ 0 _< ε <_ 1 _, s.t._ _∂ρ∂_ _[h]_ [(] _[ρ, n]_ [)] _[ >]_ [ 1] _[ if][ ρ < ε][,][ L][t][ >]_ [27] 46 _[α][D][, and][ c][t][ >]_ [ 2] _[.]_



1 ~~¯~~ 1
_As a result, the variance approximation in Eq. 1 increases by order of_ _Rt_ [2] _[in][ −][R][t][ and]_ _Nt_ [2] _[in][ −][N]_ [¯] _[t][.]_

```
                  [Link to Proof]

```

Theorem 4 shows that the variance approximation in Eq. 1 in Remark 3 increases by order of
1
_Rt_ [2] [during an ETH return shock (result 2). Recall that] _[ R][t]_ [ is multiplicative return, and so the effect]
is large for a significant shock _Rt <_ 1. Similarly, settings with lower collateralization in the initial
~~¯~~ 1
conditions have higher variance approximation by order of _Nt_ [2] [(result 3). Such differences in initial]
conditions of collateral could result from, for example, different realizations of liquidations or the
speculator abandoning its collateral position (and so extracting any excess collateral it can). Result
4 shows that there are cases where the _h_ _[′]_ factor in the variance approximation is _>_ 1, meaning that
the variance of _Rt_, the inherently volatile process, will carry through directly to _Zt_, the ‘stable’

process.
Note that the extra conditions on the scale of _Lt_ and _ct_ in Theorem 4 results 2-4 may seem
strange at first sight. Since the ( _Zt_ ) process is scale-invariant, as proven in Proposition 2, the
results about _Zt_ variance hold more generally. In particular, recall that a term of _∼_ _L_ 1 _t_ [shows up]
in the variance approximation in Remark 3, which will cancel out the conditions on scale.
Up to this point, we have only been able to say things about variance estimations. We will
now show that the ‘stable’ and ‘unstable’ regimes are well-interpreted in the following sense: given
different initial conditions of the same process, the forward-looking stablecoin price variances are
indeed distinct. If we start in the unstable regime, we will always have higher variance than if we
start in the stable regime. The next result formalizes this.


**Theorem 5.** _In addition to the previous assumptions, suppose Xt ≥_ _b_ ( _Lt−_ 1)+ _ϵ for some ϵ >_ 0 _(the_
_pre-decision collateral constraint is exceeded by ϵ, which restricts the ranges of both Xt and_ _N_ [¯] _t−_ 1 _)._
_Consider two possible statesN_ ¯ _t_ _[s]_ _−_ 1 _[> N]_ _t_ _[u]_ _−_ 1 _[and evolve driven by the common price process]_ _s and u of the stablecoin at time t_ [ (] _that differ only in collateral amounts_ _[X][t]_ [)] _[. Then the forward-looking price]_
_variances satisfy_
_Var_ ( _Zt_ _[s][|F][t][−]_ [1][)] _[ <][ Var]_ [(] _[Z]_ _t_ _[u][|F][t][−]_ [1][)] _[.]_

```
                  [Link to Proof]

```

Special care should be given to the treatment of _Zt_ under the condition _Xt ≤_ _c_ ( _Lt−_ 1), as the
STBL price may no longer be well-defined without _ζ >_ 0 as no collateral remains. In a real system,
this is equivalent to the event that all speculators are wiped out. The reason for our condition

- n _Xt_ in the above result is partly to keep things well-defined and partly because there can be a
non-smooth point in _h_ at _Xt_ = _b_ ( _Lt−_ 1).
Similar variance difference results can be derived for varying initial conditions of _Xt−_ 1 and _Lt−_ 1
as opposed to _N_ [¯] _t−_ 1. In some sense, these are all similar as they change the initial collateralization
level, though there will be some difference in price effect.
These analytical results describe regimes in which the stablecoin can be interpreted as stable
and unstable. As we have discussed, they can be adapted into data-driven risk tools, for instance


22


to estimate probabilities of peg deviations and to infer about how likely regimes are to change in
the near future.

While these results apply over limited steps ahead–e.g., forward-looking variance is derived for
the next time period–they _do_ point in the right direction that stability domains are related to
traditional measures in finance. Naturally, it would be good to have results describing further
periods into the future. In principle, these could be estimated, although the process in this section
is already complex. The fact that we are able to relate these regimes analytically to forward-looking
variance is already a step ahead, and a valuable new result in its own right. We conjecture that it
could work similarly over multi-steps, though in less tractable ways.

### **5 Stability in ‘Perfect’ Settings**


In the previous section, we considered the given model of a single speculator facing imperfectly
elastic demand for STBL. We now consider idealized settings, in which STBL demand is perfectly
elastic and/or unlimited speculator supply exists. In these idealized settings, we demonstrate that
stablecoin can be interpreted as well-stabilized.


**5.1** **Perfectly elastic demand**


Under perfectly elastic demand, STBL demand is time-dependent _Dt_, which adapts in each time
period to match STBL supply. This results in _Zt_ = 1. In this case, the speculator’s issue and
repurchase price is always $1 and $ _α_ in a liquidation. The problem simplifies to evaluating


_∞_
E[ _Yt_ +1 _|Ft_ ] = ∆ _t_ E[ _Rt_ +1 _|Ft_ ] + ( _N_ [¯] _tXtz −Lt_ ) _g_ ( _z_ ) _dz_

                     - _ct_

_Xt_



_bt_
_Xt_
+ (1 _−_ _α_ )

    - _ct_

_Xt_



_βLt −_ _N_ [¯] _tXtz_

_g_ ( _z_ ) _dz,_
_β −_ 1



_NtXt_ +1
where the liquidation effect is now _ℓt_ +1(1 _−_ _α_ ) where _ℓt_ +1 = _[β][L][t][−]_ _β−_ [¯] 1 .

In this setting, we have _∂_ _[∂]_ _L_ _[ψ]_ _t_ [=][ E][[] _[R][t]_ [+1] _[|F][t]_ []] _[−]_ [P][(] _[A][t][ ∪]_ _[B][t]_ [)] _[−]_ _β−β_ 1 [(] _[α]_ _[−]_ [1)][ P][(] _[B][t]_ [). Recalling that][ P][(] _[A][t]_ [)]

and P( _Bt_ ) are functions of _Lt_ and supposing a non-binding collateral constraint, the speculator
chooses _Lt_ such that

_β_
E[ _Rt_ +1 _|Ft_ ] = P( _At ∪_ _Bt_ ) +
_β −_ 1 [(] _[α][ −]_ [1)][ P][(] _[B][t]_ [)] _[.]_


Noting that E[ _Rt_ +1] _≥_ 1, P( _At ∪_ _Bt_ ) is decreasing in _Lt_ but generally _∼_ 1, and P( _Bt_ ) is increasing
_β_
in _Lt_, this is interpretable as the speculator balancing expected return against _β−_ 1 _[×]_ [ the expected]
(constant) liquidation cost in deciding whether to issue a new unit of STBL.
In this setting, the STBL price is identically $1 and the speculator only faces the risk of leveraged
ETH declines subject to a fixed liquidation fee. Liquidations generally work well to keep the system

- ver-collateralized, and the only real risk to STBL holders is from extreme single period declines
in ETH price.


**5.2** **Unlimited speculator capital supply**


Suppose there is an infinite depth of speculator’s capital ready to enter the STBL market given what
they see as a profitable opportunity subject to STBL demand _D_ . The speculator in such a market
would choose to deposit collateral and issue new STBL at time _t_ if _[DL]_ _L_ _[t]_ [2] _t_ _[−]_ [1] E[ _Rt_ +1 _|Ft_ ] _−_ _γ ≥_ 0, where


23


_γ_ represents the representative speculator’s expected liability and liquidation cost after entering the
market. Arguably, _γ ∼_ 1 as, in an infinite depth market, the speculator can start from a position

- f low leverage.
The speculator’s profitability (for the marginal STBL issue) will be 0, which yields equality in
the above condition, and therefore,


_Lt_ = ~~�~~ _γDLt−_ 1 E[ _Rt_ +1 _|Ft_ ] _._


Notice the similarity with the upper bound in Proposition 4.
Further using that ( _Xt_ ) is a submartingale, in which case E[ _Rt_ +1 _|Ft_ ] _≥_ 1, we find the STBL
price is constrained to a small range of _Z_ 0 _≥_ _Zt ≥_ 1
_γr_ [. This resembles the perfectly elastic demand]
case. In this case speculators are able to liquidate positions without influencing STBL price, while
in the infinite depth case because the speculator is always willing to issue new STBL to offset a
liquidation.


**5.3** **No stable region if** ( _Xt_ ) **is not a submartingale**


The mechanisms that make the idealized settings well-stabilized break down when the ETH price
process ( _Xt_ ) is not a submartingale. This stresses how fragile the stablecoin market is to negative
expectations in the primary ETH market, even under these idealized settings. In the unlimited
speculator case, speculators no longer enter the market if expectations are negative, and so we
don’t achieve the supply bound developed above. Instead, we return to the main setting of the
paper, which can be interpreted as unstable under negative expectations as it leads to deleveraging
effects. In the perfectly elastic demand setting, the STBL supply goes to zero as the speculator
chooses not to participate.

### **6 Discussion**


This paper presents a new stochastic model of non-custodial over-collateralized stablecoins, where
the collateral has value exogenous to the stablecoin system and the stablecoin has an endogenous
market price. These stablecoins bear a resemblance to a non-custodial form of the current monetary
system of commercial bank money but give rise to new risks such as those experienced on Black
Thursday. These stablecoins stand in contrast to unbacked or endogenously backed stablecoins, such
as Terra UST, which are better understood using tools of insolvency and currency peg models, as
well as custodial stablecoins such as Tether, which can resemble the underlying structures of narrow
banks or money market funds.
In our model, we formally characterize domains that can be interpreted as stable and unstable
for the stablecoin. By bounding the probability of large deviations and the quadratic variation of
the price process, we prove that the stablecoin behaves in a stable way when restricted to a certain
region. In contrast, price variance is shown to be distinctly greater in a separate region. This
is triggered by large deviations, collapsed expectations, and liquidity problems from deleveraging.
We also characterize a deflationary deleveraging spiral as a submartingale, which can exacerbate
liquidity problems in a crisis. These deleveraging spirals resemble short squeezes, and are counterintuitive as they lead to stablecoin price appreciation during times of shock, whereas we might

- therwise expect prices to depreciate given the riskier state of the system. Further, this appreciation is detrimental: it leads to faster collateral drawdown, and potentially shortfalls, as more
collateral is required to fulfill liquidations and is accompanied by higher price variance.
An observation from the model is that the speculator chooses a collateral level _above_ the required
collateral factor. This is because the expected liquidation cost is greater than the $1 face value. The


24


speculator will desire to increase the collateralization during times when the expected liquidation
cost is higher, which can occur after a shock to collateral value or if the speculator expects the
collateral to be more volatile. This generally explains the high level of over-collateralization seen
in Dai, which typically ranges 2 _._ 5 _−_ 5 _×_ although the collateral factor is 1 _._ 5 _×_ .
The presence of deleveraging effects poses fundamental trade-offs in decentralized design. One
way to bring the stablecoin closer to the ‘perfect’ stability cases is to increase elasticity of demand.
This relies on the presence of good uncorrelated alternatives to the stablecoin. As all non-custodial
stablecoins likely face similar deleveraging risks, greater elasticity relies on custodial stablecoins

- r greater exchangeability to fiat currencies. Another way to bring the stablecoin closer ‘perfect’
stability is to increase the supply of new speculators. As there will not be unlimited supply of
speculators with positive ETH expectations (especially during an extended bear market), this relies

- n having another uncorrelated collateral asset. As all decentralized assets are very correlated, this
again largely relies on including custodial collateral assets, like Maker’s recent addition of USDC. [16]

While these measures strengthen the stability results, it’s at the expense of greater centralization
and moves the system away from being ‘non-custodial’.
We suggest a way to improve the design of Dai’s savings pool toward damping deleveraging
effects without greater centralization through incentivizing exchangeability of Dai during deleveraging events. In its current state, the Maker system charges fees to speculators, part of which it
passes on to Dai holders as an interest rate if the holder locks the Dai into a savings pool. With
modified mechanics, this savings pool can provide a buffer to deleveraging effects. For instance,
if we allow Dai in the savings pool to be bought out at a reasonable premium to face value by a
speculator who uses it to deleverage, then deleveraging effects are bounded by the premium amount
up to the size of the savings buffer. The Dai holders who participate in this savings pool are then
compensated for providing a repurchase option to the speculator. The Dai holder could elect to
have the repurchase fulfilled in the collateral asset, or something else, like a custodial stablecoin.
In this way, this mechanism can provide some of the benefits of the ‘perfect’ stability settings while
enabling Dai holders to choose how decentralized they want to be. A Dai holder who does not require high decentralization would elect to receive the compensation from the savings pool whereas
a Dai holder who requires higher decentralization would choose not to use the savings pool. Our
model can be extended to consider such mechanisms.

Since the release of our paper, mechanisms resembling this, which try to boost liquidity around
liquidations to quell deleveraging spirals, have been adopted by projects such as Liquity [2020].
Empirically, these mechanisms have the effect of smoothing deleveraging effects over a longer time
period, lowering the effect of shocks but not entirely removing the short squeeze effect (see Figure 4).
Maker has chosen to go a different direction by maintaining direct exchangeability with the custodial
USDC MakerDAO [2020b], which has allowed Dai to maintain a close peg through subsequent crises
at the expense of heavy reliance on custodial stablecoins. The stablecoin Rai has chosen a third
path of instituting negative rates on stablecoin holders during crises Reflexer [2020] via a PID
controller, which is effectively charging stablecoin holders insurance premiums when demand for
stablecoins outweights demand for leverage, thus lowering demand to help attain peg.
Our model and results can also apply more broadly to synthetic and cross-chain assets and overcollateralized lending protocols that allow borrowing of illiquid and/or inelastic assets– whenever


16Recall that custodial assets face their own risks, however, which may not be uncorrelated in extreme crises.
Custodial stablecoins are subject to counterparty risk, systematic risks, bank run risks, asset seizure risk, and effects
from negative interest rates. The treasury secretary J. Yellen referred to the materialization of these risks in her
annual testimony in front of the Senate Banking Committee, on May 10th 2022: “A stablecoin known as TerraUSD
experienced a run and declined in value,” Yellen said. “I think that this simply illustrates that this is a rapidly
growing product and there are rapidly growing risks.”


25


Figure 4: Effect of Liquity’s stability pool on LUSD price in Curve’s on-chain market in the May
2021 crisis. Deleveraging effect is delayed and smoother compared to Dai’s price effect on Black
Thursday (cf. Figure 3b).


the mechanism is based on leveraged positions and leads to an endogenous price of the created

- r borrowed asset. We have characterized the risk that such structures feature intertwining of
collateral liquidation spirals and short squeezes of the created asset. Synthetic assets generally use
a similar mechanism just with a different target peg. Cross-chain assets that port an asset from a
blockchain without smart contract capability (e.g., Bitcoin) to a blockchain with smart contracts
(e.g., Ethereum) also tend to rely on a similar mechanism. In non-custodial constructions such as
Zamyatin et al. [2019] and Synthetix [2020], vault operators are required to lock ETH collateral
in addition to the deliverable BTC asset. They bear a leveraged ETH/BTC exchange rate risk
and face similar deleveraging risk. In particular, to reduce exposure, they need to repurchase the
version of the cross-chain asset on Ethereum.

Several generalizations of analytical results are left for future research. Here we considered
collateral prices exogenous, but it would be interesting to model market impact effects of large
collateral liquidations and also enable modeling of stablecoins like Synthetix sUSD that have _en-_
_dogenous_ collateral (see Klages-Mundt et al. [2020]). One possible way to endogenize collateral
prices is via an inverse demand function. We expect that the general methods used in this paper
can be applied to partial equilibrium settings such as this. Naturally, this would necessitate conditions on the inverse demand function that ensure that the expected returns as a function of the

issuance remains concave.

We have specified the speculator’s decision-making in terms of a sequence of one-period optimization problems. Alternatively, the speculator could strategically coordinate the sequence of
decisions further into the future and develop long-term strategies. This could be formulated by
using an exit time for the speculator, when they can cash our their position by selling to someone
else at par. If this terminal time is deterministic, the problem can be formulated as a dynamic
program, in which the terminal decision results from the one-period optimization, intermediate
decisions solve a Bellman equation conditioned on the information revealed up to that point, and
random returns are independent. For instance, Biais et al. [2019] sets up a supermodular game in
a setting where agents exit at a random exponential time. in t The model could be extended to
include multiple speculators. Speculators have in reality a finite depth and moreover, they maintain positions with different leverage points and ETH expectations. This can lead to a sequential
schedule of liquidation points at a given time throughout the system, which will be reflected in a
speculator’s expected liquidation costs. A given speculator will take into account price effects from
the potential liquidations of other speculators’ positions in addition to their own, see Minca and
Wissel [2020] for leveraging-deleveraging games in the traditional banking system. Here, the speculator’s value depends on liquidation costs and on the supply limit imposed by the finite market
depth. Incorporating strategic aspects is left for future research.


26


### **7 Data availability statement**

The contribution of this paper is theoretical. Where examples have been provided to support
theoretical findings, price data is publicly available (by Kaiko - Digital Assets Data Provider and
LoanScan platform).

### **References**


Angeris, G., Kao, H.-T., Chiang, R., Noyes, C., and Chitra, T. (2020). An analysis of Uniswap
markets. _Crypto Economic Systems 2020_ .


Biais, B., Bisi`ere, C., Bouvard, M., and Casamatta, C. (2019). The Blockchain Folk Theorem.
_Review of Financial Studies_, 32(5):1662–1715.


Blocknative (2020). Evidence of mempool manipulation on black thursday: Hammerbots, mempool
compression, and spontaneous stuck transactions.


Bloomberg (20 May 2022). How $60 Billion in Terra Coins Went Up in Algorithmic Smoke. `[https:](https://www.bloomberg.com/graphics/2022-crypto-luna-terra-stablecoin-explainer/)`
`[//www.bloomberg.com/graphics/2022-crypto-luna-terra-stablecoin-explainer/](https://www.bloomberg.com/graphics/2022-crypto-luna-terra-stablecoin-explainer/)` .


Boyd, S. and Vandenberghe, L. (2009). _Convex optimization_ . Cambridge university press.


Bullmann, D., Klemm, J., and Pinna, A. (2019). In search for stability in crypto-assets: Are
stablecoins the solution? _ECB Occasional Paper_, (230).


Burkholder, D. L. (1973). Distribution function inequalities for martingales. _the Annals of Proba-_
_bility_, pages 19–42.


Cao, Y., Dai, M., Kou, S., Li, L., and Yang, C. (2021). Designing stable coins. _Available at SSRN:_
_`[https: // ssrn. com/ abstract= 3856569](https://ssrn.com/abstract=3856569)`_ .


Chitra, T. (2020). Competitive equilibria between staking and on-chain lending. _Crypto Economic_
_Systems 2020_ .


cLabs (2019). An analysis of the stability characteristics of Celo. Technical report, `[https://celo.](https://celo.org/papers/Celo_Stability_Analysis.pdf)`

`[org/papers/Celo_Stability_Analysis.pdf](https://celo.org/papers/Celo_Stability_Analysis.pdf)` .


Coindesk (17 Mar. 2020). MakerDAO adds USDC as DeFi collateral following ‘Black Thursday’ chaos. `[https://www.coindesk.com/](https://www.coindesk.com/makerdao-adds-usdc-as-defi-collateral-following-black-thursday-chaos)`
`[makerdao-adds-usdc-as-defi-collateral-following-black-thursday-chaos](https://www.coindesk.com/makerdao-adds-usdc-as-defi-collateral-following-black-thursday-chaos)` .


Compound (2019). Compound:the money market protocol. `[https://compound.finance/](https://compound.finance/documents/Compound.Whitepaper.pdf)`
`[documents/Compound.Whitepaper.pdf](https://compound.finance/documents/Compound.Whitepaper.pdf)` .


Detrio, C. (2015). Smart markets for stablecoins. Technical report, `[http://cdetr.io/](http://cdetr.io/smart-markets/)`
`[smart-markets/](http://cdetr.io/smart-markets/)` .


Diamond, D. W. and Dybvig, P. H. (1983). Bank runs, deposit insurance, and liquidity. _Journal_

_of political economy_, 91(3):401–419.


Dybvig, P. H. and Zender, J. F. (1991). Capital structure and dividend irrelevance with asymmetric
information. _The Review of Financial Studies_, 4(1):201–219.


27


Evans, A. (2019). A Ratings-Based Model for Credit Events in MakerDAO.


Gudgeon, L., Perez, D., Harz, D., Gervais, A., and Livshits, B. (2020). The Decentralized Financial
Crisis: Attacking DeFi. _arXiv preprint arXiv:2002.08099_ .


Guimaraes, B. and Morris, S. (2007). Risk and wealth in a model of self-fulfilling currency attacks.
_Journal of Monetary Economics_, 54(8):2205–2230.


Harz, D., Gudgeon, L., Gervais, A., and Knottenbelt, W. J. (2019). Balance: Dynamic Adjustment

 - f Cryptocurrency Deposits. In _Proceedings of the 2019 ACM SIGSAC Conference on Computer_
_and Communications Security (CCS ’19)_ . ACM.


Huo, L., Klages-Mundt, A., Minca, A., Munter, F., and Wind, M. (2022). Decentralized Governance

 - f Stablecoins with Closed Form Valuation. In _Mathematical Research for Blockchain Economy_
(to appear). `[https://arxiv.org/abs/2109.08939](https://arxiv.org/abs/2109.08939)` .


Kacperczyk, M. and Schnabl, P. (2013). How safe are money market funds? _The Quarterly Journal_

_of Economics_, 128(3):1073–1122.


Klages-Mundt, A. (14 Dec 2018). The state of stablecoins–update 2018. `[https://medium.com/](https://medium.com/coinmonks/the-state-of-stablecoins-update-2018-56fb82efe6de)`
`[coinmonks/the-state-of-stablecoins-update-2018-56fb82efe6de](https://medium.com/coinmonks/the-state-of-stablecoins-update-2018-56fb82efe6de)` .


Klages-Mundt, A., Harz, D., Gudgeon, L., Liu, J.-Y., and Minca, A. (2020). Stablecoins 2.0:
Economic Foundations and Risk-based Models. In _Proceedings of the 2nd ACM Conference on_
_Advances in Financial Technologies_, pages 59–79.


Klages-Mundt, A. and Minca, A. (2021). (In) Stability for the Blockchain: Deleveraging Spirals
and Stablecoin Attacks. _Cryptoeconomic Systems,_ _`[https: // arxiv. org/ abs/ 1906. 02152](https://arxiv.org/abs/1906.02152)`_ .


Lipton, A., Hardjono, T., and Pentland, A. (2018). Digital trade coin: towards a more stable digital
currency. _Royal Society open science_, 5(7):180155.


Liquity (2020). Stability pool and liquidations. `[https://docs.liquity.org/faq/](https://docs.liquity.org/faq/stability-pool-and-liquidations)`
`[stability-pool-and-liquidations](https://docs.liquity.org/faq/stability-pool-and-liquidations)` .


MakerDAO (12 Mar 2020a). Black Thursday response thread. `[https://forum.makerdao.com/t/](https://forum.makerdao.com/t/black-thursday-response-thread/1433)`
`[black-thursday-response-thread/1433](https://forum.makerdao.com/t/black-thursday-response-thread/1433)` .


MakerDAO (2017). The Dai stablecoin system whitepaper. `[https://makerdao.com/whitepaper/](https://makerdao.com/whitepaper/DaiDec17WP.pdf)`
`[DaiDec17WP.pdf](https://makerdao.com/whitepaper/DaiDec17WP.pdf)` .


MakerDAO (2019). The maker protocol: Makerdao’s multi-collateral dai (mcd) system. `[https:](https://docs.makerdao.com/)`
`[//docs.makerdao.com/](https://docs.makerdao.com/)` .


MakerDAO (Nov. 2020b). MIP29 - peg stability module. `[https://forum.makerdao.com/t/](https://forum.makerdao.com/t/mip29-peg-stability-module/5071)`
`[mip29-peg-stability-module/5071](https://forum.makerdao.com/t/mip29-peg-stability-module/5071)` .


Minca, A. and Wissel, J. (2020). Dynamic leveraging–deleveraging games. _Operations Research_,
68(1):93–114.


Morris, S. and Shin, H. S. (1998). Unique equilibrium in a model of self-fulfilling currency attacks.
_American Economic Review_, pages 587–597.


O’Hara, M. (1997). _Market microstructure theory_ . Wiley.


28


Parlatore, C. (2016). Fragility in money market funds: Sponsor support and regulation. _Journal_

_of Financial Economics_, 121(3):595–623.


PeckShield (Feb. 2020a). bZx Hack Full Disclosure (With Detailed Profit Analysis). `[https://](https://link.medium.com/LlXArFK7e7)`
`[link.medium.com/LlXArFK7e7](https://link.medium.com/LlXArFK7e7)` .


PeckShield (Feb. 2020b). bZx Hack II Full Disclosure (With Detailed Profit Analysis). `[https:](https://link.medium.com/9K9LrFQ7e7)`
`[//link.medium.com/9K9LrFQ7e7](https://link.medium.com/9K9LrFQ7e7)` .


Platias, N. and DiMaggio, M. (2019). Terra money: stability stress test. Technical report, `[https:](https://agora.terra.money/t/stability-stress-test/55)`
`[//agora.terra.money/t/stability-stress-test/55](https://agora.terra.money/t/stability-stress-test/55)` .


Reflexer (2020). Rai. `[https://reflexer.finance/](https://reflexer.finance/)` .


Rennison, J., Stafford, P., Smith, C., and Wigglesworth, R. (Mar. 23, 2020). ‘great liquidity crisis’
grips system as banks step back. Financial Times.


See, C.-T. and Chen, J. (2008). Inequalities on the variances of convex functions of random variables.
_Journal of inequalities in pure and applied mathematics_, 9(3):1–5.


Synthetix (16 Sep. 2019a). Addressing claims of deleted balances. `[https://blog.synthetix.io/](https://blog.synthetix.io/addressing-claims-of-deleted-balances/)`
`[addressing-claims-of-deleted-balances/](https://blog.synthetix.io/addressing-claims-of-deleted-balances/)` .


Synthetix (Jun. 2019b). Synthetix Response to Oracle Incident. `[https://blog.synthetix.io/](https://blog.synthetix.io/response-to-oracle-incident/)`
`[response-to-oracle-incident/](https://blog.synthetix.io/response-to-oracle-incident/)` .


Synthetix (Mar. 2020). tBTC: a decentralized redeemable BTC-backed ERC-20 token. `[https:](https://docs.keep.network/tbtc)`
`[//docs.keep.network/tbtc](https://docs.keep.network/tbtc)` .


Terra Research (Jul. 2019). Increasing Robustness of the Terra Oracle. `[https://agora.terra.](https://agora.terra.money/t/increasing-robustness-of-the-terra-oracle/82)`
`[money/t/increasing-robustness-of-the-terra-oracle/82](https://agora.terra.money/t/increasing-robustness-of-the-terra-oracle/82)` .


Topbottom, F. (2020). Black Thursday for MakerDAO: $8.32 million was liquidated for 0 DAI.


Werner, S. M., Perez, D., Gudgeon, L., Klages-Mundt, A., Harz, D., and Knottenbelt, W. J. (2021).
SoK: Decentralized Finance (DeFi). _arXiv preprint arXiv:2101.08778_ .


Zamyatin, A., Harz, D., Lind, J., Panayiotou, P., Gervais, A., and Knottenbelt, W. J. (2019).
XCLAIM: Trustless, Interoperable, Cryptocurrency-Backed Assets. In _Proceedings of the IEEE_
_Symposium on Security & Privacy, May 2019._, pages 1254–1271.


29


### **A Proofs**

In the proofs, we often use the following elementary result


**Lemma 2.** _For α, D, L ≥_ 0 _,_


_αD_ + _L ≤_ ~~�~~ _α_ [2] _D_ [2] + 4 _αDL_ + _L_ [2] _≤_ min 2 _αD_ + _L, αD_ + _L_ + _√_

                    


2 _αDL_ _._

  


_Proof._ Define _ε_ := _√_



_α_ [2] _D_ [2] + 4 _αDL_ + _L_ [2] . We have _ε_ _≤_ 2 _αD_ + _L_ as long as _αD ≥_ _L_ ( _√_



_Proof._ Define _ε_ := _√α_ [2] _D_ [2] + 4 _αDL_ + _L_ [2] . We have _ε_ _≤_ 2 _αD_ + _L_ as long as _αD ≥_ _L_ ( _√_ 3 _−_ 2), which

is true since _α, D, L ≥_ 0. Next, notice that _ε_ = - ( _αD_ + _L_ ) [2] + 2 _αDL_ . Thus _ε > αD_ + _L_ since



is true since _α, D, L ≥_ 0. Next, notice that _ε_ = - ( _αD_ + _L_ ) [2] + 2 _αDL_ . Thus _ε > αD_ + _L_ since

2 _αDL ≥_ 0. Lastly, by concavity, _ε ≤_ _αD_ + _L_ + _√_ 2 _αDL_ .



2 _αDL_ .



**Proposition 1**


_Proof._ Consider _Xt_ +1 = _XtRt_ +1. For notational simplicity, drop subscripts as follows: _N_ ¯ _t �→_ _N_,
_Xt �→_ _X_, _Lt �→L_, ∆= _Lt −Lt−_ 1, _c_ ( _Lt_ ) _�→_ _c_, _b_ ( _Lt_ ) _�→_ _b_, _gt �→_ _g_, _Rt_ +1 _�→_ _R_ . Define _ψ_ := E[ _Yt_ +1 _|Ft_ ].
Then




_[· D]_ _∞_

E[ _R|Ft_ ] +
_L_ 


_c/X_



_ψ_ ( _L_ ) = [∆] _[· D]_



_∞_ _b/X_

( _NXz −L_ ) _g_ ( _z_ ) _dz_ +
_c/X_ - _c/X_



_αDL_
3 _L −_ _g_ ( _z_ ) _dz._

- 2 _NXz −L_ _[−]_ [2] _[NXz]_ 


_αDL_
Recall that the integrand factor 3 _L −_ 2 _NXz−L_ _[−]_ [2] _[NXz]_ evaluated at _Xz_ = _c_ is _L −_ _Nc_ (the

             -             liquidation zeros out the speculator’s collateral position), and evaluated at _Xz_ = _b_ is 0 (on the
threshold of liquidation).
We obtain



_g_ ( _z_ ) _dz_
_c_

_X_



_∂ψ_ _[DL][t][−]_ [1]
_∂L_ [=] _L_ [2]




_[t][−]_ [1]

E[ _R|Ft_ ] _−_ _NX_ _[c]_
_L_ [2] - _X_




_[c]_ _g_ _c_

_X_ _[−L]_ - - _X_




- _∂∂c_



_X_



_∂c_ 1 _∞_

_∂L_ _X_ _[−]_ - _c_



_αDNXz_
3 _−_

- 2( _NXz −L_ ) [2]



_g_ ( _z_ ) _dz_




_c_

_X_




_−_ _L −_ _NX_ _[c]_

 - _X_



_c_
_g_

- - _X_




- _∂∂cL_



_b_

_∂c_ 1 _X_

_∂L_ _X_ [+] - _c_



_∞_

_[t][−]_ [1]

E[ _R|Ft_ ] _−_
_L_ [2] - _c_



_c_

_X_



= _[DL][t][−]_ [1]



_b_

_∞_ _X_

_g_ ( _z_ ) _dz_ +
_c_ - _c_
_X_ _X_



_αDNXz_
3 _−_ _g_ ( _z_ ) _dz_

- 2( _NXz −L_ ) [2] 


_∂_ [2] _ψ_

[=] _[ −]_ [2] _[DL][t][−]_ [1]
_∂L_ [2] _L_ [3]




_[t][−]_ [1] _b_

E[ _R|Ft_ ] + _g_
_L_ [3] - _X_



_αDNb_
3 _−_

- 2( _Nb −L_ ) [2]







_X_



_∂b_ 1

- _∂L_ _X_



_αDNc_

- 2 _−_ 2( _Nc −L_ ) [2]



_b_

_X_

_−_

- - _Xc_



_b_

_X_

_−_

- - _c_



_αDNXz_

_[g]_ [(] _[z]_ [)] _[dz.]_
( _NXz −L_ ) [3]



_c_

_−_ _g_

  - _X_




- _∂L∂c_ _X_ 1



Notice that _[∂b]_




_[∂b]_ _[∂c]_

_∂L_ _[>]_ [ 0,] _∂L_



_∂L_ _[>]_ [ 0,] _[ g][ ≥]_ [0, and]



_αDNb_ _αDβL_
3 _−_ [= 3] _[ −]_ [= 3] _[ −]_ [3] _[α][D]_ _<_ 0
2( _Nb −L_ ) [2] 2( _L_ ( _β −_ 1)) [2] _L_



by assumption that liquidation repurchase price always _≥_ 1. Additionally, the remaining integral
is always positive as the integrand is positive between the limits and _g ≥_ 0. Finally, E[ _R|Ft_ ] _≥_ 0
since ( _Xt_ ) is a submartingale. Thus under the given conditions, _∂_ _[∂]_ _L_ [2] _[ψ]_ [2] _[≤]_ [0 as all terms are] _[ ≤]_ [0.]

Further supposing that either E[ _R|Ft_ ] _>_ 0 or P  - _c_ ( _L_ ) _< XR < b_ ( _L_ )� =  - _c/Xb/X_ _[g]_ [(] _[z]_ [)] _[dz >]_ [ 0, then]

_∂_ [2] _ψ_
_∂L_ [2] _[<]_ [ 0.]


30


Notice that the [1]




[1] [3]

2 [in the bound is related to the choice] _[ β]_ [ =] 2



2 [.]



**Proposition 2**


_Proof._ Easily verifiable by substitution, noting that factors of _γ_ cancel in the integral limits.


**Proposition 3**


_Proof._ The speculator can at most buy back using all its ETH. At time _t_, this amount is the solution
∆ _t_ to the following
∆ _tD_
+ _Nt−_ 1 _Xt −_ _Lt−_ 1 _−_ ∆ _t_ = 0 _,_
_Lt−_ 1 + ∆ _t_


supposing there is no liquidation at time _t_ . It is straightforward to verify the solution, giving the
lower bound:



∆ _t ≥_ [1] _−_

2   -   


_D_ [2] _−_ 4 _DLt−_ 1 + 2 _DNt−_ 1 _Xt_ + _Nt_ [2] _−_ 1 _[X]_ _t_ [2] [+] _[ D −]_ [2] _[L][t][−]_ [1][ +] _[ N][t][−]_ [1] _[X][t]_ _._

                      


Note that if the speculator is not solvable at time _t_, then there is no real solution.


**Proposition 4**


_Proof._ ¯ As above, consider _Xt_ +1 = _XtRt_ +1. For notational simplicity, we drop subscripts as follows:
_Nt �→_ _N_, _Xt �→_ _X_, _Lt �→L_, ∆= _Lt −Lt−_ 1, _c_ ( _Lt_ ) _�→_ _c_, _b_ ( _Lt_ ) _�→_ _b_, _gt �→_ _g_, _Rt_ +1 _�→_ _R_,
P( _At|Ft_ ) _�→_ P( _A_ ), P( _Bt|Ft_ ) _�→_ P( _B_ ).
Suppose the first condition is true. We have



_g_ ( _z_ ) _dz_




_∞_

_[t][−]_ [1] E[ _R|Ft_ ] _−_

_L_ [2] - _c_



_c_

_X_



_∂ψ_
_∂L_ [=] _[ DL]_ _L_ _[t]_ [2] _[−]_ [1]



_b_

_∞_ _X_

_g_ ( _z_ ) _dz_ +
_c_ - _c_
_X_ _X_



_αDNXz_
3 _−_

- 2( _NXz −L_ ) [2]



_≤_ _[DL][t][−]_ [1] E[ _R|Ft_ ] _−_ P( _A ∪_ _B_ )

_L_ [2]



_≤_ _[DL][t][−]_ [1] E[ _R|Ft_ ] _−_ _κ_ _[−]_ [1] _._

_L_ [2]



Notice this is monotonic decreasing in _L_ - ver the domain, so the critical point will be a bound for
the optimal value of _L_ _[∗]_ . Setting equal to 0, we have


_L_ _[∗]_ _≤_ ~~�~~ _κDLt−_ 1 E[ _R|Ft_ ] _._


Now suppose the second condition is true instead. We have



_c_

_X_



_∞_

_[t][−]_ [1]

E[ _R|Ft_ ] _−_
_L_ [2] - _b_



_b_ _b_

_X_ _X_

_g_ ( _z_ ) _dz −_
_c_ - _c_
_X_ _X_



_∂ψ_ _[DL][t][−]_ [1]
_∂L_ [=] _L_ [2]



_b_

_∞_ _X_

_g_ ( _z_ ) _dz_ + 2
_b_ - _c_
_X_ _X_



_αDNXz_

_[g]_ [(] _[z]_ [)] _[dz]_
2( _NXz −L_ ) [2]



_≤_ _[DL][t][−]_ [1] E[ _R|Ft_ ] _−_ P( _A_ ) _−_ 2 P( _B_ )

_L_ [2]  -  


_≤_ _[DL][t][−]_ [1] E[ _R|Ft_ ] _−_ _κ_ _[−]_ [1] _._

_L_ [2]



which delivers the desired result as above.



31


**Proposition 5**


_Proof._ By assuming _TZ_ 0 _> τ_, we have _Z_ 0 _≥_ _Zt∧τ_ . Applying Proposition 4 to _Zt_ = _LDt_ [provides]

_Zt∧τ ≥_ - _κLt∧Dτ_ _−_ 1 _r_ [. Notice that the upper bound on] _[ L][t]_ [ and the lower bound on] _[ Z][t]_ [ can be written]

respectively as increasing and decreasing sequences in _t_ starting from initial state as follows:



2 _[t]_ _−_ 1
_Lt_ = ( _κDr_ ) 2 ~~_[t]_~~



1
2 ~~_[t]_~~
0 _[.]_



2 ~~_[t]_~~ _L_



_D_
_Z_ ~~_t_~~ = _[t]_



2 _[t]_ _−_ 1
( _κDr_ ) 2 ~~_[t]_~~



1
2 ~~_[t]_~~
0



_._



2 ~~_[t]_~~ _L_



These have limits _L∞_ = _κDr_ and _Z_ ~~_∞_~~ = _κr_ 1 [that also bound] _[ L][t]_ [ and] _[ Z][t]_ [ respectively.]


**Proposition 6**



_Proof._ For _t −_ 1 _< τ_,
_D_ _D_
E[ _Lt|Ft−_ 1] _[≤]_ [E]                - _L_



_D_ _D_ _D_

_|Ft−_ 1 _≤_

E[ _Lt|Ft−_ 1] _[≤]_ [E]                - _Lt_                - _Lt−_ 1


by Jensen’s inequality and the condition for _τ > t −_ 1. Thus we have



_|Ft−_ 1
_Lt_



E[ _Lt∧τ_ _|Ft−_ 1] _≥Lt∧τ_ _−_ 1


and ( _Lt∧τ_ ) is a submartingale. ( _Zt∧τ_ ) is a supermartingale by condition of _τ_ .
Applying Proposition 5, _Lt∧τ_ is bounded above and _Zt∧τ_ is bounded below. Thus they converge
almost surely by Doob’s martingale convergence theorem.


**Proposition 7**


_Proof._ The first inequality follows from Proposition 5 and supermartingale properties.
Since _Zt∧τ_ is supermartingale, we have _Zt−_ 1 _≥_ E[ _Zt|Ft−_ 1]. Assume (E[ _Rt_ +1 _|Ft_ ]) is nondecreasing for _t < τ_ . Then subject to the stopping time _τ_,



E[ _Zt|Ft−_ 1] _≥_ E




- ~~�~~



_D_
_κLt−_ 1 E[ _Rt_ +1 _|Ft_ ] _[|F][t][−]_ [1]

         


(Apply Proposition 4)



_≥_


=


_≥_




~~�~~

~~�~~ _D_

- (Jensen’s inequality)

_κLt−_ 1 E E[ _Rt_ +1 _|Ft_ ] _|Ft−_ 1

- ~~�~~ ~~�~~




~~�~~

~~�~~



_D_
(Tower property)
_κLt−_ 1 E[ _Rt_ +1 _|Ft−_ 1]


_D_

_κLt−_ 1 E[ _Rt|Ft−_ 1]



since E[ _Rt_ +1 _|Ft_ ] _≥_ E[ _Rt|Ft−_ 1].



32


**Lemma 1**


_Proof._ For _t −_ 1 _< τ ∧_ _Tm_,


E [ _|m −_ _Zt||Ft−_ 1] _≥|_ E[ _m −_ _Zt|Ft−_ 1] _|_


_≥|m −_ _Zt−_ 1 _|,_


by Jensen’s inequality and the condition for _t −_ 1 _< Tm_ that _m −_ _Zt−_ 1 _≥_ 0. Thus - _Zt_ _[′]_ _∧τ_ _∧Tm_ - is a
non-negative submartingale.


**Proposition 8**

_Proof._ Note for _t < τ ∧_ _Tm_, have _Zt_ _[∗]_ _[≤]_ _[m]_ [, and so] _[ Z]_ _τ_ _[′∗]_ _∧Tm−_ 1 _[≤]_ _[m][ −]_ _κr_ [1] [. Thus] _[ Z]_ _τ_ _[′∗]_ _∧Tm_ _[≤]_ [max] - _m −_


1
_κr_ _[, Z]_ _τ_ _[′]_ _∧Tm_ - .
Consider time _t_ = _τ ∧_ _Tm_ and note that optional stopping applies since _Z_ is bounded. Denote
_W_ := _m −_ _Zt_, _E_ := E[ _−W_ _|Zt > m_ ], and _p_ := P( _Zt ≤_ _m_ ). From optional stopping, we recall that
_m ≥_ E[ _Zt_ ] _≥_ _κr_ 1 [, and so 0] _[ ≤]_ [E][[] _[W]_ []] _[ ≤]_ _[m][ −]_ _κr_ [1] [. Then]


E[ _W_ ] = E[ _W_ 1 _Zt≤m_ ] _−_ E[ _−W_ 1 _Zt>m_ ]



_≤_ _p_ _m −_ [1]

  - _κr_




_−_ (1 _−_ _p_ ) _E._




Combining with 0 _≤_ E[ _W_ ], we have 0 _≤_ _p_ ( _m −_ _κr_ [1] [)] _[ −]_ [(1] _[ −]_ _[p]_ [)] _[E]_ [, which gives]


_E_
_p ≥_
_m −_ _κr_ [1] [+] _[ E]_ _[.]_


_E_
Then noting that (1 _−_ _p_ ) _E ≤_ _E_ (1 _−_ _m−_ _κr_ [1] [+] _[E]_ [),] _[ p][ ≤]_ [1, and][ E][[] _[Z]_ _t_ _[′]_ [] =][ E][[] _[W]_ [ 1] _[Z]_ _t_ _[≤][m]_ [] +][ E][[] _[−][W]_ [ 1] _[Z]_ _t_ _[>m]_ [],]

we have
E[ _Zt_ _[′∗]_ []] _[ ≤]_ _[p]_ [ E][[] _[Z]_ _t_ _[′∗]_ _−_ 1 [] + (1] _[ −]_ _[p]_ [)] _[E]_



_≤_ _m −_ _κr_ [1] [+] _[ E]_







_E_
1 _−_
_m −_ [1]



_κr_ [+] _[ E]_








[1] _[E]_ [(] _[m][ −]_ [1]

_κr_ [+] _m_ [1]



= _m −_ [1]




_[E]_ [(] _[m][ −]_ _κr_ [)]

_m −_ [1] [+] _[ E]_




[1] _[.]_

_κr_ [+] _[ E]_



Notice further that given either of the following conditions


1 1

  - _κr_ _[> m]_ [ and] _[ E >]_ _κr_ _[−]_ _[m]_


1

  - _κr_ [=] _[ m]_ [ and] _[ E >]_ [ 0]


1

  - _κr_ _[< m]_ [ ad] _[ E][ ≥]_ [0,]


then



0 _≤_ (1 _−_ _p_ ) _E ≤_ _[E]_ [(] _[m][ −]_ [1]



_κr_ _[.]_




_[E]_ [(] _[m][ −]_ _κr_ [)]

_m −_ [1] [+] _[ E]_




_[ −]_

_κr_ [)]

[1] _[≤]_ _[m][ −]_ _κr_ [1]

_κr_ [+] _[ E]_



Thus, recalling we used _t_ = _τ ∧_ _Tm_, we get the following result



E[ _Zτ_ _[′∗]_ _∧Tm_ []] _[ ≤]_ [2] _m −_ [1] _._

    - _κr_     

33


**Theorem 1**


_Proof._ Given Lemma 1 and Proposition 8 and noting E[ _Zτ_ _[′]_ _∧Tm_ []] _[ ≤]_ [E][[] _[Z]_ _τ_ _[′∗]_ _∧Tm_ [], apply Doob’s maximal]
inequality.


**Theorem 2**


_Proof._ Apply Theorem 3.1 in Burkholder [1973], noting that sup _n_ E[ _Zn_ _[′]_ _∧τ_ _∧Tm_ []] _[ ≤]_ [E][[] _[Z]_ _τ_ _[′∗]_ _∧Tm_ [] by]
Jensen’s inequality.


**Theorem 3**


_Proof._ For _S_ 1 _≤_ _t < S_ 2, we have



_D_
E _|Ft−_ 1

 - _Lt_



_D_
_≥_

- E[ _Lt|Ft−_ 1]


_D_
_≥_
_Lt−_ 1



by Jensen’s inequality and the _S_ 1 condition E[ _Lt|Ft−_ 1] _≤Lt−_ 1. Thus ( _ZS_ 1 _∨t∧S_ 2) is a submartingale
(though note that it can be a submartingale for more general stopping times than this).
_L_ started at _S_ 1 and stopped _S_ 2 is a supermartingale (by definition).


**Theorem 4**


_Proof._ ¯ As above, consider _Xt_ +1 = _XtRt_ +1. For notational simplicity, we drop subscripts as follows:
_Nt �→_ _N_, _Xt−_ 1 _�→_ _X_ (notice this is different from previous usage), _Lt �→L_, ∆= _Lt −Lt−_ 1,
_c_ ( _Lt_ ) _�→_ _c_, _b_ ( _Lt_ ) _�→_ _b_, and _gt �→_ _g_ .
Let _ρ_ be (deterministic) variable representing the outcome of _Rt_, such that now we have the

- utcome _Xt_ = _Xρ_ . And define _h_ ( _ρ_ ) = arg max _L ψ_ ( _ρ, L_ ) = E[ _Yt_ +1 _|Ft_ ]. By first order condition,
_∂_
_∂L_ _[ψ]_ [(] _[ρ, h]_ [(] _[ρ]_ [)) = 0. The assumptions on] _[ ψ]_ [ provide unique maximum and fulfill conditions of the]
implicit function theorem, which gives us _[∂h]_

_∂ρ_ [(] _[ρ]_ [) exists and]



_∂h_
_∂ρ_ [(] _[ρ]_ [) =] _[ −]_



_∂_ [2]
_∂ρ∂L_ _[ψ]_ [(] _[ρ, h]_ [(] _[ρ]_ [))]

_∂L∂_ [2][2] _[ψ]_ [(] _[ρ, h]_ [(] _[ρ]_ [))] _._



Calculating derivatives using the Leibniz integral rule (recalling _c, b_ are functions of _L_ ),



_∂_ [2] _ψ_ _c_
_∂ρ∂L_ [=] _[ g]_ - _Xρ_



_c_

- _Xρ_ [2]



_αDNc_

- 4 _−_ 2( _Nc −L_ ) [2]



_b_

_−_ _g_

- - _Xρ_



_b_

- _Xρ_ [2]



_αDNb_
3 _−_

- 2( _Nb −L_ ) [2]







_b_
_Xρ_
+

 - _c_

_Xρ_



_αDNXz_ ( _NXρz_ + _L_ )

_g_ ( _z_ ) _dz._
2( _NXρz −L_ ) [3]


34


_∂_ [2] _ψ_

[=] _[ −]_ [2] _[DL][t][−]_ [1][ E][[] _[R][t]_ [+1][]]
_∂L_ [2] _L_ [3]



_Xρ_




[1][ E][[] _[R][t]_ [+1][]] _b_

+ _g_
_L_ [3] 


_∂b_ 1

- _∂L_ _Xρ_



_∂b_

- _∂L_



_αDNb_
3 _−_

- 2( _Nb −L_ ) [2]







_c_

_−_ _g_

  - _Xρ_



_∂c_ 1

- _∂L_ _Xρ_



_b_

_αDNc_ _Xρ_
2 _−_ _−_

- 2( _Nc −L_ ) [2] - - _c_

_Xρ_



_αDNXρz_

_[g]_ [(] _[z]_ [)] _[dz.]_
( _NXρz −L_ ) [3]



Notice that (and continuing with _β_ = 3 _/_ 2)


_αDNb_ _αDβL_
3 _−_ [= 3] _[ −]_ [= 3] _[ −]_ [3] _[α][D]_ _<_ 0 _,_
2( _Nb −L_ ) [2] 2( _L_ ( _β −_ 1)) [2] _L_


by assumption that liquidation repurchase price always _≥_ 1. And



_αDNc_

_[≤]_
2( _Nc −L_ ) [2]



1
2 _[α][D]_ [(][2] _[α][D]_ [ +] _[ L][ −]_ _[α][D]_ [ +] _[ L]_ [)]

_−_ 2 _αD_ (2 _αD_ + _L_ ) + 2 _L_ ( _αD_ + _L_ ) + 2 _α_ [2] _D_ [2] + 2 _αDL_ + 2 _L_ [2]



_αD_ ( _αD_ + 2 _L_ )
=
4( _αD_ + _L_ )(2 _L −_ _αD_ )


_αD_ _αD_

=
12( _αD_ + _L_ ) [+] 3(2 _L −_ _αD_ )


_αD_

_≤_ [1]

12 [+] 3(2 _L −_ _αD_ ) _[.]_


This is _≤_ 2 when _L ≥_ [27] 46 _[α][D]_ [. Thus under this condition]


_αDNc_ _αDNc_
4 _−_ 2( _Nc −L_ ) [2] _[>]_ [ 2] _[ −]_ 2( _Nc −L_ ) [2] _[≥]_ [0] _[.]_


Note that all terms of _∂ρ∂L∂_ [2] _ψ_ [are non-negative and all terms of] _[∂]_ _∂L_ [2] _[ψ]_ [2] [are non-positive. Given] _[ ρ][ ≥]_



_b/X_, we have _g_ - _Xρc_ - and _g_ - _Xρb_ - are increasing in 1 _/ρ_ . Note also that _∂L_ _[∂b]_




_[∂c]_ [E][[] _[R][t]_ [+][1][]]

_∂L_ [, and][ 2] _[DL][t][−]_ _L_ [1] [3]




_[∂b]_ _[∂c]_

_∂L_ [,] _∂L_



_Xρ_ _Xρ_ _∂L_ [,] _∂L_ _L_ [3]

are constant in _ρ_ . Lastly, the numerator and denominator integrals can be rewritten respectively

as
1 _b_ _αDNz_ ( _Nz_ + _L_ ) _z_ _b_ _αDNz_ _z_

_g_ _dz_ and _[g]_ _dz_

_ρ_        - _c_ 2( _Nz −L_ ) [3]        - _Xρ_        -        - _c_ ( _Nz −L_ ) [3]        - _Xρ_        
and _[α][D]_ 2( _[Nz]_ _Nz_ [(] _−L_ _[Nz]_ [+] ) [3] _[L]_ [)] _≥_ ( _NzαD−LNz_ ) [3] [given] _[ Nz]_ [ +] _[ L ≥]_ _[Nc]_ [ +] _[ L][ >]_ [ 2, for which] _[ L][ >]_ [ 8 is sufficient. And]

so the terms in the numerator of _|h_ _[′]_ ( _ρ_ ) _|_ are growing by a factor 1 _/ρ_ faster than the terms in the
denominator as _ρ_ decreases, proving (2).
Next, note that under the condition 0 _< ρ <_ 1,




- _c_ _b_



_Nz_ ( _Nz_ + _L_ ) _z_

_g_
2( _Nz −L_ ) [3] 


_Xρ_



_αDNz_ _z_

_[g]_
( _Nz −L_ ) [3] 


_dz_




_αDNz_ ( _Nz_ + _L_ )



_b_

_dz_ and

- - _c_



_c_



_c_



_Xρ_



and _[α][D][Nz]_ [(] _[Nz]_ [+] _[L]_ [)]



_b_ _βL_ _[db]_

[=] [=]
_Xρ_ [2] _NXρ_ [2] _dL_




_[db]_ 1

_dL_ _Xρ_




_[db]_ _L_

_[≥]_ _[db]_
_dL_ _Xρ_ [2] _dL_



_c_

_[≥]_ _[dc]_
_Xρ_ [2] _dL_




_[dc]_ 1 _[≥]_ _[dc]_

_dL_ _Xρ_ [2] _dL_




_[dc]_ 1

_dL_ _Xρ_ _[.]_



The last relation uses the fact that _[dc]_



_dL_ _[dc]_ _[≤]_ 2(2 _ααDD_ ++ _LL_ ) [+ 1] _[ <]_ [ 2, and so] _[ c >]_ _dL_ _[dc]_



_dL_ [under the problem setup.]



Next note that for _ρ ≤_ _[L]_ 8 [and] _[ c][ ≤]_ _[Xρz][ ≤]_ _[b]_ [, we have]



_αDNXz_ ( _NXρz_ + _L_ ) _αDNXρz_

2( _NXρz −L_ ) [3] _≥_ ( _NXρz −L_ ) [3] _[.]_


35


This is because the expression (1) simplifies to _NXρz_ + _L ≥_ 2 _ρ_, (2) to be true over the whole range

- f _z_, we need _Nc_ + _L ≥_ 2 _ρ_, and (3) _ρ ≤_ _[L]_ 8 [is sufficient for this. Thus]



_b_
_Xρ_

- _c_

_Xρ_



_c_
_Xρ_



_b_

_NXz_ ( _NXρz_ + _L_ ) _Xρ_

_g_ ( _z_ ) _dz ≥_
2( _NXρz −L_ ) [3] - _c_



_αDNXρz_

_[g]_ [(] _[z]_ [)] _[dz]_
( _NXρz −L_ ) [3]



_αDNXz_ ( _NXρz_ + _L_ )



under these conditions.
Then note that all terms in the numerator of _h_ _[′]_ ( _ρ_ ) are greater than and grow faster in 1 _/ρ_ than
the comparable terms in the denominator. This leaves the first term in the numerator, which is
constant in _ρ_ . To get (3), then note that _ε_ can be chosen such that for _ρ_ = _ε_, the numerator and
denominator are equal.
We can derive the results for _∂n_ _[∂h]_ [in essentially the same way.] Alter the above dropping of

subscripts with _Xt �→_ _X_, let _n_ be a variable representing the realization of _N_ [¯] _t_, and consider _h_ as a
function of _n_ . Note the following relevant derivatives.



_∂b_
_∂n_ [=] _[ −]_ _[β]_ _n_ _[L]_ [2]




_[β][L]_

[=] _[ −]_ _[b]_
_n_ [2] _n_



_n_



_∂c_
_∂n_ [=] _[ −]_ 2 _n_ [1] [2]




- ~~�~~



_α_ [2] _D_ [2] + 4 _αDL_ + _L_ [2] _−_ _αD_ + _L_ = _−_ _[c]_

           - _n_



_n_



_∂n∂L∂_ [2] _ψ_ [=] _[ g]_ - _Xc_



_b_ _b_

_−_ _g_

- - _X_ - _n_



_b_

_−_ _g_

- - _X_



_b_

- _n_



_αDnb_
3 _−_

- 2( _nb −L_ ) [2]








- _nc_



_αDnc_
2 _−_

- 2( _nc −L_ ) [2]



_b_

_X_
+

 - _c_

_X_



_αDnXz_ ( _nXz_ + _L_ )

_g_ ( _z_ ) _dz._
2( _nXz −L_ ) [3]



And translating the following to the new notation



_∂_ [2] _ψ_

[=] _[ −]_ [2] _[DL][t][−]_ [1][ E][[] _[R][t]_ [+1][]]
_∂L_ [2] _L_ [3]




[1][ E][[] _[R][t]_ [+1][]] _b_

+ _g_
_L_ [3] - _X_



_αDnb_
3 _−_

- 2( _nb −L_ ) [2]







_X_



_∂b_ 1

- _∂L_ _X_



_b_

_X_

_−_

- - _Xc_



_αDnc_
2 _−_

- 2( _nc −L_ ) [2]



_αDnXz_

_[g]_ [(] _[z]_ [)] _[dz.]_
( _nXz −L_ ) [3]



_c_

_−_ _g_

  - _X_




- _∂L∂c_ _X_ 1




- _∂L∂c_



And by applying implicit function theorem, we get



_∂h_
_∂n_ [(] _[n]_ [) =] _[ −]_



_∂_ [2]
_∂n∂L_ _[ψ]_ [(] _[n, h]_ [(] _[n]_ [))]

_∂L∂_ [2][2] _[ψ]_ [(] _[n, h]_ [(] _[n]_ [))] _._



From here we can proceed with the same analysis using factors of [1]



_n_ [1] [instead of] [1]



_ρ_ [.]



**Theorem 5**


_Proof._ For notational simplicity, drop subscripts _Xt �→_ _X_, _N_ [¯] _t−_ 1 _�→_ _N_, _Lt−_ 1 _�→L_ . And consider _x_
a realization of _X_ as variable in _h_ . Define the function _f_ ( _X, n_ ) = _h_ ( _X,n_ 1 ) [where] _[ n]_ [ represents the]
realization of _N_ . With probability 1, the following are true:


  - _h_ is concave in _x_ and _n_ because _h_ _[′]_ is decreasing, as shown in the previous result.


36


- _f_ is differentiable (wrt _n_ and _x_ ) over domain using chain rule and implicit function theorem.


- _f_ is convex: it’s the composition of 1 _/x_ and _h_, and since 1 _/x_ is convex and non-increasing
and _h_ is concave, so is _f_ (see Boyd and Vandenberghe [2009] 3.2.4).


- _f_ is (strictly) decreasing (in _n_ and _x_ ) since _h_ is increasing.


- By assumption, we’ve restricted _NX_ . The derivative of _f_ at the minimum value exists and
is bounded.


- _f_ is non-negative since _h_ is non-negative.


- _∂f_
_∂n_ [is (strictly) increasing in] _[ n]_ [. We have]


1
_f_ _[′]_ ( _x, n_ ) = _−_ _h_ ( _x, n_ ) [2] _[h][′]_ [(] _[x, n]_ [)] _[,]_



where _h_ _[′]_ ( _x, n_ ) is derived in the previous proof using the implicit function theorem. _h_ is
increasing in _n_ and _h_ _[′]_ is non-negative and decreasing in _n_ . Thus _h_ _[h]_ [2] _[′]_ [is decreasing in] _[ n]_ [, and]

so _−_ _h_ _[h]_ [2] _[′]_ [is increasing.]



_∂h_

- _∂n_ [is increasing in] _[ x]_ [. This can be seen using the formulation at the end of the proof for]
the previous result as terms in _[∂]_ _∂L_ [2] _[ψ]_ [2] [grow slower in] _[ x]_ [ (in magnitude) than terms in] _∂n∂L∂_ [2] _ψ_ [. In]



particular, the first term of _[∂]_ _∂L_ [2] _[ψ]_ [2] [is decreasing in magnitude since] _[ L]_ [ is increasing in] _[ x]_ [. And the]



integral in _∂n∂L∂_ [2] _ψ_ [increases faster in] _[ x]_ [ than the integral in] _[ ∂]_ _∂L_ [2] _[ψ]_ [2] [, as can be seen by comparing]



_∂_ [2] _ψ_
the integrand numerators (a factor of _x_ [2] in _∂n∂L_ [vs. a factor of] _[ x]_ [ in] _[ ∂]_ _∂L_ [2] _[ψ]_ [2] [).]




- _∂n∂f_ [is (strictly) increasing in] _[ x]_ [ This is because] _[ h]_ [ is increasing in] _[ x]_ [ and] _∂n_ _[∂h]_ [is non-negative and]

increasing in _x_ (previous bullet).



Note additionally that, from the system setup assumptions, all of the functions are appropriately
bounded.
Thus we can apply Theorem 3.1 in See and Chen [2008] to get


Var _f_ ( _X, N_ _[s]_ ) _|Ft−_ 1 _<_ Var _f_ ( _X, N_ _[u]_ ) _|Ft−_ 1 _._

           -            -            -            

Note that the variances exist because _h_ = _Lt_ is bounded, as shown in previous results. The
variances of _Zt_ _[s]_ [and] _[ Z]_ _t_ _[u]_ [are then obtained by multiplying the above inequality by] _[ D]_ [2][.]


37


