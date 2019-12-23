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


class BuildingBlockViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = BuildingBlock.objects.all()
    serializer_class = BuildingBlockSerializer
    authentication_classes = []
    permission_classes = []


