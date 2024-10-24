import requests
from const import APIKEY

def check_bad_weather(weather):
    # Проверка каждого значения
    temperature_bool = 0 <= weather['Temperature_C'] <= 35 
    wind_speed_bool = weather['Wind_Speed_kmh'] <= 50
    rain_bool = weather['Rain_Probability'] <= 30
    humidity_bool = 20 <= weather['Humidity'] <= 70

    if temperature_bool and wind_speed_bool and rain_bool and humidity_bool:
        return 1
    else:
        return 0

def get_weather_data(city):

    url = f'http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{city}'
    params = {
        'apikey': APIKEY,
        'details': 'true'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        response.raise_for_status()
        data = response.json()

        weather = {
            "Temperature_C": (data[0]['Temperature']['Value'] - 32) * 5 / 9,
            "Humidity": float(data[0]['RelativeHumidity']),
            "Wind_Speed_kmh": float(data[0]['Wind']['Speed']['Value']) * 1.60934,
            "Rain_Probability": float(data[0]['PrecipitationProbability'])
        }


        return weather

def get_and_check(city_key_start, city_key_end):
    data_city_start = get_weather_data(city_key_start)
    data_city_end = get_weather_data(city_key_end)

    res = check_bad_weather(data_city_start) * check_bad_weather(data_city_end) # логика такая, что если погода хоть где-то не очн, то все, дома сиди
    
    res_data = {
        "weather_start" : data_city_start,
        "weather_end": data_city_end,
        "res": res
    }

    return res_data