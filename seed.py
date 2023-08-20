from models import Author, Quote
import json
import connect


with open('./json/authors.json', 'r') as f:
    authors_list = json.load(f)
    for author in authors_list:
        author_to_db = Author(**author).save()

with open('./json/qoutes.json', 'r') as f:
    quotes_list = json.load(f)
    for quote in quotes_list:
        quote['author'] = Author.objects(fullname=quote['author']).first()
        quote_to_db = Quote(**quote).save()