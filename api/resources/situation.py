from rest_framework import mixins, serializers, viewsets

from api.models import Situation
from api.utils import *

fields = AppList(
    'id',
    'situation_category',
    'title', 'description',
    'measures',
    'created', 'updated'
)


class SituationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Situation
        fields = fields
        read_only_fields = fields


class SituationViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = Situation.objects.all()
    serializer_class = SituationSerializer
    authentication_classes = []
    permission_classes = []
    filterset_fields = ['situation_category']
