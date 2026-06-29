from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import UserProfile, WholesalerProfile, RescueBuyerProfile


class RegistrationTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('register')

    def test_register_wholesaler_with_stall_number(self):
        payload = {
            'full_name': 'Stall Operator',
            'email': 'stall@example.com',
            'password': 'strongpass123',
            'phone_number': '09171234567',
            'stall_number': 'Stall 1',
        }
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(email__iexact=payload['email'])
        profile = user.profile
        self.assertEqual(profile.role, 'WHOLESALER')
        self.assertTrue(hasattr(user, 'wholesaler_profile'))
        self.assertEqual(user.wholesaler_profile.stall_number, payload['stall_number'])

    def test_register_rescue_buyer_without_stall_number(self):
        payload = {
            'full_name': 'Rescue Buyer',
            'email': 'buyer@example.com',
            'password': 'strongpass123',
            'phone_number': '09179876543',
        }
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(email__iexact=payload['email'])
        profile = user.profile
        self.assertEqual(profile.role, 'RESCUE_BUYER')
        self.assertTrue(hasattr(user, 'buyer_profile'))
        self.assertEqual(user.buyer_profile.buyer_type, 'RETAILER')
