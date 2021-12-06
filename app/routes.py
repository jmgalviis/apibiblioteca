from flask import Blueprint
from .responses import response, bad_request, not_found
from .decorator import set_book, search_book
from .schemas import book_schema

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')


@api_v1.route('/books/', methods=['GET'])
def get_books():
    return not_found()


@api_v1.route('/book/<title>/', methods=['GET'])
@set_book
def get_book(book):
    return response(book)


@api_v1.route('/book/<int:id>/', methods=['DELETE'])
@search_book
def delete_book(book):
    if book.delete():
        return response(book_schema.dump(book))

    return bad_request()
