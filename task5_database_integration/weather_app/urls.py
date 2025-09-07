from django.urls import path
from . import views

app_name = 'weather_app'

urlpatterns = [
    # Main views
    path('', views.index, name='index'),
    path('history/', views.weather_history, name='history'),
    
    # API endpoints
    path('api/status/', views.api_status, name='api_status'),
    path('api/random-weather/', views.api_random_weather, name='api_random_weather'),
    path('api/city-weather/', views.api_city_weather, name='api_city_weather'),
]
