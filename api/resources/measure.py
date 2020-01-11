from rest_framework import mixins, serializers, viewsets

from api.models import Measure
from api.utils import *


fields = AppList(
    'id',
    'situation',
    'title', 'description',
    'created', 'updated'
)


class MeasureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measure
        fields = fields
        read_only_fields = fields


class MeasureViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer
    authentication_classes = []
    permission_classes = []
    filterset_fields = ['situation']
