Introduction
This Weather App is a simple desktop application built using the Tkinter GUI toolkit in Python. It allows users to input a city name and retrieve real-time weather information for that location. The app uses the OpenWeatherMap API to fetch weather data and displays it in a visually appealing and user-friendly interface.

Features
City Search: Users can input the name of a city in the provided entry field and click the search icon to get the current weather information.

Real-time Clock: The app displays the current local time of the searched city.

Weather Information Display: The app provides information on temperature, weather condition, wind speed, humidity, description, and atmospheric pressure.

Error Handling: The application includes error handling to manage situations where the entered city name is not found or when an unexpected error occurs during the API request.

Requirements
Python 3.x
Tkinter (Included in standard Python library)
Geopy library
Timezonefinder library
Requests library
Pytz library

Install the required libraries using the following:
pip install geopy
pip install timezonefinder
pip install requests

Usage
Run the Script: Execute the script in a Python environment.

python weather_app.py
Enter City Name: Input the name of the city in the entry field and press the search icon.

View Weather Information: The app will display real-time weather information for the specified city.

File Structure
weather_app.py: The main script containing the application code.
search.png: Image file for the search icon.
search_icon.png: Image file for the search button.
logo.png: Image file for the app logo.
box.png: Image file for the frame background.

Acknowledgments
The Weather App uses the OpenWeatherMap API for weather data.
Icons and images used in the app are credited to their respective sources.

Ensure your API key is kept secure and not shared publicly.
The app design and layout can be customized by replacing the provided image files.
