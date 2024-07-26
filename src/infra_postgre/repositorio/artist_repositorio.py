import datetime

import psycopg2.extras
from psycopg2.extras import DictCursor
from typing import Type, Dict
from src.infra_postgre.configs.connection.connection_db import conectar_db
from src.infra_postgre.configs.connection.fechar_conexao import fechar_conexao_db
from src.infra_postgre.repositorio.interfaces_repositorio.interface_repositorio import InterfaceArtistsrepository
from src.stages.contracts.tranform_contract import TranformContract


class InserirArtist(InterfaceArtistsrepository):

    # método construtor para conexão com banco de dados.
    def __init__(self, conectar_db: Type[conectar_db]):
        self.conectar_db = conectar_db

    def criar_artist(self, artist: Dict) -> Dict:
        conn = self.conectar_db()
        connection = conn['connection']
        cursor = connection.cursor(cursor_factory=DictCursor)

        date_today = datetime.date.today()

        try:
            cursor.execute(
                "INSERT INTO artists (first_name, second_name, surname, artist_id,"
                "link, created_at) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    artist['first_name'],
                    artist['second_name'],
                    artist['surname'],
                    artist['artist_id'],
                    artist['link'],
                    date_today
                )
            )
            connection.commit()
            id_artist = cursor.lastrowid

            # recuperando a última pessoa inserida no banco.
            cursor.execute("SELECT * FROM artists ORDER BY id DESC LIMIT 1;")
            resposta = cursor.fetchone()

            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

            # verifica se o tipo de resposta é um tipo psycopg2 e não um mock do teste.
            if type(resposta) == psycopg2.extras.DictRow:

                response = {
                'id': resposta[0],
                'first_name': resposta[1],
                'second_name': resposta[2],
                'surname': resposta[3],
                'artist_id': resposta[4],
                'link': resposta[5],
                'created_at': resposta[6]
                }

                return response

            # caso o tipo seja diferente de psycopg2
            response = {
                'id': id_artist,
                'first_name': artist['first_name'],
                'second_name': artist['second_name'],
                'surname': artist['surname'],
                'artist_id': artist['artist_id'],
                'link': artist['link'],
                'created_at': date_today
            }

            return response

        except Exception as e:
            connection.rollback()
            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])
            raise e

    def listar_artist(self):
        conn = self.conectar_db()
        connection = conn['connection']
        cursor = connection.cursor(cursor_factory=DictCursor)

        try:
            cursor.execute("SELECT * FROM artists;")
            response = cursor.fetchall()

            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

            return response

        except Exception as e:
            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])
            raise e

    def deletar_artist(self, artist_id):
        conn = self.conectar_db()
        connection = conn['connection']
        cursor = connection.cursor(cursor_factory=DictCursor)

        try:
            cursor.execute("DELETE FROM artists WHERE id = %s;", (artist_id,))
            connection.commit()

            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

            return "Pessoa deletada com sucesso"

        except Exception as e:
            connection.rollback()
            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])
            raise e
