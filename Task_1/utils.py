from Task_1.const import APIKEY
import requests
import json


def weather_citykey(citykey): # функция погоды по городу
  url = f'http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{citykey}'
  params = {
    'apikey': APIKEY,
    'details': 'true'
  }
  response = requests.get(url, params=params)
  if response.status_code == 200:
      data = json.loads(response.text)
      return {
          "Temperature": (float(data[0]['Temperature']['Value']) - 32) * 5 / 9,
          "Humidity": float(data[0]['RelativeHumidity']),
          "wind_speed": float(data[0]['Wind']['Speed']['Value']) * 1.60934,
          "rain_probability": float(data[0]['PrecipitationProbability'])
          }
  else:
      print(json.loads(response.text)['Message'])
      return 0
  
def geoposition_Search(q): # функция нахождения города по координатам
  url = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search'
  params = {
    'q': q,
    'apikey': APIKEY
  }
  response = requests.get(url, params=params)
  if response.status_code == 200:

      data = json.loads(response.text)
      return data['Key']
  else:
      print(json.loads(response.text)['Message'])
      return 0
