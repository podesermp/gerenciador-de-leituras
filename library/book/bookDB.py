import psycopg2

#config
host = 'localhost'
dbname = 'postgres'
user = 'postgres'
password = 'postgres'
sslmode = 'require'

#string de conexão
conn_string = 'host={0} user={1} dbname={2} password={3} sslmode={4}'.format(host, user, dbname, password, sslmode)

# conecta o banco e cria a tabela
def connectBD(conn_string=conn_string):
    try:
        conn = psycopg2.connect(conn_string)

        #com o cursor consigo executar SQL
        cursor = conn.cursor()

        # criar tabelas
        cursor.execute("CREATE TABLE IF NOT EXISTS reading_list(id serial PRIMARY KEY, title VARCHAR(50) NOT NULL, author VARCHAR(50) NOT NULL, checkinBook VARCHAR(50) NOT NULL, checkoutBook VARCHAR(50), pages INTEGER NOT NULL, rating INTEGER);")

        print("tabela 'reading_list' criadas")

        #para commitar a alteração
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as erro:
        print(f"ERRO: {erro}")

# adiciona um livro na lista de leitura
def addBook(title:str, author:str, pages:int, checkinBook:str, conn_string=conn_string) -> dict:
    
    result  = {}
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        
        cursor.execute(f"INSERT INTO reading_list (title, author, pages, checkinBook) VALUES ('{title.lower()}', '{author.lower()}', {pages}, {checkinBook})")
        print(f"Livro '{title}' adicionado a lista de leitura")
        result['result'] = True
        result['message'] = f"Livro '{title}' adicionado a lista de leitura"
        conn.commit()
        cursor.close()
        conn.close()
    except:
        result['result'] = False
        result['message'] = f"Livro '{title}' não pode ser adicionado a lista de leitura"
    
    result['service'] = 1
    return result
    
# abandonar leitura consiste em simplesmente apagar o livro da lista
# uma leitura é abandonada quando não se quer mais ler aquele livro
def leaveReading(title:str, conn_string=conn_string) -> dict:
    
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    result  = {}
    titles = []
    cursor.execute(f"SELECT title FROM reading_list;")
    for t in cursor:
        titles.append(t[0])

    if title.lower() in titles:
        cursor.execute(f"delete from reading_list where title = '{title.lower()}';")
        print(f"Livro '{title}' abandonado")
        conn.commit()
        cursor.close()
        conn.close()
        result['result'] = True
        result['message'] = f"Livro '{title}' abandonado"
        result['service'] = 2
        return result
    else:
        print(f"Livro '{title}' não encontrado")
        result['message'] = f"Livro '{title}' não encontrado"
    conn.commit()
    cursor.close()
    conn.close()
    result['result'] = False
    result['service'] = 2
    return result

# visualizar a os livros e suas situações na lista de leitura
def seeList(conn_string=conn_string):
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    print('Visualizar lista de leituras')
    banco = []
    cursor.execute(f"SELECT * FROM reading_list;")
    for t in cursor:
        banco.append(t)
    result = {
        "result": banco,
        "service": 3
    }
    cursor.close()
    conn.close()
    return result

# finaliza um livro que esta na lista de leituras
def finishReading(rating:int, title:str, checkoutbook:str, conn_string=conn_string) -> dict:
    
    id = -1
    result = {}
    titles = []
    if rating >= 0 and rating <=5:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM reading_list;")
        for t in cursor:
            titles.append(t)
        for book in titles:
            # print(book)
            if book[1] == title.lower():
                id = book[0]
        if id < 0:
            result['message'] = f"Livro '{title}' não encontrado"
            result['result'] = False
            result['service'] = 4
            cursor.close()
            conn.close()
            return result
        cursor.execute(f"UPDATE reading_list SET rating = {rating}, checkoutbook = {checkoutbook} WHERE id = {id};")
        result['message'] = f"Livro '{title}' finalizado com sucesso"
        result['result'] = True
        result['service'] = 4
        print(f"Leitura do livro '{title}' finalizada")
        conn.commit()
        cursor.close()
        conn.close()
        return result
    else:
        result['message'] = f"rating precisa ser de 0 a 5"
        result['result'] = False
        result['service'] = 4
        return result

connectBD()