from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import BuildingBlock, Situation, Goal
from api.resources.building_block import BuildingBlockSerializer
from api.resources.situation import SituationSerializer
from api.resources.goal import GoalSerializer
from api.utils import *


class DiscussionViewSet(
    viewsets.GenericViewSet
):

    authentication_classes = []
    permission_classes = []

    @action(detail=False, methods=['get'])
    def tree(self, request, *args, **kwargs):
        data = {}

        building_blocks = BuildingBlock.objects.all()
        building_blocks_data = BuildingBlockSerializer(building_blocks, many=True).data
        data['building_blocks'] = building_blocks_data

        for index_a, building_block in enumerate(building_blocks):
            situations = building_block.situations.all()
            situations_data = SituationSerializer(situations, many=True).data
            data['building_blocks'][index_a]['situations'] = situations_data

            for index_b, situation in enumerate(situations):
                goals = situation.goals.all()
                goals_data = GoalSerializer(goals, many=True).data
                data['building_blocks'][index_a]['situations'][index_b]['goals'] = goals_data

        return Response(
            data=data
        )
