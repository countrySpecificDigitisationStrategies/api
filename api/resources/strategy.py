from django.shortcuts import get_object_or_404
from rest_framework import mixins, serializers, viewsets

from api.exceptions import AppException
from api.models import BuildingBlock, Situation, Goal, Measure, Strategy, StrategyMeasure
from api.permissions import UserIsObjectOwnerPermission
from api.resources.building_block import BuildingBlockSerializer
from api.resources.country import CountrySerializer
from api.resources.thread import ThreadSerializer
from api.utils import *


fields = AppList(
    'id',
    'strategy', 'measure', 'description',
    'threads',
    'created', 'updated'
)

patch_fields = AppList(
    'strategy', 'measure', 'description'
)


class StrategyMeasureSerializer(serializers.ModelSerializer):

    threads = ThreadSerializer(many=True, read_only=True)

    class Meta:
        model = StrategyMeasure
        fields = fields
        read_only_fields = fields - patch_fields


class StrategyMeasureViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = StrategyMeasure.objects.all()
    serializer_class = StrategyMeasureSerializer
    authentication_classes = []
    permission_classes = []
    filterset_fields = ['strategy', 'measure']

    def get_queryset(self):
        goal_pk = self.kwargs.get('goal_pk')
        situation_pk = self.kwargs.get('situation_pk')
        building_block_pk = self.kwargs.get('building_block_pk')
        strategy_pk = self.kwargs.get('strategy_pk')
        if strategy_pk:
            strategy = get_object_or_404(Strategy, pk=strategy_pk)
            measures = Measure.objects.filter(id__in=strategy.strategy_measures.all()).distinct()
            goals = Goal.objects.filter(measures__in=measures).distinct()

            goal = Goal.objects.get(id=goal_pk)
            goal_measures = goal.measures.all()

            #goals_measures = [list((goal.measures.all())) for goal in goals]
            goals_measures = []
            for goal in goals:
                a = list(goal.measures.all())
                for b in a:
                    goals_measures.append(b)

            #goals_measures_ids = [measure.id for measure in goals_measures]

            new_measures = [measure for measure in goals_measures if measure in list(goal_measures)]

            strategy_measures = StrategyMeasure.objects.filter(measure__in=new_measures).distinct()

            return strategy_measures
        return StrategyMeasure.objects.all()


fields = AppList(
    'id',
    'user',
    'country', 'title', 'description', 'is_published',
    'strategy_measures',
    'building_blocks',
    'created', 'updated'
)

patch_fields = AppList(
    'country', 'title', 'description', 'is_published',
    'strategy_measures'
)


class StrategySerializer(serializers.ModelSerializer):

    #user = UserSerializer(many=False, read_only=True)
    country = CountrySerializer(many=False, read_only=True)
    strategy_measures = StrategyMeasureSerializer(many=True, read_only=False)
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
