from rest_framework import mixins, serializers, viewsets

from api.models import BuildingBlock
from api.utils import *


fields = AppList(
    'id',
    'title', 'description',
    'situation_categories',
    'created', 'updated'
)


class BuildingBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildingBlock
        fields = fields
        read_only_fields = fields


class BuildingBlockViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = BuildingBlock.objects.all()
    serializer_class = BuildingBlockSerializer
    authentication_classes = []
    permission_classes = []
