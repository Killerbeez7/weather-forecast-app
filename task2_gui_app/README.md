# Task 2: Weather API Requests - GUI Application

## Overview
This is the second task of the Weather Forecast App project. It builds upon Task 1 by adding a modern graphical user interface using Tkinter, demonstrating GUI programming concepts and improved user experience.

## Features Implemented
- ✅ **All Task 1 Features**: Complete weather API functionality
- ✅ **Modern GUI Interface**: Clean, user-friendly desktop application
- ✅ **Threaded Operations**: Prevents GUI freezing during API calls
- ✅ **Progress Indicators**: Visual feedback during data fetching
- ✅ **API Key Management**: Save and persist API keys securely
- ✅ **Real-time Results**: Live weather data display with statistics
- ✅ **Enhanced User Experience**: Intuitive interface with error handling

## Improvements Over Task 1
- **Graphical Interface**: Replaces console with modern GUI
- **Threading**: Non-blocking operations for smooth user experience
- **Visual Feedback**: Progress bars and status indicators
- **Persistent Configuration**: API key saved between sessions
- **Better Error Handling**: User-friendly error messages
- **Responsive Design**: Proper window sizing and layout

## Requirements
- Python 3.7+
- OpenWeatherMap API key (free tier: 1000 calls/day)
- requests library
- tkinter (included with Python)

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
py weather_gui.py

# Linux/Mac
python weather_gui.py
```

## API Key Setup
1. Visit [OpenWeatherMap API](https://openweathermap.org/api)
2. Sign up for a free account
3. Get your API key
4. Enter it in the GUI and click "Save Key"