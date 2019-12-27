from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator

from rest_framework import mixins, serializers, viewsets
from drf_yasg.utils import swagger_auto_schema

from api.exceptions import AppException
from api.models import Strategy, StrategyMeasureInformation
from api.permissions import UserIsObjectOwnerPermission
from api.utils import *

fields = AppList(
    'id',
    'measure', 'strategy', 'description',
    'created', 'updated'
)

patch_fields = AppList(
    'measure', 'strategy', 'description',
)


class StrategyMeasureInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategyMeasureInformation
        fields = fields
        read_only_fields = fields - patch_fields


fields = AppList(
    'id',
    'user',
    'country', 'title', 'description', 'is_published',
    'strategy_measure_information',
    'created', 'updated'
)

patch_fields = AppList(
    'country', 'title', 'description', 'measures', 'is_published',
)


class StrategySerializer(serializers.ModelSerializer):
    strategy_measure_information = StrategyMeasureInformationSerializer(many=True, read_only=True)

    class Meta:
        model = Strategy
        fields = fields
        read_only_fields = fields - patch_fields
        # depth = 1

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
    filterset_fields = ['country']

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
