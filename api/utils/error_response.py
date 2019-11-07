from rest_framework import status
from rest_framework.response import Response


def generate_error_response(error_code):
    return Response({'error_code': error_code}, status=status.HTTP_400_BAD_REQUEST)
