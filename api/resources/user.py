from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework import mixins, serializers, viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import User, Token, Country, Board
from api.permissions import UserIsUserPermission
from api.resources.country import CountrySerializer
from api.resources.board import BoardSerializer
from api.utils import *


fields = AppList(
    'id',
    'email', 'country', 'firstname', 'lastname', 'current_country',
    'boards',
    'created', 'updated'
)

patch_fields = AppList(
    'email', 'country', 'firstname', 'lastname', 'current_country'
)


class UserSerializer(serializers.ModelSerializer):

    boards = BoardSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = fields
        read_only_fields = fields - patch_fields

    def to_representation(self, value):
        representation = super().to_representation(value)

        country_id = representation.get('country')
        if country_id:
            country = Country.objects.get(id=country_id)
            representation['country'] = CountrySerializer(country).data

        current_country_id = representation.get('current_country')
        if current_country_id:
            country = Country.objects.get(id=current_country_id)
            representation['current_country'] = CountrySerializer(country).data

        """representation['board'] = None
        boards = Board.objects.all()
        for board in boards:
            if value in board.users.all():
                representation['board'] = BoardSerializer(board).data"""

        return representation


class UserViewSet(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, UserIsUserPermission]

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        return Response(
            data=UserSerializer(request.user, many=False).data,
            status=status.HTTP_200_OK
        )

    @action(detail=False)
    def logout(self, request, *args, **kwargs):
        token = get_object_or_404(Token, code=request.META.get('HTTP_AUTHORIZATION'))
        token.delete()

        return Response(status=status.HTTP_200_OK)
