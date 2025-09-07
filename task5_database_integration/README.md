# Weather Forecast App - Task 5: Database Integration

## 🌤️ Overview

This is the **Task 5** implementation of the Weather Forecast App with **Database Integration** using **Django** - a full-featured Python web framework. This version demonstrates advanced web development concepts including:

- **Django Framework**: Full-stack web application with models, views, templates, and admin interface
- **Database Integration**: SQLite database with Django ORM for data persistence
- **RESTful API**: Django REST Framework for API endpoints
- **Template System**: Django's powerful templating engine with template inheritance
- **Admin Interface**: Built-in Django admin for data management
- **Static Files**: CSS, JavaScript, and image handling
- **Forms**: Django forms with validation
- **Security**: CSRF protection, input validation, and secure practices

## 🚀 Features

### Core Functionality
- ✅ **Weather API Integration**: OpenWeatherMap API for real-time weather data
- ✅ **Random Cities**: Get weather for 5 random cities worldwide
- ✅ **City Search**: Search weather for specific cities
- ✅ **Statistics**: Calculate coldest city and average temperature
- ✅ **Data Persistence**: Store weather data, requests, and statistics in database

### Django-Specific Features
- ✅ **Models**: City, WeatherData, WeatherRequest, WeatherStatistics
- ✅ **Admin Interface**: Full CRUD operations for all models
- ✅ **Template Inheritance**: Base template with consistent design
- ✅ **Forms**: Django forms with validation
- ✅ **Static Files**: Bootstrap 5, custom CSS, and jQuery
- ✅ **URL Routing**: Clean URL patterns with namespacing
- ✅ **Middleware**: Security and session management
- ✅ **Database Migrations**: Version-controlled database schema

### User Interface
- ✅ **Responsive Design**: Bootstrap 5 with mobile-first approach
- ✅ **Modern UI**: Gradient backgrounds, animations, and smooth transitions
- ✅ **Interactive Elements**: AJAX requests, loading states, and real-time updates
- ✅ **Weather Icons**: Dynamic icons based on weather conditions
- ✅ **Statistics Display**: Visual representation of weather data
- ✅ **History Page**: View past weather data and API requests

## 📁 Project Structure

```
task5_database_integration/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── test_django.py           # Test script
├── README.md                # This file
├── weather_project/         # Django project settings
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── weather_app/             # Django application
│   ├── __init__.py
│   ├── admin.py             # Admin interface configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # App URL patterns
│   ├── forms.py             # Django forms
│   └── migrations/          # Database migrations
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   └── weather_app/         # App-specific templates
│       ├── index.html       # Main page
│       └── history.html     # History page
└── static/                  # Static files
    ├── css/
    │   └── style.css        # Custom styles
    └── js/
        └── main.js          # JavaScript functionality
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+ installed
- OpenWeatherMap API key (get from https://openweathermap.org/api)

### 1. Install Dependencies

**Windows:**
```bash
py -m pip install -r requirements.txt
```

**Linux/Mac:**
```bash
pip install -r requirements.txt
```

### 2. Configure API Key

The app automatically loads the API key from the shared `config.py` file in the root directory. Make sure it's configured:

```python
# In config.py (root directory)
OPENWEATHER_API_KEY = "your_api_key_here"
```

### 3. Database Setup

```bash
# Create database migrations
py manage.py makemigrations

# Apply migrations
py manage.py migrate

# Create superuser (optional)
py manage.py createsuperuser
```

### 4. Run the Application

```bash
# Start Django development server
py manage.py runserver
```

The application will be available at: **http://localhost:8000**

## 🎯 Usage

### Main Features

1. **Random Weather**: Click "Get 5 Random Cities Weather" to fetch weather for 5 random cities
2. **City Search**: Enter a city name and click "Search" to get specific weather data
3. **Statistics**: View calculated statistics including coldest city and average temperature
4. **History**: Access the history page to view past weather data and API requests
5. **Admin**: Access the admin interface at `/admin/` for data management

### Admin Interface

- **URL**: http://localhost:8000/admin/
- **Username**: admin
- **Password**: admin123

The admin interface allows you to:
- View and manage cities
- Monitor weather data
- Track API requests
- View statistics
- Manage user accounts

## 🔧 API Endpoints

### RESTful API

- **GET** `/api/status/` - Get API status and configuration
- **POST** `/api/random-weather/` - Get weather for 5 random cities
- **POST** `/api/city-weather/` - Get weather for a specific city

### Example API Usage

```bash
# Get API status
curl http://localhost:8000/api/status/

# Get random weather
curl -X POST http://localhost:8000/api/random-weather/

# Get city weather
curl -X POST http://localhost:8000/api/city-weather/ \
  -H "Content-Type: application/json" \
  -d '{"city": "London"}'
```

## 🧪 Testing

### Run Tests

```bash
# Run the test script
py test_django.py
```

The test script will:
- ✅ Test Django setup and configuration
- ✅ Test database models and migrations
- ✅ Test Django views and URL routing
- ✅ Test API endpoints
- ✅ Test admin interface
- ✅ Test static files
- ✅ Test with live server (if running)

### Manual Testing

1. **Start the server**: `py manage.py runserver`
2. **Open browser**: Navigate to http://localhost:8000
3. **Test features**: Try random weather, city search, and history
4. **Check admin**: Access http://localhost:8000/admin/

## 🎨 Customization

### Styling

- **CSS**: Edit `static/css/style.css` for custom styles
- **Bootstrap**: Uses Bootstrap 5 for responsive design
- **Icons**: Bootstrap Icons for weather and UI icons

### Templates

- **Base Template**: `templates/base.html` for common layout
- **App Templates**: `templates/weather_app/` for specific pages
- **Template Inheritance**: Extends base template for consistency

### Models

- **City**: Store city information
- **WeatherData**: Store weather data
- **WeatherRequest**: Log API requests
- **WeatherStatistics**: Store calculated statistics

## 🔒 Security Features

- **CSRF Protection**: Django's built-in CSRF protection
- **Input Validation**: Form validation and sanitization
- **SQL Injection Protection**: Django ORM prevents SQL injection
- **XSS Protection**: Template auto-escaping
- **Secure Headers**: Django security middleware

## 📊 Database Schema

### Models

1. **City**
   - name, country, country_code
   - latitude, longitude
   - created_at, updated_at

2. **WeatherData**
   - city (ForeignKey)
   - temperature, feels_like, humidity, pressure
   - wind_speed, wind_direction, visibility
   - weather_main, weather_description, weather_icon
   - timestamp

3. **WeatherRequest**
   - request_type, city_name
   - success, response_time, error_message
   - timestamp

4. **WeatherStatistics**
   - coldest_city, coldest_temperature
   - average_temperature, total_cities
   - calculation_timestamp

## 🚀 Deployment

### Production Settings

For production deployment:

1. **Set DEBUG = False** in settings.py
2. **Configure ALLOWED_HOSTS**
3. **Use a production database** (PostgreSQL, MySQL)
4. **Set up static file serving**
5. **Configure environment variables**
6. **Use a production WSGI server** (Gunicorn, uWSGI)

### Environment Variables

```bash
# Production environment
export DEBUG=False
export SECRET_KEY=your_secret_key
export DATABASE_URL=postgresql://user:pass@host:port/db
export WEATHER_API_KEY=your_api_key
```

## 🔄 Comparison with Previous Tasks

| Feature | Task 1 (Console) | Task 2 (GUI) | Task 3 (Flask) | Task 4 (Django) | Task 5 (Database) |
|---------|------------------|--------------|----------------|-----------------|
| **Framework** | Standard Library | Tkinter | Flask | Django |
| **Database** | None | None | None | SQLite + ORM |
| **Admin Interface** | None | None | None | Built-in Admin |
| **Templates** | None | None | Jinja2 | Django Templates |
| **Forms** | Input/Print | Tkinter | HTML Forms | Django Forms |
| **API** | None | None | Flask Routes | Django REST |
| **Security** | Basic | Basic | CSRF | Full Security |
| **Scalability** | Low | Low | Medium | High |

## 🎯 Learning Objectives

This Task 5 implementation demonstrates:

- ✅ **Django Framework**: Full-stack web development
- ✅ **Database Design**: Models, migrations, and ORM
- ✅ **Template System**: Template inheritance and context
- ✅ **Admin Interface**: Built-in admin customization
- ✅ **Forms**: Django forms with validation
- ✅ **Static Files**: CSS, JavaScript, and media handling
- ✅ **URL Routing**: Clean URL patterns and namespacing
- ✅ **Security**: CSRF, XSS, and SQL injection protection
- ✅ **Testing**: Django testing framework
- ✅ **Deployment**: Production-ready configuration

## 🆘 Troubleshooting

### Common Issues

1. **API Key Not Working**
   - Check `config.py` in root directory
   - Verify API key is valid
   - Check API quota limits

2. **Database Errors**
   - Run `py manage.py migrate`
   - Check database permissions
   - Verify SQLite file exists

3. **Static Files Not Loading**
   - Run `py manage.py collectstatic`
   - Check STATIC_URL in settings
   - Verify static file paths

4. **Template Errors**
   - Check template syntax
   - Verify template paths
   - Check context variables

### Debug Mode

Enable debug mode in `settings.py`:
```python
DEBUG = True
```

This will show detailed error messages and enable the Django debug toolbar.

## 📝 License

This project is part of the Weather Forecast App series and is for educational purposes.

## 🤝 Contributing

This is a learning project. Feel free to:
- Add new features
- Improve the UI/UX
- Add more tests
- Optimize performance
- Add documentation

---

**Task 5 - Database Integration** demonstrates full-stack web development with Django, showcasing advanced features like database integration, admin interface, and production-ready architecture. This represents a significant step up from the previous console, GUI, Flask, and Django implementations.