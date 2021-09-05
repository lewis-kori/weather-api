import requests
from django.conf import settings
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from ..utils.statistics import (
    get_average_temperature,
    get_max_temperature,
    get_median_temperature,
    get_min_temperature,
)


class WeatherAPIView(APIView):
    """
    This endpoint returns weather forecast data from https://www.weatherapi.com/
    Make a get request to this endpoint with the following format:
    /api/locations/{city}/?days={number_of_days}
    """
    permission_classes = [
        AllowAny,
    ]

    def get(self, request, *args, **kwargs):

        # ensure that there's a days field in the url param and the value is not null
        if "days" in request.GET.keys() and bool(request.GET.get("days")):
            days = int(request.GET.get("days"))
            if days > 0 and days <= 10:
                city = kwargs.get("city")
                forecast_data = self.get_weather_data(city, days)
                return forecast_data
            else:
                # raise error in case number of days is less than 1 and greater than 10
                raise ValidationError(detail="Number of days must be between 0 and 10.")
        else:
            raise ValidationError(detail="Please provide number of days.")

    def get_weather_data(self, city, days):
        api_key = settings.WEATHER_API_KEY
        url = f"{settings.WEATHER_API_BASE_URL}/forecast.json?key={api_key}&q={city}&days={days}&aqi=no&alerts=no"

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            forecast_list = data.get("forecast").get("forecastday")
            
            # retrieve the day key data in the response data
            # implemented here to keep the code D.R.Y as this pattern would repeat
            # itself in all the utility functions
            forecast_days = [forecast.get("day") for forecast in forecast_list]

            forecast_data = {
                "maximum": get_max_temperature(forecast_days),
                "minimum": get_min_temperature(forecast_days),
                "average": get_average_temperature(forecast_days),
                "median": get_median_temperature(forecast_days),
            }
            return Response(data=forecast_data, status=HTTP_200_OK)
        else:
            """
            Offload error messages to the public api as they already have most of the
            status codes covered in their response.
            """
            return Response(data=response.json(), status=response.status_code)
