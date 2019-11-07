from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework import mixins, serializers, viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import User, Token
from api.permissions import UserIsUserPermission
from api.utils import *


fields = AppList(
    'id',
    'country', 'email', 'firstname', 'lastname',
    'created', 'updated'
)

patch_fields = AppList(
    'email', 'firstname', 'lastname',
)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = fields
        read_only_fields = fields - patch_fields


class UserViewSet(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, UserIsUserPermission]

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        token = get_object_or_404(Token, identifier=request.META.get('HTTP_AUTHORIZATION'))
        json = UserSerializer(token.user, many=False, context={'request': request}).data
        return Response(json, status.HTTP_200_OK)

    @action(detail=False)
    def logout(self, request, *args, **kwargs):
        token = get_object_or_404(Token, identifier=request.META.get('HTTP_AUTHORIZATION'))
        token.delete()
        return Response(status.HTTP_200_OK)
