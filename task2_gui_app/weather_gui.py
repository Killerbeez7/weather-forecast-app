"""
Task 2: Weather API requests - GUI Application
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import requests
import json
import random
import os
from typing import Dict, List

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


class WeatherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🌤️ Weather Forecast App - Task 2 (GUI)")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize weather app
        self.weather_app = None
        self.api_key = None
        
        # Create the GUI
        self.create_widgets()
        
        # Check for existing API key
        self.load_api_key()
    
    def create_widgets(self):
        """Create and arrange GUI widgets"""
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="🌤️ Weather Forecast App - Task 2", 
                               font=('Arial', 18, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))
        
        # Subtitle
        subtitle_label = ttk.Label(main_frame, text="GUI Application with Tkinter", 
                                  font=('Arial', 12, 'italic'))
        subtitle_label.grid(row=1, column=0, columnspan=3, pady=(0, 20))
        
        # API Key section
        api_frame = ttk.LabelFrame(main_frame, text="API Configuration", padding="10")
        api_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        api_frame.columnconfigure(1, weight=1)
        
        ttk.Label(api_frame, text="OpenWeatherMap API Key:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.api_key_var = tk.StringVar()
        self.api_key_entry = ttk.Entry(api_frame, textvariable=self.api_key_var, show="*", width=40)
        self.api_key_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        
        self.save_key_btn = ttk.Button(api_frame, text="Save Key", command=self.save_api_key)
        self.save_key_btn.grid(row=0, column=2)
        
        # Main buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=3, column=0, columnspan=3, pady=(0, 15))
        
        # Random cities button
        self.random_btn = ttk.Button(buttons_frame, text="🌍 Get 5 Random Cities Weather", 
                                    command=self.get_random_weather, style='Accent.TButton')
        self.random_btn.grid(row=0, column=0, padx=(0, 15))
        
        # Search frame
        search_frame = ttk.Frame(buttons_frame)
        search_frame.grid(row=0, column=1, padx=(15, 0))
        
        ttk.Label(search_frame, text="Search City:").grid(row=0, column=0, padx=(0, 5))
        self.city_var = tk.StringVar()
        self.city_entry = ttk.Entry(search_frame, textvariable=self.city_var, width=20)
        self.city_entry.grid(row=0, column=1, padx=(0, 5))
        self.city_entry.bind('<Return>', lambda e: self.search_city())
        
        self.search_btn = ttk.Button(search_frame, text="🔍 Search", command=self.search_city)
        self.search_btn.grid(row=0, column=2)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        
        # Results frame
        results_frame = ttk.LabelFrame(main_frame, text="Weather Results", padding="10")
        results_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 15))
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(5, weight=1)
        
        # Text widget for results
        self.results_text = scrolledtext.ScrolledText(results_frame, height=18, width=90, 
                                                     font=('Consolas', 10))
        self.results_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Statistics frame
        stats_frame = ttk.LabelFrame(main_frame, text="Statistics", padding="10")
        stats_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        stats_frame.columnconfigure(1, weight=1)
        
        self.stats_text = tk.Text(stats_frame, height=4, width=90, font=('Arial', 10))
        self.stats_text.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E))
        
        # Clear button
        clear_btn = ttk.Button(main_frame, text="🗑️ Clear Results", command=self.clear_results)
        clear_btn.grid(row=7, column=0, columnspan=3, pady=(10, 0))
    
    def load_api_key(self):
        """Load API key from config file if it exists"""
        try:
            import sys
            parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            sys.path.append(parent_dir)
            from config import OPENWEATHER_API_KEY
            
            if OPENWEATHER_API_KEY and OPENWEATHER_API_KEY != "":
                self.api_key_var.set(OPENWEATHER_API_KEY)
                self.api_key = OPENWEATHER_API_KEY
                self.weather_app = WeatherApp(OPENWEATHER_API_KEY)
        except ImportError:
            print("Config file not found in parent directory")
        except Exception as e:
            print(f"Error loading API key: {e}")
    
    def save_api_key(self):
        """Save API key to config file"""
        key = self.api_key_var.get().strip()
        if not key:
            messagebox.showerror("Error", "Please enter an API key")
            return
        
        try:
            # Update config file in parent directory
            import sys
            parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            config_path = os.path.join(parent_dir, 'config.py')
            
            config_content = f'''"""
Configuration file for the Weather App
Shared across all tasks (Task 1, 2, 3, 4, 5)
"""

# OpenWeatherMap API Configuration
# Get your API key from: https://openweathermap.org/api
OPENWEATHER_API_KEY = "{key}"

# App Configuration
DEFAULT_CITIES_COUNT = 5
REQUEST_TIMEOUT = 10
UNITS = "metric"  # metric, imperial, kelvin
'''
            with open(config_path, 'w') as f:
                f.write(config_content)
            
            self.api_key = key
            self.weather_app = WeatherApp(key)
            messagebox.showinfo("Success", "API key saved successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save API key: {e}")
    
    def start_progress(self):
        """Start the progress bar"""
        self.progress.start()
        self.random_btn.config(state='disabled')
        self.search_btn.config(state='disabled')
        self.save_key_btn.config(state='disabled')
    
    def stop_progress(self):
        """Stop the progress bar"""
        self.progress.stop()
        self.random_btn.config(state='normal')
        self.search_btn.config(state='normal')
        self.save_key_btn.config(state='normal')
    
    def get_random_weather(self):
        """Get weather for 5 random cities in a separate thread"""
        if not self.weather_app:
            messagebox.showerror("Error", "Please enter and save your API key first")
            return
        
        def fetch_weather():
            try:
                self.start_progress()
                self.results_text.delete(1.0, tk.END)
                self.stats_text.delete(1.0, tk.END)
                
                self.results_text.insert(tk.END, "🔄 Fetching weather for 5 random cities...\n")
                self.results_text.insert(tk.END, "=" * 60 + "\n\n")
                
                weather_data = self.weather_app.get_random_cities_weather(5)
                
                if weather_data:
                    # Display weather data
                    for data in weather_data:
                        city = data['name']
                        country = data['sys']['country']
                        temp = data['main']['temp']
                        humidity = data['main']['humidity']
                        description = data['weather'][0]['description']
                        feels_like = data['main']['feels_like']
                        
                        self.results_text.insert(tk.END, f"🌤️ {city}, {country}\n")
                        self.results_text.insert(tk.END, f"   Temperature: {temp:.1f}°C (feels like {feels_like:.1f}°C)\n")
                        self.results_text.insert(tk.END, f"   Condition: {description.title()}\n")
                        self.results_text.insert(tk.END, f"   Humidity: {humidity}%\n")
                        self.results_text.insert(tk.END, "-" * 50 + "\n\n")
                    
                    # Calculate and display statistics
                    stats = self.weather_app.calculate_statistics(weather_data)
                    self.stats_text.insert(tk.END, f"📊 Statistics:\n")
                    self.stats_text.insert(tk.END, f"   Coldest city: {stats['coldest_city']} ({stats['coldest_temperature']:.1f}°C)\n")
                    self.stats_text.insert(tk.END, f"   Average temperature: {stats['average_temperature']:.1f}°C\n")
                    self.stats_text.insert(tk.END, f"   Total cities: {stats['total_cities']}\n")
                else:
                    self.results_text.insert(tk.END, "❌ Failed to fetch weather data. Please check your API key and internet connection.\n")
                
            except Exception as e:
                self.results_text.insert(tk.END, f"❌ Error: {str(e)}\n")
            finally:
                self.stop_progress()
        
        # Run in separate thread to prevent GUI freezing
        thread = threading.Thread(target=fetch_weather)
        thread.daemon = True
        thread.start()
    
    def search_city(self):
        """Search weather for a specific city"""
        city = self.city_var.get().strip()
        if not city:
            messagebox.showerror("Error", "Please enter a city name")
            return
        
        if not self.weather_app:
            messagebox.showerror("Error", "Please enter and save your API key first")
            return
        
        def fetch_city_weather():
            try:
                self.start_progress()
                self.results_text.delete(1.0, tk.END)
                self.stats_text.delete(1.0, tk.END)
                
                self.results_text.insert(tk.END, f"🔄 Fetching weather for {city}...\n")
                self.results_text.insert(tk.END, "=" * 60 + "\n\n")
                
                weather_data = self.weather_app.get_weather(city)
                
                if weather_data:
                    # Display in GUI
                    city_name = weather_data['name']
                    country = weather_data['sys']['country']
                    temp = weather_data['main']['temp']
                    humidity = weather_data['main']['humidity']
                    description = weather_data['weather'][0]['description']
                    feels_like = weather_data['main']['feels_like']
                    pressure = weather_data['main']['pressure']
                    wind_speed = weather_data['wind']['speed']
                    
                    self.results_text.insert(tk.END, f"🌤️ Weather in {city_name}, {country}\n")
                    self.results_text.insert(tk.END, "=" * 50 + "\n")
                    self.results_text.insert(tk.END, f"Temperature: {temp:.1f}°C (feels like {feels_like:.1f}°C)\n")
                    self.results_text.insert(tk.END, f"Condition: {description.title()}\n")
                    self.results_text.insert(tk.END, f"Humidity: {humidity}%\n")
                    self.results_text.insert(tk.END, f"Pressure: {pressure} hPa\n")
                    self.results_text.insert(tk.END, f"Wind Speed: {wind_speed} m/s\n")
                else:
                    self.results_text.insert(tk.END, f"❌ Could not find weather data for {city}\n")
                    self.results_text.insert(tk.END, "Please check the city name and try again.\n")
                
            except Exception as e:
                self.results_text.insert(tk.END, f"❌ Error: {str(e)}\n")
            finally:
                self.stop_progress()
        
        # Run in separate thread to prevent GUI freezing
        thread = threading.Thread(target=fetch_city_weather)
        thread.daemon = True
        thread.start()
    
    def clear_results(self):
        """Clear all results"""
        self.results_text.delete(1.0, tk.END)
        self.stats_text.delete(1.0, tk.END)
        self.city_var.set("")


def main():
    """Main function to run the GUI application"""
    root = tk.Tk()
    
    # Configure style
    style = ttk.Style()
    style.theme_use('clam')
    
    # Create custom style for accent button
    style.configure('Accent.TButton', foreground='white', background='#0078d4')
    
    app = WeatherGUI(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()


if __name__ == "__main__":
    main()
