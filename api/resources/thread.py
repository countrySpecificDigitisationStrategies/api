from rest_framework import mixins, serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import Thread
from api.permissions import UserIsObjectOwnerPermission
from api.utils import *


fields = AppList(
    'id',
    'user', 'strategy_measure',
    'title', 'description',
    'created', 'updated'
)

post_fields = AppList(
    'strategy_measure',
    'title', 'description',
)


class ThreadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thread
        fields = fields
        read_only_fields = fields - post_fields

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class ThreadViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):

    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    filterset_fields = ['user', 'strategy_measure']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, UserIsObjectOwnerPermission]
        return [permission() for permission in permission_classes]
