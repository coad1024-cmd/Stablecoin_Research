# Research Article Versioning System

This document outlines the standard versioning and metadata conventions for the Terra analysis research repository.

## 1. File Structure

All research articles (`.md` files) must begin with a YAML frontmatter block containing metadata about the document.

### YAML Frontmatter Template

```yaml
---
title: "Full Title of the Article"
version: 1.0.0  # Semantic Versioning
status: Draft   # Options: Draft, In Review, Final, Deprecated
date: YYYY-MM-DD # Last major update date
authors: ["Author Name"]
tags: ["Topic1", "Topic2"] # Optional
---
```

## 2. Versioning Scheme

We follow a simplified **Semantic Versioning (SemVer)** scheme: `MAJOR.MINOR.PATCH`.

*   **MAJOR (1.0.0)**: Use for significant rewrites, structural changes, or finalization of a major draft.
*   **MINOR (0.1.0)**: Use for adding new sections, substantial edits to existing content, or elaborating on arguments.
*   **PATCH (0.0.1)**: Use for typo fixes, minor clarifications, formatting adjustments, or diagram updates.

### Status Definitions

*   **Draft**: Work in progress. Content may be incomplete or unverified.
*   **In Review**: Complete draft submitted for peer review.
*   **Final**: Accepted and verified version.
*   **Deprecated**: Superseded by newer analysis or proven incorrect.

## 3. Revision History

Every article must append a **Revision History** table at the very end of the document to track changes over time.

### Table Format

```markdown
## Revision History

| Version | Date       | Author          | Description                                    |
| :---    | :---       | :---            | :---                                           |
| 1.0.1   | 2026-01-03 | Internal Research   | Fixed typos in Section 2.1                     |
| 1.0.0   | 2026-01-02 | Internal Research   | Initial standardized version                   |
```

## 4. Best Practices

1.  **Duplicate vs. Version**: Do not create generic file copies like `Article_v2.md`. Instead, update the version number in the YAML header of the main file and log the change in the revision history. Old versions can be retrieved via git history if needed.
2.  **Drafts Directory**: Use the `Drafts/` directory for experimental snippets or scratchpads that are not yet ready to be part of the main document history.
3.  **Commit Messages**: Align git commit messages with the version update (e.g., "chore: bump version to 1.1.0 - added Oracle analysis").
