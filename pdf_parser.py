import fitz
from PIL import Image
import pytesseract
from io import BytesIO


def parse_pdf(path, ocr=False, no_images=False, verbose=False):
    """Parse PDF and return list of pages with text and image data."""
    doc = fitz.open(path)
    pages = []
    for page_index in range(len(doc)):
        page = doc[page_index]
        items = []
        # Extract text blocks and images using PyMuPDF
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if block["type"] == 0:  # text
                text = block.get("text", "").strip()
                if text:
                    items.append({"type": "text", "text": text})
            elif block["type"] == 1 and not no_images:
                xref = block.get("xref")
                if xref:
                    base_image = doc.extract_image(xref)
                    if base_image:
                        image_bytes = base_image.get("image")
                        items.append({"type": "image", "data": image_bytes})
        # If no text detected and OCR is requested, run Tesseract
        if ocr and not any(i["type"] == "text" for i in items):
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            ocr_text = pytesseract.image_to_string(img)
            if ocr_text.strip():
                items.append({"type": "text", "text": ocr_text})
        if verbose:
            print(f"Parsed page {page_index + 1} with {len(items)} items")
        pages.append(items)
    return pages
