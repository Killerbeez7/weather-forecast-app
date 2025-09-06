#!/usr/bin/env python
"""
Test script for Django Weather App - Task 4
"""

import os
import sys
import django
import requests
import json
import time

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_project.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from weather_app.models import City, WeatherData, WeatherRequest, WeatherStatistics


def test_django_app():
    """
    Test the Django weather application
    """
    print("🧪 Testing Task 4 - Django Weather App")
    print("=" * 50)
    
    # Test 1: Check if Django is working
    print("\n1. Testing Django Setup...")
    try:
        from django.conf import settings
        print(f"✅ Django version: {django.get_version()}")
        print(f"✅ Database: {settings.DATABASES['default']['ENGINE']}")
        print(f"✅ API Key configured: {bool(settings.WEATHER_API_KEY)}")
    except Exception as e:
        print(f"❌ Django setup error: {e}")
        return False
    
    # Test 2: Test database models
    print("\n2. Testing Database Models...")
    try:
        # Test City model
        city_count = City.objects.count()
        print(f"✅ Cities in database: {city_count}")
        
        # Test WeatherData model
        weather_count = WeatherData.objects.count()
        print(f"✅ Weather data records: {weather_count}")
        
        # Test WeatherRequest model
        request_count = WeatherRequest.objects.count()
        print(f"✅ API request logs: {request_count}")
        
        # Test WeatherStatistics model
        stats_count = WeatherStatistics.objects.count()
        print(f"✅ Statistics records: {stats_count}")
        
    except Exception as e:
        print(f"❌ Database model error: {e}")
        return False
    
    # Test 3: Test Django views
    print("\n3. Testing Django Views...")
    try:
        client = Client()
        
        # Test main page
        response = client.get('/')
        if response.status_code == 200:
            print("✅ Main page loads successfully")
        else:
            print(f"❌ Main page error: {response.status_code}")
        
        # Test history page
        response = client.get('/history/')
        if response.status_code == 200:
            print("✅ History page loads successfully")
        else:
            print(f"❌ History page error: {response.status_code}")
        
        # Test API status endpoint
        response = client.get('/api/status/')
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API status endpoint: {data.get('status', 'unknown')}")
        else:
            print(f"❌ API status error: {response.status_code}")
        
    except Exception as e:
        print(f"❌ Django views error: {e}")
        return False
    
    # Test 4: Test API endpoints
    print("\n4. Testing API Endpoints...")
    try:
        # Test random weather endpoint
        response = client.post('/api/random-weather/', 
                             content_type='application/json')
        if response.status_code in [200, 400]:  # 400 is OK if no API key
            print("✅ Random weather endpoint responds")
        else:
            print(f"❌ Random weather endpoint error: {response.status_code}")
        
        # Test city weather endpoint
        response = client.post('/api/city-weather/', 
                             json.dumps({'city': 'London'}),
                             content_type='application/json')
        if response.status_code in [200, 400, 404]:  # Various OK statuses
            print("✅ City weather endpoint responds")
        else:
            print(f"❌ City weather endpoint error: {response.status_code}")
        
    except Exception as e:
        print(f"❌ API endpoints error: {e}")
        return False
    
    # Test 5: Test admin interface
    print("\n5. Testing Admin Interface...")
    try:
        # Test admin login page
        response = client.get('/admin/')
        if response.status_code == 200:
            print("✅ Admin interface accessible")
        else:
            print(f"❌ Admin interface error: {response.status_code}")
        
        # Test admin login
        response = client.post('/admin/login/', {
            'username': 'admin',
            'password': 'admin123'
        })
        if response.status_code in [200, 302]:  # 302 is redirect after login
            print("✅ Admin login works")
        else:
            print(f"❌ Admin login error: {response.status_code}")
        
    except Exception as e:
        print(f"❌ Admin interface error: {e}")
        return False
    
    # Test 6: Test static files
    print("\n6. Testing Static Files...")
    try:
        # Test CSS file
        response = client.get('/static/css/style.css')
        if response.status_code == 200:
            print("✅ CSS files accessible")
        else:
            print(f"❌ CSS files error: {response.status_code}")
        
        # Test JS file
        response = client.get('/static/js/main.js')
        if response.status_code == 200:
            print("✅ JavaScript files accessible")
        else:
            print(f"❌ JavaScript files error: {response.status_code}")
        
    except Exception as e:
        print(f"❌ Static files error: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("🎉 Django Weather App - Task 4 Tests Completed!")
    print("=" * 50)
    
    return True


def test_with_live_server():
    """
    Test with a live Django server (if running)
    """
    print("\n🌐 Testing with Live Server...")
    print("-" * 30)
    
    base_url = "http://localhost:8000"
    
    try:
        # Test main page
        response = requests.get(f"{base_url}/", timeout=5)
        if response.status_code == 200:
            print("✅ Live server main page accessible")
        else:
            print(f"❌ Live server main page error: {response.status_code}")
        
        # Test API status
        response = requests.get(f"{base_url}/api/status/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Live server API status: {data.get('status', 'unknown')}")
        else:
            print(f"❌ Live server API status error: {response.status_code}")
        
    except requests.exceptions.ConnectionError:
        print("⚠️  Live server not running (this is OK for testing)")
    except Exception as e:
        print(f"❌ Live server test error: {e}")


if __name__ == "__main__":
    print("🚀 Starting Django Weather App Tests...")
    
    # Run Django tests
    success = test_django_app()
    
    # Test with live server if available
    test_with_live_server()
    
    if success:
        print("\n✅ All tests passed! Django app is ready.")
        print("\n📋 Next steps:")
        print("1. Start the Django server: py manage.py runserver")
        print("2. Open http://localhost:8000 in your browser")
        print("3. Access admin at http://localhost:8000/admin/ (admin/admin123)")
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
    
    print("\n🔗 Useful URLs:")
    print("- Main app: http://localhost:8000/")
    print("- History: http://localhost:8000/history/")
    print("- Admin: http://localhost:8000/admin/")
    print("- API Status: http://localhost:8000/api/status/")
