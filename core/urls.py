from django.urls import path, include

app_name = 'core'

urlpatterns = [
    path('locations/', include('core.api.urls'))
]
