import requests
from flask import Flask, render_template

from api_connection import get_weather_json, get_city_json

app = Flask(__name__)


@app.route('/')
def index():
    
    # city json based on https://openweathermap.org/api/geocoding-api
    city_json = get_city_json()
    
    # weather json based on https://openweathermap.org/current
    weather_json = get_weather_json(lat=city_json['lat'], lon=city_json['lon'])
    
    return render_template('index.html', weather_json=weather_json)


if __name__ == '__main__':
    app.run(debug=True)