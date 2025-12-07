

## 1. The Core Accounting Layer: Vat as Single Source of Truth

This section establishes the foundational data structures that make backing verifiable and enforceable through deterministic smart contract logic, supported by empirical analysis of 137,441 vault positions.

### 1.1 The Vat Contract: Sky's Ledger

The Vat contract serves as the single source of truth for all collateral balances, debt positions, and system-wide solvency across the Sky Ecosystem  (<small>[MakerDAO Docs: Vat Module](https://docs.makerdao.com/smart-contract-modules/core-module/vat-detailed-documentation) [12]</small>).

Unlike traditional finance, where reserves are audited through opaque institutional processes, Sky's reserves are updated deterministically every block (approximately 12 seconds on Ethereum). This real-time verification creates a novel property: at any moment, an external observer can query the blockchain to obtain a complete, cryptographically verified snapshot of all outstanding collateral and debt. <small>[MakerDAO Docs: Vat Module](https://docs.makerdao.com/smart-contract-modules/core-module/vat-detailed-documentation)</small>

Empirical analysis of the ETH-A program—the largest collateral type by volume—demonstrates this transparency: between November 2019 and July 2023, all 137,441 vault positions, representing $13.4 billion in DAI debt, were fully traceable on-chain with complete historical state reconstruction. (<small>[Chaleenutthawut et al. (2024), Sec. III](https://dr.ntu.edu.sg/server/api/core/bitstreams/37ceb6fd-f93a-41e0-96ab-84eab35621ac/content) [26], [Data Mining for MakerDAO GitHub](https://github.com/Sudarut-kas/Data-Mining-for-MakerDAO.git) [27]</small>)

A critical design choice distinguishes `Vat` from upgradeable proxy contracts: the core accounting logic is non-upgradeable. Interfaces (`Join adapters`), liquidation modules, and collateral adapters can be governance-updated, but `Vat`'s arithmetic invariant remains immutable. This separation of concerns creates a stark trust hierarchy: governance can modify how collateral enters the system and how debt is enforced, but it cannot rewrite the fundamental accounting equation.This immutability is intentional—it allows users and auditors to place high confidence in Vat's arithmetic even as governance evolves the protocol's operational parameters.(<small>[MakerDAO Docs](https://docs.makerdao.com/smart-contract-modules/collateral-module/join-detailed-documentation)</small>)

### 1.2 State Variables: What Gets Tracked

The Vat maintains a minimal set of state variables to optimize gas efficiency while preserving full auditability. Table 1 summarizes the key variables with their empirical ranges observed across the ETH-A dataset:

---
| Variable | Meaning | Units | Observed Range (ETH-A) | Purpose | Why It Exists |
|-----------|----------|--------|----------|-------------------|----------------|
| `gem[ilk][usr]` | Unlocked collateral held by user | Token wei (10^18) | 0–50,000 ETH | Tracks collateral outside vaults; enables free transfers | To distinguish user-owned tokens from vault-locked ones, preventing double-counting and supporting seamless deposits/withdrawals via adapters. |
| `ink[ilk][urn]` | Locked collateral securing vault's debt | Token wei (10^18) | 0.01–100,000 ETH | Core for collateral value and liquidation checks (`ink * spot`) | Enables per-vault isolation of risk; born from single-collateral DAI need for over-collateralization, scaled for multi-collateral efficiency. |
| `art[ilk][urn]` | Normalized debt (before fee multiplier applied) | Wad (10^18 internal) | 1–100M DAI equiv. | Gas-efficient tracking; actual `debt = art * rate` (in rad: 10^45) | Avoids constant fee recalculations per vault; introduced in `MCD` to handle dynamic rates without per-user storage bloat. |
| `rate[ilk]` | Cumulative stability fee multiplier | Ray (10^27) | 1.0–1.15 × 10^27 | Auto-applies fees to debt via `Jug.drip() or Vat.fold()` | Accumulates interest globally per collateral type; exists to decentralize fee accrual, reducing oracle dependency and gas costs. |
| `spot[ilk]` | Liquidation price: `oracle_price / mat` | Ray (10^27) | 900–4500 DAI/ETH | Pre-computed threshold for safe vaults (`ink * spot >= art * rate`) | Pre-calculates liquidation ratios for *O(1)* checks; key to `MCD`'s gas-optimized safety model, adapting to price feeds without runtime division. |

**Table 1:** Core Vat state variables with empirical ranges from 137,441 ETH-A vaults (Nov 2019–Jul 2023)  (<small>[Chaleenutthawut et al. (2024), Table 1, Fig. 7-8](https://dr.ntu.edu.sg/server/api/core/bitstreams/37ceb6fd-f93a-41e0-96ab-84eab35621ac/content) [26]</small>)

**The debt calculation:**

`Real debt = art × rate`

This design choice—separating normalized debt (`art`) from the fee multiplier (`rate`)—enables gas-efficient fee accrual. Alternative designs charging fees individually to each vault would require *n* state-write operations. By updating a single global `rate` variable, Sky achieves zero per-vault cost for fee distribution. 

![image](https://hackmd.io/_uploads/rJfoLbb1We.png)
*Annual Maker’s interest rate for ETH-A*
Empirical data confirms this efficiency: during the observation period, the stability fee (annualized interest rate) varied from 0% to over 10%, with rate updates applied uniformly across all 137,441 vaults without individual transaction costs. (<small>[Chaleenutthawut et al. (2024), Sec. IV.C, Fig. 5](https://dr.ntu.edu.sg/server/api/core/bitstreams/37ceb6fd-f93a-41e0-96ab-84eab35621ac/content) [26]</small>)

### 1.3 The Fundamental Invariant

The core solvency constraint enforced by Vat is: `ink × spot ≥ art × rate`

**What this means:** Collateral value (adjusted for liquidation buffer) must exceed debt (including accrued fees).

**What this means:** Collateral value (adjusted for liquidation buffer) must exceed debt (including accrued fees).

**What makes this deterministic:**

- `ink`, `art`, `rate` are on-chain state—no trust required
- `spot` is derived from oracle price feeds divided by liquidation ratio (`mat`)
- Inequality is checked by EVM—math cannot be manipulated

For any vault, violation of this invariant triggers liquidation eligibility.



During the empirical study period (Nov 2019–Nov 2021), the liquidation ratio for ETH-A was set at 150%, meaning users must maintain collateral worth at least 1.5× their debt value.  (<small>[Kjaer, Sec. 4.4](https://repositum.tuwien.at/bitstream/20.500.12708/18324/2/Quantitative%20Analysis%20of%20MakerDAOs%20Liquidation%20System.pdf#page=43) [2]</small>.
![Screenshot 2025-10-30 115220](https://hackmd.io/_uploads/B1y1uC-1-l.png)
*The collateralization ratio r(t) and the minimum allowed
collateralization ratio rmin(t) as functions of time.*[Chaleenutthawut et al. (2024), Sec. III, Fig. 3]

**Empirical validation:** Analysis of liquidation events demonstrates deterministic enforcement. During the March 2020 crash ("Black Thursday"), when ETH prices fell 43% within hours, the protocol correctly identified all underwater positions once oracle prices updated. Of 137,441 total vaults analyzed, liquidations occurred precisely when the invariant was violated, with no false positives or negatives in the arithmetic check itself  
<small>([What really happened to MakerDao](https://insights.glassnode.com/what-really-happened-to-makerdao/?utm_source=chatgpt.com), [Chaleenutthawut et al. (2024),](https://dr.ntu.edu.sg/server/api/core/bitstreams/37ceb6fd-f93a-41e0-96ab-84eab35621ac/content)</small>.

**Critical insight:** This invariant guarantees backing *arithmetically*. Whether it guarantees backing *economically* depends on whether `spot` reflects market reality and whether liquidations execute efficiently—factors that failed during Black Thursday, resulting in average Loss Given Default (LGD) of 13% for liquidated positions  
<small>[Chaleenutthawut et al. (2024), Sec. VI.B, Fig. 9](https://dr.ntu.edu.sg/server/api/core/bitstreams/37ceb6fd-f93a-41e0-96ab-84eab35621ac/content) [26]</small>.

The distinction is crucial: the Vat's arithmetic is perfect, but the mechanisms that translate arithmetic into economic reality (oracles, auctions, keeper liquidity) can fail under stress. Part II explores these failure modes in depth.

### 1.4 Pedagogical Code: Simplified IVat Interface
```
interface IVat {
    // Adjust vault (collateral & debt)
    function frob(
        bytes32 ilk,      // collateral type
        address urn,      // vault
        address usr,      // collateral src/dst
        int256 dink,      // Δcollateral
        int256 dart       // Δdebt
    ) external;

    // Liquidate unsafe vault (by Dog)
    function grab(
        bytes32 ilk,
        address urn,
        address v,        // collateral to auction
        address w,        // debt to Vow
        int256 dink,      // seized collateral (−)
        int256 dart       // cancelled debt (−)
    ) external;

    // Move internal DAI (rad = 10^45)
    function move(address src, address dst, uint256 rad) external;
}
```

**Design Insight: Atomicity of `frob`**

The frob function executes collateral and debt adjustments atomically, ensuring that vaults never exist in an intermediate or partially updated state. This design minimizes exposure to front-running and MEV risks arising from transaction reordering.

Empirical observations from the MakerDAO Loan Portfolio Dataset (<small>[Chaleenutthawut et al., 2024](https://dr.ntu.edu.sg/server/api/core/bitstreams/37ceb6fd-f93a-41e0-96ab-84eab35621ac/content)</small>) — which tracks 137,441 ETH-A vaults and millions of transactions between 2019 and 2023 — show no recorded instances of vaults becoming unsafe due to reordering or partial execution during normal frob operations. While the study focuses on credit risk rather than MEV, its comprehensive dataset indirectly supports the protocol’s robustness: every vault adjustment observed adhered to solvency constraints enforced by `Vat`.


### 1.5 Implications: What This Architecture Guarantees (and What It Doesn't)

**What Vat guarantees:**

- Every DAI issued is backed by `art × rate` worth of collateral in `ink`
- Collateral values and debt levels are auditable in real-time with complete historical reconstruction  
<small>[Chaleenutthawut et al. (2024), Sec. V](https://dr.ntu.edu.sg/server/api/core/bitstreams/37ceb6fd-f93a-41e0-96ab-84eab35621ac/content) [26]</small>
- The core arithmetic is non-fudgeable (verified by EVM)

**What Vat does NOT guarantee:**

- That `spot` reflects current market conditions during high volatility (oracle lag averaged 1 hour during Black Thursday)  <small>[How often is the price oracle read](https://www.reddit.com/r/MakerDAO/comments/frfwju/how_often_is_the_price_oracle_read/) </small>
- That liquidation auctions execute efficiently (13% average LGD demonstrates market friction)  <small>[Chaleenutthawut et al. (2024), Sec. VI.B](https://dr.ntu.edu.sg/server/api/core/bitstreams/37ceb6fd-f93a-41e0-96ab-84eab35621ac/content) [26]</small>
- That collateral types maintain value during systemic crashes

The Vat establishes verifiable arithmetic foundations. Remaining sections detail the mechanisms required to translate these foundations into actual backing under stress.

---

Having established how backing is tracked, the next section examines how collateral enters this accounting system.
