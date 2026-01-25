from ..dto.responses_dto import ResponseDTO

from rest_framework.response import Response


def return_response(dto_object: ResponseDTO):

    return Response({"success":dto_object.success, "message":dto_object.message, "data":dto_object.data},status=dto_object.status_code)
 
