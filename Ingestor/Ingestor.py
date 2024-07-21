from typing import List

from .IngestorInterface import IngestorInterface
from QuoteEngine import QuoteModel


class Ingestor(IngestorInterface):
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        subclass = set(cls.__base__.__subclasses__())
        for cl in subclass:
            if ext in cl.allowed_extensions:
                return True
        return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        ext = path.split('.')[-1]
        subclass = set(cls.__base__.__subclasses__())
        for cl in subclass:
            if ext in cl.allowed_extensions:
                return cl.parse(path)
        return None
