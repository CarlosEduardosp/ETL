

def fechar_conexao_db(cursor: None, connection: None, connection_pool: None):

    # Fecha a conexão com o banco de dados
    if connection:
        cursor.close()
        connection_pool.putconn(connection)
        print("Conexão com banco encerrada.")
