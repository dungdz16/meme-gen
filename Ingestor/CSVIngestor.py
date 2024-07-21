from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from QuoteEngine import QuoteModel


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parsing CSV files that contains quotes.
        This method using pandas library to parse CSV files.
        @param cls: pointer to this class.
        @param path: Input path for csv file.
        """
        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)
        return quotes
