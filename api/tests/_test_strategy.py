from api.tests import AbstractTestCase
from api.models import BuildingBlock, Situation, Goal, Measure, Strategy, StrategyMeasureInformation, Token, Country


class StrategyTestCase(AbstractTestCase):

    fixtures = ['country', 'user', 'token']

    def setUp(self):
        super().setUp()

        self.country = Country.objects.all().first()

    def test_create(self):
        response = self.client.post(
            '/api/v1/strategies',
            {
                'country': self.country.id,
                'title': 'title',
                'description': 'description'
            },
            content_type='application/json',
            **self.header
        )

        self.assertEqual(response.status_code, 201)

    """def test_create_second_strategy(self):
        user = Token.objects.get(code=self.header['HTTP_AUTHORIZATION']).user

        Strategy.objects.create(user=user, title='title')

        response = self.client.post(
            '/api/v1/strategies',
            {
                'country': self.country.id,
                'title': 'title',
                'description': 'description'
            },
            content_type='application/json',
            **self.header
        )

        self.assertEqual(response.status_code, 400)"""

    def test_list(self):
        response = self.client.get(
            '/api/v1/strategies'
        )

        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        user = Token.objects.get(code=self.header['HTTP_AUTHORIZATION']).user

        strategy = Strategy.objects.create(country=self.country, user=user, title='title')

        response = self.client.get(
            '/api/v1/strategies/{}'.format(strategy.id)
        )

        self.assertEqual(response.status_code, 200)

    """def test_patch(self):
        user = Token.objects.get(code=self.header['HTTP_AUTHORIZATION']).user

        strategy = Strategy.objects.create(user=user, title='title')

        pillar = Pillar.objects.create(title='pillar-a')
        building_block = BuildingBlock.objects.create(pillar=pillar, title='building-block')
        measure = Measure.objects.create(building_block=building_block, title='measure')
        smi = StrategyMeasureInformation.objects.create(measure=measure, strategy=strategy)

        response = self.client.patch(
            '/api/v1/strategies/{}'.format(strategy.id),
            {
                'title': 'title',
                'description': 'description',
                'measures': [smi.id]
            },
            content_type='application/json',
            **self.header
        )

        self.assertEqual(response.status_code, 200)

    def test_destroy(self):
        user = Token.objects.get(code=self.header['HTTP_AUTHORIZATION']).user

        strategy = Strategy.objects.create(user=user, title='title')

        response = self.client.delete(
            '/api/v1/strategies/{}'.format(strategy.id),
            content_type='application/json',
            **self.header
        )

        self.assertEqual(response.status_code, 204)

    def test_destroy_not_mine(self):
        user = Token.objects.get(code=self.header['HTTP_AUTHORIZATION']).user

        strategy = Strategy.objects.create(user=user, title='title')

        response = self.client.delete(
            '/api/v1/strategies/{}'.format(strategy.id),
            content_type='application/json',
            **self.other_header
        )

        self.assertEqual(response.status_code, 403)"""
