from api.tests import AbstractTestCase
from api.models import Strategy, Token


class StrategyTestCase(AbstractTestCase):

    fixtures = ['user', 'token']

    def setUp(self):
        super().setUp()

    def test_create(self):
        response = self.client.post(
            '/api/v1/strategies',
            {
                'title': 'title',
                'description': 'description'
            },
            content_type='application/json',
            **self.header
        )

        self.assertEqual(response.status_code, 201)

    def test_create_second_strategy(self):
        user = Token.objects.get(identifier=self.header['HTTP_AUTHORIZATION']).user

        Strategy.objects.create(user=user, title='title', description='description')

        response = self.client.post(
            '/api/v1/strategies',
            {
                'title': 'title',
                'description': 'description'
            },
            content_type='application/json',
            **self.header
        )

        self.assertEqual(response.status_code, 400)

    def test_list(self):
        response = self.client.get(
            '/api/v1/strategies'
        )

        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        user = Token.objects.get(identifier=self.header['HTTP_AUTHORIZATION']).user

        strategy = Strategy.objects.create(user=user, title='title', description='description')

        response = self.client.get(
            '/api/v1/strategies/{}'.format(strategy.id)
        )

        self.assertEqual(response.status_code, 200)

    def test_patch(self):
        user = Token.objects.get(identifier=self.header['HTTP_AUTHORIZATION']).user

        strategy = Strategy.objects.create(user=user, title='title', description='description')

        response = self.client.patch(
            '/api/v1/strategies/{}'.format(strategy.id),
            {
                'title': 'title',
                'description': 'description'
            },
            content_type='application/json',
            **self.header
        )

        self.assertEqual(response.status_code, 200)

    def test_destroy(self):
        user = Token.objects.get(identifier=self.header['HTTP_AUTHORIZATION']).user

        strategy = Strategy.objects.create(user=user, title='title', description='description')

        response = self.client.delete(
            '/api/v1/strategies/{}'.format(strategy.id),
            content_type='application/json',
            **self.header
        )

        self.assertEqual(response.status_code, 204)

    def test_destroy_not_mine(self):
        user = Token.objects.get(identifier=self.header['HTTP_AUTHORIZATION']).user

        strategy = Strategy.objects.create(user=user, title='title', description='description')

        response = self.client.delete(
            '/api/v1/strategies/{}'.format(strategy.id),
            content_type='application/json',
            **self.other_header
        )

        self.assertEqual(response.status_code, 403)
