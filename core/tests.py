from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class WeatherForecastTests(APITestCase):
    def test_days_below_range(self):
        """
        Ensure that the user doesn't provide days below 1
        """
        url = f"{reverse('core:weather_api:forecast_data', kwargs={'city': 'Nairobi'})}?days={0}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()[0], "Number of days must be between 0 and 10.")

    def test_days_over_range(self):
        """
        Ensure that the user doesn't provide days above 10
        """
        url = f"{reverse('core:weather_api:forecast_data', kwargs={'city': 'Nairobi'})}?days={11}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()[0], "Number of days must be between 0 and 10.")

    def test_days_in_url(self):
        """
        Ensure that there's an actual days value in url params
        """
        url = f"{reverse('core:weather_api:forecast_data', kwargs={'city': 'Eldoret'})}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()[0], "Please provide number of days.")

    def test_invalid_city_requested(self):
        """
        Ensures valid cities are provided and warns users of invalid cities
        """
        url = f"{reverse('core:weather_api:forecast_data', kwargs={'city': 'XYZ'})}?days={5}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "No matching location", response.json().get("error").get("message")
        )

    def test_valid_city_requested(self):
        url = f"{reverse('core:weather_api:forecast_data', kwargs={'city': 'Nairobi'})}?days={3}"
        response = self.client.get(url)
        expected_keys = ["maximum", "minimum", "average", "median"]
        self.assertEqual(list(response.json()), expected_keys)
