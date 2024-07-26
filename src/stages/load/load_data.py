from src.infra_postgre.repositorio.interfaces_repositorio.interface_repositorio import InterfaceArtistsrepository
from src.stages.contracts.tranform_contract import TranformContract
from src.errors.load_error import LoadError


class LoadData:
    def __init__(self, repository: InterfaceArtistsrepository) -> None:
        self.repository = repository

    def Load(self, transformed_data_contract: TranformContract) -> None:

        try:

            load_content = transformed_data_contract.load_content
            cont = 0
            for data in load_content:
                self.repository.criar_artist(data)
                cont += 1

            return {"Success": True, "message": f'Inserção de {cont} dados, Realizada com Sucesso'}

        except Exception as exception:
            raise LoadError(str(exception)) from exception
