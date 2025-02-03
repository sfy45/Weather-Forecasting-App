import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime
import json

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")
        self.root.geometry("600x500")
        
        # API key
        self.api_key = "034c02d4b1bed7d80047c69255ee98b8"
        
        # Configure styles
        style = ttk.Style()
        style.configure('TLabel', padding=5, font=('Helvetica', 10))
        style.configure('Header.TLabel', font=('Helvetica', 12, 'bold'))
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Search frame
        self.search_frame = ttk.Frame(self.main_frame)
        self.search_frame.grid(row=0, column=0, columnspan=2, pady=10)
        
        self.search_label = ttk.Label(self.search_frame, text="Enter City:")
        self.search_label.grid(row=0, column=0, padx=5)
        
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self.search_frame, textvariable=self.search_var, width=30)
        self.search_entry.grid(row=0, column=1, padx=5)
        
        self.search_button = ttk.Button(self.search_frame, text="Search", command=self.search_weather)
        self.search_button.grid(row=0, column=2, padx=5)
        
        # Weather info frame
        self.weather_frame = ttk.LabelFrame(self.main_frame, text="Current Weather", padding="10")
        self.weather_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # Weather information labels
        self.city_label = ttk.Label(self.weather_frame, text="", style='Header.TLabel')
        self.city_label.grid(row=0, column=0, columnspan=2)
        
        self.temp_label = ttk.Label(self.weather_frame, text="")
        self.temp_label.grid(row=1, column=0)
        
        self.feels_like_label = ttk.Label(self.weather_frame, text="")
        self.feels_like_label.grid(row=2, column=0)
        
        self.humidity_label = ttk.Label(self.weather_frame, text="")
        self.humidity_label.grid(row=3, column=0)
        
        self.wind_label = ttk.Label(self.weather_frame, text="")
        self.wind_label.grid(row=4, column=0)
        
        self.description_label = ttk.Label(self.weather_frame, text="")
        self.description_label.grid(row=5, column=0)
        
        # Forecast frame
        self.forecast_frame = ttk.LabelFrame(self.main_frame, text="5-Day Forecast", padding="10")
        self.forecast_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # Alert frame
        self.alert_frame = ttk.LabelFrame(self.main_frame, text="Weather Alerts", padding="10")
        self.alert_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        self.alert_label = ttk.Label(self.alert_frame, text="No current weather alerts", wraplength=550)
        self.alert_label.grid(row=0, column=0)

        # Bind Enter key to search
        self.search_entry.bind('<Return>', lambda event: self.search_weather())

    def search_weather(self):
        city = self.search_var.get().strip()
        if not city:
            messagebox.showerror("Error", "Please enter a city name")
            return
            
        try:
            # Get coordinates first
            coord_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={self.api_key}"
            coord_response = requests.get(coord_url)
            
            # Print response for debugging
            print(f"Geocoding Response Status: {coord_response.status_code}")
            print(f"Geocoding Response: {coord_response.text}")
            
            coord_response.raise_for_status()
            coord_data = coord_response.json()
            
            if not coord_data:
                messagebox.showerror("Error", "City not found")
                return
                
            lat = coord_data[0]['lat']
            lon = coord_data[0]['lon']
            
            # Get weather data using the 2.5 API endpoint instead of 3.0
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={self.api_key}"
            weather_response = requests.get(weather_url)
            
            # Print response for debugging
            print(f"Weather Response Status: {weather_response.status_code}")
            print(f"Weather Response: {weather_response.text}")
            
            weather_response.raise_for_status()
            weather_data = weather_response.json()
            
            # Get forecast data
            forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={self.api_key}"
            forecast_response = requests.get(forecast_url)
            forecast_response.raise_for_status()
            forecast_data = forecast_response.json()
            
            self.update_weather_display(weather_data, forecast_data, coord_data[0]['name'])
            
        except requests.RequestException as e:
            print(f"Request Exception: {str(e)}")
            messagebox.showerror("Error", f"Failed to fetch weather data: {str(e)}")
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {str(e)}")
            messagebox.showerror("Error", "Failed to parse weather data")
        except Exception as e:
            print(f"Unexpected Error: {str(e)}")
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def update_weather_display(self, weather_data, forecast_data, city_name):
        try:
            # Update current weather
            self.city_label.config(text=f"Weather in {city_name}")
            self.temp_label.config(text=f"Temperature: {weather_data['main']['temp']}°C")
            self.feels_like_label.config(text=f"Feels like: {weather_data['main']['feels_like']}°C")
            self.humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
            self.wind_label.config(text=f"Wind Speed: {weather_data['wind']['speed']} m/s")
            self.description_label.config(
                text=f"Conditions: {weather_data['weather'][0]['description'].capitalize()}"
            )
            
            # Update forecast
            for widget in self.forecast_frame.winfo_children():
                widget.destroy()
            
            # Get daily forecasts (every 24 hours)
            daily_forecasts = forecast_data['list'][::8][:5]  # Get every 8th item (24 hours) for 5 days
            
            for i, forecast in enumerate(daily_forecasts):
                date = datetime.fromtimestamp(forecast['dt']).strftime('%A')
                temp_max = forecast['main']['temp_max']
                temp_min = forecast['main']['temp_min']
                forecast_text = f"{date}: {temp_max:.1f}°C / {temp_min:.1f}°C"
                ttk.Label(self.forecast_frame, text=forecast_text).grid(row=i, column=0, sticky=tk.W)
            
        except Exception as e:
            print(f"Display Update Error: {str(e)}")
            messagebox.showerror("Error", f"Failed to update display: {str(e)}")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()