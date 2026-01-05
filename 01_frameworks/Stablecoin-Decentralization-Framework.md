# Stablecoin Decentralization Assessment Framework

**Version:** 3.0 (Merged & Unified)  
**Last Updated:** January 5, 2026  
**Status:** Canonical

---

## 1. Methodological Premise

> **Decentralization is evaluated as control distribution under adversarial conditions, not as architectural intent in steady state.**

This framework assesses decentralization as a **state-dependent property**, focusing on who retains decision authority, execution power, and control over redemption outcomes during periods of market stress. A protocol is decentralized only within a bounded **Operating Envelope**; outside this envelope, control paths often collapse to centralized actors.

---

## 2. The Four Dimensions of Decentralization

Decentralization is decomposed into four orthogonal dimensions. Let the decentralization state be valid only if:
`D = (G, C, O, E)` where failure in any dimension compromises the system.

### 2.1 Governance Decentralization (G)
**Question:** Who can modify protocol parameters, alter redemption rules, or trigger upgrades?
**Metrics:**
- Gini coefficient of governance token
- Top-N voting share (effective control)
- Governance latency vs. Crisis half-life

### 2.2 Collateral Decentralization (C)
**Question:** What ultimately backs redemptions, and how independent are those backing sources?
**Metrics:**
- HHI across collateral types (Backing diversity)
- Single counterparty exposure (Issuer/Custodian risk)
- Endogenous vs Exogenous backing share

### 2.3 Operational Decentralization (O)
**Question:** Who executes critical infrastructure (liquidations, oracles) in real-time?
**Metrics:**
- Keeper market share (HHI)
- Oracle source diversity & independence
- Infrastructure dependencies (bridges, specific RPCs)

### 2.4 Emergency/Control-Path Decentralization (E)
**Question:** Who can halt, override, or reconfigure the system during emergencies?
**Metrics:**
- Existence of emergency controls (pause, shutdown, guardians)
- Multisig threshold & signer diversity
- Discretionary vs. Algorithmic triggers

---

## 3. Quantitative Thresholds & Scoring

Derived from regulatory standards (DOJ, Basel, SEC) and academic literature.

### 3.1 Governance Thresholds (G)

| Metric | Green (Decentralized) | Yellow (Moderate) | Red (Centralized) | Benchmark Source |
|:---|:---|:---|:---|:---|
| **Gini Coefficient** | < 0.70 | 0.70 - 0.85 | > 0.85 | Crypto Wealth Studies; BTC~0.88 |
| **Top-5 Voting Share** | < 30% | 30% - 50% | > 50% | SEC "Control" (25-50%) |

### 3.2 Collateral Thresholds (C)

| Metric | Green (Decentralized) | Yellow (Moderate) | Red (Centralized) | Benchmark Source |
|:---|:---|:---|:---|:---|
| **HHI (Backing)** | < 0.25 | 0.25 - 0.50 | > 0.50 | DOJ Merger Guidelines |
| **Single Counterparty** | < 20% | 20% - 40% | > 40% | Basel III Large Exposure (25%) |

### 3.3 Operational Thresholds (O)

| Metric | Green (Decentralized) | Yellow (Moderate) | Red (Centralized) | Benchmark Source |
|:---|:---|:---|:---|:---|
| **Top-5 Keeper Share** | < 50% | 50% - 70% | > 70% | Oligopoly Economics (CR4 >40%) |
| **Oracle Sources** | ≥ 5 independent | 3-4 independent | ≤ 2 independent | Byzantine Fault Tolerance |

### 3.4 Emergency Thresholds (E)

| Metric | Green (Decentralized) | Yellow (Moderate) | Red (Centralized) | Benchmark Source |
|:---|:---|:---|:---|:---|
| **Emergency Control** | None / Timelock only | DAO Vote / High-Threshold Multisig | Small Multisig (<5) / Instant | Operational Security |

---

## 4. Composite Decentralization Score

### 4.1 Formula

```
D_score = w_G*G + w_C*C + w_O*O + w_E*E
```

**Where:**
- **G** = `1 - Gini`
- **C** = `1 - HHI_collateral`
- **O** = `0.6*(1 - Keeper_HHI) + 0.4*Oracle_Score`
- **E** = `1` if automated/DAO controlled, `0.5` if multisig constrained, `0` if centralized multisig.

**Default Weights:** w_G=0.25, w_C=0.30, w_O=0.25, w_E=0.20

### 4.2 Binding Constraint / Interpretation Rule
> **If ANY individual dimension falls into "Red" (Centralized), the composite score is capped at 0.50 ("Centralized") regardless of the weighted calculation.**

| Score | Classification | Implication |
|:---|:---|:---|
| > 0.70 | **Decentralized** | Resilient to single-point failures |
| 0.50 - 0.70 | **Boundedly Decentralized** | Vulnerable under coordinated stress |
| < 0.50 | **Centralized** | Small group controls outcomes |

---

## 5. Stress Test Framework (Required)

### 5.1 Test 1: Collateral/Backing Freeze
| Spec | Detail |
|:---|:---|
| **Scenario** | 100% of largest centralized asset (USDC/RWA) frozen. |
| **Measure** | % of vaults insolvent; Required liquidation volume vs. Keeper capacity. |
| **Output** | Bad debt estimate. |

### 5.2 Test 2: Execution Vacuum (Keeper Exit)
| Spec | Detail |
|:---|:---|
| **Scenario** | Top 3 keepers exit during 50% price crash. |
| **Measure** | Remaining capacity; Liquidation backlog latency. |
| **Output** | Price impact from delayed liquidations. |

### 5.3 Test 3: Emergency Capture
| Spec | Detail |
|:---|:---|
| **Scenario** | Emergency (E) actors coordinate to alter protocol state. |
| **Measure** | Time to execute vs. Governance response time. |
| **Output** | Probability of successful capture. |

---

## 6. Failure Propagation Diagram

```
┌────────────────────────────────────────────────────────┐
│               STABLECOIN FAILURE CASCADE               │
├────────────────────────────────────────────────────────┤
│  [Market Shock] ──► [Collateral Value ↓]               │
│                            │                           │
│  [Regulatory Event] ──► [Freeze Risk]                  │
│                            │                           │
│                            ▼                           │
│                   [Vault Insolvency]                   │
│                            │                           │
│                            ▼                           │
│  [Keeper Exit?] ────► [Liquidation Capacity?] ◄── [O]  │
│                            │                           │
│        ┌───────────────────┴──────────────────┐        │
│        ▼                                      ▼        │
│    [Successful]                          [Failed Liq]  │
│    (Peg Holds)                           (Bad Debt)    │
│                                               │        │
│                                               ▼        │
│                          [Emergency Shutdown?] ◄── [E] │
│                                  │                     │
│                        ┌─────────┴─────────┐           │
│                        ▼                   ▼           │
│                [Redemption]           [Capture]        │
└────────────────────────────────────────────────────────┘
```

---

## 7. References

### Regulatory Standards
1. **U.S. DOJ (2010).** "Horizontal Merger Guidelines." (HHI thresholds).
2. **Basel Committee (2014).** "Large Exposures Framework." (25% limit).
3. **SEC Rule 13d.** (Control definitions).

### Academic Foundations
4. **Klages-Mundt, A. et al.** "Stablecoins 2.0."
5. **Gudgeon, L. et al.** "DeFi Protocols for Loanable Funds."
6. **Lamport, L. et al.** "The Byzantine Generals Problem."

---

## 8. Applicability Notes

| Protocol | Governance (G) | Collateral (C) | Operations (O) | Emergency (E) |
|:---|:---|:---|:---|:---|
| **Sky (DAI)** | High Weight | Critical (RWAs) | Critical (Keepers) | Critical (ESM) |
| **Liquity** | *Minimized* | ETH (Low Risk) | Keepers (Critical) | *Algorithmic* |
| **Frax** | High Weight | Mix (Algo+RWA) | AMO (Critical) | Multisig |

*Framework adapted for cross-protocol comparison.*
