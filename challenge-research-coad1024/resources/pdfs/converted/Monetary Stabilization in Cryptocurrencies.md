# Monetary Stabilization in Cryptocurrencies—Design Approaches and Open Questions

Ingolf G.A. Pernice _[∗†]_ Sebastian Henningsen _[∗†]_ Roman Proskalovich _[∗†‡]_

Martin Florian _[∗†]_ Hermann Elendner Bj¨orn Scheuermann _[∗†]_


_∗_ Weizenbaum-Institute for the Networked Society

_†_ Humboldt-Universit¨at zu Berlin

_‡_ Belarusian State University



_**Abstract**_ **—The price volatility of cryptocurrencies is often**
**cited as a major hindrance to their wide-scale adoption. Conse-**
**quently, during the last two years, multiple so called** _**stablecoins**_
**have surfaced—cryptocurrencies focused on maintaining stable**
**exchange rates. In this paper, we systematically explore and**
**analyze the stablecoin landscape. Based on a survey of 24**
**specific stablecoin projects, we go beyond individual coins for**

**nomics, fostering the transfer of expertise. For example, we**
**find that 38% of the reviewed projects use a combination of**
**exchange rate targeting and specific stabilization techniques that**
**can render them vulnerable to speculative economic attacks—an**
**avoidable design flaw.**


I. INTRODUCTION


Although cryptocurrencies like Bitcoin have gained a lot

- f attention over the last years, they have not been adopted
as standard means of payment. The large fluctuations in coin
prices are often cited as one of the main reasons for everyday
users’ reluctance [1]–[3]. An increasing number of cryptocurrencies consequently devote themselves to maintaining a stable
price. These so-called “stablecoins” promise the best of both
worlds: a (permissionless) cryptocurrency such as Bitcoin
combined with the price stability of traditional fiat currencies
such as the US Dollar.

What is the current state of this development? What has
been done, and what can be done to ensure stability? In this
paper, we systematically explore and analyze the stablecoin
landscape. We go beyond individual projects and instead provide an abstract overview of concepts merged with approaches
from traditional monetary policy.
We surveyed white papers, websites and, when available,
price data of 24 stablecoin projects. While the short-lived
nature of most cryptocurrencies quickly makes any survey of
existing coins obsolete, the abstract perspective allows us to
reason about fundamental properties, risks and limitations of
stability techniques in practice. We used the union between



generalized design features and monetary theory for developing a comprehensive taxonomy on stabilization approaches for
cryptocurrencies. Our taxonomy tackles three broad questions
that are reflected in the structure of this paper:

1) Which types of practical techniques are used to achieve
stability? (Sec. IV)
2) In what way can the value of a cryptocurrency be linked
to that of an external currency (e.g., the US Dollar
(USD), the Euro (EUR))? (Sec. VI)
3) What is the stabilization target (e.g., exchange rate to
USD, inflation, etc.)? (Sec. VII)
We use our taxonomy to highlight the current state of development from different dimensions and show blank spots. As our
taxonomy bridges computer science and economics it allows
for transfer of expertise. This not only leads to the detection

- f risks but also reveals avenues for future research.
On a more detailed level, we find that almost 38 % of surveyed coins promote a problematic combination of exchange
rate targeting and techniques for reducing the coin supply
(using either limited reserves or a potentially unlimited supply

- f self-issued tokens). While more research is encouraged,
there is strong indication that this might render them vulnerable to speculative attacks, i.e., scenarios in which investors
deliberately apply market pressure to push the price of a coin
below the stable value to make a profit.
Furthermore, existing economic literature suggests that soft
pegs are not maintainable in the long run and that more
sustainable arrangements such as _smoothing_ - f short term
variations or _hard pegs_ are preferable. When it comes to the
state of developments, simple tokenization of national currency
is the most popular technique. More sophisticated techniques
have been planned for implementation, however, many face
inherent challenges such as not allowing a permanent reduction

- f the money supply.
Although we heavily focus on the economic perspective,
we also point out technical challenges. For example, almost
all surveyed stablecoins rely on a trusted price feed and
therefore a functioning decentralized oracle. This assumption
is problematic, as existing research [4]–[6] does not solve
the decentralized oracle problem for arbitrary values and a
general solution might be impossible due to the lack of
strong identities [7] or missing incentive-compatibility. While


touching on hard technical considerations only lightly, we
argue that the proposed viewpoint provides a valuable transfer

- f knowledge between economics and computer science by

- pening up new perspectives on a predominantly technical
discussion.


II. RELATED WORK


Monetary stability in cryptocurrencies has barely been studied by the scientific community. Iwamura et al. [1], [8] propose
a combination of dynamic mining reward and automatic inflation of coins. In a different approach, Caginalp et al. argue [9]
that since cryptocurrencies have no underlying value measured
by “traditional techniques” that are used to value stocks, bonds

- r derivatives, new models are necessary. Following this idea,
Caginalp [10] uses asset flow equations to model the price of
cryptocurrencies and derive conditions under which the models
differential equations stabilize. In contrast to proposing indepth designs of novel stabilization approaches, we focus on
surveying existing projects and outlining principal features of
the design space.
Another branch of scientific research concerns itself with
_central bank digital currency (CBDC)_ [11]–[14]. We deliberately chose not to cover this topic, since the central bank, as
the central actor, remains in control of both monetary policy
and mining. Effectively, this creates another form of national
money, leaving monetary policy aspects mostly unchanged.
There already exists variety of (non-scientific) classifications and stablecoin lists, [1] as well as prominent criticism of the
concept itself. [2] Although valuable and highly informative, in

- ur analysis we take a broader, more structured and systematic
approach, by stepping away from specific projects and towards
the underlying concepts.


III. SURVEY METHODOLOGY


Exploring and understanding the stablecoin landscape is a
tedious task but a prerequisite for any further insights. Due to
the short lived nature of many coins, any such perspective is
necessarily a momentary snapshot of current projects. Therefore, we avoid reasoning about individual coins and only use
them as examples for abstract approaches instead. [3] In [15],
stablecoins are identified as cryptocurrencies “whose values
are pegged to [i.e. stabilized relative to] some other fiat money

- r asset with inherent value”. This definition of stablecoins,
however, is exceedingly narrow. In traditional economics,
stability can go beyond a long-term link to an foreign currency

- r some asset. As a consequence, we broaden the definition


1 For example:
https://github _._ [com/sdtsui/awesome-stablecoins](https://github.com/sdtsui/awesome-stablecoins)
[https://stablecoinindex](https://stablecoinindex.com/) _._ com/
https://media _._ consensys _._ [net/the-state-of-stablecoins-2018-79ccb9988e63](https://media.consensys.net/the-state-of-stablecoins-2018-79ccb9988e63)
https://cryptoinsider _._ 21mil _._ [com/stablecoins-everything-need-know/](https://cryptoinsider.21mil.com/stablecoins-everything-need-know/)
https://hackernoon _._ [com/stablecoins-designing-a-price-stable-cryptocurrency-](https://hackernoon.com/stablecoins-designing-a-price-stable-cryptocurrency-6bf24e2689e5)
[6bf24e2689e5](https://hackernoon.com/stablecoins-designing-a-price-stable-cryptocurrency-6bf24e2689e5)

2 https://prestonbyrne _._ [com/2018/03/22/stablecoins-are-doomed-to-fail/](https://prestonbyrne.com/2018/03/22/stablecoins-are-doomed-to-fail/)
3 Classification details for individual projects can be referred to in Appendix A.



TABLE I: Basic descriptive statistics for available daily USDprices of stablecoin projects until the 7th of February 2019.


Projects Obs. Mean Min. Max. Std. Dev.

NuBits (Nubits) 1587 0 _._ 819 0 _._ 030 1 _._ 264 0 _._ 332
BitShares (BitUSD) 1525 1 _._ 016 0 _._ 680 1 _._ 600 0 _._ 076
Tether (USDT) 1429 1 _._ 000 0 _._ 914 1 _._ 058 0 _._ 010
Karbo (Karbo) 904 0 _._ 299 0 _._ 005 2 _._ 066 0 _._ 418
Minex Coin (Minex Coin) 458 10 _._ 991 0 _._ 549 56 _._ 586 10 _._ 201
Maker (Dai) 404 1 _._ 002 0 _._ 939 1 _._ 053 0 _._ 010
Trusttoken (TrueUSD) 335 1 _._ 006 0 _._ 985 1 _._ 132 0 _._ 012
Digix (Digix Gold Token) 263 42 _._ 075 36 _._ 243 50 _._ 207 2 _._ 294
Sythetix (SUSD) 205 0 _._ 989 0 _._ 867 1 _._ 029 0 _._ 018
Stasis (EURS) 188 1 _._ 143 1 _._ 086 1 _._ 260 0 _._ 025
Centre (USD Coin) 118 1 _._ 013 0 _._ 983 1 _._ 037 0 _._ 008
Stronghold (USDS) 46 1 _._ 016 0 _._ 947 1 _._ 076 0 _._ 021
USC (USC) 32 0 _._ 912 0 _._ 656 1 _._ 027 0 _._ 152


to cryptocurrencies “with mechanisms to mitigate fluctations
in their purchasing power”. [4]

The scope of our analysis is limited to stablecoins that are (i)
permissionless, (ii) intended for general use as a currency, and
(iii) provide a whitepaper and website. By permissionless [16]
we mean any coin or token that runs on a permissionless Blockchain—specifically including IOU-Tokens such as
Tether [17]. We exclude central bank digital currencies, pure
utility tokens and stablecoins without a website or corresponding white paper. At the time of writing we identified
24 projects that fit these criteria. [5] Of these projects, 13 are
launched and traded on exchanges. As an overview of their
performance, Table I summarizes the mean, standard deviation,
minimum and maximum price (in USD) of each launched coin
[according to data gathered from https://coinmarketcap](https://coinmarketcap.com) _._ com. It
can be observed that the projects show divergent performance
and general statistic characteristics. This is due to the fact that
each coin chooses a different strategy to stabilize its value.
We analyze approaches to achieve price stability using
three classifications based on the monetary regimes proposed
in [18], an International Monetary Fund (IMF) study on
exchange-rate arrangements [19] and practice of stabilization
techniques by major central banks [20], [21].
In the following section, we investigate practical stabilization techniques proposed.


IV. STABILIZATION TECHNIQUES


Fundamentally, all stabilization techniques are based on the
elementary economic model of supply and demand. The _price_

_of a currency_ [6] can be modeled as the level at which its supply
and demand meet each other on the market. A change in
price is therefore due to changes in supply and/or demand—to
maintain stability, any such change has to be counteracted.


4 _Purchasing power of a currency_ describes how many units of certain
goods, services or other currencies it can buy.
5 Some projects issue stablecoins pegged to different national currencies.
In these cases we exclusively address the coin pegged to the USD.
6 The price of a currency describes how many units of other currencies
are given in exchange for it. The price can also be expressed in terms of

- ther goods or services. Thus, in presented context the term can be seen as
an equivalent to the currency’s _exchange rate_ and _purchasing power_ .


Price [USD]


_P_ 1

_P_ 2










|USD]|Col2|Col3|
|---|---|---|
|_S_<br>_S′_<br>3<br>1|_S_<br>_S′_<br>3<br>1|_S_<br>_S′_<br>3<br>1|
||2|_D′_<br>_D_|
||||



_Q_ 3 _Q_ 2 _Q_ 1 Quantity [units]


Fig. 1: Examplary supply and demand model.


Fig. 1 illustrates this concept, with price (in USD) on the
y-axis and quantity (coins in this case) on the x-axis. The
solid _S_ and _D_ curves depict the money supply and demand,
respectively. [7] Both curves intersect at ( _Q_ 1 _, P_ 1), yielding an
equilibrium quantity of _Q_ 1 and price of _P_ 1. Stablecoins aim
to maintain a constant price, say _P_ 1 in this example.
Assume the demand decreases, i.e., users would purchase
fewer coins at each price level, effectively shifting the demand
curve to the left—from _D_ to _D_ _[′]_ . The new equilibrium, the
intersection of _D_ _[′]_ and _S_ at ( _Q_ 2 _, P_ 2), has a smaller quantity
( _Q_ 2) and lower price ( _P_ 2)—which violates the aim of maintaining a constant price _P_ 1. To recover, one can (i) increase
demand (shift _D_ _[′]_ to the right), (ii) decrease supply (shift _S_
to the left) or (iii) adjust both. Especially for cryptocurrency
systems, demand is much harder to influence directly and
instantaneously, therefore, supply is often the target of choice.
This is depicted in Fig. 1, where supply is adjusted, shifting
_S_ to _S_ _[′]_ which yields an equilibrium of ( _Q_ 3 _, P_ 1). Here, the
quantity of coins on the market ( _Q_ 3) is smaller, but their price
in terms of US dollars is back to the desired level ( _P_ 1).
Whatever deviation from the initial price, the stable purchasing power can, theoretically, be restored by adjusting supply
and demand. Naturally, this model is a simplification and realworld examples are a lot more involved—however, it is helpful
to analyze and classify techniques for maintaining stability.
In the following, we systematically investigate the techniques used by stablecoins to influence supply and demand
and subsequently discuss potential risks and limitations. The
techniques are abstracted to underline their key features and
to remove discrepancies in denominations used by different projects. Furthermore, we compare these to techniques
employed by traditional central banks. In our analysis we
identified six major techniques: (i) collateralization, (ii) interest rates, (iii) currency interventions, (iv) open market


7 Note that the specific shape of the curves is merely an example. It abstracts
the market where a cryptocurrency is exchanged for goods, services or other
currencies. For some cryptocurrency setups, in the short run, the money supply
is independent of the price. This makes the money supply curve a vertical
line that is shifted in the long run. The shape of the curve has no influence

- n the general rationale in the following explanations of stability techniques.




- perations, (v) dynamic block reward and (vi) dynamically
burned transaction fee. The usage of those techniques is not
mutually exclusive, a combination can be applied in practice.


_A. Tokenization of collateral_


Tokenization of collateral (or simply collateralization) links
the coin supply to the demand, so that any change in the
demand incentivizes market participants to change the supply
accordingly. Each stablecoin token is backed by a certain
amount of (crypto-)currencies, assets or fiat money. Users can
create tokens by depositing an underlying backing, the socalled _collateral_ and can redeem (destroy) tokens to receive
their collateral. The entity which stores collateral might be a
smart contract or centralized (as in the case of Tether [17])—
the limitations and drawbacks are discussed in Sec. V.

The creation and destruction of coins through users provides
a mechanism for supply adjustment. On the one side, when
demand increases, market participants can simply create new
coins by depositing collateral, effectively increasing supply.
Due to the excess demand, a coin might trade at a price higher
than the value of the underlying collateral—in this case this
arbitrage opportunity further incentivizes the creation of new
coins. On the other side, when demand decreases, supply can
decrease as well by redeeming coins in exchange for their
collateral and therefore destroying them. Similarly, a coin
might trade below the value of its collateral, creating arbitrage

- pportunities and therefore incentives to destroy coins.
Note that the described incentives (and therefore the success

- f this technique) rely on perfect transferability between coin
and collateral: a coin can always be redeemed for its collateral
and vice versa, without delays or any other friction. A violation

- f this assumption in practice might make this technique less
efficient and therefore a coin subject to price swings.
A number of assets have been proposed as collateral. We
distinguish three subcategory of collateralization: _direct_, _proxy_
and _self-collateralization_ .
In _direct collateralization_, each token is backed by the
asset pegged to (i.e. the asset it is stabilized against). For
example, if the goal is a stable exchange rate to the Euro,
each token is backed by one Euro. This design resembles
the approach of fiat currencies such as the Bulgarian Lev
backed by Euro or Djiboutian Franc backed by US dollars.
Examples of implemented projects include _Stably_ [22] and
_Tether_ [17]. The already implemented concepts show relatively
stable exchange rates to the USD. _Stably_ [22] historically been
able to maintain within a band of 10 % around the peg, and
_Tether_ [17] even within a band of 5 %. There are, however,
examples with larger deviations.
In _proxy collateralization_ each token is not backed by
the targeted currency itself but instead by some other
(crypto-)currency, asset or basket of assets. Different from
direct collateralization, there is a gap between collateral (e.g.,
Ether) and the stabilization target (e.g., USD): falling prices

- f the collateral may lead to insufficient backing.
_Self-collateralization_ is a subform of proxy collateralization.
In this technique, another token which is issued within the


ecosystem of the cryptocurrency itself is used as collateral. The
collateral risk is therefore elevated, since the fate of the ecosystem affects the stablecoin as well as its backing. An already
implemented example is the stablecoin _BitUSD_ [23] which
is backed by the token _BitShares_ [23]. While _BitUSD_ [23]
appeared relatively stable between 0.76 and 1.60 USD per
_BitUSD_ [23] for several years, it slumped below 0.67 USD in
December 2018 when collateral prices declined.
For self and proxy collateralization, the gap between collateral and asset pegged to is mitigated with two (often combined) approaches: first, requiring more collateral than necessary ( _over-collateralization_ ) and second, enforcing automatic
re-collateralization ( _margin calls_ ). In over-collateralization,
more backing is required than the actual price goal of the token
would suggest. As an example, say a stable token backed with
_Bitcoin_ [24] should trade at 1 USD, then over-collateralization
would require to deposit _Bitcoin_ [24] worth 1.5 USD to create a
token. This allows for some volatility of the collateral without
risking that tokens become undercollateralized, i.e., when the
backing is worth less than the price goal of the token.
Margin calls are triggered, if the value of the collateral falls
below a predetermined value, the “margin”, in order to avoid
undercollateralized tokens. In a margin call either the creator

- f a token deposits more collateral or the collateral is offered
for sale on the market in exchange for stable tokens. Given
sufficient liquidity on markets, this effectively rolls back the
creation of a token and decreases its supply.


_B. Use of interest rates_


Interest rates are an instrument to guide a decentralized
adjustment of the money supply. For example, in the current
real-world credit money system, most of the money is created
when commercial banks issue loans to their clients [25]. The
money stock decreases when loans are paid back or money
in circulation is used to make deposits which lock money for
a certain amount of time. Central banks set and adjust the
base interest rate to influence interest rates of the commercial
banks. The higher the rates, the smaller is the number of loans
and the higher is the number of deposits in the system and the
smaller the money supply becomes and vice versa for lower
interest rates. The effectiveness of the technique ultimately
depends on the decisions of the market participants to make
_deposits_ and to take _loans_ .
_Interest rates on deposits_ are in some stablecoin projects
denominated as _parking_ - r _locking_ fees. In this technique,
users lock their coins in order to receive them back after

a specific time with some additional reward (interest). The
interest is paid by the system, most often through the minting

- f new coins. Higher interest rates make the currency more
attractive for investors—demand increases. At the same time,
as a higher fraction of currency is locked in deposits, supply
decreases; at least temporarily. In the long run, supply only
increases as deposits are paid back with interest rate. Among

- thers, “Stableunit” [26], “Minex Coin” [27] and “Nubits” [28]
employ interest rates on deposits.



_Interest rates on loans_ are sometimes referred to as _stability_
_fees_ . Current implementations of loans in cryptocurrencies can
be seen as a generalization of the collateralization technique:
the stable token issued when depositing collateral is a loan

- n that collateral. However, to get the collateral back a user
has to return the stablecoin and may also need to pay a nonzero interest. The interest rate is used to control the number

- f created coins. For instance, raising interest rates makes
borrowing stablecoins more expensive—supply decreases. A
project that has launched a system with interest rates for both
deposits and loans is _Maker_ [29] with its token _Dai_ . Since
December 2017, it has deviated from a 5 % band around the
1 USD peg, with a single day at 0.94 USD.


_C. Currency interventions_

Currency interventions are a technique for a direct money
supply adjustment. Here, an abstract monetary actor in the
form of multiple persons and/or trading bots, intervenes in
currency markets by buying and selling coins in exchange
for the currency to which the stablecoin is pegged. When
demand increases, coins are created and sold on the market
for reserves. This increases the money supply to match the
increased demand and subsequently normalize the price. In
the opposite situation, when demand decreases, coins have to
be bought back, decreasing supply and therefore stabilizing
the price again. In contrast to collateralization where market
participants are incentivized to stabilize the price through the
backing with collateral, currency interventions require active
intervention by some actor related to the stablecoin. Naturally,
the purchase of coins requires that the monetary actor has
currency reserves that can be spent on the market. Once the
reserves are depleted, the exchange rate is governed by market
forces, which can lead to a drastic change in the price and
damage trust.


_D. Open market operations_

Open Market Operations (OMO) can be seen as a generalization of the currency interventions technique. A monetary
actor manually or (semi-)automatically purchases external assets and pays them with newly minted money which increases
the money supply. The system contracts supply by selling
the assets back to the market [8] . For instance, if the Fed buys
U.S. Treasury Securities on the open market, it effectively
increases the supply of dollars. Selling these securities back
to the market allows to decrease the supply again. A number

- f stablecoins implicitly or explicitly consider replicating this
technique. The proposed designs, however, ignore certain
safeguards often used by national central banks.
The most important of these safeguards are _eligibility_ and
_reversibility_ . Eligibility demands that only highly secure and
liquid third-party assets can built central bank reserves (compare [30], [31], [32] or [33], [34]). This ensures that supply


8 We differentiate between currency interventions and OMO to highlight the
specific feature of the former. Buying or selling the targeted currency against
stable coins implies a more effective impact on the mutual exchange rate as
the supplies of the targeted currency and stable coin move in the opposite
direction simultaneously.


can be decreased in the future by selling the assets. The
higher their price, the more money supply can be absorbed.
Reversibility requires, that OMO is automatically reversed
after a predetermined period. This ensures that, by default,
supply increases only short term.
To highlight negligence of the above safeguard principles,
we differentiated between three sub-categories:
_Standard OMO_ classifies OMO implementations satisfying
the eligibility and reversibility safeguards. None of the proposed techniques in current projects can be classified as such.
_Proxy OMO_ violates at least one of the safeguards. Proposals in projects like _Celo_ [35] or _Augmint_ [36] are examples.
_Self-tokenizing OMO_ decreases supply not by selling external assets, but other assets generated within their own
ecosystem. Examples are _Basecoin_ [3], _Carbon_ [37] and
_Fragments_ [38]. All these projects target a 1-to-1 relationship
between their stablecoin and the USD. To decrease the money
supply, the projects propose mechanisms that create specialpurpose tokens that are sold for stablecoins which are then
destroyed by the system. In theory, with such a design, supply
can be decreased to any desired level. This is different from
standard and proxy OMO that are restricted by the available
reserves of external assets. In practice, many open questions
remain (addressed in Sec. V).


_E. Use of dynamic block rewards and dynamically burned_
_transaction fees_


Instead of a pre-defined change in the money supply as in
_Bitcoin_ [24] or _Ethereum_ [39], the mining reward can depend on
the current state of the system. If supply needs to be increased
this can be done by increasing the mining reward. Since a
very low or even negative block reward is not practical, this
technique can only increase supply. Furthermore, increasing
the mining reward is equivalent to “printing” money since
currency is issued without any backing. Note that a variable
block reward leads to variability in the hash rate due to varying
incentives to increase/decrease mining power—elevating the
risk of double-spending attacks [40]. To provide a way to
decrease supply, some projects suggest _dynamically burned_
_transaction fees_, i.e., a part of transactions fees is not given to
miners but burned instead. Hence, the possibility to decrease
supply is limited by the total volume of fees over a period of
time.


V. STABILIZATION TECHNIQUES: DISCUSSION


In the preceding section we presented the stabilization
concepts underlying the surveyed stablecoins. We purposefully
disconnected the in-depth description of the techniques from
the discussion of their merits and drawbacks, which is the

center of this section.


_A. Tokenization of collateral_


While in theory collateralization in itself provides an elegant
way to link money supply and demand through the action of
market participants, it exhibits several risks and limitations
that render this technique less reliable in practice. Direct



collateralization, due the to link to fiat currencies or traditional
assets, requires a trusted third party that manages funds,
assets and the correct issuance of tokens. While the resulting
counterparty risk can be remedied to some degree by, e.g.,
escrow accounts and diversified banking partners, the necessity

- f a trusted third party remains as a major limitation.
Proxy collateralization could help to avoid above risks, since
the collateral can be another cryptocurrency (e.g., _Bitcoin_ [24]

- r _Ether_ [39]). However, even if the counterparty risk can be
eliminated, the requirement of a trusted price feed gives rise to
the oracle problem (cf. Sec. VIII). Furthermore, if the collateral’s value fluctuates (as it is the case for cryptocurrencies),
price risk of the collateral has to be mitigated. Margin calls
are often cited as a remedy for collateral risk, however, margin
calls require the assumption that markets for the collateral
asset are liquid and large enough to allow for timely provision

- r absorption of collateral. This assumption might become an
issue for young stablecoin projects or if expectations on the
future development of the collateral are dire.
As a subform of proxy collateralization, self collateralization exhibits the same risks. Moreover, it suffers from additional systematic risk between the collateral and the stablecoin,
as the value of the collateral is often a function of the future

expected demand on the stablecoin.


_B. Interest rates on deposits and loans_

As discussed in Sec. IV, interest rates on deposits can
reduce the money supply only temporarily and thus should
be coupled with other techniques. When it comes to loans, an
interesting question is whether under-collateralized loans can
be implemented at all. This is the case in the regular economy,
where wealth or future income can be used as collateral. We

argue that this is impossible in permissionless cryptocurrencies due to the lack of strong identities and the resulting
vulnerability to Sybil attacks [7]. If under-collateralized loans
were implemented, rational actors would spawn multiple fake
identities to obtain loans and free money.


**Theorem 1.** _In a permissionless setting without strong iden-_
_tities, under-collateralized loans enable arbitrage to the point_
_where only fully collateralized loans are available._


_Proof._ Let _L_ be a loan that can be taken by depositing an
amount of collateral _C_, with _pL_ and _pC_ denoting the respective
prices. In an under-collateralized setting _pC < pL_ . A rational
agent would seize the arbitrage opportunity, spend _pC_ - n
collateral and receive a loan with value _pL_ = _pC_ + _ϵ_ . The
loan can be used to purchase more collateral and create more
loans, generating a profit of _ϵi_ in each step _i_, until the arbitrage

- pportunity closes due to increased collateral demand, i.e.
_pC_ ≮ _pL_ . Since there are no identities, the agent can refuse
to repay the loans he has taken without any risk, locking the
collateral forever and still generating a profit of [�] _ϵi_ .


Even with smart contracts that enforce payments and interest rates, the lack of strong identities makes it easy to
simply “exit-scam” the system, i.e., to generate a new debtfree identity and start over without negative consequences.


_C. Currency Interventions_

For currency interventions, the ability to maintain a peg
during falling prices is limited by the amount of available
reserves and the monetary authorities’ commitment to make
use of them. Once the reserves are depleted, the exchange
rate is governed by market forces, which can lead to a drastic
change in the exchange rate. The usage of currency interventions can, under certain assumptions, increase the vulnerability
to speculative attacks (cf. Sec. VI-C). The interplay of full
transparency of the system and gameability of the intended
interventions is an interesting open question.


_D. Open market operations_

The negligence of safeguards by techniques classified as
proxy OMO is no triviality. High quality (eligibility) of the
assets seized by the cryptocurrency system prevents erosion of
its reserves that can be used to buy back outstanding currency
units. The programmatic reversal of open market arrangements
ensures that a long term expansion of the money supply is
not possible without manually overriding the default policy.
While reviewed projects only allow using cryptocurrencies
with a relatively long track record ( _Bitcoin_ [24], _Ether_ [39]),
reversibility has not been proposed yet.
In self-tokenizing OMO not reserves but special-purpose
tokens are sold against currency units. While the designs of
the tokens vary, all provide some form of success-related
monetary incentive that is payed out if a certain target price
for the stablecoin is achieved. The incentive is paid out in
form of newly minted money supply. The lower the probability of success, the higher the necessary incentives. Risk
is either remunerated by higher relative ownership of future
money growth or by a promised absolute increase of future
minted money. Excessive use thus may either lead to reduced

- wnership in risk remuneration or to an uncontrolled increase

- f promises of future remuneration in the money supply.
Similar to currency interventions, OMO setups are vulnerable
to speculative attacks (c.f. Sec. VI-C). Lastly, the technique
can decrease supply only in the short run, as long as token
remuneration promises are not retracted.


_E. Dynamic mining reward_

Mining is a vital function of most cryptocurrency systems.
The goal of making the money supply dynamic should be
subordinated to the security and usability of the financial
system. Low block rewards or high difficulty, e.g., in phases of
stagnating demand for the currency, would lead to less incentive for miners to process transactions. This would necessarily
lead to lower transaction throughput, which would not only
reduce the liquidity of the coin, but also increase the risk of
double-spending attacks. Moreover, as this technique cannot
be used to reduce the money supply, it should be coupled
with other instruments.


_F. Classification results and blank spots_

Fig. 2 shows a full list of techniques discussed in this section
as well as their prevalence of adoption in stablecoins projects,
distinguished by planned and implemented.






















|Col1|Col2|Col3|Col4|Col5|375<br>.|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||8.3|||41|.7||
|||8.3|2|5||||
||4|.2|20|.8||||
||0||20|.8||||
||4|.2|20|.8||||
|||8.3<br>1|2.5|||||
|||8.3<br>8.3||||||
||0|8.3||||||
||0<br>4|.2||||||
||0<br>0|||||||
||0|||||||





Fig. 2: Planned and implemented stabilization techniques.


The most popular technique according to our observations
is direct collateralization. It is followed by the use of dynamic
mining reward, interest rates on deposits and self-tokenizing
OMO. None of these methods can permanently decrease
money supply. Current stablecoin projects plan to launch
primarily solutions which either require the participation of
a trusted third-party or are focused on techniques that can
decrease supply only temporarily and consequently are not
sustainable in the long term.
Interest rates on loans, currency interventions, standard
OMO and maybe even proxy OMO might be useful techniques
as they allow for decreasing the money supply permanently.
However, exactly those have been worked on to a lower
degree: although well over 40 % of projects plan some form

- f OMO, only around 4 % implemented their proposed setup.
Note that established monetary policy standards find little
acknowledgment—no project implemented the requirements

- f standard OMO, although other types of OMO are introduced. As there is little practical experience yet, risks and
potentials of these techniques are hard to assess.
But also for less complex approaches there are blank spots.
None of the reviewed projects has implemented dynamically
burned transaction fees or proxy collateralization.


VI. EXCHANGE RATE REGIMES


So far we implicitly interpreted “stability” as stabilizing the
price of each stablecoin to _exactly_ 1 EUR or 1 USD. While this
seems to be an intuitive approach, other so called _exchange_
_rate regimes_ are possible.


TABLE II: Percentage of days for which certain bands around
the 1 USD peg are violated.


Projects _±_ 1 % _±_ 5 % _±_ 10 % _±_ 20 %

Tether (USDT) 12 _._ 11 1 _._ 05 0 0
Maker (Dai) 25 _._ 25 0 _._ 50 0 0
Trusttoken (TrueUSD) 30 _._ 75 0 _._ 60 0 _._ 60 0
Sythetix (SUSD) 33 _._ 66 3 _._ 90 0 _._ 98 0
Centre (USD Coin) 66 _._ 10 0 0 0
Stronghold (USDS) 80 _._ 43 8 _._ 70 0 0
BitShares (BitUSD) 70 _._ 95 30 _._ 23 13 _._ 84 4 _._ 26
NuBits (Nubits) 42 _._ 22 27 _._ 22 26 _._ 59 24 _._ 07
USC (USC) 56 _._ 25 31 _._ 25 31 _._ 25 25






|Col1|Col2|Col3|Col4|396<br>.|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||13<br>~~2~~|~~.8~~||50|||||
|||2|0.8|~~37.5~~<br>41.|7|||||
||~~0~~<br>4.2|16.1||||||||
||1<br><br>~~4.2~~<br>4.2|0.4||||||||
||~~0~~<br>0|||||||||





Fig. 3: Exchange rate arrangements: stablecoins and national
currencies.


_A. Types of exchange rate regimes_


We build upon a taxonomy of the IMF [19] which splits
exchange rate regimes into three main types: _hard pegs_,
_soft pegs_ and _floating regimes_ . Compare Appendix B for a
hierarchical representation of these regimes.
A _hard peg_ can come in one of two flavors: arrangements
without legal tender and so-called _currency boards_ . In an
arrangement without legal tender a country chooses to simply
use a well-known foreign currency like the USD instead of
issuing their own. [9] We neglect this case since it is clearly not
useful for cryptocurrencies: it would essentially mean to avoid
them altogether. In a currency board the domestic currency is
backed 1:1 (or more) by reserves of the foreign currency [41].
That is, for every issued unit of domestic currency, there has
to be at least one unit of the foreign currency in the reserves.
Different from hard pegs, _soft pegs_ are characterized by
weaker commitments to a fixed rate, i.e., there does not need
to be a 1:1 backing with reserves. Soft pegs come in a variety

- f different flavors. The most important are: conventional pegs,
pegs with horizontal bands and crawling pegs.
A _conventional peg_ is defined by the level of allowed
deviations. The IMF specifies a maximum fluctuation of 1 %

- ver a time period of at least six months around the pegged
value. A weaker form is the so-called _peg with horizontal_
_bands_, where the exchange rate is allowed to fluctuate within a
pre-announced (wider) range around the pegged value. These
peg types share a common property: the exchange rate is
constant over time. In contrast, _crawling pegs_ allow for a
gradual adjustment in the exchange rate.
Last but not least, if the exchange rate is _floating_, little to no
guarantees are given about the stability of the value. Instead,


9 Note that, on a more general level, currencies can also peg against external
assets (e.g., gold).



the exchange rate is determined by market forces to a large
degree and monetary interventions are kept to a minimum. Due
to the fact that free floating can lead to high volatility, some
countries intervene aggressively against short term fluctuations
(compare Sec. IV). This practice is known as “smoothing” or
_floating with interventions_ .


_B. Classification results and blank spots_



Fig. 3 shows a comparison of exchange rate arrangements in
stablecoins and traditional central banks. [10] The data for central

banks stems from a study of the IMF in 2016 [19].
The majority of stablecoins, 91 _._ 7 %, commit to achieve
some kind of peg. As in traditional central banking, in cryptocurrencies one has to distinguish between what is announced
(de-jure) and the historical exchange rate (de-facto). De-jure
the majority of stablecoins commit themselves to a fixed 1:1
correspondence to the USD in their whitepapers. 41 _._ 7 % of all
projects, tries to enforce this by establishing a currency board
and storing the fiat currency pegged to. Implemented examples
include _Tether_ [17], _Stasis_ [42] and _Trusttoken_ [43].
The remainder (50 % of all projects), does not implement
a currency board and are therefore classified as a soft peg.
Examples include _Maker_ [29], _Stasis_ [22], _Nubits)_ [28], _Syn-_
_thetix_ [44] and _Bitshares_ [23]. Most abstain from explicitly
specifying bands and are therefore conventional soft pegs. [11]

Table II shows the fraction of daily closing prices violating
certain thresholds between the launch of the respective coin
and February 7, 2019. The Table contains the subset of
coins that pursue a 1-to-1 peg to the USD. De-facto, none

- f the already launched cryptocurrencies meets the demands
that would be posed by the IMF for a working conventional
peg. Interestingly, even _Tether_ [17] and _Trusttoken_ [43] violate the requirements, despite implementing currency boards.
These fluctuations may stem from uncertainty caused by a
perceived lack of transparency and accountability or lower
market liquidity. National currencies in turn tend to use
floating arrangements more often. Although the majority of
analyzed stablecoins pursues pegs, concepts for floating arrangements with interventions are also in development, e.g.,


10 Note that the category “residual” refers mainly to countries with
frequently changing monetary policy approaches.
11 Some projects mention “some” corridor around the peg. As bands are
supposed to be predetermined and announced for accountability reasons, we
still classify them as conventional pegs.


_MinexCoin_ [27] proposes interventions to keep daily price
changes from exceeding 5 %.


_C. Vulnerabilities to speculative attacks_


The usefulness of soft pegs is disputed in economic literature. This standpoint is called the _bipolar view_ [45], [46],
and is broadly supported by mainstream economists [45],

[47]–[49]. The bipolar view suggests that there are only
two long-term viable options for currency regimes that care
for exchange rates: hard pegs or floating with interventions.
Reasons given are short life expectancy of soft pegs and
vulnerability to speculative attacks [45].
Speculative attacks on soft pegs are known from traditional
central banking [50], [51], but the threat is equally applicable
to cryptocurrencies. This is especially relevant considering that
50 % of stablecoin projects plan on using soft pegs.
If the market believes that a fixed exchange rate is not
sustainable, investors will start speculating against it to make
a profit in the event that it eventually breaks. To counteract,
central banks have to invest resources to defend the peg, which
is costly and oftentimes unsuccessful [52]. A vivid illustration

- f unsuccessful peg defense is the Bank of England’s attempt
to maintain a fixed Great Britain Pound (GBP)-European
Currency Unit (ECU) exchange rate during a speculative attack
in 1992 lead by the hedge fund “Quantum”. [12]

The investors and, subsequently, other market participants
followed a simple algorithm:


1) Borrow GPB and sell them, at market price, for German
Marks (DM); this is called a _short sale_ .
2) When the peg fails and the exchange rate drops, buy
back GBP at a cheaper price and return to lender.

The selling of borrowed GBP for DM increases the supply of
GBP and reduces the supply of DM. Due to the fundamental
principles of demand and supply, this in turn leads to an
appreciation of DM and depreciation of GBP. To counteract
and maintain the target exchange rate, the Bank of England
bought the excess GBP on the foreign exchange market in
exchange for their DM reserves. Furthermore, the Bank of
England also increased the base interest rate. Buying the
excess supply of GBP aimed at reducing the supply of GBP

- n the markets, whereas the increase of the interest rate aimed
to increase the demand for GBP. However, after spending
15 billion USD in foreign reserves in only a single day,
the Bank of England eventually had to abandon the pegged
arrangement [53], [54]. The exchange rate on the market
dropped, yielding an estimated profit of 1.5 billion USD [13] .
There are two main sources that make speculative attacks

- n pegs highly probable [50], [51]: unsustainably constructed
pegs and untrustworthy commitment to defend the peg. A peg
is unsustainable if the central bank lacks sufficient reserves to
invest in the case of a speculative attack. In cryptocurrencies
this vulnerability is increased further, since they often have a


12 ECU was an artificial currency used within the European Monetary
System before the introduction of the Euro in 1999 [53].
13 https://www _._ forbes _._ [com/sites/steveschaefer/2015/07/07/forbes-](https://www.forbes.com/sites/steveschaefer/2015/07/07/forbes-flashback-george-soros-british-pound-euro-ecb/4e0e93346131)
[flashback-george-soros-british-pound-euro-ecb/4e0e93346131](https://www.forbes.com/sites/steveschaefer/2015/07/07/forbes-flashback-george-soros-british-pound-euro-ecb/4e0e93346131)



small market capitalization and little reserves in comparison
to traditional financial assets and currencies. Furthermore, the
complete transparency of reserves due to the transparency

- f the blockchain makes it easy for speculative attackers to
validate the success of their strategy [55].
Adapting [50] to cryptocurrencies, consider a situation
where the natural floating exchange rate would be lower then
the peg. Among others, reasons might be new vulnerabilities

- r general uncertainty in cryptocurrencies due to regulation.
In both cases, the stablecoin system would need to intervene

- ver longer periods of time, draining its reserves. Two longerterm outcomes are possible: (1) the peg holds or (2) the
currency finally depreciates when the intervention capabilities
are depleted.
Now consider a user of the coin who chooses to _hold_ her

position. This user will have no payoff in case (1) and negative
payoff in case (2). Therefore, the expected payoff from holding
is negative. In contrast, if the user _sells_ her coins, the sale can
be reverted with little cost in case (1) and can avoid a loss in
case (2). Therefore, the payoff for selling is higher than for
holding. Rational market participants will sell their holdings.
The expected payoff of the sell strategy can even be
increased through leverage by borrowing coins. [14] Speculators
might borrow large quantities of stable coins at the pegged
price and sell them on the exchanges: if the stability system
succeeds in defending the peg, speculators can buy back the
coins at the peg and revert their positions with little losses.
If the attack depletes the reserves of the system, the peg can
no longer withstand the selling pressure and the exchange rate
depreciates and becomes floating. Attackers can now buy back
the stablecoins much cheaper, give back borrowed coins and
keep the difference as profit.


_D. Peg hard or do not peg at all?_


As discussed, the bipolar view suggests hard pegs, float or
float with interventions.
While conclusions transferred from monetary policy studies
should be treated with caution, the bipolar view still offers
insights useful for cryptocurrency systems: Hard pegs using
full direct collateralization and floating exchange rate arrangements are less vulnerable to speculative attacks then soft pegs.
This explicitly holds for all soft peg implementations that do
not allow for the retraction of most of the money stock in any
kind of market situation.

As discussed, currency interventions and open market operations (OMO) that contract money supply by selling limited
reserves are definitely concerned. Self-tokenizing OMO and
interest rates on deposits buy back coins against self-issued
securities with potentially unlimited supply. As discussed in
Sec. V, buyers of these special-purpose tokens are incentivized
by a share in newly minted money in the case of _longterm_ increasing demand for the stablecoin. As discussed in Sec. VI-C
speculative attacks entail almost no risk or costs for the


14 Since efficient credit markets have not yet developed for all cryptocurrencies, the transaction costs to execute speculative attacks might be increased.


attacker, making repeated attempts in the _short run_ possible.
While in the presence of speculators for and against the peg
the first series of speculative attacks might be neutralized,
claims for risk remuneration will stack up quickly. Leading to
a decrease in relative ownership of future remuneration, this
will decrease the demand for the used special-purpose tokens
with every round of attack. Missing demand for the self-issued
tokens makes it impossible to absorb money supply and defend
against the attack. Further research is strongly encouraged as
the above setup is quite popular. Nine out of the 24 reviewed
projects and thus almost 38 % consider it.
We do question though, if all kinds of soft pegs are equally
vulnerable in the case of cryptocurrencies. Soft-pegs relying
solely on full proxy and self-collateralization promise to
provide sufficient collateral to buy back the complete stock

- f money at any moment of time. This, in turn, makes them
immune to the above described attack [52].


VII. MONETARY REGIMES


Up to this point, we used the notion of “stability” in the
sense of low exchange rate volatility. In the following, we
zoom out further, stressing the difference between


_•_ stabilizing the _amount of another currency_  - ne cryptocurrency unit can buy (exchange rate) and

_•_ stabilizing the _amount of goods and services_  - ne cryptocurrency unit can buy (purchasing power).

Stable purchasing power is a goal which traditional central
banks and stablecoins both pursue. Stability of prices can be
measured, e.g., through a basket of goods in a consumer price
index (CPI). In practice it is can be influenced only via indirect
measures. These encompass interest rates, exchange rates and
many others. The respective choice of tool set constitutes the
monetary regime. Each monetary regime chooses a certain
core variable, the so-called _nominal anchor_, to construct its
monetary policy around. The chosen nominal anchor is used
to choose practical applications of monetary instruments and
to evaluate their effectiveness. It can be seen as the central

element of the monetary regime and as the measurement
variable around which central bank communication and also

accountability line up.
Thus, while stable purchasing power is the overarching
goal—fixing exchange rates (so called _exchange rate target-_
_ing_ ) is only one of several strategies to achieve it. Other
monetary regimes focus on other factors than the exchange
rate, namely _monetary targeting_ and _inflation targeting_ .
_Monetary targeting_ uses the amount of money as its nominal
anchor [56]. Assuming predictable velocity of money, the socalled Quantity Equation of Money can be used to calculate
the necessary money supply to achieve a certain level of
prices [57]. [15] Correspondingly, adjusting the money supply is
a key means of intervention for a central bank in such regimes.


15 Different versions of the quantity equation of money arose after being
popularized by [58]. All have in common that they relate the aggregated
flows of money to aggregated flows of goods and services. The equations

- ffer different perspectives on the demand of money.



_Inflation targeting_ uses the change in a consumer price index
as nominal anchor [59]. The most characteristic differences
to monetary targeting lies in the publication of numerical
inflation targets and the commitment to hit them. Additionally,
also commitment and ability to achieve the inflation target,
emphasis on transparency and increased accountability are
quoted characteristic of inflation targeting [56].


_A. Regime-inherent aspects_


While _exchange rate targeting_ is a popular arrangement
for cryptocurrencies and countries alike, it exhibits major
drawbacks. First, as stated in [52], exchange rate targeters lose
the ability to pursue independent monetary policy. Moreover,
inflationary tendencies and shocks are imported directly into
the cryptocurrency. Third, as discussed in Sec. VI-D, exchange
rate targeting can lead to vulnerabilities to speculative attacks.
On the other hand, exchange rate targeting offers convincing
advantages from the perspective of cryptocurrencies. First,
pegging the value of a cryptocurrency to some other currency

- r asset can reduce the volatility drastically, since price
fluctuations of, e.g., USD, are magnitudes smaller than in
most cryptocurrencies [2]. Second, not even the most mature
cryptocurrencies do succeed to be used as unit of account for
the purchase of goods or services [2], [60], so that prices are
not typically quoted in cryptocurrency units. Therefore, also
from a usability perspective it is a reasonable choice to strive
for a stable relationship to fiat currencies.
_Inflation targeting_ poses the obvious challenges of the
definition and tracking of an adequate basket of goods and
services. More importantly, goods usually are denominated
in some national currency. Purchasing power fluctuations of
a volatile cryptocurrency measured by a basket of dollar
denominated goods should mainly be caused by exchange rate
variability. As a consequence inflation targeting and exchange
rate targeting would be close to equivalent.
_Monetary targeting_ in a sense is already implemented by
traditional cryptocurrencies with predetermined block reward.
More sophisticated monetary targeting approaches might use
literature around rule based monetary policy (e.g. [61], [62],

[63] or [64]) as first starting point. If additional measures
against exchange rates are to be taken, managed floating
regimes as promoted by [65], [66], might offer a simple
but sustainable alternative to exchange rate targeting. This
approach, however, mitigates only short term fluctuations.


_B. Classification results and blank spots_


Fig. 4 shows that the prevalence of exchange rate targeting
in the reviewed projects is in stark contrast to traditional
central banks (numbers for countries from [19]). Exchange
rate targeting, accounting for 91 _._ 7 % of all projects, is the clear
favorite of current approaches to cryptocurrency stabilization.
Only 42 _._ 7 % of countries use a certain exchange rate as
their currency’s nominal anchor. While monetary targeting in
combination with short term exchange rate smoothing could
be an interesting alternative, it has largely been ignored by
cryptocurrencies.


|Col1|Col2|Col3|Col4|42<br>.|7|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||12.5|||~~5~~|~~.3~~||91.|7|
||~~4.2~~<br>8.|3|24|||||||
||~~0~~<br>0|2|0.8|||||||
||~~0~~<br>0|||||||||



Fig. 4: Monetary regimes: reviewed projects and central banks.


VIII. DECENTRALIZATION AND TRUST


Departing from mainly economic questions, we will now
discuss the design of stable cryptocurrencies in terms of their
”decentralization” and ”trustlessness”—notions that cryptocurrencies are commonly associated with and potentially owe
their popularity to. We focus on contrasting fully _permis-_
_sionless_ systems, i.e., systems that function without previous
assumptions about the identifiability of participants or their
trustworthiness, with architectures in which the existence of
a group of well-known _trusted actors_ must be assumed. With
the current state of knowledge, it is an outstanding question
whether an effectively price-stable cryptocurrency can at all
be realized in a fully permissionless setting.
Techniques based on the collateralization or holding of
”off-chain” assets (such as classical currencies) are _inherently_
_incompatible_ with a fully permissionless setup. Neither the
actual existence nor the correct management of off-chain
collateral can, in general, be secured through purely technical
means. Rather than that, a form of trust, either in one ore more
well-known custodians or in a surrounding legal framework
and its enforcement mechanics, must be assumed.
Techniques based on collateralization, interest rates and
OMOs are in principle compatible with a fully permissionless
mode of operation as long as they act on assets whose ownership can be securely tracked and managed in a permissionless
manner (e.g., are recorded on the same permissionless ledger).
Even then, however, a fully permissionless mode of operation
is only possible under a significant caveat—the existence

- f a secure (permissionless) _oracle_ for the chosen nominal
anchor. Oracles are system components that transfer ”external”
information onto the blockchain. Monetary information, such
as the price of the cryptocurrency relative to another currency,
are required for monetary policy mechanisms. They are typically not natively generated ”on-chain” and must therefore
be provided by an oracle. Oracles can be trivially realized
using a trusted party that vouches for the correctness of
data by means of cryptographic signatures. However, this



clearly reinstates a globally trusted actor (or a group thereof).
Completely permissionless oracles are, on the other hand, still
an active research field, with no sufficiently secure solutions
for, e.g., transferring price data, currently in sight [4]. It is
possible that secure permissionless oracles for arbitrary data
are a theoretical impossibility [7]. In such a case, a final
possibility for the realization of completely permissionless
stablecoins remains in the deepened investigation of on-chain
_proxy variables_ for relevant nominal anchors like current
prices. We are currently aware only of the current mining hash
rate, as materialized, e.g., in the timing between blocks and the
current mining difficulty, as a potentially viable representative

- f this class. More research is needed here to further test the

viability of this approach, especially in respect to incentivecompatibility, gameability and security (c.f. Sec. V-E).


IX. FROM INDIVIDUAL CLASSIFICATIONS TO TAXONOMY



In the course of this article, we put together three perspectives on price stability: (i) practical stabilization techniques,
(ii) exchange rate regimes, (iii) monetary regimes. Each
perspective offers a classification. Taken together, the three
classifications build a taxonomy that might prove a helpful tool
for developers, research and investors. A schematic overview

- ver can be found in Appendix B


X. CONCLUSION


In this paper, we systematically explore the enigma of
monetary stabilization in cryptocurrencies. We go beyond
individual proposals, focusing on overarching concepts and
approaches. We extracted information from 24 stablecoin
projects and combine the resulting insights with economic
literature yielding a comprehensive taxonomy for the analysis
and classification of stablecoins. We find that, the three most
popular stability techniques following after direct collateralization are unsustainable in the long run. Moreover, our
findings show that almost 38 % of surveyed coins promote a
problematic combination of exchange rate targeting and using
either limited reserves or a potentially unlimited supply of
self-issued tokens to reduce the coin supply. There are strong
indicators that the above setup can result in a vulnerability
to speculative attacks. On the other hand, proxy and self
collateralization (promising alternative techniques that might
be applicable in “trustless” settings) rely heavily on margin
calls with questionable robustness. Further research is required
to evaluate the viability of such margin calls in small and potentially illiquid markets. Zooming out, we suggest that short
term smoothing of exchange rates might offer a sustainable
alternative to exchange rate targeting—the current focus of

- ver 90 % of projects.
We identify a number of further opportunities for technical
and economics research on cryptocurrency stabilization, such
as on the resilience of self-tokenizing techniques, on the
viability of secure permissionless price feeds for informing
policing decisions, and on the actual effectiveness of monetary
policy given the complete transparency of both the policy and
its enforcement.


APPENDIX A

SURVEYED PROJECTS


A list of surveyed stablecoin projects and their respective classification. Note that, “partially implemented” refers to the fact
that the coin itself is traded while not all announced stabilization techniques are implemented yet.


Project (Stabilized Token) Status MR ERA T1 T2 T3 T4 T5 T6 T7 T8 T9 T10 T11


Augmint (A-EUR) not impl. ERT soft peg  -  -  -  - yes yes  - yes  -  -  Aurora (Boreal) not impl. ERT soft peg   -   -   -   - yes   -   - yes   -   -   Basecoin (Basis) retracted ERT soft peg   -   -   -   -   -   -   -   - yes yes   BitShares (BitUSD) impl. ERT soft peg  -  - yes  -  -  -  -  -  -  -  Carbon (Carbon) impl. ERT soft peg   -   -   -   -   -   -   -   - yes yes   Celo (Celo) not impl. ERT soft peg    -    -    -    -    -    -    - yes yes yes    Centre (USD Coin) impl. ERT hard peg yes  -  -  -  -  -  -  -  -  -  Digix (Digix Gold Token) impl. ERT hard peg yes - - - - - - - - - Fragments (Fragments) not impl. ERT soft peg - - - - - - - yes yes - Globcoin (GLC Token) impl. ERT hard peg yes - - - - - - - - - Karbo (Karbo) partially impl. MT free float   -   -   -   -   - yes   -   -   - yes   Kowala (kUSD) not impl. ERT soft peg   -   -   -   -   -   -   -   -   - yes yes
Maker (Dai) impl. ERT soft peg    -    -    -    - yes    -    -    -    -    -    Minex Coin (Minex Coin) impl. MT float. w. int. - - - yes - yes - - - - NuBits (Nubits) impl. ERT soft peg   -   -   - yes   - yes   -   -   - yes   Stableunit (Stableunit) not impl. ERT soft peg  -  -  -  -  - yes  - yes yes  -  Stably (StableUSD) impl. ERT hard peg yes  -  -  -  -  -  -  -  -  -  Stasis (EURS) impl. ERT hard peg yes   -   -   -   -   -   -   -   -   -   Stronghold (USDS) impl. ERT hard peg yes  -  -  -  -  -  -  -  -  -  Sythetix (SUSD) impl. ERT soft peg   -   - yes   -   -   -   -   -   -   -   Tether (USDT) impl. ERT hard peg yes   -   -   -   -   -   -   -   -   -   Trusttoken (TrueUSD) impl. ERT hard peg yes  -  -  -  -  -  -  -  -  -  USC (USC) impl. ERT hard peg yes   -   -   -   -   -   -   -   -   -   x8currency (X8C) not impl. ERT hard peg yes   -   -   -   -   -   -   -   -   -   

**Abbreviation** **Full text**

MR Monetary regime
ERA Exchange range arrangement
MT Monetary targeting
ERT Exchange rate targeting
float. w. int. Floating with interventions
impl. Implemented
T1 Collateralization (direct)
T2 Collateralization (proxy)
T3 Collateralization (self)
T4 Currency interventions
T5 Interest rates with loans

T6 Interest rates with deposits
T7 Open market operations (standard)
T8 Open market operations (proxy)
T9 Open market operations (self-tokenizing)
T10 Dynamic mining reward
T11 Dynamically burned transaction fee


APPENDIX B

TAXONOMY












|Hard peg|Currency board|Soft peg|Crawling|Floating arrangements|Floating with<br>interventions|
|---|---|---|---|---|---|
|Hard peg|Currency board|Soft peg|Horizontal bands|Horizontal bands|Horizontal bands|
|Hard peg|No legal tender|No legal tender|No legal tender|No legal tender|Free ﬂoat|
|Hard peg|No legal tender|No legal tender|Conventional|Conventional|Conventional|
















|Direct<br>collaterali<br>-<br>zation|Proxy<br>collaterali<br>-<br>zation|Self<br>collaterali<br>-<br>zation|Interest<br>rates on<br>loans|Interest<br>rates on<br>deposits|Dyn<br>.<br>mining<br>reward|Dyn burned<br>.<br>transaction<br>fee|
|---|---|---|---|---|---|---|
|Open<br>market<br>operations<br>(proper)|Open<br>market<br>operations<br>(proxy)|Open<br>market<br>operations<br>(self)|Currency<br>interventions|Currency<br>interventions|Currency<br>interventions|Currency<br>interventions|


REFERENCES


[1] K. Saito and M. Iwamura, “How to make a digital currency on a
blockchain stable,” _CoRR_, vol. abs/1801.06771, 2018.

[2] D. Yermack, “Is bitcoin a real currency? an economic appraisal,” in
_Handbook of digital currency_, Elsevier, 2015.

[3] Misc., _Basis coin whitepaper_ [, https://www.basis.io/basis whitepaper](https://www.basis.io/basis_whitepaper_en.pdf)
[en.pdf, visited on 2018-07-13, 2017.](https://www.basis.io/basis_whitepaper_en.pdf)

[4] J. Adler, R. Berryhill, A. G. Veneris, _et al._, “Astraea: A decentralized
blockchain oracle,” _CoRR_, vol. abs/1808.00528, 2018.

[5] J. Peterson and J. Krug, “Augur: A decentralized, open-source platform
for prediction markets,” _CoRR_, vol. abs/1501.01042, 2015.

[6] F. Zhang, E. Cecchetti, K. Croman, A. Juels, and E. Shi, “Town crier:
An authenticated data feed for smart contracts,” in _Prof. of CCS_, ACM,
2016.

[7] J. R. Douceur, “The sybil attack,” in _Peer-to-peer Systems_, Springer,
2002.

[8] M. Iwamura, Y. Kitamura, T. Matsumoto, and K. Saito, “Can we
stabilize the price of a cryptocurrency?: Understanding the design of
bitcoin and its potential to compete with central bank money,” _SSRN_,
vol. abs/2519367, 2014.

[9] C. Caginalp and G. Caginalp, “Opinion: Valuation, liquidity price, and
stability of cryptocurrencies,” _Proceedings of the National Academy of_
_Sciences_, vol. 115, no. 6, 2018.

[10] C. Caginalp, “A dynamical systems approach to cryptocurrency stability,” _CoRR_, vol. abs/1805.03143, 2018.

[11] G. Danezis and S. Meiklejohn, “Centrally banked cryptocurrencies,”
in _23rd Annual Network and Distributed System Security Symposium,_
_NDSS_, The Internet Society, 2016.

[12] M. L. Bech and R. Garratt, “Central bank cryptocurrencies,” _SSRN_,
vol. abs/3041906, 2017.

[13] J. Koning, “Fedcoin: A central bank-issued cryptocurrency,” _R3 Report_,
vol. 15, 2016.

[14] O. Bjerg, “Designing new money - the policy trilemma of central bank
digital currency,” _SSRN_, vol. abs/2985381, no. ID 2985381, 2017.

[15] S. Kim, A. Sarin, and D. Virdi, “Crypto-assets unencrypted,” _SSRN_,
vol. abs/3117859, 2018.

[16] K. W¨ust and A. Gervais, “Do you need a blockchain?” In _Proc. of_
_CVCBT_, 2018.

[17] Misc., _Tether whitepaper_ [, https://tether.to/wp-content/uploads/2016/](https://tether.to/wp-content/uploads/2016/06/TetherWhitePaper.pdf)
[06/TetherWhitePaper.pdf, visited on 2018-07-16.](https://tether.to/wp-content/uploads/2016/06/TetherWhitePaper.pdf)

[18] F. S. Mishkin, “International experiences with different monetary
policy regimes,” _Journal of monetary economics_, vol. 43, no. 3, 1999.

[19] I. M. Fund, “Exchange arrangements and exchange restrictions: Annual
report,” International Monetary Fund, Tech. Rep., 2016.

[20] B. of Governors of the Federal Reserve System, _Policy tools_, 2017.

[21] E. C. Bank, _The eurosystem’s instruments_, 2019.

[22] Misc., _Stably whitepaper_ [, https://s3.ca- central- 1.amazonaws.com/](https://s3.ca-central-1.amazonaws.com/stably-public-documents/whitepapers/Stably+Whitepaper+v6.pdf)
[stably- public- documents/whitepapers/Stably+Whitepaper+v6.pdf,](https://s3.ca-central-1.amazonaws.com/stably-public-documents/whitepapers/Stably+Whitepaper+v6.pdf)
visited on 2018-07-16, 2018.

[23] - —, _Bitshares whitepaper_ [, https : / / web . archive . org / web /](https://web.archive.org/web/20170822062343/http://docs.bitshares.eu:80/_downloads/bitshares-financial-platform.pdf)
[20170822062343/http://docs.bitshares.eu:80/ downloads/bitshares-](https://web.archive.org/web/20170822062343/http://docs.bitshares.eu:80/_downloads/bitshares-financial-platform.pdf)
[financial-platform.pdf, visited on 2018-07-16, 2015.](https://web.archive.org/web/20170822062343/http://docs.bitshares.eu:80/_downloads/bitshares-financial-platform.pdf)

[24] S. Nakamoto _et al._, “Bitcoin: A peer-to-peer electronic cash system,”
2008.

[25] M. McLeay, A. Radia, and R. Thomas, “Money creation in the modern
economy,” _Bank of England Quarterly Bulletin Q1_, 2014.

[26] Misc., _Stableunit whitepaper_ [, https : / / stableunit . org / documents /](https://stableunit.org/documents/StableUnit-whitepaper.pdf)
[StableUnit-whitepaper.pdf, visited on 2018-09-03.](https://stableunit.org/documents/StableUnit-whitepaper.pdf)

[27] - —, _Minexcoin whitepaper_ [, https : / / minexcoin . com / whitepaper,](https://minexcoin.com/whitepaper)
visited on 2018-09-07.

[28] - —, _Nubits whitepaper_ [, https://www.nubits.com/about/white-paper,](https://www.nubits.com/about/white-paper)
visited on 2018-07-13, 2014.

[29] - —, _Dai whitepaper_ [, https://makerdao.com/whitepaper, visited on](https://makerdao.com/whitepaper)
2018-11-30, 2017.

[30] E. C. Bank, _Purchase programme for covered bonds_, 2009.

[31] - —, _Eligibility criteria and assessment_, 2019.

[32] - —, _Guiding principles (with examples) of eurosystem-preferred_
_eligible abss_, 2015.

[33] M. C. of the Bank for International Settlements, “Monetary policy
frameworks and central bank market operations,” Bank for International Settlements, Tech. Rep., 2009.

[34] S. Cheun, I. von K¨oppen-Mertes, and B. Weller, “The collateral
frameworks of the eurosystem, the federal reserve system and the bank




    - f england and the financial market turmoil,” ECB Occasional Paper,
Tech. Rep., 2009.

[35] Misc., _Celo whitepaper_, Whitepaper classified Please request access
via community@celo.org. visited on 2018-11-30.

[36] - —, _Augmints whitepaper_ [, https://docs.google.com/document/d/](https://docs.google.com/document/d/1IQwGEsImpAv2Nlz5IgU_iCJkEqlM2VUHf5SFkcvb80A/edit)
[1IQwGEsImpAv2Nlz5IgU iCJkEqlM2VUHf5SFkcvb80A/edit, visited](https://docs.google.com/document/d/1IQwGEsImpAv2Nlz5IgU_iCJkEqlM2VUHf5SFkcvb80A/edit)

    - n 2018-07-16, 2018.

[37] - —, _Carbon whitepaper_ [, https://www.carbon.money/whitepaper.pdf,](https://www.carbon.money/whitepaper.pdf)
visited on 2018-07-16, 2018.

[38] - —, _Fragments whitepaper_ [, https://fragments.network/fragments-](https://fragments.network/fragments-platform-whitepaper.pdf)
[platform-whitepaper.pdf, visited on 2018-09-03.](https://fragments.network/fragments-platform-whitepaper.pdf)

[39] G. Wood _et al._, “Ethereum: A secure decentralised generalised transaction ledger,” _Ethereum project yellow paper_, vol. 151, 2014.

[40] M. Rosenfeld, “Analysis of hashrate-based double spending,” _CoRR_,
vol. abs/1402.2009, 2014.

[41] J. A. Frankel, “No single currency regime is right for all countries or
at all times,” _Essays in International Finance_, vol. 215, 1998.

[42] Misc., _Stasis whitepaper_ [, https://www.docdroid.net/QdCqGO9/stasis-](https://www.docdroid.net/QdCqGO9/stasis-white-paper-2.pdf)
[white-paper-2.pdf, visited on 2018-07-16.](https://www.docdroid.net/QdCqGO9/stasis-white-paper-2.pdf)

[43] - —, _Trusttoken whitepaper_ [, https://thetoken.io/TKN- WhitePaper-](https://thetoken.io/TKN-WhitePaper-en_US.pdf)
[en US.pdf.](https://thetoken.io/TKN-WhitePaper-en_US.pdf)

[44] - —, _Synthetix whitepaper_ [, https : / / havven . io / uploads / havven](https://havven.io/uploads/havven_whitepaper.pdf)
[whitepaper.pdf, visited on 2018-07-16, 2018.](https://havven.io/uploads/havven_whitepaper.pdf)

[45] S. Fischer, “Exchange rate regimes: Is the bipolar view correct?”
_Journal of economic perspectives_, vol. 15, no. 2, 2001.

[46] J. Williamson and T. H. Moran, _Exchange rate regimes for emerg-_
_ing markets: Reviving the intermediate option_ . Peterson Institute for
International Economics, 2000.

[47] B. Eichengreen and R. Hausmann, “Exchange rates and financial
fragility,” in _Proceedings - Economic Policy Symposium_, 1999.

[48] B. Eichengreen, A. K. Rose, and C. Wyplosz, “Speculative attacks on
pegged exchange rates: An empirical exploration with special reference
to the european monetary system,” National Bureau of economic
research, Tech. Rep., 1994.

[49] A. Crockett _et al._, “Monetary policy implications of increased capital
flows,” in _Changing Capital Markets: Implications for Monetary_
_Policy_, Citeseer, 1994.

[50] P. Krugman, “A model of balance-of-payments crises,” _Journal of_
_money, credit and banking_, vol. 11, no. 3, 1979.

[51] M. Obstfeld, “Models of currency crises with self-fulfilling features,”
_European economic review_, vol. 40, no. 3-5, 1996.

[52] M. Obstfeld and K. Rogoff, “The mirage of fixed exchange rates,”
_Journal of Economic perspectives_, vol. 9, no. 4, 1995.

[53] B. Eichengreen, “The ems crisis in retrospect,” Social Science Research
Network, SSRN Scholarly Paper, 2000.

[54] A. Harmes, “The trouble with hedge funds,” _Review of Policy Research_,
vol. 19, no. 1, 2002.

[55] M. A. Bhundia and M. M. R. Stone, “A new taxonomy of monetary
regimes,” International Monetary Fund, Tech. Rep., 2004.

[56] F. S. Miskin, _Monetary policy strategy_ . MIT Press, 2006.

[57] M. Friedman, “Quantity theory of money,” _The new Palgrave dictio-_
_nary of economics_, 2017.

[58] I. Fisher, “The equation of exchange 1896-1910,” _The American_
_Economic Review_, vol. 1, no. 2, 1911.

[59] B. S. Bernanke, T. Laubach, F. S. Mishkin, and A. S. Posen, _Inflation_
_targeting_ . Princeton University Press, 1999.

[60] F. Glaser, K. Zimmermann, M. Haferkorn, M. Weber, and M. Siering,
“Bitcoin – asset or currency? revealing users’ hidden intentions,” _SSRN_,
vol. abs/2425247, 2014.

[61] B. T. McCallum, _Credibility and monetary policy_, 1984.

[62] - —, “Issues in the design of monetary policy rules,” _Handbook of_
_macroeconomics_, vol. 1, 1999.

[63] A. T. Levin, V. Wieland, and J. Williams, “Robustness of simple
monetary policy rules under model uncertainty,” in _Monetary policy_
_rules_, University of Chicago Press, 1999.

[64] B. T. McCallum, “Robustness properties of a rule for monetary policy,”
in _Carnegie-Rochester conference series on public policy_, Elsevier,
vol. 29, 1988.

[65] F. Larra´ın and A. Velasco, “How should emerging economies float
their currencies?” _Economics of Transition_, vol. 10, no. 2, 2002.

[66] M. Goldstein, _Managed floating plus. policy analyses in international_
_economics_ . Peterson Institute for International Economics, 2002.


