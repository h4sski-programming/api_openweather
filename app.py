import requests
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect

from api_connection import get_weather_json, get_city_json, get_weather_history_json
from forms_custom import FormCity
from validate_custom import validate_country_code


app = Flask(__name__)
app.secret_key = 'h4sski'

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)


# 
# Routes
# 
@app.route('/')
@app.route('/?city=<city>&country_code=<country_code>')
def index(city='Krakow', country_code='PL'):
    # city json based on https://openweathermap.org/api/geocoding-api
    city_json = get_city_json(city, country_code)[0]
    
    
    # weather json based on https://openweathermap.org/current
    weather_json = get_weather_json(lat=city_json['lat'], lon=city_json['lon'])
    
    content = {
        'weather_json': weather_json,
        'city_json': city_json,
    }
    return render_template('index.html', **content)
    # return render_template('index.html', weather_json=weather_json, city_json=city_json)


@app.route('/city', methods=['GET'])
def city(city_name=None, country_code=None, list_of_cities=None):
    form_city = FormCity()
    if city_name and country_code:
        return redirect( url_for('index'))
    elif list_of_cities:
        return redirect( url_for('city', city=city_name, country_code=country_code, list_of_cities=list_of_cities))
    return render_template('city.html', form_city=form_city)


@app.route('/city', methods=['POST'])
def city_post():
    form_city = FormCity()
    if form_city.validate_on_submit():
        city_name = form_city.city.data
        country_code = form_city.country_code.data
        list_of_cities = get_city_json(city_name=city_name, country_code=country_code)
        return redirect( url_for('city', city_name=city_name, country_code=country_code, list_of_cities=list_of_cities))
    return redirect( url_for('city'))


@app.route('/history')
def history(city='Krakow', country_code='PL'):
    # city json based on https://openweathermap.org/api/geocoding-api
    city_json = get_city_json(city, country_code)[0]
    # weather json based on https://openweathermap.org/current
    weather_json = get_weather_history_json(lat=city_json['lat'], lon=city_json['lon'])
    
    content = {
        'weather_json': weather_json,
        'city_json': city_json,
    }
    
    
    return render_template('history.html', **content)


if __name__ == '__main__':
    app.run(debug=True)