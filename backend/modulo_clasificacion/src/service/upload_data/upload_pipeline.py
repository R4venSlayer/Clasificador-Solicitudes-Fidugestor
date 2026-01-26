from ...domain.dto.upload_dto import BasesUploadDTO

from ...infrastructure.file_reader.read_file_manager import FileReader

from ...infrastructure.file_manager.file_manager_operation import FileManager

from pathlib import Path

from typing import Dict

from ...infrastructure.file_reader.read_file_manager import FileReader

import pandas as pd

from colorama import init, Fore

from ..transform_data.file_transform_pipeline import TransformDataFrame

def pipeline(dto_object:BasesUploadDTO):

    # Paso 1. Guardar los archivos

    MEDIA_PATH_ROOT = Path(r"C:\Users\SoulO\Documents\Pruebas\Clasificador Solicitudes Fidugestor\media\uploaded-files")
    
    dto_object_dict = dto_object.__dict__
    
    file_directory_dict = subprocess_save_item(media_path=MEDIA_PATH_ROOT, dto_object_dict=dto_object_dict)


    init()

    # Paso 2. Validar la estructura de los archivos cargados

    dataframe_collections = subprocess_convert_to_dataframe(file_directory_dictionary=file_directory_dict)

    subprocess_preprocess_dataframe_content(df_collections=dataframe_collections)
         
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



def subprocess_convert_to_dataframe(file_directory_dictionary: Dict):
    """
    Docstring for subprocess_convert_to_dataframe
    
    Método encargado de realizar la apertura de los archivos

    """

    # Se extraen los parámetros requeridos para abrir cada archivo

    YAML_FILE_PATH = r"modulo_clasificacion\src\service\upload_data\pandas_file_parameters.yaml"
    config = FileReader().open_yaml_content(file_path=YAML_FILE_PATH)

    dataframe_collections = {}

    for key, value in file_directory_dictionary.items(): 
        if key == "base_fallos_favor":
            file_ext_value = config["base"][key]["file_extension"]
            sheet_name_value = config["base"][key]["sheet_name"]
            skip_rows_value = config["base"][key]["skip_rows"]
            

            df = FileReader().open_content_pandas(file_path=value, 
                                                file_extension=file_ext_value, 
                                                s_name=sheet_name_value,
                                                skip_rows_number=skip_rows_value)
            
            dataframe_collections[key] = df

    return dataframe_collections


def subprocess_preprocess_dataframe_content(df_collections:Dict):
    """
    Docstring for subprocess_preprocess_dataframe_content
    
    Método encargado de preparar los archivos para subirlos
    a la base de datos 

    """
    df_transformed_collections = {}

    for key, value in df_collections.items():
        TransformDataFrame(df=value, tipo_base=key).pipeline_transform_data().to_excel(fr"C:\Users\SoulO\Documents\Pruebas\Clasificador Solicitudes Fidugestor\temp\{key}.xlsx",index=False)


    return df_transformed_collections
    

def subprocess_save_dataframe_content():

    """
    Docstring for subprocess_save_dataframe_content
    
    Método encargado de realizar el guardado de los Dataframe en las respectivas
    tablas
    
    """


    # Paso 1. Crear el registro en - LoteGestorArchivo







