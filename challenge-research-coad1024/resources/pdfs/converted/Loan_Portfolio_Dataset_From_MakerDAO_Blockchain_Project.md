Received 23 January 2024, accepted 4 February 2024, date of publication 6 February 2024, date of current version 21 February 2024.


_Digital Object Identifier 10.1109/ACCESS.2024.3363225_

# Loan Portfolio Dataset From MakerDAO Blockchain Project


YATIPA CHALEENUTTHAWUT [1], VYACHESLAV DAVYDOV 2,3, MICHAEL EVDOKIMOV4,
SUDARUT KASEMSUK [1], STANISLAV KRUGLIK 5, (Member, IEEE),
GRIGORII MELNIKOV [6], AND YURY YANOVICH 1,4, (Member, IEEE)
1Skolkovo Institute of Science and Technology, 121205 Moscow, Russia
2HSE Tikhonov Moscow Institute of Electronics and Mathematics, HSE University, 123458 Moscow, Russia
3Quicktoken Tech Ltd., Dubai, United Arab Emirates
4Faculty of Computer Science, HSE University, 109028 Moscow, Russia
5School of Physical and Mathematical Sciences, Nanyang Technological University, Singapore 637371
6B4B.World, 85310 Budva, Montenegro


Corresponding author: Yury Yanovich (y.yanovich@skoltech.ru)


The work of Vyacheslav Davydov was supported by the Basic Research Program at HSE University.


**ABSTRACT** Decentralized finance (DeFi) offers a range of financial instruments and services that leverage
the capabilities of web3 technology. Maker protocol, which enables users to obtain loans backed by
cryptocurrencies, is one of them. Unlike traditional banks, Maker’s data is transparently recorded on the
Ethereum blockchain. In this research paper, we focus on analyzing the lending aspect of Maker from a
traditional finance perspective. To achieve this, we create a unique dataset with loan portfolios from the
MakerDAO project, making it the first dataset of its kind in the DeFi field. This publicly available dataset
contains essential financial characteristics related to borrowing, including balance, loss given default, annual
equivalent rate, and probability of default. Additionally, we develop a specialized mathematical model
tailored specifically to this project. This model allows us to estimate the probability of default by considering
the presence of crypto-collateral and utilizing Brownian motion passage levels. The results of this study
provide valuable insights into lending practices in DeFi projects. They also help bridge the gap between
traditional finance and blockchain-based financial services.


**INDEX TERMS** Blockchain, decentralized finance, knowledge discovery, dataset, smart contract, data
mining, Brownian motion.



**I. INTRODUCTION**

Financial services refer to the range of activities and products
provided by financial institutions, such as banks, insurance
companies, and investment firms, to meet the financial needs

- f individuals and businesses. These services encompass
various aspects of managing money, including lending,
investing, insurance, and risk management [1], [2]. Financial
services are highly regulated to maintain confidence in the
financial system, provide a financial stability and protect
consumers [3], [4]. For example, the Basel framework (BF) is
the full set of standards of the Basel Committee on Banking


The associate editor coordinating the review of this manuscript and


approving it for publication was Mueen Uddin .



Supervision, which is the primary global standard setter for
the prudential regulation of banks [5]. As of early 2024,
28 jurisdictions covering a half of the humanity population
use the BF. The key quantities of a loan in BF are an interest
rate, a loss given default, and a probability of the default.
But the real bank data is a part of bank confidential data and
may contain sensitive personal information [6], hence it is not

- penly available to compute the parameters.
Decentralized finance (DeFi)–peer-to-peer financial services on public blockchains [7], [8]–not only bring new
web3-based services but also provide analogs of traditional financial instruments [9], [10]. One of them is
Maker, a blockchain protocol that facilitates crypto-backed
loans [11]. The set of smart contracts implement Maker



2024 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License.
VOLUME 12, 2024 For more information, see https://creativecommons.org/licenses/by/4.0/ 24843


Y. Chaleenutthawut et al.: Loan Portfolio Dataset From MakerDAO Blockchain Project



protocol on the Ethereum blockchain, and a decentralized
autonomous organization (DAO) named MakerDAO governs
the project, including economic parameters assignment.
Hereafter, we will use the terms MakerDAO and Maker
interchangeably to refer to both the project and the protocol.
Maker’s smart contracts are deployed on the Ethereum
blockchain, making all related transactions visible to every
- ne. These transactions contain financial information, including user operation names and amounts. While it is technically
possible to conceal this information using zero-knowledge
proofs [12], [13], [14], doing so would greatly complicate
and slow down the protocol, increase transaction fees, and
reduce transparency for participants, ultimately making the
project less reliable. Maker does not encrypt transaction data;
the only hidden information relates to the real-world entities
behind the protocol users identifiers. As a result, financial
information can be extracted from the protocol.While user
identifiers are visible, actual names are not. Hereafter, we will
use the terms MakerDAO and Maker interchangeably to refer
to both the project and the protocol.
Despite the transparency of transactions in blockchainbased projects, they lack regulation and standards as noted in
previous studies [15], [16]. The goal of the current research
is to analyze lending in the DeFi project Maker from a
traditional finance perspective. The outcome is twofold: we
provide a real lending portfolio dataset and equip it with
standard banking numerical parameters.
The main contributions of our work are summarized below


1) We introduced a novel loan portfolio dataset obtained
from the MakerDAO project, making it the first dataset

   - f its kind in the field of DeFi. The dataset, along with
utility functions for easy access, is publicly available
at [17]. However, it should be noted that the dataset is
currently limited to the ETH-A lending program.
2) We incorporated borrowing-driven financial characteristics, such as balance, loss given default, annual
equivalent rate, and probability of default, into the
aforementioned dataset.

3) We developed a project-specific mathematical model
to estimate the probability of default. This model
takes into account the presence of crypto-collateral and
utilizes Brownian motion passage levels to provide a
comprehensive understanding of both individual loan
defaults and the correlation among different loans.


The rest of the paper is organized as follows. Section II
provides an overview of the related papers. In Section III,
we present a comprehensive perspective on the Maker
protocol from the borrower’s point of view. Section IV
introduces mathematical models that describe the financial
characteristics of loans. The structure of the dataset is

- utlined in Section V. In Section VI, a quantitative analysis
is conducted to demonstrate the practicality of the collected
data and the effectiveness of the proposed computational
models. Finally, Section VII provides concluding remarks for
the paper.



**II. RELATED WORK**

Banks use a variety of tools to maintain reasonable risk
levels and increase efficiency, including regulator-required
frameworks like the Basel framework [5] and machine
learning models [18], [19]. Loan portfolio data has also
attracted researchers’ attention, with some studies accessing
proprietary data that is not publicly available. For example,
papers [20], [21] examine the impact of loan portfolio
diversification on risk and capital efficiency based on German
and Australian large banks, respectively. They have an
access to more than thousand individual bank portfolios over
seven years. Various machine learning techniques to predict
non-performing loans using a portfolio dataset provided by a
bank for four years, consisting of 181 thousand borrowers and
hundreds of features, are compared in [22]. The paper [23]
applies random forest to classify non-performing loans for
Indonesia’s bank loan dataset with 3300 borrowers and

12 features.

Several classic finance datasets are publicly available, such
as Home Credit Default Risk on Kaggle, which challenges
participants to predict the probability of default among
307 thousand debts using 239 features [24]. The UC Irvine
Machine Learning repository contains several credit datasets,
with the Taiwan credit card defaults dataset being the largest,
containing 30 thousand debts and 24 features [25]. The peerto-peer lending platform Lending Club provides a dataset
containing 887 thousand debts collected from 2007 until
2015 with 79 features to predict the probability of the
default [26].
In addition to traditional finance, there have been several
studies on decentralized finance (DeFi) and its potential
impact on traditional finance. For instance, the risk model of
DeFi money lending was analyzed using tools from modern
portfolio theory in papers [27], [28]. The challenges and

- pportunities of DeFi in the financial industry were analyzed
in [29]. The risks and benefits of DeFi from the perspective

- f financial intermediation were analyzed in [30]. Also, the
latter paper proposed the framework for analyzing DeFi
projects.
While available data from traditional banking are limited
due to trade secrecy and privacy concerns, DeFi loan
data is openly available on public blockchains. Several
studies have been conducted on DeFi lending platforms
such as Maker, AAVE, Compound, and Spark Lend [11],

[31], [32], [33], including their data collection, economic
parameters estimation, and risk management. For example,
the paper [34] analyzes data from the decentralized Ethereum
protocol called Compound, using a relational database and
providing statistical details to facilitate further analysis. The
paper [31] assess the stability of the DAI stablecoin of the
Maker project over the course of its first year deployment,
including the cryptocurrency crisis in March 2020. The
issue of high collateral requirements for blockchain-based
loans using cryptocurrencies as collateral due to their high
volatility is discussed in [35], and the authors propose
a solution to make loans more accessible by offering



24844 VOLUME 12, 2024


Y. Chaleenutthawut et al.: Loan Portfolio Dataset From MakerDAO Blockchain Project



lower collateral requirements while keeping risk for lenders
bound.

DeFi possesses unique operational characteristics. For
instance, all computations are executed lazily and only upon
a request. However, it is worth noting that the volume of
centralized crypto finance surpasses that of the decentralized counterpart. Consequently, DeFi relies on oracles to
incorporate centralized rates [36], [37], [38]. Oracles are
compensated for their transactions and receive interest for
their services. Typically, platforms obtain values from oracles
at desired intervals. Nevertheless, in times of crisis [39],
delays may occur, leading to deviations and unstable values
as shown in [40]. Moreover, the unique features of DeFi
pose challenges for new risk models. While models for
the entire system exist, for example, the stochastic model
for collateral-based stablecoins [41], models specifically
addressing individual debts are yet to be presented.
However, there has been limited research on providing
a real lending portfolio dataset for Maker and equipping
it with standard banking numerical parameters. Such a
dataset could be useful for both academic research and

practical applications, such as risk management and portfolio

- ptimization in Maker lending.


**III. MAKER PROTOCOL FOR BORROWER**

The Maker Protocol [11] operates using the native DAI
token, which has a one-to-one soft peg to the United States
dollar and is an ERC-20 token [42]. The protocol allows
for collateral-secured DAI debts, with loan terms such as
financial parameters. DAO mechanism to modify certain
debts is included in corresponding smart contract. Financial
parameters, such as the lending interest rate _f_ (the multiplier
applied to the loan balance over time) and the liquidation ratio
_r_ (the minimum allowed ratio of the locked collateral value to
the debt value), are examples of these loan terms. Users can
deposit Ethereum native cryptocurrency called Ether (ETH)

- r other tokens into their instance of a specific smart contract
(Vault) and use them as collateral to mint DAI debt.
Let’s consider a borrower’s workflow in the Maker
Protocol. The borrower starts by creating a Vault and
depositing supporting collateral. The Maker Protocol’s Oracle then evaluates the collateral, providing a real-time price
feed for each asset. Based on the current market value

- f the collateral and the chosen borrowing program, the
protocol calculates the maximum amount of DAI that can
be borrowed. For example, ETH-A, ETH-B, and ETH-C are
different borrowing programs with ETH as collateral, each
with its own set of parameters and risk profiles. ETH-A is
the original and most commonly used program, while ETH-B
and ETH-C were introduced to offer additional options for
users with different risk tolerances or preferences.
Once the borrower has minted DAI, they can use it for
any purpose. The borrower is responsible for repaying the
loan with interest, which is calculated based on the lending
interest rate and duration of the loan. They can fully or
partially repay the loan at any time, borrow more up to



the maximum permitted collateral program and size of the
collateral amount, or increase or decrease the amount of

collateral.

If the value of the collateral falls below a certain

threshold, the Vault is at risk of being liquidated. In this
case, the MakerDAO system will automatically initiate a
liquidation process, which involves selling off a portion of
the collateral to cover the outstanding debt. The borrower can
not interact with the Vault under the liquidation process.
The liquidation process is designed to be fast and efficient,
with the goal of minimizing losses for both the user and
the MakerDAO system. When a Vault is liquidated, the
collateral is sold through an auction, allowing users to bid

- n the collateral using DAI. The auction is competitive, with
bidders offering progressively lower prices until the collateral
is sold.

If the auction is successful and the collateral is sold for

a price that covers the outstanding debt, the remaining DAI
is returned to the user. If the auction is unsuccessful and the

collateral is not sold for a sufficient price, the MakerDAO
system may take a loss on the liquidation. The resulting
penalty for the borrower is flexible but usually ranges from
10% to 33% _._

All actions involving the Vault and system parameters
are recorded as plaintext Ethereum blockchain transactions.
However, these transactions may be challenging for the
general audience to understand due to Maker’s use of
technical terms such as ilk, frob, and art. To address this
issue, we aim to present the loan portfolio dataset from the
Maker project in a more accessible format.


**IV. MATHEMATICAL MODELS**

This study focuses on a single type of collateral. To obtain
a loan in the Maker protocol, a user must have a Vault.
Vaults can be associated with single user only and cannot
be transferred. Ethereum addresses, which are 42-character
hexadecimal strings, represent users. While an address does
not reveal information about the real-world owner, some users
may indirectly or directly disclose their identity. At the same
time, a user can have multiple Vaults, and we keep track

- f which Vaults belongs to which user even in case of

anonymous users.
We can determine if a Vault has an active loan at a given
time by checking if its DAI debt is non-zero. Therefore,
we define the beginning of a loan as when the DAI debt
changes from zero to a positive number. We define the end

- f a loan as when the DAI debt becomes zero from any nonzero value. A loan can be active or ended, with the latter

- ccurring either through successful repayment or liquidation.
A single Vault can have multiple loans, and all loans in it
have non-overlapping beginning-to-end time intervals. Now
let’s examine the financial characteristics of a loan.


_A. BALANCE_

When a user borrows DAI in the Maker project, they need
to provide collateral. Without the loss of generality, we will



VOLUME 12, 2024 24845


Y. Chaleenutthawut et al.: Loan Portfolio Dataset From MakerDAO Blockchain Project



refer to the collateral asset as ETH. The loan starts at _t_ 0 and
lasts until _T_, which can be either the liquidation time, full
repayment time, or maximum observed time if the loan is still
active at the point _T_ .
The amount of collateralization assets at any given time _t_
is denoted by _a_ ( _t_ ) (an example is shown in Figure 1). The
blockchain records updates to the collateral balance as a
piece-wise constant function, represented by update times _τ_
and corresponding changes _�a_ ( _τ_ ) due to collateral deposits

- r withdrawals, and liquidation processes.


**FIGURE 1.** The amount of collateralization assets _a_ ( _t_ ) as a function of
time.


The maximum allowed debt is determined by the collateral
price in DAI and the minimum allowed collateralization
ratio _r_ min( _t_ ). Oracles provide the ETH/DAI exchange rate
_e_ ( _t_ ), which is typically consistent with centralized exchange
rates except in cases of extremely high transaction fees [31].
The minimum allowed collateralization ratio _r_ min( _t_ ) is a
piece-wise linear function with small slopes at non-constant
intervals to ensure platform stability. Since debts in Maker
project are over-collateralized we have that _r_ min( _t_ ) _>_ 1.


**FIGURE 2.** The debt _d_ ( _t_ ) as a function of time.



Let _d_ ( _t_ ) be the debt at time _t_ (an example is shown in
Figure 2). Interest is charged on the active debt, with the
logarithm of the interest over time denoted by _f_ ( _t_ ). If no
actions are taken on the debt during an interval ( _t_ 1 _, t_ 2], then
the debt at time _t_ 2 can be calculated as


_t_ 2
_d_ ( _t_ 2) = _d_ ( _t_ 1) · exp _f_ ( _t_ ) _dt_ _._ (1)

           - � _t_ 1            

The log-interest _f_ ( _t_ ) is piece-wise constant by design of
the platform. If _f_ ( _t_ ) is constant during ( _t_ 1 _, t_ 2], then _d_ ( _t_ 2) =
_d_ ( _t_ 1)·exp _(f_ ( _t_ 2) · ( _t_ 2 − _t_ 1) _)_ . So the collateral balance is piecewise exponential. The function breaks are due to the debt
repayment, getting more or liquidation process. Changes
in the log-interest cause derivative breaks without function
breaks.

The current collateralization ratio _r_ ( _t_ ) for _d_ ( _t_ ) _>_ 0 equals
to the following value (see Figure 3)


_r_ ( _t_ ) = _[e]_ [(] _[t]_ [)][ ·] _[ a]_ [(] _[t]_ [)] _._

_d_ ( _t_ )


If _d_ ( _t_ ) = 0, we can set _r_ ( _t_ ) = +∞ and if _r_ ( _t_ ) drops
below _r_ min( _t_ ) at any point in time, the platform triggers the
liquidation. The collateralization requirement check normally
is near real-time. And the borrower is responsible for paying
the interest during the liquidation period.


**FIGURE 3.** The collateralization ratio _r_ ( _t_ ) and the minimum allowed
collateralization ratio _r_ min( _t_ ) as functions of time.


_B. LOSS GIVEN DEFAULT_

Loss given default (LGD) refers to the portion of an asset that
is lost in the event of a borrower defaulting [5]. In the Maker
protocol, debts are typically over-collateralized, resulting in
losses for users in most cases. We can represent a user’s
balance at time _t_ as


Bal( _t_ ) = _a_ ( _t_ ) · _e_ ( _t_ ) − _d_ ( _t_ ) _,_ (2)


and the left-side limit for any given function _ϕ_ as _ϕ_ ( _t_ - ) =
lim _τ_ ↑ _t_ _[ϕ]_ [(] _[τ]_ [). To calculate][ LGD][ for a user’s collateral liquidation]



24846 VOLUME 12, 2024


Y. Chaleenutthawut et al.: Loan Portfolio Dataset From MakerDAO Blockchain Project



at time _t_, we use the following formula

LGD( _t_ ) = [Bal][(] _[t]_ [−][)][ −] [Bal][(] _[t]_ [)] _._ (3)

_d_ ( _t_              - )


A positive value for LGD indicates a loss for the user, while
a negative value indicates a gain. To determine the average

- f _D_ user defaults at times _t_ 1 _, . . ., tD_, we use a weighted

average:


_D_

    - _d_ =1 _[d]_ [(] _[t][d]_ [−][)][ ·][ LGD][(] _[t][d]_ [)]
LGD =

_D_

~~�~~ _d_ =1 _[d]_ [(] _[t][d]_ [−][)]


_D_

    - _d_ =1 [Bal][(] _[t][d]_ [−][)][ −] [Bal][(] _[t][d]_ [)]
= _D_ _._ (4)

~~�~~ _d_ =1 _[d]_ [(] _[t][d]_ [−][)]


_C. ANNUAL EQUIVALENT RATE_

The interest rate on the platform changes over time and is
charged in second-wise intervals. If a loan is liquidated, the
loss of collateral value during liquidation is calculated as
_(a_ ( _T_ ) − _a_ ( _T_ - ) _)_ - _e_ ( _T_ ). The log-equivalent rate (LER) is a
constant log-interest rate that results in the same final debt,
including any liquidation losses, for a debt from _t_ 0 to _T_ with
debt changes _�d_ 0 _, . . ., �dN_ at times _t_ 0 _, . . ., tN_ respectively.
To find the LER, we use the cumulative debt at time _T_ with
LER = _x_, denoted by _h_ ( _x_ ), which is calculated as



to either active debts or returned debts. _τ_ s are intervals

from the debt opening until the dataset generation for the
active debts. _τ_ s are intervals from the debt taking until
debt repayment for the returned debts

and consider different debt models.


1) POISSON MODEL
The classic finance baseline model is a Poisson model that
assumes all debts are independent and have an exponential
distribution with an unknown parameter _λ >_ 0 for time until
default [43]. This simplification allows for the estimation

- f _λ_ [44], [45]. However, this assumption does not hold for
Maker data since all debts are based on the same collateral

type but with different collateralized ratios.


**Statement 1.** _Let λ be the parameter of the exponential dis-_
_tribution. Let X_ 1 _, . . ., XN_ + _M be independent and identically-_
_distributed (i.i.d.) random variable from the exponential_
_distribution with a parameter λ. Let x_ 1 _, . . ., xN_ + _M be realiza-_
_tions of X_ 1 _, . . ., XN_ + _M_ _. Given x_ 1 _, . . ., xN and deterministic_
_parameters yN_ +1 _, . . ., yN_ + _M such that_ ∀ _n_ = _N_ + 1 _, . . ., N_ +
_M_ : _xn > yN_ _, the maximum likelihood estimator (MLE)_ _λ_ [ˆ] _of_
_the parameter λ is_


ˆ _N_ + _M_
_λ_ = _N_ _._ (8)

~~�~~ _n_ =1 _[x][n]_ [ +] ~~[ �]~~ _[N]_ _m_ = [+] _N_ _[M]_ +1 _[y][m]_


_Proof:_ The likelihood defines as


_LN_ _,M_ ( _λ_ ) = _L_ ( _λ, xN_ +1 _, . . ., xN_ + _M_

| _x_ 1 _, . . ., xN_ _, yN_ +1 _, . . ., yN_ + _M_ )



_h_ ( _x_ ) =



_N_

- _�dn_ - exp _(x_ ( _T_ - _tn_ ) _) ._ (5)


_n_ =1



The LER is then determined by solving the following
equation:


_h_ ( _x_ ) = _d_ ( _T_ ) + _(a_ ( _T_ ) − _a_ ( _T_     - ) _)_     - _e_ ( _T_ ) _,_ (6)


where _h_ ( _x_ ) equals the final debt plus any liquidation
losses. The function _h_ ( _x_ ) is monotonically increasing for
_x_ _>_ 0 since _d_ ( _t_ ) _>_ 0 for _t_ ∈ ( _t_ 0 _, T_ ). Therefore,
if there is no default, the LER falls within the range

- f [min _t_ ∈( _t_ 0 _,T_ ) _f_ ( _t_ ) _,_ max _t_ ∈( _t_ 0 _,T_ ) _f_ ( _t_ )]. However, if there is a
default, the LER can be large and the solution of (6) may be
unstable. To avoid this issue, we only consider values of LER
that are less than or equal to a fixed constant _f_ max _>_ 0.
To determine the average of _D_ users at time _t_, we use a
weighted average:


_D_

     - _i_ =1 _[d][i]_ [(] _[t]_ [)][ ·][ LER] _[i]_
~~LER~~ = _D_ _._ (7)

~~�~~ _i_ =1 _[d][i]_ [(] _[t]_ [)]


_D. PROBABILITY OF DEFAULT_

The probability of default (PD) is a risk assessment parameter
commonly used by financial institutions. It is a financial
term that describes the likelihood of default over a particular
time horizon. Let us consider a dataset of loans from Maker

platform in the format of time intervals as follows:


  - _N_ intervals of the time till default for default debts:

_t_ 1 _, . . ., tN_

  - _M_ intervals of the time during which there were no
defaults: _τN_ +1 _, . . ., τN_ + _M_ . These intervals correspond



The observation that MLE _λ_ [ˆ]  - f _λ_ is given by (8) finishes
the proof.



_N_ + _M_

 - _I_ ( _xn_ ≥ _yn_ ) _,_ (9)

_n_ = _N_ +1



=



_N_ + _M_

- _λ_ - exp(− _λxn_ ) ·


_n_ =1



where _I_ ( _A_ ) is an indicator function of the event _A_, i.e., _I_ ( _A_ ) =
1 if _A_ is true and _I_ ( _A_ ) = 0 if _A_ in not true. The likelihood
is non-negative, and _LN_ _,M_ ( _λ_ ) equals 0 if any _xn_ _< yn,_
_n_ = _N_ + 1 _, . . ., N_ + _M_ . So the maximum of _LN_ _,M_ ( _λ_ ) is
for _xN_ +1 _, . . ., xN_ + _M_ : _xn_ ≥ _yn, n_ = _N_ + 1 _, . . ., N_ + _M_ .
_LN_ _,M_ ( _λ_ ) is a decreasing function of _xn, n_ = _N_ +1 _, . . ., N_ +
_M_ for all _λ_ in the region _xn_ ≥ _yn, n_ = _N_ + 1 _, . . ., N_ + _M_ .
So the maximum of _LN_ _,M_ is at _xn_ = _yn, n_ = _N_ + 1 _, . . ., N_ +
_M_, and the maximization of (9) is equivalent to the classic
problem for the exponential distribution


_LN_ + _M_ ( _λ_ ) = _L_ ( _λ_ | _x_ 1 _, . . ., xN_ _, yN_ +1 _, . . ., yN_ + _M_ )



_N_ + _M_

 - _λ_ - exp(− _λyn_ ) → max _λ_ _[,]_ [ (10)]

_n_ = _N_ +1



=



_N_

- _λ_ - exp(− _λxn_ ) ·


_n_ =1



with the log-likelihood expressed as


_lN_ + _M_ ( _λ_ ) =( _N_ + _M_ ) ln _λ_



 _._ (11)






- _λ_ 






 _N_

 

_n_ =1





_xn_ +

_n_ =1



_N_ + _M_

- _yn_

_n_ = _N_ +1



VOLUME 12, 2024 24847


Y. Chaleenutthawut et al.: Loan Portfolio Dataset From MakerDAO Blockchain Project



The probability of the default for a single debt during
_T_,where _X_ is an exponential random variable with parameter
_λ_ can be written as


PD( _T_ ) = _P_ ( _X < T_ ) = 1 − exp(− _λT_ ) _._ (12)


As the likelihood is functional equivariant [44], the MLE
for PD is


ˆ
PD( _T_ ) = 1 − exp(− _λ_ [ˆ] _T_ ) _,_ (13)


where _λ_ [ˆ] is given by (8). It is important to note that the model
assumes independence between debts, so the covariance
between different users is zero.



B _t_ = _C_ } for _C <_ 0. Then for _T >_ 0 [45] from the reflexion
principle we have that



_e_ ( _t_ ) = _[d]_ [0][ ·] _[ e][ft]_ - _r_ min ≡ _e_ min( _t_ ) _._

_a_ 0



_T_
_P_ ( _Tx_ min _< T_ ) =

       - 0



| _x_ min|
~~√~~ 2 _πs_



min| _x_ min [2]

2 _πs_ [3] _[e]_ [−] 2 _s_



2 _s_ _ds,_ (19)



2 _Cπt_ [3] _[e]_ [−] _[C]_ 2 _t_ [2]



_C_
therefore the distribution density _pC_ ( _t_ ) =
~~√~~ 2



therefore the distribution density _pC_ ( _t_ ) = ~~√~~ 2 _πt_ [3] _[e]_ 2 _t_ .

Now, let stability fee be nonzero constant _f_ ≥ 0. Then
_d_ ( _t_ ) = _d_ 0 · _e_ _[ft]_ and a default is equivalent to the existence

- f such _t >_ 0 that



2) BROWNIAN MOTION MODEL

Another model considers the minimal allowed collateral
ization ratio _r_ min( _t_ ) in comparison to the actual user’s
collateralization _r_ ( _t_ ). We assume that the logarithm of
_e_ ( _t_ ) _/e_ 0 follows a Brownian motion with zero mean and an
unknown standard deviation _σ >_ 0. Therefore, _σ_ [1] [(ln] _[ e]_ _e_ [(] 0 _[t]_ [)] [) is a]

Brownian motion B _t_ with zero mean and unit variance.

Let us denote



I.e., a default is the passage of level



_d_ 0 · _r_ min

[1]

_σ_ [ln] - _a_ 0 · _e_ 0



_x_ min( _t_ ) = [1]



_a_ 0 · _e_ 0



+ _ft_ = _x_ min + _ft_ (20)




_T_
_ψ_ ( _x_ ) =

    - 0



| _x_ + _fs_ |
~~√~~ 2 _πs_ [3]



+ _fs_ |

2 _πs_ [3] _[e]_ [−] [(][|] _[x]_ [+] 2 _[f]_ _s_ _[s]_ [|][)][2]



2 _s_ _ds_ (14)



by Brownian motion B _t_ (see Figure 4).


**FIGURE 4.** Borrower default can be described as a Brownian motion level
passage. The black solid curve represents the normalized log-exchange
rate of the collateral. The magenta dashed line indicates the minimum
allowed rate before default for a user starting from _x_ min. Similarly, the
blue dash-dotted line represents the minimum allowed rate before
default for a user starting from _y_ min.


Let


_TC,f_ = inf{ _t >_ 0 : B _t_ = _C_ + _ft_ } _._ (21)


Then for _C <_ 0 and _f >_ 0



for fixed parameters _f_ and _T_ .


**Theorem 1.** _If_
_1) the normalized exchange rate_ _σ_ 1 [(ln] _[ e]_ _e_ [(] 0 _[t]_ [)] [)] _[ for a given]_

_constant σ >_ 0 _is a Brownian motion Bt with zero mean_

_and unit variance_

_2) the borrower has a debt d_ 0 _and collateral a_ 0 _at time t_ =
0

_3) the borrower has no actions with debt and collateral_
_during t_ ∈ (0 _, T_ ]
_4) the platform’s interest rate f_ ≥ 0 _and the minimum_
_collateralization ratio r_ min _>_ 0 _are constant,_

_then the probability of the borrower’s default during the time_
_interval_ (0 _, T_ ] _and its variance are given by_


_PD_ = _ψ_ ( _x_ min) (15)


_and_


_var_ = _ψ_ ( _x_ min) · (1 − _ψ_ ( _x_ min)) _,_ (16)


_respectively, where_



| _x_ min + _fs_ |
~~√~~ 2 _πs_ [3]



+ _fs_ |

_e_ [−] [(] _[x]_ [min] 2 [+] _s_ _[f][s]_ [)][2]
2 _πs_ [3]



_d_ 0 · _r_ min

[1]

_σ_ [ln] - _a_ 0 · _e_ 0



_._ (17)




_T_
_P_ ( _Tx_ min _,f < T_ ) =

        - 0



_x_ min = [1]



2 _s_ _ds._ (22)



_a_ 0 · _e_ 0



_Proof:_ Firstly, let the stability fee _f_ = 0. Then _a_ ( _t_ ) =
_a_ (0) ≡ _a_ 0 and _d_ ( _t_ ) = _d_ (0) ≡ _d_ 0. Therefore, a debt default is
equivalent to the existence of such _t >_ 0 that

_e_ ( _t_ ) = _[d]_ [0]         - _r_ min ≡ _e_ min _._ (18)

_a_ 0


A debt default occurs when the Brownian motion B _t_
reaches the level _x_ min (17). Let us enote _TC_ = inf{ _t >_ 0 :



And from (14): PD = _ψ_ ( _x_ min). As the default is a Bernoulli
random variable, its variance is given by (16) and theorem
statement follows.


**Theorem 2.** _If, in addition to the assumptions 1)-4) of_
_Theorem 1,_
_5) the second borrower has a debt_ _d_ [˜] 0 _a collateral_ ˜ _a_ 0 _at time_
_t_ = 0 _,_



24848 VOLUME 12, 2024


Y. Chaleenutthawut et al.: Loan Portfolio Dataset From MakerDAO Blockchain Project



_then the covariance of two borrowers’ defaults during time_
_interval_ (0 _, T_ ] _equals_


_cov_ = _ψ_ (min{ _x_ min _, y_ min})

           - (1 − _ψ_ (max{ _x_ min _, y_ min})) (23)


_where_







_y_ min = _σ_ [1] [ln]



˜
_d_ 0 · _r_ min


_a_ ˜ 0 · _e_ 0




_._ (24)



_Proof:_ The second user has a single asset as a collateral
with a default at level _y_ min( _t_ ) = _y_ min + _ft_, where _y_ min is given
by (24). Without loss of generality, _y_ min ≤ _x_ min. Then the
probability of the passage of both _x_ min and _y_ min is


_P_ ( _Tx_ min _,f < T_ ; _Ty_ min _,f < T_ )

= _P_ ( _Ty_ min _,f < T_ ) = _ψ_ ( _y_ min) _._ (25)


Denote _I_ ( _A_ ) the indicator of the event _Tx_ min _,f < T_, i.e.,
_I_ ( _A_ ) = 1, if _Tx_ min _,f < T_, and _I_ ( _A_ ) = 0, if _Tx_ min _,f_ ≥ _T_ .
Denote _I_ ( _B_ ) the indicator of the event _Ty_ min _,f_ _< T_ . The
mathematical expectations and the covariance can be written
in (26) and (27), in turn.


**E** _I_ ( _A_ ) = _P_ ( _Tx_ min _,f < T_ ) = _ψ_ ( _x_ min)

**E** _I_ ( _B_ ) = _P_ ( _Ty_ min _,f < T_ ) = _ψ_ ( _y_ min) (26)

cov( _I_ ( _A_ ) _, I_ ( _B_ )) = **E** _I_ ( _A_ ) _I_ ( _B_ ) − **E** _I_ ( _A_ ) **E** _I_ ( _B_ )

= 1 · _P_ ( _Tx_ min _,f < T_ ; _Ty_ min _,f < T_ )

       - **E** _I_ ( _A_ ) · **E** _I_ ( _B_ )

= _ψ_ ( _y_ min) − _ψ_ ( _x_ min) · _ψ_ ( _y_ min)

= _ψ_ ( _y_ min) · (1 − _ψ_ ( _x_ min))

= _ψ_ (min{ _x_ min _, y_ min})

             - (1 − _ψ_ (max{ _x_ min _, y_ min})) _._ (27)


The observation that (27) coincides with (23) finishes the
proof.



the ADF test is the presence of a unit root in a time series.
If the _p_ - value (the probability that the null hypothesis is true)
is less than a given significance level (usually 0 _._ 05), then the
null hypothesis is rejected, indicating that the time series is
stationary.
To compare the fit of models to data, we use four
quantities [43], [44], [47]:


  - Kullback-Leibler divergence (KL) measures the divergence between two probability distributions. It quantifies the amount of information lost when one distribution
is used to approximate another.

  - Total Variation (TV) measures the divergence between
two probability distributions. It is defined as half the sum

   - f the absolute differences between the corresponding
probabilities in the two distributions.

 - Relative Root Mean Squared Error (RRMSE) and
Relative Mean Absolute Error (RMAE) are quadratic and
linear aggregations of point-wise distances between two
datasets, respectively. In our specific case, RMAE; is
equivalent to TV, but we retain both terms since they are
commonly used by machine learners and statisticians.

For each quantity, a smaller value indicates a better fit of
the theoretical model to the empirical data.


**V. DATASET STRUCTURE**

Our focus is on the ETH-collateralized risk program A
debts (ETH-A) within the MakerDAO protocol deployed

- n the Ethereum network. This program has the largest
number of debts (137,441 out of 259,048) and debt volume
(13.4 billion DAI out of 36.9 billion DAI). We utilized
publicly available data from November 11th, 2019 (the first
debt start in the considered asset) to July 31st, 2023, accessed
via the Big Query project by Google. The collected raw data
was decoded and further processed using Python. To verify
specific information and ensure data correctness, we used a
third-party API Ethereum provider, Infura.


**FIGURE 5.** Annual Maker’s interest rate for ETH-A.


After processing all the internal terms such as frob and
wad and focusing solely on the borrower-related aspect of
the Maker protocol, we collected a loan portfolio dataset. The
dataset comprises two parts: _system_ and _borrower_ data.



As the standard deviation of the Brownian motion ln _e_ ( _t_ )

                   - _e_ 0



_e_ 0







is unobservable, we can estimate it. More precisely, given
a sample {( _tn, e_ ( _tn_ )} _[N]_ _n_ =0 [, where] _[ t]_ [0] _[ <][ t]_ [1] _[ <]_ [ · · ·] _[ <][ t][N]_ [ the]
maximum likelihood estimator is



2

_/_ ( _tn_   - _tn_   - 1) _._ (28)

~~��~~



ˆ
_σ_ =




~~�~~

~~�~~



_N_

- [1]



_N_



_n_ =1



_e_ ( _tn_ )
ln

~~�~~ ~~�~~ _e_ ( _tn_ - 1)



3) MODELS COMPARISON
Both the Poisson process and Brownian motion provide
models for predicting probability of default PD. However,
the true model cannot be observed directly. To test the
accuracy of these models, we generated a dataset of daily
defaults and utilized both models to predict defaults one
day in advance. Initially, the models assume that the data
is stationary. To verify this hypothesis, we employed the
Augmented Dickey-Fuller ADF test [46]. The ADF test is
based on the autoregressive model and assesses unit roots
in time series, which causes trends. The null hypothesis of



VOLUME 12, 2024 24849


Y. Chaleenutthawut et al.: Loan Portfolio Dataset From MakerDAO Blockchain Project



The _system_ data contains common parameters, such as
the ETH/DAI exchange rate _e_ ( _t_ ), which is used to estimate
the collaterization ratio since the ETH-A program deals
with ETH as collateral. The exchange rate is provided
by oracles and typically corresponds to the centralized
exchanges rate [31]. Maker’s loans are overcollateralized,
and the minimum allowed collaterization ratio is defined as
_r_ min( _t_ ). The platform receives interest rates from borrowers,
and the dataset contains the log-interest _f_ ( _t_ ).
The _borrower_ data contains borrowers’ catalog and debt
details. The borrower catalog lists all borrowers and their
debts, each with start and end times, status, and loan actions
(see Table 1). The possible statuses are


  - _repaid:_ the borrower returned the debt

  - _liquidated:_ the debt is fully repaid via liquidation

process

  - _restructured:_ the debt is partially repaid via liquidation
process, and a new debt started immediately after the
liquidation

  - _active:_ the loan is active by the end of the observation
period (July 31st, 2023).

The raw data only includes reference points for these
parameters. Our utility functions allow obtaining their values

- ver time and plotting system parameters for the entire period
(see Figure 5) and loan characteristics for its lifetime (see
Figure 6).


**FIGURE 6.** DAI debt over time for user
0 **×** 4032EE21404af045f6ba8022Cf4607950c87A39A.


The prepared dataset is publicly available on Gitlab [17].


**VI. NUMERICAL EXPERIMENTS**

To showcase the practicality of the gathered dataset (Section V) and viability of the suggested computational models
(Section IV), we conducted a quantitative analysis. The code
to reproduce the experiments is available on Gitlab [17].
We do note the possible presence of unexpected events that
can significantly affect the market. Examples of the latter
include the _Black Thursday_ price crash on March 12th and
13th, 2020 [40], [41], and Maker’s announcement of their



**TABLE 1.** Loan actions of user

0 **×** 931dBd7001D14112D17304B78d305c4FE317E571.


upcoming Spark Lend project in 2023. In the following
subsections, we will observe their effects.


_A. BALANCE_

The _borrower_ data contains the details of all the debts. For

- ur perposes we have to find the number of debts in Figure 7



24850 VOLUME 12, 2024


Y. Chaleenutthawut et al.: Loan Portfolio Dataset From MakerDAO Blockchain Project


and total collateral amount (total value locked, TVL) and debt
in Figure 8, where the balance is their difference.


**FIGURE 7.** The number of ETH-A debts.


**FIGURE 9.** Monthly average LGD.


**FIGURE 8.** The total collateral amount and borrowers’ balance.



The number of borrowers experienced a remarkable surge
initially, but came to a halt during the unfortunate event of
Black Thursday in 2020. The debt amount peaked in mid2021, only to witness a decline due to the cryptocurrency
market downturn known as the crypto winter in the same
year. Currently, the total debt in ETH-A is steadily decreasing
towards zero as Maker DAO transitions into the Spark Lend
Protocol, marking a significant development.


_B. LOSS GIVEN DEFAULT_

The monthly average LGD (4) is depicted in Figure 9.
Maker receives a fixed percentage of 13% from each auction
(represented by the dashed black horizontal line), which
indicates the typical loss level in an efficient market. The
efficiency of the auction is a critical factor [40] and tends to
decrease during periods of declining ETH prices.


_C. ANNUAL EQUIVALENT RATE_

The monthly average AER (7) is shown in Figure 10.
Although the AER for returned debts aligns with the annual
Maker’s interest rate for ETH-A (Figure 5), the majority of
liquidated debts have an AER that exceeds 100%.


_D. PROBABILITY OF DEFAULT_

The number of daily defaults has an ADF test statistic

- f −8 _._ 89, which is significantly smaller than the 1%
significance level of −3 _._ 45. This statistic enables us to reject



**FIGURE 10.** Monthly average AER for liquidated (left) and returned (right)
debts.


the null hypothesis of data non-stationarity and conclude that
the time series is stationary.
We have computed a day-ahead actual number of defaults
together with the predictions by Poisson and Brownian
motion models.


**TABLE 2.** Comparison of PD models. The lower the value in each column,
the better the fit to the data. The best result in each column is highlighted.


The Brownian motion model is found to be superior to the
baseline Poisson process model in describing and predicting
debt defaults (see Table 2). This conclusion is supported by
the KL; divergence, which measures the difference between
the two probability distributions. The regression-specific
RRMSE; is worse for the Brownian motion model compared
to the Poisson process model. However, the RMAE; and TV;
are comparable between the two models.
Both the RRMSE and RMAE values are close to one,
indicating that both models have poor predictive power from



VOLUME 12, 2024 24851


Y. Chaleenutthawut et al.: Loan Portfolio Dataset From MakerDAO Blockchain Project



a regression perspective. This finding suggests that further
analysis is needed.
Overall, the findings confirm the hypothesis that the
Brownian motion model is better suited for capturing
real-world data and demonstrates its superiority in fitting probabilistic distributions in collateral-based DeFi
lending.


**VII. CONCLUSION AND FUTURE WORK**

This research focuses on analyzing the lending aspect of the
Maker protocol in the DeFi space from a traditional finance
perspective. The authors have gathered a unique dataset
comprising loan portfolios sourced from the MakerDAO
project, making it the first dataset of its kind in the DeFi field.
This publicly available dataset contains essential financial
characteristics related to borrowing, including balance,
loss given default, annual equivalent rate, and probability

- f default. The current version of the dataset covers

- nly the most popular Maker’s borrowing program called
ETH-A. However, the authors plan to expand the dataset to
include other programs and new Spark Loan data in future
work.

In addition to collecting this dataset, the authors have
developed a specialized mathematical model tailored specifically to the Maker project. This model allows them
to estimate the probability of default by considering
the presence of crypto-collateral and utilizing Brownian
motion passage levels. The proposed model outperformed
the Poisson process baseline model on the loan portfolio
dataset. By incorporating borrowing-driven financial characteristics into the dataset and developing this model, the
authors provide a comprehensive understanding of both
individual loan defaults and the correlation among different
loans.

Expanding the analysis to include other borrowing
programs beyond ETH-A presents challenges in finding
the default correlation of level passage times between
two correlated Brownian motions representing different
collateral types. The authors acknowledge this as a
future work. However, this also opens up opportunities to estimate the platform’s risk, where simultaneous
defaults of a significant portion of borrowers could pose
a threat.

The findings of this study offer valuable insights into
lending practices in DeFi projects and help bridge the gap
between traditional finance and blockchain-based financial
services. This research contributes to the understanding

- f how DeFi lending operates and offers a standardized
approach to analyzing and evaluating loan portfolios in
the DeFi space. Furthermore, the methodology can be
extended to other DeFi lending platforms such as Compound
and Aave.


**REFERENCES**


[1] E. F. Fama, ‘‘Efficient capital markets: A review of theory and empirical
work,’’ _J. Finance_, vol. 25, no. 2, pp. 383–417, May 1970.




[2] R. C. Merton, ‘‘Theory of rational option pricing,’’ _Bell J. Econ. Manag._
_Sci._, vol. 4, no. 1, p. 141, 1973.

[3] C. Gorter and A. M. Bloem, ‘‘The treatment of nonperforming loans
in macroeconomic statistics,’’ _IMF Work. Papers_, vol. 1, no. 209,
pp. 1–18, 2001.

[4] L. Quaglia, ‘‘The ‘old’ and ‘new’politics of financial services regulation in
the European Union,’’ _New Political Economy_, vol. 17, no. 4, pp. 515–535,
Sep. 2012.

[5] Basel Committee - n Banking Supervisio. (2022). _The_ _Basel_
_Framework. Bank for International Settlements_ . [Online]. Available:
https://www.bis.org/basel_framework/index.htm?export=pdf

[6] P. Voigt and A. von dem Bussche, _The EU General Data Protection Reg-_
_ulation (GDPR)_ [. Cham, Switzerland: Springer, 2017, doi: 10.1007/978-3-](http://dx.doi.org/10.1007/978-3-319-57959-7)
[319-57959-7.](http://dx.doi.org/10.1007/978-3-319-57959-7)

[7] V. Buterin. (2014). _Ethereum White Paper: A Next Generation Smart_
_Contract & Decentralized Application Platform_ . [Online]. Available:
https://github.com/ethereum/wiki/wiki/White-Paper

[8] V. Buterin. (2015). _On Public and Private Blockchains—Ethereum Blog_ .

[Online]. Available: https://blog.ethereum.org/2015/08/07/on-public-andprivate-blockchains/

[9] F. Schär, ‘‘Decentralized finance: On blockchain- and smart contractbased
financial markets,’’ _SSRN Electron. J._, pp. 3571335:1–3571335:24,
Mar. 2020. [Online]. Available: https://www.ssrn.com/abstract=3571335

[10] E. Meyer, I. M. Welpe, and P. Sandner, ‘‘Decentralized finance—
A systematic literature review and research directions,’’ in _ECIS_
_Research_ _Papers_ . Amsterdam, The Netherlands: Elsevier, 2021,
pp. 1–25.

[11] MakerDAO. (2020). _The_ _Maker_ _Protocol:_ _MakerDAO’s_ _Multi-_
_Collateral Dai (MCD) System_ . [Online]. Available: https://makerdao.
com/en/whitepaper

[12] E. Ben Sasson, A. Chiesa, C. Garman, M. Green, I. Miers, E. Tromer,
and M. Virza, ‘‘Zerocash: Decentralized anonymous payments
from Bitcoin,’’ in _Proc. IEEE Symp. Secur. Privacy_, May 2014,
pp. 459–474.

[13] B. Bunz, J. Bootle, D. Boneh, A. Poelstra, P. Wuille, and G. Maxwell,
‘‘Bulletproofs: Short proofs for confidential transactions and more,’’ in
_Proc. IEEE Symp. Secur. Privacy (SP)_, May 2018, pp. 315–334.

[14] D. Korepanova, M. Nosyk, A. Ostrovsky, and Y. Yanovich, ‘‘Building a
private currency service using exonum,’’ in _Proc. IEEE Int. Black Sea Conf._
_Commun. Netw. (BlackSeaCom)_, Jun. 2019, pp. 1–3. [Online]. Available:
https://ieeexplore.ieee.org/document/8812875/

[15] V. Rossikhin, M. Burdin, and O. Mykhalskyi, ‘‘Legal regulation issues of
cryptocurrency circulation in Ukraine,’’ _Baltic J. Econ. Stud._, vol. 4, no. 3,
pp. 254–258, 2018. [Online]. Available: http://www.baltijapublishing.
lv/index.php/issue/article/view/451/pdf

[16] B. D. Feinstein and K. Werbach, ‘‘The impact of cryptocurrency regulation

   - n trading markets,’’ _SSRN Electron. J._, pp. 3649475:1–3649475:52,
Mar. 2021. [Online]. Available: https://papers.ssrn.com/abstract=3649475

[17] Y. Chaleenutthawut, M. Evdokimov, S. Kasemsuk, G. Melnikov, and
Y. Yanovich. (2023). _MakerDAO Loan Portfolio Dataset_ . [Online].
Available: https://github.com/Sudarut-kas/Data-Mining-for-MakerDAO

[18] V. Makri, A. Tsagkanos, and A. Bellas, ‘‘Determinants of nonperforming loans: The case of eurozone,’’ _Panoeconomicus_, vol. 61, no. 2,
pp. 193–206, 2014.

[19] A. Khairi, B. Bahri, and B. Artha, ‘‘A literature review of nonperforming loan,’’ _J. Bus. Manage. Rev._, vol. 2, no. 5, pp. 366–373,
May 2021.

[20] E. Hayden, D. Porath, and N. V. Westernhagen, ‘‘Does diversification
improve the performance of German banks? Evidence from individual
bank loan portfolios,’’ _J. Financial Services Res._, vol. 32, no. 3,
pp. 123–140, Oct. 2007.

[21] S. P. S. Rossi, M. S. Schwaiger, and G. Winkler, ‘‘How loan portfolio
diversification affects risk, efficiency and capitalization: A managerial
behavior model for Austrian banks,’’ _J. Banking Finance_, vol. 33, no. 12,
pp. 2218–2226, Dec. 2009.

[22] S. I. Serengil, S. Imece, U. G. Tosun, E. B. Buyukbas, and B. Koroglu,
‘‘A comparative study of machine learning approaches for non performing
loan prediction,’’ in _Proc. 6th Int. Conf. Comput. Sci. Eng. (UBMK)_,
Sep. 2021, pp. 326–331.

[23] M. Annisa, ‘‘Prediction of non-performing loans for credit application analysis of rural bank using random forest,’’ in _Proc. 9th_
_Int. Conf. Electr. Eng., Comput. Sci. Informat. (EECSI)_, Oct. 2022,
pp. 111–114.



24852 VOLUME 12, 2024


Y. Chaleenutthawut et al.: Loan Portfolio Dataset From MakerDAO Blockchain Project




[24] Md. N. Alam and M. M. Ali, ‘‘Loan default risk prediction using
knowledge graph,’’ in _Proc. 14th Int. Conf. Knowl. Smart Technol. (KST)_,
Jan. 2022, pp. 34–39.

[25] S. R. Islam, W. Eberle, and S. K. Ghafoor, ‘‘Credit default mining using combined machine learning and heuristic approach,’’ 2018,
_arXiv:1807.01176_ .

[26] Y.-R. Chen, J.-S. Leu, S.-A. Huang, J.-T. Wang, and
J.-I. Takada, ‘‘Predicting default risk    - n peer-to-peer lending
imbalanced datasets,’’ _IEEE_ _Access_, vol. 9, pp. 73103–73109,
2021.

[27] V. A. Davydov, S. A. Kruglik, and Y. A. Yanovich, ‘‘Comparison

   - f banking and peer-to-peer lending risks,’’ _Autom. Remote Con-_
_trol_, vol. 82, no. 12, pp. 2155–2168, Dec. 2021. [Online]. Available:
https://link.springer.com/article/10.1134/S0005117921120079

[28] V. A. Davydov, S. A. Kruglik, and Y. A. Yanovich, ‘‘Probability

   - f the default-free state for token package from independent loans,’’
_J. Commun. Technol. Electron._, vol. 67, no. 6, pp. 778–786, 2022, doi:
[10.1134/S1064226922060122.](http://dx.doi.org/10.1134/S1064226922060122)

[29] D. A. Zetzsche, D. W. Arner, and R. P. Buckley, ‘‘Decentralized Finance
(DeFi),’’ _SSRN Electron. J._, pp. 3539194:1–3539194:32, Sep. 2020.

[30] F. Schär, ‘‘Decentralized finance: On blockchain- and smart contractbased financial markets,’’ _Review_, vol. 103, no. 2, pp. 153–174,
2021.

[31] M. Kjäer, M. D. Angelo, and G. Salzer, ‘‘Empirical evaluation of
MakerDAO’s resilience,’’ in _Proc. 3rd Conf. Blockchain Res. Appl. Innov._
_Netw. Services (BRAINS)_, Sep. 2021, pp. 193–200. [Online]. Available:
https://ieeexplore.ieee.org/document/9569811/

[32] AAVE. (2020). _AAVE_ _Protocol_ _Whitepaper_ _V1.0_ . [Online].
Available: https://github.com/aave/prhttps://github.com/aave/aaveprotocol/blob/master/docs/Aave_Protocol_Whitepaper_v1_0.pdf

[33] R. Leshner and G. Hayes. (2019). _Compound: The Money Market Proto-_
_col_ . [Online]. Available: https://compound.finance/documents/Compound.
Whitepaper.pdf

[34] J. A. L. Escamilla and Y. Yanovich, ‘‘Data mining of compound DeFi
project,’’ in _Proc. 5th Int. Conf. Blockchain Technol. Appl._, Dec. 2022,
[pp. 16–23, doi: 10.1145/3581971.3581974.](http://dx.doi.org/10.1145/3581971.3581974)

[35] T. Azoulay, U. Carl, and O. Rottenstreich, ‘‘Allowing blockchain loans
with low collateral,’’ in _Proc. IEEE Int. Conf. Blockchain Cryptocurrency_
_(ICBC)_, May 2023, pp. 1–9.

[36] S. Ellis, A. Juels, and S. Nazarov. (2017). _ChainLink: A Decen-_
_tralized Oracle Network_ . [Online]. Available: https://link.smartcontract.
com/whitepaper

[37] S. Kruglik, K. Nazirkhanova, and Y. Yanovich, ‘‘Challenges beyond
blockchain: Scaling, oracles and privacy preserving,’’ in _Proc. 16th_
_Int. Symp. ‘Problems Redundancy Inf. Control Syst.’ (REDUNDANCY)_,
Oct. 2019, pp. 155–158. [Online]. Available: https://ieeexplore.ieee.

   - rg/document/9003331/

[38] M. Bartholic, A. Laszka, G. Yamamoto, and E. W. Burger, ‘‘A tax
   - nomy of blockchain oracles: The truth depends on the question,’’ in
_Proc. IEEE Int. Conf. Blockchain Cryptocurrency (ICBC)_, May 2022,
pp. 1–15.

[39] E. Bischof, A. Botezatu, S. Jakimov, I. Suharenko, A. Ostrovski,
A. Verbitsky, Y. Yanovich, A. Zhavoronkov, and G. Zmudze, ‘‘Longevity
foundation: Perspective on decentralized autonomous organization for
special-purpose financing,’’ _IEEE Access_, vol. 10, pp. 33048–33058, 2022.

[Online]. Available: https://ieeexplore.ieee.org/document/9739690/

[40] W. C. Gu, A. Raghuvanshi, and D. Boneh, ‘‘Empirical measurements on
pricing oracles and decentralized governance for stablecoins,’’ _Cryptoeco-_
_nomic Syst._, vol. 1, no. 2, pp. 1–29, Oct. 2021.

[41] A. Klages-Mundt and A. Minca, ‘‘While stability lasts: A stochastic model

   - f noncustodial stablecoins,’’ _Math. Finance_, vol. 32, no. 4, pp. 943–981,
Oct. 2022.

[42] F. Vogelsteller and V. Buterin. (2015). _EIP-20:_ _ERC-20_ _Token_
_Standard_ . [Online]. Available: https://github.com/ethereum/EIPs/
blob/master/EIPS/eip-20.md

[43] A. N. Shiryayev, _Probability_ (Graduate Texts in Mathematics), vol. 95.
New York, NY, USA: Springer, 1984.

[44] L. Wasserman, _All of Statistics_ (Springer Texts in Statistics). New York,
[NY, USA: Springer, 2004, doi: 10.1007/978-0-387-21736-9_24.](http://dx.doi.org/10.1007/978-0-387-21736-9_24)

[45] A. N. Shiryaev, _Essentials of Stochastic Finance_ . Singapore: World
Scientific, 1999.




[46] G. Elliott, T. J. Rothenberg, and J. H. Stock, ‘‘Efficient tests for
an autoregressive unit root,’’ _Econometrica_, vol. 64, no. 4, p. 813,
Jul. 1996.

[47] C. E. Rasmussen, ‘‘Gaussian processes in machine learning,’’ in _Advanced_
_Lectures on Machine Learning_ (Lecture Notes in Computer Science),
[vol. 3176. Berlin, Germany: Springer, 2004, pp. 63–71, doi: 10.1007/978-](http://dx.doi.org/10.1007/978-3-540-28650-9_4)
[3-540-28650-9_4.](http://dx.doi.org/10.1007/978-3-540-28650-9_4)


YATIPA CHALEENUTTHAWUT received the

bachelor’s degree in chemical engineering from
Kasetsart University, Bangkok, Thailand, in 2019,
and the master’s degree in data science from the
Skolkovo Institute of Science and Technology
(Skoltech), Moscow, Russia, in 2022.
She is currently a Quantitative Trader. During
the master’s degree, her primary area of focus
was on Decentralized Finance (DeFi) and Portfolio
Optimization. Her research pursuits primarily
revolve around quantitative trading strategies and time series analysis.


VYACHESLAV DAVYDOV received the Specialist
degree (Hons.) in informatics and computer science and the Ph.D. degree in engineering from
the Leningrad Institute of Aviation (now the Saint
Petersburg State University of Aerospace Instrumentation), Saint Petersburg, Russia, in 1992 and
1995, respectively, and the Ph.D. degree in economics from Saint Petersburg State University,
Saint Petersburg, in 2017.
Since 2017, he has been the Lead Research

Scientist with the HSE Tikhonov Moscow Institute of Electronics and

Mathematics, HSE University. Additionally, he is currently the CEO of
Quicktoken Tech Ltd., Dubai, United Arab Emirates. He is an accomplished
professional with more than 25 years of experience in the banking industry.
Throughout his career, he has held various key positions, including the
Chief Economist of the Stock Operations Department, Main Directorate

- f the Central Bank of the Russian Federation for Saint Petersburg, the
First Deputy Chairman of the Board of Viking Commercial Bank, and
the Director of the Department for Work with Problem Assets, NorthWest Sberbank. His research interests include risk assessment, portfolio
management, tokenization, and cross-border payments.


MICHAEL EVDOKIMOV received the bach
elor’s degree (Hons.) in applied mathematics
and information science from National Research

University–Higher School of Economics (HSE),
Moscow, Russia, in 2023.
Currently, he is a Middle Machine Learning
Researcher with VK, Moscow. His research interests include the analysis and prediction of time
series data and recommendation systems.



VOLUME 12, 2024 24853


Y. Chaleenutthawut et al.: Loan Portfolio Dataset From MakerDAO Blockchain Project



SUDARUT KASEMSUK received the bachelor’s

degree (Hons.) in applied mathematics from the
King Mongkut’s Institute of Technology Ladkrabang, Bangkok, Thailand, in 2017. She is currently
pursuing the master’s degree with the Skolkovo
Institute of Science and Technology (Skoltech),
Moscow, Russia.
She was a Teaching Assistant of the Quick
Success Blockchain Course in Innovation Work
shop 2023 with Skoltech. Her primary research is
Economic Data Mining and Analysis of the MakerDAO DeFi Project.


STANISLAV KRUGLIK (Member, IEEE) received
the bachelor’s and master’s degrees (Hons.)
in applied physics and mathematics from the
Moscow Institute of Physics and Technology
(MIPT), Moscow, Russia, in 2015 and 2017,
respectively, the master’s degree (Hons.) in data
science from the Skolkovo Institute of Science

and Technology (Skoltech), Moscow, in 2017, and
the Ph.D. degree in computer science from MIPT,
in 2021.

Currently, he is a Research Fellow with Nanyang Technological University, Singapore. His research interests include information theory and
its applications, in particular to problems related to data storage and
security. He was a recipient of the Potanin Foundation Scholarship, in 2017,
the Russian President Scholarship, in 2016, and the Simons Foundation
Scholarship, in 2015.



GRIGORII MELNIKOV received the bachelor’s

and master’s degrees (Hons.) in applied physics
and mathematics from the Moscow Institute of

Physics and Technology (MIPT), Moscow, Russia,
in 2018 and 2020, respectively, and the master’s
degree (Hons.) in data science from the Skolkovo
Institute of Science and Technology (Skoltech),
Moscow, in 2020.
He is currently the CTO of B4B.World. He has
experience integrating private blockchains in
enterprises and launching dApps on public chains. His research interests
include consensus protocols, blockchain, and its applications.


YURY YANOVICH (Member, IEEE) received the
bachelor’s and master’s degrees (Hons.) in applied
physics and mathematics from the Moscow Institute of Physics and Technology, Moscow, Russia,
in 2010 and 2012, respectively, and the Ph.D.
degree in probability theory and mathematical
statistics from The Institute for Information Trans
mission Problems, Moscow, in 2017.

He has been a Lecturer of the ‘‘Introduction to

Blockchain’’ course with top Russian universities,
since 2017. Currently, he is a Senior Research Scientist with the Skolkovo
Institute of Science and Technology, Moscow. He is the author of the Exonum
consensus protocol. His research interests include blockchain, consensus
protocols, privacy, and applications.



24854 VOLUME 12, 2024


