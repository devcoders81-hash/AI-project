import re


class TextCleaner:

    @staticmethod
    def clean(text: str) -> str:
        if not text:
            return ""

        # Normalize line endings
        text = text.replace("\r\n", "\n")

        # Remove tabs
        text = text.replace("\t", " ")

        # Remove multiple spaces
        text = re.sub(r" +", " ", text)

        # Remove multiple blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove page numbers like "Page 1"
        text = re.sub(r"Page\s+\d+", "", text, flags=re.IGNORECASE)

        # Remove trailing spaces
        text = "\n".join(line.strip() for line in text.splitlines())

        return text.strip()