"""
Módulo para realizar o GET dos dados.
"""

from typing import Dict
from abc import ABC, abstractmethod


class HttpRequesterInterface(ABC):
    """
    Classe HttpRequester.
    """
    @abstractmethod
    def request_from_page(self) -> Dict:
        pass
