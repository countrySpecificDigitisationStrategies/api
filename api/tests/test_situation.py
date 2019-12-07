from api.tests import AbstractTestCase
from api.models import BuildingBlock, Situation


class BuildingBlockTestCase(AbstractTestCase):

    def setUp(self):
        super().setUp()

    def test_list(self):
        building_block_a = BuildingBlock.objects.create(title='building_block_a')
        building_block_b = BuildingBlock.objects.create(title='building_block_b')

        Situation.objects.create(building_block=building_block_a, title='situation_a')
        Situation.objects.create(building_block=building_block_b, title='situation_b')

        response = self.client.get(
            '/api/v1/situations'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

        response = self.client.get(
            '/api/v1/situations?building_block={}'.format(building_block_a.id)
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_retrieve(self):
        building_block_a = BuildingBlock.objects.create(title='building_block_a')
        
        situation_a = Situation.objects.create(building_block=building_block_a, title='situation_a')

        response = self.client.get(
            '/api/v1/situations/{}'.format(situation_a.id)
        )

        self.assertEqual(response.status_code, 200)
