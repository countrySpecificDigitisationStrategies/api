from api.tests import AbstractTestCase
from api.models import Pillar


class PillarTestCase(AbstractTestCase):

    fixtures = ['user', 'token']

    def setUp(self):
        super().setUp()

    def test_list(self):
        Pillar.objects.create(title='title-a')
        Pillar.objects.create(title='title-b')

        response = self.client.get(
            '/api/v1/pillars'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_retrieve(self):
        pillar = Pillar.objects.create(title='title-a')

        response = self.client.get(
            '/api/v1/pillars/{}'.format(pillar.id)
        )

        self.assertEqual(response.status_code, 200)
