from rest_framework import mixins, serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import StrategyMeasureThread
from api.permissions import UserIsObjectOwnerPermission, UserIsObjectOwnerOrModeratorPermission
from api.resources.comments.strategy_measure_comment import StrategyMeasureCommentSerializer
from api.resources.user import UserSerializer, UserNestedSerializer
from api.utils import *


fields = AppList(
    'id',
    'user', 'strategy_measure',
    'title', 'description',
    'is_closed',
    'comment_count',
    'is_country_representative',
    'created', 'updated'
)

post_fields = AppList(
    'strategy_measure',
    'title', 'description',
    'is_closed'
)


class StrategyMeasureThreadSerializer(serializers.ModelSerializer):

    user = UserNestedSerializer(many=False, read_only=True)
    comment_count = serializers.SerializerMethodField('get_comment_count', read_only=True)
    is_country_representative = serializers.SerializerMethodField('get_is_country_representative', read_only=True)

    class Meta:
        model = StrategyMeasureThread
        fields = fields
        read_only_fields = fields - post_fields

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def get_comment_count(self, obj):
        return obj.strategy_measure_comments.count()

    def get_is_country_representative(self, obj):
        return obj.user in obj.strategy_measure.strategy.board.users.all()


fields = AppList(
    'id',
    'user', 'strategy_measure',
    'title', 'description',
    'is_closed',
    'comments',
    'is_country_representative',
    'created', 'updated'
)


class StrategyMeasureThreadRetrieveSerializer(StrategyMeasureThreadSerializer):

    comments = StrategyMeasureCommentSerializer(many=True, read_only=True, source='strategy_measure_comments')

    class Meta:
        model = StrategyMeasureThread
        fields = fields
        read_only_fields = fields


class StrategyMeasureThreadViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    queryset = StrategyMeasureThread.objects.all()
    serializer_class = StrategyMeasureThreadSerializer
    filterset_fields = ['user', 'strategy_measure']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        elif self.action in ['partial_update']:
            permission_classes = [IsAuthenticated, UserIsObjectOwnerOrModeratorPermission]
        elif self.action in ['destroy']:
            permission_classes = [IsAuthenticated, UserIsObjectOwnerOrModeratorPermission]
        else:
            permission_classes = [IsAuthenticated, UserIsObjectOwnerPermission]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
       instance = self.get_object()
       serializer = StrategyMeasureThreadRetrieveSerializer(instance)
       return Response(serializer.data)
