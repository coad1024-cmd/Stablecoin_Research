"""
Convert selected PDFs to Markdown using pymupdf4llm (lightweight, CPU‑only).
"""
from pathlib import Path
from pymupdf4llm import to_markdown

# List of PDFs to convert (absolute paths)
# List of PDFs to convert (relative paths)
pdf_paths = [
    "resources/literature/Stablecoin2.0.pdf",
    "resources/literature/While Stability Lasts.pdf",
    "resources/literature/What is Stablecoin.pdf",
    "resources/literature/Kjaeer Martin - 2021 - Quantitative Analysis of MakerDAOs Liquidation System.pdf",
]

output_dir = Path("resources/literature/converted_pymupdf")
output_dir.mkdir(parents=True, exist_ok=True)

successful = 0
failed = 0

for i, pdf_path in enumerate(pdf_paths, 1):
    pdf_file = Path(pdf_path)
    print(f"\n[{i}/{len(pdf_paths)}] Converting: {pdf_file.name}")
    print("-" * 60)
    try:
        markdown = to_markdown(str(pdf_file))
        out_path = output_dir / f"{pdf_file.stem}.md"
        out_path.write_text(markdown, encoding="utf-8")
        print(f"  ✓ Successfully converted to {out_path}")
        successful += 1
    except Exception as e:
        print(f"  ✗ Exception: {e}")
        failed += 1

print("\n" + "=" * 60)
print(f"Conversion summary: {successful}/{len(pdf_paths)} succeeded, {failed} failed")
print(f"Outputs stored in: {output_dir.resolve()}")
