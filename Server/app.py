from flask import Flask, render_template, request, flash
from get_city import get_for_coordinates, get_for_name
from weather import get_and_check
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    start_city = ''
    end_city = ''
    start_lat = ''
    start_lon = ''
    end_lat = ''
    end_lon = ''
    error_message = None
    weather_data = {}

    if request.method == 'POST':
        input_type = request.form['input_type']
        
        try:
            if input_type == 'city':
                start_city = request.form['start_city']
                end_city = request.form['end_city']
                if not start_city or not end_city:
                    return render_template('index.html', input_type=input_type, error="Все поля должны быть заполнены!")
                city_key_start = get_for_name(start_city)
                city_key_end = get_for_name(end_city)
            elif input_type == 'coordinates':
                start_lat = request.form['start_lat']
                start_lon = request.form['start_lon']
                end_lat = request.form['end_lat']
                end_lon = request.form['end_lon']
                if not start_lat or not start_lon or not end_lat or not end_lon:
                    return render_template('index.html', input_type=input_type, error="Все поля должны быть заполнены!")
                city_key_start = get_for_coordinates(start_lat, start_lon)
                city_key_end = get_for_coordinates(end_lat, end_lon)

            if "err" in city_key_start or "err" in city_key_end:
                error_message = "Кажется, API не доступен."
                return render_template('index.html', input_type=input_type, error=error_message)

            weather_data = get_and_check(city_key_start, city_key_end)

            if "error" in weather_data:
                error_message = weather_data['error']
                return render_template('index.html', input_type=input_type, error=error_message)

            return render_template('index.html', input_type=input_type,
                                   weather_start=weather_data['weather_start'],
                                   weather_end=weather_data['weather_end'],
                                   res=weather_data['res'],
                                   start_city=start_city, end_city=end_city,
                                   start_lat=start_lat,
                                   start_lon=start_lon,
                                   end_lat=end_lat,
                                   end_lon=end_lon)
        except Exception as e:
            error_message = str(e)

    return render_template('index.html', input_type='city', 
                           start_city=start_city, end_city=end_city,
                           start_lat=start_lat, start_lon=start_lon,
                           end_lat=end_lat, end_lon=end_lon,
                           error=error_message)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(port=port, threaded=True)
