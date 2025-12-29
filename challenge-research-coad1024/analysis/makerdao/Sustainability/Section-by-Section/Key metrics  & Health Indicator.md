# Key Metrics & Health Indicators (MakerDAO)

**Goal**: Define the "Vital Signs" for MakerDAO's sustainability.

## 1. Net Interest Margin (NIM)

The spread between what Maker *earns* on assets and *pays* on liabilities.

* **Formula**: $\text{NIM} = \text{WeightedAvgAssetYield} - \text{DSR}$
* **Current State**: ~1-2% spread on RWA; ~3-4% spread on Crypto.
* **Health Target**: NIM > 0 continuously.

**Diagram**: NIM Waterfall Structure
![NIM Waterfall](../Diagrams/Key%20Metrics/nim_formula_schematic.png)

## 2. Surplus Buffer Runaway

How long can MakerDAO survive if revenue drops to zero?

* **Metric**: $\frac{\text{SystemSurplus}}{\text{AnnualOpEx}}$
* **Importance**: RWA structures have high fixed costs (legal retainers). The buffer must cover these even during crypto winters.
* **Burn vs Earn**:
  * **Burn Phase**: Bear market (High DSR to retain users, low crypto fees).
  * **Earn Phase**: Bull market (High crypto fees, low DSR needed).

**Diagram**: Surplus Buffer Growth
![Surplus Buffer](../Diagrams/Key%20Metrics/surplus_buffer_growth.png)

## 3. Incentive ROI

Is the money spent on SubDAO emissions generating TVL?

* **Formula**: $\frac{\text{TVL Generated}}{\text{Value of Emissions}}$
* **Analysis**:
  * **RWA Yields**: High ROI (Organic revenue).
  * **SubDAO Farming**: Low ROI (Mercenary capital).

**Diagram**: Incentive Efficiency
![Incentive ROI](../Diagrams/Key%20Metrics/incentive_efficiency_roi.png)

## 4. DAI Velocity

* **Definition**: Daily Transaction Volume / Total Supply.
* **Goal**: High velocity implies utility beyond speculation.
* **Reality**: Low velocity (mostly sitting in DSR or farming pools).

---

## Summary of Health

| Metric | Status | Trend |
| :--- | :--- | :--- |
| **NIM** | **Healthy** | Stabilized by RWAs |
| **Buffer** | **Strong** | >$50M surplus |
| **Velocity** | **Weak** | Yield-dependent |
| **ROI** | **Mixed** | High on RWA, unclear on SubDAOs |
