# Weather Forecast Application

1. Install required packages:


```shellscript
pip install requests
```

2. Set up your OpenWeather API key:

1. Sign up at [OpenWeather](https://openweathermap.org/api)
2. Get your API key
3. Replace the `api_key` variable in `weather_app.py` with your API key





## Usage

1. Run the application:


```shellscript
python weather_app.py
```

2. Enter a city name in the search box
3. Press Enter or click the Search button
4. View the current weather and forecast information


## Dependencies

- Python 3.x
- requests
- tkinter (usually comes with Python)


## API Reference

This application uses the following OpenWeather API endpoints:

- Geocoding API: Convert city names to coordinates
- Current Weather Data API: Get current weather conditions
- 5 Day / 3 Hour Forecast API: Get weather forecasts


## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Acknowledgments

- Weather data provided by [OpenWeather](https://openweathermap.org/)
- Built with Python and tkinter
- Icons and weather descriptions from OpenWeather


## Future Enhancements

- Add weather icons
- Implement temperature unit conversion (Celsius/Fahrenheit)
- Add graphs for temperature trends
- Save favorite cities
- Add automatic location detection
- Implement periodic weather updates
- Add weather notifications system


## Support

For support, please open an issue in the GitHub repository or contact the maintainers.


## Troubleshooting

Common issues and their solutions:

1. **API Key Error**

1. Make sure you have a valid API key from OpenWeather
2. Check if the API key is correctly placed in the code


2. **City Not Found**

1. Verify the city name is spelled correctly
2. Try adding the country code (e.g., "London,UK")


3. **No Data Displayed**

1. Check your internet connection
2. Verify the API endpoints are accessible
3. Check the console for error messages



## Version History

- 1.0.0

- Initial Release
- Basic weather functionality
- Current weather and 5-day forecast



## Known Issues

- Some cities with same names might show incorrect data
- Forecast data might be delayed by up to 3 hours
- GUI might need adjustments on different screen resolutions

## Feedback

If you have any feedback or suggestions, please reach out to us through:

- Opening an issue
- Sending a pull request
- Contacting the maintainers


---

Remember to star ⭐ this repository if you find it helpful!

