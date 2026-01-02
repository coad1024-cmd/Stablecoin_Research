# Liquity V2: The Decentralization of Solvency

**Authors**: Research Challenge Team
**Date**: January 2026
**Series**: Part III (Decentralization & Risk)

---

## Abstract

This paper evaluates the censorship resistance and control dynamics of Liquity V2 (BOLD). While Part I established the mechanism's correctness and Part II its economic viability, this final analysis interrogates its **Sovereignty**. We apply the **G-B-O Framework** (Governance, Backing, Operational) to quantify the protocol's resilience against nation-state adversarial vectors. Our findings indicate a "Platinum" standard in governance minimization (Admin Keys = 0), offset by a regression in collateral trustlessness due to the integration of Liquid Staking Tokens (LSTs). We conclude that Liquity V2 effectively trades "Pure Trustlessness" (V1) for "Pragmatic Scalability" without compromising its core immutability.

> [!IMPORTANT]
> **Methodology**: Decentralization is defined here not as a philosophical ideal but as **Control Distribution under Adversarial Conditions**. We utilize the Nakamoto Coefficient for voting power and the Herfindahl-Hirschman Index (HHI) for collateral concentration to provide empirical metrics.

---

## 1. Introduction: The Governance Paradox

The central paradox of DeFi scaling is that **complexity breeds centralization**. As protocols add features (e.g., multi-collateral support), they typically introduce "Admin Keys" or "Multisigs" to manage the new parameters.

Liquity V2 attempts to break this paradox via **"Modular Initiative-based Governance."** It supports complex features (User-Set Rates, Multi-Collateral) *without* complex governance. This report verifies whether this architectural intent translates to effective resistance in practice.

---

## 2. Governance Decentralization (G)

**Question**: Who can modify protocol parameters?
**Claim**: "Immutable. No Admin Keys."

### 2.1 The Initiative Framework

Unlike MakerDAO, where token holders vote on *parameters* (e.g., "Raise the DSR to 5%"), Liquity V2 governance is constrained strictly to **Incentives**.

*   **Logic Layer**: Immutable. No one can change the `MCR` (Minimum Collateral Ratio) or `Redemption Fee` logic.
*   **Budgeting Layer**: Token holders vote only on which `Initiative` contracts receive BOLD emissions.

### 2.2 Empirical Power Distribution

We analyzed the voting power distribution of LQTY stakers.

*   **Nakamoto Coefficient**: **4**. (Only 4 entities needed to reach >51% of votes).
*   **Gini Coefficient**: **0.54** (Moderate Inequality).

While the concentration is high (typical of PoS systems), the **Consequence of Capture** is low. Even if a cartel captures 51% of the vote, they can only misallocate inflation rewards; they cannot steal user funds or censor transactions.

![Voting Power Distribution](governance/plots/voting_distribution.png)
*Figure 1: Voting Power Distribution. The "Power Law" distribution is evident, with the top 3 delegates holding ~50% of the weight.*

![Lorenz Curve](governance/plots/lorenz_curve.png)
*Figure 2: Lorenz Curve of Voting Power. The deviation from the "Line of Equality" visually represents the Gini Coefficient of 0.54.*

---

## 3. Backing & Counterparty Risk (B)

**Question**: What backs the stablecoin, and can it be frozen?
**Claim**: "User-Choice Collateral."

### 3.1 The Regression from V1

Liquity V1 was backed 100% by native Ether. Liquity V2 introduces Liquid Staking Tokens (LSTs) like **wstETH** and **rETH**. This is the protocol's primary trade-off: **Scalability for Trust.**

*   **V1 Backing**: Trustless. (Uncensorable).
*   **V2 Backing**: Trust-Minimized. (Subject to LST DAO governance and smart contract risk).

### 3.2 Concentration Analysis (Projected)

Our projection of the post-launch collateral composition suggests high dominance of Lido's **wstETH**.

*   **Herfindahl-Hirschman Index (HHI)**: **3,738**.
*   **Threshold**: An HHI > 2,500 indicates a highly concentrated market.

> [!WARNING]
> **The LST Singularity**: If wstETH captures >50% of the backing, BOLD effectively inherits the regulatory risk profile of Lido. If Lido censors, BOLD's backing is partially censored.

![Collateral Composition](collateral/plots/collateral_composition.png)
*Figure 3: Projected Collateral Composition. The dominance of LSTs (wstETH, rETH) introduces counterparty risk absent in V1.*

![Counterparty Exposure](collateral/plots/counterparty_exposure.png)
*Figure 4: Counterparty Exposure by Issuer. Visualizing the shift from "Asset Risk" (ETH Price) to "Company Risk" (Lido/Rocket Pool).*

---

## 4. Operational Resilience (O)

**Question**: Who limits access to the protocol?
**Claim**: "Unstoppable Headless Brand."

### 4.1 The Frontend Marketplace

Liquity V2 retains the "Kickback" model. There is no `liquity.com` that facilitates transactions. Instead, a competitive market of third-party frontends hosts the UI.

*   **Benefit**: Robustness. If `DefiSaver` is geoblocked, users can switch to `Instadapp` or `Liquity.App` instantly.
*   **Projected HHI**: **3,558**. The market is expected to be dominated by a few large aggregators, but the *long tail* remains permissionless.

![Frontend Market Shares](operational/plots/frontend_shares.png)
*Figure 5: Frontend Market Share Projection. While large players dominate, the "Long Tail" (43%) ensures access even if top players capitulate to regulation.*

### 4.2 Keeper Diversity

The protocol relies on "Keepers" (Liquidators) to maintain solvency. The "Stability Pool" is the primary automated keeper.

*   **Risk**: If the Stability Pool is dominated by 1-2 whales, they could theoretically grief the system by withdrawing liquidity just before a crash.
*   **Data**: The distribution of liquidity providers follows a healthy decay curve, well within censorship-resistant thresholds.

![Stability Pool Concentration](operational/plots/stability_pool_concentration.png)
*Figure 6: Liquidity Provider Concentration. The top provider holds ~25%, below the 33% threshold required to unilaterally block automated offset liquidations.*

---

## 5. Final Scorecard & Conclusion

We aggregate the findings into the G-B-O Scorecard.

| Dimension | Rating | Justification |
| :--- | :--- | :--- |
| **Governance (G)** | **Platinum** | 0 Admin Keys. Immutability is absolute. The highest standard in DeFi. |
| **Backing (B)** | **Silver** | Regression from V1 due to LST inclusion. High HHI concentration risk. |
| **Operational (O)** | **Gold** | "Headless" frontend model remains the gold standard for access resilience. |

### The Verdict: Pragmatic Sovereignty

Liquity V2 is not a "Purist" protocol like V1. It accepts the reality that Ethereum has moved toward LST dominance. By accepting LSTs, it compromises on absolute trustlessness. However, it defends this compromise with an **Immutable Core**.

Even if the assets (wstETH) are censorable, the **Liability (BOLD)** remains unstoppable. The protocol itself cannot freeze funds, blacklist users, or be shut down by a multisig. It is a sovereign financial structure built on top of an increasingly centralized base layer.

**Final Series Conclusion**:
Across Parts I, II, and III, we find that **Liquity V2** successfully solves the "Scalability Trilemma" for decentralized stablecoins. It offers the **Peg Stability** of a centralized coin (via User-Set Rates), the **Scalability** of a multi-collateral system (via LSTs), and effectively retains the **Sovereignty** of V1 (via Immutable Governance).

---

*This concludes the Research Series.*
