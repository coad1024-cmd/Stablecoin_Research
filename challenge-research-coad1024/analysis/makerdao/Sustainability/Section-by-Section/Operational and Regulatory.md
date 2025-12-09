# Operational and Regulatory (MakerDAO)

**Goal**: Quantify the external threats to MakerDAO's sustainability: Regulation, Custody, and Operations.

---

## 1. Regulatory Risk Profile

MakerDAO's "Endgame" explicitly embraces regulatory integration to scale.

* **RWA Seizure Risk**: High. Billions in US T-bills are held by custodians (Coinbase, Sygnum). These can be frozen by a court order.
* **Regulatory Moat**: High. By complying with MiCA (indirectly via partners) and holding "clean" assets, Maker avoids being targeted as a shadow bank.

**Diagram**: Regulatory Radar
![Regulatory Radar](../Diagrams/Operational%20and%20Regulatory/regulatory_risk_radar.png)

## 2. Custody Risk (The Hidden Liability)

Unlike on-chain smart contracts, RWA custody relies on legal contracts.

| Custodian | Asset Type | Risk |
| :--- | :--- | :--- |
| **Coinbase** | USDC (PSM) | Counterparty / Regulatory Freeze. |
| **Clydesdale** | T-Bills | Trustee Risk / Slow Liquidation. |
| **BlockTower** | Private Credit | Credit Default / Valuation Opacity. |

## 3. Operational Bottlenecks

### A. Governance Overhead

* **Issue**: Managing RWAs requires huge human effort (Legal, rWAs foundations).
* **Cost**: High fixed OpEx.
* **Latency**: Signing legal documents takes weeks. "Crypto speed" meets "Legal speed."

### B. Oracle Dependence

* MakerDAO runs the "Chronicle" (formerly Maker Oracle) network.
* **Sustainability**: It is a cost center, financed by the protocol.

---

## Conclusion

MakerDAO has traded **Operational Simplicity** for **Scale**. Its sustainability now depends on its ability to navigate the legal system as much as the blockchain.
