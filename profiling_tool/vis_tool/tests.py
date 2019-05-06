from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class IndexViewTests(TestCase):
    def test_index(self):
        """
        Check if page accessible.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
