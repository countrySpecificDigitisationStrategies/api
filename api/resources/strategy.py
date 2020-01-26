from django.shortcuts import get_object_or_404
from rest_framework import mixins, serializers, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.exceptions import AppException
from api.models import Country, BuildingBlock, SituationCategory, Situation, Measure, Strategy, StrategyMeasure, Board
from api.resources.board import BoardSerializer
from api.resources.building_block import BuildingBlockSerializer
from api.resources.country import CountrySerializer
from api.resources.measure import MeasureSerializer
from api.utils import *


fields = AppList(
    'id',
    'strategy', 'measure',
    'description',
    'created', 'updated'
)

patch_fields = AppList(
    'strategy', 'measure',
    'description'
)


class StrategyMeasureSerializer(serializers.ModelSerializer):

    measure = serializers.SerializerMethodField('get_measure', read_only=True)

    class Meta:
        model = StrategyMeasure
        fields = fields
        read_only_fields = fields - patch_fields

    def get_measure(self, obj):
        if 'request' in self.context:
            request = self.context['request']
            if 'type' in request.GET:
                if request.GET['type'] == 'discussion':
                    return MeasureSerializer(obj.measure, many=False).data
        return obj.measure.id


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













fields = AppList(
    'id',
    'strategy',
    'measure',
    'description',
    'created', 'updated'
)

patch_fields = AppList(
    'id',
    'measure',
    'description'
)


class NStrategyMeasureSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=False, required=False)

    class Meta:
        model = StrategyMeasure
        fields = fields
        read_only_fields = fields - patch_fields


fields = AppList(
    'id',
    'board',
    'title', 'description', 'is_published',
    'strategy_measures',
    'building_blocks', 'situation_categories', 'situations', 'measures',
    'created', 'updated'
)

patch_fields = AppList(
    'board',
    'title', 'description', 'is_published',
    'strategy_measures'
)


class StrategySerializer(serializers.ModelSerializer):

    #board = BoardSerializer(many=False, read_only=False)
    strategy_measures = NStrategyMeasureSerializer(many=True, read_only=False)

    building_blocks = serializers.SerializerMethodField('get_building_blocks', read_only=True)
    situation_categories = serializers.SerializerMethodField('get_situation_categories', read_only=True)
    situations = serializers.SerializerMethodField('get_situations', read_only=True)
    measures = serializers.SerializerMethodField('get_measures', read_only=True)

    class Meta:
        model = Strategy
        fields = fields
        read_only_fields = fields - patch_fields

    def create(self, validated_data):
        strategy_measures_data = validated_data.pop('strategy_measures')
        strategy = super().create(validated_data)
        for strategy_measure_data in strategy_measures_data:
            StrategyMeasure.objects.create(strategy=strategy, **strategy_measure_data)
        return strategy

    def update(self, instance, validated_data):
        strategy_measures_data = validated_data.pop('strategy_measures')
        strategy = super().update(instance, validated_data)
        for strategy_measure_data in strategy_measures_data:
            strategy_measure = StrategyMeasure.objects.filter(id=strategy_measure_data.get('id')).first()
            if strategy_measure:
                strategy_measure.description = strategy_measure_data.get('description')
                strategy_measure.save()
            else:
                StrategyMeasure.objects.create(
                strategy=strategy,
                measure=strategy_measure_data.get('measure'),
                description=strategy_measure_data.get('description')
            )
        return strategy

    def get_building_blocks(self, obj):
        situations = Situation.objects.filter(measures__in=obj.measures.all()).distinct()
        situation_categories = SituationCategory.objects.filter(situations__in=situations.all()).distinct()
        building_blocks = BuildingBlock.objects.filter(situation_categories__in=situation_categories.all()).distinct().values_list('id', flat=True)
        return building_blocks

    def get_situation_categories(self, obj):
        situations = Situation.objects.filter(measures__in=obj.measures.all()).distinct()
        situation_categories = SituationCategory.objects.filter(situations__in=situations.all()).distinct().values_list('id', flat=True)
        return situation_categories

    def get_situations(self, obj):
        situations = Situation.objects.filter(measures__in=obj.measures.all()).distinct().values_list('id', flat=True)
        return situations

    def get_measures(self, obj):
        return [a.id for a in obj.measures.all().distinct()]

    def to_representation(self, value):
        representation = super().to_representation(value)

        board = Board.objects.get(id=value.board.id)
        representation['board'] = BoardSerializer(board).data
        representation['strategy_measures'] = [a['id'] for a in representation['strategy_measures']]

        return representation


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
    filterset_fields = ['board']

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'discussion_tree']:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    """def create(self, request, *args, **kwargs):
        if Strategy.objects.filter(country=request.data.get('country')).exists():
            raise AppException(APP_ERROR_COUNTRY_HAS_STRATEGY)
        return super().create(request, *args, **kwargs)"""

    """def update(self, request, *args, **kwargs):
        if Strategy.objects.filter(country=request.data.get('country')).exists():
            raise AppException(APP_ERROR_COUNTRY_HAS_STRATEGY)
        return super().update(request, *args, **kwargs)"""

    @action(detail=True, methods=['get'])
    def discussion_tree(self, request, pk=None):
        from api.resources.discussion import StrategySerializer, BuildingBlockSerializer, SituationCategorySerializer, SituationSerializer, StrategyMeasureSerializer

        strategy = get_object_or_404(Strategy, pk=pk)

        measures = strategy.measures.all().distinct()
        strategy_measures = strategy.strategy_measures.all().distinct()
        situations = Situation.objects.filter(measures__in=measures.all()).distinct()
        situation_categories = SituationCategory.objects.filter(situations__in=situations.all()).distinct()
        building_blocks = BuildingBlock.objects.filter(situation_categories__in=situation_categories.all()).distinct()

        data = {}
        building_blocks_data = BuildingBlockSerializer(building_blocks, many=True).data
        strategy_data = StrategySerializer(strategy, many=False).data
        data = strategy_data
        data['building_blocks'] = building_blocks_data

        for index_a, building_block in enumerate(building_blocks):
            situation_categories_a = [(s) for s in building_block.situation_categories.all() if s in situation_categories]
            situation_categories_data = SituationCategorySerializer(situation_categories_a, many=True).data
            data['building_blocks'][index_a]['situation_categories'] = situation_categories_data

            for index_b, situation_category in enumerate(situation_categories_a):
                situations_a = [(s) for s in situation_category.situations.all() if s in situations]
                situations_data = SituationSerializer(situations_a, many=True).data
                data['building_blocks'][index_a]['situation_categories'][index_b]['situations'] = situations_data

                for index_c, situation in enumerate(situations_a):
                    sms = None
                    for measure in situation.measures.all():
                        if not sms:
                            sms = measure.strategy_measures.all()
                        else:
                            sms = sms | measure.strategy_measures.all()

                    strategy_measures_data = StrategyMeasureSerializer(sms, many=True).data

                    data['building_blocks'][index_a]['situation_categories'][index_b]['situations'][index_c]['strategy_measures'] = strategy_measures_data

        return Response(data=data)
