import pandas as pd
from pathlib import Path
from typing import Optional

class FileReader():

    def open_content_pandas(file_path:Path, file_extension:str, s_name:Optional[str]):
        """
        Docstring for open_content_pandas
        
        Método encargado de abrir el contenido con pandas

        Args:

        -   file_path (Path) : Ruta del archivo
        
        returns:

        -   DataFrame: contenido abierto con pandas
        """

        if file_extension == "xlsx":
            df = pd.read_excel(file_path, sheet_name = s_name)
        
        elif file_extension == "csv":
            df = pd.read_csv(file_path, sep=";")

        return df
    


