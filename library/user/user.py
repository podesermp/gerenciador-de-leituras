from datetime import datetime

def userShowMessage(message: dict):
    if message['service'] == 1:
        print('\n------------*---------------')
        print(message['message'])
    elif message['service'] == 2:
        print('\n------------*---------------')
        print(message['message'])
    elif message['service'] == 3:
        if len(message['result']) == 0:
            print('Você não tem livros em sua lista')
        else:
            for infoBook in message['result']:
                print(f"-> {infoBook[1].upper()} do(a) {infoBook[2].upper()} iniciado em {infoBook[3][:2]}/{infoBook[3][2:4]}/{infoBook[3][4:]}")
        
def userAddReading() -> dict:
    message = {}
    message['title'] = input('Título: ')
    message['author'] = input('Autor: ')
    message['pages'] = input('Total de páginas: ')
    message['checkinBook'] = datetime.today().strftime('%d-%m-%Y').replace('-', '') # para obter a data atual
    message['checkoutBook'] = ""
    message['rating'] = ""

    return message

def userLeaveReading() -> str:
    title = input('Título: ')
    return title

def userDefineSevice() -> dict:

    answer = {}

    print('[1] - Adicionar nova leitura')
    print('[2] - abandonar leitura')
    print('[3] - ver lista de leitura')

    service = input('Insira o número do serviço: ')
    service = int(service)
    if service == 1:
        print('\n------------*---------------')
        print('[1] - Adicionar nova leitura')
        answer['objeto'] = userAddReading()
    elif service == 2:
        print('\n------------*---------------')
        print('[2] - abandonar leitura')
        answer['title'] = userLeaveReading()
    elif service == 3:
        print('\n------------*---------------')
        print('[3] - ver lista de leitura')
    else:
        print('Opção inválida!')
        service = 0
    answer['service'] = service
    return answer