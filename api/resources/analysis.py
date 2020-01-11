from rest_framework import mixins, serializers, viewsets

from api.models import Analysis
from api.utils import *

fields = AppList(
    'id',
    'country',
    'title', 'description',
    'created', 'updated'
)


class AnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Analysis
        fields = fields
        read_only_fields = fields
        depth = 1


class AnalysisViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer
    authentication_classes = []
    permission_classes = []
    filterset_fields = ['country']
