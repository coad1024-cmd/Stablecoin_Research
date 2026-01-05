# Terra Data Forensics: Methodology & Execution Plan

## Objective
To empirically validate the "Negative Carry" and "Insolvent Absorber" hypotheses using historical data from **Jan 1, 2021 to May 15, 2022**.

## 1. Data Requirements
The following datasets are required to execute the analysis:
*   `terra_daily_metrics.csv` (Columns: Date, UST_Supply, LUNA_Supply, LUNA_Price, UST_Price, Anchor_Deposits, Anchor_Borrows)
*   `lfg_reserves.csv` (Columns: Date, BTC_Balance, BTC_Price)

## 2. Analytical Modules

### Module A: The Absorber Ratio
We test the hypothesis that **LUNA capacity ($MarketCap$) became insufficient to absorb UST liabilities ($Supply$) long before the generic "Price < Peg" event.**

$$ \text{AbsorberRatio} = \frac{\text{LUNA\_MarketCap}}{\text{UST\_Supply}} $$

*   **Danger Zone**: Ratio < 1.5
*   **Death Zone**: Ratio < 1.0 (Insolvency)

### Module B: The Negative Carry (NIM)
We reconstruct the specific cash flows of Anchor to determine the cumulative deficit.

$$ \text{DailyDeficit} = (\text{Deposits} \times \text{DepositRate}) - (\text{Loans} \times \text{BorrowRate}) $$

*   **Assumption**: DepositRate = 19.5% (approx), BorrowRate = 12% (approx).
*   **Output**: Cumulative Deficit ($).

### Module C: The Reserve Coverage
We measure the reality of the LFG "Backstop".

$$ \text{ReserveRatio} = \frac{\text{BTC\_Reserves} \times \text{BTC\_Price}}{\text{UST\_Supply}} $$

*   **Hypothesis**: Reserves never exceeded 20% coverage.

## 3. Visualization Plan
The accompanying Python scripts will generate:
1.  `fig1_absorber_capacity.png`: Overlay of UST Supply vs LUNA Mcap.
2.  `fig2_anchor_deficit.png`: Cumulative "cash burn" of the protocol.
3.  `fig3_reserve_illusion.png`: LFG Reserves vs Total Liabilities.

---
*Note: This plan corresponds to the "Master Data Extraction Prompt" and is implemented in `scripts/terra_forensics.py`.*
