import fitz
from pathlib import Path


class PDFService:

    @staticmethod
    def extract_text(file_path: str) -> str:
        """
        Extract all text from a PDF.
        """

        pdf = fitz.open(file_path)

        pages = []

        for page in pdf:
            text = page.get_text("text")

            if text:
                pages.append(text)

        pdf.close()

        return "\n".join(pages)