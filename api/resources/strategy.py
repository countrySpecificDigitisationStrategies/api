from rest_framework import mixins, serializers, viewsets

from api.exceptions import AppException
from api.models import Strategy, StrategyMeasureInformation, BuildingBlock, Situation, Goal
from api.permissions import UserIsObjectOwnerPermission
from api.resources.building_block import BuildingBlockSerializer
from api.utils import *


fields = AppList(
    'id',
    'strategy', 'measure', 'description',
    'created', 'updated'
)

patch_fields = AppList(
    'strategy', 'measure', 'description'
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
    'building_blocks',
    'created', 'updated'
)

patch_fields = AppList(
    'country', 'title', 'description', 'is_published',
    'strategy_measure_information'
)

class StrategySerializer(serializers.ModelSerializer):

    strategy_measure_information = StrategyMeasureInformationSerializer(many=True)
    building_blocks = serializers.SerializerMethodField('get_building_blocks', read_only=True)

    class Meta:
        model = Strategy
        fields = fields
        read_only_fields = fields - patch_fields

    def create(self, validated_data):
        country = validated_data.get('country')
        if country:
            exists = Strategy.objects.filter(country=country)
            if exists:
                raise AppException()

        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def get_building_blocks(self, obj):
        measures = obj.measures
        goals = Goal.objects.filter(measures__in=measures.all()).distinct()
        situations = Situation.objects.filter(goals__in=goals.all()).distinct()
        building_blocks = BuildingBlock.objects.filter(situations__in=situations.all()).distinct()
        return BuildingBlockSerializer(building_blocks, many=True).data


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
