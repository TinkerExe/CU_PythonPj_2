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
    if response.status_code == 200:

        data = json.loads(response.text)
        return data['Key']
    
def get_for_name(name):
    url = 'http://dataservice.accuweather.com/locations/v1/cities/search'
    params = {
        'q': name,
        'apikey': APIKEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:

        data = json.loads(response.text)
        return data[0]['Key']