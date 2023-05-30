# https://home.openweathermap.org/api_keys
import requests


API_KEY = 'a737dead0c6e306a297117f907aa102d'


def get_weather_json(lat, lon):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&mode=jason&units=metric')
    # city json based on https://openweathermap.org/api/geocoding-api
    return response.json()


def get_city_json(city_name='Krakow', country_code='PL', limit=5):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit={limit}&appid={API_KEY}')
    # weather json based on https://openweathermap.org/current
    return response.json()[0]
