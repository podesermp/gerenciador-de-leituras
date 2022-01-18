conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    titles = []
    cursor.execute(f"SELECT title FROM wishlist;")
    for t in cursor:
        titles.append(t[0])
    
    if title in titles:
        cmd = f"delete from wishlist where title = '{title}';"
        print(cmd)
        cursor.execute(cmd)
        print(f"{title} deletado")
        return True
    else:
        print(f"{title} não encontrado")
        conn.commit()
        cursor.close()
        conn.close()
        return False