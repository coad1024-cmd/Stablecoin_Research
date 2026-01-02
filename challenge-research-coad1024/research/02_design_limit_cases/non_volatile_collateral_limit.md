
---

# The Non-Volatile Limit Case in Stablecoin Design

## A Boundary Analysis and Degeneracy Result
*Canonical Version — Frozen for Submission*

---

## Abstract

This paper analyzes the theoretical limit case of stablecoin design in which reserve assets are strictly non-volatile relative to the unit of account and legally enforceable for redemption. Under these assumptions, we show that the stablecoin design space collapses to a degenerate structure equivalent to a tokenized narrow bank. In this limit, mechanisms such as over-collateralization, liquidation engines, algorithmic stabilization, and discretionary governance controls become mathematically redundant. The result is not a novel design proposal, but a boundary condition that serves as a reference baseline against which stablecoin systems backed by volatile collateral must be evaluated. Residual risk is shown to be exclusively operational, legal, and custodial in nature, consistent with prior economic treatments of fully backed money-like liabilities ([Gorton & Metrick, 2010](#ref-gorton-metrick); [Cao et al., 2025](#ref-cao)).

---

## 1. Introduction: The Purpose of a Limit Case

Stablecoin design literature frequently focuses on mechanisms intended to mitigate collateral volatility, including liquidation thresholds, feedback controllers, and dynamic monetary policy rules. These mechanisms are often treated as intrinsic features of decentralized currency systems rather than contingent responses to risk ([Catalini & de Gortari, 2021](#ref-catalini-degortari)).

This paper adopts a different approach. Rather than proposing an improved mechanism, it analyzes a **limit case**: a hypothetical regime in which reserve assets exhibit zero price volatility relative to the peg and are legally enforceable for redemption.

The objective is not realism, but **structural clarity**.

> **Thesis:**
> In the limit where reserve asset volatility approaches zero and legal enforceability holds, all stablecoin designs converge to a fully backed, primary-market-only structure equivalent to a tokenized narrow bank.

This result is not a policy recommendation. It is a degeneracy condition that isolates which components of stablecoin design exist to manage volatility rather than to define money-like liabilities themselves, echoing classical narrow-banking arguments ([Gorton & Zhang, 2021](#ref-gorton-zhang)).

**Figure 1: Design Space Collapse in the Non-Volatile Limit**
![**Figure 1: Design Space Collapse in the Non-Volatile Limit**](../../Design/Design%20with%20Non-volatle%20reserves/Output/Diagrams/Gemini_Generated_Image_5b291m5b291m5b29.png)
_Design space collapse under the non-volatile collateral limit. As reserve volatility approaches zero (σ² → 0), stablecoin mechanisms designed to manage price risk become redundant, and system design converges to a fully backed, primary-market-only structure equivalent to a tokenized narrow bank._

---

## 2. Explicit Assumptions and Scope

This analysis relies on the following assumptions, which are intentionally strong and explicitly bounded:

1. **Zero Price Volatility**
   Reserve assets have deterministic value relative to the unit of account
   $$
   \sigma^2 = 0
   $$

2. **Legal Enforceability**
   Reserve assets are bankruptcy-remote, senior to issuer liabilities, and legally redeemable for stablecoin holders, consistent with reserve-quality standards discussed in the policy literature ([Catalini & Shah, 2021](#ref-catalini-shah)).

3. **High-Quality Liquid Assets (HQLA)**
   Reserves can be liquidated at par at scale without price impact under normal market conditions, as assumed in currency-board and reserve-backed models ([Gorton & Metrick, 2010](#ref-gorton-metrick)).

4. **Atomic Mint/Burn Operations**
   Stablecoin issuance and redemption are fully collateralized and settled atomically.

5. **Rational Arbitrage**
   Arbitrageurs exist and act on deviations between market price and redemption value.

These assumptions define a **boundary regime**, not an attainable design target. Any relaxation of these assumptions reintroduces complexity and risk, as shown in stochastic models of stablecoin instability ([Klages-Mundt et al., 2022](#ref-klages)).

---

## 3. Risk Taxonomy Under the Non-Volatile Constraint

We classify stablecoin risks and evaluate their status under the stated assumptions.

### 3.1 Eliminated Risks (by Assumption)
**Figure 2: Stablecoin Risk Matrix Across Collateral Regimes**
![**Figure 2: Stablecoin Risk Matrix Across Collateral Regimes**](../../Design/Design%20with%20Non-volatle%20reserves/Output/Diagrams/Gemini_Generated_Image_efeyzlefeyzlefey.png)
_Risk classification under volatile and non-volatile collateral regimes. Price-driven solvency risks are eliminated by assumption in the non-volatile limit, while operational and custodial risks remain active constraints_.

1. **Credit Risk**
   Eliminated *conditional on legal enforceability*.
   If reserve assets default or become legally inaccessible, this assumption fails and the model no longer applies.

2. **Market / Price Risk**
   Eliminated by definition ($\sigma^2 = 0$).

3. **Endogenous Reflexive Risk (“Death Spirals”)**
   Eliminated because collateral value is exogenous to protocol success and cannot be diluted or reflexively impaired, unlike algorithmic designs with endogenous backing ([Cao et al., 2025](#ref-cao)).

4. **Price-Driven Liquidity Risk**
   Eliminated insofar as reserve liquidation does not introduce price impact or solvency impairment.

### 3.2 Residual Risks (Irreducible)

1. **Operational Risk**
   Smart-contract failure, custody errors, fraud, governance bugs.

2. **Custodial and Legal Risk**
   Asset freezes, jurisdictional seizure, regulatory intervention, as illustrated by real-world reserve-backed proposals such as Libra/Diem ([Libra Association, 2019](#ref-libra)).

3. **Settlement and Coordination Risk**
   Delays, halts, or legal suspensions in redemption processes.

> **Key distinction:**
> Economic insolvency risk is eliminated.
> Institutional and operational risk is not.

---

## 4. Formal Limit-Case Result

Let:

* $S$ = stablecoin supply
* $A$ = market value of reserve assets
* $L = S$ = stablecoin liabilities

In standard models, $A(t)$ is stochastic and requires over-collateralization ($k > 1$) such that:
$$
A(0) = k \cdot L(0)
$$

In the non-volatile limit:
$$
\sigma^2 = 0 \Rightarrow A(t) = A(0)
$$

Solvency requires:
$$
A(t) \ge L(t)
$$

Under atomic mint/burn operations:
$$
k \to 1
$$

**Result:**
Over-collateralization becomes unnecessary. Solvency is preserved through strict issuance discipline rather than price buffers, reproducing the balance-sheet structure of narrow banks and currency boards ([Gorton & Metrick, 2010](#ref-gorton-metrick)).

This is a **degenerate baseline**, not an optimal solution in the general case.

---

## 5. Redundancy of Common Stablecoin Mechanisms

### 5.1 Liquidation Engines as Dead Code

Liquidation logic is triggered when collateral value falls below a threshold.

In this regime:
$$
V_c(t) = V_c(0) \quad \forall t
$$

The trigger condition is unreachable. Liquidation mechanisms become dead code.

---

### 5.2 Algorithmic Stabilization Redundancy

Supply-elasticity mechanisms exist to counteract price deviation driven by collateral volatility or demand shocks.

Here, redemption value is invariant and directly enforceable. Arbitrage restores the peg without protocol intervention, rendering algorithmic stabilization redundant ([Catalini & de Gortari, 2021](#ref-catalini-degortari)).

---

### 5.3 Governance Parameter Redundancy

Governance mechanisms designed to tune risk parameters exist solely to manage volatility.

With volatility removed, discretionary governance introduces risk rather than mitigating it, a point emphasized in analyses of governance-heavy stablecoin systems ([Klages-Mundt et al., 2022](#ref-klages)).

---

## 6. Peg Behavior Under Demand Shocks

Mass redemptions do not induce insolvency or price dislocation, provided reserve liquidity assumptions hold.

However:

* **Economic runs** (price-driven solvency failures) are eliminated.
* **Institutional runs** (legal, operational, or coordination failures) remain possible.

This distinction is critical. The absence of market risk does not imply the absence of systemic risk ([Gorton & Zhang, 2021](#ref-gorton-zhang)).

---

## 7. Residual Risk Management and Capital Structure

Because operational and custodial risks persist, the system requires a junior capital buffer ($\epsilon$):

* strict subordination,
* non-dilution of stablecoin holders,
* automatic mint halts below thresholds,
* external recapitalization only, and
* orderly wind-down procedures.

The buffer is non-yield-bearing and exists solely to absorb non-market losses, consistent with narrow-bank capital logic.

---

## 8. Incompatibilities and Exclusions

This limit case is **structurally incompatible** with:

* censorship resistance,
* permissionless custody,
* endogenous crypto collateral,
* monetary sovereignty independent of legal systems.

These are not oversights. They are the cost of eliminating volatility.

---

## 9. Interpretation and Use

This model should be read as:

* a **baseline**, not a recommendation,
* a **reference point**, not an aspiration,
* a **boundary condition** for evaluating volatile-collateral designs.

Any real-world stablecoin deviates from this structure precisely because its reserves are volatile, endogenous, or legally constrained.

---

## 10. Conclusion

In the non-volatile, legally enforceable limit, stablecoin design collapses to a narrow bank with tokenized liabilities and a junior operational buffer. Complexity in DeFi stablecoins is not a consequence of decentralization per se, but a defensive response to collateral volatility.

This limit case establishes a clean baseline against which the necessity, cost, and failure modes of volatile-world mechanisms can be rigorously evaluated.

---

## References

* <span id="ref-cao"></span>Cao, Y., Cong, L., & Yang, X. (2025). *[Designing Stablecoins](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3887012)*. Mathematical Finance.
* <span id="ref-catalini-degortari"></span>Catalini, C., & de Gortari, A. (2021). *[On the Economic Design of Stablecoins](https://www.nber.org/papers/w29115)*. NBER.
* <span id="ref-catalini-shah"></span>Catalini, C., & Shah, N. (2021). *[Setting Standards for Stablecoin Reserves](https://www.catalini.com/wp-content/uploads/2021/11/Standards-Reserves-Catalini-Shah-2021.pdf)*.
* <span id="ref-gorton-metrick"></span>Gorton, G., & Metrick, A. (2010). *[Regulating the Shadow Banking System](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1676947)*. Brookings Papers.
* <span id="ref-gorton-zhang"></span>Gorton, G., & Zhang, G. (2021). *[Taming Wildcat Stablecoins](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3888752)*. SSRN.
* <span id="ref-klages"></span>Klages-Mundt, A., et al. (2022). *[While Stability Lasts: A Stochastic Model of Non-Custodial Stablecoins](https://arxiv.org/abs/2004.01304)*. Mathematical Finance.
* <span id="ref-libra"></span>Libra Association. (2019). *[The Libra Reserve](https://libra.org/en-US/white-paper/)*.

---