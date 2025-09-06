"""
Test script for Task 1 - Console Weather App
"""

import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from weather_app import WeatherApp

def test_weather_app():
    """
    Test the weather app functionality
    """
    print("🧪 Testing Task 1 - Console Weather App")
    print("=" * 50)
    
    # Test with a dummy API key (this will fail, but we can test the structure)
    app = WeatherApp("test_key")
    
    # Test city selection
    print(f"Available cities: {len(app.cities)}")
    print(f"Sample cities: {app.cities[:5]}")
    
    # Test statistics calculation
    test_data = [
        {
            'name': 'Test City 1',
            'main': {'temp': 20.0},
            'weather': [{'description': 'sunny'}],
            'sys': {'country': 'TC'}
        },
        {
            'name': 'Test City 2', 
            'main': {'temp': 15.0},
            'weather': [{'description': 'cloudy'}],
            'sys': {'country': 'TC'}
        },
        {
            'name': 'Test City 3',
            'main': {'temp': 25.0},
            'weather': [{'description': 'rainy'}],
            'sys': {'country': 'TC'}
        }
    ]
    
    stats = app.calculate_statistics(test_data)
    print(f"\nTest Statistics:")
    print(f"Coldest city: {stats['coldest_city']} ({stats['coldest_temperature']}°C)")
    print(f"Average temperature: {stats['average_temperature']:.1f}°C")
    print(f"Total cities: {stats['total_cities']}")
    
    print("\n✅ Task 1 basic functionality test completed!")
    print("\nTo run the full application:")
    print("python weather_app.py")

if __name__ == "__main__":
    test_weather_app()
