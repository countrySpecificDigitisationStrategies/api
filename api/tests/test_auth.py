from api.models import EmailConfirmation
from api.tests import AbstractTestCase


class AuthTestCase(AbstractTestCase):

    def setUp(self):
        super().setUp()

    def test_register(self):
        response = self.client.post(
            '/api/v1/auth/register',
            {
                'email': 'a@b.com',
                'password': 'password'
            }
        )

        self.assertEqual(response.status_code, 200)

    def test_register_can_not_with_invalid_email(self):
        response = self.client.post(
            '/api/v1/auth/register',
            {
                'email': 'a',
                'password': 'password'
            }
        )

        self.assertEqual(response.status_code, 400)

    def test_register_can_not_with_invalid_password(self):
        response = self.client.post(
            '/api/v1/auth/register',
            {
                'email': 'a@b.com',
                'password': 'p'
            }
        )

        self.assertEqual(response.status_code, 400)

    def test_login(self):
        self.test_register()

        response = self.client.post(
            '/api/v1/auth/login',
            {
                'email': 'a@b.com',
                'password': 'password'
            }
        )

        self.assertEqual(response.status_code, 200)

    def test_login_email_does_not_exist(self):
        self.test_register()

        response = self.client.post(
            '/api/v1/auth/login',
            {
                'email': 'a@c.com',
                'password': 'password'
            }
        )

        self.assertEqual(response.status_code, 400)

    def test_login_password_invalid(self):
        self.test_register()

        response = self.client.post(
            '/api/v1/auth/login',
            {
                'email': 'a@b.com',
                'password': 'password_'
            }
        )

        self.assertEqual(response.status_code, 400)
