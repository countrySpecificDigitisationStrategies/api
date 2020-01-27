from api.tests import AbstractTestCase


class MeasureTestCase(AbstractTestCase):

    fixtures = ['building_block', 'situation', 'goal', 'measure']

    def setUp(self):
        super().setUp()

    def test_list(self):
        response = self.client.get(
            '/api/v1/measures'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

        response = self.client.get(
            '/api/v1/measures?goal={}'.format(2)
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], 2)

    def test_retrieve(self):
        response = self.client.get(
            '/api/v1/measures/{}'.format(1)
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], 1)
