import os
from PyPDF2 import PdfReader
import textract


class FileConverter:
    SUPPORTED_FORMATS = (".pdf", ".txt", ".docx")

    def __init__(self):
        pass

    def convert_to_text(self, file_path):
        file_extension = os.path.splitext(file_path)[1]
        if file_extension == ".pdf":
            return self._convert_pdf_to_text(file_path)
        elif file_extension == ".txt":
            return self._convert_txt_to_text(file_path)
        elif file_extension == ".docx":
            return self._convert_docx_to_text(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")

    def detect_file_type(self, file_path):
        file_extension = os.path.splitext(file_path)[1]
        return file_extension

    def _convert_pdf_to_text(self, file_path):
        with open(file_path, "rb") as f:
            pdf_reader = PdfReader(f)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
            return text

    def _convert_txt_to_text(self, file_path):
        with open(file_path, "r") as f:
            return f.read()

    def _convert_docx_to_text(self, file_path):
        return textract.process(file_path).decode("utf-8")
