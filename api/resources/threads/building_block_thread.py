from rest_framework import mixins, serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import BuildingBlockThread
from api.permissions import UserIsObjectOwnerPermission
from api.resources.comments.building_block_comment import BuildingBlockCommentSerializer
from api.resources.user import UserSerializer, UserNestedSerializer
from api.utils import *


fields = AppList(
    'id',
    'user', 'strategy', 'building_block',
    'title', 'description',
    'is_closed',
    'comment_count',
    'created', 'updated'
)

post_fields = AppList(
    'strategy', 'building_block',
    'title', 'description',
    'is_closed'
)


class BuildingBlockThreadSerializer(serializers.ModelSerializer):

    user = UserNestedSerializer(many=False, read_only=True)
    comment_count = serializers.SerializerMethodField('get_comment_count', read_only=True)

    class Meta:
        model = BuildingBlockThread
        fields = fields
        read_only_fields = fields - post_fields

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def get_comment_count(self, obj):
        return obj.building_block_comments.count()


fields = AppList(
    'id',
    'user', 'strategy', 'building_block',
    'title', 'description',
    'comments',
    'created', 'updated'
)


class BuildingBlockThreadRetrieveSerializer(serializers.ModelSerializer):

    user = UserNestedSerializer(many=False, read_only=True)
    comments = BuildingBlockCommentSerializer(many=True, read_only=True, source='building_block_comments')

    class Meta:
        model = BuildingBlockThread
        fields = fields
        read_only_fields = fields


class BuildingBlockThreadViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):

    queryset = BuildingBlockThread.objects.all()
    serializer_class = BuildingBlockThreadSerializer
    filterset_fields = ['user', 'strategy', 'building_block']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, UserIsObjectOwnerPermission]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
       instance = self.get_object()
       serializer = BuildingBlockThreadRetrieveSerializer(instance)
       return Response(serializer.data)
