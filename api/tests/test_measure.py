from api.tests import AbstractTestCase
from api.models import BuildingBlock, Situation, Goal, Measure


class MeasureTestCase(AbstractTestCase):

    def setUp(self):
        super().setUp()

    def test_list(self):
        building_block_a = BuildingBlock.objects.create(title='building_block_a')
        building_block_b = BuildingBlock.objects.create(title='building_block_b')

        situation_a = Situation.objects.create(building_block=building_block_a, title='situation_a')
        situation_b = Situation.objects.create(building_block=building_block_b, title='situation_b')

        goal_a = Goal.objects.create(situation=situation_a, title='goal_a')
        goal_b = Goal.objects.create(situation=situation_b, title='goal_b')

        Measure.objects.create(goal=goal_a, title='measure_a')
        Measure.objects.create(goal=goal_b, title='measure_b')

        response = self.client.get(
            '/api/v1/measures'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

        response = self.client.get(
            '/api/v1/measures?goal={}'.format(goal_a.id)
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_retrieve(self):
        building_block_a = BuildingBlock.objects.create(title='building_block_a')

        situation_a = Situation.objects.create(building_block=building_block_a, title='situation_a')

        goal_a = Goal.objects.create(situation=situation_a, title='goal_a')

        measure_a = Measure.objects.create(goal=goal_a, title='measure_a')

        response = self.client.get(
            '/api/v1/measures/{}'.format(measure_a.id)
        )

        self.assertEqual(response.status_code, 200)
