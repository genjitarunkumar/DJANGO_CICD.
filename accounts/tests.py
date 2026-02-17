from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import UserCredential

class UserCredentialTests(APITestCase):
    def test_hello_world(self):
        """
        Ensure hello_world endpoint returns 200 OK.
        """
        url = reverse('hello_world')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "HELLO WORLD"})
