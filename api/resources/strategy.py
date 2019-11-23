from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from rest_framework import mixins, serializers, viewsets, status
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

    """def get_queryset(self):
        return Strategy.objects.filter(user=self.request.user)"""

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        elif self.action == 'destroy':
            permission_classes = [UserIsObjectOwnerPermission]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        count = Strategy.objects.filter(user=request.user).count()
        if count >= 1:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    """@permission_classes([])
    @authentication_classes([])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @permission_classes([])
    @authentication_classes([])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)"""

    """@authentication_classes([])
    @permission_classes([AllowAny])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @permission_classes([IsAuthenticated, UserIsObjectOwnerPermission])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)"""
