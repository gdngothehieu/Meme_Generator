import os

from ingestors.Ingestor import IngestorInterface, extensions
from ingestors.Ingestor import TextIngestor
from ingestors.Ingestor import DocxIngestor
from ingestors.Ingestor import PDFIngestor
from ingestors.Ingestor import CSVIngestor


class Ingestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        filename, file_extension = os.path.splitext(path)
        if not cls.verify(file_extension):
            raise ValueError("Unsupported file extension:", file_extension)
        if file_extension == extensions.get("TEXT"):
            return TextIngestor.parse(path)
        if file_extension == extensions.get("DOCX"):
            return DocxIngestor.parse(path)
        if file_extension == extensions.get("PDF"):
            return PDFIngestor.parse(path)
        if file_extension == extensions.get("CSV"):
            return CSVIngestor.parse(path)
