"""This module creates QuoteModel objects from quotes with a body and author."""


class QuoteModel:
    """A class definition to instantiate Quote objects."""

    def __init__(self, body: str, author: str) -> None:
        """Initialize a Quote object with the Quote's body and author.

        Arguments:
            body (str): The body of the Quote
            author (str): The author of the Quote
        """
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """Returns:
            str: string representation of the object
        """
        return f"{self.body} - {self.author}"
