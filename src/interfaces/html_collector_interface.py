# pylint: disable=W0105
"""
Arquivo html_collector
"""
from abc import ABC, abstractmethod
from typing import List, Dict
"""
Classe HtmlCollector
"""


class HtmlCollectorInterface(ABC):
    """
    classe HTMLCollector
    """

    @abstractmethod
    def collect_essential_information(self, html: str) -> List[Dict[str, str]]:
        pass
