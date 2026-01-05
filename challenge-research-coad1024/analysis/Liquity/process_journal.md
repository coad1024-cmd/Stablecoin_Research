# Process Journal: Liquity Backing Mechanism Analysis

## Objective

Produce a detailed, "bullet-proof" analysis of Liquity's backing mechanism, mirroring the depth and style of "DAI at the Crossroads, Part I".

## Workflow Log

### Phase 1: Requirement Analysis & Planning

- **Goal**: Understand the standard set by the DAI article.
- **Action**: Reading `resources/hackmd/Analysis/DAI/DAI at the Crossroads, Part I...`.
- **Focus**: Identify key sections (e.g., on-chain vs. off-chain assets, custodial risks, smart contract accounting).

### Phase 2: Information Gathering (Internal)

- **Goal**: Assess current knowledge from `resources/Liquity/dev`.
- **Action**: Review Whitepaper and README for specific backing mechanics (Trove mechanics, Stability Pool, Redemption).

### Phase 3: Information Gathering (External)

- **Goal**: Find external audits, deep dives, and blog posts to supplement official docs.
- **Search Queries**:
  - "Liquity protocol backing mechanism deep dive"
  - "LUSD solvency analysis"
  - "Liquity redemption mechanism game theory"
  - "Liquity stability pool historical performance"

### Phase 4: Gap Analysis

- **Goal**: Identify what is missing.
- **Checklist**:
  - Exact contract flow for collateral?
  - Historical de-peg events and system response?
  - Oracle dependency details?
  - Custodial risks (if any - likely none for ETH, but what about LUSD in pools?)

### Phase 5: Drafting

- **Target File**: `analysis/Liquity/Liquity_Backing_Mechanism_Deep_Dive.md`
- **Structure**:
    1. Introduction: The "On-Chain" Purist
    2. The Trove: Individual Solvency
    3. The Stability Pool: Collective Solvency
    4. Redemption: The Hard Peg
    5. Recovery Mode: Systemic Defense
    6. Oracle Dependencies: The External Link
    7. Conclusion: Solvency Verdict

### Phase 6: Liquity V2 (Bold) Analysis

- **Goal**: Analyze the new `liquity/bold` repository to write a deeper technical article on V2.
- **Action**: Cloning `https://github.com/liquity/bold` to `resources/Liquity/bold`.
- **Findings**:
  - **Philosophy Shift**: From "Immutable & Rigid" to "Immutable & Adaptive".
  - **Interest Rates**: Replaced one-time fee with user-set annual interest rates. This creates a market for borrowing cost.
  - **Multi-Collateral**: WETH, rETH, wstETH supported via "Branches".
  - **Redemption Routing**: Redemptions now target the most "unbacked" branches first.
  - **Zombie Troves**: Redemptions leave troves open to prevent griefing.
- **Target File**: `analysis/Liquity/Liquity_V2_Bold_Deep_Dive.md`
- **Structure**:
    1. **Introduction**: The Evolution of "Immutable"
    2. **Architecture**: The Branch Model (`CollateralRegistry` + `TroveManager` per asset)
    3. **The Interest Rate Market**: User-set rates, `SortedTroves` by rate, and the new game theory.
    4. **Redemption 2.0**: "Unbackedness" routing and Zombie Troves.
    5. **Safety Upgrades**: Removal of Recovery Mode, Branch Shutdown logic.
    6. **Comparison**: V1 vs V2 matrix.
