from api.tests import AbstractTestCase
from api.models import BuildingBlock


class BuildingBlockTestCase(AbstractTestCase):

    fixtures = ['user', 'token']

    def setUp(self):
        super().setUp()

    def test_list(self):
        BuildingBlock.objects.create(title='building_block_a')
        BuildingBlock.objects.create(title='building_block_b')

        response = self.client.get(
            '/api/v1/building-blocks'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_retrieve(self):
        building_block_a = BuildingBlock.objects.create(title='building_block_a')

        response = self.client.get(
            '/api/v1/building-blocks/{}'.format(building_block_a.id)
        )

        self.assertEqual(response.status_code, 200)
