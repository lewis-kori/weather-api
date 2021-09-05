from django.urls import path

from .views import WeatherAPIView

app_name = 'weather_api'

urlpatterns = [
    path('<city>/', WeatherAPIView.as_view(), name='forecast_data')
]
