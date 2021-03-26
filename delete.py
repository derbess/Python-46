import requests

KEY = '186a2ae6b4e4a7465105495e3430df15'
URL = 'https://api.openweathermap.org/data/2.5/weather'
city_name = 'Astana'
parameters = {
    'q': city_name,
    'appid': KEY,
    'units': 'metric'
}
weather = requests.get(URL, params=parameters)

print(weather.json())
