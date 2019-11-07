from api.models import EmailConfirmation
from api.tests import AbstractTestCase


class AuthTestCase(AbstractTestCase):

    def test_register(self):
        response = self.client.post(
            '/api/v1/auth/register',
            {
                'email': 'a@b.com',
                'password': 'password'
            }
        )

        self.assertEqual(response.status_code, 200)

    """def test_activate(self):
        self.test_register()

        response = self.client.post(
            '/api/v1/auth/activate',
            {
                'identifier': EmailConfirmation.objects.first().identifier
            }
        )

        self.assertEqual(response.status_code, 200)"""

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
