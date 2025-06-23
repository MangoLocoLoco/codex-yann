import argparse

from pdf_parser import parse_pdf
from docx_builder import build_docx


def main():
    parser = argparse.ArgumentParser(description="Convert PDF files to DOCX")
    parser.add_argument("--input", required=True, help="Input PDF file")
    parser.add_argument("--output", required=True, help="Output DOCX file")
    parser.add_argument("--ocr", action="store_true", help="Use OCR on scanned pages")
    parser.add_argument("--no-images", action="store_true", help="Ignore images in output")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()

    pages = parse_pdf(args.input, ocr=args.ocr, no_images=args.no_images, verbose=args.verbose)
    build_docx(pages, args.output)


if __name__ == "__main__":
    main()
