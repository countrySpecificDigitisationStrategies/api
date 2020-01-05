from rest_framework import mixins, serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.exceptions import AppException
from api.models import Comment
from api.permissions import UserIsObjectOwnerPermission
from api.resources.user import UserSerializer
from api.utils import *


fields = AppList(
    'id',
    'user', 'thread', 'parent', 'description',
    'created', 'updated'
)

post_fields = AppList(
    'thread', 'parent', 'description',
)


class CommentSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Comment
        fields = fields
        read_only_fields = fields - post_fields

    def create(self, validated_data):
        parent = validated_data.get('parent')
        if parent:
            comment = Comment.objects.get(id=parent.id)
            if comment.parent:
                raise AppException

        validated_data['user'] = self.context['request'].user

        return super().create(validated_data)


class CommentViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_fields = ['user', 'thread']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, UserIsObjectOwnerPermission]
        return [permission() for permission in permission_classes]
