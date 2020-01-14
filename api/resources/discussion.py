from rest_framework import serializers

from api.models import BuildingBlock, SituationCategory, Situation, StrategyMeasure
from api.utils import *


fields = AppList(
    'id',
    'title'
)


class SituationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Situation
        fields = fields
        read_only_fields = fields


fields = AppList(
    'id',
    'title',
    'goal_title'
)


class SituationCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SituationCategory
        fields = fields
        read_only_fields = fields


fields = AppList(
    'id',
    'title'
)


class BuildingBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildingBlock
        fields = fields
        read_only_fields = fields


fields = AppList(
    'id',
    'measure',
    'thread_count'
)


class StrategyMeasureSerializer(serializers.ModelSerializer):

    thread_count = serializers.SerializerMethodField('get_thread_count', read_only=True)

    class Meta:
        model = StrategyMeasure
        fields = fields
        read_only_fields = fields
        depth = 1

    def get_thread_count(self, obj):
        return obj.threads.all().count()

















"""class DiscussionViewSet(
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
            for index_a, building_block in enumerate(building_blocks):
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
                        data['building_blocks'][index_a]['situations'][index_b]['goals'][index_c]['strategy_measures'] = strategy_measures_data


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
        )"""
