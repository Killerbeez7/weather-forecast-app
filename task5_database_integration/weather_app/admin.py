from django.contrib import admin
from .models import City, WeatherData, WeatherRequest, WeatherStatistics


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'country_code', 'created_at']
    list_filter = ['country', 'created_at']
    search_fields = ['name', 'country']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ['city', 'temperature', 'weather_main', 'humidity', 'timestamp']
    list_filter = ['weather_main', 'timestamp', 'city__country']
    search_fields = ['city__name', 'weather_description']
    readonly_fields = ['timestamp']
    date_hierarchy = 'timestamp'


@admin.register(WeatherRequest)
class WeatherRequestAdmin(admin.ModelAdmin):
    list_display = ['request_type', 'city_name', 'success', 'response_time', 'timestamp']
    list_filter = ['request_type', 'success', 'timestamp']
    search_fields = ['city_name', 'error_message']
    readonly_fields = ['timestamp']
    date_hierarchy = 'timestamp'


@admin.register(WeatherStatistics)
class WeatherStatisticsAdmin(admin.ModelAdmin):
    list_display = ['coldest_city', 'coldest_temperature', 'average_temperature', 'total_cities', 'calculation_timestamp']
    list_filter = ['calculation_timestamp']
    search_fields = ['coldest_city']
    readonly_fields = ['calculation_timestamp']
    date_hierarchy = 'calculation_timestamp'


# Customize admin site
admin.site.site_header = "Weather Forecast App - Task 5"
admin.site.site_title = "Weather Admin"
admin.site.index_title = "Weather Data Management"