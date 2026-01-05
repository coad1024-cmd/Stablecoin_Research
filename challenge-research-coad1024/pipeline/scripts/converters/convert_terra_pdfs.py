"""
Convert Terra PDFs using pymupdf4llm (fallback since marker is missing).
"""
import os
from pathlib import Path
try:
    import pymupdf4llm
except ImportError:
    print("Error: pymupdf4llm not installed.")
    exit(1)

# Setup paths
pdf_dir = Path("challenge-research-coad1024/resources/Terra/papers")
output_dir = Path("challenge-research-coad1024/resources/Terra/converted_papers")
output_dir.mkdir(exist_ok=True, parents=True)

# Get all PDFs
pdf_files = sorted([f for f in pdf_dir.glob("*.pdf") if f.is_file()])
print(f"Found {len(pdf_files)} PDF files to convert in {pdf_dir}\n")

# Convert each PDF
successful = 0
failed = 0

for i, pdf_file in enumerate(pdf_files, 1):
    print(f"\n[{i}/{len(pdf_files)}] Converting: {pdf_file.name}")
    print("-" * 60)
    
    try:
        # Convert using pymupdf4llm
        md_text = pymupdf4llm.to_markdown(str(pdf_file))
        
        # Save to file
        output_file = output_dir / f"{pdf_file.stem}.md"
        output_file.write_text(md_text, encoding="utf-8")
        
        print(f"  ✓ Converted successfully")
        print(f"  ✓ Output: {output_file}")
        print(f"  ✓ Size: {output_file.stat().st_size:,} bytes")
        successful += 1
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        failed += 1

print("\n" + "="*60)
print(f"\nConversion Summary:")
print(f"  ✓ Successful: {successful}/{len(pdf_files)}")
print(f"  ✗ Failed: {failed}/{len(pdf_files)}")
print(f"\nOutput directory: {output_dir.absolute()}")