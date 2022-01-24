import library.book.bookDB as bookDB

def forwarding(message) -> dict:
    result = {}
    try:
        if message['service'] == 1:
            result = bookDB.addBook(
                    title=message['objeto']['title'],
                    author=message['objeto']['author'],
                    pages=message['objeto']['pages'],
                    checkinBook=message['objeto']['checkinBook']
                )
        elif message['service'] == 2:
            result = bookDB.leaveReading(
                    title=message['title']
                )
        elif message['service'] == 3:
            result = bookDB.seeList()

        elif message['service'] == 4:
            result = bookDB.finishReading(
                title=message['objeto']['title'],
                rating=message['objeto']['rating'],
                checkoutbook=message['objeto']['checkoutBook']
            )
        return result
    except Exception as erro:
        result['message'] = erro
        print(f"erro: {erro}")
        return result

