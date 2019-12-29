from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator

from rest_framework import mixins, serializers, viewsets

from drf_yasg.utils import swagger_auto_schema

from api.models import Country, Strategy
from api.resources.strategy import StrategySerializer
from api.utils import *

fields = AppList(
    'id',
    'name', 'flag_circle', 'flag_rectangle', 'is_developing_country',
    'strategy',
    'created', 'updated'
)


class CountrySerializer(serializers.ModelSerializer):

    #strategy = serializers.SerializerMethodField('get_strategy', read_only=True)

    class Meta:
        model = Country
        fields = fields
        read_only_fields = fields

    """def get_strategy(self, obj):
        strategy = Strategy.objects.filter(country=obj)
        #return None
        return StrategySerializer(strategy).data"""


class CountryViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = []
    permission_classes = []
