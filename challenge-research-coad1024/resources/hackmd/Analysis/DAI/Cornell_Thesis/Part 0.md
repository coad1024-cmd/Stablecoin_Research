# TL;DR (2–3 short paragraphs)

Ariah Klages-Mundt’s dissertation shows that **stablecoin “sustainability” is multi-dimensional, fragile, and modelable**. Non-custodial over-collateralized designs can admit *stable* and *unstable* parameter regimes: in the unstable regime endogenous dynamics (speculator issuance, liquidations, and an endogenous stablecoin price) can create deflationary deleveraging spirals and short-squeeze behaviour that accelerate collateral drawdown and break peg protection. (See Ch.2 & Ch.3 for formal models and characterizations.)

Beyond single-protocol dynamics, the thesis develops **network-level theory** showing how contract structure, cycles, and parameter sensitivity produce cascading losses and extreme sensitivity to small parameter changes — meaning protocol-level safeguards can be overwhelmed by system interactions. It also supplies practical algorithmic tools for intervention and bounding sensitivity. Together these parts imply that a sustainable stablecoin needs careful design across (i) microeconomic issuance mechanics and liquidation rules, (ii) governance/oracle incentives, and (iii) system-level network robustness. (See Ch.5–Ch.7.)

---

## 0. Document navigation map (quick)

Below are the dissertation parts most directly relevant to “stablecoin sustainability,” with a 1–2 sentence description and a short statement of how each connects to stability/sustainability. References point to the dissertation chapters/sections (primary file).

* **Chapter 2 — *While Stability Lasts: A Stochastic Model of Noncustodial Stablecoins***
  *What it contains:* a stochastic single-speculator model of over-collateralized non-custodial stablecoins, formal collateral constraints, liquidation mechanics, and proofs characterizing stable vs unstable domains (Sections 2.2–2.5).
  *Connection to sustainability:* provides the core mathematical characterization of how issuance decisions + endogenous stablecoin pricing produce (or fail to prevent) deleveraging spirals and sets the baseline for parameter regimes that must be satisfied for “sustainable” operation.

* **Chapter 3 — *(In)Stability for the Blockchain: Deleveraging Spirals and Stablecoin Attacks***
  *What it contains:* dynamic models with explicit speculator/stablecoin-holder interactions, market-clearing, limits to liquidity, numerical simulations, and a taxonomy of attack vectors (including liquidation/MEV manipulation).
  *Connection to sustainability:* shows how realistic market frictions, liquidation processes, and adversarial behavior can convert modelled instability into real peg breakdowns; provides actionable insights (e.g., limits on leverage, auction design) to mitigate failure modes.

* **Chapter 4 — *Stablecoins 2.0: Economics Foundations and Risk-Based Models***
  *What it contains:* taxonomy of custodial vs non-custodial designs, capital-structure framing, governance/oracle risk discussion, composite designs (ETF/CDO/RDF), and open questions about incentive sustainability.
  *Connection to sustainability:* maps design choices (custodial reserves, fractional reserves, endogenous collateral, composite/rainy-day funds) to their risk profiles and highlights governance/oracle incentive constraints that affect long-run sustainability.

* **Chapter 5 — *Cascading Losses in Reinsurance Networks***
  *What it contains:* general contagion model for networks of reinsurance contracts, fixed-point existence/uniqueness results, and identification of dangerous network structures (cycles, retrocession spirals).
  *Connection to sustainability:* provides theory and examples of how networked exposures concentrate risk — directly relevant when stablecoins are embedded in broader DeFi webs (DEXs, lending, yield strategies) that can transmit and amplify failures.

* **Chapter 6 — *Optimal Intervention in Economic Networks using Influence Maximization Methods***
  *What it contains:* computational hardness of optimal intervention and scalable approximation algorithms (adapted influence-maximization) for allocating limited budgets to mitigate cascades.
  *Connection to sustainability:* gives practical methods for protocol designers/regulators to design interventions (buffers, recapitalizations, targeted support) that maximize system-wide stability under budget constraints.

* **Chapter 7 — *Cascading Risks and Sensitivity in Economic Networks***
  *What it contains:* perturbation-theory analysis of sensitivity, bounds for acyclic/cyclic systems, and simulation evidence on conditioning and parameter perturbations.
  *Connection to sustainability:* quantifies how small parameter errors or mis-specifications (or unexpected correlations) can produce large changes in loss outcomes — crucial for assessing robustness of any “sustainable” design.

* **Appendices and Proofs (Ch.2 App., Ch.3 App., Ch.4 App. 4.7, Ch.5 App.)**
  *What they contain:* detailed derivations, parameter tables, simulation methodology, and model proofs.
  *Connection to sustainability:* source of the exact equations, assumptions and parameter choices you must audit and test when operationalizing the dissertation’s recommendations.

---
