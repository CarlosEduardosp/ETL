"""
Módulo para realizar o GET dos dados.
"""
from typing import Dict
import requests
from src.interfaces.http_requester_interface import HttpRequesterInterface


class HttpRequester(HttpRequesterInterface):
    """
    Classe HttpRequester.
    """

    def __init__(self) -> None:
        """
        Método construtor com a URL da requisição.
        """
        self.__url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'

    def request_from_page(self) -> Dict:
        """
        Realiza uma requisição GET na URL desejada e retorna um dicionário com os dados.

        :return: Dicionário com dados do GET na URL desejada.
        """
        response = requests.get(self.__url, timeout=10)
        return {
            "status_code": response.status_code,
            "html": response.text
        }
