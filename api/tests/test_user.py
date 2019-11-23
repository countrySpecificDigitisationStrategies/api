from api.tests import AbstractTestCase
from api.models import User, Token


class UserTestCase(AbstractTestCase):

    fixtures = ['user', 'token']

    def setUp(self):
        super().setUp()

    def test_me(self):
        response = self.client.get(
            '/api/v1/users/me',
            **self.header
        )

        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get(
            '/api/v1/users/logout',
            **self.header
        )

        exists = Token.objects.filter(code=self.header['HTTP_AUTHORIZATION']).exists()

        self.assertEqual(exists, False)
        self.assertEqual(response.status_code, 200)
