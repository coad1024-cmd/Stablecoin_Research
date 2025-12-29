Good — I’ll rewrite this **cleanly, precisely, and defensibly**, the way it would appear in a serious research or policy-facing publication.

Key changes I will make (intentionally):

* Remove **bank balance-sheet metaphors** that don’t strictly apply
* Eliminate loaded language (“Ponzi”)
* Replace “assets/liabilities” where misleading with **endogenous absorber language**
* Center the analysis on **negative carry + expectation dependence**, not moral judgment
* Keep the quantitative intuition, but tighten the claims

I’ll give you the rewritten section in full, self-contained, and publication-ready.

---

# 1. Business Model Decomposition

## Overview

The Terra protocol operated as a **reflexive monetary system** with two tightly coupled policy functions:

1. **Monetary stabilization:** Maintaining the price stability of UST through on-chain convertibility with LUNA.
2. **Demand subsidization:** Stimulating sustained demand for UST through externally funded yield incentives, primarily via the Anchor Protocol.

Unlike collateralized stablecoins or traditional banking systems, Terra did not rely on exogenous assets held in reserve to back its liabilities. Instead, UST stability depended on the **endogenous market value of LUNA**, a token whose valuation was itself a function of the system’s growth, adoption, and expected future demand.

This structure created a system in which monetary stability, fiscal subsidy, and market expectations were inseparable.

---

## 2. Economic Structure and Implied Balance Sheet

### 2.1 UST Supply (Protocol Liabilities)

At its peak, UST supply reached approximately **$18.7 billion**.

UST functioned as a **demand liability** with the following properties:

* **Convertibility:** UST could be exchanged on demand for LUNA via the protocol’s mint–burn mechanism, at oracle-determined prices and subject to spreads and liquidity constraints.
* **Duration:** Effectively zero-duration; holders could exit positions immediately through on-chain swaps or secondary markets.
* **No senior claim:** UST did not represent a legal or contractual claim on exogenous assets or reserves.

Crucially, UST was not redeemable for a fixed quantity of value. Its backing was operational rather than contractual, defined entirely by the continued functioning of the convertibility mechanism.

---

### 2.2 Absorber Capacity: LUNA

Rather than serving as collateral in a traditional sense, **LUNA acted as the system’s volatility absorber**.

At peak conditions, LUNA’s market capitalization exceeded **$40 billion**, substantially larger than the outstanding UST supply. However, this apparent coverage was **endogenous and reflexive**:

* LUNA’s valuation depended on confidence in UST demand and network growth.
* UST expansion reduced LUNA supply (via burns), reinforcing price appreciation in growth regimes.
* UST contraction increased LUNA supply (via minting), placing downward pressure on price during stress.

As a result, LUNA could not be treated as an independent asset backing UST. Its capacity to absorb redemptions was conditional on **market expectations**, liquidity in centralized exchanges, and the willingness of participants to hold newly minted supply.

---

### 2.3 Exogenous Reserves

In the later stages of the system’s life, the Luna Foundation Guard (LFG) accumulated approximately **$3 billion in Bitcoin reserves** intended to support UST stability during stress events.

While these reserves represented an attempt to introduce exogenous backing, they exhibited several structural limitations:

* **Insufficient scale:** Reserves represented less than 20% of outstanding UST liabilities.
* **Non-mechanical deployment:** Reserves were not integrated into an automatic redemption or settlement mechanism.
* **Discretionary use:** Deployment relied on governance and operational decisions rather than protocol-level enforcement.

Accordingly, these reserves functioned as **intervention capital**, not as a binding reserve backing UST.

---

## 3. Revenue Sources

The Terra protocol did not generate revenue in the conventional sense of interest income or asset yield. Instead, its economic inflows consisted of the following:

### 3.1 Seigniorage Effects

When demand for UST increased, LUNA was burned to mint new UST. This supply contraction mechanically supported LUNA’s price, assuming sufficient market demand.

Importantly, this was **not protocol income**. No surplus accrued to a treasury or reserve. Value accrual occurred implicitly through market revaluation of LUNA, benefiting existing holders rather than strengthening the system’s balance sheet.

---

### 3.2 Transaction Fees

Terra levied modest transaction fees, including:

* A Tobin tax (approximately 0.35%)
* A minimum stability spread (approximately 0.5%)

These fees funded validator rewards and oracle incentives. Their magnitude was negligible relative to the scale of UST liabilities and Anchor subsidy outflows, and they declined during periods of reduced transaction volume.

---

### 3.3 Anchor Borrowing Interest

Borrowers on Anchor paid interest (approximately 12%) on loans collateralized by bLUNA and bETH. This represented the primary endogenous source of cash inflow into the Anchor ecosystem.

However, borrowing demand remained structurally lower than deposit demand, limiting the scale of this revenue stream.

---

## 4. Cost Structure

### 4.1 Anchor Yield Subsidy

The dominant cost in Terra’s economic model was the **Anchor deposit yield**, which paid approximately **19.5% annually** to UST depositors.

This yield substantially exceeded the income generated by borrowers and protocol fees, creating a persistent funding gap.

---

### 4.2 Operational and Network Costs

Additional costs included:

* Validator rewards
* Oracle incentives
* Operational expenses associated with maintaining the protocol

These were minor relative to the Anchor yield subsidy but nonetheless contributed to ongoing cash outflows.

---

## 5. Structural Negative Carry

The defining economic characteristic of Terra’s business model was a **persistent negative carry**.

This can be expressed using a simplified net interest margin (NIM) formulation:

[
\text{NIM} = \text{Yield}*{\text{Assets}} - \text{Cost}*{\text{Liabilities}}
]

Using approximate peak values:

* **Yield on assets:** ~12% on roughly $3 billion in Anchor loans
* **Cost of liabilities:** ~20% on roughly $14 billion in Anchor deposits

This implies an annualized funding gap on the order of:

[
$14\text{B} \times (20% - 12%) \approx $1.1\text{B per year}
]

This deficit was not covered by organic protocol revenue. Instead, it was financed through:

* Depletion of the Anchor yield reserve
* External capital injections
* Sale or dilution of LUNA supply

Economically, this structure amounted to **equity-funded yield subsidization**: value expectations embedded in LUNA were continuously drawn down to support UST demand growth.

---

## 6. Implications for Sustainability

Terra’s model did not fail because of a temporary liquidity mismatch or an isolated market shock. Its core vulnerability was structural:

* Stability depended on continued confidence in LUNA’s future market value.
* Yield subsidies accelerated UST adoption while deepening negative carry.
* The system lacked a mechanism to convert growth-phase market value into durable reserves.

Once expectations about LUNA’s future absorption capacity weakened, the convertibility mechanism no longer stabilized the system. Instead, it amplified exit pressure by transforming UST liabilities into rapidly expanding LUNA supply.

In this sense, Terra’s sustainability hinged not on solvency in the accounting sense, but on the persistence of a favorable **expectation regime**.

---

### Closing Note (Section Boundary)

This section has deliberately focused on Terra’s economic structure as designed and operated. It does not address the dynamic failure process, reflexive feedback loops, or parameter sensitivity under stress. Those dynamics are examined separately in the sustainability and regime analysis sections that follow.

---

