from api.tests import AbstractTestCase
from api.models import Measure, BuildingBlock, Pillar


class MeasureTestCase(AbstractTestCase):

    def setUp(self):
        super().setUp()

    def test_list(self):
        pillar = Pillar.objects.create(title='pillar-a')

        building_block_a = BuildingBlock.objects.create(pillar=pillar, title='building-block-a')
        building_block_b = BuildingBlock.objects.create(pillar=pillar, title='building-block-b')

        Measure.objects.create(building_block=building_block_a, title='title-a')
        Measure.objects.create(building_block=building_block_b, title='title-b')

        response = self.client.get(
            '/api/v1/measures'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

        response = self.client.get(
            '/api/v1/measures?building_block={}'.format(building_block_b.id)
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_retrieve(self):
        pillar = Pillar.objects.create(title='pillar-a')

        building_block = BuildingBlock.objects.create(pillar=pillar, title='title-a')

        measure = Measure.objects.create(building_block=building_block, title='title-a')

        response = self.client.get(
            '/api/v1/measures/{}'.format(measure.id)
        )

        self.assertEqual(response.status_code, 200)
