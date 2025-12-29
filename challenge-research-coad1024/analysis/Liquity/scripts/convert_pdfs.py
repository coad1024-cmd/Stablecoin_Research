import os
import subprocess
import sys

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
MARKER_DIR = os.path.join(BASE_DIR, "pipeline", "tools", "marker")
OUTPUT_DIR = os.path.join(BASE_DIR, "analysis", "Liquity", "converted_docs")
RESOURCES_DIR = os.path.join(BASE_DIR, "resources", "Liquity")

# PDFs to convert
pdfs = [
    # "ChainSecurity_Liquity_Bold_audit.pdf",
    # "Liquity v2 - Whitepaper rev. 0.3 (November, 2024) (1).pdf",
    "Liquity V2 (BOLD)_ Overcollateralized Stablecoin Architecture (1).pdf",
    # "Liquity V2 Mechanism Desgin Review.pdf"
]

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Environment with PYTHONPATH
env = os.environ.copy()
env["PYTHONPATH"] = MARKER_DIR + os.pathsep + env.get("PYTHONPATH", "")

# Run conversion
for pdf in pdfs:
    input_path = os.path.join(RESOURCES_DIR, pdf)
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        continue

    print(f"Converting {pdf}...")
    cmd = [
        sys.executable,
        os.path.join(MARKER_DIR, "convert_single.py"),
        input_path,
        "--output_dir", OUTPUT_DIR,
        "--output_format", "markdown"
    ]
    
    try:
        result = subprocess.run(cmd, env=env, check=True, capture_output=True, text=True)
        print(f"Successfully converted {pdf}")
        # print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error converting {pdf}:")
        print(e.stderr)
