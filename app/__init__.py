from flask import Flask
from .models import db
from .models.book import Book
from .models.author import Author
from .models.category import Category
from .routes import api_v1


def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    app.register_blueprint(api_v1)

    app.url_map.strict_slashes = False

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
