def check_bad_weather(weather): # На вход подается словарь с важными переменными

  temperature_bool = 0 <= weather['Temperature'] <= 35
  wind_speed_bool = weather['wind_speed'] <= 50
  rain_bool = weather['rain_probability'] <= 30
  humidity_bool = 20 <= weather['Humidity'] <= 70

  if temperature_bool and wind_speed_bool and rain_bool and humidity_bool:
    return 1
  else:
    return 0
  
