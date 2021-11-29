# from flask import request
from flask import jsonify


#from .schemas import book_schema, autor_schema, category_schema
from .models.book import Book
from .models.author import Author
from .models.category import Category


def store(req):
    data = req

    book = Book(
        title=data.get('title'),
        subtitle=data.get('subtitle'),
        published_date=data.get('published_date'),
        publisher=data.get('publisher'),
        description=data.get('description'),
        image=data.get('image')
    )
    for author in data.get('authors'):
        book.authors.append(Author(author))
    for category in data.get('categories'):
        book.categories.append(Category(category))

    book.save()
