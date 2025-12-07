"""
Convert a specific PDF to Markdown page-by-page to avoid timeouts and identify issues.
"""
import fitz  # PyMuPDF
import pymupdf4llm
from pathlib import Path
import sys

pdf_path = r"c:/Users/DELL/Desktop/Research Challenge/challenge-research-coad1024/resources/pdfs/Kjaeer Martin - 2021 - Quantitative Analysis of MakerDAOs Liquidation System.pdf"
output_dir = Path("resources/pdfs/converted_pymupdf")
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "Kjaeer Martin - 2021 - Quantitative Analysis of MakerDAOs Liquidation System.md"

print(f"Opening PDF: {pdf_path}")
try:
    doc = fitz.open(pdf_path)
    print(f"Total pages: {doc.page_count}")
except Exception as e:
    print(f"Failed to open PDF: {e}")
    sys.exit(1)

full_text = []

# Clear output file initially
output_file.write_text("", encoding="utf-8")

for i in range(doc.page_count):
    print(f"Converting page {i+1}/{doc.page_count}...", end="", flush=True)
    try:
        # Convert single page
        # pymupdf4llm.to_markdown can take the doc and a pages list
        page_md = pymupdf4llm.to_markdown(doc, pages=[i])
        
        # Append to list
        full_text.append(page_md)
        
        # Append to file immediately to save progress
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(page_md + "\n\n")
            
        print(" Done.")
    except Exception as e:
        print(f" Failed: {e}")
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(f"\n\n<!-- Error converting page {i+1}: {e} -->\n\n")

print(f"\nConversion finished. Saved to: {output_file}")
