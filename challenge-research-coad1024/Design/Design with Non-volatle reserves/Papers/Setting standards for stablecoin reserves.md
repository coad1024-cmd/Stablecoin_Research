# Setting Standards for Stablecoin Reserves

**Authors:** Christian Catalini, Nihar Shah  
**Date:** November 24, 2021

## Abstract

US regulators have suggested that only FDIC-insured financial institutions be allowed to issue stablecoins. We propose an alternative path, which provides similar guarantees in terms of financial resilience, but without the same narrow restriction on issuers and negative consequences on innovation and competition. Stablecoin issuers should comply with the capital and liquidity standards encoded in the Basel accords, and put aside appropriate capital buffers to mitigate credit risk, market risk, and operational risk. Furthermore, stablecoin issuers should hold appropriate liquidity to mitigate sudden redemptions and outflows. While many existing stablecoin issuers would struggle to comply with such standards under their current reserve design, they could successfully comply under a simpler balance sheet centered around short-maturity, high-quality, and liquid assets such as 3 months or less U.S. Treasuries.

---

## 1 Introduction

Worth under $10 million just five years ago, stablecoins are suddenly a mainstream asset class, with a market capitalization well over $100 billion today. But this new prominence brings increased scrutiny from policymakers – most recently from the President’s Working Group (2021). In addition to well known illicit finance concerns, the President’s Working Group identified three key dimensions of risk for stablecoins: loss in value of the coins, failures in the payments system, and amplified risks for large scale systems. Focusing on the first two risks, they recommend that only banks issue stablecoins:

> Legislation should limit stablecoin issuance, and related activities of redemption and maintenance of reserve assets, to entities that are insured depository institutions. The legislation would prohibit other entities from issuing payment stablecoins.

At face value, this recommendation makes sense. While stablecoin issuers point to price histories or high-level audits to build confidence, this is unlikely to be enough as coins move beyond crypto use cases and are used for mainstream payments. As the history of financial institutions painfully reminds us, balance sheets need to be able to withstand financial distress, operational failures, and more to foster trust.

At the same time, limiting the issuance of stablecoins to banks also has significant side-effects. It limits competition and innovation to incumbents, and decreases the likelihood that consumers and businesses will benefit from lower costs and new types of products and services.

But there is another path that can both minimize risk and unlock innovation: stablecoin issuers should follow established bank standards for their reserves. More specifically, regulators could build on the guidelines developed by the Basel Committee on Banking Supervision (“Basel accords”) to harmonize reserve designs. These standards have been developed and improved over the last fifty years to keep financial institutions solvent and liquid through a variety of distressed scenarios. With some adjustments and extensions, they therefore provide a rigorous and effective approach to regulating stablecoins.

## 2 A Short Primer on Capital and Liquidity Requirements

The Basel accords focus on capital and liquidity requirements, which are essential for banks to remain solvent and liquid through distress. Consider first capital requirements, which focus on defining an appropriate capital buffer for a bank’s balance sheet. Conceptually, a capital buffer refers to extra assets on the balance sheet that are not associated with liabilities. Such a buffer is critical to absorb unexpected losses.

Take a simple example: a bank that collects $100 in cash from the public, in exchange for $100 in deposits. This bank has no excess assets on its balance sheet, and thus no capital buffer. Should the bank lose $1 of assets (due to, say, theft), the bank would hold fewer assets than liabilities, become insolvent and immediately be vulnerable to a run.

**Scenario 1: No Capital Buffer**
```
Assets      | Liabilities
$100 Cash   | $100 Deposits
```
*After losing $1:*
```
Assets      | Liabilities
$99 Cash    | $100 Deposits
```

Now, suppose the same bank had raised $2 from its shareholders without issuing them deposit liabilities. In this scenario, the bank has $2 in excess, or $2 capital buffer. Should the bank lose $1 in assets, it would still hold more assets than liabilities and remain solvent. This illustrates the critical role of a capital buffer.

**Scenario 2: With Capital Buffer**
```
Assets      | Liabilities
$102 Cash   | $100 Deposits
            | $2 Capital
```
*After losing $1:*
```
Assets      | Liabilities
$101 Cash   | $100 Deposits
            | $1 Capital
```

Next, consider liquidity requirements, which focus on ensuring an institution can meet unexpected redemptions of its deposits. A bank that holds a large share of illiquid assets would be unable to redeem a sizable share of its deposits. To illustrate, consider a bank with no capital buffer that takes $100 in cash in exchange for $100 in deposit slips, and then invests the $100 in residential mortgages. Should depositors redeem unexpectedly, the bank will be forced to sell some of its mortgages quickly, but since mortgages are hard-to-value assets, it will likely not get fair market price and have to sell the mortgages at a discount. This would make the bank insolvent and immediately vulnerable to a run.

**Scenario 3: Illiquid Assets**
```
Assets          | Liabilities
$100 Mortgages  | $100 Deposits
```
*Forced sale:*
```
Assets          | Liabilities
$1 Cash         | $100 Deposits
$99 Mortgages   |
```

Now, suppose the bank purchased mortgages, but also held an appropriate part of its balance sheet in cash. Cash offers easy access to liquidity to meet redemptions, and helps the bank meet its obligations without triggering insolvency. This illustrates the importance of liquidity standards.

**Scenario 4: With Liquidity**
```
Assets          | Liabilities
$10 Cash        | $100 Deposits
$90 Mortgages   |
```
*After redemption:*
```
Assets          | Liabilities
$9 Cash         | $99 Deposits
$90 Mortgages   |
```

## 3 Applying the Basel Framework to Stablecoins

The Basel accords are primarily focused on ensuring solvency and that financial institutions have enough capital to hedge risks. These risks are the same stablecoin issuers face: credit risk, market risk, and operational risk. The guidance is risk-sensitive, meaning that larger risks need to be offset by larger capital requirements. Riskier assets on a balance sheet or, similarly, an increase in the riskiness of the existing assets need to be met with a larger capital buffer.

The first category of risk is credit risk, or the risk that the backing assets will partially or fully default. For each dollar of assets on a balance sheet, the accords prescribe some amount of capital to be held against the risk of default.

The following table illustrates requirements for a range of assets (normalized as required capital per $100 of underlying assets). Many of these assets are commonly held by existing stablecoin issuers. As evident from the table, riskier assets such as commercial paper require substantially more capital than creditworthy assets such as Treasury bonds.

| Underlying Asset | Credit Risk-Based Capital Per $100 |
| :--- | :--- |
| Treasury bonds | $0.00 |
| Deposits with the Federal Reserve | $0.00 |
| Deposits with highly-rated bank | $1.60 |
| Commercial paper rated A-1/P-1 | $1.60 |
| Commercial paper rated A-2/P-2 | $4.00 |
| Commercial paper rated A-3/P-3 | $8.00 |
| Bitcoin and other cryptocurrencies | $100.00 |

Stablecoin issuers that hold riskier assets without a corresponding increase in capital buffer are at risk of becoming insolvent and exposed to a run.

The second category of risk is market risk, or the risk that the market price of the backing assets will fall. For each dollar of assets, Basel prescribes some amount of capital to hold against market shocks, with larger requirements associated with more volatile assets.

Stablecoin issuers often hold fixed-rate assets such as commercial paper or Treasury bonds. As a result, their core market risk is interest rate risk, or the risk that interest rates will rise and the assets will fall in price. The following table illustrates requirements for different maturities of fixed-rate assets (normalized as required capital per $100 of the underlying assets).

| Underlying Maturity | Interest Risk-Based Capital Per $100 |
| :--- | :--- |
| 0-1 Months | $0.12 |
| 1-3 Months | $0.48 |
| 3-6 Months | $1.03 |
| 6-12 Months | $1.84 |
| 12-36 Months | $3.90 |

Stablecoin issuers that hold longer maturity assets without increasing their capital buffer, are at greater risk of insolvency and a run.

The third category of risk is operational risk, or the risk that internal processes, people, or systems will fail. This serves as a catch-all bucket for operational failures, such as wrongful termination lawsuits, theft, government fines, and much more. While the Basel accords include risks typically encountered by banks, these risks do not always translate to stablecoins. Stablecoins issuers may need more bespoke approaches that cover novel categories of risk such as bugs in smart contracts, problems with network validators, unauthorized or impeded minting and burning operations, vulnerabilities in cryptographic primitives, financial crime risks and more.

The Basel framework also offers guidance on aggregating categories of risk, and introduces the concept of a “leverage ratio”, i.e. a minimum capital requirement that is completely risk-insensitive and directly grows with the size of a balance sheet. This type of ratio was designed for institutions that have complex balance sheets, and is unsuited for stablecoin issuers that do not engage in extensive maturity transformation and only invest in short term U.S. Treasuries. If applied to stablecoins, it could make them commercially non-viable.

To identify unexpected weaknesses in a balance sheet, the Basel framework relies on stress tests which typically include some combination of credit, market, and operational shocks, as well other shocks to the underlying business or economy. In the case of stablecoins, for example, stress tests reveal that sudden expansions in supply can be as problematic as contractions, as they require issuers to raise capital quickly to grow their capital buffer. While stopping minting may seem an appealing way to slow down growth, it would be a disastrous one as it would lead to the stablecoin breaking its peg upwards.

The Basel accords also focus on ensuring that financial institutions have enough liquidity to meet unexpected outflows. They rely on two key metrics to measure liquidity, one of which is highly relevant to stablecoin issuers. This metric is the liquidity coverage ratio, which ensures that banks have enough “hiqh-quality, liquid assets” (HQLAs), i.e. assets that can be easily sold for cash to meet prolonged and extensive redemptions. This prevents a bank from having to sell less liquid assets at a discount, and potentially being unable to meet redemptions altogether. Formally, the ratio is computed as the stock of HQLAs divided by the net cash outflows over the next thirty days, and it should always exceed 100%. The framework also computes a worst-case scenario for net cash outflows, where a bank’s creditors who are considered flighty (e.g. institutional investors) raise the net cash outflow totals more than creditors who are considered sticky (e.g. retail depositors). Finally, cash that a bank holds in other banks’ accounts qualifies as a special category: rather than adding to the stock of HQLAs, it can lower the net cash outflows – but only up to a point.

## 4 Towards an Ideal Reserve Design

The framework outlined so far can not only be applied to existing stablecoins, but also provides guidance on what an ideal reserve balance sheet should look like.

For instance, consider Tether, who released a breakdown of its reserves as of June 30, 2021. Tether had approximately $63 billion in assets, of which they provided sufficient detail on some $53.4 billion to estimate capital and liquidity requirements. This portion of Tether’s balance sheet consisted of cash and bank deposits, commercial paper, short-maturity Treasury bonds, and reverse repos.

In total, these generate estimated capital requirements amounting to 2.9% of Tether’s balance sheet (excluding additional capital needed to cover operational risk), and they generate an estimated liquidity coverage ratio between 58% and over 100%, depending on exactly how flighty Tether’s liabilities actually are. It is likely that the estimated capital requirements and liquidity coverage ratio respectively rise and fall when expanded to Tether’s entire balance sheet, as the remaining portion of the balance sheet includes secured loans, precious metals, cryptocurrencies, and other assets that are substantially riskier and less liquid.

Alternatively, consider USDC, who released a breakdown of its reserves as of September 30, 2021. USDC had $31.7 billion in assets, all held as cash and cash equivalents. In total, these generate estimated capital requirements under the Basel framework amounting to 1.6% of Circle’s balance sheet (again excluding additional capital needed to cover potential operational risk losses), and generate an estimated liquidity coverage ratio of 0%.

A simpler solution, originally proposed by Diem, is to hold a balance sheet that is almost entirely short-term Treasury bills, with a small allocation to cash. For instance, suppose a balance sheet that is held 90% in Treasury bills with a residual maturity of under three months, and 10% in cash at a well-rated financial institution. This balance sheet would have a capital requirement that is under 0.5% of its balance sheet (holding aside operational risk-based capital) and a liquidity coverage ratio that is always over 100%, regardless of the treatment that regulators apply to stablecoin liabilities.

This makes for a safer reserve, reducing the capital and liquidity burdens on the issuer, while ensuring that the underlying coin can withstand severe distress.

While at face value, the simplest solution may seem for a stablecoin issuer to back a stablecoin with cash at one or more commercial banks, this introduces a different set of challenges. Cash at a bank has no interest rate risk, appears fully liquid, and benefits from protections by the Federal Deposit Insurance Corporation (FDIC). At the same time, there are three shortcomings to an all-cash balance sheet for a stablecoin.

First, while consumers are protected by FDIC, institutions are not. As such, if a bank goes bankrupt, a stablecoin’s cash deposit may be lost. Second, banks do not want to hold a large amount of cash because it comes with large capital requirements, and in a low interest rate environment can be completely uneconomical. Third, cash may not be as liquid as it appears. The liquidity standards in the Basel accords do not allow for unrestricted usage of cash to meet the liquidity coverage ratio, as stablecoin issuers run the risk that a bank may suspend access to its deposits – particularly if the bank is undergoing the same liquidity crunch that the stablecoin issuer is facing.

This calculus would rapidly change if stablecoin issuers could hold deposits directly with the central bank. Cash held with the central bank has no credit risk, and unlike private banks, the central banks typically do not limit the amount of cash that financial institutions hold with them, nor suspend access to those deposits. Indeed, such a reserve would be almost riskless, and stablecoin issuers would only have to hold a capital buffer to cover operational risks. However, while central banks are exploring ways to support central bank digital currencies and expand access to fintech players, stablecoin issuers do not have access to central banks today. As a result, the best design remains one that relies on high quality, liquid assets, such as short term U.S. Treasuries.

While the President’s Working Group has correctly identified issues with the status quo, the cure should not restrict innovation to incumbents. The Basel accords offer a number of ideas on how to design safer stablecoins that can withstand stressed market conditions. Expanding the framework and using it for a new type of bank charter that takes a “same risks, same rules” approach but also does not block entry by new players may be a more promising avenue for supporting competition and innovation in payments and financial services.

## References

Basel Committee on Banking Supervision. Basel III: The Liquidity Coverage Ratio and liquidity risk monitoring tools. Technical report, Jan. 2013.

Basel Committee on Banking Supervision. Basel III: The net stable funding ratio. Technical report, Oct. 2014.

Basel Committee on Banking Supervision. CRE20 - Standardised approach: individual exposures. Technical report, Dec. 2019a.

Basel Committee on Banking Supervision. CRE21 - Standardised approach: use of external ratings. Technical report, Dec. 2019b.

Basel Committee on Banking Supervision. MAR10 - Definition and application for market risk. Technical report, Dec. 2019c.

Basel Committee on Banking Supervision. MAR20 - Standardised approach. Technical report, Dec. 2019d.

Basel Committee on Banking Supervision. MAR30 - Internal models approach: general provisions. Technical report, Dec. 2019e.

Basel Committee on Banking Supervision. OPE25 - Standardised approach. Technical report, Dec. 2019f.

Basel Committee on Banking Supervision. SRP31 - Interest rate risk in the banking book. Technical report, Dec. 2019g.

Basel Committee on Banking Supervision. Prudential treatment of cryptoasset exposures. Technical report, Sept. 2021.

C. Catalini and J. Massari. Stablecoins and the Future of Money. Harvard Business Review, Aug. 2021. ISSN 0017-8012. URL https://hbr.org/2021/08/stablecoins-and-the-future-of-money. Section: Economics.

Grant Thornton. Circle Examination Report - September 2021. Technical report, Oct. 2021.

Moore Cayman. Tether Assurance: Consolidated Reserves Report as of June 30, 2021. Technical report, Aug. 2021.

President’s Working Group on Financial Markets, the Federal Deposit Insurance Corporation, and the Office of the Comptroller of the Currency. Report on Stablecoins. Technical report, Nov. 2021.

The Block. Total Stablecoin Supply. URL https://www.theblockcrypto.com/data/decentralized-finance/stablecoins.
