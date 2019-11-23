from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from rest_framework import mixins, serializers, viewsets, status
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.exceptions import AppException
from api.models import Strategy
from api.permissions import UserIsObjectOwnerPermission
from api.utils import *

from rest_framework.permissions import IsAuthenticated, AllowAny



fields = AppList(
    'id',
    'user',
    'title', 'description', 'measures', 'is_published',
    'created', 'updated'
)

patch_fields = AppList(
    'title', 'description', 'measures', 'is_published',
)


class StrategySerializer(serializers.ModelSerializer):

    class Meta:
        model = Strategy
        fields = fields
        read_only_fields = fields - patch_fields

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class StrategyViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    queryset = Strategy.objects.all()
    serializer_class = StrategySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        else:
            permission_classes = [UserIsObjectOwnerPermission]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        count = Strategy.objects.filter(user=request.user).count()
        if count >= 1:
            raise AppException()
        return super().create(request, *args, **kwargs)
