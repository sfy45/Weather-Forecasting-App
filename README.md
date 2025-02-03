# Weather Forecast Application

The Weather Forecast App is a graphical user interface (GUI) application built using Tkinter. It allows users to search for a city and get real-time weather updates, a 5-day forecast, and weather alerts using the OpenWeatherMap API.

## Features
- Search for current weather conditions by city name.
- Display temperature, humidity, wind speed, and weather description.
- Fetch and show a 5-day weather forecast.
- Display weather alerts if available.
- User-friendly interface built with Tkinter and ttk widgets.

## Technologies Used
- Python
- Tkinter (GUI framework)
- Requests (for API calls)
- OpenWeatherMap API

## Prerequisites
- Python 3.x installed
- Required libraries:
  ```sh
  pip install requests
  ```
- An API key from [OpenWeatherMap](https://openweathermap.org/api)

## Installation & Usage
1. Clone the repository or download the script.
2. Open the terminal and navigate to the script directory.
3. Run the script:
   ```sh
   python weather_app.py
   ```
4. Enter a city name and click the "Search" button to get weather details.

## Code Structure
- **WeatherApp Class:** Manages the GUI components and interactions.
- **search_weather():** Fetches weather data from OpenWeatherMap API.
- **update_weather_display():** Updates the UI with fetched weather details.
- **main():** Initializes and runs the Tkinter application.

## API Usage
- **Geocoding API**: Converts city names into latitude and longitude.
- **Weather API**: Retrieves current weather conditions.
- **Forecast API**: Provides a 5-day weather forecast.

## Error Handling
- Handles incorrect city names with appropriate error messages.
- Displays API request errors and connection failures.

## Future Improvements
- Add more weather details such as sunrise/sunset times.
- Implement a settings page for unit selection (Celsius/Fahrenheit).
- Improve UI styling with custom themes.

## Contributing
If you have a contribution to make, feel free to submit issues or pull requests. PRs are more than welcome!

## Contact
If you have any queries or feedback drop us a mail [sophiasad1421@gmail.com].

