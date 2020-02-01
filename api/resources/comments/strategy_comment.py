from rest_framework import mixins, serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.exceptions import AppException
from api.models import StrategyComment
from api.permissions import UserIsObjectOwnerPermission
from api.resources.user import UserSerializer, UserNestedSerializer
from api.utils import *


fields = AppList(
    'id',
    'user', 'strategy_thread', 'parent', 'description',
    'created', 'updated'
)

post_fields = AppList(
    'strategy_thread', 'parent', 'description',
)


class StrategyCommentSerializer(serializers.ModelSerializer):

    user = UserNestedSerializer(many=False, read_only=True)

    class Meta:
        model = StrategyComment
        fields = fields
        read_only_fields = fields - post_fields

    def create(self, validated_data):
        parent = validated_data.get('parent')
        if parent:
            strategy_comment = StrategyComment.objects.get(id=parent.id)
            if strategy_comment.parent:
                raise AppException()

        validated_data['user'] = self.context['request'].user

        return super().create(validated_data)


class StrategyCommentViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    queryset = StrategyComment.objects.all()
    serializer_class = StrategyCommentSerializer
    filterset_fields = ['user', 'strategy_thread']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, UserIsObjectOwnerPermission]
        return [permission() for permission in permission_classes]
