from api.tests import AbstractTestCase


class CountryTestCase(AbstractTestCase):

    fixtures = ['country']

    def setUp(self):
        super().setUp()

    def test_list(self):
        response = self.client.get(
            '/api/v1/countries'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_retrieve(self):
        response = self.client.get(
            '/api/v1/countries/{}'.format(1)
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], 1)
