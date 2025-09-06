# Task 1: Weather API Requests - Console Application

## Overview
This is the first task of the Weather Forecast App project. It demonstrates the core functionality of making HTTP requests to the OpenWeatherMap API and processing JSON data in a console application.

## Features Implemented
-  **HTTP/HTTPS Requests**: Direct API calls to OpenWeatherMap
-  **JSON Data Processing**: Parsing and extracting weather information
-  **Random City Selection**: 5 randomly selected cities from 266 worldwide cities
-  **User Input Handling**: Interactive console interface
-  **Statistics Calculation**: Coldest city and average temperature
-  **Individual City Search**: Search weather for any specific city
-  **Error Handling**: Network errors, invalid API keys, city not found

## Requirements
- Python 3.7+
- OpenWeatherMap API key (free tier: 1000 calls/day)
- requests library

## Installation
```bash
# Windows
py -m pip install -r requirements.txt

# Linux/Mac
pip install -r requirements.txt
```

## Usage
```bash
# Windows
py weather_app.py

# Linux/Mac
python weather_app.py
```

## API Key Setup
1. Visit [OpenWeatherMap API](https://openweathermap.org/api)
2. Sign up for a free account
3. Get your API key
4. Enter it when prompted by the application

## Technical Implementation
- **API Endpoint**: `http://api.openweathermap.org/data/2.5/weather`
- **Data Format**: JSON responses
- **Units**: Metric (Celsius)
- **Timeout**: 10 seconds for API requests
- **City Database**: 266 cities worldwide with Latin names

## Sample Output
```
Weather Forecast App - Task 1
========================================
Features:
• HTTP/HTTPS requests to OpenWeatherMap API
• JSON data processing
• Random city selection (5 cities)
• User input for individual city search
• Statistics calculation
========================================

Choose an option:
1. Show weather for 5 random cities
2. Search weather for a specific city
3. Exit

Enter your choice (1-3): 1

Fetching weather for 5 random cities...
Fetching weather for: London, Tokyo, Sydney, Berlin, Paris
--------------------------------------------------
✓ London: 15.2°C, overcast clouds
✓ Tokyo: 22.1°C, clear sky
✓ Sydney: 18.5°C, light rain
✓ Berlin: 12.8°C, broken clouds
✓ Paris: 16.3°C, scattered clouds

Statistics:
--------------------
Coldest city: Berlin (12.8°C)
Average temperature: 16.98°C
Total cities: 5
```

## Next Steps
This console application serves as the foundation for:
- **Task 2**: GUI interface using Tkinter
- **Task 3**: Flask web application
- **Task 4**: Django web application
- **Task 5**: Database integration with persistence
