# Sky Ecosystem: Backing Mechanism Profile (Part I)

**Authors**: Research Challenge Team
**Date**: January 2026
**Series**: Sky Research Series (Part I)

---

## 1. Executive Verdict

**Status:** 🟡 **Structurally Robust / Politically Fragile**

The Sky Backing Mechanism passes the "Kinetic Audit" with flying colors. The transition to Liquidation 2.0 has fixed the mechanical throughput issues of 2020. However, the backing portfolio has shifted from **Trustless Volatility** (ETH) to **Trusted Stability** (USDC/RWA). The risk is no longer that the "Machine Breaks" (Backing Physics), but that the "Assets Freeze" (Decentralization).

### The Solvency Lens

* **Kinetic Solvency (Physics)**: **Robust**. The auction engine can clear bad debt in 1 block via Flash Loans.
* **Static Solvency (Assets)**: **Fragile**. 42%+ of assets are centrally custodial.

---

## 2. Backing Scorecard (Pillar I)

| Dimension | Score (0-10) | Status | Key Driver |
| :--- | :--- | :--- | :--- |
| **Asset Quality** | **8/10** | 🟢 **Liquid** | 60% HQLA (Treasuries/USDC). 40% Crypto (ETH). Zero Governance Token backing. |
| **Custody Risk** | **2/10** | 🔴 **Critical** | Type C (Hybrid). 42% of assets (USDC) are essentially "Bank Deposits" subject to seizure. |
| **Engine Speed** | **9/10** | 🟢 **Atomic** | Dutch Auctions (`Clip`) allow Flash Loan liquidations (1-tx settlement). Solved Black Thursday congestion issues. |
| **Redemption LCR** | **9/10** | 🟢 **Robust** | PSM Pocket holds ~$4B USDC for instant 1:1 exit. |

---

## 3. Evidence Classification

### 3.1 Verified Facts (Type A)

* **F1 (Surplus):** The `Vow` holds ~$247M surplus cushion.
* **F2 (Bad Debt):** The system cleared the 2022/2023 crashes with minimal bad debt (<$5M).

### 3.2 Risk Scenarios (Type D)

* **Scenario A (The Freeze):** OFAC sanctions the RWA/USDC vaults.
  * *Result:* 42% of backing vanishes. Solvency ratio drops to 0.58.
  * *Defense:* None. Smart contracts cannot unfreeze a bank account.
* **Scenario B (The Crash):** ETH drops 50% in 1 hour.
  * *Result:* `Dog` initiates auctions. `Clipper` sells collateral via Dutch Auction.
  * *Throughput:* Validated. **Flash Loan Liquidity** allows keepers to clear debt without capital lockup. Risk of "Zero Bids" (Black Thursday) is effectively eliminated.

---

## 4. Conclusion

* **Is it backed?** Yes. Arithmetically.
* **Can you redeem it?** Yes. The PSM provides the deepest on-chain liquidity for stablecoin exit.
* **Is it safe?** Only if you accept the **Legal Jurisdiction** of the assets.

---

### Series Navigation

* **Part I: Backing Profile** (You are here)
* [Part II: Economic Sustainability Profile](../Sustainability/Artifact/Sky-Economic-Sustainability.md)
* [Part III: Decentralization Profile](../Decentralization/Artifact/Sky-Decentralization-DeepDive.md)
