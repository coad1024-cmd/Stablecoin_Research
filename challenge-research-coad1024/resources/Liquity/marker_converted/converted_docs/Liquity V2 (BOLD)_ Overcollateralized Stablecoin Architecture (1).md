# **Liquity V2 (BOLD): Overcollateralized Stablecoin** **Architecture**



Liquity V2 (BOLD) is a fully collateralized, multi-collateral lending protocol where users lock up accepted
ERC-20 assets to mint the stablecoin BOLD. The system is architected around _isolated collateral branches_,
each of which maintains an independent over-collateralized debt market and stability pool. A top-level
**CollateralRegistry** maps each supported collateral token (WETH, rETH, wstETH) to its branch-specific
contracts [1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch) [2](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=Liquity%20V2%20supports%20multiple%20collateral,it%20is%20impossible%20to%20add) . Each branch has its own **TroveManager** (managing loans) and **StabilityPool**, as well as
**BorrowerOperations** for user actions. Troves are NFT-backed positions holding one type of collateral and
debt, and collateral from one branch never mixes with another [1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch) [3](https://github.com/liquity/bold#:~:text=,deployed%20for%20each%20collateral%20%E2%80%9Cbranch%E2%80%9D) . This multi-branch design means, for
example, that liquidations in the WETH branch only affect the WETH Stability Pool and active WETH Troves,
and similarly for the LST branches [1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch) [3](https://github.com/liquity/bold#:~:text=,deployed%20for%20each%20collateral%20%E2%80%9Cbranch%E2%80%9D) . Each branch is parameterized independently, with its own

**Minimum Collateral Ratio (MCR)**, **Critical Collateral Ratio (CCR)**, and **Shutdown Collateral Ratio (SCR)**,

ensuring that one branch’s health does not directly jeopardize another’s [1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch) [4](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=1.%20Multi,handled%20within%20the%20same%20branch) .



[1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch) [2](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=Liquity%20V2%20supports%20multiple%20collateral,it%20is%20impossible%20to%20add)



[1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch) [3](https://github.com/liquity/bold#:~:text=,deployed%20for%20each%20collateral%20%E2%80%9Cbranch%E2%80%9D)



[1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch) [3](https://github.com/liquity/bold#:~:text=,deployed%20for%20each%20collateral%20%E2%80%9Cbranch%E2%80%9D)



[1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch) [4](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=1.%20Multi,handled%20within%20the%20same%20branch)



**CollateralRegistry:** A single registry contract lists all supported collaterals and points to each
branch’s TroveManager [3](https://github.com/liquity/bold#:~:text=,deployed%20for%20each%20collateral%20%E2%80%9Cbranch%E2%80%9D) . It is the entry point for redemptions, routing BOLD redemptions to
different branches based on each branch’s “unbacked” debt [5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP) [6](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=How%20is%20the%20collateral%20split,determined) . Once deployed, the collateral
set is fixed (no new tokens can be added) [7](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=CollSurplusPool,to%20add%20any%20new%20collateral) .
**Collateral Branches:** For each supported token (currently WETH, rETH, wstETH), Liquity deploys a
full set of core contracts: `BorrowerOperations`, `TroveManager`, `StabilityPool`,







[3](https://github.com/liquity/bold#:~:text=,deployed%20for%20each%20collateral%20%E2%80%9Cbranch%E2%80%9D)



[5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP) [6](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=How%20is%20the%20collateral%20split,determined)



[7](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=CollSurplusPool,to%20add%20any%20new%20collateral)







`SortedTroves`, `ActivePool`, `DefaultPool`, `CollSurplusPool`, `GasPool`, etc. This



ensures _operational independence_ . A branch contains all logic for opening/adjusting Troves,
liquidations, and redemptions for that collateral [3](https://github.com/liquity/bold#:~:text=,deployed%20for%20each%20collateral%20%E2%80%9Cbranch%E2%80%9D) [8](https://github.com/liquity/bold#:~:text=%2A%20%60CollateralRegistry%60%20,proportion%20to%20their%20%E2%80%9Coutside%E2%80%9D%20debt) .
**Smart-Contract Architecture:** The core contracts mirror Liquity V1 at each branch. Key components

include:

**BorrowerOperations:** User-facing functions to open/modify/close Troves and adjust interest. It

passes state updates to the TroveManager and interacts with Pools (e.g. minting interest via the

ActivePool) [9](https://github.com/liquity/bold#:~:text=%2A%20%60BorrowerOperations%60,the%20ActivePool%20to%20mint%20interest) .

**TroveManager:** Stores each Trove’s collateral, debt, and interest rate. Handles liquidations,
redemptions, and computes accrued interest. It never holds tokens itself but instructs pools to move

collateral/BOLD [10](https://github.com/liquity/bold#:~:text=%2A%20%60TroveManager%60%20,to%20move%20collateral%20or%20BOLD) [11](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=,49) .

**StabilityPool:** Holds BOLD deposits for a branch, plus accrued yields. On liquidations, it
automatically absorbs undercollateralized debt (burning BOLD) and credits depositors with collateral


[12](https://github.com/liquity/bold#:~:text=1.%20Offset%20under,Troves%20in%20the%20same%20branch) [5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP) .


**SortedTroves:** A specialized doubly-linked list sorted by _interest rate_, not collateral ratio, allowing
efficient insertion and redeployment of Troves by rate [13](https://github.com/liquity/bold#:~:text=%2A%20%60SortedTroves%60%20,list%20slices) .
**ActivePool/DefaultPool:** ActivePool tracks total active collateral and debt; DefaultPool holds

collateral+debt from liquidated Troves pending redistribution [14](https://github.com/liquity/bold#:~:text=%2A%20%60ActivePool%60%20,currently%2C%20to%20MockInterestRouter) .
**CollSurplusPool/GasPool:** Tracks post-liquidation collateral surpluses claimable by borrowers, and
collects WETH gas compensation deposits from borrowers [15](https://github.com/liquity/bold#:~:text=%2A%20%60CollSurplusPool%60%20,surplus%20when%20they%20claim%20it) [16](https://github.com/liquity/bold#:~:text=Liquidation%20gas%20compensation) .



[3](https://github.com/liquity/bold#:~:text=,deployed%20for%20each%20collateral%20%E2%80%9Cbranch%E2%80%9D) [8](https://github.com/liquity/bold#:~:text=%2A%20%60CollateralRegistry%60%20,proportion%20to%20their%20%E2%80%9Coutside%E2%80%9D%20debt)











[9](https://github.com/liquity/bold#:~:text=%2A%20%60BorrowerOperations%60,the%20ActivePool%20to%20mint%20interest)







[10](https://github.com/liquity/bold#:~:text=%2A%20%60TroveManager%60%20,to%20move%20collateral%20or%20BOLD) [11](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=,49)







[12](https://github.com/liquity/bold#:~:text=1.%20Offset%20under,Troves%20in%20the%20same%20branch) [5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP)







[13](https://github.com/liquity/bold#:~:text=%2A%20%60SortedTroves%60%20,list%20slices)







[14](https://github.com/liquity/bold#:~:text=%2A%20%60ActivePool%60%20,currently%2C%20to%20MockInterestRouter)







[15](https://github.com/liquity/bold#:~:text=%2A%20%60CollSurplusPool%60%20,surplus%20when%20they%20claim%20it) [16](https://github.com/liquity/bold#:~:text=Liquidation%20gas%20compensation)



1


Together, this branch-based architecture ensures each collateral market can have custom parameters and
isolated risk, while sharing the single BOLD token and global Oracle infrastructure.

## **Accepted Collaterals and Branch Handling**



Liquity V2 accepts only **high-grade assets** : WETH and two Liquid Staking Tokens (LSTs), specifically rETH and
wstETH [17](https://github.com/liquity/bold#:~:text=,accept%20native%20ETH%20as%20collateral) [18](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=handled%20within%20the%20same%20branch,but%20not%20native%20ETH) . Native ETH is _not_ accepted. Each of these tokens has its own branch, meaning a Trove in the
WETH branch uses WETH as collateral only, while Troves in LST branches use the respective staked-ETH
tokens. The CollateralRegistry enforces this mapping, so users cannot mix collaterals in one Trove [1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch) [3](https://github.com/liquity/bold#:~:text=,deployed%20for%20each%20collateral%20%E2%80%9Cbranch%E2%80%9D) .



[17](https://github.com/liquity/bold#:~:text=,accept%20native%20ETH%20as%20collateral) [18](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=handled%20within%20the%20same%20branch,but%20not%20native%20ETH)



[1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch) [3](https://github.com/liquity/bold#:~:text=,deployed%20for%20each%20collateral%20%E2%80%9Cbranch%E2%80%9D)




- **LST Handling:** Pricing LSTs requires composite oracles. Liquity uses Chainlink oracles: for wstETH

and rETH, a CompositePriceFeed takes the stETH-USD price from Chainlink and the token’s own
exchange rate (wstETH/STETH or rETH/ETH) to compute a conservative USD price (the minimum of



market price and on-chain exchange rate) [19](https://github.com/liquity/bold#:~:text=%2A%20%60CompositePriceFeed%60%20,min%28market_price%2C%20exchange_rate_price) [20](https://github.com/liquity/bold#:~:text=%2A%20%60WSTETHPriceFeed%60%20,collateral%20on%20a%20WSTETH%20branch) . This prevents one-shot price spikes from causing
unsafe redemptions.
**Price Feeds:** Each branch has a dedicated `PriceFeed` contract. WETH branch uses a simple ETH

USD feed. LST branches use either a composite feed (rETH) or calculate via stETH price (wstETH) [21](https://github.com/liquity/bold#:~:text=,collateral%20on%20the%20WETH%20branch) .
If an oracle fails or the price deviates drastically, the branch can trigger an _emergency shutdown_,
pausing borrowing and enabling special redemptions [22](https://github.com/liquity/bold#:~:text=,branch%20as%20quickly%20as%20possible) [11](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=,49) .
**Branch Parameters:** The MCR, CCR, and SCR are set per branch based on collateral volatility. For
example, a wstETH branch might have a higher MCR than WETH if staked ETH is considered riskier.
The system ensures each branch individually remains over-collateralized: its total collateral value
always exceeds total BOLD debt [1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch) [4](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=1.%20Multi,handled%20within%20the%20same%20branch) . In other words, each branch’s Total Collateral Ratio (TCR) is
kept above 100% even in stress, and typically well above MCR.



[19](https://github.com/liquity/bold#:~:text=%2A%20%60CompositePriceFeed%60%20,min%28market_price%2C%20exchange_rate_price) [20](https://github.com/liquity/bold#:~:text=%2A%20%60WSTETHPriceFeed%60%20,collateral%20on%20a%20WSTETH%20branch)







[21](https://github.com/liquity/bold#:~:text=,collateral%20on%20the%20WETH%20branch)



[22](https://github.com/liquity/bold#:~:text=,branch%20as%20quickly%20as%20possible) [11](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=,49)







[1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch) [4](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=1.%20Multi,handled%20within%20the%20same%20branch)



By isolating collateral types, Liquity V2 prevents contagion: a crash in one token’s price only directly affects
that branch. During normal operation, cross-branch interactions occur only via redemptions (routed by the
CollateralRegistry) and global BOLD mint/burn functions.

## **Trove System: Collateral, Debt, and Interest Rates**


Each user debt position is a **Trove NFT** . A single address can own multiple Troves (NFTs), each identified by

an ID. When opening a Trove, the user chooses one branch (collateral type) and deposits that ERC-20 token.
They then draw BOLD up to ensure the Trove’s Individual Collateral Ratio (ICR) stays at or above the branch’s
MCR [23](https://github.com/liquity/bold#:~:text=Upon%20opening%20a%20Trove%20by,90%20BOLD%20against%20it) . For example, with a 110% MCR, \$10,000 of WETH allows up to 9,090.90 BOLD borrowed [23](https://github.com/liquity/bold#:~:text=Upon%20opening%20a%20Trove%20by,90%20BOLD%20against%20it) . The

Trove’s debt increments the branch’s total debt, and the collateral increases the branch’s total collateral.



Importantly, **interest is user-set** : the borrower chooses an annual interest rate (between 0.5% and 100%
APR currently) when opening, and can adjust it later [24](https://github.com/liquity/bold#:~:text=%2A%20User,is%20periodically%20minted%20as%20BOLD) [25](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=2,to%20choose%20higher%20interest%20rates) . This is a core monetary-policy mechanism. The
Trove accrues simple (continuous) interest on its recorded debt at the chosen rate. Interest is _not_
compounded every second; instead, accrued interest is tallied continuously and then added (compounded)
discretely whenever the Trove is “touched” (e.g. when the borrower changes collateral/debt or claims
rewards) [26](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=In%20Liquity%20V2%2C%20trove%20owners,However%2C%20users%20are%20also) [27](https://github.com/liquity/bold#:~:text=given%20Trove%20debt%2C%20interest%20accrues,as%20the%20Trove%20isn%E2%80%99t%20altered) . The user may change their interest rate anytime (subject to cooldowns and fees), and
Troves are constantly re-sorted in the branch’s SortedTroves list whenever their rate changes.



[24](https://github.com/liquity/bold#:~:text=%2A%20User,is%20periodically%20minted%20as%20BOLD) [25](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=2,to%20choose%20higher%20interest%20rates)



[26](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=In%20Liquity%20V2%2C%20trove%20owners,However%2C%20users%20are%20also) [27](https://github.com/liquity/bold#:~:text=given%20Trove%20debt%2C%20interest%20accrues,as%20the%20Trove%20isn%E2%80%99t%20altered)



The **interest revenue** is used as yield for the protocol. The system tracks the _total system interest_ as a
weighted sum of each Trove’s debt × interest rate [26](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=In%20Liquity%20V2%2C%20trove%20owners,However%2C%20users%20are%20also) . On each relevant operation, the protocol mints the


2


accumulated interest as new BOLD. This BOLD is split in a fixed proportion: currently 75% goes into the
Stability Pool (payable to depositors in proportion to their share) and 25% goes to an interest router
(intended for DEX liquidity providers) [28](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=This%20expression%20is%20then%20used,it%20requires%20user%20action%20to) . Crucially, 75% of all branch interest goes back to that branch’s
Stability Pool [29](https://github.com/liquity/bold#:~:text=,SP%20on%20that%20same%20branch) [28](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=This%20expression%20is%20then%20used,it%20requires%20user%20action%20to) . Thus, lending yields are paid to depositors and the ecosystem, supporting the peg
and rewarding participants.



[28](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=This%20expression%20is%20then%20used,it%20requires%20user%20action%20to)



[29](https://github.com/liquity/bold#:~:text=,SP%20on%20that%20same%20branch) [28](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=This%20expression%20is%20then%20used,it%20requires%20user%20action%20to)



To prevent _interest-rate front-running_, Liquity V2 imposes a **7-day upfront fee** - n Trove creation and on early
interest adjustments [30](https://github.com/liquity/bold#:~:text=,they%20make%20a%20premature%20adjustment) [31](https://github.com/liquity/bold#:~:text=,equal%20to%207%20days%20of) . Concretely, when opening a Trove or borrowing more, the borrower pays a
small fee equal to the interest they’d accrue over 7 days at the _current system-average_ rate. If the borrower
changes their rate again within 7 days, a similar fee is applied. The user must specify a `_maxUpfrontFee`


to protect against slippage if rates move between submitting the transaction and execution [30](https://github.com/liquity/bold#:~:text=,they%20make%20a%20premature%20adjustment) . This
mechanism ensures borrowers commit to their rate choices and cannot rapidly game redemption ordering

without cost.





Other Trove features:


    - **Debt & Collateral Adjustments:** Users (or delegated managers) can top up or withdraw collateral



and borrow or repay BOLD, so long as ICR≥MCR and other branch rules are respected [32](https://github.com/liquity/bold#:~:text=,mints%20BOLD%20stablecoins%20to%20the) .
Adjustments reinsert the Trove into the SortedTroves structure if needed.
**Delegation:** Trove owners can appoint _individual_ managers to adjust one Trove’s rate or debt, and
_batch_ managers that can update rates for many Troves within a set range. This allows professional
“rate managers” to service multiple Troves, earning fees [33](https://github.com/liquity/bold#:~:text=,control%20debt%20and%20collateral%20adjustments) . The contract interface provides for
registering managers and joining/leaving batches, all subject to rate-change cooldowns [34](https://github.com/liquity/bold#:~:text=,the%20delegates%27s%20interest%20rate%20adjustments) [35](https://github.com/liquity/bold#:~:text=_upperHint%2C%20uint256%20_lowerHint%2C%20uint256%20_maxUpfrontFee,date) .
**Minimum Debt:** Troves have a minimum debt (e.g. 2,000 BOLD) to remain active. If redemptions or
repayments drive a Trove’s debt below this threshold, it becomes a _zombie Trove_ (dormant) until debt
is brought back up [36](https://github.com/liquity/bold#:~:text=,MIN_DEBT) [37](https://github.com/liquity/bold#:~:text=,If) . This avoids griefing from tiny debts. Zombie Troves cannot be redeemed
again until they repay additional debt above the minimum [36](https://github.com/liquity/bold#:~:text=,MIN_DEBT) .



[32](https://github.com/liquity/bold#:~:text=,mints%20BOLD%20stablecoins%20to%20the)







[33](https://github.com/liquity/bold#:~:text=,control%20debt%20and%20collateral%20adjustments)



[34](https://github.com/liquity/bold#:~:text=,the%20delegates%27s%20interest%20rate%20adjustments) [35](https://github.com/liquity/bold#:~:text=_upperHint%2C%20uint256%20_lowerHint%2C%20uint256%20_maxUpfrontFee,date)







[36](https://github.com/liquity/bold#:~:text=,MIN_DEBT) [37](https://github.com/liquity/bold#:~:text=,If)



[36](https://github.com/liquity/bold#:~:text=,MIN_DEBT)



Overall, the Trove system is carefully engineered: per-Trove interest is linear in time and proportional to
debt [27](https://github.com/liquity/bold#:~:text=given%20Trove%20debt%2C%20interest%20accrues,as%20the%20Trove%20isn%E2%80%99t%20altered) [38](https://github.com/liquity/bold#:~:text=This%20is%20calculated%20in%20), and global interest can be calculated via aggregated state (e.g. ActivePool uses tracker sums
so interest minting is gas-efficient) [39](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20contract%20stores%20the%20total,to%20how%20collateral%20gains%20are) [40](https://github.com/liquity/bold#:~:text=Redistribution%20is%20performed%20in%20a,TroveManager.getEntireDebtAndColl) .



[27](https://github.com/liquity/bold#:~:text=given%20Trove%20debt%2C%20interest%20accrues,as%20the%20Trove%20isn%E2%80%99t%20altered) [38](https://github.com/liquity/bold#:~:text=This%20is%20calculated%20in%20)



[39](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20contract%20stores%20the%20total,to%20how%20collateral%20gains%20are) [40](https://github.com/liquity/bold#:~:text=Redistribution%20is%20performed%20in%20a,TroveManager.getEntireDebtAndColl)


## **Redemption Mechanism (BOLD → Collateral)**



Redemptions enforce a hard \$1 floor for BOLD by allowing anyone to swap BOLD for collateral at face
value (minus a small fee) [41](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=Redemptions%20serve%20the%20crucial%20purpose,centralized%20assets%20or%203rd%20parties) [42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins) . The key innovation is multi-collateral redemption routing: when a user
redeems _X_ BOLD, the CollateralRegistry distributes this demand across branches **in proportion to each**
**branch’s** _**unbacked debt**_ [43](https://github.com/liquity/bold#:~:text=,BOLD%20in%20the%20branch%E2%80%99s%20SP) [5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP) . Unbackedness is defined as (total BOLD debt in branch) minus (BOLD held
in that branch’s Stability Pool) [43](https://github.com/liquity/bold#:~:text=,BOLD%20in%20the%20branch%E2%80%99s%20SP) [5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP) . Intuitively, if a branch has a lot of debt relative to its SP backing, it is
considered “risky” and redemptions target it more heavily (to restore backing). For example, if branch A has
twice the outside debt of branch B, then two-thirds of the redemption volume hits A and one-third hits B [44](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=Example%3A%20Two%20active%20collateral%20branches%2C,as%20that%20of%20branch%201)

[45](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=To%20mitigate%20this%20risk%2C%20the,Pool%20for%20that%20borrowing%20market) . This mechanism **maximizes economic safety** by preferentially liquidating collateral from the weakest

backed markets [6](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=How%20is%20the%20collateral%20split,determined) [5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP) .



[41](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=Redemptions%20serve%20the%20crucial%20purpose,centralized%20assets%20or%203rd%20parties) [42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins)



[43](https://github.com/liquity/bold#:~:text=,BOLD%20in%20the%20branch%E2%80%99s%20SP) [5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP)



[43](https://github.com/liquity/bold#:~:text=,BOLD%20in%20the%20branch%E2%80%99s%20SP) [5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP)



[44](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=Example%3A%20Two%20active%20collateral%20branches%2C,as%20that%20of%20branch%201)



[45](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=To%20mitigate%20this%20risk%2C%20the,Pool%20for%20that%20borrowing%20market)



[6](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=How%20is%20the%20collateral%20split,determined) [5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP)



3


Within each branch, the redemption process is as follows:

   - The branch’s `TroveManager.redeemCollateral()` iterates over Troves in ascending order of



interest rate (from lowest rate to highest) [46](https://github.com/liquity/bold#:~:text=,at%20all%20for%20redemption%20ordering) [47](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=Redemptions%20in%20each%20branch%20still,the%20lowest%20collateral%20ratio%20trove) . Troves with lower interest rates have more “debt
ahead” and hence get hit first; higher-rate Troves are shielded. Importantly, **collateral ratio is**
**ignored** during redemption ordering [46](https://github.com/liquity/bold#:~:text=,at%20all%20for%20redemption%20ordering) .
As each Trove is redeemed, an amount of debt and corresponding collateral (worth \$1 per BOLD) is
removed. The borrower’s debt is paid off, and the collateral is transferred to the redeemer, less a
small redemption fee. The fee accrues to the system (and ultimately to borrowers or SP depositors
depending on design).
Troves fully redeemed remain open (“zombie mode” if debt falls below minimum), but future
redemptions skip any Trove with debt below the MIN_DEBT threshold [36](https://github.com/liquity/bold#:~:text=,MIN_DEBT) [47](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=Redemptions%20in%20each%20branch%20still,the%20lowest%20collateral%20ratio%20trove) . This prevents tinydebt Troves from being targeted repeatedly.
Borrowers **do not lose USD value** - n redemption: they simply trade collateral for debt. In fact, they
may effectively _earn_ the fee paid by the redeemer, as that fee is left in their Trove collateral [48](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=You%20can%20think%20of%20redemptions,of%20your%20collateral%20in%20return) [49](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=,ETH%20collateral%2C%2020%27000%20BOLD%20debt) .





[46](https://github.com/liquity/bold#:~:text=,at%20all%20for%20redemption%20ordering)











[36](https://github.com/liquity/bold#:~:text=,MIN_DEBT) [47](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=Redemptions%20in%20each%20branch%20still,the%20lowest%20collateral%20ratio%20trove)







[48](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=You%20can%20think%20of%20redemptions,of%20your%20collateral%20in%20return) [49](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=,ETH%20collateral%2C%2020%27000%20BOLD%20debt)



In summary, a redemption swaps _X_ BOLD for \$X worth of branch collateral across branches, using the
“outside debt” split [44](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=Example%3A%20Two%20active%20collateral%20branches%2C,as%20that%20of%20branch%201) [45](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=To%20mitigate%20this%20risk%2C%20the,Pool%20for%20that%20borrowing%20market) . This guarantees a _hard peg floor_ : no rational arbitrageur will let BOLD fall below
\$1, because they could always redeem at \$1 value [41](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=Redemptions%20serve%20the%20crucial%20purpose,centralized%20assets%20or%203rd%20parties) [42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins) . The CollateralRegistry’s routing logic and the

- rdered redemption algorithm ensure that redemptions automatically target system weaknesses while
preserving overall backing [43](https://github.com/liquity/bold#:~:text=,BOLD%20in%20the%20branch%E2%80%99s%20SP) [6](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=How%20is%20the%20collateral%20split,determined) .



[44](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=Example%3A%20Two%20active%20collateral%20branches%2C,as%20that%20of%20branch%201) [45](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=To%20mitigate%20this%20risk%2C%20the,Pool%20for%20that%20borrowing%20market)



[41](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=Redemptions%20serve%20the%20crucial%20purpose,centralized%20assets%20or%203rd%20parties) [42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins)



[43](https://github.com/liquity/bold#:~:text=,BOLD%20in%20the%20branch%E2%80%99s%20SP) [6](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=How%20is%20the%20collateral%20split,determined)


## **Risk Management: Liquidations and Collateral Ratios**



Liquidity risk in each branch is managed by straightforward collateral-ratio rules and liquidation mechanics.
A Trove becomes _liquidatable_ immediately when its ICR (instant collateral ratio) drops below the branch’s
MCR [50](https://github.com/liquity/bold#:~:text=The%20Liquity%20v2%20system%20prices,and%20is%20vulnerable%20to%20liquidation) . (Unlike V1, there is no separate “Recovery Mode” – liquidations occur only below MCR [51](https://github.com/liquity/bold#:~:text=,for%20a%20given%20branch) [52](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=12,compensation%20in%20a%20mix%20of) .)
Critical Collateral Ratio (CCR) and other thresholds can impose borrowing restrictions: e.g. borrowers cannot
mint new BOLD if the branch TCR is below CCR [52](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=12,compensation%20in%20a%20mix%20of) [53](https://github.com/liquity/bold#:~:text=system%E2%80%99s%20TCR%20,interest%20rate%20increases%20and%20in) . In extremis, if an oracle signals a crash or fails, the
branch can **shutdown**, freezing borrowing and turning on _urgent redemptions_ at a 1.01\$ collateral bonus


[22](https://github.com/liquity/bold#:~:text=,branch%20as%20quickly%20as%20possible) [52](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=12,compensation%20in%20a%20mix%20of) .



[50](https://github.com/liquity/bold#:~:text=The%20Liquity%20v2%20system%20prices,and%20is%20vulnerable%20to%20liquidation) [51](https://github.com/liquity/bold#:~:text=,for%20a%20given%20branch) [52](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=12,compensation%20in%20a%20mix%20of)



[52](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=12,compensation%20in%20a%20mix%20of) [53](https://github.com/liquity/bold#:~:text=system%E2%80%99s%20TCR%20,interest%20rate%20increases%20and%20in)



[22](https://github.com/liquity/bold#:~:text=,branch%20as%20quickly%20as%20possible) [52](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=12,compensation%20in%20a%20mix%20of)



Liquidation itself is a two-step process per branch [54](https://github.com/liquity/bold#:~:text=When%20a%20Trove%E2%80%99s%20collateral%20ratio,IDs%20to%20attempt%20to%20liquidate) :



**Offset via Stability Pool:** First, the Stability Pool absorbs as much undercollateralized debt as
possible. The liquidated Trove’s debt is matched against BOLD in the SP; that BOLD is burned to pay
down the debt, and the seizer receives the collateral. Those seizer (normally the SP depositors)
collect the Trove’s collateral. The liquidated Trove is then closed (its recorded debt becomes zero) [12](https://github.com/liquity/bold#:~:text=1.%20Offset%20under,Troves%20in%20the%20same%20branch) .
**Redistribution:** If the Stability Pool is empty before clearing all debt, the remaining debt and
collateral are _redistributed_ to all active Troves in that branch, pro-rata by collateral [12](https://github.com/liquity/bold#:~:text=1.%20Offset%20under,Troves%20in%20the%20same%20branch) [55](https://github.com/liquity/bold#:~:text=If%20the%20liquidated%20debt%20is,active%20Troves%20in%20the%20branch) . This
means each surviving Trove gets a small amount of extra collateral and corresponding extra debt,
preserving the branch’s total balance.



1.


2.



[12](https://github.com/liquity/bold#:~:text=1.%20Offset%20under,Troves%20in%20the%20same%20branch)



[12](https://github.com/liquity/bold#:~:text=1.%20Offset%20under,Troves%20in%20the%20same%20branch) [55](https://github.com/liquity/bold#:~:text=If%20the%20liquidated%20debt%20is,active%20Troves%20in%20the%20branch)



Unlike V1, liquidated borrowers in V2 may _retain a collateral surplus_ . The protocol defines separate

**liquidation penalties** for offset vs. redistribution liquidations, each ≤10% (and ≤MCR) [56](https://github.com/liquity/bold#:~:text=Separate%20liquidation%20penalty%20percentages%20are,%60LIQUIDATION_PENALTY_SP%60%20and%20%60LIQUIDATION_PENALTY_REDISTRIBUTION) . In a pure offset
(when SP covers all debt), at most `(1 + LIQUIDATION_PENALTY_SP)` fraction of the Trove’s collateral is


seized; any remainder is returned to the borrower as a surplus [57](https://github.com/liquity/bold#:~:text=back%20,always%20seized%20in%20Normal%20Mode) . In a pure redistribution, at most `(1 +`





4


`LIQUIDATION_PENALTY_REDISTRIBUTION)` is seized, with surplus returned [57](https://github.com/liquity/bold#:~:text=back%20,always%20seized%20in%20Normal%20Mode) . In mixed liquidations the

penalties apply sequentially (offset penalty on the offset portion, redistribution penalty on the rest) [58](https://github.com/liquity/bold#:~:text=In%20a%20mixed%20offset%20and,that%20is) .
Borrowers must explicitly claim these surplus tokens via `claimColl()` . This change means liquidated


users often leave with some collateral, reducing their loss and socializing less of the bad-debt cost.



Liquidators are also compensated for gas. Each new Trove deposits 0.0375 WETH into the GasPool (not
counted as collateral) [59](https://github.com/liquity/bold#:~:text=When%20a%20Trove%20is%20opened%2C,ICR%20or%20the%20TCR%20calculations) . Upon liquidation, the liquidator always receives that 0.0375 WETH. Additionally,
they receive up to 0.5% of the Trove’s collateral (capped at 2 token units, e.g. 2 rETH) as extra compensation

[60](https://github.com/liquity/bold#:~:text=The%20collateral%20portion%20of%20the,2%20units%20of%20the%20LST) . This encourages keepers to trigger liquidations quickly even on-chain congestion or multiple branches

(and covers gas with protocol-held funds).



[59](https://github.com/liquity/bold#:~:text=When%20a%20Trove%20is%20opened%2C,ICR%20or%20the%20TCR%20calculations)



[60](https://github.com/liquity/bold#:~:text=The%20collateral%20portion%20of%20the,2%20units%20of%20the%20LST)



Finally, branches enforce minimum BOLD in SP: once a branch’s Stability Pool has ≥1 BOLD deposited, the
protocol will never allow it to fall below 1 BOLD (via partial withdrawals or full offsets) [61](https://github.com/liquity/bold#:~:text=Minimum%201%20BOLD%20token%20in,the%20SP) . This ensures the
SP is never completely drained by accident. If ever an SP is temporarily under 1 BOLD (e.g. at launch),
liquidations will skip offsets and only do redistribution [62](https://github.com/liquity/bold#:~:text=,the%20offset%20boundary%20has%20shifted) .



[61](https://github.com/liquity/bold#:~:text=Minimum%201%20BOLD%20token%20in,the%20SP)



[62](https://github.com/liquity/bold#:~:text=,the%20offset%20boundary%20has%20shifted)



Overall, risk is managed by requiring strict over-collateralization (ICR ≥ MCR), absorbing bad debt into the
Stability Pool, returning surplus collateral to borrowers, and isolating branches. If a branch’s collateral
market severely crashes, it can be shut down to protect peg and allow rapid cleanup via bonus redemptions


[22](https://github.com/liquity/bold#:~:text=,branch%20as%20quickly%20as%20possible) [52](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=12,compensation%20in%20a%20mix%20of) .

## **Stability Pool: Purpose and Mechanics**



The **Stability Pool (SP)** in each branch is the protocol’s first defense against bad debt. Anyone can deposit
BOLD into a branch’s SP to earn two forms of yield [12](https://github.com/liquity/bold#:~:text=1.%20Offset%20under,Troves%20in%20the%20same%20branch) [63](https://docs.liquity.org/v2-faq/bold-and-earn#:~:text=The%20yield%20comes%20from%20two,sources) : (1) **Liquidation gains** - when Troves in that
branch are liquidated, the SP’s BOLD is used to cancel their debt, and SP depositors receive the Troves’
collateral (at an effective discount, since they provide less than face value BOLD); (2) **Interest yield** - 75%

- f branch Trove interest is periodically paid into the SP (minted as new BOLD) [28](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=This%20expression%20is%20then%20used,it%20requires%20user%20action%20to) [63](https://docs.liquity.org/v2-faq/bold-and-earn#:~:text=The%20yield%20comes%20from%20two,sources) . Together, these yields
let SP depositors grow their stake in BOLD and accumulate LST collateral.



[12](https://github.com/liquity/bold#:~:text=1.%20Offset%20under,Troves%20in%20the%20same%20branch) [63](https://docs.liquity.org/v2-faq/bold-and-earn#:~:text=The%20yield%20comes%20from%20two,sources)



[28](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=This%20expression%20is%20then%20used,it%20requires%20user%20action%20to) [63](https://docs.liquity.org/v2-faq/bold-and-earn#:~:text=The%20yield%20comes%20from%20two,sources)





`doClaim)` . The `doClaim` flag lets depositors either claim accumulated gains (in collateral and

BOLD) or keep them compounded.
**Scalable Accounting:** The StabilityPool uses a _product-sum_ tracking algorithm (Batog’s UniPool
method) to manage rewards with O(1) gas cost [64](https://github.com/liquity/bold#:~:text=When%20a%20liquidation%20occurs%2C%20rather,corresponding%20to%20the%20collateral%20gain) . Two global trackers, a product _P_ and sum _S_, are
updated on each liquidation. Each depositor’s share and gains are calculated from their initial
snapshot of _(P,S)_ . This avoids per-user updates on every event [64](https://github.com/liquity/bold#:~:text=When%20a%20liquidation%20occurs%2C%20rather,corresponding%20to%20the%20collateral%20gain) .
**Liquidation Absorption:** As noted, liquidating a Trove burns an equal amount of BOLD from the SP
and allocates collateral to depositors proportionally. Deposit value typically _increases_, since a Trove
liquidated at just-below-MCR usually yields slightly more collateral value than the cancelled BOLD


[65](https://github.com/liquity/bold#:~:text=Stability%20Pool%20depositors%20can%20expect,take%20a%20value%20above%20100)

. The effect is that SP depositors earn excess ETH/LST at a roughly 5–10% discount, locked in at
liquidation time [63](https://docs.liquity.org/v2-faq/bold-and-earn#:~:text=The%20yield%20comes%20from%20two,sources) [65](https://github.com/liquity/bold#:~:text=Stability%20Pool%20depositors%20can%20expect,take%20a%20value%20above%20100) . Depositors must claim these collateral gains (or choose to reinvest them) by
interacting with the pool.
**Yield Gains:** When interest is minted, 75% flows into the SP. The protocol triggers a proportional
crediting of BOLD to each depositor (via the same _P,S_ tracking, using an analogous _B_ sum) [66](https://github.com/liquity/bold#:~:text=BOLD%20Yield%20Gains) . This







[64](https://github.com/liquity/bold#:~:text=When%20a%20liquidation%20occurs%2C%20rather,corresponding%20to%20the%20collateral%20gain)



[64](https://github.com/liquity/bold#:~:text=When%20a%20liquidation%20occurs%2C%20rather,corresponding%20to%20the%20collateral%20gain)







[65](https://github.com/liquity/bold#:~:text=Stability%20Pool%20depositors%20can%20expect,take%20a%20value%20above%20100)



[63](https://docs.liquity.org/v2-faq/bold-and-earn#:~:text=The%20yield%20comes%20from%20two,sources) [65](https://github.com/liquity/bold#:~:text=Stability%20Pool%20depositors%20can%20expect,take%20a%20value%20above%20100)







[66](https://github.com/liquity/bold#:~:text=BOLD%20Yield%20Gains)



5


BOLD yield is _not_ auto-staked; depositors must withdraw and re-deposit (or call the “doClaim”
function) to compound it.
**Minimum 1 BOLD Rule:** Once total SP deposits reach at least 1 BOLD, the system enforces that at
least 1 BOLD remains. Withdrawals or liquidations will never fully deplete the SP below 1 BOLD [61](https://github.com/liquity/bold#:~:text=Minimum%201%20BOLD%20token%20in,the%20SP) .
This guard prevents the pool from unintentionally emptying.







[61](https://github.com/liquity/bold#:~:text=Minimum%201%20BOLD%20token%20in,the%20SP)



In short, each branch’s SP safely buffers liquidations and returns value to depositors. By design, it is the
_absorber_ - f last resort: any undercollateralized debt is first and foremost paid by burning SP BOLD,
protecting active Troves and limiting contagion [12](https://github.com/liquity/bold#:~:text=1.%20Offset%20under,Troves%20in%20the%20same%20branch) . The dual-yield model (collateral + BOLD) incentivizes
deposits without needing inflationary token emissions.

## **Oracle Integration**


Liquity V2 relies on **decentralized price oracles** for each collateral. Every branch uses a specialized oracle

contract:



**WETHPriceFeed:** Fetches the ETH-USD price from a Chainlink feed [21](https://github.com/liquity/bold#:~:text=,collateral%20on%20the%20WETH%20branch) .
**WSTETHPriceFeed:** Gets the STETH-USD price from Chainlink, then converts to WSTETH-USD using




- **WETHPriceFeed:** [21](https://github.com/liquity/bold#:~:text=,collateral%20on%20the%20WETH%20branch)







the wstETH↔stETH exchange rate from the wstETH contract [20](https://github.com/liquity/bold#:~:text=%2A%20%60WSTETHPriceFeed%60%20,collateral%20on%20a%20WSTETH%20branch) .
**RETHPriceFeed:** Uses a composite approach: it fetches rETH-ETH and ETH-USD prices (from on-chain
and Chainlink, respectively) to compute rETH-USD [19](https://github.com/liquity/bold#:~:text=%2A%20%60CompositePriceFeed%60%20,min%28market_price%2C%20exchange_rate_price) [20](https://github.com/liquity/bold#:~:text=%2A%20%60WSTETHPriceFeed%60%20,collateral%20on%20a%20WSTETH%20branch) . The returned price is the _minimum_ - f the
market price and the token’s internal exchange rate price, to guard against oracle mismatches.



[20](https://github.com/liquity/bold#:~:text=%2A%20%60WSTETHPriceFeed%60%20,collateral%20on%20a%20WSTETH%20branch)







[19](https://github.com/liquity/bold#:~:text=%2A%20%60CompositePriceFeed%60%20,min%28market_price%2C%20exchange_rate_price) [20](https://github.com/liquity/bold#:~:text=%2A%20%60WSTETHPriceFeed%60%20,collateral%20on%20a%20WSTETH%20branch)



Oracles are “push” style with fail-safes. The MainnetPriceFeedBase contract verifies fresh data and enforces
sanity bounds; if an oracle feed fails or deviates grossly, it can **trigger branch shutdown** [2](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=Liquity%20V2%20supports%20multiple%20collateral,it%20is%20impossible%20to%20add) . For example,
if Chainlink goes stale, the CollateralRegistry can close the branch to prevent mispricing. Thus, oracle errors
lead to temporary halting of Trove operations in that branch, while urgent redemptions (with bonus) may
be allowed to restore solvency [22](https://github.com/liquity/bold#:~:text=,branch%20as%20quickly%20as%20possible) [11](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=,49) . In normal operation, however, branch oracles feed into the TCR
calculations and liquidation triggers: a drop in price raises ICRs of Troves toward MCR, activating
liquidations as needed [50](https://github.com/liquity/bold#:~:text=The%20Liquity%20v2%20system%20prices,and%20is%20vulnerable%20to%20liquidation) [54](https://github.com/liquity/bold#:~:text=When%20a%20Trove%E2%80%99s%20collateral%20ratio,IDs%20to%20attempt%20to%20liquidate) .



[2](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=Liquity%20V2%20supports%20multiple%20collateral,it%20is%20impossible%20to%20add)



[22](https://github.com/liquity/bold#:~:text=,branch%20as%20quickly%20as%20possible) [11](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=,49)



[50](https://github.com/liquity/bold#:~:text=The%20Liquity%20v2%20system%20prices,and%20is%20vulnerable%20to%20liquidation) [54](https://github.com/liquity/bold#:~:text=When%20a%20Trove%E2%80%99s%20collateral%20ratio,IDs%20to%20attempt%20to%20liquidate)


## **Multi-Collateral Independence**



Each collateral branch operates **in isolation** . Troves never share collateral, stability pools never mix tokens,
and liquidations/redemptions are branch-specific. The CollateralRegistry only synchronizes branches in
three ways: (1) it mints/burns BOLD (global token) in total supply; (2) it routes redemptions across branches;
and (3) it holds global parameters like overall Stability Pool usage in extreme cases [43](https://github.com/liquity/bold#:~:text=,BOLD%20in%20the%20branch%E2%80%99s%20SP) [5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP) . Importantly,
aggregate metrics like system TCR are branch-local (each branch has its own TCR), and branch health is
evaluated independently [4](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=1.%20Multi,handled%20within%20the%20same%20branch) [42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins) .



[43](https://github.com/liquity/bold#:~:text=,BOLD%20in%20the%20branch%E2%80%99s%20SP) [5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP)



[4](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=1.%20Multi,handled%20within%20the%20same%20branch) [42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins)



This means, for instance, that if rETH crashes while WETH remains strong, only the rETH branch’s operations
and redemptions are directly affected. A Trove in the WETH branch sees no collateral from rETH. In practice,
however, monetary policy (interest rates) and user behavior may correlate across branches. Still, the
protocol’s _backing mechanism_ benefits from decentralization: the peg is supported by a diverse basket of
assets, and a drop in one can be counterbalanced by others. The multi-branch structure also allows the


[1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch)

system to fine-tune MCR/CCR per asset, reflecting their risk profiles, without harming other markets


[4](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=1.%20Multi,handled%20within%20the%20same%20branch) .



[1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch)



[4](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=1.%20Multi,handled%20within%20the%20same%20branch)



6


## **Long-Term Peg Stability**

Liquity’s design ensures that 1 BOLD ≃ \$1 USD is an equilibrium:



1.


2.


3.


4.


5.



**Over-collateralization:** By construction, all Troves are individually >MCR, and each branch’s total
collateral exceeds debt [42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins) [1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch) . This means the system always holds more value than the BOLD it
issues. Economically, this creates a hard price floor: if BOLD ever deviated below \$1, arbitrageurs


[41](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=Redemptions%20serve%20the%20crucial%20purpose,centralized%20assets%20or%203rd%20parties)

could redeem BOLD for \$1 worth of collateral (from the Stability Pools) and immediately profit

[42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins) . This redemption mechanism _stabilizes_ the peg.

**Redemption Guarantees:** Unlike many DeFi stablecoins, Liquity ensures _full redeemability_ - f BOLD
at face value (minus a dynamic fee) across the whole basket [41](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=Redemptions%20serve%20the%20crucial%20purpose,centralized%20assets%20or%203rd%20parties) [42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins) . Any shortfall in one asset’s
backing is automatically compensated by others via redemption routing [5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP) [6](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=How%20is%20the%20collateral%20split,determined) . The fee schedule is



leaving price at equilibrium.
**Dynamic Interest (Demand) Adjustment:** The user-set interest-rate mechanism introduces a
market-driven monetary policy [67](https://docs.liquity.org/v2-faq/bold-and-earn#:~:text=What%20is%20BOLD%E2%80%99s%20peg%20mechanism%3F) [26](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=In%20Liquity%20V2%2C%20trove%20owners,However%2C%20users%20are%20also) . If BOLD trades _above_ \$1, borrowers can lower their rates
(making borrowing cheaper and BOLD issuance easier), increasing BOLD supply and pushing price
down. If BOLD trades _below_ \$1, borrowers will have an incentive to raise rates (pay more interest),
reducing new borrowing and even encouraging some to close Troves, which reduces BOLD supply
and pushes price up [67](https://docs.liquity.org/v2-faq/bold-and-earn#:~:text=What%20is%20BOLD%E2%80%99s%20peg%20mechanism%3F) . In addition, redemptions below \$1 “use up” undercollateralized positions,
forcing borrowers to pick safer rates or close Troves. Combined, these pressures help keep BOLD

anchored.
**Stability Pool Cushion:** The Stability Pools act as a liquidity buffer. By soaking up liquidations and

- ffering depositors attractive yields, they ensure that sharp dips in collateral prices don’t
immediately cause uncovered debt or cascade liquidations. This shock-absorption helps the peg
survive short-term market turbulence. The SP also earns BOLD supply (from interest yield) which
drains some buying demand when BOLD is above peg, and provides BOLD to cancel debt when price
falls – a stabilizing feedback loop.
**Branch Redundancy:** Multiple collateral types provide robustness. For example, if staking yields or
demand for LSTs change, the protocol can adjust branch parameters or rely more on the other
markets. The CollateralRegistry’s redemption split ensures no single collateral’s weakness collapses
the peg.



[42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins) [1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch)



[41](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=Redemptions%20serve%20the%20crucial%20purpose,centralized%20assets%20or%203rd%20parties)



[42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins)



[41](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=Redemptions%20serve%20the%20crucial%20purpose,centralized%20assets%20or%203rd%20parties) [42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins)



[5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP) [6](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=How%20is%20the%20collateral%20split,determined)



set so that redemptions remain profitable whenever BOLD < \$1, but vanish when BOLD ≥ \$1,



[67](https://docs.liquity.org/v2-faq/bold-and-earn#:~:text=What%20is%20BOLD%E2%80%99s%20peg%20mechanism%3F) [26](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=In%20Liquity%20V2%2C%20trove%20owners,However%2C%20users%20are%20also)



[67](https://docs.liquity.org/v2-faq/bold-and-earn#:~:text=What%20is%20BOLD%E2%80%99s%20peg%20mechanism%3F)



In sum, Liquity V2’s backing mechanism — combining strict overcollateralization, a decentralized
redemption market, and an adaptive interest system — is engineered for sustainable peg stability. The
system documentation and audits emphasize this design: “The system is designed to always be overcollateralized and BOLD is fully redeemable [42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins) ”, and “redemptions are managed by the CollateralRegistry
aiming to restore the BOLD peg and reduce unbackedness [43](https://github.com/liquity/bold#:~:text=,BOLD%20in%20the%20branch%E2%80%99s%20SP) ”. The result is a stablecoin that maintains a
hard \$1 floor without relying on central reserve assets.



[42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins)



[43](https://github.com/liquity/bold#:~:text=,BOLD%20in%20the%20branch%E2%80%99s%20SP)


## **References**



Key protocol sources have been used to assemble this analysis. Core details are drawn directly from
Liquity’s **official repository** and documentation [1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch) [42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins), as well as protocol FAQs [41](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=Redemptions%20serve%20the%20crucial%20purpose,centralized%20assets%20or%203rd%20parties) [6](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=How%20is%20the%20collateral%20split,determined) . Audit and formal
reports (ChainSecurity, Dedaub) confirm and explain the mechanisms [68](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=1.%20Multi,and%20change%20their%20annual%20interest) [5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP) . The interested reader may
consult the Liquity GitHub (liquity/bold) for full contract logic and the Liquity V2 whitepaper/docs for

additional context.



[1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch) [42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins) [41](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=Redemptions%20serve%20the%20crucial%20purpose,centralized%20assets%20or%203rd%20parties) [6](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=How%20is%20the%20collateral%20split,determined)



[68](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=1.%20Multi,and%20change%20their%20annual%20interest) [5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP)



7


[1](https://github.com/liquity/bold#:~:text=separately%20with%20its%20own%20Minimum,active%20Troves%20in%20that%20branch) [3](https://github.com/liquity/bold#:~:text=,deployed%20for%20each%20collateral%20%E2%80%9Cbranch%E2%80%9D) [8](https://github.com/liquity/bold#:~:text=%2A%20%60CollateralRegistry%60%20,proportion%20to%20their%20%E2%80%9Coutside%E2%80%9D%20debt) [9](https://github.com/liquity/bold#:~:text=%2A%20%60BorrowerOperations%60,the%20ActivePool%20to%20mint%20interest) [10](https://github.com/liquity/bold#:~:text=%2A%20%60TroveManager%60%20,to%20move%20collateral%20or%20BOLD) [12](https://github.com/liquity/bold#:~:text=1.%20Offset%20under,Troves%20in%20the%20same%20branch) [13](https://github.com/liquity/bold#:~:text=%2A%20%60SortedTroves%60%20,list%20slices) [14](https://github.com/liquity/bold#:~:text=%2A%20%60ActivePool%60%20,currently%2C%20to%20MockInterestRouter) [15](https://github.com/liquity/bold#:~:text=%2A%20%60CollSurplusPool%60%20,surplus%20when%20they%20claim%20it) [16](https://github.com/liquity/bold#:~:text=Liquidation%20gas%20compensation) [17](https://github.com/liquity/bold#:~:text=,accept%20native%20ETH%20as%20collateral) [19](https://github.com/liquity/bold#:~:text=%2A%20%60CompositePriceFeed%60%20,min%28market_price%2C%20exchange_rate_price) [20](https://github.com/liquity/bold#:~:text=%2A%20%60WSTETHPriceFeed%60%20,collateral%20on%20a%20WSTETH%20branch) [21](https://github.com/liquity/bold#:~:text=,collateral%20on%20the%20WETH%20branch) [22](https://github.com/liquity/bold#:~:text=,branch%20as%20quickly%20as%20possible) [23](https://github.com/liquity/bold#:~:text=Upon%20opening%20a%20Trove%20by,90%20BOLD%20against%20it) [24](https://github.com/liquity/bold#:~:text=%2A%20User,is%20periodically%20minted%20as%20BOLD) [27](https://github.com/liquity/bold#:~:text=given%20Trove%20debt%2C%20interest%20accrues,as%20the%20Trove%20isn%E2%80%99t%20altered) [29](https://github.com/liquity/bold#:~:text=,SP%20on%20that%20same%20branch) [30](https://github.com/liquity/bold#:~:text=,they%20make%20a%20premature%20adjustment) [31](https://github.com/liquity/bold#:~:text=,equal%20to%207%20days%20of) [32](https://github.com/liquity/bold#:~:text=,mints%20BOLD%20stablecoins%20to%20the) [33](https://github.com/liquity/bold#:~:text=,control%20debt%20and%20collateral%20adjustments) [34](https://github.com/liquity/bold#:~:text=,the%20delegates%27s%20interest%20rate%20adjustments) [35](https://github.com/liquity/bold#:~:text=_upperHint%2C%20uint256%20_lowerHint%2C%20uint256%20_maxUpfrontFee,date) [36](https://github.com/liquity/bold#:~:text=,MIN_DEBT) [37](https://github.com/liquity/bold#:~:text=,If) [38](https://github.com/liquity/bold#:~:text=This%20is%20calculated%20in%20) [40](https://github.com/liquity/bold#:~:text=Redistribution%20is%20performed%20in%20a,TroveManager.getEntireDebtAndColl) [42](https://github.com/liquity/bold#:~:text=1,value%20of%20the%20issued%20stablecoins)


[43](https://github.com/liquity/bold#:~:text=,BOLD%20in%20the%20branch%E2%80%99s%20SP) [46](https://github.com/liquity/bold#:~:text=,at%20all%20for%20redemption%20ordering) [50](https://github.com/liquity/bold#:~:text=The%20Liquity%20v2%20system%20prices,and%20is%20vulnerable%20to%20liquidation) [51](https://github.com/liquity/bold#:~:text=,for%20a%20given%20branch) [53](https://github.com/liquity/bold#:~:text=system%E2%80%99s%20TCR%20,interest%20rate%20increases%20and%20in) [54](https://github.com/liquity/bold#:~:text=When%20a%20Trove%E2%80%99s%20collateral%20ratio,IDs%20to%20attempt%20to%20liquidate) [55](https://github.com/liquity/bold#:~:text=If%20the%20liquidated%20debt%20is,active%20Troves%20in%20the%20branch) [56](https://github.com/liquity/bold#:~:text=Separate%20liquidation%20penalty%20percentages%20are,%60LIQUIDATION_PENALTY_SP%60%20and%20%60LIQUIDATION_PENALTY_REDISTRIBUTION) [57](https://github.com/liquity/bold#:~:text=back%20,always%20seized%20in%20Normal%20Mode) [58](https://github.com/liquity/bold#:~:text=In%20a%20mixed%20offset%20and,that%20is) [59](https://github.com/liquity/bold#:~:text=When%20a%20Trove%20is%20opened%2C,ICR%20or%20the%20TCR%20calculations) [60](https://github.com/liquity/bold#:~:text=The%20collateral%20portion%20of%20the,2%20units%20of%20the%20LST) [61](https://github.com/liquity/bold#:~:text=Minimum%201%20BOLD%20token%20in,the%20SP) [62](https://github.com/liquity/bold#:~:text=,the%20offset%20boundary%20has%20shifted) [64](https://github.com/liquity/bold#:~:text=When%20a%20liquidation%20occurs%2C%20rather,corresponding%20to%20the%20collateral%20gain) [65](https://github.com/liquity/bold#:~:text=Stability%20Pool%20depositors%20can%20expect,take%20a%20value%20above%20100) [66](https://github.com/liquity/bold#:~:text=BOLD%20Yield%20Gains) GitHub - liquity/bold: Liquity v2 monorepo

containing the contracts, subgraph and frontend.


[https://github.com/liquity/bold](https://github.com/liquity/bold)



[2](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=Liquity%20V2%20supports%20multiple%20collateral,it%20is%20impossible%20to%20add) [4](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=1.%20Multi,handled%20within%20the%20same%20branch) [5](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20CollateralRegistry%20is%20now%20the,SP) [7](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=CollSurplusPool,to%20add%20any%20new%20collateral) [11](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=,49) [18](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=handled%20within%20the%20same%20branch,but%20not%20native%20ETH) [25](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=2,to%20choose%20higher%20interest%20rates) [26](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=In%20Liquity%20V2%2C%20trove%20owners,However%2C%20users%20are%20also) [28](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=This%20expression%20is%20then%20used,it%20requires%20user%20action%20to) [39](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=The%20contract%20stores%20the%20total,to%20how%20collateral%20gains%20are) [44](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=Example%3A%20Two%20active%20collateral%20branches%2C,as%20that%20of%20branch%201) [47](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=Redemptions%20in%20each%20branch%20still,the%20lowest%20collateral%20ratio%20trove) [52](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=12,compensation%20in%20a%20mix%20of) [68](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4#:~:text=1.%20Multi,and%20change%20their%20annual%20interest)



files.gitbook.com



[https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4)


[spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4)


[alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE2A1Xrcj7XasxOiotWky%2Fuploads%2F7ELJ5yuvXnUtgd9NQPHk%2FChainSecurity_Liquity_Bold_audit.pdf?alt=media&token=eb681c56-e650-499b-aaca-7099823e08c4)



[6](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=How%20is%20the%20collateral%20split,determined) [41](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=Redemptions%20serve%20the%20crucial%20purpose,centralized%20assets%20or%203rd%20parties) [45](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=To%20mitigate%20this%20risk%2C%20the,Pool%20for%20that%20borrowing%20market) [48](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=You%20can%20think%20of%20redemptions,of%20your%20collateral%20in%20return) [49](https://docs.liquity.org/v2-faq/redemptions-and-delegation#:~:text=,ETH%20collateral%2C%2020%27000%20BOLD%20debt)



Redemptions and Delegation | Liquity Docs



[https://docs.liquity.org/v2-faq/redemptions-and-delegation](https://docs.liquity.org/v2-faq/redemptions-and-delegation)



[63](https://docs.liquity.org/v2-faq/bold-and-earn#:~:text=The%20yield%20comes%20from%20two,sources) [67](https://docs.liquity.org/v2-faq/bold-and-earn#:~:text=What%20is%20BOLD%E2%80%99s%20peg%20mechanism%3F)



BOLD & Earn | Liquity Docs



[https://docs.liquity.org/v2-faq/bold-and-earn](https://docs.liquity.org/v2-faq/bold-and-earn)



8


