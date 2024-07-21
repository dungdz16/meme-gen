from typing import List
from .IngestorInterface import IngestorInterface
from QuoteEngine import QuoteModel


class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parsing TXT files that contains quotes.
        @param cls: pointer to this class.
        @param path: Input path for txt file.
        """
        file_ref = open(path, "r")
        quotes = []
        for line in file_ref.readlines():
            print(line)
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split('-')
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        file_ref.close()
        return quotes
