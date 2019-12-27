from api.tests import AbstractTestCase


class GoalTestCase(AbstractTestCase):

    fixtures = ['building_block', 'situation', 'goal']

    def setUp(self):
        super().setUp()

    def test_list(self):
        response = self.client.get(
            '/api/v1/goals'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

        response = self.client.get(
            '/api/v1/goals?situation={}'.format(2)
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], 2)

    def test_retrieve(self):
        response = self.client.get(
            '/api/v1/goals/{}'.format(1)
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], 1)
