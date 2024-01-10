from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class FizzBuzzTests(TestCase):
    def test_fizz_buzz_endpoint(self):
        url = reverse('fizz_buzz', args=(3, 5, 15, 'Fizz', 'Buzz'))
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14",
                          "FizzBuzz"])

    def test_invalid_parameters(self):
        url = reverse('fizz_buzz', args=(0, 0, 0, '', ''))  # Invalid parameters
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non-positive', response.json()['detail'])

    def test_statistics_endpoint(self):
        # Call fizz_buzz endpoint multiple times to create statistics
        for _ in range(5):
            self.client.get(reverse('fizz_buzz', args=(3, 5, 15, 'Fizz', 'Buzz')))

        url = reverse('statistics')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('int1', response.json())
        self.assertIn('int2', response.json())
        self.assertIn('limit', response.json())
        self.assertIn('str1', response.json())
        self.assertIn('str2', response.json())
        self.assertIn('count', response.json())
