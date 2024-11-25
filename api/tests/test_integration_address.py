from lib2to3.fixes.fix_input import context

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from base.models.address_model import Address
# Create your tests here.


class TestIntegrationAddress(APITestCase):
    def test_create_address(self):
        url = reverse("api:address-list")
        data = context ={
            "city": "yakro",
            "street": "Plateau",
            "country": "CI",
            "name":"jojo"
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(Address.objects.count(), 1)


