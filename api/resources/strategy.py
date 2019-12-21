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
    'title', 'description', 'is_published',
    'strategy_measure_information',
    'created', 'updated'
)

patch_fields = AppList(
    'title', 'description', 'measures', 'is_published',
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


@method_decorator(name='list',
                  decorator=swagger_auto_schema(operation_id="Get List of all Strategies",
                                                operation_description='some description coming soon',
                                                responses={'200': StrategySerializer(many=True), '400': "Bad Request"}
                                                ))
@method_decorator(name='retrieve',
                  decorator=swagger_auto_schema(operation_id="Get Strategie by ID",
                                                operation_description='some description coming soon.',
                                                responses={'200': StrategySerializer(many=False),
                                                           '404': "Strategy Not Found"}
                                                ))
@method_decorator(name='create',
                  decorator=swagger_auto_schema(operation_id="Create new Strategy",
                                                operation_description='some description coming soon',
                                                responses={'201': StrategySerializer(many=False), '400': "Bad Request"}
                                                ))
@method_decorator(name='update',
                  decorator=swagger_auto_schema(operation_id="Edit specific Strategy",
                                                operation_description='some description coming soon',
                                                responses={'200': StrategySerializer(many=False), '400': "Bad Request"}
                                                ))
@method_decorator(name='destroy',
                  decorator=swagger_auto_schema(operation_id="Delete specific Strategy",
                                                operation_description='some description coming soon',
                                                responses={'204': StrategySerializer(many=False),
                                                           '404': "Strategy Not Found"}
                                                ))
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
