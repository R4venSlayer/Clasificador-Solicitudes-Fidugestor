

from .base_repository import BaseRepository

from ..models.modelo import Tipoarchivo, Tipobaseinicial


class TipoArchivoRepository(BaseRepository):
    model = Tipoarchivo 

class TipoBaseInicialRepository(BaseRepository):
    model = Tipobaseinicial
