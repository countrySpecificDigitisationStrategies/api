from api.tests import AbstractTestCase
from api.models import BuildingBlock, Pillar


class BuildingBlockTestCase(AbstractTestCase):

    def setUp(self):
        super().setUp()

    def test_list(self):
        pillar_a = Pillar.objects.create(title='pillar-a')
        pillar_b = Pillar.objects.create(title='pillar-a')

        BuildingBlock.objects.create(pillar=pillar_a, title='building-block-a')
        BuildingBlock.objects.create(pillar=pillar_b, title='building-block-b')

        response = self.client.get(
            '/api/v1/building-blocks'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

        response = self.client.get(
            '/api/v1/building-blocks?pillar={}'.format(pillar_a.id)
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_retrieve(self):
        pillar = Pillar.objects.create(title='pillar-a')
        building_block = BuildingBlock.objects.create(pillar=pillar, title='title-a')

        response = self.client.get(
            '/api/v1/building-blocks/{}'.format(building_block.id)
        )

        self.assertEqual(response.status_code, 200)
