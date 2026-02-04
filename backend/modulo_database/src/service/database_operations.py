from ..domain.ports import (
    CreateRepository,
    BulkCreateRepository,
    QueryRepository
)

from typing import Dict, List

class CrearRegistroUseCase:

    """
    Docstring for RegistrarLoteArchivoUseCase
    
    Clase encargada de ejecutar la operación para crear los registros
    en la tabla de LoteGestorArchivo


    """

    def __init__(
        self,
        repository: CreateRepository
    ):

        self.repository = repository

    def execute(self, data: Dict):
        
        self.repository.create(**data)

class CrearMasivoRegistroUseCase:

    """
    Docstring for CrearMasivoRegistroUseCase
    
    Clase encargarda de ejecutar la operación para crear los registros
    en las diferentes tablas a procesar

    """
    def __init__(
        self,
        repository: BulkCreateRepository
    ):
        self.repository = repository

    def execute(self, dto_list: List):
        
        objects_list = self.create_list_obj_from_dto(dto_list=dto_list)
        self.repository.bulk_create(objs=objects_list)

    def create_list_obj_from_dto(self, dto_list):
        
        objects_list = []

        for item in dto_list:
            objects_list.append(self.repository.model(**item.__dict__))
        
        return objects_list

        
class ObtenerRegistrosUseCase:
    def __init__(
        self,
        repository: QueryRepository
    ):
        self.repository = repository
        
    def execute(self, filters_dictionary):
        return self.repository.get(**filters_dictionary)


        

# class ObtenerTipoArchivoUseCase:

#     def __init__(
#         self,
#         tipo_archivo_repo: CreateRepository,

#     ):
#         self.archivo_repo = archivo_repo


#     def execute(self, archivo_data: Dict):
        
#         self.archivo_repo.create(**archivo_data)
