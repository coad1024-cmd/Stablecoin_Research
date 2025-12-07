import os
import subprocess
import sys

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
MARKER_TOOL_DIR = os.path.join(BASE_DIR, "pipeline", "tools", "marker")
OUTPUT_DIR = os.path.join(BASE_DIR, "resources", "Liquity", "marker_converted")
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

# Environment with PYTHONPATH to include the local marker tool
env = os.environ.copy()
# Prepend the local marker directory to PYTHONPATH
env["PYTHONPATH"] = MARKER_TOOL_DIR + os.pathsep + env.get("PYTHONPATH", "")

# Run conversion
for pdf in pdfs:
    input_path = os.path.join(RESOURCES_DIR, pdf)
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        continue

    print(f"Converting {pdf}...")
    # Using convert_single.py from the local tool directory
    script_path = os.path.join(MARKER_TOOL_DIR, "convert_single.py")
    
    cmd = [
        sys.executable,
        script_path,
        input_path,
        "--output_dir", OUTPUT_DIR,
        "--output_format", "markdown",
        "--force_ocr" # Adding force_ocr might help if it's stuck on layout detection, or might make it slower. Let's stick to defaults first or maybe add it if needed. 
        # Actually, let's NOT force OCR to start with, to be faster.
    ]
    
    # Remove --force_ocr for now to speed up if possible, unless text extraction fails.
    cmd = [
        sys.executable,
        script_path,
        input_path,
        "--output_dir", OUTPUT_DIR,
        "--output_format", "markdown"
    ]

    print(f"Running command: {' '.join(cmd)}")
    
    try:
        # increasing timeout to 10 minutes per file as marker can be slow on CPU
        result = subprocess.run(cmd, env=env, check=True, capture_output=True, text=True, timeout=600)
        print(f"Successfully converted {pdf}")
        print(result.stdout)
    except subprocess.TimeoutExpired:
        print(f"Timeout converting {pdf}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {pdf}:")
        print(e.stderr)
        print(e.stdout)
