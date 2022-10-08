import pandas as pd
from docx import Document
import subprocess

from models import QuoteModel
extensions = {
    "TEXT": ".txt",
    "CSV": ".csv",
    "PDF": ".pdf",
    "DOCX": ".docx",
}


class IngestorInterface:
    @classmethod
    def verify(cls, file_extension):
        return file_extension in extensions.values()

    @classmethod
    def parse(cls, path):
        pass
class PDFIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        text_file = './pdftotext.txt'
        cmd = f"./pdftotext -layout -nopgbrk {path} {text_file}"
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        quotes = TextIngestor.parse(text_file)
        os.remove(text_file)
        return quotes


class TextIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        file = open(path, "r", encoding="utf-8-sig")
        lines = file.readlines()
        file.close()
        return [QuoteModel(*quote.rstrip("\n").split(" - ")) for quote in lines]


class DocxIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        document = Document(path)
        quotes = []
        for paragraph in document.paragraphs:
            paragraph.text and quotes.append(
                QuoteModel(*paragraph.text.split(" - ")))
        return quotes

class CSVIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        csv = pd.read_csv(path)
        return [QuoteModel(**row) for index, row in csv.iterrows()]
