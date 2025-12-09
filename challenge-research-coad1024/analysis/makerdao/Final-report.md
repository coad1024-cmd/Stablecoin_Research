# DAI — Decentralization Analysis (Full, Bulletproof, Research-Grade)

## **Executive Summary**

DAI is not fully decentralized: while the protocol is permissionless at the smart-contract layer, its economic security and governance outcomes are dominated by centralized counterparties, a small set of delegates, and RWA custodial dependencies.

> **Short verdict:** DAI is *hybrid* — decentralized in machinery, centralized in power.

---

# 1. What “Decentralization” Means (Three Measurable Dimensions)

*(No figures required here)*

---

# 2. Appearance vs. Reality Under Stress

*(No figures required here)*

---

# 3. Evidence of Centralization (Your Extracted Metrics)

---

## **A. Governance Centralization**

---

### **A1. MKR Holder Inequality**

From your distribution snapshot:

* **Gini:** 0.9886
* **Top 1%:** 90.53%
* **Top 10 holders:** 29.89%

**Insert Figure G1 — MKR Holder Distribution (Top 20)**

**[Figure G1 — MKR Holder Distribution (Top 20) - Pending Real-Time Data Pipeline]**

---

### **A2. Delegation Concentration**

* **Top delegate:** 86.56%
* **Top 5 delegates:** 99.16%

**Insert Figure G2 — Delegation Concentration**

**[Figure G2 — Delegation Concentration - Pending Real-Time Data Pipeline]**

---

### **A3. Voting Power / Turnout**

From your governance dataset:

* **Avg turnout:** 15.78%
* **Unique voters:** 10–16
* **Top voter share:** ~53%

**Insert Figure G3 — MKR Governance Turnout Over Time**

**[Figure G3 — MKR Governance Turnout Over Time - Pending Real-Time Data Pipeline]**

---

### **Governance verdict:**

**Governance is decentralized in form, centralized in function.**

---

## **B. Collateral Centralization**

---

### **B1. Collateral Composition**

**Insert Figure C1 — Collateral Composition Breakdown (ETH, WBTC, USDC, RWAs)**

**[Figure C1 — Collateral Composition Breakdown - Pending Real-Time Data Pipeline]**

---

### **B2. Collateral Concentration Metrics**

HHI: 2340
CR3: 80.27%
CR5: 93.47%

**Insert Figure C2 — Collateral Concentration (HHI, CR3, CR5)**

**[Figure C2 — Collateral Concentration (HHI, CR3, CR5) - Pending Real-Time Data Pipeline]**

---

### **B3. Single-Counterparty Exposure**

**Insert Figure C3 — RWA & Custodian Exposure**

**[Figure C3 — RWA & Custodian Exposure - Pending Real-Time Data Pipeline]**

Caption:
*Share of DAI collateral controlled by each custodial class (Circle/Coinbase, U.S. banks, BitGo, trustless ETH).*

---

## **Collateral Verdict:**

DAI is *not decentralized* in its collateral backing.

---

## **C. Operational Decentralization**

---

### **C1. Keeper / Liquidator Distribution (ETH-A)**

**Insert Figure O1 — Keeper Concentration (Top 10)**

**[Figure O1 — Keeper Concentration (Top 10) - Pending Real-Time Data Pipeline]**

Caption:
*Distribution of liquidation volume among ETH-A keeper addresses.*

---

### **C2. Oracle Dependence**

**Insert Figure O2 — Oracle Architecture Diagram**

**[Figure O2 — Oracle Architecture Diagram - Pending Real-Time Data Pipeline]**

---

### **C3. RWA Legal & Custody Stack**

**Insert Figure O3 — RWA Custody Stack Diagram**

**[Figure O3 — RWA Custody Stack Diagram - Pending Real-Time Data Pipeline]**

---

# 4. Systemic Failure Channels

### **Insert Figure F1 — Failure Propagation Pathways (Governance → Collateral → Operations)**

![Figure F1 — Failure Propagation Pathways - Pending Real-Time Data Pipeline]

---

# 5. Recommendations

### **Optional Figure R1 — Summary of Mitigation Strategies**

![Figure R1 — Decentralization Mitigation Strategies - Pending Real-Time Data Pipeline]

---

# 6. Overall Scorecard

### **Insert Figure S1 — Decentralization Radar Chart (G / C / O)**

![Figure S1 — Decentralization Scorecard Radar - Pending Real-Time Data Pipeline]

---

# 7. References

*(no images)*

---

# ✔ Summary Table (Text Only)

| Dimension          | Score     | Summary                                                           |
| ------------------ | --------- | ----------------------------------------------------------------- |
| **Governance (G)** | **1/5**   | Delegate dominance → >50% single-actor control                    |
| **Collateral (C)** | **1.5/5** | USDC + RWA dominance → 74% custodial                              |
| **Operations (O)** | **2.5/5** | Strong keepers, weak oracles, centralized custodians              |
| **Overall**        | **1.7/5** | Architecture decentralized, incentives & dependencies centralized |
