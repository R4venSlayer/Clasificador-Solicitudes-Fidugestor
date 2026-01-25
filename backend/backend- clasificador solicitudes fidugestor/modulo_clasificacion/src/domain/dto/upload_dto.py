from dataclasses import dataclass
from typing import Optional
from django.core.files.uploadedfile import UploadedFile


@dataclass(frozen=True)
class BasesUploadDTO:
    # Base inicial
    base_inicial: Optional[UploadedFile]
    tipo_base_inicial: Optional[str]

    # Bases adicionales
    base_accion_grupo: Optional[UploadedFile]
    base_fallos_favor: Optional[UploadedFile]
    base_pension_gracia: Optional[UploadedFile]

    # Bases pensionado
    base_pensionado_fec_status: Optional[UploadedFile]
    base_pensionado_fec_vinc: Optional[UploadedFile]
