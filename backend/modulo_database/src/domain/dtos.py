# domain/dtos/dtos.py

from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from decimal import Decimal
from uuid import UUID

# =========================
# BaseAccionGrupo
# =========================
@dataclass
class BaseAccionGrupoDTO:
    id: UUID
    num_documento_usuario: Optional[str]
    id_archivo_id: UUID


# =========================
# BaseFalloJudicial
# =========================
@dataclass
class BaseFalloJudicialDTO:
    id: UUID
    radicado_caso: Optional[str]
    nombre_caso: Optional[str]
    num_documento_demandante: Optional[str]
    nombre_demandante: Optional[str]
    jurisdiccion_caso: Optional[str]
    estado_proceso: Optional[str]
    id_archivo_id: UUID


# =========================
# BaseInicial
# =========================
@dataclass
class BaseInicialDTO:
    id: UUID
    radicado: Optional[str]
    proceso: Optional[str]
    id_tipo_base_inicial_id: int
    nombre_accionante: Optional[str]
    num_documento_accionante: Optional[str]
    tipo_documento_accionante: Optional[str]
    email_accionante: Optional[str]
    id_archivo_id: UUID


# =========================
# BasePensionGracia
# =========================
@dataclass
class BasePensionGraciaDTO:
    id: UUID
    num_documento_pensionado: Optional[str]
    id_archivo_id: UUID


# =========================
# BasePensionadosFecStatus
# =========================
@dataclass
class BasePensionadosFecStatusDTO:
    id: UUID
    num_documento_pensionado: Optional[str]
    fecha_status: Optional[datetime]
    id_archivo_id: UUID


# =========================
# BasePensionadosFecVinculacion
# =========================
@dataclass
class BasePensionadosFecVinculacionDTO:
    id: UUID
    num_documento_pensionado: Optional[str]
    fecha_vinculacion: Optional[datetime]
    mesada: Optional[Decimal]
    regimen_pension: Optional[str]
    id_archivo_id: UUID


# =========================
# GestorArchivo
# =========================
@dataclass
class GestorArchivoDTO:
    id: UUID
    nombre_archivo: str
    ruta_archivo: str
    id_tipo_archivo_id: int
    id_lote_gestor_archivo_id: UUID
    procesado: bool


# =========================
# LoteGestorArchivo
# =========================
@dataclass
class LoteGestorArchivoDTO:
    id: UUID
    id_usuario_quien_carga: Optional[UUID]
    fecha_hora_carga: Optional[datetime]
    procesado: bool


# =========================
# TipoArchivo (catálogo)
# =========================
@dataclass
class TipoArchivoDTO:
    nombre_tipo_archivo: str


# =========================
# TipoBaseInicial (catálogo)
# =========================
@dataclass
class TipoBaseInicialDTO:
    id: int
    nombre_base_inicial: str
