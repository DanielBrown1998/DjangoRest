from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class AuthenticationTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_superuser(
            username="admin",
            password="1234",
        )

    def test_authentication_with_valid_credentials(self):
        # Test authentication with valid credentials
        user = authenticate(username="admin", password="1234")
        self.assertTrue((user is not None) and (user.is_authenticated))

    def test_authentication_with_invalid_credentials(self):
        # Test authentication with invalid password
        user = authenticate(username="admin", password="wrongpassword")
        self.assertIsNone(user)

