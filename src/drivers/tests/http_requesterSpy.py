# pylint: disable=W0105, W0221, C0103
from typing import Dict
from src.drivers.interfaces.http_requester_interface import HttpRequesterInterface


class HttpRequesterSPY(HttpRequesterInterface):
    """
    Classe HttpRequester.
    """

    def __init__(self) -> None:
        """
        Método construtor com a URL da requisição.
        """
        self.request_from_page_count = 0

    def request_from_page(self) -> Dict:
        """
        Realiza uma requisição GET na URL desejada e retorna um dicionário com os dados.

        :return: Dicionário com dados do GET na URL desejada.
        """
        self.request_from_page_count += 1
        return {
            "status_code": 200,
            "html": "<h1>Olá Mundo!</h1>"
        }
