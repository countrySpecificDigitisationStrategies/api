from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator

from rest_framework import mixins, serializers, viewsets

from drf_yasg.utils import swagger_auto_schema

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


@method_decorator(name='list',
                  decorator=swagger_auto_schema(operation_id="Get List of all Measures",
                                                operation_description='some description coming soon',
                                                responses={'200': MeasureSerializer(many=True), '400': "Bad Request"}
                                                ))
@method_decorator(name='retrieve',
                  decorator=swagger_auto_schema(operation_id="Get Measure by ID",
                                                operation_description='some description coming soon.',
                                                responses={'200': MeasureSerializer(many=False),
                                                           '404': "Measure Not Found"}
                                                ))
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
