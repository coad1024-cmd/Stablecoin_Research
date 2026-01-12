# Research Frameworks

**Repository:** Challenge Research Coad1024  
**Date:** January 5, 2026

---

## 1. Hierarchy

This directory contains the canonical analytical frameworks used for the Stablecoin Research Challenge. The hierarchy is:

* **Level 1: Meta-Framework** (Philosophy & Broad Structure)
* **Level 2: Execution Frameworks** (Specific Metrics & Stress Tests per Pillar)

```
research/frameworks/
├── INDEX.md                                   (This file)
├── Stablecoin-Meta-Framework.md               (The "Bible" - Broad Theory)
├── Stablecoin-Decentralization-Framework.md   (Deep Dive: Pillar III)
├── Stablecoin-Sustainability-Framework.md     (Deep Dive: Pillar II)
└── general_backing_framework.md               (Deep Dive: Pillar I - Universal)
```

---

## 2. Framework Summaries

### [Stablecoin-Meta-Framework.md](./Stablecoin-Meta-Framework.md)

* **Scope:** The overarching philosophy of "Stablecoin LEGO" analysis.
* **Pillars:** Backing Integrity, Economic Sustainability, Decentralization.
* **Use Case:** Use this to define *what* good analysis looks like at a high level.

### [Stablecoin-Decentralization-Framework.md](./Stablecoin-Decentralization-Framework.md)

* **Scope:** Rigorous quantification of control distribution.
* **Key Models:** Decentralization Envelope `D = (G,C,O,E)`, Stress Tests.
* **Status:** Merged & Unified (Version 3.0).
* **Use Case:** Use this to generate the "Decentralization Scorecard" for any protocol.

### [Stablecoin-Sustainability-Framework.md](./Stablecoin-Sustainability-Framework.md)

* **Scope:** Economic viability and business model analysis.
* **Key Models:** Net Interest Margin (NIM), Liquidation Dependency Ratio (LDR), Surplus Buffer Runway.
* **Use Case:** Use this to assess if a protocol can survive long-term.

### [general_backing_framework.md](./general_backing_framework.md)

* **Scope:** The Universal "Physics of Backing" (Pillar I).
* **Key Models:** WACS (Asset Quality), LCR (Liquidity), Dynamic Mechanism (Auctions/Redemptions).
* **Use Case:** The standard template for analyzing ANY stablecoin's backing.

---

## 3. Usage Guidelines

1. **Start** with the *Meta-Framework* to understand the "Why".
2. **Apply** the *Execution Frameworks* to gather the "Data".
3. **Synthesize** findings into the final protocol profile (e.g., `Sky_Sustainability_Profile.md`).
