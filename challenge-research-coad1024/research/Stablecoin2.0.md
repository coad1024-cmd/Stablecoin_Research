## **Stablecoins 2.0: Economic Foundations and Risk-based Models**

Ariah Klages-Mundt Dominik Harz Lewis Gudgeon
Cornell University Imperial College London Imperial College London


Jun-You Liu Andreea Minca
Cornell University Cornell University



**ABSTRACT**


Stablecoins are one of the most widely capitalized type of cryptocurrency. However, their risks vary significantly according to
their design and are often poorly understood. We seek to provide a
sound foundation for stablecoin theory, with a risk-based functional
characterization of the economic structure of stablecoins. First, we
match existing economic models to the disparate set of custodial
systems. Next, we characterize the unique risks that emerge in noncustodial stablecoins and develop a model framework that unifies
existing models from economics and computer science. We further
discuss how this modeling framework is applicable to a wide array of cryptoeconomic systems, including cross-chain protocols,
collateralized lending, and decentralized exchanges. These unique
risks yield unanswered research questions that will form the crux

- f research in decentralized finance going forward.


**KEYWORDS**


Stablecoins, Risk, Governance, Capital Structure Models, DeFi


**ACM Reference Format:**

Ariah Klages-Mundt, Dominik Harz, Lewis Gudgeon, Jun-You Liu, and Andreea Minca. 2020. Stablecoins 2.0: Economic Foundations and Risk-based

Models. In _2nd ACM Conference on Advances in Financial Technologies (AFT_
_’20), October 21–23, 2020, New York, NY, USA._ ACM, New York, NY, USA,
[21 pages. https://doi.org/10.1145/3419614.3423261](https://doi.org/10.1145/3419614.3423261)


**1** **INTRODUCTION**


Stablecoins are cryptocurrencies with an added economic structure
that aims to stabilize their price and purchasing power. There are
two classes of stablecoin: custodial, which require trust in a third
party, and non-custodial, which replace this trust with economic
mechanisms. Major custodial examples such as Tether, Binance
USD, USDC, and TrueUSD have a combined market capitalization

- f over USD 10bn. On the non-custodial side, of the USD 1bn of
value locked in so-called Decentralized Finance (DeFi) protocols,
more than 50% are allocated to Maker’s Dai stablecoin.

Several recent papers and industry reports provide overviews

- f stablecoins [12, 17, 62, 63, 71, 76]. These typically categorize
stablecoins based on the type of collateral used, peg target, and
technological mechanics (e.g., on-chain, off-chain, algorithmic) and


Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation

- n the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
_AFT ’20, October 21–23, 2020, New York, NY, USA_
© 2020 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 978-1-4503-8139-0/20/10...$15.00
[https://doi.org/10.1145/3419614.3423261](https://doi.org/10.1145/3419614.3423261)


|Col1|E|
|---|---|
|||


|Col1|N|
|---|---|
||N|
|||



Bank Fund

Central Bank

|Col1|Fra|
|---|---|
|||


|Col1|Mon|
|---|---|
||o|
|||



**Figure 1: Risk-based overview of stablecoin design space.**


informally relate stablecoin mechanisms to traditional monetary
tools (e.g., interest rates). The history of money and stablecoins,
and the institutional structures of stablecoins are discussed in [51].
The regulatory perspective of stablecoins, including classification,
regulatory gaps, and systemic stability risks are discussed in [1].
In this paper our fundamental aim is different. Market events
have demonstrated that even stablecoins—supposedly price stable—
can exhibit significant volatility. On the 12th March 2020, amidst the
SARS-COV-2 pandemic, market volatility affected the stablecoin
Dai [55] so severely that it entered a deflationary deleveraging
spiral, forcing it to deviate from its peg. While the aforementioned
papers observe and categorize _existing_ stablecoin designs, none of
the works develop risk-based models of a broad design space of
_possible_ choices and their fundamental trade-offs. Here we seek
to fill this gap, providing sound economic foundations to inform
stablecoin design, focusing on financial risk. As such, the work is
intended to serve as a “manual" for future stablecoin research.

Firstly, we provide an overview of the relevant risk-based models
from economics and computer science, seeking to avoid duplication

- f work by only extending models where necessary. Secondly, we
provide a number of formalized open questions drawing on capital
structure theory. Throughout we assume that stablecoin systems are
used and operated by economically rational agents whose actions
ultimately determine the stability and security of these systems.
However, we do not solve the stated open problems in the context of
this paper. This work builds on the previous attacks on decentralized
stablecoins identified in [48].
We uncover five central dimensions of risks. In non-custodial sta
blecoins: (1) effects from deleveraging-like processes on collaterallike assets and risk in underlying collateral-like thing (as discussed,
e.g., in [48, 49]), (2) data feed and governance risks, (3) base layer
risks from mining incentives, and (4) smart contract coding risks,

- n which the formal verification literature can be applied. In contrast, in custodial stablecoins, the first applies in a very different
way to affect issuer incentives as well as an additional central risk
dimension of (5) censorship and counterparty risk. Our stablecoin
mechanism categorization decomposes the design space according



Implicit Collateral


Endogenous Collateral


Exogenous Collateral


Reserve Fund
Money Market Fund

Fractional Reserve Fund



**Stablecoin**



Non-Custodial


Custodial


to these dimensions of risk. Figure 1 summarizes our categorization
along some of the most important dimensions of risk.


**Contributions**


  - We provide a functional breakdown of custodial stablecoin
designs with a correspondence to taxonomy and models for
traditional financial instruments (Section 2).

  - We provide a common functional framework for relating the
economic mechanics of all non-custodial stablecoin designs
and a discussion of new risks that emerge in this setting
(Section 3).

   - We provide questions of economic stability and security that
apply in evaluating non-custodial stablecoins (Section 3).

  - We provide a framework of models toward measuring stability and security including open research questions based on
agents’ decisions (Section 4).

  - We provide methods for estimating agents’ preferences as
represented by utility functions, providing a minimal working example using historical data from Maker (Section 4).

  - Last, we outline how our models can be applied to DeFi
protocols including composite stablecoins, cross-chain and
syntehtic assets as well as lending protocols and decentralized exchanges (Section 5).


**2** **CUSTODIAL STABLECOINS**


In custodial stablecoins, custodians are entrusted with off-chain
collateral assets, such as fiat currencies, bonds, or commodities.
An issuer (possibly the same entity) then offers digital tokens to
represent an on-chain version of a reserve asset (e.g., USD). Holders

- f the digital token have some form of claim against the custodial
assets, which maintains the peg. The custodial assets include _reserve_
_assets_, which are what the stablecoin is pegged against (e.g., USD),
and _capital assets_, which are other assets that back stablecoin supply.
Capital assets are comparable to illiquid assets held by a bank and
short-term treasuries held by money market funds.
Custodial stablecoins introduce coin holders to _counterparty_ and
_censorship_ risks related to the off-chain assets and _economic_ risks

- f the capital assets. These risks are similar to risks in traditional
assets. Counterparty risks may be heightened due to the shared account structure with the custodian and lack of government deposit
insurance. In the event that the central entities are unable to fulfill

their obligations (e.g., the result of fraud, mismanagement, theft, or
government seizure), the stablecoin value can go to zero. Table 1
summarizes categories, applicable models, and projects.


**2.1** **Reserve Fund = 100% reserve off-chain**


In Reserve Fund stablecoins, the stablecoin maintains a 100% reserve
ratio–i.e., each stablecoin is backed by a unit of the reserve asset
(e.g., 1 USD) held by the custodian. The price target is maintained
via two mechanisms. Coins may be directly redeemable off-chain
for the underlying reserve asset. In this case, arbitrage trades incentivize external actors to close any price deviations that occur.
Alternatively, the issuer may designate ‘authorized participants’
(possibly the issuer itself) who alone have the ability to create and
redeem stablecoins against the reserve. In this case, the authorized
participants capture price deviation arbitrage.



Reserve Fund stablecoins resemble the structures of e-money,
narrow banks, and currency boards. E-money is a prepaid bearer
instrument. Deposits at a narrow bank are backed by 100% reserves
held at a central bank. A currency board maintains a fixed exchange
rate of a sovereign currency using 100% reserves in a foreign currency (e.g., the Hong Kong Dollar maintains a USD peg using USD
reserves). Of these, the Reserve Fund stablecoin most closely mirrors the currency board as the market price of the stablecoin floats
subject to creation and redemption similarly to how the sovereign
currency floats subject to creation and redemption of the currency
board. On the other hand, e-money and narrow bank deposits are
treated identically with the currency itself. Notably, unlike the currency board, the stablecoin reserves may be stored in commercial
bank deposit accounts, which may bear bank run risks. We discuss
approaches to modeling Reserve Fund stablecoins in Appendix A.2.


**2.2** **Fractional Reserve Fund**


A Fractional Reserve Fund stablecoin is backed by a mixture of
reserve assets and other capital assets, and has a target price. The
fund holds reserves in a target asset (or other highly liquid stable
assets) that account for _<_ 100% of the stablecoin supply in order
to facilitate stablecoin redemptions. Similar to the Reserve Fund
design, these reserve assets may resemble commercial bank deposits
which exceed the government deposit insurance level, in which
case they may take on commercial bank run risk. The other capital
assets account for the remaining stablecoin supply value and earn
a higher interest rate for the stablecoin issuer. The capital assets
can be liquidated to handle additional stablecoin redemptions, but
are subject to price risk. Within this class, the important dividing
point is the type of capital assets held: illiquid assets (similar to a
commercial bank) or low-risk assets (similar to a money market
fund). In either case, the stablecoin has a floating price, and so the
peg is maintained through similar ETF arbitrage trades involving
fund redemptions. Thus applicable risk models would take the form

- f ETF models in serial with bank run or money market models,
which we discuss next. We provide further detail on each type of
stablecoin in Appendix A.3.


**2.3** **Central Bank Digital Currency**


Central Bank Digital Currency (CBDC) is a consumer-facing fiat digital currency that aims to provide a risk-free store of value. CBDC
proposes a different monetary system to the status quo. Currently,
central bank reserve deposits are available to commercial banks,
but not to consumers or non-bank businesses. Consumers and busi
nesses hold commercial bank accounts. The non-cash money supply
is determined by the lending of commercial banks (see [60]). The
government intervenes in this monetary system to create risk-free
consumer deposit accounts by providing commercial bank deposit
insurance. Instead, CBDC provides consumer-facing deposits at the
central bank. [1]


CBDC represents a change in the structure of money deposits
within the banking system and not a change in the currency stability model itself. In fact, CBDC is in many ways a more ideal
setting for existing currency models as it is closer in form to fiat


1See [7] for a discussion on design and architecture of CBDC. The version comparable
to stablecoins is the token-based design.



2


than commercial bank deposits. Traditional currency models like

[64] and [38] apply to understand the stability of fiat currencies.
These models typically assume that the central bank/government
is stability-seeking for its own sake as opposed to private banks discussed above, which are profit-seeking. A fiat currency is assumed
to have the backing of a given country’s economy, which provides
a natural demand from economic activity in the currency, as well as
military power and legal system. Given this setting, agents in these
models hedge their current positions to account for demand in a
next period, some of which occurs in the fiat currency and other

- f which occurs in a foreign currency, under a potential currency
attack from an attacking agent. The ability to maintain a peg in this
setting will depend on a relationship between reserves held by the
central bank and economic demand.

Research questions around CBDC focus on wider economic effects and indirect effects on stability, such as through commercial
bank lending, credit availability, and funding in the real economy.

[9] models the effects of CBDC on the wider economy through competition with commercial bank deposits. [68] explores the effect of
CBDC on commercial bank lending to the real economy through a
case study analysis of government subsidies.


**3** **NON-CUSTODIAL STABLECOINS**


Non-custodial stablecoins aim to be independent of the societal
institutions that custodial designs rely on. They achieve this by
establishing economic structure between participants implemented
through smart contracts. In this setting, directly confiscating assets
is prevented by the underlying blockchain mechanism.
Non-custodial stablecoins structurally resemble dynamic versions of risk transfer instruments, such as collateralized debt obligations (CDO) and contracts for difference (CFD). [2] CDOs are backed
by a pool of collateral assets and sliced into tranches. Any losses are
absorbed first by the junior tranche; a senior tranche only absorbs
losses if the junior tranche is wiped out.
Functionally, a non-custodial stablecoin system contains the
following components in some form:


  - _Primary value_ : the economic structure of the base value in
the stablecoin. This is an abstracted concept of collateral
with the following types: _exogenous_ when the collateral has
primary outside use cases, _endogenous_ when the collateral
is created for the purpose of being collateral, and _implicit_
when the design lacks explicit collateralization.

  - _Risk absorbers_ : speculative agents who absorb risk and profit

∼
in the system ( the junior tranche of a CDO).

  - _Stablecoin holders_ : agents who make up the demand side of

∼
the stablecoin market ( senior tranche holder of a CDO).

  - _Issuance_ : a function performed by an agent or algorithm that

∼
determines stablecoin issuance ( how levered a CDO is),
including a deleveraging process to reduce stablecoin supply.

  - _Governance_ : a function performed by an agent or algorithm
to manage system parameters, such as deleveraging factors
and price feeds, and collects a fee on system operation (∼ an
equity position in managing CDOs).


2They also resemble perpetual swaps, which are relatively new products on cryptocurrency exchanges.




  - _Data feed_ : a function to import external asset data (e.g., exchange price of assets in USD) into the blockchain virtual
machine so that it is readable by the system’s smart contracts.

  - _Miners_ : agents who decide the inclusion and ordering of
actions in the base blockchain layer (PoW or PoS).

The specific form of components may differ, but the general functions are universal across stablecoin designs. Depending on the
design, several functions may be performed by a single agent type
and others may be algorithmic. Notice that the last three components can be simplified out of traditional financial models because

- f legal protections; in traditional systems, we typically assume
these processes are mechanical as opposed to strategic actions. As
a result, stablecoins are susceptible to new manipulation attacks
around governance, price feeds, and miner-extractable value (MEV).


_Analogy to traditional monetary system._ We provide an illustration between the Maker stablecoin system [3] and the traditional
monetary system to aid the reader in understanding the components and functional differences. In Maker, _vaults_ absorb risk and
perform issuance. Vaults deposit ETH collateral (primary value),
issue Dai secured against this collateral, and invest proceeds from
Dai issuance to achieve a leveraged position. The fiat system contains a central bank, commercial bank, and depositors. The central
bank regulates commercial banks and holds bank currency reserves.
Commercial banks decide the money supply through lending. Depositors hold fiat currency accounts at commercial banks.
Maker vaults are parallel to commercial banks in that they both
they decide money supply based on issuance incentives. For banks,
this depends on profitability of lending, which incorporates the
spread between long-term and short-term rates, subject to balance
sheet and regulatory constraints and depositor withdrawal expectations. Vaults make a different bet collateral leverage. [4] Governance
is parallel to the central bank. The central bank sets rates to target economic stability and capital requirements for banks. Models
typically assume the central bank mechanically targets stability by
mandate. Stablecoin governance takes a different form. Governance
sets rates and collateral factors to maximize system profits, which
we hope to be aligned with stability. Stablecoin holders are parallel
to depositors. Whereas bank depositors are guaranteed deposit redemption, stablecoin holders may have no such guarantee. Instead,
they must hope that system incentives are aligned to make the
stablecoin floating price stable and liquid.
A final useful parallel is in governance attacks. Through setting
system parameters, stablecoin governors could inherently steal the
value locked in the system, something we discuss in the context

- f models in the next section. A parallel attack in the traditional
monetary system would be an infinite printing of money by the
central bank, to the benefit of the government.


**3.1** **Primary Value**


The primary value is an abstract concept of collateral that is the
basis for value in the stablecoin system. It incorporates the value of


3The most capitalized non-custodial stablecoin system as of 10 June 2020.
4Commercial bank money supply is often described as a ‘money multiplier’ based

- n the required reserve ratio. This is only accurate if we assume that banks lend the
maximum allowed by their constraints. This need not be the case that the optimal
lending always has a binding constraint. Similarly, vaults in Maker typically do not
issue stablecoins to the maximum extent of the collateral factor.



3


collateral with explicit market prices and/or non-tokenized value
‘in the system’ coordinated among participants, which we term
_implicit collateral_ . This primary value is derived from market expectations in some system. For exogenous cryptocurrency collateral
(e.g., ETH), this is expectations and ‘confidence’ about Ethereum.
In implicit collateral, it is coordinated ‘confidence’ in the stablecoin
system itself. In comparison, in fiat currencies, this is confidence in
a nation’s government, economy, and legal system. In gold-backed
currencies, it is confidence in gold. [5] In tokenized assets, it may be
confidence in the custodian and expectations about cashflows of
the underlying assets.


_Exogenous collateral._ An exogenous collateral is an asset that
has uses outside of the stablecoin system and for which only a
small portion may be tied up in collateral for the stablecoin. An
example is ETH in Maker. Stablecoins are issued against this collateral subject to a collateral factor that dictates the minimum overcollateralization allowed in the system. From a model perspective,
the prices of exogenous collateral can be modeled exogenously.


_Endogenous collateral._ An endogenous collateral is an asset created with the purpose of being collateral for the stablecoin. This
means that it has few, if any, competing uses outside of the stablecoin system. Examples include SNX in Synthetix (in which issuance
is agent-based) and ‘shares’ in seigniorage shares (in which issuance
is algorithmic) [77]). In seigniorage shares, an ‘equity’-like position insures the system against price risk, absorbing losses when
stablecoin demand is low and the supply needs to be contracted,
and receiving newly minted stablecoins when demand is high and
the supply needs to be expanded. [6] The price of endogenous collateral cannot be modeled exogenously due to endogenous feedback
effects between stablecoin usage and collateral value. Its value is
derived from a self-fulfilling coordination of ‘confidence’ between
its participants.
For instance, in a crisis of confidence, if expectations of stablecoin
holder demand are low, then the value of the endogenous collateral
should be low, which will further shake confidence in the system
and demand. On the other hand, high expectations can be selffulfilling: with high collateral value, the stablecoin is, in a sense,
more secure. If stablecoin holder demand is high, then a high price

- f the endogenous collateral can be justified.
The distinction between exogenous and endogenous collateral
may be best conceptualized as a spectrum. For instance, selected
collateral has outside uses but are significantly intertwined with
the stablecoin (e.g., Steem Dollars) and some stablecoins are backed
by a collateral basket, including both exogenous and endogenous
collateral (e.g., Celo). From a model perspective, this spectrum can
be represented as the strength of these feedback effects.


_Implicit collateral._ Some stablecoin designs do not have explicit
collateral but instead propose market mechanisms to dynamically


5At some level, confidence in _something_ seems unavoidable as a source of value in a
monetary system.
6While, in general, seigniorage shares has a risk absorbing effect, extremes of the idea
(Ampleforth) are really just a twist on a fixed supply cryptocurrency misinterpreted
as a stablecoin. Ampleforth transforms price volatility into supply volatility (e.g.,
daily stock splits) without having an _economically_ stabilizing effect on purchasing
power (though may have a _psychological_ effect). Thus it can be interpreted as akin to
seigniorage shares where all positions are the ‘shares’ and so in fact no positions are
stabilized.



adjust supply to stabilize price. These designs work when speculators can be incentivized to absorb losses when the supply needs
to be decreased by the prospect for rewards when the stablecoin
supply needs to increase. We draw a parallel between the positions

- f such speculators and the endogenous collateral case with important functional differences. Both obtain value from self-fulfilling
coordination of confidence in the stablecoin from usage and speculative expectations between the participants. Endogenous collateral
represents the explicit tokenization of this, including obligation
to absorb losses during supply decreases, which means it has a
directly observable market price. Implicit collateral is not explicitly
tokenized _and_ risk absorbers do not have direct obligations to absorb losses. For modeling, implicit collateral can be interpreted like
endogenous collateral behind-the-scenes and accounting for this
difference in financial structure of risk absorbers. The behind-thescenes ‘market price’ of this coordination will only be indirectly

- bservable in the levels of stablecoin and speculative demand. However, they will play a similar role to endogenous collateral in valuing
both the speculative and stablecoin positions. The stability of both
endogenous and implicit collateral stablecoins will rely on how
participants perceive and coordinate this value over time.
One type includes Basis [2] and NuBits [50]. In these designs
‘shares’ are awarded if stablecoin supply increases, but do not necessarily face direct losses when supply contracts (but, of course,
they do face indirect losses from the share market price). Supply
contraction relies on selling ‘bond’ positions to remove stablecoins
from circulation in return for future rewards when supply is next
increased. In Basis, this is algorithmic, whereas in NuBits, this is
coordinated through share voting (and a couple other stabilization
mechanisms, including share demurrage, are available for voters
to choose from). If we tokenize an obligation to purchase ‘bonds’
during contractions and combine with ‘shares’ positions, then the
result resembles seigniorage shares. As it is not tokenized in this
way, the equivalent of ‘collateral’ is only implicit with no observable market price. Comparatively, seigniorage ‘shares’ ought to
be valued differently to be compensated for extra obligation. And
downside price stabilization will depend on incentives of risk absorbers at the time as opposed to in advance (see [45] for a critique).
We refer to a second type as _miner-absorbed_ (e.g., [33]), which
aims to stabilize the base asset of a blockchain by manipulating
protocol incentives. These designs propose for the supply to be
dynamically adjusted by manipulating mining rewards, mining
difficulty, and the level and burning of transaction fees or interest
charges. This means that miners take an implicit risk absorber
position that is meant to absorb price risk, but without an obligation
to continue mining/risk absorbing. In many ways, this parallels
the Basis/Nubits design. Miners are rewarded with newly minted
stablecoins when the supply needs to be increased and face slashed
rewards and burned transaction fees if they choose to continue
mining when the supply needs to be reduced.


**3.2** **Risk Absorption and Issuance**


The stablecoin mechanism works when speculators are incentivized
to absorb price risk. These risk absorbing positions have two primary forms. In _equity risk absorption_, a secondary asset exists, and
any holder of this asset implicitly absorbs risk from the stablecoin.



4


For instance, the Steem market cap implicitly backs Steem Dollars;
a Steem Dollars holder can redeem Steem Dollars for newly minted
Steem, and all Steem holders bear this inflation cost. In _agent risk_
_absorption_, individual agents manage a vault containing primary
value that absorbs stablecoin risk. In agent risk absorption, agents
decide how much to participate with their asset whereas, in equity
risk absorption, every holder of the secondary asset participates proportionately. In many cases, the risk absorber role is also combined
with stablecoin issuance.

An issuance process determines the stablecoin supply. A lot

- f variation is possible in the process specifics, but there are two
general types. In _agent-based issuance_, the size of the stablecoin
supply, or more specifically the leverage of the system (the size of
the stablecoin supply relative to the collateral value), is decided by
agents in the course of optimizing their positions. The deciding
agents are typically the risk absorbers in the system. For instance,
in Maker, vaults determine their stablecoin issuance in managing
the leverage of their vaults. In NuBits, owners of ‘equity’-like shares
collectively vote on issuance decisions to balance demand.
In _algorithmic issuance_, a process to adjust leverage (relative
supply) is codified in the stablecoin protocol. For instance, in Duo
Network, leverage is determined algorithmically through ‘leverage
resets’, which balance the stablecoin supply relative to collateral
value. In seigniorage shares, new issuance is awarded algorithmically to ‘equity’ holders to balance demand.
A _deleveraging process_ is also part of issuance that can be invoked
to reduce the stablecoin supply if a deleveraging factor is breached,

- r if stablecoin holders are allowed to redeem stablecoins for the

collateral. For instance, in Maker, if the stablecoin issuance of a
vault is too large relative to the collateral value, the collateral is
liquidated to reduce leverage. In Duo Network, ‘leverage resets’
may force the liquidation of some positions if a collateral factor is
breached. In seigniorage shares, losses are born by ‘equity’ holders
to reduce the stablecoin supply in a demand shock. In Steem Dollars,
if price is below target, stablecoin holders may redeem for newly
minted Steem.

As introduced in [48] and [49], non-custodial stablecoins based

- n leveraged lending markets face deleveraging risks, which
can cause feedback spirals on primary value. Most existing noncustodial stablecoins fit this leveraged lending characterization.
These deleveraging risks take two forms. The first is a feedback
effect on the stablecoin market: collateral value may be consumed
faster in liquidations due to drying of stablecoin liquidity. The cost

- f deleveraging in a crisis may be significantly higher than $1 per
stablecoin due to this effect, as predicted in [48] and validated in
Maker during ‘Black Thursday’ in March 2020. The second is a
feedback effect directly on endogenous and implicit collaterals. For
endogenous collateral, liquidations can cause a liquidity and fire
sale effect on the collateral asset market in addition to a feedback

effect on reduced expectations.
A similar feedback occurs in implicit collateral and affects the
risk absorbers’ positions and stablecoin demand. For both types of
implicit collateral, there is a ceiling on how much can be absorbed.
For seigniorage shares, this is in demurrage of equity holders. For
miner-absorbed, this is likely around 0 block reward, except possibly
in staking systems in which stake can be slashed as demurrage. The
result is feedback in the participation incentives and value of the risk



absorbing position. For instance, for miners to be willing to continue
mining without a mining reward, the expectations of future profit
need to outweigh the costs. A continued participation decision
will depend on whether the investment can be repurposed and
potential returns from competing alternatives. After this ceiling, the
remaining flexibility is only in burning of fees charged in stablecoin
usage, which has a feedback effect on the attractiveness of holding
the stablecoins.

This leads to two universal and fundamental questions:


**Question 1** (Incentive Security) **.** Is there mutually profitable continued participation across all required parties?


If not, then the mechanism cannot work as no one will participate.
This question also includes incentives around attacks; in particular,
if incentives lead to profitable attacks, then _rational_ agents will
be less inclined to participate. After this is answered, we can then
make sense of the follow-up question:


**Question 2** (Economic Stability) **.** Do the incentives actually lead
to stable outcomes?


Note that particular feedback effects can be mitigated. However,
the result is typically to shift the risk from one agent to another.
In either case, the risk will affect participation incentives. For instance, in collateral liquidations, some stablecoin holders could be
liquidated at par for the collateral asset as opposed to at a floating
market price. This eliminates the feedback effect on the stablecoin
market price, reducing deleveraging risk on risk absorbers. Instead,
however, the stablecoin may be less attractive to stablecoin holders
as they now take on more liquidation risk.
The type of stablecoin structure will also significantly affect incentives. When designs are more agent-based, agents have greater
decision flexibility and are more likely to find a profitable participation level. In comparison, when designs are more algorithmic and/or
with equity risk absorption, agents are more restricted and may
be less likely to participate in the system relative to alternatives. [7]

Several past stablecoin events serve as case studies for deleveraging
effects. These are described in Table 4 in the Appendix.
Stablecoins can also incorporate other insurance mechanisms
to mitigate risk (e.g., [66, 69, 81]). The simplest is creating a fully
collateralized put option market, from which individual stablecoin
holders can purchase an option to swap from this stablecoin to an
- ther stablecoin/asset. Naturally, this insurance is only as valuable
as the collateral behind it. Other insurance mechanisms add a layer
to the protocol intended to globally buffer against shortfalls—e.g., in
case the ‘dynamic’ part of the CDO structure fails to cover all losses.
In some cases, these can be interpreted as a ‘mezzanine’ tranche
in the CDO-like structure, though this is not completely accurate
as this ‘tranche’ is often unsecured. In particular, many current
stablecoins generate cash flows from fees that are securitized into
governance tokens (e.g., MKR in Maker)). To cover a shortfall situation, the value of future cash flows can be auctioned off by selling
new governance tokens. However, the value of future cash flows
can evaporate in death spiral situations. Alternatively, a portion


7An interesting anecdote is the ‘miracle’ of the Wörgl Experiment. In this experiment,
currency demurrage is purported to stabilize the local economy in a depression by
incentivizing current spending. However, as discussed in [35], this ought to have an
effect on participation incentives, leading to a lower equilibrium price of the demurrage
currency relative to alternatives.



5


- f past fees can be diverted to serve as a buffer to cover shortfalls.
There is in fact a spectrum between these options, in which securitized cash flows can be sold at arbitrary times to maintain an
adequate buffer. [8]


_A design gap: buffers._ This largely unexplored spectrum of options represents a more general design gap: an under-appreciation

- f buffers in stablecoin design. [49] shows that leveraged lendingbased stablecoins can be stable in regions in which the underlying
collateral price process is a submartingale (i.e., the next period expected return is positive) and can break down outside of this. While
there is some concern about the reasonableness of a submartin
gale assumption, it may be more reasonable in a relaxed form, in
which downward movements are transitory (or long-term expected
return is positive). There is little that derivative design can do to
help systems survive aside from transitory downside events. In this
relaxed form, it is important that systems have adequate buffers
so as to survive transitory events; we suggest that many concerns
about the appropriateness of submartingale assumptions can be
translated to concern about adequate buffer size. In this way, we
expect an optimized buffer design can extend regions of stability
for stablecoins, whereas this is largely underexplored in current
designs. [9] Another form of such a buffer is proposed in [49]: vault
insurance that can cushion the effects of deleveraging spirals.
We also suggest that well-designed buffers can expand design
possibilities beyond leveraged lending-based stablecoins. For instance, stablecoin designs with different fundamentals based on
money market fund and currency peg models where the peg is maintained by an internal buffer effect. One example of these ideas is
discussed more in the context of _composite_ stablecoins in Section 5.2
and in [44, 47].


**3.3** **Governance, Mining, and Manipulation**


We now introduce design components that introduce manipulation
potential in the system. In custodial systems, such manipulations
are typically avoided by relying on societal institutions. In contrast,
permissionless systems usually do not offer strong identities, which

- pen up various anonymous attacks that cannot be prevented by
institutions. The precise form of these components affect the size
and scope of attack vectors, but don’t substantially change their
form; thus we focus our discussion on the functional forms that
are important for economic models. We provide a list of historical
manipulation events as case studies in Table 6 in the Appendix.


_Data Feeds._ Non-custodial stablecoins require asset price data
in terms of the target peg (e.g., ETH/USD prices). This data is not
natively accessible on-chain since fiat-cryptocurrency conversions
can only take place on off-chain exchanges. As a result, the stablecoin relies on a mechanism to import this data into the blockchain
virtual machine so that it is readable by the stablecoin smart contracts (also known as an ‘oracle’). As a result, the correctness of the
imported data is not objectively verifiable on-chain, as opposed to


8This can be interpreted similarly to corporate financing decisions around if/when to
raise capital vs. internally finance.
9For instance, Maker has a ‘system surplus’ account that served as a buffer during
Black Thursday. This was not in fact intended as a stability buffer and is typically used
to accrue fees until they reach a size for returning to ‘equity’ holders. Instead, Maker’s
intended buffer is an auction of MKR, arguably at the worst possible times, to cover
shortfalls.



native actions such as intra-blockchain transaction validity or interblockchain transaction validity [83]. There are various methods,
both centralized and decentralized, to construct such data feeds.
We give a brief overview of these in the appendix. Though, from a
functional standpoint, we can abstract from the technical details to
focus on the economic structure that these data feeds add.

Data feeds introduce a new incentive problem: if importing data
into the system has an extractable value X, then an attacker will
spend up to X to manipulate that data. Centralized feeds can be
manipulated by the counterparty, which introduces potentially
perverse incentives for the counterparty as well as single points

- f failure. Decentralized methods typically collapse in the face of
game-theoretic attacks. As a result, data feeds add an inherent manipulation potential into our general model. _The important factors_

_of this include who can manipulate the feed, how much the feed can_
_be manipulated, and the cost involved in such manipulation._ Given
this, a reasonable aim is to achieve data feed incentive compatibility
to report honestly in the combined data feed-stablecoin system.


_Governance._ Stablecoin governance is tasked with managing system parameters, such as interest rates, collateral factors, data feed
curation, time delays, system upgrades, and emergency system settlement. In return, they typically receive some fee revenue from the
system. Governors may take the form of governance token holders
who vote on parameters, the founding company, a subsumed role

- f other agents in the system, or may be algorithmic.
If it is performed by agents, then these agents have power to
manipulate the system through these parameters. For the system to
be secure, governance must be disincentivized from fatally attacking the system. The potential for profitable attacks will feedback
into the participation decisions of the other agents in the system.
For instance, if governance is tokenized, then the token valuation/expectations, which could be slashed after an attack, and any

- ther costs must be sufficiently higher than the proceeds of the
attack. We discuss several attacks, involving manipulations of data
feeds and parameters to extract collateral value, in the context of
proposed models in the next section.
Governance is also inter-related with system stability. In this
anonymous setting, governance can be expected to maximize expected profits as opposed to targeting stability for its own sake, as
is typically assumed in central bank models. It is an open question
to what extent various governance structures align incentives with
the targeting of stability.
On the other hand, if governance is algorithmic, the stablecoin
may be susceptible to gaming attacks from the other participants.
These attacks can take a related form assuming the governance
algorithm as given and construct similar end results: e.g., bribe the
chosen data feeds in order to extract system value. Potential profitability of these attacks will feedback into participation incentives

- f the agents in the system.


_Miners._ A non-custodial stablecoin is implemented in a base
blockchain layer. This can either be “on top” of a blockchain in the
form of smart contracts or directly into the core runtime. In either
case, the base blockchain is maintained by a set of miners. In this
paper, we subsume both miners (typically used in the context of
PoW) and validators (typically used in PoS) under the term “miner”.
In maintaining the blockchain, miners decide transaction inclusion



6


and ordering in the ledger–both in the next block mined and in
the previous blocks, as a miner could always choose to re-mine an
earlier block to change the transaction structure. Hence, they have
full control over the history of the ledger.
The blockchain system _intends_ for miners to ensure desired properties of persistence and liveness of the ledger [32]. In this context
persistence states that a valid transaction included in the ledger is
eventually considered final, i.e., all honest agents will report the
transaction in the same position in the ledger. The liveness property
requires that a transaction sent from an honest agent is eventually
inserted into the ledger. In return, miners are paid a rewards in
the form of fees for including transactions into blocks and block
rewards for extending the ledger with new blocks. Since present
and future rewards are typically paid out in the base asset, miners
have an incentive to avoid attacks that jeopardize these rewards.
However, miners can also receive payoffs from other sources

- utside of the blockchain protocol. For instance, miners can capture
arbitrage opportunities in the exchange of assets on the ledger or
by placing bets and manipulating the outcomes in the course of
mining, or receiving bribes to do so on behalf of others [59]. This
is broadly summarized as Miner Extractable Value (MEV) [26]. A
rational miner will decide profit-maximizing actions taking MEV
into account, which may not always be honest mining supporting
the blockchain. If MEV is valuable enough, miners will generally
be incentivized to capture it through an attack.
MEV poses a few risks in the context of stablecoins. First, specialized attacks are possible that exploit stablecoin deleveraging events
and liquidations [48]. This leads to MEV opportunities that can
incentivize destabilizing attacks on the stablecoin. Understanding
security and incentive alignment in this context and game theoretic
interaction of many stablecoin agents and miners remain open problems. Second, miner attacks pose consensus risk to the blockchain
layer (e.g., affecting persistence). An attack of this form could have
an effect on the base asset of the blockchain, which may be a collateral asset in the stablecoin. This can have an effect on stablecoin

stability even if the stablecoin itself is not the focus of the attack.
Third, in the case of stablecoins embedded in the base protocol,
the stablecoin may directly manipulate miner reward incentives,
as opposed to indirectly manipulating incentives via MEV. This
presents a related open problem of whether such blockchains can
function (e.g., whether liveness is achievable).


_Miscellaneous risks._ We briefly mention two other risks. One
is often called ‘smart contract risk’. Since stablecoin systems execute algorithmically without specific institutional oversight, they
face the risk of bugs in their specification and implementation–
e.g., transaction-ordering dependencies, overflows, and re-entrancy.
These risks may be representable in similar ways to credit risk
models by introducing some probability of ‘default’, in this case
a software bug, and some random recovery ratio. Formal verification methods are typically used to mitigate these risks. Another
risk is contagion risk from other protocols. In real environments,
these systems do not occur in isolation. For instance, cascading
liquidations in ETH and BTC between multiple leverage platforms

- ccurred on ‘Black Thursday’ in March 2020. We suggest that cascading liquidations like this can be modeled using fire sale models

- f networks of common asset holdings (e.g., [14]).



**4** **MODELS AND MEASURES OF**

**NON-CUSTODIAL STABLECOINS**


Based on the novel risks in non-custodial stablecoins, existing financial models cannot be used ‘out-of-the-box’. Here we introduce foun
dational models for non-custodial stablecoins which adequately
capture these risks. First, we draw inspiration from capital structure models, extending a basic model to capture additional aspects
and formulate four formal examples of such problems. Second, we
consider forking models, moving from the single-shot nature of the
capital structure models we present to games of multiple rounds.
Third, we provide a brief review of models that focus on whether
non-custodial incentive structures can lead to stable price dynamics.
Finally, we include an estimation of utility functions specifically
for the Maker protocol.


**4.1** **Capital Structure Models**


We draw inspiration from capital structure models ([29], [67]) to
understand incentives and attacks in stablecoins. The original formulation of these models describe incentives in an IPO offering
between equity holders, bond holders, and managers. In the stablecoin adaptation, the model describes incentives between governors
who hold governance tokens (∼ equity), stablecoin holders (∼ bond

∼
holders), and vaults/risk absorbers ( managers). We relate vaults
to managers as vaults decide the stablecoin supply.
We consider three assets: COL (collateral asset, e.g., ETH), GOV
(governance token), and STBL (stablecoin). In Problems 1-2, we consider vaults endowed with COL, governors endowed with GOV, and
stablecoin holders who purchase STBL. In Problem 3, we consider
a different formulation in which agents choose portfolios of assets,
including strategic holdings of GOV. We define the following model
components


  - _𝑁_ = dollar value of vault collateral (COL position)

  - _𝑅_ = random return rate on COL

  - _𝐹_ = total stablecoin issuance (debt face value)

  - _𝑏_ = return rate on a new opportunity; vault issues stablecoins
(raises debt) to pursue this

  - _𝛽_ = collateral factor

  - _𝛿_ = interest rate paid by vault to issue STBL

  - _𝑢_ = vault’s utility from an outside COL opportunity

  - _𝑈_ (·) = stablecoin holder’s utility function

  - _𝐵_ = STBL market price at issuance

  - _𝑃𝑡_ = GOV market value at model time _𝑡_ with terminal valuation parameter _𝜅_ .

The model proceeds in three stages: (0) governance decides interest rate _𝛿_ (i.e., the contract with the vault), (1) vault decides
stablecoin issuance leveraged against a collateral position, and (2)
the system is settled with an attack occurring if profitable. In a
simplest formulation, the vault and governance are assumed to
maximize expected value (risk neutral), and the stablecoin holder
has risk averse utility _𝑈_ with unlimited demand depth at this utility,
which we later relax.

The three model stages lead to a sequence of GOV token prices

[ _𝑃_ 0 _, 𝑃_ 1 _, 𝑃_ 2]. In the simplest form, these represent discounted cash
flows accruing to governance given the information at each time.
Note that which _𝑃𝑡_ appear in an optimization problem will depend

- n the precise problem setting we model. _𝑃_ 0 is the objective that



7


governors optimize in period 0. _𝑃_ 1 gives the GOV valuation after
vaults and stablecoin holders strategically participate in GOV ownership (e.g., in Problem 3). _𝑃_ 2 gives the GOV valuation at the end

- f the model. Conditioned on no attack taking place, _𝑃_ 2 = _𝛿𝐹_ + _𝜅_,
where _𝜅_ is a terminal valuation parameter. If an attack occurs, then
we assume participants abandon the system yielding _𝑃_ 2 = 0. The
terminal valuation _𝜅_ represents the growth potential of the stablecoin: for instance, if _𝐹_ becomes large in the future, then GOV
cashflows _𝛿𝐹_ become large as well.


_4.1.1_ _Problem 1: Capital structure with no attack._ Problem 1 introduces a simple setup with no attacks. This resembles the classic
capital structure problem (and can be solved similarly to [29]) with
a particular form of contract between the equity and manager: now,
vaults receive all profits from leverage with an interest fee paid to
governance. The governance choice problem is to maximize the
expected fee revenue subject to the vault’s stablecoin issuance. The
vault choice problem is to maximize expected returns from leverage
minus fees subject to these constraints: (1) the collateral constraint,
(2) the participation constraint, (3) stablecoin market price as the
stablecoin holder’s expected utility of holding one stablecoin.
Notice that, for simplicity, there are several limitations to the
model as formulated. In a more complete model, the vault may
account for collateral liquidation costs (as in [49]) and last-resort
insurance roles of GOV to make up for any collateral shortfalls
(which can be accounted for by adding terms of −[ _𝐹_ (1 + _𝛿_ ) − _𝑁_ (1 +
_𝑅_ )] [+] to the governance objective and modifying the stablecoin
pricing constraint). Some stablecoins also include an interest rate
paid to or by stablecoin holders. Finally, notice that both the setups
with sequential choices by the vault and the governance as well as
concurrent choices are realistic.


**Problem 1** Capital structure with no attack vectors


**Governance choice**


max E _𝛿𝐹_ + _𝜅_
_𝛿_ ∈[0 _,_ 1) ~~�~~              

s.t. _𝐹_ is vault choice


**Vault choice**


max E[ _𝑁𝑅_ + _𝐹_ ( _𝐵𝑏_       - _𝛿_ )]
_𝐹_ ≥0


s.t. _𝐹_ ≤ _𝛽𝑁_


_𝑢_ ≤ E[ _𝑁𝑅_ + _𝐹_ ( _𝐵𝑏_          - _𝛿_ )]


1
_𝐵_ = E _𝑈_

                   -                    - _𝐹_ [min][(] _[𝐹, 𝑁]_ [(][1][ +] _[ 𝑅]_ [) −] _[𝛿𝐹]_ [)]                    - �


_4.1.2_ _Problem 2: Capital structure with governance attack._ We consider a governance attack vector of the form described in [86] and

[37]. In such an attack, an agent with a _𝜁_ fraction of GOV tokens is
able to steal _𝛾_ fraction of collateral in the system. As described in

[86], this could occur in the Maker system at the time with _𝜁_ = 0 _._ 1
and _𝛾_ = 1 (or possibly _𝛾_ _>_ 1 after accounting for simultaneous
attack on other systems using the stablecoin) because governance
is granted the power to arbitrarily alter the contracts. [10]


10Note that governance attacks like this can be mitigated by limiting the contract
structure governance can alter and implementing long time delays between changes,
but it is a realistic attack vector in currently deployed systems that build in broad
contract upgrade capability. The structure of the formal problem can also be altered
by tailoring emergency settlement triggers.



This attack is profitable if the proceeds exceed the costs:


_𝛾𝑁_ (1 + _𝑅_ ) _> 𝜁_ ( _𝛿𝐹_ + _𝜅_ ) + _𝛼,_


where _𝛼_ incorporates an outside cost to attack and _𝜁_ ( _𝛿𝐹_ + _𝜅_ ) is
the opportunity cost of attack (the value of _𝜁_ fraction of GOV
tokens). Note that in traditional financial settings, we typically
have _𝛼_ _>> 𝛾𝑁_ : _𝛼_ represents a high cost due to legal/reputational
recourse. This simplifies the problem to Problem 1 as the attack is
always unprofitable.
In the Problem 2 setting, the governors split into two groups:
attack and non-attack groups. If we think of individual governors
having individual _𝛼_ costs to attack, then the attack group will form
from the _𝜁_ fraction with lowest _𝛼_ . If we take _𝜁_ _<_ 0 _._ 5, then the
non-attack group will decide interest rate _𝛿_ while the attack group
will decide _𝑑_ ∈{0 _,_ 1} whether to attack. If _𝜁_ _>_ 0 _._ 5, then the attack
group decides both _𝛿_ and _𝑑_ . Problem 2 models the case of _𝜁_ _<_ 0 _._ 5:
the governance choice problem represents the non-attack group
decision over _𝛿_, and the attack group decision is represented by the
1 _𝑑_ constraint. Note that a simple reformulation of the governance

- bjective would model the case of _𝜁_ _>_ 0 _._ 5.
The vault decision is expanded to include the amount of collateral
_𝑁_ locked in the stablecoin subject to an amount _𝑁_ [¯] available to
the vault; the amount locked is subject to seizure by a governance
attack. This compares to Problem 1, in which all vault COL is locked
since there is no attack vector (the previous _𝑁_ is the new _𝑁_ [¯] ). For
simplicity, the setup assumes that _𝛾_ is such that, under a successful
attack, no collateral is recoverable by the vault after accounting for
_𝐹_ ; this could be relaxed with an extra term in the vault’s objective.
As an extension to Problem 2, _𝛼_ could also incorporate a bribe
decision from the vault to governance to change attack incentives.


**Problem 2** Capital structure with governance attack vector


**Governance choice**


max E (1 − _𝑑_ ) _𝛿𝐹_ + _𝜅_
_𝛿_ ∈[0 _,_ 1) ~~�~~           -           - �

s.t. _𝑑_ = 1 ( _𝛾𝑁_ (1+ _𝑅_ ) _>𝜁_ ( _𝛿𝐹_ + _𝜅_ )+ _𝛼_ )

_𝐹_ is vault choice


**Vault choice**


max E[( _𝑁_ [¯]    - _𝑁_ ) _𝑅_ + (1 − _𝑑_ ) _𝑁𝑅_ + _𝐹_ ( _𝐵𝑏_    - _𝛿_ ) − _𝑑𝑁_ (1 + _𝑅_ )]
_𝑁,𝐹_ ≥0


s.t. _𝐹_ ≤ _𝛽𝑁_


1 ( _𝑁_ _>_ 0) _𝑢_ ≤ E[ _𝐹_ ( _𝐵𝑏_       - _𝛿_ ) − _𝑑𝛾𝑁_ (1 + _𝑅_ )]


1
_𝐵_ = E       - _𝑈_       - _𝐹_ [min]       - _𝐹,_ (1 − _𝛾𝑑_ ) ( _𝑁_ (1 + _𝑅_ ) − _𝛿𝐹_ )���

_𝑑_ = 1 ( _𝛾𝑁_ (1+ _𝑅_ ) _>𝜁_ ( _𝛿𝐹_ + _𝜅_ )+ _𝛼_ )

0 ≤ _𝑁_ ≤ _𝑁_ [¯]


In Problem 2, incentive alignment against attack (security) will
depend critically on _𝜅_ and _𝛼_ as it’s unrealistic for _𝛿𝐹_ to be on the

- rder of _𝑁_ (∼ 100% interest rate). In a long-run growth equilibrium
_𝜅_ will be related to the geometric sum ~~1~~ _[𝛿𝐹]_ ~~−~~ ~~_𝑟_~~ [for some discount fac-]

tor _𝑟_ . This allows us to understand the settings in which long-run
incentive security will depend on a large _𝛼_ term, which equates to
centralized recourse. In particular, combining the conditions for a
non-attack decision with the collateral constraint, we need _[𝛾][𝑟]_

_𝜁𝛿_ _[<][ 𝛽]_
to have incentive security against attack with _𝛼_ = 0, which is very



8


limiting for practical values of these quantities. Notice that, if incentive security is lacking or the opportunity is not profitable enough
for the vault, an equilibrium can be no participation from the vault
(in which case 1 ( _𝑁_ _>_ 0) = 0 in the utility threshold constraint).
We can interpret this as a ‘price of anarchy’ concept. In this case,
we may want to measure the ratio between the ‘best decentralized
equilibrium’ and the optimal ‘centralized’ solution (e.g., when _𝛼_ _>>_
0 simplifies the setting to Problem 1). A natural task of a protocol
designer would be to optimize this cost.


_4.1.3_ _Problem 3: Portfolio selection with collusion attack._ We now
consider a collusion attack vector of the form described in [46].
For instance, a group that controls a large share of GOV (e.g., 51%,
though possibly lower) can manipulate price feeds and settle the
system such that stablecoin holders or vaults have claim to greater
share of collateral. If the group also holds the profitable position
(e.g., stablecoins), then the attack can be profitable unless the GOV
token holds adequate market value. These 51%-style attacks can’t
inherently be mitigated. [11]

We model these attacks in a more complex setting; a full formal
setup is in Appendix Problem 3. In this setting, vaults and stablecoin
holders are endowed with a value and choose a portfolio of available
assets, some of which entail participation in the stablecoin system
and are subject to attack. They may strategically bid up the price

- f GOV to secure the system or acquire GOV and/or issue a bribe
to try to trigger a instigate a profitable attack. A third agent is an

- utside GOV holder who may choose to collude with other agents.
These agents make the following strategic decisions:


  - Vault decides portfolio x allocated between COL and GOV,
level of participation in the stablecoin _𝑁_ and _𝐹_, and bribe
factor _𝛾𝑣_ to the outside governors.

  - Stablecoin holders decide portfolio y allocated between
STBL, GOV, and COL and bribe factor _𝛾𝑠_ to the outside gov
ernors.

  - Outside governors hold _𝜀_ fraction of GOV, decide interest
rate _𝛿_ and decide whether to collude with the vault ( _𝑑𝑣_ ), the
stablecoin holder ( _𝑑𝑠_ ), or whether no attack occurs ( _𝑑𝑛_ ).


The offered bribes are a _𝛾𝑣_ and _𝛾𝑠_ fraction of attack profitability.
An attack is profitable if _𝜁_ fraction of governance collude (e.g.,
a threshold to manipulate the price feed)–we can generally take
_𝜁_ ≥ 0 _._ 5, but could be lower if collusion with miners is added in.
The portfolios x _,_ y have components measured in dollar value and
which sum to the total endowed values ¯ _𝑥,_ ¯ _𝑦_ .
The COL market is assumed to be perfectly liquid at the given
price, and so portfolio decisions have no price effect on COL.
We restrict the focus to modeling endogenous prices of GOV
and STBL. The price of GOV is determined through the function
_𝑃_ (x _𝐺,_ y _𝐺,𝛿, 𝐹_ ); we assume this = E[ _𝛿𝐹_ + _𝜅_ ] without vault or stablecoin holder participation in the GOV market. In the model, _𝑃_ 2 = _𝑃_ 1
conditional on no attack. If an attack occurs, then GOV price goes
to zero. The STBL price is determined through the function _𝐵_ ( _𝐹,_ y _𝑆_ )
in a way that balances supply and demand. Since the stablecoin
holder has an endowed value in this problem, we no longer assume


11Common mitigations include governance delays and maximum governance changes,
but these are only effective to a certain extent. As discussed in [46], once there is a
profitable coalition, they can wait out any time delays–e.g., vaults are not able to exit
if they can’t buy back the stablecoins.



the STBL market demand has an unlimited depth at a given utility
value, as done in the previous formulations. The behavior of this
model will likely depend largely on the choice of functions _𝑃, 𝐵_ . A
number of choices could be explored to consider different market

structures.


**Problem 3** Portfolio selection with collusion attack vector


**Outside governance choice**

_𝛿_ ∈[0 _,_ 1) _,𝑑_ max{ _𝑛,𝑣,𝑠_ }∈{0 _,_ 1} E ~~�~~ _𝑑𝑛𝜀_ ( _𝛿𝐹_ + _𝑃_ 1) + _𝑑𝑣_ - _𝛾𝑣_ ( _𝐹_ - x _𝐺_ ) − _𝛼_ 
+ _𝑑𝑠_             - _𝛾𝑠_ ( _𝑁_             - y _𝐺_ ) − _𝛼_             - [�]


s.t. _𝑃_ 1 = _𝑃_ (x _𝐺_ _,_ y _𝐺_ _,𝛿, 𝐹_ )



+ _𝑑𝑠_ (1 − _𝛾𝑠_ ) ( _𝑁_          - y _𝐺_ )��

s.t. 1 _[𝑇]_ y = ¯ _𝑦_


_𝐵_ = _𝐵_ ( _𝐹,_ y _𝑆_ )


_𝑃_ 1 = _𝑃_ (x _𝐺_ _,_ y _𝐺_ _,𝛿, 𝐹_ )


_𝛿,𝑑,_ x _, 𝑁, 𝐹_ from outside governor and vault choices


Compared to Problem 2, the vault now decides the amount of
COL to hold (x _𝐶_ ), equivalent to previous _𝑁_ [¯] ) and, of that amount,
the amount to lock as collateral in the stablecoin ( _𝑁_ ). Similarly,
x _𝐺,_ y _𝐺_ represents the amount of GOV in the vault and stablecoin
holder portfolios respectively. We now have three attack decision
variables ( _𝑑𝑛,𝑑𝑣,𝑑𝑠_ ), precisely one of which will take the value
1. The logic for this is encoded in the 2nd-4th constraints of the

- utside governance choice problem.


_4.1.4_ _Problem 4: Miner-absorbed mechanism._ The miner-absorbed

system is a variation of the presented problems as it explicitly
models miners as the core participants. The miner-absorbed stablecoin includes two agents: _Miners_ taking the role of risk absorbers,
governance and miners as well as _stablecoin holders_ . Further, the
system includes an algorithmic _issuance_ role (i.e., part of the base



~~_𝑃_~~ _𝐺_ 1 [≥] _[𝜁]_ [)][ ≤] _[𝑑][𝑣]_ [≤] [1] [(] _[𝜀]_ [+] [x] ~~_𝑃_~~ _[𝐺]_ 1

~~_𝑃_~~ _𝐺_ 1 [≥] _[𝜁]_ [)][ ≤] _[𝑑][𝑠]_ [≤] [1] [(] _[𝜀]_ [+] [y] ~~_𝑃_~~ _[𝐺]_ 1



1 ( x ~~_𝑃_~~ _𝐺_ 1

1 ( y _𝐺_



~~_𝑃_~~ 1 [≥] _[𝜁]_ [)]


_[𝐺]_

~~_𝑃_~~ 1 [≥] _[𝜁]_ [)]



_𝑑𝑛_ = (1 − _𝑑𝑣_ ) (1 − _𝑑𝑠_ ) and _𝑑𝑣_ = (1 − _𝑑𝑛_ ) (1 − _𝑑𝑠_ )

x _,_ y _, 𝑁, 𝐹,𝛾𝑣,𝛾𝑠_ from vault and stablecoin holder choices


**Vault choice**


max E x _𝐶_ _𝑅_ + _𝐹_ ( _𝐵𝑏_   - _𝛿_ ) + _𝑑𝑛_ x _𝐺_ ( _𝛿𝐹_ + _𝑃_ 1)
x _,𝑁,𝐹_ ≥0 _,𝛾𝑣_ ∈[0 _,_ 1) - _𝑃_ 1

+ _𝑑𝑣_ (1 − _𝛾𝑣_ ) ( _𝐹_           - x _𝐺_ ) − _𝑑𝑠_ _𝑁_           
s.t. 1 _[𝑇]_ x = ¯ _𝑥_

0 ≤ _𝑁_ ≤ x _𝐶_

_𝐹_ ≤ _𝛽𝑁_

1 ( _𝑁_ _>_ 0) _𝑢_ ≤ E       - _𝐹_ ( _𝐵𝑏_       - _𝛿_ ) + _𝑑𝑛_ x _𝑃𝐺_ 1 ( _𝛿𝐹_ + _𝑃_ 1)

+ _𝑑𝑣_ (1 − _𝛾𝑣_ ) ( _𝐹_           - x _𝐺_ ) − _𝑑𝑠_ _𝑁_           
_𝐵_ = _𝐵_ ( _𝐹,_ y _𝑆_ )


_𝑃_ 1 = _𝑃_ (x _𝐺_ _,_ y _𝐺_ _,𝛿, 𝐹_ )


_𝛿,𝑑,_ y from outside governor and stablecoin holder choices


**Stablecoin holder choice**



y _𝑆_
y _,𝛾𝑠_ max∈[0 _,_ 1) E ~~�~~ _𝑈_ ~~�~~ y _𝐶_ _𝑅_ + _𝑑𝑛_ - min - _𝐵_



_𝑆_

_𝐵_ _[, 𝑁]_ [(][1][ +] _[ 𝑅]_ [) −] _[𝛿𝐹]_ - + [y] _𝑃_ _[𝐺]_




_[𝐺]_

( _𝛿𝐹_ + _𝑃_ 1)
_𝑃_ 1 


9


blockchain consensus protocol). The primary value in a minerabsorbed mechanism is implicit collateral. In this problem setting, we assume that miners are risk-neutral, economically rational
agents [12] . Further, we assume that the base blockchain includes a
single currency STBL (i.e. the GOV and COL tokens are not present)
and that it includes a correct and up-to-date price oracle.
We define Problem 4 as follows: Should a miner generate a new
block given an expectation of the rewards _𝑟_ being paid, the return
rate on the rewards _𝑏_ at the market price of STBL _𝐵_ considering the
cost for mining _𝑐_ as well as a long-term confidence in the system
expressed as _𝑃_ 1? In _𝑐_ we subsume all variable and fixed costs for
generating a block. The miner’s decision is expressed by _𝑑_ such
that _𝑑_ = 1 encodes generating a block and _𝑑_ = 0 the opposite.
The stablecoin holder decides to participate in the minerabsorbed systems based on the expected stability of the system
expressed by the utility function _𝑈_ . The stablecoin holder has a
portfolio of assets y. The portfolio consists of two asset: STBL denoted as y _𝑆_ and a second exogenous stablecoin denoted as y _𝐴_ . For
example, this could be a miner-absorbed system like Kowala and
USDC as exogenous system. The stablecoin holder re-balances the
weight of the portfolio from one block (denoted by y0 ) to the next
block (denoted by y1). The decision is based on the price of STBL
expressed by _𝐵_ and the price of the exogenous stablecoin denoted
as _𝐵𝐴_ . Additionally, there is a cost _𝛿_ to acquire STBL. The stablecoin holders portfolio re-balancing has an impact on the price _𝐵_
expressed by the abstract function _𝐵_ ( _𝑟,_ y1 _,𝑑, 𝑃_ 1). If the stablecoin
holder sells significant amounts of his STBL holdings, this should
have a severe implications for the price. Last, we define the abstract
function _𝑃_ (yS _,𝑑_ ) that determines the confidence in the system of
the stablecoin holder. For example, the stablecoin holder could
short-term sell STBL without affecting the long-term confidence in
the system. This is similar to a stablecoin holder using STBL to e.g.,
pay bills but planning to keep using the system in the long-run.
Miner rewards _𝑟_ are adjusted by the issuance algorithm.The
issuance algorithm is left abstract. However, the objective of the
issuance algorithm is to minimize the change in price _𝐵_ . We note
that in a PoW system the reward is constrained such that _𝑟_ ≤ 0 since
the issuance algorithm can in the worst-case pay zero rewards but
not “take-away" existing value. In a PoS system this can be achieved
by slashing PoS miners as well as in seigniorage share systems
were miners additionally hold a risky asset such as COL [77]. The
issuance algorithm takes as inputs the price function, but has to
assume that _𝑑_ = 1. The miner-absorbed problem adopts previous
components and adds new ones as follows:


  - _𝑐_ = cost for mining a block

  - _𝛿_ = cost to obtain a stablecoin

  - _𝑢_ = stablecoin holder’s utility for an outside STBL opportunity

  - _𝑟_ = reward paid in the next block


Given the problem 4, _𝑟_ depends on the the expectation the stablecoin holder has towards the price of STBL _𝐵_ and the subsequent
re-balanacing of the portfolio y. If the stablecoin holder expects
the price stability, he will either increase his holdings of STBL (considering the cost of obtaining expressed by _𝛿_ ) or keep his current


12Non-risk neutral miners could also be observed and are covered for a non-stable
currency in [21]



**Problem 4** Miner choice with no attack vectors


**Miner (governance) choice**


max E _𝑑_ ( _𝐵𝑏𝑟_         - _𝑐_ ) + _𝑃_ 1
_𝑑_ ∈{0 _,_ 1} ~~�~~           

s.t. _𝑑𝑢_ ≤ E[ _𝐵𝑏𝑟_                     - _𝑐_ ]

_𝑟_ is algorithmic issuance


**Stablecoin holder choice**


max E ~~�~~ _𝑈_ (y1 _𝑆_ _𝐵_ + y0 _𝐴_ ∗ _𝐵𝐴_ + (y0 _𝑆_     - y1 _𝑆_ ) _𝐵_ (1 − _𝛿_ ))     y1


s.t. _𝐵_ = _𝐵_ ( _𝑟,_ y1 _,𝑑, 𝑃_ 1)


_𝑃_ 1 = _𝑃_ (y _𝑆_ _,𝑑_ )


**Issuance algorithm**

min _𝑟_ ≥0 | _𝐵_ ( _𝑟,_ y1 _,_ 1 _, 𝑃_ 1) − 1|


holdings. On the other hand, price instability will lead to a reallocation of portfolio weights towards the exogenous stablecoin [13] . We
discuss the changes in portfolio allocation as these lead to more
severe impacts on _𝑟_ .
_Case 1: Increased demand for STBL_ y0S _<_ y1S _._ To keep the price
stable (i.e. min | _𝐵_ () − 1|), the issuance algorithm sets _𝑟_ _>_ 0. In turn,
this increases the total supply _𝐹_ . Assuming that _𝐵𝑏𝑟_ _> 𝑐_, miners
should choose to mine a block such that _𝑑_ = 1. Notably, the issuance
algorithm can increase _𝑟_ to meet any demand by simply increasing
mining rewards. However, there is can still be a problem here: _𝑟_
is directly paid to miners. If miners are not spending STBL such
that it is reallocated to stablecoin holders, even issuing _𝑟_ can lead
to a price increase. Conversely, if _𝑟_ is set too high and miners sell
STBL directly, the price of STBL can decrease. Hence, finding a
price-stabilizing issuance algorithm is non-trivial given that the
portfolio allocation and miner decisions cannot be known a priori.
_Case 2: Decreased demand for STBL_ y0S _>_ y1S _._ In this case, stablecoin holders are selling STBL in favor of an exogenous stablecoin.
The issuance algorithm reduces _𝑟_ in return to limit the increase of
_𝐹_ - r do not increase _𝐹_ at all. However, the problem of paying low
rewards introduces two distinct problems. First, it is possible that
even in the case of _𝑟_ = 0, _𝐵_ will still decrease if there is too much
supply in the market. A short-term price increase might still be
counter-acted if stablecoin holders and miners have long-term confidence in the system expressed by _𝑃_ 1. However, second, without
block rewards, the expected utility for miners is can be negative
since they cost for mining a block _𝑐_ is only compensated with the
long-term confidence _𝑃_ 1. If miners only consider the next block
(without _𝑃_ 1), the liveness of the ledger is sacrificed due to the “Gap
Game" [20, 80]. Even worse, miners could fork the chain with the
most valuable transactions from the previous blocks to continue to
earn rewards. If the liveness of the miner-absorbed system is not
present, it will likely also affect the long-term confidence in the
system for stablecoin holders and miners.
Moreover, if the miner can easily switch between different chains,
they would likely abandon the current stablecoin chain for one that
pays high rewards. One can motivate the miner to stay if the cost for


13We note that we could extend this model with a preference for either STBL or the
exogenous stablecoin. For example, if the stablecoin holder prefers a non-custodial
STBL and his only alternative would be a custodial exogenous stablecoin, we could
increase the preference of STBL.



10


switching is high, e.g., if a miner does not produce blocks in a given
time they are slashed as in PoS systems. However, hard-to-leave also
means hard-to-join: a miner needs to be ensured that his rewards
will be positive in expectation. By adding up-front requirements
like specialized hardware or acquiring certain currency, the rewards
in expectation are minimized by the cost of acquisition as well as

- pportunity cost for maintaining the hardware/stake of coins.


_4.1.5_ _Further variations._


_Endogenous collateral._ We now need to account for the endogenous COL price: the actions of the stablecoin agents will have a
direct price effect on COL if the primary use of COL is within the
stablecoin system. One way is to define the COL price return as
a function of the decision variables and update the vault and stablecoin holder objectives with this price formulation. In this way,
a driving random variable (like _𝑅_ in the exogenous formulation)
describing outside faith in the system would be an input to the
price function in addition to agent decisions. As with the functions
_𝐵, 𝑃_ in Problems 1-2, the precise formulation of this price function
will play an important role in the problem, but we can explore a
number of different market structures. In addition, the governance
and vault roles may be merged into the same position if GOV =
COL. Governance can also be an outside party without an explicit
token–e.g., addresses controlled by the founding company.


_Algorithmic issuance._ When stablecoin issuance is automated by
the protocol, the vault is no longer a player. Instead, the issuance
process becomes a constraint for the remaining players, as in Problem 4. The issuance process will directly affect the value of GOV,
in which case, it may be worth considering a participation decision
in owning GOV (e.g., in a portfolio selection problem). If all COL
is implicitly backing the stablecoin, an insurance role will factor
into a general COL holder’s decision to hold COL, and thus into
the pricing of COL. If GOV = COL, then this all comes down to the
pricing of GOV. In the case that a specific portfolio of COL (and/or

- ther assets) is backing STBL, and not all COL, then a money market model may be useful. Models such as [70] could be adapted to

∼
consider portfolio and last-resort insurance role of GOV ( sponsor
support) in a stablecoin setting with added attack vectors.


_MEV: Miners as additional governance._ Some single period MEV
attacks can be modeled within the capital structure framework by
including miners as a second governance-type agent, who decides
transaction inclusion and ordering. For instance, miners could earn
potential profits from front-running STBL issuance decisions or
from bribes to limit the actions of other agents. For richer MEV
attacks, we describe the adaptation of blockchain forking models
in the next section.


**4.2** **Forking Models**


The capital structure models consider a single time-step: depending

- n the expectations of agents, they will choose to execute certain
actions in the next round. In this section, we extend the models to
explore how multiple rounds of agent decisions can affect stability
and security of stablecoin systems. Specifically, we need to consider
feedback mechanisms between different agents interacting over
multiple rounds. In such a setting, agents adjust their _future_ actions



based on their beliefs of the other agents’ actions and the output

- f the integrated algorithms (e.g., issuance or/and governance).
Moreover, we consider that permissionless ledgers used in noncustodial designs (e.g. Maker) lack finality. Miners are able to re
- rder transactions and re-write history within certain depths of
the ledger [32]. This allows agents to adjust _past_ actions as well [14] .
The resulting forking models are highly complex especially when
considering a combination of a complex non-custodial system like
Maker with a base blockchain like Ethereum.

Below, we consider a simpler formulation with specific couplings
between otherwise separate models of a base blockchain and an
application layer. An output of one layer would serve as exogenous
input to the other layer and vice versa. For instance, the size of
MEV determined in application layer participation feeds back into
incentives for forking attacks in the base layer, which feeds back
into the probabilities of attack in application layer incentives. In
this way, a complex forking model could be simplified into simpler problems that can be solved iteratively to find an equilibrium.
This section is kept informal such that we describe the extensions
required but do not include formal problems.


_Base blockchain._ As explored in the blockchain folk theorem [11],
miners have an incentive to coordinate on the longest chain to increase their success of finding the next block. However, if a miner
is already invested in a fork, the miner decides based on his vested
interest (e.g., accumulated work or committed stake) whether to
switch to a different chain. We need to take these two competing incentives into consideration when arguing about MEV, which serves
as an implicit bribe for miners toward specific chains. A forking
model can explore the success probability of bribing miners based

- n their prior incentives. Instead of modelling all miners with the
same incentives, a forking model considers that miners already mining on a fork will have a higher incentive to take the bribe as they
are invested in a fork. Additionally, the setup in [11] can be extended
by a network game as a stochastic dynamic system [85] or a global
game [65] with noisy observations (e.g., network delay, reward
expectations). Moreover, we can incorporate various assumption

- f risk-appetite of miners [21], selfish mining [31], and the impact

- f block rewards in comparison to transaction fees [20, 80].


_Application layer._ A stablecoin that is built as an application on
top of the base blockchain results in two directions of attack effects.
In one direction, the application layer creates MEV that affects incentives on the base layer. For example, an agent wishing to prevent
a liquidation transaction in Maker could offer a payment in another
token to miners on Ethereum. Additionally, miners themselves are
able to profit from their ability to determine the history of the
ledger by e.g., execution of arbitrage opportunities, “time-bandit attacks”, or oracle manipulation. Prior work on MEV in decentralized
exchanges (DEXs) [26] and data feed issues [30, 84] describe some
effects of this direction. The other direction affects participation
in the application layer. A forking model could model the success
probability of an exogenous bribe within the base blockchain. If
successful, an attack would capture value locked in the stablecoin.
The possibility of such an attack (now or in the future) will have an


14While only miners can directly re-order and decide on the inclusion of transactions,

- ther agents can employ bribing strategies to effectively achieve similar outcomes [59].



11


effect on participation incentives in the stablecoin, similar to the
description in the capital structure models. Stablecoin participation
decisions in turn determine the size of MEV opportunities, which
served as bribe inputs to the base layer model. Incentives created
in the stablecoin system can therefore impact the security of the
base blockchain system and vice versa.


**4.3** **Price Dynamic Models**


We provide a brief review on models that explore the higher-level
problem of whether non-custodial stablecoin incentive structures
can lead to stable price dynamics. A challenge here is in modeling
the feedback effects of agent decisions, as discussed in the previous
section. To illustrate, in the most closely related traditional financial
models, an assumed stable asset is borrowed against collateral,
whereas in the non-custodial stablecoin setting, the ‘stable’ asset
that is borrowed has an endogenous price and/or participation level.
The decisions of the other agents will affect this endogenous price
and participation level of the stablecoin holder.

[49] and [48] construct stochastic models involving endogenous
stablecoin price in exogenous collateral systems, taking into account deleveraging and liquidation actions given imperfectly elastic
stablecoin demand. In this context, they model vault issuance incentives considering that issuance involves taking a leveraged bet on
the collateral asset. They illustrate potential deleveraging feedback
effects on stablecoin markets that lead to stablecoin price appreciation and characterize stable and unstable regions for stablecoins.
As a result, vaults may have to pay above face value to deleverage
in a crisis. This is validated by observed behavior of Dai on ‘Black
Thursday’, and was actually predicted a year before in [48].
There are several open follow-up questions. For instance, evaluating the effect deleveraging events have on stablecoin holder participation incentives (particularly for different designs and relative
to alternatives available to stablecoin holders), exploring strategic
interaction of many vaults, destabilizing effects of attacks such
as in the previously mentioned forking models, and extending to
endogenous collateral models.
A few other papers are applicable to stability of stablecoins. [37]
and [43] model cryptocurrency-collateralized lending platforms.
These do not incorporate feedback effects on the stable asset market,
but do incorporate feedback effects on collateral asset liquidity. [15] A
simpler stablecoin problem involving no feedback effects is modeled
in [15]. Option pricing theory is applied in [18] to value tranches in
a proposed stablecoin using PDE methods, also under no feedback
effects. Some stablecoins have also performed stability analyses
(e.g., [22], [72]), though these are typically limited in scope and
include generous assumptions.


**4.4** **Agents, preferences and attitudes to risk**


Agents’ preferences, and in turn their behavior, are a central object
in stablecoin design. In Appendix A.5, we first describe an framework which can be used to model preferences, and then outline
two methods which can be used to estimate agents’ risk attitudes.
The attainment of a clear understanding of agents’ risk attitudes
would serve to improve protocol design and parameter selection.


15These are similar to models for traditional collateral and debt security markets and
repurchase agreements.



**5** **FROM STABLECOINS TO DEFI**


In this section we discuss a likely implication of our capital structure models. Further, we outline how the modelling framework
presented herein is applicable to other cryptoeconomic systems
including composite assets, cross-chain protocols, synthetic assets,
collateralized lending protocols, and DEXs.


**5.1** **Sustainability of Incentives**


As discussed in the context of our capital structure models, to maintain incentive security long-term, the value of a governance token
may need to be disjoint from system growth. In particular, system
growth rates (in supply, capital locked) are unlikely to be high in a
long-term ‘steady state’ (and may be zero). However, the value of
the governance token, if derived from discounted future fees, may

- nly provide incentive security when the expected growth rates
are high—in essence, when borrowing from the future is possible.
A long-term equilibrium without large future growth expectations
may not be possible with governance token value derived from
fees alone as they may be small with respect to value locked. Instead, other parties to the system may need to hold governance
tokens to bid up governance token market value. This will feedback into participation incentives of these other parties; there is
no guarantee that equilibrium participation exists in this context
either. To illustrate, stablecoin holders may need to hold significant
positions in a risky governance asset in order to secure their stable
positions, which may defeat their purpose in holding the stablecoin.
This leads us to a frustrating impossibility conjecture about many
current systems in the context of our models:


Conjecture 1. _In fully decentralized stablecoins (𝛼_ = 0 _) with (i)_
_multiple classes of interested parties (e.g., risk absorbers vs. stablecoin_
_holders) and (ii) a high degree of flexibility in governance design,_
_no equilibrium exists with long-term participation under realistic_
_parameter values._


An analogy helps to illustrate impossibility of some designs:
if incentive security requires a bank’s equity market value to be
worth multiples of total deposits, then no depositors will participate.
The bank’s _long-term_ P/E ratio would need to be in the 100s or
1000s. The conjecture reinforces the importance of studying mutual
incentives in choosing the right stablecoin design. Note that the

- racle incentive compatibility problem also closely resembles the
stablecoin governance incentive problem. Solving these problems
in a fully decentralized way remains an open problem.
Current solutions implemented by stablecoins essentially centralize governance. This solution relies on a form of institutional
liability and translates into a high _𝛼_ value (e.g., in Problem 2). This
is not necessarily a problem; many traditional financial systems

- perate in this way. This is why banks do _not_ need to be worth
multiples of total deposits. However, we should openly recognize
that this trust line exists and may be vital.


**5.2** **Composite Stablecoins**


So far we have focused on _primary_ stablecoin mechanisms. Another
class of _composite_ stablecoins involves baskets of primary stablecoins to try to further absorb risk. The simplest is an _ETF stablecoin_,



12


which works using the ETF arbitrage mechanism to create/redeem
the composite stablecoin against the basket.
A _DEX stablecoin_ aims to spread risk over the basket while providing an exchange service between the constituents, and so the
basket weights change with exchange demand. DEX stablecoins
take on the risk of liquidity provision to these exchanges. For constant function market maker (CFMM)-based exchanges, this risk is
described in [3, 4]. Other DEX stablecoin designs propose limited
1-to-1 stablecoin swaps. Existing DEX stablecoins bear the risk
that the value of the basket may devolve into the value of the least
valuable constituent(s) (e.g., if an underlying stablecoin fails).
A _CDO composite stablecoin_ segregates stablecoin risk into
tranches. [16] For instance, the basket may have _𝑛_ stablecoins and _𝑛_
tranches. At settlement, the senior tranche holder gets first choice

- f which stablecoin to redeem for while holders of the most junior
tranche picks last. Thus, junior tranche holders bear the risks of first
stablecoin failures and are compensated with interest payments.
This structure introduces a similar participation problem: enough
agents need to be willing to take the different positions given the
equilibrium level of interest payments.
A rainy day fund _RDF stablecoin_, as introduced in [44] and [47],
holds a basket of assets that accrues value to a safety buffer over
time through arbitrage, fees, and other collateral uses. The collateral
basket aims to target 1 USD, whereas the accrued buffer aims to
smooth any asset failures/deviations over time.
Other composite stablecoins may also be possible. The stability

- f all composite stablecoins relies on primary stablecoin failures
not being highly correlated. Table 3 summarizes categories for
composite stablecoins, applicable models, and projects.


**5.3** **Cross-chain and Synthetic Assets**


The foundations in this paper can also apply more broadly to synthetic and cross-chain assets. In Appendix A.6 we explain the relevant differences between these asset types in the present setting,
and set out how our foundations apply.


**5.4** **Lending Protocols and DEXs**


_Lending protocols._ Collateralized lending protocols share a similar structure to non-custodial stablecoins. Our models are easily
adapted to describe such protocols. Lending protocols are simpler
than non-custodial stablecoins in that borrowed assets are exogenous, rather than endogenously created by the protocol. This makes
system time delays more effective protective measures. In the noncustodial stablecoin setting, a vault is not able to deleverage and
exit unless they can repurchase stablecoins. Therefore in the event

- f a governance attack, a system time delay built into the protocol
would likely be ineffective as a (profitable) coalition between stablecoin holders could simply wait out the delay, preventing many
vaults from exiting. In contrast, in the collateralized lending setting, an important security implication of the exogeneity of the
borrowed assets is that it can allow protocol participants to leave a
protocol before a governance attack is fully realized. The typical
borrowed asset either has a much larger market or is a custodial
stablecoin, in which case the vault can always create new stablecoins at par through the issuer to deleverage. A system time delay


16Note the difference from the CDO analogy used to describe primary stablecoins.



could therefore protect participants by allowing them to exit before
many impending governance attacks could be realized. [17]


_DEXs._ Some DEXs directly or indirectly have governance layers. When on the same native blockchain as the deposited assets,
similarly to collateralized lending protocols, a DEX may also permit participants to exit before a governance attack is fully realized.
However, where DEXs operate their own blockchain and control
its governance (e.g., Rune), the ability for participants to exit in an
attack can be fundamentally restricted. In this latter case, incentive security is an important question, and mutual participation of
governance and other participants can be modeled as in our capital
structure models.

For DEXs, fees are proportional to exchange volume while the
potential payout of governance attacks is proportional to liquidity
provider deposits. Therefore a key ratio of interest to protocol designers is volume relative to deposits. For a DEX, annualized volume
can be as high as ∼ 100× deposits (e.g. Uniswap). In comparison,
for a collateralized stablecoin accruing fees on borrowed assets,
such fees can be as low as ∼ 1/4 of deposits. This ∼ 400× factor
makes the feasible region for incentive security against governance
attacks potentially larger in DEXs than stablecoins. This leads us
to the following conjecture in the context of our models:


Conjecture 2. _Considering fully decentralized systems (𝛼_ = 0 _)_
_with (i) multiple classes of interested parties and (ii) a high degree of_
_flexibility in governance design, DEXs have a wider range of feasible_
_long-term participation equilibria than stablecoins under realistic_
_parameter values._


An interpretation is that it may be fundamentally easier to economically secure DEXs against governance attacks than stablecoins. The conjecture also suggests ways in which broad stablecoin governance powers could be better aligned: by taxing transac
∼
tions/economic activity ( DEX volume) as opposed to assets under
management. Of course, such a tax would make these stablecoins
altogether less desirable to users with a cost for flexible governance.


**6** **CONCLUDING REMARKS**


We have introduced a foundational framework for relating economic mechanics of all stablecoins and formulated three classes of

models for non-custodial stablecoins, for which traditional financial
models are sparse. These models evaluate measures of economic
stability and incentive-based security considering mutual participation incentives of agents necessary for a mechanism to function.
These models consider attack vectors including governance, data
feeds, miners, and deleveraging market feedback effects.


**ACKNOWLEDGMENTS**


We thank Andrew Miller and the anonymous reviewers for their
feedback and suggestions. This project received funding from a
Bloomberg Fellowship, NSF CAREER award #1653354, EPSRC Standard Research Studentship (DTP) (EP/R513052/1) and the BinanceX
Fellowship programme.


17A likely exception is price feed attacks.



13


**REFERENCES**


[1] Mitsutoshi Adachi, Matteo Cominetta, Christoph Kaufmann, Anton van der
Kraaij, et al. 2020. A regulatory and financial stability perspective on global
stablecoins. _Macroprudential Bulletin_ 10 (2020).

[2] Nader Al-Naji, Josh Chen, and Lawrence Diao. 2017. Basis: A Price-Stable
Cryptocurrency with an Algorithmic Central Bank. (2017), 19 pages. [https:](https://www.basis.io/basis{_}whitepaper{_}en.pdf)
[//www.basis.io/basis{_}whitepaper{_}en.pdf](https://www.basis.io/basis{_}whitepaper{_}en.pdf)

[3] Guillermo Angeris and Tarun Chitra. 2020. Improved Price Oracles: Constant
Function Market Makers. _arXiv preprint arXiv:2003.10001_ (2020).

[4] Guillermo Angeris, Hsien-Tang Kao, Rei Chiang, Charlie Noyes, and Tarun Chitra.
2019. An analysis of Uniswap markets. _arXiv preprint arXiv:1911.03380_ (2019).

[5] Sirio Aramonte, Fernando Avalos, et al. 2020. _The recent distress in corporate bond_
_markets: cues from ETFs_ . Technical Report. Bank for International Settlements.

[6] Kenneth Joseph Arrow. 1965. _Aspects of the theory of risk-bearing_ . Yrjö Jahnssonin
Säätiö.

[7] Raphael Auer and Rainer Böhme. 2020. _The technology of retail central bank_
_digital currency_ . Technical Report. BIS Quarterly Review, March.

[8] Bruce A Babcock, E Kwan Choi, and Eli Feinerman. 1993. Risk and probability
premiums for CARA utility functions. _Journal of Agricultural and Resource_
_Economics_ (1993), 17–24.

[9] John Barrdear and Michael Kumhof. 2016. _The macroeconomics of central bank_
_issued digital currencies_ . Technical Report. Bank of England.

[10] Itzhak Ben-David, Francesco Franzoni, and Rabih Moussawi. 2018. Do ETFs
increase volatility? _The Journal of Finance_ 73, 6 (2018), 2471–2535.

[11] Bruno Biais, Christophe Bisière, Matthieu Bouvard, and Catherine Casamatta.
2019. The Blockchain Folk Theorem. _Review of Financial Studies_ 32, 5 (2019),
[1662–1715. https://doi.org/10.1093/rfs/hhy095](https://doi.org/10.1093/rfs/hhy095)

[12] Blockchain.com. 2019. _The state of stablecoins_ [. Technical Report. https://www.](https://www.blockchain.com/ru/static/pdf/StablecoinsReportFinal.pdf)
[blockchain.com/ru/static/pdf/StablecoinsReportFinal.pdf.](https://www.blockchain.com/ru/static/pdf/StablecoinsReportFinal.pdf)

[13] Taras Bodnar, Nestor Parolya, and Wolfgang Schmid. 2015. On the exact solution

   - f the multi-period portfolio choice problem for an exponential utility under
return predictability. _European Journal of Operational Research_ 246, 2 (2015), 528

[– 542. https://doi.org/10.1016/j.ejor.2015.04.039](https://doi.org/10.1016/j.ejor.2015.04.039)

[14] Anton Braverman and Andreea Minca. 2018. Networks of common asset holdings:
aggregation and measures of vulnerability. _The Journal of Network Theory in_
_Finance_ 4, 3 (2018).

[15] Philip N Brown. 2019. Incentives for Crypto-Collateralized Digital Assets. In
_Proceedings of the 3rd Annual Decentralized Conference on Blockchain and Cryp-_
_tocurrency_, Vol. 28. 2.

[16] Vitalik Buertin. Jan. 2018. Collateralized Debt Obligations for Issuer-Backed
[Tokens. https://ethresear.ch/t/collateralized-debt-obligations-for-issuer-backed-](https://ethresear.ch/t/collateralized-debt-obligations-for-issuer-backed-tokens/525)
[tokens/525.](https://ethresear.ch/t/collateralized-debt-obligations-for-issuer-backed-tokens/525)

[17] Dirk Bullmann, Jonas Klemm, and Andrea Pinna. 2019. In search for stability in
crypto-assets: Are stablecoins the solution? _ECB Occasional Paper_ 230 (2019).

[18] Y Cao, M Dai, S Kou, L Li, and C Yang. 2018. Designing stable coins. _Duo Network_
_[Whitepaper, https://duo.network/papers/duo_academic_white_paper.pdf](https://duo.network/papers/duo_academic_white_paper.pdf)_ (2018).

[19] Hans Carlsson and Eric Van Damme. 1993. Global games and equilibrium selection. _Econometrica: Journal of the Econometric Society_ (1993), 989–1018.

[20] Miles Carlsten, Harry Kalodner, Arvind Narayanan, and S. Matthew Weinberg.
2016. On the instability of Bitcoin without the block reward. In _Proceedings of_
_the ACM Conference on Computer and Communications Security_, Vol. 24-28-Octo.
[154–167. https://doi.org/10.1145/2976749.2978408](https://doi.org/10.1145/2976749.2978408)

[21] Xi Chen, Christos Papadimitriou, and Tim Roughgarden. 2019. An Axiomatic
[Approach to Block Rewards. (2019), 124–131. arXiv:1909.10645 http://arxiv.org/](https://arxiv.org/abs/1909.10645)
[abs/1909.10645](http://arxiv.org/abs/1909.10645)

[22] cLabs. 2019. _An analysis of the stability characteristics of Celo_ . Technical Report.
[https://celo.org/papers/Celo_Stability_Analysis.pdf.](https://celo.org/papers/Celo_Stability_Analysis.pdf)

[23] Coindesk. Jul. 2019. Bitfinex Repays Tether $100 Million of $700 Million
[Loan. https://www.coindesk.com/bitfinex-repays-tether-100-million-of-700-](https://www.coindesk.com/bitfinex-repays-tether-100-million-of-700-million-loan)
[million-loan.](https://www.coindesk.com/bitfinex-repays-tether-100-million-of-700-million-loan)

[24] Cointelegraph. Apr. 2019. Fractional Reserve Stablecoin Tether Only 74% Backed
by Fiat Currency, Say Lawyers. [https://cointelegraph.com/news/fractional-](https://cointelegraph.com/news/fractional-reserve-stablecoin-tether-only-74-backed-by-fiat-currency-say-lawyers)
[reserve-stablecoin-tether-only-74-backed-by-fiat-currency-say-lawyers.](https://cointelegraph.com/news/fractional-reserve-stablecoin-tether-only-74-backed-by-fiat-currency-say-lawyers)

[25] Cointelegraph. Oct. 2018. Crypto Exchange Bitfinex Suspends Fiat Deposits,
[Expects to Resume ‘Within a Week’. https://cointelegraph.com/news/crypto-](https://cointelegraph.com/news/crypto-exchange-bitfinex-suspends-fiat-deposits-expects-to-resume-within-a-week)
[exchange-bitfinex-suspends-fiat-deposits-expects-to-resume-within-a-week.](https://cointelegraph.com/news/crypto-exchange-bitfinex-suspends-fiat-deposits-expects-to-resume-within-a-week)

[26] Philip Daian, Steven Goldfeder, Tyler Kell, Yunqi Li, Xueyuan Zhao, Iddo Bentov,
Lorenz Breidenbach, and Ari Juels. [n.d.]. Flash Boys 2.0: Frontrunning in Decentralized Exchanges, Miner Extractable Value, and Consensus Instability. In _2020_
_IEEE Symposium on Security and Privacy (SP)_ . 566–583.

[27] Douglas W Diamond and Philip H Dybvig. 1983. Bank runs, deposit insurance,
and liquidity. _Journal of political economy_ 91, 3 (1983), 401–419.

[28] Yuhao Dong and Raouf Boutaba. 2020. Melmint: trustless stable cryptocurrency.
In _Cryptoeconomic Systems 2020_ .

[29] Philip H Dybvig and Jaime F Zender. 1991. Capital structure and dividend
irrelevance with asymmetric information. _The Review of Financial Studies_ 4, 1
(1991), 201–219.




[30] Steve Ellis, Ari Juels, and Sergey Nazarov. Sep. 4, 2017. ChainLink: A Decentralized
[Oracle Network. https://link.smartcontract.com/whitepaper.](https://link.smartcontract.com/whitepaper)

[31] Ittay Eyal and Emin Gün Sirer. 2018. Majority is Not Enough: Bitcoin Mining is
Vulnerable. _Commun. ACM_ [61, 7 (June 2018), 95–102. https://doi.org/10.1145/](https://doi.org/10.1145/3212998)
[3212998](https://doi.org/10.1145/3212998)

[32] Juan Garay, Aggelos Kiayias, and Nikos Leonardos. 2015. The Bitcoin Backbone Protocol: Analysis and Applications. Lecture Notes in Computer Sci[ence, Vol. 9057. Springer Berlin Heidelberg, Berlin, Heidelberg, 281–310. https:](https://doi.org/10.1007/978-3-662-46803-6_10)
[//doi.org/10.1007/978-3-662-46803-6_10](https://doi.org/10.1007/978-3-662-46803-6_10)

[33] Eiland Glover and John Reitano. 2018. The Kowala Protocol: a family of
distributed, self-regulating, asset-tracking cryptocurrencies. (2018). [https:](https://web.archive.org/web/20181024035504/https://www.kowala.tech/pdf/kowala-protocol-white-paper.pdf)
[//web.archive.org/web/20181024035504/https://www.kowala.tech/pdf/kowala-](https://web.archive.org/web/20181024035504/https://www.kowala.tech/pdf/kowala-protocol-white-paper.pdf)
[protocol-white-paper.pdf](https://web.archive.org/web/20181024035504/https://www.kowala.tech/pdf/kowala-protocol-white-paper.pdf)

[34] Itay Goldstein and Ady Pauzner. 2005. Demand–deposit contracts and the probability of bank runs. _the Journal of Finance_ 60, 3 (2005), 1293–1327.

[35] Jonathan Goodwin. 2013. A Free Money Miracle. _Mises Daily_ (2013). [https:](https://mises.org/library/free-money-miracle)
[//mises.org/library/free-money-miracle](https://mises.org/library/free-money-miracle)

[36] John M Griffin and Amin Shams. 2019. Is bitcoin really un-tethered? _Available at_
_SSRN 3195066_ (2019).

[37] Lewis Gudgeon, Daniel Perez, Dominik Harz, Arthur Gervais, and Benjamin
Livshits. 2020. The Decentralized Financial Crisis: Attacking DeFi. _arXiv preprint_
_arXiv:2002.08099_ (2020).

[38] Bernardo Guimaraes and Stephen Morris. 2007. Risk and wealth in a model

   - f self-fulfilling currency attacks. _Journal of Monetary Economics_ 54, 8 (2007),
2205–2230.

[39] Dominik Harz, Lewis Gudgeon, Arthur Gervais, and William J. Knottenbelt. 2019.
Balance: Dynamic Adjustment of Cryptocurrency Deposits. In _Proceedings of the_
_2019 ACM SIGSAC Conference on Computer and Communications Security (CCS_
_’19)_ [. ACM, New York, NY, USA. https://doi.org/10.1145/3319535.3354221](https://doi.org/10.1145/3319535.3354221)

[40] Zhiguo He and Wei Xiong. 2012. Rollover risk and credit risk. _The Journal of_
_Finance_ 67, 2 (2012), 391–430.

[41] Marcin Kacperczyk and Philipp Schnabl. 2013. How Safe Are Money Market Funds?*. _The Quarterly Journal of Economics_ 128, 3 (07 2013), 1073–1122.
[https://doi.org/10.1093/qje/qjt010 arXiv:https://academic.oup.com/qje/article-](https://doi.org/10.1093/qje/qjt010)
[pdf/128/3/1073/30631031/qjt010.pdf](https://arxiv.org/abs/https://academic.oup.com/qje/article-pdf/128/3/1073/30631031/qjt010.pdf)

[42] Izabella Kaminska. Mar. 12, 2009. The curious case of ETF NAV deviations.
Financial Times.

[43] Hsien-Tang Kao, Tarun Chitra, Rei Chiang, and John Morrow. 2020. An Analysis

   - f the Market Risk to Participants in the Compound Protocol. (2020).

[44] Ariah Klages-Mundt. 2018. Proposal: a framework for designing better stablecoins.
[https://github.com/aklamun/Stablecoin_grant_proposal_122018.](https://github.com/aklamun/Stablecoin_grant_proposal_122018)

[[45] Ariah Klages-Mundt. Aug. 23, 2018. Basis/Basecoin is a Bob Rubin trade. https:](https://link.medium.com/lKjfepv1r9)
[//link.medium.com/lKjfepv1r9.](https://link.medium.com/lKjfepv1r9)

[46] Ariah Klages-Mundt. Nov. 14, 2019. Vulnerabilities in Maker: oracle[governance attacks, attack DAOs, and (de)centralization. https://link.medium.](https://link.medium.com/VZG64fhmr6)
[com/VZG64fhmr6.](https://link.medium.com/VZG64fhmr6)

[47] Ariah Klages-Mundt, Lewis Gudgeon, and Daniel Perez. 2020. Rainy Day Fund
[Stablecoin. https://www.initc3.org/events/2020-07-26-IC3-Blockchain-Camp.](https://www.initc3.org/events/2020-07-26-IC3-Blockchain-Camp.html)
[html.](https://www.initc3.org/events/2020-07-26-IC3-Blockchain-Camp.html)

[48] Ariah Klages-Mundt and Andreea Minca. 2019. (In) Stability for the Blockchain:
Deleveraging Spirals and Stablecoin Attacks. _arXiv preprint arXiv:1906.02152_
(2019).

[49] Ariah Klages-Mundt and Andreea Minca. 2020. While Stability Lasts: A Stochastic
Model of Stablecoins. _arXiv preprint arXiv:2004.01304_ (2020).

[50] Jordan Lee. 2014. Nubits. (2014). [https://doi.org/10.1038/483531a](https://doi.org/10.1038/483531a)
[arXiv:9907372v1 [arXiv:cond-mat]](https://arxiv.org/abs/9907372v1)

[51] Alexander Lipton, Aetienne Sardon, Fabian Schär, and Christian Schüpbach.
2020. 10. Stablecoins, Digital Currency, and the Future of Money. In _Build-_
_ing the New Economy_ (0 ed.). [https://wip.mitpress.mit.edu/pub/17h9tjq7](https://wip.mitpress.mit.edu/pub/17h9tjq7)
https://wip.mitpress.mit.edu/pub/17h9tjq7.

[52] Loi Luu. 2017. PeaceRelay: Connecting the many Ethereum Blockchains.
(2017). [https://medium.com/@loiluu/peacerelay-connecting-the-many-](https://medium.com/@loiluu/peacerelay-connecting-the-many-ethereum-blockchains-22605c300ad3)
[ethereum-blockchains-22605c300ad3](https://medium.com/@loiluu/peacerelay-connecting-the-many-ethereum-blockchains-22605c300ad3)

[53] Loi Luu. 2020. BTC Parachain Specification: Staked Relayers. (2020). [https:](https://interlay.gitlab.io/polkabtc-spec/spec/staked-relayers.html)
[//interlay.gitlab.io/polkabtc-spec/spec/staked-relayers.html](https://interlay.gitlab.io/polkabtc-spec/spec/staked-relayers.html)

[54] Richard K Lyons and Ganesh Viswanath-Natraj. 2020. _What Keeps Stablecoins_
_Stable?_ Technical Report. National Bureau of Economic Research.

[[55] MakerDAO. 2020. MakerDAO. https://makerdao.com/en/.](https://makerdao.com/en/)

[[56] MakerDAO. 2020. MakerDAO GraphQL API. https://developer.makerdao.com/](https://developer.makerdao.com/dai/1/graphql/ )
[dai/1/graphql/.](https://developer.makerdao.com/dai/1/graphql/ )

[57] Semyon Malamud. 2016. A dynamic equilibrium model of ETFs. (2016).

[58] Andreu Mas-Colell, Michael Dennis Whinston, Jerry R Green, et al. 1995. _Mi-_
_croeconomic theory_ . Vol. 1. Oxford university press New York.

[59] Patrick McCorry, Alexander Hicks, and Sarah Meiklejohn. 2018. Smart Contracts for Bribing Miners. In _Financial Cryptography and Data Security. FC 2018._,
[Vol. 10958. Springer Berlin Heidelberg, 3–18. https://doi.org/10.1007/978-3-662-](https://doi.org/10.1007/978-3-662-58820-8_1)
[58820-8_1](https://doi.org/10.1007/978-3-662-58820-8_1)



14


[60] Michael McLeay, Amar Radia, and Ryland Thomas. 2014. Money creation in the
modern economy. _Bank of England Quarterly Bulletin_ (2014), Q1.

[[61] Meter. 2020. Meter Whitepaper. https://www.meter.io/.](https://www.meter.io/)

[62] Makiko Mita, Kensuke Ito, Shohei Ohsawa, and Hideyuki Tanaka. 2019. What
is Stablecoin?: A Survey on Price Stabilization Mechanisms for Decentralized
Payment Systems. _arXiv preprint arXiv:1906.06037_ (2019).

[63] Amani Moin, Kevin Sekniqi, and Emin Gun Sirer. 2020. SoK: A classification
framework for stablecoin designs. In _Financial Cryptography_ .

[64] Stephen Morris and Hyun Song Shin. 1998. Unique equilibrium in a model of
self-fulfilling currency attacks. _American Economic Review_ (1998), 587–597.

[65] Stephen Morris and Hyun Song Shin. 2000. _Global Games: Theory and Applications_ .
Cowles Foundation Discussion Papers 1275R. Cowles Foundation for Research
[in Economics, Yale University. https://ideas.repec.org/p/cwl/cwldpp/1275r.html](https://ideas.repec.org/p/cwl/cwldpp/1275r.html)

[66] Nexus Mutual. 2020. A Decentralized Alternative to Insurance. [https://](https://nexusmutual.io/)
[nexusmutual.io/.](https://nexusmutual.io/)

[67] Stewart C Myers and Nicholas S Majluf. 1984. Corporate financing and investment
decisions when firms have informationthat investors do not have. _Journal of_
_Financial Economics_ 13, 2 (1984), 187–221.

[68] Jeremy Ney and Nicolas Xuan-Yi Zhang. 2020. Central Bank Digital Currencies and the Long-Term Advancement of Financial Stability. In _Cryptoeconomic_
_Systems 2020_ .

[[69] Opyn. 2020. Opyn protection. https://opyn.co/.](https://opyn.co/)

[70] Cecilia Parlatore. 2016. Fragility in money market funds: Sponsor support and
regulation. _Journal of Financial Economics_ 121, 3 (2016), 595–623.

[71] Ingolf GA Pernice, Sebastian Henningsen, Roman Proskalovich, Martin Florian,
Hermann Elendner, and Björn Scheuermann. 2019. Monetary Stabilization in
Cryptocurrencies–Design Approaches and Open Questions. In _2019 Crypto Valley_
_Conference on Blockchain Technology (CVCBT)_ . IEEE, 47–59.

[72] Nicholas Platias and Marco DiMaggio. 2019. _Terra money: stability stress test_ .
[Technical Report. https://agora.terra.money/t/stability-stress-test/55.](https://agora.terra.money/t/stability-stress-test/55)

[73] John W Pratt. 1978. Risk aversion in the small and in the large. In _Uncertainty in_
_Economics_ . Elsevier, 59–79.

[74] J. Rennison, P. Stafford, C. Smith, and R. Wigglesworth. Mar. 23, 2020. ‘Great
liquidity crisis’ grips system as banks step back. Financial Times.

[75] Jean-Charles Rochet and Xavier Vives. 2004. Coordination failures and the lender

   - f last resort: was Bagehot right after all? _Journal of the European Economic_
_Association_ 2, 6 (2004), 1116–1147.

[76] G. Samman and A. Masanto. 2019. _The state of stablecoins_ . Technical Report.
[Reserve, https://reserve.org/stablecoin-report.](https://reserve.org/stablecoin-report)

[77] Robert Sams. 2015. A Note on Cryptocurrency Stabilisation: Seigniorage Shares.
[(2015). https://github.com/rmsams/stablecoins/blob/master/paper.pdf](https://github.com/rmsams/stablecoins/blob/master/paper.pdf)

[78] Raghu Nandan Sengupta, Aparna Gupta, and Joydeep Dutta. 2016. _Decision_
_sciences: theory and practice_ . Crc Press.

[79] Sargent Thomas. 1987. Macroeconomic theory.

[80] Itay Tsabary and Ittay Eyal. 2018. The Gap Game. In _Proceedings of the 2018 ACM_
_SIGSAC Conference on Computer and Communications Security - CCS ’18_ . ACM
Press, New York, New York, USA, 713–728. [https://doi.org/10.1145/3243734.](https://doi.org/10.1145/3243734.3243737)
[3243737 arXiv:arXiv:1805.05288v2](https://doi.org/10.1145/3243734.3243737)

[[81] yEarn. 2020. yInsure. https://yinsure.finance/.](https://yinsure.finance/)

[82] Alexei Zamyatin, Mustafa Al-Bassam, Dionysis Zindros, Eleftherios KokorisKogias, Pedro Moreno-Sanchez, Aggelos Kiayias, and William J. Knottenbelt.
2019. SoK: Communication Across Distributed Ledgers. Cryptology ePrint
[Archive, Report 2019/1128. https://eprint.iacr.org/2019/1128.](https://eprint.iacr.org/2019/1128)

[83] Alexei Zamyatin, Dominik Harz, Joshua Lind, Panayiotis Panayiotou, Arthur
Gervais, and William J. Knottenbelt. 2019. XCLAIM: Trustless, Interoperable,
Cryptocurrency-Backed Assets. In _Proceedings of the IEEE Symposium on Security_
_& Privacy, May 2019._ [1254–1271. https://doi.org/10.1109/SP.2019.00085](https://doi.org/10.1109/SP.2019.00085)

[84] Fan Zhang, Ethan Cecchetti, Kyle Croman, Ari Juels, and Elaine Shi. 2016. Town
Crier: An Authenticated Data Feed for Smart Contracts. In _Proceedings of the 2016_
_ACM SIGSAC Conference on Computer and Communications Security_ (Vienna,
Austria) _(CCS ’16)_ . Association for Computing Machinery, New York, NY, USA,
[270–282. https://doi.org/10.1145/2976749.2978326](https://doi.org/10.1145/2976749.2978326)

[85] Zixuan Zhang, Michael Zargham, and Victor M. Preciado. 2020. On modeling
blockchain-enabled economic networks as stochastic dynamical systems. _Applied_
_Network Science_ [5, 1 (19 Mar 2020), 19. https://doi.org/10.1007/s41109-020-0254-9](https://doi.org/10.1007/s41109-020-0254-9)

[[86] Micah Zoltu. Dec. 9, 2019. How to turn $20M into $340M in 15 seconds. https:](https://link.medium.com/k8QTaHzmr6)
[//link.medium.com/k8QTaHzmr6.](https://link.medium.com/k8QTaHzmr6)



**A** **APPENDIX**

**A.1** **Tables**


**Category** **Stability Models** **Stablecoins**


Reserve Fund ETF TUSD, USDC, Libra v2
Bank Fund ETF, bank run Tether [1]

MMF ETF, MMF Libra v1
CBDC Currency Chinese DC/EP


**Table 1: Custodial stablecoins and applicable models. NB as**

**of 2019, Tether held 74% reserves in USD/equivalents but**
**claimed to be fully collateralized taking into account the**
**value of loans to partner Bitfinex [23, 24].**


**Category** **Relevant Models** **Projects**


ETF ETF Reserve

DEX Liquidity provider PieDAO, mStable, yCRV, CementDAO, Neutral
CDO CDO Introduced in [16]
RDF Introduced in [44, 47]


**Table 3: Composite stablecoins summary.**


**A.2** **Reserve Fund Stablecoins**


Reserve Fund stablecoins can be modeled as Exchange-Traded
Funds (ETFs). [18] In ETFs, an investment vehicle (the ETF) is created
with indirect claims to a portfolio of underlying assets (e.g., stocks,
bonds, and commodities) held by a custodian. [19] A set of _authorized_
_participants_ (APs) are allowed to redeem shares of the ETF for the
underlying assets and create new shares of the ETF by depositing
underlying assets at the net asset value (NAV). The ETF price is
pegged to the NAV. This peg is maintained by the APs, who capture
arbitrage between the ETF shares and the underlying portfolio. If
direct redemption is allowed in a Reserve Fund stablecoin, then
anyone can be an AP. [20] Some stablecoins make no promises about
future redeemability; in this case, the de facto AP is the issuer itself.
As with ETFs, given sufficiently liquid collateral, the price target
is always maintainable within some bounds through these mechanisms. The tightness of the bounds, however, depend on the liquidity and volatility of the reserve assets. For instance, corporate
bond ETFs traded at significant deviations from NAV during the
financial crisis in 2008 [42] and during the SARS-COV-2 market
panic in 2020 [5]. Even US government bonds, which are normally
highly liquid, faced high liquidity stress in March 2020 [74] with
corresponding ETFs facing similar NAV-price deviations.
Empirical analysis of ETFs, e.g., [10], suggest that securities
with higher ETF ownership are more volatile, which raises concerns about the ETF mechanism. While ETF membership leads to


18To account for risk in underlying commercial bank deposits, we can also add a bank
run model in serial to an ETF model.
19ETFs can provide simpler access to underlying portfolio, which may not be accessible
to the investor otherwise, and reduced frictions/fees in maintaining small positions.
20Fees may discourage small redemptions, so that large redeemers are de facto APs.



15


**Table 2: Non-custodial stablecoins as related by several components (excluding governance and data feeds).**







|Col1|Project|Col3|When|Col5|Event|
|---|---|---|---|---|---|
||||||Deleveraging feedback leads to Dai trading<br>at above 1 USD<br>Collateral liquidation auctions settle at 0 DAI<br>due to illiquidity and network congestion<br>Broken peg, broken settlement due to low<br>collateralization<br>Broken peg, haircut in redeemability due to<br>system debt level<br>Deleveraging feedback leads to Dai trading at<br>above 1 USD<br>Crisis of confidence<br>Crisis of confidence, equity position unable to<br>absorb enough supply|
||Dai|Dai|December 2018|December 2018|December 2018|
||Dai|Dai|March 2020|March 2020|March 2020|
||Dai|Dai|March 2020|March 2020|March 2020|
||bitUSD||Winter 2018-19|Winter 2018-19|Winter 2018-19|
||Steem Dollars|Steem Dollars||December 2018|December 2018|
||NuBits|NuBits|Summer 2016|Summer 2016|Summer 2016|
||NuBits|NuBits|March 2018 - ongoing|March 2018 - ongoing|March 2018 - ongoing|
|||||||


**Table 4: Notable non-custodial stablecoin deleveraging events.**


16


**Stablecoin** **Time Period** **Event**


Tether Oct. 2018 Partner Bitfinex suspends fiat convertibility =⇒ Tether crisis [25]


**Table 5: Custodial stablecoin depegging events.**

|Project|When|Event|
|---|---|---|
|||Error in FX price feed made KRW price skyrocket<br>Link token price cannot be correctly read due to<br>single point of failure<br>Price of Luna/KRW pair on Coinone exchange<br>is manipulated<br>wBTC price on Uniswap was pumped by margin<br>trading on bZx<br>sUSD price on KyberSwap and Uniswap<br>manipulated|
|Synthetix|June 2019|June 2019|
|Nuo Network|June 2019|June 2019|
|Terra|July 2019|July 2019|
||||
|bZx|February 2020|February 2020|
|bZx|February 2020|February 2020|
||||



**Table 6: Non-custodial system oracle manipulation events.**



wider access and so increased trading volume, the relationship with
volatility is unclear as the empirical comparison is not controlled.
Rather, we would want to compare with a setting in which the
underlying portfolio is as easily accessible without the ETF. An
equilibrium model analysis confirms a more nuanced relationship
with volatility. [57] develops a model of endogenous feedback effects in ETFs, in which the liquidity of the underlying portfolio is
influenced by the ETF. This model shows that ETFs are exposed
to different demand shocks than the underlying basket. Even with
small deviations, APs that arbitrage through leveraged positions
can amplify the differences. [21]

An ETF-like model is developed for Reserve Fund stablecoins
in [54] and interpreted against Tether trading data. Models such
as these are a natural starting point to address the following open
questions about Reserve Fund stablecoins:


  - **Issuer AP incentives.** Issuers are in a position to prevent
competition and decide timing in capturing arbitrage. There
is a trade-off between the size of mispricings before APs
intervene, and maintaining a stable asset, which affects demand and ultimately assets under management, for which
they are awarded deposit interest.


21As stated in [57], “ETFs may be both a blessing and a curse. That is introducing new
ETFs may lead to a significant amplification of speculative behavior of arbitrageurs,
destablize the market, and lead to a spike in volatility; however, at the same time,
a “good” ETF may actually stabilize the economy, lead to a significant reduction in
volatility, and improve the liquidity of the underlying securities.”




  - **Issuer target incentives.** If the peg target is defined at the
discretion of the issuer (e.g., not USD or an external index),
then the issuer may have incentive to manipulate the target
index to its advantage. For instance, if the stablecoin is large
enough, changing the target can have a market impact, which
may be advantageous to outside positions held by the issuer.

  - **Effects on fiat currencies.** Does stablecoin structure affect
the ability of government to stabilize currencies? This is
a concern of regulators regarding the size of potential stablecoins, like Libra. This effect could be modeled with ETF
structure in series with currency models.

  - **Effects on crypto markets.** [36] suggested that stablecoins
have been used to manipulate Bitcoin prices. A model of the
economic structure in Bitcoin/stablecoin markets (e.g., [54])
could help determine the direction of causality suggested by
the data.

Some of these open questions are relevant to the wider ETF
literature itself and are not specific to stablecoins.


**A.3** **Fractional Reserve Fund**


_Bank Fund._ In a Bank Fund stablecoin, the issuer maintains a
balance sheet functionally similar to a commercial bank. This balance sheet is based on fractional reserves with deposit obligations
tied to stablecoins that are issued. Aside from the fractional reserve,
the bank holds other capital assets that are illiquid and earn a yield
for the bank. This is a nearly identical model to a normal bank with
a few exceptions: (1) the stablecoin bank my not be regulated or



17


audited, (2) the bank my not be government-insured against bank
runs, and (3) the bank may be freer to deny redemptions and/or
apply redemption fees.
Bank Fund stablecoins can be understood using bank run models in series with ETF models. In a bank run, the fractional liquid
reserve of the bank is depleted from redemptions, after which the
bank defaults as the bank’s remaining assets are illiquid and can

- nly be sold quickly at large discounts (a fire sale). In a bank run,
remaining depositors’ lose their money. [27] shows multiple equilibria to the game played between depositors. This includes a bank run
equilibrium, in which all depositors scramble to redeem their deposits, triggering the collapse in a self-fulfilling way. One approach
is the global games setting of [19] adapted to bank runs in [75] and

[34]. In this setting, depositors observe bank fundamentals with
noise (e.g., the reserve ratio could be random), and they will choose
to rollover (i.e., extend the maturity of) their deposits if their signal
is above a threshold. [40] introduced a staggered debt structure

- f deposit maturities. A point of difference to existing bank run
models are the non-negligible network effects among stablecoin
holders, much less so than among traditional bank depositors.
Bank runs used to happen somewhat regularly. To prevent
frequent crises of faith, governments issued depositor insurance
against bank runs. However, Bank Fund stablecoins are unlikely to
have such insurance and so remain susceptible to bank runs. A key
consideration here is that bank runs follow a threshold effect in

depositor faith. After a threshold is reached, too many depositors
try to redeem, sending the bank’s balance sheet into a ‘death spiral’.
Below this threshold, however, the coin may be very stable.
As noted above, a Bank Fund stablecoin may be freer to deny
redemptions and/or apply redemption fees. An event like this triggered a crisis in Tether in Oct. 2018 (see Table 5). These levers may
also be applied strategically to discourage the continuation of bank
runs or could be abused to create profitable price discrepancies for
the issuer to arbitrage. Thus open questions emerge around issuer
incentives as in the Reserve Fund.


_Money Market Fund._ In a Money Market Fund an underlying
portfolio is meant to closely track a target, with some return. A
traditional Money Market Fund maintains a fixed NAV for redemptions. While the underlying assets are usually highly liquid and
relatively stable, their market values float and so there is some
risk that the fixed NAV is unsustainable. This leads to a liquidity
risk related to bank runs: shocks to the underlying assets leads
money market funds to liquidate assets, which can have the effect

- f lowering prices further if liquidity is temporarily constrained,
which can cause even more liquidations. Money Market stablecoins
can be understood using money market fund models, e.g., [70], in
series with ETF models. There are many case studies of money
market funds breaking the dollar during the 2008 financial crisis. In
particular, [41] show that in the presence of high inflows, money
market funds had expanded their risk-taking and they suffered runs
as a result. Some of the proposed forms of Libra closely resemble
money market structures.


**A.4** **Discussion of Oracles**


Centralized oracles control the risk of outside attack but can lead to

perverse incentives for the provider–at some point, manipulating



the feeds may be more profitable than providing data honestly. They
also introduce single points of failure. Centralized approaches can
be made more secure, for instance, through the use of trusted execution environments [84]. Through such methods, it can be proven
that the data feed is an authentic representation of a particular
source, but it is still inherently manipulable by the source.
Decentralized oracle approaches exist, but remain an open research question. Existing solutions fall short of a full solution. They
rely on Schelling point schemes, in which agents vote on the price
feed and are incentivized by slashing if their vote deviates from the
consensus. These are problematic because incentives are related to
the consensus, which is not objectively verifiable for correctness
and can be manipulable through game theoretic attacks.
There are methods to mitigate these risks. For instance, medianizers are typically used to aggregate prices from a number of

- racles, half of which must then be incorrect to manipulate the final
feed. Some services, such as Chainlink, provide such a medianizer
using an incentivized reputation system [30]. The security of such
systems also remains an open question.
Other methods attempt to create a price feed inferred from onchain metrics, which is then objectively verifiable on-chain [44].
A related method attempts to couple the price of a token to the
cost of mining in proof-of-sequential work (e.g., Elasticoin [28] and
Meter [61]). [22] The security of these methods also remains an open
question.
Some cryptocurrency-to-cryptocurrency prices can be determined on-chain through decentralized exchanges, given appropriately controlled construction (e.g., to account for limited liquidity
and time-averaged over extended time periods to make manipulation more costly). A missing link is still to outside fiat prices,
however. Prices in terms of other stablecoins may be used, but this
faces the same inherent problem: we then rely on that stablecoin,
which may be manipulated or fail, for the data feed.


**A.5** **Agents, preferences and attitudes to risk**


_A.5.1_ _Utility functions._ Provided an agent’s preferences satisfy
certain properties, an agents’ preferences over consumption set
_𝑌_ can be represented by a utility function [58]. In particular, here
we assume that an agents are _mean-variance_ maximizers, roughly
wanting to maximize the mean and minimize the variance of a portfolio, with preferences over a random variable _𝑋_ can be described
as follows:


_𝑈_ ( _𝑋_ ) = _𝜇𝑋_        - _𝜌𝐴𝜎𝑋_ [2] (1)
2

where _𝑋_ ∼ _𝑁_ ( _𝜇𝑋_ _, 𝜎𝑋_ ), with _𝜇𝑋_ denoting the mean of _𝑋_, _𝜎𝑋_ denoting the variance and _𝜌𝐴_ denoting the coefficient of risk aversion.
We provide more information on this formulation in A.5.5.


_A.5.2_ _Method 1: one risky asset, one riskless asset._ In one simple
framework, a _mean-variance_ maximizer can invest proportion _𝛼_ - f
their wealth in a risky asset, and proportion (1 − _𝛼_ ) in a risk free
asset. From this setup, it is possible to derive, as we do in A.5.6, that
their optimal choice of _𝛼_ is given as follows:


22Though note that as ‘stablecoins’ Elasticoin and Meter are only upper bounded
in price without a risk absorption mechanism. Melmint adds a seigniorage shares
mechanism atop Elasticoin to absorb risk.



18


**Figure 2: Values of** _𝜌_ **per CDP.**



_𝛼_ [∗] _𝑤_ = [E][[] _[𝑅]_ []][ −] _[𝑟]_ (2)

_𝜌𝐴𝑉𝑎𝑟_ ( _𝑅_ )



**Figure 3: Values of** _𝜌_ **per Externally Owned Account.**


where _𝑢_ ( _𝑤_ ) is the utility arising form a certain level of wealth
_𝑤_, _𝑎_ _>_ 0, _𝛾_ ≠ 0 and ~~1~~ _[𝑎𝑤]_ ~~−~~ ~~_𝛾_~~ [+] _[ 𝑏]_ _[>]_ [ 0. A standard measure of risk is]

the Arrow-Pratt coefficient of absolute risk-aversion [6, 73], which
extracts a measure of risk-aversion that is invariant to affine transformations as follows: [24]



where _𝑤_ denotes the agent’s wealth, E[ _𝑅_ ] and _𝑉𝑎𝑟_ ( _𝑅_ ) the expected return and variance of a risky asset and _𝑟_ denotes the return

- n a risk-free asset. From this expression, all that is required to
compute _𝜌𝐴_ is knowledge of the five variables in this equation,
making it a tractable place to begin with the estimation of agents’
preferences.


_A.5.3_ _Method 2: preferences from portfolio weights._ It is also possible to uses agents’ investment history to infer agents’ risk-aversion
coefficients. In particular, [13] consider an investor who invests into
_𝑘_ risky assets and a single riskless asset, basing their investment
strategy on an exponential utility function, as above. As well as permitting multiple risky assets, in contrast to above, the closed-form
solution to the portfolio choice problem provided by the authors is
also explicitly multi-period. We present the details of this approach
in A.5.7.


_A.5.4_ _A case study of MakerDAO using Method 1._ We apply Method
1 to Equation 2 to seek to recover agents’ risk aversion in choosing
leverage in the MakerDAO protocol [55], a non-custodial collateral
backed stablecoin (see Section 3). We use data on single collateral
Dai (Sai) up until November 18th 2019. A histogram of the resulting
values of _𝜌_ per CDP is given in Figure 2 [23] . While these results
should only be considered indicative, we find a mean value for _𝜌_ - f
0.0011, which seems approximately consistent with other estimates

- f risk-aversion coefficients in the literature [8]. We also provide
an average value of _𝜌_ per address, rather than per CDP, in Figure 3.
Looking at ‘active’ accounts with more than 10 CDP actions, we
find a mean value for _𝜌𝐴_ - f 0.0012. The main takeaway from figure 3
is that on an address level, most addresses appear to exhibit some
degree of risk aversion, with some estimates of _𝜌_ providing notably
higher levels of risk aversion than appear in the literature.


_A.5.5_ _Utility function estimation - details._ We take as our starting
point a general class of utility functions: those representing Hyperbolic Absolute Risk Aversion (HARA), where the level of risk
tolerance is a linear function of wealth:



_𝐴_ ( _𝑤_ ) = − _[𝑢]_ [′′][(] _[𝑤]_ [)] (4)

_𝑢_ [′] ( _𝑤_ )



Importantly, imposing parameter restrictions _𝑎_ _>_ 0, _𝑏_ = 1 and
_𝛾_ →−∞ ( [78] on equation (3) yields an exponential utility function
_𝑢_ ( _𝑤_ ) = − _𝑒_ [−] _[𝑎𝑤]_, with the property of _constant absolute risk aversion_
_(CARA)_ : _𝐴_ ( _𝑤_ ) = − [−] ~~_𝑎𝑒_~~ _[𝑎]_ [2] ~~[−]~~ _[𝑒]_ ~~_[𝑎𝑤]_~~ [−] _[𝑎𝑤]_ = _𝑎_ = _𝜌𝐴_ . CARA implies that the

amount an agent optimally invests in a risky asset does not depend

- n their wealth. In turn, assuming that agents’ utility functions
feature can be characterized as CARA, then for random variable
_𝑋_, provided _𝑋_ ∼ _𝑁_ ( _𝜇𝑋_ _, 𝜎𝑋_ ) where _𝜇𝑋_ denotes the mean of _𝑋_ and
_𝜎𝑋_ denotes the variance, it can be shown that the expected utility








[79]. The agent




              - _𝜌𝐴_
E[ _𝑢_ ( _𝑋_ )] is given by E[ _𝑢_ ( _𝑋_ )] = − _𝑒_



_𝜇𝑋_ - _𝜌𝐴𝜎_ 2 _𝑋_ [2]




maximizes this expected utility when they maximize _𝜇𝑋_ - _[𝜌][𝐴]_ ~~2~~ _[𝜎]_ _𝑋_ [2] .
Therefore, if we characterize an agent as having exponential utility,
and therefore CARA, then when they maximize this utility when
faced with a normally distributed random variable _𝑋_, they can be
considered a _mean-variance maximizer_, with utility given by:


_𝑈_ ( _𝑋_ ) = _𝜇𝑋_        - _𝜌𝐴𝜎𝑋_ [2] (5)
2

Treating agents as mean-variance maximizers yields one
tractable framework within which agents risk aversion, an aspect

- f their preferences, can be measured. Yet there are several points
to note about this approach. Firstly, assuming that agents exhibit
CARA—where their investment in a risky asset does not depend on
their wealth—may not be wholly realistic. Perhaps agents actually
invest a constant _proportion_ - f their wealth. Moreover, here we
are implicitly assuming that agents are not concerned with the
shape of the risk, aside from the variance, so for instance are not
concerned with heavy tails. In the stablecoin setting, this may too
be an unrealistic representation of the true distributions. We note
these limitations and posit this framework as a tractable entry point
for future research.


24See [58] for further information on expected utility theory and the relevance of
affine transformations.



_𝑢_ ( _𝑤_ ) = [1][ −] _[𝛾]_

_𝛾_



_𝑎𝑤_ _𝛾_

(3)

- 1 − _𝛾_ [+] _[ 𝑏]_ 


23Note that we exclude outliers in the plot, e.g. those with risk aversion above 1



19


_A.5.6_ _Method 1: one risky asset, one riskless asset._ Let us assume
that an agent can invest proportion _𝛼_ - f their wealth in a risky
asset, and proportion (1 − _𝛼_ ) in a risk free asset. [25] This would
provide a total return _𝑋_ ( _𝛼_ ) = _𝛼𝑅_ + (1 − _𝛼_ ) _𝑟_ . Since E[ _𝑋_ ( _𝛼_ )] =
_𝑟_ + _𝛼_ (E[ _𝑅_ ] − _𝑟_ ) and _𝑣𝑎𝑟_ ( _𝑋_ ( _𝛼_ )) = _𝛼_ [2] _𝑣𝑎𝑟_ ( _𝑅_ ), setting _𝜇𝑋_ = E[ _𝑋_ ( _𝛼_ )]
and _𝜎_ [2]
_𝑋_ [=] _[ 𝑣𝑎𝑟]_ [(] _[𝑋]_ [(] _[𝛼]_ [))][, an agent with wealth] _[ 𝑤]_ [will maximize]


_𝑤_ [ _𝑟_ + _𝛼_ (E[ _𝑅_ ] − _𝑟_ )] − [1] (6)

2 _[𝜌][𝐴][𝑤]_ [2] _[𝛼]_ [2] _[𝑉𝑎𝑟]_ [(] _[𝑅]_ [)]

with respect to _𝛼_, yielding optimal solution as given in Equation 2.
From Equation 2 all that is required to compute _𝜌𝐴_ is knowledge

- f the five variables in this equation, making it a tractable place to
begin with the estimation of agents’ preferences.


_A.5.7_ _Method two: preferences from portfolio weights._ Letting X _𝜏_
be a random return vector of _𝑘_ risky assets, and supposing that
X _𝜏_ and a vector of _𝑝_ predictable variables z _𝜏_ jointly follow a vector autoregressive process of order 1, the authors prove that the

- ptimal multi-period portfolio weights for all periods [0 _,𝑇_ - 1]
can be analytically stated. In particular, by Corollary 2, letting
X _𝜏_ = ( _𝑋𝜏,_ 1 _,𝑋𝜏,_ 2 _, ...,𝑋𝜏,𝑘_ ) [′] be a sequence of independently and identically normally distributed vectors of _𝑘_ risky assets (X _𝜏_ ∼ _𝑁_ ( _𝜇,_ Σ)),
_𝑟_ _𝑓,𝜏_ be the riskless asset return, and provided Σ is positive definite,
then ∀ _𝑡_ = 1 _, ...𝑇_ :

w [∗] T−t [=] _𝜌_ AWT−tΠ1 [T] i=T−t+2 [R][f] _[,]_ [i] Σ [−][1] _𝜇_ ˆ (7)

where ˆ _𝜇_ = _𝜇_  - _𝑟_ _𝑓,𝑇_  - _𝑡_ +21, which can be rearranged to yield an
explicit expression for _𝜌𝐴_ :


_𝜌𝐴_ = 1 Σ [−][1] _𝜇_ ˆ (8)

w [∗] T−t [W][T][−][t][Π] i [T] =T−t+2 [R][f] _[,]_ [i]

On this approach, provided data is available on agents’ portfolio
weights through time, a value for _𝜌𝐴_ could potentially be calibrated
more precisely than method one would allow; however, this data
requirement in itself is more demanding. In particular, in the context

- f stablecoins, for example, the possibility that one agent uses
multiple blockchain addresses would obfuscate the true portfolio
weights through time. However, to the extent that future work is
able to accurately determine these weights, this offers a promising
approach to calibrate values of _𝜌𝐴_ .


_A.5.8_ _Empirical case study of Method 1._ To illustrate how these
utility function estimation techniques can be applied, we provide a
minimal working example, applying method 1 to MakerDAO [55].
A core component of the Maker stablecoin system is the issuance

- f a stablecoin against the value of collateral. In particular, down
to a threshold value of 150%, agents choose how much stablecoin
to issue as debt against their collateral. For example, for 150 USD
worth of ETH collateral, at the 150% threshold an agent can issue
up to 100 USD of stablecoin debt. However, if the ETH/USD price
falls, then the agent would become undercollateralized relative
to the 150% threshold, and would incur liquidation costs. On the
converse—and one of the primary use cases of such a stablecoin—if
the agent repurchases more ETH with their debt, the agent has


25Here we are not considering the participation question about whether to invest
at all, but instead considering how, given a fixed amount to invest, this can be done

- ptimally.



accessed leverage. If the ETH/USD price rises, then the agent will
stand to benefit more from this price increase than if they had not
issued themselves debt.

Thus, following method 1, in this section the goal is to estimate
equation (2). We proceed with the following demonstrative steps.


(1) **Data collection.** We use the MakerDAO GraphQL API [56]
to obtain data on Collateralized Debt Position (CDP) actions. [26]


(2) **Data cleaning and sample selection.** We clean the data,
focusing only on Externally Owned Accounts prior to the
launch of multi-collateral DAI. We further only consider
CDPs with more than 50 USD of collateral.

(3) **Wealth calculation (** _𝑤_ **).** We assume that each time an agent
issues themselves with the stablecoin, this is used to buy
more ETH. Therefore for each agent we calculate their total
wealth as the sum of their ETH holdings (ETH collateral and
ETH bought with stablecoin) less their debt.
(4) **Risky asset holding (** _𝛼_ **).** We calculate the ratio of ETH
holdings to original ETH collateral. Leverage is represented

as _𝛼_ _>_ 1.

(5) **Computation of mean and variance of risky asset**
**(** E[ _𝑅_ ] **and** _𝑉𝑎𝑟_ ( _𝑅_ ) **).** We compute the mean and variance of
the risky asset by computing the cumulative rolling moving
average mean and variance of daily ETH/USD returns.
(6) **Assumption of a risk free rate (** _𝑟_ **).** We assume that the
investor has access to a risk-free interest rate of 2% annually.


**A.6** **Cross-chain and Synthetic Assets**


Synthetic assets use the same mechanisms as non-custodial stablecoins but with different target pegs (e.g., dYdX’s perpetuals using
synthetic BTC). In comparison, cross-chain mechanisms transfer
assets between blockchains. Where both blockchains are able to

verify state of the other, cross-chain assets do not require collateral
as the issue and redeem procedures can be executed through transaction inclusion proofs via a chain relay on each blockchain (e.g.
PeaceRelay [52]). Hence, incentive design for cross-chain mechanisms is not required to maintain a price peg, but rather to keep
the relays on each side up-to-date and protected against attacks
such as relay poisoning [53, 83].
If a cross-chain mechanism enables asset transfers (i.e., not
atomic swaps) from a blockchain which does _not_ have the ability to verify the state of another blockchain (e.g., Bitcoin) to one
that does (e.g., Ethereum), collateral or trust in a third party is required. [27] These cross-chain mechanisms utilize intermediaries that
hold custody over the locked asset. We can distinguish between
trusted non-collateralized intermediaries where custodial models

can be applied (e.g., wBTC) and non-custodial cross-chain mechanisms (e.g., XCLAIM, tBTC, RenBTC). Non-custodial designs rely

- n collateral for incentive security in addition to collateral of the
transferred asset itself.

Exogenous collateral without governance assets (e.g.
XCLAIM [39, 83]) can be modelled using the capital structure models without considering the long-term impact of
governance token value. Models that use exogenous collateral for


26This API only covers the stablecoin SAI, the precursor to DAI.
27For a formal proof of this requirement see [82].



20


the transferred asset in combination with endogenous collateral
for incentives (e.g. tBTC), might be subject to a similar governance
token value problem as outlined in 5.1. However, in both cases the
underlying asset is insured by exogenous collateral and hence the
design provides protection of the transferred assets independent of
the success of the cross-chain mechanism. Endogenous collateral



structures, on the other hand, are subject to the same incentive
sustainability issues that rely on an increasing governance token
value (e.g. RenBTC). Here, the security of the transferred asset
relies on the long-term success of the cross-chain mechanism to
disincentivize attacks.



21


