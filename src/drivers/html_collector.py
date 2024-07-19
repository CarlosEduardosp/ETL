# pylint: disable=W0105
"""
Arquivo html_collector
"""
from typing import List, Dict
from bs4 import BeautifulSoup

"""
Classe HtmlCollector
"""


class HtmlCollector:
    """
    classe HTMLCollector
    """

    @classmethod
    def collect_essential_information(cls, html: str) -> List[Dict[str, str]]:
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
