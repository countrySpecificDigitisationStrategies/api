from api.tests import AbstractTestCase


class BuildingBlockTestCase(AbstractTestCase):

    fixtures = ['building_block', 'situation']

    def setUp(self):
        super().setUp()

    def test_list(self):
        response = self.client.get(
            '/api/v1/situations'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

        response = self.client.get(
            '/api/v1/situations?building_block={}'.format(2)
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], 2)

    def test_retrieve(self):
        response = self.client.get(
            '/api/v1/situations/{}'.format(1)
        )

        self.assertEqual(response.status_code, 200)
