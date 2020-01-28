from rest_framework import mixins, serializers, viewsets

from api.models import Board
from api.utils import *


fields = AppList(
    'id',
    'country', 'users',
    'created', 'updated'
)


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = fields
        read_only_fields = fields
        depth = 1


class BoardViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
