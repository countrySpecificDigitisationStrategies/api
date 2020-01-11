from api.tests import AbstractTestCase


class AnalysisTestCase(AbstractTestCase):

    fixtures = ['country', 'analysis']

    def setUp(self):
        super().setUp()

    def test_list(self):
        response = self.client.get(
            '/v1/analysis'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

        """response = self.client.get(
            '/v1/analysis?country={}'.format(2)
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], 2)"""

    def test_retrieve(self):
        response = self.client.get(
            '/v1/analysis/{}'.format(1)
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], 1)
