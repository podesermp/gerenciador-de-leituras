import json
from scr.library.book.book import Book

book = Book(title='Algoritmos de destruição em massa',checkinBook='21-07-2005',pages=200, author='Marcos')

# json_book = book.to_dict()

message = book.to_dict()

def serializar(data):
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)

serializar(message)
print('serializado!')

def deserialization():
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
    return data

dataa = deserialization()
# dataa = json.dumps(dataa)
print(dataa['title'])