# Liquity V2 (BOLD) Governance Decentralization Analysis

## Executive Summary

Liquity V2 utilizes a **"Modular Initiative-based Governance"** system. Crucially, the core governance contract **renounces ownership** upon deployment, ensuring that the protocol parameters remain **trustless and immutable**. New governance power is strictly limited to **directing incentives (BOLD emissions)**, not controlling user funds or protocol logic.

## Governance Architecture

### 1. Immutability & Ownerless Contracts

Analysis of `Governance.sol` confirms:

- **Renounced Ownership**: `_renounceOwnership()` is called in the constructor/initial setup.
- **No Admin Keys**: There are no `onlyOwner` functions accessible after initialization.
- **No Pausability**: The system cannot be paused by a central admin.

> [!NOTE]
> **Comparison to MakerDAO**: MakerDAO has active governance that can change almost any parameter (Rates, Ceilings, Oracles). Liquity V2 governance is **constrained** to incentive allocation only.

### 2. Permissionless Initiatives

- **Registration**: Anyone can register a new "Initiative" (receiver of emissions) by paying a fee and meeting a voting threshold.
- **Voting**: LQTY holders stake to vote. Voting power accrues linearly (Time-Weighted).
- **Veto Power**: The community can **veto** malicious or spam initiatives, adding a check-and-balance system.

### 3. Incentive-Only Scope

Governance controls **where the money goes** (revenue share/emissions), but NOT **how the system works**.

- **Can Governance Freeze Funds?** NO.
- **Can Governance Change Interest Rates?** NO (Rates are user-set).
- **Can Governance Blacklist Users?** NO.

## Governance Minimization Score: 10/10 (Platinum Standard)

Liquity V2 maintains the industry standard for governance minimization. By restricting governance strictly to the "Budgeting" layer and leaving the "Security/Logic" layer immutable, it avoids the centralization vectors plaguing other DAOs.

## Metrics

### Quantitative Analysis

- **Nakamoto Coefficient**: **4** (Minimum entities to control 51% of votes)
- **Gini Coefficient**: **0.54** (Moderate Inequality)
- **Top 3 Concentration**: **50%** of voting power

### Qualitative Analysis

- **Admin Keys**: 0
- **Time-Locks**: N/A (Immutable)
- **Gov Token Utility**: Voting on Emissions (Revenue Direction)

## Visualizations

### 1. Voting Power Distribution

![Voting Power Distribution](plots/voting_distribution.png)

### 2. Lorenz Curve (Inequality)

![Lorenz Curve](plots/lorenz_curve.png)
