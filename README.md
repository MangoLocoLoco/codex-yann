# codex-yann

This repository contains utilities for converting PDF files to DOCX.

## Usage

Install dependencies (fitz/PyMuPDF, python-docx, Pillow, pytesseract, opencv-python) and run:

```bash
python pdf2docx.py --input example.pdf --output example.docx [--ocr] [--no-images] [--verbose]
```

The `--ocr` option enables text extraction from scanned pages using Tesseract. Images can be ignored with `--no-images`. Verbose output prints parsing information.
