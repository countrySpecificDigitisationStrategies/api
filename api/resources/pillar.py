from django.utils.translation import gettext_lazy as _
from rest_framework import mixins, serializers, viewsets
from rest_framework.decorators import action, authentication_classes, permission_classes

from api.models import Pillar
from api.permissions import UserIsObjectOwnerPermission
from api.utils import *


fields = AppList(
    'id',
    'title', 'description', 'image',
    'created', 'updated'
)

class PillarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pillar
        fields = fields
        read_only_fields = fields


class PillarViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = Pillar.objects.all()
    serializer_class = PillarSerializer
    authentication_classes = []
    permission_classes = []
