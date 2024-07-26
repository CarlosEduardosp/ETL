from abc import ABC, abstractmethod
from typing import Type, Dict


class InterfaceArtistsrepository(ABC):
    @abstractmethod
    def criar_artist(self, artist: Dict) -> Dict:
        pass

    @abstractmethod
    def listar_artist(self):
        pass

    @abstractmethod
    def deletar_artist(self, artist_id):
        pass
