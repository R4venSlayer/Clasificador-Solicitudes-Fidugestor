import pandas as pd
from pathlib import Path
from typing import Optional
import yaml

class FileReader:

    def open_content_pandas(self, file_path:Path, file_extension:str, s_name:Optional[str], skip_rows_number:Optional[int]):
        """
        Docstring for open_content_pandas
        
        Método encargado de abrir el contenido con pandas

        Args:

        -   file_path (Path) : Ruta del archivo
        
        returns:

        -   DataFrame: contenido abierto con pandas
        """

        if file_extension == "xlsx":
            df = pd.read_excel(file_path, sheet_name = s_name, skiprows=skip_rows_number) 
        
            return  df
        
        elif file_extension == "csv":
            df = pd.read_csv(file_path, sep=";", encoding="latin1")

            return df 
        
    
    def open_yaml_content(self, file_path:Path):
        """
        Docstring for open_yaml_content
        
        Método encargado de abrir el contenido de un archivo con extensión yaml

        Args:
            -   file_path (Path) : Ruta del archivo yaml

        Return:

            -   Dict: Diccionario con los parametros obtenidos
        """

        with open(file_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        
        return config
        
    


