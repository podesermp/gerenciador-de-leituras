import server.bookDB as bookDB

def addBook(objeto:dict)->dict:    
    result = bookDB.addBook(
        title=objeto['title'],
        author=objeto['author'], 
        pages=objeto['pages'], 
        checkinBook=objeto['checkinBook']
    )
    return result

def leaveReading(objeto:dict) -> dict:
    result = bookDB.leaveReading(title=objeto['title'])
    return result

def seeList() -> dict:
    result = bookDB.seeList()
    return result

def finishReading(objeto:dict)->dict:
    result = bookDB.finishReading(
                title=objeto['title'],
                rating=objeto['rating'],
                checkoutbook=objeto['checkoutBook']
            )
    return result