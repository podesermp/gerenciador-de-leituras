from datetime import datetime

# mostra a mensagem para o usuário de acordo com o serviço que
# foi solicitado ao servidor
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
# interage com o usuário para coletar as informações necessárias
# para adicionar um livro na lista de leituras

def userAddReading() -> dict:
    message = {}
    message['title'] = input("Título: ")
    message['author'] = input("Autor: ")
    message['pages'] = input("Total de páginas: ")
    message['checkinBook'] = datetime.today().strftime('%d-%m-%Y').replace('-', '') # para obter a data atual
    message['checkoutBook'] = ""
    message['rating'] = ""

    return message

# interage com o usuário para coletar as informações necessárias
# para abandonar um livro da lista de leituras (abandonar leitura)
def userLeaveReading() -> str:
    title = input('Título: ')
    return title

def userFinishReading() -> dict:
    message = {}
    message['title'] = input('Título: ')
    message['rating'] = int(input('Avaliação do livro (0-5): '))
    message['checkoutBook'] = datetime.today().strftime('%d-%m-%Y').replace('-', '') # para obter a data atual
    return message

# menu de serviços
def userDefineService() -> dict:
    answer = {}

    print('[1] - Adicionar nova leitura')
    print('[2] - Abandonar leitura')
    print('[3] - Ver lista de leitura')
    print('[4] - Finalizar livro')

    service = input('\nInsira o número do serviço: ')
    service = int(service)
    if service == 1:
        print('\n------------*---------------')
        print('[1] - Adicionar nova leitura\n')
        answer['objeto'] = userAddReading()
    elif service == 2:
        print('\n------------*---------------')
        print('[2] - Abandonar leitura\n')
        answer['title'] = userLeaveReading()
    elif service == 3:
        print('\n------------*---------------')
        print('[3] - Ver lista de leitura\n')
    elif service == 4:
        print('\n------------*---------------')
        print('[4] - Finalizar livro\n')
        answer['objeto'] = userFinishReading()
    else:
        print('Opção inválida!\n')
        service = 0
    answer['service'] = service
    return answer