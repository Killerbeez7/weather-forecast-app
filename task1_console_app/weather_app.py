"""
Task 1: Weather API requests - Console Application
"""

import requests
import json
import random
from typing import Dict, List, Tuple

class WeatherApp:
    def __init__(self, api_key: str):
        """
        Initialize the Weather App with OpenWeatherMap API key
        
        Args:
            api_key (str): OpenWeatherMap API key
        """
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
        """
        Get weather data for a specific city
        
        Args:
            city (str): City name
            
        Returns:
            Dict: Weather data or None if error
        """
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  # Celsius
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather for {city}: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON for {city}: {e}")
            return None
    
    def get_random_cities_weather(self, num_cities: int = 5) -> List[Dict]:
        """
        Get weather data for random cities
        
        Args:
            num_cities (int): Number of random cities to select
            
        Returns:
            List[Dict]: List of weather data for random cities
        """
        selected_cities = random.sample(self.cities, num_cities)
        weather_data = []
        
        print(f"Fetching weather for: {', '.join(selected_cities)}")
        print("-" * 50)
        
        for city in selected_cities:
            data = self.get_weather(city)
            if data:
                weather_data.append(data)
                print(f"✓ {city}: {data['main']['temp']:.1f}°C, {data['weather'][0]['description']}")
            else:
                print(f"✗ Failed to get weather for {city}")
        
        return weather_data
    
    def calculate_statistics(self, weather_data: List[Dict]) -> Dict:
        """
        Calculate weather statistics from the data
        
        Args:
            weather_data (List[Dict]): List of weather data
            
        Returns:
            Dict: Statistics including coldest city and average temperature
        """
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
    
    def display_weather_info(self, weather_data: Dict) -> None:
        """
        Display detailed weather information for a city
        
        Args:
            weather_data (Dict): Weather data for a city
        """
        if not weather_data:
            print("No weather data available")
            return
        
        city = weather_data['name']
        country = weather_data['sys']['country']
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        feels_like = weather_data['main']['feels_like']
        pressure = weather_data['main']['pressure']
        wind_speed = weather_data['wind']['speed']
        
        print(f"\n🌤️  Weather in {city}, {country}")
        print("=" * 40)
        print(f"Temperature: {temp:.1f}°C (feels like {feels_like:.1f}°C)")
        print(f"Condition: {description.title()}")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Wind Speed: {wind_speed} m/s")
    
    def run_console_app(self):
        """
        Run the console version of the weather app
        """
        print("🌤️  Weather Forecast App - Task 1")
        print("=" * 40)
        print("Features:")
        print("• HTTP/HTTPS requests to OpenWeatherMap API")
        print("• JSON data processing")
        print("• Random city selection (5 cities)")
        print("• User input for individual city search")
        print("• Statistics calculation")
        print("=" * 40)
        
        while True:
            print("\nChoose an option:")
            print("1. Show weather for 5 random cities")
            print("2. Search weather for a specific city")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                print("\n🔄 Fetching weather for 5 random cities...")
                weather_data = self.get_random_cities_weather(5)
                
                if weather_data:
                    print("\n📊 Statistics:")
                    print("-" * 20)
                    stats = self.calculate_statistics(weather_data)
                    print(f"Coldest city: {stats['coldest_city']} ({stats['coldest_temperature']:.1f}°C)")
                    print(f"Average temperature: {stats['average_temperature']:.1f}°C")
                    print(f"Total cities: {stats['total_cities']}")
                
            elif choice == '2':
                city = input("\nEnter city name: ").strip()
                if city:
                    print(f"\n🔄 Fetching weather for {city}...")
                    weather_data = self.get_weather(city)
                    if weather_data:
                        self.display_weather_info(weather_data)
                    else:
                        print(f"❌ Could not find weather data for {city}")
                else:
                    print("❌ Please enter a valid city name")
            
            elif choice == '3':
                print("👋 Goodbye!")
                break
            
            else:
                print("❌ Invalid choice. Please enter 1, 2, or 3.")


def main():
    """
    Main function to run the weather app
    """
    # You need to get your API key from https://openweathermap.org/api
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    
    if not api_key:
        print("❌ API key is required. Please get one from https://openweathermap.org/api")
        return
    
    app = WeatherApp(api_key)
    app.run_console_app()


if __name__ == "__main__":
    main()
