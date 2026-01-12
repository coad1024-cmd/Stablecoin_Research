# General Backing Framework: The Kinetic Solvency Audit (Pillar I)

**Status:** Hardened Audit Tool
**Philosophy:** "Trust is a vulnerability. Verification is the only defense."
**Scope Distinctness:**

* **Backing Framework (Technical):** Focuses on the **Mechanism**. (Code, Invariants, Liquidation Logic, Throughput). "Does the machine work?"
* **Sustainability Framework (Economic):):** Focuses on the **Model**. (Business Model, Profitability, Yield, Solvency). "Is the business viable?"
* **Decentralization Framework (Political):** Focuses on **Control**. (Admin Keys, Custody, Governance). "Who holds the gun?"

## 1. The Interrogation Objective

Most frameworks ask "How does it work?" avoiding the real question: **"How does it die?"**
Your job is to test the **Liquidation Engine**.

**The Core Axiom:** Every stablecoin behaves like a risky bond.

* **Face Value:** $1.00.
* **Risk:** Duration, Credit, Liquidity.
* **Verdict:** Is the collateral recoverable during a Black Swan?

## 2. Structural Taxonomy (Know Your Enemy)

Risk profile defines the stress test.

* **Type A: Legal Fiction (Fiat-Backed)**
  * *Constraint:* You cannot audit the money. You audit the *lawyer*.
  * *Failure Mode:* Seizure, Regulatory Freeze, Bank Run (SVB).
* **Type B: The Casino (Crypto-Backed)**
  * *Constraint:* The collateral is correlated with the market crash.
  * *Failure Mode:* Liquidation Cascade, Oracle Latency, Smart Contract Bug.
* **Type C: The Chimera (Hybrid)**
  * *Constraint:* Imports the worst risks of both. Censorship of Type A + Volatility of Type B.
  * *Failure Mode:* All of the above.

## 3. Pillar I: The Balance Sheet (Static Audit)

*Do not look at the Dashboard. Look at the Contract.*

### A. Asset Quality: The "Liquidation Value" Test

**Metric:** **WACS (Weighted Average Credit Score)** is trash if you don't discount for liquidity.
**The Ruthless Rule:** Mark every asset to its **Fire Sale Value**.

* **Treasuries:** 98% (Slippage negligible).
* **ETH:** 70% (Assume 30% crash).
* **Altcoins/Governance Tokens:** 0%. **Yes, 0%.** If your stablecoin needs SHIB to stay solvent, it's already dead.
* **RWA (Private Credit):** 0%. It's illiquid. You can't sell a bridge loan in 10 minutes to defend a peg.
* *(Note: Concentration calculations belong in the [Sustainability Framework](./Stablecoin-Sustainability-Framework.md) under HHI).*

### B. Custody Risk: The "Seizure" Test

*Distinct from Decentralization (User Control), this checks **Asset Location**.*

* **Question:** Where do the assets legally sit?
  * **Smart Contract:** Code access only. (Type B).
  * **Bank Account:** Legal process access. (Type A).
* **Pass Condition:** If Off-Chain, is there a **Statutory Trust** (Bankruptcy Remote)? Or is it a general creditor claim (FTX)?

## 4. Pillar II: The Engine (Kinetic Stress)

*Mechanisms work in fair weather. Do they work in a hurricane?*

### C. Liquidation Physics: The "Death Spiral" Threshold

**Metric:** **Maximum System Throughput ($/block).**

* **The Test:**
    1. Assume Price drops 50% in 1 hour.
    2. Calculate `Total_Debt_Underwater`.
    3. Compare to `Max_Auction_Throughput`.
    4. **Verdict:** If `Debt > Throughput`, the system is insolvent. The "Backing" is a math error.

### D. The Peg: Redemption vs. Imagination

**Metric:** **Cost of Exit.**

* **Hard Peg:** "I give you 1 Token, you give me $1 Collateral." (Liquity/USDC).
  * *Status:* Real.
* **Soft Peg:** "I promise to raise interest rates until someone buys it." (DAI DSR / Reflexer).
  * *Status:* Hope.
* **Market Ops (PSM):** "We have a bucket of USDC."
  * *Status:* Reliable until the bucket is empty.

### E. Redemption Liquidity (LCR)

**Metric:** **The "Run on the Bank" Ratio.**

* **Formula:** `Liquid_Assets_Available_in_1hr / Total_Liabilities`.
* **Requirement:** Must be > 20% for pure crypto, > 100% for fiat wrappers.
* **Failure:** If you hold Commercial Paper (90-day maturity) against instant redemptions, you are facing a duration mismatch.

## 5. The "Red Flag" Checklist (Immediate Fail)

If the protocol does any of these, the analysis ends. Verdict: **UNSAFE**.

1. **"Capital Efficient":** Euphemism for "Undercollateralized."
2. **"Algorithmic":** Euphemism for "Unbacked."
3. **"Community Backed":** Means "We will print a governance token to pay you." (Ponzi).
4. **Rehypothecation:** Are they lending the collateral out? If yes, it's not backing. It's a liability.

---

## 6. Final Verdict Template

Don't waffle. Give a score.

| Component | Rating (0-10) | Reason |
| :--- | :--- | :--- |
| **Asset Liquidity** | | Did you mark "GovTokens" to 0? |
| **Engine Speed** | | Can it clear a Black Thursday? |
| **Custody Safety** | | Is it Bankruptcy Remote? |
| **Solvency Score** | **/30** | < 20 = Junk. |
