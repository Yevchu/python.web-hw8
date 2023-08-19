from models import Author, Quote
import json
import connect


with open('./json/authors.json', 'r') as f:
    authors_list = json.load(f)
    for author in authors_list:
        author_to_db = Author(
            fullname=author.get('fullname'), 
            born_date=author.get('born_date'),
            born_location=author.get('born_location'),
            description=author.get('description')
        ).save()

with open('./json/qoutes.json', 'r') as f:
    quotes_list = json.load(f)
    for quote in quotes_list:
        quote_to_db = Quote(
            tags=quote.get('tags'),
            author=quote.get('author'),
            quote=quote.get('quote')
        ).save()