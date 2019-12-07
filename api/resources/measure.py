from django.utils.translation import gettext_lazy as _
from rest_framework import mixins, serializers, viewsets

from api.models import Measure
from api.utils import *


fields = AppList(
    'id',
    'goal', 'title', 'description',
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
    filterset_fields = ['goal']
