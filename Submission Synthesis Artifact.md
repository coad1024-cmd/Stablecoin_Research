
---

# Submission Synthesis Artifact

## Research Backbone & Integration Map

### Status

**Canonical – Stable**
This document is not rewritten per submission. It is referenced.

---

## 1. Purpose of This Artifact

This document defines the **structural composition** of the research submission and provides a stable mapping between:

* canonical analytical artifacts
* design synthesis artifacts
* modeling artifacts
* the final submission narrative

It exists to ensure:

* internal consistency
* traceability of claims
* clean separation between analysis, design, and modeling
* future reuse without reinterpretation

This document contains **no analysis** and **no conclusions**.

---

## 2. Canonical Research Artifacts

These artifacts are the **source of truth**.
All published, rendered, or summarized materials derive from these.

### 2.1 System Analysis Articles (9)

Each system is analyzed along three orthogonal dimensions.

#### Terra

* A1. Terra — Backing Mechanism
* A2. Terra — Sustainability
* A3. Terra — Decentralization

#### Sky Ecosystem

* A4. Sky — Backing Mechanism
* A5. Sky — Sustainability
* A6. Sky — Decentralization

#### Liquity

* A7. Liquity — Backing Mechanism
* A8. Liquity — Sustainability
* A9. Liquity — Decentralization

Each artifact:

* is mechanism-first
* is self-contained
* excludes design proposals
* excludes modeling conclusions
* defines explicit scope boundaries

---

## 3. Design Synthesis Artifacts (2)

These artifacts abstract across systems and are explicitly **non-empirical**.

* D1. Stablecoin Design with Non-Volatile Collateral
* D2. Stablecoin Design with Highly Volatile Collateral

Properties:

* draw exclusively from A1–A9
* introduce no new system facts
* operate under explicit hypothetical assumptions
* do not claim optimality

---

## 4. Modeling Artifact (1)

* M1. Economic Feasibility of Attacks on Stablecoin Systems

Scope:

* formal modeling of attack cost vs profit
* parameterized, not calibrated
* references only mechanisms defined in A1–A9
* uses mathematical abstraction (Appendix-style)

---

## 5. Supporting Formal Appendices

These are reusable formal components.

* F1. Mathematical Abstraction of Convertibility-Based Backing
* F2. Generic Oracle Latency and Pricing Error Model (if used)

These appendices:

* contain no narrative
* are system-agnostic unless explicitly specialized
* may be reused verbatim across submissions

---

## 6.Rendered Views (Non-Canonical)

The following materials are derived representations of the canonical research artifacts. They exist to support communication, evaluation, comparison, or reuse across different audiences and contexts. They do not constitute sources of truth.

Examples of rendered views include, but are not limited to:

* Paradigm-style research articles
* Academic or preprint papers
* Blog, essay, or Medium-style publications
* Executive technical briefs or reviewer-focused summaries
* Cross-system comparison matrices or synthesis tables
* Design pattern or anti-pattern extractions
* Slide decks or diagram-centric presentations

### Constraints on Rendered Views

All rendered views must adhere to the following constraints:

* They must not introduce new mechanisms, assumptions, or claims
* All substantive statements must be traceable to one or more canonical artifacts, referenced by identifier
* Tone, structure, ordering, and pedagogical framing may vary by audience
* Rendered views may be revised, reformatted, or retired without requiring changes to canonical artifacts
* Rendered views serve as projections of the underlying research, not extensions of it.

---

## 7. Final Submission Assembly

The final submission is a **synthesis layer**, not a research layer.

It:

* references A1–A9, D1–D2, and M1
* summarizes findings without re-deriving them
* demonstrates comparative reasoning across systems
* avoids introducing new definitions or mechanisms

The submission narrative answers:

* *what was analyzed*
* *how systems differ structurally*
* *what design tradeoffs emerge*
* *what attacks are economically plausible*

All detailed reasoning remains in the referenced artifacts.

---

## 8. Change Control Policy

* Canonical artifacts change only when analysis changes.
* Rendered publications may change independently.
* This synthesis artifact changes only if the **structure** changes.

Versioning applies at the artifact level, not the submission level.

---

## 9. Intended Use

This artifact is intended to:

* anchor future submissions
* support external review
* enable rapid synthesis without re-analysis
* demonstrate research discipline and scope control

It is not intended for public publication.

---

## End of Artifact

---

