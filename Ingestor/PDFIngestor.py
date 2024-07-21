from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from QuoteEngine import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parsing pdf files that contains quotes.
        This method using pdftotext library to parse pdf files.
        Text file generated from pdf file will be cached in /tmp folder.
        Then it will be removed after finishing the process.
        @param cls: pointer to this class.
        @param path: Input path for pdf file.
        """
        tmp = f'/tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split('-')
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
