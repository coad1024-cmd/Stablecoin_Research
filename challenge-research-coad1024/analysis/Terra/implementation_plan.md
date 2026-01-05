# Terra Analysis: Research Acquisition Plan

## Goal

Systematically aggregate a "Prosecutor's Database" of high-quality primary and secondary sources regarding the Terra/Ust collapse. This dataset will fuel the "Death Spiral" analysis.

## Phase 1: Academic & Formal Research (The "Theory")

**Sources**: Arxiv, SSRN, Google Scholar.
**Target Topics**: "Algorithmic Stablecoins", "Death Spirals", "Seigniorage Shares", "Soros Attacks".
**Action**:

- Automated search & download of top 5 cited papers.
- Save to `resources/Terra/papers/`.

## Phase 2: "Grey" Literature (The "Evidence")

**Sources**: Industry Post-Mortems (Nansen, Jump Crypto, Chainalysis), Vitalik's critiques, Matt Levine (Bloomberg).
**Target**: Detailed, forensic timelines of the de-peg.
**Action**:

- Curate list of high-value URLs.
- Fetch and convert to Markdown for RAG/Analysis.
- Save to `resources/Terra/articles/`.

## Phase 3: Source Code Forensics (The "Weapon")

**Targets**:

- `terra-money/classic-core` (The Chain)
- `Anchor-Protocol/anchor-token-contracts` (The Yield Source)
**Action**:
- Clone repositories to `resources/Terra/repos/`.
- Identify key contracts: "Market Module" (Swap Mechanism), "Earn" (Anchor Rate).

## Phase 4: Official Documentation (The "Promise")

**Sources**: Archived Developer Docs (Whitepaper, Stablecoin specs).
**Action**:

- Snapshot archived documentation.
- Save to `resources/Terra/docs/`.

## Execution Tooling

Create `pipeline/scripts/fetch_terra_resources.py`:

1. **Paper Fetcher**: Use `arxiv` API to get PDFs.
2. **Article Scraper**: Use `requests` + `BeautifulSoup` to get text.
3. **Repo Cloner**: Use `gitpython` or `subprocess`.

## Directory Structure

```
resources/Terra/
├── papers/       # PDFs of academic theories
├── articles/     # Markdown of post-mortems
├── repos/        # Cloned source code
└── docs/         # Official whitepapers/specs
```
