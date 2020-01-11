from rest_framework import mixins, serializers, viewsets

from api.models import SituationCategory
from api.utils import *


fields = AppList(
    'id',
    'building_block',
    'title', 'description',
    'goal_title', 'goal_description',
    'situations',
    'created', 'updated'
)


class SituationCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SituationCategory
        fields = fields
        read_only_fields = fields


class SituationCategoryViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = SituationCategory.objects.all()
    serializer_class = SituationCategorySerializer
    authentication_classes = []
    permission_classes = []
    filterset_fields = ['building_block']
