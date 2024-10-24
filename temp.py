import requests
import json


url = f'http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{289243}'
params = {
'apikey': 'cTr4efNjQKOeARHIdXtEN9A8HTDgw1Am',
'details': 'true'
}
response = requests.get(url, params=params)
if response.status_code == 200:
    data = json.loads(response.text)
    weather =  {
        "Temperature": (float(data[0]['Temperature']['Value']) - 32) * 5 / 9,
        "Humidity": float(data[0]['RelativeHumidity']),
        "wind_speed": float(data[0]['Wind']['Speed']['Value']) * 1.60934,
        "rain_probability": float(data[0]['PrecipitationProbability'])
        }
    
    print(weather)

else:
    print(json.loads(response.text)['Message'])
    print(0)