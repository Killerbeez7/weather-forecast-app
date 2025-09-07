from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views import View
from django.conf import settings
import requests
import json
import random
import time
from typing import Dict, List

from .models import City, WeatherData, WeatherRequest, WeatherStatistics
from .forms import CitySearchForm, WeatherPreferencesForm


class WeatherApp:
    """Weather application logic"""
    
    def __init__(self):
        self.api_key = settings.WEATHER_API_KEY
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.timeout = settings.WEATHER_REQUEST_TIMEOUT
        self.units = settings.WEATHER_UNITS
        
        # List of cities for random selection
        self.cities = [
            "London", "Paris", "Tokyo", "New York", "Sydney", "Berlin", "Rome", 
            "Madrid", "Amsterdam", "Vienna", "Prague", "Warsaw", "Moscow", 
            "Istanbul", "Cairo", "Dubai", "Mumbai", "Bangkok", "Singapore", 
            "Seoul", "Beijing", "Shanghai", "Hong Kong", "Taipei", "Manila",
            "Jakarta", "Kuala Lumpur", "Ho Chi Minh City", "Bangkok", "Dhaka",
            "Karachi", "Lahore", "Tehran", "Baghdad", "Riyadh", "Kuwait City",
            "Doha", "Abu Dhabi", "Muscat", "Sanaa", "Amman", "Beirut", "Damascus",
            "Jerusalem", "Tel Aviv", "Ankara", "Athens", "Sofia", "Bucharest",
            "Budapest", "Zagreb", "Ljubljana", "Bratislava", "Vilnius", "Riga",
            "Tallinn", "Helsinki", "Stockholm", "Oslo", "Copenhagen", "Reykjavik",
            "Dublin", "Edinburgh", "Cardiff", "Belfast", "Lisbon", "Porto",
            "Barcelona", "Valencia", "Seville", "Bilbao", "Marseille", "Lyon",
            "Nice", "Toulouse", "Strasbourg", "Lille", "Nantes", "Montpellier",
            "Bordeaux", "Rennes", "Toulon", "Grenoble", "Dijon", "Angers",
            "Le Havre", "Saint-Etienne", "Tours", "Limoges", "Amiens", "Perpignan",
            "Metz", "Besancon", "Boulogne-Billancourt", "Orleans", "Mulhouse",
            "Rouen", "Caen", "Nancy", "Saint-Denis", "Argenteuil", "Montreuil",
            "Roubaix", "Tourcoing", "Nanterre", "Avignon", "Creteil", "Dunkirk",
            "Poitiers", "Asnieres-sur-Seine", "Versailles", "Courbevoie", "Vitry-sur-Seine",
            "Colombes", "Aulnay-sous-Bois", "La Rochelle", "Rueil-Malmaison", "Antibes",
            "Saint-Maur-des-Fosses", "Champigny-sur-Marne", "Aubervilliers", "Cannes",
            "Beziers", "Bourges", "Colmar", "Drancy", "Merignac", "Saint-Nazaire",
            "Issy-les-Moulineaux", "Noisy-le-Grand", "Evry", "Cergy", "Pessac",
            "Venissieux", "Clichy", "Ivry-sur-Seine", "Levallois-Perret", "Troyes",
            "Neuilly-sur-Seine", "Antony", "Lorient", "Sarcelles", "Niort", "Le Mans",
            "Aix-en-Provence", "Montauban", "Villeurbanne", "Hyeres", "Cholet",
            "Meudon", "Chambery", "Maisons-Alfort", "Belfort", "Blois", "Annecy",
            "Boulogne-sur-Mer", "Brive-la-Gaillarde", "Cannes", "Chalon-sur-Saone",
            "Charleville-Mezieres", "Chartres", "Chateauroux", "Chaumont", "Cherbourg",
            "Colmar", "Creil", "Dax", "Dieppe", "Douai", "Dreux", "Epinay-sur-Seine",
            "Evreux", "Frejus", "Gap", "Gennevilliers", "Givors", "Grasse", "Haguenau",
            "La Ciotat", "La Seyne-sur-Mer", "Laval", "Le Creusot", "Le Havre",
            "Le Perreux-sur-Marne", "Levallois-Perret", "Libourne", "Lunel", "Macon",
            "Mantes-la-Jolie", "Martigues", "Meaux", "Melun", "Menton", "Montbeliard",
            "Montlucon", "Montrouge", "Narbonne", "Neuilly-sur-Marne", "Nogent-sur-Marne",
            "Palaiseau", "Pantin", "Pierrefitte-sur-Seine", "Plaisir", "Pontault-Combault",
            "Pontoise", "Rambouillet", "Rosny-sous-Bois", "Rueil-Malmaison", "Saint-Brieuc",
            "Saint-Chamond", "Saint-Etienne", "Saint-Germain-en-Laye", "Saint-Jean-de-Luz",
            "Saint-Laurent-du-Var", "Saint-Leu", "Saint-Malo", "Saint-Mande", "Saint-Maur-des-Fosses",
            "Saint-Michel-sur-Orge", "Saint-Ouen", "Saint-Pol-sur-Mer", "Saint-Priest",
            "Saint-Quentin", "Saint-Raphael", "Sainte-Genevieves-des-Bois", "Sainte-Maxime",
            "Salon-de-Provence", "Sartrouville", "Savigny-sur-Orge", "Schiltigheim",
            "Sevran", "Sotteville-les-Rouen", "Stains", "Sucy-en-Brie", "Suresnes",
            "Taverny", "Thiais", "Thionville", "Torcy", "Toulon", "Toulouse", "Tourcoing",
            "Tours", "Trappes", "Tremblay-en-France", "Valence", "Valenciennes", "Vandœuvre-les-Nancy",
            "Vaulx-en-Velin", "Vaulx-en-Velin", "Vierzon", "Vigneux-sur-Seine", "Villeneuve-d'Ascq",
            "Villeneuve-la-Garenne", "Villeneuve-Saint-Georges", "Villepinte", "Villeurbanne",
            "Vincennes", "Viry-Chatillon", "Vitry-sur-Seine", "Wasquehal", "Wattrelos",
            "Wittenheim", "Yerres", "Yvetot", "Yzeure"
        ]
    
    def get_weather(self, city: str) -> Dict:
        """Get weather data for a specific city"""
        start_time = time.time()
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': self.units
            }
            
            response = requests.get(self.base_url, params=params, timeout=self.timeout)
            response.raise_for_status()
            
            response_time = time.time() - start_time
            data = response.json()
            
            # Log successful request
            WeatherRequest.objects.create(
                request_type='city',
                city_name=city,
                success=True,
                response_time=response_time
            )
            
            return data
            
        except requests.exceptions.RequestException as e:
            response_time = time.time() - start_time
            # Log failed request
            WeatherRequest.objects.create(
                request_type='city',
                city_name=city,
                success=False,
                response_time=response_time,
                error_message=str(e)
            )
            return None
        except json.JSONDecodeError as e:
            response_time = time.time() - start_time
            WeatherRequest.objects.create(
                request_type='city',
                city_name=city,
                success=False,
                response_time=response_time,
                error_message=f"JSON decode error: {str(e)}"
            )
            return None
    
    def get_random_cities_weather(self, num_cities: int = 5) -> List[Dict]:
        """Get weather data for random cities"""
        selected_cities = random.sample(self.cities, num_cities)
        weather_data = []
        
        for city in selected_cities:
            data = self.get_weather(city)
            if data:
                weather_data.append(data)
        
        return weather_data
    
    def calculate_statistics(self, weather_data: List[Dict]) -> Dict:
        """Calculate weather statistics from the data"""
        if not weather_data:
            return {"error": "No weather data available"}
        
        temperatures = [data['main']['temp'] for data in weather_data]
        cities = [data['name'] for data in weather_data]
        
        # Find coldest city
        coldest_index = temperatures.index(min(temperatures))
        coldest_city = cities[coldest_index]
        coldest_temp = temperatures[coldest_index]
        
        # Calculate average temperature
        avg_temp = sum(temperatures) / len(temperatures)
        
        stats = {
            "coldest_city": coldest_city,
            "coldest_temperature": coldest_temp,
            "average_temperature": avg_temp,
            "total_cities": len(weather_data)
        }
        
        # Save statistics to database
        WeatherStatistics.objects.create(
            coldest_city=coldest_city,
            coldest_temperature=coldest_temp,
            average_temperature=avg_temp,
            total_cities=len(weather_data)
        )
        
        return stats


# Initialize weather app
weather_app = WeatherApp()


def index(request):
    """Main page view"""
    context = {
        'has_api_key': bool(settings.WEATHER_API_KEY),
        'api_key_status': "✅ Configured" if settings.WEATHER_API_KEY else "❌ Not configured",
        'city_form': CitySearchForm(),
        'preferences_form': WeatherPreferencesForm(),
    }
    return render(request, 'weather_app/index.html', context)


@csrf_exempt
@require_http_methods(["POST"])
def api_random_weather(request):
    """API endpoint to get weather for random cities"""
    try:
        if not settings.WEATHER_API_KEY:
            return JsonResponse({"error": "API key not configured"}, status=400)
        
        weather_data = weather_app.get_random_cities_weather(5)
        
        if not weather_data:
            return JsonResponse({"error": "Failed to fetch weather data"}, status=500)
        
        # Calculate statistics
        stats = weather_app.calculate_statistics(weather_data)
        
        return JsonResponse({
            "success": True,
            "weather_data": weather_data,
            "statistics": stats
        })
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def api_city_weather(request):
    """API endpoint to get weather for a specific city"""
    try:
        if not settings.WEATHER_API_KEY:
            return JsonResponse({"error": "API key not configured"}, status=400)
        
        data = json.loads(request.body)
        city = data.get('city', '').strip()
        
        if not city:
            return JsonResponse({"error": "City name is required"}, status=400)
        
        weather_data = weather_app.get_weather(city)
        
        if not weather_data:
            return JsonResponse({"error": f"Could not find weather data for {city}"}, status=404)
        
        return JsonResponse({
            "success": True,
            "weather_data": weather_data
        })
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def api_status(request):
    """API status endpoint"""
    return JsonResponse({
        "status": "running",
        "api_key_configured": bool(settings.WEATHER_API_KEY),
        "cities_available": len(weather_app.cities),
        "version": "Task 5 - Database Integration"
    })


def weather_history(request):
    """View to display weather history"""
    recent_weather = WeatherData.objects.select_related('city').order_by('-timestamp')[:20]
    recent_requests = WeatherRequest.objects.order_by('-timestamp')[:20]
    recent_statistics = WeatherStatistics.objects.order_by('-calculation_timestamp')[:10]
    
    context = {
        'recent_weather': recent_weather,
        'recent_requests': recent_requests,
        'recent_statistics': recent_statistics,
    }
    return render(request, 'weather_app/history.html', context)