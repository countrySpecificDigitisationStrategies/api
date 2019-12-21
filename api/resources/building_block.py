from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator

from rest_framework import mixins, serializers, viewsets, status
from rest_framework.decorators import api_view, action

from drf_yasg.utils import swagger_auto_schema

from api.models import BuildingBlock
from api.utils import *


fields = AppList(
    'id',
    'title', 'description', 'image',
    'created', 'updated'
)


class BuildingBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildingBlock
        fields = fields
        read_only_fields = fields


@method_decorator(name='list',
                  decorator=swagger_auto_schema(operation_id="Get List of all Building Blocks",
                                                operation_description='some description coming soon',
                                                 responses={'200': BuildingBlockSerializer(many=True), '400': "Bad Request"}))
@method_decorator(name='retrieve',
                  decorator=swagger_auto_schema(operation_id="Get Building Block by ID",
                                                operation_description='Providing you the Building Block you are looking for.',
                                                responses={'200': BuildingBlockSerializer(many=False), '404': "Building Block Not Found"}))
class BuildingBlockViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = BuildingBlock.objects.all()
    serializer_class = BuildingBlockSerializer
    authentication_classes = []
    permission_classes = []


