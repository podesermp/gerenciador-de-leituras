from datetime import datetime
import client.proxy as proxy

# mostra a mensagem para o usuário de acordo com o serviço que foi solicitado ao servidor
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
                # um print diferente caso o livro ja tenha sido finalizado
                if infoBook[4] == None:
                    print('------------------------------------------------------------------------------')
                    print(f"|-> {infoBook[1].upper()} do(a) {infoBook[2].upper()} iniciado em {infoBook[3][:2]}/{infoBook[3][2:4]}/{infoBook[3][4:]}|")
                    # print('--------------------------------------------------')
                else:
                    print('------------------------------------------------------------------------------')
                    print(f"|-> {infoBook[1].upper()} do(a) {infoBook[2].upper()} iniciado em {infoBook[3][:2]}/{infoBook[3][2:4]}/{infoBook[3][4:]} e terminado em {infoBook[4][:2]}/{infoBook[4][2:4]}/{infoBook[4][4:]} foi avaliado em {infoBook[6]}/5|")
    elif message['service'] == 4:
        print('\n------------*---------------')
        print(message['message'])
    else:
        print('\n------------*---------------')
        print(message['message'])

# menu de serviços
def userDefineService():
    result = {}

    print('[1] - Adicionar nova leitura')
    print('[2] - Abandonar leitura')
    print('[3] - Ver lista de leitura')
    print('[4] - Finalizar livro')

    service = input('\nInsira o número do serviço: ')
    service = int(service)
    if service == 1:
        print('\n------------*---------------')
        print('[1] - Adicionar nova leitura\n')
        title = input("Título: ")
        author = input("Autor: ")
        pages = input("Total de páginas: ")
        checkinBook = datetime.today().strftime('%d-%m-%Y').replace('-', '') # para obter a data atual
        checkoutBook = ""
        rating = ""
        result = proxy.addBook(
            title=title, 
            author=author, 
            pages=pages, 
            checkinBook=checkinBook,
            checkoutBook=checkoutBook,
            rating=rating
        )
        return result
    elif service == 2:
        print('\n------------*---------------')
        print('[2] - Abandonar leitura\n')
        title = input('Título: ')
        result = proxy.leaveReading(title=title)
        return result
    elif service == 3:
        print('\n------------*---------------')
        print('[3] - Ver lista de leitura\n')
        result['service'] = 3
        return result
    elif service == 4:
        print('\n------------*---------------')
        print('[4] - Finalizar livro\n')
        title = input('Título: ')
        rating = int(input('Avaliação do livro (0-5): '))
        checkoutBook = datetime.today().strftime('%d-%m-%Y').replace('-', '') # para obter a data atual
        result = proxy.finishReading(
            rating=rating, 
            title=title, 
            checkoutbook=checkoutBook
        )
        return result
    else:
        print('Opção inválida!\n')
        service = 0
    result['service'] = service
    return result