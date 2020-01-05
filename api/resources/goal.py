from django.shortcuts import get_object_or_404
from rest_framework import mixins, serializers, viewsets

from api.models import BuildingBlock, Situation, Goal, Measure, Strategy, StrategyMeasure
from api.resources.strategy import StrategyMeasureSerializer
from api.utils import *

fields = AppList(
    'id',
    'situation',
    'title', 'description',
    'strategy_measures',
    'created', 'updated'
)


class GoalSerializer(serializers.ModelSerializer):

    strategy_measures = serializers.SerializerMethodField()

    class Meta:
        model = Goal
        fields = fields
        read_only_fields = fields

    def get_strategy_measures(self, obj):
        measures = obj.measures.all()
        strategy_measures = StrategyMeasure.objects.filter(measure__in=measures)
        return StrategyMeasureSerializer(strategy_measures, many=True).data


class GoalViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    authentication_classes = []
    permission_classes = []
    filterset_fields = ['situation']

    def get_queryset(self):
        situation_pk = self.kwargs.get('situation_pk')
        building_block_pk = self.kwargs.get('building_block_pk')
        strategy_pk = self.kwargs.get('strategy_pk')
        if strategy_pk:
            strategy = get_object_or_404(Strategy, pk=strategy_pk)
            measures = Measure.objects.filter(id__in=strategy.strategy_measures.all()).distinct()
            goals = Goal.objects.filter(measures__in=measures).distinct()
            return goals
        return Goal.objects.all()
