from uuid import uuid4

from django.utils import timezone
from django.utils.decorators import method_decorator
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from api.exceptions import AppException
from api.models import User, Token, EmailConfirmation
from api.utils import *


class AuthViewSet(viewsets.ViewSet):

    authentication_classes = []
    permission_classes = []

    def generate_token(self, user):
        return Token.objects.create(
            user=user,
            identifier=str(uuid4()),
        )

    @method_decorator(
        name='register',
        decorator=swagger_auto_schema(
            operation_description='Register user',
            operation_id='register',
            operation_summary='Register',
            request_body=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'email': openapi.Schema(title='email', type=openapi.TYPE_STRING),
                    'password': openapi.Schema(title='password', type=openapi.TYPE_STRING),
                }, required=['email', 'password']
            ),
            responses={
                '200': 'OK',
                '400': 'Bad Request'
            }
        )
    )
    @action(detail=False, methods=['post'])
    def register(self, request, *args, **kwargs):
        json = request.data

        if 'email' not in json or 'password' not in json:
            raise ParseError()

        user_exists = User.objects.filter(email=json['email']).exists()
        if user_exists:
            raise AppException(APP_ERROR_REGISTER_EMAIL_EXISTS)

        # if not UserService().is_password_valid(json['password']):
            #raise ParseError()

        user = User.objects.create(
            country=AFGHANISTAN,
            email=json['email'],
            is_active=True  # temp
        )
        user.set_password(json['password'])
        user.save()

        return Response(status=status.HTTP_200_OK)

    '''@action(detail=False, methods=['post'])
    def activate(self, request, *args, **kwargs):
        json = request.data

        if 'identifier' not in json:
            raise ParseError()

        threshold = timezone.now() - timezone.timedelta(hours=24)

        token = EmailConfirmation.objects.filter(identifier=json['identifier'], created__gt=threshold).first()
        if token:
            user = token.user
            if user.is_active:
                raise AppException(APP_ERROR_ACTIVATE_ALREADY_ACTIVE)
            else:
                user.is_active = True
                user.save()

                return Response(status=status.HTTP_200_OK)
        else:
            raise AppException(APP_ERROR_ACTIVATE_INVALID_IDENTIFIER)'''

    @method_decorator(
        name='login',
        decorator=swagger_auto_schema(
            operation_description='Login user',
            operation_id='login',
            operation_summary='Login',
            request_body=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'email': openapi.Schema(title='email', type=openapi.TYPE_STRING),
                    'password': openapi.Schema(title='password', type=openapi.TYPE_STRING),
                }, required=['email', 'password']
            ),
            responses={
                '200': 'OK',
                '400': 'Bad Request'
            }
        )
    )
    @action(detail=False, methods=['post'])
    def login(self, request, *args, **kwargs):
        json = request.data

        if 'email' not in json or 'password' not in json:
            raise ParseError()

        user = User.objects.filter(email=json['email']).first()
        if user:
            if not user.is_active:
                return generate_error_response(APP_ERROR_LOGIN_NOT_ACTIVE)

            if user.check_password(json['password']):
                token = self.generate_token(user)
                json = {'token': token.identifier}

                user.last_login = timezone.now()
                user.save()

                return Response(json, status=status.HTTP_200_OK)
            else:
                return generate_error_response(APP_ERROR_LOGIN_WRONG_PASSWORD)
        else:
            return generate_error_response(APP_ERROR_LOGIN_DOES_NOT_EXIST)
