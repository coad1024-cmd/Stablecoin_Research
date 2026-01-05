# The Stablecoin Trilemma: Efficiency, Safety, & Scale
**A Comparative Analysis of Sky Ecosystem, Liquity V1, and Liquity V2**

**Date:** January 5, 2026  
**Authors:** Research Challenge Team  
**Framework Version:** v3.1 (Triangular Comparison)

---

## 1. Executive Verdict: The Three Species

The stablecoin landscape is no longer a binary choice between "Centralized" and "Decentralized". Our analysis reveals three distinct architectural species, each optimizing for a specific vertex of the **Impossible Trinity**.

| Feature | **Sky Ecosystem** (The Bank) | **Liquity V1** (The Vault) | **Liquity V2** (The Hybrid) |
|:---|:---|:---|:---|
| **Archetype** | Regulatory Neo-Bank | Cypherpunk Public Utility | Pragmatic DeFi Protocol |
| **Primary Goal** | **Scale & Efficiency** | **Absolute Safety** | **Yield & Growth** |
| **Backing** | Custodial (USDC/RWA) | Trustless (ETH) | Diversified (LSTs) |
| **Governance** | Plutocratic (Active) | None (Immutable) | Limited (Incentive-Only) |
| **Risk Profile** | Censorship / Regulatory | Economic Stagnation | LST Contagion |
| **Score (Decent.)** | � **0.50** (Fail) | 🟢 **0.99** (Perfect) | � **0.85** (Compromised) |
| **Score (Sust.)** | � **High** (Active Yield) | � **Broken** (0% Yield) | 🟢 **High** (User-Set Yield) |

> **The Trade-Off Map:**
> *   **Sky** sacrifices Safety for **Efficiency**.
> *   **Liquity V1** sacrifices Efficiency for **Safety**.
> *   **Liquity V2** sacrifices "Pure Safety" for **Scale**.

---

## 2. Sustainability Analysis (The Business Case)

**Question:** *Can the protocol survive in a high-rate environment?*

### Sky Ecosystem: The Profit Machine
*   **Mechanism:** Active Treasury Management. Sky captures the spread between RWA yields (5%) and DSR (1.25%).
*   **Result:** Massive surplus ($60M+) and ability to vote-buy growth.
*   **Verdict:** **Resilient.** It acts like a sovereign wealth fund.

### Liquity V1 (LUSD): The Stagnation Trap
*   **Mechanism:** Zero-interest loans. Protocol earns only one-time fees.
*   **Result:** **Economic Failure.** In a 5% rate world, LUSD supply collapsed because it pays 0% yield. Users fled to Treasuries. LUSD is safe, but "dead".
*   **Verdict:** **Obsolete** (Economically).

### Liquity V2 (BOLD): The Market Fix
*   **Mechanism:** User-Set Interest Rates. Borrowers compete for liquidity, generating real yield for BOLD holders.
*   **Result:** **Competitive.** It matches the Risk-Free Rate (RFR) indigenously.
*   **Verdict:** **Sustainable.** It solves V1's flaw but introduces complexity.

---

## 3. Decentralization Analysis (The Sovereignty Case)

**Question:** *Who controls the money?*

![Comparative Decentralization Scorecard](comparative_decentralization_bar.png)
*Figure 1: The Hierarchy of Trust. Sky (Red) relies on legal trust. Liquity V2 (Orange) relies on LST trust. Liquity V1 (Green) relies on Math.*

### Sky Ecosystem: Effectively Centralized
*   **Governance:** Top-1 delegate holds 86% of voting power.
*   **Collateral:** 42% USDC. Circle can freeze the protocol instantly.
*   **Verdict:** Sky is a "Crypto-Wrapped Bank". It is not sovereign.

### Liquity V1: The Platinum Standard
*   **Governance:** 0 Admin Keys. 0 Governance Votes.
*   **Collateral:** 100% ETH. No counterparty risk.
*   **Verdict:** The only truly "Unstoppable" money.

### Liquity V2: The Calculated Risk
*   **Governance:** No admin keys, but voting directs incentives (controlling liquidity).
*   **Collateral:** Accepts LSTs (wstETH).
    *   *Risk:* If Lido DAO censors, Liquity V2 is affected.
*   **Verdict:** **Trust-Minimized**, not Trustless. A pragmatic compromise to unlock LST liquidity.

---

## 4. The Efficient Frontier

We visualize the design space as a curve where you cannot maximize all variables.

```
Decentralization (Safety)
  ^
  |        [Liquity V1] (Max Safety, Min Scale)
  |             *
  |
  |                        [Liquity V2] (Balanced Trade-off)
  |                               *
  |
  |                                            [Sky Ecosystem]
  |                                          (Max Scale, Min Safety)
  |__________________________________________________________> Efficiency (Scale)
```

**Strategic Insight:**
*   **Liquity V1** is the *theoretical limit* of decentralization.
*   **Sky** is the *theoretical limit* of efficiency without being a fiat bank.
*   **Liquity V2** attempts to push the frontier outward, seeking the "Goldilocks Zone".

---

## 5. Final Recommendations

### For Different user Profiles
| User Type | Recommendation | Why? |
|:---|:---|:---|
| **Yield Farmer** | **Sky (USDS)** | Highest liquidity, RWA backing, "Too Big To Fail". |
| **Cypherpunk** | **Liquity V1 (LUSD)** | Zero trust required. Immune to regulation. |
| **Sophisticated User** | **Liquity V2 (BOLD)** | High yield potential, but requires monitoring LST risks. |

### The Future
The industry is bifurcating. Sky is merging with Traditional Finance (TradFi). Liquity is retracting into "Hyper-DeFi". V2 is the bridge attempt. **We recommend maintaining exposure to distinct species to hedge regulatory vs. economic risks.**

---

### Artifact Index
See `research/00_canonical/` for verification data.
*   [Sky Sustainability Profile](../00_canonical/Sky%20Ecosystem/Sustainability/Atrifact/Sky_Sustainability_Profile_Jan2026.md)
*   [Sky Decentralization Profile](../00_canonical/Sky%20Ecosystem/Decentralization/Atrifact/Sky_Decentralization_Profile_Jan2026.md)
*   [Liquity V1 Sustainability Profile](../00_canonical/Liquity/01_V1_LUSD/Sustainability/Artifact/Liquity_V1_Sustainability_Profile.md)
*   [Liquity V1 Decentralization Profile](../00_canonical/Liquity/01_V1_LUSD/Decentralization/Artifact/Liquity_V1_Decentralization_Profile.md)
*   [Liquity V2 Economic Resilience](../00_canonical/Liquity/02_V2_BOLD/Sustainability/Artifact/Liquity_V2_Economic_Resilience.md)
*   [Liquity V2 Decentralization Analysis](../00_canonical/Liquity/02_V2_BOLD/Decentralization/Artifact/Liquity_V2_Decentralization_Analysis.md)
