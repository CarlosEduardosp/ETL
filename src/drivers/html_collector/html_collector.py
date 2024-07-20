# pylint: disable=W0105, W0221
"""
Arquivo html_collector
"""
from typing import List
from bs4 import BeautifulSoup
from src.interfaces.html_collector_interface import HtmlCollectorInterface
"""
Classe HtmlCollector
"""


class HtmlCollector(HtmlCollectorInterface):
    """
    classe HTMLCollector
    """

    @classmethod
    def collect_essential_information(cls, html: str) -> List:
        """
        :param html:
        :return:
        """

        soup = BeautifulSoup(html, 'html.parser')

        artist_name_list = soup.find(class_='BodyText')

        artist_name_itens = artist_name_list.find_all('a')

        essential_information = []
        for artist_name in artist_name_itens:
            names = artist_name.contents[0]
            links = 'https://web.archive.org' + artist_name.get('href')

            essential_information.append({
                "name": names,
                "link": links
            })

        return essential_information
