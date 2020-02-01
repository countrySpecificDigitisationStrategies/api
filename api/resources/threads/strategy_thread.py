from rest_framework import mixins, serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import StrategyThread
from api.permissions import UserIsObjectOwnerPermission
from api.resources.comments.strategy_comment import StrategyCommentSerializer
from api.resources.user import UserSerializer, UserNestedSerializer
from api.utils import *


fields = AppList(
    'id',
    'user', 'strategy',
    'title', 'description',
    'is_closed',
    'comment_count',
    'created', 'updated'
)

post_fields = AppList(
    'strategy',
    'title', 'description',
    'is_closed',
)


class StrategyThreadSerializer(serializers.ModelSerializer):

    user = UserNestedSerializer(many=False, read_only=True)
    comment_count = serializers.SerializerMethodField('get_comment_count', read_only=True)

    class Meta:
        model = StrategyThread
        fields = fields
        read_only_fields = fields - post_fields

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def get_comment_count(self, obj):
        return obj.strategy_comments.count()


fields = AppList(
    'id',
    'user', 'strategy',
    'title', 'description',
    'comments',
    'created', 'updated'
)


class StrategyThreadRetrieveSerializer(serializers.ModelSerializer):

    user = UserNestedSerializer(many=False, read_only=True)
    comments = StrategyCommentSerializer(many=True, read_only=True, source='strategy_comments')

    class Meta:
        model = StrategyThread
        fields = fields
        read_only_fields = fields


class StrategyThreadViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):

    queryset = StrategyThread.objects.all()
    serializer_class = StrategyThreadSerializer
    filterset_fields = ['user', 'strategy']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, UserIsObjectOwnerPermission]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
       instance = self.get_object()
       serializer = StrategyThreadRetrieveSerializer(instance)
       return Response(serializer.data)
