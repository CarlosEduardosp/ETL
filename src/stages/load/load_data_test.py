import unittest
from unittest.mock import patch, MagicMock
from .load_data import LoadData
from src.stages.contracts.mocks.transform_contract_mock import transform_contract_mock
from src.infra_postgre.repositorio.artist_repositorio import InserirArtist
from src.infra_postgre.configs.connection.connection_db import conectar_db
from src.errors.load_error import LoadError


class TestRepositorioSpy(unittest.TestCase):

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

    def test_load(self):

        # testando inserção com banco mock
        load = LoadData(self.mock_conectar_db)

        # testando inserção com banco real.
        #load = LoadData(InserirArtist(conectar_db))

        response = load.Load(transformed_data_contract=transform_contract_mock)
        print(response)


    def test_load_error(self):

        # testando inserção com banco mock
        load = LoadData(self.mock_conectar_db)

        # testando inserção com banco real.
        #load = LoadData(InserirArtist(conectar_db))

        try:
            response = load.Load('entrada com erro')

        except Exception as exception:
            print(exception)
            assert isinstance(exception, LoadError)
