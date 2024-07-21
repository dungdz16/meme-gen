class QuoteModel:
    def __init__(self, body: str, author: str):
        """
        Initialize QuoteModel object.

        @param self: The object pointer.
        @param body: Body text of this quote.
        @param author: Author of this quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Represent string format of QuoteModel object."""
        return f"{self.body} - {self.author}"
