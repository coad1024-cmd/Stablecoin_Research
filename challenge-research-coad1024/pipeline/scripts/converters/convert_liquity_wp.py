
import pymupdf4llm
from pathlib import Path

# Paths
pdf_path = Path("resources/Liquity/Liquity v2 - Whitepaper rev. 0.3 (November, 2024) (1).pdf")
output_dir = Path("resources/Liquity/marker_converted")
output_path = output_dir / "Liquity_v2_Whitepaper.md"

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
