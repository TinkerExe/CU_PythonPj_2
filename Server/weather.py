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
    try:
        url = f'http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{city}'
        params = {'apikey': APIKEY, 'details': 'true'}
        response = requests.get(url, params=params)
        response.raise_for_status()  # Поднимаем исключение при статусе ошибки

        data = response.json()

        weather = {
            "Temperature_C": round((data[0]['Temperature']['Value'] - 32) * 5 / 9, 1),
            "Humidity": int(data[0]['RelativeHumidity']),
            "Wind_Speed_kmh": round(float(data[0]['Wind']['Speed']['Value']) * 1.60934, 1),
            "Rain_Probability": int(data[0]['PrecipitationProbability'])
        }

        return weather
    except requests.exceptions.RequestException as e:
        return {"error": f"Ошибка при запросе данных погоды: {str(e)}"}

def get_and_check(city_key_start, city_key_end):
    data_city_start = get_weather_data(city_key_start)
    data_city_end = get_weather_data(city_key_end)

    if "error" in data_city_start or "error" in data_city_end:
        return {"error": "Не удалось получить данные от Api-сервера"}

    if check_bad_weather(data_city_start) * check_bad_weather(data_city_end) == 1:
        res = "Ого, погода супер!"
    else:
        res = "Сегодня погодка не очень."

    return {
        "weather_start": data_city_start,
        "weather_end": data_city_end,
        "res": res
    }
