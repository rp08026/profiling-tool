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

    def test_dataframes(self):
        """
        Check if dataframe option works
        """
        response = self.client.get(reverse('index'), {'dataframe': 'acc'})
        self.assertEqual(response.status_code, 200)

    def test_column(self):
        """
        Check if columns option works
        """
        response = self.client.get(reverse('index'), {'columnns': 'Accident_Index'})

        self.assertEqual(response.status_code, 200)

    def test_columns(self):
        """
        Check if columns option works
        """
        response = self.client.get(reverse('index'), {'columnns': 'Accident_Index,Vehicle_Reference'})
        self.assertEqual(response.status_code, 200)
