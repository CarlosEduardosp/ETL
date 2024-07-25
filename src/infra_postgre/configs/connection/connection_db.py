import psycopg2
from psycopg2 import pool
from src.model.data_connection_db import data_connection_db


def conectar_db():

    connection = None

    try:

        # Criando um pool de conexões
        connection_pool = psycopg2.pool.SimpleConnectionPool(1, 10,
                                                             user=data_connection_db.user,
                                                             password=data_connection_db.password,
                                                             host=data_connection_db.host,
                                                             port=data_connection_db.port,
                                                             database=data_connection_db.database)

        connection = connection_pool.getconn()

        # retorna uma variável com a conexão
        return {"connection": connection, "connection_pool": connection_pool}

    except psycopg2.Error as e:
        print(f"Erro ao conectar com o banco: {e}")

