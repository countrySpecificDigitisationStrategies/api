from rest_framework import mixins, serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import StrategyMeasureThread
from api.permissions import UserIsObjectOwnerPermission
from api.resources.comments.strategy_measure_comment import StrategyMeasureCommentSerializer
from api.resources.user import UserSerializer
from api.utils import *


fields = AppList(
    'id',
    'user', 'strategy_measure',
    'title', 'description',
    'comment_count',
    'created', 'updated'
)

post_fields = AppList(
    'strategy_measure',
    'title', 'description',
)


class StrategyMeasureThreadSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)
    comment_count = serializers.SerializerMethodField('get_comment_count', read_only=True)

    class Meta:
        model = StrategyMeasureThread
        fields = fields
        read_only_fields = fields - post_fields

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def get_comment_count(self, obj):
        return obj.strategy_measure_comments.count()


fields = AppList(
    'id',
    'user', 'strategy_measure',
    'title', 'description',
    'strategy_measure_comments',
    'created', 'updated'
)

post_fields = AppList(
    'strategy_measure',
    'title', 'description',
)


class StrategyMeasureThreadRetrieveSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)
    strategy_measure_comments = StrategyMeasureCommentSerializer(many=True, read_only=True)

    class Meta:
        model = StrategyMeasureThread
        fields = fields
        read_only_fields = fields - post_fields

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class StrategyMeasureThreadViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):

    queryset = StrategyMeasureThread.objects.all()
    serializer_class = StrategyMeasureThreadSerializer
    filterset_fields = ['user', 'strategy_measure']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, UserIsObjectOwnerPermission]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
       instance = self.get_object()
       serializer = StrategyMeasureThreadRetrieveSerializer(instance)
       return Response(serializer.data)
