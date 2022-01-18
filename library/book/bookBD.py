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

    conn = psycopg2.connect(conn_string)
    print('conectado')

    #com o cursor consigo executar SQL
    cursor = conn.cursor()

    # criar tabelas
    cursor.execute("CREATE TABLE reading_list(id serial PRIMARY KEY, title VARCHAR(50) NOT NULL, author VARCHAR(50) NOT NULL, checkinBook VARCHAR(50) NOT NULL, checkoutBook VARCHAR(50), pages INTEGER NOT NULL, rating INTEGER);")
    cursor.execute("CREATE TABLE wishlist (id serial PRIMARY KEY, title VARCHAR(50), author VARCHAR(50), pages INTEGER);")

    print("tabela 'reading_list' e 'wishlist' criadas")

    #para commitar a alteração
    conn.commit()
    cursor.close()
    conn.close()

# adiciona um livro na lista de leitura
# essa função corresponde a addNewReading(book:Book, list: int): boolean
def addBook(title, author, pages, checkinBook, conn_string=conn_string):
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO reading_list (title, author, pages, checkinBook) VALUES ('{title.lower()}', '{author.lower()}', {pages}, {checkinBook})")
    print(f"item '{title}' adicionado a lista de leitura")

    conn.commit()
    cursor.close()
    conn.close()
    return True
    
def leaveReading(title, conn_string=conn_string):
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    cursor.execute(f"delete from reading_list where title = '{title.lower()}';")

    print(f"'{title}' deletado")

    conn.commit()
    cursor.close()
    conn.close()

    return True

# title = input('Title (del): ')
# leaveReading(title=title, conn_string=conn_string)