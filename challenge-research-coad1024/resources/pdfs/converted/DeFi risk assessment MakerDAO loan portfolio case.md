Blockchain: Research and Applications 6 (2025) 100259


Contents lists available at [ScienceDirect](http://www.ScienceDirect.com/)

# Blockchain: Research and Applications


journal homepage: [www.journals.elsevier.com/blockchain-research-and-applications](http://www.journals.elsevier.com/blockchain-research-and-applications)


Research Article

## DeFi risk assessment: MakerDAO loan portfolio case


Ignat Melnikov [a] _[,]_ [b] _[,]_ [∗] _[,]_, Irina Lebedeva [a] _[,]_ [b] _[,]_, Artem Petrov [b] _[,]_ [c], Yury Yanovich [a] _[,]_ [d] _[,]_


a _Skolkovo_ _Institute_ _of_ _Science_ _and_ _Technology,_ _Moscow_ _121205,_ _Russia_
b _Blockchain_ _Laboratory,_ _Sberbank_ _PJSC,_ _Moscow_ _117312,_ _Russia_
c _Blockchain_ _Department,_ _Moscow_ _Institute_ _of_ _Physics_ _and_ _Technology,_ _Moscow_ _141701,_ _Russia_
d _Faculty_ _of_ _Computer_ _Science,_ _HSE_ _University,_ _Moscow_ _109028,_ _Russia_


A R T I C L E I N F O A B S T R A C T



_Keywords:_

Blockchain

Decentralized finance
Risk assessment

Knowledge discovery

Smart contract

Brownian motion


**1.** **Introduction**



Decentralized finance (DeFi) is a rapidly evolving blockchain technology that - ffers a new perspective - n financial
services through Web3 applications. DeFi - ffers developers the flexibility to create financial services using smart
contracts, leading to a lack - f standardized protocols and challenges in applying traditional finance models for risk
assessment, especially in the early stages - f adoption. The Maker protocol is a prominent DeFi platform known for
its diverse functionalities, including loan services. This study focuses - n analyzing the risk associated with Maker’s
loan portfolio by developing a risk model based - n multiple Brownian motions and passage levels, with Brownian
motions representing different collateral types and passage levels representing users’ collateralization ratios.
Through numerical experiments using art­ficial and real data, we evaluate the model’s effectiveness in assessing
risk within the loan portfolio. While - ur findings demonstrate the model’s potential for assessing risk within a
single DeFi project, it is important to acknowledge that the model’s assumptions may not be fully applicable to
real-world data. This research underscores the importance - f developing project-specific risk assessment models
for individual DeFi projects and encourages further exploration - f - ther DeFi protocols.



Decentralized finance (DeFi) [1,2] refers to peer-to-peer financial
services - n public blockchains [3] that introduce new Web3-based - f­
ferings and replicate traditional financial instruments. The lack - f reg­
ulation in DeFi [4--6] has led to concerns about potential fraud, scams,
and security vulnerabilities [7--10]. In traditional finance, regulations
are in place to protect consumers and ensure the stability - f the finan­
cial system [11]. However, in DeFi, users are responsible for their - wn
security and must conduct thorough due diligence before participating
in any protocol.

Despite these risks, DeFi has gained significant traction in recent
years due to its potential for financial inclusion and innovation [12,13].
Traditional financial services are - ften inaccessible to those without a
bank account - r credit history, but DeFi allows anyone with an internet
connection to access financial services. This has the potential to revolu­
tionize banking and finance, particularly in developing countries where
traditional banking infrastructure is lacking.

In addition to providing access to financial services, DeFi also  - ffers

- pportunities for individuals to earn passive income through activities



such as liquidity provision and yield farming [14]. By providing liquidity
to decentralized exchanges - r lending platforms, users can earn interest

- n their crypto assets. Yield farming involves moving assets between
different DeFi protocols to maximize returns, - ften through the use - f
governance tokens that provide additional rewards.

One  - f the key ben­fits  - f DeFi is its transparency and accessibil­
ity [15]. Since transactions are recorded - n public blockchains, anyone
can verify the integrity - f the system and audit smart contracts [16].
This level - f transparency is not possible in traditional finance, where
transactions are - ften - paque and controlled by centralized institutions.

However, the rapid growth  - f DeFi has also led to challenges such
as scalability issues and high gas fees - n the Ethereum network [17].
As more users participate in DeFi protocols, the network becomes con­
gested, leading to slower transaction times and higher fees. This has
prompted developers to explore alternative blockchains and Layer 2 so­
lutions [18,19] to improve scalability and reduce costs [20--22].

One prominent DeFi project is Maker, a blockchain protocol that en­
ables crypto-backed loans [13,23]. The Maker protocol is implemented
through smart contracts - n the Ethereum blockchain, - verseen by a




 - Corresponding author. Skolkovo Institute - f Science and Technology, Moscow 121205, Russia.

_E-mail_ _addresses:_ [ignat.melnikov@skoltech.ru (I.](mailto:ignat.melnikov@skoltech.ru) Melnikov), [irina.lebedeva@skoltech.ru (I.](mailto:irina.lebedeva@skoltech.ru) Lebedeva), [petrov.ag@phystech.edu (A.](mailto:petrov.ag@phystech.edu) Petrov),
[y.yanovich@skoltech.ru (Y.](mailto:y.yanovich@skoltech.ru) Yanovich).


[https://doi.org/10.1016/j.bcra.2024.100259](https://doi.org/10.1016/j.bcra.2024.100259)
Received 5 May 2024; Received in revised form 31 August 2024; Accepted 25 December 2024


Available online 31 December 2024
2096-7209/© 2025 THE AUTHORS. Published by Elsevier B.V. on behalf of Zhejiang University Press. This is an open access article under the CC BY license
(http://creativecommons.org/licenses/by/4.0/).


_I. Melnikov,_ _I. Lebedeva,_ _A. Petrov_ _et_ _al._


decentralized autonomous - rganization (DAO) called MakerDAO. For
simplicity, we will use the terms MakerDAO and Maker interchangeably.

Transactions related to Maker are recorded  - n the Ethereum block­

chain, making them visible to all. This includes financial data such as
user - perations and amounts. Although it is possible to conceal this in­
formation using zero-knowledge proofs [24--26], it would complicate
the protocol, increase fees, and reduce transparency. Maker does not
encrypt transaction data; - nly the identities - f the real-world entities
behind the users are hidden. This allows financial information to be ex­
tracted from the protocol, while user names remain undisclosed.

Unlike traditional financial services, DeFi protocols are largely lack­
ing risk assessment protocols. While some qualitative and case study
risk assessments have been conducted for DeFi protocols [27,28], there
have been few studies that have developed mathematical models to as­
sess risk. For example, a specialized mathematical model was proposed
in Ref. [29] to predict default likelihood in Maker lending, considering
crypto-collateral and using Brownian motion for analyzing loan defaults
and correlations. Similarly, a linear regression model was introduced in
Ref. [30] for risk estimation in Compound and Aave lending protocols.

The goal  - f the current research is to evaluate the risk  - f MakerDAO
loan portfolio. The main contributions - f - ur work to DeFi risk assess­
ment are as follows:


1. Extending a DeFi loan-specific mathematical model - f loan default
correlation to incorporate various types   - f collaterals;
2. Developing an art­ficial DeFi loan portfolio simulator;
3. Computing DeFi loan portfolio risk using both art­ficial and real
data.


The remainder  - f this paper is structured as follows. Section 2 of­
fers background information - n MakerDAO, while Section 3 contains
the literature review. In Section 4, an extended DeFi loan-specific math­
ematical model - f loan default correlation that includes various types

- f collaterals is presented. The model is then evaluated in Section 5.
Finally, Section 6 provides the conclusions - f the paper.


**2.** **MakerDAO** **borrowing** **protocol** **background**


The MakerDAO Protocol [23] is a DeFi project which  - perates  - n the
Ethereum blockchain, - ffering a sophisticated lending platform under­
pinned by the DAI stablecoin. DAI stands - ut as an ERC-20 token [31],
engineered to maintain a soft peg to the United States dollar. This stabil­
ity is achieved through a collateralized debt position framework, where
users can lock in Ethereum and - ther approved cryptocurrencies as
collateral in smart contracts, known as Vaults, to generate DAI. Cen­
tral to the protocol’s governance is the MakerDAO, a DAO composed

- f DAI holders who vote - n critical decisions affecting the protocol’s
parameters. These parameters include the stability fee (interest rate),
which i­fluences the cost - f borrowing DAI, and the liquidation ratio,
determining the minimum collateralization required for loans, thus safe­
guarding the system’s stability. By leveraging blockchain technology,
MakerDAO facilitates a lending environment where loans are managed
by smart contracts, minimizing the risk and enhancing the accessibility

- f financial services.

Let’s consider a borrower’s wor­flow in the Maker Protocol.


  - **Creating** **a Vault:** The first step for a borrower in the Maker Proto­

col is to create a Vault. This Vault acts as a personal container   - n
the blockchain where the borrower can deposit collateral. Collateral
types are diverse within the Maker ecosystem, but Ethereum (ETH)
is among the most commonly used. The deposited collateral serves
as a security for the loan the borrower intends to take   - ut. The con­
cept   - f a Vault is crucial as it segregates each user’s funds and
activities, ensuring personalized risk management and loan details.

  - **Oracle’s** **Role** **in** **Valuation:** The Maker Protocol utilizes Oracles

to maintain a real-time price feed   - f the collateral assets. These Or­
acles are external sources   - f information that feed data into the



_Blockchain: Research and Applications 6 (2025) 100259_


system, ensuring that the valuation   - f collateral is current and re­
flects market prices. This step is critical for determining how much
DAI (the stablecoin   - f the Maker Protocol) can be safely borrowed
against the collateral.

  - **Choosing** **a** **Borrowing** **Program:** Borrowers have   - ptions regard­

ing the terms under which they borrow. For the collateral, there are
different programs like ETH-A, ETH-B, and ETH-C. Each program
has its   - wn parameters, including interest rates, minimum collat­
eralization ratios, and liquidation penalties. These programs cater
to various risk tolerances and borrowing needs, the most balanced
and popular   - f which is ETH-A.

  - **Borrowing DAI:** Based   - n the real-time valuation   - f the deposited
collateral and the specific parameters   - f the chosen borrowing pro­
gram, the protocol calculates the maximum amount   - f DAI that can
be borrowed. Borrowers can then generate DAI up to this limit. The
borrowed DAI can be used for a range   - f activities, including invest­
ment, liquidity provision,   - r personal spending, while the collateral
remains locked in the Vault.

  - **Unlocking** **and** **Liquidation** **Collateral:** To regain access to their
collateral, the borrower needs to repay the borrowed DAI along
with any accumulated stability fee (interest rate). Once the repay­
ment is complete, the borrower can withdraw their collateral. In
contrast, if a Vault’s collateral value dips below a critical thresh­

   - ld, it triggers an automatic liquidation process where the system
auctions the collateral to recoup the   - utstanding debt. During this
phase, the Vault becomes inaccessible to the borrower, ensuring
the process is swift and aims to limit losses for both the borrower
and MakerDAO. The collateral auction employs a competitive bid­
ding mechanism using DAI. Successful auctions that cover the debt
result in any excess DAI being returned to the borrower. However,
if the auction fails to cover the debt fully, MakerDAO might incur
losses, and the borrower faces a liquidation penalty, typically rang­
ing between 10% to 33%.


**3.** **Related** **work**


Banks use various methods to keep risks at reasonable levels and
improve their efficiency. They use frameworks required by regulators,
like the Basel framework [11], and machine learning models [32--34].
There is also a lot - f interest in the research - f loan portfolio data, which

- ften uses private data not available to the public. For instance, some
studies, such as those - n German and Australian big banks, look at how
spreading - ut loans to different types - f borrowers affects the banks’
risk and their use - f capital [35,36]. These studies have access to details
from - ver a thousand bank portfolios across seven years. Another study
compares different machine learning methods to predict loans that will
not be paid back. It uses data from a bank that covers four years, 181
thousand borrowers, and many different data points [37]. Additionally,
a paper uses the random forest technique to identify loans likely not to
be repaid in an Indonesian bank dataset, which included 3300 borrowers
and 12 features [38].

Research has expanded beyond traditional finance to include DeFi
and its interplay with conventional financial systems. Several studies
have employed modern portfolio theory to delve into the risk mod­
els associated with DeFi money lending, as discussed in Refs. [39,40].
The financial industry’s response to the - pportunities and challenges
presented by DeFi was thoroughly analyzed in Ref. [1]. Moreover,
Schar [41] explored the risks and ben­fits - f DeFi through the lens

- f financial intermediation and proposed a framework for evaluating
DeFi projects. In addition, the Ref. [42] provides the analysis - f Value­
at-Risk, estimating the probable maximum loss from cryptocurrency
investments that will not be exceeded - ver a spec­fied period at a given
probability. Kaplan et al. [43] extended this analysis by empirically
examining the relationship between the S&P500 index and DeFi as­
sets (MKR, AVE, COMP), - ffering insights into the dynamics between
centralized and DeFi.



2


_I. Melnikov,_ _I. Lebedeva,_ _A. Petrov_ _et_ _al._


Data from traditional banks are  - ften restricted due to trade secrets

and privacy issues, whereas loan data from DeFi platforms is readily
available - n public blockchains, facilitating extensive research. Stud­
ies - n platforms such as Maker, AAVE, Compound, and Spark Lend
focused - n data collection, economic parameters estimation, and risk
management [23,44--46]. For example, the Ref. [47] provides a detailed
statistical analysis using data from the decentralized Ethereum protocol
Compound, leveraging a relational database for further research explo­
ration. Another study [44] evaluates the stability - f the DAI stablecoin
from the Maker project during its first year, including its response to
the cryptocurrency crisis in March 2020. The issue - f high collateral
requirements for loans that use volatile cryptocurrencies as collateral
is discussed in Ref. [48], where the authors suggested a solution to
lower collateral requirements, thus enhancing loan accessibility while
controlling lender risk. The distinctive characteristics - f DeFi introduce
complexities in developing new risk models. Although there are exist­
ing models that address the system as a whole, such as the stochastic
model for collateral-based stablecoins [49], there is still a lack - f mod­
els tailored to individual debts. Samreen and Alalfi [13] categorized
the in-demand usage scenarios - f decentralized applications (DApps)
into seven categories, including finance, gaming, exchanges, security,
development, healthcare, and marketplace. Their study found that the
MakerDAO platform ranked third in the finance category. Moreover,
Chaleenutthawut et al. [29] created a unique set - f data - n loan portfo­
lios from the MakerDAO project and developed a method for assessing
the probability - f default risk for borrowers using - ne asset as collat­
eral. The dataset was initially focused - n a single borrowing program,
but with slight mod­fications to the methodology and code, it can be
applied to all borrowing programs.

Bertomeu et al. [30] presented a method for evaluating DeFi lending
risk by dissecting lending and borrowing activities into synthetic bor­
rower and lender components. This methodology, when combined with
a linear regression model, - ffers a reliable way to pinpoint weaknesses
and track fluctuations in risk levels in real-time. The effectiveness - f this
model was tested using data from the Compound and Aave projects.

Huang et al. [50] analyzed the popularity  - f various DeFi projects,
and they noted that lending is the most active subcategory in the de­
velopment - f applications for Web3. However, there is still no model
assessing the risks - f default - f the users’ collateral portfolio in decen­
tralized lending. Such a model would make it possible to improve smart
lending contracts and reduce risks for both lenders and borrowers.


**4.** **Mathematical** **model**


This study is centered around conducting a risk assessment for the
DeFi loan portfolio. In - rder to accurately compute this assessment, it is
crucial to understand the joint distribution - f borrowers’ defaults. Since
borrowers may possess various types - f collateral, it is important to ad­
dress this complexity in - ur analysis. The primary focus - f this paper is

- n examining two specific types - f collateral as a basic yet significant
example - f multiple assets. As proposed in the Ref. [29], the cryptocur­
rency exchange rate can be described by Brownian motion. However,
in the case - f multiple assets, the task becomes more difficult, as cryp­
tocurrency assets definitely depend - n each - ther. In this section, we
propose to describe the exchange rate - f a secondary asset as a linear
combination - f Brownian motion for the first asset, and an independent
Brownian process for the second asset. Based - n this proposal, we cal­
culate probabilities for joint defaults from both assets, as well as the
covariance - f these joint defaults. Additionally, we calculate the proba­
bility distribution for default amounts for a protocol.


_4.1._ _Basic_ _notations_


In the context  - f the Maker project, when a user initiates a borrowing
transaction involving the digital currency DAI, it is requisite for them to



_given_ _constant_ _𝜎_ 2 _>_ 0 _is_ _a_ _linear_ _combination_ _of_ _Brownian_ _motions_



_Blockchain: Research and Applications 6 (2025) 100259_


deposit a collateral asset. For the purposes - f this discussion, and with­

- ut loss - f generality, this collateral will be referred to as ETH (Ether).
The initiation - f the loan - ccurs at time _𝑡_ 0 and extends to a termination
point denoted as _𝑇_ . The termination point, _𝑇_, is d­fined by - ne - f three
potential - utcomes: the time - f liquidation, the moment - f complete re­
payment, - r the maximum - bserved time duration in cases where the
loan remains active at the point _𝑇_ .

At any given moment _𝑡_, the quantity  - f collateralization assets is
represented by _𝑎_ ( _𝑡_ ). The blockchain ledger chronicles alterations to
the collateral balance through a piece-wise constant function, charac­
terized by specific update instances _𝜏_ and the respective adjustments
Δ _𝑎_ ( _𝜏_ ). These adjustments stem from actions such as collateral deposits

- r withdrawals, as well as liquidation events. The determination - f the
maximum permissible debt level is contingent upon both the collater­
al’s valuation in DAI and the minimum required collateralization ratio,
denoted as _𝑟_ min( _𝑡_ ). The conversion rate between ETH and DAI, _𝑒_ ( _𝑡_ ),
is supplied by Oracles and is generally aligned with rates from cen­
tralized exchanges, barring instances - f exceedingly high transaction
costs [44]. The minimum required collateralization ratio, _𝑟_ min( _𝑡_ ), is de­
fined by a piece-wise linear function featuring minimal gradients - ver
non-uniform intervals, a measure implemented to uphold platform equi­
librium. Given that the Maker project mandates a collateralization level
exceeding the value - f the debt, it follows that _𝑟_ min( _𝑡_ ) _>_ 1.

Consider the representation  - f debt  - ver time as _𝑑_ ( _𝑡_ ). Interest accrues

- n the - utstanding debt, and the time evolution - f the logarithm - f the
interest rate is denoted by _𝑓_ ( _𝑡_ ). In the absence - f any interventions - n
the debt within the interval ( _𝑡_ 1 _,𝑡_ 2], the debt at _𝑡_ 2 can be expressed as:



⎛
_𝑑_ ( _𝑡_ 2) = _𝑑_ ( _𝑡_ 1) ⋅ exp ⎜⎜⎝



_𝑡_ 2



⎞
_𝑓_ ( _𝑡_ ) _𝑑𝑡_ ⎟ _._ (1)
⎟⎠



∫
_𝑡_ 1



By the platform’s design, the log-interest function, _𝑓_ ( _𝑡_ ), is piece-wise
constant. If _𝑓_ ( _𝑡_ ) remains constant within the interval ( _𝑡_ 1 _,𝑡_ 2], then the
debt at _𝑡_ 2 simpl­fies to _𝑑_ ( _𝑡_ 2) = _𝑑_ ( _𝑡_ 1) ⋅ exp [(] _𝑓_ ( _𝑡_ 2) ⋅ ( _𝑡_ 2 − _𝑡_ 1) [)] . Consequently,

the collateral balance evolves in a piece-wise exponential manner. Dis­
continuities in this function arise due to debt repayments, further bor­
rowings, - r the liquidation process. Alterations in the log-interest rate
result in derivative discontinuities without affecting the continuity - f
the function itself.


The current collateralization ratio, _𝑟_ ( _𝑡_ ), for instances where _𝑑_ ( _𝑡_ ) _>_ 0,
is given as:

_𝑟_ ( _𝑡_ ) = _[𝑒]_ [(] _[𝑡]_ [)][ ⋅] _[𝑎]_ [(] _[𝑡]_ [)] _._

_𝑑_ ( _𝑡_ )


For conditions where _𝑑_ ( _𝑡_ ) = 0, it is appropriate to assign _𝑟_ ( _𝑡_ ) = +∞.
Should the collateralization ratio _𝑟_ ( _𝑡_ ) fall beneath the minimum thresh­

- ld _𝑟_ min( _𝑡_ ) at any point, the platform initiates a liquidation process. The
ver­fication - f collateralization ratios is performed with near real-time
accuracy. Moreover, the borrower is - bliged to satisfy the interest pay­
ments throughout the duration - f the liquidation process.


_4.2._ _Probability_ _of_ _default_


The probability  - f default (PD) is a risk assessment parameter com­
monly used by financial institutions. In - ur model, we call the default,
the moment - f the beginning - f the liquidation - f the Value in the
MakerDAO protocol.


**Theorem** **1.** _If_




[1]

_𝜎_ 1 [ln] _[ 𝑒]_ [1] _𝑒_ [1][(] _[𝑡]_ [)]



1. _The_ _normalized_ _exchange_ _rate_ _of_ _the_ _first_ _asset_ [1]



_𝑒_ [1]
0



_for_ _a_ _given_



_constant_ _𝜎_ 1 _>_ 0 _is_ _a_ _Brownian_ _motion_ _B_ [1] _𝑡_ _[with]_ _[zero]_ _[mean]_ _[and]_ _[unit]_ _[vari­]_

_ance;_




[1]

_𝜎_ 2 [ln] _[ 𝑒]_ [2] _𝑒_ [2][(] _[𝑡]_ [)]



2. _The_ _normalized_ _exchange_ _rate_ _of_ _the_ _second_ _asset_ [1]



_𝑒_ [2]
0



_for_ _a_



3


_I. Melnikov,_ _I. Lebedeva,_ _A. Petrov_ _et_ _al._


_B_ [2] _𝑡_ [=] _[ 𝛼][B]_ [1] _𝑡_ [+] _[ B]_ [∗] _𝑡_ _[,]_ _[where]_ _[B]_ [∗] _𝑡_ _[is]_ _[Brownian]_ _[motion]_ _[with]_ _[zero]_ _[mean]_ _[and]_
_𝜎_ ∗ ≥ 0 _;_
3. _The_ _platform’s_ _interest_ _rates_ _𝑓_ 1 = 0 _,_ _𝑓_ 2 = 0 _and_ _the_ _minimum_ _collater­_

_alization_ _ratios_ _𝑟_ [1] _[𝑟]_ [2] _[constant;]_
min _[>]_ [ 0] _[,]_ min _[>]_ [ 0] _[ are]_

4. _The_ _first_ _borrower_ _has_ _a_ _debt_ _𝑑_ 0 [1] _[and]_ _[collateral]_ _[𝑎]_ [1] 0 _[at]_ _[time]_ _[𝑡]_ [= 0] _[ in]_ _[the]_

_first_ _asset_ _and_ _the_ _second_ _borrower_ _has_ _a_ _debt_ _𝑑_ 0 [2] _[,]_ _[𝑎]_ [2] 0 _[in]_ _[the]_ _[second]_ _[asset,]_



0


_𝑃_ ( sup _𝐵𝑠_ [1] [≥] [−] _[𝑥]_ [1] min _[,]_ [ sup] _𝐵𝑠_ [2] [≥] [−] _[𝑥]_ [2] min [) =]
0≤ _𝑠_ ≤ _𝑇_ 0≤ _𝑠_ ≤ _𝑇_ ∫

                 - _𝑥_ [2] min


where _𝐹_ 1 _,_ 2( _𝑎,𝑏_ ) is calculated from Eq. (3).


_4.3._ _Risk_ _assessment_



_Blockchain: Research and Applications 6 (2025) 100259_



0

∫

- _𝑥_ [1] min



_𝜕_ [2] _𝐹_ 1 _,_ 2( _𝑎,𝑏_ ) _𝑑𝑎𝑑𝑏_

_𝜕𝑎𝜕𝑏_



_and_



_𝑎_ _[𝑖]_
_𝑑_ 0 _[𝑒][𝑖]_ _[𝑖]_ 0 ≥ _𝑟_ _[𝑖]_ _min_ _[,]_ _[𝑖]_ [= 1] _[,]_ [2] _[;]_
0



5. _The_ _borrowers_ _have_ _performed_ _no_ _actions_ _with_ _debt_ _and_ _collateral_ _during_

_𝑡_ ∈(0 _,𝑇_ ] _in_ _both_ _assets,_


_then_ _the_ _probability_ _of_ _the_ _simultaneous_ _default_ _of_ _borrowers_ _in_ _two_ _assets_
_during_ _the_ _time_ _interval_ (0 _,𝑇_ ] _are_ _given_ _by:_



The previous theorem also allows us to calculate the probability dis­
tribution for debt assets falling under liquidation.


**Theorem** **2.** _If_


1. _There_ _are_ _𝑚_ _assets,_ _in_ _the_ _𝑘-th_ _asset_ _there_ _are_ _𝑛𝑘_ _users,_ _𝑘_ = 1 _,_ … _,𝑚;_



0



0

∫

- _𝑥_ [1]
min



_𝜕_ [2] _𝐹_ 1 _,_ 2( _𝑎,𝑏_ ) _𝑑𝑎𝑑𝑏,_ (2)

_𝜕𝑎𝜕𝑏_




[1]

_𝜎_ [ln] _[ 𝑒][𝑘]_ _𝑒_ _[𝑘]_ [(] _[𝑡]_ [)]



_𝑒_ _[𝑘]_
0



PD( _𝑥_ [1] min _[,𝑥]_ [2] min [) =]

∫

       - _𝑥_ [2]
min


_where_



2. _The_ _normalized_ _exchange_ _rate_ _of_ _the_ _𝑘-th_ _asset_ 𝙴 _[𝑘]_ _𝑡_ [=] [1]



_for_ _a_




[(] _[𝑎,𝑏]_ [)] ⋅ _𝑒_ [−] _[𝑟]_ [0][(] 4 _[𝑎,𝑏]_ _𝑡_ [)2]


2π _𝑡_



_𝑛_ =1 _,_ 3 _,..._



)



_𝐹_ 1 _,_ 2( _𝑎,𝑏_ ) = [2] _[𝑟]_ [0][(] _[𝑎,𝑏]_ [)]



4 _𝑡_
∑



1 _𝑛_ π _𝜃_ 0( _𝑎,𝑏_ )
_𝑛_ [⋅] [sin] ( _𝛾_



~~√~~



; (3)
)]



_given_ _constant_ _𝜎>_ 0 _;_
3. _𝑥_ _[𝑘]_ _[the]_ _[level]_ _[passage]_ _[of]_ _[𝑖][-th]_ _[user]_ _[in]_ _[the]_ _[𝑘][-th]_ _[asset]_ _[at]_ _[the]_ _[initial]_
_𝑚𝑖𝑛,𝑖_ [=] _[ 𝑥]_ _𝑖_ _[𝑘]_ _[is]_
_moment_ _of_ _time,_ _𝑖_ = 1 _,_ … _,𝑛𝑘;_
4. 0 = _𝑥_ _[𝑘]_ _[that]_ _[is,]_ _[users’]_
0 _[> 𝑥][𝑘]_ 1 _[> 𝑥][𝑘]_ 2 _[>]_ [ …] _[ > 𝑥][𝑘]_ _𝑛𝑘_      - 1 _[> 𝑥][𝑛]_ _𝑘_ _[> 𝑥]_ _𝑛_ _[𝑘]_ _𝑘_ +1 [= −∞] _[,]_

_collaterals_ _are_ _sorted_ _from_ _the_ _most_ _risky_ _to_ _the_ _least_ _risky;_
5. _𝑑_ _[𝑘]_ _[the]_ _[debt]_ _[of]_ _[𝑖][-th]_ _[user]_ _[in]_ _[the]_ _[𝑘][-th]_ _[asset;]_
_𝑖_ _[is]_
6. _𝑓𝑘_ ≥ 0 _is_ _the_ _platform’s_ _interest_ _rate_ _for_ _the_ _𝑘-th_ _asset;_
7. _The_ _joint_ _distribution_ _density_ _of_ sup (𝙴 _[𝑘]_ _𝑠_ [−] _[𝑓][𝑘][𝑠]_ [)] _[,]_ _[𝑘]_ [= 1] _[,]_ […] _[,𝑚][,]_ _[is]_ _[equal]_
0≤ _𝑠_ ≤ _𝑇_

_to_ _𝑓𝑚_ ( _𝑥_ [1] _,_ … _,𝑥_ _[𝑚]_ ) _,_


_then_ _the_ _probability_ _of_ _default_ _a_ _certain_ _sum_ _is_ _equal:_


_𝑃_ (𝙳𝚎𝚏𝚊𝚞𝚕𝚝𝙲𝚘𝚕𝚕𝚊𝚝𝚎𝚛𝚊𝚕𝚜 ∶{ _𝐷𝑖_ _[𝑘]_ _𝑘_ _[,𝑘]_ [= 1] _[,]_ […] _[,𝑚]_ [}] )



2 [(] _[ 𝑛]_ [π]



_𝑟_ 0( _𝑎,𝑏_ )2
( 4 _𝑡_



_𝛾_ [−1)]



+ I 1
) 2



2 [(] _[ 𝑛]_ [π]



_𝛾_ [+1)]



_𝑟_ 0( _𝑎,𝑏_ )2
( 4 _𝑡_



⋅ I 1

[ 2


1− _𝛼_ [2]


_𝛼_



√



_𝛾_ =



⎧
⎪
⎨
⎪⎩



tan [−1] (



π + tan [−1] (



√



1− _𝛼_ [2]


_𝛼_



_if_ _𝛼<_ 0
)



;

_otherwise_
)




- _𝑥_ [1]
_𝑖_ 1+1



_𝜃_ 0 =



⎧
⎪
⎨
⎪⎩



_𝑏_
tan [−1][ (] _𝑎_ - _𝛼𝑍_ 2



_𝑏_
π + tan [−1][ (] _𝑎_ - _𝛼𝑍_ 2



_if_ ( _._ ) _>_ 0
)




- _𝑥_ _[𝑚]_
_𝑖𝑚_ +1



;

_otherwise_
)



⋯

∫

 - _𝑥_ [1] _𝑖_ 1



=



∫

- _𝑥_ _[𝑚]_
_𝑖𝑚_



_𝑓𝑚_ ( _𝑥_ [1] _,_ … _,𝑥_ _[𝑚]_ ) _𝑑𝑥_ [1] … _𝑑𝑥_ _[𝑚]_ _,_ (4)



1

_[𝑏]_ sin( _𝜃_ 0); _𝜎_ ∗ =

_𝜎_ ∗ ~~√~~ 1 −



_𝑟_ 0 = _[𝑏]_



;
1 − _𝛼_ [2]



_𝑥_ _[𝑖]_ [1] ln
min [=] _𝜎_ 1



_𝑥_ _[𝑖]_ [1]
min [=]



_𝑑_ _[𝑖]_
0 [⋅] _[𝑟]_ [min]

_𝑎_ _[𝑖]_
( 0 [⋅] _[𝑒][𝑖]_ 0



)



_,𝑖_ = 1 _,_ 2 _,_



I _𝜇_ ( _𝑧_ ) _is_ _the_ _mod­fied_ _Bessel_ _function_ I _with_ _order_ _𝜇._


_Proof._ Firstly, let’s consider the results from Ref. [29]. It follows that the
probability - f default can be interpreted as the intersection - f the pas­



sage level _𝑥_ _[𝑖]_ min [(] _[𝑡]_ [) =] _𝜎_ [1] [ln] _𝑑𝑎_ 0 _[𝑖]_ _[𝑖]_ [⋅] _[𝑟]_ min _[𝑖]_

( 0 [⋅] _[𝑒][𝑖]_ 0



)



by B _[𝑖]_ _𝑡_ [,] _[𝑖]_ [= 1] _[,]_ [2][,] [and] [from] [the] [condition]



_where_ _𝐷_ _[𝑘]_ _𝑑_ _[𝑘]_
_𝑖𝑘_ [=][ ∑] _𝑗_ ≤ _𝑖𝑘_ _𝑗_ _[.]_


_Proof._ If a certain user defaults, then more and more risky users will
also default. This means that the default - f the first _𝑙_ users in the asset

- ccurs when sup (𝙴 _[𝑘]_ _𝑠_ [−] _[𝑓][𝑘][𝑠]_ [)][ reaches] [values] [from] [−] _[𝑥][𝑚]_ _𝑙_ to - _𝑥_ _[𝑚]_ _𝑙_ +1 [,] [the]
0≤ _𝑠_ ≤ _𝑇_

Eq. (4) follows from this.

In the case  - f _𝑚_ = 1, this can be written as follows:


_𝑃_ (𝙳𝚎𝚏𝚊𝚞𝚕𝚝𝙲𝚘𝚕𝚕𝚊𝚝𝚎𝚛𝚊𝚕𝚜 ∶ _𝐷𝑖_ ) = PD( _𝑥𝑖_ ) − PD( _𝑥𝑖_ +1)


_𝑚_ = 2:


_𝑃_ [(] 𝙳𝚎𝚏𝚊𝚞𝚕𝚝𝙲𝚘𝚕𝚕𝚊𝚝𝚎𝚛𝚊𝚕𝚜 ∶{ _𝐷𝑖_ [1] _[,𝐷]_ _𝑘_ [2][}][)]




- f the theorem, this means that _𝑥_ _[𝑖]_ min [(] _[𝑡]_ [) =] _[ 𝑥][𝑖]_ min [and] _[𝑥][𝑖]_ min [≤] [0][.] [Then] [the]
probability - f default in two assets for the period _𝑇_ is equal:


PD( _𝑥_ [1] min _[,𝑥]_ [2] min [) =] _[ 𝑃]_ [(] _[𝑇]_ _𝑥_ [1] min _[< 𝑇,𝑇][𝑥]_ [2] min _[< 𝑇]_ [)]

= _𝑃_ ( inf0≤ _𝑠_ ≤ _𝑇_ _[𝐵]_ _𝑠_ [1] [≤] _[𝑥]_ [1] min _[,]_ [ inf] 0≤ _𝑠_ ≤ _𝑇_ _[𝐵]_ _𝑠_ [2] [≤] _[𝑥]_ [2] min [)]

= _𝑃_ ( sup _𝐵𝑠_ [1] [≥] [−] _[𝑥]_ [1] min _[,]_ [ sup] _𝐵𝑠_ [2] [≥] [−] _[𝑥]_ [2] min [)] _[,]_
0≤ _𝑠_ ≤ _𝑇_ 0≤ _𝑠_ ≤ _𝑇_


where _𝑇𝐶,𝑓_ = inf{ _𝑡>_ 0 ∶ B _𝑡_ = _𝐶_ }, and the latter equality is true due to
the symmetry - f Brownian motion.

Next, let us look at the results  - f Ref. [51]. In the Main Results 1,
Zhou d­fined the probability equation for the default - f at least - ne
_𝑃_ ( sup _𝐵𝑠_ [1] [≥] [−] _[𝑥]_ [1] min [or] [sup] _𝐵𝑠_ [2] [≥] [−] _[𝑥]_ [2] min [)][.] [From] [here,] [it] [is] [not] [difficult]
0≤ _𝑠_ ≤ _𝑇_ 0≤ _𝑠_ ≤ _𝑇_

to understand that:


_𝐹_ 1 _,_ 2(− _𝑥_ [1] min _[,]_ [−] _[𝑥]_ [2] min [) =] _[ 𝑃]_ [( sup] _𝐵𝑠_ [1] [≤] [−] _[𝑥]_ [1] min [or] [sup] _𝐵𝑠_ [2] [≤] [−] _[𝑥]_ [2] min [)]
0≤ _𝑠_ ≤ _𝑇_ 0≤ _𝑠_ ≤ _𝑇_

= 1 − _𝑃_ ( sup _𝐵𝑠_ [1] [≥] [−] _[𝑥]_ [1] min [or] [sup] _𝐵𝑠_ [2] [≥] [−] _[𝑥]_ [2] min [)]
0≤ _𝑠_ ≤ _𝑇_ 0≤ _𝑠_ ≤ _𝑇_


From here we can get the necessary probability:



**Note** **1.** _In_ _Theorem_ _2,_ _we_ _make_ _the_ _assumption_ _that_ _all_ _levels_ _𝑥_ _[𝑘]_ _𝑖_ _[within]_ _[an]_
_asset_ _𝑘_ = 1 _,_ … _,𝑚_ _are_ _unique._ _To_ _ensure_ _this_ _property,_ _we_ _can_ _first_ _group_
_loans_ _by_ _levels_ _for_ _each_ _asset._


**Corollary** **2.1.** _The_ _probability_ _of_ _a_ _specific_ _liquidation_ _value_ _occurring_ _is:_


_𝑃_ (𝙻𝚒𝚚𝚞𝚒𝚍𝚊𝚝𝚒𝚘𝚗𝚅𝚊𝚕𝚞𝚎 = _𝑋_ ) =

∑ _𝑃_ (𝙳𝚎𝚏𝚊𝚞𝚕𝚝𝙲𝚘𝚕𝚕𝚊𝚝𝚎𝚛𝚊𝚕𝚜 ∶{ _𝐷𝑖_ _[𝑘]_ _𝑘_ _[,𝑘]_ [= 1] _[,]_ […] _[,𝑚]_ [}] ) _._ (5)


_𝑚_
_𝑖_ 1 _,_ … _,𝑖𝑚_ ∶ _𝑘_ ∑=1 _𝐷𝑖𝑘_ _[𝑘]_ [=] _[𝑋]_




- _𝑥_ [2] - _𝑥_ [1]
_𝑘_ +1 _𝑖_ +1



∫

- _𝑥_ [1] _𝑖_



=



∫

- _𝑥_ [2] _𝑘_



_𝑓_ 2( _𝑥_ [1] _,𝑥_ [2] ) _𝑑𝑥_ [1] _𝑑𝑥_ [2]



4


_I. Melnikov,_ _I. Lebedeva,_ _A. Petrov_ _et_ _al._



_Blockchain: Research and Applications 6 (2025) 100259_



**Fig.** **1.** The results - f comparing the theory with the Monte Carlo modulation method for different interest rates _𝑓_, for _𝑥_ [1] min [=] _[ 𝑥]_ [2] min [=] _[ 𝑥]_ [min][ and] _[𝛼]_ [= 0] _[.]_ [8][.]



**Table** **1**

The Shapiro-Wilk test for the normality    - f BTC exchange rate
increments for different time periods. The time series    - f the ex­
change rate from the beginning    - f BTC trading (2014-09-17) to
the present (2024-03-29) is considered.


Duration: 100 days 3 years For all time


Shapiro-Wilk statistics 0.959 0.942 0.909
_𝑝_ value 0.004 2 _._ 63 ⋅ 10 [−20] 2 _._ 72 ⋅ 10 [−35]


Theorem 2 has been proven for the case where the joint distribution

- f the supremums - f _𝑚_ assets is known. However, the theoretical distri­
bution result has - nly been - btained for _𝑚_ = 2 in Theorem 1. To bridge
this gap, it is feasible to estimate the joint distribution for _𝑚>_ 2 through
statistical modeling.


**5.** **Numerical** **experiments**


In this section, we validate theoretical results by applying them to
synthetic and real data.


_5.1._ _Synthetic_ _data_


As synthetic data, we consider the Brownian motions from Theo­
rem 1, the coefficients for which we calculate from the exchange rates

- f real data.


_5.1.1._ _Approximation_

Theorem 1 suggests that two assets can be described by Brownian
motion, with the second asset being a linear combination - f the first
asset and another independent Brownian motion. In this section, we
will test the normality - f the increases in the real exchange rates - f BTC
and calculate the coefficient _𝛼_ BTC-ETH for the relationship between the

two assets.


To test the normality  - f increments, we will use the Shapiro-Wilk
statistical test - n varying time periods. Specifically, we will analyze the
BTC exchange rate - ver different durations. The dataset includes ex­
change rate values from the inception - f BTC trading (2014-09-17) to
the current date (2024-03-29). The results - f the test are summarized in

Table 1.


The findings suggest that labeling the exchange rate as a Brown­
ian motion may be challenging. However, it serves as a fundamental
concept in financial mathematics, and even with potential model inac­
curacies, we can still derive meaningful insights. Future research will
delve deeper into the distribution - f increments in cryptocurrency ex­
change rates.

To calculate the coefficient _𝛼_, which relates the exchange rates  - f
two assets, we need to determine the covariance between the normal­
ized exchange rates - f these assets. Let us take BTC as the first underlying
asset with the highest capitalization, and ETH as the second asset. The



**Table** **2**

The coefficients       - f the relationship       - f Brownian
movements in the context       - f BTC-ETH.


Duration: 100 days 3 years For all time


_𝛼_ BTC-ETH 0.8007 0.8415 0.7922


**Table** **3**

The root mean square error (RMSE) and mean bias
error (MBE) for theoretical and experimental data.


_𝑓_ = 0 _𝑓_ = 0 _._ 01 _𝑓_ = 0 _._ 05 _𝑓_ = 0 _._ 1


RMSE 0.0097 0.0112 0.0171 0.0249

MBE      - 0.0059      - 0.0072      - 0.0121      - 0.0179


results for various considered periods are displayed in Table 2. It is ev­
ident from the results that, despite the varying time periods, the assets
exhibit a strong correlation ranging from 0 _._ 79 to 0 _._ 84.


_5.1.2._ _Default_ _of_ _users_ _in_ _different_ _assets_

In the formulation  - f Theorem 2, an assumption posits the inter­
est rate to be zero, an assertion that diverges from practical scenarios.
Nevertheless, it is - bserved that real interest rates typically range be­
tween 1% and 5% per annum. Given the temporal scope - f the current
investigation, which focuses - n the imminent days, the effective interest
rate is hypothesized to diminish further. A comparative analysis will be
conducted to substantiate the validity - f this assumption. This analysis
will juxtapose the theoretical - utcomes derived under the zero-interest
rate assumption against empirical results - btained through the appli­
cation - f the Monte Carlo simulation method. Specifically, the Monte
Carlo simulation will incorporate Brownian motion to model exchange
rates, utilizing the coefficients delineated in Section 5.1.1. The results
for different interest rates _𝑓_ which equal the passage levels in both as­
sets for _𝑥_ [1] [shown] [in] [Fig.] [1][.] [The] [root] [mean] [square]
min [=] _[ 𝑥]_ [2] min [=] _[ 𝑥]_ [min][ are]
error (RMSE) and mean bias error (MBE) metrics for the theoretical re­
sult are presented in Table 3. Based - n the results, it can be seen that the
zero interest rate approximation holds, as the discrepancy is negligible
for the interest rates - ffered by the MakerDAO protocol.


_5.1.3._ _Risk_ _assessment_


Theorem 2 and its Corollary 2.1 allow us to calculate the dis­
tribution function for the default amount _𝑃_ (𝙻𝚒𝚚𝚞𝚒𝚍𝚊𝚝𝚒𝚘𝚗𝚅𝚊𝚕𝚞𝚎 ≥
𝚂𝚑𝚊𝚛𝚎𝙾𝚏𝙰𝚜𝚜𝚎𝚝𝚜). The result - f calculating the complementary cumula­

tive distribution function for _𝑛_ = 20 users in each - f the two resources
with equal levels, for _𝑥_ [1] min [=] _[ 𝑥]_ [2] min [∈{−0] _[.]_ [1] _[𝑘]_ [|] _[𝑘]_ [= 0] _[,]_ […] _[,]_ [10}][,] [equal] [the]
debt - f each user, _𝑓_ = 0 _._ 05 and _𝛼_ = 0 _._ 8 are shown in Fig. 2.



5


_I. Melnikov,_ _I. Lebedeva,_ _A. Petrov_ _et_ _al._



_Blockchain: Research and Applications 6 (2025) 100259_



**Fig.** **2.** Complementary cumulative distribution function for _𝑛_ = 20 users in each - f two assets with equal levels, for _𝑥_ [1] min [=] _[ 𝑥]_ [2] min [∈{−0] _[.]_ [1] _[𝑘]_ [|] _[𝑘]_ [= 0] _[,]_ […] _[,]_ [10}][,] _[𝑓]_ [= 0] _[.]_ [05][ and]
_𝛼_ = 0 _._ 8.


**Fig.** **3.** The total number                             - f borrowed DAI for asset.



_5.2._ _Real_ _data_


_5.2.1._ _Data_ _structure_


To illustrate the above mathematical theorems  - n real data, we used
public data located in the Google Big Query project. Since we concen­
trate - n various assets in this research, the assets with the largest amount

- f debt (Fig. 3) were selected for the demonstration:


  - ETH-C collateralized risk programs A, B, and C (ETH-A, ETH-B,
and ETH-C accordingly) within the MakerDAO protocol deployed

  - n the Ethereum network debts;

 - Wrapped Bitcoin WBTC-A is a tokenized addition to the cryptocur­

rency space that allows participation in transactions within the
ecosystem   - f DeFi;

  - Gelato Network’s Uniswap V3 token  - f the liquidity provider
(GUNIV3DAIUSDC2-A).


We analyzed the data from November 2019 to July 2023 (see Fig. 4).
Each asset contains its - wn parameters common to all users. Such pa­
rameters are the log interest rate _𝑓_ ( _𝑡_ ), exchange rate _𝑒_ ( _𝑡_ ), and minimal
collateral ratio _𝑟_ min( _𝑡_ ). These parameters may change - ver time as de­
cided by Oracles - r Maker (MKR) token holders.



In raw data, information about user actions is determined by special
functions (such as _𝑓𝑟𝑜𝑏_, _𝑓𝑜𝑟𝑘_, and _𝑔𝑟𝑎𝑏_ ). If a user’s action is labeled as
_𝑓𝑟𝑜𝑏_, it means that the user generates dai/payback DAI or lock/unlock
assets; the _𝑓𝑜𝑟𝑘_ function is responsible for transferring assets and debt
between vaults, and the _𝑔𝑟𝑎𝑏_ function d­fines the liquidation process.
The data - btained from BigQuery contains - nly information about the
user’s actions, the amount - f borrowed DAI, and collateral. Additional
data were processed to - btain the parameters - f each program. For a
more detailed - verview - f data decoding and to - btain the final loan
portfolio dataset, you can refer to GitHub [(https://github.com/swnirk/](https://github.com/swnirk/DeFi-Risk-Assessment-MakerDAO-Loan-Portfolio-Case)
[DeFi-Risk-Assessment-MakerDAO-Loan-Portfolio-Case).](https://github.com/swnirk/DeFi-Risk-Assessment-MakerDAO-Loan-Portfolio-Case)


_5.2.2._ _Default_ _of_ _one_ _user_ _in_ _one_ _asset_

We conducted a series  - f experiments to assess how well theoretical
considerations are suited for real-life data analysis. In - rder to check
it, we calculated the actual number - f defaults a day ahead, together
with the predictions from the Brownian motion mathematical model.
To calculate it we used the results from the Ref. [29]:



_𝑡_



_𝑥_ min  - _𝑓𝑇_
( _𝜎_ ~~√~~ _𝑡_



)]



_𝑥_ min + _𝑓𝑇_
( _𝜎_ ~~√~~ _𝑡_



)]



1 −Φ

[



+



PD _𝐵_ ( _𝑇_ ) = _𝑒_



2 _𝑓𝑥_ min

_𝜎_ [2] ⋅



_𝜎_ ~~√~~ _𝑡_



1 −Φ

[



_,_



_𝜎_ ~~√~~ _𝑡_



_𝑡_



6


_I. Melnikov,_ _I. Lebedeva,_ _A. Petrov_ _et_ _al._



_Blockchain: Research and Applications 6 (2025) 100259_


**Fig.** **4.** Dependence          - f borrowed DAI on date for each asset.


**Table** **4**

Performance metrics for different mathematical models.


Asset Poisson model Brownian model


MSE MAE TV KL MSE MAE TV KL


ETH-A 0.048 0.113 0.057 0.744 **0.047** **0.005** **0.024** **0.046**

ETH-B **0.167** 0.217 0.108 0.794 0.173 **0.181** **0.090** **0.175**

ETH-C **0.049** 0.091 0.046 0.818 0.050 **0.050** **0.025** **0.050**

WBTC-A **0.004** **0.061** **0.031** 0.769 0.115 0.116 0.058 **0.115**

GUNIV3DAIUSDC2-A **0.004** 0.031 0.016 0.872 **0.004** **0.004** **0.002** **0.004**



where _𝑥𝑚𝑖𝑛_ is the passage level - f the definite user and _𝑓_ is a log inter­
est rate at the current time moment (the day before the time moment
_𝑇_ ). For comparison, we also considered the Poisson model since it is a
baseline in classical finance. This model assumes all debts are indepen­
dent and have an exponential distribution with an unknown parameter
_𝜆>_ 0. Thus, the probability - f default for a single debt during time _𝑇_,
PD _𝑃_ ( _𝑇_ ) = 1 − _𝑒_ [−] _[𝜆𝑇]_ . The assumptions are also taken from the Ref. [29].

To compare the fit  - f models to the real data, we use the following
metrics:


 - Mean squared error (MSE) and Mean absolute error (MAE) are mean

   - f squared and absolute differences between the   - bserved and pre­
dicted values.

  - Total variation (TV) measures the discrepancy between two prob­

ability distributions. It is d­fined as half the sum   - f the absolute
differences between the corresponding probabilities in the two dis­
tributions.

  - Kullback-Leibler divergence (KL) measures the discrepancy be­

tween two probability distributions. It determines the amount   - f
information lost by using   - ne distribution to approximate the   - ther.


The results  - f calculating default probabilities for the Poisson and
Brownian motion models were taken as predicted data, while the true
values were - btained by comparing the collateral-to-debt ratio _𝑟_ for the
definite user with the minimal collateral ratio _𝑟𝑚𝑖𝑛_ . In the case - f _𝑟< 𝑟𝑚𝑖𝑛_
user is marked as defaulted. For each metric, a smaller value indicates a
better fit - f the theoretical model to the empirical data. Let us compare
the - btained results.


Table 4 shows the result  - f comparing two mathematical models for
different assets. For each asset, the best results are highlighted in bold.
As can be seen that in most cases the Brownian motion model gives more
accurate and reliable forecasts. This result can be explained by the fact
that in the case - f the Poisson model, all debts are assumed to be in­
dependent. However, for the Maker data, this assumption is incorrect



because all debts - f the same asset are based - n the same type - f col­
lateral but with different collateralization ratios. In the case - f WBTC-A,
the Poisson model shows better result, this may be due to the fact that
the Poisson model more effectively captures the likelihood - f sudden,
discrete price jumps that are characteristic - f Bitcoin’s volatility.


_5.2.3._ _Default_ _of_ _users_ _in_ _different_ _assets_

As it was shown in the previous paragraph 5.2.2, the Brownian mo­
tion model most accurately describes the behavior - f users in real life,
so we chose this model for further experiments. To calculate the prob­
ability - f default - f a share _𝑥_ in two assets, we used Corollary 2.1. The
Fig. 5 shows the probability - f a random process to reach threshold _𝑥_
for different time intervals, such as - ne day, - ne month, and - ne year.
For the experiment, portfolios - f different users at the same moment in
time were taken from the ETH-A and WBTC-A assets. As the time hori­

zon increases, the probability - f default - f share _𝑥_ increases, which is
consistent with real logical considerations. Since the exchange rate and
the annual interest rate usually increase, the default probability - f the
user will also increase day by day, in case they stop replenishing their
balance, securing themselves against liquidation.

Thus, we estimated the default risks  - f two programs at  - nce, using
real loan portfolios. In reality, the default risk is even smaller due to
the presence - f more users and - ther programs. The proposed method

- f risk assessment is not sufficient to use in real life, but it serves as a
good tool to prevent dangerous situations for the platform.


**6.** **Conclusions**


DeFi presents a new frontier in the financial world,  - ffering inno­
vative Web3-based products as well as mimic for traditional financial
instruments. However, the lack - f regulation in DeFi has raised concerns
about potential risks such as fraud, scams, and security vulnerabilities.
While some qualitative risk assessments have been conducted - n DeFi



7


_I. Melnikov,_ _I. Lebedeva,_ _A. Petrov_ _et_ _al._



_Blockchain: Research and Applications 6 (2025) 100259_


**Fig.** **5.** Probability - f default - f a share ≥ _𝑥_ - f two assets (ETH-A and WBTC-A).



protocols, there is a need for more robust mathematical models to eval­

uate risk.


One prominent DeFi project is Maker, a blockchain protocol that fa­
cilitates crypto-backed loans. The - bjective - f - ur current research is
to evaluate the risk associated with MakerDAO’s loan portfolio. In - r­
der to accomplish this, we have expanded upon a mathematical model
specifically designed for DeFi loans to incorporate a variety - f collateral
types, as - utlined in Theorems 1 and 2. Theorem 1 enables the calcula­
tion - f the joint distribution - f default probabilities for two borrowers,
each with their - wn type - f collateral. Theorem 2 provides a way to de­
termine the probability - f a certain portion - f the portfolio defaulting.

We tested  - ur theoretical models using art­ficial data generated by

- ur simulator, which is based - n Brownian motion modeling. Subse­
quently, we applied these theorems to real data from MakerDAO, span­
ning from its launch in November 2019 to July 2023. Our findings
indicate that there is a potential for the loan portfolio to default within

a reasonable timeframe.


The research has several limitations that prevent its real-life appli­
cation. Firstly, Maker is not solely focused - n loans, so its - perational
stability is i­fluenced by various factors, including the stability - f the
loan portfolio. Secondly, the proposed model is based - n strong assump­
tions, such as the collateral price following an unshifted Brownian mo­
tion and borrowers not taking any actions to avoid defaults during the
spec­fied period. These assumptions are unlikely to hold, as evidenced
by statistical testing and user - peration history. However, - ur model has
the potential to - ffer quantitative insights into the protocol’s risk. Ad­
ditionally, incorporating models - f Brownian motion with jumps could
enhance the model’s accuracy and may be considered for future work,
although - btaining theoretical results for such a model will be challeng­

ing.

Our model draws inspiration from Maker’s loan portfolio and is eval­
uated using its data. However, it’s important to note that - ther DeFi
projects such as AAVE, Compound, and Spark Lend also have loan port­
folios. Although the - perational principles - f DeFi lending are similar,
the specific details and smart contracts may vary depending - n differ­
ent protocols. This presents a challenge for data collection and model
transfer when analyzing - ther protocols in future research.

The Brownian motion model, while parametric and interpretable,
lacks certain crucial aspects such as user activity. With DeFi usage
data being publicly available, data-driven machine learning models hold
promise for providing more accurate default probability predictions.

Our research underscores the importance  - f conducting thorough
risk assessments in DeFi projects and emphasizes the need for further
exploration - f risk evaluation methodologies across a range - f DeFi pro­

tocols.



**CRediT** **authorship** **contribution** **statement**


**Ignat** **Melnikov:** Conceptualization, Data curation, Formal analysis,
Investigation, Methodology, Software, Validation, Visualization, Writ­
ing - - - riginal draft, Writing - - review & editing. **Irina** **Lebedeva:** Concep­
tualization, Data curation, Formal analysis, Investigation, Methodology,
Software, Validation, Visualization, Writing - - - riginal draft, Writing - review & editing. **Artem** **Petrov:** Conceptualization, Validation, Writing

- review & editing. **Yury** **Yanovich:** Conceptualization, Formal analysis,
Investigation, Methodology, Supervision, Validation, Writing - - - riginal
draft, Writing - - review & editing.


**Declaration** **of** **generative** **AI** **and** **AI-assisted** **technologies** **in** **the**
**writing** **process**


During the preparation  - f this work the authors used ChatGPT in

- rder to enhance the English language and readability - f the paper. After
using this tool/service, the authors reviewed and edited the content as
needed and take full responsibility for the content - f the publication.


**Declaration** **of** **competing** **interest**


The authors declare that they have no known competing financial
interests - r personal relationships that could have appeared to i­fluence
the work reported in this paper.


**References**


[1] D.A. Zetzsche, D.W. Arner, R.P. Buckley, Decentralized finance (DeFi), J. Finance
Regul. 6 (2) (2020), [https://doi.org/10.2139/ssrn.3539194.](https://doi.org/10.2139/ssrn.3539194)

[2] F. Schär, Decentralized finance: - n blockchain- and smart contract-based financial
markets, Rev. Fed. Reserv. Bank   - f St Louis 103 (2) (2021) 153--174, [https://doi.](https://doi.org/10.20955/r.103.153-74)

[org/10.20955/r.103.153-74.](https://doi.org/10.20955/r.103.153-74)

[3] V. Buterin, On public and private blockchains - Ethereum blog, [https://blog.](https://blog.ethereum.org/2015/08/07/on-public-and-private-blockchains/)

[ethereum.org/2015/08/07/on-public-and-private-blockchains/,](https://blog.ethereum.org/2015/08/07/on-public-and-private-blockchains/) 2015. (Accessed 6
December 2024).

[4] V. Rossikhin, M. Burdin, O. Mykhalskyi, Legal regulation issues - f cryptocurrency
circulation in Ukraine, Balt. J. Econ. Stud. 4 (3) (2018) 254--258, [https://doi.org/](https://doi.org/10.30525/2256-0742/2018-4-3-254-258)

[10.30525/2256-0742/2018-4-3-254-258.](https://doi.org/10.30525/2256-0742/2018-4-3-254-258)

[5] B.D. Feinstein, K. Werbach, The impact - f cryptocurrency regulation - n trading mar­

kets, SSRN Electron. J. 7 (1) (2021) 48--99, [https://doi.org/10.2139/SSRN.3649475,](https://doi.org/10.2139/SSRN.3649475)
[https://doi.org/10.1093/jfr/fjab003.](https://doi.org/10.1093/jfr/fjab003)

[6] S.A. Lee, G. Milunovich, Digital exchange attributes and the risk - f closure,
Blockchain Res. Appl. 4 (2) (2023) 100131, [https://doi.org/10.1016/j.bcra.2023.](https://doi.org/10.1016/j.bcra.2023.100131)

[100131.](https://doi.org/10.1016/j.bcra.2023.100131)

[7] W. Chen, Z. Zheng, E.C.-H. Ngai, et al., Exploiting blockchain data to detect smart
Ponzi schemes   - n Ethereum, IEEE Access 7 (2019) 37575--37586, [https://doi.org/](https://doi.org/10.1109/ACCESS.2019.2905769)

[10.1109/ACCESS.2019.2905769.](https://doi.org/10.1109/ACCESS.2019.2905769)

[8] L. Galletta, F. Pinelli, Sharpening Ponzi schemes detection - n Ethereum with ma­

chine learning, in: Proceedings   - f the 39th ACM/SIGAPP Symposium   - n Applied
Computing (SAC), ACM, 2024, pp. 1014--1023, [https://doi.org/10.1145/3605098.](https://doi.org/10.1145/3605098.3636060)

[3636060.](https://doi.org/10.1145/3605098.3636060)



8


_I. Melnikov,_ _I. Lebedeva,_ _A. Petrov_ _et_ _al._


[9] T. Hu, X. Liu, T. Chen, et al., Transaction-based class­fication and detection approach
for Ethereum smart contract, Inf. Process. Manag. 58 (2) (2021) 102462, [https://](https://doi.org/10.1016/j.ipm.2020.102462)
[doi.org/10.1016/j.ipm.2020.102462.](https://doi.org/10.1016/j.ipm.2020.102462)

[10] S. Srifa, Y. Yanovich, A.S. S, et al., Scam token class­fication for decentralized ex­

change using transaction data, SSNR, 2023, [https://doi.org/10.2139/ssrn.4582918.](https://doi.org/10.2139/ssrn.4582918)

[11] Basel Committee - n Banking Supervision, The Basel Framework, Bank for Interna­

tional Settlements, 2022, [https://www.bis.org/basel_framework/.](https://www.bis.org/basel_framework/) (Accessed 6 De­
cember 2024).

[12] E. Meyer, I.M. Welpe, P. Sandner, Decentralized Finance—a Systematic Literature
Review and Research Directions, in: Proceedings   - f the International Conference   - n
Electronics, Communications and Intelligent Science, IEEE, 2022, [https://doi.org/](https://doi.org/10.2139/ssrn.4016497)

[10.2139/ssrn.4016497.](https://doi.org/10.2139/ssrn.4016497)

[13] N.F. Samreen, M.H. Alalfi, An empirical study - n the complexity, security and main­

tainability    - f Ethereum-based decentralized applications (DApps), Blockchain Res.
Appl. 4 (2) (2023) 100120, [https://doi.org/10.1016/j.bcra.2022.100120.](https://doi.org/10.1016/j.bcra.2022.100120)

[14] J. Xu, K. Paruch, S. Cousaert, et al., SoK: decentralized exchanges (DEX) with au­

tomated market maker (AMM) protocols, ACM Comput. Surv. 55 (11) (2023) 1--50,
[https://doi.org/10.1145/3570639.](https://doi.org/10.1145/3570639)

[15] B. Group, On blockchain auditability, bitfury.com, 2016, pp. 1--40, [https://bitfury.](https://bitfury.com/content/downloads/bitfury_white_paper_on_blockchain_auditability.pdf)

[com/content/downloads/bitfury_white_paper_on_blockchain_auditability.pdf.](https://bitfury.com/content/downloads/bitfury_white_paper_on_blockchain_auditability.pdf) (Ac­
cessed 6 December 2024).

[16] P.D. Filippi, C. Wray, G. Sileno, Smart contracts, Internet Policy Rev. 10 (2) (2021)
1--9, [https://doi.org/10.14763/2021.2.1549.](https://doi.org/10.14763/2021.2.1549)

[17] V. Buterin, Ethereum white paper: a next generation smart contract & decentralized
application platform, Ethereum (2014) 1--36, [https://github.com/ethereum/wiki/](https://github.com/ethereum/wiki/wiki/White-Paper)
[wiki/White-Paper.](https://github.com/ethereum/wiki/wiki/White-Paper) (Accessed 6 December 2024).

[18] J. Poon, T. Dryja, The bitcoin lightning network: scalable - ff-chain instant payments,

[https://lightning.network/lightning-network-paper.pdf,](https://lightning.network/lightning-network-paper.pdf) 2016. (Accessed 6 Decem­
ber 2024).

[19] P. Prihodko, S. Zhigulin, M. Sahno, et al., Flare: an approach to routing
in lightning network, [https://bitfury.com/content/downloads/whitepaper_flare_an_](https://bitfury.com/content/downloads/whitepaper_flare_an_approach_to_routing_in_lightning_network_7_7_2016.pdf)
[approach_to_routing_in_lightning_network_7_7_2016.pdf,](https://bitfury.com/content/downloads/whitepaper_flare_an_approach_to_routing_in_lightning_network_7_7_2016.pdf) 2016. (Accessed 6 Decem­
ber 2024).

[20] V. Buterin, The limits to blockchain scalability, [https://vitalik.ca/general/2021/05/](https://vitalik.ca/general/2021/05/23/scaling.html)

[23/scaling.html,](https://vitalik.ca/general/2021/05/23/scaling.html) 2021. (Accessed 6 December 2024).

[21] S. Kruglik, K. Nazirkhanova, Y. Yanovich, Challenges Beyond Blockchain: Scaling,
Oracles and Privacy Preserving, in: Proceedings   - f the 2019 XVI International Sym­
posium ``Problems   - f Redundancy in Information and Control Systems'' (REDUN­
DANCY), IEEE, 2019, pp. 155--158, [https://doi.org/10.1109/REDUNDANCY48165.](https://doi.org/10.1109/REDUNDANCY48165.2019.9003331)

[2019.9003331.](https://doi.org/10.1109/REDUNDANCY48165.2019.9003331)

[22] V. Amelin, E. Gatiyatullin, N. Romanov, et al., Black-box for blockchain parame­

ters adjustment, IEEE Access 10 (2022) 101795--101802, [https://doi.org/10.1109/](https://doi.org/10.1109/ACCESS.2022.3208702)

[ACCESS.2022.3208702.](https://doi.org/10.1109/ACCESS.2022.3208702)

[23] MakerDAO, The maker protocol: MakerDAO’s multi-collateral Dai (MCD) system,

[https://makerdao.com/whitepaper/,](https://makerdao.com/whitepaper/) 2020. (Accessed 6 December 2024).

[24] E. Ben-Sasson, A. Chiesa, C. Garman, et al., Zerocash: Practical Decentralized Anony­

mous e-Cash from Bitcoin, IEEE, 2014, pp. 459--474, [https://doi.org/10.1109/SP.](https://doi.org/10.1109/SP.2014.36)

[2014.36.](https://doi.org/10.1109/SP.2014.36)

[25] B. Bunz, J. Bootle, D. Boneh, et al., Bulletproofs: Short Proofs for Co­fidential Trans­

actions and More, in: Proceedings   - f the 2018 IEEE Symposium   - n Security and
Privacy (SP), IEEE, 2018, pp. 315--334, [https://doi.org/10.1109/SP.2018.00020.](https://doi.org/10.1109/SP.2018.00020)

[26] D. Korepanova, M. Nosyk, A. Ostrovsky, et al., Building a Private Currency Service
Using Exonum, in: Proceedings   - f the 2019 IEEE International Black Sea Conference

  - n Communications and Networking (BlackSeaCom), IEEE, 2019, pp. 1--3, [https://](https://doi.org/10.1109/BlackSeaCom.2019.8812875)
[doi.org/10.1109/BlackSeaCom.2019.8812875.](https://doi.org/10.1109/BlackSeaCom.2019.8812875)

[27] N. Carter, L. Jeng, Defi protocol risks: the paradox - f defi, SSRN Electron. J. (2021),

[https://doi.org/10.2139/ssrn.3866699.](https://doi.org/10.2139/ssrn.3866699)

[28] OECD, Lessons from the crypto winter: Defi versus cefi, in: OECD Business and
Finance Policy Papers, 2022, pp. 1--46, [https://www.oecd.org/en/publications/](https://www.oecd.org/en/publications/lessons-from-the-crypto-winter_199edf4f-en.html)
[lessons-from-the-crypto-winter_199edf4f-en.html.](https://www.oecd.org/en/publications/lessons-from-the-crypto-winter_199edf4f-en.html) (Accessed 6 December 2024).

[29] Y. Chaleenutthawut, V. Davydov, M. Evdokimov, et al., Loan portfolio dataset from
makerdao blockchain project, IEEE Access 12 (2024) 24843--24854, [https://doi.org/](https://doi.org/10.1109/ACCESS.2024.3363225)

[10.1109/ACCESS.2024.3363225.](https://doi.org/10.1109/ACCESS.2024.3363225)

[30] J. Bertomeu, X. Martin, I. Sall, Measuring defi risk, Finance Res. Lett. 63 (2024)
105321, [https://doi.org/10.1016/j.frl.2024.105321.](https://doi.org/10.1016/j.frl.2024.105321)

[31] F. Vogelsteller, V. Buterin, EIP-20: ERC-20 Token Standard, [https://github.com/](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md)

[ethereum/EIPs/blob/master/EIPS/eip-20.md,](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md) 2015. (Accessed 6 December 2024).



_Blockchain: Research and Applications 6 (2025) 100259_


[32] V. Makri, A. Tsagkanos, A. Bellas, Determinants - f non-performing loans: the case - f
Eurozone, Panoeconomicus 61 (2) (2014), [https://doi.org/10.2298/pan1402193m.](https://doi.org/10.2298/pan1402193m)

[33] A. Khairi, B. Bahri, B. Artha, A literature review - f non-performing loan, J. Bus.
Manag. Rev. 2 (5) (2021), [https://doi.org/10.47153/jbmr25.1402021.](https://doi.org/10.47153/jbmr25.1402021)

[34] Fahmida-E-Moula, N.A. Shilpa, P. Shaha, et al., Default Risk Prediction Based - n Sup­

port Vector Machine and Logit Support Vector Machine, in: M.Z. Abedin, P. Hajek,
et al. (Eds.), Novel Financial Applications    - f Machine Learning and Deep Learning.
International Series in Operations Research & Management Science., Springer Inter­
national Publishing, 2023, pp. 93--106, [https://doi.org/10.1007/978-3-031-18552-](https://doi.org/10.1007/978-3-031-18552-6_6)

[6_6.](https://doi.org/10.1007/978-3-031-18552-6_6)

[35] E. Hayden, D. Porath, N.V. Westernhagen, Does divers­fication improve the perfor­

mance   - f German banks? Evidence from individual bank loan portfolios, J. Financ.
Serv. Res. 32 (3) (2007), [https://doi.org/10.1007/s10693-007-0017-0.](https://doi.org/10.1007/s10693-007-0017-0)

[36] S.P. Rossi, M.S. Schwaiger, G. Winkler, How loan portfolio divers­fication affects
risk, efficiency and capitalization: a managerial behavior model for Austrian banks,
J. Bank. Finance 33 (12) (2009), [https://doi.org/10.1016/j.jbankfin.2009.05.022.](https://doi.org/10.1016/j.jbankfin.2009.05.022)

[37] S.I. Serengil, S. Imece, U.G. Tosun, et al., A comparative study - f machine learning
approaches for non performing loan prediction, in: Proceedings   - f the 2021 6th In­
ternational Conference    - n Computer Science and Engineering, (UBMK), IEEE, 2021,
[https://doi.org/10.1109/UBMK52708.2021.9558894.](https://doi.org/10.1109/UBMK52708.2021.9558894)

[38] M. Annisa, Rusdah, Prediction - f non-performing loans for credit application anal­

ysis    - f rural bank using random forest, in: Proceeding    - f the 2022 9th international
Conference   - n Electrical Engineering, Computer Science and Informatics (EECSI),
IEEE, 2022, pp. 111--114, [https://doi.org/10.23919/EECSI56542.2022.9946628.](https://doi.org/10.23919/EECSI56542.2022.9946628)

[39] V.A. Davydov, S.A. Kruglik, Y.A. Yanovich, Comparison - f banking and peer-to-peer
lending risks, Autom. Remote Control 82 (12) (2021) 2155--2168, [https://doi.org/](https://doi.org/10.1134/S0005117921120079)

[10.1134/S0005117921120079.](https://doi.org/10.1134/S0005117921120079)

[40] V.A. Davydov, S.A. Kruglik, Y.A. Yanovich, Probability - f the default-free state for
token package from independent loans, J. Commun. Technol. Electron. 67 (6) (2022)
778--786, [https://doi.org/10.1134/S1064226922060122.](https://doi.org/10.1134/S1064226922060122)

[41] F. Schar, Decentralized finance: - n blockchain- and smart contract-based financial
markets, Review 103 (2) (2021) 153--174, [https://doi.org/10.20955/r.103.153-74.](https://doi.org/10.20955/r.103.153-74)

[42] A. Som, P. Kayal, A multicountry comparison - f cryptocurrency vs gold: portfolio

   - ptimization through generalized simulated annealing, Blockchain Res. Appl. 3 (3)
(2022) 100075, [https://doi.org/10.1016/j.bcra.2022.100075.](https://doi.org/10.1016/j.bcra.2022.100075)

[43] B. Kaplan, V.F. Benlı, E. Aykaç Alp, Blockchain based decentralized lending pro­

tocols: a return analysis between s&p 500 and defi assets, J. Emerg. Econ. Policy
8 (1) (2023) 360--378, [https://dergipark.org.tr/en/download/article-file/2989413.](https://dergipark.org.tr/en/download/article-file/2989413)
(Accessed 6 December 2024).

[44] M. Kjaer, M. Di Angelo, G. Salzer, Empirical evaluation - f MakerDAO’s resilience,
in: Proceeding    - f the 2021 3rd Conference    - n Blockchain Research and Applications
for Innovative Networks and Services, (BRAINS), IEEE, 2021, pp. 193--200, [https://](https://doi.org/10.1109/BRAINS52497.2021.9569811)
[doi.org/10.1109/BRAINS52497.2021.9569811.](https://doi.org/10.1109/BRAINS52497.2021.9569811)

[45] AAVE, AAVE Protocol Whitepaper v1.0, Github, December 2020, pp. 1--21, [https://](https://github.com/aave/prhttps://github.com/aave/aave-protocol/blob/master/docs/Aave_Protocol_Whitepaper_v1_0.pdf)

[github.com/aave/prhttps://github.com/aave/aave-protocol/blob/master/docs/](https://github.com/aave/prhttps://github.com/aave/aave-protocol/blob/master/docs/Aave_Protocol_Whitepaper_v1_0.pdf)
[Aave_Protocol_Whitepaper_v1_0.pdf.](https://github.com/aave/prhttps://github.com/aave/aave-protocol/blob/master/docs/Aave_Protocol_Whitepaper_v1_0.pdf) (Accessed 6 December 2024).

[46] R. Leshner, G. Hayes, Compound: the Money Market Protocol, compound.finance,
2019, pp. 1--8, [https://compound.finance/documents/Compound.Whitepaper.pdf.](https://compound.finance/documents/Compound.Whitepaper.pdf)
(Accessed 6 December 2024).

[47] J.A.L. Escamilla, Y. Yanovich, Data mining - f compound DeFi project, in: Proceed­

ings   - f the 2022 5th International Conference   - n Blockchain Technology and Appli­
cations, 2022, pp. 16--23, [https://doi.org/10.1145/3581971.3581974.](https://doi.org/10.1145/3581971.3581974)

[48] T. Azoulay, U. Carl, O. Rottenstreich, Allowing blockchain loans with low collateral,
in: Proceedings    - f the 2023 IEEE International Conference    - n Blockchain and Cryp­
tocurrency (ICBC), IEEE, 2023, pp. 1--9, [https://doi.org/10.1109/ICBC56567.2023.](https://doi.org/10.1109/ICBC56567.2023.10174887)

[10174887.](https://doi.org/10.1109/ICBC56567.2023.10174887)

[49] A. Klages-Mundt, A. Minca, While stability lasts: a stochastic model - f noncustodial
stablecoins, Math. Finance 32 (4) (2022) 943--981, [https://doi.org/10.1111/mafi.](https://doi.org/10.1111/mafi.12357)

[12357.](https://doi.org/10.1111/mafi.12357)

[50] R. Huang, J. Chen, Y. Wang, et al., An - verview - f Web3 technology: infrastructure,
applications, and popularity, Blockchain Res. Appl. 5 (1) (2024) 100173, [https://](https://doi.org/10.1016/j.bcra.2023.100173)
[doi.org/10.1016/j.bcra.2023.100173.](https://doi.org/10.1016/j.bcra.2023.100173)

[51] C. Zhou, An analysis - f default correlations and multiple defaults, Rev. Financ. Stud.
14 (2) (2001) 555--576, [http://www.jstor.org/stable/2696751.](http://www.jstor.org/stable/2696751) (Accessed 6 Decem­
ber 2024).



9


