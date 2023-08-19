from mongoengine import Document
from mongoengine.fields import StringField, ListField, ReferenceField
from bson import ObjectId


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField()
    author = ReferenceField(Author)
    quote = StringField()