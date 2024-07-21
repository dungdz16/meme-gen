from typing import List
import docx

from .IngestorInterface import IngestorInterface
from QuoteEngine import QuoteModel


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parsing Docx files that contains quotes.
        This method using docx library to parse docx files.
        @param cls: pointer to this class.
        @param path: Input path for docx file.
        """
        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
