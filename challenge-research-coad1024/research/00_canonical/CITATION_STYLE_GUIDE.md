# Citation Style Guide for Canonical Research Artifacts

**Style:** Author-Date with HTML Named Anchors  
**Compatibility:** Markdown + HTML (GitHub-friendly)  
**Academic Standard:** APA/Chicago Author-Date hybrid

---

## In-Text Citations

### Basic Format
```markdown
([Author, Year](#ref-shortname))
```

### Examples

**Single Author:**
```markdown
([Catalini, 2021](#ref-catalini-stablecoins))
```

**Two Authors:**
```markdown
([Catalini & de Gortari, 2021](#ref-catalini-degortari))
```

**Three or More Authors:**
```markdown
([Klages-Mundt et al., 2022](#ref-klages-stability))
```

**Multiple Citations:**
```markdown
([Gorton & Zhang, 2021](#ref-gorton-zhang); [The Basel Framework, 2019](#ref-basel-framework))
```

**Institutional Author:**
```markdown
([The Basel Framework, 2019](#ref-basel-framework))
```

---

## Reference List Format

### Section Header
```markdown
## References
```

### Reference Entry Structure
```html
<span id="ref-shortname"></span>Author(s). (Year). *[Title](URL)*. Publisher/Journal.
```

### Examples

**Academic Paper:**
```html
<span id="ref-catalini-degortari"></span>Catalini, C., & de Gortari, A. (2021). *[On the Economic Design of Stablecoins](https://www.nber.org/papers/w29115)*. NBER Working Paper.
```

**Book:**
```html
<span id="ref-gorton-slapped"></span>Gorton, G. (2010). *Slapped by the Invisible Hand: The Panic of 2007*. Oxford University Press.
```

**Report:**
```html
<span id="ref-basel-framework"></span>The Basel Framework. (2019). *[Liquidity Coverage Ratio](https://www.bis.org/basel_framework/standard/LCR.htm)*. Bank for International Settlements.
```

**Whitepaper/Documentation:**
```html
<span id="ref-makerdao-whitepaper"></span>MakerDAO. (2017). *[The Dai Stablecoin System](https://makerdao.com/whitepaper/)*. Technical Documentation.
```

**Internal Project Reference:**
```html
<span id="ref-sky-sustainability"></span>Research Team. (2026). *[Sky Ecosystem Economic Sustainability Analysis](../Sky%20Ecosystem/Sustainability/Artifact/Sky-Economic-Sustainability.md)*. Project Artifact.
```

**On-Chain Data:**
```html
<span id="ref-etherscan-sky-vow"></span>Etherscan. (2026). *[Sky Vow Contract (0x...)](https://etherscan.io/address/0x...)*. Verified Contract Data (Jan 5, 2026).
```

**API/Subgraph:**
```html
<span id="ref-liquity-api"></span>Liquity Protocol. (2026). *[Official V2 Stats API](https://api.liquity.org/v2/ethereum.json)*. Real-time Data Endpoint.
```

---

## Naming Convention for Anchors

**Format:** `ref-[firstauthor]-[keyword]`

**Examples:**
- `ref-catalini-stablecoins`
- `ref-gorton-zhang`
- `ref-basel-framework`
- `ref-makerdao-whitepaper`
- `ref-sky-sustainability` (internal)

**Rules:**
- All lowercase
- Hyphen-separated
- No special characters
- Maximum 3 words after author name
- Institutional authors use org name (e.g., `ref-basel-framework`)

---

## Data Source Citations

### For On-Chain Verified Data
```html
<span id="ref-data-sky-vow"></span>Ethereum Mainnet. (2026). *Sky Vow Balance Query*. Retrieved via `scripts/fetch_maker_data.js` on Jan 5, 2026. Contract: `0x...`.
```

### For Snapshot Data
```html
<span id="ref-data-liquity-troves"></span>Liquity V2 Mainnet. (2025). *Trove Snapshot Dataset*. Captured Dec 9, 2025. Source: `analysis/Liquity/data/trove_snapshot_mainnet.csv`.
```

---

## Placement Guidelines

1. **In-Text**: Place citation at the end of the claim/sentence
2. **Before Period**: `([Author, Year](#ref-id)).` ✅
3. **After Period**: `([Author, Year](#ref-id))` ❌
4. **Multiple on Same Topic**: Separate with semicolons: `([A, 2020](#ref-a); [B, 2021](#ref-b))`

---

## Converting Existing Documents

### Current Format (No Citations)
```markdown
Sky Ecosystem has high USDC exposure creating centralization risk.
```

### Updated Format (With Citation)
```markdown
Sky Ecosystem has high USDC exposure creating centralization risk ([Research Team, 2026](#ref-sky-decentralization)).
```

### Adding Reference Section
```markdown
---

## References

<span id="ref-sky-decentralization"></span>Research Team. (2026). *[Sky Decentralization Profile](../Sky%20Ecosystem/Decentralization/Artifact/Sky_Decentralization_Profile_Jan2026.md)*. Project Artifact.
```

---

## Template for New Documents

```markdown
# Document Title

**Authors**: Research Team  
**Date**: January 2026  

---

## Abstract

Your abstract here...

---

## 1. Introduction

Your content with citations ([Author, Year](#ref-author-keyword)).

---

## References

<span id="ref-author-keyword"></span>Author, A. (Year). *[Title](URL)*. Publisher.
```

---

## Tools for Verification

**Check broken links:**
```bash
# Run from project root
grep -r "](#ref-" research/00_canonical/ | grep -v "CITATION_STYLE_GUIDE"
```

**Find uncited references:**
```bash
# Find all anchor IDs
grep -r '<span id="ref-' research/00_canonical/ -h | sort | uniq

# Find all citations
grep -r '](#ref-' research/00_canonical/ -h | sort | uniq
```

---

## Common Mistakes to Avoid

❌ **Missing anchor span:**
```markdown
Author. (2021). *Title*. Publisher.
```

✅ **Correct:**
```html
<span id="ref-author"></span>Author. (2021). *Title*. Publisher.
```

❌ **Anchor mismatch:**
```markdown
([Author, 2021](#ref-wrong-name))
...
<span id="ref-correct-name"></span>
```

✅ **IDs must match exactly**

❌ **No italics on title:**
```markdown
On the Economic Design of Stablecoins
```

✅ **Use Markdown italics with linked title:**
```markdown
*[On the Economic Design of Stablecoins](URL)*
```

---

## Priority Documents for Citation Implementation

1. `Final-Comparative-Report.md` - Main synthesis document
2. `Sky Ecosystem/Decentralization/Artifact/Sky-Decentralization-DeepDive.md`
3. `Liquity/02_V2_BOLD/Decentralization/Artifact/Liquity_V2_Decentralization_Analysis.md`
4. `Liquity/01_V1_LUSD/Sustainability/Artifact/Liquity-Economic-Resilience.md`

**Status:** Ready for implementation. See implementation plan in next section.
