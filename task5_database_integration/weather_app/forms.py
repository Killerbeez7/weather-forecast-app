from django import forms
from .models import City


class CitySearchForm(forms.Form):
    """Form for searching weather by city"""
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Enter city name...',
            'id': 'cityInput'
        }),
        label='City Name'
    )

    def clean_city(self):
        city = self.cleaned_data.get('city')
        if city:
            return city.strip().title()
        return city


class WeatherPreferencesForm(forms.Form):
    """Form for weather preferences"""
    UNITS_CHOICES = [
        ('metric', 'Celsius (°C)'),
        ('imperial', 'Fahrenheit (°F)'),
        ('kelvin', 'Kelvin (K)'),
    ]
    
    units = forms.ChoiceField(
        choices=UNITS_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Temperature Units',
        initial='metric'
    )
    
    default_cities_count = forms.IntegerField(
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '1',
            'max': '10'
        }),
        label='Default Number of Random Cities',
        initial=5
    )
