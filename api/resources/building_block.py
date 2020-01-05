from django.shortcuts import get_object_or_404
from rest_framework import mixins, serializers, viewsets

from api.models import BuildingBlock, Situation, Goal, Measure, Strategy
from api.utils import *


fields = AppList(
    'id',
    'title', 'description', 'image',
    'situations',
    'created', 'updated'
)


class BuildingBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildingBlock
        fields = fields
        read_only_fields = fields
        depth = 1


class BuildingBlockViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = BuildingBlock.objects.all()
    serializer_class = BuildingBlockSerializer
    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        strategy_pk = self.kwargs.get('strategy_pk')
        if strategy_pk:
            strategy = get_object_or_404(Strategy, pk=strategy_pk)
            measures = Measure.objects.filter(id__in=strategy.strategy_measures.all()).distinct()
            goals = Goal.objects.filter(measures__in=measures).distinct()
            situations = Situation.objects.filter(goals__in=goals).distinct()
            building_blocks = BuildingBlock.objects.filter(situations__in=situations).distinct()
            return building_blocks
        return BuildingBlock.objects.all()
