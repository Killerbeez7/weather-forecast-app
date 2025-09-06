"""
Task 3: Weather API requests - Flask Web Application
"""

from flask import Flask, render_template, request, jsonify
import requests
import json
import random
import sys
import os
from typing import Dict, List

# Add parent directory to path to access config.py
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

try:
    from config import OPENWEATHER_API_KEY, DEFAULT_CITIES_COUNT, REQUEST_TIMEOUT, UNITS
except ImportError:
    # Fallback if config not found
    OPENWEATHER_API_KEY = ""
    DEFAULT_CITIES_COUNT = 5
    REQUEST_TIMEOUT = 10
    UNITS = "metric"

app = Flask(__name__)

class WeatherApp:
    def __init__(self, api_key: str):
        """Initialize the Weather App with OpenWeatherMap API key"""
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        # List of cities for random selection (worldwide cities with Latin names)
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
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': UNITS
            }
            
            response = requests.get(self.base_url, params=params, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather for {city}: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON for {city}: {e}")
            return None
    
    def get_random_cities_weather(self, num_cities: int = DEFAULT_CITIES_COUNT) -> List[Dict]:
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
        
        return {
            "coldest_city": coldest_city,
            "coldest_temperature": coldest_temp,
            "average_temperature": avg_temp,
            "total_cities": len(weather_data)
        }

# Initialize weather app
weather_app = WeatherApp(OPENWEATHER_API_KEY)

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html', 
                         has_api_key=bool(OPENWEATHER_API_KEY),
                         api_key_status="✅ Configured" if OPENWEATHER_API_KEY else "❌ Not configured")

@app.route('/api/random-weather', methods=['POST'])
def get_random_weather():
    """API endpoint to get weather for random cities"""
    try:
        if not OPENWEATHER_API_KEY:
            return jsonify({"error": "API key not configured"}), 400
        
        weather_data = weather_app.get_random_cities_weather(5)
        
        if not weather_data:
            return jsonify({"error": "Failed to fetch weather data"}), 500
        
        # Calculate statistics
        stats = weather_app.calculate_statistics(weather_data)
        
        return jsonify({
            "success": True,
            "weather_data": weather_data,
            "statistics": stats
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/city-weather', methods=['POST'])
def get_city_weather():
    """API endpoint to get weather for a specific city"""
    try:
        if not OPENWEATHER_API_KEY:
            return jsonify({"error": "API key not configured"}), 400
        
        data = request.get_json()
        city = data.get('city', '').strip()
        
        if not city:
            return jsonify({"error": "City name is required"}), 400
        
        weather_data = weather_app.get_weather(city)
        
        if not weather_data:
            return jsonify({"error": f"Could not find weather data for {city}"}), 404
        
        return jsonify({
            "success": True,
            "weather_data": weather_data
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/status')
def api_status():
    """API status endpoint"""
    return jsonify({
        "status": "running",
        "api_key_configured": bool(OPENWEATHER_API_KEY),
        "cities_available": len(weather_app.cities),
        "version": "Task 3 - Flask Web Application"
    })

if __name__ == '__main__':
    print("🌤️ Weather Forecast App - Task 3 (Flask Web)")
    print("=" * 50)
    print(f"API Key Status: {'✅ Configured' if OPENWEATHER_API_KEY else '❌ Not configured'}")
    print(f"Available Cities: {len(weather_app.cities)}")
    print("=" * 50)
    print("Starting Flask development server...")
    print("Open your browser to: http://localhost:5000")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
