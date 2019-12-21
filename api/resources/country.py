from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator

from rest_framework import mixins, serializers, viewsets

from drf_yasg.utils import swagger_auto_schema

from api.models import Country
from api.utils import *

fields = AppList(
    'id',
    'name', 'flag_circle', 'flag_rectangle',
    'created', 'updated'
)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = fields
        read_only_fields = fields


@method_decorator(name='list',
                  decorator=swagger_auto_schema(operation_id="Get List of all Countries",
                                                operation_description='some description coming soon',
                                                responses={'200': CountrySerializer(many=True), '400': "Bad Request"}
                                                ))
@method_decorator(name='retrieve',
                  decorator=swagger_auto_schema(operation_id="Get Country by ID",
                                                operation_description='some description coming soon.',
                                                responses={'200': CountrySerializer(many=False),
                                                           '404': "Country Not Found"}
                                                ))
class CountryViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = []
    permission_classes = []
