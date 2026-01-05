# Stablecoin Decentralization Assessment Framework

**Version:** 2.0  
**Last Updated:** January 5, 2026  
**Status:** Validated

---

## 1. Overview

This framework provides a rigorous, quantitative methodology for assessing the decentralization of overcollateralized stablecoins. Decentralization is measured across three orthogonal dimensions, each with specific metrics, thresholds, and real-world benchmarks.

**Core Principle:** On-chain code is necessary but insufficient. Decentralization must survive *adversarial* states — that's where most protocols fail.

---

## 2. The Three Dimensions of Decentralization

### 2.1 Governance Decentralization (G)

**Definition:** The distribution of decision-making power among token holders.

**Metrics:**
- Gini coefficient of governance token holdings
- Top-N address share (voting power concentration)
- Voter turnout and delegation concentration
- Effective control threshold (minimum coalition to pass votes)

### 2.2 Collateral Decentralization (C)

**Definition:** The diversity and independence of assets backing the stablecoin.

**Metrics:**
- Herfindahl-Hirschman Index (HHI) across collateral types
- Single counterparty exposure (largest issuer/custodian)
- On-chain vs off-chain collateral ratio
- Jurisdictional concentration

### 2.3 Operational Decentralization (O)

**Definition:** The resilience of critical infrastructure (liquidators, oracles) to concentrated failure.

**Metrics:**
- Keeper/liquidator market share (HHI)
- Oracle source diversity
- Off-chain dependency points
- Infrastructure liveness during stress events

---

## 3. Quantitative Thresholds

All thresholds are derived from established regulatory standards and academic literature.

### 3.1 Governance Thresholds

| Metric | Green (Decentralized) | Yellow (Moderate) | Red (Centralized) | Regulatory Basis |
|:---|:---|:---|:---|:---|
| **Gini Coefficient** | < 0.70 | 0.70 - 0.85 | > 0.85 | Wealth inequality studies; Bitcoin Gini = 0.88 |
| **Top-5 Voting Share** | < 30% | 30% - 50% | > 50% | SEC "control" definitions (25-50%) |

**Citations:**
- Srinivasan & Lee, "Quantifying Decentralization" (2017): Nakamoto coefficient and distribution metrics
- SEC Rule 13d: 10%+ ownership triggers disclosure; 25%+ considered control
- Glassnode Bitcoin Wealth Distribution: Top 1% holds ~27% of BTC

### 3.2 Collateral Thresholds

| Metric | Green (Decentralized) | Yellow (Moderate) | Red (Centralized) | Regulatory Basis |
|:---|:---|:---|:---|:---|
| **HHI (Collateral Types)** | < 0.25 | 0.25 - 0.50 | > 0.50 | DOJ Merger Guidelines (2010) |
| **Single Counterparty** | < 20% | 20% - 40% | > 40% | Basel III Large Exposures (25%) |

**Citations:**
- U.S. Department of Justice Horizontal Merger Guidelines (2010):
  - HHI < 1500 (0.15): Unconcentrated
  - HHI 1500-2500 (0.15-0.25): Moderately concentrated
  - HHI > 2500 (0.25): Highly concentrated
- Basel III Large Exposures Framework (2014): 25% single counterparty limit for banks
- Adapted for crypto: 20% threshold accounts for higher volatility

### 3.3 Operational Thresholds

| Metric | Green (Decentralized) | Yellow (Moderate) | Red (Centralized) | Regulatory Basis |
|:---|:---|:---|:---|:---|
| **Top-5 Keeper Share** | < 50% | 50% - 70% | > 70% | Oligopoly economics (CR4 > 40%) |
| **Oracle Sources** | ≥ 5 independent | 3-4 independent | ≤ 2 independent | Byzantine fault tolerance (n ≥ 3f+1) |

**Citations:**
- U.S. Census Bureau market concentration: CR4 > 40% = oligopoly
- Lamport, Shostak & Pease (1982): Byzantine fault tolerance requires n ≥ 3f+1 nodes
- Black Thursday (March 2020): Keeper withdrawal led to $0 liquidation bids

---

## 4. Composite Decentralization Score

### 4.1 Formula

```
D = w_G × G + w_C × C + w_O × O
```

**Where:**
- **G** = Governance Score = `1 - Gini`
- **C** = Collateral Score = `1 - HHI`
- **O** = Operational Score = `0.6 × (1 - Keeper_HHI) + 0.4 × min(1, oracle_count / 5)`

**Default Weights:**
- w_G = 0.35 (Governance)
- w_C = 0.35 (Collateral)
- w_O = 0.30 (Operational)

### 4.2 Score Interpretation

| Composite Score | Classification | Implication |
|:---|:---|:---|
| D > 0.70 | **Decentralized** | Resilient to single-point failures |
| D = 0.50 - 0.70 | **Moderate Centralization** | Vulnerable under coordinated stress |
| D < 0.50 | **Centralized** | Single actors can compromise system |

### 4.3 Binding Constraint Rule

**If ANY individual dimension (G, C, or O) falls into "Red", the composite score is capped at 0.50 regardless of the weighted calculation.**

*Rationale:* A chain is only as strong as its weakest link. Perfect governance cannot compensate for total collateral concentration.

---

## 5. Stress Test Framework

### 5.1 Test 1: Collateral Freeze (USDC/RWA Freeze)

| Parameter | Specification |
|:---|:---|
| **Scenario** | 100% of USDC collateral frozen by issuer |
| **Input** | Current USDC backing percentage |
| **Measure 1** | Percentage of vaults now undercollateralized |
| **Measure 2** | Total DAI requiring immediate liquidation |
| **Measure 3** | Keeper capacity vs required liquidation volume |
| **Output** | Expected bad debt (DAI) |

### 5.2 Test 2: Keeper Withdrawal (Liquidator Exit)

| Parameter | Specification |
|:---|:---|
| **Scenario** | Top 3 keepers withdraw during 50% ETH crash |
| **Input** | Keeper concentration data, ETH vault distribution |
| **Measure 1** | Remaining liquidation capacity (%) |
| **Measure 2** | Liquidation backlog (DAI volume) |
| **Output** | Bad debt from delayed liquidations |

### 5.3 Test 3: Oracle Outage

| Parameter | Specification |
|:---|:---|
| **Scenario** | Primary oracle source fails for 60 minutes |
| **Input** | OSM delay, oracle redundancy count |
| **Measure 1** | Price staleness during outage |
| **Measure 2** | Vaults that should have been liquidated but weren't |
| **Output** | Accumulated bad debt from oracle blindness |

---

## 6. Risk Channels

### Channel 1: Governance Capture

**Mechanism:** Top MKR holders coordinate to modify liquidation ratios or block emergency measures.

**Short-term effect:** Preserve their own positions.  
**Long-term effect:** Capture protocol fees; undermine neutrality.

**Measure:** Simulate scenario where top 5 addresses vote to reduce liquidation penalties; compute expected change in tail risk.

### Channel 2: Collateral Contagion

**Mechanism:** If USDC issuer freezes funds or RWA custodian is sanctioned, usable collateral drops by ΔC.

**Effect:** Required overcollateralization rises → more vaults undercollateralized → fire sales → contagion.

**Measure:** Remove top 2 collateral types and compute fraction of vaults hitting liquidation thresholds.

### Channel 3: Liquidity Provider Withdrawal

**Mechanism:** Sudden withdrawal of top N keepers increases liquidation slippage.

**Effect:** Price impact amplifies; combined with oracle delay, insolvency cascades.

**Measure:** If L_capacity < needed_sell_volume, compute price impact and residual bad debt.

---

## 7. Recommendations

### 7.1 Governance

- **Voting power decay:** Cap effective voting weight for large positions
- **Quorum plus dispersion:** Require votes from ≥ K distinct addresses
- **Target:** Top-5 share < 30%

### 7.2 Collateral Policy

- **USDC Cap:** Hard limit at **20%** of total collateral (per Basel III guidance)
- **RWA Ramp:** Require ≥ 2 custodians for any tranche > **$100M**
- **Target:** HHI < 0.25

### 7.3 Operational Resilience

- **Keeper subsidies:** Protocol incentives for small keepers during stress
- **AMM fallback:** Automated partial liquidation when keeper depth insufficient
- **Target:** Top-5 keeper share < 50%

### 7.4 Oracle Redundancy

- **Minimum sources:** At least **3 independent oracle families**
- **Divergence threshold:** If feeds diverge > **5%**, halt risky liquidations
- **Performance bond:** **0.1 ETH** bond for keepers, slashed if withdrawal during > 30% price drop

---

## 8. Submission Checklist

A complete decentralization analysis MUST include:

- [ ] Precise definitions for G, C, O with formulas
- [ ] Current snapshot numbers from on-chain data
- [ ] 2-3 stress scenarios with quantified impacts
- [ ] Concrete mitigations with specific parameters
- [ ] Citations to Klages-Mundt, Kjaeer, SOK Blockchain Governance
- [ ] Diagram showing centralization channels and failure propagation

---

## 9. Failure Propagation Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        STABLECOIN SYSTEM                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  [Users] ──► [Vaults] ──► [Collateral Pool]                            │
│                                 │                                       │
│                    ┌────────────┴────────────┐                         │
│                    ▼                         ▼                         │
│           {On-chain Assets}         {Off-chain Assets}                 │
│           (ETH, WBTC, LSTs)         (USDC, RWAs)                       │
│                    │                         │                         │
│                    │              ┌──────────┴──────────┐              │
│                    │              │  FREEZE RISK        │              │
│                    │              │  (Issuer/Custodian) │              │
│                    │              └──────────┬──────────┘              │
│                    │                         │                         │
│  [Governance] ────►│◄──── [Policy Controls] ◄┘                         │
│  (MKR/SKY)         │      (PSM, Debt Ceilings)                         │
│       │            │                                                   │
│       │   CAPTURE  │                                                   │
│       │   RISK     │                                                   │
│       ▼            │                                                   │
│  [Keepers] ───────►│◄──── [Liquidation Market] ◄── [DEXes/AMMs]       │
│       │            │                                                   │
│       │  WITHDRAWAL│                                                   │
│       │  RISK      │                                                   │
│       ▼            │                                                   │
│  [Oracles] ───────►│◄──── [Price Feeds] ──► [Liquidation Triggers]    │
│       │            │                                                   │
│       │  OUTAGE    │                                                   │
│       │  RISK      │                                                   │
│       ▼            ▼                                                   │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │                     FAILURE CASCADE                              │  │
│  │  Freeze → Collateral ↓ → Vaults Insolvent → Liquidation ↑ →    │  │
│  │  Keeper Exit → Bad Debt → Emergency Shutdown (Centralized)       │  │
│  └─────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 10. References

### Regulatory Standards
1. **U.S. DOJ (2010).** "Horizontal Merger Guidelines." HHI concentration thresholds.
2. **Basel Committee (2014).** "Large Exposures Framework." BCBS 283. Single counterparty limits.
3. **SEC Rule 13d.** Beneficial ownership disclosure and control definitions.

### Academic Foundations
4. **Klages-Mundt, A. et al. (2020).** "Stablecoins 2.0: Economic Foundations and Risk-based Models." *Advances in Financial Technologies*.
5. **Gudgeon, L. et al. (2020).** "DeFi Protocols for Loanable Funds." *FC 2020*.
6. **Perez, D. et al. (2021).** "Liquidations: DeFi on a Knife-edge." *FC 2021*.
7. **Lamport, L., Shostak, R. & Pease, M. (1982).** "The Byzantine Generals Problem." *ACM TOPLAS*.

### Governance & Decentralization
8. **Srinivasan, B. & Lee, L. (2017).** "Quantifying Decentralization."
9. **Reijers, W. et al. (2021).** "SOK: Blockchain Governance." *arXiv:2105.05460*.
10. **Barbereau, T. et al. (2022).** "Decentralised Finance's Unregulated Governance." *Journal of Risk and Financial Management*.

---

## 11. Applicability

This framework is designed to be **protocol-agnostic** and applicable to any overcollateralized stablecoin system, including but not limited to:

| Protocol | Governance Token | Stablecoin | Notes |
|:---|:---|:---|:---|
| **Sky Ecosystem** | SKY/MKR | DAI/USDS | CDP-based, RWA integration |
| **Liquity** | LQTY | LUSD | Governance-minimized, ETH-only |
| **Aave GHO** | AAVE | GHO | Facilitator model |
| **crvUSD** | CRV | crvUSD | Soft liquidations |
| **Frax** | FXS | FRAX | Partially algorithmic |

### Adaptation Notes

When applying this framework to different protocols:

1. **Liquity:** Governance dimension (G) is structurally minimized by design. Weight may be reduced to w_G = 0.15 with justification.

2. **Algorithmic components:** For partially algorithmic stablecoins (e.g., Frax), add a fourth dimension for "Algorithmic Risk" (A) measuring peg mechanism concentration.

3. **L2 deployments:** For multi-chain protocols, operational decentralization (O) should include cross-chain bridge concentration as a metric.

---

*This framework provides a quantitative, defensible methodology for decentralization assessment. All thresholds are grounded in established regulatory and academic standards, and the methodology is designed to be applied across any overcollateralized stablecoin system.*

