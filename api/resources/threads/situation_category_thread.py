from rest_framework import mixins, serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import SituationCategoryThread
from api.permissions import UserIsObjectOwnerPermission
from api.resources.comments.situation_category_comment import SituationCategoryCommentSerializer
from api.resources.user import UserSerializer
from api.utils import *


fields = AppList(
    'id',
    'user', 'strategy', 'situation_category',
    'title', 'description',
    'is_closed',
    'comment_count',
    'created', 'updated'
)

post_fields = AppList(
    'strategy', 'situation_category',
    'title', 'description',
    'is_closed'
)


class SituationCategoryThreadSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)
    comment_count = serializers.SerializerMethodField('get_comment_count', read_only=True)

    class Meta:
        model = SituationCategoryThread
        fields = fields
        read_only_fields = fields - post_fields

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def get_comment_count(self, obj):
        return obj.situation_category_comments.count()


fields = AppList(
    'id',
    'user', 'strategy', 'situation_category',
    'title', 'description',
    'situation_category_comments',
    'created', 'updated'
)


class SituationCategoryThreadRetrieveSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)
    situation_category_comments = SituationCategoryCommentSerializer(many=True, read_only=True)

    class Meta:
        model = SituationCategoryThread
        fields = fields
        read_only_fields = fields


class SituationCategoryThreadViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):

    queryset = SituationCategoryThread.objects.all()
    serializer_class = SituationCategoryThreadSerializer
    filterset_fields = ['user', 'strategy', 'situation_category']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, UserIsObjectOwnerPermission]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
       instance = self.get_object()
       serializer = SituationCategoryThreadRetrieveSerializer(instance)
       return Response(serializer.data)
