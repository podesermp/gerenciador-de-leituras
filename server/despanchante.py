import server.bookDB as bookDB
import server.esqueleto as esqueleto

def invoke(message:dict) -> dict:
    result = {}
    try:
        if message['service'] == 1:
            result = esqueleto.addBook(message['objeto'])
        elif message['service'] == 2:
            result = esqueleto.leaveReading(message)
        elif message['service'] == 3:
            result = esqueleto.seeList()

        elif message['service'] == 4:
            result = esqueleto.finishReading(message['objeto'])
        return result
    except Exception as erro:
        result['message'] = erro
        print(f"erro: {erro}")
        return result

