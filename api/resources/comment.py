from django.utils.translation import gettext_lazy as _
from rest_framework import mixins, serializers, viewsets

from api.models import Comment
from api.utils import *


fields = AppList(
    'id',
    'parent', 'measure', 'description',
    'created', 'updated'
)

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = fields
        read_only_fields = fields


class CommentViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = []
    permission_classes = []
