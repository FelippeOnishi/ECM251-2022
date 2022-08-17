from datetime import date
from turtle import title


class Document:
    def __init__(self, authors = [], date = date.today()) -> None:
        self._authors = authors
        self._date = date
    def __str__(self) -> str:
        return f'Document: Authors:{self._authors} Date:{self._date}'
    def get_authors(self):
        return self._authors
    def get_date(self):
        return self._date
    def add_author(self,author):
        self._authors.append(author)

# Classe EMail herda Document
class EMail(Document):
    def __init__(self,to ,subject = "No Subject", authors=[], date=date.today()) -> None:
        super().__init__(authors, date)
        self._subject = subject
        self._to = to
    def get_subject(self):
        return self._subject
    def get_to(self):
        return self._to

    def __str__(self) -> str:
        return f"Email: to: {self._to} subjetct: {self._subject} authors: {super().get_authors()} date:{super().get_date()}"

# Classe book herda Document
class Book(Document):
    def __init__(self,title, authors=[], date=date.today()) -> None:
        super().__init__(authors, date)
        self._title = title
    def get_title(self):
        return self._title

    def __str__(self) -> str:
        return f'Book: Title: {self._title} - {super().__str__()}'