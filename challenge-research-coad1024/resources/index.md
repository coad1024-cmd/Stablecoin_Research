# Research Resources

This directory acts as the central repository for all raw materials, external literature, and protocol documentation.

## Directory Structure

```
resources/
├── literature/          # Academic papers & converted PDFs
├── protocols/           # Official protocol documentation
│   ├── Liquity/
│   ├── Sky_Ecosystem/   # (MakerDAO & Sky)
│   └── Terra/
├── notes/               # Rough research notes & HackMD exports
└── index.md             # This file
```

---

## 1. Literature (`resources/literature/`)

Research papers converted to Markdown for analysis.

| Title / File | Topics |
|---|---|
| [(In)Stability for the Blockchain](literature/(In)Stability%20for%20the%20Blockchain.md) | Stability analysis |
| [Algorithmic Stablecoins Analysis](literature/Algorithmic%20Stablecoins-dual%20token%20sim.md) | Algo-stable simulation |
| [Collateral Portfolio Optimization](literature/Collateral%20Portfolio%20Optimization%20in%20Crypto%20Backed%20Stablecoins.md) | Portfolio risk |
| [Designing Stablecoins](literature/Designing%20Stablecoins.md) | Design principles |
| [From Stablecoins to CBDCs](literature/From%20Stablecoins%20to%20CBDCs.md) | Macro view |
| [Kjaeer Martin (2021) - MakerDAO Liquidations](literature/Kjaeer%20Martin%20-%202021%20-%20Quantitative%20Analysis%20of%20MakerDAOs%20Liquidation%20System.md) | **MakerDAO Deep Dive** |
| [Klages-Mundt: While Stability Lasts](literature/While%20Stability%20Lasts.md) | **Canonical Framework** |
| [Liquity V2 Mechanism Design Review](literature/Liquity%20V2%20Mechanism%20Desgin%20Review.md) | **Liquity V2 Source** |
| [On the Economic Design of Stablecoins](literature/On%20the%20Economic%20Design%20of%20Stablecoins.md) | Economics |
| [Setting Standards for Reserves](literature/Setting%20standards%20for%20stablecoin%20reserves.md) | Regulation |
| [Some Simple Economics of Stablecoins](literature/Some%20Simple%20Economics%20of%20Stablecoins.md) | Basic models |
| [Stablecoin 2.0](literature/Stablecoin2.0.md) | Next-gen design |
| [The Libra Reserve](literature/TheLibraReserve_en_US_Rev0814.md) | Historical context |

---

## 2. Protocol Documentation (`resources/protocols/`)

Official local copies of documentation.

### Sky Ecosystem (MakerDAO)
*Location: `resources/protocols/Sky_Ecosystem/`*

- **Legacy MakerDAO:** `legacy_makerdao/intro_docs/`, `legacy_makerdao/technical_docs/`
- **Sky Docs:** `sky_docs/developerguides/`, `sky_docs/sky/`

### Liquity
*Location: `resources/protocols/Liquity/`*

- V2 Mechanism Reviews
- Protocol Specifications

### Terra
*Location: `resources/protocols/Terra/`*

- Historical documentation and post-mortem analysis.

---

## 3. Research Notes (`resources/notes/`)

*Location: `resources/notes/hackmd/`*

Contains raw notes pulled from HackMD, organized by topic:
- **Analysis/DAI**: Deep dives into MakerDAO solvency and mechanics.
- **Design**: Notes on stablecoin design frameworks.

> **Note:** These notes are raw inputs. Canonical research is located in the `research/` directory.
