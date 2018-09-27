from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from rest_framework import status


# Create your tests here.
def test_create_account(self):
    """
    Ensure we can create a new account object.
    """
    url = reverse('account-list')
    response = self.client.get(url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)