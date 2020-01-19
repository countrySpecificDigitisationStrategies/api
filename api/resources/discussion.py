from rest_framework import serializers

from api.models import BuildingBlock, SituationCategory, Situation, StrategyMeasure
from api.utils import *


fields = AppList(
    'id',
    'title',
    'thread_count'
)


class SituationSerializer(serializers.ModelSerializer):

    thread_count = serializers.SerializerMethodField('get_thread_count', read_only=True)

    class Meta:
        model = Situation
        fields = fields
        read_only_fields = fields

    def get_thread_count(self, obj):
        return obj.situation_threads.all().count()


fields = AppList(
    'id',
    'title',
    'goal_title',
    'thread_count'
)


class SituationCategorySerializer(serializers.ModelSerializer):

    thread_count = serializers.SerializerMethodField('get_thread_count', read_only=True)

    class Meta:
        model = SituationCategory
        fields = fields
        read_only_fields = fields

    def get_thread_count(self, obj):
        return obj.situation_category_threads.all().count()


fields = AppList(
    'id',
    'title',
    'thread_count'
)


class BuildingBlockSerializer(serializers.ModelSerializer):

    thread_count = serializers.SerializerMethodField('get_thread_count', read_only=True)

    class Meta:
        model = BuildingBlock
        fields = fields
        read_only_fields = fields

    def get_thread_count(self, obj):
        return obj.building_block_threads.all().count()


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
        return obj.strategy_measure_threads.all().count()
