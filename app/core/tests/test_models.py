from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUser(TestCase):

    def test_user_model(self):
        email = 'test@email.com'
        password = 'testPass123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
