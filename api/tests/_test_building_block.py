from api.tests import AbstractTestCase


class BuildingBlockTestCase(AbstractTestCase):

    #fixtures = ['country', 'user', 'token', 'building_block']
    fixtures = ['building_block']

    def setUp(self):
        super().setUp()

    def test_list(self):
        response = self.client.get(
            '/api/v1/building-blocks'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_retrieve(self):
        response = self.client.get(
            '/api/v1/building-blocks/{}'.format(1)
        )

        self.assertEqual(response.status_code, 200)
