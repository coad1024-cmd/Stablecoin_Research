# Terra (UST) Analysis: Post-Mortem

## 1. Executive Summary

**Verdict**: Failed.
**Reason**: Endogenous Collateral (LUNA) + Unsustainable Yield (Anchor) = Death Spiral.

## 2. Backing Mechanism

* **Type**: Algorithmic (Seigniorage Shares).
* **Mechanism**: Burn $1 UST to mint $1 LUNA.
* **Failure Mode**: When Market Cap(LUNA) < Supply(UST), the system is insolvent.

## 3. Sustainability (The "Ponzi" Model)

* **Revenue**: Transaction fees (negligible).
* **Cost**: Anchor Yield (~20% APY).
* **Deficit**: Subsidized by Terraform Labs (TFL) reserves.
* **[TODO]**: Add "Death Spiral" diagram here.

## 4. Decentralization

* **Validators**: Highly concentrated set of LUNA validators.
* **Governance**: Centralized control via TFL.

## 5. Comparison

| Feature | Terra (UST) | Maker/Liquity |
| :--- | :--- | :--- |
| **Backing** | Endogenous (LUNA) | Exogenous (ETH/RWA) |
| **Risk** | Death Spiral | Liquidation |
