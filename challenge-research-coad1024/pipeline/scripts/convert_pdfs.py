"""
Convert PDFs using marker CLI directly - more stable than Python API on Windows.
"""
import subprocess
from pathlib import Path

# Setup paths
pdf_dir = Path("resources/pdfs")
output_dir = Path("resources/pdfs/converted_marker")
output_dir.mkdir(exist_ok=True, parents=True)

# Get all PDFs
pdf_files = sorted([f for f in pdf_dir.glob("*.pdf") if f.is_file()])
print(f"Found {len(pdf_files)} PDF files to convert\n")
print("="*60)
print("\nPDF files to convert:")
for i, pdf in enumerate(pdf_files, 1):
    print(f"  {i}. {pdf.name}")
print("\n" + "="*60)

# Convert each PDF using marker_single CLI
successful = 0
failed = 0

for i, pdf_file in enumerate(pdf_files, 1):
    print(f"\n[{i}/{len(pdf_files)}] Converting: {pdf_file.name}")
    print("-" * 60)
    
    try:
        # Run marker_single with output directory
        cmd = [
            "marker_single",
            str(pdf_file.absolute()),
            "--output_dir", str(output_dir.absolute())
        ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=600  # 10 minute timeout per PDF
        )
        
        # Check if output file exists
        output_file = output_dir / pdf_file.stem / f"{pdf_file.stem}.md"
        if output_file.exists():
            file_size = output_file.stat().st_size
            print(f"  ✓ Converted successfully")
            print(f"  ✓ Output: {output_file}")
            print(f"  ✓ Size: {file_size:,} bytes")
            successful += 1
        else:
            print(f"  ✗ Output file not found")
            if result.stderr:
                print(f"  ✗ Error: {result.stderr[:200]}")
            failed += 1
        
    except subprocess.TimeoutExpired:
        print(f"  ✗ Timeout (>10 minutes)")
        failed += 1
    except Exception as e:
        print(f"  ✗ Error: {str(e)[:150]}")
        failed += 1

print("\n" + "="*60)
print(f"\nConversion Summary:")
print(f"  ✓ Successful: {successful}/{len(pdf_files)}")
print(f"  ✗ Failed: {failed}/{len(pdf_files)}")
print(f"\nOutput directory: {output_dir.absolute()}")

if successful > 0:
    print(f"\n✅ {successful} PDF(s) successfully converted!")
