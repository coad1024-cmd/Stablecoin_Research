# 🗳️ MakerDAO Governance Voter Turnout Analysis

**Generated on:** 2025-11-25

## 1. Executive Summary

This analysis examines the voter turnout and decentralization of MakerDAO governance based on a sample of **50 recent polls** (March - May 2025).

**Key Findings:**

* **Turnout is Consistent but Moderate:** Average turnout is **15.8%**, with a tight range (15-22%). This indicates a stable but relatively small subset of active MKR supply participating in governance.
* **High Centralization:** The top delegate consistently controls **~53-54%** of the vote share. This means a single entity effectively dictates the outcome of these polls.
* **Low Voter Count:** On average, only **10-12 unique addresses** vote per proposal. This reinforces the "whale-dominated" nature of the governance.

---

## 2. Detailed Metrics

| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Average Turnout** | **15.78%** | ~137,000 MKR voted out of ~872,000 supply. |
| **Median Turnout** | **15.37%** | Most polls cluster tightly around this figure. |
| **Max Turnout** | **22.05%** | Peak participation observed in Poll 1200. |
| **Avg Unique Voters** | **10** | Extremely low participation breadth. |
| **Avg Top Delegate Share** | **53.0%** | **CRITICAL RISK:** One delegate holds majority power. |

---

## 3. Visual Analysis & Chart Explanations

### A. Turnout Distribution

**What this chart shows:** The frequency of different turnout percentages.
**Analysis:** The histogram shows a very narrow spike around **15%**. This lack of variance suggests that the same block of large delegates votes on almost every proposal, with very little "organic" fluctuation from smaller holders.
![Turnout Distribution](file:///c:/Users/DELL/Desktop/Research%20Challenge/challenge-research-coad1024/analysis/makerdao/governance/plots/turnout_distribution.png)

### B. Top Delegate Dominance

**What this chart shows:** The percentage of the total vote contributed by the single largest voter (delegate) in each poll.
**Analysis:** The distribution centers around **54%**. In a "one token, one vote" system, any entity with >50% share has absolute control. This confirms that MakerDAO governance, for this period, was effectively determined by one dominant delegate (likely a major recognized delegate or a consolidated voting bloc).
![Delegate Dominance](file:///c:/Users/DELL/Desktop/Research%20Challenge/challenge-research-coad1024/analysis/makerdao/governance/plots/delegate_dominance_distribution.png)

### C. MKR Voted vs. Unique Voters

**What this chart shows:** A scatter plot comparing the number of unique voters (X-axis) to the total MKR weight voted (Y-axis).
**Analysis:** There is **no strong correlation**. You can have 10 voters or 16 voters, but the total MKR weight remains largely flat (~134k - 142k). This proves that the "long tail" of small voters contributes negligible weight compared to the whales. Adding more individual voters barely moves the needle on total turnout.
![Turnout vs Voters](file:///c:/Users/DELL/Desktop/Research%20Challenge/challenge-research-coad1024/analysis/makerdao/governance/plots/turnout_vs_voters_scatter.png)

---

## 4. Proposal Breakdown (Sample)

*Top 10 recent polls by date*

| Date | ID | MKR Voted | Turnout | Voters | Title |
|---|---|---|---|---|---|
| 2025-05-12 | 1247 | 134,055 | 15.37% | 12 | SparkLend Ethereum - Adjust DAI Interest Rate Model |
| 2025-05-12 | 1253 | 134,055 | 15.37% | 12 | Spark Liquidity Layer Mainnet and Unichain |
| 2025-05-12 | 1252 | 134,055 | 15.37% | 12 | Spark Liquidity Layer Base - Spark USDC Morpho |
| 2025-05-12 | 1254 | 134,055 | 15.37% | 12 | Spark Liquidity Layer Mainnet and OP Mainnet |
| 2025-05-12 | 1250 | 134,055 | 15.37% | 12 | Spark Liquidity Layer Mainnet - Increase USDS Mint |
| 2025-05-12 | 1249 | 134,055 | 15.37% | 12 | SparkLend Ethereum - Reduce WBTC Liquidation |
| 2025-05-12 | 1248 | 134,055 | 15.37% | 12 | SparkLend Ethereum - Adjust USDS Interest Rate |
| 2025-05-05 | 1245 | 134,259 | 15.39% | 13 | Atlas Edit Weekly Cycle Proposal - May 5, 2025 |
| 2025-04-28 | 1244 | 134,175 | 15.38% | 12 | Atlas Edit Weekly Cycle Proposal - April 28, 2025 |
| 2025-04-21 | 1238 | 134,109 | 15.37% | 13 | SparkLend Ethereum - Adjust USDT Cap Automator |

---

## 5. Conclusion

The data paints a picture of a **highly efficient but centralized** governance system. While "voter apathy" (low turnout) is a common critique, the bigger issue here is **delegate concentration**. With a single delegate holding >50% power, the "voting" process is effectively a formality unless that delegate is split or contested. The low unique voter count (avg 10) further suggests that governance is the domain of a very small circle of professional participants.
