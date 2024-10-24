from flask import Flask, render_template, request
from get_city import get_for_coordinates, get_for_name
from  weather import get_and_check
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_type = request.form['input_type']
        
        start_city = None
        end_city = None
        start_lat = None
        start_lon = None
        end_lat = None
        end_lon = None

        if input_type == 'city':
            start_city = request.form['start_city']
            end_city = request.form['end_city']
            
            city_key_start = get_for_name(start_city)
            city_key_end = get_for_name(end_city)

        elif input_type == 'coordinates':
            start_lat = request.form['start_lat']
            start_lon = request.form['start_lon']
            end_lat = request.form['end_lat']
            end_lon = request.form['end_lon']

            city_key_start = get_for_coordinates(start_lat, start_lon)
            city_key_end = get_for_coordinates(end_lat, end_lon)


        weather_data = get_and_check(city_key_start=city_key_start, city_key_end=city_key_end)

        return render_template('index.html', input_type=input_type,
                               weather_start=weather_data['weather_start'],
                               weather_end=weather_data['weather_end'],
                               res=weather_data['res'],
                               start_city=start_city, end_city=end_city,
                               start_lat=request.form.get('start_lat'),
                               start_lon=request.form.get('start_lon'),
                               end_lat=request.form.get('end_lat'),
                               end_lon=request.form.get('end_lon'))

    return render_template('index.html', weather_start=None, weather_end=None, input_type='city')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(port=port, threaded=True)
