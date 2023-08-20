from models import Author, Quote
import connect


def search_by_name(author_name):
    quote_list = []
    author = Author.objects(fullname=author_name).first()
    if author:
        quotes = Quote.objects(author=author)
        for quote in quotes:
            quote_list.append(quote.quote)
    else:
        print(f"Автор {author_name} не знайдений.")
    return quote_list


def search_by_tag(tag):
    res = []
    tegs_quotes = Quote.objects(tags=tag).all()
    for el in tegs_quotes:
        res.append(el.quote)
    return res

def search_by_tags(args):
    tag1, tag2 = args.split(',')
    res = []
    tegs_quotes = Quote.objects(tags__in=[tag1, tag2]).all()
    for el in tegs_quotes:
        res.append(el.quote)
    return res


if __name__ == "__main__":
    while True:
        user_input = input("Надайте команду та аргументи: ")
        if not user_input:
            continue
        command, *args = user_input.strip().split(': ', 1)
        
        if command == 'exit':
            break

        if command == 'name':
            res = search_by_name(*args)
        elif command == 'tag':
            res = search_by_tag(*args)
        elif command == 'tags':
            res = search_by_tags(*args)
        print(res)
        

