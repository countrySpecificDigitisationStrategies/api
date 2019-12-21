from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator

from rest_framework import mixins, serializers, viewsets

from drf_yasg.utils import swagger_auto_schema

from api.models import Comment
from api.utils import *

fields = AppList(
    'id',
    'measure', 'parent', 'description',
    'created', 'updated'
)


class CommentSerializer(serializers.ModelSerializer):
    measure = serializers.CharField(
        help_text=_("Measure to which the comment belongs."),
    )
    parent = serializers.CharField(
        help_text=_("The parent comment.")
    )
    class Meta:
        model = Comment
        fields = fields
        read_only_fields = fields


@method_decorator(name='list',
                  decorator=swagger_auto_schema(operation_id="Get List of all Comments",
                                                operation_description='some description coming soon',
                                                responses={'200': CommentSerializer(many=True), '400': "Bad Request"}
                                                ))
@method_decorator(name='retrieve',
                  decorator=swagger_auto_schema(operation_id="Get Comment by ID",
                                                operation_description='some description coming soon.',
                                                responses={'200': CommentSerializer(many=False),
                                                           '404': "Comment Not Found"}
                                                ))
class CommentViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = []
    permission_classes = []
    filterset_fields = ['measure']
