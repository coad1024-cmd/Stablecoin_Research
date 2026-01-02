# LLM Context Map: Research Challenge Coad1024

> **For the AI Agent:** This file represents the "Mental Model" of the project. Read this to understand where to find information and where to place new work.

## 1. Project Mission
This is a **forensic research repository** focused on the analysis, design, and modeling of Web3 technologies, specifically **Algorithmic and Hybrid Stablecoins**.
*   **NOT a Software Project:** We are not building a dApp. We are writing research papers and running simulation scripts.
*   **Key Subjects:** Terra (Classic), MakerDAO (Sky), Liquity (LUSD).

## 2. Directory Structure Taxonomy

The project is organized by **Protocol** -> **Research Dimension**.

### The Core (`analysis/`)
This is where 90% of the work lives.
*   `analysis/[Protocol Name]/`:
    *   `Backing Mechanism/`: How the peg is maintained (e.g., PSM, CPMM, Troves).
    *   `Sustainability/`: Business model, revenue vs. expenses, failure modes (e.g., Death Spirals).
    *   `Decentralization/`: Governance, control vectors, oracle dependencies.
    *   `Diagrams/`: Visual assets (Mermaid, SVG, PNG) supporting the articles.
    *   `Drafts/`: Working copies. **Do not edit these unless explicitly told.**
    *   `Article_[Topic].md`: The **Master** publishable documents. **Edit these.**

### The Tools (`pipeline/`)
Scripts for data acquisition and simulation.
*   `pipeline/scripts/`: Python scripts for fetching price data, simulating attacks, or converting formats.

### The Source (`resources/`)
Raw PDF papers and whitepapers. (Read-only reference).

## 3. Key Files & "Sources of Truth"

| File | Purpose |
| :--- | :--- |
| **`Analysis-Meta-framework.md`** | The theoretical lens for the research. Defines the "integrity of backing," "sustainability," and "decentralization" pillars. |
| **`GEMINI.md`** | High-level project tracker and memory bank. |
| **`analysis/Terra/Backing Mechanism/Article_Backing.md`** | **Gold Standard** example of a finished, versioned article. Use this as a style guide. |
| **`analysis/Terra/VERSIONING.md`** | Rules for versioning .md files (YAML frontmatter + Revision History). |

## 4. Rules of Engagement for AI Agents

1.  **Do Not Invent**: When analyzing mechanisms, look at the code references provided in `resources/` or the `x/[module]` folders.
2.  **Scope Strictness**:
    *   *Backing* = The Mechanism (How it works).
    *   *Sustainability* = The Solvency (How it survives or dies).
    *   *Decentralization* = The Control (Who holds the keys).
    *   *Do not mix them.* (e.g., Do not put Attack Analysis in the Backing article).
3.  **Diagrams**: We use Mermaid for flows and SVGs for architecture. Prefer relative paths `Diagrams/[file]` in markdown.
4.  **Versioning**: Always update the YAML version and Revision History when making substantive changes to a Master Article.

## 5. Current State (January 2026)
*   **Terra**: Deep analysis phase. Backing article is polished. Sustainability/Decentralization are in progress.
*   **MakerDAO**: Early draft phase.
*   **Liquity**: Reference phase.
