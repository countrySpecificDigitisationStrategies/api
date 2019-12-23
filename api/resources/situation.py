from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator

from rest_framework import mixins, serializers, viewsets

from drf_yasg.utils import swagger_auto_schema

from api.models import Situation
from api.utils import *

fields = AppList(
    'id',
    'building_block',
    'title', 'description',
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
    filterset_fields = ['building_block']
