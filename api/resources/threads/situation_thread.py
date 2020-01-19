from rest_framework import mixins, serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import SituationThread
from api.permissions import UserIsObjectOwnerPermission
from api.resources.comments.situation_comment import SituationCommentSerializer
from api.resources.user import UserSerializer
from api.utils import *


fields = AppList(
    'id',
    'user', 'strategy', 'situation',
    'title', 'description',
    'comment_count',
    'created', 'updated'
)

post_fields = AppList(
    'strategy', 'situation',
    'title', 'description',
)


class SituationThreadSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)
    comment_count = serializers.SerializerMethodField('get_comment_count', read_only=True)

    class Meta:
        model = SituationThread
        fields = fields
        read_only_fields = fields - post_fields

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def get_comment_count(self, obj):
        return obj.situation_comments.count()


fields = AppList(
    'id',
    'user', 'strategy', 'situation',
    'title', 'description',
    'situation_comments',
    'created', 'updated'
)


class SituationThreadRetrieveSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)
    situation_comments = SituationCommentSerializer(many=True, read_only=True)

    class Meta:
        model = SituationThread
        fields = fields
        read_only_fields = fields


class SituationThreadViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):

    queryset = SituationThread.objects.all()
    serializer_class = SituationThreadSerializer
    filterset_fields = ['user', 'strategy', 'situation']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, UserIsObjectOwnerPermission]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
       instance = self.get_object()
       serializer = SituationThreadRetrieveSerializer(instance)
       return Response(serializer.data)
