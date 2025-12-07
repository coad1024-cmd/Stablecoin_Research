# DAI at the Crossroads, Part I: Where Sky's Solvency Lives On-Chain (and Where It Doesn't)


**Title:** DAI at the Crossroads, Part I: Where Sky's Solvency Lives On-Chain (and Where It Doesn't)

**Subtitle:** A three-part technical series unpacking Sky Ecosystem's architecture—from its on-chain reserves to its evolving sustainability model and the governance layer that now defines its credibility.

**Target Audience:** Senior Solidity devs, protocol engineers, DeFi risk teams.

**Publication Note:** October 29, 2025

---

## Introduction: The Evolution of "Backed"

[On March 12, 2020, ETH crashed 43% in a matter of hours](https://www.coindesk.com/tech/2020/03/12/defi-leader-makerdao-weighs-emergency-shutdown-following-eth-price-drop).[16].[Thousands of MakerDAO vaults—each holding Ethereum as collateral for DAI debt—suddenly became underwater](https://repositum.tuwien.at/handle/20.500.12708/18324). But here's the critical moment: [the liquidation didn't happen instantly](https://repositum.tuwien.at/handle/20.500.12708/18324).[2] The oracle delay meant the on-chain system didn't *know* about the crash for another hour. By the time liquidations began, the collateral had fallen so far that auctions couldn't cover the debt. The result: [$4-6M in unrecoverable losses](https://www.coindesk.com/tech/2020/03/12/defi-leader-makerdao-weighs-emergency-shutdown-following-eth-price-drop), forcing the system to dilute its governance token (`MKR`) by [~3% to recapitalize](https://repositum.tuwien.at/handle/20.500.12708/18324).[16][2] 

[Recent empirical research analyzing over 130,000 MakerDAO vaults confirms the systemic severity of these events](https://dr.ntu.edu.sg/server/api/core/bitstreams/37ceb6fd-f93a-41e0-96ab-84eab35621ac/content), quantifying average portfolio liquidation losses and auction dynamics on-chain <small>Chaleenutthawut et al. (2024) [NEW-REF]</small>
The crisis revealed that even perfect arithmetic—even an immutable invariant enforced in code—could fail when mechanism design met market reality. This was Black Thursday, and it fundamentally changed what "backed" means in DeFi.

**The Central Tension: From Collateral to Pragmatism**

Three years later, a similar moment tested a different backing model. On March 10, 2023, Silicon Valley Bank failed. Circle, which holds USDC collateral entirely in institutional deposits, disclosed that [$3.3B (8% of reserves) sat frozen at SVB](https://www.coindesk.com/tech/2020/03/12/defi-leader-makerdao-weighs-emergency-shutdown-following-eth-price-drop).[16] USDC instantly [depegged to $0.88](https://www.galaxy.com/insights/research/usdcs-fall-below-usd1-sends-ripples-across-defi?utm_source=chatgpt.com). DAI, which by then was [60% backed by USDC](https://docs.mai.finance/peg-stability-module) (via the Peg Stability Module), followed to $0.88.[10][25] But unlike Black Thursday—which was a mechanism failure—SVB was a backing failure. The collateral itself lost value. [Recovery came within hours of the Fed's emergency backstop](https://blockworks.co/news/makerdao-endgame-update), with both stablecoins returning to $1.00 by March 13, 5 AM UTC.[7] The second crisis revealed that even diversified backing has a fault line: custodial dependencies.

These two events anchor a larger story about the evolution of DAI's backing model. From 2017-2020, backing meant [pure crypto—over-collateralized ETH vaults, trustless but fragile](https://repositum.tuwien.at/handle/20.500.12708/18324).[2] From 2020-2023, it meant emergency pragmatism—the [PSM](https://github.com/makerdao/dss-lite-psm)(Peg Stability Module) [inverted the model on March 17, 2020](https://mirror.xyz/dewiz.xyz/cs-D34NCp2JK9oMs61oKV-YLbSXTsZyxjxt4l_hZW6c), swapping USDC directly for DAI with minimal fees, stable but custodial.[15][19] From 2023-2025, it has meant distributed risk—a portfolio spanning [crypto (38%), stablecoins (22%), and real-world assets (14%, ~$948M)](https://info.sky.money/collateral).[20] Each shift was forced by crisis. Each shift bought stability at the cost of decentralization. The question now is whether this hybrid model is sustainable.

**The Macro-Thesis: Series Overarching Argument**

This three-part series argues that **Sky Ecosystem's backing architecture has [pushed the frontier of mechanistic solvency verification—but at the cost of centralizing governance risk](https://tradedog.io/makerdao-announces-launch-season-of-endgame-plan/) in ways the system has not yet tested under sustained stress.**[5] The argument proceeds in three stages:

- **Part I** establishes that backing *can* be verifiable on-chain through deterministic mechanisms—Vat accounting, liquidation logic, oracle feeds, and terminal guarantees. These mechanisms are mathematically non-fudgeable.
- **Part II** demonstrates that [verifiable backing is not the same as sustainable backing](https://arxiv.org/abs/1906.02152). The [mechanisms fail under specific conditions: oracle lag exceeds the liquidation window, keeper liquidity dries up, network throughput constrains auction velocity, or off-chain collateral dependencies (USDC, RWA) snap](https://repositum.tuwien.at/handle/20.500.12708/18324).[4][2]
- **Part III** shows that resilience ultimately depends on governance discipline—the ability to adjust parameters before crises hit, to coordinate SubDAOs without succumbing to rent-seeking, and to [resist the urge to mint new governance tokens (`MKR` dilution)](https://blockworks.co/news/sky-dao-adoption) as a permanent solution to solvency shortfalls.[8]

The overarching tension: the system has optimized for *mechanism robustness* at the expense of *governance accountability*. This series traces that tradeoff.

**The Micro-Thesis: Part I's Specific Claim**

Part I answers a single, self-contained question: **How is backing actually enforced on-chain <small>([Maker Dao Docs](https://docs.makerdao.com/smart-contract-modules/shutdown/the-emergency-shutdown-process-for-multi-collateral-dai-mcd),[Sky Ecosystem Collateral](https://info.sky.money/collateral))</small>, and what makes it verifiable?** It establishes that Sky's backing is verifiable through three layers: (1) deterministic arithmetic [(the `Vat` invariant), (2) enforced liquidations (the `Dog` + `Clipper` auction system), and (3) terminal guarantees (Global Settlement)](https://docs.makerdao.com/smart-contract-modules/shutdown/the-emergency-shutdown-process-for-multi-collateral-dai-mcd#the-implementation-properties-of-emergency-shutdown). By the end of Part I, the reader understands *where* backing lives, *how* to verify it, and *why* it holds under normal market conditions. But Part I explicitly avoids answering what should happen when market conditions are not normal—that's Part II's domain.

**Historical Anchors: Why These Crises Shaped Current Design**

The current architecture can only be understood through its crisis history:

- **Black Thursday (March 12, 2020):** 4,600 vaults liquidated, $8.3M in collateral, $4-6M unrecovered because auctions couldn't find bidders (<sub>[Kjaer Thesis, Sec 4.2](https://repositum.tuwien.at/handle/20.500.12708/18324)[2], [CoinDesk (March 12, 2020)](https://coinlaw.io/makerdao-statistics/)[16]</sub>). The lesson: pure crypto backing becomes fragile under leverage and correlated crashes.
- **PSM Introduction (March 17, 2020):** Five days after Black Thursday, MakerDAO introduced the Peg Stability Module—a radical inversion of the vault model, allowing users to swap USDC for DAI at near-peg prices.(<sub>[GitHub: dss-lite-psm](https://github.com/makerdao/dss-lite-psm)[15], [Mirror.xyz: PSM Analysis](https://mirror.xyz/dewiz.xyz/cs-D34NCp2JK9oMs61oKV-YLbSXTsZyxjxt4l_hZW6c)[19]</sub>) The lesson: fast, arbitrage-driven stabilization is powerful, but it imports custodial risk.
- **[SVB Crisis (March 10-13, 2023](ttps://www.galaxy.com/insights/research/usdcs-fall-below-usd1-sends-ripples-across-defi?utm_source=chatgpt.com)):** USDC depegged to $0.88 because Circle's institutional deposits froze at SVB; DAI followed instantly; recovery happened only after Fed backstop. The lesson: diversification without off-chain risk management is incomplete.
- **Current State (October 2025):** Sky has implemented the Endgame plan, distributing backing across crypto (38%), stablecoins (22%), and RWAs (14%).[6][7] SubDAOs now manage different collateral silos. The bet: distributed risk beats concentrated risk.(<small>[CoinLaw, Collateral Stats](https://coinlaw.io/makerdao-statistics/)[1], [Sky Collateral Dashboard](https://info.sky.money/collateral)[20]</small>)

**By the end of Part I, you will understand**:

- **The `Vat` contract's design**: Why normalized debt via a global rate multiplier is gas-efficient, how it maintains the core invariant (`ink × spot ≥ art × rate`), and why this matters for Solidity developers  (<small>[MakerDAO Docs (2020) Smart Contracts](https://docs.makerdao.com/smart-contract-modules/vat) [12], [MakerDAO Docs (2019) Emergency Shutdown](https://docs.makerdao.com/smart-contract-modules/shutdown) [13]</small>)
- **How collateral enters and exits**: `Join adapters`, vault state machines, and the full liquidation pipeline from unsafe vault detection through auction settlement.(<sub>[Kjaer, Sec. 4.2, Liquidation System (PDF, p.48)](https://repositum.tuwien.at/bitstream/20.500.12708/18324/2/Quantitative%20Analysis%20of%20MakerDAOs%20Liquidation%20System.pdf#page=48) [2], [MakerDAO Docs: Liquidations](https://docs.makerdao.com/smart-contract-modules/liquidation-2.0/liquidations-2.0---clipper-auctions) [12])</sub>

- **How oracles create verifiable price feeds**: The Median aggregation strategy, the 1-hour `OSM` delay and its tradeoffs, and why oracle lag is a fundamental bottleneck (not a bug) (<small>[Kjaer, Sec. 4.3, Oracles (PDF, p.49)](https://repositum.tuwien.at/bitstream/20.500.12708/18324/2/Quantitative%20Analysis%20of%20MakerDAOs%20Liquidation%20System.pdf#page=49) [2], [CoinDesk Black Thursday](https://www.coindesk.com/tech/2020/03/12/defi-leader-makerdao-weighs-emergency-shutdown-following-eth-price-drop) [16]</small>)

- **How liquidations actually enforce solvency:** The `Dog` contract's role, the `Clipper` auction mechanism, partial fills, and why 2020's `Flipper` design was abandoned (<small>[Kjaer, Sec. 5.2, Clipper (PDF, p.56)](https://repositum.tuwien.at/bitstream/20.500.12708/18324/2/Quantitative%20Analysis%20of%20MakerDAOs%20Liquidation%20System.pdf#page=56) [2], [GitHub PSM](https://github.com/makerdao/dss-lite-psm) [15]</small>)

- **Alternative backing models:** The PSM's instant arbitrage, why it replaced slow vault liquidations, and what it costs in terms of centralization  (<small>[GitHub PSM](https://github.com/makerdao/dss-lite-psm) [15], [Mirror.xyz PSM Overview](https://mirror.xyz/dewiz.xyz/cs-D34NCp2JK9oMs61oKV-YLbSXTsZyxjxt4l_hZW6c) [19], [MAI Finance Docs](https://docs.mai.finance/peg-stability-module) [10]</small>)

- **Terminal guarantees:** Global Settlement's role as the ultimate backstop—deterministic proportional redemption when the system shuts down (<small>[MakerDAO Docs Emergency Shutdown](https://docs.makerdao.com/smart-contract-modules/shutdown) [12], [Tudhope Emergency Shutdown](https://andytudhope.github.io/community/faqs/emergency-shutdown/) [11]</small>)

- **Formal grounding:** A brief introduction to the Klages-Mundt framework, which will become critical in Part II for analyzing when mechanisms fail. (<small>[Klages-Mundt & Minca (2019), Sec 3.3](https://arxiv.org/pdf/1906.02152.pdf#page=6) [4], [Klages-Mundt Thesis (2021)](https://ecommons.cornell.edu/bitstreams/a4503e36-e8c1-47d8-8f35-e11796d8258c/download) [3]</small>)


You need to know this because governance decisions affecting DAI/USDS depend on understanding these mechanisms first. You can't assess whether a parameter change is safe without understanding what it affects.

**The Series Promise: What You Can Trust**

This series has a complete plan. Part I is not preliminary setup; it is a closed argument that gives you practical knowledge you can verify on-chain. Part II builds on it by exploring bottlenecks—it doesn't restart the discussion. Part III assumes both prior parts; it adds governance and incentive analysis on top of established mechanism and sustainability foundations  (<small>[Blockworks (One year into Sky)](https://blockworks.co/news/sky-dao-adoption) [8], [Token Vitals (Endgame Plan)](https://tokenvitals.com/blog/makerdao-endgame-plan-mkr-holders-defi) [9]</small>)  
You will not invest your time in a series that abandons you partway through.

After Part I, you will understand backing as a mechanistic system. Part II then asks: does this system remain backed under stress?

**The Bridge to Part II: Why You Should Return**

Part I closes by establishing a fact: Sky's mechanisms can enforce backing during normal market conditions. But markets are not always normal. [The oracle delay that protects users during ordinary volatility becomes a liability during crashes. The keeper liquidity that ensures fast liquidations during routine operations dries up when cascades overwhelm the network](https://repositum.tuwien.at/bitstream/20.500.12708/18324/2/Quantitative%20Analysis%20of%20MakerDAOs%20Liquidation%20System.pdf#page=49). The USDC backing that provides instant arbitrage creates a dependency that fails when institutions fail. Part II explores these failure modes—not as hypotheticals, but grounded in Black Thursday and SVB empirics<small> ([CoinDesk Black Thursday](https://www.coindesk.com/tech/2020/03/12/defi-leader-makerdao-weighs-emergency-shutdown-following-eth-price-drop) [16], [Galaxy Digital SVB/USDC Depeg](https://www.galaxy.com/insights/research/usdcs-fall-below-usd1-sends-ripples-across-defi?utm_source=chatgpt.com) [25]</small>). It applies the Klages-Mundt framework to quantify when submartingale (stable) regimes flip to supermartingale (unstable) regimes. By then, the question shifts: mechanisms can verify backing, but can they *sustain* it?  <small> ([Klages-Mundt & Minca (2019) regime analysis](https://arxiv.org/pdf/1906.02152.pdf#page=6) [4], [Klages-Mundt Thesis (2021)](https://ecommons.cornell.edu/items/8f5ed403-6b8a-4e09-b436-16e61e3ce549) [3])</small>


**Tone & Authority: How to Read This Series**

This series is technical but not academic. It speaks to practitioners—engineers, risk analysts, protocol designers—who need to understand Sky's architecture deeply enough to make governance decisions or audit smart contracts.[9] It does not assume you have read the Klages-Mundt papers or memorized MakerDAO's governance history, but it will reference both. Code snippets are shown for pedagogical clarity, not production use. Crisis examples (Black Thursday, SVB) are used as proof points, not as scare tactics.

---


---

