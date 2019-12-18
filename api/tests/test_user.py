from api.tests import AbstractTestCase
from api.models import User, Token, Country
from api.utils import *


class UserTestCase(AbstractTestCase):

    fixtures = ['country', 'user', 'token']

    def setUp(self):
        super().setUp()

    def test_me(self):
        response = self.client.get(
            '/api/v1/users/me',
            content_type='application/json',
            **self.header
        )

        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json['country']['id'], int)
        self.assertIsInstance(json['current_country']['id'], int)

    def test_patch(self):
        user = Token.objects.get(code=self.header['HTTP_AUTHORIZATION']).user

        country = Country.objects.create(name='Germany')

        response = self.client.patch(
            '/api/v1/users/{}'.format(user.id),
            {
                'country': country.id,
                'current_country': country.id
            },
            content_type='application/json',
            **self.header
        )

        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['country']['id'], country.id)
        self.assertEqual(json['current_country']['id'], country.id)

    def test_logout(self):
        response = self.client.get(
            '/api/v1/users/logout',
            content_type='application/json',
            **self.header
        )

        exists = Token.objects.filter(code=self.header['HTTP_AUTHORIZATION']).exists()

        self.assertEqual(exists, False)
        self.assertEqual(response.status_code, 200)
