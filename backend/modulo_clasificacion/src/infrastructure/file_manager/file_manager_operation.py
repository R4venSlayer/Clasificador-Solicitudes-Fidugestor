from pathlib import Path

from django.core.files.uploadedfile import UploadedFile

class FileManager:

    def __init__(self, file:UploadedFile , file_path:Path):

        self.file_path = file_path
        self.file = file
        
    def save_file(self):

        """
        Docstring for save_file
        
        Método para guardar los archivos recibidos

        :param self: Description
        
        """

        with open(f"{self.file_path}", "wb+") as destino:
            for chunk in self.file.chunks():
                destino.write(chunk)
