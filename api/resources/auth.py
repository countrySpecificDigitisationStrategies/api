from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from api.exceptions import AppException
from api.models import User, Country, Token, EmailConfirmation
from api.services.user import UserService
from api.utils import *

from drf_yasg.utils import swagger_auto_schema


class AuthViewSet(viewsets.GenericViewSet):

    authentication_classes = []
    permission_classes = []

    #@swagger_auto_schema(auto_schema=None)
    @action(detail=False, methods=['post'])
    def register(self, request, *args, **kwargs):
        json = request.data

        if not UserService().email_valid(json.get('email')) or not UserService().password_valid(json.get('password')):
            raise ParseError()

        if User.objects.filter(email=json['email']).exists():
            raise AppException(APP_ERROR_REGISTER_EMAIL_EXISTS)

        country = Country.objects.filter(id=json.get('country')).first()

        user = User.objects.create(
            email=json['email'],
            firstname=json.get('firstname'),
            lastname=json.get('lastname'),
            country=country,
            is_active=True
        )
        user.set_password(json['password'])
        user.save()

        return Response(status=status.HTTP_200_OK)

    #@swagger_auto_schema(auto_schema=None)
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
                raise AppException(APP_ERROR_LOGIN_WRONG_PASSWORD)
        else:
            raise AppException(APP_ERROR_LOGIN_DOES_NOT_EXIST)
