# NOVEL FINANCIAL TECHNOLOGIES FOR STABLECOINS, MARKET STABILITY, AND NETWORK ANALYSIS

A Dissertation


Presented to the Faculty of the Graduate School


            - f Cornell University


in Partial Fulfillment of the Requirements for the Degree of


Doctor of Philosophy


by


Ariah Aram Klages-Mundt


May 2023


© 2023 Ariah Klages-Mundt


ALL RIGHTS RESERVED


NOVEL FINANCIAL TECHNOLOGIES FOR STABLECOINS, MARKET


STABILITY, AND NETWORK ANALYSIS


Ariah Aram Klages-Mundt, Ph.D.


Cornell University 2023


This thesis confronts the challenges of complexity in financial systems, in which


economic questions transform into computer science and mathematical prob

lems. For instance, this occurs when systems have complicated dynamic inter

actions, and when systems are large and direct solution methods are not neces

sarily feasible.


The first part of the thesis focuses on decentralized finance systems, which


leverage new blockchain technologies to replace the role of risky financial in

termediaries with decentralized (and more robust) structures, and the design


- f stablecoins, which aim to be a stable asset in a setting in which USD cannot


be held directly. Decentralized stablecoins aim to function based on incentive


design supported by transparent rules enforced cryptographically, in contrast to


traditional currencies, which are supported by legal and governmental systems.


This work explores new risks that complicate the design of resilient stablecoins,


leading to significant results characterizing stablecoin runs and deleveraging


spirals and new governance risks in decentralized finance protocols.


The second part of this thesis focuses on cascades in economic networks, in


which many firms interact with each other. This work explores new types of


risks that can arise due to network structure and confronts two main issues that


prevent the application of economic network models in practice, namely that


these models can be very sensitive to parameter uncertainty and many aspects


- f these models can be computationally hard to compute. This leads to several


significant results:


  - Characterizing mathematical properties of reinsurance contagion models,


including dangerous structures that lead to retrocession spirals and un

derestimation of risk;


  - Adapting influence maximization methods to the problem of interven

ing in economic network contagion, enabling an NP-hard problem to be


solved approximately in practice;


  - Applying perturbation theory to bound sensitivity in economic networks,


improving on and unifying past results, and providing a means for net

work analysis to be more actionable in practice.


This work involves applying methods from network analysis, perturbation


theory, stochastic processes, agent-based models, game theory, and simulations.


**BIOGRAPHICAL SKETCH**


Ariah conducted his dissertation research at the Center for Applied Mathemat

ics at Cornell University between 2016 and 2023. His research is at the intersec

tion of economics, computer science, and applied mathematics. During his PhD,


Ariah was a Bloomberg Fellow and Commercialization Fellow and published


research in top venues including Management Science, Mathematical Finance,


and the ACM Conference on Computer and Communications Security. Ariah


spent several semesters of his PhD visiting the CFM Imperial Institute of Quan

titative Finance in London, London Business School, and the Chinese University


- f Hong Kong-Shenzhen and working with the Initiative for Cryptocurrencies


and Contracts.


Before starting the PhD, Ariah worked in the financial technology sector in


New York and earned a bachelor’s degree in mathematics at Amherst College in


2012. Ariah also has experience in research and development of smart contract


software.


iii


**ACKNOWLEDGEMENTS**


My PhD work was made possible with support from the Bloomberg Fellowship,


NSF CAREER Award #1653354, NSF RTG Award #1645643, and NSF CRISP


Award #1638230. I also thank Amherst College, the Cornell Commercialization


Fellowship, a Binance Fellowship, and Smart Contract Research Forum for ad

ditional financial support.


I would like to acknowledge a few individuals who were especially forma

tive across my PhD research: Andreea Minca (my advisor), Austin Benson, Stef

fen Schuldenzucker, Christopher Chen, Andrew Horning, Dominik Harz, Lewis


Gudgeon, Daniel Perez, Zhimeng Yang, as well as many members of the Initia

tive for Cryptocurrencies and Contracts (IC3). While I had initially aimed to


complete my PhD quickly, it became such a fun endeavor because of these peo

ple that I ended up continuing it for a total of 7 years.


I would also like to acknowledge all collaborators across my PhD research:


Andreea Minca, Austin Benson, Zhimeng Yang, Lewis Gudgeon, Daniel Perez,


Dominik Harz, Sam Werner, William Knottenbelt, Michael Mirkin, Yan Ji,


Jonathan Pang, Ittay Eyal, Ari Juels, Jun-You Liu, Lucy Huo, Frederik Chris

tian M¨unter, and Mads Rude Wind. I would additionally like to thank my PhD


committee members, Steve Strogatz and Sid Banerjee, as well as Erika Fowler

Decatur, who was always extremely helpful in the administration of CAM.


Not least, I would also like to acknowledge the following individuals who


guided me on the research path through a number of topics to ultimately settle


- n applied mathematics: Paul Gunnells, William Stein, Kreˇsimir Josi´c, William


Loinaz, Toby Dogwiler, Saeed Ziaee, Jeanne Franz, and Ken Mann.


iv


**TABLE OF CONTENTS**


Biographical Sketch . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . iii
Acknowledgements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . iv
Table of Contents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . v


**1** **Introduction** **1**
1.1 Mathematics of stability in decentralized finance . . . . . . . . . . 3
1.1.1 Stability in leverage-based stablecoins. . . . . . . . . . . . 3
1.1.2 Stability in general stablecoins. . . . . . . . . . . . . . . . . 5
1.2 Mathematics of stability in economic networks . . . . . . . . . . . 6
1.2.1 Contagion in reinsurance networks. . . . . . . . . . . . . . 8
1.2.2 Intervention in economic networks. . . . . . . . . . . . . . 9
1.2.3 Sensitivity in economic networks. . . . . . . . . . . . . . . 10
1.3 Impact . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10


**2** **While Stability Lasts: A Stochastic Model of Noncustodial Stablecoins 12**
2.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

2.1.1 Stablecoins . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2.1.2 This paper . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.1.3 Relation to Prior Work . . . . . . . . . . . . . . . . . . . . . 20

2.2 Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
2.2.1 Formal setup . . . . . . . . . . . . . . . . . . . . . . . . . . 25
2.2.2 Collateral constraint . . . . . . . . . . . . . . . . . . . . . . 27
2.2.3 Speculator decides ∆ _t_ taking into account real liability value 28
2.2.4 Speculator’s collateral at stake . . . . . . . . . . . . . . . . 29
2.2.5 Collateral liquidation mechanics . . . . . . . . . . . . . . . 30
2.2.6 System of random variables . . . . . . . . . . . . . . . . . . 32
2.3 Foundational Results . . . . . . . . . . . . . . . . . . . . . . . . . . 33
2.3.1 Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . 34
2.3.2 Concavity and scale invariance . . . . . . . . . . . . . . . . 36
2.3.3 Economic limits to speculator behavior . . . . . . . . . . . 38
2.4 Stable and Unstable Domains . . . . . . . . . . . . . . . . . . . . . 40
2.4.1 Domain barriers/Stopped processes . . . . . . . . . . . . . 40
2.4.2 ‘Stable’ domain . . . . . . . . . . . . . . . . . . . . . . . . . 42

2.4.3 ‘Unstable’ domain . . . . . . . . . . . . . . . . . . . . . . . 48
2.5 Stability in ‘Perfect’ Settings . . . . . . . . . . . . . . . . . . . . . . 56
2.5.1 Perfectly elastic demand . . . . . . . . . . . . . . . . . . . . 57
2.5.2 Unlimited speculator capital supply . . . . . . . . . . . . . 58
2.5.3 No stable region if ( _Xt_ ) is not a submartingale . . . . . . . 58
2.6 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
2.7 Appendix: Proofs . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65


v


**3** **(In)Stability for the Blockchain: Deleveraging Spirals and Stablecoin**
**Attacks** **78**

3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
3.1.1 Non-custodial (decentralized) stablecoins . . . . . . . . . . 82
3.1.2 Relation to prior work . . . . . . . . . . . . . . . . . . . . . 86
3.1.3 This paper . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
3.2 Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92

3.2.1 Stablecoin holder . . . . . . . . . . . . . . . . . . . . . . . . 95
3.2.2 Speculator . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
3.2.3 DStablecoin market clearing . . . . . . . . . . . . . . . . . . 103
3.3 Stable Asset Market Dynamics . . . . . . . . . . . . . . . . . . . . 105
3.3.1 Solution to the speculator’s decision . . . . . . . . . . . . . 105
3.3.2 Maintenance condition for the stable asset market . . . . . 106
3.3.3 Deleveraging effects, limits to market liquidity . . . . . . . 107
3.4 Stability results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
3.4.1 Stability if leverage constraint is non-binding . . . . . . . . 114
3.4.2 Instability if leverage constraint is binding . . . . . . . . . 116
3.5 Simulation Results . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
3.5.1 Speculator behavior affects volatility . . . . . . . . . . . . . 119
3.5.2 Stable asset failure is dominated by collateral asset returns 122
3.6 Stablecoin Attacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
3.6.1 Expanded Model: Adding an Attacker . . . . . . . . . . . 124
3.6.2 Profitable bets on liquidations . . . . . . . . . . . . . . . . 124
3.6.3 Attacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125

3.7 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
3.8 Appendix: Derivation of Results . . . . . . . . . . . . . . . . . . . 135


**4** **Stablecoins 2.0: Economics Foundations and Risk-Based Models** **141**

4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142

4.2 Custodial Stablecoins . . . . . . . . . . . . . . . . . . . . . . . . . . 145

4.2.1 Reserve Fund = 100% reserve off-chain . . . . . . . . . . . 146

4.2.2 Fractional Reserve Fund . . . . . . . . . . . . . . . . . . . . 147
4.2.3 Central Bank Digital Currency . . . . . . . . . . . . . . . . 148
4.3 Non-custodial Stablecoins . . . . . . . . . . . . . . . . . . . . . . . 149
4.3.1 Primary Value . . . . . . . . . . . . . . . . . . . . . . . . . . 152
4.3.2 Risk Absorption and Issuance . . . . . . . . . . . . . . . . . 156
4.3.3 Governance, Mining, and Manipulation . . . . . . . . . . . 161
4.4 Models and Measures of Non-Custodial Stablecoins . . . . . . . . 166
4.4.1 Capital Structure Models . . . . . . . . . . . . . . . . . . . 166
4.4.2 Forking Models . . . . . . . . . . . . . . . . . . . . . . . . . 181
4.4.3 Price Dynamic Models . . . . . . . . . . . . . . . . . . . . . 183
4.4.4 Agents, preferences and attitudes to risk . . . . . . . . . . 185
4.5 From Stablecoins to DeFi . . . . . . . . . . . . . . . . . . . . . . . . 185
4.5.1 Sustainability of Incentives . . . . . . . . . . . . . . . . . . 185


vi


4.5.2 Composite Stablecoins . . . . . . . . . . . . . . . . . . . . . 187
4.5.3 Cross-chain and Synthetic Assets . . . . . . . . . . . . . . . 188
4.5.4 Lending Protocols and DEXs . . . . . . . . . . . . . . . . . 189
4.6 Concluding Remarks . . . . . . . . . . . . . . . . . . . . . . . . . . 191
4.7 Appendix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
4.7.1 Tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192

4.7.2 Reserve Fund Stablecoins . . . . . . . . . . . . . . . . . . . 195

4.7.3 Fractional Reserve Fund . . . . . . . . . . . . . . . . . . . . 197

4.7.4 Discussion of Oracles . . . . . . . . . . . . . . . . . . . . . 199
4.7.5 Agents, preferences and attitudes to risk . . . . . . . . . . 201
4.7.6 Cross-chain and Synthetic Assets . . . . . . . . . . . . . . . 209


**5** **Cascading Losses in Reinsurance Networks** **211**
5.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212
5.2 Reinsurance Contagion Model . . . . . . . . . . . . . . . . . . . . 216
5.2.1 Primer on reinsurance contracts . . . . . . . . . . . . . . . 216
5.2.2 Two contagion mechanisms . . . . . . . . . . . . . . . . . . 217
5.2.3 Network definitions . . . . . . . . . . . . . . . . . . . . . . 220
5.3 Network Liabilities . . . . . . . . . . . . . . . . . . . . . . . . . . . 222
5.3.1 Liabilities without contract caps . . . . . . . . . . . . . . . 222
5.3.2 Liabilities with contract caps . . . . . . . . . . . . . . . . . 223
5.3.3 Unique fixed point . . . . . . . . . . . . . . . . . . . . . . . 225
5.3.4 Other cases: unique, multiple, and no fixed points . . . . . 228
5.3.5 Least fixed points . . . . . . . . . . . . . . . . . . . . . . . . 232
5.3.6 Multiple fixed points: net liabilities equal . . . . . . . . . . 233
5.3.7 Consequences of multiple fixed points . . . . . . . . . . . . 235
5.3.8 Algorithms to find the least fixed point . . . . . . . . . . . 237
5.4 Real World Implications of the Network Model . . . . . . . . . . . 241
5.4.1 Dangerous network structures cause reinsurance spirals . 241
5.4.2 Extreme parameter sensitivity . . . . . . . . . . . . . . . . 246
5.4.3 Implications for contract design . . . . . . . . . . . . . . . 248
5.5 Simulations with Real Network Data . . . . . . . . . . . . . . . . . 249

5.5.1 Network construction . . . . . . . . . . . . . . . . . . . . . 249
5.5.2 Sensitivity to parameter perturbations . . . . . . . . . . . . 251
5.5.3 Systemic effects of contract structures . . . . . . . . . . . . 253
5.5.4 Effects of time dependency of claims . . . . . . . . . . . . . 257
5.6 Concluding Remarks . . . . . . . . . . . . . . . . . . . . . . . . . . 260
5.7 Appendix: Proofs . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
5.8 Appendix: Simulation Details . . . . . . . . . . . . . . . . . . . . . 274
5.8.1 Network Construction . . . . . . . . . . . . . . . . . . . . . 274
5.8.2 Sensitivity to parameter perturbations . . . . . . . . . . . . 279
5.8.3 Systemic effects of contract structures . . . . . . . . . . . . 280


vii


**6** **Optimal Intervention in Economic Networks using Influence Maxi-**
**mization Methods** **281**

6.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282

6.2 Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 287
6.2.1 Financial network contagion model . . . . . . . . . . . . . 287
6.2.2 Optimal intervention . . . . . . . . . . . . . . . . . . . . . . 290
6.3 Analytical Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295
6.3.1 Hardness of optimal intervention . . . . . . . . . . . . . . . 296
6.3.2 Approximation with randomized thresholds . . . . . . . . 297
6.3.3 Identifying large failure cascade scenarios . . . . . . . . . 300
6.4 Application to WIOD dataset . . . . . . . . . . . . . . . . . . . . . 303
6.4.1 Simulation setup . . . . . . . . . . . . . . . . . . . . . . . . 305
6.4.2 Intervention algorithms . . . . . . . . . . . . . . . . . . . . 306
6.4.3 Simulated interventions . . . . . . . . . . . . . . . . . . . . 308
6.4.4 Efficiency of intervention . . . . . . . . . . . . . . . . . . . 310
6.5 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 312
6.6 Appendix: Proofs and Additional Details . . . . . . . . . . . . . . 314
6.6.1 Overview of Influence Maximization . . . . . . . . . . . . 314
6.6.2 Proofs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 316
6.6.3 Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . 325


**7** **Cascading Risks and Sensitivity in Economic Networks** **330**
7.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 331

7.2 Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 338
7.3 Connecting Network Structures to Risk and Sensitivity . . . . . . 341
7.3.1 Illustrating Problems from Sensitivity . . . . . . . . . . . . 342
7.3.2 Sensitivity Problems in Realistic Networks . . . . . . . . . 345
7.3.3 How this Paper Addresses these Problems . . . . . . . . . 347
7.4 Perturbation Theory for Cascade Models . . . . . . . . . . . . . . 348
7.4.1 Background on Perturbation Theory . . . . . . . . . . . . . 349
7.4.2 Acyclic Systems . . . . . . . . . . . . . . . . . . . . . . . . . 350
7.4.3 Cyclic Systems . . . . . . . . . . . . . . . . . . . . . . . . . 351
7.5 Model Results: Sensitivity without Threshold Effects . . . . . . . 355
7.5.1 Acyclic Networks without Threshold Effects . . . . . . . . 356
7.5.2 Cyclic Networks without Threshold Effects . . . . . . . . . 357
7.5.3 Asset Price Perturbations without Threshold Effects . . . . 360
7.5.4 Bounding Sensitivity for Particular Instances . . . . . . . . 361
7.6 Simulations: Sensitivity in Practice . . . . . . . . . . . . . . . . . . 363
7.6.1 Simulation setup . . . . . . . . . . . . . . . . . . . . . . . . 364
7.6.2 Network shape and conditioning . . . . . . . . . . . . . . . 365
7.7 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 367
7.8 Appendix: Proofs and Additional Details . . . . . . . . . . . . . . 370


**Bibliography** **382**


viii


CHAPTER 1


**INTRODUCTION**


1


Economic systems in the 21st century have grown to be larger and more


complex, often with cycles of economic interactions, increasingly complicated


financial instruments, and higher levels of automation and speed. The economic


world is also in the midst of a new movement to build decentralized finance


(DeFi) systems that leverage new technologies to replace the role of risky finan

cial intermediaries with decentralized (and more robust) structures. These are


- ften complex automated systems built as programs (smart contracts) that ex

ecute autonomously on blockchain virtual machines with little external ability


to intervene in crises. While such systems aim to enable the laudable ideals of


DeFi (e.g., non-custodial, permissionless, openly auditable, and composable),


they introduce new risks and complexity [185].


Concurrently with these complexity changes, systems are experiencing some


- f the largest economic shocks in recent times in an increasingly volatile world.


For instance, the economic crisis following the COVID-19 pandemic saw entire


supply chains and economic systems disrupted, with cutting actions across all


markets. Understanding economic risks and designing resilient financial sys

tems is increasingly important. Due to the size and complexity of these systems,


these economic problems intersect with modeling and computational problems


in the realm of computer science and applied math. This thesis focuses on two


aspects of mathematical modeling and computer science applied to understand

ing the complexities of financial systems.


2


#### **1.1 Mathematics of stability in decentralized finance**

In the first part of this thesis, I explore the design of decentralized stablecoins.


Most stablecoins today are pegged to the US dollar and exist because USD can

not be used directly on-chain. Cryptoassets need to be natively ‘issued’ as a to

ken within the blockchain environment. In principle, this could be done by the


central bank, but in practice is not. The closest form of direct USD on-chain oth

erwise is to rely on a third party who issues a _centralized_ stablecoin and promises


to custody the real asset off-chain on behalf of token holders.


_Decentralized_ stablecoins, on the other hand, are new types of financial in

struments that aim to become decentralized currencies within the new DeFi


ecosystem. In principle, they may adopt future monetary policies other than


a peg to USD. These resemble central bank and commercial bank monies with


new differences enabled by the underlying technology. Such stablecoins can be


less reliant on governments and banks to manage a currency, instead relying


- n incentive systems with transparent rules enforced cryptographically. How

ever, they also introduce new risks that increase the scope of complexity and


complicate the task of designing resilient systems.


This sections contains work that has been published in [114, 112, 110].

#### **1.1.1 Stability in leverage-based stablecoins.**


In [114] and [112], I model stablecoins, like Dai, which build on leverage market


mechanisms. In these stablecoins, speculators borrow against volatile collateral


to generate stablecoins that they can sell/use to achieve a leveraged position.


3


These stablecoins differ from traditional monetary system models in that there


is no central that we can assume is stability seeking for its own sake, instead re

lying on a system of incentives to coordinate profit maximizing agents. Stable

coins of this type have an endogenous pricing within this system of incentives


as opposed to traditional leverage models, in which the issued asset is assumed


stable (e.g., commercial bank issuance of US dollars). In these papers, I address


the question of whether these stablecoins can achieve stability through such in

centives setups.


In these models, I characterize a stable region for these stablecoins in terms


- f bounded probabilities of large deviations and quadratic variation based on


Doob’s inequality and Burkholder’s inequality. I also characterize an unstable


region, in which the stablecoin can experience short squeeze-like deleveraging


spirals (formally the stablecoin price becomes a submartingale) that can amplify


collateral drawdown and instability (formally the forward-looking variance is


higher than in the stable region). Following the characterization in these papers,


deleveraging spirals were observed in the stablecoin Dai contributing to the


Black Thursday crisis in March 2020.


No stable region exists in the models when the collateral price process is


not a submartingale. This is problematic for non-custodial stablecoins because


all crypto assets are highly correlated, and there is no way to get full stabil

ity in all circumstances unless collateral types extend to custodial assets. At

tempts to patch this dilemma has pushed the stablecoin space forward. Dai has


evolved to incorporate a mechanism of exchangeability with the custodial sta

blecoin USDC; Rai incorporated a mechanism of negative interest rates on hold

ing the stable asset, aiming to compensate speculators so that their value pro

4


cess remains a submartingale; Liquity incorporated dedicated liquidity pools


that smooth out crises, a mechanism that I proposed in [114].


In [112], I additionally characterize exploitable arbitrage opportunities that


arise from deleveraging and liquidations. Blockchain validators can cen

sor/reorder transactions to extract profit and even to create more arbitrage


- pportunities through market manipulation and blockchain reorganization at

tacks. Variants on these economic attacks also occurred in Dai on Black Thurs

day, costing the protocol $8m when mempool manipulation led to the clearing


- f collateral liquidation auctions at near zero prices. These attacks today are


part of a wider area known as miner/maximal extractable value (MEV), that in

cludes generalized front-running and back-running of blockchain transactions.

#### **1.1.2 Stability in general stablecoins.**


In [110], I explore stability in stablecoins based on non-leverage mechanisms.


Some of these stablecoins resemble traditional currency peg models with some


distinctions in terms of new risks that need to be incorporated. One notable type


is ‘algorithmic stablecoins’, which are wholly or partially backed by endoge

nous collateral that has self-referential value, fit this categorization. Adapting


models such as [144] suggests that these designs are fragile if the intangible


underlying economic value of these systems is small. These types of stable

coins (most prominently Terra UST, which reached billions of dollars in size)


subsequently collapsed. A persisting idea following from this work is that sta

blecoin stability can be characterized by redemption curve design, which rep

resents the monetary policy of the stablecoin. For instance, this is explored in


5


[116], which explains algorithmic stablecoin collapses as well as the instability


- f asset-backed stablecoins like Fei.


In [110], I also characterize governance and oracle risks in stablecoins by


modeling incentive compatibility in extended forms of capital structure models.


In these models, I characterize an extra cost in aligning incentives to secure de

centralized systems compared to centralized systems, similar to a cost of anar

chy. This characterization has motivated follow-up work [95], where we charac

terize Stackelberg equilibria in further iterations of these capital structure mod

els and additionally propose solutions for expanding the region of incentive


compatibility. This solution takes the form of ‘optimistic approval’, a negative


consent mechanism that affords users of the stablecoin a route to veto malicious


governance proposals. This mechanism is now used in decentralized protocols


such as Lido’s dual governance system. My work in [112] also motivates other


types of checks and balances that constrain governance oracle decisions, such


as the enforcement of no arbitrage conditions with markets observable on-chain


to restrict oracle misincentives as specified in [115] and by comparing with sig

nals about off-chain prices recovered from behaviors in other on-chain markets


[187].

#### **1.2 Mathematics of stability in economic networks**


In the second part of this thesis, I develop network mathematics to analyze sta

bility in more traditional markets, involving networks of interacting firms (e.g.,


in insurance and financial networks). In this work, I focus on characterizing


new risks that arise from the complex structure of these networks and address

6


ing difficulties that currently prevent the use of economic network models for


quantifying risks in real world settings. On the first topic, I characterize how


firms can be in dangerous positions within the global network structure even if


it has controlled its risk exposure well from its local perspective. For example, a


firm can end up in a position of bearing risk that is aggregated nonlinearly from


across the network. On the second topic, I address two current barriers to using


network models in practice:


1. **Sensitivity.** Network models involve large parameter sets and are very


sensitive to parameter uncertainty. This combines the problem of fun

damentally having large uncertainty in calibrating social science models


with the mathematical problem of understanding how this uncertainty


propagates into model error (e.g., error in modeling risk in these systems).


This mathematical problem is currently not well understood.


2. **Computational difficulty.** Many aspects of network models can be com

putationally hard to compute. For instance, many NP-hard problems


come up in this context and it is also practically hard to run Monte Carlo


simulations over large parameter spaces.


The space lacks tools to address these problems. Ultimately, this prevents the


use of financial network analysis in real applications, including financial market


design, government policy, and firm-level risk evaluation. My work develops


underlying theory that enables computational and sensitivity tools that make


network analysis more applicable in practice to large economic systems. This


section contains the work that has been published in [111, 113] as well as work


in [108] that has been invited for revisions.


7


#### **1.2.1 Contagion in reinsurance networks.**

It becomes increasingly complex to model realistic contagion in financial net

works with complicated derivatives. Most existing models are restricted to the


relatively simple cases of networks of debt and equity contracts. In [111], I de

velop a general contagion model for networks of reinsurance contracts. Evalu

ating this model involves working on the line graph, in which the links of the


network are interpreted as the nodes of a new network. I characterize the con

ditions under which a unique fixed point exists for the model using the Banach


fixed point theorem. A weaker corollary of my result provides a more direct


proof of uniqueness in existing debt network models. I additionally show that


if _some_ fixed point exists, then fixed point iteration converges to a least fixed


point based on an application of the Kleene fixed point theorem. I also charac

terize conditions under which there are least and greatest fixed points based on


the Tarski fixed point theorem. Finally, I show that net liabilities of each firm are


equal under any fixed point, which ties the fixed point results together with the


practical consequence that the least fixed points are the real world solutions of


the model.


Using this model of reinsurance networks, I characterize how nonlinearities


in the model lead to a host of new problems. I characterize dangerous spirals


that can concentrate losses on unsuspecting parts of the network. An example of


this is a reinsurer who acts like a damper on a cycle of reinsurers. With current


risk tools, it is not possible to measure or control for these risks. And it is hard to


develop new tools due to inherent uncertainty about global network structure


and due to the sensitivity of the model to parameter choice, which I demonstrate


using a reinsurance network dataset. I also show how past simplified models of


8


reinsurance networks greatly underestimate contagion risks on this dataset.

#### **1.2.2 Intervention in economic networks.**


In [113], I model intervention in an economic network contagion model. The


goal is to maximize overall system value under a budget constraint and consid

ering the nonlinear contagion process. In large systems, this quickly becomes


computationally hard, as I show formally in the paper. In practice, approxima

tions to optimal intervention are needed that can scale with network size. To


achieve this, I show how influence maximization methods can be extended to


economic network settings, which leads to an efficient approximation for opti

mal economic intervention. Compared to the influence maximization literature,


the economic case requires handling a more complicated triggering model (e.g.,


the influence matrix is a Neumann series, including self-loops). I additionally


show how the problem can be flipped around and similar methods applied to


efficiently sample shocks that lead to large cascade events. This can provide


a means of importance sampling, ensuring that samples can be obtained from


the tail of the contagion distribution, which I show is similarly as hard as the


- ptimal intervention problem. This work leads to a new scalable computation


tool toward designing interventions and stress testing in the economic network


setting.


9


#### **1.2.3 Sensitivity in economic networks.**

In [108], I confront this issue by developing further theory to understand net

work sensitivity. I improve on existing results with the unifying (and simplify

ing) perspective of perturbation theory. This allows an analytical explanation of


how structures involving network cycles cause high sensitivity. I also develop


foundational results for bounding sensitivity within a given instance of the sys

tem (vs globally across instances), leading to bounds that may be tight enough


to be useful in practice.


In subsequent work to be released following this thesis, I show how these


foundational results can be extended to form a scalable method of bounding


network sensitivity including threshold effects, something that is not achieved


in existing literature. This method turns out to be useful in practice, revealing


actionable information about the network that was not accessible before, and I


believe will open a new direction of using ecomonic network analysis in indus

try.

#### **1.3 Impact**


This body of work has been influential for regulators and policymakers. My fi

nancial networks research has been cited by the Bank of England in [118], where


it motivated their approach to measuring reinsurance contagion risks. And my


DeFi research has been cited by the Bank for International Settlements in [18],


where it motivated risk assessment of stablecoin runs and deleveraging spi

rals as well as the approach to understanding the DeFi technology stack. My


10


work on stablecoins has also been presented at the European Central Bank and


the Federal Reserve, and I have additionally met with regulators at the Bank of


England and the UK Financial Conduct Authority. My work in [110] coining the


term ‘endogenously collateralized stablecoin’ also appears to have influenced


draft legislation in the US, which proposed a moratorium on certain types of


stablecoins by this name [38].


This work has also been influential in the cryptocurrency industry. My work


has characterized problems with existing systems that later materialized and


influenced design changes. Designs from my research have been adopted by


DeFi projects. I have also presented my work at major industry conferences,


like Ethereum Devcon and Stanford’s Science of Blockchain Conference.


11


CHAPTER 2


**WHILE STABILITY LASTS: A STOCHASTIC MODEL OF**


**NONCUSTODIAL STABLECOINS**


The content of this chapter has previously appeared in:


“While Stability Lasts: A Stochastic Model of Noncustodial Stable

coins.” Ariah Klages-Mundt and Andreea Minca. _**Mathematical Fi-**_


_**nance**_, 32(4):943-981, 2022.


And was awarded Honorable Mention for Best Finance Student Papaer at IN

FORMs 2021.


12


The ‘Black Thursday’ crisis in cryptocurrency markets demonstrated


deleveraging risks in over-collateralized non-custodial stablecoins. We de

velop a stochastic model that helps explain deleveraging crises in these over

collateralized systems. In our model, the stablecoin supply is decided by spec

ulators who optimize the profitability of a leveraged position while incorpo

rating the forward-looking cost of collateral liquidations, which involves the


endogenous price of the stablecoin. We formally characterize regimes that are


interpreted as stable and unstable for the stablecoin. We prove bounds on


quadratic variation and the probability of large deviations in the stable domain


and we demonstrate distinctly greater price variance in the unstable domain.


We identify a deflationary deleveraging spiral by means of a submartingale.


These deleveraging spirals, which resemble short squeezes, lead to faster collat

eral drawdown (and potential shortfalls) and are accompanied by higher price


variance, as experienced on Black Thursday. We conclude by discussing non

custodial ways in which the issues raised in this paper can be mitigated.

#### **2.1 Introduction**


On March 12, 2020, called ‘Black Thursday’ during the COVID-19 market panic,


cryptocurrency prices dropped _∼_ 50% in the day. [1] This was accompanied by


cascading liquidations on cryptocurrency leverage platforms, including both


centralized platforms like exchanges and new decentralized finance (DeFi) plat

forms that facilitate on-chain over-collateralized lending. Among many events


from this day, the story of Maker’s stablecoin Dai stands out, which entered a


deflationary deleveraging spiral (akin to a short squeeze on Dai). This triggered


1This occurred while writing up the first draft of this paper.


13


high volatility of the ‘stable’ asset and a breakdown of the collateral liquidation


process. Due to market illiquidity exacerbated by network congestion, some


collateral liquidations were performed at near-zero prices. As a result, the sys

tem developed a collateral shortfall, which prompted an emergency response


and had to be made up by selling new equity-like tokens to recapitalize [130].


During this time, there was a huge demand for Dai. It became a much riskier


and more volatile asset, yet traded at a high premium and fetched lending rates


in the mid double digits. Leveraged speculators, who must repurchase Dai in


- rder to deleverage their positions, were exhausting Dai liquidity, driving up


the price of Dai and subsequently increasing the cost of future deleveraging


(we discuss some further causes that led to market illiquidity in developing the


model in the next section). These speculators began to realize that, in these con

ditions, they face concrete risk that a debt reduction of $1 could cost a significant


premium. Eventually, a new exogenously stable asset–the USD-backed custo

dial stablecoin USDC–had to be brought in as a new collateral type to stabilize


the system [56].

#### **2.1.1 Stablecoins**


A stablecoin is a cryptocurrency with added economic structure that aims to


stabilize price/purchasing power. For a recent overview of stablecoins, see


[110, 44] and the references therein. Stablecoins are meant to bootstrap price


stability into cryptocurrencies as a stop-gap measure for adoption. They also


serve as mechanics to avoid fiat to crypto conversions, which are rather costly.


This is in fact a key motivation for their use, hence the system can remain ‘fully


14


Figure 2.1: Stablecoin supply.


decentralized’.


Stablecoins are either _custodial_ and rely on custodians to hold reserve assets


- ff-chain (e.g., $1 per coin) or _non-custodial_ and set up a risk transfer market


through smart contracts, which are programs that execute on the blockchain


computer. Custodial stablecoins include Tether, USDC, and the proposed


Diem/Libra and can often be viewed analogously to narrow banks or money


market funds in terms of underlying structure. Alternatively, non-custodial sta

blecoins aim to retain the property of reduced counterparty/censorship risk.


Figure 2.1 illustrates the market share of the main stablecoins. The largest three


are custodial stablecoins (USDT, USDC, BUSD) whereas only one non-custodial


stablecoin, Dai, is among the top four stablecoins in terms of market share.


Non-custodial stablecoins have a wide design space, which is captured in the


taxonomy of [110]. A key dimension in this design space is the source of value


backing the stablecoin. This ranges from exogenous asset backing, where assets


have value unrelated to the system, to endogenous asset backing, where assets


are like ‘system equity’ and have value that is circular with the system itself.


This latter class, which is often ill-defined as ‘algorithmic’, often blurs the line


with being effectively unbacked, as the value of endogenous assets can spiral


to zero if confidence is broken. This latter type includes the Terra UST stable

15


coin that collapsed in May 2022 [37]. These stablecoins that are fully or partly


endogenously backed can largely be understood using generalizations of cur

rency peg models, such as [144], for which the risks of currency runs and spec

ulative attacks are well studied. These existing tools help to understand these


systems and how they (usually) fail, considering that the ‘economies’ around


these stablecoins are quite fragile.


In contrast, non-custodial stablecoins that are backed by exogenous assets


have greater similarities to non-custodial forms of the current monetary system


- f commercial bank money, as discussed in [110]. In this paper, we focus on new


risks that arise in these types of stablecoins, which require further study. Stable

coins of this type transfer risk from stablecoin holders to speculators, who hold


leveraged collateralized positions in cryptocurrencies. [2] The speculator repre

sents any actor (usually automated) who has an incentive to issue the coin. [3]


Such actor issues the stablecoin continuously by locking in collateral. The incen

tive to issue (or redeem) coin is captured by the speculators’ return expectations


including potential liquidation costs and the endogenous stablecoin price.


The collateralization structure is different for non-custodial stablecoins than


for the custodial ones. It is similar to a tranche structure, in which stablecoins act


like senior debt while speculators are akin the buyers of the junior tranche of a


CDO. In contrast to the classical case, the ‘CDO’ issue is dynamic and by anyone


in the system. We refer the reader to the Dai white paper [131]. The white


paper describes how _anyone could generate Dai using that system_ by leveraging


Ethereum (ETH) as collateral through smart contracts known as Collateralized


Debt Positions (CDPs).


2
‘Leverage’ means that speculators holds _>_ 1 _×_ initial assets but face new liabilities.
3They are part a form of ‘keepers’ in the MakerDAO protocol.


16


A dynamic and automatic deleveraging process balances positions if collat

eral value deviates too much, as determined by a price feed. Two major risks


in non-custodial stablecoins emerge around market structure collapse and price


feed and governance manipulation. In this paper, we focus completely on the


market structure risk, assuming that price feeds, governance, and the underly

ing blockchain perform as expected. [4]


In addition to the COVID-19 panic, the effects of these risks are also wit

nessed in bitUSD, Steem Dollars, and NuBits, which suffered serious depegging


events in 2018 [103], and Terra and Synthetix, which suffered price feed manip

ulation attacks in 2019 ([176], [175], [178]). Similar manipulations were also ob

served on the bZx lending protocol in 2020 ([157], [158]). Many similar examples


- f mechanism failures and exploitations occurred through the rest of 2020 (see


[110, 185]). Stablecoins currently serve a central role in an increasingly complex


decentralized finance environment, involving composability with other DeFi


platforms. In addition, many other blockchain assets, such as synthetic and


cross-chain assets, rely on the basic mechanism behind stablecoins, which we


explore further in the discussion section.

#### **2.1.2 This paper**


In this paper, we construct a stochastic model of over-collateralized non

custodial stablecoins, with an endogenous price (Section 2.2). The system is


based on a speculator who solves an optimization problem accounting for po

tential returns from leverage as well as potential liquidation costs. The specu

4Note, however, that blockchain congestion can serve to decrease elasticity in the market
structure, which we discuss in the model construction.


17


lator decides the supply of stablecoins secured by its collateral position while


considering demand for the stablecoin. Our interest in non-custodial stable

coins lies in understanding deleveraging spirals when the price and stablecoin


issue is endogenous and the collateral management is decentralized. In this


case, a deleveraging spiral results from the intertwining of a short squeeze in


the stablecoin price and a liquidation spiral of the collateral. This is in con

trast to potential liquidation crises in custodial coins such as Tether and USDC


- r ‘algorithmic’ stablecoins such as Terra UST (which coincidentally also had


a partial custodial reserve). Custodial stablecoins maintain stability through


arbitrageurs who mint and redeem for assets with the custodian. Unbacked


- r partially backed stablecoins like Terra UST instead are subject to death spiral


risks from runs and speculative attacks due to insolvency. In both of these cases,


classical models for money market funds and currency pegs apply well. [5] We


focus on the non-custodial variant involving exogenous over-collateralization,


whose risks are yet to be analyzed rigorously.


We derive fundamental results about non-custodial stablecoins in our


model, including economic limits to the speculator’s behavior, in Section 2.3. In


Section 2.4 we develop the primary results of the paper: we analytically charac

terize regions in which the stablecoin can be intepreted as stable (Theorems 2.2


and 2.3) and unstable (Theorems 2.5 and 2.6), and a region in which a delever

aging spiral occurs that can cause liquidity problems in a crisis (Theorem 2.4).


These deleveraging spirals, which resemble short squeezes, are counterintuitive


as they lead to stablecoin price appreciation during times of shock, whereas we


[5The recent collapse of the peg in TerraUSD, see e.g., https://www.wsj.com/articles](https://www.wsj.com/articles/cryptocurrency-terrausd-falls-below-fixed-value-triggering-selloff-11652122461)
[/cryptocurrency-terrausd-falls-below-fixed-value-triggering-selloff](https://www.wsj.com/articles/cryptocurrency-terrausd-falls-below-fixed-value-triggering-selloff-11652122461)

[-11652122461 can be modeled similarly to the run on money market funds in the financial](https://www.wsj.com/articles/cryptocurrency-terrausd-falls-below-fixed-value-triggering-selloff-11652122461)
crisis, [98], or currency peg attacks, [144]. In particular, restoring the peg relies on open market

- perations by an entity running the reserve fund, such as Luna Foundation in the case of the
TerraUSD stablecoins.


18


might otherwise expect prices to depreciate given the riskier state of the system.


Further, this appreciation is detrimental: it leads to faster collateral drawdown,


and potentially shortfalls, as more collateral is required to fulfill liquidations


and is accompanied by higher price variance.


The context for our analytical results is a model with a single speculator fac

ing imperfectly elastic demand for the stablecoin; however, many of the meth

- ds can extend to generalized settings. In Section 2.5, we consider idealized


settings that lead to ‘perfect’ stability properties.


We discuss in Section 2.6 a seeming contradiction that arises: while the goal


is to make decentralized non-custodial stablecoins, these can only be fully sta

bilized from deleveraging effects by adding uncorrelated assets, which are cur

rently centralized/custodial. This is a consequence of our instability results in


Section 2.4 and, as introduced in Section 2.5, the absence of a stable region in


idealized settings when underlying asset markets deviate from a submartin

gale setting. We suggest an alternative: a buffer to dampen deleveraging effects


without directly incorporating custodial assets. This buffer works by separating


those who are willing to have stablecoins swapped to custodial assets in a crisis


(in return for an ongoing yield from option buyers) from those who require full


decentralization.


Non-custodial stablecoins such as Dai, Rai, and Liquity have since moved in


directions such as this to overcome the issues we illustrate in this paper.


19


#### **2.1.3 Relation to Prior Work**

While there is a rich literature on related financial instruments, there is limited


research directly applicable to stablecoins. [46] are the first to point out the


analogy of stablecoins to Collateralized Loan Obligations, and contribute to the


securitization literature by proposing designs in the decentralized context. They


use option pricing theory and PDE methods for valuation of their new design


features. Our work is complimentary: we analyze the stability over time of


these new securities.


A simple stablecoin model is developed in [112] and introduces the concept


- f deleveraging spirals, which later materialized on Black Thursday. This pa

per supersedes that model and its results. Whereas the model in [112] doesn’t


directly account for the actual repurchase price in deleveraging–instead delegat

ing to a risk constraint in the optimization–we set up a stochastic process model


in this paper that includes forward-looking liquidation prices in the speculator’s


- ptimization. Our analytical results supersede [112] in the following ways:


  - We formally characterize a deleveraging spiral as a submartingale,


whereas their paper lacks a formal treatment.


  - We give stability results in terms of probabilities of large deviations and


quadratic variation of the price process.


  - An unstable region is conjectured in their paper, backed by simulation. We


formally prove distinct price variances in stable and unstable regions.


[78] analyzes credit risk stemming from collateral type in Maker’s stable

coin Dai. [160, 55] model stability in Terra and Celo stablecoins under Brown

ian motion scenarios in the absence of endogenous market feedback effects that


20


motivate this paper. [110, 95] discuss models of governance and oracle attack


surfaces for non-custodial stablecoins. More generally in the context of decen

tralized finance, [185] treat the governance extractable value.


[69] discusses stablecoin concepts based on monetary policy and hedging


strategies and introduces methods for enhancing liquidity using combinatorial


auctions and automated market makers. [122] studied custodial stablecoins


and considers the use of hedging techniques to build an asset-backed cryp

tocurrency. [88] explores the robustness of decentralized lending protocols to


shocks and liquidations. [54] explores competition between decentralized lend

ing yields and staking yields in proof-of-stake blockchains. However, these do


not model a stablecoin mechanism with endogenous price behavior.


[91] designs a reputation system for crypto-economic protocols to reduce col

lateral requirements. This does not readily apply to understanding stablecoin


collaterals, however, as it requires identification of ‘good’ behavior and, addi

tionally, stablecoin speculators face leveraged exchange rate bets and will have


reason to provide greater than minimal collateral. This additionally motivates


- ur model to understand how liquidation effects affect speculator decisions.


Stablecoins share similarities with currency peg models, e.g., [144, 89]. In


these models, the government plays a mechanical market making role to seek


stability and is not a player in the game. In contrast, in non-custodial sta

blecoins, decentralized speculators take the market making role. They is

sue/withdraw stablecoins to optimize profits and are not committed to main

taining a peg. In a stablecoin, the best we can hope is that the protocol is well

designed and that the peg is maintained with high probability through incen

tives. A fully strategic model would be a complicated (and likely intractable)


21


dynamic game.


There are also similarities with collateral and debt security markets and re

purchase agreements. These have also experienced unprecedented stress in the


COVID-19 market panic, during which even 30-year US government bonds–


normally highly liquid–have been difficult to trade [163]. Such debt securities


differ from stablecoins in that dollars are borrowed against the collateral as op

posed to a new instrument, like a stablecoin, with an endogenous price. These


debt security markets do, however, demonstrate that liquidity in the underlying


markets can dry up in crises even in highly liquid markets. Stablecoins face this


liquidity risk in the underlying market as well as an endogenous price effect on


the stable asset.


The problem resembles classical market microstructure models (e.g., [154]);


it is a multi-period system with agents subject to leverage constraints that take


recurring actions according to their objectives. In contrast, the stablecoin set

ting has no exogenously stable asset that is efficiently and instantly available.


Instead, agents make decisions that endogenously affect the price of the ‘stable’


asset and affect future incentives.

#### **2.2 Model**


Our model is very closely related to Maker’s stablecoin Dai [131] as well as


newer stablecoins by UMA, Reflexer, and Liquity. Crucially, these stablecoins


are backed by over-collateralization in assets that have value exogenous to the


stablecoin system as opposed to assets whose value is circularly derived from


the stablecoin itself. There are two primary feedback effects to consider in these


22


stablecoins: (1) feedback of deleveraging on an endogenous stablecoin price,


and (2) feedback of deleveraging on collateral price. We focus on the former.


The latter can be described using existing deleveraging models (e.g., this is con

sidered in the stablecoin context in [88]). We later discuss how our model can


be adapted to incorporate these endogenous effects on collateral in Section 2.6.


The model contains a stablecoin market and two assets: a risky asset (ETH) [6]


with exogenous price _Xt_ and an ETH-collateralized stablecoin STBL with en

dogenous price _Zt_ . The stablecoin market connects stablecoin holders, who seek


stability, and speculators, who make leveraged bets backing STBL. The STBL


protocol requires the STBL supply to be over-collateralized in ETH by collateral


factor _β_ .


In order to focus on the effects of speculator decisions in this paper, we


simplify the stablecoin holder demand as exogenous with constant unit price

elasticity. This is equivalent to a fixed STBL demand _D_ in dollar terms, though


not quantity. Note that there is no direct redemption process for stablecoin hold

ers aside from a global settlement/shutdown of the system at par value, which


can be triggered by a governance process (see [131]).


From a practical perspective, STBL demand is not elastic, at least short

term, even if it were in principle elastic longer-term. A significant portion


- f stablecoin supplies are locked in other applications, like lending proto

cols and lotteries. These applications promise (in some sense) value safety in


- ver-collateralization, but don’t guarantee liquidity to withdraw. Additionally,


Ethereum transactions cannot be executed in parallel; during volatile times,


transactions can be delayed due to congestion, causing timely trades (especially


6We designate the risky collateral asset as ETH for simplicity. In principle, it could be another
cryptoasset or even outside of a cryptocurrency setting.


23


involving transfer to/from centralized exchanges) to fail. This occurs even if,


in principle, there is liquidity in these markets. On the other hand, longer-term


demand elasticity will naturally depend on the presence of good uncorrelated


alternatives. [7]


The speculator has ETH locked in the system and decides the STBL supply,


which represents a liability against its locked collateral. At the start of step _t_,


there are _Lt−_ 1 STBL coins in supply. The speculator holds _Nt−_ 1 ETH and chooses


to change the STBL supply by ∆ _t_ = _Lt −Lt−_ 1. If ∆ _t >_ 0, the speculator sells new


STBL on the market for ETH at the market clearing price _Zt_ . This increases the


ETH position _Nt_ . If ∆ _t <_ 0, the speculator buys STBL on the market, reducing


_Nt_ . We denote by _N_ [¯] _t_ the speculator’s locked collateral. Informed by limitations


- f actual implementations, we formalize the process ( _N_ [¯] _t_ ) based on ( _Nt_ ). [8] The


speculator decides _Lt_ by optimizing expected profitability in the next period


based on expectations about ETH returns and the cost of collateral liquidation


if the collateral factor is breached.


In this way, the speculator myopically optimize for the next period. A


simplification of our model is a one-off game, which hosts a single period of


decision-making before the system is settled in the final period. In this case,


the myopic setup is parallel to major single period games in finance (e.g.,


[144, 89, 70, 74, 156]). Our results make significant contributions over the ex

isting state of research on stablecoins, describing different system behavior de

pending on initial conditions in one-off games. The more general multi-period


7From another perspective, a strategic stablecoin holder would take into account expectations about speculator issuance and ability to maintain the price target and expectations about
a global settlement. This is outside of our model as formulated.
8In principle, the speculator’s decision could be extended to deciding ¯ _Nt_ in addition to ∆ _t_ .
Note however that this would make most sense if the speculator’s position is further extended
to include multiple assets.


24


form of our model then describes a dynamic process composed of a series of


- ne-off games with changing initial conditions. Our results also apply more


generally to this multi-period setting, where they are stronger than simply a


series of the one-off version of the results. Both of these contribute to stable

coin modeling as there are not better candidates for multi-period models at this


point, although we later discuss ideas toward adapting the model into a multi

period control problem.


Given supply and demand, the STBL market clears by setting demand equal


to supply in dollar terms. This yields the clearing price _Zt_ = _L_ _[D]_ _t_ [.][9][ This clearing]


equation is related to the quantity theory of money and is similar to the clearing


in automated market makers [13] but processed in batch.

#### **2.2.1 Formal setup**


We formalize the model as follows. We define the following _parameters_ :


 - _D_ = STBL demand in dollar value (equivalent to constant unit price

elasticity)


 - _β_ = collateral factor for ETH


 - _α ≥_ 1 = liquidation cost multiple (reflecting the fee paid to liquidators)


The system is composed of the following _processes_ :


9We can consider constant elasticity STBL demand functions that depend on _Zt_ . Letting _q_ be
the quantity of STBL demanded at $1 price and assuming a constant price elasticity _−γ <_ 0, the
dollar-denominated demand function is _D_ ( _Zt_ ) = _ZtQ_ ( _Zt_ ) = _Ztq/_ (1 _−_ _γ_ (1 _−_ _Zt_ )) _._ for _γ_ = 1 we

- btain the case of constant dollar denominated demand. In clearing the market, the generalized

price process is a linear transformation _Zt_ = _γ_ [1] - _Lqt_ _[−]_ [1] - + 1.


25


  - ( _Xt_ ) _t≥_ 0 = exogenous ETH price process in dollars.


 - _Lt_ = stablecoin supply at time _t_ that obeys


_Lt_ = _ζ_ + _Lt−_ 1 + ∆ _t,_


where _Lt−_ 1 _>_ 0 is the speculator’s STBL liabilities from the previous


period, ∆ _t_ is the speculator’s change in liabilities at time _t_ (such that


_Lt_ = _Lt−_ 1 + ∆ _t_ ), and _ζ_ is a real number that modifies circulating supply


 - _Nt_ = speculator’s ETH position at time _t_, including collateral


 - _N_ [¯] _t_ = speculator’s locked ETH collateral at time _t_ (and start of time _t_ + 1)


  - ( _Yt_ ) _t≥_ 0 = speculator’s value process


 - _Zt_ = _L_ _[D]_ _t_ [defines the STBL price process.]


We take ( _Ft_ ) _t≥_ 0 to be the natural filtration where _Ft_ = _σ_ ( _X_ 0 _, . . ., Xt, L_ 0 _, . . ., Lt_ ).


The system is driven by the process ( _Xt_ ) subject to the speculator’s decisions ∆ _t_


(equivalently _Lt_ given _Lt−_ 1).


The parameter _ζ_ modifies circulating STBL supply. This could come from an


- utside amount of STBL not created by the speculator (a positive adjustment), or


some STBL could essentially be locked (a negative adjustment). As formulated,


- ur model applies to a system that can be described with monopolistic agents,


- r where agents behave similarly (have similar beliefs). With _ζ >_ 0, the model


becomes similar to having heterogeneous agents. Whereas, in general to do


this, we would have to consider both heterogeneous beliefs about the future as


well as different _ζ_ s, which together would be intractable, _ζ_ provides a way to


aggregate these various effects in a simpler model. In particular, we suggest a


positive _ζ_ may make numerical results more applicable to real settings.


26


To simplify the exposition of analytical results going forward, we simplify


to the case that _β_ = 2 [3] [(the collateral factor used in Maker’s Dai stablecoin) and]


_ζ_ = 0. _Note that under these conditions, and in the remainder of the paper, we use Lt_


_and Lt interchangeably_ .

#### **2.2.2 Collateral constraint**


The collateral constraint requires the collateral locked in the system to be _≥_ a


factor of _β_ times by liabilities. It applies in both a pre-decision and post-decision


sense. The _pre-decision_ version determines when a liquidation occurs: a liquida

tion is triggered at the start of time _t_ if the following condition is breached


¯
_Nt−_ 1 _Xt ≥_ _βLt−_ 1 _._


The _post-decision_ version constrains the speculator’s decision-making, limiting


_Lt_ such that


_N_ ¯ _tXt ≥_ _βLt._


Note that the nominal stablecoin price ($1) is used in these constraints instead of


the real price because these are encoded by the protocol’s smart contracts as one


- f the means toward incentivizing the $1 target. [10] The collateral factor could be


dynamic, in the sense that the governance of the protocol could vote to change


its value. Proposals to change the collateral factor are in practice infrequent,


[see https://makerdao.world/en/learn/vaults/liquidation/, so](https://makerdao.world/en/learn/vaults/liquidation/)


we consider here a constant factor. We leave it for future research to model the


governance’s decision.


10Conceptually, outside of this model, this has the effect of upper bounding the stablecoin
price at _β_ as an arbitrage opportunity would be created otherwise.


27


#### 2.2.3 Speculator decides ∆ t taking into account real liability **value**

We assume the speculator is risk-neutral and optimizes its next-period expected


value, taking into account expectations around liquidations. In particular, this


means that the speculator takes into account the real cost of deleveraging its


liabilities in the event it needs to reduce its position in the next time step and


doesn’t simply measure the nominal value of liabilities. Its value at time _t_ is its


nominal equity at the start of period (pre-decision), adjusted by a liquidation


effect that describes how the real value deviates from nominal in the event that


the speculator needs to deleverage. That is


_Yt_ = _Nt−_ 1 _Xt −_ _Lt−_ 1 _−_ liquidation effect _._


A liquidation effect is outlined in a following subsection.


Note that _Nt_ is a function of the decision variable ∆ _t_, and recall _Lt_ = _Lt−_ 1 +


∆ _t_ . The speculator decides ∆ _t_ (equivalently _Lt_ given _Lt−_ 1) to optimize next

period expected value subject to the post-decision collateral constraint in the


current period:


max E[ _Yt_ +1 _|Ft_ ]
∆ _t_


s.t. _N_ ¯ _tXt ≥_ _βLt._


Thus the speculator accounts for the expected deviation of real from nominal


liability value. If the expected liquidation effect is small —for instance if the


probability that the speculator needs to deleverage next period is small— then


the speculator treats _Lt_ near face value in the optimization for a mix of short

and long-term reasons. As long as speculators can survive liquidation, they can


expect to dispose of liabilities near face value longer-term when markets are


28


liquid. The protocol smart contracts also add a precedent for treating liabilities


at face value: it is encoded in this way in the collateral constraint and in the


event of global settlement of the system, which is intended to be be triggered


should the system diverge too significantly from the intended structure (and


which would occur in the final period of the one-off version).

#### **2.2.4 Speculator’s collateral at stake**


We consider that the speculator decides on a level of participation as a com

ponent of their entire portfolio. This takes place in a separate optimization


problem outside the scope of this model (although we discuss how it could


be extended later). The speculator’s level of participation amounts to the ini

tial collateral at the start of our model–for simplicity, we say this also includes


any amount they have decided beforehand may be accessible to top up collat

eral later. The speculator’s behavior in our model amounts to maximizing the


expected value of this component of their portfolio. On the other hand, if this


were the speculator’s entire portfolio, we note that the story may be different–


e.g., they may want to maximize expected log values as in the Kelly criterion


and would probably choose to participate differently, as is common in problems


- f leverage if the whole portfolio is at stake.


We take the speculator’s collateral at stake at the start of time _t_ + 1 to be


¯
_Nt_ = _Nt−_ 1 minus any collateral liquidation that happens at time _t_ . This is con

sistent with the speculator’s collateral being blocked: it cannot be used to repur

chase STBL in the same step. This means that the speculator (1) has an outside


amount (or is able to borrow) to repurchase STBL if ∆ _t <_ 0 and then later repays


29


this from unlocking collateral and (2) can’t post proceeds of new STBL issuance


(∆ _t >_ 0) as collateral within the same step.


While there are settings in which we could alternatively use _Nt_ as the collat

eral at stake at the start of _t_ + 1 (e.g., if flash loans are used), the choice of _Nt−_ 1


additionally leads to a simpler exposition of results as it decouples the collateral


from the decision variable.

#### **2.2.5 Collateral liquidation mechanics**


In time _t_ + 1, the pre-decision collateral constraint is _N_ [¯] _tXt_ +1 _≥_ _βLt_ . If this is


breached, then the speculator’s collateral is partially liquidated, if possible, to


repurchase an amount _ℓt_ +1 _>_ 0 of STBL. In real protocols, liquidation amounts


are automated by an algorithm and will inherently be first order estimates of the


amount needed to rebalance the debt position as the algorithm will not be able


to know the actual market structure and price impact. For instance, liquidations


in Maker and Compound release a certain amount of debt to be repaid, and un

lock a corresponding amount of collateral that an arbitrager can use to rebalance


the debt position (both decided algorithmically in [60] and [131], and the latter


decided through auction in Maker’s newer version [132]). Consistent with these


protocols, we set the amount of debt that needs to be repaid in a liquidation to


be _ℓt_ +1 of STBL such that post liquidation we have _N_ [¯] _tXt_ +1 _−_ _ℓt_ +1 = _β_ ( _Lt −_ _ℓt_ +1).


With _β_ = [3] 2 [, this amount is]


_ℓt_ +1 = _[β][L][t][ −]_ _[N]_ [¯] _[t][X][t]_ [+1] = 3 _Lt −_ 2 _N_ [¯] _tXt_ +1 _._

_β −_ 1


We interpret this as the protocol’s encoded estimate, using nominal stablecoin


price, of how much collateral it should liquidate in an ‘auction’ to deleverage,


30


similar to Maker. Our model simplifies the auction to settle on the endogenous


stablecoin market. Other liquidation algorithms could also be considered and


would lead to similar qualitative effects.


In a time step with a liquidation, the liquidation forces an upper bound


∆ _t_ +1 _≤−ℓt_ +1 as this amount would, in the real protocol, be unlocked for ar

bitrageurs. But the speculator could choose to repurchase more STBL to further


reduce leverage. The repurchase of _ℓt_ +1 through the liquidation mechanism is


subject to a liquidation cost multiple _α ≥_ 1–i.e., the effective repurchase price


is _α×_ the STBL market price. The purpose of this fee is that, in real stablecoin


systems, liquidations are performed by arbitrageurs who capture this fee.


Notice that the STBL market price will itself be affected by liquidations. De

pending on market impact, which the algorithms can only observe sequentially,


the liquidation may be insufficient to fully rebalance the debt position back to


the collateral constraint. If this occurs, then the issue will be taken into account


with further liquidations in subsequent time steps. The parameter _β_ in real sys

tems is intended to provide safety in such events so that the system does not


become under-collateralized.


Two thresholds are relevant at time _t_ for calculating expectations of a liq

uidation effect at time _t_ + 1. These are non-time-dependent functions of the


random variable _Lt_ :

_b_ ( _Lt_ ) := _[β]_ ~~¯~~ _[L][t]_

_Nt_



1
_c_ ( _Lt_ ) :=
2 _N_ ~~[¯]~~ _t_




~~�~~ _α_ [2] _D_ [2] + 4 _αDLt_ + _L_ [2] _t_ _[−]_ _[α][D]_ [ +] _[ L][t]_ _._

- 


The threshold _b_ ( _Lt_ ) gives the highest _t_ +1 ETH price that breaches the collateral


constraint while the threshold _c_ ( _Lt_ ) gives the _t_ + 1 ETH price that consumes the


entirety of the speculator’s locked collateral in a liquidation repurchase due to


31


the effect on STBL repurchase price. [11] Below this level, the speculator cannot


meet the collateral demand even by liquidating everything. The formulation of


_b_ ( _Lt_ ) follows directly from the collateral constraint; the formulation of _c_ ( _Lt_ ) fol

lows from equating the repurchase cost of liquidation _ℓt_ +1 to _N_ [¯] _tXt_ +1 and solving


for _Xt_ +1.


If _c_ ( _Lt_ ) _≤_ _Xt_ +1 _≤_ _b_ ( _Lt_ ), then the liquidation effect is _ℓt_ +1 _−_ _ℓt_ +1 _Lt−Dℓt_ +1 _[α]_ [. This]


represents a repurchase of _ℓt_ +1 STBL (reducing collateral by the repurchase price


_D_
_Lt−ℓt_ +1 [with liquidation fee factor] _[ α]_ [) and subsequent reduction of the specula-]


tor’s liabilities by the _ℓt_ +1. The variables _Lt_ +1 and _Nt_ are affected similarly. [12]


If _Xt_ +1 _< c_ ( _Lt_ ), then the speculator’s collateral position is zeroed out in the


liquidation. We define the corresponding events


_At_ = _{Xt_ +1 _≥_ _b_ ( _Lt_ ) _}_


_Bt_ = _{c_ ( _Lt_ ) _≤_ _Xt_ +1 _< b_ ( _Lt_ ) _}._

#### **2.2.6 System of random variables**


Putting all the pieces together, we have the following system of random vari

ables driven by the random process ( _Xt_ ):


11The probability of a large deviation like this is not zero. For instance, it could represent the
possibility of a contentious hard fork that splits ETH value.
12Note that _Nt_ is affected because this is the locked collateral at time _t_ + 1. Alternatively,
working with _Nt_ +1 as locked collateral, we would update _Nt_ +1.


32


_Xt_


_αD_

_Yt_ +1 = [∆] _[t][D][X][t]_ [+1] + ( _N_ [¯] _tXt_ +1 _−_ _Lt_ ) 1 _At∪Bt_ + 1 _Bt_ (3 _Lt −_ 2 _N_ [¯] _tXt_ +1) 1 _−_

_LtXt_     - 2 _N_ ~~[¯]~~ _tXt_ +1 _−_ 2 _Lt_







∆ _[∗]_ _t_ [=]














¯
min - arg max∆ _t_ E[ _Yt_ +1 _|Ft_ ] _,_ _Nt−β_ 1 _Xt_



_β_ 1 _Xt_ _−_ _Lt−_ 1� if _Xt ≥_ _[β]_ _N_ ~~¯~~ _[L]_ _t_ _[t]_ _−_ _[−]_ 1 [1]



~~¯~~
_Nt−_ 1



min - arg max∆ _t_ E[ _Yt_ +1 _|Ft_ ] _, −_ (3 _Lt−_ 1 _−_ 2 _N_ [¯] _t−_ 1 _Xt_ )� if _Xt <_ _[β]_ _N_ ~~¯~~ _[L]_ _t_ _[t]_ _−_ _[−]_ 1 [1]



~~¯~~
_Nt−_ 1



_Lt_ = _Lt−_ 1 + ∆ _[∗]_ _t_



_Nt_ =


_N_ ¯ _t_ =























_Nt−_ 1 + ∆ _[∗]_ _t_ _XZtt_ if _Xt ≥_ _[β]_ _N_ ~~¯~~ _[L]_ _t_ _[t]_ _−_ _[−]_ 1 [1]



~~¯~~
_Nt−_ 1



_X_ _[Z][t]_ _t_ [(∆] _[t]_ [ + (1] _[ −]_ _[α]_ [)(3] _[L][t][−]_ [1] _[ −]_ [2 ¯] _[N][t][−]_ [1] _[X][t]_ [))] if _Xt <_ _[β]_ _N_ ~~¯~~ _[L]_ _t_ _[t]_ _−_ _[−]_ 1 [1]



_Nt−_ 1 + _[Z][t]_



~~¯~~
_Nt−_ 1



_Nt−_ 1 if _Xt ≥_ _[β]_ ~~¯~~ _[L][t][−]_ [1]



~~¯~~
_Nt−_ 1



_Nt−_ 1 _−_ _α_ (3 _Lt−_ 1 _−_ 2 _N_ [¯] _t−_ 1 _Xt_ ) if _Xt <_ _[β]_ ~~¯~~ _[L][t][−]_ [1]



~~¯~~
_Nt−_ 1



_Zt_ = _L_ _[D]_ _t_ _._



In the above, the first case for ∆ _[∗]_ _t_ [comes from maximizing expected value]


∆ _[∗]_
subject to the post-decision collateral constraint while the second cases for _t_ [,]


_Nt_, and _N_ [¯] _t_ apply the liquidation effects that occur during time _t_ .

#### **2.3 Foundational Results**


In this section, we derive foundational results about the model that we will use


to prove the primary results of the paper in the next section.


33


#### **2.3.1 Assumptions**

We begin by defining the assumptions we will use in the rest of the paper.


**Assumption 2.1.** ( _Xt_ ) _is a submartingale with respect to_ ( _Ft_ ) _and is independent from_


( _Lt_ ) _and_ ( _Nt_ ) _._


A submartingale is a stochastic process in which the expected future value,


conditioned on all prior values, is greater than or equal to the current value. The


submartingale assumption can be relaxed somewhat while preserving some re

sults. It is useful, though not necessarily critical, in our proof of problem concav

ity. However, the results are most meaningful in a setting like a submartingale,


which always provides a fundamental reason that a speculator might desire


leverage. In such a setting, it is _conceivable_ that the stablecoin could maintain a


dollar peg, whereas in long periods of negative expected returns, the stablecoin


concept falls apart as no speculators will want to participate. As noted in the


introduction, such a deviation from the submartingale setting appears to have


- ccurred in March 2020.


**Assumption 2.2.** _Each Xt_ +1 _has a conditional probability distribution given Ft, which_


_admits a density function ft that is continuous almost surely._


Equivalently, we consider the process in terms of returns _Rt_, where _Xt_ +1 =


_XtRt_ +1. Conditioned on _Ft_, then _Rt_ +1 admits density function _gt_ . In the i.i.d.


setting for ( _Rt_ ), the time dependence can be dropped. For most results, we do


not need to assume i.i.d.


**Assumption 2.3.** _There is some upper bound r ≥_ sup _n_ E[ _Rn|Fn−_ 1] _._


34


The next assumption is needed to interchange derivative and integration op

erators. It also translates to an upper bound on _Lt_ and a lower bound on _Nt−_ 1.


**Assumption 2.4.** _There is some upper bound u ≥_ _c_ ( _Lt_ ) _for all Lt._


The next assumption ensures that the STBL price is bounded away from in

finity.


**Assumption 2.5.** _Lt ≥_ _v >_ 0 _for some v._


The next assumption simplifies repurchase considerations. It is reasonable


_r_
given a reasonable bound - n expected returns.


**Assumption 2.6.** _The liquidation premium factor α is sufficiently high that the repur-_


_chase price in a liquidation is >_ 1 _almost surely._


The next assumption translates to a reasonable condition on _X_ distributions


considering _b_ ( _Lt_ ) is linearly increasing whereas _c_ ( _Lt_ ) decreases with _Lt_ .


**Assumption 2.7.** P( _Bt|Ft_ ) = P _c_ ( _Lt_ ) _≤_ _Xt_ +1 _≤_ _b_ ( _Lt_ ) _|Ft_ _is increasing in Lt._

            -            

Define _ψ_ ( _Lt_ ) := E[ _Yt_ +1 _|Ft_ ]. Note that _ψ_ could have a subscript _t_, or equiv

alently other time _t_ inputs ( _N_ [¯] _t, Xt, gt_ ), but we relax notation as we only use it


in the context of time _t_ . The next assumption ensures that _ψ_ is concave in _Lt_, a


result that we prove in Proposition 2.1. When this is not met, the model starts


in a strange region in which the speculator’s objective can be non-concave and


real and nominal liability values can be disassociated. This is an artifact of the


simplified structure of demand in the model, which we would expect to adapt


in such a setting. Thus we expect the model to not apply well outside of this


assumption. Live stablecoin systems that remain operational readily satisfy this


assumption.


35


**Assumption 2.8.** 2( _NcαDtNc−Ltt_ ) [2] _[≤]_ [2] _[ (note][ L][t][ ≥]_ 46 [27]



46 [27] _[α][D][ (or][ αZ][t][ ≤]_ 27 [46]



27 _[is sufficient).]_



Live stablecoin systems readily satisfy this assumption. [13]


Additionally, the next assumption ensures that _ψ_ is _strictly_ concave in _Lt_,


which we also prove in Proposition 2.1. Notice that this means that _either_ the


submartingale inequality is strict at time _t_ - r there is non-zero probability that


a liquidation is triggered in the next step. Given that the latter is certainly rea

sonable, this assumption is not much stronger than the basic submartingale as

sumption.


**Assumption 2.9.** _Either_ E[ _Rt_ +1 _|Ft_ ] _>_ 0 _or_


P( _Bt|Ft_ ) = P _c_ ( _Lt_ ) _≤_ _Xt_ +1 _≤_ _b_ ( _Lt_ ) _|Ft_ _>_ 0 _._

            -            

While strict concavity of _ψ_ is not necessary for all results, it does simplify


the analysis considerably. More generally, concavity of _ψ_ could reasonably be


expected in many settings, and so the assumptions can probably be relaxed. In

formally, reasonable distributions for _Xt_ will have concentration about the cen

ter. In this case, moving ∆ _t_ in the positive direction, expected liabilities increase


faster than revenue from new STBL issuance. Moving ∆ _t_ in the negative direc

tion, the cost to buyback grows faster than the decrease in expected liabilities.

#### **2.3.2 Concavity and scale invariance**


Our first result is to prove that _ψ_ ( _Lt_ ) is concave in _Lt_ .


13Recall that _α ≥_ 1 is the liquidation cost multiple (reflecting the fee paid to liquidators).
Assuming _α_ = 1 _._ 05, the sufficient condition in Assumption 2.8 is implied by _Zt <_ 1 _._ 62, which
is verified in practice for all live stablecoins.


36


**Prop. 2.1.** _Given Assumptions 1-8, ψ_ ( _Lt_ ) := E[ _Yt_ +1 _|Ft_ ] _is concave in Lt._


_Further, given additional Assumption 9, ψ_ ( _Lt_ ) _is_ strictly _concave in Lt._


[Link to Proof]


In deriving some results, it will be useful to make assumptions about the


scale of the system. The next result shows that results about _Zt_ should translate


to differently scaled systems, validating that such results will describe the STBL


price process more generally. In the following, we define _h_ to output _Lt_ as a


function of the system state.


**Prop. 2.2.** _Consider a system setup_ ( _Lt−_ 1 _, D, Nt−_ 1) _with ETH price process_ ( _Xt_ ) _. For_


_γ >_ 0 _,_


_h_ ( _γLt−_ 1 _, γD, γNt−_ 1 _, Xt_ ) = _γh_ ( _Lt−_ 1 _, D, Nt−_ 1 _, Xt_ )

_h_ ( _Lt−_ 1 _, D,_ _γ_ [1] _[N][t][−]_ [1] _[, γX][t]_ [) =] _[ h]_ [(] _[L][t][−]_ [1] _[,][ D][, N][t][−]_ [1] _[, X][t]_ [)] _[.]_


_As a result, the STBL price process_ ( _Zt_ ) _is equivalent across these system rescalings._


[Link to Proof]


Under these condtions, we can interchange derivative and integration oper

ators in _∂ψ_
_∂Lt_ [according to Leibniz integral rules (a variation of dominated con-]


vergence theorems). The speculator’s choice of _Lt_ will fulfill the first order con

dition of _∂ψ_
_∂Lt_ [= 0][. From concavity, we can then conclude that the speculator]

chooses to increase the STBL supply when _∂∂Lψt_ [(] _[L][t][−]_ [1][)] _[ >]_ [ 0][ and to decrease the]

STBL supply when _∂_ _[∂]_ _L_ _[ψ]_ _t_ [(] _[L][t][−]_ [1][)] _[ <]_ [ 0][.]


37


Note that we can derive sufficient conditions for these events using


Lemma 2.7 from the Appendix. Such conditions can be useful as concrete in

terpretations of the events and can be checked against incoming data. That


said, these general sufficient conditions are far from necessary if we are given


additional information about the return distributions.

#### **2.3.3 Economic limits to speculator behavior**


We now present some fundamental results that bound the speculator’s decision

making. These results will be useful in developing the primary results of the


paper in the next section. The next result introduces a lower bound to the spec

ulator’s STBL supply decision that arises from the fundamental price impact of


repurchasing STBL.


**Prop. 2.3.** _Suppose the pre-decision collateral constraint is met at time t. There is a_


_computable lower bound to_ ∆ _t._


We can interpret the lower bound in terms of a balance sheet constraint de

scribing when the speculator’s ETH position is exhausted in a repurchase. We


give the specific bound in the proof but note that it is not especially useful on


its own. Given information about the returns distribution and the level of cur

rent collateral and considering _∂_ _[∂]_ _L_ _[ψ]_ _t_ [, much better bounds are possible. Note that]


if _ζ >_ 0 is high enough, the lower bound may be the speculator’s entire debt


position, which would be expected in a liquid environment with heterogeneous


agents.


[Link to Proof]


38


The next result provides a useful upper bound to the speculator decision _Lt_ .


The result is derived from incentives to issue STBL. Intuitively, it says that if


supply is below this bound, then a speculator may see a profitable opportunity


to expand supply. It’s simply not profitable to issue more STBL than this bound.


This doesn’t mean that the speculator decides to achieve the bound, however, as


it underestimates the liquidation costs that the speculator might face. [14] Notice


_κ ∼_ 1.
that the bound is strongest when we have


**Prop. 2.4.** _Suppose either of the following hold for given κ:_







_Xt_

- _c_ _[b]_ ( [(] _L_ _[L]_ _t_ _[t]_ ) [)]

_Xt_



_αDN_ [¯] _tXtz_

- 3 _−_ 2( _N_ ~~[¯]~~ _tXtz−Lt_ ) [2] - _gt_ ( _z_ ) _dz ≤_ 0 _and_ P( _At ∪_ _Bt|Ft_ ) _≥_ _κ_ _[−]_ [1] _>_ 0




  - 1 _≥_ P( _At|Ft_ ) _−_ 2 P( _Bt|Ft_ ) _≥_ _κ_ _[−]_ [1] _>_ 0 _._


_Then Lt ≤_ ~~�~~ _κLt−_ 1 _D_ E[ _Xt_ +1 _|Ft_ ] _/Xt._


[Link to Proof].


The first condition comes from the derivative of the expected liquidation ef

fect with respect to _Lt_ taking _β_ = [3] 2 [. The integrand can be interpreted as the ef-]


fective leverage change in a given liquidation. This quantity is _<_ 0 evaluated at


_b_ ( _Lt_ ) (small liquidations effectively reduce leverage) whereas it is _>_ 0 evaluated


at _c_ ( _Lt_ ) (in very large liquidations, leverage reduction may not be effective due


to effect on repurchase price). The integral condition then says that, in expecta

tion, liquidations effectively reduce leverage. This is a reasonable assumption


14The model as formulated does not incorporate an interest rate paid by the speculator on
issued STBL (the ‘stability fee’ in Dai). Additionally, it does not incorporate a possible yield if
the speculator creates STBL to lend on a lending platform as opposed to selling on the market.
Under either of these extensions, Proposition 2.4 would change by an appropriate factor.


39


given a starting state of sufficient over-collateralization, since reasonable distri

butions of _Xt_ +1 will place most mass in the integral around _b_ ( _Lt_ ) as opposed to


_c_ ( _Lt_ ), which is a tail event.


The second (alternative) condition says that the probability of having a liq

uidation is sufficiently smaller than not having a liquidation.


This result holds if _either_   - f the two conditions hold, both of which could be


checked in data-driven modeling. We will formalize an assumption like the first


condition in the next section. Similar results going forward could be derived


instead using a variation on the second condition.

#### **2.4 Stable and Unstable Domains**


The primary results of the paper characterize regions in which the stablecoin


price process can be interpreted as ‘stable’ and ‘unstable’. In this section, we


derive these results for the given model of a single speculator facing imperfectly


elastic demand for STBL. In the next section, we consider generalizations of


the model and how these results will differ given different design and market


structures.

#### **2.4.1 Domain barriers/Stopped processes**


We first establish results in terms of barriers. While the stablecoin process is


within certain barriers, we prove that it behaves in ways that are interpretable


as ‘stable’ and ‘unstable’. These barriers are generally stopping times, and we


40


proceed by considering the stopped processes.


Assume that in the initial condition we have E  - _L_ 11 _[|F]_ [0]  - _≤_ _L_ 10 [. We define the]


following stopping times:


 - _τ_ is the hitting time of E  - _Lt_ 1+1 _[|F][t]_  - _>_ _L_ 1 _t_


 - _Tm_ is the hitting time of _Zt > m_, for _m ≥_ _Z_ 0


 - _S_ 1 is the hitting time of E[ _Lt_ +1 _|Ft_ ] _< Lt_


 - _S_ 2 is the hitting time of E[ _Lt_ +1 _|Ft_ ] _≥Lt_ such that _S_ 2 _> S_ 1.


As we will see, while the stablecoin mechanism is working as intended, we


generally expect the STBL supply to increase (equivalently in this setting, the


STBL price to decrease, though in slow and bounded way). With this context


in mind, _τ_ represents the first time we _expect_ the STBL price to increase. No

tice that this is an expectation of reciprocal of supply, a convex function, and


so through Jensen’s inequality, this is weaker than expecting the speculator to


deleverage/reduce supply. In particular, we have _τ ≤_ _S_ 1.


Note that the expectations of the process are not necessarily the same as the


_τ_
movements of the process: does not necessarily correspond to the first time


the process actually increases in price. We track this with _Tm_, the time the STBL


price breaches a given level above _Z_ 0, which may be before or after _τ_ .


The stopping times _S_ 1 and _S_ 2 track when expectations about STBL sup

ply change. These can be equivalently stated (and calculated in a data-driven


model) based on expectations about the derivative of E[ _Yt_ +2 _|Ft_ ] with respect to


_Lt_ +1 evaluated at _Lt_, similarly to the discussion from the previous section on


concavity.


41


Before proceeding, we formalize stopped versions of assumptions in Propo

sition 2.4. The interpretation of these assumptions is the same as discussed in


the previous section. Note that the results going forward could also apply more


generally subject to additional stopping times embedding these assumptions.


For notational simplicity, we just present the results subject to the stopping


times already defined with the assumptions given.


**Assumption 2.10.** _For t ≤_ _τ_ _,_ P( _At ∪_ _Bt|Ft_ ) = P( _Xt_ +1 _≥_ _c_ ( _Lt_ ) _|Ft_ ) _≥_ _κ_ _[−]_ [1] _>_ 0 _._



**Assumption 2.11.** _For t ≤_ _τ_ _,_ - _c_ _[b]_ ( [(] _LXt_ _[L]_ _t_ _[t]_ ) [)]

_Xt_



_αDN_ [¯] _tXtz_

- 3 _−_ 2( _N_ ~~[¯]~~ _tXtz−Lt_ ) [2] - _gt_ ( _z_ ) _dz ≤_ 0 _._



Notice that _κ_ will be _>_ 1 but _∼_ 1 as _X < c_ ( _Lt_ ) is a low probability event.


Recall that the STBL price _Zt_ is a function of collateral value, expectations


about ETH returns, and expectations of liquidation costs (related to tail risks).


These factors enter the speculator’s supply decision, which then enters _Zt_ . Go

ing forward, we will explore how changes in these affect the STBL price process.

#### **2.4.2 ‘Stable’ domain**


Subject to the barriers _τ_ and _Tm_, the stablecoin process can be interpreted as


stable in the following ways. In this domain, we derive bounds on large price


movements and quadratic variation. We show below that for realistic values of


parameters, the bounds are sufficiently powerful in practice.


Our first result bounds _Zt_ under the condition _TZ_ 0 _> τ_ . Conditioned on this,


the price is contained within small variation–e.g., consider _Z_ 0 = 1 and consider


1 E[ _Xt_ +1]
_κr_ _[∼]_ [1][. Recall that] _[ r]_ [ represents the upper bound on returns,] _[ r]_ [ = sup] _[t]_ _Xt_,


42


whereas _κ_ _[−]_ [1] is a lower bound for the probability that the collateral is not ex

hausted in a liquidation event, P( _Xt_ +1 _≥_ _c_ ( _Lt_ ) _|Ft_ ) _≥_ _κ_ _[−]_ [1] .


**Prop. 2.5.** _If TZ_ 0 _> τ_ _, then_



2 _[t]_ _−_ 1
( _κDr_ ) 2 ~~_[t]_~~



2 ~~_[t]_~~ _L_



_Z_ 0 _≥_ _Zt∧τ ≥_




~~�~~



_D_ _D_
_κLt∧τ_ _−_ 1 _r_ _[≥]_ 2 _[t]_



1 _._
2 ~~_[t]_~~
0



_Furthermore for any t, Lt∧τ ≤_ _κDr and Zt∧τ ≥_ _κr_ 1 _[.]_


[Link to Proof]


The condition _TZ_ 0 _> τ_ introduces dependence on future events. As such, we


can’t conclude with the information at time _t_ that the _t_ + 1 price is bounded in


this way.


However, we can bound our expectations on the _t_ + 1 price given the infor

mation at time _t_ ( _Ft_ ). This approach relies on the fact that the versions of the


process behave as submartingales in the stopped setting.


**Prop. 2.6.** ( _Lt∧τ_ ) _is a submartingale bounded above and_ ( _Zt∧τ_ ) _is a supermartingale_


_bounded below. Thus they converge almost surely._


[Link to Proof]


An immediate bound on expected price comes from the fact that stopped


version of _Zt_ is a supermartingale. This is the first result of the next proposition.


Additionally, with a stronger assumption on ( _Xt_ ) that conditional expectation


- f returns is non-decreasing within the domain barriers, we can bound the ex

pected price further.


43


**Prop. 2.7.** _The process_ ( _Zt∧τ_ _∧TZ_ 0 ) _is bounded in expectation by_


_Z_ 0 _≥_ E[ _Zt∧τ_ _∧TZ_ 0 ] _≥_ _κr_ [1] _[.]_


_Further, assuming that for t < τ_ _,_ (E[ _Rt_ +1 _|Ft_ ]) _is non-decreasing, then for t ≤_ _τ_ _,_



_Zt−_ 1 _≥_ E[ _Zt∧τ_ _|Ft−_ 1] _≥_







_D_

_κLt−_ 1 E[ _Rt|Ft−_ 1] _[.]_




[Link to Proof]


Going forward, we will work with a variation on the price process


_Zt_ _[′]_ [:=] _[ |][m][ −]_ _[Z][t][|]_ for given _m ≥_ _Z_ 0 _._


_m_ = 1
Using, this has concrete interpretation as the absolute price deviation


from the stablecoin peg. The stopped version of this process has the useful


property of being a non-negative submartingale. In addition, ( _Zt_ _[′]_ [)][ shares similar]


large deviation and quadratic variation properties with ( _Zt_ ), which we explore


in the remainder of this subsection.


**Lemma 2.1.** _The stopped process_ ( _Zt_ _[′]_ _∧τ_ _∧Tm_ [)] _[ is a non-negative submartingale.]_


[Link to Proof]


We define the maximum process over some process ( _θt_ ) as _θN_ _[∗]_ [= max] _[t][≤][N][ |]_ [Θ] _[t][|]_ [.]


The next result bounds the expected maximum of the deviation process ( _Zt_ ).


**Prop. 2.8.** _Suppose m ≥_ _Z_ 0 _. Denote E_ := E[ _Zτ_ _∧Tm −_ _m|Zτ_ _∧Tm > m_ ] _. Suppose any_


_one of the following conditions holds:_


 - _κr_ 1 _[> m][ and][ E >]_ _κr_ 1 _[−]_ _[m]_


44


 - _κr_ 1 [=] _[ m][ and][ E >]_ [ 0]


 - _κr_ 1 _[< m][ and][ E][ ≥]_ [0] _[.]_


_Then_ E[ _Zτ_ _[′∗]_ _∧Tm_ []] _[ ≤]_ [2] - _m −_ _κr_ [1] - _._


[Link to Proof]


1
The value ( _m −_ _κr_ [)][ describes the range of the domain considered. Prior to]


_Tm_, we know that the price falls in this range. The nontrivial part is describing


what happens at the stopping time as it _exceeds_ this range if the stop is triggered


by _Tm_ . The value _E_ is the expected deviation at the stopping time _given_ that _Tm_


triggers the stop. By definition, we have that _E >_ 0. Given reasonable _κ_, _r_, and


_m_
, the condition for Proposition 2.8 is satisfied quite broadly. For instance, the


concrete instance with _m_ = 1 is satisfied since _κr_ 1 _[<]_ [ 1][ taking into account the]


above discussion on _κ_ .


Notice that the analysis for the proof can lead to better bounds if we have


more information about _E_ - r _p_ := P( _Zτ_ _∧Tm ≤_ _m_ ), e.g., by incorporating in

formation from other results above or from knowledge about the distributions


- f ( _Xt_ ), such as from historical data. Additionally, the analysis can be used to


bound either _E_ - r _p_ given bounds on the other.


We now state the first main results of the paper. Our next result applies


Doob’s inequality to bound the probability of large deviations in the stopped


process.


**Theorem 2.2.** _For m ≥_ _Z_ 0 _and ϵ >_ 0 _,_



P - _n≤_ max _τ_ _∧Tm_ _[Z]_ _n_ _[′]_ _[> ϵ]_ - _≤_ 2 _ϵ_ _[−]_ [1] - _m −_ _κr_ [1]


45



_._



[Link to Proof]


The result can be quite powerful. Consider the concrete case of _m_ = 1, in


which case _Zt_ _[′]_ [describes the deviation from the peg, and take (arguably reason-]


able) _κ_ _[−]_ [1] = 0 _._ 999 (99 _._ 9% chance _Xt_ won’t drop below _c_ ( _Lt_ )) and _r_ annualized as


1.5 (daily _r_ = 1 _._ 0011). Then the probability that the stablecoin deviates from the


peg by more than 0.1 is P( _Zτ_ _[′∗]_ _∧T_ 1 _[>]_ [ 0] _[.]_ [1)] _[ ≤]_ [0] _[.]_ [042][.]


Our next result derives from a form of Burkholder’s inequality that applies


to non-negative submartingales. We define the quadratic variation of ( _Zt_ _[′]_ [)][ by]




[ _Z_ _[′]_ ] _t_ :=



_t_

- ( _Zk_ _[′]_ _[−]_ _[Z]_ _k_ _[′]_ _−_ 1 [)][2] _[.]_


_k_ =1



The quadratic variation is a stochastic process that measures how spread out


the underlying process is. Its expectation at time _t_ is related to the variance


at that time, supposing variance is defined–in particular, they are equal if the


underlying process is a martingale. The result bounds the probability of large


quadratic variation in the stopped process. In essence, with high probability,


the quadratic variation can’t be _too far_ away from the expected maximum.


**Theorem 2.3.** _Suppose m ≥_ _Z_ 0 _and ϵ >_ 0 _. Then_




[ _Z_ _[′]_ ] _τ_ _∧Tm > ϵ_ _≤_ 6 _ϵ_ _[−]_ [1] _m −_ [1]

     - _κr_

      


P

 - ~~�~~



_κr_



_._





[Link to Proof]


This result is also quite powerful. Considering the same setting as above, we


have


P( ~~�~~ [ _Z_ _[′]_ ] _τ_ _∧T_ 1 _>_ 0 _._ 1) _≤_ 0 _._ 127


46


in the stable domain.


Bounds on the expectation of quadratic variation can also be obtained using


a more classical form of Burkholder’s inequality, albeit with stronger assump

tions. We develop this idea in the next remark.


**Remark 2.1.** _There is an additional form of Burkholder’s inequality that extends to non-_


_p_ [�]
E _Z_ _[′]_
_negative submartingales. If we are additionally given a useful bound on_ _τ_ _∧Tm_ 
                                 - �


_for some_ 1 _< p < ∞_ _(for instance, if we have some distribution assumptions on_ ( _Xt_ ) _),_


_then we can apply Lemma 3.1 in [45] to derive the following bound on quadratic varia-_


_tion expectations:_



1
_p_ 9 _p_ 2 _p_ [�] _p_ [1]
_≤_ [E] _Zτ_ _[′]_ _∧Tm_ 
[1] 1 _−_ _p_ _[−]_ [1] - �



_p_ [�] _p_ [1]
E [ _Z_ _[′]_ ] _τ_ _∧Tm_ 
 - �



_p_

_._



_A topic of ongoing research is obtaining the Best constants/bounds in Burkholder’s in-_


_equality, which may be able to tighten the bound. The classical two-sided Burkholder_


_inequailty may not extend to non-negative submartinagales. In general, only the first_


_half of the Burkholder inequality (bounding expectations about quadratic variation by_


_the maximum) extends to this setting and only for_ 1 _< p < ∞. This contrasts with_


_Proposition 2.3, where we can derive results about probability of large quadratic varia-_


_tion of non-negative submartingales for the p_ = 1 _case. From a practical point of view,_


_this may be sufficient._


Notice that with an effective bound on the expectation of quadratic variation


(QV) of the entire stable process, we have by law of large numbers


_QV_

_→_ 0 as _n →∞._
_n_


So the longer the process is stable, the smaller the variability.


As we’ve characterized this ‘stable’ domain based on _τ_ and _Tm_, an exit from


_τ_
this region corresponds to either a change in expectations ( ) or a large deviation


47


event ( _Tm_ ). In actual applications, we will know when these stopping times


arrive (or will at least have good measures of it, when hard to directly observe).


These could be used by system stakeholders as indicators that the local regime


is changing. Statistical analysis on historical data could also predict how likely


we are to see such indicators in coming steps.

#### **2.4.3 ‘Unstable’ domain**


We now characterize how the stablecoin can be interpreted as unstable outside


- f the barriers described above. The intuition here is that the speculator’s po

sition is nearer to _c_ ( _Lt_ ) and _b_ ( _Lt_ ), and so expected costs of liquidation increase


and are more sensitive to the threshold proximity, in addition to being driven by


the volatile process ( _Xt_ ). The remaining results in this section characterize a de

flationary regime that is connected with instability in terms of forward-looking


variance of stablecoin prices and large deviations. In this regime, we observe


deleveraging spirals, which resemble short squeezes, and are counterintuitive


as they lead to stablecoin price appreciation during times of collateral shock and


lead to faster collateral drawdown.


Our next result characterizes a deflationary regime defined by stopping


times _S_ 1 and _S_ 2. In such a setting, an opposite behavior occurs compared to


the stable region: ( _Zt_ ) behaves as a submartingale, tending to increase in price.


The submartingale nature of the stablecoin price underpins the short squeezes


within _deleveraging spirals_ .


**Theorem 2.4.** _Restarting the process at S_ 1 _, we have that_ ( _Lt∧S_ 2) _is a supermartingale_


_and_ ( _Zt∧S_ 2) _is a submartingale._


48


[Link to Proof]


The previous result guarantees that the process, after crossing _S_ 1, enters a de

flationary regime in a precise sense. This deflationary regime can be triggered


by the factors affecting _S_ 1, such as any of the following: shocks to collateral


levels, increased expectations around deleveraging costs, or depressed ETH ex

pectations. Similarly to the results above, in real applications, these stopping


times can be used by stablecoin stakeholders as indicators that the local regime


is changing and to statistically estimate the probable lengths of such deleverag

ing spirals.


The intuition behind deleveraging spirals is illustrated in Figure 2.2. In an


equilibrium, the stablecoin supply is matched to demand. As a first wave of


speculator liquidations occur, whether voluntary deleveraging or automated by


the protocol, collateral is used to repurchase the stablecoin to reduce the supply.


In an imperfectly elastic market, this causes an imbalance in demand relative to


supply, and an increase in stablecoin price is needed to reduce demand. This


has an amplifying effect, however, in follow-on rounds of liquidations: more


collateral is needed to reduce supply by the same amount because of the in

creased stablecoin price, and each round of liquidations continues to increase


the stablecoin price.


Black Thursday in March 2020 provides strong evidence of deleveraging spi

rals in the Dai stablecoin. ETH price crashed _∼_ 50% on 12 March 2020 (Fig

ure 2.3a) This triggered a wave of liquidations in Dai, as well as other cryptocur

rency systems. These liquidations led to a cornering effect from deleveraging


spirals in the Dai market, as shown in Figure 2.3b. Speculators faced premiums


in excess of 10% to deleverage during the crisis and lingering premiums _>_ 2%


49


Figure 2.2: Illustration of deleveraging spirals. In liquidations, collateral is used
to reduce supply. Stablecoin price rises in response to imbalance with demand.
This has an amplifying effect in follow-on liquidations.


several weeks after. The cornering effect is also supported by lending rates on


Dai, which reached high double digits during the crisis (Figure 2.3c). Maker was


also affected by global mempool flooding on Ethereum during the crisis, which


caused many Dai liquidation auctions to clear at near zero prices. This had the


effect of amplifying the deleveraging effect on collateral and led to a $4m short

fall in the system. See [36, 182] for more details. Many market participants were


surprised in this crisis that Dai traded at significant premiums despite the much


riskier state of Maker in terms of collateral and liquidations, which our model


explains as deleveraging spirals.


**Remark 2.2.** _(Interaction with cascading liquidations) A different type of deleveraging_


_spiral can occur in debt security models when the collateral asset price is endogenous to_


_the model and can be depressed from the market impact of liquidations (e.g., fire sales)._


_In this context, liquidations can cascade with a first round of liquidations triggering a_


50


(a)


(b)


(c)


Figure 2.3: Black Thursday in March 2020. (a) _∼_ 50% ETH price crash (OnChainFX). (b) Deleveraging effects on Dai price and volatility (OnChainFX). (c)
Deleveraging effects on Dai lending rate (LoanScan)


51


_follow-up rounds due to the impact on the collateral market. Conceptually, when this_


_endogenous collateral effect is added to our model, the two deleveraging spiral types_


_amplify each other. In particular, when the price of the stablecoin increases from the ef-_


_fects described above, more collateral must be liquidated to deleverage the same amount,_


_and this greater collateral liquidation has a higher impact on the collateral asset market,_


_which can trigger further liquidations cyclically in larger size than with the fire sale_


_effect solely. We discuss how to endogenize collateral asset prices to the model in the_


_Appendix._


We now derive practical tools that will connect these regimes containing


deleveraging spirals with instability in terms of forward-looking price variance


- f the stablecoin, and which do not require the detection of whether _S_ 1 has oc

curred. This formalizes the high price variation observed in Dai during and


after Black Thursday. We begin in the next remark by setting up a variance


estimation idea based on Taylor approximation.


**Remark 2.3.** _(Estimating variances) Taylor approximations can be applied to estimate_


_the variances of the stablecoin process. Consider Xt_ = _Xt−_ 1 _Rt for return Rt ≥_ 0 _. For_


_notational clarity, define_ [15]


_h_ ( _ρ, n_ ) := arg max
_Lt_ [E][[] _[Y][t]_ [+1] _[|F][t]_ [] =] _[ L][t][,]_


_where ρ, n are realizations of Rt,_ _N_ [¯] _t. Variance in stablecoin supply follows_


2
_Var_ ( _Lt|Ft−_ 1) _≈_ _h_ _[′]_ [ �] E[ _Rt|Ft−_ 1] _,_ _N_ [¯] _t_        - _Var_ ( _Rt|Ft−_ 1)


_and the stablecoin price_ _**variance approximation**_ _is_


_Var_ ( _Zt|Ft−_ 1) _≈_ _[D][h][′]_ [(][E][[] _[R][t][|][F][t][−]_ [1][]] _[,]_ [ ¯] _[N][t]_ [)][2] _Var_ ( _Rt|Ft−_ 1) _._ (2.1)

E[ _Lt|Ft−_ 1] [4]


15As in the case of _ψ_, _h_ could have a subscript _t_ (or equivalently other time _t_ inputs), but we
relax notation as we only use in the context of time _t_ .


52


_This is given informally, but could in principle be formalized using two steps of com-_


_pounded Taylor approximation error. The approximation error is arguably moderate_


_considering that our domain is bounded away from singularities (e.g., our lower bound_


_results on L)._


This variance approximation (Eq. 2.1 in Remark 2.3) is low in the stable do

main and can be high in the unstable domain, as formalized in the following


Theorem 2.5. We introduce a few more assumptions that we use only in deriv

ing the remaining results in this section. All of these assumptions come down


to assumed properties of the _Rt_ distribution.


**Assumption 2.12.** _The post-decision collateral constraint at time t is not binding in_


_the speculator’s maximization._


This first assumption means that the speculator’s objective fully accounts


for the post-decision collateral constraint (i.e., by maximizing the objective, the


speculator by extension also satisfies the constraint). This is reasonable unless


expected returns are excessively high.


**Assumption 2.13.** _Returns Rt−_ 1 _and Rt are independent._


**Assumption 2.14.** _ψ is twice continuously differentiable._


This last assumption restricts the density _gt_ . We now present the result,


which applies the implicit function theorem to derive the derivatives of _h_, which


describe the sensitivity of _h_ to price and collateral level.


**Theorem 2.5.** _Under the above assumptions, the following hold:_


_1._ _∂_ _∂_
_∂ρ_ _[h]_ [(] _[ρ, n]_ [)] _∂n_ _[h]_ [(] _[ρ, n]_ [)] _[ exist;]_


53


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



_4. ∃ε with_ 0 _< ε <_ 1 _, s.t._ _∂ρ∂_ _[h]_ [(] _[ρ, n]_ [)] _[ >]_ [ 1] _[ if][ ρ < ε][,][ L][t][ >]_ 46 [27] _[α][D][, and][ c][t][ >]_ [ 2] _[.]_



_As a result, the variance approximation in Eq. 2.1 increases by order of_ _R_ 1 _t_ [2] _[in][ −][R][t][ and]_

_N_ ~~¯~~ 1 _t_ [2] _[in][ −][N]_ [¯] _[t][.]_


[Link to Proof]


Theorem 2.5 shows that the variance approximation in Eq. 2.1 in Remark 2.3


increases by order of _R_ 1 _t_ [2] [during an ETH return shock (result 2). Recall that] _[ R][t]_ [ is]


multiplicative return, and so the effect is large for a significant shock _Rt <_ 1.


Similarly, settings with lower collateralization in the initial conditions have


~~¯~~ 1
higher variance approximation by order of _Nt_ [2] [(result 3). Such differences in]


initial conditions of collateral could result from, for example, different realiza

tions of liquidations or the speculator abandoning its collateral position (and so


extracting any excess collateral it can). Result 4 shows that there are cases where


the _h_ _[′]_ factor in the variance approximation is _>_ 1, meaning that the variance of


_Rt_, the inherently volatile process, will carry through directly to _Zt_, the ‘stable’


process.


Note that the extra conditions on the scale of _Lt_ and _ct_ in Theorem 2.5 results


2-4 may seem strange at first sight. Since the ( _Zt_ ) process is scale-invariant, as


proven in Proposition 2.2, the results about _Zt_ variance hold more generally. In


1
_∼_
particular, recall that a term of _Lt_ [shows up in the variance approximation in]


Remark 2.3, which will cancel out the conditions on scale.


54


Up to this point, we have only been able to say things about variance esti

mations. We will now show that the ‘stable’ and ‘unstable’ regimes are well

interpreted in the following sense: given different initial conditions of the same


process, the forward-looking stablecoin price variances are indeed distinct. If


we start in the unstable regime, we will always have higher variance than if we


start in the stable regime. The next result formalizes this.


**Theorem 2.6.** _In addition to the previous assumptions, suppose Xt ≥_ _b_ ( _Lt−_ 1) + _ϵ for_


_some ϵ >_ 0 _(the pre-decision collateral constraint is exceeded by ϵ, which restricts the_


_ranges of both Xt and_ _N_ [¯] _t−_ 1 _). Consider two possible states s and u of the stablecoin_


_at time t that differ only in collateral amounts_ _N_ [¯] _t_ _[s]_ _−_ 1 _[> N]_ _t_ _[ u]_ _−_ 1 _[and evolve driven by the]_


_common price process_ ( _Xt_ ) _. Then the forward-looking price variances satisfy_


_Var_ ( _Zt_ _[s][|F][t][−]_ [1][)] _[ <][ Var]_ [(] _[Z]_ _t_ _[u][|F][t][−]_ [1][)] _[.]_


[Link to Proof]


Special care should be given to the treatment of _Zt_ under the condition


_Xt ≤_ _c_ ( _Lt−_ 1), as the STBL price may no longer be well-defined without _ζ >_ 0


as no collateral remains. In a real system, this is equivalent to the event that


all speculators are wiped out. The reason for our condition on _Xt_ in the above


result is partly to keep things well-defined and partly because there can be a


non-smooth point in _h_ at _Xt_ = _b_ ( _Lt−_ 1).


Similar variance difference results can be derived for varying initial condi

tions of _Xt−_ 1 and _Lt−_ 1 as opposed to _N_ [¯] _t−_ 1. In some sense, these are all similar as


they change the initial collateralization level, though there will be some differ

ence in price effect.


55


These analytical results describe regimes in which the stablecoin can be in

terpreted as stable and unstable. As we have discussed, they can be adapted


into data-driven risk tools, for instance to estimate probabilities of peg devia

tions and to infer about how likely regimes are to change in the near future.


While these results apply over limited steps ahead–e.g., forward-looking


variance is derived for the next time period–they _do_ point in the right direction


that stability domains are related to traditional measures in finance. Naturally,


it would be good to have results describing further periods into the future. In


principle, these could be estimated, although the process in this section is al

ready complex. The fact that we are able to relate these regimes analytically


to forward-looking variance is already a step ahead, and a valuable new result


in its own right. We conjecture that it could work similarly over multi-steps,


though in less tractable ways.

#### **2.5 Stability in ‘Perfect’ Settings**


In the previous section, we considered the given model of a single speculator


facing imperfectly elastic demand for STBL. We now consider idealized set

tings, in which STBL demand is perfectly elastic and/or unlimited speculator


supply exists. In these idealized settings, we demonstrate that stablecoin can be


interpreted as well-stabilized.


56


#### **2.5.1 Perfectly elastic demand**

Under perfectly elastic demand, STBL demand is time-dependent _Dt_, which


adapts in each time period to match STBL supply. This results in _Zt_ = 1. In


this case, the speculator’s issue and repurchase price is always $1 and $ _α_ in a


liquidation. The problem simplifies to evaluating


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


_∂ψ_ _β_
In this setting, we have _∂Lt_ [=][ E][[] _[R][t]_ [+1] _[|F][t]_ []] _[ −]_ [P][(] _[A][t][ ∪]_ _[B][t]_ [)] _[ −]_ _β−_ 1 [(] _[α][ −]_ [1)][ P][(] _[B][t]_ [)][.]


Recalling that P( _At_ ) and P( _Bt_ ) are functions of _Lt_ and supposing a non-binding


collateral constraint, the speculator chooses _Lt_ such that


_β_
E[ _Rt_ +1 _|Ft_ ] = P( _At ∪_ _Bt_ ) +
_β −_ 1 [(] _[α][ −]_ [1)][ P][(] _[B][t]_ [)] _[.]_


Noting that E[ _Rt_ +1] _≥_ 1, P( _At ∪_ _Bt_ ) is decreasing in _Lt_ but generally _∼_ 1, and


P( _Bt_ ) is increasing in _Lt_, this is interpretable as the speculator balancing ex

_β_
pected return against _β−_ 1 _[×]_ [ the expected (constant) liquidation cost in deciding]


whether to issue a new unit of STBL.


In this setting, the STBL price is identically $1 and the speculator only faces


the risk of leveraged ETH declines subject to a fixed liquidation fee. Liquida

tions generally work well to keep the system over-collateralized, and the only


real risk to STBL holders is from extreme single period declines in ETH price.


57


#### **2.5.2 Unlimited speculator capital supply**

Suppose there is an infinite depth of speculator’s capital ready to enter the STBL


market given what they see as a profitable opportunity subject to STBL demand


_D_ . The speculator in such a market would choose to deposit collateral and issue


new STBL at time _t_ if _[DL]_ _L_ _[t]_ [2] _t_ _[−]_ [1] E[ _Rt_ +1 _|Ft_ ] _−_ _γ ≥_ 0, where _γ_ represents the repre

sentative speculator’s expected liability and liquidation cost after entering the


market. Arguably, _γ ∼_ 1 as, in an infinite depth market, the speculator can start


from a position of low leverage.


The speculator’s profitability (for the marginal STBL issue) will be 0, which


yields equality in the above condition, and therefore,



_Lt_ = 


_γDLt−_ 1 E[ _Rt_ +1 _|Ft_ ] _._



Notice the similarity with the upper bound in Proposition 2.4.


Further using that ( _Xt_ ) is a submartingale, in which case E[ _Rt_ +1 _|Ft_ ] _≥_ 1, we


find the STBL price is constrained to a small range of _Z_ 0 _≥_ _Zt ≥_ _γr_ 1 [. This re-]


sembles the perfectly elastic demand case. In this case speculators are able to


liquidate positions without influencing STBL price, while in the infinite depth


case because the speculator is always willing to issue new STBL to offset a liq

uidation.

#### 2.5.3 No stable region if ( Xt ) is not a submartingale


The mechanisms that make the idealized settings well-stabilized break down


when the ETH price process ( _Xt_ ) is not a submartingale. This stresses how frag

ile the stablecoin market is to negative expectations in the primary ETH market,


58


even under these idealized settings. In the unlimited speculator case, specula

tors no longer enter the market if expectations are negative, and so we don’t


achieve the supply bound developed above. Instead, we return to the main


setting of the paper, which can be interpreted as unstable under negative expec

tations as it leads to deleveraging effects. In the perfectly elastic demand setting,


the STBL supply goes to zero as the speculator chooses not to participate.

#### **2.6 Discussion**


This paper presents a new stochastic model of non-custodial over-collateralized


stablecoins, where the collateral has value exogenous to the stablecoin system


and the stablecoin has an endogenous market price. These stablecoins bear a re

semblance to a non-custodial form of the current monetary system of commer

cial bank money but give rise to new risks such as those experienced on Black


Thursday. These stablecoins stand in contrast to unbacked or endogenously


backed stablecoins, such as Terra UST, which are better understood using tools


- f insolvency and currency peg models, as well as custodial stablecoins such as


Tether, which can resemble the underlying structures of narrow banks or money


market funds.


In our model, we formally characterize domains that can be interpreted as


stable and unstable for the stablecoin. By bounding the probability of large


deviations and the quadratic variation of the price process, we prove that the


stablecoin behaves in a stable way when restricted to a certain region. In con

trast, price variance is shown to be distinctly greater in a separate region. This


is triggered by large deviations, collapsed expectations, and liquidity problems


59


from deleveraging. We also characterize a deflationary deleveraging spiral as


a submartingale, which can exacerbate liquidity problems in a crisis. These


deleveraging spirals resemble short squeezes, and are counterintuitive as they


lead to stablecoin price appreciation during times of shock, whereas we might


- therwise expect prices to depreciate given the riskier state of the system. Fur

ther, this appreciation is detrimental: it leads to faster collateral drawdown, and


potentially shortfalls, as more collateral is required to fulfill liquidations and is


accompanied by higher price variance.


An observation from the model is that the speculator chooses a collateral


level _above_ the required collateral factor. This is because the expected liquida

tion cost is greater than the $1 face value. The speculator will desire to increase


the collateralization during times when the expected liquidation cost is higher,


which can occur after a shock to collateral value or if the speculator expects the


collateral to be more volatile. This generally explains the high level of over

collateralization seen in Dai, which typically ranges 2 _._ 5 _−_ 5 _×_ although the col

lateral factor is 1 _._ 5 _×_ .


The presence of deleveraging effects poses fundamental trade-offs in decen

tralized design. One way to bring the stablecoin closer to the ‘perfect’ stability


cases is to increase elasticity of demand. This relies on the presence of good un

correlated alternatives to the stablecoin. As all non-custodial stablecoins likely


face similar deleveraging risks, greater elasticity relies on custodial stablecoins


- r greater exchangeability to fiat currencies. Another way to bring the stable

coin closer ‘perfect’ stability is to increase the supply of new speculators. As


there will not be unlimited supply of speculators with positive ETH expecta

tions (especially during an extended bear market), this relies on having another


60


uncorrelated collateral asset. As all decentralized assets are very correlated, this


again largely relies on including custodial collateral assets, like Maker’s recent


addition of USDC. [16] While these measures strengthen the stability results, it’s


at the expense of greater centralization and moves the system away from being


‘non-custodial’.


We suggest a way to improve the design of Dai’s savings pool toward damp

ing deleveraging effects without greater centralization through incentivizing ex

changeability of Dai during deleveraging events. In its current state, the Maker


system charges fees to speculators, part of which it passes on to Dai holders as


an interest rate if the holder locks the Dai into a savings pool. With modified


mechanics, this savings pool can provide a buffer to deleveraging effects. For


instance, if we allow Dai in the savings pool to be bought out at a reasonable


premium to face value by a speculator who uses it to deleverage, then delever

aging effects are bounded by the premium amount up to the size of the savings


buffer. The Dai holders who participate in this savings pool are then compen

sated for providing a repurchase option to the speculator. The Dai holder could


elect to have the repurchase fulfilled in the collateral asset, or something else,


like a custodial stablecoin. In this way, this mechanism can provide some of the


benefits of the ‘perfect’ stability settings while enabling Dai holders to choose


how decentralized they want to be. A Dai holder who does not require high


decentralization would elect to receive the compensation from the savings pool


whereas a Dai holder who requires higher decentralization would choose not to


16Recall that custodial assets face their own risks, however, which may not be uncorrelated
in extreme crises. Custodial stablecoins are subject to counterparty risk, systematic risks, bank
run risks, asset seizure risk, and effects from negative interest rates. The treasury secretary
J. Yellen referred to the materialization of these risks in her annual testimony in front of the
Senate Banking Committee, on May 10th 2022: “A stablecoin known as TerraUSD experienced
a run and declined in value,” Yellen said. “I think that this simply illustrates that this is a rapidly
growing product and there are rapidly growing risks.”


61


Figure 2.4: Effect of Liquity’s stability pool on LUSD price in Curve’s on-chain
market in the May 2021 crisis. Deleveraging effect is delayed and smoother
compared to Dai’s price effect on Black Thursday (cf. Figure 2.3b).


use the savings pool. Our model can be extended to consider such mechanisms.


Since the release of our paper, mechanisms resembling this, which try to


boost liquidity around liquidations to quell deleveraging spirals, have been


adopted by projects such as [124]. Empirically, these mechanisms have the effect


- f smoothing deleveraging effects over a longer time period, lowering the ef

fect of shocks but not entirely removing the short squeeze effect (see Figure 2.4).


Maker has chosen to go a different direction by maintaining direct exchangeabil

ity with the custodial USDC [136], which has allowed Dai to maintain a close


peg through subsequent crises at the expense of heavy reliance on custodial sta

blecoins. The stablecoin Rai has chosen a third path of instituting negative rates


- n stablecoin holders during crises [162] via a PID controller, which is effectively


charging stablecoin holders insurance premiums when demand for stablecoins


- utweights demand for leverage, thus lowering demand to help attain peg.


Our model and results can also apply more broadly to synthetic and cross

chain assets and over-collateralized lending protocols that allow borrowing of


illiquid and/or inelastic assets– whenever the mechanism is based on leveraged


positions and leads to an endogenous price of the created or borrowed asset. We


62


have characterized the risk that such structures feature intertwining of collateral


liquidation spirals and short squeezes of the created asset. Synthetic assets gen

erally use a similar mechanism just with a different target peg. Cross-chain as

sets that port an asset from a blockchain without smart contract capability (e.g.,


Bitcoin) to a blockchain with smart contracts (e.g., Ethereum) also tend to rely


- n a similar mechanism. In non-custodial constructions such as [190] and [177],


vault operators are required to lock ETH collateral in addition to the deliverable


BTC asset. They bear a leveraged ETH/BTC exchange rate risk and face similar


deleveraging risk. In particular, to reduce exposure, they need to repurchase the


version of the cross-chain asset on Ethereum.


Several generalizations of analytical results are left for future research. Here


we considered collateral prices exogenous, but it would be interesting to model


market impact effects of large collateral liquidations and also enable modeling


- f stablecoins like Synthetix sUSD that have _endogenous_ collateral (see [110]).


One possible way to endogenize collateral prices is via an inverse demand func

tion. We expect that the general methods used in this paper can be applied to


partial equilibrium settings such as this. Naturally, this would necessitate con

ditions on the inverse demand function that ensure that the expected returns as


a function of the issuance remains concave.


We have specified the speculator’s decision-making in terms of a sequence


- f one-period optimization problems. Alternatively, the speculator could strate

gically coordinate the sequence of decisions further into the future and develop


long-term strategies. This could be formulated by using an exit time for the


speculator, when they can cash our their position by selling to someone else at


par. If this terminal time is deterministic, the problem can be formulated as a


63


dynamic program, in which the terminal decision results from the one-period


- ptimization, intermediate decisions solve a Bellman equation conditioned on


the information revealed up to that point, and random returns are independent.


For instance, [33] sets up a supermodular game in a setting where agents exit at


a random exponential time. in t The model could be extended to include mul

tiple speculators. Speculators have in reality a finite depth and moreover, they


maintain positions with different leverage points and ETH expectations. This


can lead to a sequential schedule of liquidation points at a given time through

- ut the system, which will be reflected in a speculator’s expected liquidation


costs. A given speculator will take into account price effects from the potential


liquidations of other speculators’ positions in addition to their own, see [142]


for leveraging-deleveraging games in the traditional banking system. Here, the


speculator’s value depends on liquidation costs and on the supply limit im

posed by the finite market depth. Incorporating strategic aspects is left for fu

ture research.


**Acknowledgements** his paper is based on work supported by NSF CAREER


award #1653354 and the Bloomberg Fellowship. We thank Dominik Harz,


Georgios Konstantopoulos, the anonymous referees for valuable feedback that


helped improve the paper.


**Data availability statement** The contribution of this paper is theoretical.


Where examples have been provided to support theoretical findings, price data


is publicly available (by Kaiko - Digital Assets Data Provider and LoanScan


platform).


64


#### **2.7 Appendix: Proofs**

In the proofs, we often use the following elementary result


**Lemma 2.7.** _For α, D, L ≥_ 0 _,_



_αD_ + _L ≤_ _√_



_α_ [2] _D_ [2] + 4 _αDL_ + _L_ [2] _≤_ min 2 _αD_ + _L, αD_ + _L_ + _√_ 2 _αDL_ _._

          -          


_Proof._ Define _ε_ := _√_



_α_ [2] _D_ [2] + 4 _αDL_ + _L_ [2] . We have _ε ≤_ 2 _αD_ + _L_ as long as



_αD ≥_ _L_ ( _√_



_αD ≥_ _L_ ( _√_ 3 _−_ 2), which is true since _α, D, L ≥_ 0. Next, notice that _ε_ =


- ( _αD_ + _L_ ) [2] + 2 _αDL_ . Thus _ε > αD_ + _L_ since 2 _αDL ≥_ 0. Lastly, by concav


( _αD_ + _L_ ) [2] + 2 _αDL_ . Thus _ε > αD_ + _L_ since 2 _αDL ≥_ 0. Lastly, by concav


ity, _ε ≤_ _αD_ + _L_ + _√_


**Proposition 2.1**



2 _αDL_ .



_Proof._ Consider _Xt_ +1 = _XtRt_ +1. For notational simplicity, drop subscripts as


follows: _N_ [¯] _t �→_ _N_, _Xt �→_ _X_, _Lt �→L_, ∆= _Lt −Lt−_ 1, _c_ ( _Lt_ ) _�→_ _c_, _b_ ( _Lt_ ) _�→_ _b_, _gt �→_ _g_,


_Rt_ +1 _�→_ _R_ . Define _ψ_ := E[ _Yt_ +1 _|Ft_ ]. Then




_[· D]_ _∞_

E[ _R|Ft_ ] +
_L_ 


_ψ_ ( _L_ ) = [∆] _[· D]_



( _NXz −L_ ) _g_ ( _z_ ) _dz_
_c/X_



_b/X_

+

 - _c/X_



_αDL_
3 _L −_ _g_ ( _z_ ) _dz._

- 2 _NXz −L_ _[−]_ [2] _[NXz]_ 


_αDL_
Recall that the integrand factor - 3 _L −_ 2 _NXz−L_ _[−]_ [2] _[NXz]_ - evaluated at _Xz_ = _c_


is _L −_ _Nc_ (the liquidation zeros out the speculator’s collateral position), and


evaluated at _Xz_ = _b_ is 0 (on the threshold of liquidation).


65


We obtain



_∂ψ_
_∂L_ [=] _[ DL]_ _L_ _[t]_ [2] _[−]_ [1]



_g_ ( _z_ ) _dz_

_c_

_X_




_[t][−]_ [1] E[ _R|Ft_ ] _−_ _NX_ _[c]_

_L_ [2] - _X_




_[c]_ _g_ _c_

_X_ _[−L]_ - - _X_



_X_




- _∂∂c_



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
2 _−_

- 2( _Nc −L_ ) [2]



_b_

_X_

_−_

- - _Xc_



_b_

_X_

_−_

- - _c_



_αDNXz_
( _NXz −L_ ) [3] _[g]_ [(] _[z]_ [)] _[dz.]_



_c_

_−_ _g_

  - _X_




- _∂L∂c_ _X_ 1



Notice that _[∂b]_



_∂L_ _[>]_ [ 0][,] _[ g][ ≥]_ [0][, and]




_[∂b]_ _[∂c]_

_∂L_ _[>]_ [ 0][,] _∂L_



_αDNb_ _αDβL_
3 _−_ [= 3] _[ −]_ [= 3] _[ −]_ [3] _[α][D]_ _<_ 0
2( _Nb −L_ ) [2] 2( _L_ ( _β −_ 1)) [2] _L_



by assumption that liquidation repurchase price always _≥_ 1. Additionally, the


remaining integral is always positive as the integrand is positive between the


limits and _g ≥_ 0. Finally, E[ _R|Ft_ ] _≥_ 0 since ( _Xt_ ) is a submartingale. Thus under


the given conditions, _∂_ _[∂]_ _L_ [2] _[ψ]_ [2] _[≤]_ [0][ as all terms are] _[ ≤]_ [0][.]


Further supposing that either E[ _R|Ft_ ] _>_ 0 or P _c_ ( _L_ ) _< XR < b_ ( _L_ ) =

                    -                    
- _c/Xb/X_ _[g]_ [(] _[z]_ [)] _[dz >]_ [ 0][, then] _∂_ _[∂]_ _L_ [2] _[ψ]_ [2] _[<]_ [ 0][.]



Notice that the [1]




[1] [3]

2 [in the bound is related to the choice] _[ β]_ [ =] 2



2 [.]



**Proposition 2.2**



66


_Proof._ Easily verifiable by substitution, noting that factors of _γ_ cancel in the in

tegral limits.


**Proposition 2.3**


_Proof._ The speculator can at most buy back using all its ETH. At time _t_, this


amount is the solution ∆ _t_ to the following


∆ _tD_
+ _Nt−_ 1 _Xt −_ _Lt−_ 1 _−_ ∆ _t_ = 0 _,_
_Lt−_ 1 + ∆ _t_


supposing there is no liquidation at time _t_ . It is straightforward to verify the


solution, giving the lower bound:



∆ _t ≥_ [1]

2




_−_ _D_ [2] _−_ 4 _DLt−_ 1 + 2 _DNt−_ 1 _Xt_ + _Nt_ [2] _−_ 1 _[X]_ _t_ [2] [+] _[ D −]_ [2] _[L][t][−]_ [1] [+] _[ N][t][−]_ [1] _[X][t]_ _._

- ~~�~~ 


Note that if the speculator is not solvable at time _t_, then there is no real solution.


**Proposition 2.4**


_Proof._ As above, consider _Xt_ +1 = _XtRt_ +1. For notational simplicity, we drop


subscripts as follows: _N_ [¯] _t �→_ _N_, _Xt �→_ _X_, _Lt �→L_, ∆= _Lt −Lt−_ 1, _c_ ( _Lt_ ) _�→_ _c_,


_b_ ( _Lt_ ) _�→_ _b_, _gt �→_ _g_, _Rt_ +1 _�→_ _R_, P( _At|Ft_ ) _�→_ P( _A_ ), P( _Bt|Ft_ ) _�→_ P( _B_ ).


67


Suppose the first condition is true. We have



_g_ ( _z_ ) _dz_




_∂ψ_
_∂L_ [=] _[ DL]_ _L_ _[t]_ [2] _[−]_ [1]



_b_

_∞_ _X_

_g_ ( _z_ ) _dz_ +
_c_ - _c_
_X_ _X_



_∞_

_[t][−]_ [1] E[ _R|Ft_ ] _−_

_L_ [2] - _c_



_c_

_X_



_αDNXz_
3 _−_

- 2( _NXz −L_ ) [2]



_≤_ _[DL][t][−]_ [1] E[ _R|Ft_ ] _−_ P( _A ∪_ _B_ )

_L_ [2]



_≤_ _[DL][t][−]_ [1] E[ _R|Ft_ ] _−_ _κ_ _[−]_ [1] _._

_L_ [2]



Notice this is monotonic decreasing in _L_ - ver the domain, so the critical point


will be a bound for the optimal value of _L_ _[∗]_ . Setting equal to 0, we have



_L_ _[∗]_ _≤_ 


_κDLt−_ 1 E[ _R|Ft_ ] _._



Now suppose the second condition is true instead. We have



_c_

_X_



_∂ψ_
_∂L_ [=] _[ DL]_ _L_ _[t]_ [2] _[−]_ [1]



_b_

_∞_ _X_

_g_ ( _z_ ) _dz_ + 2
_b_ - _c_
_X_ _X_



_∞_

_[t][−]_ [1] E[ _R|Ft_ ] _−_

_L_ [2] - _b_



_b_ _b_

_X_ _X_

_g_ ( _z_ ) _dz −_
_c_ - _c_
_X_ _X_



_αDNXz_
2( _NXz −L_ ) [2] _[g]_ [(] _[z]_ [)] _[dz]_



_≤_ _[DL][t][−]_ [1] E[ _R|Ft_ ] _−_ P( _A_ ) _−_ 2 P( _B_ )

_L_ [2]  -  


_≤_ _[DL][t][−]_ [1] E[ _R|Ft_ ] _−_ _κ_ _[−]_ [1] _._

_L_ [2]



which delivers the desired result as above.


**Proposition 2.5**


_Proof._ By assuming _TZ_ 0 _> τ_, we have _Z_ 0 _≥_ _Zt∧τ_ . Applying Proposition 2.4 to



_Zt_ = _LDt_ [provides] _[ Z][t][∧][τ][ ≥]_ ~~�~~



_D_
_κLt∧τ_ _−_ 1 _r_ [. Notice that the upper bound on] _[ L][t]_ [ and]



the lower bound on _Zt_ can be written respectively as increasing and decreasing


sequences in _t_ starting from initial state as follows:



2 _[t]_ _−_ 1
_Lt_ = ( _κDr_ ) 2 ~~_[t]_~~



1
2 ~~_[t]_~~
0 _[.]_



2 ~~_[t]_~~ _L_



68


_D_
_Z_ ~~_t_~~ = _[t]_



2 _[t]_ _−_ 1
( _κDr_ ) 2 ~~_[t]_~~



1 _._
2 ~~_[t]_~~
0



2 ~~_[t]_~~ _L_



1
These have limits _L∞_ = _κDr_ and _Z_ ~~_∞_~~ = _κr_ [that also bound] _[ L][t]_ [ and] _[ Z][t]_ [ respec-]


tively.


**Proposition 2.6**


_Proof._ For _t −_ 1 _< τ_,



_D_ _D_

_|Ft−_ 1

E[ _Lt|Ft−_ 1] _[≤]_ [E] - _Lt_



_D_
_≤_

- _Lt−_ 1



by Jensen’s inequality and the condition for _τ > t −_ 1. Thus we have


E[ _Lt∧τ_ _|Ft−_ 1] _≥Lt∧τ_ _−_ 1


and ( _Lt∧τ_ ) is a submartingale. ( _Zt∧τ_ ) is a supermartingale by condition of _τ_ .


Applying Proposition 2.5, _Lt∧τ_ is bounded above and _Zt∧τ_ is bounded below.


Thus they converge almost surely by Doob’s martingale convergence theorem.


**Proposition 2.7**


_Proof._ The first inequality follows from Proposition 2.5 and supermartingale


properties.


69


Since _Zt∧τ_ is supermartingale, we have _Zt−_ 1 _≥_ E[ _Zt|Ft−_ 1]. Assume


(E[ _Rt_ +1 _|Ft_ ]) is non-decreasing for _t < τ_ . Then subject to the stopping time _τ_,







E[ _Zt|Ft−_ 1] _≥_ E




- ~~�~~



_D_
_κLt−_ 1 E[ _Rt_ +1 _|Ft_ ] _[|F][t][−]_ [1]



(Apply Proposition 2.4)



_≥_


=


_≥_




~~�~~

~~�~~ _D_

- (Jensen’s inequality)

_κLt−_ 1 E E[ _Rt_ +1 _|Ft_ ] _|Ft−_ 1

- ~~�~~ ~~�~~



_D_
(Tower property)
_κLt−_ 1 E[ _Rt_ +1 _|Ft−_ 1]

~~�~~


_D_

_κLt−_ 1 E[ _Rt|Ft−_ 1]

~~�~~



since E[ _Rt_ +1 _|Ft_ ] _≥_ E[ _Rt|Ft−_ 1].


**Lemma 2.1**


_Proof._ For _t −_ 1 _< τ ∧_ _Tm_,


E [ _|m −_ _Zt||Ft−_ 1] _≥|_ E[ _m −_ _Zt|Ft−_ 1] _|_


_≥|m −_ _Zt−_ 1 _|,_


by Jensen’s inequality and the condition for _t −_ 1 _< Tm_ that _m −_ _Zt−_ 1 _≥_ 0. Thus

_Z_ _[′]_

- _t∧τ_ _∧Tm_ - is a non-negative submartingale.


**Proposition 2.8**


_Proof._ Note for _t < τ ∧_ _Tm_, have _Zt_ _[∗]_ _[≤]_ _[m]_ [, and so] _[ Z]_ _τ_ _[′∗]_ _∧Tm−_ 1 _[≤]_ _[m][ −]_ _κr_ 1 [. Thus]


_Zτ_ _[′∗]_ _∧Tm_ _[≤]_ [max] _m −_ _κr_ [1] _[, Z]_ _τ_ _[′]_ _∧Tm_ .

     -      

70


Consider time _t_ = _τ ∧_ _Tm_ and note that optional stopping applies since _Z_ is


bounded. Denote _W_ := _m −_ _Zt_, _E_ := E[ _−W_ _|Zt > m_ ], and _p_ := P( _Zt ≤_ _m_ ). From


- ptional stopping, we recall that _m ≥_ E[ _Zt_ ] _≥_ _κr_ 1 [, and so][ 0] _[ ≤]_ [E][[] _[W]_ []] _[ ≤]_ _[m][ −]_ _κr_ 1 [.]


Then

E[ _W_ ] = E[ _W_ 1 _Zt≤m_ ] _−_ E[ _−W_ 1 _Zt>m_ ]



_≤_ _p_ _m −_ [1]

_κr_

 



_−_ (1 _−_ _p_ ) _E._




Combining with 0 _≤_ E[ _W_ ], we have 0 _≤_ _p_ ( _m −_ _κr_ [1] [)] _[ −]_ [(1] _[ −]_ _[p]_ [)] _[E]_ [, which gives]



_E_
_p ≥_
_m −_ _κr_ [1] [+] _[ E]_ _[.]_



Then noting that (1 _−_ _p_ ) _E ≤_ _E_ (1 _−_ _m−_ _κrE_ [1] [+] _[E]_ [)][,] _[ p][ ≤]_ [1][, and][ E][[] _[Z]_ _t_ _[′]_ [] =][ E][[] _[W]_ [ 1] _[Z]_ _t_ _[≤][m]_ []+]



E[ _−W_ 1 _Zt>m_ ], we have


E[ _Zt_ _[′∗]_ []] _[ ≤]_ _[p]_ [ E][[] _[Z]_ _t_ _[′∗]_ _−_ 1 [] + (1] _[ −]_ _[p]_ [)] _[E]_



_E_

[1] 1 _−_

_κr_ [+] _[ E]_ - _m −_ [1]



_≤_ _m −_ [1]



_κr_ [+] _[ E]_








[1] _[E]_ [(] _[m][ −]_ [1]

_κr_ [+] _m −_ [1] [+]



= _m −_ [1]




_[E]_ [(] _[m][ −]_ _κr_ [1] [)]

_m −_ [1] [+] _[ E]_



_κr_ [1] [+] _[ E]_ _[.]_



Notice further that given either of the following conditions


 - _κr_ 1 _[> m]_ [ and] _[ E >]_ _κr_ 1 _[−]_ _[m]_


 - _κr_ 1 [=] _[ m]_ [ and] _[ E >]_ [ 0]


 - _κr_ 1 _[< m]_ [ ad] _[ E][ ≥]_ [0][,]


then



0 _≤_ (1 _−_ _p_ ) _E ≤_ _[E]_ [(] _[m][ −]_ [1]

[1]



_κr_ _[.]_




_[E]_ [(] _[m][ −]_ _κr_ [1] [)]

_m −_ [1] [+] _[ E]_




_[ −]_

_κr_ [)]

[1] _[≤]_ _[m][ −]_ _κr_ [1]

_κr_ [+] _[ E]_



Thus, recalling we used _t_ = _τ ∧_ _Tm_, we get the following result



E[ _Zτ_ _[′∗]_ _∧Tm_ []] _[ ≤]_ [2] _m −_ [1] _._

_κr_

    -     

71


**Theorem 2.2**


_Proof._ Given Lemma 2.1 and Proposition 2.8 and noting E[ _Zτ_ _[′]_ _∧Tm_ []] _[ ≤]_ [E][[] _[Z]_ _τ_ _[′∗]_ _∧Tm_ []][,]


apply Doob’s maximal inequality.


**Theorem 2.3**


_Proof._ Apply Theorem 3.1 in [45], noting that sup _n_ E[ _Zn_ _[′]_ _∧τ_ _∧Tm_ []] _[ ≤]_ [E][[] _[Z]_ _τ_ _[′∗]_ _∧Tm_ []][ by]


Jensen’s inequality.


**Theorem 2.4**


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



by Jensen’s inequality and the _S_ 1 condition E[ _Lt|Ft−_ 1] _≤Lt−_ 1. Thus ( _ZS_ 1 _∨t∧S_ 2)


is a submartingale (though note that it can be a submartingale for more general


stopping times than this).


_L_ started at _S_ 1 and stopped _S_ 2 is a supermartingale (by definition).


72


**Theorem 2.5**


_Proof._ As above, consider _Xt_ +1 = _XtRt_ +1. For notational simplicity, we drop


subscripts as follows: _N_ [¯] _t �→_ _N_, _Xt−_ 1 _�→_ _X_ (notice this is different from previous


usage), _Lt �→L_, ∆= _Lt −Lt−_ 1, _c_ ( _Lt_ ) _�→_ _c_, _b_ ( _Lt_ ) _�→_ _b_, and _gt �→_ _g_ .


Let _ρ_ be (deterministic) variable representing the outcome of _Rt_, such that


now we have the outcome _Xt_ = _Xρ_ . And define _h_ ( _ρ_ ) = arg max _L ψ_ ( _ρ, L_ ) =


E[ _Yt_ +1 _|Ft_ ]. By first order condition, _∂L∂_ _[ψ]_ [(] _[ρ, h]_ [(] _[ρ]_ [)) = 0][. The assumptions on] _[ ψ]_


provide unique maximum and fulfill conditions of the implicit function theo


rem, which gives us _[∂h]_ _∂ρ_ [(] _[ρ]_ [)][ exists and]


_∂h_
_∂ρ_ [(] _[ρ]_ [) =] _[ −]_



_∂_ [2]
_∂ρ∂L_ _[ψ]_ [(] _[ρ, h]_ [(] _[ρ]_ [))]

_∂_ [2] _[.]_
_∂L_ [2] _[ψ]_ [(] _[ρ, h]_ [(] _[ρ]_ [))]



Calculating derivatives using the Leibniz integral rule (recalling _c, b_ are func

tions of _L_ ),



_∂_ [2] _ψ_ _c_ _c_
_∂ρ∂L_ [=] _[ g]_ - _Xρ_ - _Xρ_ [2]



_αDNc_
4 _−_

- 2( _Nc −L_ ) [2]



_b_

_−_ _g_

- - _Xρ_



_b_

_−_ _g_

- 


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



_∂_ [2] _ψ_

[=] _[ −]_ [2] _[DL][t][−]_ [1][ E][[] _[R][t]_ [+1][]]
_∂L_ [2] _L_ [3]



_Xρ_



_αDNb_
3 _−_

- 2( _Nb −L_ ) [2]








[1][ E][[] _[R][t]_ [+1][]] _b_

+ _g_
_L_ [3] 


_∂b_ 1

- _∂L_ _Xρ_



_αDNc_
2 _−_

- 2( _Nc −L_ ) [2]



_b_
_Xρ_

_−_

- - _c_

_Xρ_



_c_

_−_ _g_

 - _Xρ_



_∂c_ 1

- _∂L_ _Xρ_



_αDNXρz_
( _NXρz −L_ ) [3] _[g]_ [(] _[z]_ [)] _[dz.]_



Notice that (and continuing with _β_ = 3 _/_ 2)


_αDNb_ _αDβL_
3 _−_ [= 3] _[ −]_ [= 3] _[ −]_ [3] _[α][D]_ _<_ 0 _,_
2( _Nb −L_ ) [2] 2( _L_ ( _β −_ 1)) [2] _L_


73


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
4 _−_
2( _Nc −L_ ) [2] _[>]_ [ 2] _[ −]_ 2( _Nc −L_ ) [2] _[≥]_ [0] _[.]_


Note that all terms of _∂ρ∂L∂_ [2] _ψ_ [are non-negative and all terms of] _[ ∂]_ _∂L_ [2] _[ψ]_ [2] [are non-]

positive. Given _ρ ≥_ _b/X_, we have _g_ - _Xρc_ - and _g_ - _Xρb_ - are increasing in 1 _/ρ_ .



Note also that _[∂b]_




_[∂c]_ [E][[] _[R][t]_ [+][1][]]

_∂L_ [, and][ 2] _[DL][t][−]_ _L_ [1] [3]




_[∂b]_ _[∂c]_

_∂L_ [,] _∂L_



_L_ [1] [3] _[t]_ [+][1] are constant in _ρ_ . Lastly, the numerator



and denominator integrals can be rewritten respectively as



_αDNz_ _z_
( _Nz −L_ ) [3] _[g]_ - _Xρ_



_Nz_ ( _Nz_ + _L_ ) _z_

_g_
2( _Nz −L_ ) [3] 


_dz_




1

_ρ_




- _c_ _b_



_αDNz_ ( _Nz_ + _L_ )



_Xρ_



_b_
_dz_ and

- - _c_



and _[α][D]_ 2( _[Nz]_ _Nz_ [(] _−L_ _[Nz]_ [+] ) [3] _[L]_ [)] _≥_ ( _NzαD−LNz_ ) [3] [given] _[ Nz]_ [ +] _[ L ≥]_ _[Nc]_ [ +] _[ L][ >]_ [ 2][, for which] _[ L][ >]_ [ 8][ is]


sufficient. And so the terms in the numerator of _|h_ _[′]_ ( _ρ_ ) _|_ are growing by a factor


1 _/ρ_ faster than the terms in the denominator as _ρ_ decreases, proving (2).


Next, note that under the condition 0 _< ρ <_ 1,



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




_[dc]_ 1

_[≥]_ _[dc]_
_dL_ _Xρ_ [2] _dL_




_[dc]_ 1

_dL_ _Xρ_ _[.]_



_dL_ _[dc]_ _[≤]_ 2(2 _ααDD_ ++ _LL_ ) [+ 1] _[ <]_ [ 2][, and so] _[ c >]_ _dL_ _[dc]_



The last relation uses the fact that _[dc]_



_dL_ [under the]



problem setup.



74


Next note that for _ρ ≤_ _[L]_ 8 [and] _[ c][ ≤]_ _[Xρz][ ≤]_ _[b]_ [, we have]


_αDNXz_ ( _NXρz_ + _L_ ) _αDNXρz_

_≥_
2( _NXρz −L_ ) [3] ( _NXρz −L_ ) [3] _[.]_


This is because the expression (1) simplifies to _NXρz_ + _L ≥_ 2 _ρ_, (2) to be true


- ver the whole range of _z_, we need _Nc_ + _L ≥_ 2 _ρ_, and (3) _ρ ≤_ _[L]_ 8 [is sufficient for]



this. Thus

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
( _NXρz −L_ ) [3] _[g]_ [(] _[z]_ [)] _[dz]_



_αDNXz_ ( _NXρz_ + _L_ )



under these conditions.


Then note that all terms in the numerator of _h_ _[′]_ ( _ρ_ ) are greater than and grow


faster in 1 _/ρ_ than the comparable terms in the denominator. This leaves the first


term in the numerator, which is constant in _ρ_ . To get (3), then note that _ε_ can be


chosen such that for _ρ_ = _ε_, the numerator and denominator are equal.


We can derive the results for _∂n_ _[∂h]_ [in essentially the same way. Alter the above]


dropping of subscripts with _Xt �→_ _X_, let _n_ be a variable representing the re

alization of _N_ [¯] _t_, and consider _h_ as a function of _n_ . Note the following relevant


derivatives.



_∂b_
_∂n_ [=] _[ −][β]_ _n_ _[L]_ [2]




_[L]_

[=] _[ −]_ _[b]_
_n_ [2] _n_



_n_



_∂c_
_∂n_ [=] _[ −]_ 2 _n_ [1] [2]




- _√_



_α_ [2] _D_ [2] + 4 _αDL_ + _L_ [2] _−_ _αD_ + _L_ = _−_ _[c]_

           - _n_



_∂n∂L∂_ [2] _ψ_ [=] _[ g]_ - _Xc_



_b_


_n_




_b_


_n_




_αDnb_
3 _−_

- 2( _nb −L_ ) [2]








- _nc_



_αDnc_
2 _−_

- 2( _nc −L_ ) [2]



_b_

_−_ _g_

_X_

- 


_b_

_−_ _g_

_X_

- 


_b_

_X_
+

 - _c_

_X_



_αDnXz_ ( _nXz_ + _L_ )

_g_ ( _z_ ) _dz._
2( _nXz −L_ ) [3]


75


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
( _nXz −L_ ) [3] _[g]_ [(] _[z]_ [)] _[dz.]_



_c_

_−_ _g_

  - _X_




- _∂L∂c_ _X_ 1



And by applying implicit function theorem, we get



_∂h_
_∂n_ [(] _[n]_ [) =] _[ −]_



_∂_ [2]
_∂n∂L_ _[ψ]_ [(] _[n, h]_ [(] _[n]_ [))]

_∂_ [2] _[.]_
_∂L_ [2] _[ψ]_ [(] _[n, h]_ [(] _[n]_ [))]



From here we can proceed with the same analysis using factors of _n_ [1] [instead of]


1
_ρ_ [.]


**Theorem 2.6**


_Proof._ For notational simplicity, drop subscripts _Xt �→_ _X_, _N_ [¯] _t−_ 1 _�→_ _N_, _Lt−_ 1 _�→L_ .


And consider _x_ a realization of _X_ as variable in _h_ . Define the function _f_ ( _X, n_ ) =


_h_ ( _X,n_ 1 ) [where] _[ n]_ [ represents the realization of] _[ N]_ [. With probability 1, the following]


are true:


 - _h_ is concave in _x_ and _n_ because _h_ _[′]_ is decreasing, as shown in the previous


result.


 - _f_ is differentiable (wrt _n_ and _x_ ) over domain using chain rule and implicit


function theorem.


 - _f_ is convex: it’s the composition of 1 _/x_ and _h_, and since 1 _/x_ is convex and


non-increasing and _h_ is concave, so is _f_ (see [40] 3.2.4).


 - _f_ is (strictly) decreasing (in _n_ and _x_ ) since _h_ is increasing.


76


- By assumption, we’ve restricted _NX_ . The derivative of _f_ at the minimum


value exists and is bounded.


- _f_ is non-negative since _h_ is non-negative.


- _∂n∂f_ [is (strictly) increasing in] _[ n]_ [. We have]


1
_f_ _[′]_ ( _x, n_ ) = _−_
_h_ ( _x, n_ ) [2] _[h][′]_ [(] _[x, n]_ [)] _[,]_


where _h_ _[′]_ ( _x, n_ ) is derived in the previous proof using the implicit function


theorem. _h_ is increasing in _n_ and _h_ _[′]_ is non-negative and decreasing in _n_ .



_h_ _[h]_ [2] _[′]_ [is decreasing in] _[ n]_ [, and so] _[ −]_ _h_ _[h][′]_



Thus _[h][′]_



_h_ [2] [is increasing.]




 - _∂n∂h_ [is increasing in] _[ x]_ [. This can be seen using the formulation at the end]

   - f the proof for the previous result as terms in _[∂]_ _∂L_ [2] _[ψ]_ [2] [grow slower in] _[ x]_ [ (in]

magnitude) than terms in _∂n∂L∂_ [2] _ψ_ [. In particular, the first term of] _[ ∂]_ _∂L_ [2] _[ψ]_ [2] [is de-]


_L_ _x_ _∂_ [2] _ψ_
creasing in magnitude since is increasing in . And the integral in _∂n∂L_

increases faster in _x_ than the integral in _[∂]_ _∂L_ [2] _[ψ]_ [2] [, as can be seen by comparing]

the integrand numerators (a factor of _x_ [2] in _∂n∂L∂_ [2] _ψ_ [vs. a factor of] _[ x]_ [ in] _[ ∂]_ _∂L_ [2] _[ψ]_ [2] [).]


 - _∂n∂f_ [is (strictly) increasing in] _[ x]_ [ This is because] _[ h]_ [ is increasing in] _[ x]_ [ and] _∂n_ _[∂h]_ [is]


_x_
non-negative and increasing in (previous bullet).


Note additionally that, from the system setup assumptions, all of the func

tions are appropriately bounded.


Thus we can apply Theorem 3.1 in [173] to get


Var _f_ ( _X, N_ _[s]_ ) _|Ft−_ 1 _<_ Var _f_ ( _X, N_ _[u]_ ) _|Ft−_ 1 _._

        -         -         -         

Note that the variances exist because _h_ = _Lt_ is bounded, as shown in previous


results. The variances of _Zt_ _[s]_ [and] _[ Z]_ _t_ _[u]_ [are then obtained by multiplying the above]


_D_ [2] .
inequality by


77


CHAPTER 3


**(IN)STABILITY FOR THE BLOCKCHAIN: DELEVERAGING SPIRALS**


**AND STABLECOIN ATTACKS**


The content of this chapter has previously appeared in:


“(In)Stability for the Blockchain: Deleveraging Spirals and Stable

coin Attacks.” Ariah Klages-Mundt and Andreea Minca. _**Cryptoeco-**_


_**nomic Systems**_, 1(2), 2021.


78


We develop a model of stable assets, including non-custodial stablecoins


backed by cryptocurrencies. Such stablecoins are popular methods for boot

strapping price stability within public blockchain settings. We derive funda

mental results about dynamics and liquidity in stablecoin markets, demonstrate


that these markets face deleveraging feedback effects that cause illiquidity dur

ing crises and exacerbate collateral drawdown, and characterize stable dynam

ics of the system under particular conditions. The possibility of such ‘delever

aging spirals’ was first predicted in the initial release of our paper in 2019 and


later directly observed during the ‘Black Thursday’ crisis in Dai in 2020. From


these insights, we suggest design improvements that aim to improve long-term


stability. We also introduce new attacks that exploit arbitrage-like opportunities


around stablecoin liquidations. Using our model, we demonstrate that these


can be profitable. These attacks may induce volatility in the ‘stable’ asset and


cause perverse incentives for miners, posing risks to blockchain consensus. A


variant of such attacks also later occurred during Black Thursday, taking the


form of mempool manipulation to clear Dai liquidation auctions at near zero


prices, costing $8m.

#### **3.1 Introduction**


In 2009, Bitcoin [150] introduced a new notion of decentralized cryptocurrency


and trustless transaction processing. This is facilitated by blockchain, which in

troduced a new way for mistrusting agents to cooperate without trusted third


parties. This was followed by Ethereum [186], which introduced generalized


scripting functionality, allowing ‘smart contracts’ that execute algorithmically


in a verifiable and somewhat trustless manner. Cryptocurrencies promise no

79


tions of cryptographic security, privacy, incentive alignment, digital usability,


and open accessibility while removing most facets of counterparty risk. How

ever, as these cryptocurrencies are, by their nature, unbacked by governments


- r physical assets, and the technology is quite new and developing, their prices


are subject to wild volatility, which affects their usability.


A stablecoin is a cryptocurrency with an economic structure built on top of


blockchain that aims to stabilize the purchasing power of the coin. A true stable

coin, often referred to as the “Holy Grail of crypto”, would offer the benefits of


cryptocurrencies without the unusable volatility and remains elusive. A more


tangible goal is to design a stablecoin that maximizes the probability of remain

ing stable long-term. If one can establish guarantees for the stability of such a


stablecoin, this would be a significant step toward forming a robust decentral

ized financial system and facilitating economic adoption of cryptocurrencies.


**Cryptocurrency volatility.** Cryptocurrencies face difficult technological, us

ability, and regulatory challenges to be successful long-term. Many cryptocur

rency systems develop different approaches to solving these problems. Even


assuming the space is long-term successful, there is large uncertainty about the


long-term value of individual systems.


The value of these systems depends on network effects: value changes in


a nonlinear way as new participants join. In concrete terms, the more peo

ple who use the system, the more likely it can be used to fulfill a given real


world transaction. The success of a cryptocurrency relies on a mass of agents–


e.g., consumers, businesses, and/or financial institutions–adopting the system


for economic transactions and value storage. Which systems will achieve this


80


adoption is highly uncertainty, and so current cryptocurrency positions are very


speculative bets on new technology. Further, cryptocurrency markets face lim

ited liquidity and market manipulation. In addition, the decentralized control


and privacy features of cryptocurrencies can be at odds with desires of govern

ments, which introduces further uncertainty around attempted interventions in


the space.


These uncertainties drive price volatility, which feeds back into fundamen

tal usability problems. It makes cryptocurrencies unusable as short-term stores


- f value and means of payment, which increases the barriers to adoption. In

deed, today we see that most cryptocurrency transactions represent speculative


investment as opposed to typical economic activity.


**Stablecoins.** Stablecoins aim to bootstrap price stability into cryptocurrencies


as a stop-gap measure for adoption. Current projects take one of two forms:


 - **Custodial stablecoins** rely on trusted institutions to hold reserve assets


   - ff-chain (e.g., $1 per coin). This introduces counterparty risk that cryp

tocurrencies otherwise solve.


 - **Non-custodial (or decentralized) stablecoins** create on-chain risk transfer


markets via complex systems of algorithmic financial contracts backed by


volatile cryptoassets.


We focus on non-custodial stablecoins and, more generally, the stable asset


and risk transfer markets that they represent. Non-custodial systems are not


well understood whereas custodial stablecoins can be interpreted using existing


well-developed financial literature. Further, non-custodial stablecoins operate


81


in the public/permissionless blockchain setting, in which any agent can partic

ipate. In this setting, malicious agents can participate in stablecoin systems. As


we will see, this can introduce new economic attacks.

#### **3.1.1 Non-custodial (decentralized) stablecoins**


The non-custodial stablecoins that we consider create systems of contracts on

chain with the following features encoded in the protocol. We refer to these as


**DStablecoins** .


  - Risk is transferred from stablecoin holders to speculators. Stablecoin hold

ers receive a form of price insurance whereas speculators expect a risky


return from a leveraged position. [1]


  - Collateral is held in the form of cryptoassets, which backs the stable and


risky positions.


  - An oracle provides pricing information from off-chain markets.


  - A dynamic deleveraging process balances positions if collateral value de

viates too much.


  - Agents can change their positions through some pre-defined process.


These systems are non-custodial (or decentralized) because the contract execu

tion and collateral are all completely on-chain; thus they potentially inherit all


- f the benefits of cryptocurrencies, such as minimization of counterparty risk.


DStablecoins are variants on contracts for difference, which we describe next.


The risk transfer typically works by setting up a tranche structure in which


1
‘Leverage’ means that the speculator holds _>_ 1 _×_ their initial assets but faces new liabilities.


82


losses (or gains) are borne by the speculators and the stablecoin holder holds


an instrument like senior debt. [2] There are also other _non-collateralized_ (or _algo-_


_rithmic_ ) stablecoins–for a discussion of these, see [35]. We don’t consider these


directly in this paper; however, we discuss in Section 3.7 how our model can


accommodate these systems as well.


**Contract for difference.** Two parties enter an overcollateralized contract, in


which the speculator pays the buyer the difference (possibly negative) between


the current value of a risky asset and its value at contract termination. [3] For


example, a buyer might enter 1 Ether into the contract and a speculator might


enter 1 Ether as collateral. At termination, the contract Ether is used to pay the


buyer the original dollar value of the 1 Ether at the time of entry. Any excess


goes to the speculator. If the contract approaches undercollateralization (if Ether


price plummets), the buyer can trigger early settlement or the speculator can


add more collateral.


**Variants on contracts for difference.** DStablecoins differ from basic contracts


for difference in that (1) the contracts are multi-period and agents can change


their positions over time, (2) the positions are dynamically deleveraged accord

ing to the protocol, and (3) settlement times are random and dependent on the


protocol and agent decisions. The typical mechanics of these contracts are as


follows:


  - Speculators lock cryptoassets in a smart contract, after which they can cre

2Intuitively, these are like collateralized debt obligations (CDOs) with the important addition

- f dynamic deleveraging according to the rules of the protocol. As we will see, it is critical to
understand deleveraging spirals as they affect the senior tranches.
3Intuitively, this is similar to a forward contract except that the price is only fixed in fiat terms
while payout is in the units of the underlying collateral.


83


ate new stablecoins as liabilities against their collateral up to a threshold.


These stablecoins are sold to stablecoin holders for additional cryptoas

sets, thus leveraging their positions.


  - At any time, if the collateralization threshold is surpassed, the system


attempts to liquidate the speculator’s collateral to repurchase stable

coins/reduce leverage.


  - The stablecoin price target is provided by an oracle. The target is main

tained by a dynamic coin supply based on an ‘arbitrage’ idea. Notably,


this is not true arbitrage as it is based on assumptions about the future


value of the collateral.


**–**
If price is above target, speculators have increased incentive to create


new coins and sell them at the ‘premium price’.


**–**
If price is below target, speculators have increased incentive to repur

chase coins (reducing supply) to decrease leverage ‘at a discount’.


  - Stablecoins are redeemable for collateral through some process. This can


take the form of global settlement, in which stakeholders can vote to liq

uidate the entire system, or direct redemption for individual coins. Settle

ment can take 24 hours-1 week.


  - Additionally, the system may be able to sell new ownership/decision

making shares as a last attempt to recapitalize a failing system – e.g., the


[role of MKR in Dai (see [131]).](https://makerdao.com/dai)


**DStablecoin risks.** DStablecoins face two substantial risks:


1. Risk of market collapse,


84


2. Oracle/governance manipulation.


Our model in this paper focuses on market collapse risk. We further remark on


- racle/governance manipulation in Section 3.7.


**Existing DStablecoins.** At the time of initial writing in 2019, major non

custodial stablecoins included Dai, BitShares Market Pegged Assets (like bi

tUSD), and Steem Dollars. In the latter, Steem market cap is essentially col

lateral; Steem Dollars can be redeemed for $1 worth of newly minted Steem,


and so redemptions affect all Steem hodlers via inflation. Since then, many new


stablecoins have arisen based on similar ideas by UMA, Reflexer, and Liquity,


as well as _endogenous collateral_ stablecoins like Synthetix sUSD, Terra UST, and


Celo Dollar (see [110] for further discussion). Notably, unlike custodial stable

coins, Dai is not currently considered as emoney or payment method subject to


the Payment Services Directive in the European Union since there is no single


issuer or custodian. Thus it does not have AML/KYC requirements.


In an academic white paper, [46] proposed a variation on cryptocurrency

collateralized DStablecoin design. It standardizes the speculative positions by


restricting leverage to pre-defined bounds using automated resets. A conse

quence of these leverage resets is that stablecoin holders are partially liquidated


from their positions during downward resets–i.e., when leverage rises above


the allowed band due to a cryptocurrency price crash. This compares with Dai,


in which stablecoin holders are only liquidated in global settlement. An effect


- f this difference is that, in order to maintain a stablecoin position in the short

term, stablecoin holders need to re-buy into stablecoins (at a possibly inflated


price) after downward resets. Of the many designs, it is unclear which delever

85


aging method would lead to a system that survives longer. This motivates us to


study the dynamics of DStablecoin systems.


Non-custodial stablecoins have now experienced a wide array of volatility


events, failures, and attacks. Since the initial release of this paper in 2019, Black


Thursday in March 2020 saw massive liquidation events result in a substan

tial depegging in Dai [130], mirroring our results in Sections 3.3-3.4, and miner


mempool manipulation that contributed to Dai liquidation auctions clearing at


near zero prices at a cost of $8m to the Maker system [36], mirroring attack sur

[faces we described in Section 3.6. Prior to this, as discussed in [103], Nubits](https://nubits.com/)


has traded at cents on the dollar since 2018 (Figure 3.1a), and bitUSD and Steem


Dollars have broken their USD pegs periodically (Figure 3.1b). Many additional


examples of stablecoin mechanism failures and exploitations occurred through


the rest of 2020 (see [110, 185]). Yet, the stablecoin space has remained heated


with projects such as Dai growing rapidly and many new contenders arising,


including UMA, Reflexer, Celo, and Liquity. The work in this paper has proven


consequential for the progression of these projects (e.g., [121, 133]).

#### **3.1.2 Relation to prior work**


Stablecoins are active cryptocurrencies, for which pre-existing models do not


understand how the collateral rule enforces stability and how the interaction of


different agents can affect stability.


With the notable exception of [46], rigorous mathematical work on non

custodial stablecoins is lacking. They applied option pricing theory to valuing


tranches in their proposed DStablecoin design using advanced PDE methods.


86


##### NuBits Charts

Zoom 1d 7d 1m 3m 1y YTD **ALL**


0



From Sep 24, 2014 To Dec 12, 2018



Jan '15 Jul '15 Jan '16 Jul '16 Jan '17 Jul '17 Jan '18 Jul '18

|2015 2016|Col2|2017 20|
|---|---|---|
||||



**Market Cap** **Price (USD)** **Price (BTC)** **24h Vol**


(a) NuBits trades at cents on the dollar.


##### bitUSD Charts

Zoom 1d 7d 1m **3m** 1y YTD ALL


0



From Sep 12, 2018 To Dec 12, 2018



17. Sep 1. Oct 15. Oct 29. Oct 12. Nov 26. Nov 10. Dec

|2016|2018|
|---|---|
|||



**Market Cap** **Price (USD)** **Price (BTC)** **Price (BTS)** **24h Vol**


(b) BitUSD has broken its USD peg.


Figure 3.1: Depeggings in decentralized stablecoins.


87



$1.00


$0.500000


$0


coinmarketcap.com


$1.00


$0.800000


$0.600000


coinmarketcap.com


In doing so, they need the simplifying assumption that DStablecoin payouts


(e.g., from interest/fee payments and liquidations from leverage resets) are ex

- genously stable with respect to USD. This may circularly cause stability. In


reality, these payouts are made in volatile cryptocurrency (ETH). From these


ETH payments, stablecoin holders can


1. Hold ETH and so take on ETH exposure,


2. Use the ETH to re-buy into stablecoin, likely at an inflated price as it en

dogenously increases demand after a supply contraction,


3. Convert the ETH to fiat, which requires waiting for block confirmations


in an exchange (possibly hours) during times when ETH is particularly


volatile and paying costs for fiat conversion (fees, potentially taxes). No

tably, this is not available in all jurisdictions.


To maintain a DStablecoin position, stablecoin holders need to re-buy into


DStablecoins at each reset at endogenously higher price. Stablecoin holders ad

ditionally face the risk that the size of the DStablecoin market collapses such that


the position cannot be maintained (and so ends up holding ETH). As no stable


asset models exist to understand these endogenous effects, the analysis can’t


be easily extended using the traditional financial literature. [4] Our focus in this


paper is complementary to understand these endogenous stable asset effects.


[122] studied the evolution of custodial stablecoins. A few works on sta

blecoins have also arisen since the initial release of our paper. [107] described


governance attack surfaces in non-custodial stablecoins, which is extended with


4A secondary issue with their continuous model is that these systems are inherently discontinuous due to the discrete nature of incorporating blockchain transactions into blocks. Thus
resets can occur beyond the set thresholds.


88


general models in [110]. [78] presented an analysis of credit risk stemming from


collateral type in the Maker system. And [160, 55] modeled stability in the Terra


and Celo stablecoins under different scenarios of Brownian motion without the


endogenous market feedback effects we study in this paper.


In the context of central counterparty clearinghouses, the default fund con

tributions, margin requirements and participation incentives have been studied


in, e.g., [48], [8], and [73]. The critical question in this area is understanding the


effects of a liquidation policy of a member’s portfolio in the case of a significant


event. The counterpart of this in a decentralized setting is understanding the


impact of DStablecoin deleveraging on system stability.


Stablecoin holders bear some resemblance to agents in currency peg and in

ternational finance models, e.g., [144] and [89]. In these models, the market


maker is essentially the government but is modeled with mechanical behavior


and is not a player in the game. For instance, in [89], devaluation is modeled


by a simple exogenous threshold rule: the government abandons the peg if the


net demand for currency breaches the threshold and is otherwise committed to


maintaining the peg. In contrast to currency markets, no agents are committed


to maintaining the peg in DStablecoin markets. The best we can hope is that the


protocol is well-designed and that the peg is maintained with high probability


through the protocol’s incentives. The role of government is replaced by decen

tralized speculators, who issue and withdraw stablecoins in a way to optimize


profit. A fully strategic model would be a complicated dynamic game–these


tend to be intractable and, indeed, are avoided in the currency peg literature in


favor of a sequence of one period games. We enable a more endogenous mod

eling of speculators’ optimization problems under a variety of risk constraints.


89


Our model is a sequence of one-period optimization problems, in which dy

namic coupling comes through the risk constraints.


DStablecoin speculators are similar to market makers in market microstruc

ture models (e.g., [154]). Like classical market microstructure, we do have a


multi-period system with multiple agents subject to leverage constraints that


take recurring actions according to their objectives. In contrast, in the DStable

coin setting, we do not have a truly stable asset that is efficiently and instanta

neously available. Instead, agents make decisions that endogenously affect the


price of the ‘stable’ asset and affect the agents’ future decisions and incentives


to participate in a non-stationary way. In turn, the (in)stability results from the


dynamics of these decisions.


Since the initial release of our paper in June 2019, [114] has described a


complementary model of non-custodial stablecoins related to the model in this


paper. That paper explores a different model of liquidation structure that af

fects speculator decision-making and applies martingale methods to analyti

cally characterize stability. In contrast, in this paper we derive stability results


about a simpler model that is more amenable to simulations, which we perform,


and demonstrate stablecoin attacks that can arise from profitable bets against


- ther agents.

#### **3.1.3 This paper**


We develop a dynamic model for non-custodial stablecoins that is complex


enough to take into account the feedback effects discussed above and yet re

mains tractable. Our model can be interpreted as a market microstructure model


90


in this new type of asset market.


Our model involves agents with different risk profiles; some desire to hold


stablecoins and others speculate on the market. These agents solve optimization


problems consistent with a wide array of documented market behaviors and


well-defined financial objectives. As is common in the literature on market mi

crostructure and currency peg games, these agents’ objectives are myopic. These


- bjectives are coupled for non-myopic risk using a flexible class of rules that are


widely established in financial markets; these allow us to model the effects of


a range of cyclic and counter-cyclic behaviors. The exact form of these rules is


selected and self-imposed by speculators to match their desired responses and


not part of the stablecoin protocol. Thus well-established manipulation of simi

lar rules as applied to traditional financial regulation is not a problem here. Our


model goes largely beyond a one-period model. We introduce this model with


supporting rationale for design choices in Section 3.2.


Using our model, we make the following contributions:


  - We derive fundamental results about dynamics and liquidity in our model


(Section3.3).


  - We demonstrate that stablecoins face deleveraging feedback effects that


may cause illiquidity during crises and exacerbate collateral drawdown


(Section 3.3.3).


  - We characterize stable dynamics of the system under certain conditions


that guarantee no liquidity crash (Section 3.4) and show instability can


   - ccur in simulations outside of this setting (Section 3.4.2).


  - We simulate a wide range of market behaviors and find that speculator be

91


havior has a large effect on realized volatilities, but that stablecoin failure


times are largely determined by underlying asset movements (Section 3.5).


  - We describe new attacks that exploit arbitrage-like opportunities around


stablecoin liquidations (Section 3.6).


We relate these results to historical stablecoin events and apply these insights


to suggest design improvements that aim to improve long-term stability. Based


- n these insights, we also suggest that interactions between multiple specula

tors and attackers may be the most interesting relationships to explore in more


complex models.

#### **3.2 Model**


Our model couples a number of variables of interest in a risk transfer market


between stablecoin holders and speculators. The stablecoin protocol dictates


the logic of how agents can interact with the smart contracts that form the sys

tem; the design of this influences how the market plays out. Many DStablecoin


designs have been proposed. We set up our model to emulate a DStablecoin


protocol like Dai with global settlement, but the model is adaptable to different


design choices. Note that our model is formulated with very few parameters


given the problem complexity.


Our model builds on the model of traditional financial markets in [19] but is


new in design by incorporating endogenous stablecoin structure. In the model,


we assume that the underlying consensus layer (e.g., blockchain) works well to


confirm transactions without censorship or attack and that the system of con

92


tracts executes as intended.


**Agents.** Two agents participate in the market.


 - The **stablecoin holder** seeks stability and chooses a portfolio to achieve


this.


 - The **speculator** chooses leverage in a speculative position behind the


DStablecoin.


Stablecoin holders are motivated by risk aversion, trade limitations, and


budget constraints. They are inherently willing to hold cryptoassets. In the


current setting, this means they are likely either traders looking for short-term


stability, users from countries with unstable fiat currencies, or users who are


using cryptocurrencies to move money across borders. In the future, cryptocur

rencies may be more accepted in economic exchange. In this case, stablecoin


holders may be ordinary consumers who face risk aversion and budgeting for


required consumption.


Speculators are motivated by (1) access to leverage and (2) security lending


to borrow against their Ether holdings without triggering tax incidence or giv

ing up Ether ownership. In order to begin participating, speculators need to


either have confidence in the future of cryptocurrencies, think they can make


money trading the markets, or face unusually high tax rates (or other barriers)


that make security lending cheaper than outright selling assets. The model in


this paper focuses on the first motivation. We propose an extension to the model


that considers the second motivation.


93


**Assets.** There are two assets. For simplicity, we give these assets specific


names; however, they could be abstracted to other cryptocurrencies or outside


- f a cryptocurrency setting.


 - **Ether** : high risk asset whose USD market prices _p_ _[E]_ _t_ [are exogenous]


 - **DStablecoin** : a ‘stable’ asset collateralized in Ether whose USD price _p_ _[D]_ _t_ [is]


endogenous


Notably, a large DStablecoin system may have endogenous amplification ef

fects on Ether price, similarly to how CDOs affected underlying assets in the


2008 financial crisis. We discuss this further in Section 3.7 but leave formal mod

eling of this to future work.


There are several barriers for trading between crypto and fiat, which mo

tivate our choice of assets. Most crypto-fiat pairs are through Bitcoin or Ether,


which act as a gateway to other cryptoassets. Trading to fiat can involve moving


assets between a number of exchanges and can take considerable time to con

firm on the blockchain. Trading to a stablecoin is comparatively simple. Trading


to fiat can also trigger more clear tax incidence. Additionally, some countries


have imposed strict capital controls on trading between fiat and crypto.


**Model outline.** At _t_ = 0, the agents have endowments and prior beliefs. In


each period _t_ :


1. New Ether price is revealed


2. Ether expectations are updated


3. Stablecoin holder decides portfolio weights


94


4. Speculator, seeing demand, decides leverage


5. DStablecoin market is cleared

#### **3.2.1 Stablecoin holder**


The stablecoin holder starts with an initial endowment and decides portfolio


weights to attain the desired stability. The following table defines the agent’s


state variables.


**Variable** **Definition**


_n_ ¯ _t_ Ether held at time _t_


_m_ ¯ _t_ DStablecoin held at time _t_


**wt** Portfolio weights chosen at time _t_


The stablecoin holder weights its portfolio by **wt** . We denote the components


as _wt_ _[E]_ [and] _[ w]_ _t_ _[D]_ [for Ether and DStablecoin weights respectively. The stablecoin]


holder’s portfolio value at time _t_ is


_At_ = ¯ _ntp_ _[E]_ _t_ [+ ¯] _[m][t][p][D]_ _t_ [= ¯] _[n][t][−]_ [1] _[p][E]_ _t_ [+ ¯] _[m][t][−]_ [1] _[p][D]_ _t_ _[.]_


Given weights, ¯ _nt_ and ¯ _mt_ will be determined based on the stablecoin clearing


price _p_ _[D]_ _t_ [.]


The basic results in Section 3.3 hold generally for any **wt** _≥_ 0 (i.e., there


is no shorting). In this case, **wt** could be chosen, e.g., from Sharpe ratio op

timization, mean-variance optimization, or Kelly criterion (among others). In


Sections 3.4 & 3.5, in order to focus on the effects of speculator decisions, we


simplify the stablecoin holder as exogenous with unit price-elastic demand. In


this case, DStablecoin demand is constant in dollar terms.


95


#### **3.2.2 Speculator**

The speculator starts with an endowment of Ether and initial beliefs about


Ether’s returns and variance and decides leverage to maximize expected returns


subject to protocol and self-imposed constraints. The following tables define


variables and parameters for the speculator.


**Variable** **Definition**


_nt_ Ether held at time _t_


_rt_ Expected return of Ether at time _t_


_σt_ [2] Expected variance of Ether at time _t_


_Lt_ Total stablecoins issued at time _t_


∆ _t_ Change to stablecoin supply at time _t_


˜
_λt_ Leverage bound at time _t_


**Parameter** **Definition**


_γ_ Memory parameter for return estimation


_δ_ Memory parameter for variance estimation


_β_ Collateral liquidation threshold


_α_
Parameter governing risk measure (inversely related to VaR)


_b_ Cyclicality parameter in risk constraint:


pro- ( _b >_ 0) or counter-cyclic ( _b <_ 0)


96


**Ether expectations**


The speculator updates expected returns _rt_, log-returns _µt_ (used for the variance


estimation), and variance _σt_ [2] [based on observed Ether returns as follows:]


_t_
_rt_ = (1 _−_ _γ_ ) _rt−_ 1 + _γ_ _[p][E]_ _,_
_p_ _[E]_ _t−_ 1



_t_
_µt_ = (1 _−_ _δ_ ) _µt−_ 1 + _δ_ log _[p][E]_ _,_
_p_ _[E]_ _t−_ 1


2
_σt_ [2] [= (1] _[ −]_ _[δ]_ [)] _[σ]_ _t_ [2] _−_ 1 [+] _[ δ]_ log _[p]_ _t_ _[E]_ _−_ _µt_ _._

        - _p_ _[E]_ _t−_ 1        


(3.1)



For fixed memory parameters _γ, δ_ (lower memory parameter = longer mem

- ry), these are exponential moving averages consistent with the RiskMetrics


approach commonly used in finance [126]. For sufficiently stepwise decreasing


memory levels and assuming i.i.d. returns, this process will converge to the true


values supposing they are well-defined and finite. In reality, speculators don’t


- utright know the Ether return distribution and, as we will see in the simula

tions, the stablecoin system dynamics occur on timescales shorter than required


for convergence of expectations. Thus, we focus on the simpler case of fixed


memory parameters.


Note that _γ ̸_ = _δ_ may be reasonable. Current cryptocurrency markets are


not very price efficient, and so traders might reasonably take into account mo

mentum when estimating returns while using a wider memory for estimating


covariance.


We additionally consider the case in which the speculator knows the Ether


distribution outright and _γ_ = _δ_ = 0. This is consistent with a rational expecta

tions standpoint but ignores how the speculator arrives at that knowledge.


97


**Optimize leverage: choose** ∆ _t_


The speculator is liable for _Lt_ DStablecoins at time _t_ . At each time _t_, it decides


the number of DStablecoins to create or repurchase. This changes the stable

coin supply _Lt_ = _Lt−_ 1 + ∆ _t_ . If ∆ _t >_ 0, the speculator creates and sells new


DStablecoin in exchange for Ether at the clearing price. If ∆ _t <_ 0, the speculator


repurchases DStablecoin at the clearing price.


Strictly speaking, the speculator will want to maximize its long-term with

drawable value. At time _t_, the speculator’s withdrawable value is the value of


its ETH holdings minus collateral required for any issued stablecoins: _ntp_ _[E]_ _t_ _[−]_


_βLt_ . Maximizing this is not amenable to a myopic view, however, as maximiz

ing the next step’s withdrawable value is only a good choice when the specula

tor intends to exit in the next step.


Instead, we frame the speculator’s objective as maximizing expected equity:


_ntp_ _[E]_ _t_ _[−]_ **[E]** [[] _[p][D]_ []] _[L][t]_ [. In this, the speculator expects to be able to settle liabilities at a]


long-term expected value of **E** [ _p_ _[D]_ ]. The market price of DStablecoin will fluctu

ate above and below $1 naturally depending on prevailing market conditions.


The actual expected value is nontrivial to compute as it depends on the stability


- f the DStablecoin system. For individual speculators with small market power,


we argue that **E** [ _p_ _[D]_ ] = 1 is a an assumption they may realistically make, as we


discuss further below. This is additionally the value realized in the event of


global settlement.


We suggest that this optimization is a candidate for ‘honest’ behavior of a


speculator as it is consistent with the speculator acting on perceived arbitrage


in mispricings of DStablecoin from the peg. In essence, the speculator expects to


98


increase (reduce) leverage ‘at a discount’ when _p_ _[D]_ _t_ [is above (below) target. This]


is the typically cited mechanism by which these systems maintain their peg and


thus how the designers _intend_ for speculators to behave. However, this assumes


that _p_ _[D]_ _t_ [is sufficiently stable/mean-reverting to $1 and so this behavior may not]


in fact be a best response.


**Aggregate vs. individual speculators.** In our model, the single speculative


agent, which is not a price-taker, is intended to reflect the aggregate behavior of


many individual speculators, each with small market power. [5] In a normal liquid


market, an individual speculator would be able to repurchase DStablecoins at


dollar cost and walk away with the equity. By maximizing equity, the aggregate


speculator considers its liabilities to be $1 per DStablecoin. This may turn out to


be untrue during liquidity crises as the repurchase price may be higher. In our


model, speculator’s don’t know the probability of crises and instead account for


this in a conservative risk constraint.


**Formal optimization problem.** The speculator chooses ∆ _t_ by maximizing ex

pected equity in the next period subject to a leverage constraint:


max _rt_ _nt−_ 1 _p_ _[E]_ _t_ [+ ∆] _[t][p][D]_ _t_ [(] _[L][t]_ [)] _−Lt_
∆ _t_          -          

s.t. ∆ _t ∈Ft_


where _Ft_ is the feasible set for the leverage constraint. This is composed of two


separate constraints: (1) a **liquidation constraint** that is fundamental to the pro

tocol, and (2) a **risk constraint** that encodes the speculator’s desired behavior.


Both are introduced below.


5We propose to relax this simplification in follow-up work by considering the interaction of
many speculators with longer term strategic thinking.


99


If the leverage constraint is unachievable, we assume the speculator enters


a ‘recovery mode’, in which it tries to maximize its chances of returning to the


normal setting. In this case, it solves the optimization using only the liquidation


constraint. If the liquidation constraint is unachievable, the DStablecoin system


fails with a global settlement.


**Liquidation constraint: enforced by the protocol**


The liquidation constraint is fundamental to the DStablecoin protocol. A spec

ulator’s position undergoes forced liquidation at time _t_ if either (1) after _p_ _[E]_ _t_ [is]


revealed, _nt−_ 1 _p_ _[E]_ _t_ _[< β][L][t][−]_ [1][, or (2) after][ ∆] _[t]_ [is executed,] _[ n][t][p][E]_ _t_ _[< β][L][t]_ [. The speculator]


aims to control against this as liquidations can occur at unfavorable prices and


are associated with fees in existing protocols (we exclude these fees from our


simple model, but they can be easily added).


Define the speculator’s leverage as the _β_  - weighted ratio of liabilities to as

sets [6]

_λt_ = _[β][ ·]_ [ liabilities] _._

assets


The liquidation constraint is then _λt ≤_ 1.


**Risk constraint: self-imposed speculator behavior**


The risk constraint encodes the speculator’s desired behavior into the model.


_We assume no specific type for the risk constraint in our analytical results, which are_


_generic._ For our simulations, we explore a variety of speculator behaviors via the


6We choose this definition to simplify the model. The alternative definition
_λ_ _[′]_ = assets _−_ assets _β·_ liabilities [describes the same idea scaled from 0 to] _[ ∞]_ [. I.e.,] _[ λ][′]_ [ =] 1 _−_ 1 _λ_ [is monoton-]
ically increasing in _λ_ for 0 _≤_ _λ_ _[′]_ _<_ 1.


100


risk constraint. We first consider Value-at-Risk (VaR) _as an example_ - f a constraint


realistically used in markets. This is consistent with narratives shared by Dai


speculators about leaving a margin of safety to avoid liquidations. We then


construct a generalization that goes well beyond VaR and allows us to explore


a spectrum of pro-cyclical and counter-cyclical behaviors encoded in the risk


constraint.


Manipulation and instability resulting from similar _externally-imposed_ VaR


rules is a well-known problem in the risk management and financial regulatory


literature (see e.g., [19]). This is of less concern here as the precise parameters


- f the risk constraint are selected and self-imposed by speculators to approxi

mate their own utility optimization and are not part of the DStablecoin protocol.


Further, we consider constraints that go _beyond VaR_ . We instead need to show


that our results are robust to a variety of risk constraints that speculators could


select.


**Example: VaR-based constraint.** The VaR-based version of the risk constraint


is


_λt ≤_ exp( _µt −_ _ασt_ ) _,_


where _α >_ 0 is inversely related to riskiness. This is consistent with VaR for


normal and maximally heavy-tailed symmetric return distributions with finite


variance.


Let VaR _a,t_ be the _a_  - quantile per-dollar VaR of the speculator’s holdings at


time _t_ . This is the minimum loss on a dollar in an _a_ - quantile event. With a VaR


constraint, the speculator aims to avoid triggering the liquidation constraint in


the next period with probability 1 _−_ _a_, i.e., **P** _ntp_ _[E]_ _t_ +1 _[≥]_ _[β][L][t]_ _≥_ 1 _−_ _a._ To achieve

                 -                 

101


this, the speculator chooses ∆ _t_ such that


_nt−_ 1 _p_ _[E]_ _t_ [+ ∆] _[t][p][D]_ _t_ [(] _[L][t]_ [)] (1 _−_ VaR _a,t_ ) _≥_ _βLt._

        -        

This requires _λt ≤_ 1 _−_ VaR _a,t_, which addresses the probability that the liquida

tion constraint is satisfied next period and implies that it is satisfied this period.


Define _λ_ [˜] _t_ := exp( _µt −_ _ασt_ ). Then _λ_ [˜] _t_ is increasing in _µt_ and decreasing in _σt_ .


Further, the fatter the speculator thinks the tails of the return distribution are,


the greater _α_ will be, and the lesser _λ_ [˜] _t_ will be, as we demonstrate next.


**VaR constraint with normal returns.** If the speculator assumes Ether log re


turns are ( _µt, σt_ ) normal, then VaR _a,t_ = 1 _−_ exp _µt_ + _√_

                 


2 _σt_ erf _[−]_ [1] (2 _a−_ 1) _._ Defining

      


_α_ = _−√_



2erf _[−]_ [1] (2 _a −_ 1), which is positive for appropriately small _a_, the VaR con


straint is _λt ≤_ 1 _−_ VaR _a,t_ = exp( _µt −_ _ασt_ ) _._


**VaR constraint with heavy tails.** If Ether log returns _X_ are symmetrically dis

tributed with finite mean _µt_ and finite variance _σt_ [2][, then for any] _[ α >]_ [ 1][, Cheby-]


shev’s inequality gives us


1
**P** ( _X < µt −_ _ασt_ ) _≤_
2 _α_ [2] _[.]_


For the maximally heavy-tailed case, this inequality is tight. Then for VaR quan

1
tile _a_, we can find the corresponding _α_ such that _a_ = 2 _α_ [2] [. The log return VaR is]


_µt −_ _ασt_, which gives the per-dollar VaR _a,t_ = 1 _−_ exp( _µt −_ _ασt_ ). Then the VaR


constraint is _λt ≤_ exp( _µt −_ _ασt_ ).


102


**Generalized risk constraint.** Similarly to [19], we can generalize the bound to


explore a spectrum of different behaviors:


ln _λ_ [˜] = _µt −_ _ασt_ _[b][,]_


where _α_ is an inverse measure of riskiness and _b_ is a cyclicality parameter. A


positive _b_ means that _λ_ [˜] _t_ decreases with perceived risk (pro-cyclical). A negative


_b_ means that _λ_ [˜] _t_ increases with perceived risk (counter-cyclical).

#### **3.2.3 DStablecoin market clearing**


The DStablecoin market clears by setting demand = supply in dollar terms:


_wt_ _[D]_ _n_ ¯ _t−_ 1 _p_ _[E]_ _t_ [+ ¯] _[m][t][−]_ [1] _[p][D]_ _t_ [(] _[L][t]_ [)] = _Ltp_ _[D]_ _t_ [(] _[L][t]_ [)] _[.]_

         -         

The demand (left-hand side) comes from the stablecoin holder’s portfolio


weight and asset value. Notice that while the asset value depends on _p_ _[D]_ _t_ [, the]


portfolio weight _wt_ _[D]_ [does not. That is, the stablecoin holder buys with market]


- rders based on weight. This simplification allows for a tractable market clear

ing; however, it is not a full equilibrium model.


We justify this choice of simplified market clearing with the following obser

vations:


  - The clearing is similar to constant product market maker model used in


the Uniswap decentralized exchange (DEX) [192].


  - Sophisticated agents are known to be able to front-run DEX transactions


[64]. As speculators are likely more sophisticated than ordinary stable

103


coin holders, in many circumstances they can see demand before making


supply decisions. [7]


  - Evidence from Steem Dollars suggests that demand need not decrease


tremendously with price in the unique setting in which stable assets are


not efficiently available. Steem Dollars is a stablecoin with a mechanism


for price ‘floor’ but not ‘ceiling’. Over significant stretches of time, it has


traded at premiums of up to 15 _×_ target.


In most of our results, the time period context is clear. To simplify notation,


in a given time _t_, we drop subscripts and write with the following quantities:


**Quantity** **Sign** **Interpretation**


_x_ := _wt_ _[D][n]_ [¯] _[t][−]_ [1] _[p][E]_ _t_ _x ≥_ 0 New DStablecoin demand available


_y_ := _wt_ _[D][m]_ [¯] _[t][−]_ [1] _[−L][t][−]_ [1] _y ≤_ 0 _|y|_ = ‘free supply’ in DStablecoin market


_z_ := _nt−_ 1 _p_ _[E]_ _t_ _z ≥_ 0 Speculator value available to maintain market


_L_ := _Lt−_ 1


∆ := ∆ _t_


˜ ˜
_λ_ := _λt_


**w** := **wt**


With ∆ _> y_, which turns out to be always true as discussed later, the clearing


price is


_x_
_p_ _[D]_ _t_ [(∆) =] ∆ _−_ _y_ _[.]_


7This said, DEX mechanics differ slightly from our specific formulation. To make the model
more realistic, stablecoin holders could issue buy offers in token units instead of weights at the
expense of greater model complexity.


104


As the model is defined thus far, stablecoin holders only redeem coins for


collateral through global settlement. However, this assumption is easily relaxed


to accommodate algorithmic or manual settlements.

#### **3.3 Stable Asset Market Dynamics**


We derive tractable solutions to the proposed interactions and results about liq

uidity and stability.

#### **3.3.1 Solution to the speculator’s decision**


We first introduce some basic results about the speculator’s leverage optimiza

tion problem.


**Solving the leverage constraint.**


**Prop. 3.1.** _Let_ ∆min _≥_ ∆max _be the roots of the polynomial in_ ∆


˜

_−β_ ∆ [2] + ∆ _λ_ ( _z_ + _x_ ) _−_ _β_ ( _L −_ _y_ ) _−_ _λzy_ [˜] + _βLy._

          -           

_Assuming_ ∆ _> y,_


 - _If_ ∆min _,_ ∆max _∈_ R _, then_ [∆min _,_ ∆max] _∩_ ( _y, ∞_ ) _is the feasible set for the leverage_


_constraint._


 - _If the roots are not real, then the constraint is unachievable._


[Link to Proof]


105


Setting _λ_ [˜] = 1 gives the expression for the liquidation constraint alone.


The condition ∆ _> y_ makes sense for two reasons. First, if ∆ _< y_ then _p_ _[D]_ _t_ _[<]_ [ 0][.]


Second, as we show below, the limit lim∆ _→y_ + _p_ _[D]_ _t_ [=] _[ ∞]_ [. Thus, if we start in the]


previous step under the condition ∆ _> y_, then the speculator will never be able


to pierce this boundary in subsequent steps. We further discuss the implications


- f this condition later.


**Solving the leverage optimization.**


**Prop. 3.2.** _Assume that the speculator’s constraint is feasible and let_ [∆min _,_ ∆max] _∩_


( _y, ∞_ ) _be the feasible region. Define r_ := _rt, let_ ∆ _[∗]_ = _y_ + _[√]_ ~~_−yrx_~~ _, and define_


_x_
_f_ (∆) = _r_ ∆∆ _−_ _y_ _[−]_ [∆] _[.]_


_Then the solution to the speculator’s optimization problem is_


 - ∆ _[∗]_ _if_ ∆ _[∗]_ _∈_ [∆min _,_ ∆max] _∩_ ( _y, ∞_ )


  - ∆min _if_ ∆ _[∗]_ _<_ ∆min


  - ∆max _if_ ∆ _[∗]_ _>_ ∆max


[Link to Proof]

#### **3.3.2 Maintenance condition for the stable asset market**


The next result describes a bound to the speculator’s ability to maintain the


market. This bound takes the form of


106


(a lower bound on collateral) - (capital available to enter the market),


which must be sufficiently high for the system to be maintainable.


**Prop. 3.3.** _The feasible set for the speculator’s liquidation constraint is empty when_


˜
_λ_ ( _x_ + _z_ ) _−_ _βLw_ _[D]_ [�][2] _<_ 4 _βλ_ [˜] _Lxw_ _[E]_

         

[Link to Proof]


In Prop. 3.3, _βLw_ _[D]_ _≥_ 0 is interpreted as a lower bound on the capital re

quired to maintain the DStablecoin market into the next period (i.e., the collat

eral required for the minimum size of the DStablecoin market), _λ_ [˜] _∈_ [0 _,_ 1], and


_x_ + _z ≥_ 0 is the capital available to enter the DStablecoin market from both


the supply and demand sides. The inequality then states that the difference


between the capital available to enter the market and the lower bound mainte

nance capital must be sufficiently high for the market to be maintainable by the


speculator. The constraint ∆ _< y_ implies that the case of the negative difference


does not work.

#### **3.3.3 Deleveraging effects, limits to market liquidity**


**Limits to the speculator’s ability to decrease leverage.** The next result


presents a fundamental limit to how quickly the speculator can reduce lever

age by repurchasing DStablecoins, given the modeled market structure. Note


that this limit applies even if the speculator can bring in additional capital. The


term _−y_ = _L_ (1 _−_ _w_ _[D]_ ) represents the ‘free supply’ of DStablecoin available for


∆.
exchange, which can be increased by a positive


107


**Prop. 3.4.** _The speculator with asset value z cannot decrease DStablecoin supply at t_


_more than_


_z_
∆ _[−]_ :=
_z_ + _x_ _[y.]_


_Further, even with additional capital, the speculator cannot decrease the DStablecoin_


_supply at t by more than y._


[Link to Proof]


**Deleveraging affects collateral drawdown through liquidity crises.** The re

sult leads to a DStablecoin market price effect from leverage reduction. This


can lead to a _deleveraging spiral_, which is a feedback loop in leverage reduction


and drying liquidity. In this, the speculator repurchases DStablecoin to reduce


leverage at increasing prices as liquidity dries up as repurchase tends to push


up _p_ _[D]_ _t_ [if outside demand remains the same. At higher prices, more collateral]


needs to be sold to achieve deleveraging, leaving relatively less in the system.


Subsequent deleveraging, whether voluntary or through liquidation, becomes


more difficult as the price effects compound.


Whether or not a spiraling effect occurs will depend on the demand behavior


- f stablecoin holders. The action of the stablecoin holder may actually exacer

bate this effect: during extreme Ether price crashes, stablecoin holders will tend


to increase their DStablecoin demand in a ‘flight to safety’ move. Table 3.1 illus

trates an example scenario of a deleveraging spiral in a simplified setting with


constant unit demand elasticity and in which the speculator’s risk constraint is


the liquidation constraint. Similar results hold under other constant demand


elasticities. The system starts in a steady state. the Ether price declines trigger


108


_t_ _p_ _[E]_ _t_ ∆ _t_ _Lt_ _p_ _[D]_ _t_ _nt_
0 85 100 _._ 583 0 _._ 994 1 _._ 8

1 83 _−_ 3 _._ 115 97 _._ 468 1 _._ 026 1 _._ 761

2 82 _−_ 4 _._ 105 93 _._ 363 1 _._ 071 1 _._ 708

3 81 _−_ 4 _._ 57 88 _._ 793 1 _._ 126 1 _._ 644


Table 3.1: Example scenario of a deleveraging spiral.


three waves of liquidations, forcing the speculator to liquidate her collateral to


deleverage at rising costs.


If Ether prices continue to go down, [8] the deleveraging spiral is only fixed if


(1) more money comes into the collateral pool to create more DStablecoins, or (2)


people lose faith in the system and no longer want to hold DStablecoins, which


can cause the system to fail. There is no guarantee that (1) always happens.


This liquidity effect on DStablecoin price makes sense because the stablecoin


(as long as it’s working) should be worth more than the same dollar amount of


ETH during a downturn because the stablecoin comes with additional protec

tion. If the speculator is forced to buy back a sizeable amount of the coin supply,


it will have to do so at a premium price.


One might think the spiral effect is good for stablecoin holders. As we ex

plore in Section 3.6, this can be the case for a short-term trade. However, as


we will see, the speculator’s ability to maintain a stable system may deteriorate


during these sort of events as it has less control or less willingness to control the


coin supply. Deleveraging effects can siphon off collateral value, which can be


detrimental to the system in the long-term.


This suggests the question: do alternative non-custodial designs suffer sim

8Ether price decline can further be facilitated by feedback from large liquidations, as discussed earlier.


109


ilar deleveraging problems? We compare to an alternative design described in


[46]. In this design, the stablecoin is restricted to pre-defined leverage bounds,


at which algorithmic ‘resets’ partially liquidate both stablecoin holder and spec

ulator positions at $1 price. While this quells the price effect on collateral, it


_shifts_ the deleveraging risk from speculator to stablecoin holder. The stablecoin


holder is liquidated at $1 price but, if they want to maintain a stablecoin posi

tion, they have to re-buy in to a smaller market at inflated price. Of the many


designs, it is unclear which deleveraging method would lead to a system that


survives longer.


**Results explain real market data.** A preliminary analysis of Dai market data


suggests that our results apply. Figure 3.2a shows the Dai price appreciate in


Nov-Dec 2018 during multiple large supply decreases. This is consistent with


an early phase of a deleveraging spiral. Figure 3.2b shows trading data from


multiple DEXs over Jan-Feb 2019: price spikes occur in the data reportedly from


speculator liquidations [166]. This provides empirical evidence that liquidity is


indeed limited for lowering leverage in Dai markets. Further, as discussed in the


next section, Dai empirically trades below target in many normal circumstances.


Since releasing the initial version of this paper in June 2019, massive liqui

dation events around Black Thursday in March 2020 provide additional strong


evidence of deleveraging effects in the Dai market. Figure 3.3a depicts a _∼_ 50%


ETH price cash on 12 Mar. 2020, which precipitated a cascade of cryptocurrency


liquidations. Figure 3.3b depicts the price effects of these liquidations on Dai


prices on DEXs. Speculators deleveraging during this event had to pay premi

ums of _∼_ 10% and face consistent premiums _>_ 2% weeks into the aftermath.


Concurrently, Maker was affected by global mempool flooding on Ethereum.


110


Dai Charts


Zoom 1d 7d **1m** 3m 1y YTD ALL


$70M


$60M


$50M


0



From Nov 12, 2018 To Dec 12, 2018



$1.04


$1.00


$0.960000



14. Nov 18. Nov 22. Nov 26. Nov 30. Nov 4. Dec 8. Dec 12. Dec





**Market Cap** **Price (USD)** **Price (BTC)** **Price (ETH)** **24h Vol**


coinmarketcap.com


(a)


(b)


Figure 3.2: Model Results explain data from Dai market. (a) Dai deleveraging feedback in Nov-Dec 2018 (image from coinmarketcap). (b) Dai normally trades below target with spikes in price due to liquidations (image from
dai.stablecoin.science).


111


This additionally contributed to Dai liquidation auctions clearing at near zero


prices, which may in fact have amplified the deleveraging feedback effects. Al

together, Dai traded at significant premiums over this time despite Maker being


in a much riskier state in terms of collateral and liquidations. See [105] and [36]


for further discussion of this event.

#### **3.4 Stability results**


We now characterize stable price dynamics of DStablecoins when the leverage


constraint is non-binding. For this section, we make the following simplifica

tions to focus on speculator behavior:


  - The market has fixed dollar demand at each _t_ : _wt_ _[D][A][t]_ [=] _[ D]_ [. This is consis-]


tent with the stablecoin holder having unit-elastic demand, or having an


exogenous constraint to put a fixed amount of wealth in the stable asset.


  - Speculator’s expected Ether return is constant _rt_ = ˆ _r >_ 1. This means they


always want to fully participate in the market and is consistent with _γ_ = 0.


This amounts to setting _x_ = _D_ and _y_ = _−L_ . Now the DStablecoin market


clearing price is _p_ _[D]_ _t_ [=] _L_ _[D]_ _t_ _[.]_ [ The leverage constraint (assuming] _[ L]_ [+∆] _[>]_ [ 0][) becomes]


_−β_ ∆ [2] + ∆( _λ_ [˜] ( _z_ + _D_ ) _−_ 2 _βL_ ) + _L_ ( _λz_ [˜] _−_ 2 _β −_ _βL_ ) _≥_ 0 _._


ˆ _r_ ∆ _D_
The speculator’s maximization objective becomes _L_ +∆ _[−]_ [∆] _[,]_ [ which gives]



∆ _[∗]_ = _−L_ + _√_


112



ˆ
_LDr._


(a)


(b)


Figure 3.3: Black Thursday in March 2020. (a) _∼_ 50% ETH price crash (image
from OnChainFX). (b) liquidation price effect on Dai DEX trades (image from
dai.stablecoin.science).


113


While we prove a stability result in this simplified setting, we believe the


results can be extended beyond the assumption of constant unit-elastic demand.

#### **3.4.1 Stability if leverage constraint is non-binding**


**Prop. 3.5.** _Assume wt_ _[D][A][t]_ [=] _[ D][ (DStablecoin dollar demand) and][ r][t]_ [= ˆ] _[r][ (speculator’s]_


_expected Ether return) remain constant. If the leverage constraint is inactive at time t,_



_then the DStablecoin return is_
_p_ _[D]_ _t_
=
_p_ _[D]_ _t−_ 1




~~�~~



_L_

_Dr_ ˆ _[.]_




[Link to Proof]


Supposing that _D ≈L_ (i.e., the previous price was close to the $1 target) and


the constraint is inactive, Prop. 3.5 tells us that the DStablecoin behaves stably


like the payment of a coupon on a bond.


Consider estimators for DStablecoin log returns ¯ _µt_ and volatility ¯ _σt_ com

puted in a similar way to Ether expectations in Eq. 3.2.2. When the leverage


constraint is non-binding, DStablecoin log returns remain ¯ _µt ≈_ 0, the contribu
tion to volatility at time _t_ is ln _p_ _[p][D]_ _t−t_ _[D]_ 1 _[−]_ _[µ]_ [¯] _[t][ ≈]_ [0][, and the DStablecoin tends toward]


a steady state with stable price and zero variability. The next theorem formal

izes this result to describe stable dynamics of price and the volatility estimator


under the condition that the system doesn’t breach the speculator’s leverage


threshold.


**Theorem 3.1.** _Assume wt_ _[D][A][t]_ [=] _[ D][ (DStablecoin demand) and][ r][t]_ [= ˆ] _[r][ (speculator’s]_


_expected Ether return) remain constant. Let L_ 0 = _D and_ ¯ _µ_ 0 _,_ ¯ _σ_ 0 _be given. If the leverage_


114


_constraint remains inactive through time t, then_



ˆ2 _[t]_ _−_ 1 ¯
_Lt_ = _Dr_ 2 ~~_[t]_~~ _,_ _µt_ =














¯
(1 _−_ _δ_ ) _[t]_ _µ_ 0 _−_ _δ_ [(][1] _[−][δ]_ _−_ [)] _[t][−]_ _−_ [2] _[−][t]_



2(1 _[−]_ _−δ_ _[−]_ ) _−_ 1 [ln ˆ] _[r,]_ _if δ ̸_ = 1 _/_ 2



2 _[−][t]_ [�] _µ_ ¯0 _−_ [1] 2




[1] 2 _[t]_ [ ln ˆ] _[r]_ _,_ _if δ_ = 1 _/_ 2

  


_σ_ ¯ _t_ [2] [=]














_t_ ¯

- _k_ =1 [(1] _[ −]_ _[δ]_ [)] _[t][−][k][δ]_ - (1 _−_ _δ_ ) _[k]_ _µ_ 0 _−_ [(][1] _[−][δ]_ [)] 2(1 _[k][−]_ _−_ [2] _[−]_ _δ_ _[k]_ ) _−_ [+1] 1 [(][1] _[−][δ]_ [)]



2
2 _[−][t]_ [ �] _[t]_ _k_ =1 [2] _[−][k][−]_ [1][�] ( _k/_ 2 _−_ 1) ln ˆ _r −_ _µ_ ¯0 + 2 _[−][t]_ _σ_ ¯0 [2] _[,]_ _δ_ = [1] 2

             


2
2(1 _[k][−]_ _−_ [2] _[−]_ _δ_ _[k]_ ) _−_ [+1] 1 [(][1] _[−][δ]_ [)] ln ˆ _r_ - + (1 _−_ _δ_ ) _[t]_ _σ_ ¯0 [2] _[,]_ _δ ̸_ = [1] 2



2



2



_Further, assuming the constraint continues to be inactive and that δ ≤_ [1] 2 _[, the system]_


_converges exponentially to the steady state Lt →Dr_ ˆ _,_ ¯ _µt →_ 0 _,_ ¯ _σt_ [2] _[→]_ [0] _[.]_


[Link to Proof]


Notice that if the leverage constraint in the system is reached, we can still


treat the system as a reset of ¯ _µ_ 0 and ¯ _σ_ 0 when we reach a point at which the


constraint is no longer binding. While the system subsequently remains without


a binding constraint, we again converge to a steady state starting from the new


initial conditions.


**Interest rates and trading below $1.** A consequence of Theorem 3.1 is that the


DStablecoin will trade below target during times in which Ether expectations


are high. This is empirically seen in Figure 3.2b. An interest rate charged to


speculators can balance the market (the ‘stability fee’ in Dai). This can temper


_r_
expectations by effectively reducing in Theorem 3.1. In the stable steady state,


setting the interest rate to offset the average expected ETH return will achieve


_r_
the price target. However, this is practically difficult as changes over time and


is difficult to measure accurately. It also depends on holding periods of specu

lators. It is an open question how to target these fees in a way that maintains


long-term stability.


115


#### **3.4.2 Instability if leverage constraint is binding**

When the speculator’s leverage constraint is binding, DStablecoin price behav

ior can be more extreme. We argue informally that this can lead to high volatil

ity in our model. The probability distribution for the leverage constraint to be


binding in the next step has a kink at the boundary of the leverage constraint. In


particular, it becomes increasingly likely that the leverage constraint is binding


in a subsequent step due to deleveraging effects described previously. Note that


feedback of large liquidations on Ether price, if added to the model, will add to


this effect.


We show such instability computationally in Figure 3.4a in simulation re

sults. In this figure, the shape of the inactive histogram reflects the specula

tor’s willingness to sell at a slight discount when the leverage constraint is non

binding due to the constant ˆ _r_ assumption.


We relax this assumption in Figure 3.4b, which shows the effects on volatil

ity of different speculator memory parameters. This figure is a heat map/2D


histogram. A histogram over _y_ - values is depicted in the third dimension (color:


_x_
light=high density, dark=low density) for each - value. Each histogram depicts


realized volatilities across 10k simulation paths using the simulation setup in

troduced in the next section and the given memory parameter ( _x_ - value). Hor

izontal lines depict selected percentiles in these histograms. The dotted line


depicts the historical level of Ether volatility for comparison.


In Figure 3.4b, volatility is bounded away from 0 even in non-binding lever

age constraint scenarios; the distance increases with the memory parameter.


_r_
This happens because updates faster with a higher memory parameter. As the


116


(a) Histogram of DStablecoin returns when leverage
constraint is binding vs. non-binding with constant

ˆ
_r_ .







(b) Heat map of volatility under different speculator
_γ_ = _δ_ memory parameters.


Figure 3.4: DStablecoin volatility, 10k simulation paths of length 1000.


speculator’s objective then changes at each step, the steady state itself changes.


Thus we expect some nonzero volatility, although it remains low in most cases.


In not-so-rare cases, however, volatility can be on the order of magnitude of


actual Ether volatility in these simulations. As seen in Figure 3.5, this result is


robust to a wide range of choices for the speculator’s risk constraint. This sug

gests that DStablecoins perform well in median cases, but are subject to heavy


tailed volatility.


117


#### **3.5 Simulation Results**

We now explore simulation results from the model considering a wide range of


choices for the speculator’s risk constraint. Unless otherwise noted, the simu

lations use the following parameter set with a simplified constant demand as

sumption ( _D_ = 100) and a t-distribution with df=3 to simulate Ether log returns.


This carries over the simplified model from Section 3.4, although other choices


are also amenable to simulation. Cryptocurrency returns are well known for


having very heavy tails. This choice gives us these heavy tails with finite vari

ance. Note, however, that this doesn’t capture path dependence of Ether re

turns. We instead assume Ether returns in each period are independent. We run


simulations on 10k paths of 1000 steps (days) each. This is enough time to look


at short-term failures and dynamics over time. The simulation code is available


[with full details at https://github.com/aklamun/Stablecoin_Deleve](https://github.com/aklamun/Stablecoin_Deleveraging)


[raging.](https://github.com/aklamun/Stablecoin_Deleveraging)


**Parameter** **Value** **Rationale**


_n_ 0 400 4x initial collateralization _>_ typical Dai level


_r_ 0 1 _._ 00583 Historical daily Ether mult. return 2017-2018


_µ_ 0 0 _._ 00162 Historical daily Ether log return 2017-2018


_σ_ 0 0 _._ 027925 Historical daily Ether volatility 2017-2018


_γ_ = _δ_ 0 _._ 1 _∼_ Recommended value [126]


_β_ 1 _._ 5 Threshold used in MakerDAO’s Dai


_α_ _∼_ 1 _._ 28 Value assuming normal distr. + _a_ = 0 _._ 1


_b_ 1 Consistent with VaR constraint


Note that our simulations study daily movements. We choose this time step


to examine these systems under reasonable computational requirements. More


118


realistic simulations might study intraday movements. One plausible scenario


- f a Dai freeze is if the price feed moves too far too fast instraday, so that spec

ulators don’t have enough time to react before liquidations are triggered and


keepers (who perform actual liquidations) are unable to handle the avalanche


- f liquidations. As the price feed in Dai faces an hourly delay in the price feed,


hourly time steps are a natural choice for follow-up simulations. This said, daily


time steps can actually be reasonable due to a behavioral trend in Dai data: most


Dai speculators realistically don’t track their positions with very high frequency


as supported by overall high liquidation rates.

#### **3.5.1 Speculator behavior affects volatility**


We compare DStablecoin performance under the following speculator behav

iors encoded in the risk constraint.


**Name** **Speculator risk constraint**


VaRN.1 VaR using _a_ = 0 _._ 1 + normality assumption


VaRN.01 VaR using _a_ = 0 _._ 01 + normality assumption


VaRM.1 VaR using _a_ = 0 _._ 1 + heavy-tailed assumption


VaRM.01 VaR using _a_ = 0 _._ 01 + heavy-tailed assumption


AC1 Anti-cyclic constraint, _b_ = _−_ 0 _._ 5, _α_ = 0 _._ 01


AC2 Anti-cyclic constraint, _b_ = _−_ 0 _._ 5, _α_ = 0 _._ 02


RN Risk neutral, only faces liquidation constraint


Figure 3.5 compares the effects on volatility of these behavioral constraints


under various Ether return distributions. These figures are heatmaps/2D his

tograms similar to that in Figure 3.4b. The results suggest that DStablecoins face


119


significant tail volatility (on the order of Ether volatility) even under compara

tively ‘nice’ assumptions on Ether return distributions, such as with significant


upward drift (Figure 3.5b) and a normal distribution (Figure 3.5c). Figure 3.7


depicts relative (% difference) mean-squared difference of simulated volatility


for the different risk management methods vs. a risk neutral speculator. The


mean-squared difference is large, suggesting that the speculator’s risk manage

ment method has a large effect on volatility.


The results suggest how speculator behavior can affect DStablecoin volatil

ity within the model. Stricter cyclic risk management (e.g., VaR) on the part


- f the (single) speculator can lead to increased DStablecoin volatility without


improving the safety of the system. Whether countercyclic (setting constraint


to increase leverage during downturns) or cyclic (setting constraint to decrease


leverage during downturns), the resulting DStablecoin volatility is connected


with how narrow the feasible region for the constraint becomes. A risk neutral


speculator, which has the widest feasible region for the constraint, leads to the


lowest volatility. Stricter risk management serves to reduce the feasible region.


Note that these results may be different if there are multiple types of specula

tors, for instance some that are cyclic and others that are countercyclic.


Figure 3.4b further suggests that a higher speculator memory parameter


(lower memory) tends to increase volatility in typical cases. This makes sense


as high memory parameters can lead to noise chasing on the part of the spec

ulator. Note that keeping the speculator’s expected Ether returns and variance


constant is equivalent to setting a static risk constraint.


120


|0.08|DStablecoin Volatility vs. Risk Management|Col3|
|---|---|---|
|0.03<br>0.04<br>0.05<br>0.06<br>0.07<br>0.08|<br>Ether volatility<br>70 percentile<br>95 percentile||
|VaRN.1<br>VaRN.01<br>VaRM.1<br>VaRM.01<br>AC1<br>AC2<br>RN<br>0.00<br>0.01<br>0.02|||








|( 0.08|(a) Ether returns∼t-distr(df = 3, µ = 0) DStablecoin Volatility vs. Risk Management|Col3|
|---|---|---|
|0.03<br>0.04<br>0.05<br>0.06<br>0.07<br>0.08|<br>Ether volatility<br>70 percentile<br>99 percentile||
|VaRN.1<br>VaRN.01<br>VaRM.1<br>VaRM.01<br>AC1<br>AC2<br>RN<br>0.00<br>0.01<br>0.02|||







|(b 0.08|b) Ether returns∼t-distr(df = 3, µ = r0) DStablecoin Volatility vs. Risk Management|Col3|
|---|---|---|
|0.03<br>0.04<br>0.05<br>0.06<br>0.07<br>0.08|<br>Ether volatility<br>70 percentile<br>95 percentile||
|VaRN.1<br>VaRN.01<br>VaRM.1<br>VaRM.01<br>AC1<br>AC2<br>RN<br>0.00<br>0.01<br>0.02|||


(c) Ether returns _∼_ normal( _µ_ = 0)


Figure 3.5: Heatmaps of DStablecoin volatility for different speculator risk management behaviors.


121


#### **3.5.2 Stable asset failure is dominated by collateral asset re-** **turns**

We define the DStablecoin’s **failure (or stopping) time** to be either (1) when the


speculator’s liquidation constraint is unachievable or (2) when the DStablecoin


price remains below $0.5 USD. In these cases, a global settlement would be rea

sonable, leaving DStablecoin holders with Ether holdings with high volatility in


subsequent periods.


Figure 3.6 compares the effects on failure time of these behavioral risk con

straints. The stopping time distributions appear comparable across a wide


range of selections for the speculator’s risk constraint. They are additionally


comparable across the memory parameters studied above. Figure 3.7 depicts


relative mean-squared difference of simulated stopping times for the different


risk management methods vs. a risk neutral speculator. In calculating the mean

squared difference, we only include cases in which the failure is realized within


the simulation. The mean-squared difference is small (1-2 orders of magnitudes


smaller than for volatility), providing additional evidence that the stopping


time is largely independent of the speculator’s risk management. In particular,


a large proportion of failure events would not have been prevented by different


speculator risk management within the model.


DStablecoin failure probabilities appear to be dominated by Ether returns


as opposed to speculator behavior. The results suggest that DStablecoins may


not be long-term stable, even under comparatively ‘nice’ assumptions for Ether


return distributions. To avoid failure, they would essentially rely on more spec

ulator capital entering the system during downturns.


122


(a) Ether returns _∼_ t-distr(df = 3 _, µ_ = 0)









(b) Ether returns _∼_ normal( _µ_ = 0)


Figure 3.6: Heatmaps of DStablecoin failure times for different speculator risk
management behaviors.

#### **3.6 Stablecoin Attacks**


Attacking a DStablecoin is different than traditional currency attacks. The fo

cus is not on breaking the willingness of the central bank to maintain a peg. It


instead involves manipulating the interaction of agents. We show that stable

coin design can enable profitable trades against stability that attack the system.


These come from the existence of profitable trades around liquidations and the


ability of miners to reorder and censor transactions to extract value.


123


**100**


**10**


**1**


**0.1**



Simulation Mean-Squared Difference vs. Risk-Neutral


Vol, tdistr(μ=0)


Vol, tdistr(μ=r0)







Vol, normal(μ=0)


Stop, tdistr(μ=0)


Stop, tdistr(μ=r0)



**0.01**


Stop, normal(μ=0)


**0.001**


**VaRN.1** **VaRN.01** **VaRM.1** **VaRM.01** **AC1** **AC2**


Speculator Risk Management


Figure 3.7: Relative mean-squared difference (MSD) of simulated volatility and
stopping time for given speculator strategy vs. risk neutral strategy. Different
lines represent different output (volatility or stopping time) and different return
distribution assumptions for the simulations.

#### **3.6.1 Expanded Model: Adding an Attacker**


We consider an expanded model under the fixed outside demand setting of the


previous section. In the expansion, we consider an attacker, who can specula

tively enter/exit the DStablecoin market. The attacker can buy _δ_ dollar-value of


DStablecoin at some time _t_ with the goal of selling it at a later time _s_ for _δ_ + _ε_ .


These occurrences change the demand structure: _Dt_ = _D_ + _δ_, _Ds_ = _D −_ ( _δ_ + _ε_ ).

#### **3.6.2 Profitable bets on liquidations**


Table 3.2 illustrates an example scenario for a profitable bet on liquidations. The


attacker injects _δ_ = 1 in demand at _t_ = 1, which acquires 1 _._ 0008 DStablecoins at


124


_t_ _p_ _[E]_ _t_ _δ_ + _ε_ _Dt_ ∆ _t_ _Lt_ _p_ _[D]_ _t_ _nt_
0 85 100 100 _._ 583 0 _._ 994 1 _._ 8

1 85 +1 101 0 _._ 502 101 _._ 085 0 _._ 999 1 _._ 806

2 82 101 _−_ 8 _._ 716 92 _._ 369 1 _._ 093 1 _._ 690

3 82 _−_ 1 _._ 083 99 _._ 917 92 _._ 369 1 _._ 082 1 _._ 689


Table 3.2: Example scenario of a profitable bet on liquidations.


_p_ _[D]_ 1 [. In] _[ t]_ [ = 3][, after the liquidation, the attacker is then able to extract] _[ δ]_ [+] _[ε]_ [ = 1] _[.]_ [083]


from selling the DStablecoin. This yields a return of 8 _._ 3%. This is akin to a short


squeeze on existing speculators. It takes advantage of the fact that liquidations


- ccur at DStablecoin market rate, which in turn affects the market rate.


The attacker can do better by choosing _δ, ε_ to maximize _ε_ subject to _[δ]_ _p_ [+] _[D]_ 2 _[ϵ]_ _[≤]_ _pδ_ _[D]_ _o_ [.]


Choosing _δ_ = 4 _._ 5 _, ε_ = 0 _._ 59 (not optimal) yields a return of 13%. The attacker


could also spread out _δ_ - ver a longer period of time to achieve lower purchase


prices.


From a practical perspective, the optimization is sensitive to misestimation


- f demand elasticity. While Dai has hit prices as high as $1.37 historically


(source: coinmarketcap), it hasn’t typically reached prices above $1.09. Thus


smaller bets (relative to supply) may be safer. Regardless, these can be large


- pportunities in large systems. In addition, outside of this model, real imple

mentations create arbitrage of 5 _−_ 13% to automate liquidations.

#### **3.6.3 Attacks**


**Attack 1:** An attacker bets on an ETH decline and manipulates the market


to trigger and profit from spiraling liquidations. This uses the short squeeze

like trades in the previous example. It can also be supplemented with a bribe


125


to miners to freeze collateral top-ups. The attacker could also enter as a new


speculator at the high DStablecoin prices after the attack and thus leverage up


at a discount. Outside of the model, the attack may have a negative effect on


the long-term DStablecoin demand due to the induced volatility. This can be


further beneficial to the attacker, who can then also deleverage in the future at a


discount.


**Attack 2:** The attacker is also a miner and reorganizes the recent transaction


history (such as by initiating a fork) to be on the receiving end of arbitrage op

potunities from liquidations. For instance, following an ETH decline, the miner


could trigger and profit from spiraling liquidations. In a fork, the attacker cre

ates a new timeline that inherits the ETH price trajectory (via oracle transac

tions). The attacker can then censor speculator transactions (e.g., collateral top

ups) to trigger new liquidations and extract profit around all liquidations, which


are guaranteed in the timeline. If the stablecoin system is large, the miner ex

tractable value can be large (and is additive with other sources of extractable


value). This creates the perverse incentive for miners to perform this attack if


the attack rewards are greater than lost mining rewards. This is similar to the


time-bandit attack in [64].


In Attack 1, the attacker takes on market risk as the payoff relies on a future


ETH decline and liquidation. It is a speculative attack that can induce volatility


in the stablecoin. In Attack 2, the attacker’s payoffs are guaranteed if the attack


fork is successful. These payoffs incentivize blockchain consensus attack. A


possible equilibrium is for miners to collude and share this value.


These attacks occur in a permissionless setting, in which agents can en

126


ter/exit at any time with a degree of anonymity. While in traditional finance,


market manipulation rules can be enforced legally, in decentralized finance, en

forcement is only possible to the extent that it can be codified within the pro

tocol and incentive structure. We leave to future study a full exploration of


these incentive structures in a game theoretic setting based on foundations for


blockchain forking models set in, e.g., [33].


Since the initial release of this paper, this attack surface around stablecoin


liquidations was exploited in related ways to Attack 2. In Attack 2, a miner


reorganizes the recent history to extract profit from arbitrage opportunities from


liquidations. In reality on Black Thursday, mempool manipulation contributed


to the clearing of $8m of Dai liquidation auctions at near zero prices [36].


**Mitigations.** We discuss some preliminary ideas toward mitigating attack po

tential. Liquidations could be spread over a longer time period. This could


potentially lessen deleveraging spirals by smoothing demand and increase the


costs to a forking attack. However, it presents a trade-off in that slow liquida

tions come with higher risks to the stablecoin becoming under-collateralized.


We also suggest tying oracle prices and DEX transactions to recent block history


so that a reorganization attack can’t easily inherit price and exchange history.


Practically, however, this may be difficult to tune in a way that’s not disruptive


as small forks happen normally.


127


#### **3.7 Discussion**

In general, it is impossible to build a stablecoin without significant risks. As


speculators participate by making leveraged bets, there is always an undiversi

fiable cryptocurrency risk. However, a stablecoin can aim to be an effective store


- f value assuming the cryptocurrency market as a whole is not undermined.


In this case, it is _conceivable_ to sustain a dollar peg if the stablecoin survives


transitory extreme events. That is, to achieve long-term probabilistic stability, a


stablecoin should maintain a high probability of survival.


**Failure risks.** DStablecoins are complex systems with substantial failure risks.


Our model demonstrates that they can work well in mild settings, but may have


high volatility outside of these settings. As we explore in this paper, the market


can collapse due to feedback effects on liquidity and volatility from deleverag

ing effects during crises. These effects can exacerbate collateral drawdown. Sur

viving these events may rely on bringing in increasing amounts of new capital to


expand the DStablecoin supply during such crises. In these events speculators


may not always be willing and able to take these new risky positions. Indeed,


there are may examples of speculative markets drying up during extreme mar

ket movements. As we explore below, continued stability during these events


additionally relies on new capital entering the system _in a well-behaved manner_


as profitable attacks are possible.


As suggested by our simulations, stablecoin holders face the direct tail risk of


cryptocurrencies. If the market loses liquidity, there is no guarantee that forced


liquidation of speculators’ collateral will be possible within reasonable pricing


limits. Further, volatile cryptocurrency markets can, in unlikely events, move


128


too fast for speculators to adapt their positions. In these cases, stablecoin hold

ers can only truly rely on the cryptocurrency value from global settlement.


**Remark on oracle risks.** The DStablecoin design also relies on trusted oracles


to provide real world price data, which could be subject to manipulation. In


MakerDAO’s Dai, for instance, oracles are chosen by MKR token holders, who


vote on system parameters. This opens a potential 51% attack, in which enough


speculators buy up MKR tokens, change the system to use oracles that they ma

nipulate, and trigger global settlement at unfavorable rates to stablecoin holders


while pocketing the difference themselves when they recover their excess col

lateral. A hint of manipulation in oracles or large acquisitions of MKR could


potentially trigger market instability issues on its own.


Note that Dai has protections from oracle attacks. [9] First, there is a threshold


- f maximum price change and an hourly delay on new prices taking effect. This


means that emergency oracles have time to react to an attack. Second, at cur

rent prices 51% of MKR is substantially more expensive than the ETH collateral


supply. However, this second point does not have to be true in general–at least


unless Dai holders otherwise bid up the price of MKR for their own security.


The value of MKR is linked to expectations around Dai growth as fees paid in


the system are used to reduce MKR supply. At some point, the expectation may


not be enough to lift MKR value above collateral on its own. This raises the


question of whether fees should be used to reduce MKR supply at all. Alter

natively, MKR value could be completely based on the potential value of a 51%


attack, which may also grow with Dai growth, and the value of fees could be


9Though it is notable that most MKR is reputedly held by just a few individuals within the
MakerDAO team.


129


put to different uses, as we discuss further below.


**A good fee mechanism may quell deleveraging spirals.** Dai imposes fees on


speculators when they liquidate positions (e.g., liquidation penalty, stability fee,


penalty ratio). These can _amplify_ deleveraging effects by increasing delever

aging costs and disincentivizing new capital from entering the system during


crises. An alternative design with automatic counter-cyclic fees could enhance


stability by reducing feedback effects. For instance, fees could be collected while


the system is performing well, but these fees could be removed (or made nega

tive) automatically during liquidity crises in order to limit feedback effects and


remove disincentives to bringing new capital into the system.


Speculators in Dai can pay back liabilities at any time and come and go from


the system, which raises concerns about herd behavior in crises. A herd try

ing to deleverage can trigger a deleveraging spiral. Dynamic fees tuned to in

flow/outflow could additionally disincentivize herd behavior to deleverage at


the same time.


**An alternative ‘collateral of last resort’ idea in Dai.** In Dai, MKR serves a


certain ‘last resort’ role in addition to governance. If there is a collateral short

fall, then new MKR is minted and sold to cover Dai liabilities making up the


shortfall. This may not always be possible as the MKR market can similarly face


illiquidity and the market cap may not be high enough to cover shortfalls. In


some settings, MKR holders might actually have an incentive to trigger a global


settlement early before MKR would be inflated. A Dai shutdown would have


some effect on the price of MKR, but the cost may be small if MKR holders ex

pect a successful relaunch of Dai after the crisis. An early shutdown is not ideal


130


for Dai holders, as they will want to hold the stable asset for longer during ex

treme events. In addition to incentive alignment being unclear in MKR’s ‘last


resort’ role, the invocation of the role only helps cover the aftermath of a crisis


(an existing shortfall) as opposed to quelling the effects that cause the crises.


We propose an alternative ‘last resort’ role of governance tokens that instead


aims to quell deleveraging spirals. This could be achieved by automatically po

sitioning the MKR supply as system collateral against which Dai can be minted


to expand supply in crises. To illustrate, if there is a massive deleveraging by


speculators, leading to excess demand for Dai and an inflated Dai price, then


new Dai could be automatically minted against the MKR supply as collateral to


help balance the market. In this way, a deleveraging spiral is damped: should


a new wave of speculator deleveraging be triggered, it will not compound the


price effect from the past wave. System fee revenue could also be put to this


use.


**Uses of limited fee revenue.** Dai produces limited fee revenue, most of which


rewards MKR investors. There is additionally a Dai savings rate that rewards


Dai holders using fee revenue and serves as another tool to balance the Dai


market (e.g., to boost demand for Dai when the price is below target). There


is an inherent trade-off in using fee revenue, however. A Dai savings rate uses


this revenue to improve stability in relatively normal settings in which a higher


fee itself serves to balance the market. Alternatively, fee revenue can be chan

neled to an emergency fund that lessens the severity of crises–for instance as


suggested above. These fees and their potential uses can be incorporated into


- ur model to compare the effects of different design choices.


131


**Stablecoin risk tools.** Our results suggest tools and indicators that can warn


about volatility in DStablecoins. We can find proxies for the free supply, esti

mate the price impact of liquidations, and track the entrance of new capital into


speculative positions. We can connect this information with model results to


estimate the probability of liquidity problems given the current state. This in

formation is also useful in valuing token positions in these systems (e.g., Dai,


MKR, and the speculator’s leveraged position).


Some exchanges have bundled select stablecoins into a single market that en

sures 1-to-1 trading (e.g., [96]). In this case, exchanges are essentially providing


insurance to their users against stablecoin failures. These arrangements could


lead to a run on exchanges in the event that some stablecoins fail. It is unclear


if these exchanges are subject to regulation to protect users against this, and it


is further unclear if such regulations would be sufficient to account for risks in


stablecoins. Our model provides insight into the risks (to exchanges and users)


if such arrangements in the future include non-custodial stablecoins.


**Future directions.** We suggest expansions to our model to explore wider set

tings.


  - Incorporate more speculator decisions, such as locking and unlocking col

lateral and holding different assets, accommodating speculators with se

curity lending motivation. This makes the speculator’s optimization prob

lem multi-dimensional. In this expanded setting, speculators may make


more long-term strategic decisions considering whether tomorrow they


would have to buy back stablecoins and at what price.


  - Consider multiple speculators with different utility functions who partic

132


ipate in the DStablecoin market. In this expanded setting, we can con

sider the conditions under which new capital may enter the system and


formally study the economic attack described above and the effects of ex

ternal incentives.


  - Incorporate additional assets, such as a custodial stablecoin that faces


counterparty risk. This would allow us to study long-term movements be

tween stablecoins in the space and learn about systemic effects that could


be triggered by counterparty failures. This is further relevant in evaluat

ing systems like Maker’s multi-collateral Dai. However, this comes with a


trade-off of a new counterparty risk that is very hard to measure. In partic

ular, it’s not just custodian default risk, but also risk of targeted interven

tions on centralized assets. Such interventions (e.g., from a government


who wants to shut down Dai) could be highly correlated with cryptocur

rency downturns as that is when the system is naturally weakest.


  - Incorporate endogenous feedback of liquidations on Ether price, which


becomes relevant if the DStablecoin system becomes large relative to the


Ether market. This is similarly important for _endogenous collateral_ stable

coins like Synthetix sUSD and Terra UST, in which a system equity-like


asset is used as collateral (see [110]).


Additionally, our existing model can be adapted to analyze DStablecoins with


different design characteristics. For instance,


  - DStablecoins with more general collateral settlement, in which stablecoin


holders can individually redeem stablecoins for collateral. This is possi

ble, for instance, in bitUSD and Steem Dollars, and more recently in Celo


Dollars. In this case, the stablecoin acts as a perpetual option to redeem


133


collateral, and stablecoin volatility will be additionally related to the set

tlement terms.


  - DStablecoins without speculator agents (e.g., Steem Dollars, in which the


whole marketcap of Steem acts as collateral, or Celo Dollars, in which Celo


reserves act as collateral). In these systems, stablecoin issuance is auto

mated with the rest of the protocol. Our model can be adapted by remov

ing speculator decisions and modeling the growth of collateral from block


rewards and growth of stablecoin from other processes.


  - Some non-collateralized algorithmic stablecoins. We believe this setting


can also be interpreted in our model by thinking of _implicit collateral_ that


ends up describing user faith in the system (see [110]). The underlying


mechanics would be similar, simply recreating ‘out of thin air’ the value


   - f the underlying asset as opposed to building on top of the value of an


existing asset. The stability of the system ultimately still relies on how


people perceive this value over time similarly to how perceived value of


Ether changes.


**Acknowledgements** We thank David Easley, Steffen Schuldenzucker, Christo

pher Chen, Akaki Mamageishvili, Peter Zimmerman, Sergey Ivliev, Tomasz


Stanczak, Sid Shekhar, as well as the participants of the ECB P2P Financial Sys

tems (2019) workshop, Crypto Valley Conference (2019), and Crytpo Economics


Security Conference (2019) for their valuable feedback. This paper is based on


work supported by NSF CAREER award #1653354. AK thanks Lykke, Binance,


and Amherst College for additional financial support.


134


#### **3.8 Appendix: Derivation of Results**

**Prop. 3.1**


_Proof._ In each period _t_, we determine the leverage constraint by setting _λ_ [˜] = _λ_


and solving for ∆. Using the formulation of _p_ _[D]_ _t_ [from the market clearing, we]


∆:
have the following equation for



˜ _x_
_λ_ _z_ + ∆

 - ∆ _−_ _y_



= _β_ ( _L_ + ∆) _._




Given ∆ _> y_, this transforms to the quadratic equation for ∆


˜

_−β_ ∆ [2] + ∆ _λ_ ( _z_ + _x_ ) _−_ _β_ ( _L −_ _y_ ) _−_ _λzy_ [˜] + _βLy_ = 0 _._

         -          

This is a downward facing parabola. The speculator’s leverage constraint is


satisfied when the polynomial is positive. The roots, if real, bound the feasible


region of the speculator’s constraint. Due to the requirement that ∆ _> y_, the


feasible set is given by [∆min _,_ ∆max] _∩_ ( _y, ∞_ ). When there are no real roots, the


polynomial is never positive, and so the constraint is unachievable.


**Prop. 3.2**


_Proof._ By Prop. 3.1, [∆min _,_ ∆max] _∩_ ( _y, ∞_ ) is indeed the feasible region. Incorpo

135


rating the market clearing, the speculator decides ∆ in each period _t_ by solving


_̸_



_x_
max _r_ _z_ + ∆

   - ∆ _−_ _y_


_̸_




_−L −_ ∆



_̸_



s.t. ∆ _∈_ [∆min _,_ ∆max] _∩_ ( _y, ∞_ )


This optimization is solvable in closed form by maximizing over critical


points. Maximizing the objective is equivalent to maximizing


_x_
_f_ (∆) = _r_ ∆∆ _−_ _y_ _[−]_ [∆] _[.]_


We first consider the case of ∆ approaching _y_ from above and show that this


boundary is not relevant in the maximization. The limit is


lim
∆ _→y_ [+] _[ f]_ [(∆) =] _[ −∞][.]_


¯
To see this, note that _Lt−_ 1 = _mt−_ 1 _≥_ _wt_ _[D][m]_ [¯] _[t][−]_ [1][, and so in order to have] _[ L][t]_ [=]


_wt_ _[D][m]_ [¯] _[t][−]_ [1][, we must have][ ∆] _[<]_ [ 0][. Thus the sign of the term that tends to infinity]


_−∞_
is negative. The limit is because the price for the speculator to buy back


_∞_ .
DStablecoins goes to


To find the critical points of _f_, we set the derivative equal to zero:


_df_ _[y]_ [(] _[rx]_ [ +] _[y]_ [)]

= 0

_d_ ∆ [=] _[ −]_ [∆][2] _[ −]_ [2∆] (∆ _[y]_ [ +] _−_ _y_ ) [2]


Assuming ∆ = _̸_ _y_, the solutions are the roots to the quadratic ∆ [2] + _−_ 2 _y_ ∆+ _y_ ( _rx_ +


_y_ ) = 0. Notice that the axis of this parabola is at ∆= _y_ . When there are two


real solutions, then exactly one of them will be _> y_ . Given _y ≤_ 0 and _x ≥_ 0 and


noting _r ≥_ 0, a real solution always exists and the relevant critical point is


∆ _[∗]_ = _y_ + _[√]_ _−yrx._


136


If it is feasible, ∆ _[∗]_ is the solution to the speculator’s optimization problem.


If ∆ _[∗]_ is not feasible, then we need to choose along the boundary. The possible


cases are as follows.


Suppose ∆ _[∗]_ _<_ ∆min. Then ∆min is feasible since ∆ _[∗]_ _> y_ implies ∆min _> y_ .


Since _f_ is monotone decreasing to the right of ∆ _[∗]_, _f_ (∆min) _> f_ (∆max), and so


∆min is the solution.


Suppose ∆ _[∗]_ _>_ ∆max. By our assumption that the constraint is feasible, we


have that ∆max is feasible. Since _f_ is monotone decreasing to the left of ∆ _[∗]_ - n


the feasible region, _f_ (∆max) _> f_ (∆min), and so ∆max is the solution.


**Prop. 3.3**


_Proof._ The speculator’s leverage constraint is unachievable when the quadratic


has no real solutions or when all real solutions are _< y_ . The first case occurs


when

˜ 2
_λ_ ( _z_ + _x_ ) _−_ _β_ ( _L −_ _y_ ) + 4 _β_ ( _−λzy_ [˜] + _βLy_ ) _<_ 0 _._

      -       

Noting that _y_ = _−w_ _[D]_ _L_ and _L−y_ = _L_ (2 _−w_ _[D]_ ) and expanding and simplifying


terms yields


˜ 2
_βλ_ [˜] _L_ 2 _zw_ _[D]_ + 2 _x_ (2 _−_ _w_ _[D]_ ) _−_ ( _βLw_ _[D]_ ) [2] _>_ _λ_ ( _x_ + _z_ )

       -       -       -       

Completing the square by subtracting 4 _βλ_ [˜] _Lx_ (1 _−_ _w_ _[D]_ ) from each side then gives


the result.


137


**Prop. 3.4**


_x_ _z_
_Proof._ Setting _z_ = _−_ ∆ _p_ _[D]_ _t_ [=] _[ −]_ [∆] ∆ _−y_ [gives the lower bound][ ∆] _[−]_ [:=] _z_ + _x_ _[y > y]_ [.]


Note that ¯ _mt_ = _Lt_, and so _y_ = _L_ ( _w_ _[D]_ _−_ 1) = _−w_ _[E]_ _L ≤_ 0 _._ The term _wt_ _[D][m]_ [¯] _[t][−]_ [1]


presents a lower bound on the size of the DStablecoin market in the next step


from the demand side, and so the speculator can’t decrease the size of the mar

ket faster than _y_, even with additional capital beyond _z_ . As shown above,


∆ _→_ _y_ [+] coincides with _p_ _[D]_ _t_ _→∞_ . The speculator pays increasingly large


amounts to buy back more DStablecoins as liquidity dries in the market.


**Prop. 3.5**



_Proof._ With inactive constraint, _Lt_ = _√_



ˆ _D_
_LDr_, _p_ _[D]_ _t_ = ~~_√_~~ _LDr_ ˆ = ~~�~~



_D_
_Lr_ ˆ [, and]



_D_

_p_ _[D]_ _t_ _√DLr_ ˆ =
_p_ _[D]_ _t−_ 1 [=] _L_ ~~�~~


**Theorem 3.1**



_L_

_Dr_ ˆ _[.]_



ˆ2 _[t]_ _−_ 1
_Proof._ It is straightforward to verify _Lt_ = _Dr_ 2 ~~_[t]_~~



ˆ
_Proof._ It is straightforward to verify _Lt_ = _Dr_ 2 ~~_[t]_~~ by induction using _Lt_ =


ˆ

- _Lt−_ 1 _Dr_ . Then



ˆ
_Lt−_ 1 _Dr_ . Then



2 _[t][−]_ [1] _−_ 1 _−_ 1

2 ~~_[t][−]_~~ ~~[1]~~

   


= ˆ _r_ _[−]_ [2] _[−][t]_ _._



_p_ _[D]_ _t_
=
_p_ _[D]_ _t−_ 1




~~�~~



_Lt−_ 1

_Dr_ ˆ [=]




~~�~~



ˆ2 _[t][−]_ [1] _−_ 1
_Dr_ 2 ~~_[t][−]_~~ ~~[1]~~



_Dr_ ˆ = ˆ _r_



2 ~~_[t][−]_~~ ~~[1]~~



1

2

 


And so ln _[p]_ _t_ _[D]_
_p_ _[D]_ _t−_ 1 [=] _[ −]_ [2] _[−][t]_ [ ln ˆ] _[r]_ [.]



138


Next, as ¯ _µt_ = (1 _−δ_ )¯ _µt−_ 1 + _δ_ ln _p_ _[p][D]_ _t−t_ _[D]_ 1 [, it is straightforward to verify by induction]


that



¯ ¯
_µt_ = (1 _−_ _δ_ ) _[t]_ _µ_ 0 _−_ _δ_ ln ˆ _r_


**Case I:** _δ_ = 1 _/_ 2. The series in ¯ _µt_ becomes



_t_

- 2 _[−][k]_ (1 _−_ _δ_ ) _[t][−][k]_ _._


_k_ =1



_t_

- 2 _[−][k]_ (1 _−_ _δ_ ) _[t][−][k]_ =


_k_ =1



_t_

- 2 _[−][k]_ 2 _[−]_ [(] _[t][−][k]_ [)] =


_k_ =1



_t_




2 _[−][t]_ = _[t]_

- 2

_k_ =1



2 _[t]_ _[.]_



Then we have ¯ _µt_ = 2 _[−][t]_ [�] _µ_ ¯0 _−_ 2 [1] _[t]_ [ ln ˆ] _[r]_ . The first term _→_ 0 since 0 _≤_ _δ <_ 1. The

             

second term _→_ 0 by L’Hopital’s rule. Thus ¯ _µt →_ 0 as _t →∞_ .


The contributing term to volatility at time _t_, after substituting and simplify

ing terms, is

ln _[p]_ _t_ _[D]_ _−_ _µ_ ¯ _t_ = _[t][/]_ [2] _[ −]_ [1] ln ˆ _r −_ 2 _[−][t]_ _µ_ ¯0 _._
_p_ _[D]_ _t−_ 1 2 _[t]_


Then DStablecoin volatility evolves according to


2
_σ_ ¯ _t_ [2] [= (1] _[ −]_ _[δ]_ [)¯] _[σ]_ _t_ [2] _−_ 1 [+] _[ δ]_ ln _[p]_ _t_ _[D]_ _−_ _µ_ ¯ _t_

             - _p_ _[D]_ _t−_ 1             


=


=


=



_t_

2

- _k_ =1(1 _−_ _δ_ ) _[t][−][k]_ _δ_ - ln _p_ _[p][D]_ _kk_ _[D]_ _−_ 1 _−_ _µ_ ¯ _k_ - + (1 _−_ _δ_ ) _[t]_ _σ_ ¯0 [2]



_t_

2

- 2 _[−]_ [(] _[t][−][k]_ [)] _δ_ 2 _[−]_ [2] _[k]_ [�] ( _k/_ 2 _−_ 1) ln ˆ _r −_ _µ_ ¯0� + 2 _[−][t]_ _σ_ ¯0 [2]

_k_ =1



_t_




2 _−_ 1 ln ˆ _r −_ 2 _[−][k]_ _µ_ ¯0 2 + 2 _[−][t]_ _σ_ ¯0 [2]

2 _[k]_ 


_k/_ 2 _−_ 1

- 2 _[−]_ [(] _[t][−][k]_ [)] _δ_ - 2 _[k]_

_k_ =1



_t_

2

= 2 _[−][t]_ - 2 _[−][k][−]_ [1][�] ( _k/_ 2 _−_ 1) ln ˆ _r −_ _µ_ ¯0� + 2 _[−][t]_ _σ_ ¯0 [2] _[.]_

_k_ =1



The second line follows from straightforward induction. As _t →∞_, the series


converges from exponential decay. Then both terms _→_ 0 because of the factor


- f 2 _[−][t]_ . Thus ¯ _σt_ [2] _[→]_ [0][.]


139


**Case II:** _δ ̸_ = 1 _/_ 2. The series in ¯ _µt_ is a geometric progression



_t_

- 2 _[−][k]_ (1 _−_ _δ_ ) _[t][−][k]_ =


_k_ =1



_t_ _−k_

- (1 _−_ _δ_ ) _[t]_ [�] 2(1 _−_ _δ_ )�

_k_ =1



(1 _−_ _δ_ ) _[t]_ [�] 2(1 _−_ _δ_ ) _[−]_ [1] _−_ 2 _[−][t][−]_ [1] (1 _−_ _δ_ ) _[−][t][−]_ [1][�]

=

1 _−_ 2(1 _−_ _δ_ ) _[−]_ [1]

= [(][1] _[ −]_ _[δ]_ [)] _[t][ −]_ [2] _[−][t]_

2(1 _−_ _δ_ ) _−_ 1


Then we have ¯ _µt_ = (1 _−_ _δ_ ) _[t]_ _µ_ ¯0 _−_ _δ_ [(][1] 2(1 _[−][δ]_ _−_ [)] _[t]_ _δ_ _[−]_ ) _−_ [2] _[−]_ 1 _[t]_ [ln ˆ] _[r]_ [, which converges to 0 as] _[ t][ →∞]_ [.]


The contributing term to volatility at time _t_, after substituting and simplify

ing terms, is


ln _[p]_ _t_ _[D]_ _−_ _µ_ ¯ _t_ = (1 _−_ _δ_ ) _[t]_ _µ_ ¯0 _−_ [(][1] _[ −]_ _[δ]_ [)] _[t][ −]_ [2] _[−][t]_ [+1][(][1] _[ −]_ _[δ]_ [)] ln ˆ _r._
_p_ _[D]_ _t−_ 1 2(1 _−_ _δ_ ) _−_ 1


The DStablecoin volatility evolves according to



_σ_ ¯ _t_ [2] [=]


=



_t_

2

- _k_ =1(1 _−_ _δ_ ) _[t][−][k]_ _δ_ - ln _p_ _[p][D]_ _kk_ _[D]_ _−_ 1 _−_ _µ_ ¯ _k_ - + (1 _−_ _δ_ ) _[t]_ _σ_ ¯0 [2]



_t_




¯

- _k_ =1(1 _−_ _δ_ ) _[t][−][k]_ _δ_ - (1 _−_ _δ_ ) _[k]_ _µ_ 0 _−_ [(][1] _[ −]_ _[δ]_ 2(1 [)] _[k][ −]_ _−_ [2] _δ_ _[−]_ ) _[k]_ _−_ [+1][(] 1 [1] _[ −]_ _[δ]_ [)]




[)] _[ −]_ [2] _[−]_ [(][1] _[ −]_ _[δ]_ [)] ln ˆ _r_ 2 + (1 _−_ _δ_ ) _[t]_ _σ_ ¯0 [2] _[.]_

2(1 _−_ _δ_ ) _−_ 1 


Note that because (1 _−_ _δ_ ) _≥_ 1 _/_ 2, we have


_|_ (1 _−_ _δ_ ) _[t]_ _−_ 2 _[−][t]_ [+1] (1 _−_ _δ_ ) _| ≤_ (1 _−_ _δ_ ) _[t]_ + 2 _[−][t]_ [+1] (1 _−_ _δ_ )


_≤_ 2(1 _−_ _δ_ ) _[t]_ _._


Thus we have



_t_
_σ_ ¯ _t_ [2] _[≤]_ [(1] _[ −]_ _[δ]_ [)] _[t]_ 

_k_ =1



_δ_

(1 _−_ _δ_ ) _[k]_



¯ 2(1 _−_ _δ_ ) _[k]_ 2 ¯
(1 _−_ _δ_ ) _[k]_ _µ_ 0 + + (1 _−_ _δ_ ) _[t]_ _σ_ 0 [2]

- 2(1 _−_ _δ_ ) _−_ 1 [ln ˆ] _[r]_ 


_t_

¯ 2 2 ¯

= (1 _−_ _δ_ ) _[t]_    - _k_ =1(1 _−_ _δ_ ) _[k]_ _δ_    - _µ_ 0 + 2(1 _−_ _δ_ ) _−_ 1 [ln ˆ] _[r]_    - + (1 _−_ _δ_ ) _[t]_ _σ_ 0 _[t]_ _[.]_


As _t →∞_, the series converges from exponential decay. Then both terms _→_ 0


because of the factor of (1 _−_ _δ_ ) _[t]_ . Thus ¯ _σt_ [2] _[→]_ [0][.]


140


CHAPTER 4


**STABLECOINS 2.0: ECONOMICS FOUNDATIONS AND RISK-BASED**


**MODELS**


The content of this chapter has previously appeared in:


“Stablecoins 2.0: Economics Foundations and Risk-Based Models.”


Ariah Klages-Mundt, Dominik Harz, Lewis Gudgeon, Jun-You Liu,


and Andreea Minca. _**Proceedings of the 2nd ACM Conference on Ad-**_


_**vances in Financial Technologies**_, 59-79, 2020.


141


Stablecoins are one of the most widely capitalized type of cryptocurrency.


However, their risks vary significantly according to their design and are often


poorly understood. We seek to provide a sound foundation for stablecoin the

- ry, with a risk-based functional characterization of the economic structure of


stablecoins. First, we match existing economic models to the disparate set of


custodial systems. Next, we characterize the unique risks that emerge in non

custodial stablecoins and develop a model framework that unifies existing mod

els from economics and computer science. We further discuss how this model

ing framework is applicable to a wide array of cryptoeconomic systems, includ

ing cross-chain protocols, collateralized lending, and decentralized exchanges.


These unique risks yield unanswered research questions that will form the crux


- f research in decentralized finance going forward.

#### **4.1 Introduction**


Stablecoins are cryptocurrencies with an added economic structure that aims to


stabilize their price and purchasing power. There are two classes of stablecoin:


custodial, which require trust in a third party, and non-custodial, which replace


this trust with economic mechanisms. Major custodial examples such as Tether,


Binance USD, USDC, and TrueUSD have a combined market capitalization of


- ver USD 10bn. On the non-custodial side, of the USD 1bn of value locked in


so-called Decentralized Finance (DeFi) protocols, more than 50% are allocated


to Maker’s Dai stablecoin.


Several recent papers and industry reports provide overviews of stablecoins


[44, 159, 143, 35, 167]. These typically categorize stablecoins based on the type


142


- f collateral used, peg target, and technological mechanics (e.g., on-chain, off

chain, algorithmic) and informally relate stablecoin mechanisms to traditional


monetary tools (e.g., interest rates). The history of money and stablecoins, and


the institutional structures of stablecoins are discussed in [123]. The regulatory


perspective of stablecoins, including classification, regulatory gaps, and sys

temic stability risks are discussed in [3].


In this paper our fundamental aim is different. Market events have demon

strated that even stablecoins—supposedly price stable—can exhibit significant


volatility. On the 12th March 2020, amidst the SARS-COV-2 pandemic, market


volatility affected the stablecoin Dai [134] so severely that it entered a defla

tionary deleveraging spiral, forcing it to deviate from its peg. While the afore

mentioned papers observe and categorize _existing_ stablecoin designs, none of


the works develop risk-based models of a broad design space of _possible_ choices


and their fundamental trade-offs. Here we seek to fill this gap, providing sound


economic foundations to inform stablecoin design, focusing on financial risk.


As such, the work is intended to serve as a “manual” for future stablecoin re

search.


Firstly, we provide an overview of the relevant risk-based models from eco

nomics and computer science, seeking to avoid duplication of work by only ex

tending models where necessary. Secondly, we provide a number of formalized


- pen questions drawing on capital structure theory. Throughout we assume


that stablecoin systems are used and operated by economically rational agents


whose actions ultimately determine the stability and security of these systems.


However, we do not solve the stated open problems in the context of this paper.


This work builds on the previous attacks on decentralized stablecoins identified


143


Implicit Collateral


Endogenous Collateral


Exogenous Collateral


Reserve Fund
Money Market Fund

|Col1|E|
|---|---|
|||


Fractional Reserve Fund


Bank Fund

Central Bank



**Stablecoin**



Non-Custodial


Custodial


|Col1|N|
|---|---|
||N|
|||


|Col1|Mon|
|---|---|
||o|
|||


|Col1|Fract|
|---|---|
|||



Figure 4.1: Risk-based overview of stablecoin design space.


in [112].


We uncover five central dimensions of risks. In non-custodial stablecoins:


(1) effects from deleveraging-like processes on collateral-like assets and risk in


underlying collateral-like thing (as discussed, e.g., in [112, 114]), (2) data feed


and governance risks, (3) base layer risks from mining incentives, and (4) smart


contract coding risks, on which the formal verification literature can be applied.


In contrast, in custodial stablecoins, the first applies in a very different way


to affect issuer incentives as well as an additional central risk dimension of (5)


censorship and counterparty risk. Our stablecoin mechanism categorization de

composes the design space according to these dimensions of risk. Figure 4.1


summarizes our categorization along some of the most important dimensions


- f risk.

#### **Contributions**


  - We provide a functional breakdown of custodial stablecoin designs with


a correspondence to taxonomy and models for traditional financial instru

ments (Section 4.2).


144


  - We provide a common functional framework for relating the economic


mechanics of all non-custodial stablecoin designs and a discussion of new


risks that emerge in this setting (Section 4.3).


  - We provide questions of economic stability and security that apply in eval

uating non-custodial stablecoins (Section 4.3).


  - We provide a framework of models toward measuring stability and se

curity including open research questions based on agents’ decisions (Sec

tion 4.4).


  - We provide methods for estimating agents’ preferences as represented by


utility functions, providing a minimal working example using historical


data from Maker (Section 4.4).


  - Last, we outline how our models can be applied to DeFi protocols includ

ing composite stablecoins, cross-chain and syntehtic assets as well as lend

ing protocols and decentralized exchanges (Section 4.5).

#### **4.2 Custodial Stablecoins**


In custodial stablecoins, custodians are entrusted with off-chain collateral as

sets, such as fiat currencies, bonds, or commodities. An issuer (possibly the


same entity) then offers digital tokens to represent an on-chain version of a re

serve asset (e.g., USD). Holders of the digital token have some form of claim


against the custodial assets, which maintains the peg. The custodial assets in

clude _reserve assets_, which are what the stablecoin is pegged against (e.g., USD),


and _capital assets_, which are other assets that back stablecoin supply. Capital as

sets are comparable to illiquid assets held by a bank and short-term treasuries


145


held by money market funds.


Custodial stablecoins introduce coin holders to _counterparty_ and _censorship_


risks related to the off-chain assets and _economic_ risks of the capital assets. These


risks are similar to risks in traditional assets. Counterparty risks may be height

ened due to the shared account structure with the custodian and lack of govern

ment deposit insurance. In the event that the central entities are unable to fulfill


their obligations (e.g., the result of fraud, mismanagement, theft, or government


seizure), the stablecoin value can go to zero. Table 4.1 summarizes categories,


applicable models, and projects.

#### **4.2.1 Reserve Fund = 100% reserve off-chain**


In Reserve Fund stablecoins, the stablecoin maintains a 100% reserve ratio–i.e.,


each stablecoin is backed by a unit of the reserve asset (e.g., 1 USD) held by the


custodian. The price target is maintained via two mechanisms. Coins may be


directly redeemable off-chain for the underlying reserve asset. In this case, arbi

trage trades incentivize external actors to close any price deviations that occur.


Alternatively, the issuer may designate ‘authorized participants’ (possibly the


issuer itself) who alone have the ability to create and redeem stablecoins against


the reserve. In this case, the authorized participants capture price deviation


arbitrage.


Reserve Fund stablecoins resemble the structures of e-money, narrow banks,


and currency boards. E-money is a prepaid bearer instrument. Deposits at a nar

row bank are backed by 100% reserves held at a central bank. A currency board


maintains a fixed exchange rate of a sovereign currency using 100% reserves


146


in a foreign currency (e.g., the Hong Kong Dollar maintains a USD peg using


USD reserves). Of these, the Reserve Fund stablecoin most closely mirrors the


currency board as the market price of the stablecoin floats subject to creation


and redemption similarly to how the sovereign currency floats subject to cre

ation and redemption of the currency board. On the other hand, e-money and


narrow bank deposits are treated identically with the currency itself. Notably,


unlike the currency board, the stablecoin reserves may be stored in commercial


bank deposit accounts, which may bear bank run risks. We discuss approaches


to modeling Reserve Fund stablecoins in Appendix 4.7.2.

#### **4.2.2 Fractional Reserve Fund**


A Fractional Reserve Fund stablecoin is backed by a mixture of reserve assets


and other capital assets, and has a target price. The fund holds reserves in a


target asset (or other highly liquid stable assets) that account for _<_ 100% of the


stablecoin supply in order to facilitate stablecoin redemptions. Similar to the


Reserve Fund design, these reserve assets may resemble commercial bank de

posits which exceed the government deposit insurance level, in which case they


may take on commercial bank run risk. The other capital assets account for the


remaining stablecoin supply value and earn a higher interest rate for the stable

coin issuer. The capital assets can be liquidated to handle additional stablecoin


redemptions, but are subject to price risk. Within this class, the important di

viding point is the type of capital assets held: illiquid assets (similar to a com

mercial bank) or low-risk assets (similar to a money market fund). In either


case, the stablecoin has a floating price, and so the peg is maintained through


similar ETF arbitrage trades involving fund redemptions. Thus applicable risk


147


models would take the form of ETF models in serial with bank run or money


market models, which we discuss next. We provide further detail on each type


- f stablecoin in Appendix 4.7.3.

#### **4.2.3 Central Bank Digital Currency**


Central Bank Digital Currency (CBDC) is a consumer-facing fiat digital currency


that aims to provide a risk-free store of value. CBDC proposes a different mone

tary system to the status quo. Currently, central bank reserve deposits are avail

able to commercial banks, but not to consumers or non-bank businesses. Con

sumers and businesses hold commercial bank accounts. The non-cash money


supply is determined by the lending of commercial banks (see [140]). The gov

ernment intervenes in this monetary system to create risk-free consumer deposit


accounts by providing commercial bank deposit insurance. Instead, CBDC pro

vides consumer-facing deposits at the central bank. [1]


CBDC represents a change in the structure of money deposits within the


banking system and not a change in the currency stability model itself. In fact,


CBDC is in many ways a more ideal setting for existing currency models as it


is closer in form to fiat than commercial bank deposits. Traditional currency


models like [144] and [89] apply to understand the stability of fiat currencies.


These models typically assume that the central bank/government is stability

seeking for its own sake as opposed to private banks discussed above, which


are profit-seeking. A fiat currency is assumed to have the backing of a given


country’s economy, which provides a natural demand from economic activity


1See [17] for a discussion on design and architecture of CBDC. The version comparable to
stablecoins is the token-based design.


148


in the currency, as well as military power and legal system. Given this setting,


agents in these models hedge their current positions to account for demand


in a next period, some of which occurs in the fiat currency and other of which


- ccurs in a foreign currency, under a potential currency attack from an attacking


agent. The ability to maintain a peg in this setting will depend on a relationship


between reserves held by the central bank and economic demand.


Research questions around CBDC focus on wider economic effects and indi

rect effects on stability, such as through commercial bank lending, credit avail

ability, and funding in the real economy. [26] models the effects of CBDC on


the wider economy through competition with commercial bank deposits. [152]


explores the effect of CBDC on commercial bank lending to the real economy


through a case study analysis of government subsidies.

#### **4.3 Non-custodial Stablecoins**


Non-custodial stablecoins aim to be independent of the societal institutions that


custodial designs rely on. They achieve this by establishing economic structure


between participants implemented through smart contracts. In this setting, di

rectly confiscating assets is prevented by the underlying blockchain mechanism.


Non-custodial stablecoins structurally resemble dynamic versions of risk


transfer instruments, such as collateralized debt obligations (CDO) and con

tracts for difference (CFD). [2] CDOs are backed by a pool of collateral assets and


sliced into tranches. Any losses are absorbed first by the junior tranche; a senior


2They also resemble perpetual swaps, which are relatively new products on cryptocurrency
exchanges.


149


tranche only absorbs losses if the junior tranche is wiped out.


Functionally, a non-custodial stablecoin system contains the following com

ponents in some form:


 - _Primary value_ : the economic structure of the base value in the stablecoin.


This is an abstracted concept of collateral with the following types: _exoge-_


_nous_ when the collateral has primary outside use cases, _endogenous_ when


the collateral is created for the purpose of being collateral, and _implicit_


when the design lacks explicit collateralization.


 - _Risk absorbers_ : speculative agents who absorb risk and profit in the system


_∼_
( the junior tranche of a CDO).


 - _Stablecoin holders_ : agents who make up the demand side of the stablecoin


_∼_
market ( senior tranche holder of a CDO).


 - _Issuance_ : a function performed by an agent or algorithm that determines


_∼_
stablecoin issuance ( how levered a CDO is), including a deleveraging


process to reduce stablecoin supply.


 - _Governance_ : a function performed by an agent or algorithm to manage sys

tem parameters, such as deleveraging factors and price feeds, and collects


_∼_
a fee on system operation ( an equity position in managing CDOs).


 - _Data feed_ : a function to import external asset data (e.g., exchange price of


assets in USD) into the blockchain virtual machine so that it is readable by


the system’s smart contracts.


 - _Miners_ : agents who decide the inclusion and ordering of actions in the


base blockchain layer (PoW or PoS).


150


The specific form of components may differ, but the general functions are uni

versal across stablecoin designs. Depending on the design, several functions


may be performed by a single agent type and others may be algorithmic. No

tice that the last three components can be simplified out of traditional financial


models because of legal protections; in traditional systems, we typically assume


these processes are mechanical as opposed to strategic actions. As a result, sta

blecoins are susceptible to new manipulation attacks around governance, price


feeds, and miner-extractable value (MEV).


**Analogy to traditional monetary system** We provide an illustration between


the Maker stablecoin system [3] and the traditional monetary system to aid the


reader in understanding the components and functional differences. In Maker,


_vaults_ absorb risk and perform issuance. Vaults deposit ETH collateral (primary


value), issue Dai secured against this collateral, and invest proceeds from Dai


issuance to achieve a leveraged position. The fiat system contains a central bank,


commercial bank, and depositors. The central bank regulates commercial banks


and holds bank currency reserves. Commercial banks decide the money supply


through lending. Depositors hold fiat currency accounts at commercial banks.


Maker vaults are parallel to commercial banks in that they both they de

cide money supply based on issuance incentives. For banks, this depends on


profitability of lending, which incorporates the spread between long-term and


short-term rates, subject to balance sheet and regulatory constraints and depos

itor withdrawal expectations. Vaults make a different bet collateral leverage. [4]


3The most capitalized non-custodial stablecoin system as of 10 June 2020.
4Commercial bank money supply is often described as a ‘money multiplier’ based on the
required reserve ratio. This is only accurate if we assume that banks lend the maximum allowed
by their constraints. This need not be the case that the optimal lending always has a binding
constraint. Similarly, vaults in Maker typically do not issue stablecoins to the maximum extent


151


Governance is parallel to the central bank. The central bank sets rates to tar

get economic stability and capital requirements for banks. Models typically as

sume the central bank mechanically targets stability by mandate. Stablecoin


governance takes a different form. Governance sets rates and collateral factors


to maximize system profits, which we hope to be aligned with stability. Stable

coin holders are parallel to depositors. Whereas bank depositors are guaranteed


deposit redemption, stablecoin holders may have no such guarantee. Instead,


they must hope that system incentives are aligned to make the stablecoin float

ing price stable and liquid.


A final useful parallel is in governance attacks. Through setting system pa

rameters, stablecoin governors could inherently steal the value locked in the


system, something we discuss in the context of models in the next section. A


parallel attack in the traditional monetary system would be an infinite printing


- f money by the central bank, to the benefit of the government.

#### **4.3.1 Primary Value**


The primary value is an abstract concept of collateral that is the basis for value


in the stablecoin system. It incorporates the value of collateral with explicit mar

ket prices and/or non-tokenized value ‘in the system’ coordinated among par

ticipants, which we term _implicit collateral_ . This primary value is derived from


market expectations in some system. For exogenous cryptocurrency collateral


(e.g., ETH), this is expectations and ‘confidence’ about Ethereum. In implicit


collateral, it is coordinated ‘confidence’ in the stablecoin system itself. In com

parison, in fiat currencies, this is confidence in a nation’s government, economy,


- f the collateral factor.


152


and legal system. In gold-backed currencies, it is confidence in gold. [5] In to

kenized assets, it may be confidence in the custodian and expectations about


cashflows of the underlying assets.


**Exogenous collateral** An exogenous collateral is an asset that has uses outside


- f the stablecoin system and for which only a small portion may be tied up in


collateral for the stablecoin. An example is ETH in Maker. Stablecoins are issued


against this collateral subject to a collateral factor that dictates the minimum


- ver-collateralization allowed in the system. From a model perspective, the


prices of exogenous collateral can be modeled exogenously.


**Endogenous collateral** An endogenous collateral is an asset created with the


purpose of being collateral for the stablecoin. This means that it has few, if


any, competing uses outside of the stablecoin system. Examples include SNX in


Synthetix (in which issuance is agent-based) and ‘shares’ in seigniorage shares


(in which issuance is algorithmic) [168]). In seigniorage shares, an ‘equity’-like


position insures the system against price risk, absorbing losses when stablecoin


demand is low and the supply needs to be contracted, and receiving newly


minted stablecoins when demand is high and the supply needs to be expanded.


6 The price of endogenous collateral cannot be modeled exogenously due to


endogenous feedback effects between stablecoin usage and collateral value. Its


value is derived from a self-fulfilling coordination of ‘confidence’ between its


5At some level, confidence in _something_ seems unavoidable as a source of value in a monetary
system.
6While, in general, seigniorage shares has a risk absorbing effect, extremes of the idea (Ampleforth) are really just a twist on a fixed supply cryptocurrency misinterpreted as a stablecoin.
Ampleforth transforms price volatility into supply volatility (e.g., daily stock splits) without
having an _economically_ stabilizing effect on purchasing power (though may have a _psychologi-_
_cal_ effect). Thus it can be interpreted as akin to seigniorage shares where all positions are the
‘shares’ and so in fact no positions are stabilized.


153


participants.


For instance, in a crisis of confidence, if expectations of stablecoin holder


demand are low, then the value of the endogenous collateral should be low,


which will further shake confidence in the system and demand. On the other


hand, high expectations can be self-fulfilling: with high collateral value, the


stablecoin is, in a sense, more secure. If stablecoin holder demand is high, then


a high price of the endogenous collateral can be justified.


The distinction between exogenous and endogenous collateral may be best


conceptualized as a spectrum. For instance, selected collateral has outside uses


but are significantly intertwined with the stablecoin (e.g., Steem Dollars) and


some stablecoins are backed by a collateral basket, including both exogenous


and endogenous collateral (e.g., Celo). From a model perspective, this spectrum


can be represented as the strength of these feedback effects.


**Implicit collateral** Some stablecoin designs do not have explicit collateral but


instead propose market mechanisms to dynamically adjust supply to stabilize


price. These designs work when speculators can be incentivized to absorb losses


when the supply needs to be decreased by the prospect for rewards when the


stablecoin supply needs to increase. We draw a parallel between the positions of


such speculators and the endogenous collateral case with important functional


differences. Both obtain value from self-fulfilling coordination of confidence


in the stablecoin from usage and speculative expectations between the partici

pants. Endogenous collateral represents the explicit tokenization of this, includ

ing obligation to absorb losses during supply decreases, which means it has a


directly observable market price. Implicit collateral is not explicitly tokenized


154


_and_ risk absorbers do not have direct obligations to absorb losses. For model

ing, implicit collateral can be interpreted like endogenous collateral behind-the

scenes and accounting for this difference in financial structure of risk absorbers.


The behind-the-scenes ‘market price’ of this coordination will only be indirectly


- bservable in the levels of stablecoin and speculative demand. However, they


will play a similar role to endogenous collateral in valuing both the speculative


and stablecoin positions. The stability of both endogenous and implicit collat

eral stablecoins will rely on how participants perceive and coordinate this value


- ver time.


One type includes Basis [6] and NuBits [120]. In these designs ‘shares’ are


awarded if stablecoin supply increases, but do not necessarily face direct losses


when supply contracts (but, of course, they do face indirect losses from the share


market price). Supply contraction relies on selling ‘bond’ positions to remove


stablecoins from circulation in return for future rewards when supply is next


increased. In Basis, this is algorithmic, whereas in NuBits, this is coordinated


through share voting (and a couple other stabilization mechanisms, including


share demurrage, are available for voters to choose from). If we tokenize an


- bligation to purchase ‘bonds’ during contractions and combine with ‘shares’


positions, then the result resembles seigniorage shares. As it is not tokenized


in this way, the equivalent of ‘collateral’ is only implicit with no observable


market price. Comparatively, seigniorage ‘shares’ ought to be valued differently


to be compensated for extra obligation. And downside price stabilization will


depend on incentives of risk absorbers at the time as opposed to in advance (see


[106] for a critique).


We refer to a second type as _miner-absorbed_ (e.g., [84]), which aims to stabi

155


lize the base asset of a blockchain by manipulating protocol incentives. These


designs propose for the supply to be dynamically adjusted by manipulating


mining rewards, mining difficulty, and the level and burning of transaction fees


- r interest charges. This means that miners take an implicit risk absorber po

sition that is meant to absorb price risk, but without an obligation to continue


mining/risk absorbing. In many ways, this parallels the Basis/Nubits design.


Miners are rewarded with newly minted stablecoins when the supply needs


to be increased and face slashed rewards and burned transaction fees if they


choose to continue mining when the supply needs to be reduced.

#### **4.3.2 Risk Absorption and Issuance**


The stablecoin mechanism works when speculators are incentivized to absorb


price risk. These risk absorbing positions have two primary forms. In _equity_


_risk absorption_, a secondary asset exists, and any holder of this asset implicitly


absorbs risk from the stablecoin. For instance, the Steem market cap implic

itly backs Steem Dollars; a Steem Dollars holder can redeem Steem Dollars for


newly minted Steem, and all Steem holders bear this inflation cost. In _agent risk_


_absorption_, individual agents manage a vault containing primary value that ab

sorbs stablecoin risk. In agent risk absorption, agents decide how much to par

ticipate with their asset whereas, in equity risk absorption, every holder of the


secondary asset participates proportionately. In many cases, the risk absorber


role is also combined with stablecoin issuance.


An issuance process determines the stablecoin supply. A lot of variation is


possible in the process specifics, but there are two general types. In _agent-based_


156


_issuance_, the size of the stablecoin supply, or more specifically the leverage of the


system (the size of the stablecoin supply relative to the collateral value), is de

cided by agents in the course of optimizing their positions. The deciding agents


are typically the risk absorbers in the system. For instance, in Maker, vaults de

termine their stablecoin issuance in managing the leverage of their vaults. In


NuBits, owners of ‘equity’-like shares collectively vote on issuance decisions to


balance demand.


In _algorithmic issuance_, a process to adjust leverage (relative supply) is cod

ified in the stablecoin protocol. For instance, in Duo Network, leverage is de

termined algorithmically through ‘leverage resets’, which balance the stable

coin supply relative to collateral value. In seigniorage shares, new issuance is


awarded algorithmically to ‘equity’ holders to balance demand.


A _deleveraging process_ is also part of issuance that can be invoked to reduce


the stablecoin supply if a deleveraging factor is breached, or if stablecoin hold

ers are allowed to redeem stablecoins for the collateral. For instance, in Maker,


if the stablecoin issuance of a vault is too large relative to the collateral value,


the collateral is liquidated to reduce leverage. In Duo Network, ‘leverage resets’


may force the liquidation of some positions if a collateral factor is breached. In


seigniorage shares, losses are born by ‘equity’ holders to reduce the stablecoin


supply in a demand shock. In Steem Dollars, if price is below target, stablecoin


holders may redeem for newly minted Steem.


As introduced in [112] and [114], non-custodial stablecoins based on lever

aged lending markets face deleveraging risks, which can cause feedback spirals


- n primary value. Most existing non-custodial stablecoins fit this leveraged


lending characterization. These deleveraging risks take two forms. The first is


157


a feedback effect on the stablecoin market: collateral value may be consumed


faster in liquidations due to drying of stablecoin liquidity. The cost of delever

aging in a crisis may be significantly higher than $1 per stablecoin due to this


effect, as predicted in [112] and validated in Maker during ‘Black Thursday’ in


March 2020. The second is a feedback effect directly on endogenous and im

plicit collaterals. For endogenous collateral, liquidations can cause a liquidity


and fire sale effect on the collateral asset market in addition to a feedback effect


- n reduced expectations.


A similar feedback occurs in implicit collateral and affects the risk absorbers’


positions and stablecoin demand. For both types of implicit collateral, there is


a ceiling on how much can be absorbed. For seigniorage shares, this is in de

murrage of equity holders. For miner-absorbed, this is likely around 0 block


reward, except possibly in staking systems in which stake can be slashed as de

murrage. The result is feedback in the participation incentives and value of the


risk absorbing position. For instance, for miners to be willing to continue min

ing without a mining reward, the expectations of future profit need to outweigh


the costs. A continued participation decision will depend on whether the in

vestment can be repurposed and potential returns from competing alternatives.


After this ceiling, the remaining flexibility is only in burning of fees charged in


stablecoin usage, which has a feedback effect on the attractiveness of holding


the stablecoins.


This leads to two universal and fundamental questions:


**Question 4.1** (Incentive Security) **.** Is there mutually profitable continued partic

ipation across all required parties?


If not, then the mechanism cannot work as no one will participate. This ques

158


tion also includes incentives around attacks; in particular, if incentives lead to


profitable attacks, then _rational_ agents will be less inclined to participate. After


this is answered, we can then make sense of the follow-up question:


**Question 4.2** (Economic Stability) **.** Do the incentives actually lead to stable out

comes?


Note that particular feedback effects can be mitigated. However, the result


is typically to shift the risk from one agent to another. In either case, the risk


will affect participation incentives. For instance, in collateral liquidations, some


stablecoin holders could be liquidated at par for the collateral asset as opposed


to at a floating market price. This eliminates the feedback effect on the stablecoin


market price, reducing deleveraging risk on risk absorbers. Instead, however,


the stablecoin may be less attractive to stablecoin holders as they now take on


more liquidation risk.


The type of stablecoin structure will also significantly affect incentives.


When designs are more agent-based, agents have greater decision flexibility and


are more likely to find a profitable participation level. In comparison, when de

signs are more algorithmic and/or with equity risk absorption, agents are more


restricted and may be less likely to participate in the system relative to alter

natives. [7] Several past stablecoin events serve as case studies for deleveraging


effects. These are described in Table 4.5 in the Appendix.


Stablecoins can also incorporate other insurance mechanisms to mitigate risk


(e.g., [155, 188, 147]). The simplest is creating a fully collateralized put option


7An interesting anecdote is the ‘miracle’ of the W¨orgl Experiment. In this experiment, currency demurrage is purported to stabilize the local economy in a depression by incentivizing
current spending. However, as discussed in [86], this ought to have an effect on participation
incentives, leading to a lower equilibrium price of the demurrage currency relative to alternatives.


159


market, from which individual stablecoin holders can purchase an option to


swap from this stablecoin to another stablecoin/asset. Naturally, this insurance


is only as valuable as the collateral behind it. Other insurance mechanisms add


a layer to the protocol intended to globally buffer against shortfalls—e.g., in


case the ‘dynamic’ part of the CDO structure fails to cover all losses. In some


cases, these can be interpreted as a ‘mezzanine’ tranche in the CDO-like struc

ture, though this is not completely accurate as this ‘tranche’ is often unsecured.


In particular, many current stablecoins generate cash flows from fees that are


securitized into governance tokens (e.g., MKR in Maker)). To cover a shortfall


situation, the value of future cash flows can be auctioned off by selling new gov

ernance tokens. However, the value of future cash flows can evaporate in death


spiral situations. Alternatively, a portion of past fees can be diverted to serve as


a buffer to cover shortfalls. There is in fact a spectrum between these options,


in which securitized cash flows can be sold at arbitrary times to maintain an


adequate buffer. [8]


**A design gap: buffers** This largely unexplored spectrum of options represents


a more general design gap: an under-appreciation of buffers in stablecoin de

sign. [114] shows that leveraged lending-based stablecoins can be stable in re

gions in which the underlying collateral price process is a submartingale (i.e.,


the next period expected return is positive) and can break down outside of this.


While there is some concern about the reasonableness of a submartingale as

sumption, it may be more reasonable in a relaxed form, in which downward


movements are transitory (or long-term expected return is positive). There is lit

tle that derivative design can do to help systems survive aside from transitory


8This can be interpreted similarly to corporate financing decisions around if/when to raise
capital vs. internally finance.


160


downside events. In this relaxed form, it is important that systems have ade

quate buffers so as to survive transitory events; we suggest that many concerns


about the appropriateness of submartingale assumptions can be translated to


concern about adequate buffer size. In this way, we expect an optimized buffer


design can extend regions of stability for stablecoins, whereas this is largely un

derexplored in current designs. [9] Another form of such a buffer is proposed in


[114]: vault insurance that can cushion the effects of deleveraging spirals.


We also suggest that well-designed buffers can expand design possibilities


beyond leveraged lending-based stablecoins. For instance, stablecoin designs


with different fundamentals based on money market fund and currency peg


models where the peg is maintained by an internal buffer effect. One exam

ple of these ideas is discussed more in the context of _composite_ stablecoins in


Section 4.5.2 and in [104, 109].

#### **4.3.3 Governance, Mining, and Manipulation**


We now introduce design components that introduce manipulation potential


in the system. In custodial systems, such manipulations are typically avoided


by relying on societal institutions. In contrast, permissionless systems usually


do not offer strong identities, which open up various anonymous attacks that


cannot be prevented by institutions. The precise form of these components af

fect the size and scope of attack vectors, but don’t substantially change their


form; thus we focus our discussion on the functional forms that are important


9For instance, Maker has a ‘system surplus’ account that served as a buffer during Black
Thursday. This was not in fact intended as a stability buffer and is typically used to accrue fees
until they reach a size for returning to ‘equity’ holders. Instead, Maker’s intended buffer is an
auction of MKR, arguably at the worst possible times, to cover shortfalls.


161


for economic models. We provide a list of historical manipulation events as case


studies in Table 4.7 in the Appendix.


**Data Feeds** Non-custodial stablecoins require asset price data in terms of the


target peg (e.g., ETH/USD prices). This data is not natively accessible on

chain since fiat-cryptocurrency conversions can only take place on off-chain ex

changes. As a result, the stablecoin relies on a mechanism to import this data


into the blockchain virtual machine so that it is readable by the stablecoin smart


contracts (also known as an ‘oracle’). As a result, the correctness of the im

ported data is not objectively verifiable on-chain, as opposed to native actions


such as intra-blockchain transaction validity or inter-blockchain transaction va

lidity [190]. There are various methods, both centralized and decentralized, to


construct such data feeds. We give a brief overview of these in the appendix.


Though, from a functional standpoint, we can abstract from the technical de

tails to focus on the economic structure that these data feeds add.


Data feeds introduce a new incentive problem: if importing data into the


system has an extractable value X, then an attacker will spend up to X to ma

nipulate that data. Centralized feeds can be manipulated by the counterparty,


which introduces potentially perverse incentives for the counterparty as well as


single points of failure. Decentralized methods typically collapse in the face of


game-theoretic attacks. As a result, data feeds add an inherent manipulation


potential into our general model. _The important factors of this include who can_


_manipulate the feed, how much the feed can be manipulated, and the cost involved in_


_such manipulation._ Given this, a reasonable aim is to achieve data feed incentive


compatibility to report honestly in the combined data feed-stablecoin system.


162


**Governance** Stablecoin governance is tasked with managing system param

eters, such as interest rates, collateral factors, data feed curation, time delays,


system upgrades, and emergency system settlement. In return, they typically


receive some fee revenue from the system. Governors may take the form of


governance token holders who vote on parameters, the founding company, a


subsumed role of other agents in the system, or may be algorithmic.


If it is performed by agents, then these agents have power to manipulate the


system through these parameters. For the system to be secure, governance must


be disincentivized from fatally attacking the system. The potential for prof

itable attacks will feedback into the participation decisions of the other agents


in the system. For instance, if governance is tokenized, then the token valua

tion/expectations, which could be slashed after an attack, and any other costs


must be sufficiently higher than the proceeds of the attack. We discuss several


attacks, involving manipulations of data feeds and parameters to extract collat

eral value, in the context of proposed models in the next section.


Governance is also inter-related with system stability. In this anonymous


setting, governance can be expected to maximize expected profits as opposed


to targeting stability for its own sake, as is typically assumed in central bank


models. It is an open question to what extent various governance structures


align incentives with the targeting of stability.


On the other hand, if governance is algorithmic, the stablecoin may be sus

ceptible to gaming attacks from the other participants. These attacks can take a


related form assuming the governance algorithm as given and construct simi

lar end results: e.g., bribe the chosen data feeds in order to extract system value.


Potential profitability of these attacks will feedback into participation incentives


163


- f the agents in the system.


**Miners** A non-custodial stablecoin is implemented in a base blockchain layer.


This can either be “on top” of a blockchain in the form of smart contracts or


directly into the core runtime. In either case, the base blockchain is maintained


by a set of miners. In this paper, we subsume both miners (typically used in the


context of PoW) and validators (typically used in PoS) under the term “miner”.


In maintaining the blockchain, miners decide transaction inclusion and order

ing in the ledger–both in the next block mined and in the previous blocks, as a


miner could always choose to re-mine an earlier block to change the transaction


structure. Hence, they have full control over the history of the ledger.


The blockchain system _intends_ for miners to ensure desired properties of per

sistence and liveness of the ledger [83]. In this context persistence states that a


valid transaction included in the ledger is eventually considered final, i.e., all


honest agents will report the transaction in the same position in the ledger. The


liveness property requires that a transaction sent from an honest agent is even

tually inserted into the ledger. In return, miners are paid a rewards in the form


- f fees for including transactions into blocks and block rewards for extending


the ledger with new blocks. Since present and future rewards are typically paid


- ut in the base asset, miners have an incentive to avoid attacks that jeopardize


these rewards.


However, miners can also receive payoffs from other sources outside of the


blockchain protocol. For instance, miners can capture arbitrage opportunities


in the exchange of assets on the ledger or by placing bets and manipulating the


- utcomes in the course of mining, or receiving bribes to do so on behalf of oth

164


ers [139]. This is broadly summarized as Miner Extractable Value (MEV) [64]. A


rational miner will decide profit-maximizing actions taking MEV into account,


which may not always be honest mining supporting the blockchain. If MEV is


valuable enough, miners will generally be incentivized to capture it through an


attack.


MEV poses a few risks in the context of stablecoins. First, specialized attacks


are possible that exploit stablecoin deleveraging events and liquidations [112].


This leads to MEV opportunities that can incentivize destabilizing attacks on the


stablecoin. Understanding security and incentive alignment in this context and


game theoretic interaction of many stablecoin agents and miners remain open


problems. Second, miner attacks pose consensus risk to the blockchain layer


(e.g., affecting persistence). An attack of this form could have an effect on the


base asset of the blockchain, which may be a collateral asset in the stablecoin.


This can have an effect on stablecoin stability even if the stablecoin itself is not


the focus of the attack. Third, in the case of stablecoins embedded in the base


protocol, the stablecoin may directly manipulate miner reward incentives, as


- pposed to indirectly manipulating incentives via MEV. This presents a related


- pen problem of whether such blockchains can function (e.g., whether liveness


is achievable).


**Miscellaneous risks** We briefly mention two other risks. One is often called


‘smart contract risk’. Since stablecoin systems execute algorithmically without


specific institutional oversight, they face the risk of bugs in their specification


and implementation–e.g., transaction-ordering dependencies, overflows, and


re-entrancy. These risks may be representable in similar ways to credit risk mod

els by introducing some probability of ‘default’, in this case a software bug, and


165


some random recovery ratio. Formal verification methods are typically used to


mitigate these risks. Another risk is contagion risk from other protocols. In real


environments, these systems do not occur in isolation. For instance, cascading


liquidations in ETH and BTC between multiple leverage platforms occurred on


‘Black Thursday’ in March 2020. We suggest that cascading liquidations like this


can be modeled using fire sale models of networks of common asset holdings


(e.g., [41]).

#### **4.4 Models and Measures of Non-Custodial Stablecoins**


Based on the novel risks in non-custodial stablecoins, existing financial mod

els cannot be used ‘out-of-the-box’. Here we introduce foundational models for


non-custodial stablecoins which adequately capture these risks. First, we draw


inspiration from capital structure models, extending a basic model to capture


additional aspects and formulate four formal examples of such problems. Sec

- nd, we consider forking models, moving from the single-shot nature of the


capital structure models we present to games of multiple rounds. Third, we


provide a brief review of models that focus on whether non-custodial incentive


structures can lead to stable price dynamics. Finally, we include an estimation


- f utility functions specifically for the Maker protocol.

#### **4.4.1 Capital Structure Models**


We draw inspiration from capital structure models ([74], [148]) to understand


incentives and attacks in stablecoins. The original formulation of these models


166


describe incentives in an IPO offering between equity holders, bond holders,


and managers. In the stablecoin adaptation, the model describes incentives be

_∼_
tween governors who hold governance tokens ( equity), stablecoin holders


_∼_ _∼_
( bond holders), and vaults/risk absorbers ( managers). We relate vaults to


managers as vaults decide the stablecoin supply.


We consider three assets: COL (collateral asset, e.g., ETH), GOV (governance


token), and STBL (stablecoin). In Problems 1-2, we consider vaults endowed


with COL, governors endowed with GOV, and stablecoin holders who purchase


STBL. In Problem 3, we consider a different formulation in which agents choose


portfolios of assets, including strategic holdings of GOV. We define the follow

ing model components


 - _N_ = dollar value of vault collateral (COL position)


 - _R_ = random return rate on COL


 - _F_ = total stablecoin issuance (debt face value)


 - _b_ = return rate on a new opportunity; vault issues stablecoins (raises debt)


to pursue this


 - _β_ = collateral factor


 - _δ_ = interest rate paid by vault to issue STBL


 - _u_
= vault’s utility from an outside COL opportunity


 - _U_ ( _·_ ) = stablecoin holder’s utility function


 - _B_ = STBL market price at issuance


 - _Pt_ = GOV market value at model time _t_ with terminal valuation parameter


_κ_ .


167


The model proceeds in three stages: (0) governance decides interest rate _δ_


(i.e., the contract with the vault), (1) vault decides stablecoin issuance lever

aged against a collateral position, and (2) the system is settled with an attack


- ccurring if profitable. In a simplest formulation, the vault and governance are


assumed to maximize expected value (risk neutral), and the stablecoin holder


has risk averse utility _U_ with unlimited demand depth at this utility, which we


later relax.


The three model stages lead to a sequence of GOV token prices [ _P_ 0 _, P_ 1 _, P_ 2].


In the simplest form, these represent discounted cash flows accruing to gov

ernance given the information at each time. Note that which _Pt_ appear in an


- ptimization problem will depend on the precise problem setting we model. _P_ 0


is the objective that governors optimize in period 0. _P_ 1 gives the GOV valuation


after vaults and stablecoin holders strategically participate in GOV ownership


(e.g., in Problem 3). _P_ 2 gives the GOV valuation at the end of the model. Con

ditioned on no attack taking place, _P_ 2 = _δF_ + _κ_, where _κ_ is a terminal valuation


parameter. If an attack occurs, then we assume participants abandon the system


yielding _P_ 2 = 0. The terminal valuation _κ_ represents the growth potential of the


stablecoin: for instance, if _F_ becomes large in the future, then GOV cashflows


_δF_ become large as well.


**Problem 1: Capital structure with no attack**


Problem 1 introduces a simple setup with no attacks. This resembles the classic


capital structure problem (and can be solved similarly to [74]) with a particular


form of contract between the equity and manager: now, vaults receive all profits


from leverage with an interest fee paid to governance. The governance choice


168


problem is to maximize the expected fee revenue subject to the vault’s stablecoin


issuance. The vault choice problem is to maximize expected returns from lever

age minus fees subject to these constraints: (1) the collateral constraint, (2) the


participation constraint, (3) stablecoin market price as the stablecoin holder’s


expected utility of holding one stablecoin.


Notice that, for simplicity, there are several limitations to the model as for

mulated. In a more complete model, the vault may account for collateral liq

uidation costs (as in [114]) and last-resort insurance roles of GOV to make up


for any collateral shortfalls (which can be accounted for by adding terms of


_−_ [ _F_ (1 + _δ_ ) _−_ _N_ (1 + _R_ )] [+] to the governance objective and modifying the sta

blecoin pricing constraint). Some stablecoins also include an interest rate paid


to or by stablecoin holders. Finally, notice that both the setups with sequen

tial choices by the vault and the governance as well as concurrent choices are


realistic.


**Problem 1** Ca ital structure with no attack vectors
p


**Governance choice**


max E _δF_ + _κ_
_δ∈_ [0 _,_ 1) ~~�~~ ~~�~~


s.t. _F_ is vault choice


**Vault choice**


max E[ _NR_ + _F_ ( _Bb −_ _δ_ )]
_F ≥_ 0


s.t. _F ≤_ _βN_


_u ≤_ E[ _NR_ + _F_ ( _Bb −_ _δ_ )]


1
_B_ = E _U_

                  -                   - _F_ [min(] _[F, N]_ [(1 +] _[ R]_ [)] _[ −]_ _[δF]_ [)]                   - �


169


**Problem 2: Capital structure with governance attack**


We consider a governance attack vector of the form described in [194] and [88].


In such an attack, an agent with a _ζ_ fraction of GOV tokens is able to steal _γ_


fraction of collateral in the system. As described in [194], this could occur in the


Maker system at the time with _ζ_ = 0 _._ 1 and _γ_ = 1 (or possibly _γ >_ 1 after ac

counting for simultaneous attack on other systems using the stablecoin) because


governance is granted the power to arbitrarily alter the contracts. [10]


This attack is profitable if the proceeds exceed the costs:


_γN_ (1 + _R_ ) _> ζ_ ( _δF_ + _κ_ ) + _α,_


where _α_ incorporates an outside cost to attack and _ζ_ ( _δF_ + _κ_ ) is the opportunity


cost of attack (the value of _ζ_ fraction of GOV tokens). Note that in traditional


financial settings, we typically have _α >> γN_ : _α_ represents a high cost due


to legal/reputational recourse. This simplifies the problem to Problem 1 as the


attack is always unprofitable.


In the Problem 2 setting, the governors split into two groups: attack and


_α_
non-attack groups. If we think of individual governors having individual


costs to attack, then the attack group will form from the _ζ_ fraction with lowest


_α_ . If we take _ζ <_ 0 _._ 5, then the non-attack group will decide interest rate _δ_


while the attack group will decide _d ∈{_ 0 _,_ 1 _}_ whether to attack. If _ζ >_ 0 _._ 5, then


the attack group decides both _δ_ and _d_ . Problem 2 models the case of _ζ <_ 0 _._ 5:


the governance choice problem represents the non-attack group decision over


_δ_, and the attack group decision is represented by the 1 _d_ constraint. Note that


10Note that governance attacks like this can be mitigated by limiting the contract structure
governance can alter and implementing long time delays between changes, but it is a realistic
attack vector in currently deployed systems that build in broad contract upgrade capability. The
structure of the formal problem can also be altered by tailoring emergency settlement triggers.


170


a simple reformulation of the governance objective would model the case of


_ζ >_ 0 _._ 5.


The vault decision is expanded to include the amount of collateral _N_ locked


in the stablecoin subject to an amount _N_ [¯] available to the vault; the amount


locked is subject to seizure by a governance attack. This compares to Problem 1,


in which all vault COL is locked since there is no attack vector (the previous


_N_ is the new _N_ [¯] ). For simplicity, the setup assumes that _γ_ is such that, under a


successful attack, no collateral is recoverable by the vault after accounting for


_F_ ; this could be relaxed with an extra term in the vault’s objective. As an ex

tension to Problem 2, _α_ could also incorporate a bribe decision from the vault to


governance to change attack incentives.


**Problem 2** Ca ital structure with - vernance attack vector
p g


**Governance choice**


max E (1 _−_ _d_ ) _δF_ + _κ_
_δ∈_ [0 _,_ 1) ~~�~~ ~~�~~               - �


s.t. _d_ = 1 ( _γN_ (1+ _R_ ) _>ζ_ ( _δF_ + _κ_ )+ _α_ )

_F_ is vault choice


**Vault choice**


max E[( _N_ [¯] _−_ _N_ ) _R_ + (1 _−_ _d_ ) _NR_ + _F_ ( _Bb −_ _δ_ ) _−_ _dN_ (1 + _R_ )]
_N,F ≥_ 0


s.t. _F ≤_ _βN_


1 ( _N>_ 0) _u ≤_ E[ _F_ ( _Bb −_ _δ_ ) _−_ _dγN_ (1 + _R_ )]


1
_B_ = E _U_ _F,_ (1 _−_ _γd_ )( _N_ (1 + _R_ ) _−_ _δF_ )

               -                - _F_ [min]                -                - ��


_d_ = 1 ( _γN_ (1+ _R_ ) _>ζ_ ( _δF_ + _κ_ )+ _α_ )
0 _≤_ _N ≤_ _N_ [¯]


In Problem 2, incentive alignment against attack (security) will depend criti

cally on _κ_ and _α_ as it’s unrealistic for _δF_ to be on the order of _N_ ( _∼_ 100% interest


_κ_
rate). In a long-run growth equilibrium will be related to the geometric sum


_δF_
1 _−r_ [for some discount factor] _[ r]_ [. This allows us to understand the settings in]


171


_α_
which long-run incentive security will depend on a large term, which equates


to centralized recourse. In particular, combining the conditions for a non-attack


decision with the collateral constraint, we need _[γ]_ _ζδ_ _[r]_ _[< β]_ [ to have incentive secu-]


rity against attack with _α_ = 0, which is very limiting for practical values of these


quantities. Notice that, if incentive security is lacking or the opportunity is not


profitable enough for the vault, an equilibrium can be no participation from the


vault (in which case 1 ( _N>_ 0) = 0 in the utility threshold constraint).


We can interpret this as a ‘price of anarchy’ concept. In this case, we may


want to measure the ratio between the ‘best decentralized equilibrium’ and the


- ptimal ‘centralized’ solution (e.g., when _α >>_ 0 simplifies the setting to Prob

lem 1). A natural task of a protocol designer would be to optimize this cost.


**Problem 3: Portfolio selection with collusion attack**


We now consider a collusion attack vector of the form described in [107]. For


instance, a group that controls a large share of GOV (e.g., 51%, though possibly


lower) can manipulate price feeds and settle the system such that stablecoin


holders or vaults have claim to greater share of collateral. If the group also


holds the profitable position (e.g., stablecoins), then the attack can be profitable


unless the GOV token holds adequate market value. These 51%-style attacks


can’t inherently be mitigated. [11]


We model these attacks in a more complex setting; a full formal setup is in


Appendix Problem 3. In this setting, vaults and stablecoin holders are endowed


11Common mitigations include governance delays and maximum governance changes, but
these are only effective to a certain extent. As discussed in [107], once there is a profitable
coalition, they can wait out any time delays–e.g., vaults are not able to exit if they can’t buy
back the stablecoins.


172


with a value and choose a portfolio of available assets, some of which entail par

ticipation in the stablecoin system and are subject to attack. They may strategi

cally bid up the price of GOV to secure the system or acquire GOV and/or issue


a bribe to try to trigger a instigate a profitable attack. A third agent is an outside


GOV holder who may choose to collude with other agents. These agents make


the following strategic decisions:


**x**

  - Vault decides portfolio allocated between COL and GOV, level of par

ticipation in the stablecoin _N_ and _F_, and bribe factor _γv_ to the outside


governors.


  - Stablecoin holders decide portfolio **y** allocated between STBL, GOV, and


COL and bribe factor _γs_ to the outside governors.


  - Outside governors hold _ε_ fraction of GOV, decide interest rate _δ_ and de

cide whether to collude with the vault ( _dv_ ), the stablecoin holder ( _ds_ ), or


whether no attack occurs ( _dn_ ).


The offered bribes are a _γv_ and _γs_ fraction of attack profitability. An attack is


profitable if _ζ_ fraction of governance collude (e.g., a threshold to manipulate the


price feed)–we can generally take _ζ ≥_ 0 _._ 5, but could be lower if collusion with


miners is added in. The portfolios **x** _,_ **y** have components measured in dollar


value and which sum to the total endowed values ¯ _x,_ ¯ _y_ .


The COL market is assumed to be perfectly liquid at the given price, and so


portfolio decisions have no price effect on COL. We restrict the focus to mod

eling endogenous prices of GOV and STBL. The price of GOV is determined


through the function _P_ ( **x** _G,_ **y** _G, δ, F_ ); we assume this = E[ _δF_ + _κ_ ] without vault


- r stablecoin holder participation in the GOV market. In the model, _P_ 2 = _P_ 1 con

173


ditional on no attack. If an attack occurs, then GOV price goes to zero. The STBL


price is determined through the function _B_ ( _F,_ **y** _S_ ) in a way that balances supply


and demand. Since the stablecoin holder has an endowed value in this prob

lem, we no longer assume the STBL market demand has an unlimited depth at


a given utility value, as done in the previous formulations. The behavior of this


model will likely depend largely on the choice of functions _P, B_ . A number of


choices could be explored to consider different market structures.


Compared to Problem 2, the vault now decides the amount of COL to hold


( **x** _C_ ), equivalent to previous _N_ [¯] ) and, of that amount, the amount to lock as col

lateral in the stablecoin ( _N_ ). Similarly, **x** _G,_ **y** _G_ represents the amount of GOV


in the vault and stablecoin holder portfolios respectively. We now have three


attack decision variables ( _dn, dv, ds_ ), precisely one of which will take the value 1.


The logic for this is encoded in the 2nd-4th constraints of the outside governance


choice problem.


**Problem 4: Miner-absorbed mechanism**


The miner-absorbed system is a variation of the presented problems as it ex

plicitly models miners as the core participants. The miner-absorbed stablecoin


includes two agents: _Miners_ taking the role of risk absorbers, governance and


miners as well as _stablecoin holders_ . Further, the system includes an algorithmic


_issuance_ role (i.e., part of the base blockchain consensus protocol). The primary


value in a miner-absorbed mechanism is implicit collateral. In this problem


.
setting, we assume that miners are risk-neutral, economically rational agents [12]


Further, we assume that the base blockchain includes a single currency STBL


12Non-risk neutral miners could also be observed and are covered for a non-stable currency
in [53]


174


**Problem 3** Portfolio selection with collusion attack vector


**Outside governance choice**

_δ∈_ [0 _,_ 1) _,d_ max _{n,v,s}∈{_ 0 _,_ 1 _}_ E ~~�~~ _dnε_ ( _δF_ + _P_ 1) + _dv_      - _γv_ ( _F −_ **x** _G_ ) _−_ _α_      
+ _ds_           - _γs_ ( _N −_ **y** _G_ ) _−_ _α_           - [�]


s.t. _P_ 1 = _P_ ( **x** _G,_ **y** _G, δ, F_ )




**[x]** _PG_ 1 _[≥][ζ]_ [)] _[ ≤]_ _[d][v][ ≤]_ [1] [(] _[ε]_ [+] **[ x]** _P_ _[G]_ 1

**[y]** _PG_ 1 _[≥][ζ]_ [)] _[ ≤]_ _[d][s][ ≤]_ [1] [(] _[ε]_ [+] **[y]** _P_ _[G]_ 1



1 ( **[x]** _PG_ 1

1 ( **[y]** _PG_



_P_ _[G]_ 1 _[≥][ζ]_ [)]


**[y]** _P_ _[G]_ 1 _[≥][ζ]_ [)]



_dn_ = (1 _−_ _dv_ )(1 _−_ _ds_ ) and _dv_ = (1 _−_ _dn_ )(1 _−_ _ds_ )


**x** _,_ **y** _, N, F, γv, γs_ from vault and stablecoin holder choices


**Vault choice**


**x** _G_
max E **x** _CR_ + _F_ ( _Bb −_ _δ_ ) + _dn_ ( _δF_ + _P_ 1)
**x** _,N,F ≥_ 0 _,γv∈_ [0 _,_ 1) - _P_ 1


+ _dv_ (1 _−_ _γv_ )( _F −_ **x** _G_ ) _−_ _dsN_

                         
s.t. 1 _[T]_ **x** = ¯ _x_


0 _≤_ _N ≤_ **x** _C_

_F ≤_ _βN_


**x** _G_
1 ( _N>_ 0) _u ≤_ E       - _F_ ( _Bb −_ _δ_ ) + _dn_ _P_ 1 ( _δF_ + _P_ 1)


+ _dv_ (1 _−_ _γv_ )( _F −_ **x** _G_ ) _−_ _dsN_

                         
_B_ = _B_ ( _F,_ **y** _S_ )


_P_ 1 = _P_ ( **x** _G,_ **y** _G, δ, F_ )


_δ, d,_ **y** from outside governor and stablecoin holder choices


**Stablecoin holder choice**



**y** _S_
max E _U_ **y** _CR_ + _dn_ min
**y** _,γs∈_ [0 _,_ 1) ~~�~~ ~~�~~ - - _B_



_S_ + **[y]** _[G]_

_B_ _[, N]_ [(1 +] _[ R]_ [)] _[ −]_ _[δF]_ - _P_




**[y]** _[G]_ ( _δF_ + _P_ 1)

_P_ 1 


+ _ds_ (1 _−_ _γs_ )( _N −_ **y** _G_ )

               - �

s.t. 1 _[T]_ **y** = ¯ _y_


_B_ = _B_ ( _F,_ **y** _S_ )


_P_ 1 = _P_ ( **x** _G,_ **y** _G, δ, F_ )


_δ, d,_ **x** _, N, F_ from outside governor and vault choices


175


(i.e. the GOV and COL tokens are not present) and that it includes a correct and


up-to-date price oracle.


We define Problem 4 as follows: Should a miner generate a new block given


an expectation of the rewards _r_ being paid, the return rate on the rewards _b_ at


_B_ _c_
the market price of STBL considering the cost for mining as well as a long

term confidence in the system expressed as _P_ 1? In _c_ we subsume all variable


and fixed costs for generating a block. The miner’s decision is expressed by _d_


such that _d_ = 1 encodes generating a block and _d_ = 0 the opposite.


The stablecoin holder decides to participate in the miner-absorbed systems


based on the expected stability of the system expressed by the utility function


_U_ . The stablecoin holder has a portfolio of assets **y** . The portfolio consists of


two asset: STBL denoted as **y** _S_ and a second exogenous stablecoin denoted as


**y** _A_ . For example, this could be a miner-absorbed system like Kowala and USDC


as exogenous system. The stablecoin holder re-balances the weight of the port

folio from one block (denoted by **y0** ) to the next block (denoted by **y1** ). The


decision is based on the price of STBL expressed by _B_ and the price of the ex

- genous stablecoin denoted as _BA_ . Additionally, there is a cost _δ_ to acquire


STBL. The stablecoin holders portfolio re-balancing has an impact on the price


_B_ expressed by the abstract function _B_ ( _r,_ **y1** _, d, P_ 1). If the stablecoin holder sells


significant amounts of his STBL holdings, this should have a severe implications


for the price. Last, we define the abstract function _P_ ( **yS** _, d_ ) that determines the


confidence in the system of the stablecoin holder. For example, the stablecoin


holder could short-term sell STBL without affecting the long-term confidence in


the system. This is similar to a stablecoin holder using STBL to e.g., pay bills


but planning to keep using the system in the long-run.


176


Miner rewards _r_ are adjusted by the issuance algorithm.The issuance algo

rithm is left abstract. However, the objective of the issuance algorithm is to


minimize the change in price _B_ . We note that in a PoW system the reward


is constrained such that _r ≤_ 0 since the issuance algorithm can in the worst

case pay zero rewards but not “take-away” existing value. In a PoS system this


can be achieved by slashing PoS miners as well as in seigniorage share systems


were miners additionally hold a risky asset such as COL [168]. The issuance


algorithm takes as inputs the price function, but has to assume that _d_ = 1. The


miner-absorbed problem adopts previous components and adds new ones as


follows:


 - _c_
= cost for mining a block


 - _δ_ = cost to obtain a stablecoin


 - _u_
= stablecoin holder’s utility for an outside STBL opportunity


 - _r_
= reward paid in the next block


_r_
Given the problem 4, depends on the the expectation the stablecoin holder


has towards the price of STBL _B_ and the subsequent re-balanacing of the port

folio **y** . If the stablecoin holder expects the price stability, he will either increase


his holdings of STBL (considering the cost of obtaining expressed by _δ_ ) or keep


his current holdings. On the other hand, price instability will lead to a reallo

cation of portfolio weights towards the exogenous stablecoin [13] . We discuss the


_r_ .
changes in portfolio allocation as these lead to more severe impacts on


13We note that we could extend this model with a preference for either STBL or the exogenous stablecoin. For example, if the stablecoin holder prefers a non-custodial STBL and his

- nly alternative would be a custodial exogenous stablecoin, we could increase the preference of
STBL.


177


**Problem 4** Miner choice with no attack vectors


**Miner (governance) choice**


max E _d_ ( _Bbr −_ _c_ ) + _P_ 1
_d∈{_ 0 _,_ 1 _}_ ~~�~~                

s.t. _du ≤_ E[ _Bbr −_ _c_ ]


_r_ is algorithmic issuance


**Stablecoin holder choice**


max E ~~�~~ _U_ ( **y1** _SB_ + **y0** _A ∗_ _BA_ + ( **y0** _S −_ **y1** _S_ ) _B_ (1 _−_ _δ_ ))�
**y1**


s.t. _B_ = _B_ ( _r,_ **y1** _, d, P_ 1)


_P_ 1 = _P_ ( **y** _S, d_ )


**Issuance algorithm**


min _|B_ ( _r,_ **y1** _,_ 1 _, P_ 1) _−_ 1 _|_
_r≥_ 0


_Case 1: Increased demand for STBL_ **y0S** _<_ **y1S** _._ To keep the price stable (i.e.


min _|B_ () _−_ 1 _|_ ), the issuance algorithm sets _r >_ 0. In turn, this increases the total


supply _F_ . Assuming that _Bbr > c_, miners should choose to mine a block such


that _d_ = 1. Notably, the issuance algorithm can increase _r_ to meet any demand


by simply increasing mining rewards. However, there is can still be a problem


here: _r_ is directly paid to miners. If miners are not spending STBL such that it


_r_
is reallocated to stablecoin holders, even issuing can lead to a price increase.


_r_
Conversely, if is set too high and miners sell STBL directly, the price of STBL


can decrease. Hence, finding a price-stabilizing issuance algorithm is non-trivial


given that the portfolio allocation and miner decisions cannot be known a priori.


_Case 2: Decreased demand for STBL_ **y0S** _>_ **y1S** _._ In this case, stablecoin holders


are selling STBL in favor of an exogenous stablecoin. The issuance algorithm re

duces _r_ in return to limit the increase of _F_ - r do not increase _F_ at all. However,


the problem of paying low rewards introduces two distinct problems. First, it


is possible that even in the case of _r_ = 0, _B_ will still decrease if there is too


178


much supply in the market. A short-term price increase might still be counter

acted if stablecoin holders and miners have long-term confidence in the system


expressed by _P_ 1. However, second, without block rewards, the expected util

_c_
ity for miners is can be negative since they cost for mining a block is only


compensated with the long-term confidence _P_ 1. If miners only consider the


next block (without _P_ 1), the liveness of the ledger is sacrificed due to the “Gap


Game” [50, 183]. Even worse, miners could fork the chain with the most valu

able transactions from the previous blocks to continue to earn rewards. If the


liveness of the miner-absorbed system is not present, it will likely also affect the


long-term confidence in the system for stablecoin holders and miners.


Moreover, if the miner can easily switch between different chains, they


would likely abandon the current stablecoin chain for one that pays high re

wards. One can motivate the miner to stay if the cost for switching is high, e.g.,


if a miner does not produce blocks in a given time they are slashed as in PoS


systems. However, hard-to-leave also means hard-to-join: a miner needs to be


ensured that his rewards will be positive in expectation. By adding up-front re

quirements like specialized hardware or acquiring certain currency, the rewards


in expectation are minimized by the cost of acquisition as well as opportunity


cost for maintaining the hardware/stake of coins.


**Further variations**


**Endogenous collateral** We now need to account for the endogenous COL


price: the actions of the stablecoin agents will have a direct price effect on COL


if the primary use of COL is within the stablecoin system. One way is to define


the COL price return as a function of the decision variables and update the vault


179


and stablecoin holder objectives with this price formulation. In this way, a driv

ing random variable (like _R_ in the exogenous formulation) describing outside


faith in the system would be an input to the price function in addition to agent


decisions. As with the functions _B, P_ in Problems 1-2, the precise formulation


- f this price function will play an important role in the problem, but we can ex

plore a number of different market structures. In addition, the governance and


vault roles may be merged into the same position if GOV = COL. Governance


can also be an outside party without an explicit token–e.g., addresses controlled


by the founding company.


**Algorithmic issuance** When stablecoin issuance is automated by the proto

col, the vault is no longer a player. Instead, the issuance process becomes a


constraint for the remaining players, as in Problem 4. The issuance process will


directly affect the value of GOV, in which case, it may be worth considering a


participation decision in owning GOV (e.g., in a portfolio selection problem). If


all COL is implicitly backing the stablecoin, an insurance role will factor into a


general COL holder’s decision to hold COL, and thus into the pricing of COL.


If GOV = COL, then this all comes down to the pricing of GOV. In the case that


a specific portfolio of COL (and/or other assets) is backing STBL, and not all


COL, then a money market model may be useful. Models such as [156] could be


_∼_
adapted to consider portfolio and last-resort insurance role of GOV ( sponsor


support) in a stablecoin setting with added attack vectors.


**MEV: Miners as additional governance** Some single period MEV attacks can


be modeled within the capital structure framework by including miners as a


second governance-type agent, who decides transaction inclusion and order

180


ing. For instance, miners could earn potential profits from front-running STBL


issuance decisions or from bribes to limit the actions of other agents. For richer


MEV attacks, we describe the adaptation of blockchain forking models in the


next section.

#### **4.4.2 Forking Models**


The capital structure models consider a single time-step: depending on the


expectations of agents, they will choose to execute certain actions in the next


round. In this section, we extend the models to explore how multiple rounds


- f agent decisions can affect stability and security of stablecoin systems. Specif

ically, we need to consider feedback mechanisms between different agents in

acteracting over multiple rounds. In such a setting, agents adjust their _future_


tions based on their beliefs of the other agents’ actions and the output of the


integrated algorithms (e.g., issuance or/and governance). Moreover, we con

sider that permissionless ledgers used in non-custodial designs (e.g. Maker)


lack finality. Miners are able to re-order transactions and re-write history within


certain depths of the ledger [83]. This allows agents to adjust _past_ actions as


well [14] . The resulting forking models are highly complex especially when con

sidering a combination of a complex non-custodial system like Maker with a


base blockchain like Ethereum.


Below, we consider a simpler formulation with specific couplings between


- therwise separate models of a base blockchain and an application layer. An


- utput of one layer would serve as exogenous input to the other layer and vice


14While only miners can directly re-order and decide on the inclusion of transactions, other
agents can employ bribing strategies to effectively achieve similar outcomes [139].


181


versa. For instance, the size of MEV determined in application layer participa

tion feeds back into incentives for forking attacks in the base layer, which feeds


back into the probabilities of attack in application layer incentives. In this way,


a complex forking model could be simplified into simpler problems that can be


solved iteratively to find an equilibrium. This section is kept informal such that


we describe the extensions required but do not include formal problems.


**Base blockchain** As explored in the blockchain folk theorem [33], miners have


an incentive to coordinate on the longest chain to increase their success of find

ing the next block. However, if a miner is already invested in a fork, the miner


decides based on his vested interest (e.g., accumulated work or committed


stake) whether to switch to a different chain. We need to take these two com

peting incentives into consideration when arguing about MEV, which serves


as an implicit bribe for miners toward specific chains. A forking model can


explore the success probability of bribing miners based on their prior incen

tives. Instead of modelling all miners with the same incentives, a forking model


considers that miners already mining on a fork will have a higher incentive to


take the bribe as they are invested in a fork. Additionally, the setup in [33]


can be extended by a network game as a stochastic dynamic system [193] or a


global game [145] with noisy observations (e.g., network delay, reward expec

tations). Moreover, we can incorporate various assumption of risk-appetite of


miners [53], selfish mining [79], and the impact of block rewards in comparison


to transaction fees [50, 183].


**Application layer** A stablecoin that is built as an application on top of the base


blockchain results in two directions of attack effects. In one direction, the appli

182


cation layer creates MEV that affects incentives on the base layer. For example,


an agent wishing to prevent a liquidation transaction in Maker could offer a


payment in another token to miners on Ethereum. Additionally, miners them

selves are able to profit from their ability to determine the history of the ledger


by e.g., execution of arbitrage opportunities, “time-bandit attacks”, or oracle


manipulation. Prior work on MEV in decentralized exchanges (DEXs) [64] and


data feed issues [191, 77] describe some effects of this direction. The other direc

tion affects participation in the application layer. A forking model could model


the success probability of an exogenous bribe within the base blockchain. If


successful, an attack would capture value locked in the stablecoin. The possibil

ity of such an attack (now or in the future) will have an effect on participation


incentives in the stablecoin, similar to the description in the capital structure


models. Stablecoin participation decisions in turn determine the size of MEV


- pportunities, which served as bribe inputs to the base layer model. Incentives


created in the stablecoin system can therefore impact the security of the base


blockchain system and vice versa.

#### **4.4.3 Price Dynamic Models**


We provide a brief review on models that explore the higher-level problem of


whether non-custodial stablecoin incentive structures can lead to stable price


dynamics. A challenge here is in modeling the feedback effects of agent deci

sions, as discussed in the previous section. To illustrate, in the most closely re

lated traditional financial models, an assumed stable asset is borrowed against


collateral, whereas in the non-custodial stablecoin setting, the ‘stable’ asset that


is borrowed has an endogenous price and/or participation level. The decisions


183


- f the other agents will affect this endogenous price and participation level of


the stablecoin holder.


[114] and [112] construct stochastic models involving endogenous stablecoin


price in exogenous collateral systems, taking into account deleveraging and liq

uidation actions given imperfectly elastic stablecoin demand. In this context,


they model vault issuance incentives considering that issuance involves taking


a leveraged bet on the collateral asset. They illustrate potential deleveraging


feedback effects on stablecoin markets that lead to stablecoin price appreciation


and characterize stable and unstable regions for stablecoins. As a result, vaults


may have to pay above face value to deleverage in a crisis. This is validated


by observed behavior of Dai on ‘Black Thursday’, and was actually predicted a


year before in [112].


There are several open follow-up questions. For instance, evaluating the ef

fect deleveraging events have on stablecoin holder participation incentives (par

ticularly for different designs and relative to alternatives available to stablecoin


holders), exploring strategic interaction of many vaults, destabilizing effects of


attacks such as in the previously mentioned forking models, and extending to


endogenous collateral models.


A few other papers are applicable to stability of stablecoins. [88] and [100]


model cryptocurrency-collateralized lending platforms. These do not incorpo

rate feedback effects on the stable asset market, but do incorporate feedback


effects on collateral asset liquidity. [15] A simpler stablecoin problem involving


no feedback effects is modeled in [42]. Option pricing theory is applied in [46]


to value tranches in a proposed stablecoin using PDE methods, also under no


15These are similar to models for traditional collateral and debt security markets and repurchase agreements.


184


feedback effects. Some stablecoins have also performed stability analyses (e.g.,


[55], [160]), though these are typically limited in scope and include generous


assumptions.

#### **4.4.4 Agents, preferences and attitudes to risk**


Agents’ preferences, and in turn their behavior, are a central object in stablecoin


design. In Appendix 4.7.5, we first describe an framework which can be used to


model preferences, and then outline two methods which can be used to estimate


agents’ risk attitudes. The attainment of a clear understanding of agents’ risk


attitudes would serve to improve protocol design and parameter selection.

#### **4.5 From Stablecoins to DeFi**


In this section we discuss a likely implication of our capital structure models.


Further, we outline how the modelling framework presented herein is appli

cable to other cryptoeconomic systems including composite assets, cross-chain


protocols, synthetic assets, collateralized lending protocols, and DEXs.

#### **4.5.1 Sustainability of Incentives**


As discussed in the context of our capital structure models, to maintain incen

tive security long-term, the value of a governance token may need to be dis

joint from system growth. In particular, system growth rates (in supply, capital


locked) are unlikely to be high in a long-term ‘steady state’ (and may be zero).


185


However, the value of the governance token, if derived from discounted fu

ture fees, may only provide incentive security when the expected growth rates


are high—in essence, when borrowing from the future is possible. A long-term


equilibrium without large future growth expectations may not be possible with


governance token value derived from fees alone as they may be small with re

spect to value locked. Instead, other parties to the system may need to hold


governance tokens to bid up governance token market value. This will feed

back into participation incentives of these other parties; there is no guarantee


that equilibrium participation exists in this context either. To illustrate, stable

coin holders may need to hold significant positions in a risky governance asset


in order to secure their stable positions, which may defeat their purpose in hold

ing the stablecoin. This leads us to a frustrating impossibility conjecture about


many current systems in the context of our models:


**Conjecture 4.1.** _In fully decentralized stablecoins (α_ = 0 _) with (i) multiple classes_


_of interested parties (e.g., risk absorbers vs. stablecoin holders) and (ii) a high degree_


_of flexibility in governance design, no equilibrium exists with long-term participation_


_under realistic parameter values._


An analogy helps to illustrate impossibility of some designs: if incentive


security requires a bank’s equity market value to be worth multiples of total


deposits, then no depositors will participate. The bank’s _long-term_ P/E ratio


would need to be in the 100s or 1000s. The conjecture reinforces the importance


- f studying mutual incentives in choosing the right stablecoin design. Note that


the oracle incentive compatibility problem also closely resembles the stablecoin


governance incentive problem. Solving these problems in a fully decentralized


way remains an open problem.


186


Current solutions implemented by stablecoins essentially centralize gover

nance. This solution relies on a form of institutional liability and translates into


_α_
a high value (e.g., in Problem 2). This is not necessarily a problem; many tra

ditional financial systems operate in this way. This is why banks do _not_ need


to be worth multiples of total deposits. However, we should openly recognize


that this trust line exists and may be vital.

#### **4.5.2 Composite Stablecoins**


So far we have focused on _primary_ stablecoin mechanisms. Another class of


_composite_ stablecoins involves baskets of primary stablecoins to try to further


absorb risk. The simplest is an _ETF stablecoin_, which works using the ETF arbi

trage mechanism to create/redeem the composite stablecoin against the basket.


A _DEX stablecoin_ aims to spread risk over the basket while providing an


exchange service between the constituents, and so the basket weights change


with exchange demand. DEX stablecoins take on the risk of liquidity provi

sion to these exchanges. For constant function market maker (CFMM)-based


exchanges, this risk is described in [12, 11]. Other DEX stablecoin designs pro

pose limited 1-to-1 stablecoin swaps. Existing DEX stablecoins bear the risk


that the value of the basket may devolve into the value of the least valuable


constituent(s) (e.g., if an underlying stablecoin fails).


A _CDO composite stablecoin_ segregates stablecoin risk into tranches. [16] For


instance, the basket may have _n_ stablecoins and _n_ tranches. At settlement, the


senior tranche holder gets first choice of which stablecoin to redeem for while


16Note the difference from the CDO analogy used to describe primary stablecoins.


187


holders of the most junior tranche picks last. Thus, junior tranche holders bear


the risks of first stablecoin failures and are compensated with interest payments.


This structure introduces a similar participation problem: enough agents need


to be willing to take the different positions given the equilibrium level of interest


payments.


A rainy day fund _RDF stablecoin_, as introduced in [104] and [109], holds a


basket of assets that accrues value to a safety buffer over time through arbi

trage, fees, and other collateral uses. The collateral basket aims to target 1 USD,


whereas the accrued buffer aims to smooth any asset failures/deviations over


time.


Other composite stablecoins may also be possible. The stability of all com

posite stablecoins relies on primary stablecoin failures not being highly corre

lated. Table 4.4 summarizes categories for composite stablecoins, applicable


models, and projects.

#### **4.5.3 Cross-chain and Synthetic Assets**


The foundations in this paper can also apply more broadly to synthetic and


cross-chain assets. In Appendix 4.7.6 we explain the relevant differences be

tween these asset types in the present setting, and set out how our foundations


apply.


188


#### **4.5.4 Lending Protocols and DEXs**

**Lending protocols.** Collateralized lending protocols share a similar structure


to non-custodial stablecoins. Our models are easily adapted to describe such


protocols. Lending protocols are simpler than non-custodial stablecoins in that


borrowed assets are exogenous, rather than endogenously created by the pro

tocol. This makes system time delays more effective protective measures. In


the non-custodial stablecoin setting, a vault is not able to deleverage and exit


unless they can repurchase stablecoins. Therefore in the event of a governance


attack, a system time delay built into the protocol would likely be ineffective


as a (profitable) coalition between stablecoin holders could simply wait out the


delay, preventing many vaults from exiting. In contrast, in the collateralized


lending setting, an important security implication of the exogeneity of the bor

rowed assets is that it can allow protocol participants to leave a protocol before


a governance attack is fully realized. The typical borrowed asset either has a


much larger market or is a custodial stablecoin, in which case the vault can al

ways create new stablecoins at par through the issuer to deleverage. A system


time delay could therefore protect participants by allowing them to exit before


many impending governance attacks could be realized. [17]


**DEXs.** Some DEXs directly or indirectly have governance layers. When on the


same native blockchain as the deposited assets, similarly to collateralized lend

ing protocols, a DEX may also permit participants to exit before a governance


attack is fully realized. However, where DEXs operate their own blockchain


and control its governance (e.g., Rune), the ability for participants to exit in an


attack can be fundamentally restricted. In this latter case, incentive security is


17A likely exception is price feed attacks.


189


an important question, and mutual participation of governance and other par

ticipants can be modeled as in our capital structure models.


For DEXs, fees are proportional to exchange volume while the potential


payout of governance attacks is proportional to liquidity provider deposits.


Therefore a key ratio of interest to protocol designers is volume relative to de

posits. For a DEX, annualized volume can be as high as _∼_ 100 _×_ deposits (e.g.


Uniswap). In comparison, for a collateralized stablecoin accruing fees on bor

rowed assets, such fees can be as low as _∼_ 1 _/_ 4 of deposits. This _∼_ 400 _×_ factor


makes the feasible region for incentive security against governance attacks po

tentially larger in DEXs than stablecoins. This leads us to the following conjec

ture in the context of our models:


**Conjecture 4.2.** _Considering fully decentralized systems (α_ = 0 _) with (i) multiple_


_classes of interested parties and (ii) a high degree of flexibility in governance design,_


_DEXs have a wider range of feasible long-term participation equilibria than stablecoins_


_under realistic parameter values._


An interpretation is that it may be fundamentally easier to economically


secure DEXs against governance attacks than stablecoins. The conjecture also


suggests ways in which broad stablecoin governance powers could be better


_∼_
aligned: by taxing transactions/economic activity ( DEX volume) as opposed


to assets under management. Of course, such a tax would make these stable

coins altogether less desirable to users with a cost for flexible governance.


190


#### **4.6 Concluding Remarks**

We have introduced a foundational framework for relating economic mechanics


- f all stablecoins and formulated three classes of models for non-custodial sta

blecoins, for which traditional financial models are sparse. These models eval

uate measures of economic stability and incentive-based security considering


mutual participation incentives of agents necessary for a mechanism to func

tion. These models consider attack vectors including governance, data feeds,


miners, and deleveraging market feedback effects.


**Acknowledgements** We thank Andrew Miller and the anonymous review

ers for their feedback and suggestions. This project received funding from a


Bloomberg Fellowship, NSF CAREER award #1653354, EPSRC Standard Re

search Studentship (DTP) (EP/R513052/1) and the BinanceX Fellowship pro

gramme.


191


Table 4.2: Non-custodial stablecoins as related by several components (excluding governance and data feeds).

#### **4.7 Appendix** **4.7.1 Tables**


**Category** **Stability Models** **Stablecoins**


Reserve Fund ETF TUSD, USDC, Libra v2
Bank Fund ETF, bank run Tether [1]

MMF ETF, MMF Libra v1
CBDC Currency Chinese DC/EP


Table 4.1: Custodial stablecoins and applicable models. NB as of 2019, Tether
held 74% reserves in USD/equivalents but claimed to be fully collateralized
taking into account the value of loans to partner Bitfinex [58, 57].


192


Table 4.3: Non-custodial stablecoins as related by several components, updated
with recent projects and stablecoin collapse events. The category “protocol assets” indicates that the protocol maintains a direct balance sheet (similar to composite stablecoins) as opposed to agents maintaining their own balance sheets
through the protocol.


**Category** **Relevant Models** **Projects**


ETF ETF Reserve
DEX Liquidity provider PieDAO, mStable, yCRV, CementDAO, Neutral

CDO CDO Introduced in [43]
RDF Introduced in [104, 109]


Table 4.4: Composite stablecoins summary.


193


|Col1|Project|When|Col4|Event|
|---|---|---|---|---|
|||||Deleveraging feedback leads to Dai trading<br>at above 1 USD<br>Collateral liquidation auctions settle at 0 DAI<br>due to illiquidity and network congestion<br>Broken peg, broken settlement due to low<br>collateralization<br>Broken peg, haircut in redeemability due to<br>system debt level<br>Deleveraging feedback leads to Dai trading at<br>above 1 USD<br>Crisis of confidence<br>Crisis of confidence, equity position unable to<br>absorb enough supply|
||Dai|December 2018|December 2018|December 2018|
||Dai|March 2020|March 2020|March 2020|
||Dai|March 2020|March 2020|March 2020|
||bitUSD|Winter 2018-19|Winter 2018-19|Winter 2018-19|
||Steem Dollars||December 2018|December 2018|
||NuBits|Summer 2016|Summer 2016|Summer 2016|
||NuBits|March 2018 - ongoing|March 2018 - ongoing|March 2018 - ongoing|
||||||


Table 4.5: Notable non-custodial stablecoin deleveraging events.


**Stablecoin** **Time Period** **Event**


Tether Oct. 2018 Partner Bitfinex suspends fiat convertibility = _⇒_
Tether crisis [59]


Table 4.6: Custodial stablecoin depegging events.

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



Table 4.7: Non-custodial system oracle manipulation events.


194


#### **4.7.2 Reserve Fund Stablecoins**

Reserve Fund stablecoins can be modeled as Exchange-Traded Funds (ETFs). [18]


In ETFs, an investment vehicle (the ETF) is created with indirect claims to a


portfolio of underlying assets (e.g., stocks, bonds, and commodities) held by a


custodian. [19] A set of _authorized participants_ (APs) are allowed to redeem shares of


the ETF for the underlying assets and create new shares of the ETF by depositing


underlying assets at the net asset value (NAV). The ETF price is pegged to the


NAV. This peg is maintained by the APs, who capture arbitrage between the


ETF shares and the underlying portfolio. If direct redemption is allowed in a


Reserve Fund stablecoin, then anyone can be an AP. [20] Some stablecoins make no


promises about future redeemability; in this case, the de facto AP is the issuer


itself.


As with ETFs, given sufficiently liquid collateral, the price target is always


maintainable within some bounds through these mechanisms. The tightness of


the bounds, however, depend on the liquidity and volatility of the reserve as

sets. For instance, corporate bond ETFs traded at significant deviations from


NAV during the financial crisis in 2008 [99] and during the SARS-COV-2 mar

ket panic in 2020 [14]. Even US government bonds, which are normally highly


liquid, faced high liquidity stress in March 2020 [163] with corresponding ETFs


facing similar NAV-price deviations.


Empirical analysis of ETFs, e.g., [29], suggest that securities with higher ETF


- wnership are more volatile, which raises concerns about the ETF mechanism.


18To account for risk in underlying commercial bank deposits, we can also add a bank run
model in serial to an ETF model.
19ETFs can provide simpler access to underlying portfolio, which may not be accessible to the
investor otherwise, and reduced frictions/fees in maintaining small positions.
20Fees may discourage small redemptions, so that large redeemers are de facto APs.


195


While ETF membership leads to wider access and so increased trading volume,


the relationship with volatility is unclear as the empirical comparison is not


controlled. Rather, we would want to compare with a setting in which the un

derlying portfolio is as easily accessible without the ETF. An equilibrium model


analysis confirms a more nuanced relationship with volatility. [137] develops


a model of endogenous feedback effects in ETFs, in which the liquidity of the


underlying portfolio is influenced by the ETF. This model shows that ETFs are


exposed to different demand shocks than the underlying basket. Even with


small deviations, APs that arbitrage through leveraged positions can amplify


the differences. [21]


An ETF-like model is developed for Reserve Fund stablecoins in [129] and


interpreted against Tether trading data. Models such as these are a natural start

ing point to address the following open questions about Reserve Fund stable

coins:


 - **Issuer AP incentives.** Issuers are in a position to prevent competition and


decide timing in capturing arbitrage. There is a trade-off between the size


   - f mispricings before APs intervene, and maintaining a stable asset, which


affects demand and ultimately assets under management, for which they


are awarded deposit interest.


 - **Issuer target incentives.** If the peg target is defined at the discretion of the


issuer (e.g., not USD or an external index), then the issuer may have in

centive to manipulate the target index to its advantage. For instance, if the


21As stated in [137], “ETFs may be both a blessing and a curse. That is introducing new ETFs
may lead to a significant amplification of speculative behavior of arbitrageurs, destablize the
market, and lead to a spike in volatility; however, at the same time, a “good” ETF may actually
stabilize the economy, lead to a significant reduction in volatility, and improve the liquidity of
the underlying securities.”


196


stablecoin is large enough, changing the target can have a market impact,


which may be advantageous to outside positions held by the issuer.


 - **Effects on fiat currencies.** Does stablecoin structure affect the ability of


government to stabilize currencies? This is a concern of regulators re

garding the size of potential stablecoins, like Libra. This effect could be


modeled with ETF structure in series with currency models.


 - **Effects on crypto markets.** [87] suggested that stablecoins have been used


to manipulate Bitcoin prices. A model of the economic structure in Bit

coin/stablecoin markets (e.g., [129]) could help determine the direction of


causality suggested by the data.


Some of these open questions are relevant to the wider ETF literature itself


and are not specific to stablecoins.

#### **4.7.3 Fractional Reserve Fund**


**Bank Fund** In a Bank Fund stablecoin, the issuer maintains a balance sheet


functionally similar to a commercial bank. This balance sheet is based on frac

tional reserves with deposit obligations tied to stablecoins that are issued. Aside


from the fractional reserve, the bank holds other capital assets that are illiquid


and earn a yield for the bank. This is a nearly identical model to a normal bank


with a few exceptions: (1) the stablecoin bank my not be regulated or audited,


(2) the bank my not be government-insured against bank runs, and (3) the bank


may be freer to deny redemptions and/or apply redemption fees.


Bank Fund stablecoins can be understood using bank run models in series


197


with ETF models. In a bank run, the fractional liquid reserve of the bank is de

pleted from redemptions, after which the bank defaults as the bank’s remaining


assets are illiquid and can only be sold quickly at large discounts (a fire sale). In


a bank run, remaining depositors’ lose their money. [70] shows multiple equi

libria to the game played between depositors. This includes a bank run equilib

rium, in which all depositors scramble to redeem their deposits, triggering the


collapse in a self-fulfilling way. One approach is the global games setting of [49]


adapted to bank runs in [164] and [85]. In this setting, depositors observe bank


fundamentals with noise (e.g., the reserve ratio could be random), and they will


choose to rollover (i.e., extend the maturity of) their deposits if their signal is


above a threshold. [92] introduced a staggered debt structure of deposit matu

rities. A point of difference to existing bank run models are the non-negligible


network effects among stablecoin holders, much less so than among traditional


bank depositors.


Bank runs used to happen somewhat regularly. To prevent frequent crises


- f faith, governments issued depositor insurance against bank runs. However,


Bank Fund stablecoins are unlikely to have such insurance and so remain sus

ceptible to bank runs. A key consideration here is that bank runs follow a thresh

- ld effect in depositor faith. After a threshold is reached, too many depositors


try to redeem, sending the bank’s balance sheet into a ‘death spiral’. Below this


threshold, however, the coin may be very stable.


As noted above, a Bank Fund stablecoin may be freer to deny redemptions


and/or apply redemption fees. An event like this triggered a crisis in Tether in


Oct. 2018 (see Table 4.6). These levers may also be applied strategically to dis

courage the continuation of bank runs or could be abused to create profitable


198


price discrepancies for the issuer to arbitrage. Thus open questions emerge


around issuer incentives as in the Reserve Fund.


**Money Market Fund** In a Money Market Fund an underlying portfolio is


meant to closely track a target, with some return. A traditional Money Market


Fund maintains a fixed NAV for redemptions. While the underlying assets are


usually highly liquid and relatively stable, their market values float and so there


is some risk that the fixed NAV is unsustainable. This leads to a liquidity risk


related to bank runs: shocks to the underlying assets leads money market funds


to liquidate assets, which can have the effect of lowering prices further if liquid

ity is temporarily constrained, which can cause even more liquidations. Money


Market stablecoins can be understood using money market fund models, e.g.,


[156], in series with ETF models. There are many case studies of money mar

ket funds breaking the dollar during the 2008 financial crisis. In particular, [98]


show that in the presence of high inflows, money market funds had expanded


their risk-taking and they suffered runs as a result. Some of the proposed forms


- f Libra closely resemble money market structures.

#### **4.7.4 Discussion of Oracles**


Centralized oracles control the risk of outside attack but can lead to perverse


incentives for the provider–at some point, manipulating the feeds may be more


profitable than providing data honestly. They also introduce single points of


failure. Centralized approaches can be made more secure, for instance, through


the use of trusted execution environments [191]. Through such methods, it can


be proven that the data feed is an authentic representation of a particular source,


199


but it is still inherently manipulable by the source.


Decentralized oracle approaches exist, but remain an open research ques

tion. Existing solutions fall short of a full solution. They rely on Schelling point


schemes, in which agents vote on the price feed and are incentivized by slash

ing if their vote deviates from the consensus. These are problematic because


incentives are related to the consensus, which is not objectively verifiable for


correctness and can be manipulable through game theoretic attacks.


There are methods to mitigate these risks. For instance, medianizers are typ

ically used to aggregate prices from a number of oracles, half of which must


then be incorrect to manipulate the final feed. Some services, such as Chainlink,


provide such a medianizer using an incentivized reputation system [77]. The


security of such systems also remains an open question.


Other methods attempt to create a price feed inferred from on-chain metrics,


which is then objectively verifiable on-chain [104]. A related method attempts


to couple the price of a token to the cost of mining in proof-of-sequential work


(e.g., Elasticoin [72] and Meter [141]). [22] The security of these methods also re

mains an open question.


Some cryptocurrency-to-cryptocurrency prices can be determined on-chain


through decentralized exchanges, given appropriately controlled construction


(e.g., to account for limited liquidity and time-averaged over extended time pe

riods to make manipulation more costly). A missing link is still to outside fiat


prices, however. Prices in terms of other stablecoins may be used, but this faces


the same inherent problem: we then rely on that stablecoin, which may be ma

22Though note that as ‘stablecoins’ Elasticoin and Meter are only upper bounded in price
without a risk absorption mechanism. Melmint adds a seigniorage shares mechanism atop Elasticoin to absorb risk.


200


nipulated or fail, for the data feed.

#### **4.7.5 Agents, preferences and attitudes to risk**


**Utility functions**


Provided an agent’s preferences satisfy certain properties, an agents’ prefer

ences over consumption set _Y_ can be represented by a utility function [138]. In


particular, here we assume that an agents are _mean-variance_ maximizers, roughly


wanting to maximize the mean and minimize the variance of a portfolio, with


preferences over a random variable _X_ can be described as follows:


_U_ ( _X_ ) = _µX −_ _[ρ][A][σ]_ _X_ [2] (4.1)
2


where _X ∼_ _N_ ( _µX, σX_ ), with _µX_ denoting the mean of _X_, _σX_ denoting the


variance and _ρA_ denoting the coefficient of risk aversion. We provide more in

formation on this formulation in 4.7.5.


**Method 1: one risky asset, one riskless asset**


In one simple framework, a _mean-variance_ maximizer can invest proportion _α_ - f


their wealth in a risky asset, and proportion (1 _−_ _α_ ) in a risk free asset. From


this setup, it is possible to derive, as we do in 4.7.5, that their optimal choice of


_α_
is given as follows:


201


_α_ _[∗]_ _w_ = [E][[] _[R]_ []] _[ −]_ _[r]_ (4.2)

_ρAV ar_ ( _R_ )


where _w_ denotes the agent’s wealth, E[ _R_ ] and _V ar_ ( _R_ ) the expected return


and variance of a risky asset and _r_ denotes the return on a risk-free asset. From


this expression, all that is required to compute _ρA_ is knowledge of the five vari

ables in this equation, making it a tractable place to begin with the estimation


- f agents’ preferences.


**Method 2: preferences from portfolio weights**


It is also possible to uses agents’ investment history to infer agents’ risk-aversion


coefficients. In particular, [39] consider an investor who invests into _k_ risky as

sets and a single riskless asset, basing their investment strategy on an exponen

tial utility function, as above. As well as permitting multiple risky assets, in


contrast to above, the closed-form solution to the portfolio choice problem pro

vided by the authors is also explicitly multi-period. We present the details of


this approach in 4.7.5.


**A case study of MakerDAO using Method 1**


We apply Method 1 to Equation 4.2 to seek to recover agents’ risk aversion in


choosing leverage in the MakerDAO protocol [134], a non-custodial collateral


backed stablecoin (see Section 4.3). We use data on single collateral Dai (Sai) up


until November 18th 2019. A histogram of the resulting values of _ρ_ per CDP is


given in Figure 4.2 [23] . While these results should only be considered indicative,


23Note that we exclude outliers in the plot, e.g. those with risk aversion above 1


202


Figure 4.2: Values of _ρ_ per CDP.


we find a mean value for _ρ_ - f 0.0011, which seems approximately consistent


with other estimates of risk-aversion coefficients in the literature [20]. We also


provide an average value of _ρ_ per address, rather than per CDP, in Figure 4.3.


Looking at ‘active’ accounts with more than 10 CDP actions, we find a mean


value for _ρA_ - f 0.0012. The main takeaway from figure 4.3 is that on an address


level, most addresses appear to exhibit some degree of risk aversion, with some


estimates of _ρ_ providing notably higher levels of risk aversion than appear in


the literature.


**Utility function estimation - details.**


We take as our starting point a general class of utility functions: those represent

ing Hyperbolic Absolute Risk Aversion (HARA), where the level of risk toler

ance is a linear function of wealth:



_u_ ( _w_ ) = [1] _[ −]_ _[γ]_

_γ_



_γ_

_aw_

(4.3)

- 1 _−_ _γ_ [+] _[ b]_ 


203


Figure 4.3: Values of _ρ_ per Externally Owned Account.


where _u_ ( _w_ ) is the utility arising form a certain level of wealth _w_, _a >_ 0, _γ ̸_ = 0


and 1 _aw−γ_ [+] _[ b >]_ [ 0][. A standard measure of risk is the Arrow-Pratt coefficient of]


absolute risk-aversion [16, 161], which extracts a measure of risk-aversion that


is invariant to affine transformations as follows: [24]



_A_ ( _w_ ) = _−_ _[u][′′]_ [(] _[w]_ [)] (4.4)

_u_ _[′]_ ( _w_ )



Importantly, imposing parameter restrictions _a >_ 0, _b_ = 1 and _γ →−∞_


( [174] on equation (4.3) yields an exponential utility function _u_ ( _w_ ) = _−e_ _[−][aw]_,



with the property of _constant absolute risk aversion (CARA)_ : _A_ ( _w_ ) = _−_ _[−]_ _ae_ _[a]_ [2] _[−][e][−][aw][aw]_ =


_a_ = _ρA_ . CARA implies that the amount an agent optimally invests in a risky


asset does not depend on their wealth. In turn, assuming that agents’ util

ity functions feature can be characterized as CARA, then for random variable


_X_, provided _X ∼_ _N_ ( _µX, σX_ ) where _µX_ denotes the mean of _X_ and _σX_ de

notes the variance, it can be shown that the expected utility E[ _u_ ( _X_ )] is given


24See [138] for further information on expected utility theory and the relevance of affine transformations.


204


[180]. The agent maximizes this expected util



_−ρA_
by E[ _u_ ( _X_ )] = _−e_



_µX_ _−_ _ρA_ 2 _σX_ [2]




_ρAσX_ [2]
ity when they maximize _µX −_ 2 . Therefore, if we characterize an agent as


having exponential utility, and therefore CARA, then when they maximize this


utility when faced with a normally distributed random variable _X_, they can be


considered a _mean-variance maximizer_, with utility given by:


_U_ ( _X_ ) = _µX −_ _[ρ][A][σ]_ _X_ [2] (4.5)
2


Treating agents as mean-variance maximizers yields one tractable frame

work within which agents risk aversion, an aspect of their preferences, can be


measured. Yet there are several points to note about this approach. Firstly, as

suming that agents exhibit CARA—where their investment in a risky asset does


not depend on their wealth—may not be wholly realistic. Perhaps agents actu

ally invest a constant _proportion_ - f their wealth. Moreover, here we are implicitly


assuming that agents are not concerned with the shape of the risk, aside from


the variance, so for instance are not concerned with heavy tails. In the stablecoin


setting, this may too be an unrealistic representation of the true distributions.


We note these limitations and posit this framework as a tractable entry point for


future research.


**Method 1: one risky asset, one riskless asset**


_α_
Let us assume that an agent can invest proportion - f their wealth in a risky


asset, and proportion (1 _−_ _α_ ) in a risk free asset. [25] This would provide a total


return _X_ ( _α_ ) = _αR_ + (1 _−_ _α_ ) _r_ . Since E[ _X_ ( _α_ )] = _r_ + _α_ (E[ _R_ ] _−_ _r_ ) and _var_ ( _X_ ( _α_ )) =


25Here we are not considering the participation question about whether to invest at all, but
instead considering how, given a fixed amount to invest, this can be done optimally.


205


_α_ [2] _var_ ( _R_ ), setting _µX_ = E[ _X_ ( _α_ )] and _σX_ [2] [=] _[ var]_ [(] _[X]_ [(] _[α]_ [))][, an agent with wealth] _[ w]_


will maximize


_w_ [ _r_ + _α_ (E[ _R_ ] _−_ _r_ )] _−_ [1] (4.6)

2 _[ρ][A][w]_ [2] _[α]_ [2] _[V ar]_ [(] _[R]_ [)]


_α_
with respect to, yielding optimal solution as given in Equation 4.2. From


Equation 4.2 all that is required to compute _ρA_ is knowledge of the five vari

ables in this equation, making it a tractable place to begin with the estimation


- f agents’ preferences.


**Method two: preferences from portfolio weights**


Letting **X** _τ_ be a random return vector of _k_ risky assets, and supposing that **X** _τ_


and a vector of _p_ predictable variables **z** _τ_ jointly follow a vector autoregressive


process of order 1, the authors prove that the optimal multi-period portfolio


weights for all periods [0 _, T −_ 1] can be analytically stated. In particular, by


Corollary 2, letting **X** _τ_ = ( _Xτ,_ 1 _, Xτ,_ 2 _, ..., Xτ,k_ ) _[′]_ be a sequence of independently


and identically normally distributed vectors of _k_ risky assets ( **X** _τ ∼_ _N_ ( _µ,_ **Σ** )),


_rf,τ_ be the riskless asset return, and provided Σ is positive definite, then _∀t_ =


1 _, ...T_ :


**wT** _[∗]_ _−_ **t** [=] **1** **Σ** _[−]_ **[1]** _µ_ **ˆ** (4.7)
_ρ_ **AWT** _−_ **tΠ** **[T]** **i** = **T** _−_ **t** + **2** **[R][f]** _[,]_ **[i]**


where ˆ _µ_ = _µ_ _−_ _rf,T_ _−t_ +2 **1**, which can be rearranged to yield an explicit expres

sion for _ρA_ :


206


_ρA_ = 1 **Σ** _[−]_ [1] _µ_ **ˆ** (4.8)
**wT** _[∗]_ _−_ **t** **[W][T]** _[−]_ **[t][Π][T]** **i** = **T** _−_ **t** + **2** **[R][f]** _[,]_ **[i]**


On this approach, provided data is available on agents’ portfolio weights


through time, a value for _ρA_ could potentially be calibrated more precisely than


method one would allow; however, this data requirement in itself is more de

manding. In particular, in the context of stablecoins, for example, the possi

bility that one agent uses multiple blockchain addresses would obfuscate the


true portfolio weights through time. However, to the extent that future work is


able to accurately determine these weights, this offers a promising approach to


calibrate values of _ρA_ .


**Empirical case study of Method 1**


To illustrate how these utility function estimation techniques can be applied, we


provide a minimal working example, applying method 1 to MakerDAO [134].


A core component of the Maker stablecoin system is the issuance of a stable

coin against the value of collateral. In particular, down to a threshold value of


150%, agents choose how much stablecoin to issue as debt against their collat

eral. For example, for 150 USD worth of ETH collateral, at the 150% threshold


an agent can issue up to 100 USD of stablecoin debt. However, if the ETH/USD


price falls, then the agent would become undercollateralized relative to the


150% threshold, and would incur liquidation costs. On the converse—and one


- f the primary use cases of such a stablecoin—if the agent repurchases more


ETH with their debt, the agent has accessed leverage. If the ETH/USD price


rises, then the agent will stand to benefit more from this price increase than if


207


they had not issued themselves debt.


Thus, following method 1, in this section the goal is to estimate equation


(4.2). We proceed with the following demonstrative steps.


1. **Data collection.** We use the MakerDAO GraphQL API [135] to obtain data


   - n Collateralized Debt Position (CDP) actions. [26]


2. **Data cleaning and sample selection.** We clean the data, focusing only on


Externally Owned Accounts prior to the launch of multi-collateral DAI.


We further only consider CDPs with more than 50 USD of collateral.


3. **Wealth calculation (** _w_ **).** We assume that each time an agent issues them

selves with the stablecoin, this is used to buy more ETH. Therefore for


each agent we calculate their total wealth as the sum of their ETH hold

ings (ETH collateral and ETH bought with stablecoin) less their debt.


4. **Risky asset holding (** _α_ **).** We calculate the ratio of ETH holdings to original


ETH collateral. Leverage is represented as _α >_ 1.


5. **Computation of mean and variance of risky asset (** E[ _R_ ] **and** _V ar_ ( _R_ ) **).** We


compute the mean and variance of the risky asset by computing the cu

mulative rolling moving average mean and variance of daily ETH/USD


returns.


6. **Assumption of a risk free rate (** _r_ **).** We assume that the investor has access


to a risk-free interest rate of 2% annually.


26This API only covers the stablecoin SAI, the precursor to DAI.


208


#### **4.7.6 Cross-chain and Synthetic Assets**

Synthetic assets use the same mechanisms as non-custodial stablecoins but with


different target pegs (e.g., dYdX’s perpetuals using synthetic BTC). In compar

ison, cross-chain mechanisms transfer assets between blockchains. Where both


blockchains are able to verify state of the other, cross-chain assets do not re

quire collateral as the issue and redeem procedures can be executed through


transaction inclusion proofs via a chain relay on each blockchain (e.g. PeaceRe

lay [127]). Hence, incentive design for cross-chain mechanisms is not required


to maintain a price peg, but rather to keep the relays on each side up-to-date


and protected against attacks such as relay poisoning [190, 128].


If a cross-chain mechanism enables asset transfers (i.e., not atomic swaps)


from a blockchain which does _not_ have the ability to verify the state of another


blockchain (e.g., Bitcoin) to one that does (e.g., Ethereum), collateral or trust


in a third party is required. [27] These cross-chain mechanisms utilize interme

diaries that hold custody over the locked asset. We can distinguish between


trusted non-collateralized intermediaries where custodial models can be ap

plied (e.g., wBTC) and non-custodial cross-chain mechanisms (e.g., XCLAIM,


tBTC, RenBTC). Non-custodial designs rely on collateral for incentive security


in addition to collateral of the transferred asset itself.


Exogenous collateral without governance assets (e.g. XCLAIM [190, 91]) can


be modelled using the capital structure models without considering the long

term impact of governance token value. Models that use exogenous collateral


for the transferred asset in combination with endogenous collateral for incen

tives (e.g. tBTC), might be subject to a similar governance token value problem


27For a formal proof of this requirement see [189].


209


as outlined in 4.5.1. However, in both cases the underlying asset is insured by


exogenous collateral and hence the design provides protection of the transferred


assets independent of the success of the cross-chain mechanism. Endogenous


collateral structures, on the other hand, are subject to the same incentive sustain

ability issues that rely on an increasing governance token value (e.g. RenBTC).


Here, the security of the transferred asset relies on the long-term success of the


cross-chain mechanism to disincentivize attacks.


210


CHAPTER 5


**CASCADING LOSSES IN REINSURANCE NETWORKS**


The content of this chapter has previously appeared in:


“Cascading Losses in Reinsurance Networks.” Ariah Klages-Mundt


and Andreea Minca. _**Management Science**_, 66(9):4246-4268, 2020.


211


We develop a model for contagion in reinsurance networks by which pri

mary insurers’ losses are spread through the network. Our model handles gen

eral reinsurance contracts, such as typical excess of loss contracts. We show


that simpler models existing in the literature–namely proportional reinsurance–


greatly underestimate contagion risk. We characterize the fixed points of our


model and develop efficient algorithms to compute contagion with guarantees


- n convergence and speed under conditions on network structure. We char

acterize exotic cases of problematic graph structure and nonlinearities, which


cause network effects to dominate the overall payments in the system. We lastly


apply our model to data on real world reinsurance networks. Our simulations


demonstrate the following:


  - Reinsurance networks face extreme sensitivity to parameters. A firm can


be wildly uncertain about its losses even under small network uncertainty.


  - Our sensitivity results reveal a new incentive for firms to cooperate to pre

vent fraud, as even small cases of fraud can have outsized effect on the


losses across the network.


  - Nonlinearities from excess of loss contracts obfuscate risks and can cause


excess costs in a real world system.

#### **5.1 Introduction**


The London market excess of loss (LMX) spirals of the 1980-90s revealed how


global interconnections among reinsurers (i.e., insurers who insure other insur

ers) can cause contagion in the reinsurance market [21]. There was high concen

tration of losses despite the belief that all parties were properly insured. A series


212


Major

Storms


## **LMX Spirals 1980s-90s**

Primary Insurers



Flow of insurance risk

Triggered payouts


Figure 5.1: Diagram of LMX reinsurance spirals.


- f major storms caused tail losses to the London insurance market (Lloyd’s in


particular). While risks in the London market were reinsured outside the UK,


retrocession (i.e., reinsurance on reinsurance) brought these losses back to the


London market, resulting in unexpected concentration of losses. Figure 5.1 vi

sualizes these interconnections.


After these events, the industry mitigated spiral risks by reducing the size


- f the retrocession market. Today, there is a sense in insurance that the risk of


spirals is largely a thing of the past and that risks are properly shared with rein

surers. To our knowledge, no reinsurance risk models used in industry directly


account for these network effects. By applying the machinery we develop in this


paper to estimates of the current US reinsurance system, we show that the rein

surance market is, in fact, not safe to network effects. We show such network


effects can dominate the tail behavior of the system in ways that are difficult to


predict. The US has insurance guaranty mechanisms that protect policyholders


in case of insurance company insolvency. Our results are even more relevant in


213


this case because the spiraling losses would be borne by the state.


We propose a model for contagion in reinsurance markets by which primary


insurers’ losses are spread throughout the network. Despite a vast literature


- n contagion in financial networks (see e.g., [75], [2], [76]), no existing conta

gion models are general enough to cover reinsurance contracts. The majority of


financial network models are limited to simple contexts in which network in

teractions are representable by debt or equity contracts between entities. Very


little work has extended these models to more complicated derivatives whose


payoffs in equilibrium depend on the liabilities and counterparty risk across


the network. As a notable exception, [170, 172, 171] demonstrate difficulties in


clearing networks with credit default swaps in addition to initial debt contracts.


Reinsurance contracts differ from debt contracts in that we do not outright know


their liabilities. Reinsurance contracts differ from credit default swaps in that


contract liabilities are not related to default events. Instead, the liabilities of


reinsurance contracts are interrelated and nonlinear, which can lead to difficul

ties in determining equilibrium payoffs and to multiple solutions. Our model


ventures far beyond the settings and results of [75] and [2] as it, in general, re

quires working with matrices with arbitrarily large column sums as opposed to


column sums _≤_ 1.


[34] developed one of the first network models for reinsurance contagion;


however, they assume that reinsurance contracts are proportional contracts as


- pposed to the more common excess of loss contracts (we provide more back

ground on these types of contracts in the next section) and that reinsurance con

tracts do not cover liabilities from other reinsurance contracts, which limits the


propagation of losses to two steps in the network. These assumptions remove


214


exotic behavior from the system, such as reinsurance spirals, which we show


can play a critical role. Under these assumptions, they provide large deviation


results for the loss in the system. In contrast, we focus on a more general set

ting that handles a wide variety of reinsurance contracts that exist in the real


world, including the more common excess of loss contracts. Our simulations


comparing excess of loss networks with proportional networks further show


that this assumption in [34] dangerously underestimates contagion risk in real


reinsurance networks.


[24] develops a dynamic framework for contingent claims that can accom

modate some reinsurance contracts. However, the reinsurance contracts in their


model cannot have caps. [117] develop a bipartite graph model of tail risk in


insurance. However, their model does not include reinsurance.


[80] describes the sensitivity of payment equilibria in [75] to small variations


in the interbank liabilities. In contrast, our focus is on the reinsurance model


that produces these liabilities. Further, we show that these liabilities can have


wild variations from small uncertainties in network parameters.


In addition to developing a contagion model for reinsurance networks, our


contributions include the following:


  - We establish efficient algorithms to compute contagion with guarantees


   - n convergence and speed under conditions on network structure.


  - We characterize exotic cases of problematic graph structure and nonlin

earities, which cause network effects that dominate the overall payments


in the system. We relate reinsurance spirals to structural properties of the


network, such as the existence of graph cycles that recirculate large pro

215


portions of reinsurance losses. Further, we show that these cycles can be


very complicated interactions of simple graph cycles.


  - We apply our model to real world reinsurance networks using data pro

vided by the National Association of Insurance Commissioners (NAIC).


Our simulations show that, using real world data, nonlinearities in conta

gion can cause extreme uncertainties. We demonstrate that even if a firm


has unreasonably precise information [1] (i.e., with small uncertainty) about


the global structure of the system, it can still be wildly uncertain about


the losses it will face from a given shock. We further demonstrate that


these nonlinearities can cause excess costs in a real world system–i.e., the


insurance-reinsurance system could be structured differently to perform


its function to protect real world infrastructure more efficiently.


We conclude by introducing three promising starting points for solving real


world issues that our results reveal: using distributed systems to control fraud,


using network features to predict risk exposure, and designing markets to lower


systemic costs.

#### **5.2 Reinsurance Contagion Model** **5.2.1 Primer on reinsurance contracts**


Reinsurance contracts are insurance contracts that insurance companies take out


to protect against large losses on their insurance portfolios. In **primary reinsur-**


1In the extreme, some real contracts are ambiguous to the degree that the parties to the contract themselves do not even know the contract parameters. We will discuss this further later in
the paper.


216


**ance**
, the insurance company protected by the reinsurance is a primary insur

ance company. In **retrocession reinsurance**, the insurance company protected


by the reinsurance is another reinsurance company. These reinsurance contracts


are typically partly collateralized, meaning that, in the event that the reinsurer


defaults on their obligations, the reinsured firm still has recourse to the collat

eral. Most reinsurance contracts in property and casualty are treaty contracts,


which insure against losses from the reinsured company’s entire insurance port

folio. Alternatively, in a niche case that we will not consider, some contracts


have more specialized coverage of facultative risks.


The most common form of treaty reinsurance is an **excess of loss (XL)** con

tract, in which the reinsurer covers losses on the reinsured above a deductible


(or attachment point). These contracts also commonly have caps (or limits) on


the payouts of the contract. The total coverage of a firm is typically split into


multiple deductible-cap layers in a tranche structure. Multiple reinsurers typi

cally split each layer, taking fractions of the coverage. Together, the layers form


a tower.


Another treaty contract is **proportional** reinsurance. These have no de

ductibles or caps, and the reinsurer takes on a percentage of the liabilities of


the reinsured according to a coinsurance rate.

#### **5.2.2 Two contagion mechanisms**


Reinsurance contracts between a set of insurance companies form a network.


Exogenous liabilities to a subset of primary insurers constitutes a shock to this


network. This shock may activate the reinsurance to the primary insurers,


217


which can in turn activate a cascade of retrocession reinsurance. Figure 5.2a


- utlines this **liability propagation** mechanism. The equilibrium of this pro

cess gives a network of liabilities between firms. Given their available capital,


some firms may be unable to pay these liabilities. These firms default, poten

tially with extra default costs representing the legal, transactional, and liquidity


costs of default. Each default negatively affects the capital of neighboring firms


as these firms receive less on the liabilities they are owed. This can trigger a


secondary cascade of defaults. Figure 5.2b outlines this **default propagation**


mechanism. An equilibrium of this second process is a clearing payment vector


to the liability network.


Given a shock, we aim to determine the equilibrium reinsurance payments


from a complex interconnection of contracts. Unlike the case of a debt network


in [75], we do not outright know the liabilities of each contract, so we cannot


directly calculate a clearing payment vector. In a reinsurance network, the li

abilities are interrelated and nonlinear. The difficult problem in this case is to


determine the equilibrium liabilities given a shock, after which we can solve for


a clearing payment vector as in [75]. The process for calculating contagion is


then as follows:


1. Given a primary insurance shock, calculate the equilibrium reinsurance


liabilities.


2. Apply the available collateral from reinsurance contracts to fulfill or par

tially fulfill liabilities.


3. Given the remaining capital of firms, clear the remaining liabilities in the


network.


218


**Reinsurance Liability Propaga6on**


**Primary Insurers** **Reinsurers**


1. Claims > deduc/ble trigger


2. Reinsurance claims > deduc/ble


trigger retrocession contracts


3. Retrocession contracts


interact un/l next cap is met

                           - r next deduc/ble is not met


(a) Liability propagation in a reinsurance network.


**Clearing Default Propaga6on**

**Primary Insurers** **Reinsurers**


3. Lower capital can cause next firm

to default, propaga/ng the effect


2. Default lowers clearing

payment, decreasing capital

                              - f other firms


1. If liability > capital, firm

defaults, triggering default cost


(b) Default propagation in a liability network.


Figure 5.2: Propagation mechanism diagrams.


We proceed in this paper by developing the machinery to handle the missing


piece of the puzzle: the first step. This problem is much more general than


related problems formulated in [75] and [2] and involve matrices with column


sums _>_ 1.


219


#### **5.2.3 Network definitions**

We define the **reinsurance network** as follows:


 - _n_
nodes of primary insurance and reinsurance firms


 - _m_
edges represent reinsurance contracts between firms, directed from


reinsurer to reinsured firm. Edges are described by the following weight


matrices


 - Γ _n × n_ matrix of coinsurance rates on contracts (0 if no contract between


parties)


 - _DD n × n_
matrix of deductibles (also called ‘attachment points’) on rein

surance contracts (0 if no contract between parties)


 - _CP n × n_ matrix of reinsurance caps (also called ‘limits’) on contracts (0 if


no contract between parties). This is the maximum payout of the contract


 - _sh_ vector representing shocks to primary insurers.


 - _e_ 0 vector representing initial capital (also called ‘equity’) values of each


firm available to payout liabilities


We assume the graph is connected, as we can otherwise handle the compo

nents separately. We also assume that firms can only reinsure up to 100%: i.e.,


the column sums of Γ corresponding to a particular layer of reinsurance sum to


_≤_ 1. This is a reasonable assumption as otherwise the contract ceases to serve as


insurance and the insured company stands to profit from taking on large losses


to their portfolio. This assumption is a standard requirement in insurance con

tracts.


220


Reinsurance Network on Firms



Line Graph Network on Contracts













(a) Example reinsurance network.



(b) Example line graph network.



Figure 5.3: Example line graph network transformation.


We will work with the line graph of the network, i.e., the graph that repre

sents edges of the original graph as nodes in the new network and has directed


edges when the head of an edge in the original network intersects the tail of


another edge in the original network. We define the **line graph network** as


follows:


 - _m_
nodes representing contracts (i.e., edges) in the reinsurance network


 - _X m × m_
adjacency matrix of the line graph, 1-0 weighted


 - _ℓ_ liability vector on contracts


 - _d_ deductibles vector on contracts


 - _c_ caps vector on contracts


 - _s_ shock vector on contracts


 - _γ m × m_ diagonal matrix of reinsurance rates on contracts


The following example describes the transformation to the line graph network.


221


**Example 5.1.** _Consider the reinsurance network in Figure 5.3a. Figure 5.3b shows the_


_resulting line graph structure. In the original reinsurance network, suppose we have_



















20



0 0 0



0 0 0



0 0 0









_._










_, sh_ =










_, CP_ =




Γ =









0 _._ 5 0 0



_, DD_ =




100 0 0



10 0 0



0


0



0 100 0



0 0 _._ 5 0



0 10 0



_Then the line graph network becomes_







 _, γ_ =







 _, c_ =







 _, s_ =







_._








 _, d_ =







10


10





_X_ =







0 0


1 0









0 _._ 5 0


0 0 _._









100


100









20


0





1 0



0 0 _._ 5



10



100



0



The line graph network serves to consider the system as a network of con

tracts instead of a network of firms. We define a **financial system** in terms of


its line graph network ( _X, γ, d, c, s_ ) (sometimes omitting the _c_ if we are in the


domain of infinite caps) as that is the machinery we will need in our theorems


and algorithms; however, it can equivalently be defined in terms of the adja

cency graphs of the reinsurance network (Γ _, DD, CP, sh_ ). Note that since _γX_


is nonnegative, the Perron-Frobenius theorem gives us that the spectral radius


_ρ_ ( _γX_ ) = _λmax_ ( _γX_ ). We will show in the next section how to calculate the result

ing equilibrium liabilities matrix _L_ (or equivalently liabilities vector _ℓ_ in the line


graph network) giving liability weights on contracts in a financial system.

#### **5.3 Network Liabilities** **5.3.1 Liabilities without contract caps**


In the case that each contract has a deductible but no cap (equivalently, each


contract has an infinite cap, and so there is no layering of reinsurance), liabilities


222


- n contracts equal the sum of direct shocks - deductibles + cross-effects from the


network, multiplied by _γ_ and with a floor at zero. I.e., the equilibrium liabilities


_ℓ_ is a fixed point to the equation


Φ( _ℓ_ ) = _γ_ ( _s_ + _Xℓ_ _−_ _d_ ) _∨_ 0 _._


Define _B_ ( _ℓ_ ) as the _m × m_ diagonal matrix with 1-0 entries indicating which


contracts are activated (i.e., have surpassed the deductible) under _ℓ_ . Specifically,


_B_ ( _ℓ_ ) _ii_ = 1 if ( _Xℓ_ + _s −_ _d_ ) _i ≥_ 0 and 0 otherwise. We define a _B_ **-constant set** to


be the subset of the domain such that _B_ is a given constant value–i.e., the pre

image of a particular _B_ . We will mostly work with _B_ - constant sets, so we will


refer to _B_ ( _ℓ_ ) as simply _B_ . With this terminology, Φ is equivalent to


Φ( _ℓ_ ) = _γB_ ( _Xℓ_ + _s −_ _d_ ) _._


Note that this Φ is nonnegative, monotone increasing (i.e, nondecreasing),


and convex as it is the composition of an increasing affine function and a non

negative, increasing convex function (pointwise maximum). This instance of


the problem is similar to the problem considered in [75] but without a general


upper bound. We solve it in similar ways but provide more direct proofs.

#### **5.3.2 Liabilities with contract caps**


In the more general case in which each contract has a deductible and a cap (pos

sibly infinite), there can be multiple layers of reinsurance. Adding the capping


effect to the setup started above, the liabilities vector _ℓ_ is a fixed point to the


equation


Φ( _ℓ_ ) = _γ_ ( _Xℓ_ + _s −_ _d_ ) _∨_ 0 _∧_ _c._

            -            

223


We define the following


 - _C_ ( _ℓ_ ) is the _m × m_ diagonal matrix with 1-0 entries indicating which


edges have surpassed their caps (and so no longer activated); specifically,


_C_ ( _ℓ_ ) _ii_ = 1 if _γ_ ( _Xℓ_ + _s −_ _d_ ) _ii ≥_ _cii_ and 0 otherwise.


 - Ψ( _ℓ_ ) is a map to a system on the zero diagonal coordinates of _C_ ( _ℓ_ ). Essen

tially, Ψ( _ℓ_ ) is ( _I −_ _C_ ( _ℓ_ )) where we have dropped the zero rows.


  - Dropping dependence on _ℓ_, ˜ _γ_ = Ψ _γ_ Ψ _[T]_, _B_ [˜] = Ψ _B_ Ψ _[T]_, _X_ [˜] = Ψ _X_ Ψ _[T]_,


 - _ℓ_ [¯] = _Cc_, ˜ _v_ = Ψ( _Xℓ_ [¯] + _s −_ _d_ ).


We define a ( _B, C_ ) **-constant set** to be the subset of the domain such that both


_B_ and _C_ are given constant values–i.e., the intersection of the pre-image of a


particular _B_ and the pre-image of a particular _C_ . We will mostly work with


( _B, C_ )-constant sets, so we will refer to _C_ ( _ℓ_ ) and Ψ( _ℓ_ ) as simply _C_ and Ψ. With


this terminology, Φ is equivalent to


Φ( _ℓ_ ) = ( _I −_ _C_ ) _γB_ _X_ ( _I −_ _C_ ) _ℓ_ + _XCc_ + ( _I −_ _C_ )( _s −_ _d_ ) + _Cc_

          -           

= Ψ _[T]_ _γ_ ˜ _B_ [˜] ( _X_ [˜] Ψ _ℓ_ + ˜ _v_ ) + _ℓ._ [¯]


Unlike the simpler Φ without contract caps, which is a subcase of the more


general setting, the Φ with contract caps is not generally convex. It remains


monotone increasing, however. This problem is similar to the problem consid

ered in [2]; however, their methodology is limited to the case in which column


sums for the network interaction matrix are _≤_ 1. In the general case of reinsur

ance layering, column sums of _γX_ can be arbitrarily high. We develop machin

ery to handle this much more general setting.


Unless specifically pointed out, we will work with the general form of Φ


with contract caps.


224


#### **5.3.3 Unique fixed point**

We characterize conditions under which a unique fixed point exists in Theo

rem 5.3. To construct the proof, we will need the following lemmas.


**Lemma 5.1.** _A linear system with matrix A is a contraction with respect to some norm_


_if and only if the spectral radius ρ_ ( _A_ ) _<_ 1 _. Further, this norm ∥· ∥s can be taken to be_


_a weighted Euclidean norm of the form ∥y∥s_ = _∥My∥_ 2 _, where M is a square invertible_


_matrix._


A proof of Lemma 5.1 can be seen in, for example, Appendix B of [31].


**Lemma 5.2.** ( _B, C_ ) _-constant sets are convex and form a finite partition of the space_


_{ℓ|ℓ_ _≥_ 0 _}._


See proof in the Appendix.


We now define the terms used in the theorem:


  - Let _K_ ( _X, γ, d, c, s_ ) be the set of ( _B, C_ ) pairs such that the ( _B, C_ )-constant


set is nonempty. I.e., for ( _B, C_ ) _∈K_, there is a feasible _ℓ_ such that _B_ ( _ℓ_ ) = _B_


and _C_ ( _ℓ_ ) = _C_ . Notice that there is no feasible _ℓ_ such that _B_ ( _ℓ_ ) = 0 and


_C_ ( _ℓ_ ) = _I_ as the activation of all caps means that all deductibles are also


met. Contracts in different layers reinsuring the same firm also cannot


simultaneously be activated: we only reach the second layer if the first


layer has reached its cap. Additionally, unless all caps are infinite, _B_ = _I_


and _C_ = 0 is not feasible.


  - Let Ω( _X, γ, d, c, s_ ) be the element-wise maximum over all ( _B, C_ ) _∈K_  - f


the matrices


225


( _I −_ _C_ ) _γBX_ ( _I −_ _C_ ). Notice that ( _I −_ _C_ ) performs the same function


as the Ψ map here; however, it maintains zero rows and columns, making


the result comparable across different ( _B, C_ ) pairs. Notice that


( _I −_ _C_ ) _γBX_ ( _I −_ _C_ ) = Ψ _[T]_ _γ_ ˜ _B_ [˜] _X_ [˜] Ψ _._


We will use this tilde notation to simplify the algebra. To distinguish be

tween tilde notation from different Ψ( _C_ ), we will use different subscript


notations. E.g., For ( _B_ 1 _, C_ 1) _∈K_, Ψ1 := Ψ( _C_ 1) and ˜ _γ_ 1 := Ψ1 _γ_ Ψ _[T]_ 1 [.]


**Theorem 5.3.** _Let_ ( _X, γ, d, s, c_ ) _be a financial system and_


Ω:= _∧_ ( _B,C_ ) _∈K_ ( _I −_ _C_ ) _γBX_ ( _I −_ _C_ )


_be the matrix element-wise maximum. Then if ρ_ (Ω) _<_ 1 _, there is a unique fixed point_


_to_ Φ( _ℓ_ ; _X, γ, d, s, c_ ) _._


The idea behind this condition is that not all ( _B, C_ ) pairs are feasible–in par

ticular, if some caps are finite, we will never have to work with all of _γX_ at


- nce–and so we only need to consider the worst cases of the feasible pairs to


construct a dominating linear map. Then if the dominating linear map gives a


contractive norm on the whole space, the Banach fixed point theorem gives us


uniqueness. The proof is provided in the Appendix.


The following corollary describes a more intuitive condition on the spectral


radius of the ‘full’ graph _γX_ . However, this simpler condition does not cover


general layering structure. In particular, column sums are restricted to _≤_ 1.


Notice that the only condition of the corollary is that _ρ_ ( _γX_ ) _<_ 1, which further


means that any such system leads to a unique fixed point for every possible


shock.


226


**Corollary 5.1.** _Given a financial system_ ( _X, γ, d, c, s_ ) _, if the spectral radius_


_ρ_ ( _γX_ ) _<_ 1 _, there is a unique fixed point to_ Φ _._


In the case of all infinite caps (i.e., effectively no caps), Corollary 5.1 gives a


result similar to Theorems 1 and 2 in [75]. We note that our proof is more direct


and general. The more general condition on the spectral radius of _γX_ enables


the more powerful Banach fixed point theorem to prove the result directly. This


method can apply to a broader set of problems, whereas the proof in [75] re

quires minutiae of the specific contagion mechanism and the relations between


different firms to arrive at the result.


The general case of Corollary 5.1 is similar to Proposition 1 in [2], which con

siders clearing vectors in a liabilities network with external senior debt. How

ever, the theorem in [2] only applies to matrices of connectivity with all en

tries strictly positive since the proof relies on the positive version of the Perron

Frobenius theorem. To handle non-negative matrices, we need to require the


spectral radius be _<_ 1 since eigenvalues can otherwise be 1.


Theorem 5.3 and the results we derive in the following sections venture well


beyond the setting and results in [2] to describe fixed points that apply for the


full range of layering structure that can be seen in reinsurance networks. In


particular, we need to allow column sums of _γX_ to be _>_ 1 since there can be


multiple complete layers of reinsurance.


A natural question is whether we can strengthen Theorem 5.3 to a wider


setting. Conditioning on _ρ_ (Ψ _γBX_ Ψ _[T]_ ) _<_ 1 for all ( _B, C_ ) pairs that partition


the domain into non-empty ( _B, C_ )-constant sets (and recalling that _C_ defines


Ψ), Φ is everywhere a local contraction–i.e., Φ is a contraction restricted to each


227


( _B, C_ )-constant set by some metric. We can further show that Φ is globally non

expansive. We conjecture that, under these conditions, Φ has a unique fixed


point. However, this problem is more challenging because we need to estab

lish a metric over which the function is globally contractive in order to use the


existing machinery. We leave this as further work.

#### **5.3.4 Other cases: unique, multiple, and no fixed points**


Problematic graph structure can cause Φ to be non-contractive. This occurs


when circular sequences of contracts allow 100% reinsurance to be continually


recirculated through a given set of nodes. We will refer to an instance of this


as a ‘ **100% cycle** ’. Cycle here refers to the graph theoretic meaning as opposed


to the economic meaning. Figure 5.4 provides three examples of how this can


happen. Figure 5.4a is the simplest example that directly recirculates 100% rein

surance around one cycle. Figure 5.4b shows that multiple cycles can interact


to recirculate 100% reinsurance to a central node. Figure 5.4c shows that in the


most extreme case of a complete graph with all Γ = 1 _/_ ( _n −_ 1), 100% reinsurance


can be recirculated to every node in the network: as all weights are 1 _/_ 2, the rein

surance that can be recirculated to each node can be a geometric sequence that


converges to 1.


**100% cycles: no caps case**


For simplicity, we first describe the effects of these 100% cycles from the per

spective of a system with infinite/no caps, in which _γX_ mostly describes the


entire system.


228


Primary Insurer Reinsurers


(a) A direct 100% cycle.





Reinsurers





(b) 100% cycle from two interacting cycles.


Reinsurers







Γ = 1/2



(c) Many interacting cycles can form a 100% cycle.


Figure 5.4: Some examples of 100% cycles.


Analytically, these 100% cycles cause the matrix powers ( _γX_ ) _[k]_ to fail to con

verge to 0 as _k →∞_ since we enter an infinite increasing loop. On the other


hand, the condition on the spectral radius _<_ 1 from Corollary 5.1 ensures that


lim _k→∞_ ( _γX_ ) _[k]_ = 0. Checking the spectral radius is a simple check of whether


a 100% cycle exists; however, it may be difficult to identify the actual cycle in


the network. As shown by the examples in Figure 5.4, a problematic cycle can


be a complex interaction of many graph cycles. A naive method to search for


the problematic cycle would involve iterating over graph cycles in the network,


which is itself NP-hard.


If _ρ_ ( _γX_ ) _≥_ 1 in this setting, a 100% cycle exists. In this case, there may still


be a unique fixed point. If not, there may be a smallest fixed point or there may


be no fixed point. The following characterize these cases and follow from the


229


main theorems in this section.


**Unique fixed point if 100% cycles are not activated.** The term _B_ in _γBX_


serves to remove edges from the resulting graph. Since the spectral radius of


a proper subgraph is less than the spectral radius of the initial connected graph,


we may have local contraction on some _B_ - constant sets, but not on the whole


_s_
domain. Depending how far the shock spreads, there may still be a unique


fixed point on the contractive _B_ - constant sets. In this case, 100% cycles that


cause the spectral radius to be _≥_ 1 are not activated. We can restrict the domain


to the contractive region to find a unique fixed point. Notably, such a system


will not yield a fixed point for all possible shocks.


**No fixed point if 100% cycles are activated.** When 100% cycles are activated


by shocks, the system is non-contractive. In this case, there is no fixed point,


and some nominal liabilities will increase to infinity as contracts call circularly


in 100% cycles. For example, say that the primary insurer faces a shock of 10


in Figure 5.4a. Then this loss is passed around the cycle because the reinsur

ance rate is 100%. The first reinsurer faces a loss of 20, which is again passed


around the cycle, and so on. Since Φ is monotone, these “infinite” fixed points


are the only cases of nonexistence. This could happen but is extremely unlikely


in practice. The only contracts without caps are proportional and not reinsured


at 100%. A 100% cycle in this case would be quite contrived.


**Multiple fixed points from self-reinforcing claims.** If 100% cycles have their


deductibles exactly met from outside claims but are otherwise unactivated, we


have multiple solutions. A simple example of this is a 100% cycle with zero de

230


ductibles and zero outside claims. Any value on these contracts is self-fulfilling,


and so there are infinitely many fixed points. Notice that each 100% cycle is


self-contained due to the assumption that no firm can reinsure over 100%. This


means that the self-fulfilling solutions in each such cycle are independent. Then


the set of fixed points looks like a Cartesian product of individual solution sub

sets related to the 100% cycles in the network that have deductibles exactly met


by outside claims.


**100% cycles: general caps case**


Corollary 5.1 tells us cases in which we can prove unique fixed points for all


shocks. Theorem 5.3 covers more cases. Outside of these theorems, there may


still be unique fixed points in other systems: in some cases if the shocks do


not activate problematic network structure, and in other cases there may be no


problematic network structure to worry about. When we are not guaranteed


uniqueness, we can see similar effects as in the no caps case of multiple fixed


points or no fixed points. The following characterize these situations and follow


from the main theorems in this section.


**Caps limit non-contractive effects.** Even if 100% cycles are activated, finite


contract caps can limit the non-contractive effect to particular layers that reach


capacity. In this case, the finite caps remove the problematic graph structure


from the remainder of the problem.


**Multiple fixed points bounded within layers.** If a 100% cycle has deductibles


exactly met from outside claims but remains otherwise unactivated, we have


231


multiple solutions as before. However, these solutions are constrained by the


caps and restricted to self-reinforcing liabilities within particular layers of rein

surance.


As we will see in the following subsections, in the case of multiple fixed


points, there is always a least fixed point that represents the real world solution.


Other fixed points are mathematical artifacts from self-reinforcing liabilities that


are not propagations of primary insurance claims.


**No fixed point if uncapped 100% cycle is activated.** As before, the only in

stances of nonexistence are when fixed point iteration diverges to infinity on


some liabilities. This only happens when an uncapped 100% cycle is activated.


Since Φ is monotone, all other problematic structures are eventually capped out


and so do not contribute to nonexistence. For the same reasons as before, this is


extremely unlikely to occur in practice.

#### **5.3.5 Least fixed points**


In the event that we have multiple solutions, there is a least fixed point as the


- thers are self-fulfilling and not caused by actual claims. This is formalized in


the following theorem.


**Theorem 5.4.** _For financial system_ ( _X, γ, d, c, s_ ) _, if a fixed point of_ Φ( _ℓ_ ; _X, γ, d, c, s_ )


_exists, then there is a least fixed point. Further, fixed point iteration starting at 0 con-_


_verges to the least fixed point._


Note that the Tarski fixed point theorem cannot be used in this setting be

232


cause the domain lattice is not necessarily bounded above. Instead, our proof


relies on the Kleene fixed point theorem. The Kleene fixed point theorem is ad

ditionally constructive, and so guarantees that fixed point iteration converges


to the least fixed point if it exists. We present the proof of Theorem 5.4 in the


Appendix, including an overview of the Kleene fixed point theorem.


The next theorem gives us a conditions under which we can apply the Tarski


fixed point theorem, in which case we know outright that a least (and greatest)


fixed point exists.


**Theorem 5.5.** _Let_ ( _X, γ, d, c, s_ ) _be a financial system. Let_ Ψ0 _map to a system on the_


_edges with infinite caps (or map to the zero matrix if all caps are finite). Then if the_


_spectral radius ρ_ (Ψ0 _γX_ Ψ _[T]_ 0 [)] _[ <]_ [ 1] _[,]_ [ Φ] _[ has least and greatest fixed points.]_


See proof in the Appendix.


Note that this means that, if all caps are finite, there is always a maximum


fixed point. This means that liabilities cannot spiral to infinity. In practice, most


reinsurance contracts have caps, and so there will be a resulting equilibrium


liability structure.


We have provided a wide variety of cases for which we are guaranteed least


fixed points. In the next subsection, we show that the least fixed point is the real


world solution of interest.

#### **5.3.6 Multiple fixed points: net liabilities equal**


Recall that _L_ is the equilibrium firm-to-firm liabilities matrix. Rows represent


liabilities from the row firm to each column firm. Define the net liabilities of


233


each firm as a vector


∆( _L_ ) := _L_ _[T]_ _e −_ _Le,_


where _e_ is the all ones vector. ( _L_ _[T]_ _e_ ) _i_ is what _i_ is due from other firms. ( _Le_ ) _i_ is


what _i_ - wes to other firms. The following theorem shows that net liabilities of


Φ.
firms are constant across multiple fixed points of


**Theorem 5.6.** _If L, L_ _[′]_ _are fixed points of_ Φ _, then_ ∆( _L_ ) = ∆( _L_ _[′]_ ) _. I.e., the net liabilities_


_of each firm are equivalent under any fixed point._


We will need the following two lemmas to prove the theorem.


**Lemma 5.7.** _If L, L_ _[′]_ _are fixed points of_ Φ _with L ≥_ _L_ _[′]_ _(entry-wise), then_ ∆( _L_ ) _≤_


∆( _L_ _[′]_ ) _._


**Lemma 5.8.** _If L is a fixed point of_ Φ _, then_ [�] _i_ [∆] _[i]_ [(] _[L]_ [) = 0] _[.]_


See proof of Lemma 5.7 and proof of Lemma 5.8 in the Appendix. Lemma 5.8


is rather immediate because the reinsurance system does not amplify losses–it


- nly distributes losses across the network. As the initial shock is not included in


_L_, the terms in _L_ sum to 0. Once we have established these lemmas, the proof of


Theorem 5.6, which is included in the Appendix, is similar to that of Theorem 1


in [75].


As net liabilities are equivalent between fixed points, the least fixed point


corresponds to the real world solution. It represents the propagation of primary


insurance shocks, whereas other fixed points add self-fulfilling liabilities on top


- f this. To see this, note that fixed point iteration starting from zero represents


stepwise propagation of primary insurance shocks and converges to the least


fixed point. Then, from Theorem 5.6, any greater fixed points can only come


from adding additional liabilities that net out.


234


### Primary Insurer Reinsurers

Γ = 1

d = 0


Γ = 1

d = 10


Figure 5.5: Example in which different fixed points lead to different clearing
payments.

#### **5.3.7 Consequences of multiple fixed points**


Note, however, that Theorem 5.6 does not imply that the _clearing_ - f different


fixed point liabilities are equivalent. In general, the clearing will depend on the


_nominal_ liabilities as opposed to the net liabilities. Figure 5.5 gives an example


where different fixed points lead to different clearing outcomes. The liability


- n edge ( _B, A_ ) is _LBA_ = 10 in any fixed point. However, _LCB_ = _LBC_ = 0 and


_LCB_ = _LBC_ = 10 are both valid fixed points (the net liabilities are the same for


both fixed points ∆ _LA_ = _−_ 10, ∆ _LB_ = 10, ∆ _LC_ = 0). If the capital of firm _B_


has zero value, _A_ will receive zero payment after clearing in the minimum fixed


point whereas in the _LCB_ = _LBC_ = 10 fixed point, _A_ will receive 5 and _C_ will


pay 5.


The only reason a system would find itself in a non-least fixed point is from


fraud. In this case, someone has inflated their liabilities such that the network


makes it self-fulfilling. In the case of Figure 5.5, firm _A_ is better off in a non

minimal fixed point and could have an incentive to influence (outside of our


model) firm _B_ . Firm _B_ could present fraudulent higher claims to firm _C_, which


would be self-fulfilling from the 100% cycle. This would cause a non-minimal


235


fixed point in liabilities. If the network is complicated, this fraud could be diffi

cult to uncover.


**Remark 5.1.** _There are two other realistic mechanisms that can cause multiplicity of_


_solutions, which pose governance challenges:_


 - _The parameters of many reinsurance contracts are not well defined, even to the_


_parties of the contracts. It is a common practice in the reinsurance industry to_


_agree to ‘in the future agree on a specific contract’._ [2] _In extreme cases, these ‘con-_


_tracts’ have been litigated to determine what contract would have been reasonably_


_agreed upon. In this case, the global contract parameters are not in principle_


_knowable, as assumed in our model, and there are additional potential solutions_


_for the different potential versions of the unknown contract._


 - _Given liabilities, multiple fixed points for determining clearing payments can also_


_exist when costs of default are nonzero [165]. This is realistically the case as there_


_are legal, transactional, and liquidity costs associated with real world defaults._


_In either case, if there is disagreement in the payouts of reinsurance contracts, such_


_as from multiple potential solutions, the issue goes to a panel of arbitors to resolve [169]._


_The members of the panel are typically active or former executive officers of insurance_


_or reinsurance companies [169] and will have different incentives. For example, these_


_could include the following: driving a competitor out of the market, limiting contagion_


_to given markets, or pinning default on parties that are least connected to themselves._


_Even when the arbitors do not have direct conflicts of interest, indirect conflicts of inter-_


_est are unavoidable through network structure. The arbitors will have different perceived_


_risk exposure to the various solutions. These incentives are outside of the focus of this_


_study; our purpose is to illustrate that cases like this can happen. We leave it to future_


2Private conversations with an insurance industry executive. All errors are our own.


236


_work to model these incentives and design good governance structures to account for_


_these._


We have widely characterized least fixed points of Φ. In the next section, we


provide efficient algorithms for finding these fixed points.

#### **5.3.8 Algorithms to find the least fixed point**


To find the minimum fixed point, if it exists, we can perform a fixed point it

eration of Φ starting at 0. Algorithm 1 performs this fixed point iteration. The


constructive statement of the Kleene fixed point theorem guarantees that Algo

rithm 1 converges to the minimum fixed point, if it exists. In practice, this runs


efficiently. However, in the worst case, it can take arbitrarily long. To see this,


consider an arbitrarily small damping of the near-100% cycle from Figure 5.7


with infinite caps. The fixed point iteration operates by pushing mass iteratively


around the system starting at the primary liabilities. As a given edge’s liabili

ties increase in one iteration, its tail node makes further calls on its reinsurers in


the next iteration, increasing the liabilities on their edges. The number of fixed


point iterations goes to infinity as the damping goes to 0. This is because all


excess loss will end up with the damping node, but we require arbitrarily many


trips through the cycle to reach equilibrium since the mass removed from the


recirculation in each iteration is smaller with a smaller damping.


237


**Algorithm 1** Fixed point iteration algorithm to determine reinsurance network
liabilities
**Require:** _d_, _c_, _γ_, _s_, _X_

Let _ℓ_ 0 be the zero vector, _t ←_ 1, `finish` _←_ `False`
**while** `finish` = `False` **do**

Let _bt_ indicate the entries that satisfy _Xℓt−_ 1 + _s−d ≥_ 0; define _Bt_ = diag( _bt_ )

_ℓt ←_ min _Btγ_ ( _Xℓt−_ 1 + _s −_ _d_ ) _, c_ element-wise

      -      **if** _ℓt_ = _ℓt−_ 1 **then**


`finish` _←_ `True`

**end if**

_t ←_ _t_ + 1

**end while**

**return** _ℓt_


**Iterative linear solver: no caps case**


This motivates Algorithm 2, which calculates liabilities in polynomial time com

plexity by iteratively solving linear systems in networks without caps. The lin

ear systems are of the form _ℓ_ = _γB_ ( _s_ + _Xℓ_ _−_ _d_ ) which has a unique solution


_ℓ_ = ( _I −_ _γBX_ ) _[−]_ [1] _γB_ ( _s −_ _d_ )


if ( _I −_ _γBX_ ) is nonsingular. In the case of zero deductibles (i.e., proportional


contracts), costs are shared linearly according to coinsurance rates between


firms, and only one iteration is required.


**Algorithm 2** Determine reinsurance network liabilities in a system without caps
**Require:** _d_, _γ_, _s_, _X_

Let _B_ 0 be the 0 matrix and _t_ = 1
Define diagonal matrix _B_ 1 by setting _B_ 1 _,ii_ = 1 if ( _s −_ _d_ ) _i ≥_ 0 and 0 otherwise
**while** _Bt ̸_ = _Bt−_ 1 **do**

Solve for _ℓt_ = _γBt_ ( _s_ + _Xℓt −_ _d_ )
_t ←_ _t_ + 1
Define diagonal matrix _Bt_ by setting _Bt,ii_ = 1 if ( _s_ + _Xℓt −_ _d_ ) _i ≥_ 0 and 0

 - therwise

**end while**

**return** _ℓt_


238


**Prop. 5.1.** _Given a financial system_ ( _X, γ, d, s_ ) _with infinite caps, if the spectral radius_


_ρ_ ( _γX_ ) _<_ 1 _, then Algorithm 2 converges to the solution in at most O_ ( _m_ [4] ) _time._


See proof in the Appendix.


Note that Algorithm 2 works in some additional cases (still assuming infinite


caps). In the first case, we may have problematic graph structure as demon

strated in the previous section, but which is not in a region of the graph that is


activated by the given shock. This means that the algorithm never leaves the


contractive region of Φ. In the second case, ( _I −_ _γBX_ ) can be invertible even if


_ρ_ ( _γBX_ ) _≥_ 1. Note that in this latter case, ( _I −_ _γBX_ ) _[−]_ [1] will not be nonnegative,


but this is not an issue as _ℓ_ = ( _I −_ _γBX_ ) _[−]_ [1] _γB_ ( _s −_ _d_ ) will still be nonnegative as


required.


**Iterative linear solver: caps case**


We now adapt the iterative linear solver to the setting with contract caps. How

ever, this is complicated by the fact that an iteration from 0 could mistakenly ac

tivate edges due to overcapacity leakage along edges in one of the linear solves.


To avoid this, we need to start from the worst case and iterate downward, which


results in a process that terminates at the maximum fixed point. Thus, this pro

cess only converges to the least fixed point if there is a unique fixed point.


The linear systems that come up in iterations are of the form _ℓ_ [˜] = ˜ _γB_ [˜] ( _X_ [˜] _ℓ_ [˜] + ˜ _v_ )


(recall that tilde notation incorporates the Ψ transformation onto the subsystem


- f edges that are not overcapacity in the previous iteration), which has a unique


solution


˜
_ℓ_ = ( _I −_ _γ_ ˜ ˜ _B_ ˜ _X_ ) _[−]_ [1] _γ_ ˜ ˜ _Bv_ ˜


239


if ( _I −_ _γ_ ˜ _B_ [˜] _X_ [˜] ) is nonsingular.


Algorithm 3 describes the iterative linear solver.


**Algorithm 3** Determine reinsurance network liabilities in a system with deductibles and caps
**Require:** _d_, _c_, _γ_, _s_, _X_

Let _b_ 0 and _c_ 0 be all twos vectors ( _>_ all ones vectors) and _t_ = 1
Let _b_ 1 be the all ones vector and _c_ 1 indicate entries with finite caps
**while** _bt ̸_ = _bt−_ 1 and _ct ̸_ = _ct−_ 1 **do**

Let _ℓ_ [¯] = diag( _ct_ ) _c_
Let Ψ map to a system on the zero coordinates of _ct_
For _i_ a _ct_ zero coordinate index, let _ψ_ ( _i_ ) give the corresponding coordinate
index under Ψ.

Let ˜ _γ_ = Ψ _γ_ Ψ _[T]_ _,_ _B_ [˜] _t_ = Ψ _Bt_ Ψ _[T]_ _,_ _X_ [˜] = Ψ _X_ Ψ _[T]_ _,_ ˜ _v_ = Ψ( _s_ + _Xℓ_ [¯] 1 _−_ _d_ )
Solve for _ℓ_ [˜] = ˜ _γB_ [˜] _t_ ( _X_ [˜] _ℓ_ [˜] + ˜ _v_ )
Let _t ←_ _t_ + 1
_ℓ_ _←_ Ψ _[T]_ [ ˜] _ℓ_ + _ℓ_ [¯]
Let _bt_ indicate the entries that satisfy _Xℓ_ + _s −_ _d ≥_ 0
Let _ct_ indicate the entries that satisfy _γ_ ( _Xℓ_ + _s −_ _d_ ) _≥_ _c_
**end while**

**return** _ℓ_


To prove that Algorithm 3 converges, we need a stronger condition than in


Theorem 5.3. This is because we have to start at an upper bound that is easily


computable. In some cases, there may be a suitable upper bound, but unlike in


Algorithm 3, it is not immediately clear what it is. The following proposition


provides sufficient conditions for convergence.


**Prop. 5.2.** _Let_ ( _X, γ, d, s, c_ ) _be a financial system and_ Ω:= _∧_ ( _B,C_ ) _∈K_ ( _I −_ _C_ ) _γBX_ ( _I −_


_C_ ) _be the matrix element-wise maximum, and_ Ψ0 _be the map to a system on the edges_


_with infinite caps (or map to the zero matrix if all caps are finite). Then if ρ_ (Ω) _<_ 1 _and_


_ρ_ (Ψ0 _γX_ Ψ _[T]_ 0 [)] _[ <]_ [ 1] _[, Algorithm 3 converges to the solution in at most][ O]_ [(] _[m]_ [4][)] _[ time.]_


See proof in the Appendix.


240


Note that the conditions of the proposition may be difficult to check in gen

eral. An easier condition to check is that _ρ_ ( _γX_ ) _<_ 1; however, this is again


not general enough to include many real world cases of multiple layers of XL


contracts.


This algorithm additionally ‘works’ when _ρ_ (˜ _γB_ [˜] _X_ [˜] ) _<_ 1 for all ( _B, C_ ) pairs.


However, we only know that it terminates at the minimum fixed point (i.e., a


unique fixed point) when _ρ_ (Ω) _<_ 1.

#### **5.4 Real World Implications of the Network Model**


In the previous sections, we developed the machinery of our reinsurance net

work model. This model works sequentially by calculating liabilities given a


shock, applying the collateralized portion of reinsurance contracts to cover lia

bilities, and then calculating clearing payments in the network. We now discuss


two features that result from this model: dangerous network structures and pa

rameter sensitivity. These features introduce new issues in risk management,


present a new incentive to combat fraud, and demonstrate the importance of


global contract design to ensure the insurance system works well.

#### **5.4.1 Dangerous network structures cause reinsurance spirals**


Relaxations of 100% cycles cause counterintuitive nonlinear behavior known


as reinsurance spirals. By relaxation, we mean that the cycle circulates close


to (but _≤_ ) 100% reinsurance. We will refer to this as ‘ **relaxed cycles** ’. This is


introduced, for instance, in [21] with an example in the Lloyd’s and London


241


#### Primary Insurer Reinsurers Γ = 1 d = 0









Figure 5.6: Example of a reinsurance spiral. An initial shock of 5 is passed
around the reinsurance cycle with 0 deductibles until nominal liabilities reach
10, at which point the cap on edge ( _C, A_ ) is activated. All excess loss is then left
with firm A.


reinsurance markets in the 1980s. In these spirals, nominal liabilities increase at


each step through the graph cycle until one of the contract edges reaches its cap,


after which all excess liability is left with the reinsured party of that contract.


Figure 5.6 provides an example. In this example, even though the size of the


shock is less than all contract caps, the spiral effect causes the cap on ( _C, A_ )


to be reached, leaving all liability for the shock on _A_ . Given local first-degree


information, all parties think they are adequately reinsured; however, it turns


- ut that this is not the case. Relaxation of the 100% cycle to smaller values of _γ_


lessen the growth of liabilities in the cycle, but lead to a similar effect, where a


disproportionate amount of excess liability is left with a single party. Further,


the effect is the same, even if we arbitrarily scale the caps around the cycle. Even


if caps are very high, in which case a firm would intuitively expect to be very


well reinsured, firms are still subject to the exact same spiral risk.


Another type of spiral that can happen is when a relaxed cycle is damped


by a node outside the cycle. See Figure 5.7 for an example. In this case, in each


242


Primary Insurer Reinsurers



Damping Reinsurer

Γ = 0.01



Figure 5.7: Example of a relaxed cycle with a damping reinsurer. Excess loss
is passed around the cycle with 1% being absorbed by the damping reinsurer
in each circulation. If the caps on the cycle contracts are high, disproportionate
excess loss is left on the damping reinsurer.


trip through the cycle, a small proportion of excess liability is siphoned off by


the damping reinsurer. The remaining proportion continues around the cycle


until a proportion of it is again siphoned off by the damper. In equilibrium, a


disproportionate amount of the excess loss can be left on the damping reinsurer,


depending on the cap parameters in the cycle. The damping reinsurer may


not be aware of the role they are taking in the network; given local first-degree


information, they may think they are only reinsuring one firm instead of the


whole cycle.


If there are multiple damping reinsurers, it will be difficult to predict


whether one of the dampers (and which one) will be left with disproportion

ate excess liability if there is imperfect information about network parameters.


For instance, one damping contract could have a low cap, leaving most liability


- n the second damping contract. Alternatively, a contract cap within the cycle


could be activated and leave most excess loss on one of the reinsurers in the


cycle. We can also have a damping chain of reinsurers. In this case, a node can


be arbitrarily far from a relaxed cycle in a connected graph but still be left with


disproportionate excess loss.


243


**Standard risk management does not work for relaxed cycles** Relaxed cy

cles can serve to aggregate losses from multiple sources across the network in


a way that is not transparent to a damping reinsurer who only knows its local


structure in the network. Figure 5.8a is an example where losses from multiple


primary insurers are aggregated through the relaxed cycle, leaving all excess li

ability with the damping reinsurer. For comparison, a tree structure such as in


Figure 5.8b can aggregate losses from many primary insurers onto one reinsurer


(the root node). However, reinsurers can control for this tree aggregation risk


by putting limits on the size of the reinsurered portfolios (usually in terms of


premiums the reinsured firm receives). The reinsured portfolios would have to


be large to lead to large aggregations of losses. This risk management method


does not work in the case of relaxed cycles. Even if firms in a relaxed cycle


individually have small reinsurance portfolios, the relaxed cycle can include a


large number of firms and the spiraling behavior can aggregate losses from all


- f these portfolios.


Anther example of unintuitive behavior is that a contract cap does not nec

essarily limit the liability of a node caused by another node. Figure 5.9 gives an


example where graph connections through a second layer of reinsurance coun

teract the contract cap on the first layer. In this case, _B_ reinsures _A_ up to the


cap, after which additional excess loss is translated back to _B_ through a second


layer of reinsurance from _C_ . Of course, deductibles may reduce the total loss


borne by _B_ . In a real application, _B_ likely knows little of the network structure


- utside of first degree connections and so may be unaware that it is also liable


_A_ .
for parts of the second layer of reinsurance coverage of


We have demonstrated the emergence of reinsurance spirals and the extreme


244


Primary Insurer Reinsurers



Damping Reinsurer







(a) Example of cycle that aggregates multiple losses. With
high caps, most aggregated loss is absorbed by damper.


Primary Insurers Reinsurers


(b) A tree structure that aggregates many
losses on one reinsurer.


Figure 5.8: Standard risk management works for trees but fails in the case of
relaxed cycles.


Primary Insurer Reinsurers





Figure 5.9: Example in which a contract cap is counteracted. If the cap on _B_ ’s
coverage of _A_ is passed, _B_ is still liable for additional coverage of _A_ through _C_ ’s
_B_ .
second layer coverage of


245


bearing of reinsurance losses due to network structure using simple examples.


While these examples are illustrative, more complicated examples, as in real


world reinsurance networks, can exhibit the same effects.

#### **5.4.2 Extreme parameter sensitivity**


**Incomplete network information.** In a real setting, small groups of firms have


incomplete information about the global network structure. They face intrinsic


uncertainty of global contract parties and parameters. Indeed, in many cases,


the network is unable to be fully observed in principle, even by regulators or


the industry as a whole. We have previously mentioned that the parameters of


some real industry contracts are not even agreed upon beforehand. Instead, the


‘contract’ is really just an agreement to in the future agree on a contract, and so


the parties of the contract do not even know the actual terms of the contract.


**Difficulties in measuring risks.** As a result of this uncertainty, there is also


high uncertainty about which dangerous structures can emerge. For example,


it is difficult to determine if, by taking a given contract position, a firm exposes


itself to being a damping node. Thus firms face high uncertainty about their


extreme bearing of reinsurance losses. [3]


Additionally, even small perturbations in the network parameters can lead


to large differences in losses and where extreme losses are borne, presenting ad

3In the unlikely event that nodes have complete information about the network, identifying
problematic structures would remain difficult from an algorithmic perspective, as we discussed
in the previous sections. As we also noted, we can determine whether a 100% cycle occurs in a
given network using the spectral radius, but this criterion is in general not guaranteed to work
for relaxed cycles.


246


ditional complexities to risk management. To illustrate this, consider again the


example in Figure 5.6. Small changes to the contract caps (e.g., switching which


contract has a cap of 10 vs. 11) affect which edge cap is met and, in turn, who


bears all excess loss. In the real world, uncertainty around network parameters


is likely to be large, which only exacerbates the problem. We demonstrate this


high sensitivity to parameters using real network data in the next section.


**A new incentive to cooperate on fraud prevention.** Given the complexity of


real world networks, fraud can be quite difficult to uncover. In principle, to fully


protect against fraud, a system needs to allow all parties to verify that upstream


liabilities are valid propagations of primary insurance claims. Ordinarily, firms


- nly have access to audit the direct claims they receive and must trust all other


firms to properly audit their claims and to not collude in this regard. In the


industry today, there is typically no good way to detect fraud. Indeed, there is


a sense that reinsurers only work with insurers they trust. [4]


Due to the parameter sensitivity of these systems, even very small fraud


can have outsized effects on the equilibrium. Further, a fraudulent ordering of


payments could also affect the equilibrium after taking into account clearing.


As individual firms cannot fully observe the network, they face wild variability


in the valid claims they could face given a shock. Each firm should be highly


suspect of whether the network of claims is correct, especially if they face high


losses under the proposed claims. Even if fraud is very unlikely and only very


small, a firm’s potential benefit from exposing it could be quite large (e.g., the


difference of the firm defaulting or not). Thus our sensitivity results suggest


4Aside from unequivocal fraud, there are commonly grey instances in which a reinsurer will
pay a little more on a contract if the insurer is a ‘good customer’, which can affect claims down
the chain. Source: private conversations with an insurance executive.


247


a very strong–and to our knowledge, previously undiscussed–incentive for a


large majority of firms to band together to combat fraud, and potentially share


information with each other in order to do so.

#### **5.4.3 Implications for contract design**


From a global contract design perspective, there are a few things that can help


mitigate spirals and parameter sensitivity. We discuss contract deductibles and


proportional contracts. However, these are not guaranteed to be effective.


Contract deductibles help to lower the excess loss that is recirculated


through graph cycles by absorbing some loss before each edge activation. How

ever, given a large shock, deductibles may not be enough to prevent dispropor

tionate network effects from spirals, as was the case during the Lloyd’s and


London reinsurance market spiral during the 1980s.


The cap-deductible layering structure of XL reinsurance obfuscates risks and


heightens sensitivity to parameters by adding lots of nonlinearities into the net

work. On top of this, we have to clear the network liabilities given the avail

able equity, which adds additional nonlinearities. On the other hand, a system


composed of proportional reinsurance contracts is much simpler to compute as


liabilities can be calculated through a linear system. This removes many of the


nonlinearities (but not all as we still need to clear the network), which helps


make the risk faced by a firm in the network clearer. This lessens the chances


that firms think they are adequately reinsured but later find out otherwise. This


may also lead to less parameter sensitivity since, as pointed out in a previous


section, the liabilities of a proportional system are determined by solving a sin

248


gle linear system. On an aggregate level, this may also lower systemic risk,


which we examine using real network data in the next section.

#### **5.5 Simulations with Real Network Data**


In this section, we investigate two questions posed in the previous section using


simulations on real reinsurance network data:


  - Is there high parameter sensitivity in real reinsurance networks? I.e., is it


difficult to estimate the risk faced by a firm in the network from a particu

lar shock? We demonstrated that this is a theoretical issue in the previous


section.


  - Are XL or proportional contract systems better from a systemic perspec

tive? In the previous section, we demonstrated that a system based on XL


contracts adds many nonlinearities to the system, which can serve to ob

fuscate risk and concentrate losses. A proportional system, on the other


hand, has much less nonlinearities.


We also briefly explore the effect of time dependency of claims. Our code is


freely available at www.github.com/aklamun/reinsurance_networks.

#### **5.5.1 Network construction**


As the basis for our simulations, we use real network data on property and ca

sualty reinsurance from 2012 Schedule F Part 3, as obtained from the National


249


Figure 5.10: Network visualization. Pink nodes are reinsurers, green nodes are
primary insurers.


Association of Insurance Commissioners (NAIC) [149]. This data details premi

ums ceded to reinsurers by US insurance companies. Naturally, this data does


not provide all contract parameters, so we estimate these using common rules of


thumb in the insurance industry, which we back up with data where available.


We develop methods for constructing plausible networks of XL and propor

tional contracts consistent with the data. These methods and the more general


simulation setup are detailed in Appendix 5.8. In our simulations, we consider


1-in-100 and 1-in-250 year shocks to the network.


Figure 5.10 gives a visualization of a resulting XL network with edges


weighted by _γ_ . The figure shows a core-periphery structure. The core is


composed of a central group of reinsurers and primary insurers who reinsure


through most of them. This core-periphery structure is common in a variety of


financial networks, see e.g. [62].


250


#### **5.5.2 Sensitivity to parameter perturbations**

In our first set of simulations, we examine the firm-level effects of perturbations


in the XL financial network parameters. As discussed in the previous section,


the nonlinearities added by layering structure make it difficult to evaluate the


exposure of a firm to a shock under parameter uncertainty. Exposures under


slightly different parameter sets could be completely different on a theoretical


level. In these simulations, we demonstrate that sensitivity occurs in reasonable


estimates of a real world reinsurance network.


In these simulations, we construct an XL network from our data, which is


- ur base case for comparison. We then perturb the network parameters by a


factor _δ_ as described in Appendix 5.8. For moderately small values of _δ_, these


perturbations are conservative because firms face a lot of uncertainty about how


- ther firms’ contracts are structured and, because of market forces, there are


intrinsic uncertainties about each firm’s capital available to pay out liabilities at


the time of clearing. Additionally, for privately owned insurers, equity values


are not publicly available.


With a given shock _sh_, in each simulation, we calculate a liabilities matrix


_L_ and clear the liabilities using methods from [75]. [5] This second step is done


without default costs for simplicity and outputs a clearing payment vector _p_,


representing the total payment from each firm, and a default indicator vector.


After the simulation, we calculate the vector of end equities _e_ 1 as


_e_ 1 = _e_ 0 _−_ _p_ + _L_ _[T]_ _α −_ _sh,_


5Note that the clearing in [75] assumes reinsurance contracts are on the same level of clearing
importance as retrocession contracts. By using this clearing, we also assume that limited liability
is always invoked between reinsurers. In reality, however, there are vague ‘parental guarantees’
between companies in the same group as well as some degree of joint and several liability, in
which regulators can force surviving insurance firms to take on liabilities of failed firms.


251


where _e_ 0 is the initial equity vector and _α_ is defined component-wise as



( _Lp_ **1** _i_ ) _i_ _[,]_ if ( _L_ **1** ) _i >_ 0



_αi_ =














_,_

0 _,_ - therwise



where **1** is the all ones vector. The multiplicative equity return is then _e_ 1 _/e_ 0.


A return of 1 represents no loss, 0 represents complete loss of capital, and a


negative value means that a primary insurer has outside liabilities that are un

able to be covered after clearing. Note that, under this definition, reinsurers


face a return floor of zero (i.e., _e_ 1 _≥_ 0 since _sh_ = 0 for a reinsurer); this makes


sense because they have limited liability. In a legal sense, limited liability could


be applied to primary insurers; however, it will be useful to us to explore the


uncovered primary losses that are represented using our definition above for


equity. Uncovered primary liabilities represent a failure of the system, as the


purpose of the insurance-reinsurance industry is to provide protection on phys

ical infrastructure. This does not happen if primary liabilities are not met.


Under a static 1-in-250 year shock, we run simulations with 2.5%, 5%, 10%,


and 20% perturbations, each with 50 random samples. We examine how firm


equity returns and defaults differ between the perturbed systems and the base


system. Figure 5.11 shows the extent to which these perturbations change firm


equity returns. These histograms are over maximum differences observed in the


2609 network firms, excluding those with zero observed difference. Even under


small 2.5% perturbations, a firm’s equity return can differ by 100 percentage


points. [6] The tail of the distribution fattens quickly as the perturbation magni

tude increases. These results demonstrate that small uncertainties in financial


network parameters can lead to wild differences in outputs, as demonstrated


6Note that this high uncertainty in equity return could also occur at smaller perturbation
levels. In this study, we don’t attempt to numerically find a lower bound.


252


10 [0]

|Histogram:2 .5%PerturbationEffects<br>2<br>1<br>0<br>00 02 04 06 08 1<br>. . . . .<br>|Differencefirmequityreturn|>0|Col2|Col3|stogr|Col5|am:2 .5%Pert|urbat|ionEf|fects|
|---|---|---|---|---|---|---|---|---|
|0.0<br>0.2<br>0.4<br>0.6<br>0.8<br>1<br>|Difference firm equity return| > 0<br>0<br>1<br>2<br>Histogram: 2.5% Perturbation Effects|||||||||
|0.0<br>0.2<br>0.4<br>0.6<br>0.8<br>1<br>|Difference firm equity return| > 0<br>0<br>1<br>2<br>Histogram: 2.5% Perturbation Effects||||0.<br>Di|2<br>0.4<br>0.6<br>0.8<br>1<br>fference firm equity return| > 0|2<br>0.4<br>0.6<br>0.8<br>1<br>fference firm equity return| > 0|2<br>0.4<br>0.6<br>0.8<br>1<br>fference firm equity return| > 0|2<br>0.4<br>0.6<br>0.8<br>1<br>fference firm equity return| > 0|2<br>0.4<br>0.6<br>0.8<br>1<br>fference firm equity return| > 0|



(a) 2.5% perturbation



10 [2]


10 [0]

|Hi<br>2<br>1<br>0<br>00<br>.<br>||stogram:20%Pert|Col3|Col4|Col5|urbat|ionEf|Col8|fects|
|---|---|---|---|---|---|---|---|---|
|0.0<br><br>|<br>0<br>1<br>2<br>Hi|||||||||
|0.0<br><br>|<br>0<br>1<br>2<br>Hi|0.2<br>Differenc|0.<br>e f|4<br>irm|equ|0.6<br>ity re|tu|rn||0.8<br>1<br> > 0|



(b) 20% perturbation



Figure 5.11: Log-scale histograms of perturbation effects on firm equity returns,
measured by maximum absolute value of change from the base case to the perturbed case, under a static shock.


with firm equity returns.


These perturbations altered the default status of 8 firms (2.5% perturbation)


up to 21 firms (20% perturbation). Additionally, these perturbations affected


firm equity levels on the order of $790M (2.5% perturbation) up to $110B (20%


perturbation). This demonstrates that perturbations can affect key players of


the market. An individual firm could be wildly uncertain about the risks it


faces from a given shock given even small network uncertainties.

#### **5.5.3 Systemic effects of contract structures**


In our second set of simulations, we examine the systemic effects from different


contract structures. As discussed in the previous section, systems of XL con

tracts can have the effect of concentrating losses in unpredictable ways. This


can cause firms to mistakenly think they are properly reinsured when in effect


they are not. On the other hand, a system of proportional contracts can have


much less obfuscation of risk. In these simulations, we demonstrate that, given


253


real world network structure, proportional reinsurance systems are more stable


in the face of tail risk than comparable XL reinsurance systems.


A key word here is of course ‘comparable’. Our methods for constructing


comparable networks is described in Appendix 5.8. Note that this compari

son is limited because it is likely that in the real world the equilibrium graph


structure, premiums ceded, and firm capital levels would be different between


the different settings, whereas we are setting these constant. In the different set

tings, firms may make different decisions about these parameters. This said, our


comparison is still useful because it shows that, given the same aggregate costs


in terms of reinsurance premiums ceded and firm capital levels, the reinsurance


market could perform systemically better.


We simulate 50 1-in-100 year shocks and 50 1-in-250 year shocks to two com

parable XL and proportional reinsurance systems. We compare the aggregate


number of defaults, the aggregate uncovered primary claims, and the distribu

tion of firm equity returns for each network in each scenario.


Figure 5.12 compares the number of defaults and the uncovered primary li

abilities in each shock scenario. The number of defaults is a common measure


- f the resilience of financial networks. We argue that the level of uncovered pri

mary liabilities is also a useful comparison because the purpose of the reinsur

ance industry in the first place is to redistribute risk such that primary insurance


liabilities (insurance on real world infrastructure) can be more easily met during


shocks. By both measures, the XL system performs consistently worse than the


proportional system.


Figure 5.13 shows histograms comparing firm equity returns between the XL


254


1.2


1.0


0.0



120


100


80


60


40


20







0 20 40 60 80 100 120


(a) Number of defaults



|1e7 Uncovered Primary Claims per Shock|Col2|Col3|
|---|---|---|
|1e7<br> y p <br>250 yr shock<br>100 yr shock|1e7<br> y p <br>250 yr shock<br>100 yr shock|1e7<br> y p <br>250 yr shock<br>100 yr shock|
|0<br>0.2<br>0.4<br>0.6<br>0.8<br>1|.0<br>1|.2|


XL model 1e7


(b) Total uncovered primary liabilities



Figure 5.12: Aggregate comparison of proportional vs. XL systems. Each point
is a shock realization.


and proportional systems under 1-in-100 year and 1-in-250 year shocks. These


histograms collapse two (notably dependent) dimensions of data into one: the


2609 firms in the network and the 100 shock simulations. Thus each firm ac

counts for 100 data points. These histograms help to visualize the firm-level


effects across the simulations.


Figures 5.13a and 5.13b show empirical distributions of firm equity returns,


which demonstrate that firms face higher tail risk of losses under the XL system


than the proportional system. Note that the histogram spikes at 0 are caused


by the limited liability of reinsurance companies. As discussed in the previ

- us subsection, we could apply the same limited liability to primary insurers,


but find it more useful to represent the uncovered primary liabilities within the


distribution.


Figure 5.13c shows the histogram of firm-level differences in returns between


the two models, taking into account all scenarios. In these scenarios, _>_ 49% of


firms are better off under the proportional model than the XL model. In par

ticular, the additional cost of the proportional structure to the average firm is


255


(a) Firm equity returns under XL system


(c) Difference in firm equity returns between models



(b) Firm equity returns under proportional
system



|m 2D-Histogram Firm Returns:|Col2|
|---|---|
|g|g|
|20<br>1|5<br>10<br>05|


(d) 2D histogram returns in XL vs. proportional







Figure 5.13: Firm equity returns under XL and proportional systems. Histograms include all simulations, weighted by relative probability of 1-in-100 vs.
1-in-250 year events (60% vs. 40%).


small. Consistent with the previous histograms, however, firms are predomi

nantly better off in the tails under the proportional model than the XL model.


Figure 5.13d shows a 2D histogram of firm equity return under the proportional


model vs. the XL model. The same tail structure can be seen in the 2D his

togram. Note that again we can see the limited liability effect of reinsurance


companies in the square structure around 0 in the 2D histogram. Reinsurers’


returns are constrained to the square between 1 and 0 in the 2D histogram due


to the limited liability, whereas the primary insurers’ returns form the triangle


structure.


256


#### **5.5.4 Effects of time dependency of claims**

We now briefly explore the effects of claims that come in over multiple time pe

riods. In reality, claims take varying time and up to several years to reach rein

surers. Two main factors contribute to this. First, claims are largely manually


reported from one party to the next. This paperwork process can take consid

erable time to trickle through chains of reinsurers in the network. Reinsurers


who are closer to the source see claims earlier. Second, some claims do not


materialize until future years. Most reinsurance contracts are tied to property


and casualty, in which losses commonly develop over 5-10 years. Loss run-offs


beyond 10 years are common with major shocks like terrorist attacks and hurri

canes. For instance, claims from the World Trade Center attacks were litigated


- ver nearly a decade. Further, asbestos claims can come in decades after the


fact.


We consider a simple setup in which claims come in over two time periods.


After the first claims come in, the network liabilities are cleared and the firm


capital is updated. The network is cleared again after the second claims come


in. Such a setting, with multiple rounds of clearing underlies the emerging lit

erature on dynamic network models [23, 119, 47]. We compare this to a single


period setup in which all of the claims come in at the same time.


Formally, the network faces shocks _sh_ 1 and _sh_ 2 in periods one and two re

spectively. These yield network liabilities matrices _L_ 1 and _L_ 2 respectively. We


apply clearing from [75] sequentially over the periods. In period one, liabilities


_L_ 1 are cleared and firm capital is updated as follows. Given starting equities


_e_ 0, shock _sh_ 1, and liabilities _L_ 1, the period one clearing payment vector _p_ 1 is


257


calculated. Then period one end equities are calculated as


_e_ 1 = _e_ 0 _−_ _p_ 1 + _L_ _[T]_ 1 _[α]_ [1] _[−]_ _[sh]_ [1] _[,]_



where _αt_ is componentwise _αt,i_ =


vector.














( _Lptt_ **1** _,i_ ) _i_ _[,]_ if ( _Lt_ **1** ) _i >_ 0



and **1** is the all ones

0 _,_ - therwise



Recall that as the shocks only directly affect the primary insurers, the mini

mum equity of a reinsurer is zero after the clearing. As before, we allow nega

tive equities for primary insurers to account for uncovered primary losses. As


primary insurers are simply leaves in the network, these do not affect the next


period clearing.


In period two, remaining capital _e_ 1 is used to clear liabilities _L_ 2. In particular,


if a reinsurer defaults in period one, any retrocession payments they receive in


period two are channeled to the period two liabilities that triggered these pay

ments. Given equities _e_ 1, shock _sh_ 2, and liabilities _L_ 2, the period two clearing


payment vector _p_ 2 is calculated. Then period two end equities are calculated as


_e_ 2 = _e_ 1 _−_ _p_ 2 + _L_ _[T]_ 2 _[α]_ [2] _[−]_ _[sh]_ [2] _[.]_


The multiplicative equity return across the two periods is then _e_ 2 _/e_ 0.


The effect of the two period clearing is that insurers who are connected to


defaulted reinsurers may have their claims paid in different fractions of face


value depending on whether they are paid in the first or second period. This


compares to a single period clearing, in which everyone is paid out in the same


proportion. This means that earlier claims may effectively get seniority over


later claims. A reinsurer may be able to pay out in full for early claims, but may


enter default in the second period. However, the opposite can also happen. A


258


reinsurer may be unable to pay in full on early claims, but is able to pay more if


retrocession contracts are activated when the second wave of claims comes in.


Notice, however, that a firm that defaulted in the first period will never have


excess value in the second period because reinsurance coverage is _<_ 100%.


We simulate 50 1-in-250 year shocks that are split between two periods. For


each of the 50 simulations, we generate two random 250-year shocks distributed


in the same way as described in Appendix 5.8 (i.e., not uniformly distributed,


but proportional to the size of premiums). We divide the magnitude of each by


two; these are the period one and period two shocks. We then compare this to


the single aggregate shock.


Figure 5.14 shows the histogram of firm-level differences in returns between


two periods and one period clearing. The histogram collapses two (notably


dependent) dimensions of data into one: the 2609 firms in the network and


the 50 shock simulations. Thus each firm accounts for 50 data points. This


histogram is useful for visualizing how much the time dependence of claims


can affect firms’ equities. Note that the average difference is very close to 0


(0.00032) although the distribution as visualized is asymmetric. This reflects


that the structural change is not adding excess costs but rather changing the


distribution of costs. To illustrate how much firm equities can change between


the two-period and one-period clearing schemes, in every simulation, at least


5% of firms saw _>_ 22% absolute change and at least 1% of firms saw _>_ 60%


absolute change.


259


Figure 5.14: Difference in firm equity returns between two-period and oneperiod clearing.

#### **5.6 Concluding Remarks**


Current reinsurance risk models do not capture network effects, which we show


can be quite extreme. We have demonstrated that even if firms know the global


network structure unreasonably well (i.e., with small uncertainty), they can be


wildly uncertain about how losses will be distributed from a given shock. Tail


risk from network structure should be taken into account in determining capital


requirements, evaluating counterparty risk, and pricing reinsurance contracts.


This exposes inherent inefficiencies in the current system.


**Combating fraud.** Our sensitivity results reveal a strong new incentive for


firms to band together to combat fraud. This could be achieved through a


trusted central party or, in the absence of such a party, a distributed ledger sys

tem. A blockchain could provide guarantees on fraud prevention if it is able to


record audited and time-ordered claims and reinsurance payments. Such a sys

tem would need to allow participants in the network to independently verify


the equilibrium liabilities and clearing state in the network. We propose fu

260


ture work to design such a system that works given the real world constraints


around contract privacy. We note, however, that the strong incentive we have


demonstrated may make firms more willing to share some data to contribute to


fraud prevention, thus relaxing these contraints. Many organizations are mak

ing a concerted effort to incorporate blockchain systems into the (re)insurance


industry. Our paper helps to inform them about the problems they should be


addressing.


**Measuring risk.** We have revealed dangerous structures that lead to tail risk


from network effects. We propose new tools that better measure and classify tail


risk of positions (e.g., nodes or contracts) within the network. One approach is


to use inner Monte Carlo simulations over a range of shocks, and outer Monte


Carlo simulations over a range of parameters; however, convergence may be


costly. A second approach is to use machine learning classification algorithms.


This would entail generating a wide variety of graphs and parameters and eval

uating losses from contagion shocks under different scenarios via algorithms


from our paper. Using this as a training set, the aim is to detect graph structures


that predict which nodes bear tail risk from spirals. We believe the structure


that we have revealed about tail risk in this paper will aid in the construction


- f such methods. One promising result from our simulations is that, under a


given shock, the losses of many network nodes appear robust to parameter er

ror whereas others suffer more chaotic behavior. This suggests that classification


algorithms may be successful in predicting which nodes bear high uncertainty


and are therefore more susceptible to model error.


261


**Designing better systems.** Our simulations suggest that, for the same societal

level costs in terms of reinsurance premiums and capital locked in the reinsur

ance industry, the industry can be better structured to perform its social pur

pose more effectively during extreme events. We would like to extend this to


a market design perspective. One issue is that, in isolation, firms can have an


incentive to require caps on payouts (although this is not clear), but at the net

work level this does not appear optimal. We leave it to future work to explore


the robust systemic design perspective taking into account how the _γ_ matrix


changes with respect to changes in contract structure.


In recent years, catastrophe bonds held by nontraditional players, such as


hedge funds, have become more popular in place of traditional reinsurance con

tracts. One advantage of these is that they could become additional dampers in


the system as they absorb losses in the system without recirculating them. This


has the tradeoff, however, of more significantly interconnecting the larger finan

cial system, which can cause other potential exposures that are relevant from a


market design perspective.


Lastly, stemming from our discussions with industry executives, we propose


the following extensions to the model and analysis.


 - **Time dimension:** As discussed in the previous section, time dependence


   - f claims can have a large effect on firms’ equities. This warrants further


work. We note that NAIC provides an extensive historical database on


insurance loss run-offs in Schedule P.


 - **Liquidity factor:** Extreme events in the insurance-reinsurance industry–


such as high concentration of large losses due to network structure–could


trigger a liquidity crisis from fire sales of risky assets. This can am

262


plify losses within and beyond the reinsurance industry, propagating an


insurance-specific event into a systemic crisis.


**Acknowledgements** We thank Steffen Schuldenzucker for his valuable contri

bution in the proof to Thereom 5.6 and Sven Seuken and the Economics & Com

putation group at University of Zurich for helpful discussions. We also thank


Frank Krieter, Dominic Rau, and the risk team at Swiss Re and Sean Bourgeois


at Tremor for valuable discussions covering the reinsurance industry. The first


author acknowledges an Amherst College Fellowship. This work was funded


through NSF RTG Award #1645643, NSF CRISP Award #1638230 and NSF CA

REER Award #1653354.

#### **5.7 Appendix: Proofs**


**Lemma 5.2**


_Proof._ For every _ℓ_ _≥_ 0, there is a unique corresponding _B_ and _C_ defined (and


so also a unique Ψ). Note that on the boundary between ( _B, C_ )-constant sets


multiple _B_ s and _C_ s could be defined equivalently. This is because Φ is an in

tersection of linear systems on the boundaries–the difference in possible _B_ s and


_C_ s comes from edges that have exactly met their deductible or cap respectively


but have no excess liability under _ℓ_ . In these cases, _Bii_ - r _Cii_ respectively can be


set equivalently to 1 or 0, but a unique selection is defined in the definition.


The derivatives of _B_ ( _ℓ_ ) and _C_ ( _ℓ_ ) are defined and zero except at points of


discontinuity since _B_ and _C_ - nly change at thresholds. _B_ and _C_ are defined


263


such that their value on the boundary (i.e., at points of non-differentiability in


either _B_ - r _C_ ) are constant with a value on one side of the boundary. As there


are 2 _[m]_ possible _B_ and _C_ matrices (1 or 0 for each diagonal entry), the ( _B, C_ )

constant sets form a finite partition of _{ℓ|ℓ_ _≥_ 0 _}_ - f size at most 2 [2] _[m]_ .


To establish convexity, notice that systems of linear inequalities define _B_ and


_C_ . And so the ( _B, C_ )-constant sets, each the intersection of the pre-image of a


given _B_ and _C_ values, are convex sets since they are the intersections of half

spaces from each inequality.


**Theorem 5.3**


_Proof._ Lemma 5.1 gives us that a linear system with matrix Ω is a contraction


with respect to some weighted Euclidean norm. Let _∥·∥s_ be such a norm and let


_α ∈_ [0 _,_ 1) be the corresponding Lipschitz constant. Since our matrices are non

negative, the Perron-Frobenius theorem gives us that for ( _B, C_ ) _∈K_, _ρ_ ( _I −_

                           

_C_ ) _γBX_ ( _I −_ _C_ ) _≤_ _ρ_ (Ω) _<_ 1.

      

Note that the derivatives of _B_ ( _ℓ_ ) and _C_ ( _ℓ_ ) are zero except at points of dis

continuity. On the subsets of the domain space on which ( _B, C_ ) is constant


(( _B, C_ )-constant sets), Φ is a linear system described by ( _I −_ _C_ ) _γBX_ ( _I −_ _C_ ).


This can be written as


Φ( _ℓ_ ) = ( _I −_ _C_ ) _γB_ _X_ ( _I −_ _C_ ) _ℓ_ + _XCc_ + ( _I −_ _C_ )( _s −_ _d_ ) + _Cc_

          -           

= Ψ _[T]_ _γ_ ˜ _B_ [˜] ( _X_ [˜] Ψ _ℓ_ + ˜ _v_ ) + _ℓ._ [¯]


264


Let _ℓ_ 1 _, ℓ_ 2 be points in a ( _B, C_ )-constant set. Then


˜ ˜
_∥_ Φ( _ℓ_ 1) _−_ Φ( _ℓ_ 2) _∥s_ = _∥_ Ψ _[T]_ _γB_ [˜] ( _X_ [˜] Ψ _ℓ_ 1 + ˜ _v_ ) + _ℓ_ [¯] 1 _−_ Ψ _[T]_ _γB_ [˜] ( _X_ [˜] Ψ _ℓ_ 2 + ˜ _v_ ) + _ℓ_ [¯] 2 _∥s_


˜
= _∥_ Ψ _[T]_ _γB_ [˜] _X_ [˜] Ψ( _ℓ_ 1 _−_ _ℓ_ 2) _∥s_


_≤∥_ Ω( _ℓ_ 1 _−_ _ℓ_ 2) _∥s_


_≤_ _α∥ℓ_ 1 _−_ _ℓ_ 2 _∥s,_


where the third line follows because 0 _≤_ Ψ _[T]_ _γ_ ˜ _B_ [˜] _X_ [˜] Ψ _≤_ Ω element-wise. Thus Φ


is a contraction with respect to _∥· ∥s_ locally on each ( _B, C_ )-constant set.


Note that for _ℓ_ [ˆ]  - n the boundary of a ( _B_ 1 _, C_ 1)-constant set and a ( _B_ 2 _, C_ 2)

constant set,


Ψ _[T]_ 1 _[γ]_ [˜][1] _[B]_ [˜][1][( ˜] _[X]_ [1][Ψ][1] _[ℓ]_ [+ ˜] _[v]_ [1][) +] _[ C]_ [1] _[c]_ [ = Ψ] _[T]_ 2 _[γ]_ [˜][2] _[B]_ [˜][2][( ˜] _[X]_ [2][Ψ] _[ℓ]_ [+ ˜] _[v]_ [2][) +] _[ C]_ [2] _[c]_


since Φ is continuous. The explanation for this is that, on the boundary, multiple


_B_ s and _C_ s could be defined equivalently. Φ is an intersection of linear systems


- n the boundaries. The difference in possible _B_ s comes from edges that have ex

actly met their deductible but have no excess liability. The difference in possible


_C_ s comes from edges that have exactly met their cap. In these cases, _Bii_ (re

spectively _Cii_ ) can be set equivalently to 1 or 0. Hence, the contraction relation


extends to the boundaries of _B_ - constant sets.


We next show that the contraction relation extends to the union of two ad

jacent ( _B, C_ )-constant sets. Choose _ℓ_ 1 _∈_ ( _B_ 1 _, C_ 1)-constant set and _ℓ_ 2 _∈_ ( _B_ 2 _, C_ 2)

constant set such the shortest path only crosses one ( _B, C_ )-constant boundary.


Since _∥·∥s_ is a weighted Euclidean norm, there is a shortest path between _ℓ_ 1 and


_ℓ_ 2 that crosses the boundary between ( _B_ 1 _, C_ 1)- and ( _B_ 2 _, C_ 2)-constant sets. Let _ℓ_ [ˆ]


265


be the crossing point of this boundary. Then


_∥_ Φ( _ℓ_ 1) _−_ Φ( _ℓ_ 2) _∥s_ = _∥_ Φ( _ℓ_ 1) _−_ Φ( _ℓ_ [ˆ] ) + Φ( _ℓ_ [ˆ] ) _−_ Φ( _ℓ_ 2) _∥s_


= _∥_ Ψ _[T]_ 1 _[γ]_ [˜][1] _[B]_ [˜][1] _[X]_ [˜][1][Ψ][1][(] _[ℓ]_ [1] _[−]_ _[ℓ]_ [ˆ][) + Ψ] _[T]_ 2 _[γ]_ [˜][2] _[B]_ [˜][2] _[X]_ [˜][2][Ψ][2][(ˆ] _[ℓ]_ _[−]_ _[ℓ]_ [2][)] _[∥][s]_


_≤∥_ Ψ _[T]_ 1 _[γ]_ [˜][1] _[B]_ [˜][1] _[X]_ [˜][1][Ψ][1][(] _[ℓ]_ [1] _[−]_ _[ℓ]_ [ˆ][)] _[∥][s]_ [+] _[ ∥]_ [Ψ] _[T]_ 2 _[γ]_ [˜][2] _[B]_ [˜][2] _[X]_ [˜][2][Ψ][2][(ˆ] _[ℓ]_ _[−]_ _[ℓ]_ [2][)] _[∥][s]_


_≤∥_ Ω( _ℓ_ 1 _−_ _ℓ_ [ˆ] ) _∥s_ + _∥_ Ω( _ℓ_ [ˆ] _−_ _ℓ_ 2) _∥s_


_≤_ _α∥ℓ_ 1 _−_ _ℓ_ [ˆ] _∥s_ + _α∥ℓ_ [ˆ] _−_ _ℓ_ 2 _∥s_


= _α∥ℓ_ 1 _−_ _ℓ_ 2 _∥s,_


where the second line follows since either ( _B_ 1 _, C_ 1) or ( _B_ 2 _, C_ 2) can be used in


Φ along the boundary, the third line follows from the triangle inequality, the


fifth line follows from the contraction relation on ( _B, C_ )-constant sets and their


boundaries, and the sixth line follows since _ℓ_ [ˆ] is on the shortest path from _ℓ_ 1 to


_ℓ_ 2.


Next, consider the shortest path (a line) between any two points in the space


_{ℓ|ℓ_ _≥_ 0 _}_ . As established by Lemma 5.2, the ( _B, C_ )-constant sets are convex,


which means that a line cannot cross the boundary of any ( _B, C_ )-constant set


more than twice. Thus, the shortest path between the points can only cross


finitely many boundaries (at most 2 _·_ 2 [2] _[m]_, or two for each possible ( _B, C_ )

constant set). Then, by induction on the number of ( _B, C_ )-constant sets along


the shortest path, the contraction relation of Φ extends to the union of all ( _B, C_ )

constant sets, which is equivalently the whole space _{ℓ|ℓ_ _≥_ 0 _}_ by Lemma 5.2.


We now need to show that solutions are restricted to a compact set. Since


_ρ_ (Ω) _<_ 1, we can derive an upper bound for the solution by solving the domi

nating linear system Ω (which may or may not come from a feasible ( _B, C_ ) _∈K_ ),


taking the maximum coordinate, and forming the hypercube in which coordi

nates are bounded by 0 and this maximum coordinate. The Banach fixed point


266


theorem then gives the result.


**Theorem 5.4** We will first introduce the machinery behind the Kleene fixed


point theorem following the exposition from [25] and then use it to prove Theo

rem 5.4.


Let ( _P, ≤_ ) be a partially ordered set, meaning the binary relation _≤_ is reflex

ive, antisymmetric, and transitive.


  - ( _P, ≤_ ) is _ω_ **-complete** if every increasing (i.e., nondecreasing) sequence


_{xn}n∈_ N in _P_ has supremum in _P_ .


  - A function _f_ : _P →_ _P_ is _ω_ **-continuous** if it preserves supremums of in

creasing sequences. I.e., for every increasing sequence _{xn}n∈_ N in _P_ that


has supremum in _P_, the sequence _{f_ ( _xn_ ) _}n∈_ N also has supremum in _P_ and


lim lim _._
_n→∞_ _[f]_ [(] _[x][n]_ [) =] _[ f]_           - _n→∞_ _[x][n]_           

Notice that a _ω_ - continuous function is monotone increasing. This is a direct


consequence of preserving suprema of all increasing sequences.


**Theorem 5.9.** _**(Kleene fixed point theorem)**_ _Let_ ( _P, ≤_ ) _be a ω-complete partially_


_ordered set and f_ : _P →_ _P be a ω-continuous function. If there is x ∈_ _P such that_


_x ≤_ _f_ ( _x_ ) _, then_ ¯ _x_ = sup _{f_ _[n]_ ( _x_ ) _|n ∈_ N _} is the least fixed point of f in {y ∈_ _P_ _|y ≥_ _x}._


Let R [¯] be the completion of the real numbers with _∞_ . We will work in this


extended space and draw our results back to the normal real space. We now


prove Theorem 5.4.


267


_Proof._ First notice ( _{ℓ_ _∈_ R [¯] _[m]_ _|ℓ_ _≥_ 0 _}, ≤_ ) is a _ω_ - complete partial ordering. Choose


_x_ = 0 and note that 0 _≤_ Φ(0). Notice that we are working in an extension of R _[m]_,


and so we may find that the fixed point promised by the theorem is infinite. To


address this, we have assumed that there is a (finite) fixed point on R _[m]_, and so


the minimum fixed point must also be finite. It now remains to be shown that


Φ is _ω_ - continuous.


Take two sequences _xn ↑_ _x_ ¯ and _yn ↑_ _x_ ¯ in the partial ordering. We need


to establish that lim _n→∞_ Φ( _xn_ ) = lim _n→∞_ Φ( _yn_ ). This result is immediate if all


coordinates of ¯ _x_ are finite since Φ is continuous and monotone increasing. So


suppose some coordinates of ¯ _x_ are infinite. As we go along the process Φ( _xn_ ),


a finite number of edges and caps can be activated, after which activations


stop. Thus there is a step _N_ after which Φ will be a linear map on the remain

ing _xn_ s. The same is true for some step _M_ for the sequence of _yn_ s. Then for


_n ≥_ max( _M, N_ ), the Φ( _xn_ ) and Φ( _yn_ ) will lie on an increasing hyperplane, with


˜ ˜
Φ( _xn_ ) = Ψ _[T]_ _γB_ [˜] ( _X_ [˜] Ψ _xn_ + ˜ _v_ ) + _Cc_ and Φ( _yn_ ) = Ψ _[T]_ _γB_ [˜] ( _X_ [˜] Ψ _yn_ + ˜ _v_ ) + _Cc_, for some


_B, C,_ Ψ( _C_ ). Since _xn ≥_ 0 we then have


lim
_n→∞_ [Φ(] _[x][n]_ [) = Ψ] _[T]_ [ ˜] _[γ]_ [ ˜] _[B]_ [ ˜] _[X]_ [Ψ lim] _n→∞_ _[x][n]_ [ + Ψ] _[T]_ [ ˜] _[γ]_ [ ˜] _[B][v]_ [˜][ +] _[ Cc]_


= Ψ _[T]_ _γ_ ˜ _B_ [˜] _X_ [˜] Ψ¯ _x_ + Ψ _[T]_ _γ_ ˜ _B_ [˜] _v_ ˜ + _Cc._


The last equality holds since ¯ _x_ is the supremum of _xn_ and thus lies on the same


extended hyperplane. The same equality holds for the _yn_ sequence.


Now define Φ(¯ _x_ ) := lim _n→∞_ Φ( _xn_ ) for any sequence _xn ↑_ _x_ ¯. By the above, this


is well-defined because the value is independent of the sequence chosen. Thus


Φ is _ω_ - continuous. Then the Kleene fixed point theorem gives the results.


268


**Theorem 5.5**


_Proof._ Because Φ is the composition of an increasing affine map, an element

wise maximum with 0, and an element-wise minimum with _c >_ 0, Φ is non

negative and monotone increasing.


We now show that we can restrict the domain of Φ to a complete lattice con

taining all fixed points. In the worst case, all finite caps are met, leaving us with


the system Ψ0 _γX_ Ψ _[T]_ 0 [. Since this has spectral radius] _[ <]_ [ 1][, this subsystem has a]


unique fixed point _ℓmax_ by the result in the previous section. Thus, in the worst


case, this is the maximum fixed point of Φ. Note that this is dependent on the


shock _s_, but such a point exists for each _s_ . Let _y_ be the maximum element of _p_


and form the complete lattice [0 _, y_ ] _⊂_ R _[m]_ bounded in each coordinate by 0 and


_y_ .


Restrict the domain of Φ to [0 _, y_ ]. Then the Tarski fixed point theorem gives


us the existence of least and greatest fixed points.


**Lemma 5.7**


_Proof._ Let _Li∗_ := ( _Le_ ) _i_ and _L∗i_ := ( _L_ _[T]_ _e_ ) _i_ . Then ∆ _i_ ( _L_ ) = _L∗i −_ _Li∗_ . Note that


_L∗i_ = _f_ _[i]_ ( _Li∗_ ), where



_f_ _[i]_ ( _Li∗_ ) := 
_j_



Γ _ji_ ( _Li∗_ + _shi −_ _DDji_ ) _∨_ 0 _∧_ _CPji_ _._

- - - 


This is because the amount that reinsurers reimburse _i_ is dependent on the lia

bilities that _i_ directly faces–i.e., _Li∗_ .


269


Then ∆ _i_ ( _L_ ) = _f_ _[i]_ ( _Li∗_ ) _−_ _Li∗_ is monotone decreasing (i.e., nonincreasing) in


_Li∗_ since reinsurance is limited to 100%. When a contract deductible is reached,


the negative slope lessens. When a contract cap is reached, the negative slope


steepens. However, the 100% reinsurance limit means that the slope is never


greater than zero.


Since _L ≥_ _L_ _[′]_, we also have _Li∗_ _≥_ _L_ _[′]_ _i∗_ [. The result then follows from the fact]


that ∆ _i_ ( _L_ ) = ∆ _i_ ( _Li∗_ ) is monotone decreasing in _Li∗_ .


**Lemma 5.8**


_Proof._



_L_
_ij_

  _j_







∆ _i_ ( _L_ ) = 
_i_ _i_




- �



_Lji −_  _j_ _j_



_i_



=

 


_Lij −_  _i,j_ _i,j_



_L_
_ji_

_i,j_



= 0


**Theorem 5.6**


_Proof._ Without loss of generality, assume _L_ _[′]_ = _L_ _[−]_, the least fixed point. Since


_L ≥_ _L_ _[′]_, Lemma 5.7 implies that ∆( _L_ ) _≤_ ∆( _L_ _[′]_ ).


270


Now suppose there exists _i_ such that ∆ _i_ ( _L_ ) _<_ ∆ _i_ ( _L_ _[′]_ ). Then we in turn have







∆ _L_ _[′]_ _._
_j_ ( )

_j_



∆ _j_ ( _L_ ) _<_ _j_ _j_



However, by Lemma 5.8, we know that







∆ _L_ _[′]_ _._
_j_ ( )

_j_



∆ _j_ ( _L_ ) = 0 = _j_ _j_



Thus there can be no such _i_ .


**Proposition 5.1**


_Proof._ We first show that, at each step, the system ( _I −_ _γBX_ ) is nonsingular. We


are given _ρ_ ( _γX_ ) _<_ 1. Then, as noted in the proof to Theorem 5.3, the spectral


radii obey


_ρ_ ( _γBX_ ) _≤_ _ρ_ ( _γX_ ) _<_ 1


for any diagonal _B_ with 1-0 entries since _B_ - nly serves to remove edges from the


initial line graph. Then the Neumann series gives us that ( _I −_ _γBX_ ) is invertible


at each step in the algorithm.


The algorithm converges to the correct solution by a simple monotonicity


argument. At each step, we have _Bt ≤_ _B_ [ˆ], where _B_ [ˆ] is the true set of edge activa

tions, since we start with all edges unactivated and edges that become activated


are direct propagations of the claims on primary insurers. The sequence of _Bt_


is monotonically increasing in entries since the activation of edges can only in

crease the number of other edges that become activated. _Bt_ can update at most


_m_
times as that is how many edges can become activated. Eventually, we reach


271


a state that represents the correct edge activations, after which the contagion


spreads to no further edges, and the edge liabilities are the solution to the re

sulting linear system. This equilibrium point is the unique fixed point since


solving the linear system and checking that _B_ does not change is equivalent to


verifying a fixed point of Φ. As each step requires solving a linear system (re

quiring in general _O_ ( _m_ [3] ) time), and there are at most _m_ steps, the total running


time is at most _O_ ( _m_ [4] ).


**Proposition 5.2**


_Proof._ As before, we first show that, at each step, the system ( _I −_ _γ_ ˜ _B_ [˜] _X_ [˜] ) is non

singular. We are given _ρ_ (Ω) _<_ 1. Then, as noted in the proof to Theorem 5.3, the


spectral radii obey


_ρ_ (˜ _γB_ [˜] _X_ [˜] ) _≤_ _ρ_ (Ω) _<_ 1 _,_


for any ( _B, C_ ) _∈K_ and Ψ( _C_ ) since ˜ _γB_ [˜] _X_ [˜] is effectively a subgraph of Ω after


removing edges under _B_ and nodes under Ψ.


We are given _ρ_ (Ψ _γX_ Ψ) _<_ 1. This applies to the first iteration of the algo

rithm. All subsequent iterations involve ( _C, B_ ) _∈K_ . In particular, the last iter

ative _ℓ_ value at that point in the algorithm is feasible for the given ( _C, B_ ). Thus


at each iteration, we have _ρ_ (˜ _γB_ [˜] _X_ [˜] ) _<_ 1. Then the Neumann series gives us that


( _I −_ _γ_ ˜ _B_ [˜] _X_ [˜] ) is invertible at each step in the algorithm.


The algorithm converges to the correct solution by a monotonicity argument


as in Proposition 5.1. However, the setup here is more nuanced. If the iteration


had started at 0 in this setting, we would lose the property that _Bt ≤_ _B_ [ˆ] and _Ct ≤_


272


_C_ ˆ, where ˆ _B_ and ˆ _C_ are the true edge activations and cap activations, as some


edge activations could cause the linear solver to attribute more liability to some


edges than are allowed by their capacities. While the overcapacity would be


corrected in the following iteration, the overcapacity leakage could have caused


new activations in _Bt_ that cannot be corrected by the next iteration.


Instead of starting at 0, we start at an upper bound to the solution. Such an


upper bound is constructed by assuming all edges are activated ( _B_ = _I_ ) and


all finite caps are activated and solving the linear system, which has a unique


solution since as shown above. Now we will have _Bt ≥_ _B_ [ˆ] and _Ct ≥_ _C_ [ˆ] at


each step since we start with an element-wise overestimate in _B_ and _C_ and


any caps or edges that become deactivated through this process will have been


unsupported given the overestimate. In this event, either we correct an element


in _C_ downward or correct the same elements in both _B_ and _C_ downward. Thus


the sequences of _Bt_ and _Ct_ are also monotonically decreasing. Note that we


would never want to revise these corrections back upward in a later iteration as


these edges or caps will never be activated by liabilities that are lower element

wise than we have already tried in the previous round.


In the equilibrium, all edge and cap activations will be supported by the


equilibrium liability values. Eventually, we reach a state that represents the


correct edge and cap activations, and the edge liabilities are the solution to the


resulting linear system. This equilibrium point is the unique fixed point since


solving the linear system and checking that _B_ and _C_ do not change is equivalent


Φ.
to verifying a fixed point of


At each step, either _B_  - r _C_ changes or we stop our iteration. Thus there


are at most 2 _m_ steps as there are at most 2 _m_ possible changes to _B_ and _C_ . The


273


most complex task at each step is again solving a linear system, which requires


in general _O_ ( _m_ [3] ) time. Note that the Ψ transformations are sparse (at most a


single entry per row and column) and can be computed in at most _O_ ( _m_ [2] ). Thus


the algorithm converges in at most _O_ ( _m_ [4] ) time.

#### **5.8 Appendix: Simulation Details** **5.8.1 Network Construction**


As the basis for our simulations, we use real network data on property and casu

alty reinsurance from 2012 Schedule F Part 3, as obtained from the National As

sociation of Insurance Commissioners [149]. This data details premiums ceded


to reinsurers by US insurance companies. Naturally, this data does not provide


all contract parameters, so we estimate these using common rules of thumb in


the insurance industry, which we back up with data where available.


**XL contract parameters**


We construct networks of XL contracts consistent with the NAIC data by esti

mating the coverage provided by each firm’s reinsurance contracts and separat

ing its reinsurers into two layers. We introduce the following ‘in-the-ballpark’


example of a reinsurance contract. [7]


**Example 5.2.** _(‘Ballpark’ Reinsurance Contract) Suppose $500M is the 1-in-100 year_


_loss for a firm. As an ‘in-the-ballpark’ figure, this firm would purchase reinsurance_


7Private conversations with an insurance industry executive. All errors are our own.


274


_coverage of $500M in losses with a deductible of $100M. The $400M total coverage_


_limit would be separated equally into 2-3 layers. The total premiums ceded for this_


_coverage would be 10% of the $400M limit. The lower layers would receive closer to_


_20% of their respective limits, while the higher layer would receive closer to 2-3% of its_


_respective limit._


This example suggests the following rules of thumb that we use to fill in


parameters in our real world network:


  - premiums ceded _≈_ 0 _._ 1 _·_ coverage limit,


  - coverage limit _≈_ 4 _·_ deductible,


  - coverage _≈_ 5 _·_ deductible, where coverage = coverage limit + deductible,


  - top layer premiums _≈_ 0 _._ 2 _·_ total premiums ceded.


The only publicly available reinsurance contract data that we are aware of


comes from major state catastrophe funds–for instance, the Florida Hurricane


Catastrophe Fund and the Texas Windstorm Insurance Association. We com

piled data on these reinsurance contracts, which is available in our code reposi

tory. This data supports that the first rule of thumb is reasonable.


Given a separation of a firm’s reinsurers into layers, these rules of thumb


allow us to estimate each contract’s deductible and cap. We then estimate each


contract’s proportion of the layer as


_γ_ = premiums ceded _/_ total premiums ceded for layer _._


Note that the coverage limits discussed above, which represent the cap payout


from the whole reinsurance tower, are different from individual contract caps,


275


which dictate the maximum payout from each contract that is itself only a part


- f the whole tower.


To separate a firm’s reinsurers into two layers, we use the last rule of thumb


to note that the premiums from the bottom layer should add to 80% of total


premiums and the premiums from the top layer should comprise the remaining


20%. This is a knapsack problem that we can efficiently solve approximately.


**Proportional contract parameters**


We construct networks of proportional contracts consistent with the NAIC data


_∞_
by setting all contract deductibles to 0, all contract caps to, and calculating


each contract’s coinsurance rate as


remium ceded
p
_γ_ =
(primary premiums + foreign reinsur. premiums + reinsur. premiums) _[,]_


where the denominator describes insurance premiums received by the ceding


firm in the contract. In this way, the ceding firm cedes a proportion of their total


risk for the same portion of the premiums they have received. We estimate the


primary premiums and foreign reinsurance premiums next.


**Primary insurance and foreign reinsurance premiums**


We additionally need to estimate the insurance premiums received from out

side the reinsurance network. If the receiving firm is a primary insurer, this is


the primary insurance premiums they receive. If the firm is a reinsurer, this is


foreign (outside US) reinsurance premiums.


We then generate figures for these values within an estimated range:


276


1. We collect data on premiums received and reinsurance premiums ceded


from 10-ks and annual reports. Our data is available in our code reposi

tory. From this data, we determine reasonable upper and lower bounds


   - n premiums ceded _/_ premiums received for firms.


2. For each firm in the network, we generate a random number uni

formly between the upper and lower bounds. This is used as the firm’s


premiums ceded _/_ premiums received ratio.


3. From this ratio, we calculate the outside premiums–either primary insur

ance or foreign reinsurance–that the firm must receive to achieve this ratio.


If the amount is negative, it is treated as zero.


Based on the data, primary insurers generally have ratios between 0.05 and


0.5, and reinsurers generally have ratios between 0.1 and 0.3. We use these


bounds in our simulations.


**Firm capital levels**


We next need to estimate each firm’s capital that is available for paying its liabil

ities (i.e., the firm’s equity). Current capital regulations focus on various factors


through Risk-Based Capital; however, past regulations focused on the simpler


leverage ratio [97]. For simplicity, we use this latter measure as a benchmark in


- ur simulations. The leverage ratio is defined in the following way:


leverage ratio = equity _/_ net written premiums _._


According to [179], American regulation required minimum 50% leverage ra

tios. They also state that 20% leverage ratios was a “rule of thumb” in the Ger

man market for property and casualty insurers.


277


We extend this information by collecting data on equities and net written


premiums from 10-ks and annual reports. Our data is available in our code


repository. We use this data to determine reasonable upper and lower bounds


- n current leverage ratios. Based on the data, insurers generally have leverage


ratios between 0.7 and 2.0, which we use as bounds in our simulations. We then


generate figures for firm leverage ratios within the estimated range:


1. For each firm in the network, we generate a random number uniformly


between the upper and lower bounds. This is used as the firm’s leverage


ratio.


2. From the ratio, we calculate the firm’s equity.


Note that following a market collapse, leverage ratios can plummet, which


can significantly affect the capital levels in the reinsurance network. This is the


reason that Risk-Based Capital is now used for regulation instead of the leverage


ratio. For the price of adding greater complexity to our simulations, we could


alternatively use Risk-Based Capital measures to estimate equity values instead.


**Shocks to primary insurers**


The final component of our simulation setup is to calibrate network shocks.


These shocks are claims on primary insurers in the network. For our simula

tions, we consider 1-in-100 year and 1-in-250 year shocks. Industry data on


the estimated aggregate size of these shocks is available from [5]. In particular,


the North American 1-in-100 year insured loss is estimated at $215.2B, and the


North American 1-in-250 year insured loss is estimated at $290.6B. We use these


numbers for the aggregate size of tail shocks in our simulations.


278


The remaining task is to distribute this aggregate shock to primary insurers


in the network. We do this in the following way:


1. For each firm, we generate a random number uniformly between 0 and the


size of that firm, defined by the total primary premiums received. Under


this scheme, the size of a primary insurer correlates with their exposure.


Reinsurers’ initial exposure is zero as they do not offer primary insurance


coverage.


2. We then generate the shock exposure ratios by normalizing these numbers


so that they add to 1. Multiplying by the size of the aggregate shock then


gives the size of claims to primary insurers under the shock.


In reality, the relation between the size of a primary insurer and its exposure


to aggregate shocks is more complex that we model here. On one hand, larger


primary insurers may be in a better position to diversify their holdings against


geographic risk. On the other hand, their exposures could be higher since their


portfolios are larger. In a more realistic model, we would want to account for


the geographic exposures of each primary insurer and simulate geographic tail


events. However, the data needed for this is not, in general, publicly available.

#### **5.8.2 Sensitivity to parameter perturbations**


In these simulations, we construct an XL network from our data as described in


the previous subsections. This is our base case for comparison. In this process,


we store the layering structure for future access. Given a multiplicative error


term _δ_ (i.e., a percentage error), we then perturb the network parameters as


279


follows:


  - For each premium ceded value, we generate a random number uniformly


in [1 _−_ _δ,_ 1 + _δ_ ] and multiply it with the premium ceded value.


  - We then construct the contract parameters using the perturbed premium


ceded values as described in the previous subsections using the stored


layering structure.


  - For each value of a firm’s primary insurance premiums received, foreign


reinsurance premiums received, and capital levels, we perturb it by a ran

dom multiplicative value uniformly chosen in [1 _−_ _δ,_ 1 + _δ_ ].

#### **5.8.3 Systemic effects of contract structures**


We construct systems that are comparable given the structure of the graph on


premiums ceded between insurers and our rules of thumb for XL reinsurance


contracts. We construct comparable systems using the methods from the pre

vious subsections keeping premiums ceded, firm capital levels, primary insur

ance premiums, and foreign reinsurance premiums constant. The only differ

ences are in how the ceded premiums are interpreted: as part of a proportional


scheme or XL contracts based on our rules of thumb and knapsack separation


- f layers.


280


CHAPTER 6


**OPTIMAL INTERVENTION IN ECONOMIC NETWORKS USING**


**INFLUENCE MAXIMIZATION METHODS**


The content of this chapter has previously appeared in:


“Optimal Intervention in Economic Networks using Influence Max

imization Methods.” Ariah Klages-Mundt and Andreea Minca. _**Eu-**_


_**ropean Journal of Operational Research**_, 300(3):1136-1148, 2022.


281


We consider optimal intervention in the Elliott-Golub-Jackson network


model [76] and we show that it can be transformed into an influence


maximization-like form, interpreted as the reverse of a default cascade. Our


analysis of the optimal intervention problem extends well-established target

ing results to the economic network setting, which requires additional theoret

ical steps. We prove several results about optimal intervention: it is NP-hard


and cannot be approximated to a constant factor in polynomial time. In turn,


we show that randomizing failure thresholds leads to a version of the problem


which is monotone submodular, for which existing powerful approximations in


polynomial time can be applied. In addition to optimal intervention, we also


show practical consequences of our analysis to other economic network prob

lems: (1) it is computationally hard to calculate expected values in the economic


network, and (2) influence maximization algorithms can enable efficient impor

tance sampling and stress testing of large failure scenarios. We illustrate our


results on a network of firms connected through input-output linkages inferred


from the World Input Output Database.

#### **6.1 Introduction**


Following the global crisis due to the COVID-19 medical and economic con

tagion, governments have unleashed unprecedented macroeconomic stimulus.


The variety of proposed stimulus, both in government financing and in mone

tary policy form, aims to support value in a shocked global economy. The tools


to support value following a systemic shock are there since the financial cri

sis, and new ones are being proposed. One difference to the financial crisis is


that the shock originated then from within the financial system and the main


282


intervention target were systemically important institutions, i.e., those whose


failure would lead to a large impact on the economy. In this crisis the shock was


external and created disruptions to many economic sectors worldwide. Conse

quently, intervention is much more widespread.


As learned from the financial crisis, network effects underpin systemic im

portance, which can be measured based on the size of loss cascades, see e.g,


[7, 68] or centrality measures, see [27] and the references therein. Work on sys

temic risk measures, e.g.,[51, 32, 81, 15], led to different axiomatic frameworks


for capital requirements such that aggregate risk is acceptable. Notably, ag

gregation functions underlying these systemic risk measures can account for


interconnections. In [9, 10, 47], authors explore optimal capital and liquidity


intervention, and derive insights into the intervention target in stylized core

periphery banking networks subject to the risk of bank runs. Their methods are


applied for small banking systems. In [4], authors cast the intervention problem


in the context of the Eisenberg-Noe model [75] as a mixed integer-programming


_ϵ_
problem, and propose a notion of of - optimality to solve it approximately. They


apply their methods to the Korean banking system. In contrast to these past


works, our paper focuses on the computational aspect of optimal intervention


problems, which becomes critical when the number of eligible firms is large.


When entire sectors, rather than a few large institutions, are hit by shocks, one


needs to understand the systemic impact of groups of firms and optimally de

cide on where to intervene. Such problem quickly becomes computationally


hard. The government’s criterion is to maximize the overall value in the system


under a budget constraint.


Our model relies on the notion of value of an organization –firm, sector,


283


country– introduced in [76] in the context of cross-holdings. Without interven

tion, if the value of the organization drops below a failure threshold, then there


are failure losses and the values of the connected organizations drop as well


and so on. This is also in the spirit of the distress notion in [184], which allows


for contagion before the point of default. The failure threshold is interpreted


as the value below which the organization ceases operations. Intervention can


be seen as a way to increase an organization’s value or alternatively lower its


failure threshold. Several types of interventions can be modeled by a decrease


- f the failure threshold of an organization. Government bailouts could take the


form of equity infusions, as they did in the financial crisis. Central banks are in

jecting liquidity in the economy via various asset purchase programs, including


corporate debt purchases.


It is clear that direct government financing allows firms to survive by directly


lowering the failure threshold. The effect of asset purchase programs (APP) is


more subtle. A point of contention is whether asset purchase programs involve


liquidity injection, or whether they involve value injection. When central banks


can purchase corporate debt they change the outcome in debt markets. [1] An


unavoidable fact of APP is that, whenever the central bank purchases illiquid


assets to intervene in liquidity, it must price those assets in some way. Models


are usually used to calculate a ‘fundamental value’. When acting as a lender


- f last resort, central banks may essentially accomplish bailout functions. Our


model captures both direct and indirect ways of lowering the failure thresholds,


as the value of the organization increases by the intervention amount.


1Arguably, central banks can lower the failure thresholds even without actual liquidity injection: for example Boeing raised debt in capital markets following the FED’s announcement that
[they would support corporate debt markets, see e.g. thttps://www.bloomberg.com/news](thttps://www.bloomberg.com/news/articles/2020-05-02/the-non-bailout-how-the-fed-saved-boeing-without-paying-a-dime)
[/articles/2020-05-02/the-non-bailout-how-the-fed-saved-boeing-without](thttps://www.bloomberg.com/news/articles/2020-05-02/the-non-bailout-how-the-fed-saved-boeing-without-paying-a-dime)

[-paying-a-dime.](thttps://www.bloomberg.com/news/articles/2020-05-02/the-non-bailout-how-the-fed-saved-boeing-without-paying-a-dime)


284


Interventions may be accompanied by long-term moral hazard effects. Firm


default is an important long-term filter that incentivizes strong and compe

tent management. The prospect of intervention can disincentivize proper risk


management, enabling additional short-term profits to management and equity


holders while transferring tail risks to government. Note, however, that inter

ventions can be shaped to reduce moral hazard (e.g. by organizing bail-ins by


the creditors and thereby diluting equity holders). In [30], authors endogenize


intervention for a network of banks. In their paper, a bail-in can be organized


in equilibrium if and only if the regulator’s no-intervention threat is credible,


namely in the last stage of the game she could optimally abandon intervention.


Our work is complementary and could be used for the last stage of such a game,


as we find the organizations that need intervention. We leave moral hazard con

siderations for future work, given that the widespread consensus of decision


makers was to first preserve value following the COVID-19 crisis. We focus on


the specific question of how to design targeted interventions that exploit net

work effects while leaving the precise micro structure of those interventions as


a separate problem.


Our work is also part of the broader literature on targeting in networks, see


e.g., [22, 82], and in particular the literature on optimal diffusions of products


- r innovations or influence maximization, [71, 101, 102]. Our contributions are


summarized below.


**This paper.** We construct an economic network intervention model and show


how it can be solved by adapting influence maximization methods (Section 6.2).


Our analysis extends well-established targeting results to the economic net

work setting, requiring additional theoretical steps over the classical setting.


285


_∼_
For instance, the dependency matrix (“influence matrix”) is more complex (


the Neumann series of the matrix in a linear influence setting that is column

substochastic with zero diagonals) taking into account the effect of a firm on


itself and the structure of default reversals (“activations”) is more nuanced. We


contribute the following results, which provide the groundwork for adapting


powerful targeting algorithms to solve several economic network problems:


1. We define an optimal economic network intervention problem and show


how it can be expressed in an influence maximization-like form (Sec

tion 6.2.2).


2. We prove that it is NP-hard to optimize the economic network interven

tion and cannot be approximated to a constant factor in polynomial time


(Theorem 6.1 and Corollary 6.1).


3. We prove that, when modified to consider expected values under ran

dom thresholds, the intervention problem is monotone submodular (The

   - rem 6.2) and thus admits a greedy polynomial time (1 _−_ 1 _/e −_ _ϵ_ )

approximation (Corollary 6.2).


4. We show that similar results extend to a related problem: identifying large


failure cascade scenarios. We prove that it is NP-hard to find the worst case


failure scenarios given a maximum sized aggregate shock to asset values


(Theorem 6.3). Under randomized thresholds, a similar greedy approxi

mation is applicable.


5. We show two practical consequences of Theorem 6.3 in Section 6.3.3. (1)


It is computationally hard to calculate expected values in the economic


network. (2) Intervention approximation algorithms can be applied for


importance sampling to identify instances that lead to tail events, which


286


can be very valuable applied to stress testing. The depth of sampling in


the tail can be tailored by choosing a parameter.


6. We demonstrate a proof-of-concept of optimal intervention approximation


applied to economic networks constructed from the World Input-Output


Database (Section 6.4).

#### **6.2 Model**


In this section, we supplement the Elliot-Golub-Jackson network contagion


model [76] to incorporate targeted interventions. We then formulate an optimal


intervention problem that relates the economic intervention problem to influ

ence maximization problems.

#### **6.2.1 Financial network contagion model**


We define an economic network ( _C, D, β,_ _**θ**_ _,_ **p** ) based on the Elliot-Golub

Jackson network contagion model as follows:


 - _U_ = _{_ 1 _,_ 2 _, . . ., n}_ the set of firms/nodes in the network


 - _m_
assets owned by firms


 - **p** = _m ×_ 1 vector of asset prices


 - _D_ = _n × m_ matrix with _Dik ≥_ 0 the share of asset _k_ held by firm _i_ (adding


to 1)


 - _C_ = _n × n_ matrix with _Cij ≥_ 0 the fraction of firm _j_  - wned by firm _i_ and 0


along the diagonals


287


Nodes own assets,
parts of other nodes



If node value < threshold,

nonlinear default cost incurred


Default costs propagate








|assets,|Col2|
|---|---|
|Assets<br>Firm 1<br> <br>  r nodes||
|Assets|Assets|



Figure 6.1: Financial network propagation mechanism.


 - _C_ [ˆ] = _n × n_ diagonal matrix with _C_ [ˆ] _ii_ = 1 _−_ [�] _j_ _[C][ji]_ [ the share of organization]


_i_ not owned by another firm in the system


 - _**θ**_ = _n ×_ 1
vector of failure thresholds for each firm


 - _β_ = _n × n_ diagonal matrix of extra failure costs for each firm.


The matrix _C_ describes the linear cross-holding relationships between firms. If


a firm _i_ ’s market value (defined next) falls below its threshold _θi_, it incurs an


extra failure cost _βii_ . We assume _C_ is column sub-stochastic as otherwise _C_ [ˆ] _[−]_ [1] is


not well-defined. Notice that this also means that _I −_ _C_ is invertible because the


spectral radius _ρ_ ( _C_ ) _<_ 1.


The network propagates asset values and defaults across firms in the net

work. We illustrate this conceptually in Figure 6.1. _D_ describes the mapping


- f underlying assets (blue nodes) to firms (orange nodes). _C_ describes cross

holdings between firms. The breach of a threshold triggers failure costs, which


propagate to other firms through _C_ .


288


Firm book values are given by


**V** = _C_ **V** + _D_ **p** _−_ _β_ 1 _{_ **v** _<_ _**θ**_ _},_


where 1 _S_ is the 1-0 valued vector indicating the entries of set _S_ . **V** represents the


vector of all book values across the network. The first term _C_ **V** gives the firm


cross holdings, i.e., the book value of each firm contains a fraction of the values


- f all other book values. The second term _D_ **p** represents the value of the external


asset holdings, in vector form. Finally, the last term represents bankruptcy costs,


which occur in the case that the market value of the firm drops below a failure


threshold.


Notice that book values inflate the value of underlying assets because asset


values are counted multiple times across firms (consequently, _∥_ **V** _∥_ 1 _≥∥_ **p** _∥_ 1 and


can be arbitrarily large). A more useful measure of value is a scaling of book


values by _C_ [ˆ], accounting for the ownership share that each firm retains in itself.


These are market values, which are given by


**v** = _C_ [ˆ] **V** = _C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] ( _D_ **p** _−_ _β_ 1 _{_ **v** _<_ _**θ**_ _}_ ) _._


In [76], authors show that the matrix _C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] is column-stochastic.


**Lattice of solutions.** As defined, there is always a solution for **v** . The set of so

lutions forms a complete lattice via Tarski’s fixed point theorem. Further, supre

mum and infimum exist (best and worst cases). The analysis in [76] focuses on


the best case solution as other solutions in the lattice are due to self-fulfilling


failures.


289


**Intervention lowers thresholds.** Beyond the core model from [76], we add a


vector of intervention payments _**γ**_ _≥_ 0, which affect the default status of firms.


Given an intervention profile _**γ**_, firm _i_ now defaults if


_Vi_ + _γi <_ [ _C_ [ˆ] _[−]_ [1] _**θ**_ ] _i._


This leads to post-intervention market values


**˜v** = _C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] ( _D_ **p** _−_ _β_ 1 **V** + _**γ**_ _<_ ˆ _C−_ 1 _**θ**_ ) _._


An intervention via this mechanism effectively lowers the failure threshold


- f firms. This is consistent with real-world intervention mechanisms as dis

cussed in the introduction.

#### **6.2.2 Optimal intervention**


Defining an optimal intervention requires a performance measure for the sever

ity of a cascade. In economic networks, nodes can vary vastly in size with


larger and more connected institutions being more systemically important than


smaller less connected institutions. A good performance measure for economic


networks will be akin to total value of surviving nodes in the network. In an


- ptimal intervention, we should seek to maximize this or, equivalently, mini

mize the value destroyed in a default cascade. We require an appropriate _weight_


_function w_ ( _S_ ) that outputs the importance measure of node set _S ⊆_ _U_ . A few


_w_

- bvious and simple choices for are consistent with maximizing value or mini

mizing value destroyed. For example: fixed node weightings of current market


values of nodes, e.g.,


_w_ ( _S_ ) =           - _vi_

_i∈S_


290


- r, relatedly, the level of failure costs _β_ associated with each node. In particular,


these choices allow us to capture the size importance of nodes., e.g. _w_ ( _S_ ) =

- _i∈S_ _[β][i]_ [. A well-defined intervention objective is then to maximize] _[ w]_ [(] _[S]_ [)][ where]


_S_ is the set of non-defaulting nodes.


A well-defined optimal intervention also requires a resource constraint. We


define _b_ to be the intervention budget. Then a well-defined optimal intervention


is the solution to the following optimization problem.


max _w_ ( _S_ )
_**γ**_ _≥_ 0 (6.1)

s.t. **1** _[T]_ _**γ**_ _≤_ _b_


where **1** is the all-ones vector.


Toward solving this, it will be convenient to transform the problem and in

troduce some additional notation. We can reinterpret the intervention problem


in the economic network model as the following: given an impending default


cascade, how do we find an optimal intervention to optimally reduce defaults?


_T_ .
Suppose that the set of nodes that would default without intervention is


Now reduce the system to only look at effects on the nodes in _T_, while preserv

ing the entire network structure. To do this, suppose that the set of nodes that


would default without intervention is _T_ . In particular, define the following


 - _IT_ = diagonal matrix with _Iuu_ = 1 for _u ∈_ _T_ and 0 otherwise.


 - Ψ( _T_ ) maps to a system on the non-zero diagonal coordinates of _IT_ . Es

sentially, Ψ( _T_ ) is the _|T_ _| × |U_ _|_ matrix obtained by dropping zero rows of


_IT_ .


291


We can apply the above map to transform the system to look at


**¯v** := Ψ( _T_ ) _C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] ( _D_ **p** _−_ _β_ 1 **v** _<_ _**θ**_ ) _._


This transformation removes firms that don’t fail without intervention, while


preserving the networked connections through such nodes. The idea is that


among the firms who would fail without intervention, some of them will be


saved by direct intervention. Their value would then go above the failure


threshold and in particular the failure costs are reversed. In a reverse causal rela

tion of failure, other firms would be indirectly saved because their value would


also increase. To simplify notation, we will proceed where applicable without


the bar and Ψ notation, but assuming we are working in the transformed prob

lem that only directly considers nodes _T_ - n which we may intervene. In the


sequel, it is understood that the set _T_ is fixed.


**Intervention impact function.** We next let the set function _f_ define the inter

vention impact vector on the nodes in _T_ from an intervention that reverses the


failures of nodes in the set _S ⊆_ _T_ . In particular, _fu_ ( _S_ ) is the impact on node _u_


from the intervention on nodes in _S_ . As we will explain, this is given by


_f_ ( _S_ ) = ( _I −_ _C_ ) _[−]_ [1] _β_ 1 _S −_         - _Iu_ ( _I −_ _C_ ) _[−]_ [1] _β_ 1 _u ._ (6.2)

_u∈S_


This accounts for the effect on book values across the network of reversing fali

ure costs in the _S_ nodes (the first term), which pushes other nodes closer to their


failure reversal thresholds. Note that the reversal of a node’s default has an ef

fect on itself through cross-holdings. Further, notice that the intervention _**γ**_ does


not need to cover the cost of _β_ as the intervention stops this cost from being re

alized in market values. The second term in _f_ ( _S_ ) removes this self-influencing


292


effect from the impact function as it is instead represented in reduced interven

tion thresholds. Notice that _f_ ( _∅_ ) = 0 so that the impact function is normalized.


**Intervention thresholds.** For the initial defaulting set _T_ and a node _u ∈_ _T_, we


define the intervention threshold _θ_ [˜] _u_ to describe how much book values would


_u_
need to change in order for the failure of to be reversed. With some simple


algebra, this is given by



˜ ˆ
_θu_ = _C_ _[−]_ [1] _**θ**_ _−_ ( _I −_ _C_ ) _[−]_ [1] ( _D_ **p** _−_ _β_ 1 _T_ _\{u}_ )

   -   


(6.3)

_u_



This can be interpreted as the slack below threshold in the economic network.


We can obtain this by taking [ _C_ [ˆ] _[−]_ [1] _**θ**_ _−_ ( _I −_ _C_ ) _[−]_ [1] ( _D_ **p** _−_ _β_ 1 _T_ )] _u_, the divergence of


book value from the failure threshold (measured in book value), and subtracting


the self-influencing effect described above.


**Evaluating an intervention.** The intervention _γ_ reverses the defaults of a


“seed” set of nodes _S_ 0 _⊆_ _T_ . The set _S_ 0 is composed of nodes _u_ for which _γu ≥_ _θ_ [˜] _u_ .


We can iteratively construct subsequent sets of nodes _Si ⊆_ _T_ (for _i ≥_ 1) whose


defaults are reversed by propagating the effects of _Si−_ 1. This is done by adding


to _Si−_ 1 the nodes _u_ such that


_fu_ ( _Si−_ 1) + _γu ≥_ _θ_ [˜] _u._


Note that the amounts in _γ_ can be a fraction of the thresholds of the nodes.


This allows more efficient use of the budget _b_ . In particular, this takes advantage


- f the fact that we don’t have to spend as much to impact a node that already


has partial impact exerted from other impacted nodes.


293


This leads to an optimization problem equivalent to (6.1). The only change is


in the restriction of _S_ to the superset _T_, which leads to the change of a constant


_T_ .
term in the objective involving the weights of the nodes not in


**Randomized thresholds.** We will further consider a modified form of the


problem with randomized thresholds. For instance, this is the case if there is


some inherent uncertainty about what the thresholds are. In this case, a well

defined intervention problem is to optimize the expected performance measure


- f the intervention:


_σ_ ( _**γ**_ ) := E[ _w_ ( _S_ ) _|_ _**γ**_ ] _,_ (6.4)


where the expectation is taken over the random thresholds. This corresponds to


the _fractional_ intervention problem, where we select arbitrary _**γ**_ . In the proofs,


it will be helpful to start with a simplified _integral_ intervention problem, where


we select nodes to bail out in the initial seed set _S_ 0, intervening with the full in

tervention threshold value. In this case, the appropriate expected performance


measure of the intervention is


_σ_ ( _S_ 0) := E[ _w_ ( _S_ ) _|S_ 0] _._ (6.5)


These optimization problems bears striking similarity to influence maxi

mization models in social networks, like in [101, 66], with several key differ

ences in the forms of _f_ and _θ_ **[˜]**, particularly in accounting for the effects of a firm


_w_ .

- n itself, and appropriate weight functions


294


#### **6.3 Analytical Results**

In the previous section, we set up an economic network model and a well

defined optimal intervention problem that relates to influence maximization


problems. We discuss these influence models in Appendix 6.6.1. In the remain

der of the paper, we will develop this connection, which allows us to transfer


powerful tools from the influence maximization literature to the world of eco

nomic interventions.


Our proofs, given in Appendix 6.6.2 rely on strategies used in some sim

pler influence maximization-like problems, such as the linear influence model.


New challenges arise when reducing from the independent set problem to the


economic network intervention setting, which is a class of instances of more


general influence maximization-like problems.


We prove theoretical properties of the intervention model. We prove that it


is NP-hard to optimize the economic network intervention and cannot be ap

proximated to a constant factor in polynomial time. Additionally, we prove that


randomizing thresholds under appropriate assumptions yields objective func

tions that are monotone and sub-modular. Namely, we show that the economic


network intervention problem, when modified to consider expected values un

der random thresholds, is monotone submodular. Consequently, one can use


the results from [146, 66] to provide an (1 _−_ 1 _/e −_ _ϵ_ )-approximation in polyno

mial time.


295


#### **6.3.1 Hardness of optimal intervention**

In our first result, we show that the optimal economic network intervention


problem is NP-hard. Note that this result is not a consequence of influence


maximization hardness results in, e.g., [101, 66, 90]. While we can transform


the economic network intervention model into a form that resembles influence


maximization, that does not mean that the general hardness of influence maxi

mization extends to this case.


**Theorem 6.1.** _Let_ ( _C, D, β,_ _**θ**_ _,_ **p** ) _be a financial system with n firms and deterministic_


_thresholds θ, and let_ 0 _≤_ _ℓ< α ≤_ 1 _. Suppose αn firms fail in the financial system equi-_


_librium. Then it is NP-hard to determine whether there exists an intervention γi ≥_ 0


_with ∥_ _**γ**_ _∥_ 1 _≤_ _b such that at most ℓn nodes fail after the intervention._


[Link to Proof]


Recall that the meaning of NP-hard is that a general instance of the problem


is hard, while naturally there may be parameter values (e.g., budget of zero) for


_w_
which the problem may not be hard. We prove this for with equal weights,


which means that the problem is NP-hard for general weighting functions. The


proof is a reduction from independent set.


A consequence of the theorem is the following corollary describing hardness


- f approximation.


**Corollary 6.1.** _Optimal economic network intervention cannot be approximated to_


_within a constant factor in polynomial time._


Additionally, note that it may be much harder to approximate the optimal


296


intervention problem than proven in Corollary 6.1. For example, similar influ

ence maximization problems have approximation difficulties that scale in the


dimensions of the system [66, 90].


**Remark 6.1.** _(Default hierarchies) While we can identify the hierarchy of defaults in_


_the initial cascade, which the intervention aims to counteract, this does not make the_


_optimal intervention problem, in general, easier. Consistent with Corollary 6.1, simply_


_intervening in a layer of this hierarchy, which would prevent all defaults in subsequent_


_layers, does not guarantee a good approximation to optimal intervention. In particular,_


_only intervening across an entire layer may be far from optimal if all layers are very_


_wide. This is the case in the 2008 financial crisis but closer to the case in the 2020_


_Covid crisis, when much of the economy was shut down. Intuitively, the initial default_


_hierarchy doesn’t describe all possible sequences of default; making some intervention_


_payments in turn alters the effective hierarchy sequence. Similar “activation hierar-_


_chies” are also present in the influence maximization literature and do not make those_


_problems easier either. The default hierarchy does not help us devise an approxima-_


_tion algorithm in general, which remains true when using different objective weighting_


_functions, including current total market cap of solvent firms._

#### **6.3.2 Approximation with randomized thresholds**


We now establish that a modified form of the optimal intervention problem can


be well-approximated in polynomial time. The modification incorporates ran

domized thresholds and reframes the problem to optimize _in expectation_ . For


instance, this can be done by treating thresholds as random variables uniformly


distributed over any given uncertainty range. This can be done more gener

ally with different threshold distributions, as we will discuss. In essence, the


297


combinatorial complexity problems disappear in expectation. [2]


We first show that the intervention problem with random thresholds is


monotone submodular, connecting with results from [146] and [66]. As a re

sult, a greedy hill-climbing algorithm provides a (1 _−_ 1 _/e −_ _ϵ_ )-approximation


using results from [61, 151].


Our next result establishes that the intervention impact function in the inter

vention problem is monotone submodular.


**Prop. 6.1.** _The function f from Eq. 6.2 is monotone increasing and submodular._


[Link to Proof]


We need a few assumptions to prove that the objective _σ_ for intervention


problem under random thresholds is monotone submodular. The first assump

tion describes the randomization of thresholds and is necessary for the results


- f [146] to apply. It allows very general distributions of thresholds, an example


- f which is uniform distributions.


**Assumption 6.1.** _For u ∈_ _U_ _, random thresholds θu are independent with distribution_


_function Fu such that Fu ◦_ _fu is monotone increasing submodular._


The next assumption is that the intervention impact function _f_ is


normalized–all nodes in _T_ start out in default. With fixed thresholds, this is a


property of _f_, as noted in the previous section. If we make thresholds _**θ**_ random


in the economic network setting, this is more complicated because the corre

sponding intervention thresholds _**θ**_ **[˜]** in (6.3) could be zero or negative depending


2Since the range of the random variables can be arbitrarily small, this is like saying that the
approximation problem is difficult only on measure 0 sets.


298


- n the realization of thresholds, and, if this occurs, the resulting _**θ**_ **[˜]** distributions


are not independent. This can be solved in two ways that keep the initially


defaulting nodes technically fixed: (1) the randomization in thresholds can be


associated with _**θ**_ **[˜]** _≥_ 0 instead of with _**θ**_, or (2) the problem can be reformulated:


_**θ**_ **˜** becomes the positive part in (6.3), initial defaults are fixed, _f_ ( _∅_ ) := 0, and


when _θ_ [˜] _u_ = 0, _u_ can be added to the seed set with cost 0 (and so will be added


first).


**Assumption 6.2.** _The intervention impact function f is normalized, i.e., f_ ( _∅_ ) = 0 _._


The final assumption concerns the function describing node weighting in


the objective. The weight function describes how valuable it is to reverse the


defaults of a given set of nodes.


**Assumption 6.3.** _The weight function w_ : 2 _[U]_ _→R_ + _is normalized, monotone, and_


_submodular._


A very flexible range of functions satisfies this assumption. For example, the


cardinality function, which weights each node equally would be interpreted as


minimizing the number of defaults. As discussed in the previous section, for


economic networks, we generally want to incorporate the size and importance


- f nodes into this function, as we want to maximize something like the total


welfare of surviving nodes in the network or minimize the value destroyed in


a default cascade. Any fixed weighting of nodes also obeys this assumption,


including weighting by the current market values of firms or, relatedly, the level


- f failure costs associated with each node.


Under these assumptions, the intervention objective function–e.g., the ex

pected number of defaults under a given intervention–is monotone submodular


299


based on results from [146], as formalized in the next result.


**Theorem 6.2.** _Given assumptions 1-3 and an instance of the economic network inter-_


_vention problem with random thresholds, then σ_ ( _S_ 0) _and σ_ ( _**γ**_ ) _are normalized, mono-_


_tone, and submodular._


[Link to Proof]


Then following the application of results in [101], there is a greedy


(1 _−_ 1 _/e −_ 1 _/_ poly( _n_ ))-approximation algorithm for optimizing the expec

tation, as formalized in the next corollary. The integral and fractional forms of


this greedy algorithm are described in Appendix 6.6.3 (Algorithm 6 and Algo

rithm 9).


**Corollary 6.2.** _Given assumptions 1-3, there exists a polynomial-time greedy_


(1 _−_ 1 _/e −_ _ϵ_ ) _-approx. for maximizing σ_ ( _S_ 0) _and σ_ ( _**γ**_ ) _subject to budget b._


[Link to Proof]

#### **6.3.3 Identifying large failure cascade scenarios**


We now show how these results translate into related economic network prob

lems. We start by showing that it is also NP-hard to identify the worst case fail

ure scenarios given a maximum sized aggregate shock to asset values **p** . Like


the intervention problem, there is a (1 _−_ 1 _/e −_ _ϵ_ )-approximation under random


thresholds. While we may not generally be interested in uncovering the strictly


_worst_ failure scenarios, we will see that the results about this _do_ lead to very


useful and interesting applications regarding sampling tail events in general.


300


**Theorem 6.3.** _Suppose_ ( _C, D, β,_ _**θ**_ _,_ **p0** ) _is an instance of an economic network and asset_


_prices evolve to_ **p1** _such that ∥_ **p0** _∥_ 1 _−∥_ **p1** _∥_ 1 _≤_ _b for some maximum aggregate shock_


_b >_ 0 _. Let_ 0 _< ℓ<_ 1 _. Then it is NP-hard to determine if a failure cascade of size ℓ|U_ _| is_


_possible in_ ( _C, D, β,_ _**θ**_ _,_ **p** 1) _._


[Link to Proof]


The reduction from independent set again implies a corollary result that the


- ptimum is hard to approximate up to a constant factor in polynomial time. As


in the intervention case, when reframed in terms of expectations under random


thresholds, a greedy (1 _−_ 1 _/e −_ _ϵ_ )-approximation again applies.


As alluded above, we now develop two useful and interesting consequences


- f these results: (1) it is computationally hard to calculate expected values of


nodes in the economic network, and (2) approximation methods can be applied


for importance sampling to identify instances that lead to events in the tail. The


depth of sampling in the tail can be tailored by choosing the parameter _b_ . This


can be very valuable for the application of stress testing.


**Hardness of calculating expected values.** We next demonstrate a conse

quence of Theorem 6.3, namely it can be computationally hard to calculate ex

pected values of firms in an economic network even if we have perfect informa

tion about the underlying setup. Consider a simple setting in which the prices


- f underlying assets **p** are i.i.d. Bernoulli distributed 0-1 with probability _q_ . The


probability that a specific set of _b_ assets fail is (1 _−_ _q_ ) _[b]_, which is non-vanishing


in the scale of the network and so non-negligible for the calculation of expected


value of firms when the problem is large (and potentially computationally com

301


plex). Since it is NP-hard to determine whether a large failure cascade can occur


with that probability, it is in turn NP-hard to determine if the expected value


is above some given level. Further, the ability to approximate will depend on


the failure costs _β_ in the network, which could be arbitrarily large in the gen

eral case, suggesting that approximation is also difficult in general under fixed


thresholds.


This compares to what is typically done in financial models in practice.


Firms are typically treated in isolation, i.e., not part of a network model. In this


case, firm defaults are treated as independent or perhaps correlated through a


simple copula. Such distributions of credit risk, such as produced by a Gaus

sian copula, fail to capture clustering of defaults. The resulting probability that


a given fraction of firms default is exponentially unlikely as the number of firms


grows, and so this computational problem does not arise in those simple mod

els. Naturally, the assumption that firm defaults are independent is flawed, and


so the complexity problems that we describe in calculating expected values ap

ply in realistic settings.


**Importance sampling of tail events.** While it is NP-hard to identify the worst


case failure scenarios given a maximum sized aggregate shock _b_ in an eco

nomic network, it is possible to identify scenarios that approximate this up to a


(1 _−_ 1 _/e −_ _ϵ_ ) factor with random thresholds. As a result, we can apply influence


maximization approximation methods to identify instances of shocks that lead


to events in the tail of similar size to the parameter _b_ that is chosen (or indeed


for a variety of _b_ chosen). A common task in finance is to stress test a finan

cial system subject to aggregate shocks up to a particular size. Direct Monte


Carlo approaches will tend to underestimate risks because random samples are


302


unlikely to contain many of the extreme default scenarios, especially in a large


multi-dimensional space. Importance sampling using this new suite of approxi

mation algorithms thus unlocks a valuable new way to sample tail events where


it was otherwise difficult.

#### **6.4 Application to WIOD dataset**


To demonstrate the use of our results, we consider an application of influence


maximization algorithms to an economic network. We construct instances of


the economic network intervention problem based on the World Input Output


[Database (WIOD). The data is openly available at http://www.wiod.org](http://www.wiod.org/home)


[/home. We simulate a number of possible shocks to the resulting network and](http://www.wiod.org/home)


demonstrate that by adapting influence maximization algorithms, we can de

rive effective interventions using relatively modest budgets. As we might ex

pect, we see decreasing returns to scale in the size of the budget.


The simulations we perform are intended as a proof of concept of a realistic

looking setup based on real underlying data. We stress that many parts of the


setup for which data is not available remain stylized: in particular underlying


assets, thresholds, failure costs, and distribution of shocks to underlying asset


values. Additionally, there is naturally uncertainty about economic network


structure as described by the dataset and aggregation effects from grouping en

tire industries of firms into single nodes.


Our code for intervention approximation algorithms and simulation imple

[mentation is openly available at https://github.com/aklamun/optimal](https://github.com/aklamun/optimal_intervention)


[_intervention. A network visualization of the data is provided in Fig. 6.2.](https://github.com/aklamun/optimal_intervention)


303


Figure 6.2: Economic network structure inferred from World Input Output
Database (WIOD)


304


#### **6.4.1 Simulation setup**

The WIOD dataset (see, e.g., [181]) describes the flow of resources in dollar


value between different economic sectors within different nations (intermediate


demand) and national final demand (e.g., GDP components, such as consump

tion, investment, government expenditure). The dataset includes this informa

tion for 2464 distinct economic sectors spread between 28 EU countries and 15


- ther major countries for the years 2000-2014.


We construct an economic network from the 2014 dataset in the following


way:


1. We set the number of nodes to _n_, which represents the number of columns


in the dataset that refer to economic sectors or final demand components;


_n × n_
2. We set up an array of flows between nodes from dataset, with zero


rows for final demand components;


3. We transpose components of any negative entries in the array;


4. We scale columns to sum to 1 (inclusive of **value added**, a row in the


dataset that is not included in the array) or 0 if a zero column; Value added


is traced by all labor and capital that is directly and indirectly needed for


the production of final manufacturing goods, see [181];


5. We set diagonals in the array to zero to obtain _C_ ;


6. We fix unnecessarily bad conditioning in _C_ by removing nodes with near


zero **value added**
(columns referring to households);


7. We set the vector _D_ **p** to equal the output of each node at basic prices (this


is the TOT ~~G~~ O row in the dataset);


305


8. We set the vector _**θ**_ = _C_ [ˆ] ( _I−C_ ) _[−]_ [1] _D_ **p** _−_ **value added**, which gives the market


value assuming no defaults from which we subtract value added;


9. We let the diagonal matrix _β_ with diagonal entries 0 _._ 1 _·_ **value added** .


The vector _D_ **p** above represents initial asset values. We sample shocks to


these asset values by sampling a shock vector _r_ such that the shocked asset


prices are given by the component-wise multiplication _D_ **p** _·_ (1 + _r_ ). The shock


vector _r_ is sampled from a _m_ - dimensional normal distribution with the follow

ing specifications intended to sample a range of large deviations:


  - Common correlation factor _ρ_ = 0 _._ 6,


  - Marginal distributions have _σ_ = 0 _._ 15 and drift _a_ = _−_ 0 _._ 3,


  - Shocks bounded by 0 such that 1 + _ri_ = max(1 + _ri,_ 0).


Recall that _D_ **p** are underlying asset prices, and market values will have addi

tional inter-relation and correlation from the network process.

#### **6.4.2 Intervention algorithms**


Based on our main results in the previous section, under appropriate assump

tions and randomization of thresholds, the network intervention problem is


monotone submodular. In this case there are known greedy algorithms that


provide (1 _−_ 1 _/e_ _−_ _ϵ_ )-approximations. For the reader’s convenience, we provide


these explicitly in Appendix 6.6.3 (Algorithm 6 and Algorithm 9). The general


structure of these greedy algorithms is to start with an empty seed set _S_ 0 and,


iteratively, add the node _u_ to _S_ 0 that gives the maximum marginal gain. Since


306


the thresholds are random, determining the maximum marginal gain in each


step involves estimating the expected size of resulting cascades _σ_ ( _S_ 0 _∪{u}_ ) for


a number of nodes _u_ . This is typically done through Monte Carlo estimation


- f the expectation integral. For large networks, for which these integrals are


very high-dimensional, the Monte Carlo approximations become prohibitively


slow, although still within polynomial time with the Monte Carlo capped at a


constant factor. [3] This is the case for the size of networks in these simulations.


In practice, heuristic algorithms are used in influence maximization to try


to estimate the greedy algorithm in faster time with large success. For instance


DiscountFrac used in [66] starts with an empty seed set _S_ 0 and iteratively


adds the node _u_ to _S_ 0 that would exert the most total impact on the remain

ing defaulting nodes. In particular, given the initial intervention seed set _S_


at the beginning of a step, DiscountFrac picks the node _u_ that maximizes


_∥f_ ( _{u}_ ) 1 _A\{u} ∥_ 1 for remaining uninfluenced set _A_ . We provide an explicit de

scription of DiscountFrac in Appendix 6.6.3 (Algorithm 12).


In our simulations, we adapt DiscountFrac to choose the node _u_ that max

imizes
_∥f_ ( _{u}_ ) 1 _A\{u}_ _∥_ 1

_θ_ ˜ _u −_ _fu_ ( _S_ ) _,_


where _S_ is the currently influenced set. This accounts for the cost to influence


node _u_ in the current step, given that economic network thresholds can vary


significantly in size. For full implementation details of this adaptation, we refer


[to our public code repository at https://github.com/aklamun/optim](https://github.com/aklamun/optimal_intervention)


[al_intervention. The heuristic algorithm is conceptually very similar to](https://github.com/aklamun/optimal_intervention)


the ideal fractional greedy algorithm. Although it does not come with the same


3As an area of future research, it would be interesting to examine whether asymptotic results

- n the size of the cascade ´a la [7] could replace part of the Monte Carlo approximations.


307


theoretical approximation guarantees, it performs well in practice.

#### **6.4.3 Simulated interventions**


We simulate 5000 shocks and apply the adaptation of DiscountFrac to ap

proximate the resulting optimal intervention problems. In this setting, we ex

plore the effectiveness of a range of targeted intervention sizes.


Figure 6.3 depicts the percentage of firms defaulting under certain interven

tion scenarios. In particular, we compare the effects of a 1% targeted interven

tion to no intervention. Figure 6.3a shows histogram densities of firm defaults


under the sampled shocks, illustrating that the 1% intervention effectively re

duces the tails of this distribution.


Figure 6.3b shows histogram densities of defaults averted under the 1% in

tervention relative to no intervention, which also illustrates the effectiveness.


An interesting feature is the bimodal distribution of defaults averted from tar

geted intervention. One hypothesis to consider is that this is a result of the


network cluster structure itself: there are several clusters in the network, and


firms within the same cluster are more likely to default (or avert default from a


nearby intervention) together.


Figure 6.4 depicts the experimental Tail Value at Risk (TVaR) of default cas

cade size for different quantiles 0 _< q ≤_ 1. TVaR( _q_ ) is a conditional expectation,


conditioned on events falling in the _q_ - th quantile of outcomes:



_|A|_ ( _b_ )
TVaR( _q_ ; _b_ ) = E

       - _|U_ _|_



_|A|_ (0) _≥_ VaR� _|A|_ (0); _q_  - [�] _,_

- ��



where _|A|_ ( _b_ ) outputs the number of defaulting firms given budget _b_, _|U_ _|_ is the


308


(b)









(a)



Figure 6.3: Histogram densities of defaults under 1% asset value intervention
and no intervention.


**q** **% Reduction in** TVaR( **q** )
0 _._ 1 23%
0 _._ 2 29%
0 _._ 4 36%
0 _._ 6 40%
1 _._ 0 42%


Table 6.1: Percentage change in TVaR with quantile _q_ - f default cascade size
resulting from targeted intervention with budget 1% of total initial assets.


number of total firms, and VaR( _X_ ; _q_ ) is the _q_ - quantile of random variable _X_ .


Note that in our case _q_ is a quantile of a distribution that is already modeling


negative outcomes in these simulations. Also recall that _q_ = 1 gives the uncon

ditional expectation.


Figure 6.4 demonstrates that relatively small budgets effectively reduce sys

temic risks as measured by TVaR. Experimental numbers for the percentage re

duction in TVaR using an intervention budget of 1% of initial assets is presented


in Table 6.1.


309


70%


60%


50%


40%


30%



Expected Defaults vs. Intervention Budget


_TVaR(q=0.1)_


_TVaR(q=0.2)_


_TVaR(q=0.4)_



_TVaR(q=0.6)_

20%


_TVaR(q=1.0)_

10%


0.0% 0.2% 0.4% 0.6% 0.8% 1.0%


Budget % of Total Assets _|Dp|_


Figure 6.4: Simulation TVaRs with quantiles _q_ for a range of intervention budgets.

#### **6.4.4 Efficiency of intervention**


We end this section by exploring the efficiency of intervention. The question


- f computational efficiency is clear because the problem is in general NP hard:


- ptimizing naively would be quite daunting (and completely intractable given


the even modest size of the network). A naive approach would be to to consider


every subset of nodes on which to intervene. In absence of influence maximiza

tion approximation methods, one would need to resort to heuristics such as (1)


intervening on “systemically important” firms first, and (2) intervening on the


first layers of the default hierarchy. Neither of those heuristics have good guar

antees and the size of value alone cannot be a measure of systemic importance,


see e.g. [153] and the references therein.


Our influence maximization method can be applied for any weight function


_w_ ( _S_ ) that satisfies the Assumption 6.3. Our approach is computationally effi

cient and we have performance guarantees. The fact that we can consider mul

310


tiple weight functions for the same intervention algorithms allows us to exam

ine also a notion of economic efficiency. Using the cardinality weight function


amounts to minimizing the number of defaults subject to the given budget. We


now consider the weight function represented by the sum of the market value


- f the nodes


_w_ ( _S_ ) =           - _vi._

_i∈S_


In this case, the goal of intervention is to maximize value. In heterogeneous


economic networks, we can consider multiple objectives in order to assess the


efficiency of intervention. Since firms differ in terms of value, we expect that


the additional value saved decreases with the number of saved firms. The ap

proximations we provide using influence maximization methods are closer to


a policy that intervenes on ”systemically important” nodes first. With this ap

proach, the systemic importance of a node is determined by the algorithm itself


and combines the value of the firm and their position in the network.


In Figure 6.5 we plot the percentage value and the percentage of firms saved


by intervention as a function of the intervention budget. These plots both


demonstrate diminishing returns, although less so when the criterion is the


value saved. When the budget is sufficiently high, the number of firms that


are being saved stays relatively flat, whereas the value saved still exhibits sig

nificant increases. This means that the intervention set changes, and the reason


why additional value is being saved is the network effects.


Next, in Figure 6.6 we plot the histogram of defaults averted vs. value saved


across simulated shocks for a fixed budget representing 1% of the total initial


value. The histogram of the defaults averted is rather flat, whereas we note a


more u-shaped histogram for the histogram of the value saved. This is consis

311


**Efficiency of Intervention**







Figure 6.5: Efficiency of intervention










|Va|lueSavedfr|om1%|Inter|vent|ion|
|---|---|---|---|---|---|
|||||||
|0%<br>20%<br>40%<br>60%<br>80%<br>10|0%<br>20%<br>40%<br>60%<br>80%<br>10|0%<br>20%<br>40%<br>60%<br>80%<br>10|0%<br>20%<br>40%<br>60%<br>80%<br>10|0%<br>20%<br>40%<br>60%<br>80%<br>10|0%<br>20%<br>40%<br>60%<br>80%<br>10|


|De|faul|tsAver|tedf|rom1%|Inte|rvent|ion|
|---|---|---|---|---|---|---|---|
|||||||||
|0%<br>5%<br>10%<br>15%<br>20%<br>Defaults Averted (% Total Firms)|0%<br>5%<br>10%<br>15%<br>20%<br>Defaults Averted (% Total Firms)|0%<br>5%<br>10%<br>15%<br>20%<br>Defaults Averted (% Total Firms)|0%<br>5%<br>10%<br>15%<br>20%<br>Defaults Averted (% Total Firms)|0%<br>5%<br>10%<br>15%<br>20%<br>Defaults Averted (% Total Firms)|0%<br>5%<br>10%<br>15%<br>20%<br>Defaults Averted (% Total Firms)|0%<br>5%<br>10%<br>15%<br>20%<br>Defaults Averted (% Total Firms)|0%<br>5%<br>10%<br>15%<br>20%<br>Defaults Averted (% Total Firms)|



Figure 6.6: Defaults averted vs. value saved by intervention


tent with well known phase transition phenomena in networks: shocks either


die out quickly or reach a large fraction of the network, but there are few inter

mediate situations. In the cases where network contagion is high, intervention


proves highly effective and saves a large fraction of the network value.

#### **6.5 Conclusion**


We have shown that the optimal intervention problem is NP-hard under fixed


failure thresholds. Given a network, one essentially needs to choose a set of


312


firms among those who would otherwise default and reverse their defaults. The


choice of such firms saves the maximum value. Other related problems are also


shown to be computationally hard, even if we have perfect information about


the underlying setup. In particular, given a maximum aggregate shock, it is


computationally hard to determine if there is a distribution of this shock across


firms leading to a given fraction of the network to fail. In turn, when thresh

- lds are random, these problems allow (1 _−_ 1 _/e −_ _ϵ_ )-approximations. Failure


thresholds represent the points where shareholders of the firm decide to cease


the operations and liquidate the asset. In reality thresholds could be based on


the expectations of large cascades and large scale liquidations. Given the com

plexity issues in assessing which shocks lead to such extreme scenarios, it would


be interesting to explore further how strategic shareholders would make their


threshold choices.


Using the approximation algorithms, we evaluate the performance of inter

vention under a large number of shocks. We remark a significant reduction of


Tail Value at Risk of the default cascade size, even under a small intervention


budget relative to total assets. This can be explained by the fact that the solution


to the optimal intervention problem unveils a hierarchical or causal structure of


defaults, and in practice it selects a relatively small set to directly intervene on.


Most of the default cascade is then averted indirectly, by reversing failure costs


and network effects.


**Acknowledgements** The authors would like to thank Sid Banerjee for helpful


discussions in the initial stages of this project, and to Kristina Tian for research


assistance. This paper is based on work supported by NSF CAREER award


#1653354 and a Bloomberg Fellowship.


313


#### **6.6 Appendix: Proofs and Additional Details** **6.6.1 Overview of Influence Maximization**

Our analysis builds on influence propagation research in social networks. We


provide an overview of this to aid the reader. This work has historically studied


processes like diffusion of technological innovation, beliefs, product adoption,


and viral content. A natural question is how to engineer such a viral cascade


given information about the network.


A model for this problem is specified as follows:


 - _U_ is the set of nodes in the network.


 - _f_ ( _S_ ) a set function that outputs the vector of influence exerted by the acti

vation of node set _S ⊆_ _U_    - n each node in _U_ (i.e., _fu_ ( _S_ ) = influence exerted


   - n node _u_ ). We assume _f_ ( _∅_ ) = 0.


 - _w_ ( _S_ ) outputs an importance weighting of node set _S_ . In the simplest set

ting, each node is weighted by 1.


 - _**θ**_ **[˜]** is the vector of thresholds for each node. A node _u_ becomes _activated_ if


the influence exerted on it is _≥_ _θ_ [˜] _u_ .


 - _b_ is the budget for influencing nodes.


**Integral Influence Maximization,** studied in [101], focuses on maximizing the


weighted number of activated nodes by finding an optimal seed set _S_ 0 to acti

vate with payments of size _θ_ [˜] _u_ for each _u ∈_ _U_ subject to budget _b_ . An influence


cascade is calculated in stages. Given an initial set of activated nodes _S_ 0, we


314


construct the set of nodes _Si_ (for _i ≥_ 1) activated by the set _Si−_ 1 by adding the


nodes _u_ such that


_fu_ ( _Si−_ 1) _≥_ _θ_ [˜] _u._


The cascade process converges to a final set of activated nodes _S_ . The optimiza

tion problem is


max _w_ ( _S_ )
_S_ 0 _⊆U_



s.t.

  
_u∈S_ 0



_θ_ ˜ _u ≤_ _b._



**Fractional Influence Maximization,** studied in [66], is a generalization of the


**x**
integral case. In this problem, we choose a payment vector subject to budget


_b_ to exert influence on seed nodes. An influence cascade is again calculated in


stages. An initial set of activated nodes _S_ 0 is composed of nodes _u_ for which


**x** _u ≥_ _θ_ [˜] _u_ . We construct the subsequent sets of nodes _Si_ (for _i ≥_ 1) activated by


the set _Si−_ 1 by adding the nodes _u_ such that


_fu_ ( _Si−_ 1) + **x** _u ≥_ _θ_ [˜] _u._


Note that this assumes that direct influence is additive with influence from other


vertices in the network, in the sense that node activated in next stage if and


- nly if this condition satisfied. The cascade process converges to a final set of


activated nodes _S_ . The optimization problem is


max _w_ ( _S_ )
**x** _≥_ 0


s.t. **1** _[T]_ **x** _≤_ _b_


where **1** is the all-ones vector. The amounts can be a fraction of the thresholds


- f the nodes. This allows more efficient use of budget _b_ to influence an effective


seed set _S_ . In particular, this takes advantage of the fact that we don’t have to


315


spend as much to influence a node that already has partial influence exerted


from other influenced nodes.


For simple influence models, like the Linear Threshold Model and Trigger

ing Set Model, these problems are NP-hard, as shown in [101] and [66]. Further,


they are also hard to approximate within any general nontrivial factor.


However, when we consider a modified problem with randomized


thresholds–e.g., if activation thresholds for influence are uniform random


variables–then the problem changes enough in expectation to lower complex

ity. In particular, the expected cascade size _σ_ ( _S_ 0) := E[ _w_ ( _S_ ) _|S_ 0] from a given


seed set _S_ 0 (with similar definition for _σ_ ( **x** )) is monotone submodular and al

lows a greedy approximation that is provably within (1 _−_ 1 _/e_ ) _≈_ 63% of optimal


([101],[66]). [146] proved this for more general threshold models and distribu

tions for _θ_ [˜] . In particular, letting _Fu_ be the distribution function of _θ_ [˜] _u_, _σ_ ( _S_ 0) is


monotone submodular given that the following functions are monotone sub

modular: _f_, _w_, and _Fu ◦_ _fu_ for all _u ∈_ _U_ . We define these greedy algorithms


explicitly in Appendix 6.6.3.


In the typical influence maximization problem, a node in _S_ does not exert


influence on itself. This is complicated in the economic network intervention


problem because the reversal of a node’s default has an effect on itself through


cross-holdings. There are also differences in _θ_ and _w_ .

#### **6.6.2 Proofs**


316


**Theorem 6.1**


_Proof._ We will reduce from the independent set problem to an instance of the


economic network intervention problem. Our reduction strategy follows [90]


(for the linear influence model), but we note it requires additional steps to re

duce independent set to the economic network intervention setting, which is a


class of instances of more general influence maximization-like problems.


In the independent set problem, we are given an undirected graph _G_ =


( _U, E_ ) with nodes _U_ and edges _E_ . Given a number _k_, we ask if there is an


independent set in _G_ - f size _k_ .


**Reduction gadget.** For the reduction, construct a bipartite graph _G_ _[′]_ = ( _U_ 1 _∪_


_U_ 2 _, E_ _[′]_ ) as follows:


  - Add each node in _G_ to _U_ 1. Attach thresholds _|U_ 1 _|_ [to these nodes.]


  - For each edge _{i, j} ∈_ _E_, add a node _u_ to _U_ 2 and add directed edges


( _i, u_ ) _,_ ( _j, u_ ) to _E_ _[′]_ . Attach edge weights _|U_ 1 _|_ [and thresholds] _|U_ 1 _|_ [.]


  - For each possible pair _{i, j} /∈_ _E_, add two nodes _u, w_ to _U_ 2 and add di

rected edges ( _i, u_ ) _,_ ( _j, w_ ) to _E_ _[′]_ . Attach intervention weights _|U_ 1 _|_ [and thresh-]


   - lds 1
_|U_ _|_ [.]


Notice the number of vertices and edges in _G_ _[′]_ :


2
_|U_ _|_ _−_ _|U_ _|_
_|U_ 1 _∪_ _U_ 2 _|_ = _|U_ _|_ + _|E|_ + 2 _−|E|_ = _|U_ _|_ [2] _−|E|,_

2

           -           

_|E_ _[′]_ _|_ = _|U_ _|_ [2] _−|U_ _|._


317


_k|U_ _|_
Set the desired penetration rate in _G_ _[′]_ to _ζ_ = _|U_ _|_ [2] _−|E|_ [(this is the fraction of]


nodes we want to reverse the defaults of in the economic network). Notice that


_k|U_ _|_
_ζ|U_ 1 _∪_ _U_ 2 _|_ =
_|U_ _|_ [2] _−|E|_ _[|][U]_ _[|]_ [2] _[ −|][E][|]_ [ =] _[ k][|][U]_ _[|][,]_


which will be the desired penetration in the reduction graph to correspond to


the independent set (which we prove below).


**Gadget is instance of economic network intervention.** We now show that


the independent set problem on _G_ _[′]_ translates to an instance ( _C, β,_ _**θ**_ _, D,_ **p** ) of the


economic network intervention problem. Let _A_ be the adjacency matrix of _G_ _[′]_ .


Since _G_ _[′]_ is a 2-layer DAG, we have _A_ _[t]_ = 0 for integers _t >_ 1. Then the Neumann


series is


( _I −_ _A_ ) _[−]_ [1] = _I_ + _A._


Notice that _A_ is non-negative column-substochastic with zero diagonal.


Thus we take _C_ = _A_, and _C_ [ˆ] is well-defined.


**Claim:** ( _β,_ _**θ**_ _, D,_ **p** ) can be chosen such that, before intervention, all nodes fail


with end values **v** = 0, _θ_ [˜] _u_ = _|U_ 1 _|_ [for all] _[ u]_ [, and] _[ β][ ≥]_ [1][.]


**Proof of claim:** To find such a ( _β,_ _**θ**_ _, D,_ **p** ), we can setup the following system


**V** = ( _I_ + _C_ )( _D_ **p** _−_ _β_ 1 _U_ 1 _∪U_ 2) = 0



ˆ
_θu >_ _C_ ( _I_ + _C_ ) _D_ **p**

   -   


_u_ [for] _[ u][ ∈]_ _[U]_ [1]



ˆ
_θu >_ _C_ ( _I_ + _C_ )( _D_ **p** _−_ _β_ 1 _U_ 1)

   -   


_u_ [for] _[ u][ ∈]_ _[U]_ [2]



˜ ˆ
_θu_ = _C_ _[−]_ [1] _**θ**_ _−_ ( _I_ + _C_ ) _D_ **p** _−_ _Cβ_ 1 _U_ 1 _∪U_ 2 _\{u}_

   -   

_β ≥_ 1 _._


318




[1]
_u_ [=] _|U_ _|_ [for all] _[ u]_


The system has the same number of variables as dimensions. Because of the


2-layer DAG structure, it is simple to see that the system is solvable.


Notice that in the equation for _θ_ [˜] is valid. Taking failure set _T_, we have



˜ ˆ
_θu_ = _C_ _[−]_ [1] _**θ**_ _−_ ( _I_ + _C_ )( _D_ **p** _−_ _β_ 1 _T_ _\{u}_ )

   -   - _u_



ˆ
= _C_ _[−]_ [1] _**θ**_ _−_ ( _I_ + _C_ ) _D_ **p** _−_ _Cβ_ 1 _T_ _\{u}_

            -            - _u_


because [ _Iβ_ 1 _T_ _\{u}_ ] _u_ = 0.


**Claim:** The effect of reversing defaults _S_ propagates to other nodes through


_f_ ( _S_ ) = _Cβ_ 1 _S_ .


**Proof of claim:** First notice that for all nodes _u_,



( _I_ + _C_ ) _β_ 1 _u_

- 


_u_ [=] _[ β][u][.]_



This is a simple result because _C_ has zero diagonal and the only nonzero entry


- f 1 _u_ is the _u_ th entry; thus there is 0 contribution from _Cβ_ 1 _u_ for the _u_ th entry.


Then we have


_f_ ( _S_ ) = ( _I_ + _C_ ) _β_ 1 _S −_          - _Iu_ ( _I_ + _C_ ) _β_ 1 _u_

_u∈S_


= ( _I_ + _C_ ) _β_ 1 _S −_             - _Iuβ_ 1 _u_

_u∈S_


= ( _I_ + _C_ ) _β_ 1 _S −β_ 1 _S_


= _Cβ_ 1 _S ._


**Claim:** If we reverse the default of a node in _U_ 1, then its neighbors in _U_ 2 are also


saved from default.


319


**Proof of claim:** Suppose we reverse the default of _u ∈_ _U_ 1. Suppose _w ∈_ _U_ 2 is a


neighbor of _u_ . Then _w_ ’s value is affected by




[ _f_ ( _u_ )] _w_ = [ _Cβ_ 1 _u_ ] _w_ = _[β]_



_|U_ _|_ [= ˜] _[θ][w]_




_[β]_ [1]

_|U_ _|_ _[>]_ _|U_



since _β ≥_ 1. Thus _w_ ’s default is also reversed.


To complete the translation into the economic network intervention prob

lem, define the following:

_b_ = _[k]_

_|U_ _|_


_α_ = 1


_ℓ_ = 1 _−_ _ζ._


In intuitive terms, the corresponding economic network is a 2-layer DAG, in


which the only cross-holdings are the shares in the first layer held by the second


layer. In this case, the interactions are quite simple, described solely by _C_ . In


this network, every node starts in default. We can pay _θ_ [˜] = _|U_ 1 _|_ [to reverse a node’s]


default. Our budget is _b_ and we can choose at most _k_ nodes to intervene on.


**Reduction to integral case.** We first consider the integral case and then extend


to the fractional case. We want to select a subset _S_ - f _k_ nodes from _G_ _[′]_ such that,


if we provide payments equal to their _θ_ [˜], a cascade of reverse-defaults occurs of


size at least _ζ|U_ 1 _∪_ _U_ 2 _|_ (i.e., at most _ℓ|U_ 1 _∪_ _U_ 2 _|_ nodes fail after intervention). This


- ccurs if and only if _G_ has an independent set of size _k_, as we prove next.


First, note that sets _S ⊆_ _U_ 1 always dominate sets _S ⊆_ _U_ 1 _∪_ _U_ 2 with _S_ ⊊


_U_ 1. This is because, by construction, reversing the default of any node in _U_ 1 in


turn impacts its neighbors in _U_ 2, reversing their defaults, whereas reversing the


320


default of a node in _U_ 2 does not impact its neighbors in _U_ 1. Since each node in _U_ 2


has a neighbor in _U_ 1, it always makes sense to impact such a neighbor instead of


the considered node in _U_ 2. Thus it is sufficient to consider only solutions in _U_ 1.


Notice that this extends to the fractional case since threshold-crossing payments


are of the same size for nodes in _U_ 1 and _U_ 2.


Each node in _U_ 1 has _|U_ _| −_ 1 neighbors, and two nodes in _V_ 1 share a neighbor


if and only if they are neighbors in _G_ . So if we pick the subset _S ⊆_ _U_ 1, the size


- f the default reverse cascade is


#default reverses = _|U_ _||S| −|{{i, j} ∈_ _E|i, j ∈_ _S}|._


E.g., if no nodes in _S_ are connected in _G_, then the second term is 0 and each


default reverting node impacts itself and _|U_ _| −_ 1 unique nodes in _U_ 2 for a total


- f _|S|_ + ( _|U_ _| −_ 1) _|S|_ = _|U_ _||S|_ nodes.


The number of default reversals is _≥_ _ℓ|U_ 1 _∪U_ 2 _|_ = _k|U_ _|_ if and only if _∀u, v ∈_ _S_,


_{u, v} /∈_ _E_, which is that case if and only if there is an independent set of size _k_


in _G_ .


**Reduction to fractional case.** Notice that this easily extends to the fractional


case. In this case, we want to find payments such that [�] _i_ _[γ][i][ ≤]_ _[b]_ [ =] _|Uk_ _|_ [and]


we save _ζ|U_ 1 _∪_ _U_ 2 _|_ nodes from failure (i.e., at most _ℓ|U_ 1 _∪_ _U_ 2 _|_ nodes fail after


intervention). In _G_ _[′]_, all edges and thresholds have value _|U_ 1 _|_ [. Given the structure]

- f _G_ _[′]_, optimal node payments will obey _γi ∈{_ 0 _,_ _|U_ 1 _|_ _[}]_ [. This is because a payment]


to a node in _U_ 1 is again always better than a payment to a node in _U_ 2 (same


argument as before), and any payment smaller than _|U_ 1 _|_ [will result in no default]


reversals in _U_ 1, and hence no subsequent effect on _U_ 2. Thus there is one-to

- ne correspondence between optimal integral solutions and optimal fractional


321


solutions. Thus the fractional case is NP-hard in general.


**Proposition 6.1**


_Proof._ To simplify notation, define _A_ := ( _I −_ _C_ ) _[−]_ [1] _β_ .


(Monotonicity) Let _T ⊂_ _U_ and _u ∈_ _U \ T_ . Then we have


_f_ ( _T ∪{u}_ ) = _A_ 1 _T_ _∪{u} −_        - _IjA_ 1 _j_

_j∈T_ _∪{u}_


= _A_ 1 _T −_         - _IjA_ 1 _j_ + _A_ 1 _u −IuA_ 1 _u_

_j∈T_


= _f_ ( _T_ ) + _A_ 1 _u −IuA_ 1 _u ._


Since _A_ is non-negative, the second term is _≥_ 0. The third term only affects the


_u_
th component, and then only cancels the contribution of the second term. Thus


we have _f_ ( _T ∪{u}_ ) _≥_ _f_ ( _T_ ).


(Submodularity) Let _S ⊆_ _T ⊆_ _U_ and _u ∈_ _U \ T_ . From the above equations,


we have _f_ ( _T ∪{u}_ ) _−_ _f_ ( _T_ ) = _A_ 1 _u −IuA_ 1 _u_ . and similarly with _S_ . Thus the


submodularity condition _f_ ( _S ∪{u}_ ) _−_ _f_ ( _S_ ) _≥_ _f_ ( _T ∪{u}_ ) _−_ _f_ ( _T_ ) holds with


equivalence.


**Theorem 6.2**


_Proof._ Recall that the intervention problem can be expressed in an influence


maximization-like form. By assumption, _w_ is normalized, monotone, and sub

322


modular, and _f_ is normalized. And by Prop. 6.1, _f_ is monotone and submod

ular. Notice that the intervention problem is easily normalized (in a different


sense) so as to restrict each _fi_ and _θ_ [˜] _i_ to the range [0 _,_ 1]. Then by Theorem 1 in


[146], the integral intervention problem has _σ_ ( _S_ 0) normalized, monotone, and


submodular. And by Theorems 2-3 in [66], the fractional intervention problem


has _σ_ ( _**γ**_ ) normalized, monotone, and submodular (note that these definitions


are modified to describe non-set functions in the fractional case).


**Corollary 6.2**


_Proof._ This follows using the same application of results as in [101]. In particu

lar, the results of [61],[151] show that a greedy hill-climbing algorithm approx

imates the optimum of monotone submodular problems to within a factor of


(1 _−_ 1 _/e_ ). Given that _σ_ has to be approximated, the result can be extended to


show that for any _ϵ >_ 0, there is _δ >_ 0 such that by using (1+ _δ_ )-approximate val

ues for the _σ_ function, we obtain a (1 _−_ 1 _/e−ϵ_ )-approximation. For the fractional


case, this uses Theorem 4 in [66].


**Theorem 6.3**


_Proof._ First consider a specific subclass of economic network instances. We will


reduce independent set to an instance of this subclass. The subclass has the


following properties:


323


  - Asset prices **p** take values in _{_ 0 _,_ 1 _}_ .


 - _D_ is row-sub-stochastic, such that a firm’s underlying assets can be valued


at most 1.


 - _C_ = 0, in which case _C_ [ˆ] = _I_ and ( _I −_ _C_ ) _[−]_ [1] = _I_ .


 - _β_ = 0, in which case a firm’s value is in [0 _,_ 1].


 - _b_ is an integer.


As a result, the shock to be chosen in our problem, if applied to asset _i_, can


change it’s price from 1 to 0. The problem at hand is now to find a set of _b_ assets


that, if set to 0, cause _ℓ|U_ _|_ firms to default.


Next consider a reformulation of the network process into a bipartite graph


_G_ _[′]_ as follows:


  - Add nodes for each underlying asset. Denote these nodes _U_ 1.


  - Add nodes for each firm. Denote these nodes _U_ 2.


  - For each _u ∈_ _U_ 1, add a weighted directed edge from _u_ to nodes in _U_ 2


according to the matrix _D_ . The weights here represent the effect of the


asset on the book values of firms that own those assets in the simple setting


with _C_ = 0.


Assume the assets in _U_ 1 are initially set to 1. If an asset is changed to 0, (negative)


impact is exerted on its connections in _U_ 2 via _D_, lowering those firms’ values. If


enough (negative) impact is exerted on a firm in _U_ 2, its value decreases below


threshold, triggering default. The equivalent problem is to find a set of _b_ nodes


in _U_ 1 such that, if set to 0, cause _ℓ|U_ _|_ firms to default.


324


To reduce from independent set, we can follow essentially the same reduc

tion as in Theorem 6.1 to a process on a bipartite graph like above. With appro

priate definition of parameters, this is an instance of the subclass of economic


networks above. And thus independent set reduces to economic network max

imum shock problem.

#### **6.6.3 Algorithms**


We provide explicit descriptions of the optimal intervention approximation al

gorithms to aid the reader, as their adaptations in the influence maximization


literature are usually not made explicit. The algorithms below use the follow

ing problem setting consistent with the intervention problem developed in the


paper:


 - _f_ ( _S_ ) outputs the intervention impact vector exerted by set _S_  - n each node.


 - _w_ ( _S_ ) outputs a weight of node set _S_ .


  - Θ is node threshold distribution, uniformly distributed between _θ_ **[˜]** min and


_θ_ **˜** max. The thresholds **˜** _θ_ are sampled from this distribution.


 - _b_ = budget.


There are three primary intervention algorithms. The remaining algorithms


serve as helper functions used in these primary algorithms.


  - Algorithm 6 is the greedy algorithm for approximating optimal integral


interventions with 63% guarantees.


325


  - Algorithm 9 is the greedy algorithm for approximating optimal fractional


interventions with 63% guarantees.


ˆ _σ_
Notice that these algorithms need to re-estimate a high-dimensional integral


at each step through Monte Carlo, which is often too computationally intense to


run in high-dimensional systems, even though it is technically polynomial time


with the Monte Carlo capped at a constant factor.


  - Algorithm 12 is a fast heuristic greedy algorithm that is very close to the


ideal fractional greedy algorithm. It does not come with provable guaran

tees, but is used similarly in influence maximization with large success.


[Full and optimized Python implementation is available at https://github](https://github.com/aklamun/optimal_intervention)


[.com/aklamun/optimal_intervention.](https://github.com/aklamun/optimal_intervention)


**Algorithm 4** CalcIntCascade( _S_ ; _f,_ _θ_ **[˜]** )

**Require:** set _S_, set function _f_, thresholds _θ_ **[˜]**

Initialize _S_ 0 _←∅_, _S_ 1 _←_ _S_, _i ←_ 1
**while** _Si ̸_ = _Si−_ 1 **do**

_Si_ +1 = _{_ node _v|f_ ( _Si_ )[ _v_ ] _≥_ _θ_ **[˜]** [ _v_ ] _} ∪_ _Si_
_i ←_ _i_ + 1

**end while**

**return** _Si_


**Algorithm 5** ˆ _σ_ ( _S_ ) estimate of _σ_ ( _S_ ) for integral intervention
**Require:** set _S_, set function _f_, weight function _w_, thresholds distr. Θ, sample
size _k_ = 1 _e_ 4


Initialize _σ ←_ 0

**for** _i ≤_ _k_ **do**

Sample _θ_ **[˜]** _∼_ Θ

_T,_ = CalcIntCascade _S_ ; _f,_ _θ_ **[˜]**

           -            
_σ ←_ _σ_ + _w_ ( _T_ )
**end for**
**return** _σ/k_


326


**Algorithm 6** GreedyInt = Greedy algorithm for optimal integral intervention
**Require:** set function _f_, weight function _w_, thresholds distr. Θ, budget _b_

Initialize _S_ 0 _←∅_, _i ←_ 0
**while** _|Si| < b_ **do**

**for** node _v /∈_ _Si_ **do**

**q** [ _v_ ] = ˆ _σ_ _Si ∪{v}_ ; _f,_ Θ _, w_

       -       
**end for**
_Si_ +1 _←_ _Si ∪{_ arg max **q** _}_, _i ←_ _i_ + 1
**end while**
**if** _|Si| ≤_ _b_ **then**

**return** _Si_
**else**


**return** _Si−_ 1
**end if**


**Algorithm 7** CalcFracCascade( _**γ**_ ; _f,_ _θ_ **[˜]** )

**Require:** vector _**γ**_, set function _f_, thresholds _θ_ **[˜]**

Initialize _S_ 0 _←∅_, _i ←_ 1
_S_ 1 _←{_ node _v|_ _**γ**_ _v ≥_ _θ_ **[˜]** _v}_
**while** _Si ̸_ = _Si−_ 1 **do**

_Si_ +1 = _{_ node _v|f_ ( _Si_ )[ _v_ ] + _**γ**_ _v ≥_ _θ_ **[˜]** _v}_
_i ←_ _i_ + 1

**end while**

**return** _Si_


**Algorithm 8** ˆ _σ_ ( _**γ**_ ) estimate of _σ_ ( _**γ**_ ) for fractional intervention
**Require:** vector _**γ**_, set function _f_, weight function _w_, thresholds distr. Θ, sample
size _k_ = 1 _e_ 4


Initialize _σ ←_ 0

**for** _i ≤_ _k_ **do**

Sample _θ_ **[˜]** _∼_ Θ

_T_ = CalcFracCascade _**γ**_ ; _f,_ _θ_ **[˜]**

            -            
_σ ←_ _σ_ + _w_ ( _T_ )
**end for**
**return** _σ/k_


327


**Algorithm 9** GreedyFrac = Greedy algorithm for optimal fractional intervention
**Require:** set function _f_, weight function _w_, thresholds distr. Θ, budget _b_

Initialize _**γ**_ **0** _←_ **0**, _i ←_ 0
**while 1** _[T]_ _**γ**_ **i** _< b_ **do**

_Si_ = _{_ node _v|_ _**γ**_ **i** [ _v_ ] _>_ 0 _}_
**for** node _v /∈_ _Si_ **do**

_**γ**_ **v** = _**γ**_ **i** + _θ_ max[ _v_ ] _−_ Γ [+] ( _v, Si_ ) **1** _v_

       -        
**q** [ _v_ ] = ˆ _σ_ _**γ**_ **v** ; _f,_ Θ _, w_

       -       
**end for**

_u_ = arg max **q**

**˜**
_**γ**_ **i** + **1** _←_ _**γ**_ **i** + _θ_ max[ _u_ ] _−_ Γ [+] ( _u, Si_ ) **1** _u_, _i ←_ _i_ + 1

       -       **end while**
**if 1** _[T]_ _**γ**_ **i** _≤_ _b_ **then**

**return** _**γ**_ **i**
**else**


**return** _**γ**_ **i** _−_ **1**
**end if**


**Algorithm 10** Γ [+] ( _v, A_ ) = total sum of weight of edges from set _A_ to node _v_
**Require:** set _A_, set function _f_, node _v_

**return** _f_ ( _A_ )[ _v_ ]


**Algorithm 11** Γ _[−]_ ( _v, A_ ) = total sum of weight of edges from node _v_ to set _A_
**Require:** set _A_, set function _f_, node _v_

**return 1** _[T]_ _A_ _[f]_ [(] _[{][v][}]_ [)]


328


**Algorithm 12** DiscountFrac heuristic intervention algorithm
**Require:** set function _f_, weight function _w_, thresholds distr. Θ, budget _b_

Initialize **x0** _←_ **0**, _i ←_ 0
**while 1** _[T]_ _**γ**_ **i** _< b_ **do**

_Si_ = _{_ node _v|_ _**γ**_ **i** [ _v_ ] _>_ 0 _}_
**for** node _v /∈_ _Si_ **do**

**q** [ _v_ ] = Γ _[−]_ ( _v, V \Si_ )
**end for**

_u_ = arg max **q**

**˜**
_**γ**_ **i** + **1** _←_ _**γ**_ **i** + _θ_ max[ _u_ ] _−_ Γ [+] ( _u, Si_ ) **1** _u_, _i ←_ _i_ + 1

       -       **end while**
**if 1** _[T]_ _**γ**_ **i** _≤_ _b_ **then**

**return** _**γ**_ **i**
**else**


**return** _**γ**_ **i** _−_ **1**
**end if**


329


CHAPTER 7


**CASCADING RISKS AND SENSITIVITY IN ECONOMIC NETWORKS**


The content of this chapter has been invited for revisions for _**Operations Re-**_


_**search**_ .


“Cascading Risks and Sensitivity in Economic Networks.” Ariah


Klages-Mundt, Austin Benson, and Andreea Minca.


330


Agents in economic networks face intrinsic uncertainty about global net

work structure. As real networks are large and complex, even small network


uncertainties can lead to huge uncertainties about the market values and risks


(i.e., high parameter sensitivity) of firms and organizations in the face of net

work cascades. This raises the theoretical and practical question of how orga

nizations, regulators, or investors in the network can use such network models


to evaluate organization-level risks given imperfect information. We derive a


solution to this problem and a new unifying perspective. We apply perturba

tion theory based on conditioning to quantify the sensitivity of node values to


uncertainty in network parameters in the presence of nonlinear cascade effects.


We prove bounds that improve on existing results with the unifying (and sim

plifying) perspective of system conditioning. We further show analytically how


structures involving network cycles cause high sensitivity.

#### **7.1 Introduction**


The global medical and economic contagion due to the Covid-19 crisis caused


unprecedented change and uncertainty in the global economic network. The


crisis effectively saw China shut down in January, Europe shut down in Febru

ary, and the US shut down in March. In the summer, contagion hit the southern


hemisphere and then recirculated back to the northern hemisphere with further


waves of shut downs. Typically, financial shocks originate within subsectors


- f the network. For instance, in the 2008 financial crisis, losses on derivatives


threatened the default of the largest insurer, which would have lit a cascade of


losses across the network. The Covid-19 shock, however, caused external dis

ruptions to most economic sectors worldwide. Large uncertainties were intro

331


duced across the entire global economy as supply chains were disrupted, large


swathes of economies were in essence shut down, and an unprecedented scale


- f government interventions attempted to support shocked economies.


Research on contagion in networks of interacting economic firms has flour

ished over the last couple of decades, motivated by the cascading effects of re

cent financial crises. While conceptually useful in understanding contagion,


these network models have proven difficult to apply quantitatively in real set

tings, particularly when there is uncertainty about precise network shape. Two


connected issues lie at the heart of the problem: (1) these models are hugely sen

sitive to change in parameter values, and (2) real instances of these models are


typically very high-dimensional systems, and many algorithms and simulations


quickly encounter computational limits.


To illustrate how this is problematic on the ground, consider an individual


firm in the network that has some information about the global structure of the


network, but not perfect information. How should this firm evaluate its risk ex

posure in the network, for instance in making decisions about contracts, capital


allocations, and treasury management? Point estimates from these models are


not helpful alone since the firm is uncertain about the precise structure of the


network. Slightly different network structures, within the range of uncertainty,


may yield very different point estimates (the parameter sensitivity issues). In

stead, for these network models to be useful for the firm in evaluating risk expo

sure, they must rely on a range or distribution of outcomes given the uncertainty


(i.e., a good understanding of “model error”). Currently, network models lack


generally efficient ways to calculate or estimate ranges that incorporate such un

certainty, aside from large Monte Carlo simulations over the parameter space,


332


which can become quickly intractable (the computational issues). As a result,


existing models are not generally tractable in real world contexts, even when


there is good documentation of what the networks look like. We develop the


difficulty of these problems in further detail and wider application, including


not just firms but also regulators, in Section 7.3 in our particular context.


The scale of uncertainty in the Covid-19 crisis highlighted these issues, par

ticularly in the related area of epidemiological models (and indeed these prob

lems likely affect most large-scale models in social sciences). Modeling of the


medical contagion was notoriously imprecise and inaccurate compared to the


real contagion trajectory. Sensitivity of these models to deviations in parameter


values was initially poorly understood, leading to underestimation of uncer

tainty ranges in these network models. Further, huge computational resources


were devoted to running many scenarios to try to better estimate the range of


- utcomes.


In principle, these are the same sensitivity and computational issues affect

ing economic network contagion models. For instance, the European Central


Bank runs a stress test using an interbank contagion model in Ch. 12 of their


A
STAMPC analysis [65]. In this report, they recognize that estimating interbank


numbers correctly is a difficult task. They perform an entropy maximization


to estimate parameters and then lengthy Monte Carlo simulations on random

ized network structures. In the end, the precise Monte Carlo setup is difficult to


decide on and can have large effects on stress test outcomes.


We consider the Elliott-Golub-Jackson network model of [76], which models


the notion of value of an organization –firm, sector, country– introduced in the


context of cross-holdings. In this model, if the value of an organization drops


333


below a failure threshold, there are failure losses and the values of connected or

ganizations drop as well and so on. This shares the spirit of the distress notion


in [184], which allows for contagion before the point of failure. Conceptually, we


distinguish between “threshold effects” that arise from crossing failure thresh

- lds and other distress that translates through cross-holdings before reaching


points of failure.


Many related models have been developed, including debt networks [75,


165, 2], networks with reinsurance contracts [111], networks with credit de

fault swaps [170, 171, 172], and intersectoral networks [1], among others. These


works develop network models and analyze them in fixed contexts. For in

stance, in [76], when the effects of changes to network parameters are consid

ered, it is constrained to changes that do not affect initial organization values


(what they call “fair trades”). Our focus is different in this paper on instead


understanding how any general perturbation of parameter values affects orga

nization values in the network. While we work in the context of [76], we will


discuss later how the general results that we develop in this paper can be trans

lated to many of these other model contexts as well.


In several contexts, network models have been shown to be computation

ally complex. In the context of the Elliott-Golub-Jackson model, [93] show that


it is NP-hard to estimate the number of failures that could be caused by a small


shock to the system. And [113] show that is NP-hard to determine or approx

imate an optimal intervention, as well as NP-hard to determine the expected


values of organizations in the network. Interestingly, in a similar manner to


influence targeting results in social networks, [113] also show that by random

izing failure thresholds, optimal intervention can then be approximated in poly

334


nomial time. In the context of networks with credit default swaps, [171] showed


that it is NP-complete to decide if a clearing payment vector exists, as well as


determining which organizations default even in settings in which a solution is


generally guaranteed. These works deal with the setting of perfect network in

formation and computational complexity that arises from combinatorial struc

ture. Where uncertainty is considered, it is actually to simplify the problem.


In contrast, in this paper, we focus on problems that arise entirely from uncer

tainty in network structure and address computational problems arising from


the need for high-dimensional Monte Carlo simulations.


Parameter sensitivity of network models, and how it extends to risk and


model error, has been studied, but with limited progress so far. An overarch

ing limitation of the current literature is that it focuses on sensitivity in contexts


with no threshold effects (i.e., no failure thresholds are crossed). This makes


sense from a practical perspective since sensitivities can then be expressed as


directional derivatives of functions without discontinuities from threshold ef

fects. However, sensitivities arising from threshold effects are arguably a much


larger component of total uncertainty, so these miss a significant piece of the


puzzle. [93] explore this in the context of the Elliott-Golub-Jackson model and


demonstrate that, in the presence of cycles in cross-holdings, the model can be


very sensitive to uncertainty in cross-holdings; this compares to less sensitiv

ity when the graph is acyclic. In the Eisenberg-Noe model ([75]), sensitivity of


clearing payments is characterized with respect to changes in initial wealth is


studied in [125] and with respect to network shape in [80]. [52] study sensitivity


- f a similar network model with respect to external value shocks. [28] study sen

sitivity in a related network model; they show that longer and more numerous


chains and cycles lead to stronger amplification by connecting a leading term of


335


the derivative with the presence of chains or cycles in star, chains, and circle net

works. In this simple context without threshold effects, the models are closely


ressemble systems. Even in this simple context, however, the current results in


above literature are scattered across different models and methods without a


unifying framework.


**This Paper**


In this paper, we present a unifying methodology on analyzing sensitivity us

ing perturbation theory and analysis based on condition numbers, which allows


us to unite previous results and go further. While we develop it in the context


- f the Elliott-Golub-Jackson model, we discuss how the general methodology is


equally applicable to most of the other network models discussed. This method

- logy is able to unify previous results and, where applicable, extend them to


general input graphs, and improve on previous bounds in the setting with no


threshold effects. We then show how this methodology can be extended to ad

ditionally quantify sensitivity in settings with threshold effects, in which the


systems are more nonlinear and sensitivity is worse.


We begin our analysis by delving intuitively and with examples into the con

nections between network structure, sensitivity and risk management in Sec

tion 7.3, including how our later results help to address the resulting problems.


Our examples demonstrate that even if an organization has unreasonably pre

cise information about the global structure of the system, it can still be wildly


uncertain about the losses it will face in a given shock, which motivates the


remainder of our work. We then derive a series of perturbation theory results


that will be of interest for cascade models generally in Section 7.4. We then show


336


how these results can be used to bound sensitivities in the Elliott-Golub-Jackson


model in the absence of threshold effects in Section 7.5, improving on past re

sults in terms of tightness and generalization. In these results, we show how


cyclic networks give rise to inherently higher sensitivity than acyclic networks.


In many systems, we show that strongly weighted cycles are the specific


cause of sensitivity problems. In general, however, sensitivity cannot be not de

termined by the weight of the cycles alone and cycles can still have strong effects


even though individual edges and subcycles may not be strongly weighted; Per

turbation theory allows us to characterize the strength of the cycles in general


in terms of impact on condition numbers. Our framework can be thought of


as a risk methodology, whereby for an ’acceptable’ level of sensitivity in the


network, one can monitor if cycles are becoming too strong.


Our analytical contributions include the following:


  - We derive results and examples that relate nonlinear contagion effects


to structural properties of the network, involving cycles, and how these


cause extreme sensitivity (Section 7.3 and Prop. 7.2).


  - We show that sensitivity in acyclic networks is bounded above in the size


   - f the network (Corollary 7.1 and Theorem 7.1).


  - In contrast, we show that sensitivity in cyclic networks is bounded below


based on the strength of cycles in the network (Prop. 7.2) with a near

tight general upper bound that also increases significantly in the weight


   - f cycles, as measured through the column sums of _C_ being close to 1


(Prop. 7.4 and Theorem 7.2).


  - Further, we show that if a cyclic network is sufficiently close to acyclic,


337


meaning its cycles are sufficiently weak, then sensitivity is bounded simi

larly tight as in acyclic networks (Theorem 7.3).


In deriving our results, we primarily focus on uncertainty in the state of


the network in terms of the cross-holdings matrix ( _C_ ). Even if we know _C_,


underlying asset prices ( **p** ) still evolve, and it can be hard to evaluate if small


changes in _p_ can cause big cascades that affect an organization. This is a reason


why determining expected organization values in the network was shown to


be computationally hard in [113]. While we’ve developed the explicit results


in terms of uncertainty in _C_, similar results and algorithms can be derived by


simple extension for any combination of uncertainties in _C_, _D_, or **p** in the model.


We apply our methods to simulations on the World Input-Output Database


to show their utility toward evaluating organization-level risks in the network


(Section 7.6).

#### **7.2 Model**


In this section, we introduce the Elliot-Golub-Jackson network contagion model


[76]. Our results will be derived with this model in mind. However, many of the


methods we will use can be applied more generally to derive similar results in a


diverse array of network models, including [75, 2, 165, 119, 111], as well as mod

els which use Cobb-Douglass production functions in a Leontief-like model, as


in [1], since these can be reduced to linear systems with log transforms. In par

ticular, the results in the following two sections only require that the model can


be formulated as the solution of a dependent sequence of linear systems and


row scaling operations.


338


We define an economic network ( _C, D,_ _**β**_ _,_ _**θ**_ _,_ **p** ) in the model as follows:


 - _n_
    - rganizations (also referred to as nodes) in the network


 - _m_
assets owned by organizations


 - **p** = _m ×_ 1 vector of asset prices


 - _D_ = _n × m_ matrix with _Dik ≥_ 0 the share of asset _k_ held by organization _i_


(adding to 1)


 - _C_ = _n × n_ matrix with _Cij ≥_ 0 the fraction of organization _j_  - wned by


   - rganization _i_ and 0 along the diagonals


 - _C_ [ˆ] = _n × n_ diagonal matrix with _C_ [ˆ] _ii_ = 1 _−_ [�] _j_ _[C][ji]_ [ the share of organization]


_i_ not owned by another organization in the system


 - _**θ**_ = _n ×_ 1
vector of failure thresholds for each organization


 - _**β**_ = _n ×_ 1 vector of extra failure costs for each organization.


The matrix _C_ describes cross-holding relationships between organizations. If


an organization _i_ ’s market value (defined below) falls below its threshold _**θ**_ _i_,


it incurs an extra failure cost _**β**_ _i_ . The matrix _C_ is required to be column sub

stochastic as otherwise _C_ [ˆ] _[−]_ [1] is not well-defined. This in turn means that means


that _I −_ _C_ is invertible since the spectral radius _ρ_ ( _C_ ) _<_ 1.


The network propagates asset values and defaults across organizations in


the network, as visualized conceptually in Figure 7.1. Matrix _D_ describes the


- wnership mapping of underlying assets (blue nodes) to organizations (orange


nodes). Matrix _C_ describes cross-holdings between organizations. The breach


- f a threshold triggers failure costs (threshold effects), which propagate to other


- rganizations through _C_ .


339


Nodes own assets,
parts of other nodes



If node value < threshold,

nonlinear default cost incurred


Default costs propagate








|assets,|Col2|
|---|---|
|Assets<br>Firm 1<br> <br>  r nodes||
|Assets|Assets|



Figure 7.1: Financial network propagation mechanism.


Organization _book values_ are given by


**V** = _C_ **V** + _D_ **p** _−_ 1 _{_ **v** _<_ _**θ**_ _}_ _**β**_ _,_


where 1 _S_ is the diagonal binary matrix with diagonal entries indicating the en

tries of set _S_ . Notice that book values inflate the value of underlying assets


because asset values are counted multiple times across organizations (conse

quently, _∥_ **V** _∥_ 1 _≥∥_ **p** _∥_ 1 and can be arbitrarily large). A more useful measure of


the value of organizations is provided by _market values_ . These are calculated as


the scaling of book values by _C_ [ˆ], which accounts for the ownership share that


each organization retains in itself. Formally, market values are


**v** = _C_ [ˆ] **V** = _C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] ( _D_ **p** _−_ 1 _{_ **v** _<_ _**θ**_ _}_ _**β**_ ) _._


**Lattice of solutions.** A solution always exists for **v** . By applying Tarski’s fixed


point theorem, the set of solutions forms a complete lattice with supremum and


infimum, which represent best and worst case failure cascades. The supremum


340


solution is the canonical solution, as the other solutions arise solely from self

fulfilling failures beyond this case.


**Calculating cascades.** Given a financial network ( _C, D,_ **p** _,_ _**θ**_ _,_ _**β**_ ), the supremum


solution can be computed by solving a dependent sequence of linear equations


and row scaling operations. We provide the details of this in Appendix 7.8.


**Relating the model to the real world.** The variables of the model have sim

ple real world interpretations. For instance, underlying assets **p** can represent


cash reserves and other assets held by organizations. Failure costs _**β**_ can repre

sent how a organization’s assets would be depleted in, for instance, liquidation


and bankruptcy costs. And cross-holdings _C_ can represent approximate pair

wise relationships between organizations, modeled as equity relationships in


the Elliott-Golub-Jackson model, though can also easily be treated as debt rela

tionships as in [75] and related models.

#### **7.3 Connecting Network Structures to Risk and Sensitivity**


In this section, we make intuitive connections between certain network struc

tures that lead to extreme sensitivity in contagion and how this relates to vari

- us realistic problems in risk management. We derive results and examples that


demonstrate that, even if an organization has unreasonably precise information


about the global structure of the system, it can still be wildly uncertain about the


losses it will face in a given shock. We then discuss how these apply in realistic


networks and how our results in later sections address these problems.


341


#### **7.3.1 Illustrating Problems from Sensitivity**

We begin by considering an individual organization in the network. For sim

plicity consider that the organization is a firm, although depending on the


model context, it could be another form of organization, like a sector. Real

istically, agents in the network face imperfect and asymmetric information in


their knowledge about the system. Managers of the firm itself, or even small


groups of firms together, can observe the direct relationships that they take part


in, but are intrinsically uncertain about the global network structure, including


contracts among other firms. Even to regulators or the industry as a whole, the


network may not be fully observable in principle; for instance, many contracts


may be informal and intrinsically uncertain until events are realized. Several


natural questions emerge about how to measure risk in such systems. How


should a given firm evaluate its risk exposure, for instance in making decisions


about contracts, capital allocations, and treasury management? How should


regulators evaluate the risk of a given firm/organization and the structural ef

fects it could have on the wider network?


Consider that an agent has incomplete information about the network and


also has estimates about what they don’t know: i.e., uncertainty ranges about


the variables in the network. Our first example will show that it is non-trivial


for this organization to bound uncertainty about market values in the network


(including its own) since market values are not monotonic in network variables.


The results also extend to considering book values, which can sometimes also


be of interest.


**Example 7.1.** _(_ **v** ( _C_ ) _is non-monotonic in C) Define a financial network_ ( _C, D,_ _**β**_ _,_ _**θ**_ _,_ **p** )


342


Market Values are Non-Monotonic in _C_


Firm 1 Total Network


1.0


0.5


0.0
#### _C < C’ < C’’_

1 2 1 2 1 2


Figure 7.2: Example in which **v** ( _C_ ) is not monotonic in _C_ .


_and perturbed cross-holdings C_ _[′]_ _and C_ _[′′]_ _as follows:_











 _, D_ = _I,_ _**θ**_ =







 _,_ _**β**_ =







_,_








0 _._ 35


0 _._ 6









0 _._ 2


0 _._ 2





**p** =



0 _._ 3


0 _._ 6





0 _._ 6



0 _._ 6



0 _._ 2







_′_
 _, C_ =















0 0 _._ 1


0 0









0 0 _._ 1


0 _._ 2 0





_C_ =







0 0


0 0





0 0



0 0



_′′_
 _, C_ =



0 _._ 2 0



_._




_This is a simple two organization network. With cross-holdings C, the organizations are_


_not connected, with C_ _[′]_ _there is a one-way connection, and with C_ _[′′]_ _the organizations_


_form a cycle. In this example, C ≤_ _C_ _[′]_ _≤_ _C_ _[′′]_ _component-wise. We are interested in_


_the market values of the organizations and total network and seek to understand how_


_it is sensitive to changes in C. Figure 7.2 demonstrates that these market values are_


_not monotonic in C. As a result, the extreme values can occur within the interior of_


_bounds for C, as in this example. Identifying the best and worst case outcomes from_


_perturbations of C becomes a nontrivial task as we can’t just check the boundary points._


This result in itself isn’t exactly surprising as changing of cross-holdings can


shift value around significantly between organizations. Rather, it demonstrates


the tangible problem to organizations who want to evaluate the risks they face in


the network under imperfect network information. Our next example solidifies


343


0.95





Figure 7.3: Example network that is very sensitive to perturbations in _C_ .


this problem by showing that small uncertainty in the state of the network can


cause extreme sensitivity in market values.


**Example 7.2.** _(High sensitivity of_ **v** ( _C_ ) _to perturbations in C) Define a financial net-_


_work_ ( _C, D,_ _**β**_ _,_ _**θ**_ _,_ **p** ) _and perturbed cross-holdings C_ _[′]_ _and C_ _[′′]_ _as follows:_









0 _._ 7



0 0 _._ 95 0 0









0 _._ 37



0 _._ 58



0 0 0 _._ 98 0



0 _._ 21



0 _._ 7















_,_ _**β**_ =









_, C_ =



_D_ = _I,_ **p** =









1


1


1



_,_ _**θ**_ =



0 _._ 98 0 0 0



0 _._ 7



0 _._ 1



0









0









0 0 _._ 04 0 0



_This network contains a strongly weighted cycle (for this simple example, weights are_


_chosen close to 1), and a lightly connected organization d that ‘damps’ the cycle, as_


_shown in Figure 7.3. Consider that C_ _[′]_ _is a perturbation of C in which the only perturbed_


_entry is Cc,a_ = 0 _._ 99 _, corresponding to the fraction in other organizations owned by the_


_organization with the largest failure threshold. This represents a 1% perturbation, and_


_so a very small network change, but this change triggers a failure cascade in the cycle_


_with significant losses borne by organization d. In particular, organization d faces a_


_∼_ 61% _lower market value under C_ _[′]_ _as opposed to C even though it is only lightly_


_connected to the cycle and not part of the cycle itself._


344


**A.**


**B.**


**C.**





Figure 7.4: Examples of strong cycles that are combinations of weaker cycles.

#### **7.3.2 Sensitivity Problems in Realistic Networks**


While Example 7.2 is a toy example, its effects can translate to realistic settings,


and in fact real settings can be worse. In a real network, cycles may be more


complex, involving longer chains and interconnected subcycles. **A cycle can**


**still have a strong effect even though individual edges and subcycles may**


**not be strongly weighted.** Figure 7.4 illustrates strong cycles that can emerge


from interconnected weaker cycles. Many further variations are possible also.


In realistic networks, organizations lack a complete picture of the network


and may not even know whether they are connected to dangerous cycles,


whether part of a cycle itself or in a damping node position like organization


_d_ in Example 7.2. This becomes even harder for an organization to detect, and


so its risk harder to quantify, when cycles are more complex, like in Figure 7.4. In


real financial networks, it is not unheard of that organizations do not know that


they form dangerous cycles with each other. For instance, such cycles, unknown


to reinsurers at the time, ultimately contributed to large unintuitive losses expe

rienced during the London LMX spirals [111, 21].


345


Figure 7.5: A cycle in _C_ that aggregates losses from across the network. It is
hard for the green node to estimate its risk.


Real situations can actually be worse than in Example 7.2 because cycles can


connect organizations across the entire network and aggregate losses from dif

ferent parts. Figure 7.5 depicts such an aggregative cycle. In this case, the failure


- f any orange organization could cause the blue cycle to cascade. Any orange


losses, though they come from disparate parts of the network, get aggregated


through the cycle. Significant losses may be borne by blue organizations, as part


- f the cycle, and green organizations that damp the cycle.


In the context of dangerous cycles, diversification becomes difficult. In Fig

ure 7.5, greater connectivity of the cycle to disparate parts of the network can


be detrimental because of the aggregation effect that increases the likelihood


that the cycle cascades. Further, while damping nodes could theoretically di

versify, they may not realistically know whether or not other organizations are


also connected to the dangerous cycle.


In contrast, graphs without cycles have different behavior. For instance, con

sider the tree in Figure 7.6. While trees can aggregate losses from the leaves to


parent nodes, they do so in a way with less sensitivity since the aggregation can


346


Figure 7.6: Tree structures in _C_ can only aggregate losses in a line.


- nly occur in chains, and each link in the chain must be strong for aggregation


to continue. Knowing local information about your neighbors and the strength


- f their links goes a long way toward risk management in an acyclic network as


- pposed to cyclic networks.

#### **7.3.3 How this Paper Addresses these Problems**


Our illustration above of risk quantification problems arising from sensitivity


and model error motivates the questions we address in the remainder of this


work: (i) what formally causes network sensitivity, and (ii) how can we ef

ficiently quantify network sensitivities so that we can evaluate risks faced by


- rganizations in the network?


**What causes network sensitivity?** In the remaining sections, we formalize


how the major sensitivity issues emerge primarily from strong cycles and


threshold effects in the network. In Sections 7.4 and 7.5, we characterize dif

ferences in sensitivity between cyclic and acyclic networks. We show that sen

sitivity in acyclic networks is bounded in the size of the network (Corrollary 7.1


347


and Theorem 7.1).


In contrast, we show that sensitivity in cyclic networks is lower bounded


based on the weight of cycles in the network (Prop. 7.2) with a near-tight gen

eral upper bound that also increases significantly in the weight of cycles, as


measured through the column sums of _C_ being close to 1 (Prop. 7.4 and Theo

rem 7.2). Our results improve on past results in the literature in terms of tight

ness and generalization. Further, we show that if a cyclic network is sufficiently


close to acyclic, meaning its cycles are sufficiently weak, then sensitivity is in


turn bounded similarly low as in acyclic networks (Theorem 7.3). This helps us


address the question of how strong does a cycle have to be to pose sensitivity


challenges in the network. In principle, given an ‘acceptable’ level of sensitiv

ity in the network, it provides a means to determine how strong a cycle can be


allowed to get before the network exits the acceptable region.

#### **7.4 Perturbation Theory for Cascade Models**


In this section, we derive perturbation theory results about the types of systems


that we will encounter in analyzing the network cascade model. The structure


- f this type of model allows us to use standard techniques to bound sensitivities


using condition numbers. Our main results about economic cascade models in


the following sections build on these. We are not aware of the specific results


in this section being developed elsewhere. It is also separately worth demon

strating these methods and results as a tool that is more widely applicable to


network contagion models more generally.


348


#### **7.4.1 Background on Perturbation Theory**

We refer the reader to [94] and [67] for a review on condition numbers in nu

merical analysis. Conceptually, the condition number of a function measures


how much the output of the function can change in value for a small change


in the function input. Consider the linear system _A_ **x** = **b** and the perturbed


system ( _A_ + _δA_ )( **ˆx** ) = **b** where _δA_ perturbs _A_ . And suppose that, for some non

negative error matrix E and using the _L_ _[p]_ norm, we have _∥δA∥p ≤_ _ε∥E∥p_ and


that _ε∥A_ _[−]_ [1] _∥p∥E∥p ≤_ 1. Then the following inequalities describe perturbations


in **x** :

_∥δ_ **x** _∥p ≤_ _ε∥A_ _[−]_ [1] _∥p∥E∥p∥_ **ˆx** _∥p_


_∥δ_ **x** _∥p_ _ε∥A_ _[−]_ [1] _∥p∥E∥p_

_≤_ _._
_∥_ **x** _∥p_ 1 _−_ _ε∥A_ _[−]_ [1] _∥p∥E∥p_

We define the norm-wise condition number as _κ_ _[p]_ ( _A, E_ ) = _∥A_ _[−]_ [1] _∥p∥E∥p_ . When


_E_ = _A_, we have _κ_ _[p]_ ( _A_ ) = _∥A_ _[−]_ [1] _∥p∥A∥p_ .


Let _|A|_ represent the entry-wise absolute value of the matrix _A_ . Alternatively,


supposing _|δA| ≤_ _εE_ component-wise for non-negative error matrix _E_ and that


_ε∥|A_ _[−]_ [1] _|E∥p ≤_ 1, we have the following inequalities:




_−_ 1
_∥δ_ **x** _∥p ≤_ _ε_ - � _|A_ _|E|_ **ˆx** _|_ - � _p_
_∥δ_ **x** _∥p_ _≤_ _ε_

_∥_ **x** _∥p_ 1 _−_ _ε∥|A_ _[−]_ [1] _||E|∥p_



_∥|A_ _[−]_ [1] _|E|_ **x** _|∥p_


_._
_∥_ **x** _∥p_



We define the relative component-wise condition number as


_κ_ _[p]_ _c_ [(] _[A, E,]_ **[ x]** [) =] _[∥|][A][−]_ [1] _[|][E][|]_ **[x]** _[|∥][p]_ _._

_∥_ **x** _∥p_


For the _L_ _[∞]_ norm, _κ_ _[∞]_ _c_ [(] _[A, E]_ [) =] _[ ∥|][A][−]_ [1] _[|][E][∥][∞]_ [represents the worst-case condition-]


ing in **x** . It describes the maximum component-wise sensitivity of **x** = _A_ _[−]_ [1] **b** to


errors in _A_ - r **b**
. In our financial network setting, this will describe the maxi

mum sensitivity an organization faces (on market value, loss, etc) resulting from


349


errors in this linear system. If _E_ = _|A|_, this yields Skeel’s condition number


_κc_ ( _A_ ) = _∥|A_ _[−]_ [1] _||A|∥∞_ .


**Remark 7.1.** _Compared to typical numerical analysis in computing, the bar for de-_


_termining “ill-conditioned” is much lower in social science models because the level of_


_uncertainty is much higher than machine epsilon in these systems. For instance, condi-_


_tion numbers of 1000 can cause problems, whereas normally this would not be a problem_


_in computing. With threshold models in particular, digits of accuracy become very im-_


_portant as large errors are propagated to the next steps in the process, leading to even_


_more errors._

#### **7.4.2 Acyclic Systems**


Prop. 7.1 bounds Skeel’s condition number of _I −_ _C_ when _C_ is the adjacency


matrix of an acyclic network, i.e., a directed acyclic graph (DAG).


**Prop. 7.1.** _Let C be a n × n non-negative weakly column sub-stochastic nilpotent_


_matrix. Then Skeel’s condition number κc_ ( _I −_ _C_ ) _≤_ 2 _n −_ 1 _. Further, this bound is_


_tight._


[Link to Proof]


Interestingly, this bound depends linearly on the dimensionality of the sys

tem. Thus, acyclic graphs guarantee a relatively low condition number. By


comparison, Theorem 3.9 in [63] gives that the expected norm-wise _L_ [2] condi

tion number of a random Gaussian distributed matrix is on the order of _n_ [5] _[/]_ [2] .


_L_ [2] conNote that this comparison isn’t perfect, however, as (i) the norm-wise


dition number is not quite the same as Skeel’s condition number, and (ii) we


350


require the matrix _C_ is sub-stochastic, which requires appropriate scaling of a


random Gaussian matrix.


When we consider the system ( _I −C_ ) **x** = **b**, we can actually guarantee better


conditioning than given by Skeel’s condition number by noting that the pertur

bations to _I −_ _C_ - nly occur in the off-diagonal. The following corollary formal

izes this.


**Corollary 7.1.** _Let C be a n × n non-negative weakly column sub-stochastic nilpotent_


_matrix that is subject to perturbations |δC| ≤_ _εC. Then the component-wise relative_


_condition number of I −_ _C is κ_ _[∞]_ _c_ [(] _[I][ −]_ _[C, C]_ [)] _[ ≤]_ _[n][ −]_ [1] _[. Further, this bound is tight.]_


[Link to Proof]

#### **7.4.3 Cyclic Systems**


**Lower bound on condition number.** The well-conditioning of acyclic systems


suggests that cycles can cause sensitivity problems. Prop. 7.2 characterizes this


explicitly by lower bounding Skeel’s condition number based on the weight of


cycles in the network. In particular, for a 2-cycle with edges weighted _a_ and


_b_ in some power of the adjacency matrix, Skeel’s condition number is lower


1
bounded by a term of 1 _−ab_ [.]


**Prop. 7.2.** _Let C be a n × n non-negative weakly column sub-stochastic matrix with_


_spectral radius ρ_ ( _C_ ) _<_ 1 _. Suppose that for some power q, Ci,j_ _[q]_ [=] _[ a][ and][ C]_ _j,i_ _[q]_ [=] _[ b][ (i.e.,]_


_i →_ _j →_ _i is a cycle in C_ _[q]_ _). Then_


_κc_ ( _I −_ _C_ ) _≥_ 1 + [2] _[a]_ [(] _[b]_ [ + 1][)]

1 _−_ _ab_ _[.]_


351


[Link to Proof]


**Remark 7.2.** _Note that all even cycles in C can be represented as a 2-cycle in C_ _[q]_ _for_


_some q. This allows us to simplify the statement of Prop. 7.2. An analogous result can_


_be formulated for odd cycles. Further, Prop. 7.2 can be easily strengthened by summing_


_over the terms corresponding to all cycles that show up in a given row of C._


This result demonstrates that graph cycles can give rise to sensitivity that is


distinctly different than in acyclic graphs. To illustrate that the acyclic upper


bound is no longer valid in a domain with cycles, consider a two node cyclic


graph with _a_ = 1 and _b_ = 0 _._ 99. The maximum row sum of [�] _[∞]_ _k_ =1 _[C]_ _[k]_ [ is then]


199 _>> n −_ 1 = 1.


**Upper bound on condition number.** We next characterize the degree to which


cycles can lead to ill-conditioning. Prop. 7.3 and Prop. 7.4 give upper bounds


for the condition numbers of _I −_ _C_ and ( _I −_ _C_ ) _C_ [ˆ] _[−]_ [1] respectively. In particular,


these are upper bounded by a factor of 1 _−∥_ 1 _C∥_ 1 [, which can be large when strong]


cycles lead to column sums close to one.


**Prop. 7.3.** _Let C be a n × n non-negative weakly column sub-stochastic matrix with_


_zero diagonals and spectral radius ρ_ ( _C_ ) _<_ 1 _. Then the L_ [1] _-norm condition number of_


_I −_ _C satisfies_

_[∥][C][∥]_ [1]
_κ_ [1] ( _I −_ _C_ ) _≤_ [1 +] _._

1 _−∥C∥_ 1


[Link to Proof]


A type of cycles, termed ‘relaxed cycles’ in [111], come close to realizing the


worst case bounds in Prop. 7.3, as demonstrated in Figure 7.7. The concept of


352


relaxation here means that the cycle recirculates close to (but _≤_ ) 100% value.


Cycles of this type were present in the Lloyd’s and London reinsurance mar

kets in the 1980s and are associated with the resulting London LMX spirals. As


explored in [111], relaxed cycles lead to a host of counterintuitive spiral behav

iors in reinsurance networks. In such spirals, a majority of insurance liabilities


can be borne by unsuspecting organizations in the network due to the network


structure.


We can similarly bound the conditioning of the product matrix ( _I −_ _C_ ) _C_ [ˆ] _[−]_ [1] .


**Prop. 7.4.** _Let C be a n × n non-negative column strictly sub-stochastic matrix with_


_zero diagonals and_ _C_ [ˆ] _be the diagonal matrix with entries_ _C_ [ˆ] _ii_ = 1 _−_ [�] _j_ _[C][ji][. Then the]_


_L_ [1] _-norm condition number of the product matrix_ ( _I −_ _C_ ) _C_ [ˆ] _[−]_ [1] _satisfies_


_[∥][C][∥]_ [1]
_κ_ [1][�] ( _I −_ _C_ ) _C_ [ˆ] _[−]_ [1][�] _≤_ [1 +] _._

1 _−∥C∥_ 1


[Link to Proof]


Notice that _κ_  - ( _I −C_ ) _C_ [ˆ] _[−]_ [1][�] describes sensitivity of perturbations to _the product_


_matrix_, whereas we are more interested in perturbations to _C_ . In this case, ( _I −_


_C_ ) _C_ [ˆ] _[−]_ [1] is not a linear transformation in propagating errors. However, it still


provides a useful theoretical perspective on conditioning. The intuition from


this actually lines up with what we see in the next section when we consider the


network system more directly.


We show how tight these two bounds are in Figure 7.7. To do so, we consider


two parameterized families of adjacency matrices with relaxed cycles: one that


forms a damped cycle as in Figure 7.3, and one that forms a more complex cycle,


composed of interconnecting subcycles. These are labeled “Damped Cycle” and


353


|0000 ComplexCycle<br>7500<br>5000<br>2500<br>0000<br>7500<br>5000<br>2500<br>0<br>0 2500 5000 7500 10000 12500 15000 17500 20000|ComplexCycle|Col3|Col4|
|---|---|---|---|
|0<br>2500<br>5000<br>7500<br>10000<br>12500<br>15000<br>17500<br>20000<br>0<br>2500<br>5000<br>7500<br>0000<br>2500<br>5000<br>7500<br>0000<br>Complex Cycle|Complex Cycle|500<br>10000<br>12500<br>15000<br>1|7500<br>20000|


L1 Cond. # Bound


(b) _κ_ [1][�] ( _I −_ _C_ ) _C_ [ˆ] _[−]_ [1][�] vs. bound



20000


5000


2500


0







0 2500 5000 7500 10000 12500 15000 17500 20000


(a) _κ_ [1] ( _I −_ _C_ ) vs. bound



Figure 7.7: _L_ [1] condition number bounds are (a) near tight for _κ_ [1] ( _I −_ _C_ )

(Prop. 7.3), and (b) tight for _κ_ [1][�] ( _I −_ _C_ ) _C_ [ˆ] _[−]_ [1][�] (Prop. 7.4), for relaxed cycles as
indicated by points near the diagonal.


“Complex Cycle”. These families are parameterized by the strength of the cycle:


a higher parameter changes the strength of the cycle while keeping the size


and shape of the network otherwise constant. The precise specification of these


families is given in the following two examples.


**Example 7.3.** _(Damped Cycle) For a parameter ω ∈_ (0 _,_ 1) _, define the following:_









0 0 0 0 0



0 0 1 0 0



_ω ∈_ (0 _,_ 1) _, X_ = _ω_









0 0 0 1 0



_,_ _**γ**_ =









1


_ω_


1


1



_._



1 1 0 0 0



0 0 1 0 0



1 _−_ _ω_









_The adjacency matrix containing the damped cycle is then C_ = _**γ**_ _X. Notice that it is_


_column-substochastic with zero diagonals, as required._


354


**Example 7.4.** _(Complex Cycle) For a parameter ω ∈_ (0 _,_ 1) _, define the following:_









0 0 0 0 0 0 0



1 0 0 1 1 0 0



1


0 _._ 5









0 1 0 0 0 1 0



0 _._ 5 _ω_



_ω ∈_ (0 _,_ 1) _, X_ = _ω_









0 0 1 0 0 0 1



_,_ _**γ**_ =









0 _._ 5


0 _._ 5


0 _._ 5


0 _._ 5



0 1 0 0 0 1 0



0 0 1 0 0 0 1



1 0 0 1 1 0 0



_The adjacency matrix containing the complex cycle is then C_ = _**γ**_ _X. Notice that it is_


_column-substochastic with zero diagonals, as required. Additionally, all entries of C are_


_less than 0.5, illustrating that complex cycles can cause strong effects even with all edge_


_weights much less than 1._


In Figure 7.7, we plot the _L_ [1] condition numbers of the resulting _I −_ _C_ and


( _I −_ _C_ ) _C_ [ˆ] _[−]_ [1] matrices arising in these families for parameter values in the range


(0 _._ 8 _,_ 1). We plot the condition number on the _y_ - axis and the upper bound from


_x_
Prop. 7.3 on the - axis. In Figure 7.7a, these families appear very close to the


_y_ = _x_ line, showing that the bound in Prop. 7.3 is near tight for these cycles.


Figure 7.7b shows that the bound in Prop. 7.4 is tight for the complex cycle (not


shown, also for the damped cycle). Notably, the complex cycle shows strong


sensitivity effects near the bound despite having all edge weights less than 0.5.

#### **7.5 Model Results: Sensitivity without Threshold Effects**


We now build on our perturbation theory results in Section 7.4 to describe sen

sitivity in the network model. In this section, we develop direct bounds for


355


the effects of cross-holdings and asset price perturbations when failure costs are


zero (no threshold effects). Where there are previous results in the literature, our


results improve on them. We also present new results that go beyond previous


results. As we demonstrated earlier, graph perturbations lead to non-monotonic


behavior in the parameters, which presents problems in identifying uncertainty


propagation bounds, whereas asset price perturbations are monotonic. Our re

sults suggest the former can lead to larger errors.

#### **7.5.1 Acyclic Networks without Threshold Effects**


In Theorem 7.1, we show that the sensitivity of an acyclic network without


threshold effects is bounded in terms of the system dimensions. This means


that these are relatively well-behaved systems.


**Theorem 7.1.** _Let_ ( _C, D,_ _**β**_ _,_ _**θ**_ _,_ **p** ) _be an economic network with_ _**β**_ = 0 _and C an n × n_


_non-negative strictly column sub-stochastic nilpotent matrix with zero diagonals (i.e.,_


_C is acyclic). Then under perturbations |C_ [˜] _−_ _C| < ε|C| such that_ _C_ [˜] _is still non-_


_negative strictly column sub-stochastic with zero diagonals, organization book values_


_are perturbed by at most_


_∥_ **V** **[˜]** _−_ **V** _∥∞_ _≤_ _ε_ ( _n −_ 1) _∥_ **p** _∥_ 1


_and organization market values are perturbed by at most_


_∥_ **˜v** _−_ **v** _∥∞_ _≤_ _ε_ 1 + ( _n −_ 1)(1 + _ε_ ) _∥_ **p** _∥_ 1 _._

             -             

[Link to Proof]


Theorem 7.1 additionally suggests that, even in simple acyclic networks, sen

sitivity _can_ be quite high in very large systems, for instance, when there are long


356


chains. This is consistent with the results in [28], though covering a more gen

eral context than specific example graphs, about sensitivity arising from chains


in the network.


Theorem 7.1 improves on Corollary 1 from [93] in a number of ways. Their


Corollary 1 establishes that, given a non-cyclic network subject to a perturbation


_ε_

- n one edge of at most, the uncertainty in any one market value is limited to


_ε∥_ **p** _∥_ 1.


  - A straightforward extension of their Corollary 1 to the setting of perturba

tions on all edges adds a factor of _n_ [2] as the maximum number of edges in


a DAG is _n_ ( _n −_ 1) _/_ 2, and we may further have uncertainty about which


edges are actually in the DAG. In contrast, our bound contains a single


factor of _n_ . It is unclear how to arrive at our better bound starting solely


from the results in [93]


  - Our bounds apply in a more general setting. In particular, our Theo

rem 7.3, introduced in the next section extends our bounds to cyclic net

works that are ‘close’ to acyclic.

#### **7.5.2 Cyclic Networks without Threshold Effects**


Recall that Prop. 7.4’s bound on the condition number of ( _I −_ _C_ ) _C_ [ˆ] _[−]_ [1] applies to


perturbations of the product matrix and not to perturbations of _C_ itself. In fact,


a similar bound holds for perturbations to _C_ in the economic network model,


which demonstrates that uncertainty in _C_ has a much more extreme effect on **v**


in the cyclic setting. The next theorem restates a result from [93] in a corrected


form (for completeness, we also provide the corrected proof). The correction is


357


that there should be a coefficient of 2 _ε/r_ since _∥E∥_ 1 + _∥E_ [ˆ] _∥_ 1 _<_ 2 _ε_ instead of _< ε_


as they state. This comes from the fact that all market values add to the value of


all underlying assets, and so the output is constrained from changing too much.


**Theorem 7.2.** _(Corrected from [93]) Let_ ( _C, D,_ _**β**_ _,_ _**θ**_ _,_ **p** ) _be an economic network with_


_**β**_ = 0 _and C an n × n non-negative column strictly sub-stochastic matrix with zero_


_diagonals. Define_ _C_ [ˆ] _to be the diagonal matrix with entries_ _C_ [ˆ] _ii_ = 1 _−_ [�] _j_ _[C][ji][. Then]_


_for perturbations ∥C −_ _C_ [˜] _∥_ 1 _< ε, such that_ _C_ [˜] _is still non-negative column strictly_


_sub-stochastic with zero diagonals, organization market values are perturbed by at most_


2 _ε_
_∥_ **v** _−_ **˜v** _∥_ 1 _≤_ min _∥D_ **p** _∥_ 1 _,_

               - _r_ _[,]_ [ 2]                

ˆ˜
_where r_ = min _i_ _Cii,_ ˆ _Cii_ _._

      -      

[Link to Proof]


In [93], they also provide an example to illustrate an instance of ill

conditioning along these lines. Notice that similar bounds can’t be made on


**V** because we cannot bound _∥_ **V** _∥_ across all cyclic networks. This is because **V**


represents book values in the model, which include double counting through


cross-holdings (one of the motivations for defining market values **v** ).


We can in fact improve on these results using our perturbation theory anal

ysis. In fact, the well-behaved bounds in Theorem 7.1 can be extended to some


cyclic networks. If our given network is ‘sufficiently close’ to a DAG, then the


sensitivity is bounded even if _C_ is not itself a DAG. To formalize ‘sufficiently


close’, we need the following conditions on _C_, some DAG _C_ [¯], and _ε_ :


 - _|C −_ _C_ [¯] _| < εC_, meaning that _C_ [¯] is a small perturbation of _C_ .


358


¯

 - _ε_ _|_ ( _I −_ _C_ ) _−_ 1 _||_ 2 _C|_

        - ��         - �� _∞_ _[≤]_ _[ε]_ [(2] _[n][ −]_ [1)] _[ <]_ [ 1][, meaning that] _[ εC]_ [ perturbations of]

_I −_ _C_ [¯] are nonsingular.


The following theorem gives the resulting bounds.


**Theorem 7.3.** _Let_ ( _C, D,_ _**β**_ _,_ _**θ**_ _,_ **p** ) _be an economic network with_ _**β**_ = 0 _. Suppose there_


_is a DAG_ _C_ [¯] _(i.e.,_ _C_ [¯] _is an n × n non-negative strictly column sub-stochastic nilpotent_


_matrix with zero diagonals) such that |C_ [¯] _−_ _C| < ε|C|. Then under perturbations_


_|C_ [˜] _−_ _C| < ε|C| such that_ _C_ [˜] _is still non-negative strictly column sub-stochastic and the_


_condition_ (2 _n −_ 1) _ε <_ 1 _, organization book values are perturbed by at most_



_n −_ 1 2( _n −_ 1)
_∥_ **V** **[˜]** _−_ **V** _∥∞_ _≤_ _ε_

            - 1 _−_ _nε_ [+] 1 _−_ (2 _n −_ 1) _ε_


_and organization market values are perturbed by at most_



_∥_ **p** _∥_ 1




_n −_ 1 2( _n −_ 1)
_∥_ **˜v** _−_ **v** _∥∞_ _≤_ _ε_ 1 + (1 + _ε_ )

     -      - 1 _−_ _nε_ [+] 1 _−_ (2 _n −_ 1) _ε_



_∥_ **p** _∥_ 1 _._

- �




[Link to Proof]


Note how the bounds here are more complicated than in Theorem 7.1. Com

plications arise when comparing perturbations to the DAG _C_ [¯] that may turn it


into a cyclic graph, at which point we no longer have that _∥_ **V** **[˜]** _∥∞_ _≤∥_ **p** _∥_ 1 (and


it is in fact not bounded at all). Instead, we need to express bounds in terms of


_∥_ **V** **[¯]** _∥∞_, which does satisfy this. However, this requires incorporating the more


complicated conditioning bounds in Section 7.4.1. The extra conditions arise


from both requirements of this process and the restriction to the substochstic


_ε_ .
space of matrices–both of which depend on


Adding to previous results, this confirms that strongly weighted cycles are


specifically what cause sensitivity problems in these systems. These problems


359


become even worse with the inclusion of threshold effects. Theorem 7.3 can be


used to give an idea of how strong cycles need be before introducing sensitivity


problems. For instance, we can determine how far _C_ has to be from a DAG to


achieve a given unacceptable level of end uncertainty.

#### **7.5.3 Asset Price Perturbations without Threshold Effects**


We now briefly consider the effects of perturbations to asset prices **p**, which we


will see are more contained than the case of perturbations to _C_ . Theorem 7.4


provides an upper bound to the the perturbation effects on market values for


general networks.


**Theorem 7.4.** _Let_ ( _C, D,_ _**β**_ _,_ _**θ**_ _,_ **p** ) _be an economic network with_ _**β**_ = 0 _and C an n × n_


_non-negative column strictly sub-stochastic matrix with zero diagonals. Define_ _C_ [ˆ] _to be_


_the diagonal matrix with entries_ _C_ [ˆ] _ii_ = 1 _−_ [�] _j_ _[C][ji][. Then for perturbations][ |]_ **[˜p]** _[ −]_ **[p]** _[|][ <]_


_ε|_ **p** _|, organization market values are perturbed by at most_


_∥_ **˜v** _−_ **v** _∥∞_ _≤_ _εn_ [2] _∥_ **p** _∥_ 1 _._


[Link to Proof]


Note that in the case of cyclic networks, we can use the bound on Skeel’s


condition number from Prop. 7.1 to get an uncertainty bound linear in _n_ instead


- f quadratic.


**Remark 7.3.** _Since_ _C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] _is column-stochastic, we’ve seen that ∥_ **v** _∥_ 1 = _∥_ **p** _∥_ 1 _._


_This means that perturbations in_ **p** _propagate quite mildly in the 1-norm. In particular,_



_the 1-norm relative condition number is κ_ = _[∥][D]_ **[p]** _[∥]_ [1] _[∥][C]_ [ˆ][(] _[I][−][C]_ [)] _[−]_ [1] _[∥]_ [1]




[1]

_∥_ **v** _∥_ [= 1] _[.]_




_[C]_ [(] _[I][−][C]_ [)] _[−]_ _[∥]_ [1]

= _[∥]_ **[p]** _[∥]_ [1]
_∥_ **v** _∥_ 1 _∥_ **v** _∥_



360


Together, Theorem 7.4 and Remark 7.4 show that perturbations to **p** can only


affect **v** in a limited way compared to perturbations to _C_ . Thus, we restrict our


focus to considering perturbations to _C_ . Additionally, note that **v** is monotonic


in **p**, so there are trivial bounds on uncertainty in **v** from **p** . However, we can


still apply the same condition number machinery we are developing for _C_ per

turbations to better analyze the setting of **p** perturbations. Further results in the


next section are easily extended to include perturbations to both **p** and _D_ .

#### **7.5.4 Bounding Sensitivity for Particular Instances**


While our earlier results focus on conceptual understanding of the sensitivity


problem over an entire class of systems on the global level, in this subsection we


shift the focus to solving the problem in particular instances. We will find that


this leads to fairly tight and usable bounds in practice on sensitivity. Prop. 7.5


bounds the uncertainty in **v** in terms of _∥_ **V** _∥∞_ .


**Prop. 7.5.** _Consider an economic network_ ( _C, D,_ _**β**_ _,_ _**θ**_ _,_ **p** ) _with cross-holdings matrix_


_C (i.e., non-negative strictly column sub-stochastic with zero diagonals). Suppose or-_


_ganization book values are given by_ **V** _for the given C and that C has uncertainty_


_|C_ [˜] _−_ _C| < ε|C| such that_ _C_ [˜] _is still non-negative strictly column sub-stochastic with_


_zero diagonals. Then the uncertainty in organization market values is at most_


_∥_ **˜v** _−_ **v** _∥∞_ _≤_ _ε∥_ **V** _∥∞_ (1 + _κε_ ) _∥C∥_ 1 + _κ∥C_ [ˆ] _∥∞_ _,_

              -              

_where κ_ = _κ_ _[∞]_ _c_ [(] _[I][ −]_ _[C, C]_ [)] _[ is the component-wise relative condition number.]_


[Link to Proof]


361


Note that this bound is not general in a global sense, like the bounds derived


previously, since its value depends on the system being considered. In practice,


however, this bound will often be tighter. The general error bounds can a large


- verestimate of the actual error in a given system. Prop. 7.5 will be a key part in


- ur algorithm to calculate practical error bounds for an input system.


Call the bound from Prop. 7.5 _δv_ . Recall that the crossing of a threshold is


determined by checking **v** _≥_ _**θ**_ . Accounting for uncertainty in **v**, we now need


to check **v** _± δv ≥_ _**θ**_ . The uncertainty _δv_, once known, can alternatively be inter

preted as uncertainty in _**θ**_ in this inequality. Since **v** is monotonic in _**θ**_, we can


construct best and worst cases that bound the error. We can do this iteratively


to construct best and worst cases throughout the sequence of operations in eval

uating the model. We will find that this yields bounds for best and worst case


market values given the original perturbations in _C_ .


In practice, this is not the best that we can do unless the network is nearly


homogeneous (i.e., nodes are of the same size). This is because the bounds in


Prop. 7.5 are not individualized to nodes. Since some nodes have larger val

ues, this boosts the overall error propagating in the algorithm when we use this


method as currently formulated. Instead, we will next show a way to strengthen


the results considerably, and prove that this indeed works in that context.


Much tighter bounds on sensitivity can be achieved in a comopnent-wise


manner when we also know more about the error matrix. Prop. 7.6 bounds


component-wise uncertainty in **v** based on **V** .


**Prop. 7.6.** _Consider an economic network_ ( _C, D,_ _**β**_ _,_ _**θ**_ _,_ **p** ) _with cross-holdings matrix_


_C (i.e., non-negative strictly column sub-stochastic with zero diagonals). Suppose or-_


_ganization book values are given by_ **V** _for the given C and that C has uncertainty_


362


_|C_ [˜] _−_ _C| < εE such that_ _C_ [˜] _is still non-negative strictly column sub-stochastic with zero_


_diagonals. Define A_ := _I −_ _C and suppose that I −_ _εA_ _[−]_ [1] _E is nonsingular. Then the_


_uncertainty in organization book values is at most (component-wise)_


_|_ _**δ**_ **V** _| ≤_ _ε_ ( _I −_ _εA_ _[−]_ [1] _E_ ) _[−]_ [1] _A_ _[−]_ [1] _E|_ **V** _|,_


_and the uncertainty in organization market values is at most (component-wise)_


_|_ _**δ**_ **v** _| ≤_ _C_ [ˆ] _|δ_ **V** _|_ + _εE_ [ˆ] ( _|_ **V** _|_ + _|δ_ **V** _|_ ) _,_


_where_ _E_ [ˆ] _is the diagonal matrix of column sums of E._


[Link to Proof]

#### **7.6 Simulations: Sensitivity in Practice**


To demonstrate the use of our results, we consider an application of our al

gorithm to an economic network. We construct an instance of the economic


network based on the World Input Output Database (WIOD). The data is freely


[available at http://www.wiod.org/home.](http://www.wiod.org/home)


The simulations we perform are intended as a proof of concept of a realistic

looking setup. While they are based on real underlying data, we stress that sev

eral parts of the setup remain stylized since data is not available: in particular,


underlying assets, thresholds, and failure costs. Additionally, natural distortion


arises from the aggregation effects from grouping entire industries into single


nodes.


Our code for the implementation of our algorithm and simulations will be


released at a later date.


363


#### **7.6.1 Simulation setup**

The WIOD dataset (see [181]) measures the flow of reasources in dollar value


between different economic sectors within different countries (intermediate de

mand) and national-level final demand (e.g., GDP components, such as con

sumption, investment, government expenditure). The dataset spans 2464 dis

tinct economic sectors spread between 28 EU countries and 15 other major coun

tries for the years 2000-2014.


Following the same methodology as in [113], we create economic networks


based on each year of the WIOD dataset as follows:


1. Set the number of nodes to _n_, representing the number of columns in the


dataset that refer to economic sectors or final demand components;


_n × n_
2. Set up a array of flows between nodes from the dataset, with zero


rows for final demand components;


3. Transpose the components of any negative entries in the array;


4. Scale columns to sum to 1 (inclusive of **value added**, a dataset row not


included in the array) or 0 if a zero column; [1]


5. Set all diagonals in the array to zero. The output is _C_ .


6. Remove nodes with near zero value added (columns referring to house

holds) from _C_ . This fixes unnecessarily bad conditioning in _C_ as these


nodes do not fit the model well.


7. Set the vector _D_ **p** to be the output of each node at basic prices (TOT ~~G~~ O


row in the dataset).


1Labor and capital that is directly and indirectly needed in the production of final good
manufacturing is traced by ‘value added’, see [181].


364


8. Set the vector _**θ**_ = _C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] _D_ _**p**_ _−_ **value added**, which gives the market


value in the absence of threshold effects minus value added.


9. Set the vector _**β**_ with entries 0 _._ 1 _·_ **value added** .


In the simulation study, we perform Monte Carlo simulations over the per

turbations to _C_ . The simulations take as input a non-negative error matrix _E_


and magnitude of error _ε_ such that the perturbations obey _|δC| ≤_ _εE_ . To simu

late perturbations, we sample the elements of _δC_ uniformly in this range.

#### **7.6.2 Network shape and conditioning**


We begin at a high level by comparing the various condition numbers associ

ated with our global results in previous sections. Figure 7.8 shows the _κc, κ_ [1] _, κ_ _[∞]_


condition numbers of _I −_ _C_ and ( _I −_ _C_ ) _C_ [ˆ] in these networks over different years.


Note that these condition numbers are not altogether large (the spike in 2006


is likely a fluke of the data as opposed to a particular event, but even that is


not generally large). As discussed before, the bar for “ill-conditioned” is much


lower in these models because the level of uncertainty is much higher than ma

chine epsilon. Condition numbers around 1000 can be problematic, particularly


around threshold values, when digits of accuracy become very important.


Figure 7.9 provides a network visualization of the WIOD 2014 network that


we use in the simulation study.


Figure 7.10 shows the weights of cycles in the WIOD networks measured by


the product of edge weights traversing the cycle. A 2-cycle of weight 0 _._ 05 would


mean the geometric mean of edge weight in the cycle is _≈_ 0 _._ 22. We measure


365


WIOD         Conditioning (𝐼−𝐶ሻ


I-C Sk 𝜅 I-C L1 𝜅 [1] I-C inf 𝜅 [∞]



1.E+08


1.E+06


1.E+04


1.E+02


1.E+00



WIOD            Conditioning (𝐼−𝐶) 𝐶 [መ] [−1]



A Sk 𝜅𝑐



𝜅𝑐



WIOD         Conditioning (𝐼−𝐶ሻ



1.E+03


1.E+02


1.E+01



I-C Sk 𝜅𝑐 I-C L1 𝜅 [1] 𝜅 [∞]







1.E+00


(a) _I −_ _C_ condition numbers



(b) ( _I −_ _C_ ) _C_ [ˆ] _[−]_ [1] condition numbers



Figure 7.8: Condition numbers in WIOD networks.


Figure 7.9: Visualization of 2014 WIOD network.


366


the cycle weights in this way by iteratively calculating powers of the adjacency


matrix and zeroing out the diagonal before continuing with the next power.


_n_ _n_
Note that the diagonal of - th power matrix tells us about the weight of - cycles


in the network. Figure 7.10 shows both the maximum weight of a cycle in each


network as well as the sum of all cycles’ weights, which describes the scope


- f cyclical shape in the network. Note also that the sum across all cycles then


contains some double-counting of cycles depending on how long cycles are; in


particular, a 2-cycle is counted twice as there will be a diagonal entry for each


node in the cycle. Considering both this and the limited data itself, it is difficult


to draw firm conclusions solely on the basis of cycle weights. Nevertheless, an


interesting observation is that the sum of cycle weights decreases sharply since


2009 and the financial crisis whereas the largest cycle weights remain relatively


unchanged over time. In particular, the sensitivity effects of these cycles can still


be present in the network even though the aggregate cycle weight decreases. In


such a setting, it is of particular importance to organizations in the network to


know the extent to which they are connected to strong cycles and the sensitivity


effects this has on their own model error. In the next section we apply our


methodology to study these sensitivities.

#### **7.7 Discussion**


We have developed a framework that relies on perturbation theory to charac

terize nodes’ sensitivity to parameter values, and in particular to changes in


the network structure. The risk manager or regulator can set an ’acceptable’


level of sensitivity in the network, and our results would allow for monitoring


if cycles are becoming too strong. In such case the impact of even small vari

367


10


9.9


9.8


9.7


9.6


9.5


9.4


9.3


9.2


9.1


9



0.08


0.07


0.06


0.05


0.04


0.03


0.02


0.01


0



Cycle Weights in WIOD Networks





2000 2002 2004 2006 2008 2010 2012 2014


Year


Figure 7.10: Cycle weights in WIOD networks


ations along those cycles could be large enough to make an organization face


unacceptable levels of risk. From a technical standpoint, the key elements that


allow us to derive the results are the fact that the Elliott-Golub-Jackson model


can be interpreted as a sequence of dependent linear systems and the fact that


model outputs are monotonic in nonlinear events such as failures. Our results


can therefore generalize to a class of models that have these characteristics di

rectly or after simple transformations. This is the case for the vast majority of


literature, for example the one deriving from [75], where results can readily be


adapted.


We address one component of model error: assuming that the risk model


is correct, we measure the effect of parameter uncertainty. This relates to the


question of model choice in economic network analysis. A model can be too


qualitative and limited to only some effects, so one would need a class of mod

els to capture realistic effects and believable ranges of outcomes. Rather than


thinking about this as model ambiguity, we can think of it as model aggrega

tion. In general, aggregating and extracting information from a class of models


368


is hindered by computational and sensitivity difficulties. Our results allow us


to reduce this problem to a much simpler one. Indeed, our methodology can be


used for the entire class of models to obtain upper and lower sensitivity bounds


for each model, which can then be aggregated.


We have related sensitivity to network substructures such as strong cycles,


which are represented not only by strongly weighted cycles but also by certain


dangerous configurations of multiple cycles that can make system conditioning


bad. Further research is needed to actually identify such configurations. A first


approach would be to consider a large number of simulated and real datasets


for parameters and estimate node values under various risk scenarios. How

ever, the scenario and parameter space can be huge and thus convergence slow


and costly. One possible direction is to reduce the dimensionality of the prob

lem by identifying the critical directions that cause parameter sensitivity (active


subspace method). These directions can be used to restrict dimensionality and


may even help in directly linking strong cycles that correspond to them. One


question is how sensitive are the extracted important directions to the ground


truth setup and level of uncertainty. More importantly, what information can


we extract in a model independent way?


Using machine learning techniques such as training a neural network func

tion to estimate node sensitivity could also help lower the complexity of the sim

ulations for large networks. Generating a training set for a neural network en

tails generating a wide variety of networks and evaluating nodes’ holdings and


cross holdings under different stress scenarios and failure thresholds. Another


approach could rely on developing classification algorithms that can effectively


identify highly sensitive nodes and structures with ’strong’ effects emerging in


369


the network. Graph kernels, which define a distance between networks, could


be used in algorithms to cluster networks with similar structures and sensitivi

ties.

#### **7.8 Appendix: Proofs and Additional Details**


**Calculating cascades** Given an economic network ( _C, D,_ _**β**_ _,_ _**θ**_ _,_ **p** ), we can com

pute the best case cascade (minimum solution) through the following algorithm.


**Algorithm 13** Calculate Golub-Jackson cascade
**Require:** _C_, _D_, **p**, _**θ**_, _**β**_

Let _B_ 0 be the 0 matrix, _t_ = 0, _B−_ 1 _̸_ = _B_ 0, and _C_ [ˆ] be diagonal matrix s.t. _C_ [ˆ] _ii_ =
1 _−_ [�] _j_ _[C][ji]_

**while** _Bt ̸_ = _Bt−_ 1 **do**

_t ←_ _t_ + 1
Calculate **vt** = _C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] ( _D_ **p** _−_ _Bt−_ 1 _**β**_ )
Define diagonal matrix _Bt_ by setting _Bt,ii_ = 1 if **vt** _,i ≤_ _**θ**_ _i_ and 0 otherwise
**end while**

**v** _←_ **vt**, _B ←_ _Bt_
**return v** _, Bt_


In [76], they don’t discuss how to solve for **vt** above. For numerical reasons,


we will not want to compute _C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] directly. Instead, since _C_ [ˆ] is diagonal,


we will want to solve


( _I −_ _C_ ) _C_ [ˆ] _[−]_ [1] **vt** = _D_ **p** _−_ _Bt−_ 1 _**β**_


for **vt** . In fact, since the matrix _C_ doesn’t change between iterations, we can


re-use the LU factorization at each step. This means we can run the algorithm


in _O_ ( _n_ [3] ) time instead of _O_ ( _n_ [4] ).


370


**Prop. 7.1**


_Proof._ The nilpotency of _C_ means that _C_ _[n]_ = 0. Then


_κc_ ( _I −_ _C_ ) =            - � _|_ ( _I −_ _C_ ) _−_ 1 _||I −_ _C|_            - � _∞_




- ���� _∞_



=


=




- ����



_n−_ 1

_I_ + 2 _C_ _[k]_

 
- ���� _k_ =1 - ���� _∞_




- - _[n][−]_ [1]




- _C_ _[k]_ [�] ( _I_ + _C_ )


_k_ =0



_≤_ 1 + 2




- ����



_n−_ 1

- _C_ _[k]_ _._

_k_ =1 - ���� _∞_



_n−_ 1




The second line follows because (1) ( _I −_ _C_ ) _[−]_ [1] is non-negative since _ρ_ ( _C_ ) = 0


because _C_ is nilpotent, (2) ( _I −_ _C_ ) _[−]_ [1] is equal to the Neumann series capped at


_n −_ 1 since _C_ is nilpotent, and (3) _C_ is non-negative with zero diagonals. The


fourth line follows from triangle inequality.


As _C_ is non-negative and nilpotent, it is the adjacency matrix of a directed


acyclic graph (DAG). Since _C_ is column sub-stochastic, all entries are in [0 _,_ 1].


Recall that the induced _L_ _[∞]_ norm of a matrix is equal to the maximum absolute


row sum.


We next show that each entry of the matrix [�] _[n]_ _k_ =1 _[−]_ [1] _[C]_ _[k]_ [ must be] _[ ≤]_ [1][. Note the]


following


  - Interpreting the matrix as a directed graph, all incoming edges to a node _j_


sum to _≤_ 1 because the matrix is column sub-stochastic.


  - The weight from a given path from _i_ to _j_ (i.e., the contribution of this path


to the ( _i, j_ ) entry of [�] _[n]_ _k_ =1 _[−]_ [1] _[C]_ _[k]_ [) is the product of edge weights along the]


path. This is _≤_ the weight of the final edge connecting to _j_, which follows


by a simple induction on the max length of paths.


371


6000


5000


4000


3000


2000


1000


0



𝜅(𝐼−𝐶ሻ for Random Trees


0 500 1000 1500 2000 2500 3000

_n_ = # nodes



Figure 7.11: Condition numbers of _I −_ _C_ for random trees _C_ achieve the bounds
in Prop. 7.1 and Cor. 7.1


Thus the sum along all paths from _i_ to _j_ is _≤_ the sum of all incoming edges to _j_,


which is _≤_ 1.


Let _i_ be an arbitrary row. There are _n −_ 1 possible nonzero entries in an



arbitrary row _i_ - f [�] _[n]_ _k_ =1 _[−]_ [1] _[C]_ _[k]_ [, each of which can be at most 1. Thus]


_n−_ 1

_C_ _[k]_ _≤_ _n −_ 1 _,_

     
                                                            - ���� _k_ =1                                                            - ���� _∞_



_n−_ 1

_C_ _[k]_ _≤_ _n −_ 1 _,_


_k_ =1 - ���� _∞_



_n−_ 1




and _κc_ ( _I −_ _C_ ) _≤_ 1 + 2( _n −_ 1).


The bound is tight as demonstrated by examples in Figure 7.11.


**Cor. 7.1**


_Proof._ For _A_ **x** = _b_ with _|δA| ≤_ _εE_, the component-wise relative condition num

ber is

_∥|A_ _[−]_ [1] _||E||_ **x** _|∥∞_
_κ_ _[∞]_ _c_ [(] _[A, E]_ [) = max] = _∥|A_ _[−]_ [1] _||E|∥∞._
**x** _∥_ **x** _∥∞_


372


Following the same steps as in Prop. 7.1, we have


_κ_ _[∞]_ _c_ [(] _[I][ −]_ _[C, C]_ [) =]          - � _|_ ( _I −_ _C_ ) _−_ 1 _||C|_          - � _∞_


_−_ 1
=           - �( _I −_ _C_ ) _C_           - � _∞_




- ���� _∞_



=


=




- ����

- ����




- - _[n][−]_ [1]



_n−_ 1

- _C_ _[k]_

_k_ =1 - ���� _∞_



_n−_ 1





- _C_ _[k]_ [�] _C_


_k_ =0



_≤_ _n −_ 1 _._


The bound is tight as demonstrated by examples in Figure 7.11.


**Prop. 7.2**


_Proof._ Let _A_ be the subsystem of _C_ _[q]_ with just _i, j_ nodes. Since entries are non

negative, the respective _i_ and _j_ row sums of [�] _[∞]_ _k_ =1 _[C]_ _[k]_ [ are] _[ ≥]_ [those of][ �] _[∞]_ _k_ =1 _[A][k]_ [.]


The latter matrix takes the form







_∞_

- _A_ _[k]_ =


_k_ =1









_k−_ 1 _k_ _k_ _k_

- _a_ _b_ - _a_ _b_



_k_ _k_ _k_ _k−_ 1

- _a_ _b_ - _a_ _b_






_._




Following from the geometric progression, the _i_ row sum of [�] _[∞]_ _k_ =1 _[A][k]_ [ is]



_∞_



_k_ =1



_∞_




1 _−_ _ab_ _[.]_



_a_ _[k]_ _b_ _[k]_ + _a_ _[k]_ _b_ _[k][−]_ [1][�] =




_∞_

- ( _ab_ ) _[k]_ +


_k_ =1


373




- _a_ ( _ab_ ) _[k]_ = _[a]_ 1 [(] _−_ _[b]_ [ + 1] _ab_ [)]

_k_ =0


We then have



_κc_ ( _I −_ _C_ ) = _∥|_ ( _I −_ _C_ ) _[−]_ [1] _||I −_ _C|∥∞_




- ���� _∞_



=


=




- ����



_I_ + 2

- ����



_∞_

- 



- _C_ _[k]_ [�] ( _I_ + _C_ )


_k_ =0



_∞_

- _C_ _[k]_

_k_ =1 - ���� _∞_



= 1 + 2 _·_ max row sum of



_∞_

- _C_ _[k]_


_k_ =1



_≥_ 1 + [2] _[a]_ [(] _[b]_ [ + 1][)]

1 _−_ _ab_ _[.]_


The second line follows because (1) ( _I −_ _C_ ) _[−]_ [1] is non-negative since _ρ_ ( _C_ ) _<_ 1, (2)


( _I −_ _C_ ) _[−]_ [1] is equal to the Neumann series, and (3) _C_ is non-negative with zero


diagonals.


**Prop. 7.3**


_Proof._

_κ_ [1] ( _I −_ _C_ ) = _∥_ ( _I −_ _C_ ) _∥_ 1         - �( _I −_ _C_ ) _−_ 1��1



_≤_ 1 + _∥C∥_ 1

 -  - [�]

                       - ���



_∞_

- _C_ _[k]_

_k_ =0 - ����1



_∞_




_∞_
_≤_ - 1 + _∥C∥_ 1� - _∥C∥_ 1 _[k]_

_i_ =0




_[∥][C][∥]_ [1]
= 1 [1 +] _−∥C∥_ 1 _._



The second line follows from the triangle inequality and the Neumann series,


which converges since _ρ_ ( _C_ ) _<_ 1. The third line follows from Tonelli’s Theorem


(since entries are non-negative) and properties of the norm. The fourth line


follows from the geometric progression since _∥C∥_ 1 _<_ 1.


374


**Prop. 7.4**


_Proof._ Notice that strict sub-stochasticity of _C_ is required for _C_ [ˆ] _[−]_ [1] to be well

defined.

ˆ _−_ 1
_κ_ [1][�] ( _I −_ _C_ ) _C_ [ˆ] _[−]_ [1][�] = _∥_ ( _I −_ _C_ ) _C_ [ˆ] _[−]_ [1] _∥_ 1 _C_ ( _I −_ _C_ )

                                                           - ��                                                           - ��1

_≤_          - ��( _I_ + _C_ ) ˆ _C_ _−_ 1���1


_≤∥I_ + _C∥_ 1 _∥C_ [ˆ] _[−]_ [1] _∥_ 1


_[∥][C][∥]_ [1]
= 1 [1 +] _−∥C∥_ 1 _._


The second line follows because _C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] is column stochastic (see e.g. [76])


and since _C_ is non-negative. The third line follows from sub-multiplicativity of


induced norms. The fourth line follows from the triangle inequality and because


the max column sum of _C_ [ˆ] is the reciprocal of 1 minus the max column sum of


_C_ .


**Theorem 7.1**


_Proof._ The graph represented by _C_ is acyclic if and only if _C_ is non-negative


nilpotent. Corollary 7.1 then gives that _κ_ _[∞]_ _c_ [(] _[I][ −]_ _[C, C]_ [)] _[ ≤]_ _[n][ −]_ [1][. The output error]


is then bounded as follows:


_∥_ **V** **[˜]** _−_ **V** _∥∞_ _≤_ _κc_ ( _I −_ _C, C_ ) _ε∥_ **V** _∥∞_


_≤_ _κ_ _[∞]_ _c_ [(] _[I][ −]_ _[C, C]_ [)] _[ε][∥]_ **[p]** _[∥]_ [1]


375


The last line follows because the acyclic nature of _C_ guarantees that _∥_ **V** _∥∞_ _≤_


_∥_ **p** _∥_ 1.


To compute market values, we then multiply **V** by _C_ [ˆ] . Error in this calcu

lation comes from error in **V**, as bounded above, and error in _C_ [ˆ], which comes


from error in _C_ . Given _|C_ [˜] _−_ _C| < ε|C|_, the error in each diagonal term of _C_ [ˆ] is at


most _ε∥C∥_ 1 ( _ε·_ the max column sum). The error in the multiplication **v** = _C_ [ˆ] **V** is


then bounded as


_∥_ **˜v** _−_ **v** _∥∞_ _≤_ _ε∥C∥_ 1 _∥_ **V** _∥∞_ + _κ_ _[∞]_ _c_ [(] _[I][ −]_ _[C, C]_ [)] _[ε][∥]_ **[V]** _[∥][∞][∥][C]_ [ˆ] _[∥][∞]_ [+] _[ κ][∞]_ _c_ [(] _[I][ −]_ _[C, C]_ [)] _[ε]_ [2] _[∥]_ **[V]** _[∥][∞][∥][C][∥]_ [1]


_≤_ _ε∥_ **p** _∥_ 1 + _ε_ ( _n −_ 1) _∥_ **p** _∥_ 1 + _ε_ [2] ( _n −_ 1) _∥_ **p** _∥_ 1


= _ε_ 1 + (1 + _ε_ )( _n −_ 1) _∥_ **p** _∥_ 1

     -      

_x_
The first line follows from the error in multiplying two uncertain numbers


˜˜
and _y_ : _|xy −_ _xy| ≤_ _δx|y|_ + _δy|x|_ + _δxδy_ . The second line follows from _∥C∥_ 1 _≤_ 1,


_∥C_ [ˆ] _∥∞_ _≤_ 1, and _∥_ **V** _∥∞_ _≤∥_ **p** _∥_ 1.


**Theorem 7.2**


_Proof._ We have _C_ [˜] = _C_ + _E_ for a suitable perturbation matrix _E_ . Then also

_C_ ˆ˜ = ˆ _C_ + ˆ _E_ describes the column sums of _E_ . Then


_C_ ˆ˜( _I −_ _C_ ˜) _−_ 1 _−_ _C_ ˆ( _I −_ _C_ ) _−_ 1 = ( ˆ _C_ + ˆ _E_ )( _I −_ _C_ ˜) _−_ 1 _−_ _C_ ˆ( _I −_ _C_ ) _−_ 1( _I −_ _C_ ˜)( _I −_ _C_ ˜) _−_ 1


= ( _C_ [ˆ] + _E_ [ˆ] ) _−_ _C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] ( _I −_ _C −_ _E_ ) ( _I −_ _C_ [˜] ) _[−]_ [1]

           -            

ˆ ˆ
= _C_ + ˆ _E −_ _C_ _I −_ ( _I −_ _C_ ) _[−]_ [1] _E_ ( _I −_ _C_ [˜] ) _[−]_ [1]

           -            -            - �


ˆ
= _E_ + ˆ _C_ ( _I −_ _C_ ) _[−]_ [1] _E_ ( _I −_ _C_ [˜] ) _[−]_ [1] _._

           -            

376


The first line follows from substitution and since ( _I −_ _C_ [˜] )( _I −_ _C_ [˜] ) _[−]_ [1] = _I_ . The


second line follows from substitution and distributive property.


Then noting that _∥E∥_ 1 = _∥E_ [ˆ] _∥_ 1 and _∥C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] _∥_ 1 = 1,


_∥_ **˜v** _−_ **v** _∥_ 1 = _∥_ ( _C_ [ˆ˜] ( _I −_ _C_ [˜] ) _[−]_ [1] _−_ _C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] ) _D_ **p** _∥_ 1


_≤∥_ ( _E_ [ˆ] + _C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] _E_ )( _I −_ _C_ [˜] ) _[−]_ [1] _∥_ 1 _∥D_ **p** _∥_ 1


_≤∥_ ( _I −_ _C_ [˜] ) _[−]_ [1] _∥_ 1 _∥E_ [ˆ] _∥_ 1 + _∥C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] _∥_ 1 _∥E∥_ 1 _∥D_ **p** _∥_ 1

             -             

1
= 2 _∥E∥_ 1 _._

1 _−∥C_ [ˆ] _∥_ 1


Alternatively, we also have


_∥_ **˜v** _−_ **v** _∥_ 1 _≤_ _∥C_ [ˆ˜] ( _I −_ _C_ [˜] ) _[−]_ [1] _∥_ 1 + _∥C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] _∥_ 1 _∥D_ **p** _∥_ 1 = 2 _∥D_ **p** _∥_ 1 _._

       -        

**Theorem 7.3**


_Proof._ We have the systems ( _I −C_ ) **V** = _D_ **p**, ( _I −C_ [¯] ) **V** **[¯]** = _D_ **p**, and ( _I −C_ [˜] ) **V** **[˜]** = _D_ **p**


with _|C_ [¯] _−_ _C| < εC_, _|C_ [˜] _−_ _C| < εC_, and _|C_ [˜] _−_ _C_ [¯] _| <_ 2 _εC_ . Consider _C_ and _C_ [˜] as


perturbations of _C_ [¯] . Then consider _κ_ := _κ_ _[∞]_ _c_ [(] _[I][ −]_ _[C, C]_ [¯] [) :=] _[ ∥|]_ [(] _[I][ −]_ _[C]_ [¯][)] _[−]_ [1] _[||][C][|∥][∞]_ [:]


¯ _−_ 1
_κ_ =         - � _|_ ( _I −_ _C_ ) _||C|_         - � _∞_


¯ _−_ 1
=       - �( _I −_ _C_ ) _|C_ ¯ + _δC|_       - � _∞_


_≤∥_ ( _I −_ _C_ [¯] ) _[−]_ [1][ ¯] _C∥∞_ + _∥_ ( _I −_ _C_ [¯] ) _[−]_ [1] _εC∥∞_


_≤_ _n −_ 1 + _εκ._


The second line follows because ( _I_ _−C_ [¯] ) _[−]_ [1] is non-negative. The third line follows


by triangle inequality and because _|δC| < εC_ . Thus _κ ≤_ _[n]_ 1 _−_ _[−]_ _ε_ [1] [by solving for] _[ κ]_ [.]


377


¯
Note that this bound on - � _|_ ( _I −_ _C_ ) _−_ 1 _||C|_ - � _∞_ [is not exactly a condition number, as]


it depends on _ε_, but it is still useful.


Applying _κ_ to analyze perturbations of _C_ [¯], we get


_εκ_
_∥_ **V** **[¯]** _−_ **V** _∥∞_ _≤_
1 _−_ _εκ_ _[∥]_ **[¯V]** _[∥][∞]_


_ε_ ( _n−_ 1)



=



1 _−ε_ _∥_ **V** **[¯]** _∥∞_
1 _−_ _[ε]_ [(] 1 _[n]_ _−_ _[−]_ _ε_ [1][)]



= _ε_ _[n][ −]_ [1]

1 _−_ _nε_ _[∥]_ **[¯V]** _[∥][∞]_



_≤_ _ε_ _[n][ −]_ [1]

1 _−_ _nε_ _[∥]_ **[p]** _[∥]_ [1] _[.]_



The first line follows from the bounds introduced in Section 7.4.1 noting that


_nε <_ 1 since _ε_ (2 _n −_ 1) _<_ 1. The final line follows since _∥_ **V** **[¯]** _∥∞_ _≤∥_ **p** _∥_ 1 since _C_ [¯] is


acyclic. Similarly, using 2 _ε_ instead of _ε_,


2 _εκ_
_∥_ **V** **[˜]** _−_ **V** **[¯]** _∥∞_ _≤_
1 _−_ 2 _εκ_ _[∥]_ **[¯V]** _[∥][∞]_


2 _ε_ ( _n−_ 1)



=



1 _−ε_ _∥_ **V** **[¯]** _∥∞_
1 _−_ [2] _[ε]_ 1 [(] _[n]_ _−_ _[−]_ _ε_ [1][)]



We then have



2( _n −_ 1)
= _ε_
1 _−_ (2 _n −_ 1) _ε_ _[∥]_ **[p]** _[∥]_ [1] _[.]_


_∥_ **V** **[˜]** _−_ **V** _∥∞_ = _∥_ ( **V** **[˜]** _−_ **V** **[¯]** ) _−_ ( **V** _−_ **V** **[¯]** ) _∥∞_


_≤∥_ **V** **[˜]** _−_ **V** **[¯]** _∥∞_ + _∥_ **V** _−_ **V** **[¯]** _∥∞_



_n −_ 1 2( _n −_ 1)
_≤_ _ε_

            - 1 _−_ _nε_ [+] 1 _−_ (2 _n −_ 1) _ε_


Following the steps from the Theorem 7.1 proof, we get



_∥_ **p** _∥_ 1 _._




_n −_ 1 2( _n −_ 1)
_∥_ **˜v** _−_ **v** _∥∞_ _≤_ _ε_ 1 + (1 + _ε_ )

     -      - 1 _−_ _nε_ [+] 1 _−_ (2 _n −_ 1) _ε_


378



_∥_ **p** _∥_ 1 _._

- �


**Theorem 7.4**


_Proof._ Considering the linear system ( _I_ _−C_ ) _C_ [ˆ] _[−]_ [1] **v** = _D_ **p** with **p** as the only input,


the relative component-wise condition number is



_κrel_ =


_≤_




- � _|C_ ˆ( _I −_ _C_ ) _−_ 1 _| · |D_ **p** _|_ - �

- - _∞_
_∥_ **v** _∥∞_


ˆ

- � _C_ ( _I −_ _C_ ) _−_ 1��

- - _∞_ _[∥][D]_ **[p]** _[∥][∞]_

_∥_ **v** _∥∞_



_≤_ _[n]_ 1 _[∥]_ **[p]** _[∥]_ [1]

_n_ _[∥]_ **[p]** _[∥]_ [1]



= _n_ [2] _._


The second line follows from non-negativity of _C_ [ˆ] ( _I_ _−C_ ) _[−]_ [1] and submultiplicativ

ity of induced matrix norms. The third line follows since (1) _C_ [ˆ] ( _I −_ _C_ ) _[−]_ [1] is non

negative column stochastic and so rows can sum to at most _n_, (2) _∥D_ **p** _∥∞_ _≤∥_ **p** _∥_ 1,


and (3) market values sum to _∥_ **p** _∥_ 1 and so the smallest possible maximum value


- f **v** is [1]

_n_ _[∥]_ **[p]** _[∥]_ [1][ (value equally spread across all nodes).]


The uncertainty in market values is then


_∥_ **˜v** _−_ **v** _∥∞_ _≤_ _κrelε∥_ **v** _∥∞_


_≤_ _εn_ [2] _∥_ **p** _∥_ 1 _._


**Prop. 7.5**


_Proof._ Let _κ_ = _κ_ _[∞]_ _c_ [(] _[I][ −]_ _[C, C]_ [)][. The uncertainty in] **[ V]** [ is bounded] _[ ∥]_ **[˜V]** _[ −]_ **[V]** _[∥][∞]_ _[≤]_

_κε∥_ **V** _∥∞._ The uncertainty in _C_ [ˆ] is bounded _∥C_ [˜ˆ] _−_ _C_ [ˆ] _∥∞_ _≤_ _ε∥C∥_ 1 _._ Then the uncer

379


tainty from the multiplication **v** = _C_ [ˆ] **V** is bounded


_∥_ **˜v** _−_ **v** _∥∞_ _≤_ _ε∥C∥_ 1 _κε∥_ **V** _∥∞_ + _∥C_ [ˆ] _∥∞κε∥_ **V** _∥∞_ + _ε∥C∥_ 1 _∥_ **V** _∥∞_


= _ε∥_ **V** _∥∞_ (1 + _κε_ ) _∥C∥_ 1 + _κ∥C_ [ˆ] _∥∞_ _._

           -            

**Prop. 7.6**


_Proof._ Consider the systems _A_ **x** = **b** and ( _A_ + _δA_ )( **x** + _**δ**_ **x** ) = **b** for _|δA| ≤_ _εE_ .


Then

**b** _−_ **b** = ( _A_ + _δA_ )( **x** + _**δ**_ **x** ) _−_ _A_ **x**


= _δA_ **x** + ( _A_ + _δA_ ) _**δ**_ **x**


= _δA_ ( **x** + _**δ**_ **x** ) + _A_ _**δ**_ **x** _._


Re-arranging terms, _**δ**_ **x** = _A_ _[−]_ [1] ( _−δA_ )( **x** + _**δ**_ **x** ). Then


_|_ _**δ**_ **x** _|_ =                  - � _A−_ 1( _−δA_ )( **x** + _**δ**_ **x** )��


_≤_        - � _A−_ 1�� ( _|δA|_ ( _|_ **x** _|_ + _|_ _**δ**_ **x** _|_ )


_≤_        - � _A−_ 1�� _εE_ ( _|_ **x** _|_ + _|_ _**δ**_ **x** _|_ )


_−_ 1 _−_ 1
= _ε_         - � _A_         - � _E|_ _**δ**_ **x** _|_ + _ε_         - � _A_         - � _E|_ **x** _|._


Re-arranging terms, we have ( _I −_ _ε |A_ _[−]_ [1] _| E_ ) _|_ _**δ**_ **x** _| ≤_ _ε |A_ _[−]_ [1] _| E|_ **x** _|_ . Supposing


( _I −_ _ε |A_ _[−]_ [1] _| E_ ) is nonsingular, we then have


_−_ 1 _−_ 1 _−_ 1
_|_ _**δ**_ **x** _| ≤_ _ε_                  - _I −_ _ε_                  - � _A_                  - � _E_                  -                  - � _A_                  - � _E|_ **x** _|._


In the case of a financial system, _A_ = _I −_ _C_, **b** = _D_ **p** _−_ _B_ _**β**_, and **x** = **V** . Since


_C_ is non-negative and _∥C∥_ 1 _<_ 1, we know that _A_ _[−]_ [1] is non-negative via the Neu

mann series; thus _|A_ _[−]_ [1] _|_ = _A_ _[−]_ [1] . We are given that ( _I −_ _ε|A_ _[−]_ [1] _|E_ ) is nonsingular.


380


Since _A_ _[−]_ [1] _E_ is also non-negative, ( _I −_ _ε|A_ _[−]_ [1] _|E_ ) _[−]_ [1] is additionally non-negative


via the Neumann series. Putting everything together, we have


_|_ _**δ**_ **V** _| ≤_ _ε_ ( _I −_ _εA_ _[−]_ [1] _E_ ) _[−]_ [1] _A_ _[−]_ [1] _E|_ **V** _|._


Next recall that **v** = _C_ [ˆ] **V** and note that _|δC_ [ˆ] _| ≤_ _εE_ [ˆ] . Then


_|_ _**δ**_ **v** _|_ = ( ˆ _C_ + _δ_ ˆ _C_ )( **V** + _**δ**_ **V** ) _−_ _C_ ˆ **V**

                                                           - ��                                                            - ��


ˆ
= _C_ _**δ**_ **V** + _δ_ ˆ _C_ ( **V** + _**δ**_ **V** )

                                                           - ��                                                            - ��


_≤_ _C_ [ˆ] _|_ _**δ**_ **V** _|_ + _εE_ [ˆ] ( _|_ **V** _|_ + _|_ _**δ**_ **V** _|_ ) _._


381


**BIBLIOGRAPHY**


[1] Daron Acemoglu, Vasco M Carvalho, Asuman Ozdaglar, and Alireza
Tahbaz-Salehi. The network origins of aggregate fluctuations. _Economet-_
_rica_, 80(5):1977–2016, 2012.


[2] Daron Acemoglu, Asuman Ozdaglar, and Alireza Tahbaz-Salehi. Systemic risk and stability in financial networks. _American Economic Review_,
105(2):564–608, 2015.


[3] Mitsutoshi Adachi, Matteo Cominetta, Christoph Kaufmann, Anton
van der Kraaij, et al. A regulatory and financial stability perspective on
global stablecoins. _Macroprudential Bulletin_, 10, 2020.


[4] Dohyun Ahn and Kyoung-Kuk Kim. Optimal intervention under stress
scenarios: A case of the korean financial system. _Operations Research Let-_
_ters_, 47(4):257–263, 2019.


[5] AIR Institute’s Certified Catastrophe Modeler Program. 2016 global mod[eled catastrophe losses. Nov. 2016. AIR Worldwide. Available at http:](http://airww.co/GlobalEP16)
[//airww.co/GlobalEP16.](http://airww.co/GlobalEP16)


[6] Nader Al-Naji, Josh Chen, and Lawrence Diao. Basis: A Price-Stable
Cryptocurrency with an Algorithmic Central Bank. 2017.


[7] Hamed Amini, Rama Cont, and Andreea Minca. Resilience to contagion
in financial networks. _Mathematical finance_, 26(2):329–365, 2016.


[8] Hamed Amini, Damir Filipovi´c, and Andreea Minca. Systemic risk and
central clearing counterparty design. _Swiss Finance Institute Research Paper_,
(13-34), 2015.


[9] Hamed Amini, Andreea Minca, and Agnes Sulem. Control of interbank
contagion under partial information. _SIAM Journal on Financial Mathemat-_
_ics_, 6(1):1195–1219, 2015.


[10] Hamed Amini, Andreea Minca, and Agn`es Sulem. Optimal equity infusions in interbank networks. _Journal of Financial stability_, 31:1–17, 2017.


[11] Guillermo Angeris and Tarun Chitra. Improved price oracles: Constant
function market makers. _arXiv preprint arXiv:2003.10001_, 2020.


382


[12] Guillermo Angeris, Hsien-Tang Kao, Rei Chiang, Charlie Noyes, and
Tarun Chitra. An analysis of uniswap markets. _arXiv preprint_
_arXiv:1911.03380_, 2019.


[13] Guillermo Angeris, Hsien-Tang Kao, Rei Chiang, Charlie Noyes, and
Tarun Chitra. An analysis of Uniswap markets. _Crypto Economic Systems_
_2020_, 2020.


[14] Sirio Aramonte, Fernando Avalos, et al. The recent distress in corporate
bond markets: cues from etfs. Technical report, Bank for International
Settlements, 2020.


[15] Yannick Armenti, St´ephane Cr´epey, Samuel Drapeau, and Antonis Papapantoleon. Multivariate shortfall risk allocation and systemic risk. _SIAM_
_Journal on Financial Mathematics_, 9(1):90–126, 2018.


[16] Kenneth Joseph Arrow. _Aspects of the theory of risk-bearing_ . Yrj¨o Jahnssonin
S¨a¨ati¨o, 1965.


[17] Raphael Auer and Rainer B¨ohme. The technology of retail central bank
digital currency. Technical report, BIS Quarterly Review, March, 2020.


[18] Raphael Auer, Bernhard Haslhofer, Stefan Kitzler, Pietro Saggese, and
Friedhelm Victor. The technology of decentralized finance (defi). 2023.


[19] Christoph Aymanns and J Doyne Farmer. The dynamics of the leverage
cycle. _Journal of Economic Dynamics and Control_, 50:155–179, 2015.


[20] Bruce A Babcock, E Kwan Choi, and Eli Feinerman. Risk and probability
premiums for cara utility functions. _Journal of Agricultural and Resource_
_Economics_, pages 17–24, 1993.


[21] A.D. Bain. Insurance spirals and the london market. _The Geneva Papers on_
_Risk and Insurance_, 24(2):228–242, 1999.


[22] Coralio Ballester, Antoni Calv´o-Armengol, and Yves Zenou. Who’s who
in networks. wanted: The key player. _Econometrica_, 74(5):1403–1417, 2006.


[23] Tathagata Banerjee, Alex Bernstein, and Zachary Feinstein. Dynamic clearing and contagion in financial networks. _arXiv preprint_
_arXiv:1801.02091_, 2018.


383


[24] Tathagata Banerjee and Zachary Feinstein. Impact of contingent payments on systemic risk in financial networks. _Mathematics and Financial_
_Economics_, 13:617–636, 2019.


[25] A. Baranga. The contraction principle as a particular case of kleene’s fixed
point theorem. _Discrete Mathematics_, 98:75–79, 1991.


[26] John Barrdear and Michael Kumhof. The macroeconomics of central bank
issued digital currencies. Technical report, Bank of England, 2016.


[27] Paolo Bartesaghi, Michele Benzi, Gian Paolo Clemente, Rosanna Grassi,
and Ernesto Estrada. Risk-dependent centrality in economic and financial
networks. _Forthcoming in SIAM J. on Financial Mathematics_, 2019.


[28] Stefano Battiston, Guido Caldarelli, Robert M May, Tarik Roukny, and
Joseph E Stiglitz. The price of complexity in financial networks. _Proceed-_
_ings of the National Academy of Sciences_, 113(36):10031–10036, 2016.


[29] Itzhak Ben-David, Francesco Franzoni, and Rabih Moussawi. Do etfs increase volatility? _The Journal of Finance_, 73(6):2471–2535, 2018.


[30] Benjamin Bernard, Agostino Capponi, and Joseph E Stiglitz. Bail-ins and
bail-outs: Incentives, connectivity, and systemic stability. Technical report,
National Bureau of Economic Research, 2017.


[31] D. Bertsekas. _Abstract Dynamic Programming_ . Athena Scientific, 2013.


[32] Francesca Biagini, Jean-Pierre Fouque, Marco Frittelli, and Thilo MeyerBrandis. A unified approach to systemic risk measures via acceptance
sets. _Mathematical Finance_, 29(1):329–367, 2019.


[33] Bruno Biais, Christophe Bisiere, Matthieu Bouvard, and Catherine
Casamatta. The blockchain folk theorem. _The Review of Financial Studies_,
32(5):1662–1715, 2019.


[34] J. Blanchet, J. Li, and Y. Shi. Stochastic risk networks: Modeling, analysis
and efficient monte carlo. _Working paper available on SSRN_, 2015.


[[35] Blockchain.com. The state of stablecoins. Technical report, https://ww](https://www.blockchain.com/ru/static/pdf/StablecoinsReportFinal.pdf)
[w.blockchain.com/ru/static/pdf/StablecoinsReportFina](https://www.blockchain.com/ru/static/pdf/StablecoinsReportFinal.pdf)
[l.pdf, 2019.](https://www.blockchain.com/ru/static/pdf/StablecoinsReportFinal.pdf)


384


[36] Blocknative. Evidence of mempool manipulation on black thursday:
Hammerbots, mempool compression, and spontaneous stuck transactions, 2020.


[37] Bloomberg. How $60 Billion in Terra Coins Went Up in Algorithmic
[Smoke. https://www.bloomberg.com/graphics/2022-crypt](https://www.bloomberg.com/graphics/2022-crypto-luna-terra-stablecoin-explainer/)

[o-luna-terra-stablecoin-explainer/, 20 May 2022.](https://www.bloomberg.com/graphics/2022-crypto-luna-terra-stablecoin-explainer/)


[38] Bloomberg. House stablecoin bill would put two-year ban on Terra-like
[coins. https://www.bloomberg.com/news/articles/2022-09-2](https://www.bloomberg.com/news/articles/2022-09-20/house-stablecoin-bill-would-put-two-year-ban-on-terra-like-coins?leadSource=uverify%20wall)
[0/house-stablecoin-bill-would-put-two-year-ban-on-ter](https://www.bloomberg.com/news/articles/2022-09-20/house-stablecoin-bill-would-put-two-year-ban-on-terra-like-coins?leadSource=uverify%20wall)
[ra-like-coins?leadSource=uverify%20wall, 20 Sep 2022.](https://www.bloomberg.com/news/articles/2022-09-20/house-stablecoin-bill-would-put-two-year-ban-on-terra-like-coins?leadSource=uverify%20wall)


[39] Taras Bodnar, Nestor Parolya, and Wolfgang Schmid. On the exact solution of the multi-period portfolio choice problem for an exponential utility under return predictability. _European Journal of Operational Research_,
246(2):528 – 542, 2015.


[40] Stephen Boyd and Lieven Vandenberghe. _Convex optimization_ . Cambridge
university press, 2009.


[41] Anton Braverman and Andreea Minca. Networks of common asset holdings: aggregation and measures of vulnerability. _The Journal of Network_
_Theory in Finance_, 4(3), 2018.


[42] Philip N Brown. Incentives for crypto-collateralized digital assets. In _Pro-_
_ceedings of the 3rd Annual Decentralized Conference on Blockchain and Cryp-_
_tocurrency_, volume 28, page 2, 2019.


[43] Vitalik Buertin. Collateralized debt obligations for issuer-backed tokens.
[https://ethresear.ch/t/collateralized-debt-obligatio](https://ethresear.ch/t/collateralized-debt-obligations-for-issuer-backed-tokens/525)
[ns-for-issuer-backed-tokens/525, Jan. 2018.](https://ethresear.ch/t/collateralized-debt-obligations-for-issuer-backed-tokens/525)


[44] Dirk Bullmann, Jonas Klemm, and Andrea Pinna. In search for stability in
crypto-assets: Are stablecoins the solution? _ECB Occasional Paper_, (230),
2019.


[45] Donald L Burkholder. Distribution function inequalities for martingales.
_the Annals of Probability_, pages 19–42, 1973.


[46] Y Cao, M Dai, S Kou, L Li, and C Yang. Designing stable coins. _Available_
_[at SSRN: https://ssrn.com/abstract=3856569](https://ssrn.com/abstract=3856569)_, 2021.


385


[47] Agostino Capponi and Peng-Chu Chen. Systemic risk mitigation in financial networks. _Journal of Economic Dynamics and Control_, 58:152–166,
2015.


[48] Agostino Capponi, W Cheng, and Jay Sethuraman. Clearinghouse default waterfalls: Risk-sharing, incentives, and systemic risk. _Incentives,_
_and Systemic Risk (August 30, 2017)_, 2017.


[49] Hans Carlsson and Eric Van Damme. Global games and equilibrium selection. _Econometrica: Journal of the Econometric Society_, pages 989–1018,
1993.


[50] Miles Carlsten, Harry Kalodner, Arvind Narayanan, and S. Matthew
Weinberg. On the instability of Bitcoin without the block reward. In _Pro-_
_ceedings of the ACM Conference on Computer and Communications Security_,
volume 24-28-Octo, pages 154–167, 2016.


[51] Chen Chen, Garud Iyengar, and Ciamac C. Moallemi. An axiomatic approach to systemic risk. _Management Science_, 59(6):1373–1388, 2013.


[52] Nan Chen, Xin Liu, and David Yao. An optimization view of financial
systemic risk modeling: Network effect and market liquidity effect. _Oper-_
_ations Research_, 64(5):1089–1108, 2016.


[53] Xi Chen, Christos Papadimitriou, and Tim Roughgarden. An Axiomatic
Approach to Block Rewards. pages 124–131, 2019.


[54] Tarun Chitra. Competitive equilibria between staking and on-chain lending. _Crypto Economic Systems 2020_, 2020.


[55] cLabs. An analysis of the stability characteristics of celo. Technical report,
[https://celo.org/papers/Celo_Stability_Analysis.pdf,](https://celo.org/papers/Celo_Stability_Analysis.pdf)
2019.


[56] Coindesk. MakerDAO adds USDC as DeFi collateral following ‘Black
[Thursday’ chaos. https://www.coindesk.com/makerdao-add](https://www.coindesk.com/makerdao-adds-usdc-as-defi-collateral-following-black-thursday-chaos)
[s-usdc-as-defi-collateral-following-black-thursday-c](https://www.coindesk.com/makerdao-adds-usdc-as-defi-collateral-following-black-thursday-chaos)
[haos, 17 Mar. 2020.](https://www.coindesk.com/makerdao-adds-usdc-as-defi-collateral-following-black-thursday-chaos)


[[57] Coindesk. Bitfinex repays tether $100 million of $700 million loan. http](https://www.coindesk.com/bitfinex-repays-tether-100-million-of-700-million-loan)
[s://www.coindesk.com/bitfinex-repays-tether-100-milli](https://www.coindesk.com/bitfinex-repays-tether-100-million-of-700-million-loan)

[on-of-700-million-loan, Jul. 2019.](https://www.coindesk.com/bitfinex-repays-tether-100-million-of-700-million-loan)


386


[58] Cointelegraph. Fractional reserve stablecoin tether only 74% backed by
[fiat currency, say lawyers. https://cointelegraph.com/news/fra](https://cointelegraph.com/news/fractional-reserve-stablecoin-tether-only-74-backed-by-fiat-currency-say-lawyers)
[ctional-reserve-stablecoin-tether-only-74-backed-by-f](https://cointelegraph.com/news/fractional-reserve-stablecoin-tether-only-74-backed-by-fiat-currency-say-lawyers)
[iat-currency-say-lawyers, Apr. 2019.](https://cointelegraph.com/news/fractional-reserve-stablecoin-tether-only-74-backed-by-fiat-currency-say-lawyers)


[59] Cointelegraph. Crypto exchange bitfinex suspends fiat deposits, expects
[to resume ‘within a week’. https://cointelegraph.com/news/c](https://cointelegraph.com/news/crypto-exchange-bitfinex-suspends-fiat-deposits-expects-to-resume-within-a-week)
[rypto-exchange-bitfinex-suspends-fiat-deposits-expec](https://cointelegraph.com/news/crypto-exchange-bitfinex-suspends-fiat-deposits-expects-to-resume-within-a-week)
[ts-to-resume-within-a-week, Oct. 2018.](https://cointelegraph.com/news/crypto-exchange-bitfinex-suspends-fiat-deposits-expects-to-resume-within-a-week)


[[60] Compound. Compound:the money market protocol. https://compou](https://compound.finance/documents/Compound.Whitepaper.pdf)
[nd.finance/documents/Compound.Whitepaper.pdf, 2019.](https://compound.finance/documents/Compound.Whitepaper.pdf)


[61] Gerard Cornuejols, Marshall L. Fisher, and George L. Nemhauser. Location of bank accounts to optimize float: An analytic study of exact and
approximate algorithms. _Management Science_, 23(8):789–810, 1977.


[62] B Craig and G. Von Peter. Interbank tiering and money center banks.
_Journal of Financial Intermediation_, 23(3):322–347, 2014.


[63] Felipe Cucker. Probabilistic analyses of condition numbers. _Acta Numer-_
_ica_, 25:321–382, 2016.


[64] Philip Daian, Steven Goldfeder, Tyler Kell, Yunqi Li, Xueyuan Zhao, Iddo
Bentov, Lorenz Breidenbach, and Ari Juels. Flash boys 2.0: Frontrunning
in decentralized exchanges, miner extractable value, and consensus instability. In _2020 IEEE Symposium on Security and Privacy (SP)_, pages 566–583.


[65] St´ephane Dees and J´erˆome Henry. Stress-test analytics for macropruden
A
tial purposes: Introducing stampC. _Satellite Models_, 13, 2017.


[66] Erik D Demaine, MohammadTaghi Hajiaghayi, Hamid Mahini, David L
Malec, S Raghavan, Anshul Sawant, and Morteza Zadimoghadam. How
to influence people with partial incentives. In _Proceedings of the 23rd inter-_
_national conference on World wide web_, pages 937–948, 2014.


[67] James W Demmel. _Applied numerical linear algebra_ . SIAM, 1997.


[68] Nils Detering, Thilo Meyer-Brandis, Konstantinos Panagiotou, and Daniel
Ritter. Managing default contagion in inhomogeneous financial networks.
_SIAM Journal on Financial Mathematics_, 10(2):578–614, 2019.


387


[[69] C. Detrio. Smart markets for stablecoins. Technical report, http://cdet](http://cdetr.io/smart-markets/)
[r.io/smart-markets/, 2015.](http://cdetr.io/smart-markets/)


[70] Douglas W Diamond and Philip H Dybvig. Bank runs, deposit insurance,
and liquidity. _Journal of political economy_, 91(3):401–419, 1983.


[71] Pedro Domingos and Matt Richardson. Mining the network value of customers. In _Proceedings of the seventh ACM SIGKDD international conference_

_on Knowledge discovery and data mining_, pages 57–66, 2001.


[72] Yuhao Dong and Raouf Boutaba. Melmint: trustless stable cryptocurrency. In _Cryptoeconomic Systems 2020_, 2020.


[73] Darrell Duffie, Martin Scheicher, and Guillaume Vuillemey. Central clearing and collateral demand. _Journal of Financial Economics_, 116(2):237–256,
2015.


[74] Philip H Dybvig and Jaime F Zender. Capital structure and dividend
irrelevance with asymmetric information. _The Review of Financial Studies_,
4(1):201–219, 1991.


[75] Larry Eisenberg and Thomas H Noe. Systemic risk in financial systems.
_Management Science_, 47(2):236–249, 2001.


[76] Matthew Elliott, Benjamin Golub, and Matthew O Jackson. Financial networks and contagion. _American Economic Review_, 104(10):3115–53, 2014.


[77] Steve Ellis, Ari Juels, and Sergey Nazarov. Chainlink: A decentralized

[oracle network. https://link.smartcontract.com/whitepaper,](https://link.smartcontract.com/whitepaper)
Sep. 4, 2017.


[78] Alex Evans. A Ratings-Based Model for Credit Events in MakerDAO,
2019.


[79] Ittay Eyal and Emin G¨un Sirer. Majority is not enough: Bitcoin mining is
vulnerable. _Commun. ACM_, 61(7):95–102, June 2018.


[80] Zachary Feinstein, Weijie Pang, Birgit Rudloff, Eric Schaanning, Stephan
Sturm, and Mackenzie Wildman. Sensitivity of the eisenberg–noe clearing vector to individual interbank liabilities. _SIAM Journal on Financial_
_Mathematics_, 9(4):1286–1325, 2018.


388


[81] Zachary Feinstein, Birgit Rudloff, and Stefan Weber. Measures of systemic
risk. _SIAM Journal on Financial Mathematics_, 8(1):672–708, 2017.


[82] Andrea Galeotti and Sanjeev Goyal. Influencing the influencers: a theory

   - f strategic diffusion. _The RAND Journal of Economics_, 40(3):509–532, 2009.


[83] Juan Garay, Aggelos Kiayias, and Nikos Leonardos. The bitcoin backbone protocol: Analysis and applications. In _Advances in Cryptology-_
_EUROCRYPT 2015: 34th Annual International Conference on the Theory and_
_Applications of Cryptographic Techniques, Sofia, Bulgaria, April 26-30, 2015,_
_Proceedings, Part II_, pages 281–310. Springer, 2015.


[84] Eiland Glover and John Reitano. The kowala protocol: a family of distributed, self-regulating, asset-tracking cryptocurrencies. 2018.


[85] Itay Goldstein and Ady Pauzner. Demand–deposit contracts and the
probability of bank runs. _the Journal of Finance_, 60(3):1293–1327, 2005.


[86] Jonathan Goodwin. A free money miracle. _Mises Daily_, 2013.


[87] John M Griffin and Amin Shams. Is bitcoin really un-tethered? _Available_
_at SSRN 3195066_, 2019.


[88] Lewis Gudgeon, Daniel Perez, Dominik Harz, Benjamin Livshits, and
Arthur Gervais. The decentralized financial crisis. In _2020 crypto valley_
_conference on blockchain technology (CVCBT)_, pages 1–15. IEEE, 2020.


[89] Bernardo Guimaraes and Stephen Morris. Risk and wealth in a model of
self-fulfilling currency attacks. _Journal of Monetary Economics_, 54(8):2205–
2230, 2007.


[90] Dilek G¨unnec¸, S. Raghavan, and Rui Zhang. Least-cost influence maximization on social networks. _INFORMS Journal on Computing_, 32(2):289–
302, 2020.


[91] Dominik Harz, Lewis Gudgeon, Arthur Gervais, and William J. Knottenbelt. Balance: Dynamic Adjustment of Cryptocurrency Deposits. In _Pro-_
_ceedings of the 2019 ACM SIGSAC Conference on Computer and Communica-_
_tions Security (CCS ’19)_ . ACM, 2019.


[92] Zhiguo He and Wei Xiong. Rollover risk and credit risk. _The Journal of_
_Finance_, 67(2):391–430, 2012.


389


[93] Brett Hemenway and Sanjeev Khanna. Sensitivity and computational
complexity in financial networks. _Algorithmic Finance_, 5(3-4):95–110, 2016.


[94] Nicholas J Higham. _Accuracy and stability of numerical algorithms_ . SIAM,
2002.


[95] Lucy Huo, Ariah Klages-Mundt, Andreea Minca, Frederik Christian
M¨unter, and Mads Rude Wind. Decentralized governance of stablecoins
with closed form valuation. In _Mathematical Research for Blockchain Econ-_

_omy_, 2022.


[96] Huobi. Announcement on the launch of husd solution on huobi global.
[https://huobiglobal.zendesk.com/hc/en-us/articles/360](https://huobiglobal.zendesk.com/hc/en-us/articles/360000170601)
[000170601, 19 Oct. 2018.](https://huobiglobal.zendesk.com/hc/en-us/articles/360000170601)


[97] D. Ingram. How much capital should an insurer hold. Jun. 2016. Willis
[Towers Watson Wire. Available at https://blog.willis.com/2016](https://blog.willis.com/2016/06/how-much-capital-should-an-insurer-hold/)
[/06/how-much-capital-should-an-insurer-hold/.](https://blog.willis.com/2016/06/how-much-capital-should-an-insurer-hold/)


[98] Marcin Kacperczyk and Philipp Schnabl. How safe are money market
funds? _The Quarterly Journal of Economics_, 128(3):1073–1122, 2013.


[99] Izabella Kaminska. The curious case of etf nav deviations. Financial
Times, Mar. 12, 2009.


[100] Hsien-Tang Kao, Tarun Chitra, Rei Chiang, and John Morrow. An Analysis of the Market Risk to Participants in the Compound Protocol. 2020.


[101] David Kempe, Jon Kleinberg, and Eva Tardos. Maximizing the spread

   - f influence through a social network. In _Proceedings of the ninth ACM_
_SIGKDD international conference on Knowledge discovery and data mining_,
pages 137–146, 2003.


[102] David Kempe, Jon Kleinberg, and Eva Tardos. Influential nodes in a dif- [´]
fusion model for social networks. In _International Colloquium on Automata,_
_Languages, and Programming_, pages 1127–1138. Springer, 2005.


[[103] Ariah Klages-Mundt. The state of stablecoins–update 2018. https://li](https://link.medium.com/8rZUYg1c16)
[nk.medium.com/8rZUYg1c16, 14 Dec. 2018.](https://link.medium.com/8rZUYg1c16)


[104] Ariah Klages-Mundt. Proposal: a framework for designing better stable

390


[coins. https://github.com/aklamun/Stablecoin_grant_prop](https://github.com/aklamun/Stablecoin_grant_proposal_122018)

[osal_122018, 2018.](https://github.com/aklamun/Stablecoin_grant_proposal_122018)


[[105] Ariah Klages-Mundt. Insights from modeling stablecoins. https://li](https://link.medium.com/FLOZ5dbd16)
[nk.medium.com/FLOZ5dbd16, 6 Apr. 2020.](https://link.medium.com/FLOZ5dbd16)


[[106] Ariah Klages-Mundt. Basis/basecoin is a bob rubin trade. https://li](https://link.medium.com/lKjfepv1r9)
[nk.medium.com/lKjfepv1r9, Aug. 23, 2018.](https://link.medium.com/lKjfepv1r9)


[107] Ariah Klages-Mundt. Vulnerabilities in Maker: oracle-governance at[tacks, attack DAOs, and (de)centralization. https://link.medium.](https://link.medium.com/VZG64fhmr6)
[com/VZG64fhmr6, Nov. 14, 2019.](https://link.medium.com/VZG64fhmr6)


[108] Ariah Klages-Mundt, Austin Benson, and Andreea Minca. Cascading
risks and sensitivity in economic networks. _Submitted_, 2023.


[109] Ariah Klages-Mundt, Lewis Gudgeon, and Daniel Perez. Rainy day fund
[stablecoin. https://www.initc3.org/events/2020-07-26-IC3](https://www.initc3.org/events/2020-07-26-IC3-Blockchain-Camp.html)

[-Blockchain-Camp.html, 2020.](https://www.initc3.org/events/2020-07-26-IC3-Blockchain-Camp.html)


[110] Ariah Klages-Mundt, Dominik Harz, Lewis Gudgeon, Jun-You Liu, and
Andreea Minca. Stablecoins 2.0: Economic foundations and risk-based
models. In _Proceedings of the 2nd ACM Conference on Advances in Financial_
_Technologies_, pages 59–79, 2020.


[111] Ariah Klages-Mundt and Andreea Minca. Cascading losses in reinsurance
networks. _Management Science_, 66(9):4246–4268, 2020.


[112] Ariah Klages-Mundt and Andreea Minca. (in) stability for the blockchain:
Deleveraging spirals and stablecoin attacks. _Cryptoeconomic Systems_, 1(2),
2021.


[113] Ariah Klages-Mundt and Andreea Minca. Optimal intervention in economic networks using influence maximization methods. _European Journal_

_of Operational Research_, 300(3):1136–1148, 2022.


[114] Ariah Klages-Mundt and Andreea Minca. While stability lasts: A stochastic model of noncustodial stablecoins. _Mathematical Finance_, 32(4):943–981,
2022.


[115] Ariah Klages-Mundt and Steffen Schuldenzucker. Design of the gy

391


roscope consolidated price feed and circuit breaker system. [https:](https://t.co/4BBXYPWTU7)
[//t.co/4BBXYPWTU7, 2022.](https://t.co/4BBXYPWTU7)


[116] Ariah Klages-Mundt and Steffen Schuldenzucker. Designing autonomous
markets for stablecoin monetary policy. _arXiv preprint arXiv:2212.12398_,
2022.


[117] O. Kley, C. Kl¨uppelberg, and G. Reinert. Risk in a large claims insurance
market with bipartite graph structure. _Operations Research_, 64(5):1159–
1176, 2016.


[118] Artur Kotlicki, Andrea Austin, David Humphry, Hanna Burnett, Philip
Ridgill, and Sam Smith. Network analysis of the uk reinsurance market.
Technical report, Bank of England, 2023.


[119] Michael Kusnetsov and Luitgard Veraart. Interbank clearing in financial
networks with multiple maturities. _SIAM Journal on Financial Mathematics_,
10(1):37–67, 2019.


[120] Jordan Lee. Nubits. 2014.


[121] Matteo Leibowitz. Addressing popular makerdao criticisms. The Block,
12 Sep 2019.


[122] Alex Lipton, Thomas Hardjono, and Alex Pentland. Digital trade
coin: towards a more stable digital currency. _Royal Society open science_,
5(7):180155, 2018.


[123] Alexander Lipton, Aetienne Sardon, Fabian Sch¨ar, and Christian
Sch¨upbach. 10. stablecoins, digital currency, and the future

   - f money. In _Building_ _the_ _New_ _Economy_ . 0 edition, 4 2020.
https://wip.mitpress.mit.edu/pub/17h9tjq7.


[[124] Liquity. Stability pool and liquidations. https://docs.liquity.org](https://docs.liquity.org/faq/stability-pool-and-liquidations)
[/faq/stability-pool-and-liquidations, 2020.](https://docs.liquity.org/faq/stability-pool-and-liquidations)


[125] Ming Liu and Jeremy Staum. Sensitivity analysis of the eisenberg–noe
model of contagion. _Operations Research Letters_, 38(5):489–491, 2010.


[126] Jacques Longerstaey. Riskmetrics—technical document. Technical report,
J.P. Morgan., 1996.


392


[127] Loi Luu. PeaceRelay: Connecting the many Ethereum Blockchains. 2017.


[128] Loi Luu. BTC Parachain Specification: Staked Relayers. 2020.


[129] Richard K Lyons and Ganesh Viswanath-Natraj. What keeps stablecoins
stable? Technical report, National Bureau of Economic Research, 2020.


[[130] MakerDAO. Black thursday response thread. https://forum.make](https://forum.makerdao.com/t/black-thursday-response-thread/1433)
[rdao.com/t/black-thursday-response-thread/1433, 12 Mar](https://forum.makerdao.com/t/black-thursday-response-thread/1433)
2020.


[[131] MakerDAO. The Dai stablecoin system whitepaper. https://makerd](https://makerdao.com/whitepaper/DaiDec17WP.pdf)
[ao.com/whitepaper/DaiDec17WP.pdf, 2017.](https://makerdao.com/whitepaper/DaiDec17WP.pdf)


[132] MakerDAO. The maker protocol: Makerdao’s multi-collateral dai (mcd)
[system. https://docs.makerdao.com/, 2019.](https://docs.makerdao.com/)


[133] MakerDAO. Awesome makerdao, 2020.


[[134] MakerDAO. Makerdao. https://makerdao.com/en/, 2020.](https://makerdao.com/en/)


[[135] MakerDAO. Makerdao graphql api. https://developer.makerdao](https://developer.makerdao.com/dai/1/graphql/)
[.com/dai/1/graphql/, 2020.](https://developer.makerdao.com/dai/1/graphql/)


[[136] MakerDAO. MIP29 - peg stability module. https://forum.makerdao](https://forum.makerdao.com/t/mip29-peg-stability-module/5071)
[.com/t/mip29-peg-stability-module/5071, Nov. 2020.](https://forum.makerdao.com/t/mip29-peg-stability-module/5071)


[137] Semyon Malamud. A dynamic equilibrium model of etfs. 2016.


[138] Andreu Mas-Colell, Michael Dennis Whinston, Jerry R Green, et al. _Mi-_
_croeconomic theory_, volume 1. Oxford university press New York, 1995.


[139] Patrick McCorry, Alexander Hicks, and Sarah Meiklejohn. Smart Contracts for Bribing Miners. In _Financial Cryptography and Data Security. FC_
_2018._, volume 10958, pages 3–18. Springer Berlin Heidelberg, 2018.


[140] Michael McLeay, Amar Radia, and Ryland Thomas. Money creation in
the modern economy. _Bank of England Quarterly Bulletin_, page Q1, 2014.


[[141] Meter. Meter whitepaper. https://www.meter.io/, 2020.](https://www.meter.io/)


393


[142] Andreea Minca and Johannes Wissel. Dynamic leveraging–deleveraging
games. _Operations Research_, 68(1):93–114, 2020.


[143] Makiko Mita, Kensuke Ito, Shohei Ohsawa, and Hideyuki Tanaka. What
is stablecoin?: A survey on price stabilization mechanisms for decentralized payment systems. _arXiv preprint arXiv:1906.06037_, 2019.


[144] Stephen Morris and Hyun Song Shin. Unique equilibrium in a model of
self-fulfilling currency attacks. _American Economic Review_, pages 587–597,
1998.


[145] Stephen Morris and Hyun Song Shin. Global Games: Theory and Applications. Cowles Foundation Discussion Papers 1275R, Cowles Foundation
for Research in Economics, Yale University, September 2000.


[146] Elchanan Mossel and Sebastien Roch. On the submodularity of influence
in social networks. In _Proceedings of the thirty-ninth annual ACM symposium_

_on Theory of computing_, pages 128–134, 2007.


[[147] Nexus Mutual. A decentralized alternative to insurance. https://nexu](https://nexusmutual.io/)
[smutual.io/, 2020.](https://nexusmutual.io/)


[148] Stewart C Myers and Nicholas S Majluf. Corporate financing and investment decisions when firms have information that investors do not have.
_Journal of Financial Economics_, 13(2):187–221, 1984.


[149] NAIC. Reinsurance data. 2018. National Association of Insurance Com[missioners. Available at http://www.naic.org/prod_serv_idp_r](http://www.naic.org/prod_serv_idp_reinsurance.htm)

[einsurance.htm.](http://www.naic.org/prod_serv_idp_reinsurance.htm)


[150] Satoshi Nakamoto. Bitcoin: A peer-to-peer electronic cash system. Tech[nical report, https://bitcoin.org/bitcoin.pdf, 2009.](https://bitcoin.org/bitcoin.pdf)


[151] George L Nemhauser, Laurence A Wolsey, and Marshall L Fisher. An
analysis of approximations for maximizing submodular set functions-i.
_Mathematical programming_, 14(1):265–294, 1978.


[152] Jeremy Ney and Nicolas Xuan-Yi Zhang. Central bank digital currencies
and the long-term advancement of financial stability. In _Cryptoeconomic_
_Systems 2020_, 2020.


394


[153] OFR Viewpoint. Size alone is not sufficient to identify systemically important banks. Technical report, Office of Financial Research, 2017.


[154] Maureen O’hara. _Market microstructure theory_ . Wiley, 1997.


[[155] Opyn. Opyn protection. https://opyn.co/, 2020.](https://opyn.co/)


[156] Cecilia Parlatore. Fragility in money market funds: Sponsor support and
regulation. _Journal of Financial Economics_, 121(3):595–623, 2016.


[157] PeckShield. bZx Hack Full Disclosure (With Detailed Profit Analysis).
[https://link.medium.com/LlXArFK7e7, Feb. 2020.](https://link.medium.com/LlXArFK7e7)


[158] PeckShield. bZx Hack II Full Disclosure (With Detailed Profit Analysis).
[https://link.medium.com/9K9LrFQ7e7, Feb. 2020.](https://link.medium.com/9K9LrFQ7e7)


[159] Ingolf GA Pernice, Sebastian Henningsen, Roman Proskalovich, Martin
Florian, Hermann Elendner, and Bj¨orn Scheuermann. Monetary stabilization in cryptocurrencies–design approaches and open questions. In _2019_
_Crypto Valley Conference on Blockchain Technology (CVCBT)_, pages 47–59.
IEEE, 2019.


[160] Nicholas Platias and Marco DiMaggio. Terra money: stability stress test.
[Technical report, https://agora.terra.money/t/stability-str](https://agora.terra.money/t/stability-stress-test/55)
[ess-test/55, 2019.](https://agora.terra.money/t/stability-stress-test/55)


[161] John W Pratt. Risk aversion in the small and in the large. In _Uncertainty_
_in Economics_, pages 59–79. Elsevier, 1978.


[[162] Reflexer. Rai. https://reflexer.finance/, 2020.](https://reflexer.finance/)


[163] J. Rennison, P. Stafford, C. Smith, and R. Wigglesworth. ‘great liquidity
crisis’ grips system as banks step back. Financial Times, Mar. 23, 2020.


[164] Jean-Charles Rochet and Xavier Vives. Coordination failures and the
lender of last resort: was bagehot right after all? _Journal of the European_
_Economic Association_, 2(6):1116–1147, 2004.


[165] Leonard CG Rogers and Luitgard Veraart. Failure and rescue in an interbank network. _Management Science_, 59(4):882–898, 2013.


395


[[166] Kenny Rowe. https://twitter.com/kennyrowe/status/10986](https://twitter.com/kennyrowe/status/1098639092332412929)
[39092332412929, 21 Feb 2019.](https://twitter.com/kennyrowe/status/1098639092332412929)


[167] G. Samman and A. Masanto. The state of stablecoins. Technical report,
[Reserve, https://reserve.org/stablecoin-report, 2019.](https://reserve.org/stablecoin-report)


[168] Robert Sams. A Note on Cryptocurrency Stabilisation: Seigniorage
Shares. 2015.


[169] L. Schiffer. Reinsurance arbitration–a primer. Jun. 2006. International Risk
[Management Institute, Inc. Available at https://www.irmi.com/art](https://www.irmi.com/articles/expert-commentary/reinsurance-arbitration-a-primer)
[icles/expert-commentary/reinsurance-arbitration-a-pri](https://www.irmi.com/articles/expert-commentary/reinsurance-arbitration-a-primer)

[mer.](https://www.irmi.com/articles/expert-commentary/reinsurance-arbitration-a-primer)


[170] Steffen Schuldenzucker, Sven Seuken, and Stefano Battiston. Clearing
payments in financial networks with credit default swaps. In _Proceedings_

_of the 2016 ACM Conference on Economics and Computation_, pages 759–759,
2016.


[171] Steffen Schuldenzucker, Sven Seuken, and Stefano Battiston. Finding
clearing payments in financial networks with credit default swaps is
ppad-complete. _LIPIcs: Leibniz International Proceedings in Informatics_, (67),
2017.


[172] Steffen Schuldenzucker, Sven Seuken, and Stefano Battiston. Default ambiguity: Credit default swaps create new systemic risks in financial networks. _Management Science_, 66(5):1981–1998, 2020.


[173] Chuen-Teck See and Jeremy Chen. Inequalities on the variances of convex
functions of random variables. _Journal of inequalities in pure and applied_
_mathematics_, 9(3):1–5, 2008.


[174] Raghu Nandan Sengupta, Aparna Gupta, and Joydeep Dutta. _Decision_
_sciences: theory and practice_ . Crc Press, 2016.


[[175] Synthetix. Addressing claims of deleted balances. https://blog.syn](https://blog.synthetix.io/addressing-claims-of-deleted-balances/)
[thetix.io/addressing-claims-of-deleted-balances/, 16](https://blog.synthetix.io/addressing-claims-of-deleted-balances/)
Sep. 2019.


[[176] Synthetix. Synthetix Response to Oracle Incident. https://blog.syn](https://blog.synthetix.io/response-to-oracle-incident/)
[thetix.io/response-to-oracle-incident/, Jun. 2019.](https://blog.synthetix.io/response-to-oracle-incident/)


396


[177] Synthetix. tBTC: a decentralized redeemable BTC-backed ERC-20 token.
[https://docs.keep.network/tbtc, Mar. 2020.](https://docs.keep.network/tbtc)


[[178] Terra Research. Increasing Robustness of the Terra Oracle. https://ag](https://agora.terra.money/t/increasing-robustness-of-the-terra-oracle/82)

[ora.terra.money/t/increasing-robustness-of-the-terra](https://agora.terra.money/t/increasing-robustness-of-the-terra-oracle/82)

[-oracle/82, Jul. 2019.](https://agora.terra.money/t/increasing-robustness-of-the-terra-oracle/82)


[179] The Actuary. Return on equity. Jun. 2004. The magazine of the Institute
[& Faculty of Actuaries. Available at http://www.theactuary.com/a](http://www.theactuary.com/archive/old-articles/part-5/return-on-equity/)
[rchive/old-articles/part-5/return-on-equity/.](http://www.theactuary.com/archive/old-articles/part-5/return-on-equity/)


[180] Sargent Thomas. Macroeconomic theory, 1987.


[181] Marcel P Timmer, Erik Dietzenbacher, Bart Los, Robert Stehrer, and
Gaaitzen J De Vries. An illustrated user guide to the world input–output
database: the case of global automotive production. _Review of International_
_Economics_, 23(3):575–605, 2015.


[182] Frank Topbottom. Black Thursday for MakerDAO: $8.32 million was liquidated for 0 DAI, 2020.


[183] Itay Tsabary and Ittay Eyal. The Gap Game. In _Proceedings of the 2018_
_ACM SIGSAC Conference on Computer and Communications Security - CCS_
_’18_, pages 713–728, New York, New York, USA, 2018. ACM Press.


[184] Luitgard Veraart. Distress and default contagion in financial networks.
_Mathematical Finance_, 2020.


[186] Gavin Wood. Ethereum: A secure decentralised generalised transaction
ledger. Technical report, Ethereum project yellow paper, 2014.


[187] Zhimeng Yang, Ariah Klages-Mundt, and Lewis Gudgeon. Oracle counterpoint: Relationships between on-chain and off-chain market data.
_arXiv preprint arXiv:2303.16331_, 2023.


[[188] yEarn. yinsure. https://yinsure.finance/, 2020.](https://yinsure.finance/)


397


[189] Alexei Zamyatin, Mustafa Al-Bassam, Dionysis Zindros, Eleftherios
Kokoris-Kogias, Pedro Moreno-Sanchez, Aggelos Kiayias, and William J.
Knottenbelt. Sok: Communication across distributed ledgers. Cryptology
[ePrint Archive, Report 2019/1128, 2019. https://eprint.iacr.org/](https://eprint.iacr.org/2019/1128)
[2019/1128.](https://eprint.iacr.org/2019/1128)


[190] Alexei Zamyatin, Dominik Harz, Joshua Lind, Panayiotis Panayiotou,
Arthur Gervais, and William J. Knottenbelt. XCLAIM: Trustless, Inter
   - perable, Cryptocurrency-Backed Assets. In _Proceedings of the IEEE Sym-_
_posium on Security & Privacy, May 2019._, pages 1254–1271, 2019.


[191] Fan Zhang, Ethan Cecchetti, Kyle Croman, Ari Juels, and Elaine Shi. Town
crier: An authenticated data feed for smart contracts. In _Proceedings of the_
_2016 ACM SIGSAC Conference on Computer and Communications Security_,
CCS ’16, page 270–282, New York, NY, USA, 2016. Association for Computing Machinery.


[192] Yi Zhang, Xiaohong Chen, and Daejun Park. Formal specification of constant product (xy= k) market maker model and implementation. Techni[cal report, https://github.com/runtimeverification/verifie](https://github.com/runtimeverification/verified-smart-contracts/blob/uniswap/uniswap/x-y-k.pdf)
[d-smart-contracts/blob/uniswap/uniswap/x-y-k.pdf, 2018.](https://github.com/runtimeverification/verified-smart-contracts/blob/uniswap/uniswap/x-y-k.pdf)


[193] Zixuan Zhang, Michael Zargham, and Victor M. Preciado. On modeling
blockchain-enabled economic networks as stochastic dynamical systems.
_Applied Network Science_, 5(1):19, Mar 2020.


[[194] Micah Zoltu. How to turn $20m into $340m in 15 seconds. https://li](https://link.medium.com/k8QTaHzmr6)
[nk.medium.com/k8QTaHzmr6, Dec. 9, 2019.](https://link.medium.com/k8QTaHzmr6)


398


