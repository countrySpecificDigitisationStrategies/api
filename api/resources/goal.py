from django.utils.translation import gettext_lazy as _
from rest_framework import mixins, serializers, viewsets

from api.models import Goal
from api.utils import *


fields = AppList(
    'id',
    'situation',
    'title', 'description',
    'created', 'updated'
)

class GoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = fields
        read_only_fields = fields


class GoalViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    authentication_classes = []
    permission_classes = []
    filterset_fields = ['situation']