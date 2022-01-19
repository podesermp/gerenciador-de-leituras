import library.book.bookDB as bookDB

def forwarding(message):
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
    return result