from ..domain.dto.upload_dto import BasesUploadDTO

from ..infrastructure.file_reader.read_file_manager import FileReader

from ..infrastructure.file_manager.file_manager_operation import FileManager

from pathlib import Path

from typing import Dict

from ..infrastructure.file_reader.read_file_manager import FileReader

def pipeline(dto_object:BasesUploadDTO):

    # Paso 1. Guardar los archivos

    MEDIA_PATH_ROOT = Path(r"C:\Users\SoulO\Documents\Dev\Cruce de bases pensionales\output_code")
    
    dto_object_dict = dto_object.__dict__
    
    file_directory_dict = subprocess_save_item(media_path=MEDIA_PATH_ROOT, dto_object_dict=dto_object_dict)
    
    # Paso 2. Validar la estructura de los archivos cargados

         
def subprocess_save_item(media_path:Path, dto_object_dict:Dict):
        
    """
    Docstring for subprocess_save_item
    
    Método encargado de realizar el proceso de guardado de los archivos
    recibidos por el endpoint

    Args:
        -   media_path (Path):  Ruta de la carpeta dónde se alojarán los archivos
        -   dto_object_dict (Dict): Diccionario con los archivos recibidos por el endpoint

    Returns:
        -   Dict : Diccionario con la ruta dónde se guardan los archivos 
    """

    file_directory_dict = {}

    for key, value in dto_object_dict.items():

        if type(value) is not str:

            final_path = Path(media_path, str(value))
            
            FileManager(file_path = final_path, file=value).save_file()

            file_directory_dict[key] = final_path

    return file_directory_dict



def subprocess_convert_to_dataframe():
    """
    Docstring for subprocess_convert_to_dataframe
    
    Método encargado de realizar la apertura de los archivos
    """


