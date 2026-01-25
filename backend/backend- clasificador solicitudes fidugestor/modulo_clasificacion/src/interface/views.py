from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from ..domain.dto.responses_dto import ResponseDTO
from ..domain.dto.upload_dto import BasesUploadDTO

from ..domain.port.response_http import return_response

from ..service.upload_pipeline import pipeline

from rest_framework.request import Request

class UploadFileView(APIView):

    def post(self, request:Request):

        base_inicial_value = request.FILES.get("base_inicial")
        tipo_base_inicial = request.POST.get("tipo_base_inicial")

        base_accion_grupo_value = request.FILES.get("base_accion_grupo")
        base_fallos_favor_value = request.FILES.get("base_fallos_favor")
        base_pension_gracia_value = request.FILES.get("base_pension_gracia")

        base_pensionado_fec_status_value = request.FILES.get("base_pensionado_fec_status")
        base_pensionado_fec_vinc_value = request.FILES.get("base_pensionado_fec_vinc")

        base_dto = BasesUploadDTO(
                                    base_inicial=base_inicial_value,
                                    tipo_base_inicial=tipo_base_inicial,

                                    base_accion_grupo=base_accion_grupo_value,
                                    base_fallos_favor=base_fallos_favor_value,
                                    base_pension_gracia=base_pension_gracia_value,

                                    base_pensionado_fec_status=base_pensionado_fec_status_value,
                                    base_pensionado_fec_vinc=base_pensionado_fec_vinc_value

                                    )

        pipeline(dto_object=base_dto)

        response_dto_object = ResponseDTO(status_code=200, success=True, message="Prueba", data=None)
    
        return return_response(dto_object=response_dto_object)
    




