from rest_framework import mixins, serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.exceptions import AppException
from api.models import BuildingBlockComment
from api.permissions import UserIsObjectOwnerPermission
from api.resources.user import UserSerializer, UserNestedSerializer
from api.utils import *


fields = AppList(
    'id',
    'user', 'building_block_thread', 'parent', 'description',
    'created', 'updated'
)

post_fields = AppList(
    'building_block_thread', 'parent', 'description',
)


class BuildingBlockCommentSerializer(serializers.ModelSerializer):

    user = UserNestedSerializer(many=False, read_only=True)

    class Meta:
        model = BuildingBlockComment
        fields = fields
        read_only_fields = fields - post_fields

    def create(self, validated_data):
        parent = validated_data.get('parent')
        if parent:
            building_block_comment = BuildingBlockComment.objects.get(id=parent.id)
            if building_block_comment.parent:
                raise AppException()

        validated_data['user'] = self.context['request'].user

        return super().create(validated_data)


class BuildingBlockCommentViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    queryset = BuildingBlockComment.objects.all()
    serializer_class = BuildingBlockCommentSerializer
    filterset_fields = ['user', 'building_block_thread']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, UserIsObjectOwnerPermission]
        return [permission() for permission in permission_classes]
