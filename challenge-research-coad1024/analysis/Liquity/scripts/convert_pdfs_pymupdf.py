import os
import pymupdf4llm

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
OUTPUT_DIR = os.path.join(BASE_DIR, "analysis", "Liquity", "converted_docs")
RESOURCES_DIR = os.path.join(BASE_DIR, "resources", "Liquity")

# PDFs to convert
pdfs = [
    "ChainSecurity_Liquity_Bold_audit.pdf",
    "Liquity v2 - Whitepaper rev. 0.3 (November, 2024) (1).pdf",
    "Liquity V2 (BOLD)_ Overcollateralized Stablecoin Architecture (1).pdf",
    "Liquity V2 Mechanism Desgin Review.pdf"
]

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Run conversion
for pdf in pdfs:
    input_path = os.path.join(RESOURCES_DIR, pdf)
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        continue

    print(f"Converting {pdf}...")
    try:
        md_text = pymupdf4llm.to_markdown(input_path)
        
        output_filename = os.path.splitext(pdf)[0] + ".md"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_text)
            
        print(f"Successfully converted {pdf} to {output_path}")
    except Exception as e:
        print(f"Error converting {pdf}: {e}")
