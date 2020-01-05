from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import BuildingBlock, Situation, Goal, Strategy, StrategyMeasure, Measure
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


fields = AppList(
    'id',
    'building_block',
    'title', 'description',
    'goals',
    'created', 'updated'
)


class SituationSerializer(serializers.ModelSerializer):

    goals = GoalSerializer(many=True, read_only=True)

    class Meta:
        model = Situation
        fields = fields
        read_only_fields = fields


fields = AppList(
    'id',
    'title', 'description', 'image',
    'situations',
    'created', 'updated'
)


class BuildingBlockSerializer(serializers.ModelSerializer):

    situations = SituationSerializer(many=True, read_only=True)

    class Meta:
        model = BuildingBlock
        fields = fields
        read_only_fields = fields

















class DiscussionViewSet(
    viewsets.GenericViewSet
):

    authentication_classes = []
    permission_classes = []

    @action(detail=False, methods=['get'])
    def tree(self, request, *args, **kwargs):
        data = {}

        strategy = request.GET.get('strategy')
        if strategy:
            strategy = Strategy.objects.get(id=strategy)
            strategy_measures = StrategyMeasure.objects.filter(strategy=strategy)
            #strategy_measures_data = StrategyMeasureSerializer(strategy_measures, many=True).data
            #data['strategy_measures'] = strategy_measures_data

            measures = [strategy_measure.measure.id for strategy_measure in strategy_measures]
            measures_ids = Measure.objects.filter(id__in=measures).distinct()

            goals = Goal.objects.filter(measures__in=measures_ids).distinct()
            print(goals)

            situations = Situation.objects.filter(goals__in=goals).distinct()
            print(situations)

            building_blocks = BuildingBlock.objects.filter(situations__in=situations).distinct()
            print(building_blocks)
            building_blocks_data = BuildingBlockSerializer(building_blocks, many=True).data
            data['building_blocks'] = building_blocks_data

            print('loop')
            """for index_a, building_block in enumerate(building_blocks):
                situations_a = [(s) for s in building_block.situations.all() if s in situations]
                situations_data = SituationSerializer(situations_a, many=True).data
                data['building_blocks'][index_a]['situations'] = situations_data

                for index_b, situation in enumerate(situations):
                    print(index_a)
                    print(index_b)
                    goals_a = [(g) for g in situation.goals.all() if g in goals]
                    goals_data = GoalSerializer(goals_a, many=True).data
                    data['building_blocks'][index_a]['situations'][index_b]['goals'] = goals_data

                    for index_c, goal in enumerate(goals):
                        measures = goal.measures.all()
                        strategy_measures = StrategyMeasure.objects.filter(measure__in=measures)
                        strategy_measures_data = StrategyMeasureSerializer(strategy_measures, many=True).data
                        data['building_blocks'][index_a]['situations'][index_b]['goals'][index_c]['strategy_measures'] = strategy_measures_data"""


        else:
            building_blocks = BuildingBlock.objects.all()
            building_blocks_data = BuildingBlockSerializer(building_blocks, many=True).data
            data['building_blocks'] = building_blocks_data

            for index_a, building_block in enumerate(building_blocks):
                situations = building_block.situations.all()
                situations_data = SituationSerializer(situations, many=True).data
                data['building_blocks'][index_a]['situations'] = situations_data

                for index_b, situation in enumerate(situations):
                    goals = situation.goals.all()
                    goals_data = GoalSerializer(goals, many=True).data
                    data['building_blocks'][index_a]['situations'][index_b]['goals'] = goals_data

                    for index_c, goal in enumerate(goals):
                        measures = goal.measures.all()
                        strategy_measures = StrategyMeasure.objects.filter(measure__in=measures)
                        strategy_measures_data = StrategyMeasureSerializer(strategy_measures, many=True).data
                        data['building_blocks'][index_a]['situations'][index_b]['goals'][index_c]['strategy_measures'] = strategy_measures_data

        return Response(
            data=data
        )
