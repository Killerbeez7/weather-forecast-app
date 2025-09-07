from django.db import models
from django.utils import timezone


class City(models.Model):
    """Model to store city information"""
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Cities"
        ordering = ['name']

    def __str__(self):
        return f"{self.name}, {self.country}"


class WeatherData(models.Model):
    """Model to store weather data"""
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='weather_data')
    temperature = models.FloatField()
    feels_like = models.FloatField()
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    wind_speed = models.FloatField()
    wind_direction = models.IntegerField(null=True, blank=True)
    visibility = models.IntegerField(null=True, blank=True)
    weather_main = models.CharField(max_length=50)
    weather_description = models.CharField(max_length=100)
    weather_icon = models.CharField(max_length=10, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Weather Data"
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.city.name} - {self.temperature}°C - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class WeatherRequest(models.Model):
    """Model to log API requests"""
    REQUEST_TYPES = [
        ('random', 'Random Cities'),
        ('city', 'Specific City'),
        ('status', 'Status Check'),
    ]
    
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    city_name = models.CharField(max_length=100, null=True, blank=True)
    success = models.BooleanField()
    response_time = models.FloatField(null=True, blank=True)  # in seconds
    error_message = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        status = "Success" if self.success else "Failed"
        return f"{self.request_type} - {self.city_name or 'N/A'} - {status}"


class WeatherStatistics(models.Model):
    """Model to store calculated weather statistics"""
    coldest_city = models.CharField(max_length=100)
    coldest_temperature = models.FloatField()
    average_temperature = models.FloatField()
    total_cities = models.IntegerField()
    calculation_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Weather Statistics"
        ordering = ['-calculation_timestamp']

    def __str__(self):
        return f"Stats - {self.coldest_city} ({self.coldest_temperature}°C) - {self.calculation_timestamp.strftime('%Y-%m-%d %H:%M')}"