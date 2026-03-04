from ...domain.dto.upload_dto import BasesUploadDTO

from ...infrastructure.file_reader.read_file_manager import FileReader

from ...infrastructure.file_manager.file_manager_operation import FileManager



from ...infrastructure.file_reader.read_file_manager import FileReader



from colorama import init, Fore

from ..transform_data.file_transform_pipeline import TransformDataFrame

import pandas as pd


import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict

from modulo_database.src.domain.dtos import GestorArchivoDTO, LoteGestorArchivoDTO

from modulo_database.src.infrastructure.repository.catalogo_repositories import (TipoArchivoRepository,  TipoBaseInicialRepository)

from modulo_database.src.service.database_operations import CrearRegistroUseCase, CrearMasivoRegistroUseCase, ObtenerRegistrosUseCase

from modulo_database.src.infrastructure.repository.tipo_archivo_repositories import (BaseInicialRepository,BaseAccionGrupoRepository,
                                                                                     BaseFalloJudicialRepository, BasePensionGraciaRepository,
                                                                                     BasePensionadosFecStatusRepository, BasePensionadosFecVinculacionRepository) 

from modulo_database.src.domain.dtos import (BaseInicialDTO, BaseAccionGrupoDTO, BaseFalloJudicialDTO,
                                             BasePensionGraciaDTO, BasePensionadosFecStatusDTO, BasePensionadosFecVinculacionDTO,
                                             TipoArchivoDTO, TipoBaseInicialDTO)

from modulo_database.src.infrastructure.repository.archivo_repositories import GestorArchivoRepository, LoteGestorArchivoRepository



def pipeline(dto_object:BasesUploadDTO):

    # Paso 1. Guardar los archivos

    MEDIA_PATH_ROOT = Path(r"C:\Users\SoulO\Documents\Pruebas\Clasificador Solicitudes Fidugestor\media\uploaded-files")
    
    dto_object_dict = dto_object.__dict__
    
    file_directory_dict = subprocess_save_item(media_path=MEDIA_PATH_ROOT, dto_object_dict=dto_object_dict)
    
    # Paso 2. Validar la estructura de los archivos cargados

    dataframe_collections = subprocess_convert_to_dataframe(file_directory_dictionary=file_directory_dict)

    dataframe_transformed_collections = subprocess_preprocess_dataframe_content(df_collections=dataframe_collections, tipo_base_inicial = dto_object.tipo_base_inicial)


    final_df = cross_process(dataframe_transformed_collections)


    final_df.to_excel(r"C:\Users\SoulO\Documents\Pruebas\Clasificador Solicitudes Fidugestor\media\resultado_cruce.xlsx", index=False)

    # print(dataframe_transformed_collections.keys())
    
    # subprocess_save_dataframe_content(file_directory_dict)

         
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

        
        file_ext_value = config["base"][key]["file_extension"]
        sheet_name_value = config["base"][key]["sheet_name"]
        skip_rows_value = config["base"][key]["skip_rows"]
        

        df = FileReader().open_content_pandas(  file_path=value, 
                                                file_extension=file_ext_value, 
                                                s_name=sheet_name_value,
                                                skip_rows_number=skip_rows_value)
            
        dataframe_collections[key] = df

    return dataframe_collections


def subprocess_preprocess_dataframe_content(df_collections:Dict, tipo_base_inicial:str):
    """
    Docstring for subprocess_preprocess_dataframe_content
    
    Método encargado de preparar los archivos para subirlos
    a la base de datos 

    """
    df_transformed_collections = {}

    for key, value in df_collections.items():

        if key != "base_inicial":
            df_transformed_collections[key] = TransformDataFrame(df=value, tipo_base=key, tipo_base_inicial=tipo_base_inicial).pipeline_transform_data()

        elif key == "base_inicial":
            df_transformed_collections[key] = TransformDataFrame(df=value, tipo_base=key, tipo_base_inicial=tipo_base_inicial).subprocess_recreate_dataframe()

    
    return df_transformed_collections


def cross_process(dictionary):

    df_base = dictionary["base_inicial"].copy()
    df_accion_grupo = dictionary["base_accion_grupo"].copy()
    df_fallos = dictionary["base_fallos_favor"].copy()
    df_pension_gracia = dictionary["base_pension_gracia"].copy()
    base_pensionados_fec_status = dictionary["base_pensionado_fec_status"].copy()
    base_pensionados_fec_vinc = dictionary["base_pensionado_fec_vinc"].copy()

    # Cruce de bases pensionales
    df_base["numDocumentoAccionante"] = (
        df_base["numDocumentoAccionante"].astype(str).str.strip()
    )
    base_pensionados_fec_vinc["numDocumentoPensionado"] = (
        base_pensionados_fec_vinc["numDocumentoPensionado"].astype(str).str.strip()
    )
    base_pensionados_fec_status["numDocumentoPensionado"] = (
        base_pensionados_fec_status["numDocumentoPensionado"].astype(str).str.strip()
    )

    base_pensionados_fec_vinc = base_pensionados_fec_vinc.drop_duplicates(
        subset=["numDocumentoPensionado"]
    )
    base_pensionados_fec_status = base_pensionados_fec_status.drop_duplicates(
        subset=["numDocumentoPensionado"]
    )

    left_pensional = [
        "numDocumentoPensionado",
        "fechaVinculacion",
        "mesada",
        "regimenPension",
    ]
    right_pensional = ["numDocumentoPensionado", "fechaStatus"]

    df_base_pensional = pd.merge(
        left=base_pensionados_fec_vinc[left_pensional],
        right=base_pensionados_fec_status[right_pensional],
        left_on="numDocumentoPensionado",
        right_on="numDocumentoPensionado",
        how="left",
    )

    right_cruce_pensional = [
        "numDocumentoPensionado",
        "fechaVinculacion",
        "fechaStatus",
        "mesada",
        "regimenPension",
    ]

    df_cruce_pensional = pd.merge(
        left=df_base,
        right=df_base_pensional[right_cruce_pensional],
        left_on="numDocumentoAccionante",
        right_on="numDocumentoPensionado",
        how="left",
    )
    df_cruce_pensional.rename(
        columns={"numDocumentoPensionado": "cedula - Base Pensionado"}, inplace=True
    )

    # Cruce base accion grupo
    df_accion_grupo["numDocumentoUsuario"] = (
        df_accion_grupo["numDocumentoUsuario"].astype(str).str.strip()
    )

    df_cruce_accion_grupo = pd.merge(
        left=df_cruce_pensional,
        right=df_accion_grupo[["numDocumentoUsuario"]],
        left_on="numDocumentoAccionante",
        right_on="numDocumentoUsuario",
        how="left",
    )
    df_cruce_accion_grupo.rename(
        columns={"numDocumentoUsuario": "cedula - Base Accion Grupo"}, inplace=True
    )

    # Cruce base fallos judiciales
    if "FALLO FINAL" in df_fallos.columns:
        df_fallos = df_fallos[df_fallos["FALLO FINAL"] == "A FAVOR"]

    df_fallos["numDocumentoDemandante"] = (
        df_fallos["numDocumentoDemandante"]
        .astype(str)
        .str.strip()
        .str.replace(".", "", regex=False)
    )

    right_fallos = [
        "nombreCaso",
        "radicadoCaso",
        "numDocumentoDemandante",
        "jurisdiccionCaso",
        "estadoProceso",
    ]
    df_cruce_fallo_judicial = pd.merge(
        left=df_cruce_accion_grupo,
        right=df_fallos[right_fallos],
        left_on="numDocumentoAccionante",
        right_on="numDocumentoDemandante",
        how="left",
    )
    df_cruce_fallo_judicial.rename(
        columns={"numDocumentoDemandante": "cedula - Base Fallos Judiciales"},
        inplace=True,
    )

    # Cruce base pension gracia
    df_pension_gracia["numDocumentoPensionado"] = (
        df_pension_gracia["numDocumentoPensionado"].astype(str).str.strip()
    )

    df_cruce_pension_gracia = pd.merge(
        left=df_cruce_fallo_judicial,
        right=df_pension_gracia[["numDocumentoPensionado"]],
        left_on="numDocumentoAccionante",
        right_on="numDocumentoPensionado",
        how="left",
    )
    df_cruce_pension_gracia.rename(
        columns={"numDocumentoPensionado": "cedula - Base Pension Gracia"},
        inplace=True,
    )

    # Validaciones
    df = df_cruce_pension_gracia.copy()

    df["fechaVinculacion"] = pd.to_datetime(df["fechaVinculacion"], errors="coerce")
    df["fechaStatus"] = pd.to_datetime(df["fechaStatus"], errors="coerce")
    df["mesada"] = pd.to_numeric(df["mesada"], errors="coerce")

    fecha_inicio = pd.Timestamp("1981-01-01")
    fecha_fin = pd.Timestamp("2003-06-26")
    fecha_inicio_status = pd.Timestamp("2005-07-25")
    fecha_fin_status = pd.Timestamp("2011-07-31")
    fecha_upper_lim = pd.Timestamp("2011-07-31")
    smmlv_3 = 5_252_715

    df["RESULTADO"] = None

    reglas = [
        (df["cedula - Base Pensionado"].isna(), "PROCESO BASE PENSIONAL"),
        (df["cedula - Base Accion Grupo"].notna(), "PROCESO ACCION GRUPO"),
        (df["cedula - Base Fallos Judiciales"].notna(), "PROCESO FALLO JUDICIAL"),
        (df["cedula - Base Pension Gracia"].notna(), "PROCESO PENSION GRACIA"),
        (
            df["fechaVinculacion"].notna()
            & ~df["fechaVinculacion"].between(fecha_inicio, fecha_fin),
            "REGLA 5 - FUERA RANGO VINCULACION",
        ),
        (
            df["fechaVinculacion"].between(fecha_inicio, fecha_fin)
            & (df["fechaStatus"] > fecha_upper_lim),
            "REGLA 6 - FECHA STATUS SUPERIOR",
        ),
        (
            df["fechaStatus"].between(fecha_inicio_status, fecha_fin_status)
            & (df["mesada"] > smmlv_3),
            "REGLA 7 - MESADA SUPERIOR SMMLV",
        ),
    ]

    for condicion, etiqueta in reglas:
        df.loc[df["RESULTADO"].isna() & condicion, "RESULTADO"] = etiqueta

    df.loc[df["RESULTADO"].notna(), "TIENE DERECHO"] = "NO"
    df["TIENE DERECHO"] = df["TIENE DERECHO"].fillna("SI")

    dictionary["cross_process_result"] = df
    return df


    



def subprocess_save_dataframe_content(file_directory:Dict):

    """
    Docstring for subprocess_save_dataframe_content
    
    Método encargado de realizar el guardado de los Dataframe en las respectivas
    tablas
    
    """

    file_type_convert_idx = {
        'base_inicial' :1,
        'base_accion_grupo' :2,
        'base_fallos_favor' :3,
        'base_pension_gracia' :4,
        'base_pensionado_fec_status' :5,
        'base_pensionado_fec_vinc' :6
    }

    repository_dictionary = {

        'base_inicial' : BaseInicialRepository(),
        'base_accion_grupo' :BaseAccionGrupoRepository(),
        'base_fallos_favor' :BaseFalloJudicialRepository(),
        'base_pension_gracia' : BasePensionGraciaRepository(),
        'base_pensionado_fec_status' : BasePensionadosFecStatusRepository(),
        'base_pensionado_fec_vinc' : BasePensionadosFecVinculacionRepository(),
        'tipo_archivo' : TipoArchivoRepository(),
        'tipo_base_inicial' : TipoBaseInicialRepository()

    }

    # Paso 1. Crear el registro en - LoteGestorArchivo / GestorArchivo

    # - Se crea el uuid para el registro de Lote
    uuid_lote = str(uuid.uuid4()) # UUID registro Lote

    # ################################### TEMPORAL #####################################################
    
    # - Se crea un uuid temporalmente que represente a un usuario
    uuid_extra = str(uuid.uuid4()) # UUID registro usuario generico

    # ################################### - - - - - - - -  #############################################

    # - Se crea el dto que va a contener la data a cargar en la tabla LoteGestorArchivo
    lote_dto = LoteGestorArchivoDTO(    id=uuid_lote,
                                        id_usuario_quien_carga=uuid_extra,
                                        fecha_hora_carga=datetime.now(),
                                        procesado=False)

    #   --- PARA CARGAR INFORMACIÓN EN LA TABLA "LoteGestorArchivo" ---

    # - Se crea una instancia con el repositorio de la tabla LoteGestorArchivo
    create_record_use_case = CrearRegistroUseCase(repository=LoteGestorArchivoRepository())
    # - Se ejecuta la operacion para cargar los datos a la tabla
    create_record_use_case.execute(data=lote_dto.__dict__)
    
    #  --- PARA CARGAR INFORMACIÓN EN LA TABLA "GestorArchivo" ---

    # - Se crea una instancia con el repositorio de la tabla GestorArchivo
    create_record_use_case = CrearRegistroUseCase(repository=GestorArchivoRepository())

    # - Se crea un ciclo para realizar el recorrido del directorio de archivos y guardar los respectivos registros
    # en la base de datos.
     
    for key, value in file_directory.items():

        # - Se crea un uuid para el registro del archivo       
        uuid_archivo = str(uuid.uuid4())

        # - Se crea el dto que va a contener la data a cargar en la tabla GestorArchivo
        gestor_dto = GestorArchivoDTO(id=uuid_archivo,
                                      nombre_archivo=value.name,
                                      ruta_archivo=value,
                                      id_tipo_archivo_id=file_type_convert_idx[key],
                                      id_lote_gestor_archivo_id=uuid_lote,
                                      procesado=False)
        
        # - Se ejecuta la operacion para cargar los datos a la tabla
        create_record_use_case.execute(data=gestor_dto.__dict__)

    # Paso 2. Cargar el contenido obtenido y previamente transformado

    # ... REGISTROS DE PRUEBA PARA CARGUE MASIVO
    uuid_prueba1 = uuid.uuid4()
    uuid_prueba2 = uuid.uuid4()


    # Se consulta la tabla catalogo TipoBaseInicial para extraer el tipo de base incial que va a cargar el usuario
    
    filter_tipo_base_inicial = { "id" : 1 }
    obtener_registro_service = ObtenerRegistrosUseCase(repository=repository_dictionary["tipo_base_inicial"])
    tipo_base_inicial_queryset = obtener_registro_service.execute(filters_dictionary=filter_tipo_base_inicial)

    # Se consulta la tabla catalogo TipoArchivo para extraer el tipo de archivo que cargó inicialmente el usuario

    filter_tipo_archivo = { "id" : 1 }
    obtener_registro_service = ObtenerRegistrosUseCase(repository=repository_dictionary["tipo_archivo"])
    tipo_archivo_queryset = obtener_registro_service.execute(filters_dictionary=filter_tipo_archivo)

    # Se consulta la tabla catalogo TipoBaseInicial para extraer el tipo de base incial que va a cargar el usuario

    filter_gestor_archivo = { "id_lote_gestor_archivo": uuid_lote, "id_tipo_archivo": tipo_archivo_queryset }
    obtener_registro_service = ObtenerRegistrosUseCase(repository=GestorArchivoRepository())
    gestor_archivo_queryset = obtener_registro_service.execute(filters_dictionary=filter_gestor_archivo)

    crear_masivo_service = CrearMasivoRegistroUseCase(repository=repository_dictionary["base_inicial"])

    item_1   =      BaseInicialDTO( id = uuid_prueba1,
                                    radicado = "sss",
                                    proceso = "sss",
                                    id_tipo_base_inicial_id = tipo_base_inicial_queryset.id,
                                    nombre_accionante = "Luis",
                                    num_documento_accionante = "123",
                                    tipo_documento_accionante =  "CC",
                                    email_accionante = "prueba@gmail.com",
                                    id_archivo_id = gestor_archivo_queryset.id )
    

    item_2   =      BaseInicialDTO( id = uuid_prueba2,
                                    radicado = "sss",
                                    proceso = "sss",
                                    id_tipo_base_inicial_id = tipo_base_inicial_queryset.id,
                                    nombre_accionante = "Andres",
                                    num_documento_accionante = "123",
                                    tipo_documento_accionante =  "CC",
                                    email_accionante = "prueba@gmail.com",
                                    id_archivo_id = gestor_archivo_queryset.id )

    dto_trial_list = [item_1, item_2]

    crear_masivo_service.execute(dto_list=dto_trial_list)

    # for key, value in df_transformed_collection.items():

    #     create_massive_record_use_case = CrearMasivoRegistro(repository=GestorArchivoRepository())

        


    







