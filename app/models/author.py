from . import db


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Author({self.name})'
