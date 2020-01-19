from rest_framework import mixins, serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.exceptions import AppException
from api.models import StrategyMeasureComment
from api.permissions import UserIsObjectOwnerPermission
from api.resources.user import UserSerializer
from api.utils import *


fields = AppList(
    'id',
    'user', 'strategy_measure_thread', 'parent', 'description',
    'created', 'updated'
)

post_fields = AppList(
    'strategy_measure_thread', 'parent', 'description',
)


class StrategyMeasureCommentSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)

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
        else:
            permission_classes = [IsAuthenticated, UserIsObjectOwnerPermission]
        return [permission() for permission in permission_classes]
