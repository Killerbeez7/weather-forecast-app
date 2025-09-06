"""
Test script for Task 3 - Flask Web Application API endpoints
"""

import requests
import json
import time

def test_api_endpoints():
    """Test the Flask API endpoints"""
    base_url = "http://localhost:5000"
    
    print("🧪 Testing Task 3 - Flask Web Application API")
    print("=" * 50)
    
    # Test 1: API Status
    print("1. Testing API Status...")
    try:
        response = requests.get(f"{base_url}/api/status", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ API Status: {data['status']}")
            print(f"   ✅ API Key Configured: {data['api_key_configured']}")
            print(f"   ✅ Cities Available: {data['cities_available']}")
            print(f"   ✅ Version: {data['version']}")
        else:
            print(f"   ❌ API Status failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ API Status error: {e}")
    
    print()
    
    # Test 2: Random Weather (if API key is configured)
    print("2. Testing Random Weather...")
    try:
        response = requests.post(f"{base_url}/api/random-weather", 
                               json={}, 
                               headers={'Content-Type': 'application/json'},
                               timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                weather_data = data['weather_data']
                statistics = data['statistics']
                print(f"   ✅ Random weather fetched successfully")
                print(f"   ✅ Cities returned: {len(weather_data)}")
                print(f"   ✅ Coldest city: {statistics['coldest_city']}")
                print(f"   ✅ Average temperature: {statistics['average_temperature']:.1f}°C")
            else:
                print(f"   ❌ Random weather failed: {data.get('error')}")
        else:
            print(f"   ❌ Random weather failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Random weather error: {e}")
    
    print()
    
    # Test 3: City Search
    print("3. Testing City Search...")
    try:
        test_city = "London"
        response = requests.post(f"{base_url}/api/city-weather", 
                               json={'city': test_city}, 
                               headers={'Content-Type': 'application/json'},
                               timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                weather_data = data['weather_data']
                print(f"   ✅ City search successful for {test_city}")
                print(f"   ✅ Temperature: {weather_data['main']['temp']:.1f}°C")
                print(f"   ✅ Condition: {weather_data['weather'][0]['description']}")
                print(f"   ✅ Humidity: {weather_data['main']['humidity']}%")
            else:
                print(f"   ❌ City search failed: {data.get('error')}")
        else:
            print(f"   ❌ City search failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ City search error: {e}")
    
    print()
    print("✅ API testing completed!")
    print("\nTo test the web interface:")
    print("1. Open your browser")
    print("2. Go to: http://localhost:5000")
    print("3. Try the 'Get 5 Random Cities Weather' button")
    print("4. Try searching for a specific city")

if __name__ == "__main__":
    print("Waiting for Flask server to start...")
    time.sleep(3)
    test_api_endpoints()
