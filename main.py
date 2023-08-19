from models import Author, Quote
import connect


def search_by_name(author_name):
    author = Author.objects(fullname=author_name).first()
    if author:
        quotes = Quote.objects(author=author)
        for quote in quotes:
            print(quote.quote)
    else:
        print(f"Автор {author_name} не знайдений")

search_by_name("Steve Martin")



# if __name__ == "__main__":
#     while True:
#         user_input = input("Надайте команду та аргументи: ")
#         if user_input is None:
#             continue
#         command, *args = user_input.split(':')
#         print(f'command:{command}')
#         print(f'args: {args}')
#         if command == 'exit':
#             break

#         if command == 'name':
#             search_from_db()
#         elif command == 'tag':
#             pass
#         elif command == 'tags':
#             pass
        

