from api.tests import AbstractTestCase
from api.models import User, Token
from api.utils import *


class UserTestCase(AbstractTestCase):

    fixtures = ['user', 'token']

    def setUp(self):
        super().setUp()

    def test_me(self):
        response = self.client.get(
            '/api/v1/users/me',
            content_type='application/json',
            **self.header
        )

        self.assertEqual(response.status_code, 200)

    def test_patch(self):
        user = Token.objects.get(code=self.header['HTTP_AUTHORIZATION']).user

        response = self.client.patch(
            '/api/v1/users/{}'.format(user.id),
            {
                'current_country': AFGHANISTAN
            },
            content_type='application/json',
            **self.header
        )
        #print(response.json())

        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get(
            '/api/v1/users/logout',
            content_type='application/json',
            **self.header
        )

        exists = Token.objects.filter(code=self.header['HTTP_AUTHORIZATION']).exists()

        self.assertEqual(exists, False)
        self.assertEqual(response.status_code, 200)
