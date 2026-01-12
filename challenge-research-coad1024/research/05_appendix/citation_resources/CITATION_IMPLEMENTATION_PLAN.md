# Citation Implementation Plan

**Objective:** Implement academic citation style across all canonical research artifacts  
**Style:** Author-Date with HTML Named Anchors (see `CITATION_STYLE_GUIDE.md`)  
**Priority:** High (required for academic credibility)

---

## Documents Requiring Citations

### Priority 1: Synthesis Documents (High Impact)

- [ ] `Final-Comparative-Report.md` - Main comparative analysis
- [ ] `INDEX.md` - Master index (already has data citations, needs academic refs)

### Priority 2: Deep Dive Papers (Research Quality)

- [ ] `Sky Ecosystem/Decentralization/Artifact/Sky-Decentralization-DeepDive.md`
- [ ] `Sky Ecosystem/Sustainability/Artifact/Sky-Economic-Sustainability.md`
- [ ] `Liquity/02_V2_BOLD/Decentralization/Artifact/Liquity_V2_Decentralization_Analysis.md`
- [ ] `Liquity/02_V2_BOLD/Sustainability/Artifact/Liquity_V2_Economic_Resilience.md`

### Priority 3: Profile Documents (Quick Reference)

- [ ] `Sky Ecosystem/Decentralization/Artifact/Sky_Decentralization_Profile_Jan2026.md`
- [ ] `Sky Ecosystem/Sustainability/Artifact/Sky_Sustainability_Profile_Jan2026.md`
- [ ] `Liquity/01_V1_LUSD/Decentralization/Artifact/Liquity_V1_Decentralization_Profile.md`
- [ ] `Liquity/01_V1_LUSD/Sustainability/Artifact/Liquity_V1_Sustainability_Profile.md`

---

## Common References to Add

### Academic Literature (Stablecoins)

```html
<span id="ref-catalini-degortari"></span>Catalini, C., & de Gortari, A. (2021). *[On the Economic Design of Stablecoins](https://www.nber.org/papers/w29115)*. NBER Working Paper No. 29115.

<span id="ref-klages-stability"></span>Klages-Mundt, A., Harz, D., Gudgeon, L., Liu, J.-Y., & Minca, A. (2022). *[While Stability Lasts: A Stochastic Model of Non-Custodial Stablecoins](https://arxiv.org/abs/2004.01304)*. Mathematical Finance.

<span id="ref-gorton-zhang"></span>Gorton, G., & Zhang, J. (2021). *[Taming Wildcat Stablecoins](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3888752)*. SSRN Electronic Journal.
```

### Protocol Documentation

```html
<span id="ref-makerdao-whitepaper"></span>MakerDAO. (2017). *[The Maker Protocol: MakerDAO's Multi-Collateral Dai (MCD) System](https://makerdao.com/en/whitepaper/)*. Technical Whitepaper.

<span id="ref-liquity-v1-paper"></span>Liquity. (2021). *[Liquity: Decentralized Borrowing Protocol](https://docsend.com/view/bwiczmy)*. Technical Paper.

<span id="ref-liquity-v2-docs"></span>Liquity. (2025). *[Liquity V2 Technical Documentation](https://docs.liquity.org/v2/)*. Protocol Documentation.
```

### Regulatory/Framework References

```html
<span id="ref-basel-framework"></span>Basel Committee on Banking Supervision. (2019). *[The Basel Framework: LCR](https://www.bis.org/basel_framework/standard/LCR.htm)*. Bank for International Settlements.

<span id="ref-fsb-cryptoassets"></span>Financial Stability Board. (2023). *[Regulatory Framework for Crypto-Assets](https://www.fsb.org/2023/07/imf-fsb-synthesis-paper-policies-for-crypto-assets/)*. FSB Report.
```

### Internal Cross-References

```html
<span id="ref-sky-sustainability"></span>Internal Research. (2026). *[Sky Economic Sustainability Analysis](Sky%20Ecosystem/Sustainability/Artifact/Sky-Economic-Sustainability.md)*. Canonical Artifact.

<span id="ref-liquity-v2-decentralization"></span>Internal Research. (2026). *[Liquity V2 Decentralization Analysis](Liquity/02_V2_BOLD/Decentralization/Artifact/Liquity_V2_Decentralization_Analysis.md)*. Canonical Artifact.

<span id="ref-decentralization-framework"></span>Internal Research. (2026). *[Stablecoin Decentralization Framework](../01_frameworks/Stablecoin-Decentralization-Framework.md)*. Methodological Framework.
```

### Data Sources

```html
<span id="ref-data-sky-vow"></span>Sky Protocol Mainnet. (2026). *Vow Contract Balance Query*. Retrieved Jan 5, 2026 via `pipeline/scripts/data_fetchers/fetch_makerdao_data.py`. Contract: `0x...`.

<span id="ref-data-liquity-v2"></span>Liquity V2 Mainnet. (2025). *Trove Snapshot Dataset*. Captured Dec 9, 2025. Source: `analysis/Liquity/data/trove_snapshot_mainnet.csv`.

<span id="ref-liquity-api"></span>Liquity Protocol. (2026). *[Official V2 Statistics API](https://api.liquity.org/v2/ethereum.json)*. Real-time operational data.
```

---

## Implementation Steps

### Step 1: Create Master References File

Create `research/00_canonical/MASTER_REFERENCES.md` with all common citations that can be referenced across documents.

### Step 2: Document-Specific Citations

For each document:

1. Identify claims requiring citations
2. Add in-text citations using `([Author, Year](#ref-id))` format
3. Create References section at end
4. Add `<span id="ref-id"></span>` anchors

### Step 3: Cross-Reference Internal Documents

- Link between canonical artifacts using internal citations
- Reference frameworks and methodologies
- Cite data provenance (scripts, snapshots)

### Step 4: Verification

- [ ] Test all anchor links work (click-through)
- [ ] Verify no broken references
- [ ] Check citation format consistency
- [ ] Ensure all claims have appropriate citations

---

## Example Implementation

### Before (No Citations)

```markdown
Sky Ecosystem shows severe governance concentration with a single delegate controlling 86% of voting power.
```

### After (With Citations)

```markdown
Sky Ecosystem shows severe governance concentration with a single delegate controlling 86% of voting power ([Internal Research, 2026](#ref-sky-decentralization)). This level of plutocratic control is well-documented in governance capture literature ([Catalini & de Gortari, 2021](#ref-catalini-degortari)).
```

### References Section

```markdown
---

## References

<span id="ref-sky-decentralization"></span>Internal Research. (2026). *[Sky Decentralization Profile](Sky%20Ecosystem/Decentralization/Artifact/Sky_Decentralization_Profile_Jan2026.md)*. Canonical Artifact.

<span id="ref-catalini-degortari"></span>Catalini, C., & de Gortari, A. (2021). *[On the Economic Design of Stablecoins](https://www.nber.org/papers/w29115)*. NBER Working Paper No. 29115.
```

---

## Timeline Estimate

- **Priority 1 (Synthesis):** 30-45 minutes per document
- **Priority 2 (Deep Dives):** 45-60 minutes per document  
- **Priority 3 (Profiles):** 20-30 minutes per document

**Total Estimated Time:** 6-8 hours for complete implementation

---

## Next Steps

**Would you like me to:**

1. **Start with Priority 1** - Implement citations in `Final-Comparative-Report.md` first?
2. **Create Master References** - Build `MASTER_REFERENCES.md` with all common citations?
3. **Batch convert specific section** - Pick one document to fully implement as a template?

**Recommendation:** Start with `Final-Comparative-Report.md` as a high-impact showcase, then create `MASTER_REFERENCES.md` to streamline the rest.
