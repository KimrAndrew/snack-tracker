from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.

class snacksTest(SimpleTestCase):
    def test_snacks_page_status_code(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)