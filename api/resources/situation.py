from django.shortcuts import get_object_or_404
from rest_framework import mixins, serializers, viewsets

from api.models import BuildingBlock, Situation, Goal, Measure, Strategy
from api.utils import *

fields = AppList(
    'id',
    'building_block',
    'title', 'description',
    'goals',
    'created', 'updated'
)


class SituationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situation
        fields = fields
        read_only_fields = fields
        depth = 1


class SituationViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = Situation.objects.all()
    serializer_class = SituationSerializer
    authentication_classes = []
    permission_classes = []
    filterset_fields = ['building_block']

    def get_queryset(self):
        building_block_pk = self.kwargs.get('building_block_pk')
        strategy_pk = self.kwargs.get('strategy_pk')
        if strategy_pk:
            strategy = get_object_or_404(Strategy, pk=strategy_pk)
            measures = Measure.objects.filter(id__in=strategy.strategy_measures.all()).distinct()
            goals = Goal.objects.filter(measures__in=measures).distinct()
            situations = Situation.objects.filter(goals__in=goals).distinct()
            return situations
            """building_blocks = BuildingBlock.objects.filter(situations__in=situations).distinct()

            building_block = BuildingBlock.objects.get(id=building_block_pk)
            building_block_situations = building_block.situations.all()

            situations = [(s) for s in situations if s in building_block_situations]
            situations_ids = [situation.id for situation in situations]
            return Situation.objects.filter(id__in=situations_ids)"""
        return Situation.objects.all()
