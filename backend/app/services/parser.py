import fitz  # PyMuPDF
from fastapi import UploadFile
import io
import traceback
from typing import List

def extract_text_by_page(file: UploadFile) -> List[str]:
    """
    Reads an uploaded PDF file and extracts text from each page.
    Tries multiple extraction modes for robustness.
    Returns a list of strings where each string is the text of a page.
    """
    page_texts = []
    try:
        file.file.seek(0)
        file_content = file.file.read()

        with fitz.open(stream=io.BytesIO(file_content), filetype="pdf") as pdf_document:
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)

                # Try default text mode
                text = page.get_text("text").strip()

                # If no text, try block mode
                if not text:
                    blocks = page.get_text("blocks")
                    text = " ".join([b[4] for b in blocks if len(b) > 4]).strip()

                # If still no text, try dict mode
                if not text:
                    dict_text = page.get_text("dict")
                    if "blocks" in dict_text:
                        text = " ".join(
                            [span["text"] for b in dict_text["blocks"] for line in b.get("lines", []) for span in line.get("spans", [])]
                        ).strip()

                # Final fallback
                if not text:
                    text = ""

                page_texts.append(text)

        return page_texts

    except Exception as e:
        print("--- PDF PARSING ERROR ---")
        traceback.print_exc()
        print("-------------------------")
        return [f"Error: Could not parse the provided file. Details: {e}"]
