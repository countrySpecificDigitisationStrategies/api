from rest_framework import mixins, serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.exceptions import AppException
from api.models import StrategyMeasureComment
from api.permissions import UserIsObjectOwnerPermission, UserIsObjectOwnerOrModeratorPermission
from api.resources.user import UserSerializer, UserNestedSerializer
from api.utils import *


fields = AppList(
    'id',
    'user', 'strategy_measure_thread', 'parent', 'description',
    'is_country_representative',
    'created', 'updated'
)

post_fields = AppList(
    'strategy_measure_thread', 'parent', 'description',
)


class StrategyMeasureCommentSerializer(serializers.ModelSerializer):

    user = UserNestedSerializer(many=False, read_only=True)
    is_country_representative = serializers.SerializerMethodField('get_is_country_representative', read_only=True)

    class Meta:
        model = StrategyMeasureComment
        fields = fields
        read_only_fields = fields - post_fields

    def create(self, validated_data):
        parent = validated_data.get('parent')
        if parent:
            strategy_measure_comment = StrategyMeasureComment.objects.get(id=parent.id)
            if strategy_measure_comment.parent:
                raise AppException()

        validated_data['user'] = self.context['request'].user

        return super().create(validated_data)

    def get_is_country_representative(self, obj):
        return obj.user in obj.strategy_measure_thread.strategy_measure.strategy.board.users.all()


class StrategyMeasureCommentViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    queryset = StrategyMeasureComment.objects.all()
    serializer_class = StrategyMeasureCommentSerializer
    filterset_fields = ['user', 'strategy_measure_thread']

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
