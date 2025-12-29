# PDF Conversion Status & Next Steps

## Current Status (2025-11-24)

### Completed

- ✅ 9/12 PDFs converted using `pymupdf4llm`
- ✅ DeepSeek-OCR cloned to `pipeline/tools/DeepSeek-OCR/`

### Converted PDFs (Basic Quality)

1. (In)Stability for the Blockchain.md
2. Collateral Portfolio Optimization in Crypto Backed Stablecoins.md
3. DeFi risk assessment MakerDAO loan portfolio case.md
4. Designing Stablecoins.md
5. KlagesMundt_cornellgrad_0058F_13656.md
6. Liquity V2 Mechanism Desgin Review.md
7. Loan_Portfolio_Dataset_From_MakerDAO_Blockchain_Project.md
8. Monetary Stabilization in Cryptocurrencies.md
9. SOK_Blockchain governance.md
10. Stablecoin2.0.md (via pymupdf4llm)
11. What is Stablecoin.md (via pymupdf4llm)
12. While Stability Lasts.md (via pymupdf4llm)

### Failed / Remaining PDFs

- Kjaeer Martin - 2021 - Quantitative Analysis of MakerDAOs Liquidation System.pdf (Failed: Timeout/Stuck)

## Issue: Low Quality Conversion

**Problem:** `pymupdf4llm` produces poor quality for academic PDFs:

- Math equations not properly converted
- Tables misformatted
- Images not extracted/described

## Solution: Deep-Seek OCR

### Requirements

- CUDA 11.8+
- PyTorch 2.6.0
- GPU (A100 recommended for 2500 tokens/s)
- Flash Attention 2.7.3
- vLLM 0.8.5

### Installation Commands

```bash
conda create -n deepseek-ocr python=3.12.9 -y
conda activate deepseek-ocr
pip install torch==2.6.0 torchvision==0.21.0 --index-url https://download.pytorch.org/whl/cu118
# Download vllm-0.8.5 wheel from GitHub releases
pip install -r pipeline/tools/DeepSeek-OCR/requirements.txt
pip install flash-attn==2.7.3 --no-build-isolation
```

### Usage for PDF

```python
cd pipeline/tools/DeepSeek-OCR/DeepSeek-OCR-master/DeepSeek-OCR-vllm
# Configure INPUT_PATH/OUTPUT_PATH in config.py
python run_dpsk_ocr_pdf.py
```

### Alternative: Transformers Interface

```python
from transformers import AutoModel, AutoTokenizer
model = AutoModel.from_pretrained('deepseek-ai/DeepSeek-OCR', 
                                   _attn_implementation='flash_attention_2',
                                   trust_remote_code=True)
res = model.infer(tokenizer, 
                  prompt="<image>\\n<|grounding|>Convert the document to markdown.",
                  image_file='your.pdf',
                  output_path='output/')
```

## Recommended Action

**Option 1:** Use existing low-quality conversions for now, manually extract key math/tables when needed
**Option 2:** Set up GPU environment and run DeepSeek-OCR for high-quality conversion
**Option 3:** Use online OCR services (e.g., Mathpix) for the 3 remaining critical PDFs

## Notes

- DeepSeek-OCR paper: `pipeline/tools/DeepSeek-OCR/DeepSeek_OCR_paper.pdf`
- Current pymupdf4llm script: `pipeline/scripts/convert_pdfs.py`
- Converted output: `resources/pdfs/converted/`
