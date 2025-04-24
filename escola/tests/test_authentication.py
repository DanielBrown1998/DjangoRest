from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class AuthenticationTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_superuser(
            username="admin",
            password="1234",
        )
        self.url = reverse("Estudantes-list")


    def test_authentication_with_valid_credentials(self):
        """Test authentication with valid credentials"""
        user = authenticate(username="admin", password="1234")
        self.assertTrue((user is not None) and (user.is_authenticated))

    def test_authentication_with_invalid_password(self):
        """Test authentication with invalid password"""
        user = authenticate(username="admin", password="wrongpassword")
        self.assertIsNone(user)

    def test_authentication_with_invalid_username(self):
        """Test authentication with invalid username"""
        user = authenticate(username="admn", password="1234")
        self.assertIsNone(user)

    def test_authentication_with_empty_credentials(self):
        """Test authentication with empty credentials"""
        user = authenticate(username="", password="")
        self.assertIsNone(user)

    def test_requisition_get_authorixed(self):
        """Test requisition get authorized"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
