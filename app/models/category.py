from . import db


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Category({self.name})'
