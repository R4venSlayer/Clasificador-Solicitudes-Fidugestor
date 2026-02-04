from .base_repository import BaseRepository
from ..models.modelo import (   Baseinicial, Basefallojudicial,
                                Baseacciongrupo, Basepensionadosfecstatus,
                                Basepensionadosfecvinculacion, Basepensiongracia )


class BaseInicialRepository(BaseRepository):
    model = Baseinicial


class BaseFalloJudicialRepository(BaseRepository):
    model = Basefallojudicial


class BaseAccionGrupoRepository(BaseRepository):
    model = Baseacciongrupo


class BasePensionadosFecStatusRepository(BaseRepository):
    model = Basepensionadosfecstatus

class BasePensionadosFecVinculacionRepository(BaseRepository):
    model = Basepensionadosfecvinculacion


class BasePensionGraciaRepository(BaseRepository):
    model = Basepensiongracia

