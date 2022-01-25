
def addBook(title:str, author:str, pages:int, checkinBook:str, checkoutBook:str, rating:str) -> dict:
    result = {
        'objeto': {}
    }
    result['objeto']['title'] = title
    result['objeto']['author'] = author
    result['objeto']['pages'] = pages
    result['objeto']['checkinBook'] = checkinBook

    result['service'] = 1
    return result

def leaveReading(title:str):
    result = {}
    result['title'] = title
    result['service'] = 2
    return result

def finishReading(rating:int, title:str, checkoutbook:str):
    result = {
        'objeto': {}
    }
    result['objeto']['title'] = title
    result['objeto']['rating'] = rating
    result['objeto']['checkoutBook'] = checkoutbook

    result['service'] = 4
    return result