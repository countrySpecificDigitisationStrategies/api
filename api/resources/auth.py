from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from api.exceptions import AppException
from api.models import User, Token, EmailConfirmation
from api.services.user import UserService
from api.utils import *


class AuthViewSet(viewsets.GenericViewSet):

    authentication_classes = []
    permission_classes = []

    @action(detail=False, methods=['post'])
    def register(self, request, *args, **kwargs):
        json = request.data

        if not UserService().email_valid(json.get('email')) or not UserService().password_valid(json.get('password')):
            raise ParseError()

        if User.objects.filter(email=json['email']).exists():
            raise AppException(APP_ERROR_REGISTER_EMAIL_EXISTS)

        user = User.objects.create(
            email=json['email'],
            is_active=True
        )
        user.set_password(json['password'])
        user.save()

        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def login(self, request, *args, **kwargs):
        json = request.data

        user = User.objects.filter(email=json.get('email')).first()
        if user:
            if user.check_password(json['password']):
                token = Token.objects.create(user=user)
                json = {'token': token.code}

                user.last_login = timezone.now()
                user.save()

                return Response(json, status=status.HTTP_200_OK)
            else:
                return generate_error_response(APP_ERROR_LOGIN_WRONG_PASSWORD)
        else:
            return generate_error_response(APP_ERROR_LOGIN_DOES_NOT_EXIST)
