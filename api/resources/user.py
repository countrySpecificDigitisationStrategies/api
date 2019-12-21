from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator

from rest_framework import mixins, serializers, viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from api.models import User, Token
from api.permissions import UserIsUserOwnerPermission
from api.utils import *


fields = AppList(
    'id',
    'email', 'country', 'firstname', 'lastname', 'current_country',
    'created', 'updated'
)

patch_fields = AppList(
    'email', 'country', 'firstname', 'lastname', 'current_country',
)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = fields
        read_only_fields = fields - patch_fields


@method_decorator(name='update',
                  decorator=swagger_auto_schema(operation_id="Edit specific User",
                                                operation_description='some description coming soon',
                                                responses={'200': UserSerializer(many=False), '400': "Bad Request"}
                                                ))
@method_decorator(name='destroy',
                  decorator=swagger_auto_schema(operation_id="Delete specific User",
                                                operation_description='some description coming soon',
                                                responses={'204': UserSerializer(many=False), '404': "User Not Found"}
                                                ))
class UserViewSet(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, UserIsUserOwnerPermission]

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        token = get_object_or_404(Token, code=request.META.get('HTTP_AUTHORIZATION'))
        json = UserSerializer(token.user, many=False, context={'request': request}).data
        return Response(json, status.HTTP_200_OK)

    @action(detail=False)
    def logout(self, request, *args, **kwargs):
        token = get_object_or_404(Token, code=request.META.get('HTTP_AUTHORIZATION'))
        token.delete()
        return Response(status.HTTP_200_OK)
