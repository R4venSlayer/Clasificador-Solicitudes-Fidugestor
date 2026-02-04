from .base_repository import BaseRepository
from ..models.modelo import Gestorarchivo, Lotegestorarchivo


class GestorArchivoRepository(BaseRepository):
    model = Gestorarchivo


class LoteGestorArchivoRepository(BaseRepository):
    model = Lotegestorarchivo


