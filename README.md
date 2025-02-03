# Weather Forecast App

## Overview
This is a Python-based Weather Forecast Application that provides real-time weather information and a 5-day forecast for a specified city. It utilizes the OpenWeatherMap API to fetch weather data and displays the results in a user-friendly graphical interface built with Tkinter.

## Features
- **Search for Weather**: Enter a city name to get current weather conditions.
- **Real-time Data**: Fetches and displays live temperature, humidity, wind speed, and weather conditions.
- **5-Day Forecast**: Provides a detailed forecast for the next five days.
- **Weather Alerts**: Displays important weather alerts (if available).
- **Responsive UI**: Built with Tkinter and ttk styles for an enhanced user experience.

## Requirements
Ensure you have Python installed on your system and install the required dependencies:

```bash
pip install requests
```

## How to Run
1. Clone or download the project files.
2. Navigate to the project directory and run:
   
   ```bash
   python weather_app.py
   ```

## Dependencies
- `tkinter`: GUI framework for building the application interface.
- `requests`: Library for making API calls to fetch weather data.
- `datetime`: Used for formatting forecast timestamps.
- `json`: Parses the API responses.

## API Usage
This application uses the OpenWeatherMap API for retrieving weather information. You need an API key to use it. Replace the default API key in the `WeatherApp` class with your own:

```python
self.api_key = "YOUR_API_KEY_HERE"
```

## Project Structure
```
weather_app.py  # Main application file
README.md       # Project documentation
```

## Error Handling
- Displays error messages if the city is not found.
- Handles API request failures and JSON parsing errors.
- Ensures smooth UI updates even when data is missing.

## Future Enhancements
- Add support for more detailed hourly forecasts.
- Implement caching to reduce redundant API calls.
- Enhance UI with better styling and icons.

