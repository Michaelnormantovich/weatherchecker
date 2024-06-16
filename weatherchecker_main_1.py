#pip requirements are import requests
import streamlit as st
import requests
import datetime as dt
import pytz

st.title('Weather App')

name = st.text_input('Enter your name', '')
if name:
    st.write(f'Hello {name}, welcome to the weather app!')
location = input('Where are you now? ')

API_KEY = "UiJOvBlqWefW45dmeRtHTylrQHF0Pmm8"
url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={API_KEY}"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)

#different weather codes
weather_code = {
      0: "Unknown",
      1000: "Clear, Sunny",
      1100: "Mostly Clear",
      1101: "Partly Cloudy",
      1102: "Mostly Cloudy",
      1001: "Cloudy",
      2000: "Fog",
      2100: "Light Fog",
      4000: "Drizzle",
      4001: "Rain",
      4200: "Light Rain",
      4201: "Heavy Rain",
      5000: "Snow",
      5001: "Flurries",
      5100: "Light Snow",
      5101: "Heavy Snow",
      6000: "Freezing Drizzle",
      6001: "Freezing Rain",
      6200: "Light Freezing Rain",
      6201: "Heavy Freezing Rain",
      7000: "Ice Pellets",
      7101: "Heavy Ice Pellets",
      7102: "Light Ice Pellets",
      8000: "Thunderstorm"
    }
if response.status_code == 200:

    weather_data = response.json()
    # Here you can handle the weather data as needed
    # Extracting temperature in Celsius
    temperature_in_celsius = (weather_data['data']['values']['temperature'])
    # Here we get the humidity
    humidity= (weather_data ['data']['values']['humidity'])
    condition= (weather_data ['data']['values']['weatherCode'])
    local_time= (weather_data ['data']['time'])
    local_time_obj=dt.datetime.strptime(local_time, "%Y-%m-%dT%H:%M:%SZ")
    friendly_local_time=local_time_obj.strftime("%A, %B %d, %Y, %I:%M %p")

    # Print the temperature in Celsius
    print(f"""Current date ad time at your location is {friendly_local_time},
    the weather is {weather_code[condition]} and the temperature in {weather_data['location']['name']}
    is {temperature_in_celsius:.2f}°C. The humidity is {humidity}%.""")
else:
    print("Failed to retrieve weather data. Please check the location or try again later.")
#now let's see the weather in your next destination
destination= input ('Where do you want to go? ')

url = f"https://api.tomorrow.io/v4/weather/realtime?location={destination}&apikey={API_KEY}"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    weather_data = response.json()
    # Here you can handle the weather data as needed
    # Extracting temperature in Celsius
    temperature_in_celsius = (weather_data['data']['values']['temperature'])
    # Here we get the humidity
    humidity= (weather_data ['data']['values']['humidity'])
    condition= (weather_data ['data']['values']['weatherCode'])
    local_time_destination= (weather_data ['data']['time'])
    local_time_obj_destination=dt.datetime.strptime(local_time_destination, "%Y-%m-%dT%H:%M:%SZ")
    friendly_local_time_destination=local_time_obj_destination.strftime("%A, %B %d, %Y, %I:%M %p")

    # Print the temperature in Celsius
    print(f"""Current date ad time at your location is {friendly_local_time_destination}
          The weather at your destination {weather_code[condition]}
          the temperature in {weather_data['location']['name']} is {temperature_in_celsius:.2f}°C. 
          The humidity is {humidity}%.""")
else:
    print("Failed to retrieve weather data. Please check the location or try again later.")


