from datetime import datetime
from multiprocessing.connection import answer_challenge

def userDefineSevice():

    answer = {}

    print('[1] - Adicionar nova leitura')
    print('[2] - abandonar leitura')

    service = input('Insira o número do serviço: ')
    service = int(service)
    if service == 1:
        print('\n[1] - Adicionar nova leitura')
        answer['objeto'] = userAddReading()
    elif service == 2:
        print('\n[2] - abandonar leitura')
        answer['title'] = userLeaveReading()
    else:
        print('Opção inválida!')
        service = 0
    answer['service'] = service
    return answer

def userAddReading():
    message = {}
    message['title'] = input('Title: ')
    message['author'] = input('Author: ')
    message['pages'] = input('Pages: ')
    message['checkinBook'] = datetime.today().strftime('%d-%m-%Y').replace('-', '') # para obter a data atual
    message['checkoutBook'] = ""
    message['rating'] = ""

    return message

def userLeaveReading():
    title = input('Title: ')
    return title