
import pymupdf4llm
from pathlib import Path

# Paths
pdf_path = Path("resources/pdfs/Algorithmic Stablecoins-dual token sim.pdf")
output_dir = Path("resources/pdfs/converted")
output_path = output_dir / "Algorithmic Stablecoins-dual token sim.md"

# Ensure output directory exists
output_dir.mkdir(parents=True, exist_ok=True)

print(f"Converting {pdf_path}...")

try:
    if not pdf_path.exists():
        print(f"Error: File not found at {pdf_path}")
    else:
        # Convert
        md_text = pymupdf4llm.to_markdown(str(pdf_path))
        
        # Save
        output_path.write_text(md_text, encoding="utf-8")
        
        print(f"Success! Saved to {output_path}")
        print(f"Size: {output_path.stat().st_size} bytes")

except Exception as e:
    print(f"Error: {e}")
