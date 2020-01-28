from rest_framework import mixins, serializers, viewsets

from api.models import Board
from api.resources.country import CountrySerializer
from api.resources.user import UserSerializer
from api.utils import *


fields = AppList(
    'id',
    'country', 'users',
    'created', 'updated'
)


class BoardSerializer(serializers.ModelSerializer):

    country = CountrySerializer(many=False, read_only=True)
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = fields
        read_only_fields = fields


class BoardViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
