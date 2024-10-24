from const import APIKEY
import json
import requests

def get_for_coordinates(lat, lon):
    url = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search'
    params = {
        'q': f"{lat}, {lon}",
        'apikey': APIKEY
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    if response.status_code == 200:
        return data['Key']
    else:
        return "err"
def get_for_name(name):
    url = 'http://dataservice.accuweather.com/locations/v1/cities/search'
    params = {
        'q': name,
        'apikey': APIKEY
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    if response.status_code == 200:
        return data[0]['Key']
    else:
        return "err"