#!/usr/bin/env python3
"""
Extract text from a PDF file and save it to a text file.
Usage: uv run extract_pdf_text.py <input_pdf> <output_txt>
"""

import sys
from pathlib import Path
from pypdf import PdfReader


def extract_pdf_text(pdf_path: str, output_path: str) -> None:
    """
    Extract all text from a PDF and save to a text file.
    
    Args:
        pdf_path: Path to the input PDF file
        output_path: Path to the output text file
    """
    print(f"Reading PDF: {pdf_path}")
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}")
    
    # Extract text from all pages
    full_text = []
    for page_num, page in enumerate(reader.pages, 1):
        if page_num % 100 == 0:  # Progress update every 100 pages
            print(f"Processing page {page_num}/{total_pages}")
        
        text = page.extract_text()
        full_text.append(f"--- PAGE {page_num} ---\n\n{text}")
    
    # Save to text file
    print(f"\nSaving to: {output_path}")
    output_file = Path(output_path)
    output_file.write_text(
        "\n\n".join(full_text),
        encoding="utf-8"
    )
    
    file_size_mb = output_file.stat().st_size / (1024 * 1024)
    print(f"Done! Extracted {total_pages} pages")
    print(f"Output file size: {file_size_mb:.2f} MB")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: uv run extract_pdf_text.py <input_pdf> <output_txt>")
        print("Example: uv run extract_pdf_text.py DaVinci_Resolve_20_Reference_Manual.pdf manual.txt")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    output_txt = sys.argv[2]
    
    if not Path(input_pdf).exists():
        print(f"Error: PDF file not found: {input_pdf}")
        sys.exit(1)
    
    extract_pdf_text(input_pdf, output_txt)
