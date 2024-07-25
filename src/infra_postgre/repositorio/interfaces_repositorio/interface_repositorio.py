from abc import ABC, abstractmethod


class InterfaceArtistsepository(ABC):
    @abstractmethod
    def criar_artist(self, first_name, second_name, surname, artist_id, link, created_at):
        pass

    @abstractmethod
    def listar_artist(self):
        pass

    @abstractmethod
    def deletar_artist(self, artist_id):
        pass
