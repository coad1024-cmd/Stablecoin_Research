

# Part I: Analysis - Stablecoin Technical Report

## 1. Executive Summary (The Alpha)

### BLUF (Bottom Line Up Front)
**Liquity (LUSD)** represents the **Gold Standard** of decentralization and censorship resistance, achieving immutability and pure crypto-backing at the cost of capital efficiency and rigid parameters. **MakerDAO (DAI)** has evolved into a **Hybrid Credit Facility**, prioritizing stability and scalability over decentralization by integrating US Treasury yields (RWA) and centralized stablecoins (USDC), creating strict regulatory vectors [[Source: MakerDAO Analysis]](/home/hash/Projects/Research%20Challenge/challenge-research-coad1024/analysis/makerdao/DAI_1&2/DAI%20at%20the%20Crossroads,%20Part%20I%20Where%20Sky's%20Solvency%20Lives%20On-Chain%20and%20Where%20It%20Doesn't.md). **Terra (UST)** serves as the canonical **Failure Mode**, ensuring solvency only through endogenous collateral (LUNA) that enters a reflexive death spiral when system liabilities exceed network valuation [[Source: Terra Sustainability]](/home/hash/Projects/Research%20Challenge/challenge-research-coad1024/analysis/Terra/Sustainability/Article_Sustainability.md).

### Comparative Matrix

| Feature | MakerDAO (DAI) | Liquity (LUSD) | Terra (UST) - *Post-Mortem* |
| :--- | :--- | :--- | :--- |
| **Type** | Exogenous CDP (Hybrid RWA/Crypto) | Exogenous CDP (Pure Crypto) | Endogenous Algorithmic |
| **Core Invariant** | $ink \cdot spot \ge art \cdot rate$ | $Collateral_{USD} \ge 1.10 \cdot Debt_{LUSD}$ | $P_{LUNA} \cdot \Delta S_{LUNA} = \Delta S_{UST}$ |
| **Min Collateral Ratio (MCR)** | 150% (ETH-A) / 101% (USDC-PSM) | 110% (Normal) / 150% (Recovery) | N/A (Algorithmic 1:1) |
| **Oracle Latency** | **1 Hour** (OSM Delay) | **None** (Direct Feed) | **VotePeriod** (~30-60s) |
| **Decentralization Vector** | **Low / Medium** (Centralized Backing) | **High** (Immutable / Pure ETH) | **Failed** (Validator Centralization) |

---

## 2. Deep Dive: Backing Architecture

### MakerDAO (DAI) - The Hybrid Ledger
**Mechanism:** Maker maintains solvency through the `Vat` contract, a single source of truth that tracks locked collateral (`ink`) and normalized debt (`art`). The fundamental safety check is enforced individually per vault.

**Invariant:**
$$ ink \cdot spot \ge art \cdot rate $$
*Where $spot$ is the price with safety margin, and $rate$ is the cumulative interest index.*

**Code Audit:**
*   **Ledger:** `Vat.sol` (Immutable core storage).
*   **Liquidation:** `Dog.sol` (Confiscates unsafe vaults), `Clipper.sol` (Dutch Auction settlement) [[Source: MakerDAO Analysis]](/home/hash/Projects/Research%20Challenge/challenge-research-coad1024/analysis/makerdao/DAI_1&2/DAI%20at%20the%20Crossroads,%20Part%20I%20Where%20Sky's%20Solvency%20Lives%20On-Chain%20and%20Where%20It%20Doesn't.md).
*   **Oracle:** `OSM` (Oracle Security Module) introduces a **1-hour delay** to prevent oracle manipulation attacks, giving users time to react.

**Visuals:**
![Plot: Dutch Auction Decay](/home/hash/Projects/Research%20Challenge/challenge-research-coad1024/analysis/makerdao/DAI_1&2/images/dutch_auction_decay.png)

### Liquity (LUSD) - The Immutable Tank
**Mechanism:** Liquity maximizes capital efficiency with a "Hard" 110% MCR and "Soft" Recovery Mode (150% TCR). It relies on the *Total Collateral Ratio* (TCR) of the entire system to trigger defensive states [[Source: Liquity Economic Engine]](/home/hash/Projects/Research%20Challenge/challenge-research-coad1024/analysis/Liquity/Backing%20Mechanism/Drafts/Sustainability/Liquity_Part_I_Economic_Engine.md).

**Invariant:**
$$ TCR = \frac{\sum Collateral_{ETH} \cdot P_{ETH}}{\sum Debt_{LUSD}} \ge 150\% \text{ (System Safe Mode)} $$

**Code Audit:**
*   **Manager:** `TroveManager.sol` (Handles liquidations and redemptions).
*   **Stability:** `StabilityPool.sol` (First line of defense; absorbs bad debt immediately).
*   **Oracle:** No delay mechanism; relies on immediate Chainlink/Tellor feeds to allow instant redemptions and liquidations, minimizing bad debt accrual during crashes.

**Visuals:**
![Plot: Liquity Recovery Mode](/home/hash/Projects/Research%20Challenge/challenge-research-coad1024/analysis/Liquity/Backing%20Mechanism/Diagrams/Article1/Gemini_Generated_Image_280wom280wom280w.png)

### Terra (UST) - The Algorithmic Illusion
**Mechanism:** Terra relied on an **Endogenous Swap** mechanism. Users could always burn \$1 of LUNA to mint 1 UST, and vice versa. This created a perfectly elastic supply that relied on LUNA's market cap to absorb volatility [[Source: Terra Sustainability]](/home/hash/Projects/Research%20Challenge/challenge-research-coad1024/analysis/Terra/Sustainability/Article_Sustainability.md).

**Invariant:**
$$ Value_{Burned} = Value_{Minted} $$
$$ P_{LUNA}(t) \cdot \Delta S_{LUNA} = 1 \cdot \Delta S_{UST} $$

**Code Audit:**
*   **Swap:** `Market.swap` (The mint/burn execution).
*   **Oracle:** `Oracle.vote` (Validators submitted prices; latency under congestion allowed arbitrageurs to drain the pool).

---

## 3. Deep Dive: Sustainability Analysis

*Applied Framework: Sustainability Triangle (Klages-Mundt) [[Source]](/home/hash/Projects/Research%20Challenge/challenge-research-coad1024/analysis/Sustianbility%20-framework%20algo%20coins.md)*

### Terra (UST): Submartingale Failure
Terra operated in a **Supermartingale (Unstable)** regime. The system relied on the **Reflexivity Gain ($G$)**:
$$ G = \frac{\Delta Demand_{LUNA}}{\Delta Supply_{UST}} $$
When $G > 1$, the system spirals.
*   **Failure Analysis:** As UST demand collapsed, the system minted infinite LUNA to honor the \$1 peg. Because LUNA demand was correlated with UST success, $P_{LUNA}$ collapsed faster than supply increased, fulfilling the condition for a **Death Spiral**.
*   **Model:** This endogenous backstop is mathematically equivalent to a bank capitalizing itself with its own stock.

### MakerDAO & Liquity: Liability Matching
**Metric:** Net Interest Margin ($NIM$)
$$ NIM = Yield_{Assets} - Cost_{Liabilities} $$

*   **Liquity (V1):**
    *   **Cost:** 0% (Holders receive 0% yield).
    *   **Yield:** 0% (One-time fee model; protocol earns no continuous revenue).
    *   **Verdict:** **Stable but Stagnant.** In a high-rate environment (5% treasury yields), LUSD suffers massive opportunity cost, trading below peg ($0.99) as capital flees to yield-bearing assets. Regimed as **Stable** but economically inefficient [[Source: Liquity Economic Engine]](/home/hash/Projects/Research%20Challenge/challenge-research-coad1024/analysis/Liquity/Backing%20Mechanism/Drafts/Sustainability/Liquity_Part_I_Economic_Engine.md).

*   **MakerDAO:**
    *   **Cost:** DAI Savings Rate (DSR) ~4-5%.
    *   **Yield:** RWA (T-Bills) ~5% + Crypto Loans.
    *   **Verdict:** **Sustainable Hybrid.** Maker extracts a spread ($Yield_{RWA} > Cost_{DSR}$). However, this forces reliance on centralized assets (USDC/RWA) to generate that yield, trading decentralization for sustainability.

**Visuals:**
![Plot: Regime Phase Plot](/home/hash/Projects/Research%20Challenge/challenge-research-coad1024/analysis/makerdao/DAI_1&2/images/regime_phase_plot.png)

---

## 4. Deep Dive: Decentralization Analysis

*Applied Framework: G-B-O-C Vector (Governance, Backing, Operational, Collateral) [[Source]](/home/hash/Projects/Research%20Challenge/challenge-research-coad1024/analysis/Decentralization-Framework.md)*

| Vector | MakerDAO (DAI) | Liquity (LUSD) | Analysis |
| :--- | :--- | :--- | :--- |
| **G (Governance)** | **Low** | **Max** | Maker is a "Plutocracy" where large MKR holders (and delegates) control risk params. Liquity is **Immutable**; no one can upgrade the contract or change core parameters. |
| **B (Backing)** | **Low** | **High** | Maker is **~60% Centralized** (USDC PSM + RWA). A single regulatory order to Circle freezes backing. Liquity is **100% ETH**, inheriting Ethereum's censorship resistance. |
| **O (Operational)** | **Medium** | **High** | Maker relies on a small set of sophisticated Keepers and specific Oracle feeds. Liquity incentivizes a broad set of public liquidators via the Stability Pool. |
| **C (Collateral)** | **Diversified** | **Single** | Liquity concentrates risk in ETH volatility. Maker diversifies across RWA/Stable/Crypto, reducing volatility risk but increasing censorship risk. |

### Stress Test: 50% Market Shock
*   **Maker:**
    *   **Oracle Delay:** 1-hour delay shields users from flash crashes but exposes the protocol to "bad debt" if the crash exceeds the safety buffer before the price updates.
    *   **USDC Risk:** If the shock is regulatory (USDC freeze), Maker becomes insolvent immediately as ~22-40% of backing vanishes.

*   **Liquity:**
    *   **Retrieval:** Recovery Mode triggers at 150% TCR. Any trove < 150% can be liquidated. This aggressive defense preserves the peg but punishes borrowers severely during volatility.
    *   **Robustness:** With no centralized dependencies, Liquity survives price shocks as long as Ethereum blocks function.

---
*Report generated for Research Challenge Context.*
