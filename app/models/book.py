from . import db


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    subtitle = db.Column(db.String)
    authors = db.relationship('Author', backref='book', lazy=False, cascade='all, delete-orphan')
    categories = db.relationship('Category', backref='book', lazy=False, cascade='all, delete-orphan')
    published_date = db.Column(db.String, nullable=False)
    publisher = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.String)
    source = db.Column(db.String, default='Interna')
    created_at = db.Column(db.DateTime(), default=db.func.current_timestamp())

    def __init__(self, title, subtitle, published_date, publisher, description, image):
        self.title = title
        self.subtitle = subtitle
        self.published_date = published_date
        self.publisher = publisher
        self.description = description
        self.image = image

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

    @classmethod
    def simple_filter(cls, title):
        search = f'%{title}%'
        return cls.query.filter(Book.title.ilike(search)).first()
