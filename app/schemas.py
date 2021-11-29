from marshmallow import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class BookSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    subtitle = fields.String()
    authors = fields.Nested('AuthorSchema', many=True)
    categories = fields.Nested('CategorySchema', many=True)
    published_date = fields.String()
    publisher = fields.String()
    description = fields.String()
    image = fields.String()
    source = fields.String()
    created_at = fields.DateTime()


class AuthorSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()


class CategorySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()


book_schema = BookSchema()
autor_schema = AuthorSchema()
category_schema = CategorySchema
