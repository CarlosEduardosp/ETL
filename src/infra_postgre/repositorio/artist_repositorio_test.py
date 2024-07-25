import unittest
from unittest.mock import patch, MagicMock
from datetime import date
from src.infra_postgre.repositorio.artist_repositorio import InserirArtist
from src.infra_postgre.configs.connection.connection_db import conectar_db
from src.stages.contracts.mocks.transform_contract_mock import transform_contract_mock


class TestInserirPessoa(unittest.TestCase):

    @patch('src.infra_postgre.configs.connection.fechar_conexao')
    @patch('src.infra_postgre.configs.connection.connection_db')
    def setUp(self, mock_conectar_db, mock_fechar_conexao):
        # Mockar a conexão com o banco de dados
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conectar_db = mock_conectar_db
        self.mock_fechar_conexao = mock_fechar_conexao

        # Configurar o retorno dos mocks
        self.mock_conectar_db.return_value = {'connection': self.mock_connection, 'connection_pool': MagicMock()}
        self.mock_connection.cursor.return_value = self.mock_cursor
        self.mock_cursor.lastrowid = 1

    def test_criar_artist(self):
        # Dados mockados para a criação da pessoa
        artist = transform_contract_mock.load_content[0]

        # Criar uma instância da classe InserirPessoa com o banco mock
        repo = InserirArtist(self.mock_conectar_db)

        # criar uma instância da classe com banco real
        #repo = InserirPessoa(conectar_db)

        response = repo.criar_artist(artist=artist)

        # Verificações
        self.mock_cursor.execute(
            "INSERT INTO artists (first_name, second_name, surname, artist_id,"
                "link, created_at) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
            (
                artist['first_name'],
                artist['second_name'],
                artist['surname'],
                artist['artist_id'],
                artist['link'],
                date.today()
            )
        )
        self.mock_connection.commit()

        # Recuperar o último id salvo no banco mockado
        id_pessoa = self.mock_cursor.lastrowid

        # Acessar os argumentos passados para o execute
        insert_query, insert_values = self.mock_cursor.execute.call_args[0]

        # Fechando conexão com banco de dados
        self.mock_fechar_conexao(cursor=self.mock_cursor, connection=self.mock_connection, connection_pool=self.mock_conectar_db.return_value['connection_pool'])

        # Validações com assertEqual, realizando comparações entre os dados da função testada, com dados do mock
        self.assertEqual(response['first_name'], insert_values[0])
        self.assertEqual(response['second_name'], insert_values[1])
        self.assertEqual(response['surname'], insert_values[2])
        self.assertEqual(response['artist_id'], insert_values[3])
        self.assertEqual(response['link'], insert_values[4])
        print(response)

        # Resultado dos testes
        print('Resultado teste test_repositorio', response)

    def test_select_all(self):
        # Criar uma instância da classe InserirPessoa com o banco mock
        repo = InserirArtist(self.mock_conectar_db)

        # criar uma instância da classe com banco real
        #repo = InserirPessoa(conectar_db)

        response = repo.listar_artist()

        # Verificações
        self.mock_cursor.execute("SELECT * FROM artists;")
        self.mock_connection.commit()

        # Fechando conexão com banco de dados
        self.mock_fechar_conexao(cursor=self.mock_cursor, connection=self.mock_connection,
                                 connection_pool=self.mock_conectar_db.return_value['connection_pool'])

        # Resultado dos testes
        print('Resultado teste test_repositorio', response)


    def test_delete(self):

        # Criar uma instância da classe InserirPessoa com o banco mock
        repo = InserirArtist(self.mock_conectar_db)

        # criar uma instância da classe com banco real
        # repo = InserirPessoa(conectar_db)

        response = repo.deletar_artist(artist_id=1)

        artist_id = 1

        # Verificações
        self.mock_cursor.execute("DELETE FROM artists WHERE id = %s;", (artist_id,))
        self.mock_connection.commit()

        # Fechando conexão com banco de dados
        self.mock_fechar_conexao(cursor=self.mock_cursor, connection=self.mock_connection,
                                 connection_pool=self.mock_conectar_db.return_value['connection_pool'])

        # Resultado dos testes
        print('Resultado teste test_repositorio', response)

    def test_teste(self):

        print(transform_contract_mock.load_content[0])
