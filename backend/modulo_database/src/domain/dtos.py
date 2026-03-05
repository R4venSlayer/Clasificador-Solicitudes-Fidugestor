from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional, TypeAlias


ModelId: TypeAlias = str
CatalogId: TypeAlias = int
ForeignKeyId: TypeAlias = str


@dataclass(slots=True)
class AudGestionUsuariosLogDTO:
    """DTO de la tabla `aud_gestion_usuarios_log` (`AudGestionUsuariosLog` en `backend/models.py`)."""

    id_operacion: ModelId
    id_tipo_operacion_id: CatalogId
    id_usuario_responsable: ModelId
    id_usuario_afectado: ModelId
    fecha_hora_operacion: datetime


@dataclass(slots=True)
class AudLogCargaDTO:
    """DTO de la tabla `aud_log_carga` (`AudLogCarga` en `backend/models.py`)."""

    id_aud_carga: ModelId
    id_tipo_archivo_id: CatalogId
    nombre_fuente: str
    id_usuario_responsable_id: ModelId
    fecha_hora_carga: datetime
    hash_archivo: str
    total_registros: Optional[int] = None


@dataclass(slots=True)
class AudLogDescargaDTO:
    """DTO de la tabla `aud_log_descarga` (`AudLogDescarga` en `backend/models.py`)."""

    id_descarga: ModelId
    id_lote_id: ForeignKeyId
    id_usuario_descarga_id: ModelId
    fecha_hora_descarga: datetime
    hash_archivo: str
    total_registros: Optional[int] = None


@dataclass(slots=True)
class AudLoginUsuariosLogDTO:
    """DTO de la tabla `aud_login_usuarios_log` (`AudLoginUsuariosLog` en `backend/models.py`)."""

    id_sesion_login: ModelId
    id_usuario_login_id: ModelId
    fecha_hora_login: datetime


@dataclass(slots=True)
class BaseAccionGrupoDTO:
    """DTO de la tabla `base_accion_grupo` (`BaseAccionGrupo` en `backend/models.py`)."""

    id_registro: ModelId
    id_lote_id: ForeignKeyId
    numdocumentousuario: Optional[str] = None


@dataclass(slots=True)
class BaseFalloJudicialDTO:
    """DTO de la tabla `base_fallo_judicial` (`BaseFalloJudicial` en `backend/models.py`)."""

    id_registro: ModelId
    id_lote_id: ForeignKeyId
    radicadocasomdocumentousuario: Optional[str] = None
    nombrecaso: Optional[str] = None
    numdocumentodemandante: Optional[str] = None
    jurisdiccioncaso: Optional[str] = None
    estadoproceso: Optional[str] = None


@dataclass(slots=True)
class BasePensionFechaStatusDTO:
    """DTO de la tabla `base_pension_fecha_status` (`BasePensionFechaStatus` en `backend/models.py`)."""

    id_registro: ModelId
    id_lote_id: ForeignKeyId
    numdocumentopensionado: Optional[str] = None
    fechastatus: Optional[datetime] = None


@dataclass(slots=True)
class BasePensionFechaVinculacionDTO:
    """DTO de la tabla `base_pension_fecha_vinculacion` (`BasePensionFechaVinculacion` en `backend/models.py`)."""

    id_registro: ModelId
    id_lote_id: ForeignKeyId
    numdocumentopensionado: Optional[str] = None
    fechavinculacion: Optional[datetime] = None
    mesada: Optional[Decimal] = None
    regimenpension: Optional[str] = None


@dataclass(slots=True)
class BasePensionGraciaDTO:
    """DTO de la tabla `base_pension_gracia` (`BasePensionGracia` en `backend/models.py`)."""

    id_registro: ModelId
    id_lote_id: ForeignKeyId
    numdocumentopensionado: Optional[str] = None


@dataclass(slots=True)
class BasePrincipalDTO:
    """DTO de la tabla `base_principal` (`BasePrincipal` en `backend/models.py`)."""

    id_registro: ModelId
    id_lote_id: ForeignKeyId
    id_tipo_base_principal_id: CatalogId
    radicado: Optional[str] = None
    proceso: Optional[str] = None
    nombreaccionante: Optional[str] = None
    numdocumentoaccionante: Optional[str] = None
    tipodocumentoremitente: Optional[str] = None
    emailremitente: Optional[str] = None


@dataclass(slots=True)
class CatEtapaValidacionDTO:
    """DTO de la tabla `cat_etapa_validacion` (`CatEtapaValidacion` en `backend/models.py`)."""

    id_etapa_validacion: CatalogId
    nombre_etapa: Optional[str] = None


@dataclass(slots=True)
class CatTipoBasePrincipalDTO:
    """DTO de la tabla `cat_tipo_base_principal` (`CatTipoBasePrincipal` en `backend/models.py`)."""

    id_base_principal: CatalogId
    nombre_base_principal: str


@dataclass(slots=True)
class CatTipoDocumentoIdentidadDTO:
    """DTO de la tabla `cat_tipo_documento_identidad` (`CatTipoDocumentoIdentidad` en `backend/models.py`)."""

    id_tipo: CatalogId
    abreviacion: str
    descripcio: str


@dataclass(slots=True)
class CatTipoFuenteArchivoDTO:
    """DTO de la tabla `cat_tipo_fuente_archivo` (`CatTipoFuenteArchivo` en `backend/models.py`)."""

    id_fuente: CatalogId
    nombre_archivo: Optional[str] = None


@dataclass(slots=True)
class CatTipoOperacionGestionUsuarioDTO:
    """DTO de la tabla `cat_tipo_operacion_gestion_usuario` (`CatTipoOperacionGestionUsuario` en `backend/models.py`)."""

    id_tipo_operacion: CatalogId
    nombre_operacion: Optional[str] = None


@dataclass(slots=True)
class HistoricalOutputDatasetsDTO:
    """DTO de la tabla `historical_output_datasets` (`HistoricalOutputDatasets` en `backend/models.py`)."""

    id_output_record: ModelId
    id_lote_id: ForeignKeyId
    radicado: Optional[str] = None
    proceso: Optional[str] = None
    nombre_accionante: Optional[str] = None
    num_documento_accionante: Optional[str] = None
    tipo_documento_accionante: Optional[str] = None
    num_documento_pensionado: Optional[str] = None
    fecha_vinculacion: Optional[datetime] = None
    fecha_status: Optional[datetime] = None
    mesada: Optional[Decimal] = None
    regimen_pension: Optional[str] = None
    num_documento_usuario_accion_grupo: Optional[str] = None
    num_documento_usuario_fallo_judicial: Optional[str] = None
    radicado_caso: Optional[str] = None
    nombre_caso: Optional[str] = None
    jurisdiccion_caso: Optional[str] = None
    estado_proceso: Optional[str] = None
    num_documento_usuario_pension_gracia: Optional[str] = None
    id_etapa_validacion_id: Optional[CatalogId] = None
    tiene_derecho: Optional[bool] = None
    fecha_ejecucion_validacion: Optional[datetime] = None


@dataclass(slots=True)
class LoteDatasetsDTO:
    """DTO de la tabla `lote_datasets` (`LoteDatasets` en `backend/models.py`)."""

    id_lote: ModelId
    id_aud_carga_id: Optional[ForeignKeyId] = None


@dataclass(slots=True)
class PermisosDTO:
    """DTO de la tabla `permisos` (`Permisos` en `backend/models.py`)."""

    id_permiso: CatalogId
    nombre_permiso: str


@dataclass(slots=True)
class RefreshTokensDTO:
    """DTO de la tabla `refresh_tokens` (`RefreshTokens` en `backend/models.py`)."""

    id_refresh_token: ModelId
    id_usuario_id: ModelId
    token_hash: str
    fecha_hora_expiracion: datetime
    revocado: bool


@dataclass(slots=True)
class RolesDTO:
    """DTO de la tabla `roles` (`Roles` en `backend/models.py`)."""

    id_rol: CatalogId
    nombre_rol: str


@dataclass(slots=True)
class RolesPermisosDTO:
    """DTO de la tabla `roles_permisos` (`RolesPermisos` en `backend/models.py`)."""

    id_rol_permiso: ModelId
    id_rol_id: CatalogId
    id_permiso_id: CatalogId


@dataclass(slots=True)
class UsuariosDTO:
    """DTO de la tabla `usuarios` (`Usuarios` en `backend/models.py`)."""

    id_usuario: ModelId
    tipo_documento_identidad_id: CatalogId
    num_documento_identidad: str
    primer_nombre: str
    segundo_nombre: Optional[str] = None
    primer_apellido: str = ""
    segundo_apellido: Optional[str] = None
    email_usuario: str = ""
    nombre_usuario: str = ""
    password_usuario: str = ""
    codigo_seguridad: str = ""
    id_rol_id: CatalogId = 0
    es_activo: bool = True
