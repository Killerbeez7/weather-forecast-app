# Task 3: Weather API Requests - Flask Web Application

## Overview
This is the third task of the Weather Forecast App project. It builds upon Tasks 1 and 2 by creating a web application using Flask microframework, demonstrating web development skills with backend and frontend integration.

## Technologies Used
- **Backend**: Python, Flask, Jinja2 templates
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Libraries**: jQuery, requests, json
- **API**: OpenWeatherMap REST API

## Key Improvements Over Task 2
- **Web Interface**: Accessible from any browser
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern UI**: Bootstrap components and styling
- **Client-Side Interactivity**: jQuery for enhanced user experience
- **Template System**: Dynamic content generation
- **RESTful Architecture**: Clean separation of concerns


## Dependencies
```
Flask>=2.3.0
requests>=2.31.0
python-dotenv>=1.0.0
```

## Usage
```bash
# Windows
cd task3_flask_web
py -m pip install -r requirements.txt
py app.py

# Linux/Mac
cd task3_flask_web
pip install -r requirements.txt
python app.py

# Then open browser to: http://localhost:5000
```

## API Endpoints
- `GET /` - Main weather page
- `POST /api/random-weather` - Get 5 random cities weather
- `POST /api/city-weather` - Get specific city weather
- `GET /api/status` - Get API status and configuration

## Frontend Features
-  Responsive navigation bar with Bootstrap
-  Weather search form with validation
-  Real-time results display with animations
-  Statistics dashboard with visual indicators
-  Loading indicators and progress bars
-  Error handling with user-friendly messages
-  Mobile-optimized responsive interface
-  Weather icons and visual enhancements

## Backend Features
-  Flask application with proper structure
-  Route handling and URL mapping
-  Jinja2 template rendering
-  RESTful API endpoint creation
-  Comprehensive error handling
-  Configuration management from shared config
-  Static file serving (CSS, JS, images)
