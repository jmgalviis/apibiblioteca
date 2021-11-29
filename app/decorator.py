from .ext.googleBook import search
from .resourses import store
from .models.book import Book
from .schemas import book_schema
from .responses import not_found


def set_book(function):
    def wrap(*args, **kwargs):
        title = kwargs.get('title', 0)

        book = Book.simple_filter(title)

        if book is None:
            book = search(title)
            store(book)

        book = book_schema.dump(book)

        return function(book)

    wrap.__name__ = function.__name__
    return wrap


def search_book(function):
    def wrap(*args, **kwargs):
        id = kwargs.get('id', 0)
        book = Book.query.filter_by(id=id).first()
        if book is None:
            return not_found()

        return function(book)

    wrap.__name__ = function.__name__
    return wrap
